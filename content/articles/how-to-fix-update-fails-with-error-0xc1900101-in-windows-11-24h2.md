---
title: "Fix Update Error 0xC1900101 on Windows 11 24H2"
slug: how-to-fix-update-fails-with-error-0xc1900101-in-windows-11-24h2
date: 2026-09-01
categories: ["windows-update"]
tags: ["0xc1900101", "windows 11 24h2", "update error", "driver conflict"]
description: "Windows 11 24H2 update failing with error 0xC1900101? This driver-related code has specific causes — identify the culprit and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0xC1900101 mean?"
    a: "It is a driver-related update failure code. During the upgrade, Windows migrates drivers to the new OS; 0xC1900101 means a driver crashed, failed to migrate, or blocked the process. The extended code after it (for example 0x20017 or 0x40017) pinpoints the phase where it failed."
  - q: "Which drivers most often cause 0xC1900101?"
    a: "Storage controller drivers, outdated BIOS-level drivers, third-party antivirus filter drivers, and old peripheral drivers (printers, docks, USB devices) top the list. On laptops, the storage and chipset drivers are the prime suspects. Updating these two first resolves the majority of cases without needing to identify the exact culprit."
  - q: "Can I update if I don't know which driver is at fault?"
    a: "Yes — the generic sequence works without identifying the driver: update BIOS and chipset/storage drivers, disconnect peripherals, remove third-party antivirus, and retry. The setup logs (setuperr.log) can identify the exact driver if you want certainty. In practice the generic sequence succeeds often enough that most people never need to open the logs."
  - q: "Does 0xC1900101 mean my hardware is incompatible?"
    a: "No. It means a driver misbehaved during migration, not that the hardware cannot run Windows 11 24H2. After updating or removing the offending driver, the same hardware usually upgrades cleanly. The code describes a software migration failure, not a hardware capability verdict, so treat it as a driver problem first."
---

Error 0xC1900101 is the signature failure of Windows feature updates: the upgrade runs, reaches a percentage, then rolls back with a code that looks like alphabet soup. On Windows 11 24H2 it most often appears during the second boot phase, when the new OS tries to bring your existing drivers along — and one of them refuses to cooperate.

The extended code matters. 0xC1900101 with 0x20017 points at a boot-phase driver failure; with 0x40017 it points at the second-boot migration. You do not strictly need to decode it, because the fix sequence is the same either way: update the critical drivers, strip the peripherals, remove filter drivers, and retry.

This guide follows the order Microsoft's own escalation engineers use. If your failure is on the older OS instead, the same driver-first logic applies — but stay here for 24H2 specifics, including the log locations that identify the exact offending driver.

## Why this happens

- **Outdated storage controller driver:** The storage driver must work in the new OS from the first boot. An old AHCI/RAID/NVMe driver that 24H2 cannot migrate triggers the rollback.
- **Third-party antivirus filter drivers:** AV products install file-system filter drivers. If they are not 24H2-ready, they crash during migration and abort the upgrade.
- **Old BIOS/UEFI firmware:** Firmware bugs in power management or storage handoff surface during the upgrade's boot phases, failing driver initialization.
- **Peripheral drivers:** Printers, docks, USB serial devices, and old webcam drivers load at boot and can wedge the migration.
- **Corrupt driver store:** The DriverStore holds every installed driver package. Corruption here makes migration fail even when the individual drivers are current.
- **Insufficient reserved partition space:** The upgrade stages boot files on the system partitions; a full recovery or EFI partition can abort the second-boot phase.
- **Overclocking or aggressive firmware settings:** Non-standard storage modes (IDE legacy mode, aggressive timings) destabilize the boot environment the upgrade depends on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decode the extended code and check the logs

The full error code tells you which phase failed, and the setup logs name the driver. Ten minutes here can save hours of guessing.

1. Note the full code, e.g. 0xC1900101 - 0x20017 (SAFE_OS boot failure) or - 0x40017 (second boot failure).
2. Open `C:\$WINDOWS.~BT\Sources\Panther\setuperr.log` and look at the final errors before the rollback — driver file names (.sys) appear here.
3. Also check `C:\Windows\Logs\MoSetup\` for the modern setup log.
4. If a specific .sys file is named, update or remove that device's driver first, then continue.

### Fix 2: Update BIOS, chipset, and storage drivers

This single step resolves most 0xC1900101 cases. The upgrade needs firmware and storage drivers that are explicitly 24H2-ready.

1. Download the latest BIOS/UEFI for your exact laptop model from the manufacturer and install it with the charger connected.
2. Install the latest chipset and storage (AHCI/NVMe/IRST) drivers from the manufacturer — not just what Windows Update offers.
3. For Intel-based laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can identify current chipset drivers.
4. Reboot and confirm the new versions in Device Manager before retrying.

### Fix 3: Disconnect all non-essential peripherals

Every attached device is a driver that must migrate. Fewer devices means fewer chances for one to abort the upgrade.

1. Unplug printers, docks, USB hubs, external drives, and USB headsets.
2. Remove SD cards and disable Bluetooth devices temporarily.
3. Keep only the charger, and a wired keyboard/mouse if you need them.
4. Retry the update with the minimal configuration.

### Fix 4: Remove third-party antivirus and filter drivers

Antivirus filter drivers are the most common software cause of 0xC1900101. Disabling is not enough — the filter driver still loads.

1. Uninstall third-party antivirus completely (Windows Security activates automatically).
2. Also remove other filter-driver software: third-party disk encryption trials, old VPN clients, and CD/DVD emulation tools.
3. Reboot, then retry the update. Reinstall your security software after 24H2 is running.

### Fix 5: Clean the driver store and free partition space

A corrupt driver store or full system partition will fail the upgrade no matter how current your drivers are.

1. Run Disk Cleanup including system files, and ensure 20 GB+ free on C:.
2. In Disk Management, check that the EFI and recovery partitions are not 100% full.
3. From an elevated prompt, run `pnputil /enum-drivers` and remove ancient duplicate driver packages for hardware you no longer own.
4. Retry the update.

### Fix 6: Retry with the Installation Assistant or mounted ISO

If Windows Update's attempt keeps failing at the same phase, run the upgrade outside the Windows Update client. The [step-by-step 24H2 feature update sequence](/articles/how-to-fix-feature-update-to-windows-11-24h2-failed-step-by-step/) covers this retry path in full detail.

1. Download the Windows 11 Installation Assistant or ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it with peripherals disconnected and antivirus removed as above.
3. The standalone installer uses the same engine but skips the Windows Update client's state, which is sometimes the actual blocker.
4. If this attempt also fails, the Panther logs from Fix 1 will show whether it is the same driver — compare before and after.

### Fix 7: Do an in-place repair only after the driver is identified

When the same driver fails across every method, remove it surgically rather than reinstalling Windows.

1. Identify the .sys file from setuperr.log as in Fix 1.
2. In Device Manager, uninstall that device and tick 'delete the driver software' if offered.
3. For a deeper look at feature-update-specific failures on your brand of laptop, the [HP 24H2 feature update guide](/articles/how-to-fix-feature-update-to-windows-11-24h2-failed-on-hp-laptop/) covers the same driver-first sequence with vendor specifics.
4. Retry the upgrade. If the hardware is genuinely unsupported, this is the point where the logs prove it — anything earlier is just a driver problem.

## Closing

Error 0xC1900101 looks intimidating, but it is Windows telling you a driver crashed the upgrade — not that your laptop is obsolete. Update the BIOS and storage drivers, strip peripherals and filter drivers, read the Panther logs to name the culprit, and retry. The same hardware that rolled back almost always upgrades cleanly once the offending driver is handled.
