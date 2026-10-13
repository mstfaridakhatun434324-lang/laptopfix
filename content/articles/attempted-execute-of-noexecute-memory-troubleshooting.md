---
title: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: Troubleshooting Guide"
slug: attempted-execute-of-noexecute-memory-troubleshooting
date: 2026-09-22
categories: ["windows-errors"]
tags: ["bsod", "noexecute-memory", "windows-11"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY means code tried to run from protected memory. Here's how to find the cause and fix it."
thumbnail: "/images/thumbs/attempted-execute-of-noexecute-memory-troubleshooting.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "It is a blue screen stop code (0x000000FC) meaning the system tried to execute code from a memory region marked non-executable (NX). Either a driver has a bug, or something malicious tried to run code from a data-only region."
  - q: "Is this error caused by a virus?"
    a: "It can be — this is exactly the kind of behavior Data Execution Prevention is designed to catch. But on most home laptops it is a buggy driver. Run a full Defender scan to rule malware out, then focus on drivers."
  - q: "What is the NX bit and why does it matter?"
    a: "The NX (No-eXecute) bit marks memory pages as data-only so the CPU refuses to run code from them. It is a hardware security feature. This blue screen means something tried to violate that protection, and Windows stopped it."
  - q: "Can RAM problems cause this stop code?"
    a: "Yes. Failing memory can corrupt page table entries, making executable regions look non-executable or vice versa. If driver fixes do not help, test the RAM — it is a legitimate suspect for this particular stop code."
---

`ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY` — stop code `0x000000FC` — is Windows' Data Execution Prevention doing its job. Modern CPUs can mark memory regions as non-executable, and when something tries to run code from one of those protected regions, the CPU faults and Windows blue-screens rather than allow it.

That "something" is usually a buggy driver with a memory-management flaw. Occasionally it is malware attempting exactly the kind of trick DEP exists to stop. Either way, the troubleshooting path is the same: rule out malware, find the driver, fix it, and check the RAM if needed.

## Why this happens

- **A driver bug corrupts memory protections.** The most common cause — a driver mishandles page permissions and tries to execute from a data region.
- **Malware attempting code injection.** Rootkits and exploits that try to run code from data pages trip this exact detection.
- **Failing RAM corrupting page tables.** Bad memory can scramble the execute permissions the CPU relies on.
- **Corrupted driver binaries.** Damaged `.sys` files behave unpredictably, including jumping to invalid addresses.
- **Overclocking or unstable memory timings.** Marginal RAM corrupts the page tables that enforce NX protection.
- **Outdated BIOS or chipset drivers.** Firmware bugs in memory management can produce spurious NX faults.
- **Conflicting low-level software.** Antivirus and virtualization drivers that manipulate memory protections can clash.

## How to fix it

Work through these in order, from least to most invasive. Start with the malware scan — this stop code warrants it.

### Fix 1: Run a full malware scan

Because this stop code is a security tripwire, rule out malicious causes first.

1. Open **Windows Security** > **Virus & threat protection** > **Scan options**.
2. Select **Full scan** and let it complete — this takes a while, so plug in the charger.
3. Then run **Microsoft Defender Offline scan**, which reboots into a clean environment outside the running OS.
4. If threats are found and removed, run `sfc /scannow` in an elevated Command Prompt to repair any system damage they caused.
5. Only move on to driver troubleshooting if scans come back clean — chasing drivers while malware is active wastes time.

### Fix 2: Identify the driver from the minidump

With malware ruled out, find the driver the same way as any other blue screen.

1. Press `Win + R`, type `%SystemRoot%\Minidump`, and press **Enter**.
2. Open the newest dump in **WinDbg Preview** (free from the Microsoft Store).
3. Run `!analyze -v` and read `MODULE_NAME` and `IMAGE_NAME`.
4. Note the faulting driver name — graphics, network, and storage drivers are the usual candidates.
5. If dumps consistently name the same driver, you have your target; if they vary wildly, skip ahead to the RAM test in Fix 5.
6. Our [DRIVER_VERIFIER_DETECTED_VIOLATION guide](/articles/how-to-fix-driver-verifier-detected-violation-youtube/) covers WinDbg analysis in detail if you need it.

### Fix 3: Update or roll back the identified driver

Fix the specific driver the dump named — not every driver on the system.

1. Open **Device Manager** and locate the device matching the `.sys` file.
2. Right-click > **Update driver** > **Search automatically for drivers**.
3. If that does not help, download the latest stable driver from your laptop maker's support page for your exact model.
4. If crashes started right after a driver update, use **Properties** > **Driver** tab > **Roll Back Driver** instead.
5. For graphics drivers, a clean reinstall with DDU in Safe Mode is worth the extra effort — use the [NVIDIA driver page](https://www.nvidia.com/Download/index.aspx) or [AMD driver page](https://www.amd.com/en/support/download/drivers.html) for the fresh copy.

### Fix 4: Remove conflicting kernel-level software

Software that manipulates memory protections can trigger NX faults when it clashes with Windows.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall third-party antivirus, virtualization tools, and system "optimizers" that install kernel drivers.
3. Restart and test for a few days with just Windows Security active.
4. Reinstall needed software one at a time, using the latest versions, to identify any offender.
5. Microsoft documents DEP behavior and troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Test the RAM thoroughly

This stop code has a genuine memory angle — corrupted page tables produce exactly this fault.

1. Press `Win + R`, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**, press **F1**, and select the **Extended** test.
3. For a definitive result, run MemTest86 from a USB drive overnight.
4. Replace any stick that errors, testing one at a time on dual-slot laptops.
5. Disable XMP or manual memory overclocks in the BIOS — unstable timings corrupt page tables. The RAM-testing steps in our [MEMORY_MANAGEMENT guide](/articles/how-to-fix-stop-code-memory-management-on-dell-laptop/) apply directly here.

### Fix 6: Repair system files and update the BIOS

Cover firmware and on-disk corruption in one pass.

1. Open an elevated Command Prompt, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Check your BIOS version with `msinfo32` and compare against the latest on your manufacturer's support page.
3. Flash the BIOS with the charger plugged in; do not interrupt it.
4. Load BIOS defaults afterward and reconfigure only what you need.
5. Restart and monitor for several days.

### Fix 7: Reset Windows if the fault persists

When the dump names Windows components themselves and everything else checks out, start fresh.

1. Back up your files to an external drive.
2. Go to **Settings** > **System** > **Recovery** > **Reset PC**.
3. Choose **Keep my files** first; use **Remove everything** only if crashes continue.
4. After the reset, install drivers from the manufacturer's site before running Windows Update.
5. NX faults on a clean install with tested RAM indicate a motherboard or CPU fault — professional diagnosis time.

## Closing

`ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY` is DEP catching something trying to run code where code should never run. Scan for malware first since this is a security boundary, then treat it like any driver crash: read the dump, fix the named driver, and test the RAM if the dumps are inconsistent. It is an intimidating stop code with a very manageable fix list.
