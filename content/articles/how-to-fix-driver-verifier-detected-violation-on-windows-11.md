---
title: "How to Fix DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 11"
slug: how-to-fix-driver-verifier-detected-violation-on-windows-11
date: 2026-10-06
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "stop code", "windows 11"]
description: "DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 11 means a diagnostic caught a bad driver. Reset Verifier, find the driver, fix it — full steps inside."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-detected-violation-on-windows-11.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 11?"
    a: "It's a blue screen raised by Driver Verifier, a built-in Windows diagnostic. Verifier stress-tests drivers, and when one breaks the rules it deliberately crashes the system to expose it. The crash is intentional — the real problem is the driver it caught."
  - q: "Why is Driver Verifier running on my laptop?"
    a: "Someone enabled it — usually during earlier troubleshooting, sometimes by a support technician or a guide you followed. Verifier is meant for short diagnostic sessions, not permanent use. Running verifier /reset and rebooting turns it off."
  - q: "Which drivers usually trigger this on Windows 11?"
    a: "Third-party drivers for VPNs, antivirus filters, RGB/peripheral utilities, printer software, and virtualization tools are the usual suspects. Windows 11's stricter driver checks catch violations that older Windows versions silently tolerated."
  - q: "Do I need to reinstall Windows to fix it?"
    a: "No. Resetting Verifier stops the crashes immediately, and updating, rolling back, or removing the offending driver resolves the root cause. Reinstallation is unnecessary for this stop code."
---

Of all the blue screens, `DRIVER_VERIFIER_DETECTED_VIOLATION` is the one most likely to be a misunderstanding. That crash isn't your laptop breaking — it's Driver Verifier, a diagnostic tool built into Windows, deliberately crashing the system because it caught a driver misbehaving. Useful during a troubleshooting session; miserable when Verifier was left running for weeks afterward.

So the fix is a two-step dance: switch Verifier off to stop the intentional crashes, then track down and fix the driver it was complaining about. Let's do both, in that order.

A word on what you're seeing: Verifier crashes can look random — different apps open, different times of day — but they're actually extremely consistent underneath. Verifier applies the same stress checks to every driver operation, so the same rule violation fires whenever the buggy driver runs that code path. If your crashes cluster around specific activities (plugging in a device, connecting to VPN, waking from sleep), that activity is pointing straight at the offending driver, and Fix 2 will confirm it.

## Why this happens

- **Verifier was enabled and never disabled**: The overwhelmingly common cause. Verifier is supposed to run temporarily while you diagnose a driver problem. Left on, every driver hiccup becomes a blue screen.
- **A third-party driver genuinely violating rules**: VPN clients, antivirus filter drivers, RGB control software, and peripheral utilities are the classic Windows 11 offenders. Windows 11 enforces driver rules more strictly than Windows 10 did.
- **Old driver meets new Windows 11 build**: Feature updates change kernel internals. A driver that behaved on 23H2 can start tripping Verifier's checks on 24H2 without any update to the driver itself.
- **Corrupted driver binaries**: A half-installed or damaged driver acts unpredictably, which is exactly what Verifier is designed to catch and report.
- **Conflicting low-level software**: Two programs installing filter drivers in the same stack — say, an antivirus and a disk encryption tool — can violate I/O rules in combination even when each is fine alone.
- **Unstable hardware making drivers fail**: Rare, but flaky RAM or an overheating component can cause driver operations to fail in ways Verifier flags as violations rather than hardware errors.

## How to fix it

Work through these in order.

### Fix 1: Turn off Driver Verifier

This ends the deliberate crash loop immediately.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run:

   ```cmd
   verifier /reset
   ```

3. Restart your laptop.
4. If Windows won't stay up long enough, boot into Safe Mode first: hold **Shift** while clicking **Restart** on the sign-in screen, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** and press **4**. Run the command there.

### Fix 2: Identify the driver from the crash dump

Don't guess — read what Verifier actually caught.

1. Open **File Explorer** and navigate to `C:\Windows\Minidump`.
2. Find the most recent `.dmp` file from a Verifier crash.
3. Analyze it following the practical steps in [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/) and note the driver filename in the crash details.
4. That filename (for example `iqvw64e.sys` or `ene.sys`) tells you exactly which software to target next.

### Fix 3: Update the offending driver

The vendor may have already fixed the violation.

1. Press **Win + X** and open **Device Manager**.
2. Locate the device, right-click it, and choose **Update driver** > **Search automatically for drivers**.
3. If Windows finds nothing, download the latest Windows 11 driver from the manufacturer's website — not from a driver-updater app.
4. For graphics drivers specifically, use [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Roll back a recently updated driver

If the violations started after a driver update, the new version is the suspect.

1. In **Device Manager**, right-click the device and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver** (grayed out means no previous version is stored).
3. Select a reason, confirm, and restart.
4. Test for a day before letting Windows Update touch that driver again — you can hide the update if needed.

### Fix 5: Uninstall the software behind the bad driver

For VPN clients, RGB utilities, old printer suites, and similar software, clean removal is often better than a driver update.

1. Go to **Settings** > **Apps** > **Installed apps** and uninstall the program.
2. Grab the vendor's official cleanup/removal tool if one exists — leftover filter drivers are the reason "I already uninstalled it" sometimes doesn't work.
3. In **Device Manager**, enable **View** > **Show hidden devices** and remove any ghost entries for the device.

### Fix 6: Install pending Windows updates

Cumulative updates regularly include driver-compatibility fixes.

1. Open **Settings** > **Windows Update** and click **Check for updates**.
2. Install everything available, including optional updates.
3. Restart and give it a day of normal use before declaring victory.

### Fix 7: Run a memory test

Bad RAM produces failures that Verifier attributes to drivers.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. If errors appear, reseat your RAM (if accessible) or have the stick replaced — no driver fix will help until the memory is sound.

### Fix 8: Clean-boot to catch software conflicts

If crashes persist with Verifier off, something else is destabilizing drivers.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services** and click **Disable all**.
3. In **Task Manager** > **Startup apps**, disable everything non-essential.
4. Restart and test. Re-enable in groups to isolate the conflicting program.

### Fix 9: Keep Verifier off and verify stability over a few days

The final step is confirming the fix actually held — Verifier crashes can be intermittent.

1. Use the laptop normally for two to three days, including the activities that used to trigger crashes.
2. Check **Settings** > **Windows Update** > **Update history** to make sure no driver update silently reinstalled the bad version.
3. If a specific driver keeps coming back via Windows Update, use the "Show or hide updates" troubleshooter to block that driver update while keeping security updates flowing.
4. Only re-enable Verifier if you're actively diagnosing a brand-new driver problem — and remember to run `verifier /reset` when that session ends.

## Closing

`DRIVER_VERIFIER_DETECTED_VIOLATION` on Windows 11 is Verifier doing its job after being left on too long. Reset it, find the driver it caught in the dump, and update or remove that driver — the crashes end there. For the Windows 10 version of this error, see [how to fix it on Windows 10](/articles/how-to-fix-driver-verifier-detected-violation-on-windows-10/), and for the I/O-manager variant read the [step-by-step IOMANAGER_VIOLATION fix](/articles/how-to-fix-driver-verifier-iomanager-violation-step-by-step/).
