---
title: "Neural Processors Missing from Device Manager? Fix It Fast"
slug: neural-processors-missing-device-manager
date: 2026-10-19
categories: ["ai-pc"]
tags: ["neural processors", "device manager", "npu", "windows 11", "driver"]
description: "Neural processors missing from Device Manager in Windows 11? Discover why the NPU section vanishes and how to restore it in minutes."
thumbnail: "/images/thumbs/neural-processors-missing-device-manager.webp"
faqs:
  - q: "What is the Neural processors section in Device Manager?"
    a: "It is the Device Manager category where Windows lists NPU hardware — Intel AI Boost, AMD NPU, or Qualcomm Hexagon entries live here. If your laptop has an NPU and its driver is installed, this section appears automatically."
  - q: "Is it normal for Neural processors to be missing on older laptops?"
    a: "Yes, completely normal. Laptops without an NPU (most machines from before 2024) never show this section. Its absence only signals a problem on AI PCs that should have one."
  - q: "Can a Windows update remove the Neural processors section?"
    a: "Yes. A bad driver pushed by Windows Update can crash the device entry so thoroughly that the whole section disappears. Rolling back or clean-installing the OEM driver brings it back."
  - q: "Should the section appear in Safe Mode?"
    a: "Not necessarily — Safe Mode loads a minimal driver set, so missing NPU entries there prove nothing. Always check in a normal boot."
---

Open Device Manager, scroll through the categories, and there is no "Neural processors" anywhere. On an AI laptop that should have an NPU, that missing section is the visible symptom of everything from a disabled BIOS toggle to a driver that Windows Update quietly destroyed. The good news: the section itself is just a label Windows creates when it sees working NPU hardware with a driver. Bring back either half of that equation and the section returns.

First, make sure you are chasing a real problem. Laptops without an NPU never show this section, so confirm your chip actually includes one — our guide on [NPU not detected in Windows 11](/articles/npu-not-detected-windows-11/) starts with exactly that check. If the hardware is confirmed and the section is still gone, the causes below are in rough order of likelihood.

## Why this happens

- **No NPU in the hardware:** The most common "cause" on older or budget laptops. No chip, no section, no fix needed.
- **NPU disabled in firmware:** BIOS/UEFI can hide the NPU, and Windows will not create a category for hardware it cannot see.
- **Driver not installed:** Without any NPU driver, Windows may show nothing at all rather than an Unknown device.
- **Driver crashed out:** A bad or mismatched driver can make Windows remove the device node entirely instead of flagging it.
- **Windows Update replaced a working driver:** A driver update that fails mid-install can delete the old working entry and fail to create the new one.
- **Device enumeration glitch:** Rarely, Windows' Plug and Play enumeration stalls and simply never builds the category, even with good hardware and drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the hardware exists

Do not troubleshoot a ghost.

1. Press Win + R, type `msinfo32`, Enter — note the exact processor model.
2. Only Intel Core Ultra, AMD Ryzen AI (300/8000 series), and Qualcomm Snapdragon X include NPUs.
3. If your chip is older or lacks an NPU, the missing section is expected behavior — stop here.
4. If the chip qualifies, continue: the problem is software or firmware.

### Fix 2: Check BIOS for a disabled NPU

Firmware is the gatekeeper. If it hides the NPU, Windows never gets a chance.

1. Reboot into BIOS/UEFI (F2, Del, or F10 during boot).
2. Search Advanced / Integrated Peripherals for NPU, AI Accelerator, or Neural Processing Unit.
3. Set it to Enabled if disabled, then save and exit.
4. Boot into Windows and recheck Device Manager — allow a minute for hardware detection.
5. If the section appears but shows a warning icon, you now have a driver problem; install the OEM NPU driver.

### Fix 3: Force a hardware rescan

Cheap and occasionally all it takes.

1. Open Device Manager, click Action, "Scan for hardware changes."
2. Watch for the Neural processors category appearing, or an Unknown device.
3. If an Unknown device appears, right-click it and update the driver automatically.
4. Still nothing? Shut down fully (not restart), power on, and scan again.

### Fix 4: Install the OEM NPU driver

The section appears when Windows sees the hardware *with* a driver. Supply the driver.

1. Get the NPU driver from your maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Run the installer as administrator and reboot.
3. Check Device Manager — the Neural processors section should now exist with the NPU listed cleanly.
4. If the installer fails, work through our [Intel AI Boost driver installation fixes](/articles/intel-ai-boost-driver-not-installing/) before continuing.

### Fix 5: Undo Windows Update damage

If the section vanished after an update, the update is guilty until proven innocent.

1. In Device Manager, check "Other devices" and "System devices" for orphaned NPU entries with warnings.
2. Uninstall any you find, ticking "Attempt to remove the driver."
3. Install the OEM driver from Fix 4 while updates are paused (Settings, Windows Update, Pause).
4. If the section was there yesterday and gone today, also check View, "Show hidden devices" — a greyed-out entry confirms a driver crash rather than missing hardware.

### Fix 6: Clean out driver conflicts

When multiple driver versions fight, Windows can give up and show nothing.

1. Disconnect from the internet.
2. Uninstall every NPU-related entry in Device Manager, removing driver software each time.
3. Open `pnputil /enum-drivers` in admin Command Prompt and delete stale NPU .inf packages with `pnputil /delete-driver oemXX.inf /uninstall`.
4. Reboot, stay offline, install the single correct OEM driver, then reconnect.
5. If the section still refuses to appear after a true clean install, suspect firmware — check for a BIOS update from your maker, since newer firmware often fixes NPU enumeration.

## Closing

The Neural processors section is Windows' way of saying "I see a working NPU." When it is missing on capable hardware, the chain broke at firmware visibility, driver presence, or a Windows Update mishap. The fixes above rebuild that chain link by link. AMD owners should note the [Ryzen AI NPU has its own detection quirks](/articles/amd-ryzen-ai-npu-not-showing-up/) tied to the chipset driver package. If the section appears but the device underneath throws [error code 43](/articles/npu-driver-error-code-43/), that is the next problem to solve — and it has its own dedicated fixes.
