---
title: "WHEA_UNCORRECTABLE_ERROR? Here's What to Do on Windows 11"
slug: what-to-do-if-whea-uncorrectable-error
date: 2026-10-09
categories: ["windows-errors"]
tags: ["whea uncorrectable error", "bsod", "hardware error", "0x124", "windows 11"]
description: "WHEA_UNCORRECTABLE_ERROR (0x124) is a hardware error report from your CPU. Here's what to do — read the error record, then work thermals, firmware, and hardware."
thumbnail: "/images/thumbs/what-to-do-if-whea-uncorrectable-error.webp"
faqs:
  - q: "What does WHEA_UNCORRECTABLE_ERROR mean?"
    a: "Stop code 0x124 means the Windows Hardware Error Architecture received a fatal hardware error report — usually from the CPU, but also from memory, PCIe devices, or the chipset. 'Uncorrectable' means the hardware's own error correction couldn't fix it. Unlike most blue screens, this one genuinely starts at hardware, though outdated firmware and drivers can create the conditions that trigger it."
  - q: "How do I find out which hardware component caused it?"
    a: "Open the crash dump in WinDbg and run '!analyze -v', then examine the WHEA error record with '!errrec' on the record address. The record identifies the error source (processor, memory, PCIe) and often the specific bank or device. Windows Event Viewer also logs WHEA-Logger entries with the same details in a more readable form. The record is the difference between guessing and knowing."
  - q: "Can overclocking cause WHEA_UNCORRECTABLE_ERROR?"
    a: "Yes — it's one of the most common causes. Unstable CPU overclocks, aggressive undervolts, and XMP memory profiles that the silicon can't sustain all produce exactly the hardware errors WHEA reports. Reset everything to stock clocks first; if the crashes stop, your tuning was the cause. This applies to factory 'performance enhancement' BIOS modes too, not just manual overclocks."
  - q: "Is my CPU dying if I get this error?"
    a: "Probably not. CPUs are extremely reliable; far more common are overheating, unstable tuning, outdated BIOS microcode, failing RAM, or power delivery issues — all of which the CPU dutifully reports through WHEA. Work through thermals, stock clocks, firmware updates, and memory tests before even considering CPU failure. The error is the messenger, not the diagnosis."
---

WHEA_UNCORRECTABLE_ERROR — stop code 0x124 — is the blue screen that starts with hardware. WHEA (Windows Hardware Error Architecture) is the system through which your CPU, memory, and PCIe devices report errors they detect in themselves. When one reports an error its own correction mechanisms couldn't fix, Windows halts. There's no driver to blame here in the usual sense — though drivers and firmware can absolutely create the conditions for the error.

The good news: WHEA errors come with receipts. Every 0x124 crash includes a detailed error record identifying the source — processor cache, memory, PCIe bus, and often the specific component. Most people never read it and start replacing parts at random. Don't. Read the record, then work the proven order: reset tuning, check thermals, update firmware and drivers, test memory and power. The CPU is the messenger; shoot the actual problem.

## Why this happens

- **Unstable overclock or undervolt**: The top cause — tuning pushed past stability produces the exact hardware errors WHEA reports.
- **CPU overheating**: Thermal overload causes internal errors that error-correction can't fix.
- **Outdated BIOS/microcode**: Old firmware mismanages the CPU; microcode updates fix entire classes of false hardware errors.
- **Failing RAM**: Memory errors reported through WHEA's memory error source.
- **PCIe device errors**: Failing GPUs, NVMe drives, or docks reporting bus errors.
- **Power delivery instability**: Voltage dips from failing chargers, batteries, or motherboard VRMs.
- **Genuinely failing CPU or motherboard**: Real, but the least common cause — diagnose everything else first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the WHEA error record

The record names the failing component — start with evidence, not guesses.

1. Open the latest minidump in WinDbg Preview and run `!analyze -v`.
2. Find the WHEA error record address in the output and run `!errrec <address>` — read the **Error Source** (Processor, Memory, PCI Express) and the specific details (cache bank, DIMM, device).
3. Simpler alternative: open **Event Viewer** > **Windows Logs** > **System**, filter for **WHEA-Logger** events around the crash time — the details tab contains the same record in readable form.
4. Processor/cache errors → focus on tuning, thermals, CPU power. Memory errors → RAM testing. PCIe errors → the named device (GPU, SSD, dock). Let the record direct you.

### Fix 2: Reset all tuning to stock immediately

The most common cause gets the first fix.

1. Enter BIOS/UEFI → **Load Optimized Defaults**. This clears CPU overclocks, undervolts, XMP/DOCP profiles, and multi-core enhancement modes.
2. Reset XTU, ThrottleStop, Ryzen Master, and vendor tuning tools to stock.
3. Retest with the workload that crashed. If crashes stop — and they often do right here — tuning was the cause.
4. Note the lesson: undervolts degrade with silicon aging. What was stable for a year can become a WHEA generator. Re-tune conservatively or not at all.

### Fix 3: Check thermals under load

Heat produces the errors WHEA reports — measure it.

1. Install HWiNFO64, enable logging, and run the crashing workload for 15–20 minutes while recording CPU temperatures.
2. Sustained 95–100°C+ on laptop CPUs is where uncorrectable errors begin. Note whether crashes correlate with temperature peaks in your log.
3. Clean vents/fans with compressed air, use hard surfaces, consider a cooling pad — then retest and compare logs.
4. For older laptops, dried thermal paste is a prime suspect — a professional repaste often resolves thermally-triggered WHEA errors completely.

### Fix 4: Update BIOS and chipset drivers

Firmware fixes hardware-error false positives regularly.

1. Check your BIOS version in `msinfo32`; download the latest for your exact model from Dell, HP, or Lenovo.
2. Read release notes for microcode updates, stability fixes, or CPU power management changes — directly relevant to WHEA.
3. Flash on AC power, uninterrupted. Load optimized defaults after.
4. Update the chipset driver from the same source, or [Intel](https://www.intel.com/content/www/us/en/support/detect.html)/AMD. Retest the crashing workload after both.

### Fix 5: Test memory (for memory-source records) and PCIe devices

Follow the error record's direction.

1. If the record implicates memory: run MemTest86 from USB, 4+ passes overnight, at stock memory speeds. Replace confirmed-bad sticks.
2. If it implicates PCIe: identify the device — GPU, NVMe SSD, Thunderbolt dock. Update that device's driver and firmware; test with the device removed/disabled if possible.
3. For GPU-implicated errors: clean-install the graphics driver ([NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, Intel) and monitor GPU temperatures — overheating GPUs report PCIe errors.
4. For dock-implicated errors: update dock firmware and test undocked. Docks are frequent WHEA-PCIe sources.

### Fix 6: Verify power delivery

Voltage instability creates hardware errors that look like component failure.

1. Test the crashing workload on the original manufacturer charger, then on battery alone — note any difference.
2. Run `powercfg /batteryreport` and compare design vs. full-charge capacity. A battery under 50% of design capacity can destabilize the power rail.
3. Inspect the charging port for looseness; wiggle-test gently while monitoring for errors.
4. Third-party chargers with poor voltage regulation under load are a documented WHEA trigger — test exclusively with the OEM charger during diagnosis.

### Fix 7: Stress-test to reproduce deliberately

Confirm the diagnosis under controlled conditions.

1. With stock clocks, current BIOS, and clean thermals, run Prime95 (small FFTs) for CPU-focused errors or FurMark for GPU-implicated ones, 15–20 minutes each.
2. Reproduces under synthetic load? You've confirmed load-dependent hardware/firmware behavior — the record's component is genuinely implicated.
3. Passes synthetics but crashes in normal use? Look for software triggers — a specific driver or application provoking the error. Clean-boot to isolate.
4. Log everything: temperatures, clocks, BIOS version, test outcomes. This log is what warranty support needs. For the machine-check cousin of this error, our [troubleshooting guide](/articles/how-to-fix-machine-check-exception-in-windows-11-24h2/) covers the parallel diagnostic path.

### Fix 8: Pursue warranty or professional repair with evidence

Hardware verdicts require hardware evidence — bring yours.

1. Compile: WHEA record details, stock-clock test results, thermal logs, BIOS version, MemTest86 results, charger tests.
2. Under warranty: contact manufacturer support with this package. Documented 0x124 at stock settings with clean thermals and passing RAM means motherboard/CPU replacement under most warranties.
3. Out of warranty: get a board-level repair quote vs. replacement cost. On 4–5+ year old laptops, replacement usually wins.
4. Check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known WHEA issues in your Windows build as a final software sanity check — rare, but documented.

## Closing

WHEA_UNCORRECTABLE_ERROR is hardware reporting on itself — and the report includes the details you need, if you read the error record instead of guessing. Reset tuning first (it's the cause most of the time), verify thermals, update firmware, then follow the record to memory, PCIe, or power testing. The CPU is almost never dying; it's overheating, over-tuned, under-powered, or running ancient microcode. Fix the conditions, read the receipts, and the uncorrectable errors stop. For the older machine-check variant of the same problem class, our [companion fix guide](/articles/whea-uncorrectable-error-windows-11-fix/) approaches from the repair angle.
