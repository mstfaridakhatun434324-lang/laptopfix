---
title: "Fix KERNEL_SECURITY_CHECK_FAILURE After a Windows 11 Update"
slug: how-to-fix-kernel-security-check-failure-after-windows-11-update
date: 2026-09-03
categories: ["windows-errors"]
tags: ["bsod", "stop code 0x139", "windows 11 update", "drivers"]
description: "Fix KERNEL_SECURITY_CHECK_FAILURE after a Windows 11 update — verify drivers, test memory, and repair the kernel's trust checks."
thumbnail: "/images/thumbs/how-to-fix-kernel-security-check-failure-after-windows-11-update.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "Stop code 0x00000139 means the kernel detected corruption in a critical data structure — a linked list, a stack cookie mismatch, or a similar integrity check failed. After a Windows 11 update, this is usually a driver that worked on the old build but corrupts structures on the new one, or damaged system files."
  - q: "Is this a virus?"
    a: "Almost never. The name sounds like a security alert, but it's a kernel integrity check, not an antivirus verdict. Malware is a distant possibility worth one offline scan, but drivers and memory are the realistic suspects — don't let the name send you down the wrong path."
  - q: "Why did it start right after the update?"
    a: "Because the update changed kernel internals. Drivers that bent the rules on the old build can break them outright on the new one. The update didn't damage anything — it exposed a driver bug that was always there, or delivered a new driver version with a fresh bug."
  - q: "How is this different from other BSODs?"
    a: "The kernel caught the corruption itself via an internal consistency check, rather than a driver doing something illegal. That makes the minidump especially informative — parameter 1 of the bugcheck tells you exactly which check failed, which narrows the suspect list fast."
---
KERNEL_SECURITY_CHECK_FAILURE (stop code 0x00000139) sounds like your antivirus found something. It didn't. This is the Windows kernel failing one of its own internal consistency checks — a corrupted linked list, a mismatched stack cookie, a data structure that doesn't add up. When it starts right after a Windows 11 update, the story is familiar: the update rearranged kernel internals, and a driver that was quietly bending the rules on the old build is now breaking them loudly.

The good news is the minidump for this stop code is unusually informative — the bugcheck parameters identify which check failed. This guide uses that to aim the fixes precisely, in the order that resolves post-update cases fastest.

## Why this happens

- **A driver incompatible with the updated kernel.** The top post-update cause. Network, storage, and antivirus filter drivers are the usual offenders.
- **Corrupted system files from the update.** A damaged update leaves kernel files or drivers in a half-updated state that fails integrity checks.
- **Failing RAM.** Bit flips in kernel data structures trip the exact checks this stop code represents. Post-update timing can be coincidence.
- **Overclocked memory or CPU.** Unstable clocks corrupt data in transit, and kernel structures are not exempt.
- **Disk corruption.** Bad sectors in the pagefile or driver storage corrupt what gets loaded into the kernel.
- **A rootkit or bootkit.** Rare, but kernel-mode malware triggers these checks by design — worth one offline scan to exclude.

## How to fix it

Work through these in order. The dump analysis first, because it tells you which check failed.

### Fix 1: Read the bugcheck parameters from the dump

This stop code's parameters are a diagnosis in themselves.

1. Open `C:\Windows\Minidump` and load the newest dump in **WinDbg Preview** (Microsoft Store).
2. Run `!analyze -v`. Note **parameter 1**: `0x3` means a LIST_ENTRY was corrupted (driver list corruption — very common), `0x0` points elsewhere. The analysis names the likely component.
3. Check **IMAGE_NAME** too — if it names a third-party driver, skip straight to Fix 3.
4. First time with WinDbg? Our [dump-reading guide](/articles/best-way-to-read-dump-files-with-windbg/) explains the commands without assuming experience.

### Fix 2: Uninstall the update that triggered it

When the timeline is clear, remove the trigger and reassess.

1. Boot to Safe Mode if needed (interrupt boot 3x > **Automatic Repair** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4**).
2. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the update matching your crash timeline.
3. Reboot and test for 24 hours. Stable? The update exposed or delivered a bad driver — now find it with Fix 3 before reinstalling the update.
4. Pause updates for two weeks while you sort the driver situation.

### Fix 3: Update or roll back the implicated driver

Target the driver the dump named — or the most recently updated one.

1. Open **Device Manager** (`devmgmt.msc`), find the device, **Properties** > **Driver** tab.
2. If the driver date matches the update window, try **Roll Back Driver** first.
3. Otherwise, **Uninstall device** (tick **Attempt to remove the driver for this device**), reboot, and install the manufacturer's latest from their support site.
4. Pay special attention to **network adapters**, **storage controllers**, and any **third-party antivirus filter drivers**. Intel Wi-Fi users can check the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for the newest stable build.

### Fix 4: Remove third-party security software temporarily

Antivirus filter drivers are disproportionately represented in 0x139 dumps.

1. Uninstall your third-party antivirus via **Settings** > **Apps** > **Installed apps**.
2. Run the vendor's official removal tool to clear leftover kernel drivers — the standard uninstall isn't enough.
3. Let Microsoft Defender take over automatically and test for a day or two.
4. If stability returns, the old suite's drivers were the problem. Reinstall only the current version from the vendor. Similar filter-driver issues cause [system service exceptions](/articles/system-service-exception-windows-11-fix/) too.

### Fix 5: Reset overclocks and test RAM

Integrity-check failures are exactly what unstable hardware produces.

1. Enter BIOS/UEFI and load **Optimized Defaults** — disable XMP/EXPO, CPU overclocks, and undervolts.
2. In Windows, run `mdsched.exe` > **Restart now and check for problems**, **F1** > **Extended**, two full passes.
3. For a definitive test, run MemTest86 from USB overnight.
4. Memory errors mean reseat or replace the stick. Clean memory plus stock clocks eliminates the hardware explanation.

### Fix 6: Repair system files and check the disk

Cover file corruption on both fronts.

1. In **Terminal (Admin)**: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
2. Run `chkdsk C: /f /r`, type **Y**, reboot for the full scan.
3. If chkdsk finds bad sectors on an SSD, back up promptly — SSDs remap silently until they can't.
4. Microsoft documents SFC and DISM usage on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: Run Driver Verifier to catch the corruptor

When the dump keeps blaming Windows components, make the real driver confess.

1. **Win + R** > `verifier` > **Create custom settings**, all checks except Low Resource Simulation.
2. Select non-Microsoft drivers, reboot, use the PC normally until it crashes.
3. The new dump will name the driver corrupting the structures.
4. Safe Mode > `verifier /reset` to disable, then replace the named driver.

### Fix 8: Offline malware scan, then repair install

Close out the remaining possibilities.

1. **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** > **Scan now**.
2. If clean and still crashing, do an in-place repair: mount the Windows 11 ISO from [Microsoft](https://www.microsoft.com/en-us/software-download/windows11), run **setup.exe**, keep files and apps.
3. After the repair, install manufacturer drivers before Windows Update runs, so validated drivers land first.

## Closing

KERNEL_SECURITY_CHECK_FAILURE after an update is the kernel telling you exactly what it found — and the dump parameters tell you where to look. Follow the evidence: uninstall the triggering update, replace the driver the dump names, evict the filter drivers, and verify the hardware. The name is scarier than the fix. Most of these resolve at Fix 2 or Fix 3, in the time it takes to reboot a few times and read one dump file.
