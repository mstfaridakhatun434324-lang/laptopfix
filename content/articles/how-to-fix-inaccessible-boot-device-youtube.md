---
title: "INACCESSIBLE_BOOT_DEVICE: How to Fix This Windows Boot Blue Screen"
slug: how-to-fix-inaccessible-boot-device-youtube
date: 2026-09-10
categories: ["windows-errors"]
tags: ["blue screen", "inaccessible boot device", "stop code 0x7b", "boot failure", "windows 11"]
description: "INACCESSIBLE_BOOT_DEVICE (0x7B) stopping Windows from booting? Fix this storage-driver boot failure in 7 steps — most need no reinstall."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-youtube.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "It's stop code 0x0000007B. Windows started booting but lost access to the system drive partway through — usually because the storage driver it needs isn't loading. The drive is often perfectly healthy; Windows just can't talk to it with the drivers it has."
  - q: "Did my SSD die?"
    a: "Probably not. This error most commonly follows a Windows update, BIOS change, or storage-mode switch (AHCI/RAID) that left Windows with the wrong storage driver. Check the BIOS storage mode and recent updates before assuming the drive failed."
  - q: "Can I fix this without reinstalling Windows?"
    a: "Usually yes. Booting into the recovery environment and running startup repair, fixing the boot records with bootrec commands, or correcting the storage driver mode resolves most cases with your files untouched."
  - q: "Why did this happen after a Windows update?"
    a: "Updates sometimes replace your storage controller driver with a generic one that can't initialize your specific SSD or RAID setup, or they reset BIOS-adjacent settings. Our [update-specific INACCESSIBLE_BOOT_DEVICE guide](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/) covers that exact scenario."
---

INACCESSIBLE_BOOT_DEVICE (0x7B) is the blue screen that greets you instead of your desktop: Windows begins to start, then realizes it can't read the drive it's booting from. It sounds catastrophic, but the drive is usually fine — what's broken is the *conversation* between Windows and the drive, most often a storage driver mismatch or a changed BIOS setting.

Because Windows won't boot, every fix here runs from the Windows Recovery Environment (WinRE), which you reach by interrupting startup three times or booting from installation media.

## Why this happens

- **Storage controller driver replaced or corrupted.** A Windows update swaps your AHCI/NVMe/RAID driver for one that can't initialize your drive.
- **BIOS storage mode changed.** Switching between AHCI, RAID, and IDE modes after Windows is installed breaks the expected driver chain.
- **Corrupted Boot Configuration Data (BCD).** The bootloader points at the wrong partition or a damaged entry.
- **Failed Windows update left boot files half-written.** An interrupted update can damage the boot partition's contents.
- **Failing SSD or loose drive connection.** Less common, but a dying drive or a reseated-after-repair laptop can trigger it.
- **BitLocker or encryption driver issues.** Encryption filter drivers that fail to load block access to the encrypted system volume.

## How to fix it

Work through these in order — start with Fix 1 and stop when Windows boots.

### Fix 1: Check the BIOS storage mode

A single changed BIOS setting is a classic cause.

1. Power on and enter BIOS/UEFI (**Del**, **F2**, or **F10** — varies by brand).
2. Find the storage configuration section (often under **Advanced > SATA Configuration** or **Storage**).
3. Note the current mode: **AHCI**, **RAID/Intel RST Premium**, or **IDE**.
4. If it was recently changed (after a BIOS update or reset), switch it back to what Windows was installed with — usually AHCI for single-drive laptops, RAID for Intel RST setups.
5. Save, exit, and try booting. If Windows starts, you're done — don't touch anything else.

### Fix 2: Run Startup Repair from the recovery environment

Let Windows attempt the automated fix first.

1. On the blue screen, click **Advanced options** (or force WinRE by holding the power button during boot three times in a row).
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation and let it run — it checks boot records and core boot files. If you can reach the desktop intermittently, [booting into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) first lets you back up files before attempting repairs.
4. Restart when prompted and see if Windows loads.
5. If Startup Repair fails, continue — the manual fixes below go further.

### Fix 3: Rebuild the boot records with bootrec

Manually repair the bootloader.

1. In WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands one at a time, pressing Enter after each:
   `bootrec /fixmbr`
   `bootrec /fixboot` (if "Access denied," continue anyway)
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `rebuildbcd` finds your Windows installation, type **Y** to add it.
4. For UEFI systems, you may also need:
   `bcdboot C:\Windows /s Z: /f UEFI` (where Z: is your EFI partition — assign it a letter first with `diskpart` if needed).
5. Type `exit`, restart, and test the boot.

### Fix 4: Run CHKDSK and SFC from recovery

Repair file-system and system-file damage on the unbootable drive.

1. Open **Command Prompt** from WinRE's **Advanced options** again.
2. First identify your Windows drive letter — in WinRE it may be D: or E:, not C:. Run `diskpart`, then `list volume`, then `exit`.
3. Run `chkdsk D: /f /r` (replace D: with your actual Windows drive) and let it complete — this can take a while.
4. Then run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` with the correct letter.
5. Restart and attempt a normal boot.

### Fix 5: Load the correct storage driver

If Windows has the wrong storage driver, inject the right one.

1. On another computer, download your laptop's storage/RAID driver from the manufacturer's support page ([Dell](https://www.dell.com/support), HP, Lenovo) and copy it to a USB stick.
2. Boot into WinRE's **Command Prompt** on the broken laptop.
3. Use `drvload X:\path\to\driver.inf` (replace with your USB letter and path) to load the driver into the recovery environment.
4. Alternatively, use DISM to inject it into the offline Windows image:
   `DISM /Image:D:\ /Add-Driver /Driver:X:\drivers /Recurse`
5. Restart and check whether Windows now boots.

### Fix 6: Uninstall the problematic update

If the failure started right after a Windows update, remove it.

1. In WinRE, go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first and restart to test.
3. If that doesn't help, return and choose **Uninstall latest feature update**.
4. Once booted, open **Settings > Windows Update** and pause updates for a week while the fixed update is reissued.
5. Then update your storage drivers from the manufacturer's page before unpausing, so the bad driver doesn't return.

### Fix 7: Check the drive health and reinstall as a last resort

Rule out physical failure before wiping anything.

1. In WinRE's **Command Prompt**, run `wmic diskdrive get status` — anything other than **OK** means the drive is failing; replace it.
2. If the status is OK but nothing boots, back up files using the Command Prompt (`xcopy` or `robocopy` to a USB drive) while you still can.
3. As a final step, do a clean install from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) — boot from the USB, and during setup load your storage driver when the drive list is empty.
4. After installation, install chipset and storage drivers from the manufacturer before anything else.
5. Microsoft's [Windows recovery documentation](https://support.microsoft.com/en-us/windows) covers additional advanced recovery options.

## Closing

INACCESSIBLE_BOOT_DEVICE feels like a dead drive, but it's a driver conversation problem far more often than a hardware funeral. The BIOS storage-mode check alone fixes a surprising number of cases in under two minutes. Work through the recovery-environment steps patiently, keep your files backed up before any reinstall, and you'll usually be back on the desktop with everything intact. When this blue screen lands right after an update, the [post-update INACCESSIBLE_BOOT_DEVICE guide](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/) covers the update-specific storage-driver regressions.
