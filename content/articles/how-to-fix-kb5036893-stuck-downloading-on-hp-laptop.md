---
title: "KB5036893 Stuck Downloading on an HP Laptop: Fixes"
slug: how-to-fix-kb5036893-stuck-downloading-on-hp-laptop
date: 2026-10-05
categories: ["windows-update"]
tags: ["kb5036893", "hp laptop", "stuck downloading", "windows update"]
description: "KB5036893 frozen mid-download on your HP laptop? Unstick it with this HP-aware fix sequence, from service restarts to manual installation."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-on-hp-laptop.webp"
faqs:
  - q: "Why does KB5036893 get stuck downloading on HP laptops?"
    a: "The stall is usually in the local download pipeline rather than anything HP-specific: a corrupted cache file that fails validation and restarts endlessly, a hung update service, or a network setting like a metered connection. HP's bundled software can add load during downloads, but the core fixes — cache clearing and service resets — are the same on every brand."
  - q: "How long should I wait before calling the download stuck?"
    a: "Wait at least an hour with no percentage movement before intervening. Large cumulative updates download gigabytes in the background and the progress bar updates in jumps, not smoothly. Confirm the stall with Task Manager: zero network activity from update processes for a full hour means it is genuinely stuck, not just slow."
  - q: "Will restarting my HP laptop damage anything during a stuck download?"
    a: "No. Restarting during the download phase only interrupts file copying — nothing has been installed yet, so there is nothing to corrupt. Windows Update resumes or restarts the download after the reboot. The dangerous phase is installation, when the screen says updates are being applied; never force a shutdown there."
  - q: "Should I use HP Support Assistant to fix a stuck Windows update?"
    a: "HP Support Assistant is good for HP driver and BIOS updates, but a stuck Windows cumulative update is Microsoft's pipeline — fix it with the Windows Update repairs in this guide. Use HP Support Assistant afterward to make sure HP drivers are current, since outdated HP drivers can cause the install phase to fail after the download finally completes."
---

A download progress bar for KB5036893 that has not moved in hours is testing your patience, but it is a well-understood failure. The bytes are not flowing because something local — the cache, the service, the network flags — is blocking them. On HP laptops the usual background noise of HP Support Assistant and other bundled utilities can make diagnosis slightly noisier, but the repair sequence is the same reliable one.

The rule for download stalls: escalate gently. Confirm the stall is real, restart the services, check the network settings, clear the cache, and only then reset components or install manually. Most stalls break in the first three steps.

This HP-focused guide follows that escalation and adds the HP-specific checks that matter at the install phase that follows.

HP laptops are common, well-supported machines, and there is nothing about their hardware that blocks Windows updates. When a download stalls here, the cause is the same set of pipeline issues that affect every brand — which means the fixes are proven, predictable, and quick when applied in order.

## Why this happens

- **Power-saving Wi-Fi naps:** HP's default wireless power settings can doze the adapter during long idle downloads, corrupting the transfer mid-stream.
- **Corrupted download cache:** A damaged partial file fails checksum validation, so the downloader discards and restarts it in a loop.
- **Hung update services:** Wuauserv or BITS deadlocks after a failed attempt, freezing the progress display.
- **Metered connection flag:** HP laptops on mobile hotspots often get marked metered, throttling update downloads to nothing.
- **HP software contention:** HP Support Assistant running its own downloads simultaneously can saturate a slow connection.
- **VPN or firewall blocking:** Security software inspecting update traffic stalls the transfer silently.
- **Disk space staging limits:** The download needs room to land; a nearly full drive stalls instead of erroring.
- **Delivery Optimization peer stall:** Waiting on unreachable peers freezes progress on some networks. The [general stuck-downloading repair](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/) covers the brand-neutral deep dive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall is real

1. Open **Task Manager → Performance** and watch the network graph for five minutes — steady traffic means it is working.
2. Note the exact percentage in **Settings → Windows Update**, wait 30 minutes, and compare.
3. Check C: free space — under 10 GB can stall large downloads.
4. If HP Support Assistant is downloading updates simultaneously, pause it to free bandwidth.
5. Zero network activity for a full hour confirms a genuine stall; proceed.

### Fix 2: Restart the update services

1. Press **Win + R**, type `services.msc`, and restart **Windows Update** and **Background Intelligent Transfer Service**.
2. Return to **Settings → Windows Update** and click **Retry**.
3. Give it 20 minutes of observation.
4. A hung service is the most common cause and this is the fastest fix.
5. If the percentage jumps then freezes again, the cache is likely poisoned — continue to Fix 4.

### Fix 3: Check network flags and interference

1. Go to **Settings → Network & internet → Wi-Fi**, select your network, and turn **off** Metered connection.
2. Disconnect any **VPN** and temporarily disable third-party firewall features.
3. In **Settings → Windows Update → Advanced options → Delivery Optimization**, turn off "Allow downloads from other PCs".
4. Restart the laptop to reset the network stack cleanly.
5. Retry the download. For the Windows 11-specific variant, the [24H2 stuck-downloading fix](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/) adds version-specific steps.

### Fix 4: Clear the download cache

1. In an admin Terminal: `net stop wuauserv`, `net stop bits`.
2. Delete everything inside `C:\Windows\SoftwareDistribution\Download`.
3. Restart the services: `net start wuauserv`, `net start bits`.
4. Click **Check for updates** — KB5036893 re-downloads from a clean cache.
5. This is safe; the folder holds only downloaded files, never installed updates.

### Fix 5: Run the Windows Update troubleshooter

1. Open **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run **Windows Update** and apply its fixes.
3. Restart if prompted.
4. Retry the download afterward.
5. The troubleshooter catches service misconfigurations that manual restarts miss.

### Fix 6: Reset the update components

1. In an admin Terminal, stop `wuauserv`, `bits`, `cryptsvc`, and `msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart all four services.
4. Restart the laptop and check for updates.
5. This full reset resolves stalls that survive a simple cache clear.

### Fix 7: Install KB5036893 manually and update HP drivers

1. Note the KB number and download the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Double-click the MSU to install directly, bypassing the stuck downloader, then restart.
3. Afterward, open **HP Support Assistant** and install any pending HP driver and BIOS updates — or get them from [HP support](https://support.hp.com/us-en).
4. Current HP drivers prevent the install-phase failures that often follow a hard-won download.
5. Confirm KB5036893 shows as installed in Update history and that future updates download normally, per the baseline on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 8: Tune the network for large updates

Make future gigabyte-scale downloads boring with a few one-time network tweaks.

1. Prefer **wired Ethernet** (via a USB adapter if needed) for Patch Tuesday downloads.
2. In **Delivery Optimization** settings, cap background bandwidth so updates do not fight your work.
3. Keep the metered-connection flag off on your home Wi-Fi permanently.
4. Update the **Wi-Fi driver** from HP support — old wireless drivers drop more chunks mid-transfer.
5. Restart the router occasionally; stale NAT sessions silently degrade long transfers.
6. With a clean pipe, large cumulative downloads finish without babysitting.

## Closing

A stuck KB5036893 download is a local plumbing problem: confirm the stall, restart the services, fix the network flags, clear the cache. On HP laptops, follow the download fix with an HP driver refresh so the install phase that follows goes smoothly. Ten minutes of methodical repair beats hours of watching a frozen bar.
