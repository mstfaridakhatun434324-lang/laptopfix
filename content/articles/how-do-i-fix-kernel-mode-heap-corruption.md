---
title: "KERNEL_MODE_HEAP_CORRUPTION: How to Fix It in Windows 11"
slug: how-do-i-fix-kernel-mode-heap-corruption
date: 2026-10-11
categories: ["windows-errors"]
tags: ["kernel mode heap corruption", "bsod", "stop code 0x13a", "windows 11"]
description: "KERNEL_MODE_HEAP_CORRUPTION (0x13A) signals memory corruption at the kernel level. Identify the cause and fix it step by step."
thumbnail: "/images/thumbs/how-do-i-fix-kernel-mode-heap-corruption.webp"
faqs:
  - q: "What does KERNEL_MODE_HEAP_CORRUPTION mean?"
    a: "It means the Windows kernel detected corruption in its heap memory — the dynamic memory pool drivers and kernel components use for allocations. Stop code 0x0000013A fires when integrity checks catch a driver writing to freed memory, overflowing a buffer, or otherwise damaging the heap. The system stops to prevent the corruption from spreading."
  - q: "Which drivers cause KERNEL_MODE_HEAP_CORRUPTION?"
    a: "Graphics drivers are the most frequent cause, followed by network and audio drivers. The minidump usually names the offending .sys file. Because the corruption is often detected later than when it happened, Driver Verifier is the most reliable tool for catching the driver in the act — it crashes the system at the moment of corruption instead."
  - q: "Can faulty RAM cause KERNEL_MODE_HEAP_CORRUPTION?"
    a: "Yes. Bad memory cells corrupt heap data exactly the way a buggy driver would, and the kernel cannot tell the difference. Run the Windows Memory Diagnostic early in troubleshooting. If it reports errors, replace the faulty module before chasing drivers — no driver update fixes bad silicon."
  - q: "Is KERNEL_MODE_HEAP_CORRUPTION caused by overclocking?"
    a: "Frequently. Overclocked CPUs and memory with aggressive timings corrupt heap allocations under load, and the kernel's integrity checks catch it as heap corruption. If the crashes started after enabling XMP or any overclock, restore BIOS defaults first — it's the fastest possible fix for this stop code."
---

**KERNEL_MODE_HEAP_CORRUPTION** (stop code **0x0000013A**) means Windows caught something damaging its kernel heap — the pool of memory where drivers and core components allocate data structures on the fly. The kernel runs integrity checks on this memory, and when it finds a driver wrote to freed memory, overflowed a buffer, or otherwise corrupted the heap, it stops the system before the damage cascades.

This error is tricky because the corruption is usually **detected later than it happened** — the driver that caused it may have run minutes before the crash, so the minidump doesn't always point at the true culprit. That makes Driver Verifier (which catches corruption the instant it occurs) more valuable here than for most blue screens. The usual suspects: graphics drivers first, then network and audio drivers, then bad RAM, then overclocking.

Don't confuse detection delay with randomness. If crashes cluster around gaming or video work, suspect the GPU driver; if they're random, suspect RAM or a filter driver. For the related pool-corruption family, see [special pool memory corruption fixes](/articles/special-pool-detected-memory-corruption-blue-screen-error-fix/) and the [Dell-specific walkthrough](/articles/how-to-fix-special-pool-detected-memory-corruption-on-dell-laptop/).

## Why this happens

- **Buggy graphics drivers**: The number one cause — GPU drivers allocate heavily from the kernel heap and bugs there corrupt it constantly.
- **Faulty RAM**: Bad cells corrupt heap data indistinguishably from driver bugs; always test memory for this stop code.
- **Overclocked CPU or memory**: Unstable clocks corrupt heap allocations under load; XMP profiles are a frequent trigger.
- **Corrupt driver installations**: Partially installed or mixed-version drivers (e.g. after a failed GPU driver update) corrupt their own heap usage.
- **Third-party filter drivers**: Antivirus, VPN, and disk utility drivers that allocate from the kernel heap incorrectly.
- **Corrupt system files**: Damage to kernel components that manage the heap.
- **Failing GPU hardware**: A dying graphics chip corrupting its own memory operations, rare but real on aging gaming laptops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean-reinstall the graphics driver

The highest-probability fix — do it properly, not via Device Manager's generic update.

1. Download **Display Driver Uninstaller (DDU)** and the latest GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for your exact GPU.
2. Boot into **Safe Mode** (hold **Shift** > **Restart** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **4**).
3. Run DDU, select your GPU brand, and choose **Clean and restart**. This removes every trace of the old driver.
4. After reboot, install the freshly downloaded driver. Choose **Custom / Clean Install** if the installer offers it.

### Fix 2: Test RAM with Windows Memory Diagnostic

Heap corruption and bad RAM look identical — rule out hardware early.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let the full test complete. Any errors = faulty RAM; reseat removable modules and retest, then replace if errors persist.
3. For a deeper test, run **MemTest86** from a USB drive overnight (4+ passes) — it catches intermittent faults the built-in test misses.
4. Only continue to driver-chasing steps after RAM passes; no software fix survives bad memory.

### Fix 3: Reset overclocks and BIOS defaults

Remove the most common self-inflicted cause.

1. Disable any overclocking or undervolting tools (Intel XTU, ThrottleStop, Ryzen Master, MSI Afterburner) and stop them auto-applying at startup.
2. Enter **BIOS/UEFI** and **Load Optimized Defaults** — this clears XMP/DOCP profiles and manual timings.
3. Save, exit, and test under the workload that crashed (game, render, or benchmark).
4. If stability returns, the overclock was corrupting the heap. Keep stock settings, or re-tune conservatively with stress testing.

### Fix 4: Run Driver Verifier to catch the corrupting driver

When the minidump doesn't name the culprit, force it to reveal itself.

1. Press **Win + R**, type `verifier`, and press Enter.
2. Choose **Create custom settings**, enable **Special pool**, **Pool tracking**, **Force IRQL checking**, and **Deadlock detection** — these target heap corruption specifically.
3. Select **Select driver names from a list** and check third-party drivers only (graphics, network, audio — skip Microsoft drivers).
4. Restart and use the laptop normally. Verifier will blue-screen at the moment of corruption, naming the driver. Then boot to Safe Mode, run `verifier /reset`, and replace that driver.

### Fix 5: Update network and audio drivers

The next most common heap-corrupting drivers after graphics.

1. In **Device Manager**, update drivers under **Network adapters** and **Sound, video and game controllers** (**Update driver** > **Search automatically**).
2. For Intel Wi-Fi/Bluetooth, run Intel's Driver & Support Assistant for the latest builds.
3. If crashes began after a specific driver update, roll that driver back (**Properties** > **Driver** > **Roll Back Driver**).
4. Restart and test — network drivers in particular corrupt the heap during sleep/wake cycles.

### Fix 6: Repair system files and check the disk

Eliminate corruption in the kernel components themselves.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` and restart to let it scan — filesystem damage can corrupt driver files that then corrupt the heap.
4. After all repairs and a restart, retest. If SFC found corruption, that alone may have been the cause.

### Fix 7: Remove conflicting filter-driver software

Antivirus, VPNs, and disk tools allocate from the same heap.

1. Temporarily **uninstall** (not just disable) third-party antivirus, VPN clients, and disk utility software one category at a time, restarting and testing after each.
2. Windows Defender covers you during testing.
3. If removing a program stops the crashes, reinstall its latest version or replace it — the old build's filter driver was the corrupter.
4. As a final step, check Microsoft's support site for any known heap-corruption issues with your Windows build, and install pending updates.

## Closing

KERNEL_MODE_HEAP_CORRUPTION looks deep and scary, but the fix is usually shallow: a clean GPU driver reinstall, RAM that passes testing, or an overclock returned to stock. The key discipline is testing RAM early — everything else is wasted effort if the memory itself is faulty — and using Driver Verifier when the dumps won't name the culprit. Persistent crashes after all seven fixes, at stock settings with good RAM, point at failing GPU hardware and a service-center visit.
