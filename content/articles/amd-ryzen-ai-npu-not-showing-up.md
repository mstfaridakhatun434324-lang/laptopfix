---
title: "AMD Ryzen AI NPU Not Showing Up? Fix It in Minutes"
slug: amd-ryzen-ai-npu-not-showing-up
date: 2026-10-19
categories: ["ai-pc"]
tags: ["amd ryzen ai", "npu", "device manager", "windows 11", "driver"]
description: "AMD Ryzen AI NPU not showing up in Windows 11? Fix missing NPU entries with chipset driver updates, BIOS checks, and clean driver reinstalls."
thumbnail: "/images/thumbs/amd-ryzen-ai-npu-not-showing-up.webp"
faqs:
  - q: "Which AMD processors have an NPU?"
    a: "Ryzen 8000 series (Hawk Point) and Ryzen AI 300 series (Strix Point) include AMD's XDNA NPU. Older Ryzen 5000/7000 chips do not. Check your exact model in System Information before troubleshooting."
  - q: "Where should the AMD NPU appear in Device Manager?"
    a: "Under a 'Neural processors' section, or sometimes under System devices, depending on driver version. If neither shows anything NPU-related, the driver is missing or the firmware has the NPU disabled."
  - q: "Do I need the AMD chipset driver for the NPU?"
    a: "Yes — on Ryzen AI laptops the NPU is delivered through the AMD chipset driver package. An outdated or missing chipset driver is the most common reason the NPU never appears."
  - q: "Can Windows Update install the AMD NPU driver?"
    a: "Sometimes, but unreliably. AMD's own chipset package from amd.com or your laptop maker's support page is far more consistent for NPU detection."
---

Your Ryzen AI laptop should have an NPU humming under the hood, but Device Manager shows no trace of it — no Neural processors, no AMD NPU, nothing. On AMD machines this almost always traces to the chipset driver package, because unlike Intel's standalone AI Boost installer, AMD delivers NPU support through its chipset drivers. No chipset driver, no NPU.

Before assuming the worst, verify your chip: Ryzen AI 300 series and Ryzen 8000 series have the XDNA NPU; anything older does not. If the hardware qualifies, the fixes below — starting with the chipset package — bring the NPU back in most cases. General [NPU detection fixes](/articles/npu-not-detected-windows-11/) also apply, but AMD has its own quirks worth handling first.

## Why this happens

- **Missing AMD chipset driver:** The top cause. Clean Windows installs and some OEM images ship without the chipset package that contains NPU support.
- **Outdated chipset driver:** Old chipset packages predate NPU enablement or carry broken NPU components.
- **NPU disabled in BIOS:** Some AMD laptops hide the NPU under "AI" or integrated-peripheral firmware toggles.
- **Windows Update partial install:** Windows may install a fragment of AMD driver support that neither works nor lets the proper package install cleanly.
- **Ryzen AI vs non-AI confusion:** Ryzen 8040 non-AI SKUs and older chips genuinely lack the NPU — marketing names are confusing.
- **Driver conflict after manual installs:** Mixing AMD.com chipset drivers with OEM-customized versions can break NPU enumeration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm you have a Ryzen AI chip

Five minutes here saves hours of fruitless troubleshooting.

1. Win + R, `msinfo32`, note the exact processor (e.g., "AMD Ryzen AI 9 HX 370").
2. Qualifying: Ryzen AI 300 series, Ryzen 8040/8000 series with "AI" in the name.
3. Not qualifying: Ryzen 7000/5000 series, or 8040 chips without AI branding — no NPU exists.
4. If qualified and still missing, continue — this is a software problem.

### Fix 2: Install the AMD chipset driver package

This is the fix that works most often on AMD machines.

1. Go to [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html), select Chipsets, your socket/platform, and download the latest chipset package.
2. Alternatively, get the chipset driver from your laptop maker's support page ([Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), [Dell](https://www.dell.com/support)) — OEM versions are tuned for your machine.
3. Run the installer as administrator and reboot when prompted.
4. Open Device Manager and look for Neural processors or new System devices entries.
5. If the installer says a newer version exists but the NPU is still missing, uninstall the chipset package first, reboot, then reinstall cleanly.

### Fix 3: Check BIOS for the NPU toggle

AMD firmware sometimes labels it obscurely.

1. Reboot into BIOS (F2/Del/F10).
2. Look for NPU, "XDNA," "AI Engine," or IPU settings under Advanced.
3. Enable anything NPU/XDNA-related that is disabled.
4. Save, exit, boot Windows, and recheck Device Manager.
5. If a BIOS update is available from your maker, install it — several vendors fixed NPU visibility in firmware updates.

### Fix 4: Clean out broken AMD driver fragments

Partial Windows Update installs block the real package.

1. Disconnect from the internet.
2. Device Manager: uninstall any AMD NPU / Unknown device entries, removing driver software.
3. Use AMD's Cleanup Utility (from AMD's support site) to remove all AMD driver components.
4. Reboot, stay offline, install the full chipset package from Fix 2.
5. Reconnect and verify the NPU appears and stays across reboots.

### Fix 5: Force hardware redetection

Sometimes the driver is present but enumeration stalled.

1. Device Manager, Action, "Scan for hardware changes."
2. Check Neural processors, System devices, and Other devices.
3. If an Unknown device appears, update its driver automatically — Windows may now find the AMD NPU driver.
4. Still nothing? Full shutdown (not restart), power on, scan again.

### Fix 6: Check for Windows 11 24H2 issues

Feature updates have broken AMD NPU support more than once.

1. Confirm your Windows version in Settings, System, About.
2. Check your maker's support page for a 24H2-validated chipset driver — install it even if your current one is "newer" by version number.
3. Install all pending Windows updates; Microsoft has shipped AMD NPU fixes in cumulative updates.
4. If problems started exactly with 24H2 and no fixed driver exists, the OEM update is the only real resolution — meanwhile the laptop works fine as a non-AI PC.

## Closing

On Ryzen AI laptops, the NPU lives and dies with the chipset driver package — that single insight resolves most "not showing up" cases. Install the correct AMD chipset driver, verify the BIOS toggle, and clean out any Windows Update fragments, and the NPU appears. Once it is running, keep an eye on [NPU power usage](/articles/npu-high-power-usage-draining-battery/) — a misbehaving driver can keep the chip working overtime and drain your battery. If you have wrestled with [Snapdragon X NPU driver issues](/articles/snapdragon-x-elite-npu-driver-issues/) on another machine, note the pattern is the same: the platform driver package matters more than any standalone NPU installer.
