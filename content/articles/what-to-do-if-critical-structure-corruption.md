---
title: "CRITICAL_STRUCTURE_CORRUPTION: What to Do About It"
slug: what-to-do-if-critical-structure-corruption
date: 2026-09-07
categories: ["windows-errors"]
tags: ["critical-structure-corruption", "bsod", "driver"]
description: "CRITICAL_STRUCTURE_CORRUPTION means a driver corrupted critical kernel code or data. Here is exactly what to do, starting with the driver hunt."
thumbnail: "/images/thumbs/what-to-do-if-critical-structure-corruption.webp"
faqs:
  - q: "What does CRITICAL_STRUCTURE_CORRUPTION mean?"
    a: "Stop code 0x109 fires when Windows detects that critical kernel code or data — the kind the system cannot run without — has been modified or corrupted. PatchGuard (Kernel Patch Protection) on 64-bit Windows catches unauthorized modifications; drivers corrupting structures trigger it the same way. Either way, something wrote where it must not."
  - q: "Is this always caused by malware or rootkits?"
    a: "No — that is the scary interpretation, but ordinary buggy drivers cause it far more often. Antivirus drivers, virtualization software, and gaming anti-cheat drivers all operate at the level where their bugs trip this check. Scan for malware once to rule it out, then focus on drivers."
  - q: "Can overclocking cause CRITICAL_STRUCTURE_CORRUPTION?"
    a: "Yes. Unstable CPU or RAM overclocks corrupt kernel structures in transit, and PatchGuard cannot distinguish corruption-by-overclock from corruption-by-driver. Reset to stock speeds early in troubleshooting — it is a two-minute test that rules out a whole category."
  - q: "Will reinstalling Windows fix it?"
    a: "Only if the cause is software corruption rather than a specific third-party driver you will just reinstall afterward. A clean install that brings back the same buggy driver brings back the same crash. Identify the driver first; reinstall Windows only when the system itself is damaged beyond SFC/DISM repair."
---
CRITICAL_STRUCTURE_CORRUPTION (stop code 0x109) is Windows finding its most protected kernel structures damaged — the code and data it guards with PatchGuard precisely because nothing should ever touch them. Something did. CRITICAL_STRUCTURE_CORRUPTION (stop code 0x109) is Windows finding its most protected kernel structures damaged — the code and data it guards with PatchGuard precisely because nothing should ever touch them. Something did.

That something is usually a driver with a bug, occasionally bad RAM, rarely malware. What you do about it is a driver hunt plus a hardware sanity check, in that order. That something is usually a driver with a bug, occasionally bad RAM, rarely malware. What you do about it is a driver hunt plus a hardware sanity check, in that order — about an hour of focused work.

## Why this happens

- **A buggy kernel-level driver.** Antivirus, anti-cheat, virtualization, and VPN drivers operate where their bugs trip this check.
- **Bad RAM.** Memory corruption damages kernel structures directly, indistinguishable from a driver bug in the dump.
- **Unstable overclock.** Corrupted execution corrupts the very structures PatchGuard verifies.
- **Rootkit or bootkit malware.** Malicious kernel patching is exactly what PatchGuard was built to catch.
- **Corrupted system files.** Damaged kernel binaries fail their own integrity checks.
- **Driver conflict after a feature update.** New kernel layouts break old drivers' assumptions about structure locations.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Scan for rootkits and malware first

This is the one stop code where malware is a first-class suspect — rule it out early. This is the one stop code where malware is a first-class suspect — rule it out early with the offline scan, which catches rootkits that hide from in-Windows scanners.

1. Run a **Full scan** in **Windows Security > Virus & threat protection > Scan options**.
2. Then run the **Microsoft Defender Offline scan**, which boots into a clean environment where rootkits cannot hide.
3. If anything is found and removed, restart and monitor — a cleaned rootkit often ends the crashes immediately.

### Fix 2: Reset overclocks to stock

Two minutes that eliminates an entire cause category. Two minutes that eliminates an entire cause category — PatchGuard cannot distinguish overclock corruption from driver corruption, so stock speeds remove the ambiguity.

1. Load optimized defaults in BIOS/UEFI.
2. Remove Intel XTU, Ryzen Master, Afterburner, or ThrottleStop settings — uninstall the tools temporarily.
3. Disable XMP/EXPO. Test for a few days at full stock before concluding anything.

### Fix 3: Identify the driver with Driver Verifier

Verifier catches the corrupting driver at the moment of corruption. Verifier catches the corrupting driver at the moment of corruption — anti-cheat and virtualization drivers deserve special suspicion for this stop code.

1. Run `verifier`, create custom settings with **Special pool** enabled.
2. Select all non-Microsoft drivers and restart.
3. Use the PC until it crashes, then read the dump in WinDbg Preview (`!analyze -v`) for the IMAGE_NAME.
4. Update, roll back, or remove that driver — anti-cheat and virtualization drivers deserve special suspicion. Run `verifier /reset` when done.

### Fix 4: Update or remove the suspect

Act on the Verifier evidence. Act on the Verifier evidence: update the driver, try the previous version if already current, or remove the product if no fixed version exists.

1. Update the driver from its vendor; if already current, try the previous version.
2. For anti-cheat drivers (game-specific), update the game — the driver ships with it.
3. For virtualization products, update to the latest release; old versions clash with new Windows kernels.
4. If no update exists and crashes persist, uninstall the product and test without it.

### Fix 5: Test the RAM

When Verifier implicates different drivers across crashes, the corruption source is hardware. When Verifier implicates different drivers across crashes, the corruption source is hardware — the RAM test is the definitive check.

1. Run `mdsched.exe` > **Restart now and check for problems**.
2. Follow with overnight MemTest86 if the quick test is clean but crashes continue.
3. Replace failing sticks. Our [memory management walkthrough](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) details RAM isolation.

### Fix 6: Repair Windows and check the drive

The final software layer — for further reading on these repair commands, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows). Corrupted kernel binaries fail their own integrity checks — SFC and DISM repair them, and chkdsk verifies the disk underneath.

1. Elevated prompt: `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. `chkdsk C: /f /r` with a reboot for the full scan.
3. If corruption keeps reappearing after repair, suspect the drive — `wmic diskdrive get status` and the maker's SMART tool confirm. For related kernel-structure crashes, see our [kernel security check guide](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/).

### Fix 7: Disable virtualization-based features temporarily as a test

Hyper-V, Memory integrity, and virtualization-based security change how kernel structures are guarded — a buggy driver that trips PatchGuard may behave under different settings, which is diagnostic.

1. Go to **Windows Security > Device security > Core isolation** and toggle **Memory integrity** off temporarily.
2. Test for a few days. If crashes stop, a driver is incompatible with HVCI — identify it via the incompatible-driver message or Verifier, and update it.
3. Re-enable Memory integrity afterward — leaving it off permanently trades real security for a workaround.
4. Similarly, if you run Hyper-V or WSL2, test with virtualization features disabled to isolate hypervisor-adjacent drivers.

## Closing

CRITICAL_STRUCTURE_CORRUPTION sounds like the system is falling apart, but it is usually one driver writing where it should not — find it with Verifier, fix it, and move on. Scan for malware once, reset any overclocks, and let the evidence name the driver instead of guessing. PatchGuard crashes feel ominous because the protected structures sound vital — they are, but the cause is usually mundane. Hunt the driver, check the RAM, and this one resolves like any other.
