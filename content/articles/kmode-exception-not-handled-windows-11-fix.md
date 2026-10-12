---
title: "How to Fix KMODE_EXCEPTION_NOT_HANDLED on Windows 11"
slug: kmode-exception-not-handled-windows-11-fix
date: 2026-10-07
categories: ["windows-errors"]
tags: ["bsod", "kmode", "drivers", "windows 11"]
description: "KMODE_EXCEPTION_NOT_HANDLED keeps crashing your Windows 11 PC? It's almost always a driver issue. Here are 6 fixes to identify and remove the bad driver."
thumbnail: "/images/thumbs/kmode-exception-not-handled-windows-11-fix.webp"
faqs:
  - q: "What causes KMODE_EXCEPTION_NOT_HANDLED on Windows 11?"
    a: "A kernel-mode driver bug: a driver accesses memory it shouldn't, or throws an exception the kernel can't catch, and Windows halts with this stop code. The usual culprits are graphics, network, or storage drivers — it often appears right after a driver or Windows update."
  - q: "How do I know which driver caused the crash?"
    a: "Check C:\\Windows\\Minidump for .dmp files from the crash time — BlueScreenView or WinDbg Preview can read them and usually name the faulty .sys file. Alternatively, open Event Viewer, go to Windows Logs > System, and look for Error events from BugCheck around the crash timestamp."
  - q: "Can faulty RAM cause KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Yes. Bad memory corrupts the data a driver reads, making a healthy driver look guilty — which is why Fix 5 is the Windows Memory Diagnostic. If successive minidumps blame different drivers, suspect RAM, and run the memory test before replacing drivers repeatedly."
  - q: "Is KMODE_EXCEPTION_NOT_HANDLED a hardware failure?"
    a: "Not usually — it's mostly a software problem: a buggy or incompatible driver, or a corrupted Windows component. Hardware only enters the picture when crashes are random across drivers or persist after a clean reinstall; then RAM and the system drive are the prime suspects."
---

KMODE_EXCEPTION_NOT_HANDLED is one of the most common blue screens on Windows 11, and the good news is hidden in the name: "KMODE" means a kernel-mode program — almost always a driver — did something illegal. That makes this one of the more diagnosable stop codes. Unlike [CRITICAL_PROCESS_DIED](/articles/critical-process-died-windows-11-fix/), where Windows just knows something critical vanished, KMODE crashes usually leave a trail pointing at the guilty driver.

It typically strikes right after a GPU, Wi-Fi, or chipset driver update. Start by identifying the driver (Fix 1), then repair or replace it, then rule out the deeper causes.

## Why this happens

- **Buggy or outdated driver** — A driver with a coding error accesses invalid memory or raises an unhandled exception in kernel mode, the most common cause by far.
- **Conflicting drivers** — Two drivers (for example, an old OEM driver and a newer Windows Update driver) fighting over the same device can trigger the crash.
- **Corrupted driver installation** — An interrupted install or a partial update leaves a driver in a half-working state.
- **Faulty RAM** — Bad memory cells corrupt driver data, making crashes blame a different driver each time.
- **Fast Startup hibernation conflicts** — The hybrid-shutdown kernel session can load stale driver state on boot, especially on dual-boot or older-driver systems.
- **Outdated BIOS/firmware** — Old firmware can misreport hardware to newer drivers, causing illegal memory access.

## How to fix it

Start by identifying the suspect driver (Fix 1), then repair or replace it. Only move to the deeper fixes if the driver work doesn't help.

### Fix 1: Identify the faulty driver from the minidump or Event Viewer

Guessing wastes time. A two-minute check usually names the exact `.sys` file.

1. Press **Win + R**, type `%SystemRoot%\Minidump`, and press Enter. If the folder doesn't exist, enable dumps at **Settings > System > About > Advanced system settings > Startup and Recovery > Settings**, setting "Write debugging information" to **Small memory dump**.
2. Note the newest `.dmp` file. Download **WinDbg Preview** from the Microsoft Store, open the dump, and run `!analyze -v`. The `MODULE_NAME` line — e.g. `nvlddmkm.sys` (NVIDIA) or `rtwlanu.sys` (Realtek Wi-Fi) — identifies the driver.
3. Or open **Event Viewer** (**Win + X**), go to **Windows Logs > System**, and filter **Error** events from **BugCheck** around the crash time.
4. Search the web for the filename to learn which device it belongs to — that tells you which driver to update or remove next.

### Fix 2: Update drivers via Device Manager

If the minidump names a specific driver, update it first. Otherwise, update graphics, network, and chipset drivers — that fixes most cases.

1. Right-click **Start** and open **Device Manager**.
2. Find the matching device — **Display adapters** for GPU, **Network adapters** for Wi-Fi/Ethernet, **Storage controllers** for storage drivers.
3. Right-click it and choose **Update driver > Search automatically for drivers**.
4. For graphics drivers, get the driver directly from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) instead — their releases are newer and better tested than Windows Update's.
5. Restart and use the PC normally before changing anything else, so you know which change worked.

### Fix 3: Roll back the recently updated driver

When blue screens started right after a driver update, the new driver is the suspect.

1. In **Device Manager**, right-click the device, choose **Properties > Driver**, and click **Roll Back Driver** if it's available.
2. Restart and test. If crashes stop, block Windows Update from reinstalling the bad version via **Settings > Windows Update > Advanced options > Optional updates** or Microsoft's **Show or hide updates** troubleshooter.
3. If Roll Back is greyed out, right-click the device and choose **Uninstall device** (check "Attempt to remove the driver for this device" if offered), then install an older stable version from the manufacturer's site.

### Fix 4: Disable Fast Startup

Fast Startup saves the kernel session to disk at shutdown, which can reload corrupted driver state on every boot. Disabling it forces a clean driver load each time.

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, uncheck **Turn on fast startup (recommended)**, and click **Save changes**.
3. Shut down fully (not restart — a restart already bypasses Fast Startup), power back on, and use the PC for a day.
4. If this fixes it, a half-finished update may have left your drivers in the state Fast Startup was tripping over — similar to the mess behind [Windows update stuck at 100 percent](/articles/windows-update-stuck-at-100-percent-fix/).

### Fix 5: Run Windows Memory Diagnostic

If minidumps keep blaming different drivers, the common denominator is probably RAM, not drivers.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The standard test takes 10–30 minutes; press **F1** at the test screen and choose **Extended** for a thorough check.
3. Results appear as a notification after Windows boots; you can also find them in **Event Viewer > Windows Logs > System**, source **MemoryDiagnostics-Results**.
4. If errors are found, reseat the RAM modules and test again. Errors that persist mean the module needs replacing — no driver update will fix bad memory.

### Fix 6: Update BIOS/firmware

An outdated BIOS can feed wrong hardware information to modern drivers, causing kernel exceptions. Treat this as a fix for persistent cases, not a first step.

1. Press **Win + R**, type `msinfo32`, and note **System Manufacturer**, **System Model**, and the current **BIOS Version/Date**.
2. On the manufacturer's support site, check the BIOS section for a version newer than yours — apply it if the release notes mention stability, BSOD, or compatibility fixes.
3. Run the update with the laptop **plugged into AC power** and all other programs closed.
4. **Safety note:** Do not power off or close the lid during a BIOS flash — an interrupted flash can brick the motherboard. This is the only fix here with that risk, which is why it's near the end.

### Fix 7: Clean driver reinstall with Display Driver Uninstaller (DDU)

When updates and rollbacks don't help — especially for GPU-related crashes — leftover files and registry entries from old installs can keep the conflict alive.

1. Download **Display Driver Uninstaller (DDU)** from Wagnardsoft's official site.
2. Boot into **Safe Mode** (hold Shift, click Restart at the login screen, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**).
3. In DDU, select your GPU brand and choose **Clean and restart**.
4. After rebooting, install only your chosen driver — prefer the **Studio/Stable** release over the newest Game Ready/beta. Stay offline during the reinstall if Windows Update keeps grabbing a driver first.

If crashes continue after a clean reinstall, try a clean boot (`msconfig`, disabling non-Microsoft services) — antivirus filters and virtualization drivers are frequent hidden offenders. Crashes on a fresh Windows install point to hardware: run the manufacturer's boot-time diagnostics or visit a repair shop.
