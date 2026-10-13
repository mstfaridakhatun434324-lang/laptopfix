---
title: "How to Use System Restore on Windows 11: Step by Step"
slug: how-can-i-use-system-restore-on-windows-11
date: 2026-09-14
categories: ["windows-errors"]
tags: ["system restore", "windows 11", "recovery"]
description: "System Restore can undo bad drivers, updates, and settings in minutes. Learn how to enable it, create restore points, and roll back Windows 11 safely."
thumbnail: "/images/thumbs/how-can-i-use-system-restore-on-windows-11.webp"
faqs:
  - q: "Will System Restore delete my personal files?"
    a: "No. System Restore only touches system files, installed programs, drivers, and registry settings. Your documents, photos, and downloads are left alone. That said, any programs installed after the restore point was created will need to be reinstalled, so it is still smart to keep a backup of anything important before you begin."
  - q: "How much disk space does System Restore need?"
    a: "Windows recommends reserving at least 1 to 3 percent of the drive, but 5 to 10 GB gives you a healthier history of restore points. You can adjust the slider in System Protection settings. When the reserved space fills up, Windows deletes the oldest restore points first, so a bigger reservation means you can roll back further."
  - q: "Can I undo a system restore?"
    a: "Yes. When you run System Restore from inside Windows, it automatically creates a new restore point right before making changes. If the restore makes things worse, just run System Restore again and pick that automatically created point to go back to where you started."
  - q: "Why are there no restore points on my laptop?"
    a: "The most common reason is that System Protection was never turned on — Windows 11 sometimes leaves it disabled, especially on fresh installs. Other causes include too little reserved disk space, the Volume Shadow Copy service being disabled, or a disk cleanup tool deleting old points. Turn protection on and create a manual point to start fresh."
---

System Restore is one of the most underrated tools in Windows 11. When a bad driver, a broken update, or a settings change turns your laptop into a mess, a restore point can roll the system back to when everything worked — usually in under 15 minutes.

The catch is that it only works if it was set up beforehand. Many laptops ship with System Protection turned off, so the first thing we'll do is check that. Then I'll show you how to create restore points manually and how to actually use one when trouble hits.

## Why this happens

- **System Protection was never enabled.** Windows 11 doesn't always turn it on during setup, so no restore points exist when you need one.
- **Too little reserved disk space.** If the reservation is tiny or the drive is nearly full, Windows silently deletes old restore points.
- **Volume Shadow Copy service disabled.** This background service creates restore points; some "optimizer" tools turn it off.
- **Restore point corrupted.** A point created during a crash or power loss can fail when you try to use it.
- **Disk cleanup removed them.** Aggressive cleaning tools can wipe restore points along with temporary files.
- **Restoring from a point that's too old.** Very old points may reference drivers that no longer match your hardware state.
- **Dual-boot or drive letter changes.** If you repartitioned the drive or changed drive letters, stored restore points can become unusable because they reference the old layout.

## How to fix it

Work through these in order, from Fix 1 onward, and stop once you're back to a working system.

### Fix 1: Turn on System Protection

Nothing else on this page matters until this is enabled. It takes about a minute.

1. Press **Win + S**, type `Create a restore point`, and open it.
2. In the **System Protection** tab, select your system drive (usually **C:**) and click **Configure**.
3. Choose **Turn on system protection**.
4. Drag the **Max Usage** slider to at least 5 percent or roughly 5 to 10 GB.
5. Click **OK**, then **Apply**. Windows will now create restore points automatically before updates and driver installs.

### Fix 2: Create a manual restore point right now

Don't wait for Windows to do it on its own. Make one before any big change — a driver update, a BIOS flash, or installing unfamiliar software.

1. Open the **System Protection** tab again (**Win + S**, type `Create a restore point`).
2. Click the **Create** button at the bottom.
3. Give it a clear name like `Before NVIDIA driver update` and click **Create**.
4. Wait for the confirmation message, then click **Close**.
5. Repeat this habit before every risky change and you'll always have a way back.

### Fix 3: Restore from inside Windows

If Windows still boots, this is the fastest way to roll back.

1. Open **System Protection** and click **System Restore**.
2. Click **Next**, then pick a restore point dated before the problem started.
3. Click **Scan for affected programs** to see what will be removed — review this list carefully.
4. Click **Next**, then **Finish**, and confirm the warning.
5. Your laptop will restart and apply the restore. Don't turn it off during the process.

### Fix 4: Restore from the recovery environment

If Windows won't boot at all, you can still reach System Restore through the recovery menus. Our [startup repair walkthrough](/articles/how-to-use-startup-repair-windows-11-on-laptop/) covers getting into this environment in detail.

1. Hold **Shift** while clicking **Restart**, or interrupt the boot three times to trigger Automatic Repair.
2. Go to **Troubleshoot > Advanced options > System Restore**.
3. Sign in with an administrator account when prompted.
4. Select a restore point and follow the same wizard as in Fix 3.
5. Let it finish and restart — the whole process usually takes 10 to 20 minutes.

### Fix 5: Undo a restore that made things worse

Sometimes a restore point itself is the problem. Windows thought of that and made restores reversible.

1. Open **System Restore** again from the **System Protection** tab.
2. You'll see a restore point named something like `Undo: Restore Operation` with today's date.
3. Select it, click **Next**, then **Finish**.
4. The laptop restarts and returns to the state it was in before the first restore.
5. From there, try a different, older restore point instead.

### Fix 6: Fix "System Restore did not complete successfully"

This error usually means the Volume Shadow Copy service isn't running properly.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Volume Shadow Copy**, double-click it, and set **Startup type** to **Manual**.
3. Find **Microsoft Software Shadow Copy Provider** and make sure it is also set to **Manual**.
4. Temporarily disable your third-party antivirus, then try the restore again.
5. Re-enable your antivirus afterward, and consider adding restore points to its exclusion list if the problem repeats.

### Fix 7: Adjust disk space so restore points survive

If restore points keep vanishing, Windows is deleting them to save space.

1. Open the **System Protection** tab and click **Configure** for your system drive.
2. Increase **Max Usage** to at least 10 percent if your drive has room.
3. Delete all but the most recent point with the **Delete** button if space is critically low, then create a fresh manual point.
4. Check that your C: drive has at least 10 to 15 GB of free space overall.
5. Going forward, verify once a month that a recent restore point actually exists.

## Closing

System Restore won't fix a dead hard drive, but for software-caused messes it's the fastest way back to normal. Enable it today, make manual points before risky changes, and check once a month that a recent point actually exists — a restore point you never verify is only half a safety net. And if a restore isn't enough and Windows still misbehaves, a [reset that keeps your files](/articles/how-to-reset-windows-11-without-losing-files/) is the next step up. Microsoft also has a [recovery options overview](https://support.microsoft.com/en-us/windows) worth bookmarking.
