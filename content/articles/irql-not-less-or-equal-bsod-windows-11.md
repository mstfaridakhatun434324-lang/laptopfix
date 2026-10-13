---
title: "IRQL_NOT_LESS_OR_EQUAL Blue Screen on Windows 11: How to Fix It"
slug: irql-not-less-or-equal-bsod-windows-11
date: 2026-10-10
categories: ["windows-errors"]
tags: ["irql not less or equal", "bsod", "driver", "0xa", "windows 11"]
description: "IRQL_NOT_LESS_OR_EQUAL (0xA) means a driver touched memory it shouldn't have. Here's how to fix it — identify the driver, update it, and test your RAM."
thumbnail: "/images/thumbs/irql-not-less-or-equal-bsod-windows-11.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "Stop code 0xA means a kernel-mode driver tried to access memory at an invalid address, or touched paged memory while running at too high an interrupt level (IRQL). In plain terms: a driver broke the rules about what memory it can touch and when. It's one of the most common blue screens on Windows 11, and the overwhelming majority of cases are fixed with a driver update — the dump usually names the offender."
  - q: "Which drivers most often cause this blue screen?"
    a: "Network drivers (Wi-Fi and Ethernet) are the most frequent offenders, followed by graphics drivers, storage controller drivers, and antivirus filter drivers. The pattern helps: crashes during downloads or video calls implicate network drivers; crashes in games implicate GPU drivers; crashes during file operations implicate storage or filter drivers. The crash dump's IMAGE_NAME field usually confirms the suspect directly."
  - q: "Can bad RAM cause IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes, though drivers are more common. Faulty RAM corrupts the addresses drivers work with, producing 0xA crashes that name innocent drivers — typically with a different driver named each time. If your dumps name a rotating cast of drivers, or explicitly show memory_corruption, test your RAM with MemTest86 before continuing to chase driver updates."
  - q: "Why does it happen right after a Windows update?"
    a: "Windows Update delivers driver updates alongside OS patches, and a new driver version with a bug can start 0xA crashes immediately. Check Update history for driver updates dated just before the crashes began and roll them back as a test. This is also why installing drivers from your laptop manufacturer's support page — tested against your exact model — beats generic Windows Update drivers for stability."
---

IRQL_NOT_LESS_OR_EQUAL — stop code 0xA — is the blue screen of driver misbehavior. The name describes the exact rule that was broken: a driver tried to access memory at an interrupt request level (IRQL) where that access isn't allowed, or simply touched an address that doesn't exist. Windows enforces these rules strictly because violating them corrupts the kernel — so instead of limping on, it crashes immediately and tells you about it.

This is one of the most common stop codes in Windows 11, and also one of the most fixable. The crash dump almost always names the offending driver file, which turns the investigation from a mystery into a to-do item: update that driver, roll it back, or remove its software. Work the steps below in order — identify, update, verify — and reserve the hardware testing for the cases where the dumps refuse to name a consistent culprit.

## Why this happens

- **Buggy network driver**: Wi-Fi and Ethernet drivers are the number one cause — they handle constant interrupt-driven I/O where IRQL rules are strictest.
- **Outdated graphics driver**: GPU drivers managing memory-mapped I/O can violate IRQL rules when buggy.
- **Bad driver delivered via Windows Update**: A new-but-buggy driver version starts crashes the day it installs.
- **Antivirus filter drivers**: Kernel security filters operating at elevated IRQL are frequent offenders when buggy.
- **Corrupt driver installation**: Damaged driver files from failed updates or disk errors misbehave unpredictably.
- **Faulty RAM**: Bad memory corrupts addresses, producing 0xA crashes naming random innocent drivers.
- **Overclocking instability**: Unstable CPU/memory clocks corrupt kernel data structures, manifesting as driver-blaming stop codes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the driver from the crash dump

The dump usually hands you the answer — collect it first.

1. Open the latest minidump in BlueScreenView (fast) or WinDbg Preview (thorough) and note the **IMAGE_NAME** / faulting module.
2. Identify the owner: `Netwtw10.sys`/`Netwtw12.sys` = Intel Wi-Fi, `rtwlanu.sys` = Realtek, `nvlddmkm.sys` = NVIDIA, `atikmdag.sys` = AMD graphics. A quick web search of the filename confirms any you're unsure about.
3. Check 2–3 dumps for consistency: same driver every time means driver bug (proceed to Fix 2); different drivers each time means suspect RAM (skip to Fix 6 after Fix 2's quick checks).
4. Our [WinDbg walkthrough](/articles/how-to-read-dump-files-with-windbg-in-windows-11-24h2/) covers dump analysis step by step if this is new to you.

### Fix 2: Update the identified driver from the manufacturer

Precision fix — the right driver, from the right source.

1. Download the latest driver for your exact laptop model from the manufacturer's support page — Dell, HP, Lenovo. For Intel Wi-Fi specifically, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is authoritative.
2. For a clean update: **Device Manager** > right-click the device > **Uninstall device** (tick "delete driver software" if offered) > reboot > install the fresh download.
3. For GPU drivers: use DDU in Safe Mode for full removal, then install fresh from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or Intel.
4. Test with the activity that previously crashed (the download, the game, the video call) — not just idle desktop time.

### Fix 3: Roll back the driver update that started it

If crashes began right after a driver update, the update is guilty until proven innocent.

1. **Device Manager** > the device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. Also check **Settings** > **Windows Update** > **Update history** > **Uninstall updates** for driver updates with matching dates.
3. After rolling back, consider pausing driver updates via Windows Update for that device: in **Device Manager**, the rolled-back version holds until you manually update.
4. Report the bad driver version to the vendor with your minidump attached — regressions get fixed when they're reported with evidence.

### Fix 4: Remove or update antivirus and filter software

Kernel filters are frequent 0xA offenders.

1. Uninstall third-party antivirus completely — not just disabled — and test for several days. Windows Defender provides protection meanwhile.
2. Also remove VPN clients, firewall suites, and "network optimizer" tools temporarily — they all install network filter drivers.
3. If crashes stop, reinstall your security software fresh (latest version) or switch to a different product, then verify stability again.
4. Never stack multiple antivirus products — their competing filters are a crash factory.

### Fix 5: Repair system files and check for bad updates

Rule out OS-level damage and update regressions.

1. Admin terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. If crashes started with a Windows quality update (not a driver update), uninstall it as a test and check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known issues.
3. Keep Windows itself current otherwise — cumulative updates do fix 0xA-class bugs on occasion, and running months behind is its own risk.
4. If SFC finds unfixable corruption, an in-place upgrade repair install is the next step, not repeated scans.

### Fix 6: Test RAM when dumps name rotating culprits

Hardware verification for the inconsistent-dump pattern.

1. Disable XMP/DOCP in BIOS first — test at stock JEDEC speeds so results are valid.
2. Run MemTest86 from USB, 4+ passes overnight. Any error fails the stick; isolate per-stick/per-slot with two sticks.
3. Also run Windows Memory Diagnostic (`mdsched.exe`) as a quick screen, but trust MemTest86's verdict.
4. Replace only confirmed-bad sticks with spec-matched RAM and re-verify. For the full memory-testing discipline, our [memory management guide](/articles/memory-management-bsod-windows-11-fix/) is the companion read.

### Fix 7: Reset overclocks and update BIOS

Eliminate tuning and firmware as contributors.

1. Load BIOS optimized defaults — clearing CPU overclocks, undervolts, XMP, and multi-core enhancement.
2. Reset XTU/ThrottleStop/Ryzen Master profiles to stock.
3. Update the BIOS from your manufacturer's support page if yours is outdated — firmware updates fix interrupt-handling and power bugs that surface as 0xA.
4. Retest the crashing scenarios at pure stock. Stability here means tuning or firmware was the cause — re-tune only with proper stress validation.

### Fix 8: Clean-boot isolation for the unnamed culprit

The final sweep when no driver will confess.

1. `msconfig` > hide Microsoft services > disable all; Task Manager > disable non-Microsoft startup apps; restart.
2. Reproduce the crashing activity. If stable, re-enable in halves until crashes return — binary search finds the offender in a few reboots.
3. Update, replace, or permanently remove the culprit. For driver-specific deep dives, our [IRQL-focused guide](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/) covers additional scenarios.
4. If even the clean boot crashes with passing RAM, current BIOS, and stock clocks, you're in rare territory — motherboard-level faults need professional diagnosis with your full test log.

## Closing

IRQL_NOT_LESS_OR_EQUAL is the most approachable of the scary-sounding stop codes: it names the rule broken, the dump usually names the breaker, and the fix is usually a single driver update away. Read the dump first, update precisely from manufacturer sources, and let dump consistency decide whether you're chasing software or testing hardware. Same driver every time means update it; a rotating cast means test the RAM. That one observation, made in the first five minutes, determines the entire shape of the fix — and it's the difference between a quick driver update and a week of frustration.
