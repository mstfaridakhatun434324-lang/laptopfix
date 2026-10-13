---
title: "Windows 11 Installation Failed: What to Do"
slug: what-to-do-if-windows-11-installation-failed
date: 2026-10-11
categories: ["windows-errors"]
tags: ["installation failed", "Windows 11", "setup errors"]
description: "Windows 11 installation failed? Decode the error code, fix media and driver issues, free disk space, and get the setup to complete successfully."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-installation-failed.webp"
faqs:
  - q: "What should I do first when Windows 11 installation fails?"
    a: "Note the exact error code and the percentage where setup stopped — that combination identifies the cause. Then check the three most common culprits: corrupted installation media, insufficient disk space, and incompatible drivers or peripherals. Recreating the USB installer with the official Media Creation Tool fixes a large share of failures."
  - q: "What does error 0x80070002 during Windows 11 setup mean?"
    a: "Error 0x80070002 means 'file not found' — setup can't find files it expects, usually because the installation media is corrupted or a download was incomplete. Recreate the USB drive with the Media Creation Tool, try a different USB port (USB 2.0 ports are more reliable for setup), and redownload the ISO if problems persist."
  - q: "Can antivirus software cause Windows 11 installation to fail?"
    a: "Yes — third-party antivirus and disk-encryption tools frequently interfere with setup, especially during upgrades. Uninstall third-party antivirus before upgrading (Windows Security stays active), and suspend BitLocker protection during the install. Reinstall your security software after Windows 11 is running."
  - q: "How much free space does Windows 11 installation need?"
    a: "Microsoft requires 64 GB of storage, but aim for at least 20–30 GB of genuinely free space beyond that for the installer to work comfortably. Setup creates temporary files, downloads updates, and keeps a Windows.old rollback folder. If you're tight on space, move personal files to an external drive before starting."
---

"Windows 11 installation has failed" — sometimes with a helpful error code, sometimes with nothing at all. Either way, the installer's complaint is usually about one of a handful of things: bad media, not enough space, a driver it chokes on, or a peripheral confusing it. The fix is systematic, not random.

This guide starts with reading the error correctly, then walks the fixes in likelihood order. If your machine fails the compatibility check before setup even starts, see our [guide to fixing "This PC can't run Windows 11"](/articles/best-way-to-fix-this-pc-can-t-run-windows-11/); Acer and Dell owners have [model-specific installation walkthroughs](/articles/how-to-fix-windows-11-installation-failed-on-acer-laptop/) as well.

## Why this happens

- Corrupted installation media — a bad USB write or incomplete ISO download.
- Insufficient free disk space for setup's temporary files and the Windows.old backup.
- Incompatible or outdated storage/chipset drivers that setup can't work with.
- Third-party antivirus or disk encryption blocking setup operations.
- Connected peripherals (docks, external drives, SD cards) confusing the installer.
- Failing RAM or storage hardware corrupting files as setup writes them.
- An overclocked or undervolted system that's stable in daily use but not under setup's sustained load.

## How to fix it

Work through these in order — Fix 1 alone resolves a huge share of failures.

### Fix 1: Recreate the installation media properly

Most "installation failed" cases trace back to the USB stick itself.

1. Download the **Media Creation Tool** from [Microsoft's official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Use a USB drive of **8 GB or larger** from a reputable brand — cheap no-name sticks cause corrupt writes.
3. Let the tool **download and create the media in one run**; don't interrupt it.
4. If setup still fails, recreate the media on a different USB stick and a different USB port.
5. Prefer a rear/USB 2.0 port on desktops; on laptops, avoid hubs and docks during setup.

### Fix 2: Decode the error code

The code tells you which fix to prioritize — don't skip this step.

1. Write down the full error code (e.g. `0x80070002`, `0xC1900101`, `0x800F081F`).
2. `0x80070002`/`0x80070003`: missing files — recreate media (Fix 1).
3. `0xC1900101`: driver conflict — disconnect peripherals and update drivers (Fixes 4–5).
4. `0x80070070`: disk space — free up space (Fix 3).
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the common setup codes if yours isn't listed here.

### Fix 3: Free up disk space

Setup needs breathing room beyond the bare 64 GB requirement.

1. In your current Windows, open **Settings > System > Storage** and run **Cleanup recommendations**.
2. Run Disk Cleanup: press **Win + R**, type `cleanmgr`, select **Clean up system files**.
3. Move personal files (videos, photos, downloads) to an external drive temporarily.
4. Aim for at least **25–30 GB genuinely free** on the system drive.
5. Uninstall large programs you can reinstall later — games especially.

### Fix 4: Disconnect all non-essential peripherals

Setup probes every connected device, and one bad actor can halt the whole install.

1. Unplug everything except keyboard, mouse, and monitor: docks, USB drives, SD cards, printers, external GPUs.
2. If you have multiple internal drives, consider disconnecting non-target drives during setup.
3. Remove any SD cards from built-in readers — they're a notorious setup trip hazard.
4. Retry the installation with the minimal configuration.
5. Reconnect peripherals one at a time after Windows 11 is running.

### Fix 5: Update drivers and BIOS before upgrading

For upgrade installs (not clean installs), the existing driver stack matters.

1. Update **chipset**, **storage**, and **graphics** drivers to Windows 11-ready versions from your maker's site.
2. Uninstall third-party antivirus — **Windows Security** remains active during setup.
3. Suspend **BitLocker**: open an elevated Command Prompt and run `manage-bde -protectors -disable C:`.
4. Update the **BIOS** to the latest version with the charger connected.
5. Retry the upgrade after these updates.

### Fix 6: Test RAM and drive health

If setup fails at random percentages with different errors each time, suspect hardware.

1. Run **Windows Memory Diagnostic** (`mdsched.exe`) before starting setup.
2. Check drive health: `wmic diskdrive get status` should report **OK**.
3. Run `chkdsk C: /f` to fix file-system errors on the target drive.
4. Bad RAM corrupts files as setup writes them — replace failing sticks first.
5. A drive with SMART warnings should be replaced before any OS install.

### Fix 7: Try a clean install instead of an upgrade

When upgrades repeatedly fail, a clean install sidesteps whatever the old system was tripping on.

1. Back up **everything** — a clean install erases the drive.
2. Boot from the USB installer and choose **Custom: Install Windows only**.
3. Delete the old partitions on the target drive and install to the unallocated space.
4. Let setup complete, then install drivers from your maker's support site.
5. Restore your files from backup afterwards.

### Fix 8: Check the setup log files

For stubborn failures, the logs name the exact failing component.

1. After a failed upgrade, open `C:\$Windows.~BT\Sources\Panther\setupact.log`.
2. Search for `Failed` or error codes near the end of the log.
3. The failing driver or component is usually named within a few lines of the error.
4. Update or remove that specific driver and retry.
5. For clean-install failures, check `X:\Windows\Panther` from the recovery Command Prompt (**Shift + F10** during setup).

## Closing

Windows 11 installation failures are almost never mysterious once you read the error code: bad media, cramped disk, hostile peripherals, or outdated drivers cover nearly every case. Recreate the USB properly, clear space, strip the peripherals, and setup completes. And when it does, leave the installer USB somewhere safe — future you will thank present you the next time a friend's laptop needs rescuing. Most failed installs are fixed within an hour once you stop reinstalling blindly and start reading what setup is actually complaining about in its detailed setup logs.
