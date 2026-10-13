---
title: "BAD_POOL_HEADER BSOD: Step-by-Step Repair"
slug: how-to-fix-bad-pool-header-step-by-step
date: 2026-09-05
categories: ["windows-errors"]
tags: ["bad pool header", "bsod", "stop code 0x19", "windows 11"]
description: "BAD_POOL_HEADER (0x19) means a driver corrupted Windows' memory pool. Repair it step by step with this guide."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-step-by-step.webp"
faqs:
  - q: "What does BAD_POOL_HEADER mean?"
    a: "Windows organizes kernel memory into 'pools,' each allocation tagged with a header. BAD_POOL_HEADER (stop code 0x00000019) means a driver wrote past its allocation and damaged a neighboring header, or freed memory incorrectly. The memory manager detects the damaged header and stops the system to prevent further corruption."
  - q: "Which driver causes BAD_POOL_HEADER?"
    a: "Any kernel driver can, but antivirus filter drivers, network drivers, and storage drivers are the most frequent offenders because they allocate heavily from the pools. The minidump sometimes names the driver; when it doesn't, Driver Verifier with pool tracking enabled catches the corrupting driver in the act."
  - q: "Can bad RAM cause BAD_POOL_HEADER?"
    a: "Yes. Faulty memory cells corrupt pool headers exactly like a buggy driver would, and Windows cannot distinguish the two from the stop code alone. Always run the Windows Memory Diagnostic for 0x19 — if RAM passes, pursue drivers; if it fails, replace the memory before doing anything else."
  - q: "Does BAD_POOL_HEADER mean I need to reinstall Windows?"
    a: "Rarely. This is a driver or memory problem, not a Windows installation problem, and the steps below resolve it in the vast majority of cases. Reinstall Windows only after RAM passes extended testing, Driver Verifier finds nothing, and SFC/DISM repairs don't help — that combination is uncommon."
---

**BAD_POOL_HEADER** (stop code **0x00000019**) is the memory manager catching a driver red-handed — or rather, catching the damage after the fact. Windows kernel memory is organized into pools, and every allocation carries a header tag. When a driver overflows its buffer, frees memory twice, or writes where it shouldn't, it damages a neighboring header. The next time the memory manager inspects that header, it finds garbage and halts the system.

Like its cousin KERNEL_MODE_HEAP_CORRUPTION, the corruption is usually **detected after it happened**, so the minidump doesn't always name the true culprit. The step-by-step order below accounts for that: test RAM first (hardware can't be fixed with drivers), isolate with Safe Mode, then use Driver Verifier's pool tracking to catch the offender live. For the related pool stop codes, see [memory management in 24H2](/articles/how-to-fix-stop-code-memory-management-in-windows-11-24h2/) and [DRIVER_IRQL_NOT_LESS_OR_EQUAL fixes](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/). A note on priority: because pool corruption is so often caused by filter drivers, the antivirus-removal step below deserves your attention even if you would rather skip it — temporarily uninstalling security software feels drastic, but it is reversible, safe with Defender active, and it resolves more 0x19 cases than any driver update. Test honestly, then move on.

## Why this happens

- **Buggy drivers corrupting pool memory**: Buffer overflows and double-frees in kernel drivers — antivirus filters, network, and storage drivers lead.
- **Faulty RAM**: Bad cells corrupting pool headers indistinguishably from driver bugs.
- **Corrupt driver installations**: Mixed or partial driver files after failed updates.
- **Third-party antivirus and security suites**: Heavy pool users with a long history of 0x19 bugs.
- **Corrupt system files**: Damaged memory-manager components.
- **Overclocked memory**: Unstable timings corrupting pool allocations under load.
- **Failing storage**: Disk faults corrupting paged pool data.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test RAM with Windows Memory Diagnostic

Hardware first — no driver fix survives bad memory.

1. Press **Win + R**, type `mdsched.exe`, press Enter.
2. Choose **Restart now and check for problems** and let the test finish.
3. Errors = faulty RAM. Reseat removable modules, retest, replace if errors persist.
4. For intermittent crashes with passing quick tests, run MemTest86 overnight — pool corruption from marginal RAM is notoriously intermittent.

### Fix 2: Isolate with Safe Mode

Determine whether a third-party driver is involved.

1. Hold **Shift** > **Restart** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
2. Use Safe Mode for a session. Stable = third-party driver or startup software; continue to Steps 3–4.
3. Crashes in Safe Mode = hardware, core files, or Microsoft drivers; prioritize Steps 5–6.
4. Record the result — it focuses the rest of your effort.

### Fix 3: Remove or update antivirus and filter drivers

The single most common software cause of 0x19.

1. **Uninstall** (not just disable) your third-party antivirus completely via **Settings** > **Apps** > **Installed apps**.
2. Restart — Windows Defender takes over automatically.
3. Test for a few days of normal use. If crashes stop, the antivirus filter driver was corrupting the pool.
4. Reinstall the latest version of the antivirus or switch products. Also review VPN clients and disk tools — they install similar filter drivers.

### Fix 4: Run Driver Verifier with pool tracking

Catch the corrupting driver at the moment of corruption.

1. **Win + R** > `verifier` > Enter. Choose **Create custom settings**.
2. Enable **Special pool**, **Pool tracking**, and **Force IRQL checking**.
3. Choose **Select driver names from a list** and check third-party drivers only.
4. Restart and use the laptop normally. Verifier will crash the system immediately when a driver corrupts the pool, naming it. Then Safe Mode > `verifier /reset` > replace that driver with the manufacturer's build. If Verifier names a driver you do not recognize, search its filename before replacing it — some are Windows components with odd names, and removing the wrong one wastes an afternoon. Get the replacement build from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/), or the chip maker.

### Fix 5: Update network and storage drivers

The heaviest pool users after antivirus.

1. In **Device Manager**, update drivers under **Network adapters** and **Storage controllers** (**Update driver** > **Search automatically**).
2. For Intel networking, use Intel's Driver & Support Assistant.
3. If a specific driver update preceded the crashes, roll it back (**Properties** > **Driver** > **Roll Back Driver**).
4. Restart and test, particularly sleep/wake cycles — network drivers corrupt pools most often during power transitions.

### Fix 6: Repair system files and reset memory clocks

Cover file corruption and unstable RAM timings.

1. **Terminal (Admin)**: run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Enter **BIOS/UEFI** and **Load Optimized Defaults** to clear XMP profiles and memory overclocks.
3. Run `chkdsk C: /f` and restart for the disk scan.
4. Retest under load. If SFC repaired files or stock clocks stabilized things, you've found it.

### Fix 7: Clean-boot to find the remaining culprit

For crashes surviving all driver-focused steps.

1. **Win + R** > `msconfig` > **Services** tab > **Hide all Microsoft services** > **Disable all**.
2. **Task Manager** > **Startup apps** > disable all. Restart.
3. Re-enable in halves until the crash returns, then uninstall the offending program.
4. As a final check, install all pending Windows updates — Microsoft ships pool-manager and driver fixes in cumulative updates; check Microsoft's support site for known issues with your build.

## Closing

BAD_POOL_HEADER is a "who damaged the header" investigation, and the steps above run it properly: RAM test, Safe Mode split, antivirus removal, Verifier with pool tracking, driver updates, file repair. The antivirus step alone resolves a striking number of cases — filter drivers and pool headers have a long, troubled history together. If every step passes and crashes continue at stock settings, extended MemTest86 and a motherboard evaluation are the remaining moves. Keep a note of which driver was at fault — pool corruption has a habit of returning with the next bad driver update from the same vendor.
