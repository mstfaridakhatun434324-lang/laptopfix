---
title: "How to Fix Driver IRQL Not Less or Equal on Windows 11"
slug: how-to-fix-driver-irql-not-less-or-equal-on-windows-11
date: 2026-09-21
categories: ["windows-errors"]
tags: ["bsod", "driver-irql", "windows-11", "blue screen"]
description: "Fix DRIVER_IRQL_NOT_LESS_OR_EQUAL on Windows 11 by identifying the faulty driver, updating it correctly, and verifying with memory tests."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-on-windows-11.webp"
faqs:
  - q: "What does Driver IRQL Not Less or Equal mean on Windows 11?"
    a: "A driver tried to access memory at an interrupt level where that access is forbidden, risking data corruption, so Windows halted. It is one of the most common blue screens and is usually caused by an outdated or corrupt network, storage, or graphics driver. The blue screen often names the offending driver file directly."
  - q: "How do I find which driver caused the IRQL error?"
    a: "Read the blue screen itself; it usually shows a line like What failed followed by a .sys filename. If you missed it, open Event Viewer, go to Windows Logs then System, and find the BugCheck event, which records the same filename. Failing that, Driver Verifier can force the culprit to identify itself in the next dump."
  - q: "Can Windows Update fix this automatically?"
    a: "Sometimes, if the problem is a known-bad driver that Microsoft has replaced. But Windows Update often installs generic drivers, and the real fix is usually the vendor's latest driver for your exact hardware. Use Windows Update as a supplement, not the primary fix."
  - q: "Does this error mean my RAM is failing?"
    a: "Not necessarily, but it is worth checking. Bad RAM can make a correct driver appear to access the wrong address, producing this exact stop code. If driver updates do not stop the crashes, run an extended memory test before assuming anything about the hardware."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the blue screen that actually tries to help you. Right there on the sad face screen, Windows usually prints the name of the driver that broke the rules, something like `What failed: Netwtw10.sys`. That single line turns a scary crash into a straightforward repair job: find that driver, replace it properly, and move on.

This is the general Windows 11 guide, good for any laptop brand. It covers reading the clue, updating correctly, and handling the cases where the blue screen names nothing. Work through the fixes in order, and resist updating every driver at once; changing one thing at a time is how you learn which change actually fixed it.

## Why this happens

- **A driver accessed memory at the wrong IRQL.** The defining violation: touching paged memory at a raised interrupt level.
- **Outdated network drivers.** Wi-Fi and Ethernet drivers are the most frequent offenders across all brands.
- **Corrupt driver binaries.** Disk errors or interrupted installs damage driver files.
- **Conflicting drivers.** Two drivers claiming the same device after mixed update sources.
- **Faulty RAM.** Memory errors mimic driver addressing violations.
- **Overclocking instability.** Aggressive settings cause timing violations under load.
- **Recent Windows update.** Kernel changes expose latent driver bugs.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Read the driver name from the crash

The diagnosis is printed on the blue screen.

1. At the next crash, look for **What failed:** followed by a `.sys` filename near the bottom of the screen.
2. Write it down exactly. Common ones: `Netwtw10.sys` (Intel Wi-Fi), `nvlddmkm.sys` (NVIDIA graphics), `iaStorAC.sys` (Intel storage), `rtwlanu.sys` (Realtek Wi-Fi).
3. If you miss it, disable automatic restart: **Control Panel** then **System** then **Advanced system settings**, click **Settings** under Startup and Recovery, and uncheck **Automatically restart**.
4. Cross-check in **Event Viewer** under **Windows Logs** then **System** for the BugCheck event naming the same file.
5. That driver is your target for Fix 2.

### Fix 2: Clean-install the correct driver

Replace the offender with the vendor's current release.

1. Open **Device Manager** (**Win + X**) and find the device matching the named driver.
2. Right-click it, choose **Uninstall device**, and check **Attempt to remove the driver for this device** if offered.
3. Restart, then download the latest driver from the hardware vendor: [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Intel network and chipset, [NVIDIA](https://www.nvidia.com/Download/index.aspx) for GeForce graphics, [AMD](https://www.amd.com/en/support/download/drivers.html) for Radeon.
4. Prefer your laptop maker's support site when the device is brand-specific.
5. Restart again and test under normal use. Include the specific activity that crashed before; IRQL errors often need a particular workload, like gaming or large downloads, to reappear.

### Fix 3: Update the big three when no driver is named

Cover the usual suspects systematically.

1. Update **network** drivers (Wi-Fi and Ethernet) from the vendor or laptop maker.
2. Update **chipset and storage** drivers from the laptop maker's support site.
3. Update **graphics** drivers with a clean installation.
4. Restart between each install to avoid tangled states.
5. Test for a full day before moving on.

### Fix 4: Run SFC and DISM

Repair corrupted driver and system files.

1. Open **Terminal (Admin)** with **Win + X**.
2. Run `sfc /scannow` and wait for completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` if SFC reports unfixable damage.
4. Run `sfc /scannow` once more to confirm.
5. Restart and monitor.

### Fix 5: Test the memory

Eliminate the hardware mimic.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**, press **F1**, and select **Extended**.
3. Run at least two full passes.
4. If errors appear, test sticks individually and replace the faulty one.
5. Clean results mean the problem is software; continue.

### Fix 6: Use Driver Verifier to name the culprit

Force an inconclusive case to identify itself.

1. Create a restore point: search **Create a restore point** in **Start** and click **Create**.
2. Open **Terminal (Admin)** and run `verifier`.
3. Choose **Create standard settings**, then **Automatically select unsigned drivers**, and finish the wizard.
4. Restart and use the laptop; Verifier crashes the guilty driver quickly and informatively.
5. After the crash, run `verifier /reset` (from Safe Mode if needed) and analyze the new dump.
6. Update or remove the named driver.

### Fix 7: Check for overheating and reset BIOS

Remove thermal and configuration variables.

1. Monitor CPU and GPU temperatures under load; sustained extremes are suspect.
2. Clean vents and fans with compressed air.
3. Enter BIOS/UEFI setup and load optimized defaults to clear unstable settings.
4. Disable any overclocking or XMP profiles.
5. Retest under the workloads that crashed.

### Fix 8: Reset Windows if crashes persist

Rebuild when the installation is the problem.

1. Open **Settings** then **System** then **Recovery** and click **Reset PC**.
2. Choose **Keep my files** first.
3. If crashes continue, back up fully and choose **Remove everything**.
4. Install only vendor drivers afterward, testing as you go.

For brand-specific versions, see our [Dell driver IRQL guide](/articles/how-to-fix-driver-irql-not-less-or-equal-on-dell-laptop/) and the [post-update variant](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/). If the blue screen never names a driver, our [unexpected kernel mode trap guide](/articles/how-to-fix-unexpected-kernel-mode-trap-after-windows-11-update/) covers the next-closest relative.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the most helpful blue screen in Windows because it usually signs its own work. Read the filename, replace that driver with the vendor's current version, and the crashes end. For the cases where it names nothing, Driver Verifier and a memory test finish the job. It is common, it is fixable, and it rarely requires anything more dramatic than the right driver installed the right way.
