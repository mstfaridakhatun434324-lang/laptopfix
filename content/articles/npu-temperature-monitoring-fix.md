---
title: "How to Fix NPU Temperature Monitoring Not Showing on Your AI PC"
slug: npu-temperature-monitoring-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["npu temperature", "npu monitoring", "copilot+ pc", "hwinfo", "thermal monitoring", "troubleshooting"]
description: "Restore missing NPU temperature readings on your Copilot+ PC with fixes for sensor drivers, monitoring tools, BIOS settings, and Windows reporting gaps."
thumbnail: "/images/thumbs/npu-temperature-monitoring-fix.webp"
faqs:
  - q: "Why does my monitoring tool show no NPU temperature?"
    a: "Most tools only show sensors the driver exposes. If the NPU driver is generic, outdated, or missing its sensor component, the temperature sensor simply is not reported, even though the NPU itself may be working."
  - q: "Does every NPU have a temperature sensor?"
    a: "Not every design exposes one to Windows. Some Copilot+ NPUs report temperature only to firmware, or only through the maker's own utility. Check your maker's tool before assuming the sensor is broken."
  - q: "Is it safe if I cannot see the NPU temperature?"
    a: "Yes, in most cases. The NPU has its own thermal protection and will throttle or shut down before damage occurs. Monitoring is useful for diagnosis, but its absence alone does not mean the chip is overheating."
  - q: "Will a BIOS update add NPU temperature reporting?"
    a: "Sometimes. Makers add sensor exposure in BIOS or firmware updates, especially on early Copilot+ models. If your maker's changelog mentions NPU monitoring or thermal reporting, that update is worth installing."
---

Your monitoring app shows CPU and GPU temperatures in detail, but the NPU line is blank, greyed out, or missing entirely. You know the NPU is there — Copilot+ features work, Task Manager shows NPU activity — yet no tool will tell you how hot it is running. That gap is annoying when you are chasing throttling, fan noise, or a hot chassis.

NPU temperature reporting is newer and less standardised than CPU or GPU monitoring. There is no single Windows sensor API that every NPU uses, so each maker exposes the reading differently: through the driver, through firmware, or only through its own utility. When any link in that chain is missing, the reading vanishes while the NPU keeps working.

This guide explains where NPU temperature data actually comes from and how to restore it, starting with the monitoring tool itself and working down to the driver and firmware. Work through the fixes in order and recheck your tool after each step.

## Why this happens

- **Generic NPU driver without a sensor component:** Windows Update drivers often include the compute driver but not the sensor or monitoring component, so tools have no temperature value to display.
- **Monitoring tool does not support your NPU:** Many popular tools added NPU support late, and only for specific chips. An older tool version may simply not know how to read your NPU at all.
- **Sensor disabled in BIOS or firmware:** Some makers ship with NPU telemetry off by default, or a BIOS update resets it, so the sensor exists but never reports to Windows.
- **NPU idle and unreported:** When the NPU is idle, some drivers stop reporting its temperature or report zero, which tools display as a blank or missing sensor rather than a real reading.
- **Conflicting monitoring tools:** Two tools polling the same sensor driver at once can lock each other out, leaving one or both with no NPU reading.
- **Windows power mode hiding the NPU:** In battery-saver or efficiency modes the NPU may be powered down so completely that its sensor disappears from the hardware list until it wakes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Generate NPU load and check what the tool actually sees

Before reinstalling anything, find out whether the sensor is missing or merely idle. An NPU that is asleep often reports nothing, and a quick AI workload wakes both the chip and its sensor. This two-minute test prevents a long driver hunt for a sensor that was never broken.

1. Open your monitoring tool and note exactly what it shows for the NPU — blank, zero, greyed out, or absent entirely.
2. Run an AI workload for two minutes: open Cocreator, apply a Windows Studio Effect in a video call, or run Recall search.
3. Watch the tool during the workload and check Task Manager's NPU graph at the same time to confirm the chip is actually active.
4. If a temperature appears under load but vanishes at idle, nothing is broken — your driver only reports the sensor while the NPU is awake.
5. If no reading appears even under load, move to Fix 2; the problem is in the tool or the driver, not the workload.

### Fix 2: Update your monitoring tool and try the maker's utility

Monitoring tools vary wildly in NPU support, so the tool itself is the most common culprit. Update to a version that explicitly lists your NPU, and cross-check with your laptop maker's own utility, which reads the sensor through the maker's private path when generic tools cannot. A similar tool-versus-driver confusion can also inflate reported load, as covered in [NPU use by Windows Search](/articles/npu-windows-search-high-usage-fix/). Generative AI features fail differently — for example, [Paint generative fill missing](/articles/paint-generative-fill-missing/) is usually an app-update issue, not a sensor one.

1. Update your monitoring tool to its latest release and check its changelog or sensor list for your exact NPU model.
2. In the tool's settings, enable any NPU, AI accelerator, or sensor option that is off by default.
3. Install your laptop maker's system utility — such as Dell, HP, or Lenovo's support or diagnostics app — and look for its thermal or NPU section.
4. Compare the two tools under an AI workload: if the maker's utility shows a temperature and the generic tool does not, your sensor works and the generic tool simply lacks support.
5. If neither tool shows anything under load, the driver or firmware is not exposing the sensor — continue to Fix 3.

### Fix 3: Reinstall the OEM NPU and chipset drivers

When no tool can see the sensor, the driver is the next suspect. The sensor component travels with the OEM driver package, and a generic Windows Update driver is the usual reason it goes missing. Reinstalling the full OEM package restores both the compute driver and its telemetry side.

1. Open **Device Manager** and confirm the NPU entry exists without a warning icon; note its exact name for the download step.
2. Download the latest **NPU and chipset driver package** for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. Uninstall the NPU device in Device Manager, ticking **"Attempt to remove the driver for this device"** if offered.
4. Run the OEM installer as administrator, restart when prompted, then run an AI workload and recheck your monitoring tool.
5. If the sensor appears, stop here — and note the driver version, so you can spot a future Windows Update swap that removes it again.

### Fix 4: Check BIOS settings and update firmware

Some Copilot+ laptops gate NPU telemetry behind a BIOS option, and early firmware versions simply did not expose the sensor to Windows at all. A BIOS check plus a firmware update is the fix when the driver is correct but the sensor still never appears.

1. Restart into BIOS setup (usually **F2**, **F12**, or **Del** at boot) and look under Advanced, Configuration, or Thermal for **NPU telemetry**, **AI accelerator**, or **sensor** options.
2. Enable any NPU telemetry or monitoring option you find, save, and exit.
3. On your maker's support page, check whether a newer BIOS mentions NPU monitoring, thermal reporting, or sensor fixes in its changelog.
4. If it does, plug in the charger, close all apps, and install the BIOS update — never update BIOS on battery power.
5. Boot into Windows, run an AI workload, and recheck your monitoring tool; firmware-exposed sensors usually appear immediately after this update.

### Fix 5: Rule out power modes and conflicting tools

Power policy and tool conflicts can hide a working sensor. Battery saver powers the NPU down so far that its sensor drops off the hardware list, and two polling tools can block each other. Isolating both variables takes a few minutes and is worth doing before a clean driver sweep.

1. Plug in the charger and set **Settings > System > Power & battery > Power mode** to **Best performance** for testing.
2. Close every monitoring tool, then open only one — your primary tool — and test under an AI workload.
3. If the reading appears with a single tool on AC power, you found the conflict or the power cause; reopen tools one at a time to identify the clash.
4. Check **Task Manager > Startup** and disable any second monitoring tool that auto-starts and polls sensors in the background.
5. If a specific app's behaviour is also odd, remember that app-level issues have their own causes — for example, [EA App problems on ARM Windows](/articles/ea-app-arm-windows-issues-fix/) are unrelated to sensor reporting and should not be mixed into this diagnosis.

## Closing

A missing NPU temperature reading is usually a reporting gap, not a failing chip — the sensor is hidden by the tool, the driver, or the firmware, while the NPU's own thermal protection keeps working. Work from the tool inward to the driver and firmware, and if the design simply does not expose the sensor, proxy measurements will still tell you everything you need about throttling.
