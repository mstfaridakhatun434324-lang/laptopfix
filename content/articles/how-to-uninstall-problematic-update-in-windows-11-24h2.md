---
title: "How to Uninstall a Problematic Update in Windows 11 24H2 (Safe Rollback)"
slug: how-to-uninstall-problematic-update-in-windows-11-24h2
date: 2026-09-24
categories: ["windows-update"]
tags: ["uninstall update", "rollback", "24h2", "windows update", "problematic update"]
description: "A Windows 11 24H2 update broke something? Here's how to safely uninstall a bad cumulative or feature update — and stop it from reinstalling."
thumbnail: "/images/thumbs/how-to-uninstall-problematic-update-in-windows-11-24h2.webp"
faqs:
  - q: "How long do I have to uninstall a Windows 11 feature update?"
    a: "You have 10 days after installing a feature update like 24H2 to use the Go back option in Settings. After that window, Windows deletes the old system files and rollback is no longer possible through Settings — you would need recovery media or a clean install. Cumulative updates, by contrast, can usually be uninstalled at any time from update history."
  - q: "Will uninstalling an update delete my files?"
    a: "No. Uninstalling a Windows update — cumulative or feature — removes the update's system changes but leaves your personal files, installed apps, and settings intact. It is one of the safest recovery operations in Windows. Still, having a current backup before any system-level change is always wise."
  - q: "Can I stop the problematic update from reinstalling?"
    a: "Yes. Use the Show or Hide Updates troubleshooter to hide a specific cumulative update, pause updates for up to five weeks, or on Pro editions use group policy to defer updates. Hiding is the most targeted option — it blocks that one update while letting everything else through."
  - q: "What is the difference between uninstalling and rolling back?"
    a: "Uninstalling usually refers to removing a cumulative update (a monthly patch) from update history. Rolling back usually means reverting a feature update (a full build upgrade like 24H2) via the Go back option. Both restore the previous system state, but they use different mechanisms and have different time limits."
---

So a Windows 11 24H2-era update broke something on your laptop — a driver stopped working, an app crashes, performance tanked, or a device vanished. Before you reach for drastic measures, know this: Windows is designed to let you remove a bad update. Uninstalling a problematic cumulative update takes five minutes; rolling back a feature update takes under an hour. Both are safe, both preserve your files, and both are far better than living with the breakage or doing a clean install.

The key is using the right removal method for the update type, then preventing the bad update from reinstalling itself — because Windows Update will cheerfully reinstall the exact package you just removed if you do not tell it not to. This guide covers the full sequence: identify the culprit, remove it safely, block its return, and handle the cases where normal uninstallation is not available.

## Why this happens

- **Bad cumulative update.** A monthly patch with a regression affecting your specific hardware or software.
- **Driver bundled in update.** Windows Update replaced a working vendor driver with a broken one.
- **Feature update incompatibility.** 24H2 (or a build within it) conflicting with your laptop's drivers or firmware.
- **Partial install corruption.** The update installed incompletely, leaving a half-applied state.
- **Software conflict.** The update changed something an installed application depended on.
- **Firmware mismatch.** The update expects newer BIOS/firmware than the laptop has.
- **The wrong fix applied.** Sometimes the "problematic update" is fine and the real issue is elsewhere — removal is still a valid diagnostic step.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the culprit update

Do not uninstall updates at random. Pin down which one caused the problem.

1. Open **Settings > Windows Update > Update history** and note the install dates.
2. Match the date your problem started to the updates installed just before — the culprit is usually the most recent cumulative or driver update.
3. Check the **Driver updates** section of the history too — Windows-bundled driver updates are frequent silent breakers.
4. Note the exact KB number of the suspect. If the problem started after a feature update (build change), note that instead — it needs the rollback path in Fix 3, not the uninstall path in Fix 2.

### Fix 2: Uninstall a cumulative update from Settings

The standard removal path for monthly updates — quick and safe.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Find the suspect KB in the list, select it, and click **Uninstall**.
3. Confirm and let it complete — the laptop will restart.
4. Test the previously broken functionality. If it works again, you have confirmed the culprit — now block its return with Fix 4 before Windows Update reinstalls it.

### Fix 3: Roll back a feature update within 10 days

For problems caused by 24H2 itself (or a build upgrade), use the Go back option.

1. Go to **Settings > System > Recovery** and look for **Go back** under Recovery options.
2. If present (within 10 days of the feature update), click it and answer the feedback questions.
3. Choose what to do about updates during rollback, and let the process complete — it restores the previous build with your files and apps intact.
4. If **Go back** is missing, the 10-day window expired or the old files were cleaned up — your options are the recovery-environment uninstall in Fix 5 or living with the build while fixing the specific symptom. For the most alarming post-update symptom, see our [24H2 black screen recovery guide](/articles/how-do-i-fix-windows-11-24h2-black-screen-after-update/).

### Fix 4: Block the bad update from reinstalling

Removal without blocking is a temporary victory — Windows Update will reinstall the package.

1. Download Microsoft's **Show or Hide Updates** troubleshooter (`wushowhide.diagcab`) and run it.
2. Choose **Hide updates**, select the problematic KB, and finish — Windows Update will now skip it.
3. As a broader measure, you can **pause updates** for up to 5 weeks in **Settings > Windows Update**.
4. On Pro editions, use `gpedit.msc` > **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update** to defer quality updates — a cleaner long-term control than pausing. Revisit the hidden update in a month or two; Microsoft often fixes bad updates, and you want the fixed version.

### Fix 5: Uninstall from the recovery environment

When Windows will not boot properly after the bad update, remove it from outside.

1. Force the recovery environment: power on, force off at the logo, repeat three times.
2. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
3. Choose **Uninstall the latest quality update** (for cumulative updates) or **Uninstall the latest feature update** (for build upgrades).
4. Let it complete and choose **Continue** to boot normally. This path works even when the installed update prevents Windows from starting — it is the escape hatch for update-caused boot failures.

### Fix 6: Roll back a bad driver delivered via update

If the culprit was a driver update rather than an OS update, target the driver.

1. Open **Device Manager**, find the misbehaving device, open **Properties > Driver**, and click **Roll Back Driver** if available.
2. If rollback is unavailable, choose **Uninstall device** (checking **delete the driver software**), then restart — Windows will reinstall its inbox driver.
3. Then install the known-good driver from your laptop manufacturer's support site — Dell ([dell.com/support](https://www.dell.com/support)), HP, Lenovo, ASUS, or Acer.
4. To stop Windows Update from replacing it again, use the Show or Hide Updates tool from Fix 4 to hide that specific driver update.

### Fix 7: Command-line removal for stubborn updates

When the Settings UI refuses to uninstall a package, the command line usually succeeds.

1. Open Command Prompt as administrator.
2. List installed updates: `wmic qfe list brief /format:table` — find your KB number.
3. Remove it: `wusa /uninstall /kb:5000000` (replace with your KB number, without the "KB" prefix).
4. Restart and verify. If `wusa` reports the update cannot be uninstalled, the package was marked permanent — in that case the DISM command `dism /online /remove-package /packagename:...` with the full package name (from `dism /online /get-packages`) is the deeper alternative. For broader pipeline repairs after removal, our [update database error guide](/articles/how-to-fix-windows-update-database-error-on-windows-11/) covers the cleanup.

## Closing

Uninstalling a problematic update is one of the safest and most underused recovery tools in Windows: identify the culprit by date, remove it through Settings or the recovery environment, and block its return with the hide-updates tool. Most "update broke my laptop" situations resolve in under half an hour this way — no clean install required. Just remember the second half of the job: blocking the reinstall, so the fix sticks.
