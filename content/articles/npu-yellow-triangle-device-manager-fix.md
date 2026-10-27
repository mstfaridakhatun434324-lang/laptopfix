---
title: "How to Fix the NPU Yellow Triangle Warning in Device Manager"
slug: npu-yellow-triangle-device-manager-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["npu yellow triangle", "device manager", "npu warning", "copilot+ pc", "windows 11", "troubleshooting"]
description: "Fix the NPU yellow triangle warning in Device Manager on your AI PC with driver cleanup, chipset updates, BIOS checks, and conflict removal for Copilot+."
thumbnail: "/images/thumbs/npu-yellow-triangle-device-manager-fix.webp"
faqs:
  - q: "What does the yellow triangle on the NPU mean?"
    a: "It means Windows detected the NPU but cannot start it correctly, usually because of a driver problem, a resource conflict, or a missing supporting driver. The device is present, so this is more fixable than a missing NPU."
  - q: "Can I still use Copilot+ features with the yellow triangle?"
    a: "Usually not reliably. Some features may appear available but fail, run slowly on the CPU, or crash. Fix the warning first rather than working around it."
  - q: "Does the yellow triangle mean my NPU is broken?"
    a: "Rarely. It almost always means a driver or configuration fault. Hardware failure is only likely if the warning survives a clean driver install, BIOS update, and Windows repair."
  - q: "Why did the yellow triangle appear after a Windows Update?"
    a: "Windows Update often replaces a validated NPU or chipset driver with a generic one. Reinstalling your laptop maker's drivers usually clears the warning."
---

Device Manager shows your neural processing unit with a yellow triangle, and its status says the device cannot start or that a driver failed to load. Copilot+ features may stutter, fail, or fall back to the CPU, even though the NPU is clearly detected — unlike a missing device, Windows knows it is there.

That distinction matters. A yellow triangle means the hardware responded, but the software chain that starts it is broken: a bad driver, a missing chipset component, a resource conflict, or a damaged driver install. The fixes below repair that chain in order.

This guide gives you six fixes, from reading the exact error code to a clean driver and BIOS pass. Check the device status after each step so you know which fix cleared the warning.

## Why this happens

- **Wrong or generic NPU driver:** A driver for a different NPU model, or a generic Windows Update package, can load far enough to detect the device but not far enough to start it.
- **Missing or outdated chipset driver:** The NPU depends on chipset services to initialise; without them, Windows flags the NPU even when its own driver is correct.
- **Driver install interrupted or corrupted:** A partial install leaves mismatched driver files that Windows cannot reconcile, producing a persistent start failure.
- **Resource or device conflict:** Another device, often the discrete GPU or a virtual device, can claim resources the NPU needs, blocking its start.
- **BIOS setting or firmware mismatch:** A disabled NPU in BIOS, or firmware that predates your Windows build, can leave the device visible but unstartable.
- **Windows Update driver replacement:** A validated maker driver can be overwritten overnight by a generic update, bringing the warning back without any change on your part. That conflict pattern also appears when the NPU fights other hardware, as in an [NPU conflict with a discrete GPU](/articles/npu-conflict-discrete-gpu-fix/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the exact error code and check for conflicts

The yellow triangle is a symptom, not a diagnosis. The error code in the device properties tells you whether to chase the driver, a conflict, or a missing component.

1. In Device Manager, right-click the NPU and open **Properties**, then read the **Device status** box and note the exact code.
2. Open the **Resources** tab if present and look for any reported conflict with another device.
3. Check whether any other device also shows a warning — a second flagged device often reveals the real conflict.
4. Note the driver version and date on the **Driver** tab for comparison after reinstalling.
5. If the code is 10, 31, or 38, the driver is the prime suspect; a code pointing at resources means you should prioritise Fix 5.

### Fix 2: Uninstall the NPU driver cleanly and redetect it

A clean removal clears mismatched files that a simple update leaves behind. Always remove the driver package, not just the device entry, or the same files will reload.

1. Right-click the NPU in Device Manager and choose **Uninstall device**.
2. Check **Attempt to remove the driver for this device**, then confirm and restart.
3. Let Windows redetect the NPU and check whether the warning is gone or changed.
4. If Windows installs the same bad driver again, do not stop here — replace it manually in the next fix.
5. Test a Copilot+ feature briefly; a warning that clears but a feature that still fails points at the chipset driver next.

### Fix 3: Install the chipset driver, then the NPU driver

Order matters. The chipset driver provides the platform services the NPU driver relies on, so installing the NPU driver first can leave it half-initialised.

1. Download the latest chipset and NPU drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
2. Install the chipset driver first, restarting if the installer asks.
3. Install the NPU driver next, as administrator, and restart again.
4. Check Device Manager: both the chipset devices and the NPU should now show no warnings.
5. If the triangle remains, try the previous NPU driver version from your maker — the newest package is not always the most stable for your BIOS.

### Fix 4: Check BIOS settings and update firmware

A BIOS that disables the NPU, or firmware older than your Windows build, can leave the device detected but unstartable. This check is quick and often overlooked.

1. Restart into BIOS setup and look for NPU, AI engine, or neural processor settings; ensure the NPU is enabled.
2. Save any change, boot into Windows, and recheck Device Manager.
3. If the setting was already enabled, check your BIOS version against your maker's support page.
4. On AC power, install the BIOS update for your exact model and let the laptop restart itself.
5. Recheck the NPU status after the update before reinstalling drivers again — firmware may have been the only fault.

### Fix 5: Resolve conflicts with the GPU and other devices

When the NPU competes with another device for resources, updating the NPU driver alone will never clear the warning. Identify the conflicting device and update or reset it too.

1. Return to the NPU properties and note any device named in the Resources or status text.
2. Update that device's driver from your laptop maker's support page, starting with the graphics driver.
3. If the conflict involves a virtual or unused device, disable it temporarily and recheck the NPU.
4. Restart and confirm both devices now show cleanly in Device Manager.
5. Re-enable anything you disabled one at a time, checking the NPU after each, to find the true conflicting device. A similar isolation method helps when media apps clash with AI hardware, as with [VLC on ARM Windows](/articles/vlc-arm-windows-issues-fix/).

### Fix 6: Repair Windows and block the bad driver update

If the warning survives clean drivers and firmware, Windows or its update behaviour is the cause. Repair the system, then stop Windows Update from reintroducing the bad driver.

1. Run **System File Checker** from an elevated terminal and repair any damage it reports.
2. Reinstall the maker's chipset and NPU drivers after the repair, in the order from Fix 3.
3. Check **Settings > Windows Update** for a pending driver update that matches the bad version.
4. Use Microsoft's Windows support pages to find the supported way to hide that specific driver update.
5. Recheck Device Manager after the next update cycle; if the triangle returns only after an update, the update — not your hardware — is the cause. If it persists through all of this, also rule out a shared AI-component fault like an [Image Creator restyle failure](/articles/image-creator-restyle-not-working/) before seeking hardware service.

## Closing

A yellow triangle on the NPU means Windows can see the device but cannot start it — usually a driver, chipset, conflict, or firmware fault. Read the error code first, uninstall the driver cleanly, install the chipset driver before the NPU driver, and check BIOS settings before assuming hardware failure. That order clears the warning in most cases and keeps it from returning after the next update.
