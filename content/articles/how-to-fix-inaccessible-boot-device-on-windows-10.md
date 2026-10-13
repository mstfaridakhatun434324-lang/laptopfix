---
title: "How to Fix INACCESSIBLE_BOOT_DEVICE on Windows 10"
slug: how-to-fix-inaccessible-boot-device-on-windows-10
date: 2026-09-10
categories: ["windows-errors"]
tags: ["blue screen", "boot error", "windows 10"]
description: "Windows 10 won't boot with INACCESSIBLE_BOOT_DEVICE? Fix the storage driver or boot config with these recovery steps."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-on-windows-10.webp"
faqs:
  - q: "What causes INACCESSIBLE_BOOT_DEVICE?"
    a: "Windows loses access to the boot drive mid-startup. The common triggers: a storage driver update that won't load, the BIOS SATA mode changed after installation (AHCI vs RAID), a Windows update replacing the storage driver, corrupted boot configuration data, or a failing drive."
  - q: "Will I lose my files?"
    a: "Almost certainly not from the error itself — your data is still on the drive; Windows just can't reach it right now. All the fixes in this guide preserve files. Only a clean reinstall would erase them, and that's the last resort after System Restore and Reset-with-files."
  - q: "Why did changing AHCI to RAID break booting?"
    a: "Windows installs the storage driver matching the mode active at install time. Switch the BIOS mode afterward and the installed driver no longer matches the hardware presentation — Windows can't initialize the drive. Either switch the mode back or inject the correct driver."
  - q: "Can a Windows update really cause this?"
    a: "Yes — it's one of the classic post-update boot failures. Updates sometimes replace the Intel RST or NVMe driver with a version that fails on specific hardware. Uninstalling the update from recovery (Fix 3) and then installing the manufacturer's driver manually is the standard fix."
---

INACCESSIBLE_BOOT_DEVICE means Windows started to boot, then lost access to the drive it's booting from. It gets far enough to show you a blue screen with that message, which actually tells you a lot: the bootloader works, but the storage driver Windows needs to read the system drive isn't loading.

This happens most often after storage driver updates, BIOS storage-mode changes (AHCI/RAID/IDE), or Windows updates. Our [INACCESSIBLE_BOOT_DEVICE reference](/articles/best-way-to-fix-inaccessible-boot-device/) has the background; the recovery steps below fix it. Start at Fix 1.

## Why this happens

- A storage controller driver update (Intel RST, AMD, NVMe) that Windows can't load at boot.

- The BIOS storage mode being changed — e.g., RAID to AHCI — after Windows was installed.

- A Windows 10 update replacing the working storage driver with a broken one.

- Corrupted Boot Configuration Data pointing at the wrong partition.

- Disk errors or a failing SSD in the boot area.

- BitLocker getting confused by a hardware or firmware change.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Check the BIOS storage mode

If the SATA mode was changed (by a BIOS update, reset, or curious hands), Windows can't find its drive. This is the first thing to verify.

1. Enter BIOS/UEFI setup during boot (**F2**, **Del**, **Esc** — varies by maker).

2. Find the storage/SATA configuration — often under **Advanced** or **Storage**.

3. Note the current mode (**AHCI**, **RAID**, or **IDE**). If it was recently changed, set it back to what Windows was installed with — usually **AHCI** on modern laptops, **RAID** on some Intel systems.

4. Save, exit, and try booting.

### Fix 2: Boot into Safe Mode

Safe Mode loads a minimal storage driver set. If it boots, the normal-mode storage driver is the problem and you can fix it from inside.

1. From the recovery environment: **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**.

2. If Safe Mode boots, open **Device Manager** and check **Storage controllers** for warning icons.

3. Roll back or reinstall the storage driver from there.

4. Restart normally and test.

### Fix 3: Uninstall the breaking update or driver

If this started right after an update, remove it from the recovery environment — you don't need to boot Windows to do it.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.

2. Remove the latest **quality update** first, restart, and test.

3. If that fails, try the latest **feature update**.

4. Once booting, pause updates and reinstall the storage driver manually from the laptop maker's site before letting updates resume.

### Fix 4: Rebuild the BCD

A corrupted Boot Configuration Data store can produce this error even with a healthy drive and drivers.

1. Open **Troubleshoot > Advanced options > Command Prompt**.

2. Run `bootrec /fixmbr`, then `bootrec /fixboot`.

3. Run `bootrec /scanos` followed by `bootrec /rebuildbcd`, confirming with **Y**.

4. Type `exit`, choose **Continue**, and attempt a normal boot.

### Fix 5: Load the correct storage driver at boot

If the driver is missing rather than broken, you can inject the right one. This is the fix when a driver update deleted the working version.

1. On another PC, download the **Intel RST** or chipset storage driver for your exact laptop model.

2. Extract it to a USB drive.

3. Boot to recovery, open **Command Prompt**, and use `dism` to add the driver offline — or simpler: boot to Safe Mode (Fix 2) and install it via **Device Manager > Update driver > Browse my computer**.

4. Restart and confirm normal boot works. Intel's driver tools are at the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 6: Run chkdsk on the system drive

File system damage in the boot area causes this error with perfectly good drivers. Check the disk from recovery.

1. In the recovery Command Prompt, identify the Windows drive with `diskpart`, `list volume`, `exit`.

2. Run `chkdsk D: /f /r` (using the correct letter — often D: in recovery).

3. Let it complete fully; bad sectors in boot files get flagged here.

4. If chkdsk finds extensive damage, back up the data with a live USB before further repairs. Microsoft's boot troubleshooting is documented on [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Use System Restore, then reset as last resort

A restore point from before the driver/update change undoes it cleanly. If nothing boots, reset.

1. From recovery: **Troubleshoot > Advanced options > System Restore**, pick a pre-problem point.

2. If restore fails or no points exist, use **Troubleshoot > Reset this PC**.

3. Choose **Keep my files** first; only go **Remove everything** if that fails too.

4. After recovery, install the storage driver manually before reconnecting to Windows Update.

### Fix 8: Suspend BitLocker before making changes

BitLocker can block booting after driver, BIOS, or hardware changes — and its recovery screen looks alarming. If your drive is encrypted, suspending protection before repairs (and having the recovery key handy) prevents a second crisis on top of the first.

1. Find your recovery key first: on another device, visit **aka.ms/myrecoverykey** while signed into your Microsoft account.

2. In the recovery Command Prompt, unlock the drive if needed: `manage-bde -unlock C: -recoverypassword YOUR-48-DIGIT-KEY`.

3. Suspend protection with `manage-bde -protectors -disable C:`.

4. Perform your driver or BCD repairs, then reboot and confirm Windows starts.

5. Re-enable protection afterward: `manage-bde -protectors -enable C:`.

6. Keep the recovery key stored somewhere reachable from your phone — you'll want it again someday.

## Closing

INACCESSIBLE_BOOT_DEVICE is Windows telling you it can't talk to its own drive — and the conversation is almost always about the storage driver or the BIOS storage mode. Check the BIOS mode first (it's a 2-minute fix when that's it), then work through the driver and BCD repairs from recovery. Resist the urge to reinstall Windows immediately; this error is one of the most repairable boot failures there is, and your data is usually sitting there perfectly intact behind it. If the BCD rebuilds don't stick, our [BAD_SYSTEM_CONFIG_INFO guide](/articles/best-way-to-fix-bad-system-config-info/) covers the registry side of boot corruption, which produces similar symptoms through a different mechanism. Boot problems cluster: fixing one layer sometimes reveals the next, and that's normal.
