---
title: "Windows 11 Installation Failed on Lenovo Laptop: Full Fix Guide"
slug: fix-windows-11-installation-failed-on-lenovo-laptop
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windows 11", "installation", "lenovo", "upgrade error"]
description: "Windows 11 setup keeps failing on your Lenovo laptop? Here's how to fix the most common causes — from BIOS settings to driver conflicts."
thumbnail: "/images/thumbs/fix-windows-11-installation-failed-on-lenovo-laptop.webp"
faqs:
  - q: "Why does Windows 11 installation fail on Lenovo laptops specifically?"
    a: "Lenovo laptops often ship with TPM 2.0 or Secure Boot disabled in the BIOS, which blocks Windows 11 setup immediately. Lenovo-specific storage drivers (Intel RST) and older BIOS versions are the other common culprits. Checking BIOS settings first solves the majority of failures."
  - q: "Can I install Windows 11 on a Lenovo laptop that isn't officially supported?"
    a: "If your Lenovo meets the core requirements (64-bit CPU, 4 GB RAM, TPM 2.0, Secure Boot, UEFI), you can install it normally. On genuinely unsupported hardware, workarounds exist but you won't get official support or guaranteed updates. Check Lenovo's support page for your model's compatibility status first."
  - q: "What does error 0x80070002 mean during Windows 11 installation?"
    a: "It means the installer can't find or access files it needs — usually a corrupt download, a bad USB drive, or Windows Update components stuck in a broken state. Redownloading the ISO, recreating the USB media, or resetting Windows Update components fixes it in most cases."
  - q: "Will fixing a failed install delete my files?"
    a: "A failed in-place upgrade normally rolls back to your previous Windows and keeps your files. But if the installer got as far as formatting or you're doing a clean install, data loss is possible. Back up your important files before attempting any installation fix."
---

Watching the Windows 11 installer roll back for the third time is a special kind of frustration. Everything looks fine, the progress bar climbs, then at some percentage it freezes, throws a cryptic error code, and dumps you back into Windows 10 — or worse, into a recovery screen. On Lenovo laptops this is especially common, because Lenovo's BIOS defaults and driver stack add a few traps that generic install guides never mention.

The good news is that installation failures almost always have a concrete cause, and it's almost never "your laptop can't run Windows 11." Nine times out of ten it's a BIOS setting, bad install media, a conflicting driver, or not enough free space. Work through the fixes below in order and you'll find the one that's blocking you.

## Why this happens

- **TPM 2.0 or Secure Boot disabled in BIOS**: Windows 11 requires both. Many Lenovo models ship with them off, or a BIOS reset turned them off silently — the installer fails its very first compatibility check.
- **Corrupt or incomplete install media**: A USB drive created with a flaky download, or an ISO that got interrupted, produces hash-mismatch errors mid-installation that look mysterious but are just bad files.
- **Incompatible storage drivers**: Lenovo laptops with Intel RST (Rapid Storage Technology) need the right storage driver at install time. Without it, setup can't see the SSD or fails when writing to it.
- **Not enough free disk space**: The upgrade needs at least 64 GB free and works better with 100 GB+. Setups that start with marginal space fail at the "copying files" stage.
- **Driver or software conflicts**: Old graphics drivers, disk encryption tools, and third-party antivirus can all interfere with the upgrade process and trigger a rollback.
- **Pending updates or a broken Windows Update cache**: A half-installed update on your current Windows can poison the upgrade. Clearing the SoftwareDistribution cache is a classic fix.
- **Outdated BIOS firmware**: Lenovo regularly fixes compatibility quirks in BIOS updates. Running a two-year-old BIOS on a new Windows 11 installer is asking for trouble.

## How to fix it

Work through these in order — start with the BIOS check, because it causes the most Lenovo-specific failures.

### Fix 1: Enable TPM 2.0 and Secure Boot in the BIOS

This is the single most common reason Windows 11 setup fails on a Lenovo.

1. Restart your laptop and press **F2** (or **Fn + F2**) repeatedly as the Lenovo logo appears to enter the BIOS.
2. Go to the **Security** tab and find **TPM** / **Trusted Platform Module** — set it to **Enabled** or **On**.
3. Go to the **Boot** tab and set **Secure Boot** to **Enabled**. If it's greyed out, set **Boot Mode** to **UEFI** first (not Legacy).
4. Press **F10** to save and exit, then retry the installation.

### Fix 2: Make sure you have enough free disk space

The installer is honest about many things but vague about space.

1. Open **File Explorer** and check your C: drive — you want at least 64 GB free, ideally 100 GB+.
2. Open **Settings** > **System** > **Storage** and click **Temporary files** to clean house.
3. Run **Disk Cleanup** (**Win + S**, type `cleanmgr`, press Enter), select C:, and tick everything safe, including **Previous Windows installation(s)** if you don't need to roll back.
4. Move large personal files to an external drive, then retry setup.

### Fix 3: Create fresh installation media

Don't trust a USB drive you made six months ago.

1. On a working PC, download the [Windows 11 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11).
2. Use a USB drive with at least 8 GB — and use a different drive than before if you suspect the old one, since cheap flash drives develop bad sectors.
3. Run the tool, choose **USB flash drive**, and let it finish completely without unplugging anything.
4. Boot from the USB (press **F12** at the Lenovo logo for the boot menu) and start the install fresh.

### Fix 4: Update your BIOS and Lenovo drivers first

Lenovo fixes install-blocking bugs in firmware updates regularly.

1. Open **Lenovo Vantage** (**Win + S**, type `lenovo vantage`) and check **System Update** for BIOS and driver updates.
2. If Vantage isn't installed, go to [Lenovo Support](https://support.lenovo.com/us/en/), enter your serial number, and download the latest BIOS and chipset drivers.
3. Install the BIOS update with the charger plugged in — never flash BIOS on battery.
4. After updating, retry the Windows 11 installation.

### Fix 5: Disconnect peripherals and disable third-party antivirus

External devices and security software are classic rollback triggers.

1. Unplug everything except the charger, mouse, and keyboard — docks, USB drives, printers, external monitors, all of it.
2. If you use third-party antivirus (Norton, McAfee, Kaspersky, Avast), uninstall it temporarily. Windows Defender will cover you during the upgrade.
3. Disable disk encryption software other than BitLocker.
4. Retry the installation with the laptop as bare as possible.

### Fix 6: Run the upgrade from a clean boot

This eliminates software conflicts without uninstalling anything.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, tick **Hide all Microsoft services**, then click **Disable all**.
3. Go to the **Startup** tab and click **Open Task Manager** — disable every startup item.
4. Restart, then run the Windows 11 installer from the USB or the mounted ISO.
5. After a successful install, reopen `msconfig` and re-enable everything.

### Fix 7: Decode the error with SetupDiag

If it still fails, get the actual reason instead of guessing.

1. After a failed install, open an elevated **Command Prompt** (**Win + X** > **Terminal (Admin)**).
2. Look in `C:\$Windows.~BT\Sources\Panther\` for `setupact.log` — search it for the error code.
3. Common codes: `0x80070002` means missing/corrupt files (see [how to fix Windows 11 install error 0x80070002 on a Lenovo laptop](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/)), and `0x80070057` points at storage or parameter problems ([error code 0x80070057 fix](/articles/error-code-0x80070057-fix/)).
4. If you upgraded from Windows 10 and the rollback keeps happening, check [how to fix a blue screen after a Windows 11 update on Lenovo](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/) since post-upgrade crashes share many of the same root causes.
5. Address the specific code rather than retrying blindly — each retry without a change wastes an hour.

## Closing

A failed Windows 11 install on a Lenovo laptop feels like the machine is rejecting the upgrade, but it's almost always one gatekeeper setting, one corrupt file, or one outdated driver standing in the way. Check TPM and Secure Boot, build fresh media, update the BIOS, and strip the setup down to essentials — and if you hit a specific error code, chase that code instead of retrying the same thing. Your Lenovo will run Windows 11 fine; it just needs the path cleared first.
