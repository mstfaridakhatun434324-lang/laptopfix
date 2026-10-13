---
title: "\"Your PC Ran Into a Problem\" in Windows 11? Do This"
slug: troubleshoot-your-pc-ran-into-a-problem
date: 2026-09-04
categories: ["windows-errors"]
tags: ["your pc ran into a problem", "bsod", "stop code", "windows 11"]
description: "Stuck on 'Your PC ran into a problem and needs to restart'? Capture the stop code and fix the real cause with this guide."
thumbnail: "/images/thumbs/troubleshoot-your-pc-ran-into-a-problem.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' mean?"
    a: "It's the user-facing text of a Windows stop error (blue screen). Underneath it is a specific stop code like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL that identifies the actual failure. The generic message tells you almost nothing — the stop code, found in Event Viewer or the minidump, tells you everything."
  - q: "How do I find the stop code after the blue screen?"
    a: "Open Event Viewer > Windows Logs > System and find the BugCheck event at the crash time — it lists the code (e.g. 0x0000001A). Or open the minidump in C:\\Windows\\Minidump with WinDbg and run !analyze -v. You can also disable automatic restart so the blue screen stays visible long enough to photograph the code."
  - q: "Is 'Your PC ran into a problem' serious?"
    a: "It ranges from trivial to serious. A one-time crash after a driver update is usually harmless once the driver is fixed. Repeated crashes with the same stop code indicate a real problem — bad driver, failing RAM, or corrupt system files — that the steps below will identify. Repeated crashes with different codes each time suggest failing hardware."
  - q: "Will my files be deleted by the automatic restart?"
    a: "No. The restart itself doesn't touch your files — but unsaved work in open programs is lost, which is why frequent crashes are disruptive. The fixes below (driver updates, SFC scans, memory tests) don't delete personal files either. Only use reset options marked 'Remove everything' if you explicitly intend to wipe the machine."
---

**"Your PC ran into a problem and needs to restart"** is Windows 11's polite mask for a blue screen of death. The message is deliberately generic — the real information is the **stop code** (like `CRITICAL_PROCESS_DIED` or `0x000000EF`) printed in small text at the bottom of the screen. Everything in this guide starts from one principle: the generic message tells you nothing, the stop code tells you everything, so step one is always capturing it.

Most people see this screen once, reboot, and move on — which is fine for a one-off. But if it repeats, you need the code and a method. The workflow below: capture the code, stop the auto-restart so you can read future crashes, identify the cause family from the code, then apply the targeted fix. For reading crash dumps in depth, see [how to read dump files with WinDbg](/articles/how-to-read-dump-files-with-windbg-in-windows-11-24h2/); to keep the blue screen visible, [disable automatic restart after BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/).

## Why this happens

- **Faulty device drivers**: The most common cause overall — a driver crashes the kernel and Windows stops.
- **Failing RAM**: Bad memory corrupting kernel data, producing various stop codes.
- **Corrupt system files**: Damaged Windows components crashing during normal operation.
- **A recent Windows or driver update**: New code introducing a bug on your specific hardware.
- **Overheating**: Thermal emergencies forcing hardware-level halts.
- **Failing storage**: A dying drive corrupting data the kernel depends on.
- **Conflicting software**: Antivirus filters, "optimizers," and virtualization tools destabilizing the kernel.
- **Failing hardware**: Motherboard, CPU, or power delivery faults — suspected when codes vary crash to crash.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the stop code

You can't fix what you can't name.

1. The next time the blue screen appears, photograph it with your phone — the stop code is at the bottom (e.g. `MEMORY_MANAGEMENT`, `0x0000001A`).
2. If it restarts too fast to read, disable auto-restart: **Win + R** > `sysdm.cpl` > **Advanced** tab > **Startup and Recovery** > **Settings** > uncheck **Automatically restart**.
3. After the next crash, open **Event Viewer** > **Windows Logs** > **System**, find the **BugCheck** event, and note the code and any named driver file.
4. Write the code down. Every remaining fix branches from it.

### Fix 2: Check what changed recently

Most repeat crashes start with a change.

1. Ask: did this start after a **Windows update**, a **driver update**, new **software**, or new **hardware**? Check **Settings** > **Windows Update** > **Update history** for dates.
2. If a Windows update matches the timeline, uninstall it: **Update history** > **Uninstall updates** > remove the most recent quality update, then test.
3. If a driver update matches, roll it back in **Device Manager** > device **Properties** > **Driver** > **Roll Back Driver**.
4. If new software matches, uninstall it and test. Recent-change correlation solves a large share of cases immediately.

### Fix 3: Boot into Safe Mode to isolate the cause

One test splits the suspect list in half.

1. Hold **Shift** > **Restart** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
2. Stable in Safe Mode = third-party driver or startup program. Unstable in Safe Mode = hardware, core files, or Microsoft drivers.
3. If stable in Safe Mode, continue with Fixes 4 and 6. If unstable, prioritize Fixes 5 and 7.
4. Don't skip this — it prevents hours of updating the wrong drivers.

### Fix 4: Update or reinstall the implicated driver

For crashes naming a driver file or a driver-class stop code.

1. Identify the driver from the BugCheck event or minidump (WinDbg `!analyze -v` shows `IMAGE_NAME`).
2. In **Device Manager**, update that device's driver (**Update driver** > **Search automatically**).
3. Better: download the manufacturer's build from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) (Intel, NVIDIA, and AMD host chip-level drivers on their own download pages), uninstall the old driver, restart, and install fresh.
4. Test under the conditions that crashed. Driver fixes resolve the majority of single-code repeat crashes.

### Fix 5: Repair system files and the disk

For crashes with no clear driver and no recent change.

1. Open **Terminal (Admin)**. Run `sfc /scannow`.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` and restart to let it scan.
4. Retest. File and filesystem corruption cause a meaningful minority of generic blue screens.

### Fix 6: Clean-boot to find conflicting software

For crashes that happen in normal mode but not Safe Mode.

1. **Win + R** > `msconfig` > **Services** tab > tick **Hide all Microsoft services** > **Disable all**.
2. **Task Manager** > **Startup apps** > disable everything. Restart.
3. If crashes stop, re-enable in halves until the crash returns — the culprit is in the last half. Antivirus, VPNs, and "game boosters" are usual suspects.
4. Uninstall the offending program properly and re-enable everything else.

### Fix 7: Test RAM and thermals

For crashes with varying codes, or crashes under load.

1. Run the Windows Memory Diagnostic: **Win + R** > `mdsched.exe` > **Restart now and check for problems**. Replace faulty RAM.
2. Monitor temperatures with HWMonitor during the crashing workload — sustained CPU temps above 95°C indicate a cooling problem. Clean vents with compressed air.
3. If codes differ every crash and RAM passes, suspect the motherboard or storage: check SSD health with the manufacturer's tool.
4. Check Microsoft's support site for known issues with your Windows build as a final step before hardware service.

## Closing

"Your PC ran into a problem" is a symptom report, not a diagnosis — the stop code is the diagnosis, and everything flows from capturing it. Work the order above: code, recent changes, Safe Mode split, targeted driver fix, file repair, software conflicts, hardware tests. One-time crashes need no action beyond noting the code; repeating crashes need the method, and the method ends with either a fixed driver or a definitive hardware answer. Keep a simple crash log — date, code, and what you were doing — and patterns that are invisible from memory become obvious on paper.
