---
title: "INACCESSIBLE_BOOT_DEVICE in Windows 11 24H2: Get Your Laptop Booting"
slug: how-to-fix-inaccessible-boot-device-in-windows-11-24h2
date: 2026-10-03
categories: ["windows-errors"]
tags: ["bsod", "stop code", "24h2", "boot", "ssd"]
description: "INACCESSIBLE_BOOT_DEVICE blue screen on Windows 11 24H2? Windows lost contact with your drive. Here's how to get it booting again."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-in-windows-11-24h2.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "Windows started loading but then lost access to the drive holding your system — usually because the storage driver it needs isn't loading, the BIOS storage mode changed, or the drive itself is failing. It's a boot-chain problem, not a Windows-is-gone problem."
  - q: "Did the 24H2 update cause this?"
    a: "Very often, yes. 24H2 updates storage drivers and can conflict with BIOS SATA mode settings (AHCI vs RAID/Intel RST). If the crash appeared on the first reboot after updating to 24H2, the driver/BIOS mismatch is the prime suspect."
  - q: "Are my files gone?"
    a: "Almost certainly not. The data is still on the drive — Windows just can't reach it during boot. Once the storage driver or BIOS setting is corrected, everything is typically right where you left it."
  - q: "Could my SSD be dead?"
    a: "It's possible but not the most likely cause — check drivers and BIOS settings first. If the drive doesn't appear in BIOS at all, though, that's a hardware failure and the drive needs replacing."
---

`INACCESSIBLE_BOOT_DEVICE` is Windows saying "I started to boot, then the drive vanished." The operating system begins loading, reaches the point where it needs its storage driver to keep reading from the disk, and that driver isn't there or can't talk to the hardware. Boot dies right there, every time.

On 24H2 this crash has a signature cause: the update's storage drivers disagreeing with the BIOS SATA mode. That makes it very fixable — you just have to get the driver and the BIOS speaking the same language again. All the work happens in the recovery environment.

## Why this happens

- **24H2 replaced your storage driver**: The update installs its own NVMe/SATA drivers, which may not match what your BIOS expects — the classic post-update trigger.
- **BIOS SATA mode changed (AHCI vs RAID/RST)**: If the mode was flipped — by a BIOS update, a reset to defaults, or an accidental change — the installed driver no longer matches the controller mode.
- **Corrupt boot configuration (BCD)**: Damage to the boot files means Windows loads the wrong storage stack or fails to initialize it.
- **Failing SSD**: A drive developing bad blocks in critical areas can drop off the bus mid-boot. Progressive worsening over days points here.
- **Loose SSD connection**: On laptops with socketed M.2 drives, a slightly unseated drive causes intermittent "inaccessible" boots.
- **Disk encryption driver issues**: BitLocker or third-party encryption filter problems can block Windows from unlocking the boot volume.

## How to fix it

Work through these in order — BIOS and driver fixes first, hardware last.

### Fix 1: Enter WinRE and check if the drive is visible

First establish whether this is software or hardware.

1. Force the recovery environment: power off during the Windows logo three times; the fourth boot enters **Automatic Repair**. Or hold **Shift** + **Restart** from the login screen if you can reach it.
2. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Type `diskpart`, then `list disk`. If your SSD appears with its full size, the drive is alive — this is a driver/BIOS problem. If it's missing entirely, skip to Fix 7.
4. Type `exit` to leave diskpart (stay in the command prompt for the next fixes).

### Fix 2: Check and correct the BIOS SATA mode

The single most common 24H2-specific cause.

1. Restart and enter BIOS/UEFI (**F2** or **Del** at the manufacturer's splash screen).
2. Find storage settings — usually under **Advanced** > **SATA Configuration** or **Storage**.
3. Note the current mode: **AHCI**, **RAID**, or **Intel RST Premium**. The critical question is what it was *before* — if a BIOS update reset it, change it back.
4. Most laptops shipped in the last 5 years expect **AHCI** or **RAID/RST** depending on the OEM. If you're unsure, try the other mode — one of them will boot.
5. Save (**F10**) and restart. If Windows boots, you've found it. Don't forget which setting worked.

### Fix 3: Boot into Safe Mode to bypass the bad driver

Safe Mode uses minimal storage drivers, which is often enough to get in and fix the real one.

1. From **Advanced options** > **Startup Settings** > **Restart**, press **4** for Safe Mode.
2. If Safe Mode boots, the problem is the normal-mode storage driver, not the drive.
3. Open **Device Manager** (**Win + X**) > **Storage controllers** and **IDE ATA/ATAPI controllers**.
4. Right-click the storage controller > **Properties** > **Driver** tab > **Roll Back Driver** if available.
5. If rollback isn't available, note the driver version — you'll replace it in Fix 4.

The [post-update INACCESSIBLE_BOOT_DEVICE guide](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/) covers additional update-specific scenarios.

### Fix 4: Update or reinstall the storage driver

Get the storage driver that matches your hardware and BIOS mode.

1. In Safe Mode (or normal mode if Fix 2 worked), download the storage driver from your laptop manufacturer's support site for your exact model — look for "Intel Rapid Storage Technology," "AMD RAID," or chipset drivers.
2. Intel users can also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Install the driver, restart normally, and confirm the BIOS SATA mode (Fix 2) matches what the driver expects.
4. If you can't reach Safe Mode at all, you'll need another PC to download the driver, then load it during recovery via Command Prompt — or use the reset path in Fix 6.

### Fix 5: Rebuild the BCD from the recovery command prompt

A damaged boot configuration can prevent the storage stack from initializing.

1. From **Advanced options** > **Command Prompt**:
   - `bootrec /fixmbr`
   - `bootrec /fixboot`
   - `bootrec /scanos`
   - `bootrec /rebuildbcd`
2. Type **Y** if it finds your Windows installation.
3. For UEFI systems, also try: `bcdboot C:\Windows /s Z: /f UEFI` after assigning a letter to the EFI partition via `diskpart` (see the detailed EFI steps in related boot guides).
4. Type `exit`, choose **Continue**, and restart.

### Fix 6: Run SFC/DISM offline and uninstall the bad update

Corrupt system files or the 24H2 update itself may be the culprit.

1. From **Advanced options** > **Command Prompt**, find your Windows drive letter (`diskpart` > `list volume` > `exit` — often `D:` in WinRE).
2. Run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows`.
3. Then `DISM /Image:D:\ /Cleanup-Image /RestoreHealth`.
4. If the crash started with 24H2, go to **Advanced options** > **Uninstall Updates** > **Uninstall latest feature update** as well.
5. Restart and test.

If you can boot far enough to learn recovery basics, the [Safe Mode boot guide](/articles/how-to-boot-windows-11-in-safe-mode/) is a useful reference for all these steps.

### Fix 7: Check the physical drive

When software fixes fail, verify the hardware.

1. Enter BIOS and check whether the SSD is listed. Not listed = dead drive or dead slot.
2. If your laptop has a socketed M.2 drive and you're comfortable opening it: power off, unplug, remove the bottom panel, reseat the SSD firmly, and re-test.
3. From recovery command prompt, run `chkdsk D: /f /r` (your Windows drive letter) to map out bad sectors.
4. If the drive is failing, back up immediately — boot from a Linux USB if Windows won't start, copy your files to an external drive, then replace the SSD.
5. After replacing the drive, reinstall Windows from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and restore your files.

For ASUS laptops that land in a repair loop alongside this error, the [ASUS automatic repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-on-asus-laptop/) covers the overlapping recovery steps.

## Closing

`INACCESSIBLE_BOOT_DEVICE` looks like a dead laptop, but it's usually a disagreement between the storage driver and the BIOS — and disagreements can be resolved. Check the SATA mode, roll back or update the storage driver, rebuild the BCD, and in most cases Windows finds its drive again like nothing happened. Your files were never gone; Windows just temporarily forgot how to reach them.
