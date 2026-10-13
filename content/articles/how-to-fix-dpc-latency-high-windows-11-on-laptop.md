---
title: "How to Fix High DPC Latency on a Windows 11 Laptop"
slug: how-to-fix-dpc-latency-high-windows-11-on-laptop
date: 2026-09-15
categories: ["performance"]
tags: ["dpc latency", "audio glitches", "windows 11", "drivers", "stutter"]
description: "Audio crackling, mouse stuttering, dropouts? High DPC latency is the hidden cause — measure it and fix the offending driver."
thumbnail: "/images/thumbs/how-to-fix-dpc-latency-high-windows-11-on-laptop.webp"
faqs:
  - q: "What is DPC latency in simple terms?"
    a: "DPC (Deferred Procedure Call) latency measures how long drivers take to finish their interrupt work. When a driver takes too long — say, 2 milliseconds instead of 0.05 — everything else in the system waits, causing audio crackles, mouse cursor jumps, and video micro-stutters. It's measured in microseconds; spikes above 1000µs are where humans start noticing problems."
  - q: "What DPC latency numbers are good or bad?"
    a: "Under 200µs average with rare spikes under 500µs is excellent. Occasional spikes to 1000µs are tolerable for most use. Sustained spikes above 2000µs cause audible audio glitches; above 5000µs you'll see mouse and UI stutter too. For professional audio work (DAWs), you want everything under 500µs — that's why musicians obsess over this metric."
  - q: "Can DPC latency cause game stuttering?"
    a: "Yes — it's a classic hidden cause of micro-stutter that FPS counters don't explain. A driver holding the system for milliseconds at a time makes frames arrive late even when the GPU is fast. If your games stutter despite good FPS and the usual fixes failed, DPC latency from a network, storage, or power-management driver is a prime suspect."
  - q: "Is high DPC latency a hardware or software problem?"
    a: "Overwhelmingly software — specifically, buggy or outdated drivers. The hardware is fine; a driver is just taking too long in its interrupt handler. That's good news: driver updates, disabling the offending device, or changing power settings usually fix it without touching hardware. True hardware-caused DPC issues (failing devices spamming interrupts) are rare."
---

DPC latency is the performance problem most people have never heard of — and it's behind a huge share of "mysterious" issues: audio that crackles and pops, a mouse cursor that jumps, video that micro-stutters despite a fast GPU, dropouts in music production. The symptoms feel like hardware failure, but the cause is almost always one misbehaving driver holding the system hostage for milliseconds at a time.

The fix process is beautifully scientific: measure with LatencyMon, identify the offending driver by name, update/disable/reconfigure it, re-measure. No guesswork. This guide walks through exactly that. For the related kernel-CPU issue, see [fixing ntoskrnl.exe high CPU](/articles/best-way-to-fix-ntoskrnl-exe-high-cpu-usage/); for general game stutter, [Windows 11 stutter fixes](/articles/best-way-to-fix-windows-11-stuttering-in-games/).

## Why this happens

- **Buggy network drivers**: Wi-Fi drivers are the number-one DPC latency offenders on laptops — power-saving polling gone wrong.
- **Storage driver issues**: Outdated Intel RST or NVMe drivers with long interrupt handlers.
- **GPU driver power management**: Drivers slow to switch power states, stalling the system during transitions.
- **USB controller drivers**: Problematic USB 3.x drivers, especially with certain docks and peripherals attached.
- **Power management transitions**: CPU C-state and PCIe link-state changes adding latency spikes.
- **Antivirus filter drivers**: Real-time AV hooking I/O paths with expensive handlers.
- **Failing hardware spamming interrupts**: A dying device generating interrupt storms (rare, but real).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure with LatencyMon

Get the numbers and the name.

1. Download **LatencyMon** (Resplendence, free) — run it as Administrator and click the **play** button to start monitoring.
2. Let it run for 10 minutes during normal use (include the activity that glitches — play audio, move the mouse, game briefly).
3. Read the **Main** tab: **Highest reported DPC routine execution time** and which driver caused it — LatencyMon names names (e.g., `ndis.sys`, `storport.sys`, `nvlddmkm.sys`, `tcpip.sys`).
4. Check the **Drivers** tab sorted by **DPC count** and **Highest execution** — the top offender is your target. Screenshot everything.
5. Note the pattern: constant high DPC = a driver always misbehaving; periodic spikes = power-state transitions or polling (Fixes 3–4).

### Fix 2: Update the offending driver

The fix for the majority of cases.

1. Identify the driver file from LatencyMon (e.g., `Netwtw10.sys` = Intel Wi-Fi, `rtwlanu.sys` = Realtek, `storahci.sys` = storage).
2. Get the update from the right source: your laptop vendor's support site first ([Dell](https://www.dell.com/support), HP's support site, Lenovo's support site), then the chip vendor ([Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html)) if the OEM version is old.
3. For Wi-Fi offenders specifically: update both the **Wi-Fi driver** and **Bluetooth driver** — they share the radio and the driver package, and Bluetooth's polling is a frequent hidden contributor.
4. For GPU offenders (`nvlddmkm.sys`, `amdkmdag.sys`): clean-install the latest driver (DDU in Safe Mode, then fresh install) — DPC issues often come from driver upgrades layered over old remnants.
5. Re-run LatencyMon for 10 minutes after each driver update — verify the specific offender's numbers dropped, don't just assume.

### Fix 3: Tame Wi-Fi power saving (the classic)

The number-one DPC latency fix on laptops.

1. **Device Manager** > **Network adapters** > your Wi-Fi adapter > **Properties** > **Advanced** tab — set **Power Saving Mode** / **Roaming Aggressiveness** to **Maximum Performance**; disable **U-APSD** / **WMM-PS** power-save features.
2. **Power Management** tab (same device) — uncheck **Allow the computer to turn off this device to save power**. The power-state transitions of the Wi-Fi radio are a legendary DPC spike source.
3. `powercfg.cpl` > advanced settings > **Wireless Adapter Settings** > **Power Saving Mode** > **Maximum Performance** (plugged in).
4. Re-run LatencyMon — Wi-Fi-related DPC spikes often collapse immediately after these changes.
5. If you use the laptop mostly docked on Ethernet, disable the Wi-Fi adapter entirely when docked (**Device Manager** > right-click > **Disable device**) — a disabled radio generates zero DPC.

### Fix 4: Disable CPU power-state transitions (diagnostic)

Proving whether C-states are the spiker.

1. Periodic DPC spikes (every few seconds, rhythmic) scream power-state transitions — CPU C-states or PCIe link-state changes.
2. Test: `powercfg.cpl` > advanced > **Processor power management** > **Minimum processor state** = **100%** (plugged in) — this keeps the CPU from deep-sleeping between tasks.
3. Also set **PCI Express** > **Link State Power Management** = **Off**.
4. Re-run LatencyMon — if spikes vanish, power management was the cause. You can then experiment with intermediate settings (minimum 50%, link-state moderate) to find the sweet spot between latency and battery.
5. For DAW/audio work, many professionals run a dedicated **high-performance power plan** with these disabled permanently — latency matters more than battery when recording.

### Fix 5: Address storage and USB offenders

For storport/USB-related DPC.

1. If LatencyMon blames `storport.sys`, `stornvme.sys`, or similar: update **chipset** and **storage drivers** (Intel RST, AMD chipset) from the vendor.
2. Check SSD firmware — storage DPC issues sometimes trace to firmware-level interrupt behavior; update via the maker's utility.
3. For USB offenders (`USBXHCI.sys`): update chipset drivers, and test with USB peripherals disconnected — a specific device (often an audio interface or dock) can trigger the controller's bad behavior.
4. In **Device Manager** > **Universal Serial Bus controllers**, check each hub's **Power Management** — uncheck **Allow the computer to turn off this device** for the xHCI controller as a test.
5. If a USB audio interface is involved: try different USB ports (different controllers), and check the interface maker's site for driver/firmware updates — audio interfaces are exquisitely sensitive to DPC.

### Fix 6: Check antivirus and filter drivers

The invisible interrupt tax.

1. LatencyMon blaming `fltMgr.sys` or AV filter drivers (names containing your AV vendor) means file-system filter overhead.
2. Test: temporarily disable real-time protection and re-run LatencyMon — a dramatic drop confirms AV involvement.
3. The fix isn't disabling AV permanently — it's updating the AV (filter driver fixes ship regularly) or switching to a product with lighter filters. Windows Defender's filters are generally well-behaved when updated.
4. Also audit other filter drivers: VPN clients, disk encryption (non-BitLocker), and backup software all install filters — LatencyMon's Drivers tab shows their DPC contribution; disable suspects one at a time.
5. Keep only the filters you need — each one adds latency to every I/O operation, and they stack.

### Fix 7: BIOS update and hardware verdict

When drivers don't explain it.

1. Check your BIOS version against the vendor's latest — BIOS/UEFI updates regularly fix interrupt routing, ACPI, and power-management issues that manifest as DPC latency. Follow the vendor's flash instructions with the charger connected.
2. In BIOS setup, look for **Intel SpeedStep / Speed Shift**, **C-states**, and **ASPM** options — disabling deep C-states here is the firmware-level version of Fix 4 (use for testing; re-enable selectively).
3. If one specific device (a failing drive, a flaky Wi-Fi card) generates interrupt storms, LatencyMon shows its driver with astronomical DPC counts — **Device Manager** > disable the device as a test; if latency normalizes, the hardware is the problem.
4. For persistent unexplained DPC after all software fixes: run the vendor's hardware diagnostics (Dell F12 diagnostics, Lenovo Vantage hardware scan, HP UEFI diagnostics).
5. True hardware DPC causes are rare — but when LatencyMon keeps naming the same driver across three driver versions and two Windows installs, the device underneath is telling you something. Microsoft documents interrupt/latency troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

High DPC latency is the rare performance problem with a perfect diagnostic loop: LatencyMon names the driver, you update or reconfigure that driver, LatencyMon confirms the fix. No guessing, no registry voodoo — just measurement and targeted action. The audio stops crackling, the mouse stops jumping, and the stutter you couldn't explain finally has a name and a fix. For a problem this annoying, the solution is refreshingly scientific.
