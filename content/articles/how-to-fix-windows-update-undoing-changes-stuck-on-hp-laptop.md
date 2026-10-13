---
title: "Windows Update Undoing Changes Stuck on an HP Laptop: How to Fix It"
slug: how-to-fix-windows-update-undoing-changes-stuck-on-hp-laptop
date: 2026-09-19
categories: ["windows-update"]
tags: ["undoing changes", "hp laptop", "windows update", "rollback stuck", "windows 11"]
description: "HP laptop frozen on the 'Undoing changes made to your computer' screen? This technician's guide covers wait windows, HP-specific conflicts, and safe recovery steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-on-hp-laptop.webp"
faqs:
  - q: "How long should an HP laptop stay on the undoing-changes screen before I act?"
    a: "Give an HP laptop a full hour if it has an SSD, or two hours if it uses a mechanical hard drive, before treating the rollback as stuck. HP machines restore thousands of system files during a rollback, and slower storage makes this look frozen. Watch the drive activity light during the wait: blinking means work is happening, so keep waiting instead of restarting."
  - q: "Is it safe to force a power-off on an HP laptop during the rollback?"
    a: "Yes, once you have waited through the full window with zero activity. The rollback was already restoring your previous working system, so interrupting a genuinely frozen rollback is much safer than interrupting an active update. Hold the power button for ten seconds, unplug peripherals, and boot. Most HP laptops then start normally or enter automatic repair, which fixes the boot files itself."
  - q: "Can HP Support Assistant or HP Wolf Security cause this problem?"
    a: "They can cause the original update failure, though not usually the stuck rollback itself. Outdated HP Support Assistant components and HP Wolf Security drivers have conflicted with update installations on several HP generations. Updating HP's own software and temporarily disabling third-party security during the retry removes two common failure sources. The rollback screen is a Windows mechanism, not an HP one."
  - q: "Will waiting on the rollback screen delete any of my personal files?"
    a: "No. The undo process reverses only the system changes the failed update had started to make. Documents, photos, installed applications, and personal settings are left alone. The entire point of the rollback is to return you to the exact working system you had before the update attempt, so your files remain exactly where they were."
---

Seeing "Undoing changes made to your computer" on your HP laptop is not, by itself, a disaster. It means a Windows update failed and Windows is doing exactly what it was designed to do: rolling the system back to the state that was working before the attempt. On healthy hardware the screen lasts anywhere from fifteen minutes to about an hour, and then the laptop restarts into a normal desktop.
The problem starts when the screen never moves. No percentage counter, no new text, just the spinning circle for two, three, or four hours. At that point you are dealing with a stalled rollback rather than a slow one, and leaving it overnight rarely changes anything. HP laptops add a few brand-specific wrinkles to the diagnosis: HP Support Assistant, HP Wolf Security, and HP's BIOS-level utilities have all been implicated in the update failures that trigger the rollback, and HP Sure Start BIOS protection interacts with the boot sequence if you are forced to power off mid-rollback.
This guide is the full technician sequence for this specific scenario on HP hardware. You will learn how long to wait, how to tell a slow rollback from a frozen one, how to intervene safely, and how to prepare the system so the next update attempt succeeds. The same rollback behavior on other brands is covered in the general guide on [what to do when the undo screen appears](/articles/how-do-i-fix-windows-update-says-undoing-changes-made-to-your-computer/), and if the machine later hangs at boot, the HP-specific [restarting-screen fix](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-hp-laptop/) continues the story.

## Why this happens

- **The original update failed and the rollback triggered.** Driver clashes, corrupted downloads, or antivirus blocking file operations abort the install; Windows reverses the partial changes automatically.
- **The rollback is slow rather than stuck.** Restoring system files takes 15 to 45 minutes on an SSD and up to two hours on a spinning hard drive, during which the screen looks identical to a frozen one.
- **The rollback process itself stalled.** Failing drive sectors, a nearly full system drive, or aggressive security software can freeze the undo mid-way.
- **Outdated HP software contributed to the failure.** HP Support Assistant and HP Wolf Security components have known conflicts with update installations when they are behind on versions.
- **The update cache was corrupted.** Damaged files in the SoftwareDistribution folder give the rollback engine bad data to work from.
- **Disk space ran out.** The undo operation needs working room on C:, and a drive with less than a few gigabytes free stalls it.
- **A queued HP driver package conflicts.** Drivers staged by HP's utilities can fight with the files the rollback is trying to restore.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait the full window and verify real activity

Most rollbacks that look stuck are simply slow. Before you touch anything, confirm that nothing is actually happening. A premature forced restart on a working rollback adds boot-repair work you did not need.

1. Note the exact time the screen appeared, then wait one full hour on an SSD-equipped HP laptop, or two full hours on a hard-drive model.
2. Watch the disk activity light. Blinking or pulsing means the rollback is doing real work, so keep waiting.
3. Listen for drive chatter or fan activity. Steady low-level noise is a good sign; total silence for 30 minutes or more suggests a stall.
4. Proceed to the next fix only after the full wait window with zero screen change and zero drive activity.

### Fix 2: Force a shutdown and let HP's boot process recover

A genuinely frozen rollback will not unfreeze on its own. The rollback was already restoring your previous system, so interrupting a stalled one is one of the safest forced restarts you can perform.

1. Hold the power button for 10 full seconds until the laptop powers off completely.
2. Disconnect every USB device, dock, external monitor, and SD card — HP laptops sometimes hang on peripheral checks after an interrupted boot.
3. Wait 30 seconds, then power the laptop back on. Most HP machines boot to the login screen or desktop at this point.
4. If the machine enters the blue recovery screen, let Automatic Repair run to completion. HP Sure Start may verify the BIOS during this boot; do not interrupt it.

### Fix 3: Boot into Safe Mode and clear the update cache

Once Windows is reachable, stop the next update attempt from failing identically. Clearing the corrupted download cache removes the bad data the rollback choked on.

1. From the login screen, hold Shift while clicking the power icon and choosing Restart, then navigate to Troubleshoot > Advanced options > Startup Settings > Restart and press 4 for Safe Mode.
2. Open an elevated Command Prompt and stop the update services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with the matching `net start` commands and reboot the laptop normally.

### Fix 4: Update HP's own software before retrying

HP's utilities are a documented source of the original update failure. Bringing them current removes the HP-specific conflicts so the retry has a clean run.

1. Open HP Support Assistant and install every pending update it offers, including BIOS and driver updates it lists.
2. Check HP Wolf Security or your third-party antivirus and update it; plan to disable real-time protection temporarily during the next update attempt.
3. Visit [HP's support site](https://support.hp.com/us-en), enter your exact model, and confirm whether a newer BIOS is available.
4. Restart to a clean state with HP's software fully current before touching Windows Update again.

### Fix 5: Free up disk space on the system drive

A rollback and its retry both need working room. Space-starved drives produce exactly this failure pattern: an update that aborts, then an undo that stalls.

1. Open Settings > System > Storage and confirm at least 20 GB free on the C: drive.
2. Run Disk Cleanup, choose the system-files view, and remove Windows Update Cleanup, temporary files, and delivery optimization files.
3. Move large personal files to external storage and uninstall programs you no longer use.
4. Check the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) on update troubleshooting for the current free-space recommendations.

### Fix 6: Repair system files with SFC and DISM

Damage in the system image is a classic cause of the original update failure. Repairing the image before the retry prevents the same abort from repeating.

1. Open an elevated Command Prompt and run `sfc /scannow`; wait for it to finish and review the result.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and allow 15 to 30 minutes for it to complete.
3. Restart the laptop after both tools finish, even if SFC reported no integrity violations.

### Fix 7: Retry the update in a clean state

With the cache cleared, HP software current, space freed, and the image repaired, the retry succeeds in most cases. Control the conditions of the attempt.

1. Connect the laptop to AC power and a stable network connection — never run the retry on battery or metered Wi-Fi.
2. Temporarily disable third-party antivirus real-time protection, leaving Windows Defender active.
3. Go to Settings > Windows Update and click Check for updates, then install whatever appears.
4. If the update fails again with a specific error code, note the code before proceeding to deeper repair.

## Closing

The undoing-changes screen is Windows protecting you from a half-installed update, and on HP laptops the usual chain is an HP-software or driver conflict causing the failure, then a slow or stalled rollback causing the panic. Wait the full window, intervene safely if it is truly frozen, then fix the underlying cause before the retry. Your files survive the rollback untouched, and a clean, prepared retry succeeds far more often than a rushed one.
