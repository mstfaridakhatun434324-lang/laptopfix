---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY Blue Screen on Windows 11"
slug: how-do-i-fix-attempted-execute-of-noexecute-memory
date: 2026-09-08
categories: ["windows-errors"]
tags: ["blue screen", "bsod", "memory error"]
description: "Seeing ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on Windows 11? This guide explains the driver and memory causes and how to fix the blue screen."
thumbnail: "/images/thumbs/how-do-i-fix-attempted-execute-of-noexecute-memory.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "It means a program or driver tried to run code from a memory area marked as no-execute. Windows uses this protection to block malicious or corrupted code, so the error usually points to a faulty driver, damaged RAM, or malware interfering with memory."
  - q: "Is this blue screen a sign of failing RAM?"
    a: "It can be, but software is the more common cause. Buggy drivers, overclocked memory, and corrupted system files cause it far more often than physically bad RAM. Run the Windows Memory Diagnostic to check your RAM before buying replacements."
  - q: "Can a driver update cause this error?"
    a: "Yes. A newly installed graphics, network, or storage driver with a bug can trigger this blue screen immediately after the update. If the error started right after a driver change, roll back or reinstall that driver first."
  - q: "Should I use Driver Verifier to find the cause?"
    a: "Driver Verifier can identify the bad driver, but use it carefully. Run it only long enough to reproduce the crash, then disable it, because it intentionally crashes the system and can make Windows unstable while active."
---

Your laptop was working fine, then the screen went blue and mentioned ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY. It might happen once and never return, or it might crash every time you open a particular program. Either way, the name alone is enough to make anyone nervous.

Here is the short version: Windows caught something trying to run code from a region of memory that was supposed to hold only data. That is a classic sign of a buggy driver, unstable overclocked memory, or malware. The fix is methodical, and in most cases you will find the culprit in a few steps.

## Why this happens

- **Faulty device driver.** A driver with a bug tries to execute instructions from memory marked non-executable. Graphics, network, and chipset drivers are the usual suspects.
- **Corrupted system files.** Damaged Windows kernel files can misreport memory permissions, triggering a false protection fault.
- **Unstable or mismatched RAM.** Overclocked memory, wrong voltage, or failing sticks can corrupt what the CPU thinks is executable code.
- **Malware.** Malicious code often tries to execute from data regions, which is exactly what this protection is designed to catch.
- **Bad Windows update.** An update can replace a stable driver with a broken version or leave system files half-installed.
- **Overclocking or XMP issues.** Aggressive memory timings push RAM past its stable limits, causing intermittent memory errors that surface as this stop code.
- **Failing storage.** A dying SSD can deliver corrupted driver files to memory, producing faults that look like memory problems.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Boot into Safe Mode and remove the recent change

Safe Mode loads only essential drivers, so it usually survives long enough to undo the problem.

1. Hold the **Shift** key while clicking **Power** > **Restart** in the Start menu to reach the recovery screen.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** and click **Restart**.
3. Press **4** for Safe Mode, or **5** if you need networking.
4. In Safe Mode, open **Device Manager** and check if you recently updated a driver. Right-click it and choose **Properties** > **Driver** > **Roll Back Driver** if the option is available.

### Fix 2: Update or reinstall the suspect driver

The most common trigger is a buggy driver, and graphics drivers lead the pack.

1. Open **Device Manager** by pressing **Windows key + X**.
2. Expand **Display adapters**, right-click your GPU, and choose **Update driver** > **Search automatically for drivers**.
3. If that does not help, download the latest driver directly from the manufacturer. Use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics, [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) for GeForce cards, or [AMD drivers](https://www.amd.com/en/support/download/drivers.html) for Radeon.
4. Perform a clean installation if the installer offers it, which removes the old driver first.

### Fix 3: Test your RAM with Windows Memory Diagnostic

Rule out hardware before going deeper.

1. Press **Windows key + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. The laptop will reboot into the memory test. Let it finish both passes.
4. When Windows boots back up, press **Windows key + X**, open **Event Viewer**, and look under **Windows Logs** > **System** for MemoryDiagnostics results.
5. If errors are found, reseat the RAM sticks or test them one at a time to find the bad one.

### Fix 4: Scan for corrupted system files

Damaged Windows files can cause exactly this stop code.

1. Press **Windows key + X** and choose **Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to complete.
3. If problems remain, run `DISM /Online /Cleanup-Image /RestoreHealth` and then run `sfc /scannow` again.
4. Restart the laptop and use it normally to see if the blue screen returns.

### Fix 5: Run a full malware scan

Since this error flags suspicious code execution, check for infection.

1. Open **Windows Security** from the Start menu.
2. Go to **Virus & threat protection** > **Scan options**.
3. Select **Microsoft Defender Offline scan** and click **Scan now**.
4. The laptop will reboot into a deep scan outside of Windows. Remove anything it finds.

### Fix 6: Undo overclocking and memory tweaks

If you enabled XMP or any overclock, dial it back.

1. Restart and enter the BIOS or UEFI, usually by pressing **F2** or **Del** during boot.
2. Find the memory settings and disable **XMP** or **EXPO** profile, or set RAM to its stock speed.
3. Save with **F10** and exit.
4. Use the laptop for a day at stock settings. If the crashes stop, your memory was not stable at the higher profile.

### Fix 7: Use Driver Verifier to identify the bad driver

When nothing else points to a culprit, this tool forces the faulty driver to reveal itself.

1. In an elevated Terminal, run `verifier` to open Driver Verifier Manager.
2. Choose **Create standard settings** and select the non-Microsoft drivers you suspect.
3. Restart and use the laptop normally. Verifier will crash the system with a driver-specific stop code when the bad driver misbehaves.
4. Read the dump or check **Event Viewer** to identify the driver name, then update or remove it.
5. Boot into Safe Mode and run `verifier /reset` to disable Verifier. Do not leave it running permanently.

For more on similar memory stop codes, see our guides on [fixing memory management blue screens](/articles/memory-management-bsod-windows-11-fix/) and the dedicated walkthrough for this exact error: [ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen fix](/articles/attempted-execute-of-noexecute-memory-blue-screen-error-fix/). Microsoft documents general blue screen troubleshooting steps on their [support site](https://support.microsoft.com/en-us/windows).

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY sounds alarming, but it is a protection mechanism doing its job, and the underlying cause is usually a driver you can update or memory timings you can reset. Work from the least invasive fixes outward: Safe Mode, drivers, memory test, system file repair. If the RAM test passes and fresh drivers do not help, a clean Windows reinstall is the reliable last resort before suspecting hardware failure.
