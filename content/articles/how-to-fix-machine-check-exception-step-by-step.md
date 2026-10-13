---
title: "Machine Check Exception: A Step-by-Step Fix Guide"
slug: how-to-fix-machine-check-exception-step-by-step
date: 2026-10-08
categories: ["windows-errors"]
tags: ["machine check exception", "hardware diagnostic", "bsod"]
description: "A careful step-by-step walkthrough for MACHINE_CHECK_EXCEPTION — diagnose the hardware fault behind it without skipping or guessing."
thumbnail: "/images/thumbs/how-to-fix-machine-check-exception-step-by-step.webp"
faqs:
  - q: "What is the very first step for MACHINE_CHECK_EXCEPTION?"
    a: "Check cooling. Shut down, clean the vents with compressed air, and make sure the laptop sits on a hard surface with unblocked intakes. Overheating is the most common cause, and it costs nothing to rule out before you touch software or run long diagnostics."
  - q: "How long does diagnosing this error take?"
    a: "The quick checks — cooling, BIOS settings, driver updates — take under an hour. Memory testing with MemTest86 needs several hours (run it overnight). Manufacturer extensive diagnostics take 2-4 hours. Plan for the quick wins first; most cases resolve there."
  - q: "Do I need any special tools?"
    a: "No purchases needed. HWMonitor or HWiNFO for temperatures (free), Windows Memory Diagnostic (built in), MemTest86 (free), CrystalDiskInfo (free), and your manufacturer's built-in boot diagnostics cover the entire process. A can of compressed air is the only physical item."
  - q: "When do I stop troubleshooting and call support?"
    a: "Stop when built-in diagnostics report a hardware failure with a failure code, or when you have completed every step here — cooling fixed, clocks stock, BIOS current, RAM tested clean, drivers fresh — and crashes continue. At that point you have a motherboard or CPU fault needing professional repair."
---
MACHINE_CHECK_EXCEPTION deserves a careful, sequential approach because it's the stop code most likely to involve real hardware. Skipping steps or jumping to conclusions wastes time — or worse, leads to replacing parts that were never broken. This guide is the full sequence, each step building on the last, with clear stop points where the evidence tells you what to do next.

Follow it top to bottom. Don't skip the "obvious" cooling step — it resolves more of these than everything else combined.

## Why this happens

- **Overheating CPU.** Thermal faults are the top cause; the CPU's own sensors report the error.
- **Unstable memory clocks (XMP).** Overclocked RAM produces hardware-level errors under load.
- **Outdated BIOS/microcode.** Firmware bugs cause false or mishandled machine checks.
- **Failing RAM modules.** Bad cells trigger genuine machine-check errors.
- **Motherboard faults.** Failing voltage regulation or damaged traces — the professional-repair tier.
- **Degraded thermal paste or failed fans.** Age-related cooling decline on older laptops.

## How to fix it

Work through these in order — each step is a gate; only proceed when the current one checks out clean.

### Fix 1: Inspect and restore cooling

Step one is physical. Do this before touching any software.

1. Power off the laptop completely and unplug it.
2. Blow compressed air through the exhaust vents in short bursts — hold fans still with a toothpick if accessible, since spinning them with air can damage bearings.
3. Check that intake vents on the bottom are unobstructed and the laptop will sit on a hard, flat surface.
4. Power on and install HWMonitor; record idle and load CPU temperatures as your baseline. Anything above 95°C under load needs further cooling work.

### Fix 2: Verify fans and thermal behavior

Confirm the cooling system actually works under stress.

1. Run a demanding task — a game, video render, or stress test — and watch temperatures and fan speed in HWMonitor.
2. Fans should ramp up audibly as temperature climbs; silence under heavy load means a dead fan.
3. If temperatures spike past 95°C within minutes on a clean laptop, the thermal paste may be degraded — on older laptops, a repaste by a repair shop is a routine service.
4. As a temporary measure, limit maximum processor state to 95% in **Power Options > Processor power management** to reduce heat while you arrange a proper fix.

### Fix 3: Reset BIOS to stock settings

Eliminate every configuration variable in one move.

1. Enter the BIOS/UEFI (**F2**, **Del**, or **F10** depending on maker) and choose **Load Optimized Defaults** or **Load Defaults**.
2. Explicitly confirm **XMP/DOCP** is disabled and no CPU overclocking is active.
3. Save and exit.
4. Use the laptop normally for a day of typical workload. If crashes stop here, a setting was the entire problem — reintroduce customizations one at a time if you want them back.

### Fix 4: Update the BIOS and chipset driver

Firmware is the next layer — outdated microcode mishandles machine checks.

1. Note your BIOS version with `msinfo32`.
2. Download the latest BIOS from your laptop maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Flash it with the charger connected, without interruption.
4. Install the latest chipset driver from the same site, restart, and monitor for several days.

### Fix 5: Test the memory systematically

RAM is the next hardware suspect, and testing must be thorough.

1. Run **Windows Memory Diagnostic** for a quick first pass.
2. Create a bootable **MemTest86** USB and run it overnight — at least 4 full passes for intermittent faults.
3. If errors appear, test sticks individually (on models with removable RAM) to identify the bad module.
4. Replace faulty RAM with the correct specification for your laptop. Memory faults here also explain [WHEA_UNCORRECTABLE_ERROR](/articles/whea-uncorrectable-error-windows-11-fix/) crashes — mixed codes strengthen the RAM hypothesis.

### Fix 6: Refresh drivers and check the disk

Cover the remaining software-adjacent causes.

1. Update **storage controller** and **graphics** drivers from the manufacturer — rare, but driver faults can provoke machine checks.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to rule out system corruption.
3. Check SSD health with CrystalDiskInfo; storage faults occasionally surface as machine checks on some platforms.
4. If all software is clean and crashes persist, the evidence points at the motherboard or CPU.

### Fix 7: Run manufacturer diagnostics and escalate

Let the official tools render the verdict.

1. Boot into your maker's diagnostics (Dell: **F12 > Diagnostics**; HP: **F2**; Lenovo: **F10** or Vantage) and run the **extensive** test suite.
2. Record every failure code exactly as displayed.
3. If a component fails, contact the manufacturer's support with those codes — this is now a warranty or professional repair matter.
4. Back up all data before any service visit. If diagnostics pass but crashes continue after every step here, describe the full sequence to support — you've done their tier-one script for them, which gets you escalated faster.

### Fix 8: Check the power supply and battery

Unstable power produces hardware errors the CPU dutifully reports.

1. Always diagnose on the original charger plugged directly into a wall outlet — not a power strip shared with heavy appliances, and not a third-party adapter.
2. Run `powercfg /batteryreport` and check the battery's design vs. full charge capacity; a severely degraded battery can't buffer power dips.
3. If the laptop allows it, test with the battery removed on AC power alone — if crashes stop, the battery is the problem.
4. Inspect the charger's cable and connector for damage, and try a known-good charger of the correct wattage if one's available. Power-related machine checks are intermittent by nature, so give each configuration a few days before judging.

## Closing

The step-by-step discipline is the whole point with MACHINE_CHECK_EXCEPTION: cooling, clocks, firmware, memory, diagnostics — in that order, no skipping. Most cases end at cooling or BIOS settings, which is why the order matters; jumping to RAM replacement first wastes money when the vents were just clogged. Document what you find at each step, and if it ends at the manufacturer's door, you'll arrive with the evidence they need. For the HP-specific variant of this process, see the [HP machine check guide](/articles/how-to-fix-machine-check-exception-on-hp-laptop/).
