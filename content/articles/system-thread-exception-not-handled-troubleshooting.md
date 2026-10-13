---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Troubleshooting Guide"
slug: system-thread-exception-not-handled-troubleshooting
date: 2026-09-04
categories: ["windows-errors"]
tags: ["bsod", "drivers", "troubleshooting"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen? A system thread crashed with an unhandled exception. Here's how to trace and fix it."
thumbnail: "/images/thumbs/system-thread-exception-not-handled-troubleshooting.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "A thread running in kernel mode threw an exception (like an access violation) that no error handler caught. Windows bugchecks with stop code 0x7E. It's almost always a faulty, outdated, or incompatible device driver — frequently graphics, Wi-Fi, or chipset drivers."
  - q: "The blue screen shows a file name like atikmdag.sys. What now?"
    a: "That file is the prime suspect. Google the filename to identify its device, then update, roll back, or cleanly reinstall that specific driver. atikmdag.sys is AMD graphics, nvlddmkm.sys is NVIDIA, Netwtw10.sys is Intel Wi-Fi."
  - q: "Can this error be caused by overclocking?"
    a: "Yes — unstable CPU, RAM, or GPU overclocks cause exceptions in system threads regularly. Reset everything to stock speeds in BIOS and in tools like MSI Afterburner before spending time on drivers."
  - q: "What if it crashes in a boot loop and I can't reach Windows?"
    a: "Use the recovery environment: force-power-off three times during boot to reach Automatic Repair, then Troubleshoot > Advanced options > Startup Settings to enter Safe Mode, where the bad driver usually doesn't load and you can remove it."
---

`SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` (0x7E) is Windows' way of saying a background system thread hit an error nobody was prepared for — usually an access violation inside a driver. Unlike some stop codes that point at hardware, this one points at software the vast majority of the time, and the blue screen often names the offending file.

That filename is your biggest shortcut. If you saw something like `nvlddmkm.sys` or `igdkmd64.sys`, you already know which driver to attack. If the screen flashed by too fast, the steps below show how to recover that information.

## Why this happens

- **Faulty graphics driver**: The most common cause by far — GPU drivers run complex kernel threads, and a buggy version throws unhandled exceptions regularly.
- **Bad network or Wi-Fi driver**: Second most common, especially Realtek, Intel, and Qualcomm wireless drivers after Windows updates.
- **Incompatible driver after a Windows update**: A driver that worked on the old build throws exceptions under the new kernel's stricter handling.
- **Corrupted driver or system files**: Damaged .sys files or kernel components crash threads that would otherwise run fine.
- **Overclocking instability**: Unstable CPU/RAM/GPU clocks cause random exceptions in kernel threads.
- **Failing RAM or storage**: Less common for this code, but bad memory corrupts thread data and a dying drive corrupts loaded drivers.

## How to fix it

Work through these in order — identify the driver, then fix or remove it.

### Fix 1: Identify the driver from the crash dump

Don't guess. Read the dump.

1. Download **BlueScreenView** (NirSoft, free) and point it at `C:\Windows\Minidump`.
2. Open the latest dump and check **Caused By Driver** — that's your suspect.
3. Common mappings: `nvlddmkm.sys` = NVIDIA GPU, `atikmdag.sys`/`amdkmdag.sys` = AMD GPU, `igdkmd64.sys` = Intel graphics, `Netwtw10.sys` = Intel Wi-Fi, `rtwlane.sys` = Realtek Wi-Fi.
4. If you can't boot into Windows, access dumps from Safe Mode (Fix 2) or copy them via the recovery command prompt.
5. Our [general blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) has more on dump analysis if you want to go deeper.

### Fix 2: Boot into Safe Mode

Safe Mode loads a minimal driver set — if the laptop is stable there, a third-party driver is confirmed as the cause.

1. Force Automatic Repair: power on, and when the Windows logo appears, hold the power button until it shuts off. Do this three times.
2. On the fourth boot, click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode.
4. If stable, proceed with the driver fixes below from within Safe Mode (with Networking, option 5, if you need to download drivers).
5. If it crashes in Safe Mode too, skip to Fix 6 (system repair) and Fix 7 (hardware).

### Fix 3: Update the suspect driver

A newer driver often fixes the exact exception you're hitting — vendors patch these crashes constantly.

1. In **Device Manager** (**Win + X** > **Device Manager**), locate the device matching your suspect file.
2. Right-click > **Update driver** > **Search automatically for drivers**.
3. Then get the latest from the source: [NVIDIA](https://www.nvidia.com/Download/index.aspx) for GeForce, [AMD](https://www.amd.com/en/support/download/drivers.html) for Radeon, [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics/Wi-Fi — or your laptop maker's page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
4. For GPU drivers, choose **Clean installation** in the installer to wipe old settings and profiles.
5. Restart and test with the workload that used to crash (gaming, video calls, heavy browsing).

### Fix 4: Roll back or cleanly reinstall the driver

If the crash started after a driver update, the new driver is guilty.

1. In **Device Manager**, right-click the device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If roll-back isn't available, do a clean reinstall: right-click > **Uninstall device**, check **Delete the driver software for this device**, restart, then install the manufacturer's driver fresh.
3. For NVIDIA/AMD GPUs, use **Display Driver Uninstaller (DDU)** in Safe Mode for the most thorough cleanup — it removes every trace of the old driver before you install the new one.
4. Block the bad version with Microsoft's **Show or hide updates** troubleshooter so Windows Update doesn't reinstall it.

### Fix 5: Reset overclocks

Unstable clocks cause unhandled exceptions in kernel threads — rule this out early if you overclock anything.

1. Enter BIOS/UEFI and load **Optimized Defaults** (disables CPU overclock and XMP).
2. Reset MSI Afterburner, Intel XTU, Ryzen Master, or any GPU tuning tool to stock.
3. Save, reboot, and test. If the crashes stop, reintroduce overclocks gradually — or leave stock for stability.

### Fix 6: Repair system files

Corrupted system components can throw exceptions in their own threads.

1. Open an elevated Command Prompt: **Win + S**, type `cmd`, right-click > **Run as administrator**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. Restart and test.
4. If SFC reports corruption it can't repair and crashes continue, run an in-place upgrade using [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) — it reinstalls Windows while keeping files and apps.

### Fix 7: Test RAM and storage

If dumps blame the kernel (`ntoskrnl.exe`) rather than a specific driver, suspect hardware feeding bad data to innocent threads.

1. Run `mdsched.exe` (**Win + R**) and choose **Restart now and check for problems**. Any error = bad RAM.
2. Run `chkdsk C: /f /r` from an elevated prompt to check the drive.
3. Check SMART health with your manufacturer's diagnostics.
4. Related stop codes with similar driver-first workflows: our guides on [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/driver-irql-not-less-or-equal-blue-screen-error-fix/) and [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED's cousin, the Driver Verifier IOManager violation](/articles/driver-verifier-iomanager-violation-blue-screen-error-fix/).

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is one of the more diagnosable blue screens because it usually names its culprit. Read the dump, identify the driver, and update or cleanly reinstall it — checking overclocks and system file integrity along the way. In most cases the fix is a single driver, and once it's sorted the crashes stop completely.
