---
title: "Driver IRQL Not Less or Equal: A Full Troubleshooting Guide"
slug: driver-irql-not-less-or-equal-troubleshooting
date: 2026-09-05
categories: ["windows-errors"]
tags: ["blue screen", "driver troubleshooting", "stop code 0xD1"]
description: "A complete troubleshooting walkthrough for DRIVER_IRQL_NOT_LESS_OR_EQUAL, from reading the dump file to verifying the permanent fix."
thumbnail: "/images/thumbs/driver-irql-not-less-or-equal-troubleshooting.webp"
faqs:
  - q: "How do I find which driver caused the crash?"
    a: "The blue screen itself usually names a .sys file. If you missed it, open the minidump in WinDbg Preview (free from the Microsoft Store) and run the !analyze -v command — the MODULE_NAME and IMAGE_NAME fields identify the driver. BlueScreenView is a simpler alternative that lists the suspect driver in a table."
  - q: "What does stop code 0x000000D1 mean?"
    a: "It is the numeric code for DRIVER_IRQL_NOT_LESS_OR_EQUAL. A kernel-mode driver attempted to access pageable memory (or an invalid address) while running at an elevated interrupt level. The four parameters in parentheses encode the memory address, the IRQL, the operation type, and the address that referenced the memory."
  - q: "Can a Windows feature update trigger this repeatedly?"
    a: "Yes, and it is a well-known pattern: a feature update replaces a working manufacturer driver with a generic inbox driver, and the generic one crashes on your specific hardware. Rolling back the driver and then blocking that specific driver update prevents the cycle."
  - q: "How do I confirm the fix actually worked?"
    a: "Reproduce the original crash conditions — the game, the video call, the large file copy — and run the machine for at least 48 hours of normal use. Check Reliability Monitor (type perfmon /rel) for a clean history with no new critical events before declaring victory."
---
This guide takes a different approach from a quick-fix list. **DRIVER_IRQL_NOT_LESS_OR_EQUAL** (stop code `0xD1`) deserves real troubleshooting because the same blue screen can come from a Wi-Fi driver, a GPU driver, bad RAM, or a dying SSD — and treating the wrong one wastes your weekend. Here you will diagnose first, then fix with confidence.

The method: capture the evidence, identify the driver, verify with targeted tests, apply the fix, and confirm stability. Every step builds on the last.

## Why this happens

- **A driver accessing invalid memory at high IRQL:** The textbook cause — a bug in the driver's memory handling, often in network, graphics, or storage drivers.
- **Driver replaced by Windows Update:** A generic driver swapped in over a working manufacturer driver, incompatible with your exact hardware revision.
- **Corrupt driver binaries:** Disk errors or a bad install leaving a driver file half-written.
- **Failing RAM:** Bit flips corrupt driver data structures, producing crashes that blame innocent drivers.
- **Overheating GPU or unstable overclock:** Hardware instability that manifests inside driver code paths.
- **Filter-driver conflicts:** Antivirus, VPN, or disk-utility filter drivers interfering with the device driver beneath them.
- **Failing storage:** A dying drive corrupting driver files or paging data at the wrong moment.

## How to fix it

Work through these in order. This is a diagnostic sequence — resist the urge to reinstall drivers blindly until Fix 3 tells you which one.

### Fix 1: Capture the crash evidence

You cannot troubleshoot what you cannot see. Make sure Windows is saving crash data.

1. Open **Settings > System > About > Advanced system settings**, and under **Startup and Recovery** click **Settings**.
2. Set **Write debugging information** to **Small memory dump (256 KB)** and uncheck **Automatically restart** so you can read the blue screen.
3. Note the exact stop code parameters and any `.sys` filename on the next crash — photograph the screen.
4. After rebooting, open **Reliability Monitor** (press **Win + R**, type `perfmon /rel`) and check the timeline for the pattern: same time of day, same application running, or totally random. Patterns point at triggers.

### Fix 2: Identify the suspect driver from the dump

The minidump names names. Read it before changing anything.

1. Install **WinDbg Preview** from the Microsoft Store, open it, and load the newest file from `C:\Windows\Minidump`.
2. Run the command `!analyze -v` and read the **MODULE_NAME** / **IMAGE_NAME** fields — that is your prime suspect.
3. If WinDbg feels heavy, **BlueScreenView** (NirSoft) shows the same information in a simple table: the driver highlighted in red is the one to investigate.
4. Write down the driver name and version. Our step-by-step dump-reading tutorial is [how to analyze BSOD dump files on Windows 10](/articles/how-to-analyze-bsod-dump-files-on-windows-10/).

### Fix 3: Verify with Driver Verifier

Before replacing the driver, confirm it is actually guilty — dumps occasionally blame the victim.

1. Press **Win + R**, type `verifier.exe`, press **Enter**, and choose **Create custom settings** with all checks except **Low resources simulation**.
2. Select **Select driver names from a list** and tick only your suspect driver (not every driver — targeted testing is faster and safer).
3. Reboot and reproduce the crash conditions. If Verifier triggers an immediate, consistent crash naming that driver, guilt is confirmed.
4. Run `verifier /reset` from an elevated Command Prompt afterward and reboot.

### Fix 4: Replace the guilty driver with the manufacturer's version

Now fix with precision instead of guesswork.

1. Download the driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/). For GPUs, use NVIDIA or AMD directly; for Intel wireless and chipset, the Intel Driver & Support Assistant.
2. First uninstall the old driver completely: in **Device Manager**, right-click the device, choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.
3. Install the fresh driver, reboot, and retest under the original crash conditions.

### Fix 5: Rule out RAM with a memory test

If dumps blame different drivers on different crashes — the classic sign of bad memory — test the RAM.

1. Run `mdsched.exe` and choose **Restart now and check for problems**.
2. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
3. Replace faulty sticks. When every crash names a different driver, the drivers are innocent and the memory is not.

### Fix 6: Check the drive and repair system files

Corrupt driver binaries and paging errors also produce 0xD1.

1. In an elevated Command Prompt: `chkdsk C: /f /r` (reboot to run it).
2. Then `sfc /scannow`, followed by `DISM /Online /Cleanup-Image /RestoreHealth` and another `sfc /scannow`.
3. Check SMART health for reallocated sectors. Storage-side blue screens have their own patterns — compare with [unexpected-store-exception-windows-11-fix](/articles/unexpected-store-exception-windows-11-fix/) to see if your symptoms match a drive problem instead.

### Fix 7: Eliminate filter-driver conflicts

If the suspect driver is `ndis.sys` or another framework file rather than a device driver, something sitting on top of it is likely at fault.

1. Uninstall third-party antivirus temporarily and test.
2. Remove VPN clients, virtual network adapters, and disk-filter utilities one at a time.
3. Disable non-Microsoft services via **msconfig** (**Win + R** > `msconfig` > **Services** tab > **Hide all Microsoft services** > **Disable all**), reboot, and re-enable in halves to isolate the conflict.

### Fix 8: Confirm stability and lock in the fix

A fix you cannot verify is a guess. Prove it.

1. Reproduce the original trigger repeatedly — the game level, the 4K export, the long video call.
2. Run the machine for 48 hours of normal use and check **Reliability Monitor** for a clean record.
3. To stop Windows Update from re-breaking it, pause updates briefly or hide the specific driver update. Document which driver version works, so a future update gone wrong is a five-minute rollback instead of another weekend.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL rewards methodical work: capture the dump, name the driver, verify with Driver Verifier, replace precisely, and confirm stability. That discipline turns a maddening random crash into a solved problem — and keeps it solved.
