---
title: "Driver Updates Failing in Windows Update on Windows 10 (Fix)"
slug: how-to-fix-driver-updates-failing-in-windows-update-on-windows-10
date: 2026-09-24
categories: ["windows-update"]
tags:
  - windows 10
  - driver updates
  - windows update
  - device drivers
  - troubleshooting
description: "On Windows 10 and driver updates keep failing in Windows Update? Use these Windows 10-specific fixes: hide the bad driver, install it manually, and stop the loop."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-on-windows-10.webp"
faqs:
  - q: "What is error 0x80070103 when installing a driver?"
    a: >
      It means Windows tried to install a driver that is older than, or identical to, the one already on your system. It is not a real failure of your hardware — it is a versioning disagreement. The correct response is to hide that driver update with the wushowhide troubleshooter so Windows stops offering it, since your installed driver is already equal or better.
  - q: "Where is wushowhide on Windows 10?"
    a: >
      Microsoft offers it as a small downloadable troubleshooter (wushowhide.diagcab) — it is not built into Settings. Run it, choose Hide updates, and tick the driver you want to block. The tool works on Windows 10 and remains the officially supported way to skip a specific driver update without disabling updates wholesale. Microsoft documents the broader update-repair options on the [Windows support hub](https://support.microsoft.com/en-us/windows).
  - q: "Will hiding a driver update affect security updates?"
    a: >
      No. The Show or hide updates tool only affects the specific driver package you tick. Security patches, cumulative updates, and feature updates continue to download and install normally. You can also unhide the driver later by running the tool again and choosing Show hidden updates.
  - q: "Should I upgrade to Windows 11 to fix driver update problems?"
    a: >
      Not for this reason alone. Windows 11 has the same driver update machinery and the same failure modes. Fix the underlying issue — usually a stale catalog driver or a corrupted driver store — on Windows 10 first. Upgrade only when you want Windows 11's features and your laptop meets its requirements, not as a troubleshooting step.
---

Windows 10 handles driver updates differently from Windows 11 — the settings live in different places, the old Control Panel paths still work, and Microsoft's Show or hide updates tool was practically built for this operating system. If driver updates keep failing on your Windows 10 laptop, the fixes below are tuned to exactly that environment.

The pattern is familiar: Update history shows the same driver failing with 0x80070103 or a similar code, each retry downloads it again, and nothing you click makes it stick. On Windows 10 this very often means the offered driver is older than what you already installed through your laptop maker's utility.

This guide uses Windows 10's own dialogs and tools — no Windows 11 paths, no guesswork — to identify the failing driver, get the right one installed, and hide the bad offering for good.

## Why this happens

- **Offered driver older than the installed one:** the classic 0x80070103: your vendor utility installed a newer driver, and Windows Update keeps pushing its older catalog copy.
- **Windows 10 driver ranking quirks:** Windows 10's driver ranking sometimes prefers the Windows Update driver over a better vendor driver, causing repeated replace-and-fail cycles.
- **Corrupted driver store entries:** half-installed drivers in the DriverStore make every subsequent install attempt fail at the same step.
- **Metered connection pausing driver downloads:** on metered networks Windows 10 may download a partial driver package and then fail the install.
- **Third-party driver updaters conflicting:** aggressive updater tools can swap driver files while Windows Update is installing, failing the install.
- **Insufficient staging space:** driver packages stage on C: first; a nearly full drive fails the staging silently.
- **Deprecated hardware with no good driver:** very old devices may have only a broken driver package in the catalog, and no retry will ever succeed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the failing driver in Update history

Windows 10 keeps the same history view as 11, just reached through a slightly different path. Get the driver name and error code first.

1. Open Settings > Update & Security > Windows Update and click View update history.
2. Expand Driver Updates and note the failing driver's name, version, and error code.
3. If the code is 0x80070103, the offered driver is older than yours — skip straight to Fix 3 after Fix 2.
4. Keep the history open; you will reference it again.

### Fix 2: Try the manual install from Optional updates

Windows 10 (version 2004 and later) lists drivers under Optional updates. The manual path often succeeds where the automatic one fails.

1. Go to Settings > Update & Security > Windows Update and click View optional updates.
2. Expand Driver updates, tick the failing driver, and click Download and install.
3. Wait for it to finish and check the history for a success entry.
4. If it fails again with the same code, the package itself is the problem — continue.

### Fix 3: Hide the failing driver with wushowhide

This Microsoft troubleshooter is the canonical Windows 10 answer to a driver that will never install. Hiding it stops the retry loop without affecting anything else.

1. Download wushowhide.diagcab (Show or hide updates troubleshooter) from Microsoft.
2. Run it, click Next, then choose Hide updates.
3. Tick the failing driver in the list and finish the wizard.
4. Run Check for updates to confirm it no longer appears. Learn how to [disable automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) entirely if this keeps recurring.

### Fix 4: Install the correct driver from your laptop maker

With the bad offering hidden, install the driver properly from the source that knows your exact model — Dell, HP, Lenovo, or ASUS support pages. For Intel graphics, Wi-Fi, or Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects your hardware and fetches the right driver automatically.

1. Open your manufacturer's support site and enter your model or serial number.
2. Download the driver for the failing device, choosing the newest Windows 10 version.
3. Run the installer as administrator and reboot when prompted.
4. Verify in Device Manager that the device shows the new driver version and date.

### Fix 5: Stop Windows 10 reinstalling drivers automatically

If Windows keeps replacing your good vendor driver with its own copy, change the device installation setting so it stops. This is the Windows 10-native way to end the tug-of-war without third-party tools, and it takes effect immediately for every device you connect or reinstall from that point forward.

1. Press Win + R, type sysdm.cpl, and open the Hardware tab.
2. Click Device Installation Settings and choose No (your device might not work as expected).
3. Click Save Changes. Windows will no longer auto-fetch drivers for new devices.
4. Note: this does not remove already-installed drivers — it only stops future automatic swaps.

### Fix 6: Clean the driver store for the problem device

When the DriverStore holds a corrupted package for the device, Device Manager surgery clears it.

1. Open Device Manager (Win + X > Device Manager) and locate the device.
2. Right-click, choose Uninstall device, and tick Delete the driver software for this device.
3. Click Action > Scan for hardware changes to redetect it cleanly.
4. Install the manufacturer's driver from Fix 4 on the clean detection.

### Fix 7: Run SFC and DISM, then do a final update pass

Persistent failures across multiple drivers suggest system image damage. Repair it, then let Windows Update have one clean shot.

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Then run: DISM /Online /Cleanup-Image /RestoreHealth.
3. Reboot, then Settings > Update & Security > Windows Update > Check for updates.
4. Confirm the driver section of update history is clean. For safety before future driver work, [back up your drivers](/articles/best-way-to-backup-drivers-before-update/).

## Closing

Windows 10 driver failures follow a simple script: identify the driver, try the optional-updates manual install, hide the bad package with wushowhide, and install the vendor's driver instead. The Device Installation Settings toggle prevents Windows from undoing your work. Keep this routine — identify, manual-install, hide, vendor driver — and driver updates stop being a monthly annoyance, leaving your Windows 10 laptop stable between Patch Tuesdays.
