---
title: "Windows Update Stuck Downloading? A Step-by-Step Unstick Guide"
slug: how-to-fix-windows-update-stuck-downloading-step-by-step
date: 2026-10-03
categories: ["windows-update"]
tags: ["windows update", "stuck downloading", "0% downloading", "bits", "troubleshooting"]
description: "Windows Update frozen at 0% or stuck downloading for hours? Diagnose whether it's the network, the cache, or the service — then unstick it step by step."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-step-by-step.webp"
faqs:
  - q: "How long should a Windows Update download normally take?"
    a: "It depends on the package size and your connection. A monthly cumulative update is typically 300 MB to 1 GB and should download in minutes on broadband. A feature update can be 4–6 GB and take an hour or more. If the percentage has not moved in over two hours on a working connection, it is stuck."
  - q: "Does a stuck download use up my data or slow my internet?"
    a: "A genuinely stuck download transfers almost nothing, so it is not consuming data. But a download that keeps restarting from zero because of an unstable connection can chew through data repeatedly. Setting the connection as metered pauses it until you are on unmetered Wi-Fi."
  - q: "Why is Windows Update stuck at 0% downloading?"
    a: "Zero-percent stalls are usually service-side, not network-side: the Background Intelligent Transfer Service (BITS) or Windows Update service is hung, the download queue is corrupted, or a proxy or VPN is blocking the connection. Restarting the services and clearing the queue fixes most 0% cases."
  - q: "Can I just turn off the laptop while an update is downloading?"
    a: "Yes, with minimal risk. A download-phase interruption is safe because nothing has been installed yet — Windows simply resumes or restarts the download next time. The real danger zone is during the installation and reboot phases, when interrupting can corrupt the update. Downloading is always the safe phase to interrupt."
---

A Windows Update download that sits at 0% — or creeps to 37% and freezes there for three hours — is one of the most common update complaints on laptops. The percentage bar is lying to you a little: it reflects the state of a download queue managed by background services, and when any link in that chain jams, the bar stops moving even though your internet works fine for everything else.

The right way to fix it is to figure out which link is jammed: your network path, the download services, or the queue itself. The steps below walk that chain in order, from the outside in. Check the download progress after each step. And remember the key reassurance: while the update is still in the downloading phase, nothing has been installed yet, so every fix here is low-risk.

## Why this happens

- **Hung BITS or Windows Update service:** The Background Intelligent Transfer Service manages the actual download. If it hangs, the queue freezes even though the network is fine.
- **Corrupted download queue:** Partial files and stale queue entries in the SoftwareDistribution folder block new download jobs from starting or progressing.
- **VPN or proxy interference:** Corporate VPNs, third-party VPN apps, and misconfigured proxies can block or throttle the specific Microsoft endpoints Windows Update uses.
- **Metered connection throttling:** On a connection marked as metered, Windows pauses or severely limits update downloads, which looks exactly like a stuck download.
- **DNS resolution failures:** If your DNS cannot resolve Microsoft's update servers, the download never starts — stuck at 0% with no useful error.
- **Third-party "update blocker" tools:** Utilities that promise to stop Windows updates often do it by breaking the services, and their damage persists after uninstallation.
- **Insufficient disk space:** The download needs room to land. With only a few hundred megabytes free, the download starts, cannot write, and stalls.
- **Corrupted network stack:** Damaged Winsock or TCP/IP configuration can break the specific type of connection BITS uses while browsers keep working normally.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the network path is actually clear

Before touching Windows, confirm the stall is not your connection, VPN, or metered setting.

1. Disconnect any VPN and, if you are on a corporate or school network, try a mobile hotspot to rule out network-level blocking.
2. Go to **Settings > Network & internet > Wi-Fi**, click your network, and check whether **Metered connection** is on — turn it off for the download.
3. Open a browser and confirm general internet works, then check for updates again and watch the percentage for five minutes.

### Fix 2: Restart the update services

A hung service is the single most common cause of a frozen download bar. Restarting BITS and the Windows Update service clears the jam without touching any files.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Background Intelligent Transfer Service**, right-click it, and choose **Restart**. If it is not running, choose **Start**.
3. Do the same for **Windows Update**.
4. Return to **Settings > Windows Update** and click **Retry** or **Check for updates**.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter detects stuck download jobs, resets the queue, and repairs service registrations automatically.

1. On Windows 11: **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.
2. On Windows 10: **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update > Run the troubleshooter**.
3. Apply all recommended fixes, restart, and check whether the download progresses.

### Fix 4: Clear the SoftwareDistribution download queue

When the queue itself is corrupted — stale partial files that BITS keeps choking on — the only cure is to empty it and start the download fresh.

1. Open **Terminal (Admin)**.
2. Stop the services: `net stop wuauserv` and `net stop bits`.
3. Delete everything inside `C:\Windows\SoftwareDistribution\Download` (open File Explorer, navigate there, select all, delete). Do not delete the folder itself.
4. Restart the services: `net start wuauserv` and `net start bits`.
5. Check for updates. The download restarts from 0% — this time it should actually move.

### Fix 5: Reset the network stack and DNS

If browsers work but BITS downloads do not, the network stack may be damaged in a way that only affects the update service. Resetting it is quick and safe.

1. Open **Terminal (Admin)**.
2. Run these commands one by one: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop.
4. Optionally switch DNS to a public resolver (1.1.1.1 or 8.8.8.8) in your adapter settings if your ISP's DNS is unreliable — guidance for this is on the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows).

### Fix 6: Check disk space and Delivery Optimization settings

A download that cannot be written stalls silently. Also, Delivery Optimization's throttling settings can make downloads crawl.

1. Ensure at least 10 GB free on C: via **Settings > System > Storage**.
2. Go to **Settings > Windows Update > Advanced options > Delivery Optimization**.
3. Under **Advanced options**, check that download bandwidth is not throttled to a trickle, and consider toggling **Allow downloads from other PCs** off if peer downloads seem to stall.
4. Retry the update.

### Fix 7: Install the update manually from the Microsoft Update Catalog

If the download pipeline refuses to cooperate, bypass it entirely. Note the KB number from update history, search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), download the `.msu` for your system type, and run it directly. This sidesteps BITS, the queue, and Delivery Optimization in one move. If even the manual installer stalls, the problem is deeper — run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`, since the same corruption behind [failed cumulative updates](/articles/how-to-fix-monthly-cumulative-update-failed-step-by-step/) can also freeze downloads.

If the download fails outright with an error code instead of merely stalling, our [0x80240034 download-failure guide](/articles/how-to-fix-windows-update-error-0x80240034-on-windows-11/) picks up where this one leaves off.

## Closing

A stuck update download is a plumbing problem with a clear diagnostic chain: network path, services, queue, network stack, disk space. Walk it in that order and you will find the blockage — most often a hung BITS service or a corrupted download queue that a five-minute reset clears. Once downloads flow again, let the update finish on a stable, unmetered connection with the charger plugged in, and the "stuck at 0%" days stay behind you.
