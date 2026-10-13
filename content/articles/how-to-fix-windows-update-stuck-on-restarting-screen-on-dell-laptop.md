---
title: "How to Fix Windows Update Stuck on the Restarting Screen on a Dell Laptop"
slug: "how-to-fix-windows-update-stuck-on-restarting-screen-on-dell-laptop"
date: 2026-10-04
categories: ["windows-update"]
tags: ["windows update", "dell laptop", "stuck on restarting", "windows 11"]
description: "Windows Update stuck on the Restarting screen on your Dell laptop? Here are 6 proven fixes, from safe waiting to BIOS and driver repairs, that get your Dell booting again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-on-dell-laptop.webp"
faqs:
  - q: "How long should I wait on the Restarting screen before forcing a shutdown?"
    a: "On a Dell laptop with an SSD, give a cumulative update 60 minutes and a feature update up to 2 hours before intervening. On a mechanical hard drive, allow twice that. Watch for drive activity or spinner movement — if either is happening, Windows is still working. Only force a shutdown when the spinner is completely frozen and there is no drive activity for at least 15 minutes."
  - q: "Will holding the power button damage my Dell laptop or corrupt Windows?"
    a: "A single forced shutdown during a hung update is very unlikely to cause physical damage, and Windows is designed to roll back an interrupted update automatically. You may see Automatic Repair or an “Undoing changes” screen on the next boot, which is normal. Repeated forced shutdowns during BIOS flashes are dangerous, but one power-button hold to escape a frozen Restarting screen is an accepted recovery step."
  - q: "Why does this restarting hang happen more often on Dell laptops?"
    a: "Dell laptops combine custom UEFI firmware, Fast Boot behavior, bundled drivers, and often docking stations — each of which can stall the firmware-to-Windows handoff that the restart phase depends on. Outdated BIOS versions and older Intel Rapid Storage drivers are the most common Dell-specific triggers. Keeping the BIOS and chipset drivers current through Dell Support eliminates most of these hangs before they start."
  - q: "Can Dell SupportAssist fix a Windows Update stuck on restarting?"
    a: "SupportAssist can help prevent the problem by keeping drivers and BIOS current, and its hardware scans can rule out a failing drive behind repeated hangs. However, it cannot unstick an update that is already frozen on the Restarting screen — for that you need the recovery steps above, such as uninstalling the update from WinRE or clearing the SoftwareDistribution cache in Safe Mode."
---

Your Dell laptop shows the blue “Restarting” screen with the spinning dots, and it just never moves on. Minutes turn into an hour, and every instinct says to hold the power button — but you are afraid of corrupting Windows. That fear is reasonable: during the restart phase of an update, Windows is replacing core system files, and an interrupted write can leave the OS in a half-updated state.

On Dell machines this hang is a known pattern. The restart phase (the second half of a cumulative or feature update) relies on Dell’s UEFI firmware handing control back to Windows cleanly, and on storage and chipset drivers loading in the right order. If a [Windows Update stuck on the restarting screen on Windows 11](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-11/) occurs on a generic PC it is usually software; on a Dell, firmware and bundled drivers deserve equal suspicion. Work through the fixes below in order and you will know exactly when it is safe to intervene.

## Why this happens

- **Dell Fast Boot or BIOS handoff stalling:** Some Dell BIOS versions hold USB or Thunderbolt initialization during reboot longer than Windows expects, so the “Restarting” spinner spins while the system waits on firmware, not on the update itself.
- **Corrupted update cache:** If files in the SoftwareDistribution folder were only half-downloaded or damaged, the restart-phase installer retries the same broken payload in a loop instead of progressing.
- **Security software locking system files:** Third-party antivirus or Dell’s bundled security tools can lock files the updater needs to replace, freezing the operation with no error message on screen.
- **Failing or nearly full system drive:** Feature updates need 20 GB or more of free space. A nearly full SSD forces the installer to shuffle files slowly, and the Restarting screen can sit for hours on a drive with under 10 percent free.
- **Peripheral devices holding the boot process:** USB docks, external drives, and even some Dell docking stations keep the reboot handshake waiting while Windows polls devices that never respond.
- **Outdated Intel Rapid Storage or chipset drivers:** If the storage driver version predates the update, Windows may fail to bring the disk back online after the firmware handoff, leaving the spinner running on a system that is actually stalled.
- **Interrupted first phase of the update:** If the laptop slept, lost power, or the lid was closed while files were being staged before the restart, the restart phase starts with an incomplete payload and cannot finish.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Give it a real deadline before touching anything

The single most common mistake is interrupting a healthy update. On an SSD, a cumulative update’s restart phase should finish within 30 to 45 minutes; a feature update can legitimately take up to 2 hours. On a spinning hard drive, double those numbers. Watch the drive activity light or listen for disk sounds — if there is activity, Windows is still working.

1. Note the time and wait at least 60 minutes on an SSD, 120 minutes on a hard drive.
2. Check for drive activity: a blinking activity LED or faint disk sounds mean progress.
3. If the spinner animation itself is frozen (dots not moving at all) for 15+ minutes, the process is genuinely hung, not slow.
4. Only proceed to a forced restart if both the spinner is frozen and there is zero drive activity.

### Fix 2: Force a restart safely and check for rollback

When the system is truly hung, holding the power button is the correct next step — Windows Update is designed to roll back gracefully in most cases. A forced shutdown during the restart phase usually triggers automatic repair or the “Undoing changes” rollback on the next boot, which is far better than a permanently spinning screen.

1. Press and hold the power button for a full 10 seconds until the laptop powers off completely.
2. Disconnect the charger, wait 30 seconds, then reconnect it and power on.
3. If Windows boots normally, open Settings > Windows Update and check the update history for a failed entry.
4. If you see the [undoing changes loop](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-dell-laptop/) instead, let it finish — it can take 30 to 60 minutes.

### Fix 3: Use Windows Recovery to uninstall the stuck update

If the laptop will not boot into Windows after the forced restart, the Windows Recovery Environment (WinRE) lets you remove the offending update without touching your files. Dell laptops reach WinRE by interrupting the boot process twice, or through the F12 boot menu.

1. Power on, and as soon as the Dell logo appears, hold the power button to force off — repeat twice to trigger Automatic Repair.
2. On the recovery screen choose Troubleshoot > Advanced options > Uninstall Updates.
3. First try “Uninstall latest quality update”; if that fails, try “Uninstall latest feature update”.
4. Select Restart and let Windows boot, then pause updates for 7 days while you apply the remaining fixes.

### Fix 4: Clear the corrupted update cache in Safe Mode

The SoftwareDistribution folder holds staged update files. When these are damaged, every retry hangs at the same point. Deleting the folder forces Windows to re-download a fresh copy, and doing it from Safe Mode avoids the file locks that cause the hang in the first place.

1. Boot into Safe Mode: WinRE > Troubleshoot > Advanced options > Startup Settings > Restart, then press 4.
2. Open an elevated Command Prompt and run: net stop wuauserv and then net stop bits.
3. Run these commands: rd /s /q C:\Windows\SoftwareDistribution and rd /s /q C:\Windows\System32\catroot2.
4. Restart normally, then check the [Windows Update troubleshooter guidance](https://support.microsoft.com/en-us/windows) if updates still misbehave before retrying.

### Fix 5: Disconnect peripherals and disable Fast Startup

Dell docks and USB devices are a classic cause of restart-phase hangs because the BIOS polls them during handoff. Fast Startup compounds the problem by keeping a hibernation-style kernel session that can conflict with the update’s driver swap.

1. Power off and unplug every USB device, dock, SD card, and external display.
2. Boot into Windows, open Control Panel > Power Options > Choose what the power buttons do.
3. Click “Change settings that are currently unavailable” and uncheck “Turn on fast startup”.
4. Retry the update with only the charger connected; reattach peripherals one at a time afterward.

### Fix 6: Update the Dell BIOS and chipset drivers

Dell’s own update packages fix exactly the firmware-handoff bugs that cause restart hangs. Check your current BIOS version against the latest on Dell’s support site for your service tag, because a BIOS that predates your Windows build by years is a red flag. The Intel chipset and Rapid Storage drivers should be refreshed at the same time.

1. Find your service tag on the bottom of the laptop or in the BIOS (F2 at boot).
2. Go to [Dell Support](https://www.dell.com/support), enter the service tag, and download the latest BIOS and chipset drivers.
3. Install the BIOS update with the charger connected and the battery above 50 percent — never interrupt a BIOS flash.
4. Also run the [Intel Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch storage and chipset drivers Windows Update missed, then retry the Windows update.

## Closing

A Dell laptop frozen on the Restarting screen almost always recovers with the sequence above: verify it is truly hung, force a clean restart, remove the bad update or its cache, and eliminate the firmware and peripheral triggers before retrying. Keep your BIOS and chipset drivers current going forward — on Dell hardware, that single habit prevents more update hangs than any other step.
