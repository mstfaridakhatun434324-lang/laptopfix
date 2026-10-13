---
title: "Driver Updates Failing in Windows Update After a Windows 11 Update — How to Fix Them"
slug: how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update
date: 2026-09-09
categories: ["windows-update"]
tags: ["driver updates failing", "windows update", "driver install error", "windows 11", "device manager"]
description: "Driver updates keep failing in Windows Update after a Windows 11 update? Diagnose which driver is stuck and get it installed cleanly with these ordered fixes."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update.webp"
faqs:
  - q: "Why do driver updates fail in Windows Update but the OS updates succeed?"
    a: "OS updates and driver updates travel through the same pipeline but have different failure modes. Drivers must match your exact hardware IDs and pass signature checks, and they interact with the currently loaded driver — which cannot always be replaced while running. A mismatch between the offered driver and your hardware revision, or a locked driver file, fails the driver package while the OS components install fine."
  - q: "Should I install drivers from Windows Update or the manufacturer?"
    a: "For laptops, prefer the manufacturer's support site. OEMs validate drivers against their firmware and custom hardware, while Windows Update sometimes offers a generic or newer-but-untested version that fails to install or causes instability. Use Windows Update drivers only when the manufacturer has not published one for your OS build, or for generic peripherals."
  - q: "What does error 0x80070103 mean on a driver update?"
    a: "It means Windows Update is trying to install a driver that is already installed or older than the one you have — essentially a redundant offering. It is harmless and you can safely hide the update. If you see it repeatedly, the manufacturer's newer driver is already in place and Windows Update's catalog is simply out of sync with your system."
  - q: "Can a failing driver update damage my laptop?"
    a: "Almost never. Failed driver installs roll back automatically, leaving the previous working driver in place — that is why the device keeps working despite the red entry in Update history. The real risk is repeatedly forcing installs of the wrong driver, which can cause instability. Identify the correct driver from the manufacturer and install it once, cleanly, instead."
---

After a Windows 11 update, opening Windows Update to find one or more driver updates marked "failed" is a common sight — and a confusing one, because the rest of the system works fine. The explanation is structural: driver packages have to match your exact hardware IDs, pass signature validation, and replace files that may currently be in use. Any mismatch aborts the driver install while the OS update sails through, leaving you with a persistent red entry that retries — and re-fails — on every scan.

The right response is not to keep hammering "Retry." Each failed attempt is telling you something: the offered driver does not fit your hardware, the download is corrupt, or the existing driver is locked. Your job is to identify which driver is failing, get the correct package from the right source, and install it cleanly once. The steps below walk that process in order.

Start in Update history (Settings, then Windows Update, then Update history). Expand the failed driver entry and note two things: the device it targets (display adapter, Wi-Fi, audio, and so on) and the error code. 0x80070103 means the driver is already installed — harmless. Anything else deserves the full treatment below.

## Why this happens

- **Hardware ID mismatch:** the offered driver targets a slightly different hardware revision than yours.
- **A newer manufacturer driver already installed:** Windows Update's catalog lags behind, offering an older package that the system correctly rejects.
- **Corrupted driver download:** a bad package in the update cache fails integrity checks on every retry.
- **The current driver is locked in use:** some drivers cannot be replaced while loaded, and the installer gives up instead of scheduling properly.
- **Signature validation failure:** the package's signature does not validate against the system's trusted publishers.
- **Pending reboot blocking installation:** a previous install left the servicing stack waiting on a restart.
- **Third-party driver updaters conflicting:** external tools can install competing versions that confuse Windows Update's detection.
- **Corrupted driver store:** damage in the system's driver repository breaks staging for new packages.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing driver precisely

You cannot fix what you have not named. Pin down the device and the error before touching anything.

1. Open Settings, then Windows Update, then Update history, and expand the failed driver entry.
2. Record the device name and the error code.
3. Open Device Manager, find the device, and check its current driver version and date on the Driver tab.
4. If the installed driver is newer than what Windows Update offers, you have a 0x80070103-style redundant offering — hide it and move on.
5. For genuine failures, continue below. If the broader update pipeline is unhealthy, our [update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) is worth a read, and the [24H2-specific driver failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) covers the stricter validation rules of the newest build.

### Fix 2: Get the correct driver from the manufacturer

For laptops, the OEM's driver is almost always the right one — validated against your firmware and hardware revision.

1. Go to your laptop manufacturer's support page (Dell, HP, Lenovo, ASUS, or Acer) and enter your exact model or serial number.
2. Download the driver for the failing device, choosing the version for your Windows 11 build.
3. For Intel-based graphics, Wi-Fi, or Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also identify the correct package.
4. Save the installer where you can find it, but do not run it yet.

### Fix 3: Cleanly remove the problem driver first

Installing over a corrupted or locked driver often just reproduces the failure. Remove it cleanly, then install fresh.

1. In Device Manager, right-click the failing device and choose Uninstall device.
2. If offered, tick "Attempt to remove the driver for this device" — for GPUs, consider Display Driver Uninstaller in Safe Mode for a truly clean slate.
3. Reboot. Windows will load a basic fallback driver.
4. Run the manufacturer's installer you downloaded in Fix 2.
5. Reboot again and verify the device works correctly in Device Manager.

### Fix 4: Hide the bad offering in Windows Update

Once the correct driver is installed manually, stop Windows Update from re-offering the broken package.

1. Run Microsoft's show-or-hide updates troubleshooter (wushowhide.diagcab).
2. Choose Hide updates and select the failing driver entry.
3. Confirm it no longer appears in the update scan.
4. Document which driver you hid and why — future you will thank present you.
5. Unhide it only if a newer revision appears that you actually want.

### Fix 5: Reset the update cache

If the failure is a corrupt download rather than a wrong driver, a cache reset forces a clean re-download.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services and reboot.
5. Check whether the driver now downloads and installs cleanly. Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) cover this reset officially.

### Fix 6: Roll back a driver that a Windows update broke

Sometimes the sequence is reversed: a Windows 11 update replaced a working OEM driver with a broken generic one. The fix is to go backward.

1. In Device Manager, open the device's Properties and go to the Driver tab.
2. If available, click Roll Back Driver and choose a reason.
3. Reboot and test the device thoroughly.
4. Then hide the offending driver update as in Fix 4 so it is not reinstalled.
5. Report the bad driver to the manufacturer — they cannot fix what they do not know about.

### Fix 7: Repair the servicing stack as a last resort

When driver updates fail across multiple unrelated devices, the problem is the pipeline, not the drivers.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Retry the driver updates.
4. If failures persist, perform an in-place upgrade repair using the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
5. After the repair, install manufacturer drivers first, then let Windows Update handle the rest.

## Closing

Failing driver updates look alarming in Update history but are usually a sourcing problem, not a system problem: the wrong package for your hardware, a corrupt download, or a catalog offering you do not need. Identify the device, get the driver from the manufacturer, install it cleanly once, and hide the bad offering. That four-step rhythm resolves the vast majority of these failures permanently — no registry edits, no driver-updater utilities, no drama.
