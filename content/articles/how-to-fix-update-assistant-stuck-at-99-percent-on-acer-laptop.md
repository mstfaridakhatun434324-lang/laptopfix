---
title: "Update Assistant Frozen at 99% on an Acer Laptop: Break the Stall"
slug: how-to-fix-update-assistant-stuck-at-99-percent-on-acer-laptop
date: 2026-10-11
categories: ["windows-update"]
tags: ["update assistant", "stuck at 99", "acer laptop", "feature update", "frozen install"]
description: "The Update Assistant is frozen at 99% on your Acer laptop. Confirm the stall, recover safely, and fix what blocked the final install phase."
thumbnail: "/images/thumbs/how-to-fix-update-assistant-stuck-at-99-percent-on-acer-laptop.webp"
faqs:
  - q: "How can I tell the difference between slow and stuck at 99%?"
    a: "Open Task Manager and watch setuphost.exe and related setup processes. Sustained CPU or disk activity means the final phase is working — it can legitimately take over an hour with no visible progress. Zero activity for a full hour, with the charger connected and the laptop awake, means it's genuinely stuck and you should proceed with recovery."
  - q: "Does Acer's factory recovery partition affect the Update Assistant?"
    a: "No, the Assistant ignores the recovery partition — it upgrades the Windows installation in place and leaves recovery intact. A nearly-full recovery partition doesn't block the upgrade either. What matters is free space on C: itself; keep 20 GB free there regardless of how the recovery partition looks."
  - q: "Should I disable Secure Boot to unstick the Assistant?"
    a: "No — don't touch Secure Boot. It has nothing to do with 99% stalls, and disabling it can complicate the boot process after the upgrade. The stall is in driver migration or final verification, not in boot security. Leave firmware security settings exactly as they are and focus on drivers, antivirus, and disk space."
  - q: "What if the laptop overheats while stuck at 99%?"
    a: "Extended high-CPU final phases do heat laptops up. Make sure vents are clear and the laptop sits on a hard surface — not a bed or couch. If it's genuinely overheating (fan at max for an hour, chassis very hot), it's reasonable to cancel via the Assistant's own cancel option, let it cool, improve ventilation, and retry. Don't force-shutdown for heat alone unless it's an emergency."
---

The Update Assistant on your Acer laptop has been sitting at 99% for what feels like forever. You have read that the last percent is the slowest — but at some point, slow becomes stuck, and you need to know which one you are looking at and what to do about it.

At 99%, the Assistant is doing its hardest work: migrating every driver to the new Windows version, running final verification, and preparing the reboot. On Acer laptops the usual blockers are outdated drivers from Acer's catalog, antivirus file locks, or a nearly-full system drive. Each is fixable; none require reinstalling Windows.

Work through these in order — diagnose first, then act.

## Why this happens

- **Driver migration deadlock.** An outdated Acer driver crashes or hangs during the final migration phase.
- **Antivirus file locks.** Real-time protection holds files the installer must replace at the end.
- **Low disk space on C:.** The final phase needs working room for rollback data and verification.
- **Corrupted Assistant package.** A damaged download passes early phases and fails final verification.
- **Acer bloatware interference.** Preinstalled utilities locking components during migration.
- **Pending servicing operations.** Earlier unfinished updates blocking final configuration.
- **Overheating throttling.** Thermal throttling stretching the final phase into hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is stuck, not working

Open Task Manager (Ctrl+Shift+Esc) and find setuphost.exe / SetupPrep.exe. Watch CPU and disk columns for 15 minutes: any sustained activity means the final phase is alive — driver migration with Acer's full driver set can genuinely take 60-90 minutes with the bar unmoving.

Only declare it stuck after a full hour of zero setup activity with the charger plugged in and sleep disabled. Acting on a working install is the main way people turn a slow upgrade into a broken one. Note the time you started watching so your "hour" is real, not felt.

### Fix 2: Cancel safely and assess

If the stall is confirmed, use the Update Assistant's own cancel/close option rather than killing setup processes in Task Manager — force-killing mid-migration is riskier than a graceful cancel. Restart the laptop afterward.

Windows will either resume the update, roll back to your previous version, or boot normally with the update pending. Let whichever happens finish completely. Do not relaunch the Assistant yet — first remove the blocker, or you will reproduce the identical stall. The ASUS version of this problem is covered in the [Update Assistant 99% guide for ASUS laptops](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-asus-laptop/), with the same final-phase mechanics.

### Fix 3: Update Acer drivers and BIOS

The 99% phase migrates drivers, so stale drivers are suspect number one. Open Acer Care Center and install all pending updates — BIOS, chipset, graphics, storage. Or get them from Acer's support site with your serial number.

Keep the AC adapter connected during any BIOS flash and leave the machine alone. Updated drivers migrate cleanly; outdated ones deadlock. After updating, restart once normally to confirm stability before retrying the Assistant. This single preparation step resolves the plurality of 99% stalls on Acer hardware.

### Fix 4: Remove antivirus and quiet the startup

Uninstall third-party antivirus completely using its removal tool — the final install phase replaces system files that antivirus products love to lock, and a lock at 99% is a deadlock. Windows Security covers you during the upgrade.

Open Task Manager, Startup tab, and disable non-essential startup items, especially Acer utilities and any "optimizer" tools. These inject into system processes the installer needs exclusive access to. Re-enable everything after the upgrade succeeds. The goal is the quietest possible system during the final phase.

### Fix 5: Free space, check the disk, mind the heat

Get 20+ GB free on C: via Storage Sense and temp-file cleanup. Run `chkdsk C: /f` from an elevated Command Prompt to rule out filesystem corruption slowing final verification.

Set the laptop on a hard, flat surface with vents unobstructed, and set the power plan to keep it awake (Settings, System, Power & battery — set screen and sleep to "Never" while plugged in during the upgrade). Thermal throttling plus sleep interruptions can stretch the final phase past the point where users assume a freeze. Eliminate both variables. Microsoft's [Windows support resources](https://support.microsoft.com/en-us/windows) document power and disk maintenance.

### Fix 6: Fresh Assistant download, clean environment

Delete the old Update Assistant executable and remove `C:\$Windows.~BT` (take ownership if denied). Download a fresh Assistant from the [official Microsoft download page](https://www.microsoft.com/en-us/software-download/windows11).

Launch it with antivirus still uninstalled, startup items disabled, 20 GB free, and drivers current. Let it run start to finish without pausing — do not put the laptop to sleep, do not run heavy apps alongside. A clean package in a clean environment is the combination that gets past 99%.

### Fix 7: Switch to the ISO-based upgrade

If the Assistant stalls at 99% a second time despite full preparation, change the installer: download the Windows 11 ISO from the [official Microsoft download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run setup.exe, and choose "Keep personal files and apps."

The ISO setup engine is more robust through the final migration phase than the Assistant's. Same upgrade, better delivery vehicle. Do the full pre-flight once more before launching — drivers, space, no antivirus, peripherals unplugged. If the Dell variant of this stall interests you for comparison, the [Update Assistant 99% guide for Dell](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-dell-laptop/) documents identical mechanics on different hardware.

## Closing

A 99% freeze is the Assistant choking on the hardest phase — driver migration and final verification — because something is in the way. Verify the stall is real with Task Manager, then clear the track: current Acer drivers and BIOS, no antivirus locks, 20 GB free, good cooling, fresh download. The ISO upgrade is the proven fallback when the Assistant's engine cannot finish. The last percent is always the slowest; make sure it is slow, not stuck, and then make it finish.
