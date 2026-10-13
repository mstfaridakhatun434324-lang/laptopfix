---
title: "INACCESSIBLE_BOOT_DEVICE on Windows 11: The Full Fix"
slug: inaccessible-boot-device-bsod-windows-11
date: 2026-10-10
categories: ["windows-errors"]
tags: ["inaccessible boot device", "bsod", "boot error", "windows 11"]
description: "INACCESSIBLE_BOOT_DEVICE means Windows can't reach its drive. Fix it from BIOS settings to BCD rebuilds — full guide."
thumbnail: "/images/thumbs/inaccessible-boot-device-bsod-windows-11.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "It means Windows started booting but lost access to the system drive partway through, so it cannot load the rest of the operating system. Common triggers: the BIOS storage mode changed between AHCI and RAID, a Windows update replaced the storage driver, the boot configuration data is corrupt, or the drive itself is failing."
  - q: "Will I lose my files fixing INACCESSIBLE_BOOT_DEVICE?"
    a: "No. Every fix below repairs boot configuration, drivers, or BIOS settings — none of them touch your personal files. Your data is still on the drive; Windows just can't reach it right now. Only a clean Windows reinstall would erase files, and that's not on this fix list."
  - q: "Why did INACCESSIBLE_BOOT_DEVICE appear after a Windows update?"
    a: "Feature updates sometimes replace your storage controller driver with a generic one that can't talk to your drive's configuration, or they reset BIOS-adjacent settings. Rolling back the update from the recovery environment, or reinstalling the manufacturer's storage driver, restores access. This is one of the most common post-update blue screens."
  - q: "Can a dead SSD cause INACCESSIBLE_BOOT_DEVICE?"
    a: "Yes. If the drive has failed electronically, Windows can't access it at any stage. Check whether the BIOS still lists the drive: if the BIOS doesn't see it either, the drive is dead or disconnected and needs reseating or replacement. If the BIOS sees it but Windows doesn't boot, the problem is drivers or boot configuration, not the drive."
---

**INACCESSIBLE_BOOT_DEVICE** (stop code **0x0000007B**) means Windows began loading, then lost contact with the drive holding the operating system. It's distinct from "no boot device" errors — your drive is present, but somewhere between the BIOS handoff and the Windows storage driver loading, access breaks. The usual suspects: a BIOS storage mode flipped between AHCI and RAID, a Windows update that swapped your storage driver, corrupt Boot Configuration Data, or a drive that's dying.

The single most useful diagnostic takes thirty seconds: enter the BIOS and check whether your drive is listed. **Drive visible in BIOS** = a software problem (drivers, BCD, updates) — very fixable. **Drive missing in BIOS** = hardware (dead drive, loose connection) — reseat or replace. Everything below assumes the drive is visible; if it isn't, skip straight to Fix 7.

You'll do most of this work from the Windows Recovery Environment (WinRE), which you reach by interrupting boot three times or via installation media. For the loop variant of this problem, see [automatic repair loop on Dell laptops](/articles/how-to-fix-automatic-repair-loop-windows-11-on-dell-laptop/); for the related startup failure, [Srttrail.txt blue screen errors](/articles/how-to-fix-srttrail-txt-blue-screen-error-in-windows-11-24h2/) covers the next step when boot files are involved.

## Why this happens

- **BIOS storage mode changed**: A BIOS update or reset flipping between RAID/Intel RST and AHCI is the classic cause — Windows loads the wrong storage driver and can't see the drive.
- **Windows update replaced the storage driver**: Feature updates install generic storage drivers that don't match RAID or custom configurations.
- **Corrupt Boot Configuration Data (BCD)**: Damaged boot entries point Windows at the wrong device or partition.
- **Failing SSD or hard drive**: A drive dropping in and out of visibility breaks access mid-boot.
- **Recently changed drive configuration**: Cloning to a new SSD, adding a drive, or repartitioning without updating boot entries.
- **Corrupt system files in the boot path**: Damage to `winload.efi`, the storage driver, or related components.
- **BitLocker complications**: Encryption metadata issues after hardware or firmware changes can block access.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the BIOS storage mode (AHCI vs RAID)

The fastest fix — a one-setting change.

1. Restart and enter **BIOS/UEFI** (**F2**, **Del**, or **Esc** at the manufacturer's logo).
2. Find **SATA Mode**, **Storage Configuration**, or **SATA Operation** (usually under Advanced or Main).
3. Note the current setting. If it's **RAID** or **Intel RST Premium** and you didn't set it that way, change it to **AHCI**. If it's AHCI and the problem started after you changed it, switch it back.
4. Save and exit. If Windows boots, that was the entire problem — a BIOS update or reset had flipped the mode.

### Fix 2: Boot into Safe Mode to load minimal drivers

Safe Mode can succeed where normal boot fails, giving you a working system to repair from.

1. From the blue screen, or by interrupting boot three times, reach **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **4** for Safe Mode. If Windows loads, the core system is intact — the problem is a normal-mode storage driver.
3. In Safe Mode, open **Device Manager**, expand **Storage controllers**, and update or roll back the storage driver.
4. Restart normally. If it still fails, continue — but you've confirmed Windows itself is healthy.

### Fix 3: Uninstall the latest Windows update from recovery

For crashes that started within days of an update.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first, restart, and test.
3. If it still fails, return and **Uninstall the latest feature update**.
4. Once booted, pause updates (**Settings** > **Windows Update** > **Pause updates**) and check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known issues with the update before reinstalling it.

### Fix 4: Rebuild the Boot Configuration Data

Repairs the boot entries Windows uses to find its drive.

1. In WinRE, open **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run these commands in order:
   - `bootrec /fixmbr`
   - `bootrec /fixboot` (if "Access denied," use the bcdboot method below instead)
   - `bootrec /scanos`
   - `bootrec /rebuildbcd`
3. If scanos finds no installations, rebuild manually:
   - `diskpart`, then `list vol` — identify the FAT32 EFI partition and your Windows partition's letter (often **D:** in recovery)
   - `select vol N` (the EFI volume), `assign letter=Z:`, `exit`
   - `bcdboot D:\Windows /s Z: /f UEFI` (use your actual Windows letter)
4. Type `exit`, choose **Continue**, and boot.

### Fix 5: Run Startup Repair and offline SFC

Let Windows attempt its own repair, then verify system files.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Startup Repair** and let it run. It fixes common boot file issues automatically.
2. If it fails, open **Command Prompt** and run offline SFC: `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` (replace **D:** with your Windows drive letter in recovery — verify with `diskpart` > `list vol`).
3. Then run `chkdsk D: /f /r` to repair filesystem damage on the Windows partition.
4. Exit and choose **Continue** to boot.

### Fix 6: Inject the correct storage driver from recovery

When Windows has the wrong storage driver and can't load the right one itself.

1. On another computer, download the storage/IRST/chipset driver for your exact laptop model from [Dell](https://www.dell.com/support) (HP and Lenovo host equivalent drivers on their support sites). Extract it to a USB drive.
2. Boot the problem laptop to WinRE > **Command Prompt**. Plug in the USB.
3. Use `dism /image:D:\ /add-driver /driver:E:\drivers /recurse` (adjust **D:** = Windows partition, **E:** = USB drive) to inject the driver into the offline Windows image.
4. Restart. With the correct storage driver present, Windows can reach the drive again.

### Fix 7: Reseat or replace the drive (BIOS doesn't see it)

The hardware path — only if the BIOS drive list is empty.

1. Power off completely, unplug, and (if the battery is removable) remove it. Hold the power button 15 seconds to drain residual charge.
2. Open the bottom panel, locate the SSD/HDD, remove it, and firmly reseat it in its slot. For 2.5" drives, check both the SATA and power connections.
3. Boot to BIOS and check the drive list again. If it appears now, the connection was loose — boot normally.
4. If it's still missing, the drive has failed. Replace it and reinstall Windows from the ISO at Microsoft's official download page, restoring your files from backup.

## Closing

INACCESSIBLE_BOOT_DEVICE is almost always a configuration problem, not a dead drive — the BIOS storage mode flip alone accounts for a huge share of cases, and the BCD rebuild handles most of the rest. Work the list in order and you'll know within an hour whether you're dealing with a setting, a driver, or hardware. If the drive is visible in BIOS throughout, your files are intact and one of the software fixes above will bring Windows back.
