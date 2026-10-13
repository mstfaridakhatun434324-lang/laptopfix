---
title: "Windows 11 Installation Failed on Your Dell Laptop? Do This"
slug: how-to-fix-windows-11-installation-failed-on-dell-laptop
date: 2026-10-12
categories: ["windows-errors"]
tags: ["windows 11", "installation failed", "dell", "setup"]
description: "Windows 11 setup keeps failing on your Dell laptop? Here are the real causes — from TPM settings to bad USB media — and how to fix each one."
thumbnail: "/images/thumbs/how-to-fix-windows-11-installation-failed-on-dell-laptop.webp"
faqs:
  - q: "Why does Windows 11 setup keep failing on Dell laptops?"
    a: "The most common reasons: TPM 2.0 or Secure Boot disabled in BIOS, an outdated BIOS that misreports hardware, corrupted USB installation media, or Intel RST/RAID storage mode hiding the drive from setup. Dell-specific storage drivers are another frequent culprit — setup needs the right driver to see the SSD."
  - q: "What does 'This PC can't run Windows 11' mean during setup?"
    a: "It means the compatibility check failed on TPM 2.0, Secure Boot, CPU generation, or RAM. On Dell laptops this is usually a BIOS setting rather than genuinely incompatible hardware — enabling TPM and Secure Boot in the BIOS resolves it on most supported models."
  - q: "Do I need to change RAID to AHCI to install Windows 11 on a Dell?"
    a: "Often, yes. Dell ships many laptops with the SATA/NVMe controller in RAID (Intel RST Premium) mode, and Windows 11 setup can't see the drive without the RST driver. Switching to AHCI/NVMe mode in the BIOS is the simplest fix — but change it before installing, or Windows won't boot afterward."
  - q: "Will reinstalling Windows 11 delete my files?"
    a: "A clean install erases everything on the system drive, so back up first. An in-place upgrade (running setup from inside Windows) keeps files and apps. If setup keeps failing, back up your data with a live USB or by connecting the drive to another PC before attempting a clean install."
---

Windows 11 Installation Failed on Your Dell Laptop? Do This

There's a special frustration in watching Windows 11 setup grind through its progress bars only to announce "Windows 11 installation has failed" and roll everything back. On Dell laptops, this almost always comes down to a short list of usual suspects: TPM and Secure Boot settings, the RAID storage mode Dell loves to ship, outdated BIOS, or flaky USB media. None of them are hard to fix once you know where to look.

This guide is Dell-specific: the exact BIOS keys, the storage controller quirk, and where to get Dell's own installation drivers. If you're hitting the compatibility error specifically, our guide on [fixing "this PC can't run Windows 11"](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/) digs into the requirements check in detail.

## Why this happens

- **TPM 2.0 or Secure Boot is disabled.** Windows 11 setup hard-requires both; many Dell BIOSes ship with one or both off.
- **RAID/RST storage mode hides the drive.** Dell defaults to Intel RST Premium mode, and setup can't see the SSD without the RST driver loaded.
- **The BIOS is too old.** Early BIOS versions misreport TPM status or CPU compatibility to the Windows 11 checker.
- **The USB installer is corrupted.** A bad ISO download or a failing flash drive causes mysterious mid-setup failures.
- **Insufficient or fragmented disk space.** Feature installs need 20GB+ free and can fail on nearly-full drives.
- **Third-party antivirus or encryption interferes.** For in-place upgrades, disk encryption and AV filters can block setup's file operations.

## How to fix it

Work through these in order. Check the BIOS settings first — they cause the majority of Dell installation failures.

### Fix 1: Enable TPM 2.0 and Secure Boot in the Dell BIOS

This resolves the compatibility failure on most supported Dell models.

1. Restart and press **F2** repeatedly during the Dell logo to enter BIOS setup.
2. Go to **Security > TPM 2.0 Security** (or **TPM On**) and make sure it's **On**. On newer BIOS versions look under **Security > TPM 2.0 Security On**.
3. Go to **Secure Boot > Secure Boot Enable** and set it to **Enabled**. If it's greyed out, change **Boot Mode** to **UEFI** first (never Legacy).
4. Press **Apply**, then **Exit** to save and reboot. Re-run setup.

### Fix 2: Switch the storage controller from RAID to AHCI

Dell's RST Premium default is the number one cause of "we couldn't find any drives" during setup.

1. Enter BIOS with **F2** and go to **System Setup > SATA/NVMe Operation** (sometimes under **Storage**).
2. Change it from **RAID On** / **Intel RST Premium** to **AHCI/NVMe**.
3. **Apply** and **Exit**. Warning: if Windows is currently installed in RAID mode, it won't boot after this change — that's expected if you're doing a clean install anyway.
4. Re-run setup; the drive should now be visible. If you must keep RAID mode (e.g., an existing install you want to preserve), load Dell's Intel RST driver during setup via the **Load driver** option instead.

### Fix 3: Update the Dell BIOS

An outdated BIOS can fail the Windows 11 compatibility check on hardware that's actually fine.

1. On a working computer, go to [Dell Support](https://www.dell.com/support), enter your Service Tag, and check **Drivers & Downloads > BIOS**.
2. Download the latest BIOS and copy it to a FAT32 USB stick (or run the .exe from within Windows if you have a working install).
3. Flash it from the BIOS itself (**F12 boot menu > BIOS Flash Update**) or by running the updater — always on AC power, never on battery alone.
4. After the flash, re-verify TPM and Secure Boot are still enabled (BIOS updates sometimes reset them), then re-run setup.

### Fix 4: Recreate the USB installer properly

Bad media causes the most confusing failures — setup dies at random percentages.

1. Download a fresh Windows 11 ISO from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create the USB with the official **Media Creation Tool** or Rufus (choose **GPT** partition scheme for UEFI).
3. Use a different, known-good USB stick — cheap or aging flash drives corrupt data silently.
4. Plug it into a **USB port directly on the laptop** (not a hub or dock) and boot via **F12 > USB**.

### Fix 5: Free space and prep the drive

Setup needs room to breathe.

1. Boot into your current Windows (if it still boots) and free at least **25GB** on C: — run **Disk Cleanup** (`cleanmgr`) including **Clean up system files**.
2. Disconnect all external drives, docks, and unnecessary USB devices during setup — extra drives confuse the installer.
3. If doing a clean install, delete the old Windows partitions during setup when asked **Where do you want to install Windows?** and let setup recreate them.
4. For in-place upgrades failing repeatedly, uninstall third-party antivirus temporarily and pause disk encryption (BitLocker: **Manage BitLocker > Suspend protection**).

### Fix 6: Load Dell's storage driver during setup

If you kept RAID mode, give setup the driver it needs.

1. From Dell's support site, download the **Intel Rapid Storage Technology** driver for your exact model and extract it to a USB stick.
2. During setup, at the drive selection screen, click **Load driver**, browse to the USB, and select the RST driver.
3. Your SSD should appear. Continue the installation normally.
4. After Windows is installed, run Dell **SupportAssist** or **Dell Update** to pull in the remaining drivers.

### Fix 7: Check the setup logs for the real error

When setup fails generically, the logs name the actual problem.

1. After a failed install, the logs live in `C:\$Windows.~BT\Sources\Panther\setuperr.log` (for upgrades) — open it in Notepad.
2. Look for error codes: `0x80070002` = missing files (bad media), `0xC1900101` = driver conflict (note the driver name beside it), `0x800F0922` = .NET/EFI partition issue.
3. A `0xC1900101` naming a driver means: update or remove that driver (often Wi-Fi or storage filter) and retry.
4. If logs point to the EFI partition being too small or full, that's a firmware-level issue — check Dell forums for your model or contact Dell Support with the error code. Microsoft documents setup error codes further in its Windows support documentation.

## Closing

Windows 11 setup failures on Dell laptops are rarely mysterious once you know Dell's defaults: check TPM and Secure Boot, flip RAID to AHCI, make sure the BIOS is current, and use trustworthy USB media. Get those four right and setup usually sails through on the next attempt. And if the install succeeds but Windows then refuses to boot, our [Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) picks up right where this one leaves off.
