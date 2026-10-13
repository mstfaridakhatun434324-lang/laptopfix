---
title: "Fix Windows Update Error 0x80246007 on Windows 10: Download Issues"
slug: how-to-fix-windows-update-error-0x80246007-on-windows-10
date: 2026-09-28
categories: ["windows-update"]
tags: ["windows update", "0x80246007", "bits", "download failed", "windows 11"]
description: "Windows 10 error 0x80246007 signals a download that never completed. Repair the download pipeline with these fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-on-windows-10.webp"
faqs:
  - q: "What is BITS and why does Windows Update need it?"
    a: "BITS — the Background Intelligent Transfer Service — is Windows 10's download manager for updates. It downloads in the background using idle bandwidth, resumes interrupted transfers, and throttles itself so your work is unaffected. Error 0x80246007 usually means BITS is stopped, stuck, or blocked, so the update content never arrives. Verifying and restarting the service is the first-line fix."
  - q: "Why does the download reach 100% and then fail with 0x80246007?"
    a: "Because reaching 100% is not the same as passing verification: if the staged files fail checksum validation, the download manager discards them and reports the content as not downloaded. Corrupted partial files in SoftwareDistribution are the usual cause — renaming that folder forces a fresh, verifiable download."
  - q: "Can I use my phone hotspot to download a stuck update?"
    a: "Yes, and it is a genuinely useful diagnostic: if the update downloads fine over the hotspot but not over your usual network, the problem is in your network path (proxy, firewall, ISP filtering), not in Windows. Just watch your mobile data allowance — feature updates are several gigabytes."
  - q: "Does Delivery Optimization help or hurt downloads?"
    a: "It usually helps: downloading parts of an update from PCs on your local network reduces load on Microsoft's servers and can route around server-side stalls. Problems are rare and typically involve strict firewalls blocking peer connections. If you suspect it, toggle it off temporarily — but leave it on afterward for faster large updates."
---
On Windows 10, error 0x80246007 means the download manager never obtained the complete update content. Windows 10 leans heavily on BITS for update downloads, and BITS is sensitive to service state, proxy configuration, and network interruptions — any of which can leave a download permanently incomplete and every retry failing the same way.

Think of this as a logistics problem: the warehouse (Microsoft's servers) has your package, but the delivery truck (BITS) broke down. Fix the truck, clear the loading dock, and the package arrives. Your installed updates and files are untouched throughout.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80246007-on-windows-11/) is the Windows 11 edition, and the [companion guide for 0x80072ee2](/articles/how-to-fix-windows-update-error-0x80072ee2-on-windows-10/) covers connection timeouts during download. Check the delivery services first.

## Why this happens

- **The BITS service is stopped, disabled, or stuck:** BITS is the download engine for Windows Update. If its service is not running — or a previous job wedged it — no content downloads and every attempt ends in 0x80246007.
- **A previous download job is jammed in the queue:** An interrupted or corrupted BITS job can block the queue indefinitely; new downloads line up behind the dead job and never start.
- **The connection is metered:** Windows restricts update downloads on metered connections. Large updates may start, stall against the metered policy, and report as not-downloaded.
- **Proxy or firewall blocks the download protocol:** BITS uses HTTP range requests that some proxies and firewalls mishandle or block outright, killing downloads that browsing never notices.
- **The download cache is corrupted:** Partial files in SoftwareDistribution with mismatched checksums cause the download manager to abort rather than assemble a bad package.
- **VPN or captive portal interrupts long downloads:** Multi-gigabyte feature updates need stable, long-lived connections; VPN drops or hotel-portal timeouts sever them mid-transfer.
- **Insufficient staging space aborts the download:** If free space runs out while the package stages, the download manager cancels and reports the content as not downloaded rather than as a disk error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the BITS and Windows Update services

If either is stopped, starting it and retrying resolves a large fraction of 0x80246007 cases immediately.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Background Intelligent Transfer Service — confirm its status is Running.
3. Find Windows Update — confirm its status is Running.
4. If either is stopped, right-click > Start, then set Startup type to Automatic (BITS may show Manual (Trigger Start), which is fine).
5. Open Settings > Update & Security > Windows Update and retry the download.

### Fix 2: Clear the stuck download queue

This is the core fix for 0x80246007 — the error is literally about the download queue, so rebuilding the queue addresses it directly.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv` and `net stop bits`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `net start bits` and `net start wuauserv`.
5. Check for updates in Settings > Update & Security > Windows Update and watch the download start fresh.

### Fix 3: Un-meter the connection and tune Delivery Optimization

Delivery Optimization settings also matter: letting the PC download from peers on your local network can speed large downloads and reduce server-side stalls.

1. Go to Settings > Network & internet, select your network, and turn off Metered connection.
2. In Settings > Update & Security > Windows Update > Advanced options > Delivery Optimization, turn it on and allow downloads from PCs on your local network.
3. If you must stay metered, use the Download updates over metered connections toggle to permit this one explicitly.
4. Restart the download from Settings > Update & Security > Windows Update.
5. For metered-connection policy details, see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Remove proxy and firewall blocks on downloads

Corporate laptops should coordinate with IT — but on home networks, direct access is the correct configuration.

1. Open Command Prompt as administrator and run `netsh winhttp reset proxy`.
2. Temporarily pause any third-party firewall or web-filtering feature.
3. Run `ipconfig /flushdns` to clear stale resolver entries.
4. Retry the download in Settings > Update & Security > Windows Update with filtering paused.
5. If it succeeds, add BITS/Windows Update exclusions per your vendor's docs instead of leaving filtering off.

### Fix 5: Reset the network stack

Saved Wi-Fi networks and passwords survive this; only the low-level protocol state is rebuilt, followed by a restart.

1. Open Command Prompt as administrator.
2. Run `netsh winsock reset` and `netsh int ip reset`.
3. Run `ipconfig /flushdns` and `ipconfig /release` followed by `ipconfig /renew`.
4. Restart the laptop.
5. Retry the update download in Settings > Update & Security > Windows Update.

### Fix 6: Download the update manually from the Catalog

A successful manual install also proves the system is healthy and only the delivery pipeline was broken.

1. Note the KB number of the stuck update in Settings > Update & Security > Windows Update > Update history.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Download the package for your architecture (x64 for most laptops).
4. Double-click the .msu and follow the installer, then restart.
5. Run a normal update check to confirm the queue is clear.

### Fix 7: Retry the download on a different network

Windows 10's BITS downloads are sensitive to proxies, ISP filtering, and router quirks that normal browsing never reveals. A mobile hotspot provides a completely independent path — no shared proxy, no shared DNS, no shared filtering. One successful download over the hotspot proves Windows is healthy and isolates the fault to your usual network.

1. Connect the laptop to your phone's mobile hotspot (watch data usage — updates are large).
2. In Settings > Update & Security > Windows Update, click Check for updates and let the download run.
3. If it completes, the usual network is blocking BITS traffic.
4. On the home network, investigate: bypass the router, check for ISP filtering, or reset the router.
5. Install the downloaded update, then switch back to your normal connection.

## Closing

On Windows 10, downloads that never complete almost always trace to BITS state, a jammed queue, or a network middlebox breaking range requests. Work the delivery chain in order and resist reinstalling anything — nothing is broken except the truck carrying your package. Fix the truck, and Windows 10 updates download like they used to.
