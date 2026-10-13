---
title: "Windows 11 Boot Loop on Dell Laptops: Fixed"
slug: fix-windows-11-boot-loop-on-dell-laptop
date: 2026-09-01
categories: ["windows-errors"]
tags: ["boot loop", "dell laptop", "windows 11", "startup repair"]
description: "Dell laptop stuck restarting on Windows 11? Dell-specific fixes — from SupportAssist OS Recovery to BIOS settings — that break the loop."
thumbnail: "/images/thumbs/fix-windows-11-boot-loop-on-dell-laptop.webp"
faqs:
  - q: "Why is my Dell laptop stuck in a boot loop on Windows 11?"
    a: "The most common Dell-specific causes: a Windows update that broke boot files, corrupt Boot Configuration Data, a BIOS storage mode flipped by a firmware update, or a failing drive. Dell laptops also ship with SupportAssist OS Recovery, a built-in recovery partition that can repair or reset the system without installation media."
  - q: "Will I lose my files fixing a Dell boot loop?"
    a: "Not with the repair steps below. Rebuilding the BCD, uninstalling updates, running Startup Repair, and using SupportAssist's repair options all preserve personal files. Only a full factory reset or 'Remove everything' reset deletes data — those are last resorts, clearly marked as such."
  - q: "How do I access recovery options on a Dell laptop?"
    a: "Interrupt the boot three times (hold the power button during the Dell logo) to reach the Windows Recovery Environment, or press F12 during the logo for the boot menu, which includes diagnostics and recovery options. Newer Dell laptops also offer SupportAssist OS Recovery, launched from the F12 menu or automatically after repeated boot failures."
  - q: "What if my Dell laptop boot-loops even in Safe Mode?"
    a: "If Safe Mode fails too, the problem is in boot files, the storage driver, or hardware — not a startup program. Work from the recovery environment: rebuild the BCD, uninstall recent updates, check the BIOS storage mode, and run Dell's built-in hardware diagnostics (F12 > Diagnostics) to rule out a failing drive."
---

A **boot loop** on a Dell laptop — Dell logo, spinning dots, restart, Dell logo, spinning dots, forever — is one of the most common Windows 11 failures we see, and Dell machines have both unique causes and unique tools. The unique causes: Dell BIOS updates that flip the SATA operation mode, and Dell's own driver packages conflicting after Windows Update replaces them. The unique tool: **SupportAssist OS Recovery**, a recovery environment baked into most modern Dell laptops that can repair Windows without you creating installation media.

Before anything else, note where the loop breaks. Logo → black screen → logo (never reaching Windows) points at boot files or BIOS settings. Logo → "Preparing Automatic Repair" → restart points at Windows boot corruption. Either way, your files are almost certainly intact — this is a boot problem, not a data problem. For the general startup-crash angle, see [BSOD on startup for Dell laptops](/articles/how-to-fix-bsod-on-startup-windows-11-on-dell-laptop/); for the automatic-repair variant, [automatic repair loop on Dell](/articles/how-to-fix-automatic-repair-loop-windows-11-on-dell-laptop/).

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: The most common cause — damaged boot entries restart the boot attempt endlessly.
- **Dell BIOS update flipped SATA mode**: Firmware updates sometimes change SATA Operation between RAID and AHCI, breaking the storage driver handoff.
- **Failed Windows update**: Updates modify boot files; an interrupted update leaves the boot chain broken.
- **Failing drive**: Bad sectors on boot-critical files cause identical failures every boot.
- **Corrupt system files**: Damage to `winload.efi` or early-boot drivers.
- **Fast Startup corruption**: Hybrid shutdown state breaking every "fast" boot identically.
- **Recent driver installation**: A bad storage or chipset driver installed just before the loop began.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Dell's built-in hardware diagnostics

Rule out a dying drive in five minutes before touching software.

1. Power off the laptop completely.
2. Power on and immediately tap **F12** repeatedly to open the **Boot Menu**.
3. Select **Diagnostics** and let the full scan run (10–20 minutes).
4. If any component fails — especially the hard drive/SSD — stop here: the loop is a hardware symptom. Back up via another PC if possible and replace the drive. If all tests pass, continue with software fixes.

### Fix 2: Check SATA Operation mode in BIOS

The classic Dell-specific cause.

1. Power on and tap **F2** repeatedly to enter **BIOS Setup**.
2. Go to **System Setup** > **SATA/NVMe Operation** (location varies by model).
3. If it's set to **RAID On** and you never chose that, change it to **AHCI**. If you changed it recently and the loop started after, change it back.
4. Click **Apply**, **Exit**, and boot. A wrong SATA mode produces exactly this endless loop, and this one setting fixes it instantly.

### Fix 3: Break into WinRE and try Startup Repair

Use the recovery environment you're landing in.

1. Interrupt boot three times (hold power during the Dell logo) to reach **Automatic Repair** > **Advanced options**, or boot from the F12 menu.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Repair** and let it run.
3. If it reports it couldn't repair, don't stop — the manual fixes below succeed where the automatic tool fails.
4. From **Advanced options**, also try **Startup Settings** > **Restart** > press **4** for Safe Mode. If Safe Mode boots, skip to Fix 6.

### Fix 4: Rebuild the BCD from Command Prompt

The core fix for most boot loops.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run in order: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /scanos`, `bootrec /rebuildbcd`.
3. If `rebuildbcd` finds zero installations, do it manually: `diskpart` > `list vol`, note the FAT32 EFI partition number and the Windows drive letter (often **D:** here), then `select vol N` > `assign letter=Z:` > `exit` > `bcdboot D:\Windows /s Z: /f UEFI`.
4. Type `exit`, choose **Continue**, and boot.

### Fix 5: Uninstall the latest update and disable Fast Startup

For loops that began within a day or two of an update.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Uninstall Updates** > **Uninstall the latest quality update**, then restart and test.
2. If still looping, go back and uninstall the latest **feature** update.
3. Once booted, open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable** and **uncheck Turn on fast startup**.
4. Pause updates (**Settings** > **Windows Update** > **Pause updates**) and check [Dell's support site](https://www.dell.com/support) for your model's driver updates before unpausing.

### Fix 6: Clean-boot to find the offending startup item

For loops that reach the login screen or desktop before restarting.

1. If you can reach Safe Mode or the desktop briefly, press **Win + R**, type `msconfig`, press Enter.
2. **Services** tab > tick **Hide all Microsoft services** > **Disable all**. **Startup** tab > open Task Manager > disable all startup items.
3. Restart normally. If the loop stops, re-enable in halves to find the culprit — Dell bloatware updaters and third-party "optimizers" are frequent offenders.
4. Uninstall the offending program from [Dell support guidance](https://www.dell.com/support) or **Settings** > **Apps**, then re-enable everything else.

### Fix 7: Use SupportAssist OS Recovery

Dell's built-in recovery when nothing else works.

1. Power on and tap **F12**, then select **SupportAssist OS Recovery** (or let repeated failures launch it automatically).
2. Choose **Repair** first — it attempts automated fixes while preserving files.
3. If repair fails, the tool offers a **Reset** with file-preservation options, and as a last resort a factory reset.
4. Only choose factory reset after backing up: remove the drive and copy files via another PC, or use the recovery environment's backup option if offered.

## Closing

Dell boot loops are very fixable because the causes are so consistent: SATA mode, BCD corruption, or a bad update, in that order. The F12 diagnostics plus the SATA mode check resolve a remarkable number of cases in under half an hour. If you've worked the full list and the loop persists with a healthy drive, SupportAssist's reset (keeping files) is the clean ending — and then update the BIOS and drivers from Dell's site before letting Windows Update run wild again.
