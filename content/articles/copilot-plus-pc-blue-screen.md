---
title: "How to Fix Blue Screen Errors on Your Copilot+ PC"
slug: copilot-plus-pc-blue-screen
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "blue screen", "bsod", "windows 11", "troubleshooting", "ai pc"]
description: "Blue screens crashing your Copilot+ PC? Learn the common causes on Snapdragon and Intel AI laptops and follow step-by-step fixes to stop them for good."
thumbnail: "/images/thumbs/copilot-plus-pc-blue-screen.webp"
faqs:
  - q: "Do Copilot+ PCs blue screen more often than regular laptops?"
    a: "They can in a chip generation's first year, because drivers for platforms like Snapdragon X and Intel Core Ultra are still maturing. As updates roll out, crash rates settle. Most BSODs trace back to drivers, not defective hardware."
  - q: "How do I find out what caused a blue screen on my Copilot+ PC?"
    a: "Start with the stop code on the blue screen — photograph it before the machine reboots. Then open Reliability Monitor or Event Viewer to find the BugCheck entry with the exact code and the driver named in the crash."
  - q: "Will resetting Windows 11 fix recurring blue screens?"
    a: "A reset often helps with driver or system-file corruption, since it replaces the whole driver stack with fresh versions. But if Windows Update reinstalls the same faulty driver, crashes can return. Diagnose first, and pause driver updates afterward if needed."
  - q: "Can overheating cause blue screens on a Copilot+ PC?"
    a: "Yes. Sustained heat can destabilize the CPU or GPU and trigger codes like WHEA_UNCORRECTABLE_ERROR, so keep vents clear during heavy AI workloads."
---

Nothing kills the "it just works" promise of a Copilot+ PC faster than a blue screen of death. One moment you are working, the next a cryptic stop code flashes past and the machine reboots — sometimes taking unsaved work with it. Once after an update is easy to shrug off; every day is a trust problem.

Copilot+ PCs have blue-screen triggers older laptops rarely see. Many run on brand-new chip platforms — Snapdragon X on ARM, Intel Core Ultra Series 2, AMD Ryzen AI 300 — whose drivers are still maturing, and the young NPU driver stack adds failure modes generic guides never mention. Instability sometimes shows up elsewhere first: if your machine drops its network connection before dying, read our guide on [Copilot+ PC Wi-Fi keeps disconnecting](/articles/copilot-plus-pc-wifi-disconnecting/) too, since a failing network driver can be the real culprit.

This guide walks you through the full diagnosis in order — reading the stop code, telling a driver crash from a hardware fault, and applying fixes from least to most disruptive, so you only reset Windows when it is actually necessary.

## Why this happens

- **Immature ARM64 drivers on Snapdragon X models:** Early Qualcomm graphics, Wi-Fi, and power drivers had kernel-crashing bugs. Updates fixed most, but a missed update can leave a crash-prone driver in place.
- **NPU driver instability:** The AI accelerator's driver stack is young across all three chip vendors, and a bad NPU driver can crash the system during AI workloads — related to the [NPU not detected in Windows 11](/articles/npu-not-detected-windows-11/) driver problems many owners report.
- **Windows 11 24H2 replacing working drivers:** Feature updates sometimes swap your stable OEM driver for a newer generic one.
- **Memory faults:** A marginal RAM stick surfaces under load, producing codes like MEMORY_MANAGEMENT or IRQL_NOT_LESS_OR_EQUAL.
- **Corrupted system files:** Interrupted updates or bad shutdowns damage Windows components the kernel depends on.
- **Overheating under sustained AI loads:** Long NPU or GPU sessions with blocked vents can overheat the SoC and cause WHEA_UNCORRECTABLE_ERROR crashes.
- **Conflicting third-party drivers:** VPN clients, antivirus filters, and old x86 peripheral drivers can clash with the ARM64 kernel on Snapdragon models.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the stop code and identify the failing driver

Every blue screen tells you what went wrong if you know where to look — never skip this.

1. Photograph the next blue screen and note the stop code (for example, DRIVER_IRQL_NOT_LESS_OR_EQUAL) and any driver file named at the bottom.
2. After rebooting, press Win + R, type `perfmon /rel`, and open Reliability Monitor.
3. In Event Viewer (Win + R, `eventvwr`), go to Windows Logs > System and filter for "BugCheck" to confirm the code.
4. If only one app dies while the system stays up, that is an app issue, not a system crash — see [Chrome crashing on ARM64 Windows](/articles/chrome-arm64-crashing-windows/) for that case.

### Fix 2: Update every driver from the right source

Most Copilot+ blue screens are driver bugs — and the fix is a correct driver update, never a random driver-updater tool.

1. Open Device Manager and check Display adapters, Network adapters, and System devices for yellow warning icons.
2. Visit your laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) and download the latest chipset, graphics, Wi-Fi, and NPU drivers for your exact model.
3. On Intel-based Copilot+ PCs, run the Intel Driver & Support Assistant to catch Intel graphics and Wi-Fi updates the OEM page may lag on.
4. Install chipset and NPU drivers first, then graphics, then network, rebooting after each group.

### Fix 3: Roll back the driver or update that started the crashes

If the blue screens began right after an update, the update itself is the prime suspect — undo it.

1. In Device Manager, right-click the suspect device, choose Properties, open the Driver tab, and use "Roll Back Driver" if it is clickable.
2. If the trigger was a Windows update, go to Settings > Windows Update > Update history > Uninstall updates and remove the most recent driver or cumulative update.
3. Pause updates for a few weeks (Windows Update > Advanced options) so the bad driver is not reinstalled immediately.
4. Report the bad driver to your laptop maker so the fixed version reaches you sooner.

### Fix 4: Test memory and repair system files

When no driver looks guilty, verify the kernel's two foundations: RAM and the Windows image.

1. Press Win + R, type `mdsched`, and choose "Restart now and check for problems" to run Windows Memory Diagnostic.
2. Let both passes finish; any error means the memory likely needs replacing under warranty.
3. In an admin Terminal, run `sfc /scannow`, then reboot.
4. If SFC reports unfixable corruption, run `DISM /Online /Cleanup-Image /RestoreHealth`, then run SFC again.
5. Run `chkdsk C: /f` in an admin Terminal, accept the reboot prompt, and let it scan the drive.

### Fix 5: Disable fast startup and try a clean boot

Fast startup and third-party startup software can load a crashing driver before you sign in — removing them isolates the problem.

1. Open Power Options > "Choose what the power buttons do" > "Change settings that are currently unavailable."
2. Uncheck "Turn on fast startup," save, and shut down fully (not restart) to clear the hibernated kernel state.
3. Press Win + R, type `msconfig`, go to the Services tab, check "Hide all Microsoft services," and click "Disable all."
4. In Task Manager > Startup apps, disable non-essential items and reboot.
5. If crashes stop, re-enable services in small groups until the culprit returns — then uninstall or update that program.

### Fix 6: Reset Windows 11 as a last resort

When diagnostics point to deep corruption and every targeted fix has failed, a fresh Windows image ends the uncertainty.

1. Back up your files to an external drive or OneDrive first.
2. Go to Settings > System > Recovery and click "Reset PC."
3. Choose "Keep my files," then "Cloud download" to fetch a clean Windows 11 image rather than reusing the damaged local one.
4. After setup, install drivers from your laptop maker's support page BEFORE running Windows Update.
5. If crashes persist after a clean reset, follow Microsoft's official blue screen troubleshooting guide — a hardware fault is likely and a warranty claim is the right move.

## Closing

Blue screens on a Copilot+ PC feel scarier than they are because the platform is new, but the diagnosis is the same one technicians have used for years: read the stop code, update or roll back drivers from trusted sources, verify memory and system files, and only reset Windows when the evidence points there. Get drivers from your laptop maker's page, and the blue screens become a one-time story instead of a daily ritual.
