---
title: "High DPC Latency in Windows 11? Find and Fix the Driver Causing It"
slug: how-do-i-fix-dpc-latency-high-windows-11
date: 2026-10-01
categories: ["performance"]
tags: ["dpc latency", "windows 11", "latencymon", "audio stuttering", "driver issues"]
description: "Audio crackling, mouse stutter, or lag spikes on Windows 11? High DPC latency is usually one misbehaving driver. Learn how to measure it and fix the culprit."
thumbnail: "/images/thumbs/how-do-i-fix-dpc-latency-high-windows-11.webp"
faqs:
  - q: "What is DPC latency and why does it cause stuttering?"
    a: "DPC stands for Deferred Procedure Call — a mechanism Windows drivers use to finish interrupt work. When a driver takes too long (typically over 1000 microseconds), it delays everything else, causing audio crackles, mouse lag, and frame stutters. It is not a CPU speed problem; even a fast laptop stutters if one driver hogs the kernel. Identifying which driver is slow is the key step."
  - q: "What DPC latency numbers are considered good or bad?"
    a: "Under 500 microseconds is excellent and suitable for real-time audio. Values between 500 and 1000 microseconds are acceptable for general use but may bother musicians. Consistently above 1000 microseconds usually produces audible crackling and visible stutter. Spikes above 2000 microseconds are a clear sign a driver needs attention. Measure with LatencyMon over at least 10 minutes of normal use for reliable numbers."
  - q: "Can high DPC latency damage my laptop?"
    a: "No, high DPC latency does not damage hardware — it is purely a responsiveness problem. Your CPU, GPU, and other components are not being harmed. The practical impact is annoyance: crackling audio, dropped frames in recordings, and laggy input. That said, the underlying cause (like an overheating component throttling, or a failing device retrying operations) is worth fixing for overall system health."
  - q: "Why does DPC latency spike only when I'm on Wi-Fi?"
    a: "Wi-Fi drivers are the single most common cause of DPC latency spikes on laptops. Many wireless drivers perform lengthy operations at high interrupt priority, especially during roaming, power-state transitions, or background scanning. If LatencyMon points at your wireless driver (often ndis.sys with the Wi-Fi miniport beneath it), updating the driver from your laptop maker's support page usually resolves it."
---

Audio crackles during a call, the mouse freezes for a split second, or the screen hitches while gaming — yet Task Manager shows the CPU barely working. That mismatch is the signature of high DPC latency. Somewhere in the kernel, a single driver is taking too long to finish its work, and everything else in the system has to wait its turn.

DPC stands for Deferred Procedure Call. When hardware raises an interrupt, Windows hands the urgent part to the driver immediately and defers the rest as a DPC. Healthy drivers finish in microseconds. A misbehaving driver — often the Wi-Fi, audio, or storage driver — can stretch a DPC to milliseconds, and during those milliseconds, audio buffers underrun (crackle), input stalls, and frames drop. The good news: it is almost always fixable, and the fix starts with naming the guilty driver rather than guessing.

This guide walks you through measuring DPC latency properly with LatencyMon, pinpointing the offending driver, and applying the targeted fixes that actually move the needle — driver updates, power-management tweaks, and device isolation — instead of the generic "reinstall Windows" advice. If your broader symptom is gaming stutter rather than system-wide hitches, also see [fixing game stuttering after Windows updates](/articles/how-to-fix-game-stuttering-after-windows-update-on-windows-11/).

## Why this happens

- **Buggy or outdated Wi-Fi driver**: Wireless drivers are the most frequent offenders; long DPCs during scanning, roaming, or power transitions.
- **Audio driver misbehaving**: The very driver feeding your speakers can delay the kernel, ironically causing the crackles it produces.
- **GPU driver DPC spikes**: Graphics drivers doing heavy work at dispatch level, especially with certain power-saving features enabled.
- **Storage driver retries**: A struggling SSD or a storage driver repeatedly retrying operations blocks the kernel.
- **CPU power-state transitions**: Aggressive C-state or frequency changes can delay DPC execution on laptops tuned for battery life.
- **USB device polling**: A misbehaving USB peripheral or hub generating constant interrupts that the driver handles slowly.
- **Network driver interrupt moderation issues**: Poorly tuned interrupt coalescing settings on Ethernet or Wi-Fi adapters.
- **Outdated BIOS or chipset firmware**: Firmware-level bugs in interrupt routing or power management that no driver update can work around.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure properly and name the culprit with LatencyMon

Guessing wastes time. Measure first.

1. Download **LatencyMon** (free, from Resplendence) and run it as administrator.
2. Click the green **play** button and let it run for at least **10 minutes** while you use the laptop normally — browse, play audio, do the things that trigger the stutter.
3. Check the **Main** tab: note the highest reported DPC routine execution time and whether the tool says your system is suitable for real-time audio.
4. Switch to the **Drivers** tab and sort by **DPC count** and **Highest execution (ms)** — the driver at the top with the biggest numbers is your prime suspect. Common names: `ndis.sys` (network stack — look beneath it at the actual miniport driver), `storport.sys` (storage), `dxgkrnl.sys` (graphics), `HDAudBus.sys`/`portcls.sys` (audio), or `USBPORT.SYS` (USB).

### Fix 2: Update or reinstall the offending driver from the right source

The manufacturer's driver beats the generic Windows one.

1. In **Device Manager**, find the device matching your suspect driver, and note the current driver version and date on the **Driver** tab.
2. Go to your laptop maker's support page — Dell, HP, or Lenovo — enter your exact model, and download the newest driver for that device. Laptop makers validate drivers against your specific hardware, which matters for DPC behavior.
3. If the maker has nothing newer, try the chip vendor directly: Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel Wi-Fi/Bluetooth, or the GPU vendor pages for graphics.
4. Install the new driver, then **restart** (not shut down — Fast Startup can preserve the old driver state).
5. Re-run LatencyMon for 10 minutes and compare numbers. If the spike driver changed, you've made progress; if it's identical, move to Fix 3 — the driver version wasn't the issue.

### Fix 3: Tame CPU and device power management

Power-saving features are a classic DPC latency source on laptops.

1. Open **Settings** > **System** > **Power & battery** > **Power mode** and set it to **Best performance** while testing — this reduces CPU frequency ramping delays. For the full walkthrough, see [changing the power plan to best performance](/articles/how-to-change-power-plan-to-best-performance-on-windows-11/).
2. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**: set **PCI Express** > **Link State Power Management** to **Off**, and **USB settings** > **USB selective suspend** to **Disabled**.
3. In **Device Manager**, open your Wi-Fi adapter's **Properties** > **Power Management** tab and uncheck **Allow the computer to turn off this device to save power** — Wi-Fi power transitions are notorious DPC spikers.
4. Still in the adapter properties, check the **Advanced** tab for **Roaming Aggressiveness** and set it to **Lowest** — less background scanning means fewer DPC storms.
5. Re-test with LatencyMon. If numbers drop dramatically, you've found a power-management trigger; you can re-enable settings one by one later to find the exact one.

### Fix 4: Isolate USB and peripheral devices

A single bad peripheral can poison the whole kernel.

1. Disconnect **all** USB devices except keyboard and mouse, then run LatencyMon again. If `USBPORT.SYS` drops out of the top offenders, a peripheral was the cause.
2. Reconnect devices one at a time, testing a few minutes each, until the latency returns — that's your culprit.
3. Common offenders: USB audio interfaces on underpowered hubs, RGB controllers, capture cards, and docks with flaky firmware.
4. For the guilty device, try a different USB port (preferably directly on the laptop, not through a hub), update its driver, or check the maker's site for firmware updates.
5. If it's a dock, test with the laptop undocked entirely — dock firmware bugs are a well-known DPC source on business laptops.

### Fix 5: Address the GPU driver

Graphics drivers run at high priority and their DPCs hurt.

1. If `dxgkrnl.sys` or your GPU vendor's driver tops LatencyMon, do a **clean** GPU driver install: download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html), choose **Custom install** and check **Perform a clean installation**.
2. In **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**, try toggling **Hardware-accelerated GPU scheduling** — on some systems it reduces DPC latency, on others it increases it; test both ways with LatencyMon. Background: [enabling hardware-accelerated GPU scheduling](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-11/).
3. Disable in-game overlays (GeForce Experience, Discord, Xbox Game Bar) one by one — overlay hooks add DPC overhead in the graphics path.
4. If the GPU driver spikes only on battery, that's power management again — test plugged in with Best performance mode.

### Fix 6: Update BIOS and chipset firmware

When drivers are innocent, suspect the firmware.

1. Check your current BIOS version: press **Win + R**, type `msinfo32`, and note **BIOS Version/Date**.
2. Visit your laptop maker's support page (Dell, HP, Lenovo) and compare against the latest BIOS for your exact model — read the release notes for mentions of latency, stutter, or interrupt fixes.
3. Install the BIOS update **with the charger plugged in and the battery charged**, following the maker's instructions exactly. Don't interrupt it.
4. Also install the latest **chipset driver** package from the same page — chipset drivers govern how interrupts route through the platform.
5. After updating, reset BIOS to defaults (or **Optimized Defaults**), then re-test. Firmware fixes are often the final answer when LatencyMon shows `hal.dll` or `ntoskrnl.exe` itself with high DPC times, meaning no single driver is to blame.

## Closing

High DPC latency looks mysterious but follows a simple rule: measure with LatencyMon, identify the worst driver, and fix that specific thing — its driver, its power settings, or its firmware. Most cases resolve at Fix 2 or Fix 3. If you've worked through all six fixes and LatencyMon still reports multi-millisecond DPCs with no clear driver, suspect hardware — a failing SSD or marginal USB controller — and contact your laptop maker's warranty support.
