---
title: "How to Fix the Inaccessible Boot Device Error on a Lenovo Laptop"
slug: how-to-fix-inaccessible-boot-device-on-lenovo-laptop
date: 2026-09-12
categories: ["windows-errors"]
tags: ["inaccessible-boot-device", "lenovo", "blue-screen"]
description: "Inaccessible Boot Device blue screen on your Lenovo laptop? Follow these steps to repair boot records, check your SSD, and get Windows booting again."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-on-lenovo-laptop.webp"
faqs:
  - q: "What causes the Inaccessible Boot Device error on Lenovo laptops?"
    a: "Windows can't read the drive it needs to boot from. On Lenovos this is most often a storage driver problem after a Windows update, a BIOS setting that changed between AHCI and RAID/IRST modes, or a failing SSD. It also appears when cloning to a new drive without the correct controller drivers installed."
  - q: "Can I fix Inaccessible Boot Device without losing my files?"
    a: "Yes, in the majority of cases. The boot configuration repair, driver reinstallation, and BIOS setting fixes below don't touch your personal data. Only a Windows reset or clean install would remove files, and that's the last resort here. Avoid formatting anything until you've tried the non-destructive steps."
  - q: "Why does my Lenovo boot into this error after a Windows update?"
    a: "Windows updates sometimes replace or reset the Intel Rapid Storage (IRST) driver that many Lenovo laptops need to see their NVMe SSD. Without the right driver, the boot process can't access the drive and throws this stop code. Booting into Safe Mode and reinstalling the storage driver usually resolves it."
  - q: "Should I change the SATA mode in BIOS to fix it?"
    a: "Only if the mode changed from what Windows was installed with. If it was installed in RAID/IRST mode and the BIOS reset to AHCI (or vice versa), Windows loses access to the drive. Match the setting to the original value. Don't toggle it randomly — pick the setting that matches your original install, then fix the driver."
---
The Inaccessible Boot Device blue screen is one of the more alarming Windows errors because it hits before you even reach the desktop. Your Lenovo laptop shows a sad face, says your PC ran into a problem, and restarts — only to land on the same screen again. It means Windows tried to start but couldn't read the drive it needs to load from.

On Lenovo laptops this error very often follows a Windows update that touched the storage driver, or a BIOS reset that changed the SATA controller mode. Your files are almost certainly still on the drive; Windows just can't reach them right now. The steps below repair that connection, from least to most invasive. If your stop code came from an update specifically, also see [Inaccessible Boot Device after a Windows 11 update](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/), and for other brands check [the Dell version](/articles/how-to-fix-inaccessible-boot-device-on-dell-laptop/).

## Why this happens

- **Wrong storage driver after a Windows update.** Many Lenovo laptops need the Intel RST (VMD) driver to see the NVMe SSD. An update can swap in a generic driver that can't find the drive.
- **BIOS storage mode changed.** Switching between AHCI and RAID/IRST (or Intel VMD on/off) makes Windows unable to talk to the drive it was installed on.
- **Corrupted boot records.** The BCD store or boot sector can be damaged by a power failure, failed update, or partition tool.
- **Failing SSD or loose connection.** A drive developing bad sectors or a loose M.2 connector produces intermittent or permanent boot failures.
- **Recent hardware or partition changes.** Cloning to a new drive, resizing partitions, or adding a second drive can shuffle boot order or break the EFI partition.
- **BitLocker without a key.** If encryption got enabled and the key wasn't saved, Windows can't read the drive at all.

## How to fix it

Work through these in order. You'll need Windows Recovery Environment (WinRE), which usually appears after two or three failed boots.

### Fix 1: Get into Windows Recovery and run Automatic Repair

Let WinRE take a first crack at the boot records.

1. Force WinRE by holding the power button to shut down during the Lenovo logo twice in a row; on the third boot choose **Advanced options**.
2. Or interrupt with the **Novo button** (the small pinhole button on many Lenovo laptops) and choose **System Recovery**.
3. Go to **Troubleshoot > Advanced options > Startup Repair** and let it run.
4. Restart when it finishes and see whether Windows boots.

### Fix 2: Rebuild the boot records with bootrec

If Automatic Repair fails, repair the boot configuration manually.

1. From WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands one at a time:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   (If `fixboot` reports access denied, skip it and continue.)
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. For UEFI systems, you may also need:
   `bcdboot C:\Windows /s Z: /f UEFI`
   (Replace Z: with your EFI partition letter if different; use `diskpart` then `list volume` to find it.)
4. Type `exit`, restart, and check whether the error is gone.

### Fix 3: Check the BIOS storage mode (AHCI vs RAID/IRST)

This is the single most common fix on Lenovo laptops.

1. Restart and press **F2** (or **Fn + F2**) at the Lenovo logo to enter BIOS setup.
2. Go to the **Configuration** tab and find **Storage** or **SATA Controller Mode**.
3. Note the current value. Try the opposite mode (if it says **AHCI**, switch to **Intel RST Premium / RAID**; if it says RAID, switch to AHCI) — Windows was installed with one specific mode, and you need to match it.
4. Also check **Configuration > Intel VMD Controller** (on 11th-gen Intel and newer): if it was originally enabled, leave it enabled.
5. Press **F10** to save and exit, then try booting.

### Fix 4: Boot into Safe Mode and reinstall the storage driver

Safe Mode loads a minimal driver set, which often lets you in to fix the real driver.

1. From WinRE go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. Once in, open **Device Manager** (press **Win + X** and choose it).
3. Expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
4. Right-click the Intel Chipset SATA/PCIe RST controller and choose **Update driver > Search automatically for drivers**.
5. Better yet, download the correct driver from [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model and install it manually.
6. Restart normally.

### Fix 5: Run CHKDSK and SFC from WinRE

File system corruption on the drive can produce this stop code.

1. From WinRE open **Command Prompt** again.
2. First find your Windows drive letter — in WinRE it may be D: or E:, not C:. Type `diskpart`, then `list volume`, then `exit`.
3. Run a disk check on the Windows volume:
   `chkdsk C: /f /r`
   (Substitute the correct letter. This can take 30 minutes or more.)
4. Then run an offline system file check:
   `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`
5. Restart and test.

### Fix 6: Run Lenovo's built-in hardware diagnostics

Rule out a dying SSD before spending more time on software fixes.

1. Restart and press **F10** (or use the **Novo button > Lenovo Diagnostics**) to enter Lenovo's diagnostics.
2. Run the **Storage / SSD** quick test first, then the extended test if you have time.
3. If the drive fails, it needs replacement — no software fix will save it. If it passes, move to Fix 7.
4. While you're there, note the drive model so you can download the right drivers from Lenovo Support.

### Fix 7: System Restore or Reset as a last resort

When boot records, drivers, and BIOS settings all check out, restore Windows itself.

1. From WinRE go to **Troubleshoot > Advanced options > System Restore** and pick a restore point from before the problem started.
2. If no restore point exists, go to **Troubleshoot > Reset this PC** and choose **Keep my files**.
3. If even the reset fails, check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the standalone storage driver for your chipset, or prepare for a clean Windows install using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

Inaccessible Boot Device on a Lenovo laptop is usually a driver or BIOS-mode problem rather than a dead drive — the storage-mode toggle in Fix 3 and the driver reinstall in Fix 4 solve most cases without touching your data. If Lenovo's own diagnostics say the SSD is healthy but nothing here helps, the clean install route from the Windows 11 download page will get you back to a working system, so back up what you can from WinRE first.
