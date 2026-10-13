---
title: "Windows Update Error 0x800f020b, Step by Step: Fix the Failed Driver Install"
slug: how-to-fix-windows-update-error-0x800f020b-step-by-step
date: 2026-10-08
categories: ["windows-update"]
tags: ["0x800f020b", "driver update failed", "windows update error", "windows 11", "windows 10"]
description: "Error 0x800f020b means a driver update failed to install via Windows Update. This step-by-step guide identifies the failing driver and gets it installed — or safely hidden."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f020b-step-by-step.webp"
faqs:
  - q: "What does 0x800f020b mean in Windows Update?"
    a: "It is the failure code Windows Update reports when a driver package fails to install. The driver downloaded but the installation step failed — because the driver did not match the hardware, a newer version was already present, the device was missing, or the package itself was corrupt."
  - q: "Is it safe to hide a failing driver update?"
    a: "Yes, when the device works correctly on its current driver. Hiding only tells Windows Update to stop offering that specific package; it does not disable the device or block security updates. If the device later develops problems, unhide the update or fetch the driver from the manufacturer."
  - q: "Why do printer drivers fail with this code so often?"
    a: "Printer drivers are frequently offered for printers that are disconnected, replaced, or shared over a network Windows no longer reaches. The installer fails because the target device is not really there. Removing the stale printer or hiding the update resolves it."
  - q: "Does this error affect Windows 10 and 11 the same way?"
    a: "Essentially yes. The driver installation mechanism, the failure modes, and this error code behave identically on both operating systems. The steps differ only cosmetically — Settings menus are arranged slightly differently — but the diagnosis, the manufacturer-driver solution, and the hide-the-update option apply exactly the same on Windows 10 and Windows 11."
---

When Windows Update reports 0x800f020b, it is telling you about one specific thing: a driver failed to install. Not a security patch, not a feature update — a driver. That focus is actually helpful, because driver failures have a short list of causes and a clean decision tree. Either the driver is wrong for your hardware, the hardware does not need it, the package is corrupt, or something blocked the install. This guide walks that tree step by step until the failure is resolved or safely retired.

Before starting, open Update history and note which driver failed — the device name matters for several steps below. HP owners dealing with this code should also read the [HP-specific 0x800f020b guide](/articles/how-to-fix-windows-update-error-0x800f020b-on-hp-laptop/), which covers the dual-pipeline conflicts HP laptops are prone to.

One reassuring fact first: a failed driver install is one of the safest failures in Windows. When the installer detects a mismatch or a problem, it aborts before making changes \u2014 the existing driver stays in place and keeps working. That is why your hardware keeps functioning normally despite the scary error code. The failure is Windows protecting you from a bad driver, which reframes the whole problem: you are not repairing damage, you are resolving a disagreement about which driver belongs on the device.

## Why this happens

- **Driver-hardware mismatch:** Windows Update's catalog occasionally pairs a driver with the wrong hardware variant, and the installer rejects it at the last step.
- **Newer driver already installed:** If a newer version is present — from the manufacturer or a previous manual install — the older offered package fails because Windows blocks the downgrade.
- **Device absent or disabled:** Drivers offered for disconnected printers, disabled Bluetooth radios, or hardware turned off in BIOS fail because there is no live device to bind to.
- **Corrupt driver package:** Damaged files in the update cache cause the installer to abort, just like with any other update payload.
- **Blocked installation:** Antivirus or device-control policies can intercept the driver install handshake, especially for kernel-mode drivers.
- **Stale device metadata:** Outdated hardware identification makes Windows Update confident about a driver that does not actually apply.
- **Interrupted install:** The laptop sleeping or restarting mid-install leaves a partial driver installation that subsequent attempts trip over.
- **Manufacturer utility conflicts:** Tools from Dell, HP, or Lenovo that manage drivers independently can install competing versions, and Windows Update's package then fails against the unexpected state — a pattern also seen when [driver updates keep failing in a loop](/articles/troubleshoot-driver-updates-keep-failing-windows-update/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Name the failing driver and assess urgency

1. Open Settings, Windows Update, Update history, and expand Driver Updates.
2. Find the 0x800f020b entry and note the exact device and version.
3. Open Device Manager, locate the device, and check whether it reports as working properly.
4. If the device works fine, this is a cosmetic problem — proceed calmly. If the device is malfunctioning, prioritize Fixes 2 and 3.

### Fix 2: Install the driver from the manufacturer's site

The manufacturer's driver is almost always fresher and better matched than the Windows Update package.

1. Identify your laptop's exact model (check the sticker on the bottom or System Information).
2. Go to the manufacturer's support site — Dell, HP, Lenovo, or your motherboard maker — and download the driver for the failing device.
3. Install it, restart, and check Windows Update. A current manufacturer driver usually makes Windows Update withdraw its older offering.

### Fix 3: Update or reinstall via Device Manager

1. Press Win + X, open Device Manager, and find the device.
2. Right-click, choose Update driver, then "Search automatically for drivers".
3. If that finds nothing, right-click the device and choose Uninstall device. If you have the manufacturer's driver ready, tick "delete the driver software"; otherwise leave it unticked.
4. Restart. Windows redetects the hardware and installs a driver. Then check Windows Update.

### Fix 4: Clear the update cache

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete everything inside C:\Windows\SoftwareDistribution.
4. Restart the services with `net start`, reboot, and check for updates to download a fresh driver package.

### Fix 5: Hide the update if the device works

1. Get the "Show or hide updates" troubleshooter (wushowhide.diagcab) from Microsoft's support pages.
2. Run it, select Hide updates, and tick the failing driver.
3. Confirm in the next Windows Update scan that it no longer appears. This is a legitimate, Microsoft-supported resolution — not a hack.

### Fix 6: Check for blocking policies or security software

1. Temporarily disable third-party antivirus real-time protection and retry the update.
2. On Pro editions, check Group Policy (gpedit.msc) under Computer Configuration, Administrative Templates, Windows Components, Windows Update for driver-related restrictions.
3. In Settings, Windows Update, Advanced options, check whether "Receive updates for other Microsoft products" or driver-specific toggles are in an odd state, and reset them to defaults.

### Fix 7: Repair system files, then do a final manual attempt

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
2. Restart.
3. Retry Windows Update once. If the same driver fails again and the device works, return to Fix 5 and hide it with confidence — you have proven the package is the problem, not your system. For persistent multi-driver failures, see the official guidance at the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Roll back if a driver install destabilized the device

Sometimes the failure is partial \u2014 the driver "installed" but the device misbehaves.

1. Open Device Manager, right-click the device, and choose Properties.
2. On the Driver tab, click "Roll Back Driver" if it is available, and follow the prompts.
3. If rollback is unavailable, uninstall the device (without deleting driver software), restart, and let Windows reinstall the last known good driver.
4. Then hide the problematic update (Fix 5) so Windows Update does not re-offer the destabilizing package.

## Closing

The 0x800f020b decision tree ends in one of three good places: the right driver installed from the manufacturer, the wrong package hidden so it stops nagging you, or a bad install rolled back to safety. All three are complete resolutions. The only losing move is retrying the same failing package indefinitely \u2014 Windows Update will happily fail the same driver every month until you intervene, so pick your ending deliberately and move on with a quiet update history.
