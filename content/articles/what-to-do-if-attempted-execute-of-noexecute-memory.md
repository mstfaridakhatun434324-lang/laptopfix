---
title: "What to Do When ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY Appears"
slug: what-to-do-if-attempted-execute-of-noexecute-memory
date: 2026-09-12
categories: ["windows-errors"]
tags: ["blue screen", "noexecute memory", "dep", "bsod fix"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen? Understand what it means and fix the driver or memory issue behind it, step by step."
thumbnail: "/images/thumbs/what-to-do-if-attempted-execute-of-noexecute-memory.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "Windows marked a region of memory as non-executable (via Data Execution Prevention), and something tried to run code from it anyway. That's either a driver bug — jumping to a bad address that lands in a no-execute region — or actual malicious code attempting to execute. Stop code 0xFC. On a normal home laptop it's a driver or RAM issue far more often than malware, but the security angle is why you shouldn't ignore it."
  - q: "Is this error a virus?"
    a: "Unlikely, but it's the one blue screen where you should actually consider it. DEP exists to stop exactly this kind of execution, and malware is one thing that tries it. Run a full Windows Security scan (or an offline scan from **Windows Security > Virus & threat protection > Scan options > Microsoft Defender Offline scan**) to rule it out, then pursue the driver and RAM fixes — which are the cause in the vast majority of cases."
  - q: "Can bad RAM cause this error?"
    a: "Yes. Corrupted memory can turn a valid code pointer into garbage that points into a no-execute region, making a perfectly good driver look like it's attempting forbidden execution. If dumps implicate different drivers on different crashes, test the RAM — that's the classic pattern of memory corruption rather than a single buggy driver."
  - q: "Should I disable DEP to stop the crashes?"
    a: "No. Disabling DEP removes a critical security protection and only masks the symptom — the underlying driver bug or memory corruption is still there, now free to execute. Fix the actual cause instead. DEP should stay on; it's doing its job by crashing instead of letting bad code run."
---

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (stop code 0xFC) is Windows' Data Execution Prevention doing exactly what it was built to do: a piece of code tried to run from a memory region marked "data only, do not execute," and Windows stopped the system rather than let it proceed. It's a security boundary doing its job — which means something crossed it, and you need to find out what.

In practice, on a regular laptop, the crosser is usually a buggy driver or faulty RAM rather than malware. But because this specific error sits at the security boundary, the guide starts by ruling out the scary stuff, then moves to the likely stuff.

## Why this happens

- **Buggy driver jumping to a bad address.** A driver computing a wrong function pointer and landing in a no-execute page.
- **Faulty RAM corrupting pointers.** Bit flips turning valid code addresses into garbage that lands in protected regions.
- **Malware attempting code execution.** The scenario DEP was designed to stop — rare on protected systems, but real.
- **Corrupted driver or system binaries.** Damaged code that jumps somewhere its source never intended.
- **Overclocked/unstable memory.** Instability corrupting pointers under load.
- **Antivirus or security driver conflicts.** Low-level security products manipulating execution paths.
- **Failing storage corrupting executables.** Disk errors damaging driver binaries on load.
- **BIOS security features conflicting.** Memory integrity (HVCI) and older drivers fighting over execution permissions can produce this fault on some systems.
- **Corrupted hibernation image.** A damaged hiberfil.sys resuming garbage into executable regions — disabling and re-enabling hibernation rebuilds it.

## How to fix it

Work through these in order — security check first, then drivers, then hardware.

### Fix 1: Rule out malware with an offline scan

Take the security angle seriously once, then move on. An offline scan runs outside the installed OS, so it catches things a normal scan might miss.

1. Open **Windows Security > Virus & threat protection > Scan options**.
2. Choose **Microsoft Defender Offline scan** and click **Scan now**. The laptop restarts into a clean environment outside the running OS.
3. Let it complete and review the results. If it finds and removes threats, monitor for a few days — the crashes may have been the infection.
4. If clean, proceed: on a protected, updated system, drivers and RAM are the real story.

### Fix 2: Identify the faulting driver from the dump

Get the name before changing anything. Guessing wastes time and risks breaking a working driver.

1. Verify minidumps are on: **Advanced system settings > Startup and Recovery > Settings > Small memory dump**.
2. After the next crash, open `%SystemRoot%\Minidump` in WinDbg Preview and run `!analyze -v`.
3. Note **MODULE_NAME** — the driver that attempted the forbidden execution.
4. If dumps name different drivers each time, skip to Fix 6 (RAM) — rotating suspects means memory corruption, not a driver bug.

### Fix 3: Update or roll back the named driver

Fix the specific driver the dump identified.

1. In **Device Manager**, locate the device and try **Update driver > Search automatically for drivers**.
2. Better: get the latest version from the manufacturer — [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or your laptop maker's support site.
3. If crashes began with a driver update, roll back instead: **Properties > Driver > Roll Back Driver**.
4. Restart and test under the conditions that used to crash.

### Fix 4: Update security software and remove conflicts

Security drivers operate exactly at this boundary.

1. Fully update your antivirus engine.
2. Remove duplicate security products — two antivirus engines' drivers interfering at the execution boundary is a known trigger.
3. Use each vendor's removal tool for clean uninstalls, then test on Windows Security alone for several days.

### Fix 5: Repair system and driver files

Eliminate corrupted binaries as the cause.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. Corrupted driver binaries jump to wrong addresses — clean files rule that out.

### Fix 6: Test the RAM thoroughly

Memory corruption is the great impersonator for this stop code.

1. Run `mdsched.exe`, choose **Restart now and check for problems**, press **F1**, and run **Extended** with 2+ passes.
2. For certainty, run MemTest86 overnight.
3. Also disable **XMP/EXPO** in the BIOS during testing — unstable memory profiles corrupt pointers under load.
4. Replace any failing stick. No driver update fixes hardware that flips bits.

### Fix 7: Check the disk

Corrupted executables load corrupted code.

1. Run `chkdsk C: /f /r` in an elevated prompt; let it complete at boot.
2. Check SSD health with the manufacturer's utility.
3. If CHKDSK repeatedly finds new corruption, the drive is suspect — and a drive that corrupts binaries will keep producing impossible crashes.

### Fix 8: Keep DEP on and verify stability

Confirm the fix without weakening security.

1. Verify DEP is enabled: **Advanced system settings > Performance Settings > Data Execution Prevention** — it should be on for essential programs and services (the default).
2. Leave it there. Never disable DEP to "fix" this error.
3. Monitor for a week. For deeper reading on DEP and exploit protection, see [Microsoft's Windows security documentation](https://support.microsoft.com/en-us/windows).

For update-triggered cases, see our [attempted execute after Windows 11 update](/articles/how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update/) guide and the [24H2 variant](/articles/how-to-fix-attempted-execute-of-noexecute-memory-in-windows-11-24h2/). The Dell-specific walkthrough at [attempted execute on Dell](/articles/how-to-fix-attempted-execute-of-noexecute-memory-on-dell-laptop/) covers brand quirks.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is DEP catching something red-handed at the security boundary. Rule out malware once with an offline scan, then treat it like the driver-or-RAM problem it almost always is: read the dump, fix the driver, test the memory — and leave DEP switched on, doing its job. And resist every forum post telling you to disable DEP or memory integrity — those protections are the reason this crash exists instead of a silent compromise.
