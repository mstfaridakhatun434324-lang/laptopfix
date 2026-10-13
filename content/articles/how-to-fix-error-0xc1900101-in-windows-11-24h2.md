---
title: "How to Fix Error 0xC1900101 When Updating to Windows 11 24H2"
slug: how-to-fix-error-0xc1900101-in-windows-11-24h2
date: 2026-10-07
categories: ["windows-errors"]
tags: ["windows update error", "0xc1900101", "windows 11 24h2"]
description: "Update to Windows 11 24H2 failing with 0xC1900101? It's a driver rollback error. Here's how to find the bad driver, free space, and complete the upgrade."
thumbnail: "/images/thumbs/how-to-fix-error-0xc1900101-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0xC1900101 mean during a Windows 11 update?"
    a: "Error 0xC1900101 is a generic driver-related rollback code. It means Windows started the upgrade to 24H2, hit a driver it couldn't migrate or that crashed the new build, and rolled back to your previous version. The extended code after it (like 0x30018 or 0x4000D) narrows down which phase failed."
  - q: "Which drivers most often cause 0xC1900101?"
    a: "Display drivers (NVIDIA/AMD/Intel), storage controller drivers, and old antivirus filter drivers top the list. Outdated BIOS firmware and connected peripherals with ancient drivers (printers, docks, USB devices) are frequent contributors too."
  - q: "How much free space do I need for the 24H2 update?"
    a: "Microsoft asks for 64 GB total storage, but the upgrade itself needs roughly 20–30 GB of free space to stage files safely. If you're under 20 GB free on C:, free up space before retrying — low space is a documented trigger for 0xC1900101 rollbacks."
  - q: "Should I disconnect peripherals before retrying the update?"
    a: "Yes — it's one of the most effective steps. USB docks, printers, external drives, and specialty hardware load drivers during the upgrade that can crash it. Disconnect everything except keyboard and mouse, retry the update, and reconnect devices afterward one by one."
---
Error 0xC1900101 is the classic "almost upgraded, then rolled back" error. Your laptop downloads Windows 11 24H2, starts installing, gets partway through — and then you're staring at your old desktop again with a cryptic code in Update history. The good news hidden in that frustration: your system protected itself. The rollback means a driver couldn't survive the upgrade, and Windows wisely backed out.

Fixing it means finding that driver (or the other blocker) before retrying. Work through these in order — most 0xC1900101 cases are solved by driver updates and peripheral removal. For other upgrade-blocking codes, see [error 0x80073712](/articles/how-to-fix-error-0x80073712-in-windows-11-24h2/) or our [installation-failed guide](/articles/best-way-to-fix-windows-11-installation-failed/).

## Why this happens

- **Incompatible device driver:** A display, storage, network, or chipset driver crashes during the driver-migration phase, forcing a rollback.
- **Outdated BIOS/firmware:** Old firmware mishandles the new build's power management or device initialization.
- **Connected peripherals:** External devices with legacy drivers (printers, docks, USB audio) inject failing drivers mid-upgrade.
- **Third-party antivirus filter drivers:** Kernel-level AV drivers are notorious upgrade blockers.
- **Insufficient free disk space:** The upgrade stages tens of gigabytes; running out of room aborts the install.
- **Corrupted system files:** Damaged servicing components cause the upgrade engine to mis-handle driver migration.
- **Overclocking or custom power settings:** Unstable hardware states during the long upgrade process trigger driver timeouts.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the 24H2 upgrade completes.

### Fix 1: Disconnect all non-essential peripherals

The single highest-yield step. External hardware is a factor in a huge share of 0xC1900101 rollbacks.

1. Shut down the laptop completely (not sleep).
2. Unplug everything USB: docks, hubs, external drives, printers, webcams, USB headsets, and SD cards.
3. Keep only the power adapter connected.
4. Boot up and retry the update in **Settings** > **Windows Update**.
5. After a successful upgrade, reconnect devices one at a time, letting Windows install fresh drivers for each.

### Fix 2: Update all major drivers before retrying

Don't let the upgrade migrate ancient drivers — update them first so there's nothing to choke on.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Update **Display adapters**, **Network adapters**, **IDE ATA/ATAPI controllers**, and **System devices** via **Update driver** > **Search automatically for drivers**.
3. Then get the manufacturer-tested versions: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) — install their latest chipset, graphics, storage, and network drivers.
4. NVIDIA/AMD GPU owners should also grab the latest driver from the maker's site.
5. Restart, then retry the 24H2 update.

### Fix 3: Temporarily uninstall third-party antivirus

AV filter drivers are among the most common specific causes of this rollback code.

1. Open **Settings** > **Apps** > **Installed apps** and uninstall your third-party antivirus completely (disabling isn't always enough — the filter driver stays loaded).
2. Confirm **Windows Security** is active: **Settings** > **Privacy & Security** > **Windows Security**.
3. Retry the update.
4. After 24H2 installs successfully, reinstall your preferred antivirus fresh — the new install will use a 24H2-compatible driver.

### Fix 4: Free up disk space

Give the upgrade the room it needs — this alone fixes a meaningful percentage of cases.

1. Open **Settings** > **System** > **Storage** > **Cleanup recommendations**.
2. Remove temporary files, unused apps, and large downloads — target at least 30 GB free on C:.
3. Check **Temporary files** and include **Previous Windows installations** if listed (frees many GB).
4. Empty the Recycle Bin.
5. Retry the update with ample free space.

### Fix 5: Update your BIOS/firmware

Old BIOS versions are a documented 0xC1900101 trigger, especially on laptops from 2019–2022.

1. Find your exact model on [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. Download the latest **BIOS** and read the release notes for Windows 11 24H2 or upgrade-related fixes.
3. Connect AC power — never flash BIOS on battery.
4. Run the updater and don't touch the machine until it reboots itself.
5. Retry the Windows update afterward.

### Fix 6: Repair system files and reset update components

Cleans up the servicing stack so the retry starts from a healthy state.

1. Open an **administrator Command Prompt**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Reset the update cache: `net stop wuauserv`, `net stop bits`, `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, `net start wuauserv`, `net start bits`.
4. Restart and retry the 24H2 update.

### Fix 7: Check the setup logs to identify the exact failing driver

If you've done everything and it still rolls back, the logs name the culprit.

1. After a failed upgrade, open **File Explorer** and go to **C:\$Windows.~BT\Sources\Panther**.
2. Open **setuperr.log** in Notepad and look at the most recent errors — driver `.inf` or `.sys` names appear here.
3. Also check **C:\Windows\Logs\DISM** and Event Viewer (**eventvwr.msc**) > **Windows Logs** > **System** around the rollback time.
4. Once you identify the driver (often a printer, old VPN, or storage filter), update or uninstall that specific device/software.
5. For help interpreting dump and log evidence, see [how to read dump files with WinDbg](/articles/how-to-read-dump-files-with-windbg-on-windows-11/).

### Fix 8: Do the upgrade from installation media

The in-place media upgrade bypasses several Windows Update-specific failure modes.

1. Download the Media Creation Tool from Microsoft's Windows 11 download page.
2. Create a USB installer (or mount the ISO directly).
3. With peripherals still disconnected and AV uninstalled, run **setup.exe** from the media.
4. Choose **Keep personal files and apps**.
5. The media-based upgrade often succeeds where Windows Update repeatedly rolls back.

## Closing

Error 0xC1900101 is Windows telling you a driver couldn't make the trip to 24H2 — and the fix is almost always preparation, not surgery. Disconnect peripherals, update every major driver from your laptop maker's site, uninstall third-party antivirus temporarily, free 30 GB, and update the BIOS. That sequence gets the overwhelming majority of stuck upgrades across the finish line. If it still rolls back, the Panther setup logs will name the exact driver — follow the evidence rather than guessing. And once 24H2 is in, reinstall your AV and reconnect devices one by one so any troublemaker is easy to spot.
