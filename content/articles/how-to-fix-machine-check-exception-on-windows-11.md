---
title: "MACHINE_CHECK_EXCEPTION on Windows 11: Fix It Step by Step"
slug: how-to-fix-machine-check-exception-on-windows-11
date: 2026-10-01
categories: ["windows-errors"]
tags: ["blue screen", "hardware", "windows 11"]
description: "MACHINE_CHECK_EXCEPTION on Windows 11 means your CPU reported a hardware fault. Follow this Windows 11-specific guide to find and fix the cause."
thumbnail: "/images/thumbs/how-to-fix-machine-check-exception-on-windows-11.webp"
faqs:
  - q: "What does MACHINE_CHECK_EXCEPTION mean on Windows 11?"
    a: "Stop code 0x0000009C: your CPU detected a hardware error and reported it. It's a hardware-origin crash — processor, RAM, motherboard, or power. Windows 11's virtualization-based security can occasionally complicate diagnosis, so this guide covers the Win11-specific angles."
  - q: "Can Windows 11 features like Memory Integrity cause this?"
    a: "Rarely directly, but virtualization-based security changes how the CPU handles certain operations, and on marginal hardware it can expose faults that stayed hidden before. Toggling Memory Integrity temporarily is a valid diagnostic step."
  - q: "How is this different from WHEA_UNCORRECTABLE_ERROR?"
    a: "They're siblings — both are CPU-reported hardware errors. WHEA_UNCORRECTABLE_ERROR (0x124) is the newer Windows Hardware Error Architecture path; MACHINE_CHECK_EXCEPTION (0x9C) is the older machine-check path. Diagnosis is nearly identical for both."
  - q: "Should I update to 24H2 to fix this?"
    a: "Not as a fix by itself — a hardware fault won't be cured by a feature update. But 24H2 includes newer CPU microcode delivery, so being current doesn't hurt. Fix the hardware first, update second."
---
MACHINE_CHECK_EXCEPTION (stop code 0x0000009C) is your CPU raising its hand and saying "something in the hardware just went wrong." It's not a driver guess — it's a processor-detected fault in the CPU, RAM, motherboard, or power delivery. This guide is tuned for Windows 11 specifically, covering the Win11 settings and features that affect diagnosis.

If you're on Windows 10, see our [Windows 10 edition](/articles/how-to-fix-machine-check-exception-on-windows-10/) — the hardware tests are the same but the settings paths differ. Either way, back up your data first: hardware faults can escalate.

## Why this happens

- **Overheating CPU.** Still the number-one fixable cause on laptops.
- **Failing RAM.** Bad memory triggers machine checks on access.
- **Unstable overclock or undervolt.** Common on performance-tuned laptops.
- **Motherboard power delivery degradation.** Aging VRMs cause voltage instability.
- **Failing charger or battery.** Power droops under load trip the CPU's fault detection.
- **Outdated BIOS/microcode.** Firmware bugs cause false or genuine machine checks.
- **Windows 11 VBS exposing marginal hardware.** Virtualization-based security stresses the CPU differently.

## How to fix it

Work through these in order — diagnose before replacing.

### Fix 1: Monitor thermals with Windows 11 tools

Start with heat — it's the most common and cheapest fix.

1. Open **Settings > System > Power & battery** and note your current **Power mode**.
2. Install HWiNFO or HWMonitor and watch CPU temperatures at idle (expect 40-55°C) and under load.
3. Sustained load temperatures above 90-95°C cause exactly these faults.
4. Clean the vents with compressed air and elevate the laptop for airflow.
5. Set **Power mode** to **Balanced** temporarily — **Best performance** on a dusty laptop is a recipe for thermal faults.
6. If cooling fixes it, consider a cooling pad and a repaste schedule for older machines.

### Fix 2: Temporarily disable Memory Integrity for diagnosis

Windows 11's virtualization-based security can expose marginal hardware.

1. Open **Settings > Privacy & security > Windows Security > Device security > Core isolation details**.
2. Toggle **Memory integrity** off.
3. Restart when prompted.
4. Use the laptop normally for a day. If machine checks stop, VBS was exposing a hardware marginality — the hardware is still marginal, so continue diagnosing rather than celebrating.
5. You can re-enable Memory integrity after fixing the root cause; don't leave security features off permanently without reason.
6. Microsoft documents Core isolation behavior on [support.microsoft.com](https://support.microsoft.com/en-us/windows) if you want the background.

### Fix 3: Reset tuning and power settings to stock

Eliminate unstable configurations.

1. Reset any undervolts/overclocks in ThrottleStop, Intel XTU, or manufacturer utilities.
2. In BIOS/UEFI, load optimized defaults.
3. Disable XMP/DOCP memory profiles for testing.
4. In **Settings > System > Power & battery**, use **Balanced** power mode.
5. In **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **Processor power management** and set **Maximum processor state** to **99%** temporarily — this disables Turbo Boost, a useful diagnostic for heat-related faults.
6. If crashes stop with Turbo off, thermals or power delivery are confirmed culprits.

### Fix 4: Test memory with Windows Memory Diagnostic

Bad RAM is the second most common cause.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. After reboot, check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
4. For certainty, run MemTest86 from a bootable USB overnight (4+ passes).
5. Replace faulty sticks with the correct spec — check the laptop manual.
6. If RAM is soldered and faulty, back up immediately and arrange board-level service.

### Fix 5: Update BIOS, chipset, and microcode

Firmware fixes resolve whole classes of machine checks.

1. Check your BIOS version: **Win + R** > `msinfo32` > **BIOS Version/Date**.
2. Download the latest BIOS and chipset driver from your laptop maker's support site.
3. Install chipset first, then BIOS — charger connected, never interrupt.
4. Also run **Settings > Windows Update** and install everything, including optional updates — Windows delivers CPU microcode updates this way too. The [Update Catalog](https://www.catalog.update.microsoft.com/) lets you manually fetch specific microcode packages if needed.
5. Load BIOS defaults after updating.
6. Monitor for several days under normal workloads.

### Fix 6: Read the WHEA-Logger entries

Windows 11 logs hardware errors in detail — use them.

1. Open **Event Viewer** (**Win + X > Event Viewer**).
2. Navigate to **Windows Logs > System**, filter by source **WHEA-Logger**.
3. Open recent entries; the **Details** tab often identifies the component — a specific processor core (APIC ID), a memory bank, or a PCIe device.
4. Consistent single-core errors suggest CPU degradation — minimize heavy loads and plan for service.
5. Memory-bank errors point back to Fix 4's RAM testing.
6. PCIe errors (GPU/SSD) mean updating that device's driver and firmware. Compare with our [WHEA_UNCORRECTABLE_ERROR guide](/articles/whea-uncorrectable-error-windows-11-fix/) for the newer error path.

### Fix 7: Isolate power and minimal hardware

The final elimination before a service verdict.

1. Test with the original OEM charger on a wall outlet — no power strips, no third-party adapters.
2. Check battery health:
   `powercfg /batteryreport`
   Compare **Design Capacity** vs **Full Charge Capacity** in the generated report.
3. Disconnect all USB devices and docks.
4. If RAM is socketed, test one stick at a time.
5. If machine checks persist at stock settings, good thermals, tested RAM, current firmware, and clean power, the fault is in the CPU or motherboard.
6. Export your WHEA logs from Event Viewer (**Save All Events As**) and bring them to service — documented evidence gets faster, more accurate repairs.

## Closing

On Windows 11, MACHINE_CHECK_EXCEPTION diagnosis follows the same hardware logic as ever, with two Win11 twists: check Memory Integrity's role early, and use the modern Settings paths for power management. Work the ladder — cooling, clocks, memory, firmware, power — and let the WHEA logs name the component when they can. Most cases end at thermals or RAM; the ones that don't end at a service bench with good documentation in hand. Resist the temptation to keep using a machine that throws machine checks daily — every fault is a small gamble with your data, and backups are far cheaper than recovery.
