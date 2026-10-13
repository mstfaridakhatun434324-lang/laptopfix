---
title: "Fixing Windows Update Error 0xC1900101 on Your Laptop"
slug: "how-to-fix-update-fails-with-error-0xc1900101-reddit"
date: "2026-10-03"
categories: ["windows-update"]
tags: ["0xc1900101", "windows-update", "driver-conflict", "feature-update"]
description: "Error 0xC1900101 kills Windows feature updates at the last moment. It's almost always a driver — here's how to find the culprit and get the upgrade through."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-reddit.webp"
faqs:
  - q: "What does error 0xC1900101 actually mean?"
    a: "It is a rollback code indicating that a Windows feature update failed during the driver migration or second boot phase and reverted to the previous version. The extended code after it, such as 0x40017 or 0x30018, narrows down the phase. In the overwhelming majority of cases, the root cause is an incompatible, outdated, or corrupted device driver that crashes the upgrade process."
  - q: "Which drivers most commonly cause 0xC1900101?"
    a: "Storage controller drivers, outdated chipset drivers, third-party antivirus filter drivers, and old Wi-Fi or Bluetooth drivers top the list. Virtualization and disk-encryption filter drivers are frequent offenders too. The setup log files usually name the specific driver, which is why checking the logs before bulk-updating everything saves time."
  - q: "Should I disconnect devices before retrying the update?"
    a: "Yes, it is one of the most effective quick fixes. USB drives, docks, printers, external GPUs, and even some USB headsets load drivers during the upgrade that can conflict with the migration. Stripping the machine down to just power and the built-in peripherals removes a whole category of failure modes with almost no effort."
  - q: "How many times should I retry before trying something drastic?"
    a: "Do not just keep retrying blindly — each failed attempt costs time and risks leaving the servicing state messier. One retry after disconnecting peripherals and updating key drivers is reasonable. If that fails, read the setup logs to identify the failing driver instead of rolling the dice again. Targeted fixes beat repeated attempts every time."
---

Error 0xC1900101 is the classic "so close, yet so far" of Windows updates. The feature update downloads fine, installs through the first phases, reboots — and then rolls everything back with this cryptic code. It is one of the most discussed update failures in community forums precisely because it strikes at the finish line, and because the fix is almost always the same category of problem: a driver that the upgrade process cannot live with.

The code itself has sub-codes that tell you which phase failed, but you rarely need to decode them by hand. The practical approach is to eliminate the usual driver suspects, read the logs if needed, and retry once the machine is in a clean state. Follow the sequence below and this error becomes very beatable.

The cruel detail of 0xC1900101 is its timing. The download succeeds, the early install phases complete, the machine reboots — and then, deep in the second boot phase where drivers are migrated to the new build, something fails and Windows rolls the entire upgrade back. The extended code that follows, such as 0x40017 or 0x30018, identifies the phase, but in practice the answer is the same in the overwhelming majority of cases: a driver that could not make the transition. Knowing that narrows the entire troubleshooting effort to one question — which driver.

## Why this happens

- **Incompatible storage drivers:** Old AHCI, RAID, or NVMe drivers crash the second boot phase when Windows tries to migrate them.
- **Antivirus filter drivers:** Third-party security products hook deep into the system and frequently block the upgrade's driver migration.
- **Outdated chipset drivers:** The chipset package orchestrates device handoff during upgrade; old versions fumble it.
- **External device drivers:** Docks, printers, and USB peripherals load drivers mid-upgrade that conflict with the new OS build.
- **Wi-Fi and Bluetooth drivers:** Aging wireless drivers are a notorious 0xC1900101 trigger on laptops.
- **Disk encryption filters:** Third-party encryption tools can interfere with the offline phase's disk operations.
- **Corrupt driver store:** A damaged driver repository causes migration failures even when individual drivers are current.
- **Insufficient reserved space:** The upgrade needs room for driver staging and rollback data; a cramped drive amplifies driver issues.

## How to fix it

Work through these in order — diagnose first, then act.

Resist the urge to retry the update repeatedly without changing anything. Each failed attempt costs twenty to forty minutes and can leave the servicing state messier than it found it. Make one targeted change — disconnect peripherals, update a driver set, remove the antivirus — then retry. Deliberate attempts beat hopeful ones.

### Fix 1: Disconnect all non-essential peripherals

This single step resolves a large fraction of 0xC1900101 failures because it removes conflicting drivers from the upgrade path.

1. Unplug every USB device: external drives, docks, printers, dongles, and hubs.
2. Disconnect external monitors and use only the laptop's built-in display.
3. Remove SD cards and eject any discs.
4. Keep only the power adapter connected, then retry the feature update.

### Fix 2: Update chipset and storage drivers

The drivers most likely to crash the upgrade deserve to be current before you retry.

1. Visit your laptop manufacturer's support page and download the latest chipset driver for your exact model.
2. Install the latest storage controller driver from the same source — Intel RST, AMD, or the vendor package as applicable.
3. Update the BIOS as well if a newer version is available, since firmware and chipset drivers work as a pair.
4. Restart normally, then attempt the feature update again.

### Fix 3: Temporarily remove third-party antivirus

Antivirus filter drivers are among the top confirmed causes of this exact error code.

1. Uninstall your third-party antivirus completely — disabling is often not enough, since filter drivers stay loaded.
2. Confirm Windows Security is active so the machine remains protected during the upgrade.
3. Retry the feature update with only Windows Security in place.
4. Reinstall your preferred antivirus after the upgrade completes successfully.

### Fix 4: Update wireless and Bluetooth drivers

Laptop wireless drivers are disproportionately represented in 0xC1900101 reports.

1. Download the latest Wi-Fi and Bluetooth drivers from your laptop manufacturer's support page.
2. Install both packages and restart the laptop.
3. Alternatively, use the Intel Driver & Support Assistant if your wireless hardware is Intel-based.
4. Retry the update once the new wireless drivers are active.

### Fix 5: Read the setup logs to name the culprit

When broad fixes fail, the logs tell you exactly which driver choked.

1. After a failed attempt, open File Explorer and navigate to `C:\$Windows.~BT\Sources\Panther`.
2. Open `setuperr.log` in Notepad and look for driver file names near the failure timestamp.
3. Also check `C:\Windows\Logs\MoSetup` for additional error context.
4. Once you identify the driver, update it from the manufacturer or uninstall the associated device before retrying.

### Fix 6: Clean up the driver store

A corrupted driver repository can sabotage migration even with current drivers installed.

1. Open Command Prompt as administrator.
2. Run `pnputil /enum-drivers` to list third-party driver packages.
3. Remove clearly obsolete duplicates with `pnputil /delete-driver oemXX.inf /uninstall`, replacing oemXX with the actual number.
4. Be conservative — only remove drivers you can identify as old duplicates for the same device.
5. Restart and retry the feature update.

### Fix 7: Free space and repair system files

Give the upgrade the room and the healthy system files it needs for driver staging.

1. Ensure at least 20 to 30 GB of free space on the system drive using Storage Sense or Disk Cleanup.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt.
3. Follow with `sfc /scannow` to repair protected system files.
4. Restart, then attempt the feature update one more time.
5. If the failure persists with a different code, our walkthrough for [manually installing the update](/articles/how-to-manually-install-windows-update-on-windows-11/) offers an alternative delivery path.

### Fix 8: Use the Installation Assistant as a final attempt

When Windows Update's own engine keeps tripping, Microsoft's assistant sometimes succeeds where it fails.

1. Download the Windows 11 Installation Assistant from Microsoft's software download page.
2. Run it with peripherals disconnected and antivirus removed as prepared above.
3. Let the assistant download and install the feature update in place.
4. If even this fails with 0xC1900101, the log-identified driver from Fix 5 needs resolving before any method will work.

In the rare cases where every driver looks current and the logs name nothing conclusive, consider the age of the installation itself: machines upgraded across many Windows versions accumulate driver remnants that no updater cleans. A clean install of the target Windows 11 build, followed by fresh drivers from the manufacturer, succeeds where in-place upgrades keep rolling back — at the cost of reinstalling your applications. Back up first, and treat it as the final option rather than the first. For upgrades that stall in a different way, our walkthrough on [diagnosing the Update Assistant stuck at 99 percent](/articles/update-assistant-stuck-at-99-percent-troubleshooting/) covers that symptom.

## Closing

Error 0xC1900101 looks intimidating, but it is really Windows telling you that one driver could not make the trip to the new build. Strip the peripherals, refresh the chipset, storage, and wireless drivers, evict the antivirus temporarily, and let the logs name any holdout — that combination gets the overwhelming majority of stuck feature updates across the finish line.
