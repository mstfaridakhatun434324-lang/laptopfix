---
title: "MACHINE_CHECK_EXCEPTION on Windows 10: Diagnosis and Fixes"
slug: how-to-fix-machine-check-exception-on-windows-10
date: 2026-09-24
categories: ["windows-errors"]
tags: ["blue screen", "hardware", "windows 10"]
description: "MACHINE_CHECK_EXCEPTION means your CPU caught a hardware fault on Windows 10. Learn to identify the failing component and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-machine-check-exception-on-windows-10.webp"
faqs:
  - q: "What does MACHINE_CHECK_EXCEPTION mean?"
    a: "It's stop code 0x0000009C — the CPU itself detected a hardware error and reported it to Windows. Unlike most blue screens, this one originates in hardware: the processor, RAM, motherboard, or power delivery. Software fixes help only when a driver is provoking the hardware fault."
  - q: "Is this error always a hardware failure?"
    a: "Almost always, yes. Overheating, failing RAM, a dying motherboard, or unstable power are the usual causes. The exception is overclocking — an unstable overclock triggers genuine machine checks that vanish at stock settings."
  - q: "How do I find which hardware component is failing?"
    a: "Check Event Viewer for WHEA-Logger entries — they often name the component (processor core, memory, PCIe). Then test systematically: memory test, temperature monitoring, and trying known-good RAM if available. The WHEA error record is your best clue."
  - q: "Can I still use my laptop while diagnosing this?"
    a: "Light use is fine, but back up your data immediately — hardware faults can escalate. Avoid heavy workloads until you've identified the cause, since stress can turn an intermittent fault into a permanent one."
---
MACHINE_CHECK_EXCEPTION (stop code 0x0000009C) is different from most blue screens: it isn't Windows guessing about a driver — it's your CPU reporting that it caught a hardware error in the act. On Windows 10 laptops, this usually means the processor, memory, motherboard, or power system has a real problem. That sounds dire, but the fix ranges from "clean the vents" to "replace the RAM," and this guide helps you figure out which.

Start by backing up your data. Hardware faults can worsen, and you don't want to lose files mid-diagnosis. Then work through the steps. If your crashes name WHEA instead, see our [WHEA_UNCORRECTABLE_ERROR guide](/articles/whea-uncorrectable-error-windows-11-fix/) — the two are close cousins.

## Why this happens

- **Overheating CPU.** Thermal faults are the most common and most fixable cause.
- **Failing RAM.** Bad memory triggers machine checks when the CPU accesses faulty cells.
- **Unstable overclock.** Overclocked CPUs or RAM produce genuine hardware errors.
- **Failing motherboard.** Degraded VRMs or capacitors cause voltage instability the CPU detects.
- **Power supply issues.** A failing charger or battery causes voltage droops under load.
- **Outdated BIOS.** Firmware bugs in CPU microcode can cause false machine checks.
- **Driver provoking hardware.** Rare, but a bad driver can push hardware into fault states.

## How to fix it

Work through these in order — diagnose before replacing anything.

### Fix 1: Check temperatures and cooling

Heat is the first suspect because it's the easiest to fix.

1. Install HWMonitor or HWiNFO from their official sites.
2. Monitor CPU temperatures during normal use and under load (open several heavy apps or run a stress test briefly).
3. Idle temps should be 40-55°C; sustained load above 90-95°C is dangerous.
4. Blow dust from vents with compressed air — short bursts, can upright.
5. Make sure the laptop sits on a hard flat surface; elevate the rear slightly for airflow.
6. If fans don't spin up under load, check **Control Panel > Power Options > Change plan settings > Change advanced power settings > Processor power management** — and inspect the fans physically. On Windows 10, also verify the active power plan isn't throttling the fan curve oddly.

### Fix 2: Reset all overclocks to stock

If anything is tuned, untune it.

1. Reset any CPU/RAM overclocks in BIOS/UEFI to defaults (**F9** loads defaults in most BIOS setups).
2. If you use Intel XTU, ThrottleStop, or Ryzen Master, reset all profiles to stock and uninstall the tool temporarily.
3. Disable XMP/DOCP memory profiles in BIOS — run RAM at JEDEC standard speeds for testing.
4. Save BIOS settings and reboot.
5. Use the laptop normally for a day. If machine checks stop, the overclock was unstable — keep stock settings or retune conservatively.
6. Document your old settings first if you plan to retune later.

### Fix 3: Test the memory thoroughly

Bad RAM is the second most common cause.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the full test complete, then check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
4. For a definitive test, run MemTest86 from a bootable USB for at least 4 passes (several hours).
5. If errors appear, test sticks individually if your laptop has two slots — this identifies the bad one.
6. Replace faulty RAM with the exact spec your laptop requires (check the manufacturer's manual for speed and voltage). Also see our [memory-focused blue screen guide](/articles/how-to-fix-memory-management-bsod-on-asus-laptop/) for related stop codes.

### Fix 4: Update the BIOS and chipset drivers

Firmware fixes resolve microcode-level machine checks.

1. Go to your laptop maker's support site and find your exact model.
2. Check the current BIOS version: press **Win + R**, type `msinfo32`, and look at **BIOS Version/Date**.
3. If a newer BIOS exists, download it. Read the release notes for mentions of stability or microcode fixes.
4. Install with the charger plugged in and battery charged — never interrupt a BIOS update.
5. Also install the latest chipset driver from the same support page.
6. After updating, load BIOS defaults, reboot, and monitor. Microsoft's [Windows 10 update catalog](https://www.catalog.update.microsoft.com/) can also supply microcode updates via Windows Update — make sure updates are current.

### Fix 5: Check the WHEA error records

Let Windows tell you which component complained.

1. Open **Event Viewer** (**Win + X > Event Viewer**).
2. Go to **Windows Logs > System** and filter for source **WHEA-Logger**.
3. Open the most recent entries — the **General** tab describes the error, and **Details** may name the component (processor core APIC ID, memory bank, or PCIe device).
4. If it consistently names a specific CPU core, the processor may be degrading — reduce load and plan for service.
5. If it names memory, focus on Fix 3's RAM testing.
6. If it names a PCIe device (often the GPU or SSD), update that device's driver and firmware.

### Fix 6: Test with known-good power

Rule out the charger and battery.

1. Use only the original OEM charger with the correct wattage.
2. Try running with the battery removed if your laptop allows it (many modern ones don't — skip if sealed).
3. Test on a different wall outlet, avoiding overloaded power strips.
4. In **Control Panel > Power Options**, switch to the **Balanced** plan temporarily — High Performance can expose marginal power delivery.
5. If crashes only happen on battery, the battery may be failing — check its health report:
   `powercfg /batteryreport`
   Open the generated HTML file and check **Design Capacity** vs **Full Charge Capacity**.
6. A swollen battery is a safety hazard — stop using it and have it replaced professionally.

### Fix 7: Strip down to minimal hardware

Isolate the failing component by elimination.

1. Disconnect all USB devices, docks, and external drives.
2. If your laptop has two RAM sticks, remove one and test; then swap.
3. Remove any aftermarket SSD or Wi-Fi card you installed, reverting to stock if possible.
4. Boot with minimal hardware and stress lightly. If machine checks stop, reintroduce components one at a time.
5. If the error persists with minimal hardware, stock BIOS, clean cooling, and good RAM, the fault is in the CPU, motherboard, or soldered components.
6. At that point, professional board-level diagnosis is needed — bring your WHEA logs (export them from Event Viewer) to speed up the repair.

## Closing

MACHINE_CHECK_EXCEPTION is your CPU telling the truth about broken hardware, so take it seriously but diagnose methodically: cooling, clocks, memory, firmware, power — in that order. Most cases resolve at the thermal or RAM stage without a repair shop. Keep those WHEA-Logger entries; they're the closest thing to a confession your hardware will ever give you, and any technician will thank you for them.
