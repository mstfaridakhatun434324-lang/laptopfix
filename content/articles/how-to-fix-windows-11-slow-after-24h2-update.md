---
title: "How to Fix Windows 11 Running Slow After the 24H2 Update"
slug: "how-to-fix-windows-11-slow-after-24h2-update"
date: "2026-09-08"
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "windows update", "performance"]
description: "Windows 11 24H2 left your laptop sluggish? Post-update cleanup, driver refreshes, and these fixes restore full speed."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-24h2-update.webp"
faqs:
  - q: "Why is Windows 11 slow right after the 24H2 update?"
    a: "The first 24 to 48 hours after a feature update are the heaviest: Windows re-indexes search, rebuilds the font and icon caches, re-optimizes the .NET native image cache, and finishes background update tasks. It is normal for the machine to feel sluggish during this window. If slowness persists beyond three days of regular use, something genuinely needs fixing rather than patience."
  - q: "Should I roll back the 24H2 update?"
    a: "Only as a last resort. Windows keeps the previous installation for 10 days precisely for this, under Settings, System, Recovery, Go back. But most post-update slowness comes from stale drivers or leftover temporary files, both fixable without the disruption of a rollback. Try the cleanup and driver steps first; roll back only if performance is clearly worse after a full week."
  - q: "Can I pause 24H2 if I have not installed it yet?"
    a: "Yes. Under Settings, Windows Update, you can pause updates for up to five weeks, which delays the feature update while still allowing security patches if you unpause selectively. A cleaner approach is to update your drivers and free disk space before installing 24H2, since most post-update problems trace back to outdated drivers meeting a new OS build."
  - q: "How much free space does 24H2 need?"
    a: "Microsoft recommends at least 20 to 30 GB of free space on the system drive for a feature update to install and settle comfortably. The update itself stages several gigabytes of temporary files, and Windows keeps the old installation for rollback. After the update, Disk Cleanup can reclaim 10 to 20 GB by removing the previous Windows installation."
---

Feature updates are the biggest single change your Windows installation will ever go through, and 24H2 is no exception. It replaces thousands of system files, migrates drivers, rebuilds caches, and re-indexes your files. It is completely normal for a laptop to feel sluggish for a day or two afterward while all that background settling finishes. The problem is when the sluggishness never goes away.

Persistent post-24H2 slowness has a short list of usual causes. Old drivers that worked fine on 23H2 can misbehave under the new build. Gigabytes of leftover setup files eat disk space and slow everything that touches the drive. Power and performance settings sometimes reset to conservative defaults. And in a minority of cases, the update itself carries a regression that a later cumulative patch fixes.

This guide starts with the quick wins, cleaning up update leftovers and checking settings, then moves to driver refreshes and the update-troubleshooting steps that resolve the stubborn cases. Give each fix a day of normal use before judging it, since background settling is real.

## Why this happens

- **Background settling after the upgrade:** Re-indexing, cache rebuilds, and .NET optimization run for 24 to 48 hours after a feature update and consume CPU and disk.
- **Stale drivers carried over:** Drivers written for 23H2 can behave badly under 24H2, especially storage, chipset, and graphics drivers.
- **Gigabytes of leftover setup files:** The Windows.old folder and staged update files can consume 15 to 25 GB, starving the system drive of breathing room.
- **Power mode reset to Balanced:** Feature updates occasionally reset the Power mode dropdown, silently capping performance.
- **A buggy cumulative update on top of 24H2:** Sometimes the base upgrade is fine but a follow-up cumulative patch introduces the regression.
- **Antivirus re-scanning everything:** After major system file changes, security software often performs a full re-scan of the drive.
- **Corrupted update components:** Interrupted or partial update staging leaves the servicing stack in a state that keeps retrying work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it 48 hours, then clean up update leftovers

First rule out normal settling. If two days of regular plugged-in use have passed and it is still slow, reclaim the gigabytes 24H2 left behind.

1. Confirm at least 48 hours have passed since the update finished, with the laptop plugged in and used normally.
2. Press Win+R, type cleanmgr, and press Enter.
3. Select the C drive, then click Clean up system files.
4. Check Previous Windows installations, Windows Update Cleanup, and Temporary files.
5. Click OK and let it finish; this alone can free 10 to 20 GB.

### Fix 2: Verify your power mode survived the update

Updates sometimes reset Power mode to Balanced. This 30-second check rules out the simplest explanation.

1. Open Settings with Win+I, then System, then Power and battery.
2. Check the Power mode dropdown.
3. If it is not on Best performance, switch it back.
4. Our full guide to [changing the power plan to best performance](/articles/how-to-change-power-plan-to-best-performance/) covers the advanced options.

### Fix 3: Refresh chipset, storage, and graphics drivers

This is the highest-value fix for genuine post-update slowness. Prioritize drivers from your laptop manufacturer's support page over generic Windows Update versions.

1. Find your exact laptop model via Win+R, msinfo32, Enter.
2. Download the latest Windows 11 24H2 chipset driver from the manufacturer and install it.
3. Install the latest storage controller and graphics drivers the same way.
4. Restart after each major driver install.
5. Use Task Manager to compare CPU and disk behavior before and after.

### Fix 4: Install the latest cumulative update

Microsoft ships monthly cumulative patches, and post-24H2 performance regressions are frequently fixed within one or two cycles. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update seems stuck.

1. Open Settings, then Windows Update.
2. Click Check for updates and install everything offered.
3. Restart when prompted, even if it says you can wait.
4. If Windows Update reports errors, note the error code for the next fix.
5. Re-test performance after the cumulative patch and a restart.

### Fix 5: Repair the update components

If updates fail or TiWorker.exe runs endlessly, the servicing stack itself needs repair. The built-in troubleshooter plus DISM usually resolves it.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Open Terminal as administrator.
4. Run DISM /Online /Cleanup-Image /RestoreHealth and wait for it to complete.
5. Follow with sfc /scannow, then restart.

### Fix 6: Roll back within the 10-day window

If a full week of fixes leaves the laptop clearly slower than before 24H2, the rollback option exists for exactly this situation.

1. Open Settings, System, Recovery.
2. Under Recovery options, click Go back next to the previous version.
3. Answer Microsoft's prompts about why you are rolling back.
4. Let the process complete; your files are preserved but reinstall recent apps afterward.
5. Pause feature updates for a few weeks before trying 24H2 again.

### Fix 7: Check for safeguard holds and known issues

Microsoft sometimes blocks 24H2 on specific hardware combinations through safeguard holds, and a partially held update can leave the system in a slow half-migrated state. Checking the known-issues list tells you whether your slowness is a documented bug with a documented workaround.

1. Search the web for Windows 11 24H2 known issues on Microsoft's release health pages.
2. Look for your hardware or driver in the list of safeguard holds.
3. If a hold mentions a driver, update that exact driver from the manufacturer.
4. Some holds lift automatically after a driver update and a reboot.
5. If your issue is listed as under investigation, pause feature updates until Microsoft ships the fix.

### Fix 8: Check for safeguard holds and known issues

Microsoft sometimes blocks 24H2 on specific hardware combinations through safeguard holds, and a partially held update can leave the system in a slow half-migrated state. Checking the known-issues list tells you whether your slowness is a documented bug with a documented workaround.

1. Search the web for Windows 11 24H2 known issues on Microsoft's release health pages.
2. Look for your hardware or driver in the list of safeguard holds.
3. If a hold mentions a driver, update that exact driver from the manufacturer.
4. Some holds lift automatically after a driver update and a reboot.
5. If your issue is listed as under investigation, pause feature updates until Microsoft ships the fix.

## Closing

Most 24H2 slowness is temporary settling plus stale drivers, and the cleanup-and-refresh sequence above resolves the large majority of cases. Be patient for the first 48 hours, reclaim your disk space, refresh drivers from the manufacturer, and keep cumulative updates current. Only consider rollback when a full week of genuine fixes has failed. And before installing the next feature update, free up disk space and update drivers first; an ounce of preparation beats every fix on this page. If startup is still heavy after the update settles, [disabling unnecessary startup apps](/articles/how-to-disable-startup-apps-on-windows-11/) is the next highest-impact step. If startup is still heavy after the update settles, [disabling unnecessary startup apps](/articles/how-to-disable-startup-apps-on-windows-11/) is the next highest-impact step.
