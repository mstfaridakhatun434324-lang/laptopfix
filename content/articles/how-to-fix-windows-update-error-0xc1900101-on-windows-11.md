---
title: "Fix Windows Update Error 0xc1900101 on Windows 11 (Upgrade Rolls Back)"
slug: how-to-fix-windows-update-error-0xc1900101-on-windows-11
date: 2026-10-05
categories: ["windows-update"]
tags: ["windows update", "0xc1900101", "drivers", "upgrade rollback", "windows 11"]
description: "Error 0xc1900101 rolls back Windows 11 upgrades — almost always a driver problem. Find the bad driver and complete your upgrade."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0xc1900101-on-windows-11.webp"
faqs:
  - q: "What do the extended codes like 0x20017 mean?"
    a: "They identify the upgrade phase that failed: 0x20017 points to the SAFE_OS boot phase (often driver or firmware), 0x40017 to the second-boot phase. The base code 0xc1900101 always means a driver-related rollback on Windows 11; the extension tells a technician where in setup the failure occurred, which narrows which drivers to suspect first."
  - q: "Why does Windows roll back instead of finishing the upgrade?"
    a: "Because booting into a half-migrated system with a broken critical driver — especially storage or display — could leave the PC unbootable. The rollback restores your known-working installation automatically. It is deliberately conservative: a failed upgrade you can retry beats a successful-looking upgrade that never boots."
  - q: "Should I update drivers before or after the upgrade?"
    a: "Before. The upgrade migrates your existing drivers into the new system, so the drivers present at upgrade time are the ones that must work. Updating chipset, storage, display, and network drivers first — from the manufacturer or Intel's Driver & Support Assistant — gives setup the best possible starting set."
  - q: "How do I find which driver caused 0xc1900101?"
    a: "Check C:\\$Windows.~BT\\Sources\\Panther\\setuperr.log and setupact.log after a failed attempt — they record driver load failures with device names. Device Manager warning icons after the rollback also hint at suspects. Fix or remove the named driver, then retry the upgrade with peripherals disconnected."
---
Error 0xc1900101 is the signature of a failed Windows 11 upgrade that rolled itself back: setup got far enough to hit a driver it could not live with — storage, display, network, or a filter driver — and chose the safe path of restoring your previous system rather than booting into a broken one. The rollback is actually good engineering; the frustration is that the code alone rarely names the driver.

Your investigation therefore has two phases: read the setup logs to identify the failing driver (or apply the usual suspects in order), remove or update the offender, and rerun the upgrade in a clean, minimal-driver environment. The fixes below follow exactly that sequence.

If update services themselves are misbehaving more broadly, the [update service troubleshooting guide](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/) covers that angle, and when the failure is a hung installer rather than a rollback, the [companion guide for 0x8024200d](/articles/how-to-fix-windows-update-error-0x8024200d-on-windows-11/) is the companion guide. Start by disconnecting the clutter.

## Why this happens

- **An outdated storage driver cannot migrate:** Storage drivers load earliest in the new OS; an ancient AHCI, RAID, or NVMe driver that the upgrade cannot initialize aborts the whole attempt and triggers the rollback.
- **The display driver crashes the new system:** GPU drivers deeply hook the kernel. An incompatible display driver can blue-screen the first boot of the upgraded system, which setup interprets as upgrade failure.
- **Antivirus filter drivers block the migration:** Third-party antivirus installs file-system filter drivers that the new OS may refuse to load; their failure cascades into a rollback.
- **A peripheral's driver misbehaves during setup:** USB devices with poor drivers — docks, printers, exotic input devices — get enumerated during upgrade, and one bad driver can poison the entire driver-migration phase.
- **BIOS/firmware is too old for the new OS:** Firmware exposes hardware to the OS; outdated BIOS/UEFI can present devices in ways the new Windows build does not expect, failing driver initialization.
- **The driver store holds corrupted packages:** Corrupted third-party driver packages in the driver store get staged into the new installation and fail there, even though the running system tolerates them.
- **Overclocking or marginal hardware destabilizes setup:** Aggressive RAM timings or CPU overclocks that are stable in daily use can produce errors under setup's heavy, sustained load, failing driver verification phases.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disconnect all non-essential peripherals

The cheapest high-yield step in 0xc1900101 troubleshooting: unplug everything the upgrade does not need — docks, printers, USB drives, external webcams, SD cards, even the mouse if the touchpad suffices. Every removed device is one fewer driver for setup to migrate.

1. Shut the laptop down fully.
2. Unplug all USB devices, docks, external monitors, printers, and SD cards.
3. If docked, undock and run on the laptop's own keyboard and display.
4. Power on and retry the upgrade from Settings > Windows Update or the Windows 11 installation media.
5. If it succeeds, reconnect peripherals one at a time afterward to find the offender.

### Fix 2: Update all critical drivers before retrying

Ancient drivers are the headline cause, so modernize the big four before the next attempt: chipset, storage, display, and network. Your laptop manufacturer's support site has validated bundles; the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) covers Intel chipset and graphics on Intel-based machines.

1. Visit your manufacturer's support site (Dell, HP, or Lenovo) and download the latest chipset, storage, and BIOS-adjacent driver bundles for your exact model.
2. Run the Intel Driver & Support Assistant for Intel components.
3. Update discrete graphics from the [NVIDIA driver download](https://www.nvidia.com/Download/index.aspx) or [AMD driver support](https://www.amd.com/en/support/download/drivers.html) page as applicable.
4. Restart after all driver updates, then retry the upgrade.

### Fix 3: Uninstall third-party antivirus completely

Disabling is not enough for 0xc1900101: antivirus filter drivers load at boot whether the UI is on or off, and they participate in the upgrade's driver migration. Full uninstallation — using the vendor's removal tool — takes their drivers out of the equation entirely.

1. Download your antivirus vendor's official removal tool.
2. Run it and choose complete uninstallation, then restart.
3. Confirm Windows Security shows active protection afterward.
4. Retry the upgrade from Settings > Windows Update or the Windows 11 installation media.
5. Reinstall your preferred antivirus only after the upgrade completes successfully.

### Fix 4: Update the BIOS/UEFI firmware

Outdated firmware is a quiet but real 0xc1900101 contributor: it governs how storage, power, and devices present themselves to the new OS. Manufacturers release BIOS updates specifically validated for new Windows builds, and applying them before the upgrade removes firmware-level incompatibilities.

1. Find your exact model on the manufacturer's support site (Dell, HP, or Lenovo).
2. Download the latest BIOS/UEFI update validated for your Windows version.
3. Connect AC power, close all programs, and run the updater.
4. Do not touch the laptop until the firmware update completes and the system reboots.
5. Retry the Windows upgrade afterward.

### Fix 5: Free space and verify the system partitions

Upgrades need working room — 20GB+ free — plus healthy system partitions. A choked drive or a damaged recovery/EFI partition can fail the upgrade in ways that surface as the generic 0xc1900101. Disk Cleanup plus a partition health check covers both.

1. Run Disk Cleanup as administrator with Clean up system files and remove old update data.
2. Confirm at least 20GB free on the system drive.
3. Open Disk Management (`diskmgmt.msc`) and confirm the EFI and recovery partitions show Healthy.
4. Run `chkdsk C: /f` to verify file-system integrity.
5. Retry the upgrade with ample free space confirmed.

### Fix 6: Run the upgrade in a clean boot from installation media

The full-surround approach: minimal drivers, minimal services, and the upgrade launched from fresh installation media rather than Windows Update. A clean boot silences third-party drivers and services; media-based setup uses the newest setup engine. Combined with the earlier fixes, this succeeds in the large majority of persistent 0xc1900101 cases.

1. Perform a clean boot via `msconfig` (hide Microsoft services, disable all others and all startup items).
2. Create fresh the Windows 11 installation media so setup is the latest build.
3. Disconnect peripherals and connect AC power.
4. Run setup.exe from the media and choose to keep files and apps.
5. If it still fails, examine C:\$Windows.~BT\Sources\Panther\setuperr.log for the named driver, fix that driver specifically, and retry.

## Closing

Error 0xc1900101 is Windows 11 protecting you from a driver it cannot trust in the new system — the rollback is the safety net working. Simplify the hardware, modernize the drivers, remove the antivirus filters, update the firmware, and the upgrade goes through. Read setuperr.log when it does not; the log almost always names the exact driver, turning the next attempt from a guess into a targeted repair.
