---
title: "How to Fix KERNEL_MODE_HEAP_CORRUPTION on Windows 11"
slug: how-to-fix-kernel-mode-heap-corruption
date: 2026-09-05
categories: ["windows-errors"]
tags: ["kernel mode heap corruption", "bsod", "heap corruption", "driver verifier", "stop code 0x13a"]
description: "KERNEL_MODE_HEAP_CORRUPTION blue screen on Windows 11? Learn what stop code 0x13A means and fix the corrupt driver behind it with 7 steps."
thumbnail: "/images/thumbs/how-to-fix-kernel-mode-heap-corruption.webp"
faqs:
  - q: "What does KERNEL_MODE_HEAP_CORRUPTION mean?"
    a: "Stop code 0x13A means Windows detected corruption in the kernel heap — the memory pool where drivers allocate their working storage. A driver wrote outside its allocation, freed the same memory twice, or used memory after freeing it. Windows catches the damage during a heap integrity check and crashes to prevent worse corruption."
  - q: "Which driver causes KERNEL_MODE_HEAP_CORRUPTION?"
    a: "Any kernel driver can corrupt the heap, but graphics drivers, network drivers, and antivirus filter drivers are the usual suspects. The blue screen rarely names the culprit directly, so Driver Verifier — which crashes the offending driver at the moment of corruption — is the definitive diagnostic tool."
  - q: "Is Driver Verifier safe to use?"
    a: "Mostly yes, with a caveat: Driver Verifier intentionally stresses drivers and will blue-screen the system when it catches a violation — that is its job. Always create a restore point first, verify only third-party drivers (never all drivers at once), and know how to boot into Safe Mode to turn it off."
  - q: "Can bad RAM cause KERNEL_MODE_HEAP_CORRUPTION?"
    a: "Yes. Faulty RAM corrupts heap contents just as effectively as a buggy driver. If Driver Verifier finds no guilty driver, or different drivers are blamed on different crashes, test your memory with mdsched.exe and MemTest86 before replacing drivers at random."
---

KERNEL_MODE_HEAP_CORRUPTION — stop code 0x13A — is Windows catching a driver red-handed in the kernel's memory pool. Drivers allocate "heap" memory for their work, and they're expected to stay inside their allocations, free memory exactly once, and never touch it afterward. When a driver breaks those rules — a buffer overflow, a double-free, a use-after-free — the heap's integrity checks eventually notice the damage and Windows crashes rather than run on corrupted kernel memory. It's the kernel equivalent of catching someone writing in another tenant's ledger.

The frustrating part of 0x13A is that the blue screen almost never names the guilty driver — the corruption is usually discovered long after the guilty write happened. That makes Driver Verifier, Windows' built-in driver stress tool, the centerpiece of the diagnosis. The sequence below builds up to it, clearing the easy causes first.

## Why this happens

- **Buggy third-party drivers.** Graphics, network, and antivirus filter drivers are the classic heap corruptors.
- **Outdated drivers on new Windows builds.** Old drivers violating heap rules that newer Windows versions check more strictly.
- **Corrupted driver installations.** Mixed or partial driver files behaving unpredictably in the kernel heap.
- **Faulty RAM.** Bad memory corrupts heap contents independently of any driver bug.
- **Incompatible security software.** Kernel filters from antivirus/VPN tools mishandling heap allocations.
- **Overclocked or unstable hardware.** Timing faults that corrupt memory the heap manager then flags.
- **Corrupted system files.** Damage to the kernel's own heap-management code producing false corruption signatures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update graphics and network drivers

Clear the most common heap-corrupting drivers first.

1. Clean-install the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) (custom install > clean installation).
2. Update the Wi-Fi/Ethernet driver from your laptop maker's support page — Dell, HP, or Lenovo all host model-specific builds.
3. Update the chipset driver package as well; it includes storage and bus drivers that allocate from the kernel heap.
4. Restart after each driver group and test with the workload that crashed.
5. If crashes began after a specific driver update, roll that driver back instead of updating further.

The 24H2-specific edition of this stop code is detailed in [how to fix KERNEL_MODE_HEAP_CORRUPTION in Windows 11 24H2](/articles/how-to-fix-kernel-mode-heap-corruption-in-windows-11-24h2/), and the post-update variant in [fix KERNEL_MODE_HEAP_CORRUPTION after Windows 11 update](/articles/fix-kernel-mode-heap-corruption-after-windows-11-update/).

### Fix 2: Remove or update security and VPN software

Kernel filters are disproportionate heap-corruption offenders.

1. Uninstall third-party antivirus using the vendor's removal tool (not just Settings > Apps).
2. Remove VPN clients, firewall utilities, and disk-encryption tools temporarily.
3. Test on Microsoft Defender alone for several days of normal use.
4. If stability returns, reinstall only the latest versions — old filter drivers are usually the problem.
5. Never stack two real-time security products; their heap interactions are a known 0x13A source.

### Fix 3: Run Driver Verifier to catch the culprit

Let Windows stress drivers until the guilty one crashes.

1. Create a **system restore point** first — this is non-negotiable.
2. Press **Windows + R**, type `verifier`, and press Enter.
3. Choose **Create custom settings**, enable **Special pool**, **Pool tracking**, **Force IRQL checking**, and **Deadlock detection**.
4. Choose **Select driver names from a list**, sort by **Provider**, and check all **non-Microsoft** drivers.
5. Click **Finish** and restart. Use the laptop normally — Verifier will blue-screen (often with a different stop code naming the driver) when it catches corruption.
6. After the crash, open the minidump in WinDbg (`!analyze -v`) — the named driver is your culprit.
7. Boot into **Safe Mode**, run `verifier /reset`, and restart to turn Verifier off, then update or remove the guilty driver.

Never verify all drivers including Microsoft's — that creates noise and boot loops. Target third-party drivers only.

### Fix 4: Test your RAM

If Verifier finds nothing, suspect the hardware.

1. Run `mdsched.exe` and check **MemoryDiagnostics-Results** in Event Viewer.
2. Run MemTest86 overnight from a USB stick for intermittent faults.
3. Load BIOS defaults to clear unstable memory timings.
4. Test RAM sticks individually if removable.
5. Heap corruption with clean Verifier results and failing memory tests means the RAM — not a driver — was corrupting the heap all along.

### Fix 5: Repair system files and update Windows

Fix the kernel's own heap machinery.

1. In **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Install every pending update in **Settings > Windows Update** — Microsoft fixes heap-manager bugs in cumulative updates.
3. If a specific update preceded the crashes, check the Microsoft Update Catalog for a superseding fix.
4. As a deeper repair, do an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
5. Retest before reinstalling third-party drivers — add them back one group at a time.

### Fix 6: Clean-boot to isolate the offender

When Verifier is inconclusive, isolate by elimination.

1. Run `msconfig`, hide Microsoft services, disable the rest; disable all Startup apps; restart.
2. Stress the system — if 0x13A stops, a disabled component was corrupting the heap.
3. Re-enable in halves to narrow it down, prioritizing RGB/fan control utilities, "optimizers," and peripheral software.
4. Update or permanently remove the offender.
5. Pay special attention to software that installs virtual devices (virtual audio cables, virtual cameras) — their drivers are frequent heap violators.

### Fix 7: Check thermals and reset hardware to stock

Unstable hardware corrupts memory that the heap checker then flags.

1. Reset all overclocks/undervolts in tuning utilities and BIOS.
2. Monitor CPU/GPU temperatures under load; clean vents and verify fans.
3. Test with the manufacturer's stock power plan and thermal profile.
4. If crashes only occur under sustained load with high temperatures, cooling maintenance is the fix, not driver surgery.
5. Persistent 0x13A at stock settings, current drivers, clean memory tests, and good thermals warrants manufacturer support — you've eliminated every software cause.

## Closing

KERNEL_MODE_HEAP_CORRUPTION looks mysterious because the blue screen hides the culprit, but the investigation is mechanical: update the usual-suspect drivers, strip out kernel-filter software, then let Driver Verifier do what it was built for — crash the guilty driver in the act. Most cases end at Fix 3 with a named driver and a clean update. The mistake is shotgun-reinstalling drivers at random or, worse, reinstalling Windows while a single bad filter driver waits to corrupt the fresh heap. Catch the corruptor, remove it, and the kernel heap stays clean.
