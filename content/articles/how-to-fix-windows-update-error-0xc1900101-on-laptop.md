---
title: "Fix Windows Update Error 0xC1900101 on Laptop (Driver Fix Guide)"
slug: how-to-fix-windows-update-error-0xc1900101-on-laptop
date: 2026-09-17
categories: ["windows-update"]
tags: ["windows update error 0xc1900101", "feature update failed", "driver incompatibility", "0xc1900101 fix"]
description: "Error 0xC1900101 means a driver blocked your Windows feature update. Identify the bad driver, update it, and get the upgrade through."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0xc1900101-on-laptop.webp"
faqs:
  - q: "What does error 0xC1900101 mean?"
    a: "It is the generic failure code for Windows feature updates, upgrades to a new Windows version, that roll back because of a driver problem. The last digits of the extended code indicate which phase failed, but in nearly all cases an incompatible, outdated, or corrupt driver is the cause."
  - q: "Which drivers most often cause 0xC1900101?"
    a: "Storage controller drivers, graphics drivers, and network drivers top the list, followed by chipset drivers and third-party antivirus filter drivers. Disconnecting peripherals also helps because their drivers load during setup and any one of them can derail the upgrade."
  - q: "Should I update my BIOS to fix 0xC1900101?"
    a: "It can help, especially on laptops where the manufacturer released BIOS updates improving Windows 11 compatibility. Only update from your manufacturer's official support page, with the charger connected, and never interrupt the flash once it starts until the system reboots on its own."
  - q: "Can I find exactly which driver failed?"
    a: "Yes. After a rollback, run Microsoft's SetupDiag tool on the setup logs in the hidden $Windows.~BT folder. It parses the logs and usually names the specific driver or phase that caused the failure, turning guesswork into a targeted fix."
---

Error 0xC1900101 is the signature failure of Windows feature updates — the big twice-yearly upgrades — and it almost always means one thing: a driver got in the way. The upgrade progressed, hit a driver it could not migrate or initialize, and rolled the whole thing back to keep your laptop working.

The maddening part is that Windows rarely names the offender. You get the code, a rollback, and a machine that looks exactly as it did before, with no hint about which of your dozens of drivers caused the wreck. The extended error code's trailing digits encode the phase, but for practical purposes the fix is the same: modernize the driver stack and remove the variables.

Laptops have some specific wrinkles here — OEM storage drivers, manufacturer power management, and docks full of peripherals. The steps below address the laptop-specific triggers first, then the general driver hygiene that gets feature updates across the finish line.

## Why this happens

- **Outdated storage controller driver.** The number one trigger on laptops: an old Intel RST, AMD, or NVMe driver that the new Windows build cannot migrate.

- **Incompatible graphics driver.** Aging GPU drivers, especially on laptops with switchable graphics, frequently fail the upgrade's driver migration.

- **Third-party antivirus filter drivers.** AV products hook deep into the storage and network stacks, and their drivers can block the upgrade phases.

- **Connected peripherals.** USB devices, docks, and external drives load their drivers during setup and any one of them can derail it.

- **Insufficient free disk space.** Feature updates need 20 GB or more of working space; a cramped drive aborts the upgrade mid-flight.

- **Outdated BIOS or firmware.** Old firmware can misreport hardware to the new OS build, failing compatibility checks deep in setup.

- **Corrupt driver store.** Damaged driver packages in the DriverStore confuse the migration engine even when the installed drivers are current.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Disconnect all peripherals

The single highest-yield step. Every USB device, dock, SD card, and external drive brings a driver into setup, and removing them eliminates a whole category of failures at once. Bluetooth dongles, printer USB cables, and even wired Ethernet adapters count here; if it connects via USB and is not essential, unplug it for the upgrade.

1. Unplug everything USB except a wired keyboard and mouse if you need them.
2. Remove SD cards, disconnect docks, and unplug external monitors if possible.
3. Retry the feature update with the bare laptop.

### Fix 2: Fix 2: Update storage, chipset, and graphics drivers

Modernize the three driver families that cause most 0xC1900101 rollbacks. Get them from the laptop manufacturer's support page rather than generic Windows Update versions where possible. Reboot between each driver install so the new driver is actually live before you layer the next one on top; stacking installs without rebooting is a classic source of false confidence.

1. Visit your manufacturer's support page, Dell, HP, or Lenovo, and download the latest chipset, storage (Intel RST/AMD), and graphics drivers for your exact model.
2. Install the chipset driver first, then storage, then graphics, restarting between each.
3. Retry the feature update. Intel users can also run the [Intel Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch stragglers.

### Fix 3: Fix 3: Uninstall third-party antivirus temporarily

Antivirus filter drivers are a classic upgrade blocker. Windows Security (Defender) takes over automatically while the third-party product is gone, so you are not unprotected during the test. Download the vendor's removal tool before you uninstall, since you will want it handy while the standard antivirus is gone and you should avoid browsing for it unprotected.

1. Open Settings, then Apps, then Installed apps, and uninstall your third-party antivirus.
2. Use the vendor's official removal tool as well, since AV products leave filter drivers behind otherwise.
3. Retry the update, then reinstall your antivirus afterward if you prefer it.

### Fix 4: Fix 4: Free up disk space

Feature updates stage gigabytes of files. If the drive is nearly full, setup fails partway with this code rather than warning you upfront. The $Windows.~BT and $Windows.~WS folders from previous failed upgrades also consume gigabytes; Disk Cleanup's system-files mode can remove them safely.

1. Open Settings, then System, then Storage, and confirm at least 20 to 30 GB free on C:.
2. Run Disk Cleanup including system files, targeting Windows Update Cleanup and temporary files.
3. Move large personal files to external storage if needed, then retry.

### Fix 5: Fix 5: Clean-boot before upgrading

Background utilities, especially OEM control panels and RGB software, install drivers and services that interfere with setup. A clean boot quiets them all. Pay special attention to OEM utilities for fan control, keyboard lighting, and battery management, which install kernel drivers that setup frequently chokes on.

1. Press Win + R, type `msconfig`, hide all Microsoft services, and disable the rest.
2. Disable every startup item in Task Manager, restart, and attempt the update.

### Fix 6: Fix 6: Update the BIOS from the manufacturer

On laptops of the Windows 10 to 11 transition era, BIOS updates frequently contain the compatibility fixes that unblock feature updates. This is a targeted fix, not a guess. If the manufacturer's site lists the BIOS update as urgent or security-related, install it regardless of the update error; those fixes matter beyond this upgrade.

1. Find your exact model on the manufacturer's support site and check for BIOS updates mentioning Windows 11 or upgrade compatibility.
2. Connect the charger, close all programs, and run the BIOS update without touching the machine.
3. After it reboots, retry the feature update.

### Fix 7: Fix 7: Run SetupDiag, then upgrade via ISO

If it still rolls back, get the actual answer from the logs. SetupDiag reads the setup failure logs and names the failing driver or phase, and upgrading from mounted ISO media bypasses Windows Update quirks entirely. Keep the SetupDiag report saved with your troubleshooting notes; if a future feature update fails the same way, the report tells you instantly whether it is the same driver.

1. Download Microsoft's SetupDiag tool and run it after a failed attempt; read its report for the named driver.
2. Update or remove the named driver.
3. Download the ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run setup.exe, and upgrade. For keeping drivers current generally, see our guide on [updating drivers on a Windows 11 laptop](/articles/how-to-update-drivers-on-windows-11-laptop/).

## Closing

Error 0xC1900101 is Windows protecting you from a bad driver combination by rolling back, which is cold comfort when the upgrade fails for the fifth time. Strip the peripherals, modernize storage, chipset, and graphics drivers, and clear the antivirus and disk-space variables, and the feature update will complete. Keep drivers maintained afterward with our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/). If the upgrade fails even with a healthy driver stack — stalling on setup screens, partition errors, or a hung progress bar — the failure is no longer driver-driven; our [Windows 11 installation-failed guide](/articles/how-to-fix-windows-11-installation-failed/) covers the storage, media, and setup-environment causes. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official upgrade troubleshooting path.
