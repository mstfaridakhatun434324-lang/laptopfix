---
title: "Attempted Execute of Noexecute Memory After a Windows 11 Update: Fix Guide"
slug: how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update
date: 2026-09-23
categories: ["windows-errors"]
tags: ["bsod", "noexecute-memory", "windows-11"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY after a Windows 11 update points to a driver or RAM fault. Track it down with these steps."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "It's a blue screen (stop code 0x000000FC) that fires when a driver or program tries to run code from a memory region marked non-executable. Modern CPUs enforce this as a security feature (DEP/NX). After an update, the trigger is usually a driver that's incompatible with the new build, or failing RAM corrupting execution addresses."
  - q: "Why did it appear right after I updated Windows 11?"
    a: "Feature updates change memory layout and enforcement. A driver with a latent bug that previous builds tolerated can start tripping the no-execute protection in the new build. The update can also install a new driver version that itself contains the bug."
  - q: "Is this error caused by a virus?"
    a: "It can be — malware often tries to execute code from data regions, which is exactly what this protection blocks. But on a freshly updated laptop, a buggy driver or bad RAM is far more likely. Run a Defender Offline scan to rule malware out, then focus on drivers and memory."
  - q: "The blue screen names a .sys file. What now?"
    a: "That file is your prime suspect. Update it, roll it back to the pre-update version, or reinstall it from the manufacturer's site. The steps below walk through exactly how, starting with identifying the file in Event Viewer if you missed it on screen."
---
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (stop code 0x000000FC) is Windows' memory protection doing its job a little too visibly. Modern processors mark certain memory regions as non-executable — data can live there, but code can't run from there. When a driver tries to execute code from one of those regions, the CPU refuses and Windows blue-screens.

When this starts right after a Windows 11 update, the usual story is a driver that the new build no longer tolerates, or RAM that's started failing and is corrupting the addresses drivers jump to. Either way, the fix sequence below will pin it down.

## Why this happens

- **An incompatible driver after the update.** The new Windows build enforces memory protections more strictly, exposing bugs in older drivers — graphics and network drivers are the usual suspects.
- **A buggy new driver installed by the update.** Windows Update sometimes bundles driver updates with OS updates, and the new driver version may contain the bug.
- **Failing RAM.** Bad memory corrupts the addresses drivers use, sending execution into non-executable regions.
- **Corrupted system files.** Damage to Windows' own drivers or kernel components from a troubled update.
- **Malware.** Malicious code attempting to execute from data regions trips this exact protection.
- **Overclocked or unstable memory.** XMP profiles and memory overclocks that aren't fully stable corrupt execution flow under load.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Identify the suspect driver from the crash

Get the filename before you change anything.

1. Press **Win + X** and open **Event Viewer**, then go to **Windows Logs > System**.
2. Find the **BugCheck** error from the crash time and open its details — it often names the `.sys` file involved.
3. If the blue screen itself showed **"What failed: something.sys"**, that's your target. Note it exactly.
4. With the filename in hand, skip to Fix 3 and deal with that driver directly. If no file is named, continue in order.

### Fix 2: Boot into Safe Mode to stabilize

If the crashes are constant, get to stable ground first.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. Stability in Safe Mode confirms a third-party driver — Safe Mode doesn't load them.

### Fix 3: Update, roll back, or reinstall the problem driver

The core fix for update-triggered cases.

1. Press **Win + X** and open **Device Manager**.
2. Locate the device for your suspect driver (**Display adapters** for GPU files, **Network adapters** for Wi-Fi files).
3. Right-click and choose **Update driver > Search automatically for drivers**.
4. Since the crashes started with the update, **Roll Back Driver** (under **Properties > Driver tab**) is often the better move — it returns to the version that worked before.
5. For the definitive fix, download the driver from your laptop maker's support site ([Dell](https://www.dell.com/support), HP, [Lenovo](https://support.lenovo.com/us/en/)) and install it manually.
6. Restart and test under the conditions that triggered the crashes. The same driver-focused approach resolves the [24H2-specific variant of this error](/articles/how-to-fix-attempted-execute-of-noexecute-memory-in-windows-11-24h2/) too.

### Fix 4: Uninstall the recent Windows update as a test

Confirm the update is what exposed the problem.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update and restart.
3. If crashes stop, the update changed something your driver couldn't handle. Reinstall the update after updating the driver from the manufacturer's site, and use **Pause updates** briefly if you need time.
4. Don't leave security updates uninstalled long-term — the driver update is the real fix.

### Fix 5: Run a malware scan and repair system files

Cover the two remaining software causes in one pass.

1. Open **Windows Security > Virus & threat protection > Scan options**, choose **Microsoft Defender Offline scan**, and click **Scan now**. Remove anything it finds.
2. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
3. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. Clean system files eliminate the corrupted-component variant of this error.

### Fix 6: Test your RAM thoroughly

Do this especially if crashes are random or name different files each time.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If errors appear, reseat the RAM sticks (power off first) and retest; replace sticks that consistently fail.
3. Disable any XMP or memory overclock in the BIOS — unstable memory tuning is a classic cause of execution-address corruption.
4. For certainty, run MemTest86 from a USB drive for two full passes — it catches intermittent faults reliably. The [Dell-specific guide for this error](/articles/how-to-fix-attempted-execute-of-noexecute-memory-on-dell-laptop/) covers the same memory diagnostics with brand-specific driver notes.

### Fix 7: Reset Windows if nothing else works

The last software resort before suspecting the motherboard.

1. Back up your files.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Remove everything**, and pick **Cloud download**.
3. After setup, install the manufacturer's drivers first and test before restoring files and apps.
4. Crashes on a clean install with passing RAM tests point to failing hardware — usually the motherboard or CPU memory controller at that point. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents repair and recovery options.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY after an update is a driver compatibility problem until proven otherwise. Check the crash details for the guilty `.sys` file, roll back or update that driver, and test your RAM thoroughly — that sequence resolves it for nearly everyone. The update didn't damage your hardware; it just started enforcing memory protection rules that a buggy driver was quietly breaking all along. Work the list patiently and you'll have a clear answer, not a guess.
