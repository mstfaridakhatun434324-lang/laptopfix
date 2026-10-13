---
title: "Fix REFERENCE_BY_POINTER BSOD on Your ASUS Laptop"
slug: how-to-fix-reference-by-pointer-bsod-on-asus-laptop
date: 2026-09-16
categories: ["windows-errors"]
tags: ["blue screen", "reference by pointer", "asus laptop", "bsod fix"]
description: "REFERENCE_BY_POINTER crashing your ASUS laptop? Find the driver with the reference-count bug and fix it with these targeted steps."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-on-asus-laptop.webp"
faqs:
  - q: "What is a REFERENCE_BY_POINTER blue screen?"
    a: "Windows tracks kernel object usage with reference counts. Bugcheck 0x18 means a driver decremented a count too many times — a coding bug in the driver. Windows crashes on purpose to stop the resulting corruption from spreading. The minidump normally identifies the faulty driver, which makes this one of the more straightforward blue screens to diagnose."
  - q: "Can Armoury Crate cause REFERENCE_BY_POINTER?"
    a: "It has been implicated. Armoury Crate installs kernel-level services for power profiles, fan control, and lighting, and bugs in those components can produce reference-count errors. If crashes correlate with Armoury Crate updates or profile switching, update it first, then test with it uninstalled."
  - q: "Why do the dumps blame different drivers each time?"
    a: "That's the classic sign the drivers are innocent and something is corrupting memory underneath them — usually bad RAM. A single consistent driver across dumps means a driver bug; a rotating cast means test the memory. Run MemTest86 overnight to settle it."
  - q: "Is this related to overclocking?"
    a: "Indirectly. Unstable CPU or RAM overclocks corrupt kernel data structures, which can manifest as reference-count errors blamed on random drivers. If you're running XMP/EXPO or any overclock, disable it and retest before blaming drivers — especially on ASUS gaming laptops where overclocking is common."
---

Stop code 0x18 — REFERENCE_BY_POINTER — means a driver told Windows it was done with a kernel object once too often. The reference count broke, Windows noticed, and the system stopped before the corruption could cascade. It's a driver bug with a paper trail: the crash dump usually names the offender outright. That paper trail is what makes this guide short on guesswork.

On ASUS laptops, Armoury Crate's kernel services join the usual lineup of antivirus filters and network drivers as suspects. Here's the full diagnostic path.

## Why this happens

- **Buggy third-party driver.** Antivirus filters, VPN clients, and disk tools with reference-counting defects.
- **Armoury Crate kernel services.** Power, fan, and lighting services operating at kernel level with occasional reference bugs.
- **Network driver bugs.** Wi-Fi drivers mishandling object lifetimes across power transitions.
- **Recent driver update.** A new version introducing the bug — check what changed when crashes began.
- **Corrupted driver binaries.** Damaged files behaving differently from their tested code.
- **Unstable overclock corrupting kernel structures.** XMP/EXPO or CPU overclocks producing errors blamed on innocent drivers.
- **Bad RAM.** The rotating-suspects pattern — different driver blamed on each dump.
- **MyASUS background services.** Like Armoury Crate, MyASUS installs services that operate at system level and have been linked to reference-count crashes.
- **RGB and peripheral utilities.** Lighting-control software with kernel drivers is a surprising but documented source of 0x18 on gaming laptops.

## How to fix it

Work through these in order — identify, fix, verify.

### Fix 1: Read the dump and note the pattern

The pattern matters as much as the name. This is the most important diagnostic step in the whole guide: a consistent culprit means a driver bug you can fix, while rotating culprits mean hardware or overclock instability underneath. Don't skip the pattern check.

1. Ensure minidumps are enabled: **Advanced system settings > Startup and Recovery > Settings > Small memory dump**.
2. Open the latest dumps in `%SystemRoot%\Minidump` with WinDbg Preview; run `!analyze -v` on each.
3. Same driver every time = driver bug (continue below). Different drivers each time = skip to Fix 7 (RAM/overclock) — that's memory corruption.
4. Write down the consistent culprit's **MODULE_NAME**.

### Fix 2: Update the driver from ASUS or the vendor

Get the validated fix.

1. For ASUS-shipped hardware, download the latest driver for your exact model from ASUS's official support page.
2. For GPUs, use [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) directly, with clean-install options.
3. Install, restart, and test for several days under normal workloads.

### Fix 3: Update or test without Armoury Crate

ASUS-specific suspect, ASUS-specific test. Armoury Crate updates frequently include kernel-service fixes that never make the changelog headlines, so "latest" is worth verifying even if you updated last month.

1. Update Armoury Crate to the latest version — ASUS fixes these kernel-service bugs in updates.
2. If crashes persist, uninstall Armoury Crate completely from **Settings > Apps > Installed apps** and test for a few days.
3. Stable without it = Armoury Crate's services were the problem. Reinstall only the latest version if you need its features, or manage fans/power through Windows and BIOS instead.

### Fix 4: Roll back recent driver updates

When the timeline is clear, act on it.

1. In **Device Manager**, find the device, open **Properties > Driver**, and click **Roll Back Driver**.
2. Restart and confirm stability.
3. Decline that driver version in **Windows Update > Advanced options > Optional updates** until a newer build appears.

### Fix 5: Eliminate antivirus filter conflicts

The most common third-party cause of this bugcheck. Antivirus filters live at the exact layer where reference counts are managed, which is why they dominate this particular stop code.

1. Fully update the antivirus engine.
2. If the dump implicates it (or crashes continue), remove it with the vendor's cleanup tool and test on Windows Security.
3. Clean on Windows Security confirms the diagnosis — reinstall only the latest version afterward.

### Fix 6: Repair system files

Exclude binary corruption. Damaged driver files fail in ways the original code never would, so this step matters most on systems with a history of bad shutdowns or disk errors.

1. Run `sfc /scannow` in **Terminal (Admin)**, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart and retest. A driver that still crashes after clean reinstall + file repair has the bug in its code — try an older version.

### Fix 7: Disable overclocks and test RAM

For the rotating-suspects pattern. When every dump blames someone different, stop updating drivers — the drivers are victims, not culprits. Unstable memory or a bad stick is corrupting kernel structures underneath them.

1. Enter the BIOS and disable **XMP**/**EXPO** and any CPU overclock or undervolt.
2. Run `mdsched.exe` in **Extended** mode; for certainty, run MemTest86 overnight.
3. If crashes stop at stock speeds, the overclock was corrupting kernel structures. If MemTest86 finds errors, replace the RAM.

### Fix 8: Verify with a clean driver state

Confirm the fix holds.

1. After fixing, use the laptop normally for a full week — including gaming or heavy workloads if those triggered crashes.
2. Check **Event Viewer > Windows Logs > System** for warning patterns even without crashes.
3. For ongoing driver-management guidance, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

For the same error on other brands, see our [Dell](/articles/how-to-fix-reference-by-pointer-bsod-on-dell-laptop/) and [Acer](/articles/how-to-fix-reference-by-pointer-bsod-on-acer-laptop/) variants, the [24H2 version](/articles/how-to-fix-reference-by-pointer-bsod-in-windows-11-24h2/), or the [general guide](/articles/how-to-fix-reference-by-pointer-bsod-on-windows-11/).

## Closing

On ASUS machines, REFERENCE_BY_POINTER is usually one bad driver — sometimes wearing an Armoury Crate uniform. Read the dumps for the pattern, fix the consistent culprit, and check the overclock if the suspects keep changing. It's methodical work, but it ends with a stable laptop. Keep Armoury Crate updated but don't let it auto-update drivers silently — review what changes so you can connect a new crash to its cause.
