---
title: "MACHINE_CHECK_EXCEPTION: The Best Way to Fix It on Windows 11"
slug: best-way-to-fix-machine-check-exception
date: 2026-09-21
categories: ["windows-errors"]
tags: ["machine check exception", "bsod", "hardware error", "windows 11", "cpu"]
description: "MACHINE_CHECK_EXCEPTION (0x9C) means your CPU detected a hardware fault it couldn't correct. Here's the best fix order: drivers, firmware, then hardware tests."
thumbnail: "/images/thumbs/best-way-to-fix-machine-check-exception.webp"
faqs:
  - q: "What causes MACHINE_CHECK_EXCEPTION?"
    a: "Stop code 0x9C fires when the CPU's machine-check architecture detects a hardware error — typically a failing CPU, bad RAM, an overheating processor, an unstable overclock, or a dying motherboard component. Outdated BIOS firmware and buggy chipset drivers can also trigger it by mishandling hardware error reporting. Because it originates in hardware, this is one of the few blue screens where you should take the hardware angle seriously from the start."
  - q: "Can a driver cause MACHINE_CHECK_EXCEPTION?"
    a: "Indirectly, yes. The error itself is hardware-detected, but outdated chipset drivers, storage drivers, or BIOS firmware can cause the conditions that trip it — for example, mishandled power states that destabilize the CPU. That's why the recommended order is drivers and firmware first: they're free to update, and they genuinely resolve a meaningful share of cases before you spend money on hardware."
  - q: "Does MACHINE_CHECK_EXCEPTION mean my CPU is dying?"
    a: "Not necessarily. CPUs are among the most reliable components in a laptop and rarely fail on their own. More common real causes are overheating, unstable overclocks or undervolts, failing RAM, a degraded power delivery system, or outdated BIOS. Only after ruling those out — with temperature monitoring, stock clocks, and memory tests — should you suspect the CPU itself."
  - q: "How is this different from WHEA_UNCORRECTABLE_ERROR?"
    a: "They're cousins. Both report hardware errors detected by the CPU, but WHEA_UNCORRECTABLE_ERROR (0x124) goes through the Windows Hardware Error Architecture with detailed error records, while MACHINE_CHECK_EXCEPTION (0x9C) is the older, rawer machine-check path. In practice you troubleshoot them almost identically: firmware, drivers, thermals, memory, then hardware. Our WHEA guide covers the shared diagnostic approach."
---

MACHINE_CHECK_EXCEPTION — stop code 0x9C — is the blue screen that makes technicians sit up straight. Unlike driver crashes, this one originates in silicon: your CPU's built-in machine-check architecture detected a hardware error serious enough that Windows had no safe way to continue. It's the processor itself raising its hand and saying something is physically wrong.

That sounds dire, and sometimes it is. But "hardware error" covers a wide range, and the most common real-world causes are fixable: an overheating CPU, an unstable overclock or undervolt, outdated BIOS firmware misreporting errors, or failing RAM. Actual dead CPUs are rare — processors are the most reliable part in your laptop. The best approach is a disciplined order: free software and firmware fixes first, then thermal and memory testing, and only then hardware conclusions. Here's that order.

## Why this happens

- **Overheating CPU**: The most common trigger. When the processor exceeds safe temperatures, internal error correction starts failing and the machine-check architecture fires.
- **Unstable overclock or undervolt**: Aggressive tuning pushes the CPU outside its stable envelope. Even "stable" undervolts degrade over time as silicon ages.
- **Outdated BIOS/UEFI firmware**: Old firmware can misconfigure power delivery, misreport hardware errors, or mishandle CPU power states — all of which surface as 0x9C.
- **Failing RAM**: Memory errors detected during CPU operations get reported through the machine-check path, especially on systems without ECC memory.
- **Buggy chipset or storage drivers**: Drivers that mishandle hardware power states can create the electrical conditions for machine-check errors.
- **Degraded power delivery**: A failing charger, worn battery, or damaged motherboard power circuitry causes voltage instability the CPU detects.
- **Genuinely failing CPU or motherboard**: Rare, but possible — especially after physical damage, liquid spills, or years of extreme heat.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check temperatures immediately

Heat is the number one cause, so measure it first.

1. Install HWMonitor or HWiNFO and watch CPU temperatures at idle and under load (open a few heavy apps or run a quick Cinebench test).
2. Idle temps should be 40–60°C; sustained load above 95–100°C on a laptop CPU is thermal throttling territory where machine checks start firing.
3. If temps are high, power off and clean the vents and fans with compressed air, holding fan blades still.
4. Use the laptop on a hard flat surface — beds and couches suffocate intake vents. A cooling pad is a cheap, effective intervention while you work the rest of the list.

### Fix 2: Reset all overclocks and undervolts to stock

Unstable tuning is the second most common cause and the easiest to rule out.

1. Enter BIOS/UEFI setup and choose **Load Optimized Defaults** — this clears CPU overclocks, XMP profiles, and aggressive power settings in one move.
2. If you use Intel XTU, ThrottleStop, or Ryzen Master, reset those profiles to stock as well. Undervolts are a frequent hidden cause: they work for months, then silicon aging makes them unstable.
3. Save, reboot, and use the machine normally for a few days. If the crashes stop, your tuning was the cause — re-tune far more conservatively or leave it stock.

### Fix 3: Update BIOS/UEFI firmware

Firmware updates routinely fix machine-check false positives and power delivery bugs.

1. Identify your exact laptop model, then visit the manufacturer's support page — [Dell](https://www.dell.com/support), HP, or Lenovo.
2. Download the latest BIOS for your exact model. Read the release notes — they often mention "fixes system stability" or "updates CPU microcode," which is directly relevant.
3. Update with the charger plugged in and the battery charged; never interrupt a BIOS flash.
4. After updating, re-check that BIOS settings are sane (load optimized defaults if anything looks odd).

### Fix 4: Update chipset and storage drivers

Drivers that mishandle hardware states can provoke the CPU's error detection.

1. From the same manufacturer support page, download the latest **chipset** driver for your model — don't rely on the generic Windows Update version.
2. Update the storage controller driver (Intel RST, AMD chipset SATA/NVMe) the same way.
3. For AMD systems, get the chipset driver from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html); for Intel, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the right chipset package.
4. Restart and monitor for a few days before declaring victory — machine-check crashes are often intermittent.

### Fix 5: Test the RAM thoroughly

Memory faults are a classic hidden cause of 0x9C.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**, and let it complete.
2. For a definitive test, run MemTest86 from a bootable USB overnight — Windows Memory Diagnostic is decent, but MemTest86 catches marginal faults the quick test misses.
3. If you have two RAM sticks and errors appear, test each stick alone in each slot to isolate whether it's the stick or the slot.
4. Replace any failing memory. On laptops with soldered RAM, this means a motherboard repair — get a quote before assuming it's economical.

### Fix 6: Rule out power delivery problems

Voltage instability trips machine checks, especially under load.

1. Test with the original manufacturer charger — third-party chargers with sagging voltage under load are a known cause.
2. Check the battery's health: open **Terminal** and run `powercfg /batteryreport`, then open the generated HTML report and compare **Design Capacity** against **Full Charge Capacity**.
3. If the battery is severely degraded, test with it disconnected if removable, or have it replaced — a failing battery can destabilize the entire power rail.
4. Inspect the charging port for looseness or damage; intermittent power connections create exactly the voltage dips that trigger machine checks.

### Fix 7: Run a controlled stress test

Once thermals and clocks are sane, verify stability deliberately.

1. With temperatures monitored, run Cinebench or Prime95 (small FFTs) for 15–20 minutes.
2. If the machine-check crash reproduces under synthetic load, you've confirmed it's load-dependent — pointing at thermals, power, or the CPU itself rather than a software fluke.
3. Note the exact conditions: immediate crash suggests severe instability (power or critically bad cooling); crash after 10+ minutes suggests heat soak overwhelming the cooling system.
4. If the system passes stress testing but crashes in normal use, suspect a specific driver or software trigger instead — our [WHEA troubleshooting guide](/articles/how-to-fix-whea-uncorrectable-error-in-windows-11-24h2/) covers the software-side investigation.

### Fix 8: Evaluate hardware replacement

When everything above is exhausted, it's hardware.

1. Document your testing: temperatures, stock clocks, BIOS version, RAM test results, charger tested. A repair shop needs this to avoid repeating your work.
2. If under warranty, contact the manufacturer with your findings — machine-check errors with clean thermals and passing RAM usually mean a motherboard replacement under warranty.
3. Out of warranty, get a repair quote and compare against the laptop's value. CPU/motherboard replacement on a laptop is major surgery; on machines more than 4–5 years old, replacement often makes more financial sense.

## Closing

MACHINE_CHECK_EXCEPTION deserves respect — it's your CPU reporting a real hardware-level problem — but respect doesn't mean panic. The best fix order is thermals first, stock clocks second, firmware and drivers third, and only then the deeper hardware investigation. Most cases resolve in those first steps: a cleaned cooling system, a reset undervolt, or a BIOS update with new CPU microcode. Save the hardware conclusions for last, document everything you test, and remember that CPUs themselves almost never die — it's nearly always the heat, the power, or the tuning around them. For the closely related WHEA variant of this error, our [companion troubleshooting guide](/articles/how-to-fix-machine-check-exception-in-windows-11-24h2/) approaches the same problem from the diagnostic angle.
