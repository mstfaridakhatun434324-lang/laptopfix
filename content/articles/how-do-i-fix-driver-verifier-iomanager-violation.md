---
title: "How to Fix DRIVER_VERIFIER_IOMANAGER_VIOLATION (Step by Step)"
slug: how-do-i-fix-driver-verifier-iomanager-violation
date: 2026-10-04
categories: ["windows-errors"]
tags: ["blue screen", "driver verifier", "windows 11"]
description: "Stuck in a DRIVER_VERIFIER_IOMANAGER_VIOLATION crash loop? Here's how to turn off Driver Verifier safely and fix the driver it caught."
thumbnail: "/images/thumbs/how-do-i-fix-driver-verifier-iomanager-violation.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_IOMANAGER_VIOLATION?"
    a: "Stop code 0x000000C9: Driver Verifier — Windows' built-in driver stress-testing tool — caught a driver mishandling I/O requests. This crash only happens when Verifier is deliberately enabled, so the first step is usually turning Verifier off to regain a bootable system."
  - q: "I didn't turn on Driver Verifier. Why am I seeing this?"
    a: "Someone or something enabled it — sometimes a support technician, a debugging tutorial, or rarely malware. It doesn't turn itself on. The priority is disabling it from Safe Mode or WinRE, then investigating which driver it flagged."
  - q: "Is the driver Verifier caught actually broken?"
    a: "Usually yes, or at least buggy under stress. Verifier is aggressive by design and can flag minor issues, but a C9 crash means the driver genuinely mishandled an I/O request. Update or replace that driver."
  - q: "How do I turn off Driver Verifier if Windows won't boot?"
    a: "Boot into Safe Mode (Verifier doesn't apply there the same way) or WinRE's Command Prompt, then run verifier /reset or delete the verify settings via the registry. Full steps are in Fix 1 below."
---
DRIVER_VERIFIER_IOMANAGER_VIOLATION (stop code 0x000000C9) is a special blue screen: it means Driver Verifier — a Windows testing tool you (or someone) switched on — caught a driver breaking I/O rules. Verifier is deliberately brutal, so the crash is Verifier doing its job. Your job now is twofold: turn Verifier off to get a working system back, then deal with the driver it caught.

If Windows still boots between crashes, start at Fix 1. If you're in a crash loop, use Safe Mode or WinRE as described. For the deeper diagnostic approach to Verifier-flagged drivers, see our companion [troubleshooting guide](/articles/troubleshoot-driver-verifier-iomanager-violation/).

## Why this happens

- **Driver Verifier is enabled.** This crash cannot happen without it — that's the defining fact.
- **A driver mishandles I/O request packets (IRPs).** The actual bug Verifier caught.
- **Verifier was left on after debugging.** The most common scenario — someone forgot to disable it.
- **An outdated driver under Verifier's stress.** Old drivers fail Verifier's strict checks.
- **Verifier configured too broadly.** Verifying all drivers at once guarantees crashes on most systems.
- **A recent driver update introduced the bug.** New driver + Verifier still on = crash loop.
- **Corrupted driver files.** Damaged binaries fail even basic I/O handling.

## How to fix it

Work through these in order — stabilize first, diagnose second.

### Fix 1: Disable Driver Verifier immediately

Stop the crash loop before anything else.

1. If Windows boots, press **Win + R**, type `verifier.exe`, and press **Enter**.
2. Choose **Delete existing settings** and click **Finish**, then restart.
3. If Windows won't boot normally, force WinRE (interrupt boot 2-3 times), go to **Troubleshoot > Advanced options > Startup Settings > Restart**, and press **4** for Safe Mode.
4. In Safe Mode, open an elevated Command Prompt and run:
   `verifier /reset`
5. Restart normally. The C9 crashes should stop — if they continue, Verifier settings may be stuck; in WinRE's Command Prompt, run `verifier /reset` there too.
6. Confirm Verifier is off by running `verifier.exe` again — it should show **No settings have been set**.

### Fix 2: Identify which driver Verifier flagged

The dump tells you who the culprit is.

1. With Verifier off and the system stable, open **Event Viewer > Windows Logs > System**.
2. Find the **BugCheck** entries from the C9 crashes — note any named driver.
3. Check `C:\Windows\Minidump` for the crash dumps; the newest one corresponds to the Verifier crash.
4. If you can read dumps (WinDbg from the Microsoft Store), the faulting driver is in the stack — otherwise the Event Viewer name is usually enough.
5. Common offenders: storage filter drivers, antivirus drivers, and old peripheral drivers.
6. Write down the driver name and its device — you'll target it in Fix 3.

### Fix 3: Update or replace the flagged driver

Fix the actual bug Verifier found.

1. Open **Device Manager** (**Win + X > Device Manager**) and locate the device.
2. Right-click, choose **Update driver > Search automatically for drivers**.
3. Better: download the latest driver from the manufacturer's official site — [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or your laptop maker's support page.
4. If the driver is already the latest, try rolling back to the previous version — new bugs happen.
5. For third-party filter drivers (antivirus, disk tools), update the parent application to its latest release.
6. Restart and use the system normally for a few days to confirm stability before even thinking about Verifier again.

### Fix 4: Repair corrupted driver files

If the driver binaries themselves are damaged.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Then:
   `sfc /scannow`
4. Restart.
5. SFC restores damaged inbox drivers (like `fltmgr.sys` and storage drivers) from clean copies.
6. Reinstall the third-party driver from Fix 3 afterward to ensure you have intact, current binaries.

### Fix 5: Check for the enabling cause

Make sure Verifier doesn't get turned back on.

1. Ask yourself (or whoever maintains the PC) why Verifier was enabled — leftover debugging is the usual answer.
2. Check **Task Scheduler** for any automated debugging or driver-testing tasks.
3. Run a full Windows Security scan — malware very occasionally enables Verifier to destabilize systems.
4. If a technician enabled it, let them know the session is over and it must stay off.
5. Document the flagged driver and the fix for future reference.
6. Microsoft's driver development docs on [support.microsoft.com](https://support.microsoft.com/en-us/windows) explain Verifier's intended (temporary) use.

### Fix 6: Test RAM and disk

Rule out hardware corrupting the driver's I/O.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. Run `chkdsk C: /f` from an elevated terminal to check the file system.
4. If Verifier flagged a storage driver specifically, check drive health: `wmic diskdrive get status` should say **OK**.
5. Hardware faults can make good drivers look buggy to Verifier — don't skip this.
6. Our [PAGE_FAULT_IN_NONPAGED_AREA guide](/articles/page-fault-in-nonpaged-area-blue-screen-error-fix/) covers memory diagnosis if errors appear.

### Fix 7: Re-enable Verifier properly (optional, advanced)

Only if you actually need to debug the driver further.

1. First confirm days of stability with Verifier off.
2. Run `verifier.exe` and choose **Create custom settings**, selecting only **I/O Verification**.
3. Choose **Select driver names from a list** and tick ONLY the suspect driver — never all drivers.
4. Click **Finish** and restart. Use the system briefly to capture a clean, targeted crash dump.
5. Analyze the dump, fix the driver, then immediately run `verifier /reset`.
6. Never leave Verifier running on a daily-use machine — it's a lab tool, not a resident guard.

## Closing

DRIVER_VERIFIER_IOMANAGER_VIOLATION is good news disguised as a crash: Verifier found a real driver bug for you. Turn Verifier off, fix that driver, and move on — the whole episode usually resolves in under an hour. The cardinal rule going forward: Verifier is a temporary diagnostic instrument. Enable it narrowly, capture your evidence, and switch it off. A Verifier left running is a crash loop waiting to happen.
