---
title: "DRIVER_VERIFIER_DETECTED_VIOLATION: Troubleshooting Guide"
slug: driver-verifier-detected-violation-troubleshooting
date: 2026-09-18
categories: ["windows-errors"]
tags: ["blue screen", "driver verifier", "bsod"]
description: "Getting DRIVER_VERIFIER_DETECTED_VIOLATION blue screens? Learn what Driver Verifier found, how to identify the driver, and how to fix it."
thumbnail: "/images/thumbs/driver-verifier-detected-violation-troubleshooting.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_DETECTED_VIOLATION mean?"
    a: "It means Windows Driver Verifier caught a driver breaking the rules: writing to memory it should not touch, mishandling interrupts, or corrupting data structures. The blue screen is Verifier doing its job. The named driver file on the screen is the one you need to update or remove."
  - q: "Why is Driver Verifier running on my laptop?"
    a: "Either you or a technician enabled it deliberately to diagnose crashes, or it was left on after a previous troubleshooting session. Verifier does not turn itself on during normal Windows use."
  - q: "How do I turn Driver Verifier off?"
    a: "Open an elevated command prompt and run verifier /reset, then restart. If Windows crashes before you can do that, boot into Safe Mode first, where Verifier is less aggressive, and run the reset command there."
  - q: "Should I leave Driver Verifier enabled to catch more bad drivers?"
    a: "No. Verifier intentionally crashes the system when it catches violations, so leaving it on makes the laptop unstable by design. Enable it only for short diagnostic sessions, then disable it."
---

DRIVER_VERIFIER_DETECTED_VIOLATION is a special blue screen. Unlike most stop codes, which appear because something went wrong by accident, this one appears because you, or someone helping you, asked Windows to watch the drivers closely and crash on purpose when one misbehaves. The tool is called Driver Verifier, and this blue screen is it reporting a catch.

That means two things. First, do not panic: the crash is the diagnostic working. Second, the blue screen almost always names the guilty driver file, so the hard part, finding the culprit, is already done. This guide explains how to read the result, fix the driver, and turn Verifier off properly when you are done.

## Why this happens

- **Driver Verifier is enabled.** The root cause of the blue screen itself is that Verifier is running. Without it, the same driver bug might cause a vaguer crash or no visible crash at all.
- **A driver violates memory rules.** The driver wrote to freed memory, accessed an invalid address at the wrong interrupt level, or corrupted a pool allocation.
- **Outdated third-party driver.** Older drivers written before current Windows driver standards are the most common violators.
- **Buggy new driver release.** A recent update can introduce violations in a driver that previously passed.
- **Overclocked hardware.** Unstable memory or CPU timings can make a correct driver appear to violate rules.
- **Corrupted driver installation.** A half-installed driver can behave erratically enough to trip Verifier's checks.
- **Antivirus or security drivers.** Deep-hooking security software is a frequent Verifier target after major Windows updates.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Read the blue screen and identify the driver

The name on the screen is the whole point of running Verifier.

1. Photograph the blue screen. Note the file name shown, such as `rtwlanu.sys` or `nvlddmkm.sys`, and any stop code parameters.
2. Search for the file name to identify which device or program it belongs to. Manufacturer driver files are usually easy to trace.
3. If the screen disappears too fast, the same information is in the memory dump. After rebooting, open **Event Viewer** > **Windows Logs** > **System** and look for the bugcheck entry at the crash time.

### Fix 2: Update the offending driver

1. Open **Device Manager** and find the device that owns the driver file.
2. Right-click it and choose **Update driver** > **Search automatically for drivers**.
3. For the best result, download the driver from the manufacturer: your laptop maker's support page, [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), or [AMD drivers](https://www.amd.com/en/support/download/drivers.html).
4. Restart and, if you want to verify the fix, re-enable Verifier briefly to confirm the driver now passes.

### Fix 3: Roll back or remove the driver

If the violation started after a driver update, the new version is the problem.

1. In **Device Manager**, right-click the device, choose **Properties** > **Driver**, and click **Roll Back Driver**.
2. If rollback is unavailable, choose **Uninstall device** instead, checking **Attempt to remove the driver for this device** if offered.
3. Restart. Windows will install its inbox driver, which is older but stable.
4. Test before installing any newer version from the manufacturer.

### Fix 4: Disable Driver Verifier correctly

Once you have your answer, turn Verifier off. This is the fix for the repeated blue screens themselves.

1. Press **Windows key + X** and open **Terminal (Admin)**.
2. Run `verifier /reset` and press Enter.
3. Restart the laptop. Verifier is now off and the intentional crashes stop.
4. If Windows crashes before you can run the command, boot into Safe Mode first. Verifier's checks are relaxed there, giving you a window to run the reset.

### Fix 5: Update or remove the owning software

Sometimes the driver belongs to a program, not a device.

1. If the file belongs to antivirus, VPN, or system utility software, update that program to its latest version.
2. If no update exists, uninstall the program temporarily and test stability.
3. Reinstall only after confirming the crashes stop without it. Some older utilities never get fixed and need replacing.

### Fix 6: Rule out unstable hardware

Verifier flags drivers, but shaky hardware can make innocent drivers look guilty, so check this before replacing half your driver stack.

1. Reset the BIOS to defaults to clear any overclock or aggressive memory profile.
2. Run the Windows Memory Diagnostic: press **Windows key + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
3. Let both passes finish. If errors appear, the RAM is corrupting driver data, and no driver update will ever fix that.
4. If Verifier flags multiple unrelated drivers, suspect RAM or an unstable overclock rather than any single driver. One bad driver is a driver problem; five bad drivers is a hardware problem.

### Fix 7: Repair system files and reset if needed

1. In an elevated Terminal, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` if SFC cannot fix everything.
3. As a last resort, use **Settings** > **System** > **Recovery** > **Reset this PC** with **Keep my files**.
4. Related reading: the step-by-step [Driver Verifier violation walkthrough](/articles/how-to-fix-driver-verifier-detected-violation-step-by-step/) and the [IRQL_NOT_LESS_OR_EQUAL guide](/articles/irql-not-less-or-equal-windows-11-fix/) for a closely related stop code. Microsoft documents Verifier on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION is the rare blue screen that hands you the answer: a driver broke the rules, and Verifier caught it red-handed. Update or remove that driver, turn Verifier off with `verifier /reset`, and the crashes end. Remember the lesson this tool teaches: when mysterious blue screens resist every fix, a short, careful Verifier session is the fastest way to get a name, and a name is everything in troubleshooting.
