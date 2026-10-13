---
title: "How to Fix the CRITICAL_STRUCTURE_CORRUPTION Error Step by Step"
slug: how-to-fix-critical-structure-corruption-step-by-step
date: 2026-10-05
categories: ["windows-errors"]
tags: ["blue screen", "critical structure corruption", "windows 11", "kernel", "stop code"]
description: "CRITICAL_STRUCTURE_CORRUPTION blue screen? Follow this step-by-step guide to find the corrupt driver or hardware behind stop code 0x109."
thumbnail: "/images/thumbs/how-to-fix-critical-structure-corruption-step-by-step.webp"
faqs:
  - q: "What does CRITICAL_STRUCTURE_CORRUPTION mean?"
    a: "Windows detected that critical kernel code or data was modified — something overwrote memory it shouldn't have touched. Stop code 0x00000109. It's usually a buggy driver writing out of bounds, but failing RAM or a rootkit can also corrupt kernel structures."
  - q: "Is CRITICAL_STRUCTURE_CORRUPTION caused by a virus?"
    a: "It can be — rootkits patch kernel code, which is exactly what this check detects. But in practice, buggy third-party drivers are far more common. Still, run a full Microsoft Defender offline scan to rule malware out, since this particular stop code is one of the few where malware is a realistic suspect."
  - q: "Can overclocking cause this blue screen?"
    a: "Yes. Unstable CPU or RAM overclocks corrupt data in transit, and the kernel's integrity checks catch it as structure corruption. If you overclock, return everything to stock speeds first — it's the fastest way to rule hardware instability in or out."
  - q: "How do I find which driver caused it?"
    a: "Enable Driver Verifier (verifier.exe) to stress drivers until the guilty one crashes identifiably, or analyze the minidump with WinDbg. The dump's stack trace usually names the driver that was running when corruption was detected."
---

CRITICAL_STRUCTURE_CORRUPTION (stop code 0x109) is Windows' kernel integrity alarm going off. The kernel keeps critical code and data structures in protected memory, and it periodically verifies nobody has tampered with them. When that check fails — because a driver wrote where it shouldn't, RAM flipped a bit, or something malicious patched the kernel — Windows stops everything immediately. That's your blue screen.

This one deserves respect: unlike a flaky app crash, kernel corruption means something is actively damaging the core of your system. The steps below go after the causes in order, from the most likely (bad driver) to the most serious (malware, failing hardware).

## Why this happens

- **A driver writing out of bounds.** Buggy third-party drivers — especially storage filters, virtualization tools, and RGB/fan control utilities — overwrite kernel memory they don't own.
- **Failing RAM.** Bad memory cells corrupt kernel data as it's read and written, tripping the integrity check randomly.
- **Rootkits or bootkits.** Malware that patches the kernel is exactly what this detection was built to catch; it's rare, but this stop code is the one where you take it seriously.
- **Unstable overclocks.** Overclocked CPU, RAM, or GPU introduces errors that look exactly like corruption to the kernel's checks.
- **Corrupted system files.** Damage to kernel images themselves (ntoskrnl.exe and friends) fails integrity verification on load or during runtime checks.
- **Hypervisor or virtualization conflicts.** Hyper-V, VirtualBox, VMware, and some antivirus sandboxes all hook the kernel; conflicts between them can corrupt shared structures.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Run a full malware scan first

Because this stop code can mean a rootkit, rule that out before anything else.

1. Open **Windows Security** from the Start menu.
2. Go to **Virus & threat protection > Scan options**.
3. Select **Microsoft Defender Offline scan** and click **Scan now**.
4. The laptop restarts into a minimal environment and scans before Windows loads — this catches rootkits that hide from normal scans.
5. If threats are found, let Defender remove them, then restart and monitor for further crashes.

If the offline scan comes back clean, malware is unlikely and you can focus on drivers with confidence. Microsoft documents offline scanning on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 2: Remove recently installed drivers and utilities

Think about what changed just before the crashes started.

1. Boot into **Safe Mode** if normal boot crashes (interrupt startup three times for Automatic Repair, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**).
2. Open **Settings > Apps > Installed apps**, sort by date, and uninstall anything added just before the crashes: RGB controllers, fan utilities, disk tools, VPN clients, virtualization software.
3. Open **Device Manager** and roll back or uninstall any driver updated in the same window (**Properties > Driver > Roll Back Driver**).
4. Restart normally and test.

System utilities that install kernel drivers (RGB lighting, hardware monitors, overclocking tools) are disproportionately represented in 0x109 crashes. Similar driver-corruption patterns are covered in our [SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION guide](/articles/how-to-fix-special-pool-detected-memory-corruption-after-windows-11-update/).

### Fix 3: Update all drivers from the manufacturer

If nothing was recently installed, an old buggy driver may have finally been triggered.

1. Open **Device Manager** and check for warning icons.
2. Update chipset, storage controller, and network drivers from your laptop manufacturer's support page.
3. For Intel-based machines, [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the newest chipset and wireless drivers automatically.
4. Update the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) with a clean installation.
5. Restart and use the laptop normally for a day before declaring victory — these crashes can be intermittent.

### Fix 4: Test your RAM thoroughly

Random, inconsistent 0x109 crashes scream bad memory.

1. Press **Windows + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. For a definitive test, create a MemTest86 USB drive and run it overnight (4+ passes).
3. If errors appear, test sticks individually to isolate the bad one.
4. Replace faulty RAM — don't try to work around it with lower speeds; corrupted kernel memory is not something to negotiate with.
5. If your laptop has soldered RAM and it fails, that's a warranty/motherboard repair situation.

### Fix 5: Reset overclocks and BIOS to defaults

Unstable clocks produce exactly this signature.

1. Reset any CPU/GPU/RAM overclocking utilities (Afterburner, Ryzen Master, Intel XTU) to defaults.
2. Enter the BIOS and choose **Load Optimized Defaults**.
3. Specifically disable **XMP/EXPO** memory profiles — set RAM to standard JEDEC speeds.
4. Save, exit, and test under load.
5. If crashes stop, your overclock was unstable; re-tune more conservatively or leave it stock.

### Fix 6: Repair system files with SFC and DISM

Corrupted kernel images fail their own integrity checks.

1. Open **Terminal (Admin)**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` first (repairs the component store).
3. Then run `sfc /scannow` (repairs protected system files).
4. If SFC still reports unfixable corruption, do an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
5. Restart and monitor.

### Fix 7: Use Driver Verifier to identify the driver

When all else fails, force the guilty driver to reveal itself.

1. Press **Windows + R**, type `verifier.exe`, and press Enter.
2. Select **Create standard settings**, then **Automatically select all drivers installed on this computer**.
3. Restart — Verifier adds checks that make buggy drivers crash immediately and identifiably.
4. The resulting blue screen names the driver; boot to **Safe Mode**, run `verifier /reset` in an admin prompt, then update or remove that driver.
5. Never leave Verifier enabled day-to-day.

Related integrity-check crashes are discussed in our [SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION blue screen guide](/articles/special-pool-detected-memory-corruption-blue-screen-error-fix/).

## Closing

CRITICAL_STRUCTURE_CORRUPTION is Windows catching something red-handed in the kernel, and the culprit is usually a driver that got too ambitious with memory it didn't own. Scan for malware first (because this is the stop code where it matters), then work the driver and RAM angles methodically. One of these seven fixes resolves the overwhelming majority of cases — the key is not skipping the order and not assuming it's hardware before you've ruled out software.
