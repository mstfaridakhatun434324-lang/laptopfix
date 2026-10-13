---
title: "Fix Windows Update Error 0x80240034 on Windows 11: Download Failed"
slug: how-to-fix-windows-update-error-0x80240034-on-windows-11
date: 2026-09-07
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x80240034", "download failed", "bits"]
description: "Error 0x80240034 means the update download failed on Windows 11. Fix the download pipeline — network, BITS, cache — with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80240034-on-windows-11.webp"
faqs:
  - q: "What does error 0x80240034 mean?"
    a: "It is WU_E_DOWNLOAD_FAILED — Windows Update could not download the update files. The causes range from network interruptions and proxy issues to corrupted download queues and a misbehaving BITS service. The update itself is fine; only the delivery failed, which is why the fixes focus on the download pipeline."
  - q: "My internet works fine. Why does the download still fail?"
    a: "Because the failure is usually in the download machinery, not your connection. BITS (the background download service), a corrupted download queue, proxy settings, or antivirus intercepting the transfer can all fail the download while your browser works perfectly — the two use completely different network paths."
  - q: "Does 0x80240034 mean the update file on Microsoft's servers is broken?"
    a: "Almost never. Microsoft's update files are hash-verified at multiple stages, from the content delivery network to your disk. When this error appears, the problem is between their servers and your disk — the network path, the download service, or the local queue — not the file itself, which is intact."
  - q: "How is this different from an update stuck at 0%?"
    a: "A stuck download usually means the queue is frozen but no error is raised. Error 0x80240034 means the download actively failed and reported it. The fixes overlap heavily — both involve BITS, the queue, and the network — but this error tells you the failure already happened rather than asking you to wait."
---

Error 0x80240034 is Windows Update's download failure code: WU_E_DOWNLOAD_FAILED. The update was found, the install was never attempted, and the files simply never made it to your laptop intact. On Windows 11 this error is refreshingly specific — it tells you the delivery failed, not the update — so the entire fix effort focuses on the download pipeline: the network path, the BITS download service, the queue, and anything intercepting the transfer.

The key distinction from other update errors: your system files, component store, and registry are probably fine. Do not start with DISM here; start with the network and the download services. Work the steps in order, retrying the download after each.

## Why this happens

- **Unstable network connection:** Drops during the multi-hundred-megabyte transfer corrupt the download and trigger the failure.
- **Hung or misconfigured BITS:** The Background Intelligent Transfer Service manages the download; if it is broken, downloads fail.
- **Corrupted download queue:** Stale or partial files in the SoftwareDistribution download folder poison new attempts.
- **Proxy or VPN interference:** Misconfigured proxies and VPN tunnels break the specific endpoints and protocols BITS uses.
- **Antivirus intercepting downloads:** Real-time scanning can quarantine or block update payloads mid-transfer.
- **Metered connection limits:** Windows pauses or throttles downloads on metered connections, which can surface as failures.
- **DNS failures:** Inability to resolve Microsoft's content delivery endpoints fails the download at the start.
- **Disk space exhaustion:** Downloads that cannot be written fail when the drive fills mid-transfer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Stabilize the connection and remove intermediaries

Rule out the network path before touching Windows.

1. Disconnect any VPN completely and, if possible, test on a different network (phone hotspot) to rule out ISP or router issues.
2. If you use a proxy (**Settings > Network & internet > Proxy**), temporarily disable it — BITS is sensitive to proxy misconfiguration.
3. Ensure the connection is not marked metered: **Settings > Network & internet > Wi-Fi**, select your network, and turn **Metered connection** off.
4. Retry the update and watch whether the download progresses further than before.

### Fix 2: Restart BITS and the Windows Update service

A hung download service is the most common local cause.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Right-click **Background Intelligent Transfer Service** and choose **Restart** (or **Start** if stopped).
3. Do the same for **Windows Update**.
4. Return to **Settings > Windows Update** and click **Retry**.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter repairs BITS registration and clears failed download jobs.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Apply all fixes, restart, and retry the download.

### Fix 4: Clear the corrupted download queue

Poisoned partial downloads cause every retry to fail identically. Empty the queue.

1. Open **Terminal (Admin)**.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete all files inside `C:\Windows\SoftwareDistribution\Download` (keep the folder).
4. Run `net start wuauserv` and `net start bits`.
5. Check for updates — the download starts fresh. This is the same queue-clearing step that unfreezes [stuck update downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/).

### Fix 5: Reset DNS and the network stack

If the download fails immediately every time, name resolution or the stack may be at fault.

1. In **Terminal (Admin)**, run `ipconfig /flushdns`.
2. Then run `netsh winsock reset` and `netsh int ip reset`.
3. Restart the laptop.
4. Consider switching to a public DNS (1.1.1.1 or 8.8.8.8) in the adapter's IPv4 properties if your ISP's DNS is flaky.

### Fix 6: Temporarily disable antivirus download scanning

Rule out security software intercepting the payload.

1. Temporarily disable real-time protection in your antivirus.
2. Immediately retry the update download.
3. Re-enable protection once the download completes (before or after install — the download is the risky phase for this error).
4. If this was the cause, add exclusions for the SoftwareDistribution folder.

### Fix 7: Download the update manually from the Update Catalog

Bypass BITS entirely: find the KB number in update history, download the `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) using your browser, and run it. Browser downloads use a completely different pipeline, so a BITS-level failure does not affect them. If the manual install succeeds, the problem was definitively in the download services — consider the full component reset from the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) guidance to restore them.

BITS deserves a closer look since it is the heart of this error. The Background Intelligent Transfer Service is designed to download in the background using idle bandwidth — throttling itself when you are actively using the connection and resuming after interruptions. That design is why update downloads normally survive sleep, reboots, and network hiccups. When BITS itself is broken — hung, misconfigured, or starved by a corrupted queue — the graceful behavior disappears and downloads fail outright with 0x80240034. Restarting the service clears transient hangs; clearing the queue clears poisoned state; and if both fail, the manual catalog download sidesteps BITS completely. Also note the metered-connection trap: Windows 11 respects metered flags strictly, and a connection mistakenly marked as metered will throttle or pause downloads in ways that look like failures. Check the metered flag whenever downloads misbehave on a new network. For Windows 10's take on the same error, see our [Windows 10 0x80240034 guide](/articles/how-to-fix-windows-update-error-0x80240034-on-windows-10/). One stable, unmetered download session is all it takes to get current again.

## Closing

Error 0x80240034 is a delivery failure, so fix the delivery: stabilize the network, restart BITS, clear the download queue, and rule out VPN, proxy, DNS, and antivirus interference. The manual catalog download is your escape hatch when the automated pipeline will not cooperate. Once files are downloading cleanly again, keep the connection stable and unmetered during updates, and this error stays a one-time visitor.
