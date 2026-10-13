---
title: "The Best Way to Fix High DPC Latency in Windows 11"
slug: best-way-to-fix-dpc-latency-high-windows-11
date: 2026-09-16
categories: ["performance"]
tags: ["dpc latency", "latency spikes", "audio stutter", "drivers", "windows 11"]
description: "High DPC latency causing audio crackles and stutters on Windows 11? The best-practice method to find the offending driver and fix it."
thumbnail: "/images/thumbs/best-way-to-fix-dpc-latency-high-windows-11.webp"
faqs:
  - q: "What is DPC latency and why does it matter?"
    a: "DPC (Deferred Procedure Call) latency measures how long drivers take to finish their interrupt work before the system can do anything else. When a driver hogs the CPU at high priority, audio crackles, video stutters, and mouse input feels laggy — even though Task Manager shows low overall CPU. For real-time tasks like audio production and gaming, DPC spikes above 1000 microseconds are where problems start."
  - q: "What is a good DPC latency number on Windows 11?"
    a: "On a healthy system, LatencyMon typically shows maximum DPC latencies under 200–500 microseconds during normal use, with averages far lower. Occasional spikes to 1000µs during heavy load are tolerable. Sustained spikes above 2000µs — or any driver routinely exceeding 1000µs — will produce audible crackles and visible stutters that you need to fix."
  - q: "Which drivers most commonly cause high DPC latency?"
    a: "Network drivers (Wi-Fi and Ethernet) are the number one offender, followed by storage controller drivers, GPU drivers, and USB controller drivers. Power management drivers and some antivirus filter drivers also appear frequently. LatencyMon's Drivers tab names the exact .sys file, which usually maps directly to one of these categories."
  - q: "Can Windows 11 power settings increase DPC latency?"
    a: "Yes, significantly. CPU parking, core frequency scaling, and PCIe link-state power management all introduce latency as hardware wakes from low-power states. Audio professionals routinely disable CPU power saving for this reason. Switching to the High Performance power plan and disabling PCI Express Link State Power Management often cuts DPC spikes dramatically on laptops."
---

If your audio crackles, your games micro-stutter, or your mouse feels intermittently drunk — while Task Manager insists the CPU is barely working — you're probably looking at high DPC latency. It's one of the sneakiest performance problems on Windows 11 because the usual monitoring tools don't show it. The CPU isn't overloaded; it's being *interrupted*.

DPC latency happens when a driver takes too long handling its hardware interrupts, blocking everything else at high priority. The fix is almost always driver-related: find the offending driver with LatencyMon, then update, replace, or reconfigure it. Here's the best-practice method, in the order professionals use it.

## Why this happens

- **Buggy network drivers**: Wi-Fi and Ethernet drivers are the most frequent DPC offenders, especially vendor-supplied ones.
- **Storage controller drivers**: Outdated AHCI/NVMe or chipset drivers stall the system during disk interrupts.
- **GPU driver issues**: Display drivers with aggressive power management spike during clock transitions.
- **CPU power-state transitions**: Core parking and frequency scaling add latency every time cores wake up.
- **USB controller problems**: Faulty USB drivers or devices generating interrupt storms.
- **Antivirus filter drivers**: Real-time scanning drivers inserting themselves into the I/O path.
- **BIOS/firmware bugs**: Platform firmware mishandling interrupts, particularly on newer laptop models.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure with LatencyMon and identify the driver

You need data, not guesses — LatencyMon names names.

1. Download **LatencyMon** (free, from Resplendence) and run it as administrator.
2. Click the **Play** button and let it monitor for at least 5–10 minutes while you reproduce the problem (play audio, game, or just use the laptop normally).
3. Check the **Main** tab: look at the **Highest reported DPC routine execution time**. Consistently over 1000µs confirms a real problem.
4. Switch to the **Drivers** tab, sort by **DPC count** or highest execution time — the top entries name the exact `.sys` files responsible (e.g., `ndis.sys`, `storport.sys`, `nvlddmkm.sys`, `dxgkrnl.sys`).
5. Google the driver filename to identify its hardware (ndis.sys = network stack, storport.sys = storage, USBXHCI = USB). This tells you exactly which device's driver to fix next. If overall system responsiveness is also poor, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

### Fix 2: Update the offending driver from the right source

Generic Windows drivers are a common DPC source — get the proper ones.

1. For **network** offenders (ndis.sys, or your Wi-Fi driver's .sys): download the latest Wi-Fi/Ethernet driver from your laptop vendor's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — or the chipmaker (Intel/Realtek/Qualcomm).
2. For **storage** offenders (storport.sys): update the **chipset driver** from your laptop vendor — it bundles the storage controller driver.
3. For **GPU** offenders (nvlddmkm.sys, dxgkrnl.sys): clean-install the latest driver from NVIDIA, AMD, or Intel's detection tool.
4. Install one driver at a time, reboot, and re-run LatencyMon for 10 minutes to verify improvement before moving on.
5. If the newest driver is worse (it happens), roll back: **Device Manager** > device > **Properties** > **Driver** tab > **Roll Back Driver**.

### Fix 3: Disable CPU power saving

Power-state transitions are a massive DPC latency source on laptops.

1. Open **Settings** > **System** > **Power & battery** and set **Power mode** to **Best performance**.
2. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
3. Expand **Processor power management** > **Minimum processor state** and set it to **100%** (plugged in). This stops cores from parking and unparking.
4. Expand **PCI Express** > **Link State Power Management** > set to **Off**.
5. Reboot and re-run LatencyMon. On many laptops this single change cuts maximum DPC latency by half or more. (Battery life will decrease — use these settings when plugged in for audio/gaming work.)

### Fix 4: Tame the network driver specifically

Since network drivers offend most often, they deserve dedicated attention.

1. Open **Device Manager** > **Network adapters**, right-click your Wi-Fi adapter > **Properties** > **Advanced** tab.
2. Disable power-hungry features: set **Power Saving Mode** to **Maximum Performance**, and disable **U-APSD support** / **WMM Power Save** if present.
3. In the **Power Management** tab, uncheck **Allow the computer to turn off this device to save power**.
4. If Wi-Fi DPC spikes persist, test with Wi-Fi off and Ethernet connected (or vice versa) to confirm which adapter's driver is guilty.
5. As a workaround for stubborn Wi-Fi drivers, some users disable the Wi-Fi adapter in Device Manager when doing latency-critical work offline — inelegant but effective.

### Fix 5: Update BIOS and disable problematic devices

Firmware-level interrupt issues need firmware-level fixes.

1. Check your laptop vendor's support page for **BIOS/UEFI updates** — release notes mentioning "stability," "interrupt," or "latency" are directly relevant. Follow the vendor's flashing instructions exactly, on AC power.
2. In **Device Manager**, look for devices with warning icons or ones you don't use (e.g., an unused fingerprint reader, SD card reader) — right-click > **Disable device** as a test.
3. Disconnect USB peripherals one by one while LatencyMon runs — a faulty USB device can generate interrupt storms that look like driver DPC spikes.
4. If you dual-boot or use virtualization, test with Hyper-V/VBS features off temporarily — hypervisor interrupt handling adds latency on some platforms.
5. Re-run LatencyMon after each change; firmware fixes often show the most dramatic improvements.

### Fix 6: Reduce background interrupt load

Fewer interrupts competing means lower worst-case latency.

1. Open **Settings** > **Apps** > **Startup** and disable everything non-essential — fewer background apps means fewer drivers being exercised. See [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) for details.
2. Pause antivirus real-time protection briefly for a LatencyMon test run (re-enable immediately after). If DPC drops, configure the AV's exclusions or gaming/silent mode rather than leaving protection off.
3. Disable Windows' **SysMain** (Superfetch) service if disk-related DPC is high: run `services.msc`, find **SysMain**, set to **Disabled**.
4. Close RGB control software, hardware monitoring tools, and overlays — these poll hardware constantly and generate interrupt traffic.
5. For persistent cases, Microsoft documents interrupt and performance troubleshooting at Windows support, and the Update Catalog can provide specific driver versions to test.

## Closing

High DPC latency feels mysterious but resolves methodically: LatencyMon identifies the guilty driver, proper vendor drivers replace the generic ones, and power-saving tweaks remove the wake-up penalties. Measure before and after each change, and you'll convert crackling audio and stuttering games back into the smooth experience your hardware is capable of.
