---
title: "INACCESSIBLE_BOOT_DEVICE: Step-by-Step Recovery Guide"
slug: how-to-fix-inaccessible-boot-device-step-by-step
date: 2026-09-20
categories: ["windows-errors"]
tags: ["blue screen", "boot", "windows 11"]
description: "Stuck on INACCESSIBLE_BOOT_DEVICE and Windows won't start? Follow this step-by-step recovery guide to repair the boot and get back to your desktop."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-step-by-step.webp"
faqs:
  - q: "What causes the INACCESSIBLE_BOOT_DEVICE error?"
    a: "Windows loses access to the system drive during boot — usually because a storage driver is wrong or missing, the SATA mode changed in BIOS, or a Windows update replaced the boot-critical driver. It can also come from disk corruption or a failing drive."
  - q: "Will fixing this delete my files?"
    a: "No. Boot repairs, driver rollbacks, and chkdsk all preserve your files. The only data risk is if the drive itself is physically failing — which is why checking drive health early and backing up matters."
  - q: "Can I fix this without reinstalling Windows?"
    a: "In most cases, yes. Safe Mode driver fixes, Startup Repair, and boot-file rebuilds resolve it without touching your data. A clean install is the last resort, and you should back up your files from the recovery environment first."
  - q: "Why did this happen right after a Windows update?"
    a: "Updates sometimes install a storage controller driver that doesn't match your hardware, or change how the boot driver loads. Rolling back the driver or the update usually restores the working configuration immediately."
---
INACCESSIBLE_BOOT_DEVICE (stop code 0x0000007B) is the blue screen that appears when Windows starts to boot and then suddenly can't read its own system drive. Your files are almost certainly still there — Windows just lost the driver or configuration it needs to reach them. This guide walks you through recovery step by step, from the simplest BIOS check to full boot repair.

You'll need access to the Windows Recovery Environment (WinRE). If Windows won't boot at all, force it: power on, and when the logo appears, hold the power button to force off. Do this two or three times and WinRE's **Automatic Repair** screen appears. If you've seen other stop codes alongside this one, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the broader toolkit.

## Why this happens

- **Wrong storage driver after an update.** Windows installed a controller driver that doesn't match your chipset.
- **SATA mode changed in BIOS.** Switching between AHCI and RAID/IDE modes breaks the boot driver chain.
- **Corrupted boot configuration data.** The BCD store lost its drive references.
- **Disk corruption.** File-system damage on the system partition blocks driver loading.
- **Failing drive.** Bad sectors in critical areas produce intermittent boot failures.
- **BIOS/UEFI update reset settings.** A firmware update can flip storage modes back to defaults.
- **Cloning or drive swap.** Moving Windows to a new SSD without the right driver breaks boot.

## How to fix it

Work through these in order — test a normal boot after each.

### Fix 1: Check the SATA mode in BIOS/UEFI

The single most common cause — a flipped storage mode.

1. Power on and press your BIOS key repeatedly (**F2**, **Del**, or **F12** depending on brand).
2. Find the storage configuration — usually under **Advanced**, **Storage**, or **SATA Configuration**.
3. Note the current mode: **AHCI**, **RAID**, or **IDE/Compatibility**.
4. If it was recently changed (by you, an update, or a BIOS reset), switch it back to what it was. When in doubt, try **AHCI** first — it's the modern default.
5. Save and exit (**F10** usually).
6. Let Windows boot. If the mode was the problem, you'll be at your desktop in under a minute.

### Fix 2: Boot into Safe Mode

Safe Mode uses minimal drivers and often boots when normal mode can't.

1. Reach WinRE via the forced-shutdown method described in the intro. Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers alternative ways to get there if the forced method doesn't trigger.
2. Choose **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode.
4. If Safe Mode boots, the problem is a driver — continue to Fix 3.
5. If Safe Mode also blue-screens with the same error, skip to Fix 4 for boot-file repair.
6. In Safe Mode, immediately back up critical files to an external drive if you haven't recently — cheap insurance.

### Fix 3: Roll back or update the storage driver

In Safe Mode, fix the driver that broke boot.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
3. Right-click each storage controller, choose **Properties > Driver**, and check the driver date.
4. If a driver was updated recently, click **Roll Back Driver** and follow the prompts.
5. If rollback isn't available, choose **Update driver > Search automatically for drivers**.
6. Better still, download the chipset/storage driver from your laptop maker's support page on another device, copy it via USB, and install it in Safe Mode. Restart and test a normal boot.

### Fix 4: Run Startup Repair

WinRE's automated fixer handles many boot-file problems on its own.

1. Boot into WinRE (forced-shutdown method).
2. Choose **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation if prompted.
4. Let it run — it takes several minutes and may restart the machine.
5. If it reports it couldn't repair the PC, note any log file path it mentions (`S:\Recovery\WindowsRE\Winre.wim\System32\Logfiles\Srt\SrtTrail.txt`) and continue to Fix 5.
6. Don't run Startup Repair repeatedly — if it fails once, move on to manual repairs.

### Fix 5: Rebuild the boot configuration data

Manual BCD repair for when automation fails.

1. In WinRE, choose **Troubleshoot > Advanced options > Command Prompt**.
2. Identify your Windows drive letter — in WinRE it's often **D:**, not C:. Check with:
   `diskpart`
   `list volume`
   `exit`
3. Run the boot repairs, replacing D: with your actual Windows drive if different:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
4. If `fixboot` gives "Access is denied," run these first:
   `diskpart`
   `list disk`
   `sel disk 0`
   `list vol`
   `sel vol 2` (the EFI/FAT32 partition, ~100MB)
   `assign letter=Z:`
   `exit`
   `bcdboot D:\Windows /s Z: /f UEFI`
5. Type `exit` and choose **Continue** to boot Windows.
6. Microsoft documents these recovery commands on [support.microsoft.com](https://support.microsoft.com/en-us/windows) if you want the official reference.

### Fix 6: Check the disk for corruption

File-system damage can block the boot driver from loading.

1. In WinRE's Command Prompt (Fix 5), run a full disk check on the Windows drive:
   `chkdsk D: /f /r` (use the letter you confirmed in Fix 5)
2. This can take a long time on large drives — let it complete without interrupting.
3. When it finishes, review the summary for bad sectors or repaired errors.
4. Type `exit` and try booting normally.
5. If chkdsk found many bad sectors, the drive is likely failing — prioritize data backup immediately using a live USB or by mounting the drive in another PC.
6. Consider replacing the drive with a new SSD and cloning while it still reads.

### Fix 7: Uninstall the latest update from WinRE

If the error appeared right after an update, roll it back.

1. In WinRE, go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first.
3. Restart and test. If the error persists, go back and try **Uninstall latest feature update**.
4. Once Windows boots, open **Settings > Windows Update** and pause updates for a couple of weeks.
5. While paused, check your laptop maker's support site for a BIOS or chipset driver update that resolves the incompatibility — then unpause.
6. If none of the above works, boot WinRE, open Command Prompt, and back up files with `xcopy` or `robocopy` to an external drive before considering a clean install from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

INACCESSIBLE_BOOT_DEVICE looks terminal but is usually a driver or configuration mismatch — the SATA mode check alone fixes a large share of cases. Work the ladder methodically, and back up your data the moment you get any bootable state, even Safe Mode. If the drive itself is failing, no software fix will hold, so let chkdsk's report guide your next move: clean disk means keep troubleshooting software; bad sectors mean replace the drive.
