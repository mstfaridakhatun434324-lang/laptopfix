---
title: "Fix Driver Updates That Keep Failing in Windows Update (Step-by-Step)"
slug: how-to-fix-driver-updates-keep-failing-windows-update-step-by-step
date: 2026-09-16
categories: ["windows-update"]
tags:
  - windows update
  - driver updates
  - device drivers
  - troubleshooting
  - windows 11
description: "Driver updates keep failing every time Windows Update runs? This step-by-step technician guide shows how to find the failing driver, install it manually, and stop the failure loop."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-step-by-step.webp"
faqs:
  - q: "Why does Windows Update keep offering a driver I already installed?"
    a: >
      Windows Update compares version numbers, not install dates. If its catalog lists a driver with a higher version number than the one on your system — even if yours is newer in reality because the vendor uses a different numbering scheme — it will keep offering it. Installing the vendor's latest driver and hiding the Windows Update offering with wushowhide breaks this loop permanently.
  - q: "Is it safe to hide a driver update with wushowhide?"
    a: >
      Yes. Hiding an update only stops Windows Update from offering that specific driver version; it changes nothing else on your system and does not affect security or quality updates. You can unhide it at any time by running the tool again and choosing Show hidden updates. It is the officially supported way to skip a problematic driver.
  - q: "Should I get drivers from Windows Update or the laptop manufacturer?"
    a: >
      Use the manufacturer's drivers for graphics, Wi-Fi, audio, and chipset components, because they are validated against your exact model and usually newer. Windows Update drivers are fine as a fallback for basic functionality. A good routine is to install vendor drivers first after setup, then let Windows Update handle only what the vendor does not cover.
  - q: "Will disabling driver updates in Windows Update break my laptop?"
    a: >
      No. Windows will simply stop replacing your manually installed drivers with its own versions. Security patches and feature updates continue normally. Many technicians disable automatic driver updates on purpose after installing vendor drivers, since unexpected driver swaps are a leading cause of new problems appearing right after Patch Tuesday.
---

There is a special kind of frustration reserved for opening Windows Update, watching it download the same Intel, Realtek, or NVIDIA driver for the fifth time, and then seeing the red text: install failed. The rest of your updates sail through, but that one driver refuses to stick, and every reboot starts the cycle again.

Driver update failures are among the most common Windows Update problems on laptops, and they are rarely caused by broken hardware. In most cases the offered driver is outdated, mismatched to your exact hardware revision, or blocked by a newer driver you installed yourself. Windows does not explain any of this — it just retries forever.

Below is the exact sequence a repair technician follows: identify which driver is failing and why, try the safe built-in routes first, then install the driver manually from the manufacturer, and finally block the bad offering so it stops coming back. Follow the steps in order and the loop ends today.

## Why this happens

- **A newer driver is already installed:** error 0x80070103 means Windows tried to install a driver older than the one on your system. This happens constantly when you update drivers through GeForce Experience, Intel DSA, or your laptop maker's app, and Windows Update later offers its own older copy.
- **The offered driver does not match your hardware:** laptop makers ship slightly different revisions of the same chip. A generic driver package from Windows Update can fail on your specific revision with error 0x800F020B or 0x800F0247 because the hardware IDs do not line up.
- **Corrupted driver store or update cache:** if the downloaded driver package in the SoftwareDistribution folder is damaged, or the local driver store has a half-installed entry, every install attempt fails at the same point no matter how many times you retry.
- **Third-party driver utilities fighting Windows Update:** tools that auto-update drivers can lock driver files or replace them mid-install. When Windows Update then tries to write the same files, the install collides and rolls back.
- **Low disk space on the system drive:** driver packages are staged on C: before installation. With less than roughly 10 GB free, staging can fail silently and the driver reports a generic install error.
- **Security software blocking driver installation:** some antivirus and endpoint protection tools flag driver .inf installs as suspicious behavior and block the write, especially for network and audio drivers.
- **A genuinely buggy driver on Microsoft's servers:** occasionally Microsoft publishes a driver with a broken installer. Thousands of identical machines fail at once, and no amount of retrying on your end will fix it until the package is revised or hidden.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing driver and its error code

Never troubleshoot blind. Windows Update keeps a history that names the exact driver and the hex error code, and that code tells you which of the causes above applies to you. Two minutes here saves an hour of guessing.

1. Open Settings with Win + I, then go to Windows Update and click Update history.
2. Scroll to Driver updates and expand the failed entry to see the driver name, version, and date.
3. Click the entry or check Event Viewer under Windows Logs > System for the full error code, such as 0x80070103 or 0x800F020B.
4. Write down the driver name, version, and code — you will need them for the steps below.

### Fix 2: Install the driver from Optional updates manually

Sometimes the automatic install fails but the manual one succeeds, because the manual path re-downloads a fresh copy and runs the installer with full user context instead of the background service context.

1. Go to Settings > Windows Update > Advanced options > Optional updates.
2. Expand Driver updates, tick the failing driver, and click Download & install.
3. If it is not listed there, click Check for updates once, wait for the scan to finish, and look again.
4. If the install succeeds here, you are done — skip to the closing section.

### Fix 3: Get the driver directly from the manufacturer

When Microsoft's copy keeps failing, the manufacturer's own package almost always works because it is newer, matched to your exact model, and uses the vendor's tested installer. For Intel graphics, Wi-Fi, or Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects your hardware and pulls the correct driver automatically.

1. Find your exact laptop model on the maker's support site (Dell, HP, Lenovo, or ASUS) and open its driver page.
2. Download the driver matching the failing device — graphics, audio, network, or chipset — choosing the newest version for your Windows build.
3. If the vendor offers an installer, run it as administrator and reboot when asked.
4. Prefer learning the manual route for every update? The official [Windows support hub](https://support.microsoft.com/en-us/windows) documents the Optional updates flow and driver rollback steps in detail.

### Fix 4: Hide the bad driver update so it stops retrying

If the driver you need is already installed from the manufacturer, the correct move is to tell Windows Update to stop offering its older copy. Microsoft's wushowhide troubleshooter does exactly that.

1. Download the Show or hide updates troubleshooter (wushowhide.diagcab) from Microsoft and run it.
2. Click Next, choose Hide updates, and tick the failing driver from the list.
3. Finish the wizard, then run Check for updates — the driver should no longer appear.
4. If you ever want it back, run the tool again and choose Show hidden updates.

### Fix 5: Reset the Windows Update components

A corrupted SoftwareDistribution cache poisons every retry. Renaming the cache folders forces Windows to rebuild them cleanly, which fixes failures caused by damaged downloads without touching your files or apps.

1. Open Command Prompt as administrator.
2. Run these commands one at a time: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services with net start wuauserv, net start bits, net start cryptsvc, then check for updates again.

### Fix 6: Clean-install the driver through Device Manager

When the driver store itself holds a broken entry, removing the device and its driver package completely, then letting Windows detect fresh hardware, clears the jam that in-place reinstalls cannot.

1. Open Device Manager (Win + X > Device Manager) and find the device matching the failing driver.
2. Right-click it, choose Uninstall device, and tick Delete the driver software for this device if offered.
3. Reboot, then in Device Manager click Action > Scan for hardware changes.
4. Let Windows install its base driver, then install the manufacturer's package from Fix 3 on top.

### Fix 7: Repair system files with SFC and DISM

If driver installs fail across multiple devices, the underlying system image may be damaged. These two built-in tools repair it using a known-good source, and they are safe to run.

1. Open Command Prompt as administrator and run: sfc /scannow. Wait for it to finish.
2. Then run: DISM /Online /Cleanup-Image /RestoreHealth. This can take 15 to 30 minutes.
3. Reboot and run Windows Update again to confirm the driver installs cleanly.

## Closing

Driver update loops look scary but they follow a pattern: find the exact driver and error code, try the manual install, go to the manufacturer when Microsoft's copy is stale, and hide the bad offering so it stops nagging you. Most cases resolve at Fix 3 or Fix 4. To prevent repeats, [disable automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) once your vendor drivers are in place, and [back up your drivers before updating](/articles/best-way-to-backup-drivers-before-update/) so a bad install is always reversible.
