---
title: "Driver Updates Keep Failing in Windows Update on Windows 11 24H2 — How to Fix It"
slug: how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2
date: 2026-09-24
categories: ["windows-update"]
tags: ["driver updates failing", "windows 11 24h2", "windows update", "driver error", "device manager"]
description: "Driver updates keep failing in Windows Update on Windows 11 24H2? Find the stuck driver, install the right package, and stop the failure loop."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Why does 24H2 fail driver updates that older builds installed fine?"
    a: "Version 24H2 enforces stricter driver validation — tighter signature checks, new requirements around memory integrity and virtualization-based security, and updated driver frameworks. A driver that installed under looser rules on 23H2 can now fail validation outright. The fix is to get the 24H2-ready driver from your laptop manufacturer, since vendors update their packages to meet the new requirements while Windows Update's catalog may lag."
  - q: "Which drivers fail most often on 24H2?"
    a: "Graphics drivers lead the list, followed by Wi-Fi and Bluetooth (especially Intel and MediaTek packages), audio drivers with custom OEM enhancements, and storage controller drivers. These are the drivers most deeply integrated with the OS, so they face the strictest migration checks. If Update history shows one of these failing repeatedly, go straight to the manufacturer's 24H2-specific package."
  - q: "Should I turn off driver updates in Windows Update entirely?"
    a: "You can reduce them via Device Installation Settings, but fully disabling is not recommended — you would miss security-relevant driver fixes. The better approach is selective: let Windows Update offer drivers, hide the specific ones that fail with the show-or-hide troubleshooter, and source those devices' drivers from the manufacturer. You keep the pipeline open while quarantining only the problem packages."
  - q: "Can a failing driver update cause the undoing changes rollback?"
    a: "Yes. When a driver package is bundled into a cumulative or feature update transaction and fails migration, the entire transaction can abort and roll back — which is why some readers arrive here from the undoing-changes screen. Fixing the driver failure with the steps in this guide often resolves the rollback loop as a side effect, since the transaction no longer has a failing component."
---

On Windows 11 24H2, driver updates fail in Windows Update more visibly than on earlier builds — and there is a reason. 24H2 tightened driver validation across the board: stricter signature enforcement, new memory-integrity expectations, and updated driver frameworks mean packages that slipped through on 23H2 now fail loudly in Update history. The OS updates themselves install fine; it is the driver payloads that keep showing red.

The pattern to recognize: the same driver, the same error, on every scan. That repetition is diagnostic gold — it tells you the offered package does not fit your hardware or the download is corrupt, and retrying will never change the outcome. The fix is a sourcing problem, not a persistence problem: identify the device, get the 24H2-ready driver from the manufacturer, install it cleanly once, and hide the bad offering so the loop ends.

Start in Update history (Settings, then Windows Update, then Update history). Expand the failed driver entry, note the device and the error code, and check whether your installed driver is already newer — 0x80070103 means Windows Update is offering you a downgrade you should simply hide.

## Why this happens

- **24H2's stricter driver validation:** signature and security requirements that older packages cannot meet.
- **Windows Update catalog lag:** the offered driver predates the manufacturer's 24H2-ready release.
- **Hardware revision mismatch:** the package targets a slightly different revision of your device.
- **A newer OEM driver already installed:** the system correctly rejects an older offered version.
- **Corrupted driver download:** a bad package failing integrity checks on every retry.
- **The loaded driver blocking replacement:** files in use that the installer cannot swap.
- **Pending reboot:** a previous install leaving the servicing stack waiting.
- **Damaged driver store:** corruption in the system's driver repository breaking staging.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing driver and check for a redundant offering

Name the device and rule out the harmless case before doing real work.

1. In Update history, expand the failed driver entry and record the device name and error code.
2. Open Device Manager, find the device, and note the installed driver version and date.
3. If the installed driver is newer than the offered one (typical with 0x80070103), hide the update and stop — there is nothing to fix.
4. For genuine failures, note whether it is graphics, Wi-Fi, audio, or storage — the usual 24H2 suspects.
5. If the whole update pipeline looks unhealthy, the [update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) is worth reading alongside.

### Fix 2: Download the 24H2-ready driver from the manufacturer

On 24H2, the manufacturer's package is not just preferred — it is often the only one that passes validation.

1. Go to your laptop manufacturer's support site and enter your exact model.
2. Download the driver for the failing device, explicitly choosing the Windows 11 24H2 version where offered.
3. For Intel graphics, Wi-Fi, or Bluetooth, cross-check with the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. For NVIDIA or AMD graphics, get the notebook driver from the manufacturer's page first, vendor second.
5. Save the installer; do not run it until the old driver is cleanly removed.

### Fix 3: Remove the old driver cleanly, then install fresh

Layering a new driver over a broken install reproduces the failure. Clean slate first.

1. In Device Manager, right-click the device and choose Uninstall device.
2. Tick "Attempt to remove the driver for this device" if offered; for GPUs, use Display Driver Uninstaller in Safe Mode for stubborn cases.
3. Reboot — Windows loads a basic fallback driver.
4. Run the manufacturer's installer from Fix 2.
5. Reboot again and verify the device in Device Manager shows the new version with no warnings.

### Fix 4: Hide the failing Windows Update offering

With the correct driver installed, stop Windows Update from re-offering the broken package.

1. Run Microsoft's show-or-hide updates troubleshooter.
2. Select Hide updates and choose the failing driver entry.
3. Verify it disappears from the next update scan.
4. Note what you hid and why for future reference.
5. This quarantine is per-package — other drivers continue updating normally.

### Fix 5: Reset the update cache for corrupted downloads

When the failure is a bad package rather than a wrong one, force a clean re-download.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services, reboot, and check for updates.
5. Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) document this reset as the standard corruption fix.

### Fix 6: Check memory integrity and driver compatibility settings

24H2-specific: memory integrity (HVCI) can block drivers that are not compatible with it.

1. Open Windows Security, then Device security, then Core isolation details.
2. Note whether Memory integrity is on — and whether Windows lists incompatible drivers.
3. If the failing driver is flagged incompatible, the manufacturer's 24H2-ready version is mandatory; do not disable memory integrity to accommodate an old driver.
4. Install the updated driver, reboot, and confirm memory integrity stays on.
5. Retry Windows Update to confirm the driver entry clears.

### Fix 7: Repair the servicing stack

Multi-device driver failures indicate pipeline damage, not driver problems.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Retry the driver updates.
4. If failures persist, do an in-place upgrade with the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
5. Afterward, install manufacturer drivers first — a lesson our [general driver-failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) reinforces — then let Windows Update handle the rest.

## Closing

Driver update failures on 24H2 are validation failures wearing an install error's clothes: the package does not meet the build's requirements, does not match your hardware, or arrived corrupted. Identify the device, source the 24H2-ready driver from the manufacturer, install it cleanly, and quarantine the bad offering. Do that once per device and Update history goes green — and stays green, because the right driver does not need to be installed twice.
