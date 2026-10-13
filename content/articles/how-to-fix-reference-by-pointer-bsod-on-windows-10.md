---
title: "How to Fix REFERENCE_BY_POINTER BSOD on Windows 10"
slug: how-to-fix-reference-by-pointer-bsod-on-windows-10
date: 2026-09-14
categories: ["windows-errors"]
tags: ["blue screen", "windows 10", "bsod"]
description: "REFERENCE_BY_POINTER blue screen on Windows 10? Learn what this driver reference-count error means and how to fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-on-windows-10.webp"
faqs:
  - q: "What is a REFERENCE_BY_POINTER blue screen?"
    a: "It means a driver's reference count for an object dropped below zero, which should never happen. It almost always points to a buggy driver mishandling memory. The fix is finding and updating or removing that driver."
  - q: "Is REFERENCE_BY_POINTER caused by bad RAM?"
    a: "Rarely. This stop code is one of the most driver-specific blue screens in Windows. RAM is worth testing, but the odds heavily favor a faulty driver, so start with driver updates and Driver Verifier."
  - q: "Why did this start after a Windows 10 update?"
    a: "Windows 10 updates sometimes install new driver versions automatically. If the replacement driver has a reference-counting bug, the blue screen appears right after the update. Rolling back the driver usually stops it immediately."
  - q: "Can antivirus cause this blue screen?"
    a: "Yes. Security products install kernel drivers, and an outdated one can corrupt object reference counts. Uninstalling third-party antivirus temporarily is a legitimate diagnostic step for this stop code."
---

A REFERENCE_BY_POINTER blue screen on Windows 10 means a driver lost track of how many times it was using something in memory, and Windows pulled the emergency brake. The name is cryptic, but the practical meaning is straightforward: somewhere in your driver stack, a piece of software is mishandling memory objects, and it needs to be found and fixed.

The good news is that this is one of the most driver-specific stop codes in Windows, which actually makes it easier to diagnose than vague crashes. The steps below go from identifying the likely driver to the heavier diagnostic tools, and they are all safe to run on a Windows 10 laptop. Take it one fix at a time rather than trying everything at once; that way, when the blue screens stop, you will know exactly what solved them.

## Why this happens

- **Buggy device driver.** A driver decrements a reference count too many times, usually because of a race condition in its code. Graphics, network, and audio drivers are the usual offenders.
- **Outdated third-party drivers.** Old drivers written for earlier Windows versions misbehave under Windows 10's stricter memory rules.
- **Conflicting drivers.** Two drivers fighting over the same hardware can corrupt each other's reference counts.
- **Antivirus kernel drivers.** Security software runs at the deepest level of the system, and an outdated version can trigger exactly this fault.
- **Corrupted system files.** Damaged Windows files can misreport object states and produce a false reference fault.
- **Recent Windows 10 update.** Automatic driver updates bundled with cumulative updates are a common trigger.
- **Failing RAM.** Uncommon for this stop code, but memory that corrupts driver data in transit can produce the same symptom.
- **Virtualization or sandbox software.** Hypervisors and sandboxing tools install kernel drivers that manage memory objects directly, and an outdated version can corrupt reference counts in the same way a buggy hardware driver does.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Boot into Safe Mode and check what changed

1. Hold **Shift** while clicking **Power** > **Restart** to reach the recovery screen.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
3. Think back: did the blue screens start after a driver update, a Windows update, or new software? The timeline is your best diagnostic clue.
4. In Safe Mode, open **Device Manager** and look for any device with a yellow warning triangle.

### Fix 2: Update the most likely drivers

1. Open **Device Manager** and expand **Display adapters**, **Sound, video and game controllers**, and **Network adapters**.
2. Right-click each device and choose **Update driver** > **Search automatically for drivers**.
3. For graphics, go straight to the source: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), [AMD drivers](https://www.amd.com/en/support/download/drivers.html), or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart after updating and use the laptop normally.

### Fix 3: Roll back a driver that updated recently

1. In **Device Manager**, right-click the suspect device and choose **Properties**.
2. Go to the **Driver** tab. If **Roll Back Driver** is available, click it and choose a reason.
3. This is the fastest fix when the blue screen started the same day a driver updated. Windows 10's automatic driver updates make this scenario very common.

### Fix 4: Temporarily uninstall third-party antivirus

1. In Safe Mode, open **Settings** > **Apps** and uninstall any third-party antivirus or firewall product.
2. Windows Defender activates automatically, so you are still protected.
3. Restart normally. If the blue screens stop, the antivirus driver was the cause. Check the vendor's site for an updated version before reinstalling.

### Fix 5: Run the system file checker

1. Press **Windows key + X** and choose **Windows PowerShell (Admin)** or **Command Prompt (Admin)**.
2. Run `sfc /scannow` and let it complete.
3. If problems are found but not fixed, run `DISM /Online /Cleanup-Image /RestoreHealth` and repeat the SFC scan.
4. Restart the laptop.

### Fix 6: Use Driver Verifier to pinpoint the driver

1. Open an elevated command prompt and type `verifier` to launch Driver Verifier Manager.
2. Select **Create standard settings**, then choose **Select driver names from a list**.
3. Check the non-Microsoft drivers, especially ones you updated recently.
4. Restart and use the laptop. Verifier forces the faulty driver to crash with a more specific error that names it.
5. Boot into Safe Mode and run `verifier /reset` to disable it, then update or remove the identified driver. Never leave Driver Verifier running for days, because it intentionally stresses drivers and will keep crashing the system on purpose until you switch it off.

### Fix 7: Test memory and consider a clean driver reinstall

1. Press **Windows key + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems** and let the test finish.
3. If RAM passes, do a full clean reinstall of the graphics driver using the manufacturer's installer with the clean install option checked.
4. As a final option, use **Settings** > **Update & Security** > **Recovery** > **Reset this PC** to refresh Windows 10.
5. For the same stop code on newer systems, see [REFERENCE_BY_POINTER after a Windows 11 update](/articles/how-to-fix-reference-by-pointer-bsod-after-windows-11-update/), and for related memory faults the [IRQL_NOT_LESS_OR_EQUAL guide](/articles/irql-not-less-or-equal-windows-11-fix/) is worth reading.

## Closing

REFERENCE_BY_POINTER is intimidating to look at, but it is a gift in disguise: it tells you the problem is almost certainly a driver, which narrows the search enormously. Update the usual suspects, roll back anything that changed recently, and use Driver Verifier when you need a name. On Windows 10, keeping third-party drivers current and letting Windows Update handle the rest keeps this particular blue screen from coming back. If you run virtualization or sandbox software, keep those tools updated too, since their kernel drivers are fully capable of producing this exact fault.
