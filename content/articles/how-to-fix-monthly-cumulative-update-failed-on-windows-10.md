---
title: "Fix Monthly Cumulative Update Failed on Windows 10"
slug: how-to-fix-monthly-cumulative-update-failed-on-windows-10
date: 2026-09-21
categories: ["windows-update"]
tags: ["cumulative update", "windows 10", "update failed", "patch tuesday"]
description: "Windows 10 cumulative update keeps failing every month? Here are 7 fixes — cache reset, manual install, and DISM repair — that break the cycle."
thumbnail: "/images/thumbs/how-to-fix-monthly-cumulative-update-failed-on-windows-10.webp"
faqs:
  - q: "Why does my Windows 10 cumulative update fail every single month?"
    a: "Monthly recurrence points to an unresolved root cause rather than bad luck. The usual suspects are a corrupted update cache that never got reset, a damaged component store, or a driver that conflicts with every new cumulative release. Because each month's cumulative update builds on the same system state, the same blocker fails it again. Fix the underlying condition once and the cycle stops."
  - q: "Is it dangerous to skip Windows 10 cumulative updates?"
    a: "Yes, over time. Cumulative updates bundle the month's security fixes, and skipping them leaves known vulnerabilities unpatched — attackers specifically target machines missing recent patches. A month or two of delay while you fix the underlying problem is acceptable; a permanent backlog is not. The manual install method below lets you stay protected even while troubleshooting."
  - q: "Will these fixes work on Windows 10 22H2?"
    a: "Yes. Windows 10 22H2 is the final Windows 10 version and the only one still receiving these monthly cumulative updates, so these steps are written for it. The servicing model — one cumulative package per month, superseding the last — is the same across all supported Windows 10 builds, and the cache-reset, DISM, and manual-install techniques apply identically."
  - q: "How much disk space does a cumulative update need?"
    a: "Plan on at least 10 to 15 GB of free space on the system drive. The download itself is a few hundred megabytes to a few gigabytes, but the install phase stages files, keeps a rollback copy, and needs working room. Laptops with small SSDs fail cumulative updates from space pressure more than any other cause, so checking storage first is always worthwhile."
---

Every second Tuesday, Windows 10 downloads its monthly cumulative update — and on some laptops, every second Tuesday ends in failure. The update downloads, installs partway, then rolls back with a generic error. Next month the same thing happens, and the month after that. The backlog grows, the machine falls further behind on security patches, and the owner starts dreading Patch Tuesday.

The monthly pattern is actually a diagnostic clue. Cumulative updates are superseding packages: each month's update contains everything from the previous months plus the new fixes. If the same failure repeats monthly, the cause is almost never the update itself — it is something about your machine that every cumulative update trips over. Corrupted update cache, damaged component store, a conflicting driver, or chronic low disk space are the usual culprits. Fix the condition once, and the monthly cycle of failure ends.

## Why this happens

- **A corrupted update cache that was never reset.** Every month's update downloads into the same damaged cache and fails the same way.
- **Component store damage.** Corruption in WinSxS breaks the staging every cumulative update must perform.
- **Chronic low disk space.** Small SSDs that hover near full fail the install phase month after month.
- **A conflicting third-party driver.** Some drivers conflict with each new cumulative release until the vendor updates them.
- **Antivirus interference.** Real-time protection that blocks one month's installer will block the next month's too.
- **A stuck servicing stack.** A failed servicing stack update months ago silently blocks every cumulative update since.
- **Pending operations backlog.** Each failed month adds pending file operations that interfere with the next attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the pattern — error code, KB, and disk space

Monthly failures deserve five minutes of diagnosis before any repair. The pattern tells you which fix to prioritize.

1. Open **Settings > Update & Security > Windows Update > View update history** and note the failing update's KB number and error code.
2. Check whether the error code is the same every month. A consistent code (like 0x80070002) points to a specific repair — our [0x80070002 guide](/articles/how-to-fix-windows-update-error-0x80070002-on-dell-laptop/) covers that code, and our [DISM RestoreHealth guide](/articles/how-to-run-dism-restore-health-on-windows-11/) covers the component-store repairs behind most other codes.
3. Open **Settings > System > Storage** and verify at least 15 GB free on C:. If the drive is nearly full, skip to Fix 5 first — nothing else matters until space is freed.
4. Note how far behind you are: months of backlog may mean a missing servicing stack update, covered in Fix 6.

### Fix 2: Reset the Windows Update cache

The single most effective fix for recurring monthly failures. A clean cache breaks the corrupted-download cycle.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`. Then check for updates and let the cumulative update download fresh.

### Fix 3: Install the cumulative update manually

If Windows Update keeps failing the install, bypass it. The standalone package installs the exact same fixes.

1. Find the failing update's KB number in Update history.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search for the KB number, and download the x64 package.
3. Double-click the `.msu` file to install it directly, then restart when prompted.
4. Verify in **View update history** that it shows as successfully installed. This keeps you protected even if the automatic path still needs work.

### Fix 4: Repair the component store with DISM and SFC

Cumulative updates stage heavily through the component store. Damage there fails every month's package identically.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes).
2. Follow with `sfc /scannow` to 100%.
3. Restart and retry the cumulative update through Windows Update.
4. If DISM cannot complete, the store needs files from installation media — create Windows 10 installation media with Microsoft's media creation tool (linked from the [Windows support page](https://support.microsoft.com/en-us/windows)) and use the ISO as a DISM source.

### Fix 5: Free up disk space permanently

If space is the monthly killer, a one-time cleanup is not enough — set up the machine so it never runs this close to full again.

1. Run Disk Cleanup as administrator: search Disk Cleanup, right-click, **Run as administrator**, check **Windows Update Cleanup** and **Temporary files**, and clean them.
2. Enable Storage Sense at **Settings > System > Storage** so temp files and old update backups are removed automatically.
3. Move personal files (photos, videos, downloads) to external storage or the cloud.
4. Uninstall unused programs. Aim to keep at least 20 GB free on C: at all times — cumulative updates plus their rollback copies need the headroom.

### Fix 6: Check the servicing stack

A failed servicing stack update from months ago silently blocks every cumulative update after it. This is the classic "it worked fine until it suddenly didn't" scenario.

1. In Update history, look for any failed **servicing stack update** entries in past months.
2. If you find one, download that KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually, oldest first if there are several.
3. Restart after each SSU install, then retry the cumulative update.
4. Going forward, never hide or skip servicing stack updates — they are prerequisites for everything else.

### Fix 7: Pause interfering software and run the troubleshooter

The final sweep: remove install-time interference and let the automated tool check service health.

1. Temporarily disable third-party antivirus real-time protection and pause any manufacturer updater utilities (Dell SupportAssist, HP Support Assistant, Lenovo Vantage).
2. Run **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update** and apply all suggested fixes.
3. Retry the cumulative update with the interfering software still paused; re-enable everything afterward.
4. If failures persist after all seven fixes, an in-place upgrade with Windows 10 installation media (keeping files and apps) rebuilds the update machinery completely.

## Closing

A Windows 10 cumulative update that fails every month is not bad luck — it is an unfixed root cause meeting an identical package each month. Reset the cache, repair the component store, keep 20 GB free, and install manually when the automatic path balks. Once the cycle is broken, the monthly updates become the quiet background event they are supposed to be. And if you ever move that laptop to Windows 11, our guide to [24H2 update problems on Dell](/articles/how-to-fix-windows-11-24h2-update-problems-on-dell-laptop/) covers the feature-update side of the same discipline.
