---
title: "How to Troubleshoot DRIVER_IRQL_NOT_LESS_OR_EQUAL on Windows 11"
slug: troubleshoot-driver-irql-not-less-or-equal
date: 2026-09-04
categories: ["windows-errors"]
tags: ["driver irql", "bsod", "driver error", "windows 11"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen on Windows 11? Learn how to identify the faulty driver and fix it step by step."
thumbnail: "/images/thumbs/troubleshoot-driver-irql-not-less-or-equal.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "A driver tried to access memory at an improper interrupt request level — essentially a driver reached for memory it wasn't allowed to touch at that moment. Windows crashes to prevent corruption. The faulting driver's name often appears on the blue screen itself (like nvlddmkm.sys or ndis.sys), which directly identifies the culprit."
  - q: "Which drivers most often cause this error?"
    a: "Network drivers (ndis.sys, Netwtw10.sys), graphics drivers (nvlddmkm.sys, amdkmdag.sys), storage controller drivers (storahci.sys), and third-party antivirus filter drivers. USB device drivers for docks and adapters are also frequent offenders on laptops. If the blue screen names a .sys file, that file's driver is your prime suspect."
  - q: "Can faulty RAM cause DRIVER_IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes, though it's less common than a bad driver. Failing memory can corrupt the data structures drivers rely on, producing this exact stop code. If driver updates and rollbacks don't help, run Windows Memory Diagnostic. RAM-caused cases often come with additional random stop codes rather than the same one every time."
  - q: "Is it safe to use Driver Verifier to find the bad driver?"
    a: "Driver Verifier is powerful but aggressive — it intentionally crashes the system when a driver misbehaves, which can create boot loops if misused. Only enable it for specific third-party drivers, never all drivers at once, and know how to disable it from Safe Mode (verifier /reset) before you start. For most users, the minidump analysis in Fix 1 is safer."
---
DRIVER_IRQL_NOT_LESS_OR_EQUAL is the blue screen that actually tries to help you: it frequently prints the name of the guilty driver right on the screen. That little `.sys` filename is a gift — it turns a mysterious crash into a targeted fix. Even when the screen doesn't name a driver, the minidump files Windows saves after each crash contain the answer, and free tools can read them.

This guide shows you how to identify the culprit first, then fix it — instead of blindly updating everything.

## Why this happens

- **A buggy or outdated driver.** The classic cause: a driver accessing paged memory at the wrong interrupt level, usually after a Windows update changed the rules.
- **Corrupted driver files.** Disk errors or interrupted installs can damage a driver that was previously fine.
- **Conflicting drivers.** Two drivers fighting over the same hardware (common with USB docks and virtual network adapters) trigger this error.
- **Overclocked or unstable hardware.** An unstable CPU or RAM overclock corrupts driver operations.
- **Third-party antivirus filters.** AV kernel drivers intercept system calls; a bug in the filter crashes with this stop code.
- **Failing RAM.** Bad memory corrupts driver data structures, mimicking a driver bug.

## How to fix it

Work through these in order — identify first, then fix.

### Fix 1: Identify the faulty driver from the crash dump

Don't guess — read the evidence Windows already collected.

1. Note any `.sys` filename shown on the blue screen itself (e.g., `Netwtw10.sys` = Intel Wi-Fi, `nvlddmkm.sys` = NVIDIA graphics).
2. Download the free tool BlueScreenView (NirSoft) and run it — it lists every crash and highlights the faulting driver in red.
3. Alternatively, open **C:\Windows\Minidump** in File Explorer; the most recent `.dmp` file corresponds to your latest crash.
4. Once you know the driver name, you know exactly which device to update, roll back, or reinstall in the next steps.

### Fix 2: Roll back or update the identified driver

Target the specific driver from Fix 1.

1. Open **Device Manager**, find the device matching the faulty driver, right-click it, and choose **Properties > Driver**.
2. If **Roll Back Driver** is available, use it — the previous version was stable.
3. If not, choose **Uninstall device**, check **Attempt to remove the driver for this device** if offered, and restart — Windows installs a clean baseline driver.
4. Then install the latest stable driver from your laptop maker's official support site, not from a driver-updater utility.

### Fix 3: Update all major drivers from official sources

If no single driver was identified, refresh the usual suspects.

1. Install the latest chipset driver from your laptop maker's site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Update graphics from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Update Wi-Fi, Bluetooth, and storage controller drivers from the laptop maker's page.
4. Restart after each major driver and test — don't batch-install five drivers and lose track of which one mattered.

### Fix 4: Remove third-party antivirus filter drivers

AV filters are a disproportionate cause of this stop code.

1. Fully uninstall any third-party antivirus from **Settings > Apps > Installed apps** — disabling leaves the kernel filter loaded.
2. Restart and use **Windows Security** for a day or two of normal use.
3. If crashes stop, the AV filter was the cause. Reinstall only the latest version, or stay with Windows Security.
4. Some AV products leave filter drivers behind after uninstall — check **Device Manager > View > Show hidden devices > Non-plug and play drivers** for leftovers.

### Fix 5: Run SFC, DISM, and check the disk

Corrupted system and driver files need repairing.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` and restart if prompted to scan for file system errors.
4. Retest. File corruption that damaged a driver binary is fixed here without touching your data.

### Fix 6: Test the memory

If the same stop code persists across driver changes, suspect RAM.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If errors appear, reseat the RAM modules and test again.
3. With multiple sticks, test one at a time to isolate the faulty module.
4. Replace the bad stick — and if you recently added RAM, verify it's on your laptop's compatibility list. The [memory management BSOD guide](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) covers deeper RAM diagnostics.

### Fix 7: Clean-install the driver stack as a last resort

When the driver situation is thoroughly tangled, start fresh.

1. Download DDU (Display Driver Uninstaller) for graphics issues, or use Device Manager's driver removal for other devices.
2. Boot into Safe Mode and remove every trace of the problematic driver.
3. Restart and install only the manufacturer's recommended driver version — not necessarily the newest, but the one your laptop maker validates.
4. If crashes continue even with a clean driver stack and passing memory tests, run the deeper [IRQL troubleshooting variant](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/) and consider professional diagnostics for a motherboard fault.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL rewards methodical work: read the dump, name the driver, fix that driver. The users who struggle are the ones who update everything at random and never learn which change mattered.

Keep BlueScreenView installed — the next time any blue screen appears, you'll have the answer in thirty seconds instead of an evening of guesswork. And build one preventive habit: before installing any driver update, create a manual restore point from **Control Panel > System > System Protection**. If the new driver crashes, you roll back in minutes instead of fighting the recovery environment. Driver problems are a when, not an if, on Windows — being ready for them is what separates a quick fix from a lost weekend.
