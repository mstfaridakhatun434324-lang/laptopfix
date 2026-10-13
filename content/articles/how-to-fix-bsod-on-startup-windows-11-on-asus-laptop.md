---
title: "Blue Screen on Startup in Windows 11 on an ASUS Laptop: Fix Guide"
slug: how-to-fix-bsod-on-startup-windows-11-on-asus-laptop
date: 2026-09-10
categories: ["windows-errors"]
tags: ["blue screen on startup", "asus", "windows 11", "boot loop", "startup repair"]
description: "Blue screen every time your ASUS laptop starts Windows 11? Break the boot loop with these 7 fixes, from Safe Mode to Startup Repair."
thumbnail: "/images/thumbs/how-to-fix-bsod-on-startup-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Why does my ASUS laptop blue screen on every startup?"
    a: "Something in the startup sequence fails consistently: a corrupt boot driver, damaged system files, a bad Windows update, or failing hardware (RAM/SSD). Because it happens at the same point each boot, it's systematic — which actually makes it easier to diagnose than random crashes."
  - q: "How do I get into Safe Mode if Windows won't start?"
    a: "Force off the laptop during boot three times in a row (hold power at the ASUS logo). On the fourth boot, Automatic Repair appears: choose Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode."
  - q: "Will Startup Repair delete my files?"
    a: "No. Startup Repair only fixes boot and system files — personal files are untouched. The same goes for System Restore and update uninstalls. Only a clean install erases data."
  - q: "What if it blue screens even in Safe Mode?"
    a: "That points to core Windows corruption or hardware failure rather than a third-party driver. Run Startup Repair, then SFC/DISM from the recovery Command Prompt, then test RAM and the SSD. Safe Mode crashes rule out most third-party software."
---

A blue screen on every startup is Windows 11's way of telling you something in the boot sequence is broken — and on ASUS laptops, it's usually a driver that loads at boot, a corrupted update, or damaged system files. The maddening part is the loop: crash, restart, crash again. The liberating part is that a consistent failure is diagnosable, because whatever breaks does so at the same point every time.

This guide breaks the loop methodically, from getting into Safe Mode through the deeper repairs.

## Why this happens

- **A corrupt boot-start driver.** Storage, chipset, or antivirus drivers that load before the desktop can crash the boot every time.
- **Damaged system files.** Corrupted kernel or boot components from an interrupted update fail at the same point each startup.
- **A bad Windows update.** Update files that don't apply cleanly leave Windows unbootable — extremely common cause of startup loops.
- **Failing SSD.** Bad sectors in boot-critical areas crash startup consistently once they hit the wrong blocks.
- **Faulty RAM.** Memory faults during the high-memory-use boot phase cause crashes before the desktop loads.
- **Fast Startup corruption.** A corrupted hibernation file from hybrid shutdown poisons every "fast" boot.
- **BIOS/firmware issues.** Rare, but a corrupted BIOS or mismatched firmware setting can crash Windows during hardware handoff.

## How to fix it

Work through these in order — start with Fix 1 and stop when Windows boots normally.

### Fix 1: Break into the Recovery Environment and try Safe Mode

First, get to a working environment.

1. Power on, and when the **ASUS logo** appears, hold the **power button** until it shuts off. Repeat this **three times**.
2. On the fourth boot, **Automatic Repair** loads — select **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode. If Safe Mode boots, the problem is a third-party driver or startup program — continue to Fix 2.
4. If Safe Mode also blue-screens, skip to Fix 4 (system repair) — it's core Windows or hardware.
5. From the Recovery Environment you can also access **Startup Repair**, **System Restore**, and **Command Prompt** for the fixes below.

For the broader post-update variant, see our [blue screen after Windows 11 update on ASUS guide](/articles/how-to-fix-blue-screen-after-windows-11-update-on-asus-laptop/).

### Fix 2: Remove the offending driver in Safe Mode

If Safe Mode works, a normal-boot driver is guilty.

1. In Safe Mode, open **Device Manager**.
2. Check for devices with yellow warnings; also consider whatever was updated most recently (display, network, storage).
3. Right-click suspects and choose **Uninstall device**, ticking **Attempt to remove the driver**.
4. Open **Settings > Apps > Installed apps** and uninstall recently added antivirus, VPN, or ASUS utility updates (Armoury Crate updates have caused boot loops).
5. Restart normally and test.

### Fix 3: Disable Fast Startup from the recovery command line

A corrupted hibernation file can crash every fast boot.

1. In the Recovery Environment, open **Command Prompt** under Advanced options.
2. Run `powercfg /h off` — this disables hibernation and Fast Startup entirely.
3. Type `exit` and choose **Continue** to boot Windows.
4. If Windows now boots, the hibernation file was corrupt. You can re-enable hibernation later with `powercfg /h on` in an admin terminal once stable.
5. Leave Fast Startup off permanently if boot loops were frequent — it's implicated in many ASUS startup issues.

### Fix 4: Run Startup Repair and System Restore

Let Windows repair its own boot.

1. In the Recovery Environment: **Troubleshoot > Advanced options > Startup Repair**. Let it run (try up to three times).
2. If that fails, choose **System Restore** and pick a restore point from before the loops began.
3. System Restore doesn't touch personal files — only system state.
4. After booting, pause Windows updates while you stabilize: **Settings > Windows Update > Pause updates**.
5. Create a new restore point once everything works.

### Fix 5: Uninstall the latest update

Updates are the most common trigger of sudden boot loops.

1. In the Recovery Environment: **Troubleshoot > Advanced options > Uninstall Updates**.
2. Remove the **latest quality update** first, restart, test.
3. Then the **latest feature update** if needed.
4. Once booted, update drivers manually (especially chipset and storage from ASUS support) before unpausing Windows Update.
5. If a specific update is the known culprit, check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a revised version later.

### Fix 6: Repair system files from the recovery prompt

Fix corruption Startup Repair can't reach.

1. Open **Command Prompt** in the Recovery Environment.
2. Find your Windows drive letter (`dir C:`, `dir D:` — it's often D: in recovery).
3. Run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` (adjust letter).
4. Run `chkdsk D: /f /r` to check the drive.
5. Type `exit`, continue to Windows, and test.

If restarts also hang rather than crash, our [ASUS restarting screen guide](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-asus-laptop/) covers that failure mode.

### Fix 7: Test hardware — RAM and SSD

When software repairs fail, suspect hardware.

1. Run ASUS pre-boot diagnostics if available (check the BIOS or boot menu for a diagnostics option).
2. From Safe Mode or recovery, run `mdsched.exe` for a Windows RAM test.
3. Review CHKDSK results from Fix 6 — recurring bad sectors mean a dying SSD.
4. Reseat accessible RAM and the SSD if you're comfortable opening the panel.
5. If hardware fails and the laptop is under warranty, contact ASUS with the diagnostic error codes — don't attempt board-level repair yourself.

## Closing

A blue screen on every startup feels like a dead laptop, but it's usually a single broken link in the boot chain — a driver, an update, or a corrupted file — and the Recovery Environment gives you every tool needed to fix it without losing data. Work the list in order, note whether Safe Mode boots (that one fact halves the suspect list), and keep a restore point habit afterward so the next bad update is a ten-minute rollback instead of another loop. A laptop that boots reliably is a laptop you can trust — and it's worth the hour of methodical repair to get there.
