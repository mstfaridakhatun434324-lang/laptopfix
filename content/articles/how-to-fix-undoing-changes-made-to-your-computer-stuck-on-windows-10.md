---
title: "How to Fix 'Undoing Changes Made to Your Computer' Stuck on Windows 10"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-10
date: 2026-09-11
categories: ["windows-update"]
tags: ["undoing changes", "windows 10", "windows update", "update stuck", "rollback"]
description: "Windows 10 stuck on 'Undoing changes made to your computer'? Learn the safe waiting window, how to force a restart, and how to stop the loop."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-10.webp"
faqs:
  - q: "How long should I wait on the 'Undoing changes' screen in Windows 10?"
    a: "Allow 45 minutes to an hour on an SSD, and up to two hours on a mechanical hard drive, before concluding it is stuck. Windows 10 rollbacks involve restoring a large number of system files, and older hardware does this slowly. Only intervene after the screen has shown zero change and the drive activity light has stayed dark for a full 30 minutes."
  - q: "Will forcing a restart during rollback damage Windows 10?"
    a: "It carries less risk than interrupting an active update installation, because the system is already reverting to its previous working state. There is still a small chance of a damaged boot configuration, so only force a restart after a genuine multi-hour stall. If the laptop then fails to boot, the built-in automatic repair usually fixes the boot files on its own."
  - q: "Why does Windows 10 keep undoing the same update?"
    a: "When an update fails the same way every time, the cause is usually a corrupted update download, a driver that conflicts with the new build, or insufficient free disk space. Windows 10 will keep attempting the update on its own schedule and rolling it back on failure. Pausing updates, clearing the cache, and identifying the specific failing update breaks the cycle."
  - q: "Do I lose my files when Windows undoes an update?"
    a: "No. The rollback reverses only the system changes the update made. Your documents, pictures, installed applications, and personal settings are not touched. The entire purpose of the rollback mechanism is to return you safely to the working system you had before the update attempt began."
---

Windows 10 handles a failed update by rolling it back automatically, and that is what the "Undoing changes made to your computer" screen means: the installer hit a problem and Windows is restoring your previous system state. It is a safety mechanism doing its job. The frustration begins when the screen sits there for hours with a spinning circle and no percentage, and you start wondering whether anything is actually happening.

On most Windows 10 laptops this rollback is slow rather than stuck. Older machines with mechanical hard drives are common in the Windows 10 world, and they can take a long time to restore thousands of system files. That said, there is a clear line between slow and frozen, and this guide shows you exactly where it is — plus what to do on each side of it.

Work through the fixes below in order. The first two deal with the stuck screen itself; the rest stop it from happening again on the next update attempt.

## Why this happens

- **The update failed its final checks.** A corrupted download, an incompatible driver, or an antivirus blocking a critical file makes the installer abort, which triggers the automatic rollback.
- **The rollback stalled on slow or failing storage.** Mechanical hard drives are slow to restore files, and drives with bad sectors can stall the process entirely.
- **The C: drive is nearly full.** Rollbacks need working space. With less than 10 GB free, the undo process crawls or freezes partway through.
- **Corrupted update cache replays bad data.** Damaged files in SoftwareDistribution can keep the rollback engine working on broken payloads.
- **A queued driver update conflicts with the rollback.** Windows 10 often bundles driver updates with system updates, and a bad driver package can fight the restore process.
- **Third-party security software interferes.** Antivirus products that hook the file system can block the rollback from writing restored files.
- **Failing memory causes silent corruption.** Bad RAM produces corrupt writes during the rollback, which the engine detects and retries in a loop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait a proper window and check for real activity

Resist the urge to act for the first stretch. Most Windows 10 rollbacks on older laptops just need time.

1. Give the screen a full hour on an SSD-based laptop, or two full hours on a mechanical hard drive, measured from when the screen first appeared.
2. Watch the disk activity LED on the laptop. Blinking or solid activity means the rollback is working — do not touch anything.
3. Listen to the machine. Drive chatter and fan noise indicate progress; total silence for 30 minutes straight indicates a stall.
4. Only move to the next fix when there has been no screen change and no drive activity for the entire waiting window.

### Fix 2: Force a restart and let automatic repair do its job

A genuinely frozen rollback will not unfreeze itself. Since Windows was already reverting to a safe state, a forced restart is the right call.

1. Press and hold the **power button** for 10 seconds until the laptop powers off. Disconnect USB drives, docks, and external displays.
2. Wait 30 seconds and power on. Most of the time Windows 10 boots to the desktop or login screen, because the rollback had partially finished its work.
3. If the laptop boots into the blue recovery screen instead, let **Automatic Repair** run — it usually fixes the boot configuration on its own.
4. Once you are in Windows, do not immediately run Windows Update again. Use the system normally first and confirm everything is stable.

### Fix 3: Clear the update cache in Safe Mode

If the next update attempt lands you right back on the undo screen, corrupted cached files are the most likely cause.

1. From the login screen, hold **Shift** and click **Restart** to reach the recovery environment, then choose **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.
2. Open an elevated Command Prompt and stop the update services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`, then reboot normally.

### Fix 4: Free up disk space before the next attempt

Windows 10 updates and their rollbacks both demand free space on C:, and older laptops are often running close to full.

1. Open **Settings > System > Storage** and check free space on the system drive. Aim for at least 20 GB free before retrying a major update.
2. Run **Disk Cleanup** as an administrator, select system files, and remove **Windows Update Cleanup**, temporary files, and delivery optimization files.
3. Move large personal files to external storage and uninstall programs you do not use.
4. Only retry the update after confirming the free space. Space-starved updates are one of the most common causes of repeat undo loops on Windows 10.

### Fix 5: Run the Windows Update troubleshooter

Windows 10 has a built-in troubleshooter that repairs the most common update pipeline problems automatically.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Update** and click **Run the troubleshooter**.
3. Apply every fix it offers, then restart the laptop.
4. Try checking for updates again. If the troubleshooter repaired a jammed service or registration, the update may now install cleanly.

### Fix 6: Repair system files with SFC and DISM

Damage in the system image can cause both the original failure and a stalled rollback.

1. Open an elevated Command Prompt and run `sfc /scannow`. Let it complete without closing the window.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth`, which downloads healthy replacement components. Allow 15 to 30 minutes.
3. Restart the laptop and check for updates. Repaired system files often break the failure cycle that was triggering the rollback.

### Fix 7: Pause updates, install manually, or block the bad update

If the same update keeps failing and rolling back, change your approach instead of repeating it.

1. In **Settings > Update & Security > Windows Update > Advanced options**, pause updates for 7 to 35 days to stop the automatic retry loop.
2. Note the failing update's KB number in **View update history**, then download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually — offline installs bypass several automatic-pipeline failure modes.
3. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that KB number; sometimes the correct move is simply waiting for a revised version.
4. For a feature update that your older hardware struggles with, consider staying on your current Windows 10 build with security updates until you are ready to move to Windows 11.

## Closing

The "Undoing changes" screen on Windows 10 is usually a slow process rather than a broken one — the critical step is verifying real disk activity before you intervene. Once you are back on the desktop, the goal is to stop the next attempt from ending the same way: clear the cache, free up space, and identify the specific failing update instead of letting Windows retry blindly. If you are seeing the undo screen after a version upgrade attempt rather than a routine update, the Windows 11 variant of this problem is covered in our guide to [undoing changes stuck on Windows 11](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11/), and the [in-depth undoing-changes walkthrough](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/) covers the 24H2-era rollback behavior in detail.
