---
title: "Fixing the ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY Blue Screen in Windows 11"
slug: attempted-execute-of-noexecute-memory-bsod-windows-11
date: 2026-10-10
categories: ["windows-errors"]
tags: ["blue screen", "noexecute memory", "windows 11", "dep", "stop code"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY crashing Windows 11? Understand this DEP-related stop code and fix it with 6 proven steps."
thumbnail: "/images/thumbs/attempted-execute-of-noexecute-memory-bsod-windows-11.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "Windows tried to run code from a memory region marked non-executable (stop code 0x000000FC). This is a Data Execution Prevention (DEP) violation — either a driver bug jumping to bad memory, or actual malicious code trying to execute. Either way, Windows crashes to stay safe."
  - q: "Is this blue screen caused by a virus?"
    a: "It can be — malware exploiting a vulnerability looks exactly like this to DEP. But buggy drivers are the more common cause. Run a full Defender scan to rule malware out, then focus on drivers, especially recently updated ones."
  - q: "Can RAM problems cause this error?"
    a: "Yes. Faulty RAM can corrupt pointers, sending execution to random addresses including non-executable regions. If driver fixes don't help, test your memory with mdsched.exe or MemTest86."
  - q: "What is DEP and should I turn it off?"
    a: "Data Execution Prevention marks data regions of memory as non-executable, blocking a whole class of exploits. You should NOT turn it off system-wide — it removes important protection. Fix the underlying driver instead."
---

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (stop code 0xFC) is Windows' Data Execution Prevention catching something red-handed. Modern CPUs mark regions of memory as either "code goes here" or "data goes here, never run it." When something tries to execute data — whether it's a confused driver jumping to a garbage address or actual exploit code — DEP kills the process, or in this case the whole system, on the spot.

The name is a mouthful, but the investigation is straightforward: it's a driver bug until proven otherwise, with malware and bad RAM as the backup suspects. Here's the order that finds the answer fastest.

## Why this happens

- **A driver jumps to an invalid address.** Corrupted function pointers in buggy drivers send execution into data regions — the classic 0xFC cause.
- **Outdated or mismatched drivers.** Old drivers on new Windows 11 builds (especially 24H2) hit changed memory layouts and crash.
- **Malware or exploit attempts.** DEP exists to stop exactly this; a genuine attack triggers the same stop code as a driver bug.
- **Faulty RAM.** Bad memory corrupts pointers, redirecting execution to non-executable pages randomly.
- **Corrupted system files.** Damage to kernel or driver files changes code paths in ways that trip DEP.
- **Incompatible antivirus or virtualization drivers.** Kernel hooks from security and VM software operate at the exact level where DEP violations occur.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Scan for malware with Defender Offline

Because this stop code can indicate an exploit attempt, check this first.

1. Open **Windows Security > Virus & threat protection > Scan options**.
2. Select **Microsoft Defender Offline scan** and click **Scan now**.
3. The system reboots into a clean environment and scans before Windows loads.
4. Remove anything found and restart.
5. If the scan is clean, move on — drivers are now your prime suspect.

### Fix 2: Update or roll back recently changed drivers

Driver bugs cause the majority of 0xFC crashes.

1. Think about what changed before crashes started — a driver update, Windows Update, or new hardware.
2. Open **Device Manager**, find recently updated devices, open **Properties > Driver**, and use **Roll Back Driver** where available.
3. For the GPU, do a clean reinstall from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. Update chipset and network drivers from your laptop manufacturer's support page.
5. Restart and test under the conditions that used to crash.

If the blue screen names a specific `.sys` file, prioritize that driver. Brand-specific variants of this crash are covered in our [ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on ASUS guide](/articles/how-to-fix-attempted-execute-of-noexecute-memory-on-asus-laptop/).

### Fix 3: Verify DEP is configured correctly

Make sure DEP itself hasn't been misconfigured.

1. Press **Windows + R**, type `sysdm.cpl`, and press Enter.
2. Go to **Advanced > Performance > Settings > Data Execution Prevention**.
3. Ensure **Turn on DEP for essential Windows programs and services only** is selected (the default).
4. If it was set to cover all programs and you're crashing in a specific app, that app may be incompatible — but don't blanket-disable DEP.
5. Click **OK** and restart.

Never select "Turn off DEP" equivalents via bcdedit (`nx AlwaysOff`) as a fix — it masks the symptom while removing exploit protection. For the broader update-related variant, see [ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY after a Windows 11 update](/articles/how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update/).

### Fix 4: Run SFC, DISM, and a memory test

Cover corrupted files and bad RAM together.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow` and restart.
3. Press **Windows + R**, type `mdsched.exe`, and run the memory diagnostic.
4. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
5. If crashes blame different drivers each time and memory shows errors, replace the faulty RAM — random 0xFC crashes are a textbook bad-memory symptom.

### Fix 5: Remove problematic security and virtualization software

Kernel-hooking software operates where DEP violations happen.

1. Uninstall third-party antivirus temporarily via **Settings > Apps > Installed apps**, testing on Microsoft Defender.
2. If you run VirtualBox, VMware, or similar, update them to the latest version — old virtualization drivers are known 0xFC triggers on Windows 11 24H2.
3. Disable **Memory integrity** temporarily to test (**Windows Security > Device security > Core isolation**) — if crashes stop, a driver is incompatible with HVCI and needs updating, not permanent disabling.
4. Re-enable Memory integrity after identifying the culprit.
5. Update or replace the incompatible software rather than leaving protection off.

### Fix 6: Check for Windows 11 24H2-specific issues

Some 0xFC clusters are build-specific.

1. Open **Settings > System > About** and note your **OS build**.
2. Check **Settings > Windows Update** and install all pending updates — Microsoft has shipped fixes for DEP-related crashes in cumulative updates.
3. If a specific update coincides with the crashes, check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a newer revision or a known-issue workaround.
4. As a last resort, an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) refreshes all system components.
5. Document the stop code and build number — if it's a genuine Microsoft bug, the Feedback Hub report helps get it fixed.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY looks exotic, but it's usually just a driver that lost its way in memory — with malware and bad RAM as the less common alternatives. Scan first (because DEP violations deserve that respect), then work the driver angle, and don't be tempted to disable DEP to make the crashes stop. The protection is doing its job; your task is to find what's tripping it.

If you've worked through all six fixes and still crash, capture the exact stop code parameters from the blue screen (the four hex values in parentheses) and note which driver the dump blames — that detail is what separates a ten-minute driver fix from a deeper hardware investigation. Either way, resist the urge to "fix" it by weakening Windows' memory protections; a system that crashes is telling you something, and a system with DEP disabled just stays silent while the real problem gets worse.
