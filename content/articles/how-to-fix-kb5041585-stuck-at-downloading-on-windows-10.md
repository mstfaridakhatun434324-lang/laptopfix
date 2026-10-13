---
title: "KB5041585 Stuck at Downloading on Windows 10? Here's the Recovery"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-windows-10
date: 2026-09-07
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "windows 10", "cumulative update", "windows update"]
description: "KB5041585 won't finish downloading on Windows 10? Unstick the transfer with service resets, a cache clear, and a manual install fallback."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-windows-10.webp"
faqs:
  - q: "Does KB5041585 apply to Windows 10?"
    a: "KB numbers are build-specific, and this guide addresses the KB5041585 package as offered to Windows 10 systems. The download mechanics — BITS transfers, the SoftwareDistribution cache, and the manual catalog fallback — work the same regardless of which build the KB targets."
  - q: "Why do downloads stall more often on older Windows 10 laptops?"
    a: "Older hardware means slower disks, weaker Wi-Fi chips, and longer histories of update cache cruft accumulated over years. A cumulative update download that a new machine finishes in fifteen minutes can expose every marginal component on a seven-year-old laptop — which is why the service resets and cache clears in this guide matter more on older machines."
  - q: "Can I skip this update and wait for the next cumulative?"
    a: "Cumulative updates are exactly that — cumulative. Skipping one just means the next month's package includes everything you missed, so you never truly 'miss' fixes by waiting. But each month's package also carries that month's security patches, so delaying leaves known vulnerabilities unpatched in the meantime. Install rather than skip; the download trouble is temporary, the security gap is not."
  - q: "What if the manual install also hangs?"
    a: "A hanging standalone installer points below the update pipeline: disk problems, corrupt system files, or conflicting software. Run CHKDSK, SFC, and DISM (covered below), retry in a clean boot state, and if it still hangs, the issue is system health, not the update."
---

When KB5041585 freezes at "Downloading" on a Windows 10 laptop, the instinct to just wait it out is strong — and occasionally right. Cumulative updates are large, and older Windows 10 hardware downloads them slowly. But there is a line between slow and stuck, and this guide is about recognizing it and acting decisively once crossed. Windows 10's update screens give you less feedback than Windows 11's, so the diagnostic approach here leans on services, logs, and the cache rather than the UI.

The [Windows 11 edition of this fix](/articles/how-to-fix-kb5041585-stuck-at-downloading-on-windows-11/) covers the same KB on the newer OS if you manage both.

Windows 10's update UI gives you less information than Windows 11's, which makes stuck downloads harder to read — but the underlying machinery is nearly identical. BITS still does the downloading, the SoftwareDistribution cache still holds partial files, and the same stalls occur for the same reasons. The practical difference is diagnostic: on Windows 10 you lean more on services.msc, Task Manager's network graph, and the event logs, and less on the Settings page. The fixes below are written with that in mind, favoring the tools that show you ground truth.

Windows 10 also caches Delivery Optimization data that can confuse the downloader after repeated failures. If you have retried several times, open Settings, Update & Security, Delivery Optimization, and check the activity monitor — a download stuck at the same byte count across retries confirms the partial file is poisoned and the cache clear is mandatory, not optional.

## Why this happens

- **BITS transfer stall:** The Background Intelligent Transfer Service wedges after a network interruption and never resumes the download.
- **Damaged partial download:** A corrupt partial file in the cache causes every resume attempt to fail at the same point.
- **Aging network hardware:** Older Wi-Fi adapters dropping sustained large transfers while handling light browsing fine.
- **Cache cruft from years of updates:** Long-lived Windows 10 installs accumulate stale cache state that confuses the downloader.
- **Metered or throttled connections:** Connection settings restricting background downloads, intentionally or accidentally.
- **Third-party firewall interference:** Security suites with aggressive network filtering breaking the update transfer's long-lived connection.
- **Insufficient free space:** The download staging area cannot fit the package, stalling the transfer silently.
- **Update service degradation:** Years of partial failures leaving wuauserv or BITS in a degraded state that a restart has not cleared — sometimes escalating to the [update service going missing entirely](/articles/how-to-fix-windows-update-service-missing-on-windows-10/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the stall correctly

1. Open Settings, Update & Security, Windows Update, and note the exact status text and percentage.
2. Leave it alone for 45 minutes on a stable connection. Check periodically — any movement means slow, not stuck.
3. Open Task Manager, Performance, Wi-Fi/Ethernet: zero network activity from the update process during a "downloading" state confirms a true stall.

### Fix 2: Pause, wait, and resume

1. Click "Pause updates for 7 days", wait 3 minutes, then resume.
2. This forces BITS to tear down and rebuild the transfer. If the download restarts from 0% and progresses, the stall is broken.
3. If it jumps back to the same frozen percentage, the partial file is corrupt — proceed to the cache clear.

### Fix 3: Restart the update services

1. Press Win + R, type `services.msc`, press Enter.
2. Restart Windows Update and Background Intelligent Transfer Service.
3. Confirm both are Running with sensible startup types (Manual for wuauserv is normal on Windows 10).
4. Check for updates again.

### Fix 4: Clear the SoftwareDistribution cache

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete everything inside C:\Windows\SoftwareDistribution.
4. Restart the services, reboot, and check for updates for a clean download.

### Fix 5: Reset BITS jobs and the network stack

1. Run `bitsadmin /reset /allusers` in an elevated Command Prompt.
2. Run `netsh winsock reset` and restart the laptop.
3. Temporarily disable third-party firewall network filtering and retry.

### Fix 6: Free space, clean the drive, check its health

1. Run Disk Cleanup as administrator; clear update cleanup files and temp files until 20+ GB is free.
2. Run `chkdsk C: /f` and schedule for restart if needed.
3. On older laptops, consider the drive's age — a failing drive corrupts partial downloads repeatedly, and no cache clear fixes hardware.

### Fix 7: Manual install and system repair

1. Download KB5041585 for Windows 10 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. If the standalone installer also struggles, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` first, then retry.
3. As a last resort before the manual install, perform a clean boot (msconfig, disable all non-Microsoft services) to eliminate software conflicts, then run the installer.
4. Verify in Update history. Official recovery documentation is at the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Install from a clean boot

Eliminate every background variable in one move.

1. Press Win + R, type `msconfig`, and press Enter.
2. On the Services tab, tick "Hide all Microsoft services" and click Disable all. On the Startup tab, open Task Manager and disable all startup items.
3. Restart into the clean boot state.
4. Retry the KB5041585 download \u2014 or run the manual installer from the Update Catalog \u2014 with nothing competing.
5. If it succeeds, re-enable services in groups afterward to identify what was interfering, then restore normal startup with `msconfig`.

## Closing

On Windows 10, a stuck KB5041585 download is usually the accumulated friction of an older system: tired cache, tired network stack, tired drive, and an update UI that tells you less than you need. The fixes are correspondingly mechanical \u2014 restart the services, clear the cache, free the space, strip the background to a clean boot \u2014 and if the pipeline will not cooperate, walk around it with a manual install. The update is worth the effort; the stall is not worth your evening.
