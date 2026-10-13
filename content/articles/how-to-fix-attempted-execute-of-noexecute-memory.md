---
title: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: Fix This Blue Screen"
slug: how-to-fix-attempted-execute-of-noexecute-memory
date: 2026-10-08
categories: ["windows-errors"]
tags: ["blue screen", "memory", "windows 11"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY means something tried to run code from protected memory. Find the culprit driver and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "Stop code 0x000000FC: a driver or program tried to execute code from a memory region marked non-executable (DEP protection). It's a security mechanism firing — usually because of a buggy driver, corrupted memory, or occasionally malware."
  - q: "Is this error caused by a virus?"
    a: "It can be — malware that injects code into protected memory trips this exact check. But buggy drivers and bad RAM are more common causes. Run a full Windows Security scan early to rule malware out."
  - q: "What is DEP and should I turn it off?"
    a: "DEP (Data Execution Prevention) marks memory regions as non-executable to block exploits. Don't disable it system-wide — it's protecting you. The fix is finding what's violating DEP, not removing the protection."
  - q: "Can bad RAM cause this blue screen?"
    a: "Yes. Corrupted memory can make valid code look like it's in a non-executable region, or corrupt the page tables that track execution permissions. Test your RAM if no driver is ever named in the crashes."
---
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (stop code 0x000000FC) is Windows' Data Execution Prevention catching something trying to run code where code isn't allowed to run. Think of it as a security guard stopping someone climbing over the fence — the guard isn't the problem; whoever's climbing is. Usually that's a buggy driver, sometimes bad RAM, occasionally malware.

Don't disable DEP to "fix" this — that's firing the guard. Instead, find the climber. Work through these in order. For other memory-related stop codes, our [PAGE_FAULT_IN_NONPAGED_AREA guide](/articles/page-fault-in-nonpaged-area-blue-screen-error-fix/) covers the sibling diagnosis.

## Why this happens

- **Buggy device driver.** Drivers executing from wrong memory regions are the top cause.
- **Corrupted RAM.** Bad memory corrupts execution-permission tracking.
- **Malware.** Code-injection techniques trip DEP constantly.
- **Corrupted system files.** Damage to kernel memory-management components.
- **Incompatible old drivers.** Legacy drivers that predate DEP enforcement.
- **Overclocked/unstable memory.** Timing errors corrupt page tables.
- **Disk corruption.** Damaged driver binaries execute unpredictably.

## How to fix it

Work through these in order — note any named driver on the blue screen.

### Fix 1: Run a full malware scan

Rule out the malicious cause first since DEP violations are a malware hallmark.

1. Boot into Safe Mode with Networking (interrupt boot 2-3 times for WinRE, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **5**).
2. Open **Settings > Privacy & security > Windows Security > Virus & threat protection**.
3. Choose **Scan options > Full scan** and run it.
4. Also run **Microsoft Defender Offline scan** from the same page — it reboots into a clean environment that catches rootkits.
5. Remove anything found and restart normally.
6. If the system is clean, continue — the cause is a driver or hardware.

### Fix 2: Identify the offending driver

Check whether the blue screen named a culprit.

1. Note any `.sys` file on the blue screen.
2. In Windows, open **Event Viewer > Windows Logs > System** and find **BugCheck** entries for stop code 0xFC.
3. Check `C:\Windows\Minidump` for dump files from the crashes.
4. If a driver is named, skip to Fix 3 with that target.
5. If no driver is ever named, lean toward RAM testing (Fix 5) — hardware causes don't name drivers.
6. Our [driver IRQL guide](/articles/how-to-fix-driver-irql-not-less-or-equal-youtube/) explains dump-reading basics that apply here too.

### Fix 3: Update or roll back the suspect driver

Fix the violating driver directly.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Find the device matching the named driver.
3. If crashes started after a driver update, use **Properties > Driver > Roll Back Driver**.
4. Otherwise, **Update driver > Search automatically for drivers**.
5. For the most reliable result, download from the manufacturer's official site — [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or your laptop maker's support page.
6. Restart and test the scenarios that previously crashed.

### Fix 4: Use Driver Verifier to catch it (advanced)

If no driver is named, force the culprit to reveal itself.

1. Press **Win + R**, type `verifier.exe`, and press **Enter**.
2. Choose **Create standard settings**, then **Select driver names from a list**.
3. Tick only third-party drivers (sort by provider — select non-Microsoft ones you suspect).
4. Click **Finish** and restart. Use the system normally — open the apps and devices you use daily, since Verifier only catches the driver when it's actually exercised.
5. Verifier will crash the system faster when the buggy driver misbehaves — and this time it usually names it. Note the driver name from the new blue screen or the subsequent BugCheck event in Event Viewer.
6. After identifying the driver, boot to Safe Mode, run `verifier /reset`, restart, and fix the driver per Fix 3. Never leave Verifier on indefinitely — it's a diagnostic instrument, and a Verifier left running will eventually crash even healthy drivers under enough stress.

### Fix 5: Test the RAM

Bad memory corrupts the execution-permission data.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
4. For a definitive answer, run MemTest86 from a bootable USB overnight.
5. Replace faulty modules with the correct specification.
6. If RAM tests clean, continue to system-file repair.

### Fix 6: Repair system files and check the disk

Fix corruption in Windows' own memory management.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Then:
   `sfc /scannow`
4. Restart.
5. Also run `chkdsk C: /f` — disk corruption damages driver binaries, which then execute unpredictably.
6. Microsoft documents these repairs on [support.microsoft.com](https://support.microsoft.com/en-us/windows).

### Fix 7: Reset memory settings and update firmware

Cover the remaining hardware angles.

1. Enter BIOS/UEFI and load optimized defaults.
2. Disable XMP/DOCP profiles — unstable memory timings corrupt page tables.
3. Check for a BIOS update from your laptop maker's support site and install it (charger connected).
4. After updating, retest for several days including the original crash scenarios.
5. If 0xFC persists with clean RAM, current drivers, repaired system files, and stock memory settings, the motherboard's memory controller may be failing.
6. Back up your data and arrange service — bring your documented test results (MemTest86 logs, dump notes) to speed up diagnosis.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is DEP doing its job, so work with it, not against it: scan for malware, identify the violating driver, test the RAM. The temptation to disable DEP is understandable but wrong — it trades a diagnosable crash for silent vulnerability. Find the climber, fix the fence-jumping, and the guard goes back to quietly doing its job. Keep a note of which driver was at fault and the version that fixed it; if a future update reintroduces the crash, you'll recognize the pattern instantly instead of starting from zero. Keep a note of which driver was at fault and the version that fixed it; if a future update reintroduces the crash, you'll recognize the pattern instantly instead of starting from zero.
