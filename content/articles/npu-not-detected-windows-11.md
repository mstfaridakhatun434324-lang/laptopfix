---
title: "NPU Not Detected in Windows 11? Here's How to Fix It"
slug: npu-not-detected-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu", "windows 11", "device manager", "ai pc", "troubleshooting"]
description: "NPU not detected in Windows 11? Learn why the Neural processors section vanishes from Device Manager and follow proven fixes to bring your AI chip back."
thumbnail: "/images/thumbs/npu-not-detected-windows-11.webp"
faqs:
  - q: "How do I know if my laptop even has an NPU?"
    a: "Check your processor model first. Intel Core Ultra (Meteor Lake and newer), AMD Ryzen AI 300 / 8000 series, and Qualcomm Snapdragon X chips all include an NPU. You can confirm in Task Manager under Performance, or read our guide on how to [check if your laptop has an NPU](/articles/check-if-laptop-has-npu/). If your CPU predates these lines, there is simply no NPU to detect."
  - q: "Why did my NPU disappear after a Windows update?"
    a: "Windows Update sometimes replaces your working NPU driver with a generic or incompatible version, which can make the whole Neural processors section vanish. This is one of the most common causes we see. Rolling back or reinstalling the driver from your laptop maker's support page usually brings it straight back."
  - q: "Can I still use AI features without a detected NPU?"
    a: "Some features fall back to the CPU or GPU, but slowly and with higher power draw. Copilot+ exclusives like Recall, Live Captions with translation, and Windows Studio Effects require a working NPU with at least 40 TOPS, so they will refuse to run until the NPU is detected again."
  - q: "Will reinstalling Windows bring the NPU back?"
    a: "Only if the problem is deep driver corruption that survives a clean driver reinstall. In most cases a proper clean reinstall of the NPU driver fixes it without touching Windows. Treat a Windows reinstall as a last resort, not a first step."
---

You opened Device Manager expecting to see your new NPU, and it is nowhere to be found — no "Neural processors" section, no Intel AI Boost, nothing. Before assuming defective hardware, know the NPU is physically fine in the vast majority of cases; a missing driver, a disabled BIOS setting, or a bad Windows update is simply hiding it from the operating system.

This is one of the most reported issues on Copilot+ PCs, partly because NPU drivers are young and Windows Update does not always handle them gracefully. If your [Neural processors section is missing from Device Manager](/articles/neural-processors-missing-device-manager/) entirely, the fixes below apply directly — and if the section exists but the driver refuses to install, see our guide on [Intel AI Boost driver installation problems](/articles/intel-ai-boost-driver-not-installing/).

Work through these fixes in order. Each one targets a specific layer — hardware presence, firmware, driver, OS — so by the end you will know exactly where the chain broke.

## Why this happens

- **Your laptop genuinely has no NPU:** Not every "AI laptop" label means a real NPU. Older Intel Core (13th gen and earlier), most discrete-GPU gaming laptops, and budget machines lack the silicon entirely.
- **NPU disabled in BIOS/UEFI:** Many laptops ship with the NPU toggled off in firmware, or a BIOS update flips it off. Windows cannot detect hardware the firmware hides.
- **Driver missing or never installed:** Fresh Windows installs often lack the NPU driver package. Without it, Device Manager shows nothing — or an "Unknown device."
- **Bad driver from Windows Update:** Windows Update occasionally pushes an NPU driver that does not match your chip revision, crashing the device entry out of Device Manager.
- **Corrupted driver stack:** Partial installs or conflicting OEM and generic drivers can leave the NPU in a broken state that presents as "not detected."
- **Windows 11 24H2 incompatibility:** Feature updates have repeatedly broken NPU drivers that worked on 23H2, particularly early Intel Core Ultra and Ryzen AI drivers.
- **Hardware failure (rare):** A dead NPU is possible but uncommon. Suspect this only after exhausting every software fix below.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your laptop actually has an NPU

Do not skip this. Check your exact processor model first, because everything else is wasted effort on hardware that does not exist.

1. Press Win + R, type `msinfo32`, and press Enter.
2. Note the exact Processor line (for example, "Intel Core Ultra 7 155H" or "AMD Ryzen AI 9 HX 370").
3. Intel Core Ultra (Series 1/2), AMD Ryzen AI 300/8000 series, and Qualcomm Snapdragon X chips include NPUs; older Intel 13th/14th gen Core, Ryzen 7000 non-AI, and most budget chips do not.
4. Still unsure? Our guide on how to [check if your laptop has an NPU](/articles/check-if-laptop-has-npu/) walks through Task Manager, Device Manager, and manufacturer spec pages.

### Fix 2: Enable the NPU in BIOS/UEFI

Firmware can hide the NPU from Windows entirely — more common than people expect, especially after BIOS updates.

1. Restart and press the BIOS key during boot (usually F2, Del, or F10).
2. Look under Advanced or Integrated Peripherals for "NPU," "AI Accelerator," or "Intel AI Boost."
3. Change Disabled to Enabled, save and exit (usually F10).
4. After boot, check Device Manager for the Neural processors section.

### Fix 3: Install the NPU driver from your laptop maker

Generic drivers from Windows Update are the number-one cause of NPU weirdness. The OEM package is matched to your exact machine.

1. Go to your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model or serial number.
2. Download the latest NPU driver under Chipset or AI/NPU.
3. If the installer refuses, uninstall the current entry first: Device Manager, right-click the NPU entry, Uninstall device, tick "Attempt to remove the driver."
4. Run the OEM installer as administrator and reboot when prompted.

### Fix 4: Force Windows to redetect the hardware

Sometimes the driver is fine but Windows' device enumeration is stuck. A rescan can shake it loose.

1. Open Device Manager (Win + X, then Device Manager).
2. Click Action, then "Scan for hardware changes."
3. Check Neural processors and "Other devices" for new entries.
4. If an "Unknown device" appears, right-click it and "Search automatically for drivers."

### Fix 5: Roll back a bad Windows Update driver

If the NPU vanished right after Patch Tuesday or a feature update, Windows Update is the prime suspect.

1. In Device Manager, find the NPU entry (it may show a yellow warning) and open Properties, Driver tab.
2. Click "Roll Back Driver" if available.
3. If greyed out, uninstall the device (ticking "Attempt to remove the driver") and install the OEM driver from Fix 3 instead.
4. Pause updates for a week via Settings, Windows Update, so it does not repeat the offense.

### Fix 6: Clean-install the NPU driver stack

When drivers are half-installed or conflicting, only a full wipe of the driver stack reliably clears the mess.

1. Download the correct OEM NPU driver package first, but do not run it yet.
2. Disconnect from the internet so Windows cannot install its own driver mid-process.
3. In Device Manager, uninstall every entry under Neural processors, ticking "Attempt to remove the driver" each time.
4. Still offline, run the OEM installer, then reboot and reconnect.

### Fix 7: Check for Windows 11 24H2-specific issues

Major Windows versions have broken NPU support more than once, and 24H2 is a repeat offender for early AI PC drivers.

1. Check your version: Settings, System, About.
2. Confirm your maker lists a 24H2-compatible NPU driver; some OEMs lag months behind.
3. Install all pending updates — Microsoft has shipped NPU compatibility fixes through cumulative updates.
4. If it worked on 23H2 and broke on 24H2 with no fixed driver, the OEM driver update is the only real fix; check back monthly.

## Closing

An undetected NPU is almost always software — missing OEM driver, disabled firmware setting, or a Windows Update that replaced a working driver with a broken one. Work the chain from hardware confirmation through BIOS to a clean OEM driver install, and the Neural processors section returns in the large majority of cases. Only if every fix fails should you suspect the silicon and contact warranty support.
