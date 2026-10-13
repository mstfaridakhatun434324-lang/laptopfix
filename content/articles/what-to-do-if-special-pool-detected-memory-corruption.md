---
title: "SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION: What to Do Next"
slug: what-to-do-if-special-pool-detected-memory-corruption
date: 2026-09-06
categories: ["windows-errors"]
tags: ["bsod", "memory-corruption", "windows-11"]
description: "SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION means Windows caught a driver writing where it shouldn't. Here's exactly what to do next."
thumbnail: "/images/thumbs/what-to-do-if-special-pool-detected-memory-corruption.webp"
faqs:
  - q: "What does SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION mean?"
    a: "It is a blue screen stop code (0x000000C1) that fires when Driver Verifier's special pool feature catches a driver writing outside its allocated memory. It means a specific driver is corrupting kernel memory — it names the culprit rather than the symptom."
  - q: "Is my RAM broken if I see this error?"
    a: "Usually not. This error specifically implicates a driver, not the physical memory. RAM failure is possible but unlikely; run a memory test to be thorough, but focus your effort on identifying and updating the bad driver first."
  - q: "Why did Driver Verifier turn itself on?"
    a: "It usually did not turn itself on. Someone — or some troubleshooting guide — likely ran the verifier command to diagnose another blue screen, and it is still active. You can check and disable it by running verifier /query in an elevated Command Prompt."
  - q: "Should I leave Driver Verifier running after the fix?"
    a: "No. Once you have identified and fixed the offending driver, disable Verifier. Running it permanently slows the system and can crash it on purpose, since that is its entire job — to stress drivers until they break."
---

`SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION` is one of the more informative blue screens you can get. Stop code `0x000000C1` means Driver Verifier — Windows' built-in driver stress-tester — caught a driver writing to memory it did not own. In plain terms: a specific driver is corrupting kernel memory, and Windows crashed on purpose to stop it.

If you are seeing this, someone (maybe you, following another guide) enabled Driver Verifier to hunt down a previous crash, and it did its job. Now you need to identify the bad driver, fix or remove it, and turn Verifier back off.

## Why this happens

- **A driver writes past its memory allocation.** The classic cause — a buggy driver overruns its buffer, and Verifier's special pool catches the overflow red-handed.
- **Driver Verifier is still running from a previous troubleshooting session.** It may have been enabled weeks ago and forgotten, and now it is crashing the system every time the buggy driver loads.
- **A recently updated driver introduced a memory bug.** New driver versions occasionally ship with pool-corruption bugs, especially beta or optional updates.
- **Third-party security or disk tools.** Antivirus filters, disk encryption, and backup tools run at kernel level and are frequent offenders in Verifier-caught crashes.
- **Corrupted driver installation.** A partially installed or mismatched driver (wrong version for the hardware) can write to invalid addresses.
- **Rarely: failing RAM or storage.** A hardware fault can mimic driver corruption, so do not skip the memory test if driver fixes change nothing.

## How to fix it

Work through these in order, from least to most invasive. The goal is to find the bad driver first, fix it, then disable Verifier.

### Fix 1: Identify the crashing driver from the minidump

Verifier crashes leave a minidump that usually names the offender, so read it before changing anything.

1. Press `Win + R`, type `%SystemRoot%\Minidump`, and press **Enter**.
2. Look for the most recent `.dmp` file matching your crash time.
3. Download and install **WinDbg Preview** from the Microsoft Store (it is free and made by Microsoft).
4. Open the dump in WinDbg, type `!analyze -v` in the command box, and press **Enter**.
5. Look for the `MODULE_NAME` and `IMAGE_NAME` lines — they typically name the exact `.sys` file responsible, such as `rtwlane.sys` (Realtek Wi-Fi) or `nvlddmkm.sys` (NVIDIA).
6. If you cannot read dumps comfortably, our [DRIVER_VERIFIER_DETECTED_VIOLATION guide](/articles/how-to-fix-driver-verifier-detected-violation-youtube/) walks through the same process with screenshots in mind.

### Fix 2: Update or reinstall the identified driver

Once you know the `.sys` file, fix that specific driver rather than updating everything blindly.

1. Match the file name to its device — for example, `rtwlane.sys` is the Realtek wireless adapter, visible under **Network adapters** in Device Manager.
2. Open **Device Manager**, right-click the device, and choose **Update driver** > **Search automatically for drivers**.
3. If that does not help, download the newest driver from the laptop maker's support page and install it manually.
4. If the crash started right after a driver update, go to the device's **Properties** > **Driver** tab and use **Roll Back Driver** instead.
5. For a corrupted install, right-click the device, choose **Uninstall device**, check **Attempt to remove the driver**, restart, and let Windows reinstall it fresh.

### Fix 3: Remove conflicting kernel-level software

If the dump points at an antivirus filter, VPN driver, or disk tool, the software itself may need to go.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall the program whose driver appeared in the crash dump.
3. Use the vendor's official removal tool if offered — ordinary uninstalls sometimes leave kernel drivers behind.
4. Restart and let the system run for a day without that software to confirm the crashes stop.
5. Only reinstall it after confirming a newer, fixed version is available from the vendor.

### Fix 4: Run SFC and DISM to rule out system corruption

Driver files themselves can be corrupted by a bad update or a failing drive sector.

1. Open an elevated Command Prompt (**Start** > type `cmd` > right-click **Command Prompt** > **Run as administrator**).
2. Run `sfc /scannow` and let it finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
4. Restart. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents both tools if you want the official reference.

### Fix 5: Test your memory

Driver corruption is the likely cause, but a failing RAM stick can produce identical-looking crashes, so test to be sure.

1. Press `Win + R`, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems** and let the full pass complete.
3. Check the results in **Event Viewer** > **Windows Logs** > **System** for `MemoryDiagnostics-Results`.
4. If errors appear, isolate the bad stick (test one at a time on laptops with two slots) and replace it. The memory-testing steps in our [MEMORY_MANAGEMENT stop code guide](/articles/how-to-fix-stop-code-memory-management-on-dell-laptop/) apply here too.

### Fix 6: Disable Driver Verifier once the cause is fixed

Verifier has done its job — now turn it off so it stops stressing drivers and crashing the machine on purpose.

1. Open an elevated Command Prompt.
2. Type `verifier /query` to confirm it is running and see which drivers are monitored.
3. Type `verifier /reset` to disable it, then restart the laptop.
4. After the reboot, run `verifier /query` once more to confirm no drivers are under verification.
5. Use the laptop normally for several days. If crashes return with Verifier off, the underlying driver problem was not fully fixed — go back to Fix 2.

### Fix 7: Update the BIOS and chipset drivers

Outdated firmware and chipset packages can make even correct drivers misbehave at the kernel level.

1. Visit your laptop manufacturer's support page and download the latest BIOS/UEFI and chipset drivers for your exact model.
2. Install the chipset package first, then the BIOS — keep the charger plugged in during the BIOS flash.
3. Reset any BIOS overclock or aggressive memory settings to defaults.
4. Restart and monitor for a few days.

## Closing

`SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION` is actually good news in disguise: Driver Verifier caught the exact driver misbehaving instead of leaving you guessing. Read the minidump, fix or replace that driver, and then remember to turn Verifier off with `verifier /reset`. Do that, and this particular blue screen should not come back.
