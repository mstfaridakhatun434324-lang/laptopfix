---
title: "Fix the DRIVER_OVERRAN_STACK_BUFFER Blue Screen After a Windows 11 Update"
slug: how-to-fix-driver-overran-stack-buffer-after-windows-11-update
date: 2026-09-19
categories: ["windows-errors"]
tags: ["driver overran stack buffer", "blue screen", "windows 11 update"]
description: "Fix the DRIVER_OVERRAN_STACK_BUFFER blue screen after a Windows 11 update: identify the faulty driver, roll back the bad update, and end the crash loop."
thumbnail: "/images/thumbs/how-to-fix-driver-overran-stack-buffer-after-windows-11-update.webp"
faqs:
  - q: "What does DRIVER_OVERRAN_STACK_BUFFER mean?"
    a: "It means a driver wrote data past the end of its stack-based buffer — a classic buffer overflow in kernel code. Windows detects the corrupted stack and crashes with stop code 0x000000F7 rather than let the bad driver keep running. It is almost always a driver bug, not broken hardware."
  - q: "Can I just ignore it if it only happened once?"
    a: "A single crash after an update can be a one-off glitch, but two or more crashes point to a genuinely incompatible driver. Update or roll back your drivers now, because a driver that overruns its stack can corrupt data or crash again at the worst moment."
  - q: "Which drivers most often cause this error?"
    a: "Graphics drivers, network drivers (Wi-Fi and Ethernet), and third-party antivirus filter drivers are the usual suspects. Anything that was updated within days of the crash deserves a close look first."
  - q: "Will reinstalling Windows fix DRIVER_OVERRAN_STACK_BUFFER?"
    a: "A clean install usually clears it because it replaces every driver with a fresh set. But it is a last resort — identifying and replacing the single bad driver fixes the problem in minutes without wiping your files."
---

A DRIVER_OVERRAN_STACK_BUFFER blue screen right after a Windows 11 update is Windows catching a driver red-handed. One of your drivers wrote past the end of its memory buffer, corrupted the stack, and Windows shut everything down with stop code 0x000000F7 rather than let the damage spread. The good news: the update usually just exposed a driver that was already buggy.

This is a very fixable crash. The update swapped in a new kernel or a new driver version, and one driver in the chain could not keep up. Your job is to find that driver, replace it with a good version, and confirm the system is stable again.

## Why this happens

- **A driver was already buggy:** The update did not create the bug; it changed timing or memory layout so an existing buffer overflow in the driver finally trips Windows' stack protection.
- **A new driver version shipped with the update:** Windows Update sometimes bundles driver updates, and the new version may contain a regression the old one did not.
- **Third-party antivirus filter drivers:** Security software hooks deep into the kernel. After a major update, an outdated filter driver is a prime candidate for stack corruption.
- **Overclocking or memory instability:** Unstable RAM can corrupt stack contents in ways that look exactly like a driver overrun. If you run XMP or manual overclocks, suspect them.
- **Corrupted driver files:** A partially downloaded or badly installed driver from the update can behave unpredictably even if the driver version itself is fine.
- **Conflicting virtualization drivers:** VPN clients, virtual machine software, and some USB utilities install kernel drivers that clash with updated Windows components.

- **Firmware memory protections toggled off:** Some BIOS setups let you disable stack-protection features while tweaking. With those guards off, a driver overrun crashes harder instead of being contained.
## How to fix it

Work through these in order — start with the most likely cause and move down.

### Fix 1: Boot into Safe Mode and check what changed

1. Hold **Shift** while clicking **Restart** from the login screen to reach the recovery environment.
2. Go to **Troubleshoot → Advanced options → Startup Settings → Restart**, then press **4** for Safe Mode.
3. If the laptop is stable in Safe Mode, a third-party driver is the culprit — Safe Mode loads only Microsoft's core drivers.
4. Open **Settings → Windows Update → Update history** and note the most recent driver updates and their dates. This list is your suspect lineup for the next steps. The general [blue screen troubleshooting process](/articles/how-to-fix-blue-screen-of-death-windows-11/) follows the same isolate-and-test logic.

### Fix 2: Roll back the most recently updated driver

1. In Safe Mode (or normal mode if the system stays up), open **Device Manager** — right-click **Start** and select it.
2. Expand **Display adapters**, right-click your graphics device, and choose **Properties → Driver → Roll Back Driver**. Do the same under **Network adapters** for Wi-Fi and Ethernet.
3. If the roll-back button is greyed out, choose **Uninstall device** instead, tick **Attempt to remove the driver for this device**, and restart — Windows will install its built-in driver.
4. Use the laptop normally for a day. If the crashes stop, you found the bad driver — get a stable version from the manufacturer's site instead of Windows Update.

### Fix 3: Remove the problematic Windows update temporarily

1. Open **Settings → Windows Update → Update history → Uninstall updates**.
2. Find the most recent quality or driver update (sort by install date) and uninstall it.
3. Restart and test. If the system stabilizes, the update itself triggered the incompatibility.
4. Go to **Settings → Windows Update** and pause updates for a week or two, then install them again once the driver vendor has shipped a fix. Manually grabbing the update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) later lets you control exactly what gets installed.

### Fix 4: Update the prime suspects from official sources

1. Download the latest graphics driver directly from NVIDIA, AMD, or Intel rather than Windows Update — use [Intel's driver update tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics and chipsets.
2. Get the newest Wi-Fi and Bluetooth drivers from your laptop manufacturer's support page (Dell, HP, Lenovo, ASUS, or Acer).
3. Update your antivirus to the latest version, or temporarily uninstall it and rely on Microsoft Defender while testing — an outdated filter driver is a classic 0xF7 trigger.
4. Restart after each major driver change so you know which one made the difference.

### Fix 5: Run System File Checker and DISM

1. Open an elevated Command Prompt: right-click **Start → Terminal (Admin)**.
2. Run `sfc /scannow` and let it finish — this repairs corrupted Windows system files the update may have left behind.
3. If SFC reports unfixable damage, run `DISM /Online /Cleanup-Image /RestoreHealth`, then run `sfc /scannow` again.
4. Restart and use the laptop normally. Corrupted system binaries can masquerade as driver faults, so this step is worth the ten minutes.

### Fix 6: Test your memory

1. Press **Win + R**, type `mdsched.exe`, and press Enter to open Windows Memory Diagnostic.
2. Choose **Restart now and check for problems**.
3. Let the standard test complete (about 15–30 minutes). Memory errors show up clearly at the end.
4. If errors appear, reseat the RAM modules if your laptop allows access, or disable any XMP/memory overclock in the BIOS and retest. Bad RAM corrupts stacks exactly like a buggy driver does, so do not skip this if the crashes continue after driver work.

### Fix 7: Use Driver Verifier to catch the guilty driver (advanced)

1. Only do this after backing up important files — Driver Verifier intentionally crashes the system when it catches bad behavior.
2. In an elevated Command Prompt, run `verifier /standard /all` and restart.
3. Use the laptop until it crashes; the blue screen or the memory dump will name the offending driver file (often a `.sys` name).
4. Boot into Safe Mode, run `verifier /reset`, then update or remove the named driver.
5. Read the dump with Microsoft's WinDbg if you want confirmation — our [dump-reading guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through it step by step.

### Fix 8: Update the BIOS and reset firmware settings

Firmware-level memory protections work together with Windows' stack cookies. A stale BIOS can undermine them, so bring firmware current and reset any experimental tweaks.

1. Press **Win + R**, type `msinfo32`, and note your **BIOS Version/Date**.
2. Compare it with the latest release on your laptop maker's support page for your exact model.
3. Install the BIOS update while plugged into AC power — do not interrupt it for any reason.
4. Enter the BIOS setup and choose **Load Optimized Defaults** to clear experimental memory or CPU tweaks, then save and exit.
5. Use the laptop for several days. If the 0xF7 crashes are gone, a firmware setting was contributing.

## Closing

DRIVER_OVERRAN_STACK_BUFFER looks alarming, but it is one of the most honest blue screens Windows produces — it is telling you a specific driver did something wrong, and the evidence points at the fix. Start with Safe Mode isolation and driver rollbacks, work through updates and memory testing, refresh the BIOS, and use Driver Verifier only if the crashes refuse to name themselves. Replace that one bad driver and the crash loop ends with it.
