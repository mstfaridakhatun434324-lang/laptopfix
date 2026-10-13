---
title: "Fix the Windows 11 24H2 Blue Screen, Step by Step"
slug: how-to-fix-windows-11-24h2-blue-screen-step-by-step
date: 2026-09-25
categories: ["windows-update"]
tags: ["windows 11 24h2", "blue screen", "bsod", "crash fix"]
description: "Windows 11 24H2 blue-screening after the update? Follow this step-by-step repair: identify the faulty driver, roll back if needed, and stabilize the system."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-blue-screen-step-by-step.webp"
faqs:
  - q: "Why did Windows 11 24H2 give me a blue screen?"
    a: "The 24H2 update replaces core drivers and kernel components, and any driver that is incompatible with the new build can crash the system during or after the upgrade. Storage, graphics, and antivirus filter drivers are the usual culprits. The stop code on the blue screen — such as DRIVER_IRQL_NOT_LESS_OR_EQUAL — usually names the category, and the memory dump names the exact driver."
  - q: "Will a blue screen during the 24H2 update damage my files?"
    a: "Your personal files are almost always safe. If the crash happens during the upgrade, Windows automatically rolls back to the previous build with files intact. If it happens after a completed upgrade, the file system is not involved in the crash. Still, keep backups current — repeated hard crashes are never good for any storage device over time."
  - q: "How do I find which driver caused the blue screen?"
    a: "Check C:\\Windows\\Minidump for dump files, then analyze them with WinDbg or the free BlueScreenView utility, which highlights the faulting driver in red. The stop code on the blue screen itself also helps: search it with the driver name. In many 24H2 cases the dump points directly at a storage or graphics driver that needs updating."
  - q: "Should I roll back to 23H2 if 24H2 keeps blue-screening?"
    a: "If crashes persist after driver updates and repairs, rolling back within the 10-day window is reasonable: Settings, then System, then Recovery, then Go back. Use the rollback period to update the BIOS and drivers from the manufacturer, then retry 24H2 later. A permanent stay on 23H2 is not a plan, since it eventually leaves support."
---

A blue screen right after the Windows 11 24H2 update is alarming, but it follows a well-understood pattern. The new build loads new kernel components and expects drivers to keep up; when a storage, graphics, or filter driver cannot, the system crashes to protect itself. The stop code and the memory dump almost always identify the offender — this is a solvable problem, not a dead laptop.

The repair sequence matters. First, stabilize: get into Safe Mode, identify the faulting driver from the dump, and update or remove it. Then repair: fix system files and the update state. Only if crashes persist do you consider rolling back. Most 24H2 blue screens resolve at the driver step.

Work through this guide in order. Each step either fixes the crash or narrows the suspect list, so even partial progress moves you forward.

## Why this happens

- **Incompatible storage driver:** Old NVMe or SATA drivers crash under 24H2's updated storage stack, often during boot — the most common 24H2 BSOD.
- **Graphics driver mismatch:** The display driver from the old build loads against the new kernel and faults, producing crashes at login or under load.
- **Antivirus filter drivers:** Third-party security drivers that hook file operations can crash the new kernel; 24H2 tightened several kernel interfaces.
- **Corrupted upgrade state:** A partially applied update leaves mismatched system files that crash when loaded together.
- **Faulty RAM exposed:** The new build's memory management can expose marginal RAM that the old build tolerated, causing random stop codes.
- **BIOS too old:** Firmware bugs in power or TPM handling crash the new build's stricter initialization sequence.
- **Overheating under new power profiles:** 24H2's changed power management can push thermals differently, crashing an already-hot laptop. Brand-specific variants like the [Lenovo 24H2 blue screen fix](/articles/how-to-fix-windows-11-24h2-blue-screen-on-lenovo-laptop/) cover vendor driver packs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the stop code and dump

1. When the blue screen appears, photograph the screen — note the **stop code** (e.g., DRIVER_IRQL_NOT_LESS_OR_EQUAL) and any named file like `nvme.sys`.
2. Let the dump percentage reach 100% so Windows writes the minidump.
3. Boot into **Safe Mode**: hold Shift while clicking Restart, then Troubleshoot → Advanced options → Startup Settings.
4. In Safe Mode, open `C:\Windows\Minidump` and confirm a recent `.dmp` file exists.
5. Download **BlueScreenView**, open the dump, and note the driver highlighted in red — that is your prime suspect.

### Fix 2: Update the faulting driver first

1. Identify the driver from the dump analysis — commonly storage (`stornvme`, vendor NVMe), graphics, or network.
2. Go to your laptop manufacturer's support site and download the **latest 24H2-compatible** version of that exact driver.
3. In Safe Mode with Networking (or normal mode if stable), install the new driver.
4. If the dump names a third-party antivirus driver, uninstall that antivirus completely rather than updating it.
5. Restart normally and stress the system for 30 minutes. If the crash is gone, update the remaining drivers too — the [Dell 24H2 blue screen guide](/articles/how-to-fix-windows-11-24h2-blue-screen-on-dell-laptop/) shows the vendor-specific driver order.

### Fix 3: Roll back the graphics driver

1. Boot into Safe Mode and open **Device Manager**.
2. Expand **Display adapters**, right-click your GPU, and choose **Properties → Driver → Roll Back Driver** if available.
3. If rollback is unavailable, choose **Uninstall device** and check "delete the driver software" — Windows will load the basic display driver.
4. Restart and download the latest stable GPU driver from NVIDIA, AMD, or Intel — use the [NVIDIA driver page](https://www.nvidia.com/Download/index.aspx) or [AMD driver page](https://www.amd.com/en/support/download/drivers.html) as appropriate.
5. Install with the "clean install" option to remove all old driver remnants.

### Fix 4: Repair system files and the component store

1. Boot into Safe Mode with Command Prompt or open an admin Terminal.
2. Run `sfc /scannow` and wait for completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
4. Run `chkdsk C: /f` and approve the scan on next restart, then restart to run it.
5. These repairs fix the corrupted-upgrade-state crashes where mismatched system files fault together.

### Fix 5: Test the memory

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Let the Windows Memory Diagnostic complete — it takes 15–30 minutes.
3. If it reports errors, the RAM is faulty: reseat the modules if accessible, or test one stick at a time.
4. Faulty RAM causes random, changing stop codes — if your codes keep changing, suspect memory over drivers.
5. Replace failing modules; no software fix compensates for bad RAM.

### Fix 6: Update the BIOS

1. Note your current BIOS version from **System Information** (`msinfo32`).
2. Download the latest BIOS for your exact model from the manufacturer — many vendors released 24H2-specific firmware fixes.
3. Update with the charger connected, following the vendor instructions exactly.
4. Re-enable TPM and Secure Boot in firmware settings if the update reset them.
5. Boot normally and monitor. Firmware-level crashes (often WHEA_UNCORRECTABLE_ERROR) frequently vanish after this step.

### Fix 7: Roll back 24H2 as a controlled retreat

1. If crashes persist after all driver and firmware updates, go to **Settings → System → Recovery**.
2. Click **Go back** next to the previous Windows version — available for 10 days after the upgrade.
3. Choose a reason and let the rollback complete; your files and apps are preserved.
4. On the old build, update **every** driver and the BIOS from the manufacturer, since the vendor may have released 24H2-ready versions meanwhile.
5. Retry 24H2 in a few weeks via the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), or follow the official recovery guidance on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

A 24H2 blue screen is the system telling you exactly what is wrong — in the stop code and the dump. Read that evidence, update the named driver, repair the system files, and check the firmware, in that order. The vast majority of these crashes end at the driver step, and the laptop that emerges is more stable than the one that went into the upgrade.
