---
title: "How to Fix the DRIVER_IRQL_NOT_LESS_OR_EQUAL Blue Screen"
slug: how-to-fix-driver-irql-not-less-or-equal
date: 2026-09-18
categories: ["windows-errors"]
tags: ["irql not less or equal", "bsod", "driver error", "windows 11"]
description: "The DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen means a driver touched memory it shouldn't. Here's how to find the driver and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal.webp"
faqs:
  - q: "What does Driver IRQL Not Less or Equal mean?"
    a: "A kernel-mode driver tried to access paged memory while running at an elevated interrupt request level (IRQL) — something Windows forbids because the memory might not be present. Stop code 0x000000D1. The blue screen usually names the offending .sys file, identifying the exact driver. Network and storage drivers are the most frequent offenders."
  - q: "Which drivers cause this error most often?"
    a: "Network drivers top the list — Wi-Fi and Ethernet drivers from Intel, Realtek, and Killer mishandle power-state transitions and trigger this. Storage controller drivers and graphics drivers follow. Antivirus filter drivers are another classic source. The named file on the blue screen tells you which category your crash belongs to."
  - q: "Can faulty RAM cause IRQL Not Less or Equal?"
    a: "Yes. Bad RAM corrupts driver code and data at runtime, causing legal driver operations to fault. The signature of memory-caused IRQL crashes is inconsistency: different .sys files named across crashes, or crashes in Safe Mode where third-party drivers aren't loaded. Run Windows Memory Diagnostic before concluding it's a driver."
  - q: "Will updating the driver always fix it?"
    a: "Not always — sometimes the newest driver is the problem, especially if crashes started right after updating. In that case roll back instead. The reliable approach is: identify the named driver, try the latest vendor version with a clean install, and if that fails, step back to the previous version that was stable."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL (stop code 0x000000D1) is Windows catching a driver breaking a fundamental rule: it tried to touch pageable memory while running at an elevated IRQL — an interrupt level where only non-pageable memory is safe to access. The kernel stops the system rather than allow the corruption this could cause. Like most driver stop codes, the blue screen usually names the guilty `.sys` file, which turns a scary crash into a straightforward driver repair job.

Network drivers cause this more than any other category — Wi-Fi drivers in particular, because they constantly transition between power states as you roam, sleep, and wake the laptop. Storage and graphics drivers are next. The fix path is: identify the file, update or roll back that driver, and verify the hardware if the culprit keeps changing. For the quick-reference version of this same error, see our [IRQL fix summary](/articles/irql-not-less-or-equal-windows-11-fix/); for crashes where the kernel's own integrity check fires instead, see our [kernel security check failure guide](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/).

## Why this happens

- **Buggy network drivers**: Wi-Fi/Ethernet drivers mishandling power transitions — the single most common trigger.
- **Driver update regressions**: A new version introducing an IRQL bug the previous version didn't have.
- **Storage driver faults**: Disk controller drivers accessing paged memory at high IRQL during I/O.
- **Antivirus filter drivers**: Kernel-level security hooks executing at the wrong IRQL after updates.
- **Failing RAM**: Memory corruption making valid driver accesses fault unpredictably.
- **Overclocked system**: Unstable CPU/RAM clocks causing timing-sensitive driver code to fault.
- **Corrupt driver files**: Damaged .sys files from disk errors or partial installations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the named driver

The blue screen usually hands you the answer.

1. Photograph the blue screen, capturing the `.sys` filename shown with the stop code.
2. Map it: `Netwtw*.sys` = Intel Wi-Fi, `rtwlanu.sys`/`rtwlane.sys` = Realtek Wi-Fi, `e2f*.sys`/`e1d*.sys` = Intel Ethernet, `storahci.sys`/`iaStor*.sys` = storage, `nvlddmkm.sys` = NVIDIA graphics.
3. If no file is named, check **Event Viewer** > **Windows Logs** > **System** for the BugCheck entry, or analyze `C:\Windows\Minidump` with BlueScreenView.
4. If the named file differs across crashes, treat it as a hardware signal and prioritize Fix 6.

### Fix 2: Update the network driver cleanly

Since network drivers lead the statistics, start here when one is named — or even when none is.

1. Download the latest driver from the chip vendor or laptop manufacturer. For Intel wireless and Bluetooth, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the exact match.
2. In **Device Manager**, right-click the network adapter > **Uninstall device** (tick **Attempt to remove the driver** if offered), then install the downloaded driver fresh.
3. For Killer/Intel Wi-Fi cards, prefer the driver from your laptop manufacturer's support page — OEMs customize these drivers and generic versions cause exactly this crash.
4. Restart and test through sleep/wake cycles and network roaming — IRQL crashes love power transitions, so test those specifically.

### Fix 3: Roll back if an update triggered it

Timing is evidence — use it.

1. If crashes began after a driver update: **Device Manager** > device > **Properties** > **Driver** > **Roll Back Driver**.
2. If they began after a Windows update: **Settings** > **Windows Update** > **Update history** > **Uninstall updates** > remove the recent KB.
3. Check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known IRQL issues with that update before reinstalling it.
4. After rolling back, pause driver updates temporarily so Windows doesn't immediately reinstall the bad version.

### Fix 4: Address the other usual suspects

Graphics, storage, and security drivers get the same treatment.

1. Clean-install the GPU driver from the vendor (NVIDIA/AMD/Intel) using the clean-install option.
2. Update the chipset and storage controller drivers from your laptop manufacturer's support page.
3. Update third-party antivirus, or temporarily uninstall it with the vendor's removal tool to test — filter drivers at the wrong IRQL are a documented cause.
4. Change one driver at a time and test between changes; shotgun-updating destroys your ability to identify the fix.

### Fix 5: Boot into Safe Mode with Networking for testing

Isolate whether third-party drivers are even involved.

1. Boot into Safe Mode with Networking (recovery > **Startup Settings** > **Restart** > **5**).
2. If crashes stop in Safe Mode, a third-party driver is confirmed — the clean-boot procedure (`msconfig`, hide Microsoft services, disable all) finds which one.
3. If IRQL crashes happen in Safe Mode too, the fault is in a Microsoft driver, system files, or hardware — continue to Fixes 6 and 7.
4. Safe Mode with Networking still loads the network stack, so Wi-Fi-driver crashes can reproduce there — useful for confirming a network driver suspect.

### Fix 6: Test the RAM

Inconsistent culprits mean memory until proven otherwise.

1. Press **Windows + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. For conclusive results, run MemTest86 from USB overnight.
3. Reseat sticks and test one at a time if errors appear; replace the failing stick.
4. Reset XMP/DOCP profiles to stock in the BIOS — aggressive memory timings are a notorious source of IRQL crashes that look exactly like driver bugs.

### Fix 7: Repair system files and reset clocks

Close out the remaining causes.

1. Run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal.
2. Reset any CPU/GPU/RAM overclocks to stock in the BIOS and vendor utilities.
3. Update the BIOS from the laptop manufacturer's support page — BIOS updates fix interrupt-routing and power-delivery bugs that manifest as IRQL errors.
4. Retest for several days under normal use including sleep/wake cycles before declaring the issue resolved.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL looks arcane, but it's one of the most actionable blue screens: it usually names the driver, and the fix is updating or rolling back that driver. The discipline is in the order — identify first, change one thing at a time, and let inconsistent culprit files redirect you to RAM testing rather than deeper into driver-chasing. Keep a note of the working driver version once you find it; driver problems recur most often when Windows Update silently "upgrades" you back to the broken one. For the condensed reference on this stop code, our [IRQL quick-fix guide](/articles/irql-not-less-or-equal-windows-11-fix/) is worth bookmarking.
