---
title: "How to Update BIOS on a Laptop Running Windows 11 (Safe Method)"
slug: how-to-update-bios-on-laptop-on-windows-11
date: 2026-09-19
categories: ["drivers"]
tags: ["bios update", "uefi firmware", "windows 11", "firmware update", "laptop bios"]
description: "A safe, step-by-step method to update your laptop's BIOS on Windows 11: preparation, the right update package, and what to do if something goes wrong."
thumbnail: "/images/thumbs/how-to-update-bios-on-laptop-on-windows-11.webp"
faqs:
  - q: "Is it safe to update the BIOS from inside Windows 11?"
    a: "Yes, when you use the manufacturer's official updater. Modern BIOS updates run through a staged process: the Windows utility verifies the image and hands it to the firmware capsule updater, which applies it during reboot. The risky era of DOS boot disks is over — just keep the charger connected and don't interrupt the process."
  - q: "Will a BIOS update delete my files or Windows installation?"
    a: "No. A BIOS update only rewrites the firmware chip on the motherboard; your SSD, Windows installation, apps, and files are untouched. That said, always back up important data before any firmware work — not because the update targets your files, but because any low-level operation deserves a safety net."
  - q: "How long does a laptop BIOS update take?"
    a: "Typically 5 to 15 minutes total, including the reboot and firmware flashing stage. The on-screen progress bar may sit at one percentage for several minutes — that's normal. If it exceeds 30 minutes with no change, leave it alone for another 15 before considering recovery steps; interrupting a flash is the main way updates go wrong."
  - q: "Should I update the BIOS if everything works fine?"
    a: "Not necessarily. The old technician's rule — 'if it ain't broke, don't flash it' — still has merit. Update when the changelog mentions your issue (thermal behavior, battery charging, new CPU support, security fixes like microcode patches) or when support asks you to. Skipping a BIOS version you don't need is perfectly fine."
---

A BIOS (or UEFI firmware) update is the one software update that touches hardware directly. Done right, it fixes battery quirks, fan behavior, sleep issues, and security vulnerabilities that no Windows patch can reach. Done carelessly — interrupted mid-flash on battery power — it can leave a laptop unbootable. That contrast is why BIOS updates deserve their own careful procedure rather than being treated like any other download.

This guide covers the safe method: identifying your current BIOS version, getting the correct package from your manufacturer, preparing the laptop, and running the update on Windows 11. If you're on the older OS, see our [Windows 10 BIOS update guide](/articles/how-to-update-bios-on-laptop-on-windows-10/). For context on why firmware matters to power behavior, our article on [battery issues after BIOS updates](/articles/how-to-reset-acpi-battery-driver-on-windows-11/) is worth a read too.

## Why this happens

- **Manufacturers release BIOS updates to fix real defects.** Fan curves, battery charge limits, thermal throttling, and sleep/wake bugs are often firmware problems, not Windows problems.
- **New hardware needs new firmware.** CPU microcode updates and support for newer SSDs or RAM arrive through BIOS updates.
- **Security vulnerabilities live in firmware.** Issues like microcode flaws and Secure Boot bypasses are patched at the BIOS level.
- **Windows 11 has stricter firmware requirements.** TPM 2.0 and Secure Boot enforcement mean firmware health matters more than it did on Windows 10.
- **Skipped updates compound.** Jumping several versions at once sometimes requires an intermediate update first — the changelog will say so.
- **Wrong-package flashes are the main danger.** Installing a BIOS meant for a different model or region is the most common cause of a failed flash.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your current BIOS version and model

Never download a BIOS update until you know exactly what you have and what machine it's for.

1. Press **Win + R**, type `msinfo32`, and press Enter.
2. Note the **System Model**, **BIOS Version/Date**, and **BIOS Mode** (should be UEFI).
3. Also note whether you're on Windows 11 Home or Pro — some updaters differ by edition.
4. Write the version down; you'll compare it against the manufacturer's latest to see if an update is even needed.

If your installed version already matches the latest on the support site, stop here — there's nothing to gain. This single check prevents the most common mistake in BIOS updating: flashing a version you already have, or one meant for a sibling model.

### Fix 2: Download the update from the manufacturer only

BIOS images must come from exactly one place: your laptop maker's official support site.

1. Go to your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model or serial number.
2. Find the **BIOS** or **Firmware** section and read the changelog for the newest version.
3. Confirm the version is newer than yours and that the notes mention your issue or a security fix.
4. Download the **Windows-based updater** (usually a `.exe`), not the DOS or USB variant, unless the instructions say otherwise.

Never use BIOS files from forums, driver aggregator sites, or a "similar" model. A mismatched image is the fastest route to a bricked board, and no forum download is worth that risk.

### Fix 3: Prepare the laptop — power, peripherals, and backup

Preparation is what separates safe updates from horror stories. Every item here exists because someone skipped it.

1. Connect the AC adapter and confirm the battery is above 50% — most updaters refuse to run otherwise, and that's a feature, not a bug.
2. Disconnect all peripherals: docks, external drives, USB hubs, SD cards. Leave only the charger.
3. Close all applications and temporarily disable third-party antivirus real-time protection.
4. Back up critical files — the update won't touch them, but firmware work deserves a safety net.
5. If BitLocker is enabled, make sure you have the recovery key accessible on another device; rare firmware changes can trigger a BitLocker prompt on next boot.

BitLocker deserves emphasis: a changed firmware measurement can make Windows ask for the recovery key at boot. Having the 48-digit key ready turns a panic into a 30-second detour.

### Fix 4: Run the update and let it finish undisturbed

With preparation done, the actual flash is straightforward — the discipline is in not touching anything.

1. Right-click the downloaded updater and choose **Run as administrator**.
2. Read the on-screen warnings, confirm the target version, and start the update.
3. The laptop will reboot into the firmware updater — the screen may go black, show a progress bar, or reboot several times.
4. Do not press the power button, close the lid, or unplug the charger for any reason until Windows is fully back at the desktop.

The progress bar lying at 0% or 99% for minutes is normal. Fans may spin loudly during the flash. Both are expected. The only action required from you is patience — plan for 15 uninterruptible minutes.

### Fix 5: Verify the update and re-check settings

A successful flash isn't quite the finish line — confirm it and clean up after it.

1. Reopen `msinfo32` and confirm the BIOS version now matches the downloaded release.
2. Enter BIOS setup once and check that your settings (boot order, virtualization, Secure Boot) survived — some updates reset to defaults.
3. Re-enable any antivirus protection you disabled.
4. If BitLocker prompted for a key, it should now boot normally; consider suspending and re-enabling BitLocker protection to re-seal to the new firmware measurements.

If settings were reset, restore them deliberately rather than from memory — a wrong Secure Boot or SATA mode change can cause its own boot failure, and you'd rather not stack problems.

### Fix 6: Recover if the update is interrupted

If the worst happened — power loss mid-flash, or the laptop now won't POST — don't panic; manufacturers built recovery paths for exactly this.

1. First, try a hard reset: hold the power button 30 seconds, disconnect everything, then try booting once more.
2. Check your manufacturer's crisis recovery method: many laptops support **BIOS recovery via USB** (e.g., holding **Win + B** or **Fn + Esc** while powering on with a recovery USB inserted).
3. Download the BIOS recovery image from the manufacturer's site using another computer and follow their exact key combination.
4. If recovery mode doesn't engage, the board needs professional service — describe exactly what happened and when, since "interrupted flash" is a known, serviceable fault.

Modern laptops with dual BIOS chips or USB recovery recover from interrupted flashes far more often than older machines. The key is using the manufacturer's documented recovery procedure rather than improvising.

### Fix 7: Decide when the next update is warranted

Post-update, set a sane policy for yourself so firmware maintenance stays boring.

1. Check for BIOS updates quarterly, or when troubleshooting an issue the changelog addresses.
2. Subscribe to your manufacturer's support notifications for your model if available.
3. Skip versions whose changelogs don't mention your hardware or a security fix — fewer flashes mean fewer chances for something to go wrong.
4. Keep a local copy of the last known-good BIOS installer; if a future update misbehaves, some vendors allow downgrading.

## Closing

BIOS updates on Windows 11 are safe when they're boring: right package, full power, no interruptions, verified afterward. The drama in BIOS horror stories almost always traces back to a skipped preparation step — wrong file, dead battery, or an impatient power button. Follow the sequence above and a firmware update becomes what it should be: fifteen quiet minutes that leave your laptop measurably better.
