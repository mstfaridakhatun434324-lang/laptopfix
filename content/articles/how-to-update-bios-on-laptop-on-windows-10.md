---
title: "How to Update BIOS on a Laptop Running Windows 10 (Safe Method)"
slug: how-to-update-bios-on-laptop-on-windows-10
date: 2026-09-26
categories: ["drivers"]
tags: ["bios update", "uefi firmware", "windows 10", "firmware update", "laptop bios"]
description: "Safe BIOS updating on Windows 10 laptops: find the right firmware package, prepare the machine, flash without bricking it, and verify the result."
thumbnail: "/images/thumbs/how-to-update-bios-on-laptop-on-windows-10.webp"
faqs:
  - q: "Is updating the BIOS on Windows 10 different from Windows 11?"
    a: "The core process is identical — same manufacturer updater, same precautions. The differences are cosmetic: settings locations and the fact that Windows 10 machines are often older, so their updaters may be legacy-style utilities rather than modern capsule updates. The safety rules (AC power, no interruptions, correct package) apply equally to both."
  - q: "My laptop is old — should I still update its BIOS?"
    a: "Check the changelog first. For older laptops, BIOS updates usually address specific bugs or security issues like microcode vulnerabilities. If the changelog doesn't mention your problem and the machine runs fine, leaving it alone is reasonable. But don't skip a security-related firmware update just because the laptop is old."
  - q: "What happens if the power goes out during a BIOS update?"
    a: "An interrupted flash can corrupt the firmware and leave the laptop unable to boot — the classic 'bricked' state. This is why the AC adapter must be connected and the battery healthy. If it happens, many laptops have a crisis-recovery mode (USB BIOS recovery); otherwise the board needs professional reflashing."
  - q: "Can I downgrade the BIOS if the new version causes problems?"
    a: "Sometimes. Some manufacturers allow flashing an older version with the same utility; others block downgrades for security reasons. Check the manufacturer's documentation before updating — knowing whether rollback is possible changes the risk calculation. Keep the previous version's installer if downgrades are supported."
---

Windows 10 laptops are often a few years old now, which makes BIOS updates both more valuable and slightly more delicate. More valuable because years of firmware fixes have accumulated — thermal behavior, battery handling, and security microcode that your machine has never received. More delicate because older updaters are less forgiving, batteries are more worn, and the margin for a power interruption is thinner.

The procedure below is the safe path: verify what you have, get the exact package from the manufacturer, prepare the machine properly, and flash without drama. If you're on Windows 11 instead, our [Windows 11 BIOS guide](/articles/how-to-update-bios-on-laptop-on-windows-11/) covers the same ground with the newer OS's specifics. BIOS updates can also affect power behavior — see our [ACPI battery driver reset guide](/articles/how-to-reset-acpi-battery-driver-on-windows-11/) if charging acts strangely afterward.

## Why this happens

- **Years of firmware fixes have piled up.** An untouched 4-year-old laptop may be a dozen BIOS revisions behind, missing thermal, battery, and compatibility fixes.
- **Security microcode updates arrive via BIOS.** CPU vulnerability mitigations are delivered as firmware, not Windows patches.
- **Windows 10 updates can expose firmware bugs.** A Windows patch may depend on firmware behavior that only newer BIOS versions provide.
- **Battery and thermal behavior is firmware-controlled.** Charge limits, fan curves, and throttling live in the BIOS, not the OS.
- **Older updaters are less forgiving.** Legacy flash utilities may lack the verification and recovery features of modern capsule updates.
- **Skipped versions may need stepping stones.** Some vendors require sequential updates when jumping many versions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check your current BIOS version

Know your starting point before downloading anything.

1. Press **Win + R**, type `msinfo32`, and press Enter.
2. Record the **System Model** and **BIOS Version/Date** exactly as shown.
3. Note your Windows 10 version too (**Settings > System > About**) — some updaters are version-specific.
4. Compare against the manufacturer's support site to see whether an update actually exists for your model.

If you're already on the latest, stop. Flashing the same version again gains nothing and carries the (small) risk of any flash operation. This check takes a minute and prevents the most pointless BIOS updates.

### Fix 2: Get the correct package from the manufacturer

On older laptops, getting the exact right file matters even more — model variants proliferate.

1. Go to your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and enter your serial number or exact model.
2. Open the BIOS/firmware section and read the changelog for the latest version.
3. Check for prerequisites: some updates require a minimum EC version or a previous BIOS as a stepping stone.
4. Download the Windows executable updater; avoid DOS/USB variants unless the instructions specify them.

Serial-number lookup beats model-name lookup on older machines, where one model name covered multiple board revisions. The support site's auto-detect tool, where available, removes the guesswork entirely.

### Fix 3: Prepare the machine thoroughly

Older batteries and older updaters demand stricter preparation.

1. Connect the AC adapter and verify the battery charges — if the battery is dead or removed, some updaters refuse to run, which is protecting you.
2. Confirm the battery is above 50% and the adapter is the original wattage; underpowered adapters can cause brownouts during flashing.
3. Disconnect all peripherals: docks, USB drives, printers, SD cards.
4. Close all programs, disable third-party antivirus temporarily, and back up important files.
5. If BitLocker is on, have the recovery key ready on another device.

On aging laptops, also verify the cooling: blow out dust from vents before the update. A flash operation with fans screaming from dust-clogged heatsinks is an avoidable stress — and thermal shutdown mid-flash is exactly the disaster we're preventing.

### Fix 4: Run the flash with zero interruptions

The update itself is simple; the discipline is everything.

1. Right-click the updater and choose **Run as administrator**.
2. Confirm the current and target versions shown by the utility match your expectations.
3. Start the update and do not touch the laptop: no lid closing, no power button, no unplugging.
4. Expect reboots, black screens, and long pauses on progress percentages — all normal.

Budget 20 uninterrupted minutes for older machines; their flash chips are slower. Put the laptop somewhere it won't be bumped, tell anyone nearby not to touch it, and walk away. The most dangerous moment in any BIOS update is a human deciding "it's stuck" at 90% and holding the power button.

### Fix 5: Verify and restore settings afterward

Older BIOS updates are more likely to reset settings to defaults — check everything.

1. Reopen `msinfo32` in Windows and confirm the new BIOS version.
2. Enter BIOS setup and review: boot order, SATA mode, virtualization, Secure Boot, and any custom fan or power settings.
3. Restore your previous settings carefully — photograph them beforehand if you customized heavily.
4. Re-enable antivirus and confirm BitLocker is happy (provide the recovery key if prompted once).

The settings reset is the most common post-update surprise on older laptops. A changed SATA mode (AHCI vs. RAID/IDE) can cause a boot failure that looks like a bricked flash but is just a setting — knowing to check saves a panic.

### Fix 6: Use crisis recovery if the flash fails

If the laptop won't POST after the update, manufacturers' recovery modes are the next step.

1. Perform a hard reset: hold power 30 seconds with everything disconnected, then try once more.
2. Look up your model's **BIOS recovery** procedure — common methods include holding **Win + B**, **Fn + B**, or **Fn + Esc** while powering on with a FAT32 USB containing the recovery image.
3. Prepare the recovery USB on another computer following the manufacturer's exact file naming and placement instructions.
4. If recovery mode won't engage, the flash chip needs professional reprogramming — take it to service with a clear description of what happened.

Older laptops vary wildly in recovery support: business lines (ThinkPad, Latitude, EliteBook) usually have robust crisis recovery; budget consumer models sometimes have none. Knowing your model's capability before you flash is part of informed risk-taking.

### Fix 7: Set a maintenance rhythm for firmware

Make future updates uneventful by planning them.

1. Check for BIOS updates twice a year, or when the changelog addresses something you experience.
2. Read changelogs skeptically: "improves system stability" without specifics is a weak reason to flash an old stable machine.
3. Prioritize updates mentioning security (microcode, Secure Boot) over feature tweaks.
4. Archive each installer you use — if downgrades are allowed, the previous version is your escape hatch.

## Closing

Updating the BIOS on a Windows 10 laptop rewards the same virtues as any firmware work: the right file, full power, patience, and verification. Older machines add one more: respect for worn batteries and legacy updaters. Follow the sequence, and a years-overdue firmware update becomes a quiet maintenance win instead of a story you tell with a wince.
