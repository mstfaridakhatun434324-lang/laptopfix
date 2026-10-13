---
title: "Windows 11 Installation Keeps Failing on Your Acer? Solve It"
slug: how-to-fix-windows-11-installation-failed-on-acer-laptop
date: 2026-09-10
categories: ["windows-errors"]
tags: ["windows 11", "installation failed", "acer", "setup"]
description: "Windows 11 setup failing on your Acer laptop? From BIOS settings to USB media to driver quirks — here's how to get the install to finish."
thumbnail: "/images/thumbs/how-to-fix-windows-11-installation-failed-on-acer-laptop.webp"
faqs:
  - q: "Why does Windows 11 setup fail on Acer laptops specifically?"
    a: "The usual Acer-specific causes: TPM/Secure Boot disabled in BIOS, the storage controller in RST/RAID mode hiding the SSD from setup, an outdated BIOS, or Acer's custom drivers conflicting during an upgrade install. Corrupted USB media and nearly-full drives cause failures on every brand."
  - q: "Setup says it can't find any drives. What do I do?"
    a: "Enter BIOS (F2 on Acer), find the SATA mode or storage controller setting, and switch it from RST/RAID/Intel RST Premium to AHCI. Save and retry setup — the drive should appear. Alternatively, load Acer's Intel RST driver during setup with the Load driver option."
  - q: "How do I update the BIOS on an Acer laptop?"
    a: "Go to Acer's support site, enter your serial number or SNID, download the latest BIOS for your model, and run the updater on AC power — never on battery alone. Some Acer models also support flashing from the F12 boot menu. Recheck TPM and Secure Boot settings afterward, as flashes can reset them."
  - q: "Will a clean install delete everything on my Acer?"
    a: "Yes — a clean install erases the system drive, so back up your files first. An in-place upgrade (launching setup from inside Windows) preserves files and apps. If setup keeps failing, copy your data to an external drive before attempting the clean install."
---

Windows 11 Installation Keeps Failing on Your Acer? Solve It

Watching Windows 11 setup fail — the progress bar freezing, the cryptic error, the rollback — is bad enough once. When it happens three times in a row on your Acer laptop, it's personal. The good news: Acer installation failures come from a short, well-understood list. TPM and Secure Boot settings, the RST storage mode that hides your SSD, an old BIOS, or bad USB media account for nearly all of them.

This guide is Acer-specific: the F2 BIOS, where Acer hides the storage controller setting, and how Acer's BIOS updates work. If you're fighting the compatibility check rather than setup itself, our [Lenovo "can't run Windows 11" guide](/articles/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop/) explains the requirements in depth (the BIOS concepts are the same on Acer).

## Why this happens

- **TPM 2.0 or Secure Boot is disabled.** Windows 11 setup requires both; Acer BIOSes don't always ship with them on.
- **RST/RAID mode hides the drive.** Acer uses Intel RST Premium on many models, and setup can't see the SSD without switching to AHCI or loading the RST driver.
- **The BIOS is outdated.** Old Acer firmware can fail the compatibility check or mishandle the installer's boot.
- **The USB installer is corrupt.** Bad ISO downloads and dying flash drives cause failures at random percentages.
- **Not enough free space.** Upgrades need 20GB+ free; nearly-full drives fail late in the process.
- **Conflicting software during upgrades.** Third-party antivirus, disk tools, and encryption can block setup's file operations.

## How to fix it

Work through these in order — BIOS settings first, since they cause most Acer failures.

### Fix 1: Enable TPM 2.0 and Secure Boot

The compatibility gate that stops setup before it starts.

1. Power off, power on, and press **F2** repeatedly to enter Acer BIOS setup.
2. Go to the **Security** tab: set **TPM** (or **TPM Device**) to **Available/Enabled**, and **Secure Boot** to **Enabled**.
3. Go to the **Boot** tab and confirm **Boot Mode** is **UEFI** (not Legacy).
4. Press **F10** to save and exit, then re-run setup.

### Fix 2: Switch the storage controller to AHCI

The number one "can't find drives" fix on Acers.

1. In BIOS (**F2**), go to the **Main** or **Advanced** tab and find **SATA Mode** (wording varies: SATA Mode, Storage Controller, VMD Controller).
2. Change it from **RST Premium** / **RAID** / **Intel RST** to **AHCI**.
3. **F10** to save and exit. Caution: an existing Windows installed in RST mode won't boot after this — fine for a clean install, but back up first if you intended an upgrade.
4. Re-run setup; your SSD should now be listed.

### Fix 3: Update the Acer BIOS

Old firmware causes both check failures and mid-install crashes.

1. Find your serial number/SNID on the bottom sticker.
2. On Acer's support site, enter it and download the latest **BIOS** for your exact model.
3. Run the updater **on AC power** with the battery charged — never flash on battery alone. Some models support flashing from the BIOS's own update utility.
4. After flashing, re-enter BIOS and verify TPM, Secure Boot, and AHCI are still set (flashes often reset them).

### Fix 4: Build fresh, trustworthy USB media

Mysterious mid-setup failures usually mean bad media.

1. Download a fresh ISO from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create the USB with Microsoft's **Media Creation Tool** or Rufus (**GPT** scheme for UEFI).
3. Use a different, known-good flash drive — old or cheap sticks corrupt data silently.
4. Plug it directly into the laptop (no hubs/docks) and boot with **F12**, selecting the USB device.

### Fix 5: Prepare the drive and disconnect extras

Give setup the cleanest possible environment.

1. If Windows still boots, free **25GB+** on C: with **Disk Cleanup** (`cleanmgr` → **Clean up system files**).
2. Unplug all external drives, docks, printers, and unnecessary USB devices — extra hardware confuses the installer.
3. For clean installs, delete old Windows partitions at the **Where do you want to install Windows?** screen and let setup recreate them.
4. For upgrades, temporarily uninstall third-party antivirus and suspend BitLocker (**Manage BitLocker > Suspend protection**).

### Fix 6: Load Acer's RST driver during setup

If you must stay in RST mode, hand setup the driver.

1. From Acer's support site, download the **Intel Rapid Storage Technology** driver for your model and extract it onto a USB stick.
2. At setup's drive selection screen, click **Load driver**, browse to the USB, and install the RST driver.
3. The SSD appears — continue the install.
4. Afterward, install remaining drivers from Acer's support page, and check [Windows support](https://support.microsoft.com/en-us/windows) if any device still misbehaves.

### Fix 7: Read the setup logs for the real error code

Generic failure messages hide specific causes — the logs don't.

1. After a failed upgrade, open `C:\$Windows.~BT\Sources\Panther\setuperr.log` in Notepad.
2. Common codes: `0x80070002` (missing/corrupt files — rebuild USB media), `0xC1900101` (driver conflict — note the named driver and update/remove it), `0x800F0922` (EFI partition problem).
3. For `0xC1900101` naming a driver, remove or update that driver (often Wi-Fi, Bluetooth, or a storage filter) and retry.
4. If the same error repeats after all fixes, try installing with only one RAM stick (on models with removable RAM) — marginal memory causes the strangest setup failures. Our [Dell installation guide](/articles/how-to-fix-windows-11-installation-failed-on-dell-laptop/) covers additional log-reading tips that apply equally to Acer.

## Closing

Acer installation failures are almost never mysterious: it's the BIOS settings (TPM, Secure Boot, AHCI), the firmware age, or the USB stick. Work the list top to bottom, and setup goes from "failed again" to "welcome to Windows 11" — usually on the very next attempt. And once you're in, run Windows Update fully before installing anything else, so drivers and firmware settle into a clean, consistent state.
