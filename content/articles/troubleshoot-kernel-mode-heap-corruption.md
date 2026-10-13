---
title: "How to Troubleshoot Kernel Mode Heap Corruption"
slug: troubleshoot-kernel-mode-heap-corruption
date: 2026-09-27
categories: ["windows-errors"]
tags: ["kernel heap corruption", "bsod", "memory corruption", "windows 11"]
description: "Troubleshoot KERNEL_MODE_HEAP_CORRUPTION: identify the corrupting driver, verify RAM, and repair the system with this step-by-step process."
thumbnail: "/images/thumbs/troubleshoot-kernel-mode-heap-corruption.webp"
faqs:
  - q: "What is kernel mode heap corruption?"
    a: "The kernel's heap — its dynamic memory allocation area — has been corrupted by something writing where it shouldn't. Stop code 0x00000013A. Windows detects the damage during heap validation and stops to prevent further corruption. A buggy driver is the usual writer, but bad RAM produces identical symptoms by corrupting heap contents at the hardware level."
  - q: "How is heap corruption different from pool corruption?"
    a: "They're closely related — the pool is the kernel's older allocation mechanism and the heap is the newer one, and drivers can corrupt either. Practically, the troubleshooting is nearly identical: find the corrupting driver or test the RAM. Special pool (via Driver Verifier) catches both, which is why Verifier is central to diagnosing either."
  - q: "Can I fix heap corruption without Driver Verifier?"
    a: "Often yes — if the blue screen names a driver, updating or rolling back that driver resolves it without Verifier. Verifier becomes necessary when no driver is named or the culprit is ambiguous. It's a diagnostic amplifier, not a requirement; start with the named driver and escalate to Verifier only if needed."
  - q: "Does this error mean my RAM is definitely bad?"
    a: "No. Drivers cause most heap corruption; RAM is the second suspect. The discriminator is consistency: one driver implicated repeatedly points at that driver, while varying culprits or crashes in Safe Mode point at RAM. Run MemTest86 overnight when the pattern suggests hardware — don't replace RAM on a hunch."
---

KERNEL_MODE_HEAP_CORRUPTION (stop code 0x00000013A) means Windows found its kernel heap — the memory region where drivers and the kernel allocate dynamic structures — damaged. Something wrote where it shouldn't have, and heap validation caught it. Like pool corruption (its close cousin), the writer is usually a buggy driver; the complication is that bad RAM corrupts heap contents in ways that look exactly like a driver bug. So this troubleshooting has two lanes from the start: find the corrupting driver, or prove the hardware.

The diagnostic centerpiece is Driver Verifier with special pool enabled — it makes the corrupting driver crash immediately at the moment of corruption instead of later at validation time, producing a far more informative stop code. But Verifier is the escalation, not the opening move: if the blue screen names a driver, you start there. For pool-type corruption specifically, see our [special pool corruption guide](/articles/how-to-fix-special-pool-detected-memory-corruption-on-windows-10/); for the memory-management sibling, see our [Memory Management guide](/articles/memory-management-bsod-windows-11-fix/).

## Why this happens

- **Buggy drivers writing out of bounds**: Heap buffer overflows in kernel drivers — the primary cause.
- **Use-after-free bugs**: Drivers accessing heap memory after freeing it, corrupting reused allocations.
- **Failing RAM**: Hardware-level corruption of heap contents indistinguishable from driver bugs.
- **Driver update regressions**: New versions introducing heap bugs.
- **Corrupt driver binaries**: Damaged .sys files misbehaving.
- **Antivirus filter drivers**: Kernel security hooks with heap-handling bugs.
- **Overclocked memory**: Unstable RAM timings corrupting heap data under load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the named driver and crash pattern

Classify before acting.

1. Photograph the blue screen — note any `.sys` filename with the stop code.
2. **Event Viewer** > **Windows Logs** > **System** > **BugCheck** entries: tabulate recent crashes and their named files.
3. Consistent file → driver lane (Fix 2). Varying files or Safe Mode crashes → hardware lane (Fix 5).
4. Note onset timing — update, new driver, new hardware — and check [Microsoft's support docs](https://support.microsoft.com/en-us/windows) for the stop code's parameter meanings if you're analyzing deeply.

### Fix 2: Replace the implicated driver

Direct action on a named culprit.

1. Download the latest driver from the manufacturer. For Intel components, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies the right package.
2. **Device Manager** > uninstall the device (with driver removal) > clean-install the downloaded driver.
3. If crashes began after a driver update, **Roll Back Driver** instead.
4. Test 48 hours under the original trigger conditions — heap corruption is often workload-specific.

### Fix 3: Deploy Driver Verifier with special pool

Catch the corrupter in the act.

1. **Windows + R** > `verifier.exe` > **Create custom settings** > enable **Special pool**, **Pool tracking**, and **Force IRQL checking**.
2. **Select driver names from a list** — tick only non-Microsoft drivers related to the crash context (graphics, network, storage, USB).
3. Restart and use the PC normally. Verifier forces an immediate, well-identified crash (typically DRIVER_VERIFIER_DETECTED_VIOLATION or a special-pool stop) at the corruption moment, naming the driver.
4. **Mandatory**: `verifier /reset` and restart after identification or 48 hours. Verifier is a diagnostic instrument, not a permanent setting.

### Fix 4: Sweep adjacent drivers and software

Broaden the driver net when Verifier is inconclusive.

1. Clean-install GPU drivers (vendor installer, clean-install option), update chipset/network/storage drivers from the laptop vendor.
2. Remove third-party antivirus with the vendor's removal tool and test — filter drivers corrupt heaps.
3. Clean-boot (`msconfig`, hide Microsoft services, disable all) and bisect to find software culprits.
4. One change per test cycle; log everything.

### Fix 5: Test the RAM definitively

The hardware lane for inconsistent culprits.

1. `mdsched.exe` → restart and check (quick screen).
2. MemTest86 overnight, 4+ passes, zero errors — the definitive verdict.
3. Reseat, isolate sticks individually, replace failures.
4. Disable XMP/DOCP in the BIOS and retest — memory overclock instability is a prime heap-corruption source on performance laptops.

### Fix 6: Repair system files and check storage

Rule out OS and disk-level corruption.

1. Elevated: `sfc /scannow` → `DISM /Online /Cleanup-Image /RestoreHealth` → SFC again.
2. `chkdsk C: /f /r` (schedule at restart) — bad sectors corrupt driver binaries and heap-adjacent structures.
3. **Microsoft Defender Offline scan** to rule out malware hooking heap functions.
4. Recurring corruption after clean repairs → drive diagnostics (**F12** > **Diagnostics** on Dell, **F2** on HP).

### Fix 7: Stabilize firmware and clocks

Remove the platform variables.

1. Update the BIOS from the laptop manufacturer's support page.
2. Update the chipset driver to match.
3. Reset all CPU/GPU/RAM overclocks to stock.
4. Extended stress test under the original crashing workload before declaring victory — heap bugs hide until the specific allocation pattern recurs.

## Closing

Kernel heap corruption troubleshooting is a two-lane road: the driver lane (named file → replace driver → Verifier for confirmation) and the hardware lane (varying files → MemTest86 → stabilize clocks). The mistake is committing to one lane without checking which the evidence points to — replacing RAM for a consistent driver bug, or reinstalling drivers for failing memory. Read the crash pattern first, and the rest of the walkthrough is just execution. Driver Verifier with special pool is the tool that turns "something corrupted the heap" into a named culprit; MemTest86 is the tool that exonerates or convicts the RAM. Between them, this stop code always yields an answer. For the pool-allocation sibling, our [special pool guide](/articles/how-to-fix-special-pool-detected-memory-corruption-on-windows-10/) runs the parallel process. A final note on prevention: heap corruption is overwhelmingly a driver-quality problem, which means your best long-term defense is driver hygiene — prefer vendor drivers over generic ones, avoid installing three overlapping "driver updater" utilities that fight over the same devices, and be skeptical of brand-new driver releases on day one, letting the early adopters find the heap bugs first. If you're a developer or power user who runs Driver Verifier regularly, remember it's a diagnostic instrument with real overhead: schedule Verifier sessions deliberately, capture the resulting dumps, and always reset it afterward. And keep a simple log — date, stop code, named driver, what you changed — because heap corruption has a long memory: the driver that corrupted the heap this year is the first suspect when a neighboring stop code appears next year, and your own notes are the fastest diagnostic database you'll ever own.
