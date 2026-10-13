---
title: "How Do I Fix the REFERENCE_BY_POINTER Blue Screen?"
slug: how-do-i-fix-reference-by-pointer-bsod
date: 2026-09-13
categories: ["windows-errors"]
tags: ["reference by pointer", "bsod fix", "stop code 0x18", "driver verifier", "windows 11"]
description: "Seeing REFERENCE_BY_POINTER blue screens? Here's the practical fix sequence — from removing filter drivers to catching the culprit with Driver Verifier."
thumbnail: "/images/thumbs/how-do-i-fix-reference-by-pointer-bsod.webp"
faqs:
  - q: "How do I fix REFERENCE_BY_POINTER quickly?"
    a: "The fastest wins: uninstall third-party antivirus and VPN software, then update your chipset, network, and graphics drivers. Those steps resolve most 0x18 crashes because filter drivers are the leading cause. If crashes continue, Driver Verifier identifies the exact guilty driver — that is the definitive step, not a guess."
  - q: "Do I need to reinstall Windows for this error?"
    a: "Almost certainly not. REFERENCE_BY_POINTER is a driver bug, and reinstalling Windows while the same buggy driver gets reinstalled afterward just reproduces the crash on a fresh system. Fix or remove the driver first; reserve reinstallation for cases where every driver avenue is exhausted."
  - q: "Why doesn't the blue screen name the driver?"
    a: "Because the corruption — a reference count decremented too many times — is usually detected long after the guilty driver made the bad call. The crash dump's stack trace may hint at it, but Driver Verifier is the reliable method: it crashes the driver at the moment of the violation, with its name attached."
  - q: "Can this blue screen damage my files?"
    a: "The crash itself doesn't target your files, but any unsaved work is lost when the system crashes, and repeated crashes increase the small risk of filesystem corruption. Run chkdsk after a crash streak, keep backups current, and fix the driver promptly rather than living with the crashes."
---

So you're staring at REFERENCE_BY_POINTER — stop code 0x18 — and wondering what to actually do about it. Here's the short version: a driver messed up its reference counting on a kernel object, Windows caught the impossible negative count, and crashed. Your job is to find which driver and either update it or remove it. The stop screen won't name it (the damage is discovered after the fact), so this is a two-phase job: clear the usual suspects first, then use Driver Verifier to get a name if needed.

This is the practical, do-this-now companion to our deeper [REFERENCE_BY_POINTER troubleshooting guide](/articles/troubleshoot-reference-by-pointer-bsod/) — same goal, tighter focus on action.

## Why this happens

- **Antivirus or VPN filter drivers.** The number-one cause — kernel filters mishandling object reference counts.
- **Virtual-device drivers.** Virtual audio, virtual cameras, emulators, and virtual disk tools.
- **Outdated hardware drivers.** Old network, storage, or peripheral drivers on new Windows 11 builds.
- **Corrupted driver installs.** Mixed-version driver files misbehaving in object management.
- **Conflicting drivers.** Two drivers managing the same device, double-releasing objects.
- **Faulty RAM.** Corrupting reference counts in memory, mimicking driver bugs.
- **System file corruption.** Damage to the kernel's object manager itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Strip out security and VPN filter drivers

The highest-probability move — do it before anything clever.

1. Uninstall your third-party antivirus using the vendor's complete removal tool.
2. Uninstall VPN clients and firewall utilities the same way.
3. Restart and run on Microsoft Defender for a few days of normal use.
4. If the crashes stop, you've found the category — reinstall only the latest version of what you actually need.
5. Don't stack security products; pick one real-time protector.

### Fix 2: Update the core driver set

Refresh the drivers most likely to contain the bug.

1. From your laptop maker's support page, install the latest **chipset**, **network**, **storage**, and **graphics** drivers.
2. Clean-install the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
3. On Intel systems, run the Intel Driver & Support Assistant for chipset and wireless updates.
4. Remove any third-party "driver updater" — a frequent source of the mismatched drivers behind 0x18.
5. Test for a few days before declaring victory; reference-count bugs can be intermittent.

If your crashes followed a Windows update, the dedicated guide is [how to fix REFERENCE_BY_POINTER BSOD after a Windows 11 update](/articles/how-to-fix-reference-by-pointer-bsod-after-windows-11-update/).

### Fix 3: Use Driver Verifier to name the driver

Stop guessing — get the name.

1. Create a **system restore point** first.
2. Run `verifier`, choose **Create custom settings**, enable **Special pool**, **Pool tracking**, **Force IRQL checking**.
3. **Select driver names from a list** → sort by **Provider** → check all **non-Microsoft** drivers → **Finish** → restart.
4. Use the PC normally until it crashes — Verifier will name the driver in the new stop screen.
5. In Safe Mode, run `verifier /reset` to disable it, then update or uninstall the named driver.

The 24H2-specific variant is covered in [how to fix REFERENCE_BY_POINTER BSOD in Windows 11 24H2](/articles/how-to-fix-reference-by-pointer-bsod-in-windows-11-24h2/).

### Fix 4: Remove virtual-device and utility software

Clear the second tier of usual suspects.

1. Uninstall virtual audio cables, virtual cameras, virtual drives, and emulators.
2. Remove RGB control, fan control, and "optimizer" utilities that install kernel drivers.
3. Disconnect unneeded USB devices and their companion software during testing.
4. Reinstall essentials one at a time, newest versions only.
5. If a specific peripheral's software correlates with crashes, check the vendor for a driver update before reinstalling.

### Fix 5: Check your memory

Rule out hardware mimicking a driver bug.

1. Run `mdsched.exe` → **Restart now and check for problems**.
2. Verify results in **Event Viewer > Windows Logs > System > MemoryDiagnostics-Results**.
3. Overnight MemTest86 for intermittent faults.
4. BIOS **Optimized Defaults** to clear unstable timings.
5. Inconsistent blame across crashes + clean Verifier = test RAM before anything else.

### Fix 6: Repair Windows' own files

Fix the object manager underneath the drivers.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending Windows updates.
3. If a specific KB preceded the crashes, look for a superseding fix in the Microsoft Update Catalog.
4. For deep corruption, an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (keep files and apps).
5. Reintroduce third-party drivers one group at a time afterward.

### Fix 7: Clean-boot to catch interactions

For crashes that survive everything above.

1. `msconfig` → hide Microsoft services → disable the rest; disable Startup apps; restart.
2. If stable, re-enable in halves until the crash returns.
3. Suspect interactions between two drivers (e.g., antivirus filter + VPN filter) rather than a single culprit — these compound failures are the hardest to find because each driver passes testing alone, and only the combination corrupts the reference counts.
4. Keep only the minimal driver set you genuinely need; every kernel driver you remove is one fewer suspect.
5. Document what you found — if it recurs after a future update, you'll know exactly where to look first.

## Closing

Fixing REFERENCE_BY_POINTER is a process of narrowing: strip the filter drivers, refresh the core driver set, and let Driver Verifier name whatever's left standing. It's tempting to skip to reinstalling Windows, but that's the one move guaranteed not to help if the same buggy driver comes back with the fresh install — you'd spend hours rebuilding the system only to watch the identical blue screen return on the first boot. The blue screen isn't telling you Windows is broken — it's telling you a driver can't count. Find the driver that can't count, update it or show it the door, and 0x18 stops appearing.
