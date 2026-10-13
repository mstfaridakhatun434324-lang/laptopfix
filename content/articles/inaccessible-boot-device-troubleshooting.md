---
title: "Inaccessible Boot Device: Step-by-Step Troubleshooting Guide"
slug: inaccessible-boot-device-troubleshooting
date: 2026-09-15
categories: ["windows-errors"]
tags: ["inaccessible boot device", "boot error", "troubleshooting", "windows 11"]
description: "A methodical troubleshooting walkthrough for INACCESSIBLE_BOOT_DEVICE — check BIOS settings, rebuild boot data, roll back updates, and test the drive."
thumbnail: "/images/thumbs/inaccessible-boot-device-troubleshooting.webp"
faqs:
  - q: "What is the first thing to check for Inaccessible Boot Device?"
    a: "The BIOS storage mode. Enter the BIOS (F2 or Del at boot), find the SATA Operation or Storage Controller setting, and check whether it's AHCI or RAID. It must match the mode Windows was installed with. A BIOS update or reset flipping this setting is the single most common cause, and switching it back fixes the boot immediately."
  - q: "Can I troubleshoot this without installation media?"
    a: "Yes. Interrupting boot three times at the Windows logo forces the Automatic Repair screen, giving you access to Startup Repair, Command Prompt, and Uninstall Updates without any USB media. Installation media is only needed if the recovery environment itself won't load or if you want to run Startup Repair from external media."
  - q: "How do I know if the drive is actually dead?"
    a: "Check whether the BIOS lists the drive at all — a missing drive suggests hardware failure or a loose connection. Then run the manufacturer's diagnostics (F12 and Diagnostics on Dell, F2 on HP) and the full drive test. Failing tests mean replacement. A drive that passes but still won't boot points to software: BCD or update damage."
  - q: "Will rebuilding the BCD delete my files?"
    a: "No. The Boot Configuration Data store only describes how Windows starts — rebuilding it with bootrec or bcdboot doesn't touch user files, installed programs, or settings. It's one of the safest repairs in Windows troubleshooting, which is why it's recommended before any drastic measures."
---

Troubleshooting INACCESSIBLE_BOOT_DEVICE works best as a process of elimination. The error means Windows can't read its boot drive, and the possible reasons form a short list: the BIOS is speaking the wrong storage language (AHCI vs. RAID), the boot data is damaged, a recent update broke the boot chain, or the drive itself is failing. Each has a distinct test, and the order matters — you check the cheap, common causes before the expensive, rare ones.

This guide is the methodical companion to our broader [Inaccessible Boot Device fix guide](/articles/best-way-to-fix-inaccessible-boot-device/): same problem, structured as a diagnostic flowchart you can work through top to bottom. You'll need access to the BIOS and the Windows recovery environment; a Windows installation USB is helpful but optional. If Windows boots but then freezes instead of blue-screening, our [restart screen troubleshooting](/articles/windows-11-stuck-on-restarting-screen-fix/) covers that branch, and our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) shows how to get a working foothold when normal boot fails.

## Why this happens

- **BIOS storage mode mismatch**: The SATA controller mode (AHCI/RAID/IDE) doesn't match what Windows was installed with.
- **Corrupt BCD store**: Boot Configuration Data damage means the bootloader can't find Windows.
- **Broken boot files**: The EFI partition's boot files damaged by updates, disk errors, or failed dual-boot experiments.
- **Bad storage driver**: A corrupted or incompatible disk controller driver breaking the OS-to-drive handoff.
- **Failed update**: A Windows or driver update that damaged the boot chain mid-install.
- **Failing drive**: Hardware-level read failures on boot-critical sectors.
- **Changed boot configuration**: Drive moved, boot order altered, or UEFI/Legacy mode switched after installation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the drive is visible in BIOS

Confirm the hardware exists before troubleshooting software.

1. Restart and enter the BIOS/UEFI (**F2**, **Del**, or **Esc** depending on brand — watch the boot splash).
2. Look at the boot priority list or storage information page: is your SSD/HDD listed?
3. If the drive is missing: power off, and if it's a removable 2.5" drive, reseat it; for NVMe drives, reseat the M.2 stick. A drive that never appears is likely dead — proceed to Fix 7.
4. If the drive appears, note its exact name and continue — the hardware is fine and the problem is configuration or software.

### Fix 2: Match the BIOS storage mode to the installation

The most common single cause, and the quickest fix.

1. In the BIOS, find **SATA Operation**, **SATA Mode**, **Storage Controller**, or **VMD Controller** (location varies: Advanced, Storage, or System Configuration tabs).
2. If it's set to **RAID On** / **Intel RST**, try **AHCI**; if it's **AHCI**, try **RAID On**. Save and boot after each change.
3. Whichever setting boots Windows is the correct one — leave it there permanently.
4. Also verify **Boot Mode** is **UEFI** (not Legacy/CSM) and **Secure Boot** matches its previous state; both affect whether the bootloader loads.

### Fix 3: Enter recovery and try Startup Repair

Let the automated tool attempt the straightforward repairs.

1. If Windows won't boot, force recovery: power off during the Windows logo three times in a row, then choose **Advanced options**.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Repair** and let it run to completion.
3. Startup Repair fixes common bootloader issues automatically — if it succeeds, boot normally and skip ahead to Fix 6 to prevent recurrence.
4. If it reports it couldn't repair, continue — the manual steps below succeed where the automated tool fails.

### Fix 4: Rebuild the BCD from the Command Prompt

The definitive software repair for boot data damage.

1. From recovery, open **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run, in order: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /scanos`, `bootrec /rebuildbcd`.
3. If `rebuildbcd` finds zero installations, do the manual EFI rebuild: `diskpart` > `list vol` > identify the FAT32 EFI partition > `select vol N` > `assign letter=Z:` > `exit` > `bcdboot C:\Windows /s Z: /f UEFI`.
4. Confirm the Windows drive letter first with `dir C:` — in the recovery environment it often appears as D: or E:.
5. Type `exit`, select **Continue**, and test the boot.

### Fix 5: Uninstall the triggering update

When the timeline points at an update, reverse it.

1. In recovery, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Remove the **latest quality update** first; test; then the **latest feature update** if needed.
3. After booting successfully, pause updates and research the KB on [Microsoft's support site](https://support.microsoft.com/en-us/windows) before allowing it again.
4. If a driver update was the trigger, boot into Safe Mode afterward and roll back that driver in Device Manager.

### Fix 6: Verify with chkdsk and update storage drivers

Make sure the drive is healthy and the driver stack is correct.

1. From the recovery Command Prompt, run `chkdsk C: /f /r` (adjusted drive letter) and let the full scan finish.
2. Once booted into Windows, open **Device Manager** > **Storage controllers** and confirm the controller driver is the correct one for your BIOS mode (Intel RST driver for RAID mode, standard AHCI driver for AHCI mode).
3. Download the latest chipset/storage driver from your laptop manufacturer's support page and install it.
4. Create fresh installation media with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) while things work — you'll want it handy if this ever recurs.

### Fix 7: Run full hardware diagnostics

When every software avenue is exhausted, trust the hardware tests.

1. Boot the built-in diagnostics: **F12** > **Diagnostics** (Dell), **F2** > **Component Tests** > **Hard Drive** (HP), **F10** > **Diagnostics** (Lenovo).
2. Run the extended/long drive test, not just the quick one.
3. A failing drive: back up immediately via a USB adapter on another PC or a Linux live USB, replace the drive, reinstall Windows, restore files.
4. A passing drive with an unfixable boot: the partition table may be damaged beyond bootrec's reach — back up what you can from recovery Command Prompt (`xcopy` to USB) and clean-install.

## Closing

The troubleshooting discipline for INACCESSIBLE_BOOT_DEVICE is elimination in cost order: BIOS visibility, BIOS mode, automated repair, manual BCD rebuild, update rollback, disk check, hardware diagnostics. Most cases resolve at step two or four — a flipped storage mode or a damaged BCD — which is why reinstalling Windows first is such an expensive mistake: it fixes neither a BIOS setting nor a dying drive, and costs you hours. Work the list, note which step fixed it, and you'll also know exactly what to check first if it ever happens again. For the variant where Windows boots but immediately crashes instead, our [main boot device guide](/articles/best-way-to-fix-inaccessible-boot-device/) covers the deeper repair paths.
