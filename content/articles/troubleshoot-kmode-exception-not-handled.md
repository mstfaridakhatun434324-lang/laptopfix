---
title: "How to Troubleshoot the KMODE Exception Not Handled Blue Screen"
slug: troubleshoot-kmode-exception-not-handled
date: 2026-09-16
categories: ["windows-errors"]
tags: ["kmode exception", "bsod", "kernel mode", "driver error"]
description: "Troubleshoot the KMODE_EXCEPTION_NOT_HANDLED blue screen: find the failing driver, update or roll it back, and run the hardware checks that rule out RAM."
thumbnail: "/images/thumbs/troubleshoot-kmode-exception-not-handled.webp"
faqs:
  - q: "What does KMODE Exception Not Handled mean?"
    a: "A kernel-mode driver generated an exception that Windows' error handler couldn't process — usually an illegal memory access. Stop code 0x0000001E. The blue screen often names the offending .sys file in parentheses, which identifies the exact driver to update, roll back, or remove. It's a driver bug in the overwhelming majority of cases."
  - q: "How is this different from IRQL Not Less or Equal?"
    a: "Both are kernel-mode driver errors, but IRQL specifically involves a driver accessing paged memory at an elevated interrupt level, while KMODE covers other unhandled exceptions like illegal instructions or access violations. Practically, the fix approach is identical: identify the named driver and update or roll it back. Our IRQL guide covers that sibling error."
  - q: "Can RAM cause KMODE Exception Not Handled?"
    a: "Yes. Bad RAM corrupts driver code and data as it runs, producing exceptions the driver didn't cause — which is why the named .sys file sometimes changes between crashes. If the culprit file varies crash to crash, suspect memory: run Windows Memory Diagnostic and test sticks individually before chasing drivers."
  - q: "Should I use Driver Verifier for this error?"
    a: "Only if the guilty driver won't identify itself. Verifier stresses selected drivers until the faulty one crashes with a clearer stop code. It's powerful but must be used carefully: select only non-Microsoft drivers, and always run verifier /reset afterward. Never leave it enabled permanently — it degrades performance and causes its own crashes."
---

KMODE_EXCEPTION_NOT_HANDLED (stop code 0x0000001E) is Windows reporting that a kernel-mode driver hit an exception — an illegal operation like accessing forbidden memory — that no error handler caught. In plain terms: a driver did something the kernel couldn't allow, and rather than risk corruption, Windows stopped. The genuinely helpful part is that the blue screen usually names the offending driver file in parentheses after the stop code, handing you the diagnosis on a plate.

Driver bugs cause the vast majority of these crashes. The classic offenders are network drivers, graphics drivers, and storage drivers, often right after an update. But there's a meaningful minority of cases where the driver is innocent and bad RAM is corrupting its code at runtime — the tell is when the named file changes from crash to crash. This guide covers both paths: identify the driver, fix the driver, then verify the hardware. For the closely related interrupt-level variant, see our [IRQL Not Less or Equal guide](/articles/irql-not-less-or-equal-windows-11-fix/); for crashes in kernel traps rather than exceptions, see our [unexpected kernel mode trap guide](/articles/how-to-fix-unexpected-kernel-mode-trap-after-windows-11-update/).

## Why this happens

- **Buggy device drivers**: Network, graphics, and storage drivers with memory-access bugs are the leading cause.
- **Driver update regressions**: A new driver version introducing a bug the old one didn't have.
- **Overclocked hardware**: Unstable CPU/RAM/GPU clocks cause exceptions under load that vanish at stock settings.
- **Failing RAM**: Memory errors corrupt executing driver code, producing exceptions with varying culprit files.
- **Corrupt driver files**: Partial installations or disk errors damaging .sys files on disk.
- **Antivirus filter drivers**: Kernel hooks from security software conflicting after updates.
- **Windows update incompatibility**: Kernel changes in an update exposing latent bugs in older drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the named driver file

Capture the diagnosis the blue screen offers.

1. Photograph the blue screen, capturing the filename in parentheses after KMODE_EXCEPTION_NOT_HANDLED (e.g., `ntoskrnl.exe`, `ndis.sys`, `nvlddmkm.sys`).
2. If you missed it, check **Event Viewer** > **Windows Logs** > **System** for the BugCheck entry, or analyze `C:\Windows\Minidump` with BlueScreenView.
3. Map common files: `ndis.sys`/`Netwtw*`/`rtwlan*` = network drivers, `nvlddmkm.sys` = NVIDIA graphics, `ntoskrnl.exe` named alone often means RAM or a driver corrupting the kernel itself.
4. If the named file is different every crash, skip driver-chasing and go straight to Fix 6 (RAM testing) — varying culprits mean hardware.

### Fix 2: Update or roll back the named driver

Act on the identification.

1. **If the crash started after a driver update**: **Device Manager** > device > **Properties** > **Driver** > **Roll Back Driver**.
2. **Otherwise**: download the latest driver from the manufacturer and clean-install it. For Intel network/chipset drivers, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies exactly what you need.
3. For graphics-related files, do a full clean install from the GPU vendor (NVIDIA/AMD/Intel) using the installer's clean-install option.
4. Restart and stress-test with the workload that triggered the crash before considering it fixed.

### Fix 3: Boot into Safe Mode to confirm it's a driver

Validate the driver theory before deeper work.

1. Reach recovery (interrupt boot three times), then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4**.
2. Stable in Safe Mode = third-party driver or startup software. Unstable in Safe Mode = system files or hardware (Fixes 5–6).
3. In Safe Mode, you can also uninstall the suspect driver entirely (**Device Manager** > **Uninstall device**) and let Windows install its inbox driver on reboot — a useful test of whether the vendor driver is the problem.
4. Check [Microsoft's support documentation](https://support.microsoft.com/en-us/windows) for the specific stop code parameters if you want the technical breakdown of the exception type.

### Fix 4: Remove conflicting software

Some crashes come from programs, not drivers per se.

1. Uninstall recently added system utilities: third-party antivirus, VPN clients, disk tools, RGB/fan control software — these install kernel drivers.
2. Use each vendor's complete removal tool where available; standard uninstalls often leave filter drivers behind.
3. Perform a clean boot (`msconfig` > hide Microsoft services > disable all; **Task Manager** > disable startup apps) and re-enable in halves to isolate the offender.
4. Keep Windows Defender active during testing so you're never unprotected.

### Fix 5: Repair system files

Rule out corrupted Windows components amplifying the problem.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`, then SFC once more.
3. Restart and retest. Clean SFC/DISM results with continuing crashes point firmly at a driver or hardware — which is useful information, not a dead end.

### Fix 6: Test the RAM thoroughly

The essential hardware check for this stop code.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. For a deeper test, run MemTest86 from a USB stick overnight — Windows Memory Diagnostic is good, MemTest86 is definitive.
3. If errors appear: power down, reseat the sticks, and test one stick at a time in the primary slot to isolate the bad one.
4. Also reset any XMP/DOCP memory profiles to stock speeds in the BIOS — aggressive memory timings cause exactly this class of exception, and "stable for months" RAM can degrade into instability.

### Fix 7: Reset overclocks and update the BIOS

Stabilize the platform underneath the drivers.

1. Reset CPU, GPU, and RAM overclocks to stock — including "auto overclock" features in vendor utilities.
2. Check your laptop manufacturer's support page for a BIOS update; BIOS updates frequently fix memory-compatibility and power-delivery issues that surface as kernel exceptions.
3. Update the chipset driver from the laptop vendor alongside the BIOS — the two work as a pair.
4. After stabilizing, reintroduce changes one at a time if you insist on overclocking, testing for a full day between changes.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is one of the more diagnosable blue screens because it usually names its culprit. The workflow that works is: read the filename, fix that driver (update or roll back), and if the filename keeps changing, test the RAM — varying culprits are hardware's signature. The expensive mistake is reinstalling Windows while a bad RAM stick or a buggy driver version remains; both survive reinstallation untouched. Identify, fix, verify under load, and this stop code becomes a one-time incident rather than a recurring nightmare. For the trap-based sibling of this error, our [unexpected kernel mode trap guide](/articles/how-to-fix-unexpected-kernel-mode-trap-after-windows-11-update/) follows the same diagnostic discipline.
