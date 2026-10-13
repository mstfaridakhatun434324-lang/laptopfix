---
title: "Fix Windows Update Error 0x80246007 on Windows 11 (Download Failed)"
slug: how-to-fix-windows-update-error-0x80246007-on-windows-11
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows update", "0x80246007", "bits", "download failed", "windows 11"]
description: "Windows 11 error 0x80246007 means the update never finished downloading. Fix BITS, the download queue, and network blocks with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-on-windows-11.webp"
faqs:
  - q: "What is BITS and why does Windows Update need it?"
    a: "BITS — the Background Intelligent Transfer Service — is Windows 11's background download manager for updates. It uses idle bandwidth, resumes interrupted transfers, and throttles itself so your work stays smooth. Error 0x80246007 usually means BITS is stopped, wedged, or blocked, so update content never arrives. Checking and restarting the service is the first-line fix."
  - q: "Why does the download reach 100% and then fail with 0x80246007?"
    a: "Because 100% is not the same as verified: if staged files fail checksum validation, the download manager discards them and reports the content as not downloaded. Damaged partial files in SoftwareDistribution are the usual cause — renaming that folder forces a fresh, verifiable download."
  - q: "Can I use my phone hotspot to download a stuck update?"
    a: "Yes, and it is a genuinely useful diagnostic: if the update downloads over the hotspot but not your usual network, the fault lies in your network path (proxy, firewall, ISP filtering), not in Windows. Just mind your mobile data allowance — feature updates run to several gigabytes."
  - q: "Does Delivery Optimization help or hurt downloads?"
    a: "It usually helps: pulling parts of an update from PCs on your local network eases Microsoft's servers and can route around server-side stalls. Trouble is rare and typically involves strict firewalls blocking peer connections. If you suspect it, switch it off temporarily — then leave it on afterward for faster large updates."
---
Error 0x80246007 — WU_E_DM_NOTDOWNLOADED — says exactly what it means: the update content never finished downloading, so there is nothing to install. On Windows 11 the download chain runs through the Background Intelligent Transfer Service (BITS), Delivery Optimization, and your network path; a break anywhere — a wedged BITS job, a metered connection, a firewall mangling range requests — aborts the download and surfaces this code.

The approach is to trace the download path end to end: confirm the services, empty the queue, lift network blocks, and if the pipeline still refuses to cooperate, fetch the package yourself. Nothing here endangers your installed system — we are only repairing delivery.

If another machine shows the same download failure, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80246007-on-windows-10/) covers Windows 10, and when downloads finish but the connection times out instead, the [companion guide for 0x80072ee2](/articles/how-to-fix-windows-update-error-0x80072ee2-on-windows-11/) is the one to read. Begin with the services.

## Why this happens

- **BITS is stopped, disabled, or wedged:** BITS is the download engine behind Windows Update. If the service is not running — or an old job jammed it — no content downloads and every attempt ends at 0x80246007.
- **A dead download job blocks the queue:** an interrupted or corrupted BITS job can plug the queue indefinitely; new downloads stack up behind the dead job and never begin.
- **The connection is metered:** Windows restrains update downloads on metered connections. Big updates may begin, stall against the metered policy, and get reported as not-downloaded.
- **A proxy or firewall breaks the download protocol:** BITS relies on HTTP range requests, which some proxies and firewalls mangle or block outright, while browsing sails through unaffected.
- **The download cache is corrupted:** partial files in SoftwareDistribution with mismatched checksums make the download manager abort rather than assemble a bad package.
- **A VPN or captive portal cuts long downloads:** multi-gigabyte feature updates need stable, long-lived connections; VPN drops or hotel-portal timeouts cut them mid-transfer.
- **Staging ran out of space:** if free space evaporates while the package stages, the download manager cancels and reports the content as not downloaded rather than a disk error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the BITS and Windows Update services are running

Everything downstream hinges on these two services: BITS performs the download, and the Windows Update service orchestrates it. Both should be set to start automatically (BITS often shows Manual-Triggered, which is normal) and both need to actually be running when you check.

1. Press Win + R, enter `services.msc`, and hit Enter.
2. Locate Background Intelligent Transfer Service — verify its status reads Running.
3. Locate Windows Update — verify its status reads Running.
4. If either shows as stopped, right-click it, choose Start, and set Startup type to Automatic — BITS may display Manual (Trigger Start), which is normal.
5. Open Settings > Windows Update and attempt the download again.

### Fix 2: Empty the jammed download queue

A stuck BITS job jams everything behind it, and the queue never drains itself. Stopping the services and renaming SoftwareDistribution wipes the dead jobs and their partial files, so the next attempt begins from an empty, healthy queue.

1. Open an elevated Command Prompt.
2. Execute `net stop wuauserv` and `net stop bits`.
3. Execute `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Execute `net start bits` and `net start wuauserv`.
5. Check for updates in Settings > Windows Update and watch the download begin fresh.

### Fix 3: Switch off metering and tune Delivery Optimization

Metered connections order Windows to hold downloads back, and the resulting stalls surface as not-downloaded errors. On a truly capped connection you may need to permit the download explicitly; on a wrongly flagged home network, simply switch metering off.

1. Open Settings > Network & internet, select your network, and switch Metered connection off.
2. In Settings > Windows Update > Advanced options > Delivery Optimization, enable it and allow downloads from PCs on your local network.
3. If metering must stay on, use the Download updates over metered connections toggle to allow this one explicitly.
4. Kick off the download again from Settings > Windows Update.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the metered-connection policy in detail.

### Fix 4: Remove proxy and firewall blocks on downloads

BITS downloads fail in ways browsing never exposes, because proxies and firewalls can disrupt HTTP range requests while passing normal page loads. Resetting the WinHTTP proxy and testing with third-party filtering paused rules out this entire class of failure.

1. Open an administrator Command Prompt and run `netsh winhttp reset proxy`.
2. Briefly pause any third-party firewall or web-filtering feature.
3. Run `ipconfig /flushdns` to wipe stale resolver entries.
4. Try the download again in Settings > Windows Update while filtering is paused.
5. On success, add BITS/Windows Update exclusions per your vendor's docs rather than leaving filtering off.

### Fix 5: Rebuild the network stack

When downloads stall on every network and queue, the local stack itself may be broken: corrupted Winsock catalogs or TCP/IP state destroy the long-lived connections large updates need. Resetting rebuilds the transport layer BITS depends on.

1. Start a Command Prompt with administrator rights.
2. Run `netsh winsock reset` and `netsh int ip reset`.
3. Flush DNS with `ipconfig /flushdns`, then release and renew with `ipconfig /release` followed by `ipconfig /renew`.
4. Reboot the machine.
5. Attempt the update download again from Settings > Windows Update.

### Fix 6: Fetch the update manually from the Catalog

The definitive bypass: if the BITS pipeline will not deliver, grab the package with your browser from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it directly. Browser downloads never touch BITS, so every queue, proxy, and service problem is sidestepped in one move.

1. Write down the KB number of the stuck update from Settings > Windows Update > Update history.
2. Look it up on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Download the package built for your architecture (x64 on most laptops).
4. Double-click the .msu, follow the installer, and restart.
5. Run a normal update check to confirm the queue cleared.

### Fix 7: Download over a different network

When every local fix fails, the blockage may sit upstream — your ISP, router, or corporate filter disrupting the specific patterns BITS uses. A phone hotspot or another Wi-Fi network both diagnoses and sidesteps the problem: if the update downloads cleanly there, your network path was the culprit all along.

1. Connect to your phone's mobile hotspot (updates are large — watch data usage).
2. In Settings > Windows Update, press Check for updates and let the download run.
3. If it completes there, your usual network is blocking BITS traffic.
4. Back on the home network, investigate: bypass the router, look for ISP filtering, or reset the router.
5. Install the downloaded update, then return to your normal connection.

## Closing

Error 0x80246007 is a delivery breakdown, not a system breakdown: BITS, the queue, or the network path failed somewhere between Microsoft and your laptop. Confirm the services, rebuild the queue, clear the blocks, and keep the manual Catalog download as your fallback. On Windows 11, once the download pipeline is healthy, updates arrive as they should — completely, verifiably, and without error codes.
