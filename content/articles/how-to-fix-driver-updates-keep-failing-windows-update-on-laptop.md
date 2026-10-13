---
title: "Driver Updates Keep Failing in Windows Update: End the Loop"
slug: how-to-fix-driver-updates-keep-failing-windows-update-on-laptop
date: 2026-10-02
categories: ["windows-update"]
tags: ["driver updates", "windows update failed", "installation error", "device manager", "drivers"]
description: "The same driver updates fail in Windows Update over and over on your laptop. Break the cycle with these targeted fixes."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-on-laptop.webp"
faqs:
  - q: "Why does Windows Update keep offering a driver I already installed?"
    a: "Windows Update's driver catalog doesn't always know about manually installed drivers, especially if they came from the chip vendor rather than Windows Update. It compares its catalog version against what it last installed itself, not what's actually on the system. Installing the manufacturer's latest version and then hiding the Windows Update offer breaks the mismatch loop."
  - q: "Is it safe to let Windows Update install drivers automatically?"
    a: "Usually yes for basic devices, but laptop-specific hardware — graphics, audio, power management, fingerprint readers — often works better with manufacturer-tuned drivers. Windows Update versions tend to be older and generic. Many technicians disable automatic driver updates on laptops and manage drivers through the manufacturer's utility instead, which avoids both failures and regressions."
  - q: "What does error 0x80070103 mean for a driver update?"
    a: "Error 0x80070103 means you're trying to install a driver that's already installed or older than the current one — Windows rejects it as a downgrade. It's the most common driver-update failure code and it's essentially harmless. The fix is to hide that specific update rather than troubleshooting it, since there's nothing actually broken."
  - q: "Can a failing driver update damage my hardware?"
    a: "No. A failed driver install doesn't touch your hardware — the driver either registers correctly or the install rolls back. The worst realistic outcome is a device temporarily using a generic driver until you install the right one. Your files and the rest of the system are unaffected by driver-update failures."
---

The pattern is exhausting: Windows Update downloads a driver, the install fails with some hex code, and tomorrow the same driver is back like nothing happened. After the fifth cycle you start wondering if something is deeply wrong with your laptop.

Usually, nothing is deeply wrong. Driver updates fail in Windows Update for a small set of repeatable reasons — version conflicts, corrupted packages, manufacturer utilities fighting over the same device — and each has a specific fix. The trick is identifying which loop you are in instead of hammering "Retry."

Work through these in order — diagnose first, then act. For the condensed version of this same loop-breaking process, our [driver-update failure walkthrough](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) keeps just the fixes that end it fastest.

## Why this happens

- **Version conflict.** Windows offers an older driver than the one already installed, and the installer refuses the downgrade (error 0x80070103).
- **Corrupted driver package.** A damaged download fails signature or integrity verification during install.
- **Manufacturer utility conflict.** Dell, HP, Lenovo, or ASUS tools managing the same driver block Windows' attempt.
- **Device disabled or in an error state.** A device with a yellow bang in Device Manager rejects driver installation.
- **Pending reboot lock.** Earlier updates awaiting restart hold the driver store locked.
- **Third-party driver updater interference.** Aggressive "driver booster" tools corrupt the driver catalog Windows relies on.
- **Failing hardware.** A dying device (common with Wi-Fi cards and SSDs) fails every driver install because the hardware cannot initialize.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the error code — it tells you which loop you are in

Go to Settings, Windows Update, Update history, and find the failing driver update. Note the exact error code: 0x80070103 means version conflict (hide it, do not fix it); 0x800F020B or similar install errors suggest package or device problems; repeated generic failures suggest cache corruption.

Also open Device Manager and check the target device's status — a yellow warning icon means the device itself is unhappy, and no driver update will install cleanly until the underlying device issue is resolved. Five minutes of reading codes beats five cycles of blind retrying.

### Fix 2: Install the manufacturer's driver directly

For the failing device, get the driver from the source: your laptop manufacturer's support site (using your exact model) or the chip vendor — [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for graphics.

1. Download the latest driver package for your exact model and OS.
2. Run the manufacturer's installer (preferred) or use Device Manager's "Browse my computer for drivers."
3. Restart the laptop.
4. Check Windows Update — it usually stops offering the older version once a newer driver is in place.

Manufacturer drivers are newer, hardware-tuned, and they make Windows' stale offer irrelevant. This single step ends most driver-update loops.

### Fix 3: Hide the update that should not be offered

If Windows keeps offering a driver you have already superseded (classic 0x80070103), hide it with Microsoft's "Show or hide updates" troubleshooter. The update disappears from Windows Update permanently until a newer version appears in the catalog.

This is the correct fix — not a workaround — for version-conflict failures. There is nothing broken to repair; Windows is simply offering something you do not need. The companion guide on [optional updates that won't install](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-laptop/) covers the hiding process and the triage mindset behind it.

### Fix 4: Clear the update cache and retry once

When the package itself is suspect, force a fresh download:

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`, then `net stop bits`
3. Delete everything inside `C:\Windows\SoftwareDistribution\Download`.
4. Run: `net start bits`, then `net start wuauserv`
5. Retry the driver update exactly once.

If it fails identically on a verified-fresh package, stop retrying — the problem is on the install side. Repeated identical failures on fresh downloads point to device state or permission issues, not bad bits.

### Fix 5: Fix the device state in Device Manager

Open Device Manager and find the device. If it shows a warning icon, right-click it, choose Uninstall device, and check "Attempt to remove the driver for this device" if offered. Restart — Windows redetects the hardware and installs a baseline driver.

Then install the manufacturer's driver from Fix 2. This clears corrupted driver registrations that block every update attempt. If the device fails to redetect or immediately shows the warning again, suspect the hardware itself — a Wi-Fi card that cannot initialize will fail every driver install, and no amount of software fixing changes that. Microsoft's Windows support documentation covers Device Manager troubleshooting steps in detail.

### Fix 6: Remove interfering driver utilities

Uninstall third-party "driver updater" or "driver booster" applications — they are a leading cause of driver catalog corruption and frequently the reason Windows Update driver installs fail. Use Settings, Apps, Installed apps, and remove them completely.

Also check whether your manufacturer's utility (SupportAssist, Vantage, MyASUS) is set to manage the same driver aggressively; temporarily pause its driver updates while you resolve the Windows Update side. One driver manager at a time — two fighting over the same device produces exactly the failure loop you are seeing. If you want to stop Windows from offering drivers altogether, the [optional updates guide](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-laptop/) explains how to disable automatic driver updates properly.

### Fix 7: Repair servicing and consider a manual driver store cleanup

For the stubborn cases, repair the underlying infrastructure:

1. Open Command Prompt as administrator.
2. Run: `DISM /Online /Cleanup-Image /RestoreHealth`
3. Run: `sfc /scannow`
4. Restart.

If a specific driver still fails, open Device Manager, uninstall the device with driver removal (Fix 5), then install the manufacturer's package in Safe Mode — Safe Mode prevents conflicting software from interfering with the install. After a successful manual install, hide the Windows Update version so the loop cannot restart.

## Closing

Driver updates fail in Windows Update for identifiable reasons, and the error code tells you which one. Version conflicts get hidden, not fixed; real failures get the manufacturer's driver installed directly; corrupted packages get a cache clear; and chronic trouble gets automatic driver updates disabled in favor of manufacturer-managed drivers. Stop retrying blindly — diagnose the loop, then break it once.
