---
title: "Undoing Changes Made to Your Computer Stuck After a Windows 11 Update? How to Fix It"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update
date: 2026-09-02
categories: ["windows-update"]
tags: ["undoing changes", "windows 11 update", "update rollback", "stuck update", "windows update fix"]
description: "Stuck on 'Undoing changes made to your computer' after a Windows 11 update? Learn why the rollback hangs and work through proven fixes in the right order."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update.webp"
faqs:
  - q: "How long should the 'Undoing changes made to your computer' screen normally take?"
    a: "On a healthy machine with an SSD, a rollback usually completes in 15 to 45 minutes, because Windows is reversing the update transaction file by file through the component store. Older laptops with mechanical hard drives can legitimately need up to an hour. If the screen has not changed and there is no disk activity for more than 60 to 90 minutes, the rollback has likely stalled and you should work through the diagnostic steps in this guide."
  - q: "Is it safe to force-shutdown a laptop stuck on the undoing changes screen?"
    a: "Only as a last resort after confirming zero disk activity for at least 30 to 60 minutes. A forced shutdown during an active rollback can corrupt the component store and leave the system unbootable. If you must do it, hold the power button once, disconnect all USB devices, wait 30 seconds, then power on and let Windows attempt the rollback again or boot into recovery."
  - q: "Will I lose my personal files when Windows undoes the changes?"
    a: "No. The rollback only reverses the update payload — system files, drivers, and registry entries that the update touched. Your documents, photos, and installed applications are not part of the update transaction and are left alone. That said, if the machine is already misbehaving, taking a backup before attempting the deeper fixes is always the smart move."
  - q: "Why does the same update keep failing and triggering the rollback again?"
    a: "Because the root cause was never fixed: a corrupted update cache, an incompatible driver, or insufficient disk space will fail the same package every time Windows retries it. Clear the SoftwareDistribution cache, free at least 20 GB on the system drive, and update your drivers from the manufacturer's site. If one specific KB keeps failing, hide it temporarily with Microsoft's show-or-hide updates troubleshooter."
---

The "Undoing changes made to your computer" screen after a Windows 11 update shows no progress bar and no error code, which makes it uniquely stressful. Here is the reassuring part first: this screen is Windows protecting you. The update failed its integrity checks, so the servicing engine is reversing every file the update touched and returning your laptop to its last known good state. Your files are not being deleted.

The rollback is a database-style transaction running through the component store (WinSxS): Windows restores drivers, registry hives, and system files from the pre-update snapshot. On a healthy SSD laptop this takes 15 to 45 minutes. When it takes much longer, something is blocking the reversal — a driver that will not unload, a corrupted update cache, or a disk too full for both copies of the changed files. Work through the fixes below in order, giving each step its fair window of time.

Before touching anything, observe three things: how long the screen has shown, whether the disk light blinks, and whether the fan runs. Blinking disk activity plus a running fan means real work is happening — walk away and let it finish. A dark, silent machine at the same screen for over an hour is the signal to intervene, which is what the rest of this guide covers.

## Why this happens

- **A corrupted download in the update cache:** an incomplete staged package that fails its hash check aborts the install and triggers the rollback.
- **A driver that conflicts with the new build:** graphics, storage controller, and Wi-Fi drivers are the usual suspects; when one cannot migrate cleanly, the update unwinds itself.
- **Too little free disk space:** Windows needs room for the staged update plus the rollback snapshot. Space running out mid-install is a classic rollback trigger.
- **Third-party antivirus locking system files:** some security suites lock files or filter drivers during installation, which the update engine reads as corruption.
- **Pending operations from a previous update:** leftover pending.xml entries or a skipped reboot leave the servicing stack in an inconsistent state for the next update.
- **Corrupted system files in the component store:** a damaged WinSxS store means new components cannot be staged, so the installer backs out every time.
- **Peripherals stalling driver migration:** USB docks, external drives, and even some keyboards can hang the plug-and-play phase of a feature update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give the rollback a genuine window to finish

The most common fix for this screen is patience: the servicing engine is slow on older hardware and shows almost no progress. Interrupting a working rollback turns a recoverable situation into an unbootable one.

1. Plug the laptop into AC power and leave it exactly where it is.
2. Watch the storage activity light for at least 30 minutes — 60 minutes if the laptop has a mechanical hard drive.
3. Do not press the power button, close the lid, or unplug anything during this window.
4. If the spinner or dots visibly advance, even slowly, keep waiting; the transaction is progressing. This is the same wait-it-out discipline that helps with any [update stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).

### Fix 2: Force a clean restart only if the machine is truly frozen

If the screen has not changed for over an hour with zero disk activity, the rollback process has likely deadlocked. One controlled hard reset is acceptable at this point — Windows is designed to resume or restart the rollback on next boot rather than load a half-written system.

1. Confirm no disk activity for at least 30 consecutive minutes first.
2. Hold the power button for 10 seconds until the machine powers off completely.
3. Disconnect all USB devices, docks, and external drives.
4. Wait 30 seconds, then power on and watch whether the rollback resumes or Windows boots normally.
5. If it boots, back up important files immediately before doing anything else.

### Fix 3: Boot into Safe Mode and run the troubleshooter

Safe Mode loads only core drivers, which bypasses the driver conflicts behind many rollbacks. From there you can run the built-in troubleshooter without the update engine fighting you.

1. Power off, then power on and interrupt the boot twice (hold the power button at the Windows logo) to reach Automatic Repair.
2. Choose Troubleshoot, then Advanced options, then Startup Settings, then Restart, and press 4 for Safe Mode.
3. In Safe Mode, open Settings, then System, then Troubleshoot, then Other troubleshooters.
4. Run the Windows Update troubleshooter and apply every fix it offers. If the troubleshooter itself misbehaves, see our guide on the [Windows Update troubleshooter not working](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).
5. Restart normally and check whether updates proceed.

### Fix 4: Reset the Windows Update cache (SoftwareDistribution)

The SoftwareDistribution folder holds staged downloads and the update database. When it is corrupted, every retry fails identically. Renaming it forces Windows to rebuild it from scratch — safe, and effective.

1. Open Command Prompt as administrator.
2. Stop the update services with these commands, one at a time: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Reboot and try Windows Update again. Microsoft documents this cache-reset approach in its [Windows update support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair system files with DISM and SFC

If the component store is damaged, no update will install until it is repaired. DISM repairs the underlying image; SFC then verifies protected files against it.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish — this takes 10 to 30 minutes.
3. Then run `sfc /scannow` and let it verify and repair files.
4. Reboot the laptop after both commands complete.
5. Re-run Windows Update to confirm the failure is gone.

### Fix 6: Free up disk space and disconnect peripherals

Updates routinely need 10 to 20 GB of working room. A nearly full drive starts the install, runs out of space mid-transaction, and unwinds — the exact loop you are seeing. Peripherals add a second failure point during driver migration.

1. Open Settings, then System, then Storage, and check free space on C:.
2. Run Disk Cleanup as administrator and tick Windows Update Cleanup and Temporary files.
3. Unplug every USB device except keyboard and mouse — docks, printers, external drives, SD cards.
4. Temporarily disable third-party antivirus (Windows Security stays on) and disconnect any VPN.
5. Aim for at least 20 GB free, then retry the update.

### Fix 7: Identify and hide the failing update

When one KB keeps failing, hiding it stops Windows retrying it while you address the cause. Microsoft's "Show or hide updates" troubleshooter still works on Windows 11.

1. Open Settings, then Windows Update, then Update history, and note the KB number that failed.
2. Check that KB on Microsoft's support site for documented known issues.
3. Download the "Show or hide updates" troubleshooter (wushowhide.diagcab) and run it.
4. Choose Hide updates and select the failing KB.
5. Retry the remaining updates; unhide the KB after Microsoft publishes a fix. If the system remains unstable, a repair install using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) ISO is the next escalation.

## Closing

Rollback screens are alarming, but they are Windows doing its job — refusing to leave you with a half-installed system. Work the list in order and give the early steps their time. If every fix fails, run a drive-health check: recurring rollbacks across different KB numbers point at failing storage more often than people expect.
