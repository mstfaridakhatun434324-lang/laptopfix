---
title: "Troubleshooting KERNEL_MODE_HEAP_CORRUPTION Blue Screens"
slug: kernel-mode-heap-corruption-troubleshooting
date: 2026-09-23
categories: ["windows-errors"]
tags: ["blue screen", "kernel mode heap corruption", "0x13a", "driver bug", "memory corruption"]
description: "KERNEL_MODE_HEAP_CORRUPTION (0x13A) crashing Windows? Learn how the kernel heap gets corrupted and troubleshoot it in 7 steps."
thumbnail: "/images/thumbs/kernel-mode-heap-corruption-troubleshooting.webp"
faqs:
  - q: "What does KERNEL_MODE_HEAP_CORRUPTION mean?"
    a: "It's stop code 0x00000013A. The kernel heap — the memory pool drivers allocate from — was found corrupted. Something wrote outside its allocation, freed memory twice, or used memory after freeing it. It's a driver bug in the overwhelming majority of cases."
  - q: "How is this different from MEMORY_MANAGEMENT?"
    a: "MEMORY_MANAGEMENT (0x1A) is a broader stop code covering many memory-manager-detected problems, while KERNEL_MODE_HEAP_CORRUPTION specifically means heap metadata or contents were corrupted. Both are usually driver-caused, but heap corruption points more specifically at a driver mishandling its allocations."
  - q: "Can I find which driver corrupted the heap?"
    a: "Yes — with Driver Verifier's special pool option enabled for suspect drivers, Windows crashes the moment a driver corrupts the heap, and the dump names it. Without Verifier, the crash is often detected long after the corruption happened, making the blamed driver unreliable."
  - q: "Is my RAM dying?"
    a: "Possibly, but drivers are far more likely. Heap corruption from bad RAM tends to blame random drivers across crashes. Consistent crashes tied to one device or activity point at that device's driver. Test memory to be sure, but start with drivers."
---

KERNEL_MODE_HEAP_CORRUPTION (0x13A) means Windows found its kernel memory pool — the heap drivers allocate from — damaged. Drivers constantly allocate and free heap memory, and when one writes past its allocation, frees the same block twice, or uses memory after freeing it, the heap's bookkeeping breaks. Windows detects the damage (sometimes much later) and crashes.

The tricky part: the crash often blames an innocent driver, because corruption is discovered after the fact. That's why this guide leans on Driver Verifier — it catches the corruption the instant it happens.

## Why this happens

- **Driver heap misuse.** Buffer overflows, double-frees, and use-after-free bugs in drivers — the classic cause.
- **Outdated drivers on new Windows builds.** Older drivers mishandle heap APIs that changed subtly.
- **Antivirus and filter drivers.** Heavy heap users operating at kernel level.
- **Corrupted driver binaries.** Damaged driver files executing incorrect allocation logic.
- **Faulty RAM.** Bad memory corrupts heap contents, mimicking driver bugs.
- **Overclocking instability.** Corrupts heap metadata under load.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Enable Driver Verifier with Special Pool

This is the key move for heap corruption — catch it at the moment of the crime.

1. Press **Windows + R**, type `verifier`, and press Enter.
2. Select **Create custom settings** and tick **Special pool** (this places each allocation on its own guarded page so overflows crash instantly).
3. Also tick **Pool tracking** to catch leaks and misuse.
4. Choose **Select driver names from a list** and tick third-party drivers — especially ones for devices involved in the crash scenario.
5. Restart and use the laptop normally. The next crash will name the corrupting driver directly. Then boot to Safe Mode and run `verifier /reset`.

### Fix 2: Fix the driver Verifier identifies

Act on Verifier's verdict.

1. Analyze the Verifier-triggered dump with BlueScreenView or WinDbg — note the named driver.
2. In **Device Manager**, find the device and try **Properties > Driver > Roll Back Driver** first.
3. If rollback isn't available, update the driver from the manufacturer's support page.
4. For persistent offenders, uninstall the device's software suite entirely and use the bare driver.
5. Keep Verifier disabled after the fix — it's a diagnostic tool, not a permanent setting.

### Fix 3: Update all major drivers systematically

If Verifier is inconclusive, refresh the whole driver stack.

1. Update chipset drivers from your laptop manufacturer's support page (Dell, HP, or Lenovo).
2. Clean-reinstall the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
3. Update network, audio, and storage drivers from the manufacturer — not from generic updater tools.
4. Restart between major groups and test.
5. If crashes started after a specific update, roll that driver back instead of updating everything blindly.

### Fix 4: Remove heap-heavy third-party software

Antivirus, backup, and "optimizer" tools are heavy kernel-heap users.

1. Uninstall third-party antivirus suites — use Windows Defender while testing.
2. Remove disk-encryption tools (other than BitLocker), backup agents with kernel drivers, and system optimizers.
3. Uninstall VPN clients temporarily.
4. Test for several days of normal use.
5. Reintroduce software one product at a time. Similar driver-hunting techniques apply to [SYSTEM_SERVICE_EXCEPTION](/articles/how-to-fix-system-service-exception-youtube/) crashes.

### Fix 5: Test memory thoroughly

Rule out RAM as the corruption source.

1. Press **Windows + R**, type `mdsched.exe`, and run the Extended memory diagnostic.
2. For deeper testing, run MemTest86 from USB for 4+ passes overnight.
3. Disable XMP/EXPO in BIOS/UEFI and retest at stock speeds.
4. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
5. Replace failing sticks with the exact spec from your laptop manual.

### Fix 6: Repair system files and check storage

Eliminate OS and disk corruption.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow` and restart.
3. Run `chkdsk C: /f` to check the system drive.
4. Verify SSD SMART health with the manufacturer's utility.
5. Corrupted driver binaries on a failing drive cause heap corruption that no driver update fixes — replace a failing drive. For the closely related stop code, see our [MEMORY_MANAGEMENT blue screen guide](/articles/memory-management-bsod-windows-11-fix/).

### Fix 7: Reset Windows when the heap is beyond repair

Last resort for a corrupted driver stack.

1. Back up your files externally.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Keep my files** with **Cloud download**.
3. After reset, install drivers only from the manufacturer's support page, in order: chipset, storage, network, graphics.
4. Test stability before reinstalling third-party utilities.
5. Microsoft's [blue screen troubleshooting hub](https://support.microsoft.com/en-us/windows) has further recovery guidance.

### Fix 8: Audit recently installed software for kernel drivers

Some applications install kernel drivers you'd never suspect.

1. Open **Settings > Apps > Installed apps** and sort by install date.
2. Look at everything installed in the weeks before crashes began — especially "system utilities," RGB software, game anti-cheat clients, and developer tools.
3. Anti-cheat drivers (used by many popular games) are notorious heap-corruption sources; try uninstalling the game that installed them as a test.
4. Check **Device Manager > View > Show hidden devices** for non-plug-and-play drivers from uninstalled software and remove the leftovers.
5. Use `fltmc` in **Terminal (Admin)** to list active filter drivers — research any unfamiliar names before removing them.

## Closing

KERNEL_MODE_HEAP_CORRUPTION is a driver bug that hides behind delayed detection — which is exactly why Driver Verifier's Special Pool exists. Enable it, let it name the culprit, fix that driver, and move on. Without Verifier you're guessing; with it, you're doing forensics. Either way, resist blaming the RAM until drivers are exonerated — the heap belongs to drivers, and they're the ones who break it. Document which driver was guilty; if the crash ever returns, you'll know exactly where to look first instead of starting over. Patience with the diagnostic steps pays off far more than guesswork ever does.
