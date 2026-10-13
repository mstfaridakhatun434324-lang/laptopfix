---
title: "Windows 11 Installation Failed? A Step-by-Step Fix Guide"
slug: how-to-fix-windows-11-installation-failed-step-by-step
date: 2026-09-03
categories: ["windows-errors"]
tags: ["windows 11", "installation", "upgrade", "troubleshooting"]
description: "Windows 11 installation failed and rolled back? Work through this step-by-step checklist — space, drivers, media, BIOS — and get it installed."
thumbnail: "/images/thumbs/how-to-fix-windows-11-installation-failed-step-by-step.webp"
faqs:
  - q: "Why does my Windows 11 installation keep failing?"
    a: "The big five: not enough free disk space, outdated BIOS, an incompatible driver blocking migration, corrupt installation media or update cache, and interfering software (antivirus, VPNs, USB peripherals). The error code tells you which one."
  - q: "Will a failed install hurt my current Windows?"
    a: "No. Failed upgrades roll back automatically to your previous system with files and apps intact. The rollback is annoying but safe — it's Windows protecting you from a half-installed state."
  - q: "How do I find out why it failed?"
    a: "Note the error code and the percentage where it stopped. Then check C:\\$Windows.~BT\\Sources\\Panther\\setupact.log — the setup logs record exactly which step failed. The code plus the log narrows it to one of the big five causes."
  - q: "Should I clean-install instead of upgrading?"
    a: "Upgrading preserves everything and should be tried first with proper preparation. Clean-install only when upgrades fail repeatedly despite the checklist — it's more work (backup, reinstall apps) but bypasses whatever the upgrade chokes on."
---

Every failed Windows 11 installation follows the same script: progress bar, error code, rollback, and you're back where you started with no explanation. But the causes aren't mysterious — they're a short, checkable list. This guide is that checklist, in the order that resolves the most failures with the least effort.

Before anything else: write down the exact error code and the percentage where setup stopped. You'll need both.

## Why this happens

- **Insufficient free disk space**: Setup needs ~20GB of working room. Full drives cause silent or cryptic failures — the single most common cause on 128GB/256GB laptops.
- **Outdated BIOS**: Old firmware lacks the TPM, Secure Boot, or hardware handling the installer expects.
- **A driver that can't migrate**: Storage, graphics, or chipset drivers that setup can't carry over halt the entire process.
- **Corrupt installation media or update cache**: Damaged USB installers or a corrupt `SoftwareDistribution` folder feed setup broken files.
- **Interfering software and peripherals**: Third-party antivirus, VPNs, disk tools, and USB devices (docks, printers, external drives) stall or break setup.
- **Unmet requirements discovered late**: TPM/Secure Boot issues or CPU incompatibility that the pre-check missed or that changed since.

## How to fix it

Work through these in order — each step eliminates a cause.

### Fix 1: Free disk space and record the failure details

Preparation that fixes the most common cause outright.

1. Note the exact error code (e.g., 0x80070002, 0xC1900101) and the progress percentage where it failed. Different codes mean different fixes — the [Lenovo 0x80070002 guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/) and [Dell 0x80070002 guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-dell-laptop/) cover the most frequent one per brand.
2. Check free space: **Settings** > **System** > **Storage**. Get C: to 20GB+ free, ideally 30GB+.
3. Run **Disk Cleanup** as admin (**Win + S** > `cleanmgr` > **Clean up system files**): remove update leftovers, temp files, delivery optimization files.
4. Uninstall unused large apps and move media files to external storage temporarily.
5. Empty the Recycle Bin (yes, really — people forget).

### Fix 2: Update BIOS and core drivers before retrying

Give setup the firmware and drivers it expects.

1. Go to your laptop manufacturer's support site, enter your exact model, and install the latest **BIOS** (on AC power, everything closed, don't interrupt).
2. Install the latest **chipset**, **storage** (Intel RST/AMD RAID), and **graphics** drivers from the same site.
3. Restart, then retry the installation before doing anything else — this step alone resolves a large share of failures.

### Fix 3: Clear the update cache and repair system files

Corrupt cached files cause a huge fraction of update-path failures.

1. Open **Terminal (Admin)** (**Win + X**).
2. Run:
   - `net stop wuauserv`
   - `net stop bits`
   - `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   - `ren C:\Windows\System32\catroot2 catroot2.old`
   - `net start wuauserv`
   - `net start bits`
3. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Retry the installation via Windows Update.

### Fix 4: Strip the system down for setup

Remove everything that can interfere, temporarily.

1. Unplug all USB devices except essentials: docks, external drives, printers, hubs, SD cards — all out.
2. Uninstall third-party antivirus (**Settings** > **Apps**) — Defender stays and doesn't interfere.
3. Disable or uninstall VPN clients, disk-encryption tools, and "system optimizer" utilities.
4. Disconnect from Wi-Fi/Ethernet during a USB-media install if driver downloads seem to stall setup (reconnect after).
5. Retry the installation in this minimal state.

### Fix 5: Use fresh USB media instead of Windows Update

When the update path keeps failing, the media path often succeeds — they exercise different code paths.

1. On another PC (or this one), download the Media Creation Tool from [Microsoft's Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create a fresh USB installer on a known-good 8GB+ drive. If a previous USB failed, **recreate it on a different drive** — flash drives fail.
3. Run `setup.exe` from the USB while booted into Windows (upgrade path, keeps everything).
4. Choose **Keep personal files and apps** when prompted.
5. If setup asks about updates during install, choose **Not right now** — get the base install down first, update after.

### Fix 6: Verify requirements and check setup logs

For failures with no clear cause, read what setup actually recorded.

1. Confirm TPM 2.0: **Win + R** > `tpm.msc` should show ready, version 2.0.
2. Confirm Secure Boot: **Win + R** > `msinfo32` > **Secure Boot State** = On.
3. Open the setup log: `C:\$Windows.~BT\Sources\Panther\setupact.log` — search for "error" near the end to find the failing step. (Show hidden files to see the `$Windows.~BT` folder.)
4. Driver migration failures show as `0xC1900101` with a driver extension code — the log names the driver. Update or remove that specific driver and retry.

### Fix 7: Clean install as the final option

When the upgrade path fails repeatedly despite all preparation, bypass it.

1. **Back up everything** to external storage — clean install wipes the drive.
2. Boot from the USB media, choose **Custom install**, delete old partitions, install fresh.
3. After install: manufacturer drivers first (chipset, graphics, network), then Windows Update, then apps, then restore files.
4. Verify activation: **Settings** > **System** > **Activation** — digital licenses reactivate automatically online.

If the machine is so broken that even setup media struggles, the [factory reset without password guide](/articles/how-to-factory-reset-windows-11-laptop-without-password/) documents the full recovery path.

## Closing

Failed installations feel random, but they're checklist problems: space, BIOS, drivers, media, interference. Work the list honestly — especially the unglamorous parts like freeing 30GB and updating the BIOS — and setup stops fighting you. The error code is your compass; the rollback is your safety net. Between the two, there's no failed install that stays mysterious for long. And once Windows 11 is finally in place, resist the urge to immediately reinstall every utility you had before — add things back gradually over a few days so that if something destabilizes the fresh system, you'll know exactly which program did it.
