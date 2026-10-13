---
title: "How to Use System Restore on a Windows 11 Laptop"
slug: how-to-use-system-restore-on-windows-11-on-laptop
date: 2026-09-02
categories: ["windows-errors"]
tags: ["system restore", "windows 11", "recovery"]
description: "Need to undo a bad driver or update on Windows 11? Here's how to use System Restore properly — including when Windows won't boot."
thumbnail: "/images/thumbs/how-to-use-system-restore-on-windows-11-on-laptop.webp"
faqs:
  - q: "Will System Restore delete my personal files?"
    a: "No. System Restore only affects system files, installed programs, drivers, Windows updates, and system settings. Your documents, photos, music, and downloads are left alone. Programs installed after the restore point was created will need to be reinstalled, though."
  - q: "How far back can System Restore go?"
    a: "Only as far as your oldest restore point. Windows creates them automatically before updates and driver installations, and old points are deleted as space fills up — typically you get days to a few weeks of history depending on your Max Usage setting and drive size."
  - q: "Why is System Restore disabled on my new laptop?"
    a: "Some manufacturers and Windows configurations ship with System Protection off to save SSD space. It's worth turning on manually — the few gigabytes it uses are cheap insurance compared to the hours a broken update costs without it."
  - q: "Can System Restore remove a virus?"
    a: "Not reliably. System Restore isn't designed for malware removal and some malware infects restore points. If malware is the problem, run a full Windows Security scan (or offline scan) instead — restore points are for undoing system changes, not infections."
---

System Restore is Windows' built-in time machine: it rolls system files, drivers, and settings back to an earlier point while leaving your personal files alone. It's the fastest way to undo a bad driver install, a broken update, or a settings change that went sideways.

There's a catch on modern laptops: System Restore is often disabled by default, so the first thing to check is whether you actually have restore points. This guide covers enabling it, creating points, restoring from inside Windows, and restoring when Windows won't boot. Pair it with our [quick reference](/articles/best-way-to-use-system-restore-on-windows-11/) if you need the short version.

## Why this happens

- System Restore being disabled by default on many new laptops, so no restore points exist when you need one.

- Restore points being deleted by low disk space or aggressive disk cleanup tools.

- The restore failing because of antivirus interference or corrupted restore point data.

- Not knowing restore points are created automatically before updates and driver installs.

- Trying to use System Restore for problems it can't fix, like hardware failure or malware.

- BitLocker or disk encryption complications when restoring from the recovery environment.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Turn on System Protection

Without System Protection enabled, Windows creates no restore points. This is step zero — do it now, before you need it.

1. Search for **Create a restore point** in the Start menu and open it.

2. Select your system drive (**C:**) and click **Configure**.

3. Choose **Turn on system protection**.

4. Set **Max Usage** to around **5-10%** of the drive so old points aren't deleted too aggressively, then click **OK**.

### Fix 2: Create a manual restore point

Automatic points are created before updates, but making one manually before risky changes (driver installs, registry edits) is a habit worth building.

1. Open **Create a restore point** from the Start menu.

2. Click **Create**, give it a descriptive name like 'Before NVIDIA driver update'.

3. Wait for the confirmation message.

4. Do this before any driver update or major settings change — it takes 30 seconds and has saved countless weekends.

### Fix 3: Restore from inside Windows

If Windows boots, this is the easy path: a wizard walks you through picking a point and rolling back.

1. Open **Create a restore point** and click the **System Restore** button.

2. Click **Next**, then tick **Show more restore points** to see them all.

3. Pick a point dated before the problem started and click **Next**.

4. Confirm and let the laptop restart — the restore takes 10-30 minutes. Don't interrupt it.

### Fix 4: Restore when Windows won't boot

System Restore also runs from the recovery environment, which is how you undo the update or driver that broke booting in the first place.

1. Force-power-off twice during the Windows logo to open recovery, or use **Settings > System > Recovery > Advanced startup**.

2. Go to **Troubleshoot > Advanced options > System Restore**.

3. Choose your account and enter your password if asked.

4. Pick the pre-problem restore point and complete the wizard. Your files are untouched — see our [boot repair guide](/articles/best-way-to-use-startup-repair-windows-11/) if recovery itself has issues.

### Fix 5: Fix 'System Restore failed' errors

Restores sometimes fail with 0x80070005 or similar. The usual cause is antivirus blocking the restore or corrupted point data.

1. Temporarily disable third-party antivirus (Windows Security can stay on) and retry.

2. Try a different, older restore point — the newest one may be the corrupted one.

3. Run the restore from **Safe Mode** if normal mode fails.

4. If all points fail, the restore data is unusable — fall back to uninstalling the recent update or driver directly. Microsoft documents the error codes on [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Manage disk space for restore points

Restore points silently vanish when disk space runs low. A little space management keeps your safety net intact.

1. In **System Protection > Configure**, check current usage against your **Max Usage** setting.

2. Raise **Max Usage** if you have space to spare — 10% is comfortable on most laptop SSDs.

3. Don't run aggressive 'cleaner' tools that wipe restore points unless you just created a fresh one.

4. Delete only the oldest points via **Disk Cleanup > Clean up system files > More Options** if you must free space.

### Fix 7: Verify restore points are actually being created

A surprising number of people discover — at the worst moment — that no restore points exist. This check confirms the safety net is real, not theoretical.

1. Open an admin Terminal and run `vssadmin list shadows` — you should see recent shadow copies.

2. If the list is empty, press **Win + R**, type `services.msc`, and set **Volume Shadow Copy** to **Manual**.

3. Open **Task Scheduler**, go to **Microsoft > Windows > SystemRestore**, and confirm the **SR** task is enabled.

4. Create a manual point via **Create a restore point > Create** and name it 'test'.

5. Re-run `vssadmin list shadows` to confirm it appears.

6. If points still don't appear, check that your antivirus isn't blocking the Volume Shadow Copy service.

## Closing

System Restore is the most underused recovery tool in Windows — it undoes exactly the kind of damage (bad updates, bad drivers, bad settings) that causes most Windows problems, in about 20 minutes, without touching your files. The only real mistake is not having it enabled: turn on System Protection today, make a manual point before your next driver update, and the next time something breaks you'll fix it with a wizard instead of a weekend. Make a habit of glancing at your restore points every month or two — open the System Protection tab and confirm recent dates are there. A safety net with holes isn't a safety net, and this thirty-second check finds out before you need it rather than after.
