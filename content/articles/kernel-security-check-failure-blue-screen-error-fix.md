---
title: "KERNEL_SECURITY_CHECK_FAILURE: Blue Screen Error Fix"
slug: kernel-security-check-failure-blue-screen-error-fix
date: 2026-09-10
categories: ["windows-errors"]
tags: ["bsod", "drivers", "stop code"]
description: "KERNEL_SECURITY_CHECK_FAILURE blue screen? Windows caught corrupted kernel data. Here's how to find the cause and fix it."
thumbnail: "/images/thumbs/kernel-security-check-failure-blue-screen-error-fix.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "The Windows kernel detected corruption in a critical data structure — like a linked list or stack cookie mismatch — and stopped the system (stop code 0x139). It's usually a buggy driver corrupting kernel memory, though bad RAM and failing drives cause it too."
  - q: "Is this error a sign of a virus?"
    a: "It can be. This stop code fires when kernel data structures are corrupted, and rootkits do exactly that. If crashes appeared alongside other suspicious behavior, run a Microsoft Defender Offline scan. But buggy drivers are the more common cause."
  - q: "Why does it happen when I open a specific app or game?"
    a: "That app loads a kernel driver (anti-cheat, audio driver, overlay software) that corrupts kernel structures when active. Update or reinstall that app and its associated drivers — the trigger app usually points straight at the culprit."
  - q: "Can overclocking cause KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Yes. Unstable CPU or RAM overclocks corrupt kernel data structures in ways that trip this exact check. Reset to stock speeds in BIOS before doing driver surgery — it's a two-minute test that rules out a whole category."
---

`KERNEL_SECURITY_CHECK_FAILURE` (stop code 0x139) is the kernel's integrity alarm: it found one of its own critical data structures corrupted — a smashed stack, a broken linked list, a failed security cookie check — and halted rather than run on compromised foundations. The name mentions "security," but most of the time it's a reliability bug: a driver scribbling where it shouldn't.

Because drivers, RAM, storage, and malware can all corrupt kernel structures, this one needs a methodical approach. The order below rules out the most likely and easiest causes first.

## Why this happens

- **Buggy or outdated driver**: The top cause. Drivers that corrupt kernel pools or stacks trip this check — graphics, network, and audio drivers lead the pack.
- **Failing RAM**: Bad memory corrupts kernel data structures directly, producing this exact stop code.
- **Corrupted system files**: Damaged kernel components fail their own integrity checks.
- **Malware or rootkits**: Kernel-mode malware corrupts the structures this check protects — that's what the check was designed to catch.
- **Overclocking instability**: Unstable clocks corrupt kernel memory under load.
- **Failing storage**: A dying drive corrupts driver and system files as they load, causing secondary corruption the kernel then detects.

## How to fix it

Work through these in order — quick checks first, deeper diagnostics after.

### Fix 1: Reset overclocks and test

The fastest thing to rule out.

1. Enter BIOS/UEFI and load **Optimized Defaults** — this clears CPU overclocks and XMP memory profiles.
2. Reset any tuning software (MSI Afterburner, Intel XTU, Ryzen Master) to stock.
3. Use the laptop normally for a day. If crashes stop, instability was the cause.
4. If you re-overclock later, stress-test with Prime95 or OCCT for several hours before trusting it.

### Fix 2: Run a malware scan

Since this stop code is literally a security check, rule out the malicious cause early.

1. Open **Windows Security** > **Virus & threat protection** > **Scan options**.
2. Run a **Microsoft Defender Offline scan** — it reboots outside Windows where rootkits can't hide.
3. Remove anything found and retest.
4. If you run third-party antivirus, make sure it's current — outdated AV kernel drivers themselves cause this crash.

### Fix 3: Update drivers, starting with graphics and network

Drivers are the most common non-malware cause.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Update display adapters first: get the latest from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) — choose clean installation options.
3. Update network adapters, audio devices, and chipset/system devices.
4. Install the full driver pack from your laptop maker's site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
5. If crashes started after a driver update, roll it back instead (**Properties** > **Driver** tab > **Roll Back Driver**).
6. Don't overlook audio drivers — Realtek and Conexant audio drivers are a surprisingly common source of this stop code. Update them from the laptop manufacturer's site rather than Windows Update, since OEM audio drivers are heavily customized.
7. After each driver change, use the laptop for several hours before moving on. This stop code can take a while to reappear, so give each change a real chance to prove itself before you declare it innocent.

### Fix 4: Test your RAM

Bad RAM is the leading hardware cause of this stop code.

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Any error means bad RAM. Confirm with MemTest86 overnight for borderline cases.
3. Reseat modules if accessible; test sticks individually on laptops with removable RAM.
4. Related reading: our [MEMORY_MANAGEMENT stop code guide](/articles/how-to-fix-stop-code-memory-management-step-by-step/) covers the full memory-diagnostic workflow.

### Fix 5: Check drive health and repair system files

Failing storage corrupts the files the kernel integrity-checks.

1. Run `chkdsk C: /f /r` from an elevated Command Prompt (schedule and reboot if needed).
2. Check SMART status with CrystalDiskInfo or manufacturer diagnostics.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
4. If the drive is failing, back up immediately and replace it — no software fix survives a dying drive.

### Fix 6: Use Driver Verifier to catch the corrupting driver

When dumps blame the kernel generally, Verifier identifies the specific driver corrupting structures.

1. Press **Win + R**, type `verifier`, press Enter.
2. **Create standard settings** > **Automatically select unsigned drivers** (or pick suspects) > **Finish**. Restart.
3. Use the laptop until it crashes — Verifier's crash names the driver.
4. Boot to Safe Mode, run `verifier`, choose **Delete existing settings**, then fix the identified driver.
5. If Verifier names a Microsoft driver like `ntoskrnl.exe` itself, don't try to "update" the kernel — a third-party driver corrupted kernel structures before the check ran. Widen Verifier's selection to cover more third-party drivers and test again.
6. If Verifier causes a boot loop, our [Driver Verifier IOManager violation guide](/articles/best-way-to-fix-driver-verifier-iomanager-violation/) shows how to escape it.
7. Never leave Verifier running once you've identified the culprit — it slows the system and manufactures crashes by design.

### Fix 7: Check the 24H2-specific angle

If this started with Windows 11 24H2, check the update-specific causes.

1. Review our [kernel security check failure on 24H2 guide](/articles/how-to-fix-kernel-security-check-failure-in-windows-11-24h2/) for update-specific driver conflicts.
2. Ensure BIOS is current — 24H2-era crashes are disproportionately fixed by firmware updates.
3. As a final step, an in-place upgrade from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) refreshes all system files while keeping your data and apps.

## Closing

KERNEL_SECURITY_CHECK_FAILURE is the kernel refusing to run on corrupted foundations — and the corruption almost always comes from a driver, bad RAM, or (less often) malware. Reset overclocks, scan for malware, update drivers, test memory, and let Driver Verifier name names if the culprit stays hidden. Work it in order and the crashes stop.
