---
title: "How to Fix INACCESSIBLE_BOOT_DEVICE on an HP Laptop"
slug: how-to-fix-inaccessible-boot-device-on-hp-laptop
date: 2026-09-02
categories: ["windows-errors"]
tags: ["bsod", "inaccessible boot device", "hp laptop", "storage driver"]
description: "INACCESSIBLE_BOOT_DEVICE on your HP laptop? Windows lost contact with your drive mid-boot. Here's how to get it back, step by step."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-on-hp-laptop.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "Windows started to boot but lost access to the system drive partway through. The usual causes: a storage driver problem (very common on HP laptops), a BIOS storage-mode change, a failed Windows update, or a dying drive."
  - q: "Will I lose my files?"
    a: "Almost certainly not. This is a boot/driver problem, not a data problem — your files are still on the drive. Every fix below is non-destructive. Still, if the drive itself is failing, back up as soon as you can boot."
  - q: "Why does this happen on HP laptops specifically?"
    a: "HP laptops commonly use Intel RST (Rapid Storage Technology) drivers and ship with the BIOS set to RAID mode. Windows updates sometimes replace the RST driver with an incompatible one, or a BIOS reset flips the storage mode — either breaks the boot path."
  - q: "What if none of the fixes work?"
    a: "Then the drive itself is likely failing. Run HP's built-in diagnostics (F2 at boot), and if the drive fails, replace it — then reinstall Windows. Your files can usually be recovered by connecting the old drive to another PC."
---

`INACCESSIBLE_BOOT_DEVICE` is one of the more alarming blue screens because it appears during startup — Windows begins to load, then loses contact with the drive it's booting from and gives up. The reassuring part: your data is almost always intact. This is a communication problem between Windows and your storage, not a data-destruction problem. On HP laptops specifically, the cause is a storage driver issue more often than not, which means it's fixable without reinstalling anything.

The classic HP scenario goes like this: a Windows update installs a new storage driver (or a BIOS update resets the storage mode), and suddenly Windows can't talk to the SSD it was happily booting from yesterday. The fixes below walk through the HP-specific causes first. If you're seeing a neighboring boot failure instead, our guide to the [automatic repair loop](/articles/automatic-repair-loop-windows-11-troubleshooting/) covers that territory.

## Why this happens

- **Intel RST driver replaced or corrupted**: The most common HP-specific cause. Windows Update swaps HP's Intel Rapid Storage Technology driver for a generic or incompatible version, and the boot-time storage driver can no longer find the drive.
- **BIOS storage mode changed**: A BIOS update or reset flips **SATA/NVMe Operation** between **RAID On** and **AHCI**. Windows was installed expecting one mode; the other mode makes the drive invisible at boot.
- **Failed or interrupted Windows update**: Updates touch boot-critical drivers. If the update fails midway, the storage driver can be left in a broken state.
- **Corrupt Boot Configuration Data (BCD)**: The BCD tells Windows where the system drive is. Corruption here produces this error instead of a clean boot.
- **Failing SSD or HDD**: A dying drive can drop off the bus intermittently. If the drive vanishes mid-boot, Windows reports exactly this error.
- **Loose drive connection (rare on laptops)**: Uncommon, but a drive that's worked loose from its connector produces intermittent inaccessible-device errors.
- **Third-party disk software**: Disk encryption, cloning tools, or "optimizer" utilities that install storage filter drivers can break the boot chain.

## How to fix it

Work through these in order — the HP-specific storage fixes come first.

### Fix 1: Check the BIOS storage mode

This is the fastest fix when it applies — a single setting, two minutes.

1. Power on and tap **F10** (or **Esc** then **F10**) to enter **BIOS Setup**. On some HP models it's **F2**.
2. Navigate to **Advanced** > **SATA/NVMe Operation** or **Storage Options** (exact location varies by model).
3. Note the current setting. HP laptops almost always ship with **RAID On** (Intel RST). If it's set to **AHCI** and you didn't change it, flip it back to **RAID On**.
4. Press **F10** to save and exit, then boot.

If you're not sure what it was originally: try **RAID On** first (the factory default for nearly all modern HP laptops). If that doesn't boot, try **AHCI**. One of the two is correct, and trying both is harmless.

### Fix 2: Boot into Safe Mode to load the generic driver

Safe Mode uses a minimal storage driver set, which often boots fine even when the normal driver is broken.

1. Force the recovery environment: power off the laptop mid-boot three times in a row.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
3. If Safe Mode boots, the problem is the normal-mode storage driver — proceed to Fix 3.
4. If Safe Mode also fails with the same error, skip to Fix 4 (the driver may need replacing offline).

### Fix 3: Reinstall the Intel RST driver from Safe Mode

With Windows booted in Safe Mode, replace the broken storage driver with HP's version.

1. In Safe Mode with Networking (press **5** instead of **4** at Startup Settings), open **Device Manager** (**Windows + X**).
2. Expand **Storage controllers**, right-click the Intel chipset SATA/PCIe RST controller, and choose **Uninstall device**. Tick **Attempt to remove the driver for this device** if offered.
3. Download the **Intel Rapid Storage Technology driver** from [HP's support site](https://support.hp.com/us-en) for your exact model and install it. (Intel's own [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) works too.)
4. Restart normally. Windows should now boot with the correct driver.

### Fix 4: Repair the storage driver offline via Command Prompt

If you can't boot even into Safe Mode, fix the driver from the recovery environment.

1. Boot into the recovery environment (interrupt boot three times) and open **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. First, try rebuilding the boot data:
   - `bootrec /fixmbr`
   - `bootrec /rebuildbcd`
3. Then check the disk: `chkdsk C: /f /r` (confirm your Windows drive letter with `dir C:` first — in WinRE it may be **D:**).
4. Run an offline system file check: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the letter to match).
5. Type `exit` and choose **Continue**.

### Fix 5: Uninstall the latest Windows update

If the error appeared within a day or two of an update, roll it back.

1. From the recovery environment: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first.
3. Restart. If Windows boots, the update's storage driver was the problem — reinstall the HP RST driver (Fix 3) before letting the update return, and check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known issues with that update.

### Fix 6: Run HP's built-in drive diagnostics

Rule out a failing drive with HP's own tools, which run outside Windows.

1. Power off completely, power on, and tap **Esc** repeatedly, then press **F2** for **HP PC Hardware Diagnostics UEFI**.
2. Run the **Hard Drive** / **SSD** test (the full/extended version, not just the quick check).
3. If the drive passes, your data path is fine and the problem is software — revisit Fixes 1-5.
4. If it fails, the drive is dying: back up immediately (boot a Linux live USB or connect the drive to another PC) and replace it. Note the failure ID for HP support if under warranty.

### Fix 7: Reset the BIOS to defaults

A last resort before reinstalling: clear any BIOS weirdness.

1. Enter **BIOS Setup** (**F10**).
2. Choose **Load Setup Defaults** (sometimes under the **Main** or **Exit** tab).
3. **Crucial**: after loading defaults, re-check the **SATA/NVMe Operation** mode — defaults sometimes set AHCI on machines that shipped with RAID On. Set it to match your Windows installation (usually **RAID On** for HP).
4. Save and exit.

## Closing

INACCESSIBLE_BOOT_DEVICE on an HP laptop is a storage-driver or BIOS-mode problem far more often than a dead drive, which is why Fixes 1 and 3 resolve so many cases. The key insight is that your files are fine — this error is about Windows losing the *path* to the drive, not losing the drive's contents. If the boot data itself turns out to be the deeper issue, our [BAD_SYSTEM_CONFIG_INFO repair guide](/articles/how-to-fix-bad-system-config-info-on-dell-laptop/) walks through the BCD rebuild in full detail. Work the list in order, and only start worrying about the drive hardware if HP's diagnostics say so. Once you're booting again, keep the HP RST driver current through HP Support Assistant so a future Windows update doesn't replay this exact scenario.
