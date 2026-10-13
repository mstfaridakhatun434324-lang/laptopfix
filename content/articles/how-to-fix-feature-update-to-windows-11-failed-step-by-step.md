---
title: "Feature Update to Windows 11 Failed: Step-by-Step Recovery"
slug: how-to-fix-feature-update-to-windows-11-failed-step-by-step
date: 2026-10-11
categories: ["windows-update"]
tags: ["feature update", "failed", "windows 11", "step by step", "recovery"]
description: "Feature update to Windows 11 failed and rolled back? Step-by-step recovery: read the error, clear blockers, repair the system, and complete the upgrade."
thumbnail: "/images/thumbs/how-to-fix-feature-update-to-windows-11-failed-step-by-step.webp"
faqs:
  - q: "Why do feature updates fail more often than cumulative updates?"
    a: "Feature updates are essentially OS upgrades — they migrate drivers, reapply settings, and replace large parts of the system, while cumulative updates patch in place. The migration phases, especially driver migration, have far more failure points. That is why feature updates demand more free space, current drivers, and fewer connected peripherals than the monthly updates that usually sail through."
  - q: "How much free space does a feature update need?"
    a: "Microsoft's minimum is around 20 GB, but 30 GB or more of free space on the system drive is the practical safe zone. The update stages gigabytes of files, keeps a rollback copy of the old system, and needs working room during migration. Machines hovering near the minimum fail in ways that look like driver or corruption problems but are really space problems."
  - q: "Should I disconnect peripherals for a feature update?"
    a: "Yes — everything except keyboard and mouse. External drives, docks, printers, USB headsets, and SD cards all load drivers into the update's hardware migration phase, and any single misbehaving driver can abort the whole update. This is the highest-value, lowest-effort preparation step for any feature update, and it takes two minutes."
  - q: "What if the feature update fails repeatedly after all fixes?"
    a: "Switch to the in-place upgrade path: download the full Windows 11 ISO from the official download page, mount it, and run setup.exe, choosing to keep files and apps. This uses the same engine with a fresh payload and bypasses the Windows Update delivery path entirely. If even the ISO upgrade fails, the setup logs will identify a specific blocker worth addressing."
---

A feature update is not a patch — it is a full operating system upgrade wearing an update's clothes. When it fails, Windows rolls the machine back to the previous build, and you are left with the same old version, a cryptic error code, and the knowledge that the multi-gigabyte download will have to happen again. The failure stings more than a cumulative update failure because the investment was larger.
The step-by-step recovery below treats the failure as an investigation with a fixed order. Feature update failures have a short list of usual causes — space, drivers, peripherals, corrupted payload, damaged image — and the sequence eliminates them from cheapest to most involved. You will read the error code, prepare the machine properly, repair what is broken, and complete the upgrade through the most reliable path available.
Begin by noting the exact failure code from the update history. If the failure left the machine on the rollback screen, the [undoing-changes best-practice guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) covers that first, and the [troubleshooter walkthrough](/articles/how-to-fix-windows-update-with-troubleshooter-on-windows-11/) automates several early repairs. The official ISOs and assistants live on the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

## Why this happens

- **Insufficient free disk space.** Feature updates need 20–30 GB; cramped drives fail the staging and migration phases.
- **A driver fails migration.** Outdated storage, display, or filter drivers abort the upgrade mid-migration.
- **Connected peripherals interfere.** External devices inject drivers into the hardware migration that fail validation.
- **The downloaded payload is corrupted.** A damaged multi-gigabyte download fails integrity checks partway through.
- **The system image is damaged.** Corruption in the current install breaks the upgrade's migration source.
- **Antivirus blocks the upgrade.** Deep hooks from security software conflict with the migration engine.
- **The BIOS is outdated.** Firmware too old for the target build fails the upgrade's hardware validation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the error code and the setup logs

Feature update failures leave detailed evidence. Collect it before changing anything.

1. Record the exact error code from Settings > Windows Update > Update history.
2. Open `C:\$Windows.~BT\Sources\Panther\setuperr.log` and look for the failing component or driver.
3. Note the failure phase — download, migration, driver install, or finalization — from the log timestamps.
4. Let the phase guide which fixes below you prioritize.

### Fix 2: Free substantial disk space

Space is the number-one feature update killer. Be generous — the rollback copy alone needs gigabytes.

1. Verify at least 30 GB free on C: via Settings > System > Storage.
2. Run Disk Cleanup with system files selected, including previous Windows installations and update cleanup.
3. Move large personal files to external storage and uninstall unused programs.
4. Re-verify the free space; do not proceed on a nearly full drive.

### Fix 3: Disconnect peripherals and pause security software

Two minutes of unplugging removes an entire category of failure. Do it before every feature update attempt.

1. Disconnect all USB devices except keyboard and mouse; remove SD cards and docks.
2. Temporarily uninstall third-party antivirus — disabling is sometimes insufficient for filter drivers.
3. Disable disk utilities and virtual drive tools that install filter drivers.
4. Keep Windows Defender as your active protection during the attempt.

### Fix 4: Update drivers and BIOS

Driver migration is the most failure-prone phase. Current drivers migrate cleanly; old ones do not.

1. Update storage, display, chipset, and network drivers from the manufacturer's support site.
2. Check for and install any available BIOS update on AC power.
3. Remove any device in Device Manager showing a warning icon.
4. Reboot after the driver and firmware refresh.

### Fix 5: Reset the update components and repair the image

A corrupted payload or damaged image poisons the upgrade. Reset both before the retry.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services, then run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
4. Reboot the machine after all repairs complete.

### Fix 6: Run the upgrade via the Installation Assistant

With the machine prepared, use the dedicated upgrade tool rather than the generic update pipeline.

1. Download the Windows 11 Installation Assistant from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Connect to AC power and a stable, unmetered network.
3. Run the assistant and let it download, verify, and install without heavy multitasking.
4. Allow several hours on slower machines — the assistant's phases are long but normal.

### Fix 7: Fall back to the mounted ISO upgrade

If the assistant path fails on prepared ground, the full ISO in-place upgrade is the most reliable route.

1. Download the Windows 11 ISO from the official download page and mount it.
2. Run setup.exe and choose to keep personal files and apps.
3. Follow the prompts through the upgrade, allowing reboots.
4. Afterward, confirm the new build in Settings > System > About and check the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) for any post-upgrade steps.

### Fix 8: Verify the upgrade and re-enable protections

A finished upgrade is not quite done until it is verified and the machine is re-secured. Close out the process properly.

1. Confirm the new build in Settings > System > About and check update history for the success entry.
2. Reinstall the antivirus and utilities you removed, then update them to versions supporting the new build.
3. Reconnect your peripherals one at a time, confirming each works before adding the next.
4. Create a fresh system restore point labeled with the new build — your clean baseline going forward.

## Closing

Feature update failures feel major because the download is major, but the causes are the familiar few: space, drivers, peripherals, payload, image. Prepare the machine like the upgrade it is — 30 GB free, minimal hardware, current drivers and BIOS, quiet security software — and the update becomes the uneventful process it was designed to be. The ISO fallback exists for the stubborn cases; use it without hesitation.
