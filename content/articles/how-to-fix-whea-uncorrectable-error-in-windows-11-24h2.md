---
title: "WHEA_UNCORRECTABLE_ERROR in Windows 11 24H2: A Hardware-First Fix Guide"
slug: how-to-fix-whea-uncorrectable-error-in-windows-11-24h2
date: 2026-09-27
categories: ["windows-errors"]
tags: ["bsod", "stop code", "24h2", "hardware"]
description: "WHEA_UNCORRECTABLE_ERROR on Windows 11 24H2 means hardware reported a fatal error. Here's how to find the failing part and fix it."
thumbnail: "/images/thumbs/how-to-fix-whea-uncorrectable-error-in-windows-11-24h2.webp"
faqs:
  - q: "What does WHEA_UNCORRECTABLE_ERROR mean?"
    a: "WHEA is the Windows Hardware Error Architecture. This stop code means a hardware component — CPU, RAM, SSD, or another device — reported an error so severe it couldn't be corrected, and Windows crashed. It's one of the few blue screens that genuinely starts with hardware."
  - q: "Can a driver cause WHEA_UNCORRECTABLE_ERROR?"
    a: "Sometimes. Outdated chipset, storage, or BIOS firmware can mishandle hardware error reporting and trigger false WHEA crashes. But unlike most stop codes, the driver-first approach often fails here — test the actual hardware early rather than updating drivers for days."
  - q: "How do I know which hardware part is failing?"
    a: "Check Event Viewer for WHEA-Logger entries (event ID 1, 17, or 18) around the crash time — they name the reporting component. Manufacturer diagnostics (Dell SupportAssist, Lenovo Vantage, HP Hardware Diagnostics) can also pinpoint CPU, RAM, or drive faults."
  - q: "Is my laptop dying if I get this error?"
    a: "Not necessarily. Overheating, unstable overclocks, and outdated BIOS versions cause WHEA crashes on perfectly healthy hardware. But if the error persists at stock settings with current firmware and good cooling, a component is genuinely failing."
---

`WHEA_UNCORRECTABLE_ERROR` is the blue screen most technicians take seriously on sight, because WHEA — the Windows Hardware Error Architecture — is the channel through which your CPU and other components report their own failures. When this stop code appears, some piece of hardware told Windows "something is fatally wrong with me," and Windows believed it.

That doesn't automatically mean buying new parts. Overheating, aggressive overclocks, and ancient BIOS versions all make healthy hardware report errors. The trick is working hardware-first: check thermals and firmware before assuming a component is dead.

## Why this happens

- **Overheating CPU or GPU**: The most common fixable cause. When a processor exceeds safe temperatures, it starts producing computation errors that WHEA reports as uncorrectable.
- **Failing or unstable RAM**: Memory errors that ECC (on systems without it, all of them) can't correct get reported through WHEA. One bad stick is enough.
- **Outdated BIOS/UEFI firmware**: The BIOS mediates hardware error reporting. Old firmware on a new Windows build (like 24H2) can misreport or mishandle errors, causing crashes on healthy hardware.
- **Unstable overclocks or undervolts**: Too-aggressive CPU undervolts (popular for thermals) or RAM overclocks produce exactly the kind of errors WHEA flags.
- **Failing SSD or storage controller**: A drive producing uncorrectable read errors triggers WHEA reports through the storage stack.
- **Loose or failing hardware connections**: On some laptops, a degrading SSD connector or a failing discrete GPU (on models with switchable graphics) is the source.

## How to fix it

Work through these in order — thermals and firmware before parts.

### Fix 1: Check temperatures immediately

Heat is the number-one fixable cause. Don't skip this.

1. Install HWMonitor or HWiNFO (both free) and watch CPU/GPU temperatures during normal use.
2. Sustained CPU temps above 95°C under load, or spikes past 100°C, will absolutely cause WHEA crashes.
3. Clean the vents with compressed air — hold the fan blades still while you blow so you don't overspin them.
4. Replace dried-out thermal paste if the laptop is more than 2–3 years old and runs hot; on many models this drops temps 10–15°C.
5. Use the laptop on a hard flat surface, not a bed or couch. A $20 cooling pad is cheap insurance while you diagnose.

### Fix 2: Reset all overclocks and undervolts to stock

Undervolting tools are beloved for thermals, but an unstable undervolt is a textbook WHEA trigger.

1. If you use ThrottleStop, Intel XTU, or Ryzen Controller, reset all offsets to zero and disable them at startup.
2. Restart into BIOS/UEFI (**F2**/**Del** at the splash screen) and load optimized defaults (**F9** on many boards, then **F10** to save).
3. Disable XMP/EXPO memory profiles — set memory to **Auto**.
4. Run the laptop at fully stock settings for several days. If WHEA crashes stop, your "stable" tuning wasn't stable.

### Fix 3: Update the BIOS/UEFI firmware

BIOS updates routinely fix WHEA error handling, especially around new Windows builds like 24H2.

1. Find your exact model on the manufacturer's support site — Dell, HP, and Lenovo all provide Windows-based BIOS updaters.
2. Plug into AC power and close all programs before running the updater. **Do not interrupt a BIOS update** — a failed flash can brick the board.
3. Let the laptop reboot itself; it may restart several times.
4. After updating, re-check that BIOS settings are at defaults (updates sometimes reset them, sometimes don't).

For related post-update crash scenarios, the [WHEA error after Windows 11 update guide](/articles/how-to-fix-whea-uncorrectable-error-after-windows-11-update/) covers update-specific triggers.

### Fix 4: Read the WHEA-Logger entries to identify the component

Windows logs the hardware error details — use them instead of guessing.

1. Open **Event Viewer** (**Win + X** > **Event Viewer**).
2. Go to **Windows Logs** > **System** and filter for source `WHEA-Logger`.
3. Look at events around your crash times: **Event ID 18** is typically a fatal CPU/hardware error, **ID 17** is a corrected error that's becoming frequent, **ID 1** covers other hardware faults.
4. The event details name the reporting component — processor core, memory controller, PCI Express device, etc. That tells you where to focus testing.

### Fix 5: Test RAM and storage thoroughly

The two most commonly failing components, tested properly.

1. Run Windows Memory Diagnostic: **Win + R** > `mdsched.exe` > **Restart now and check for problems**. Any error means bad RAM.
2. For certainty, run MemTest86 overnight from USB (4+ passes).
3. Check drive health: **Terminal (Admin)** > `wmic diskdrive get status` should return "OK".
4. Run your SSD maker's health utility and look at the SMART data — reallocated sectors or a dropping health percentage means the drive is dying.
5. If your laptop has two RAM sticks, test them one at a time to isolate the bad one.

Memory-specific crashes with a similar hardware-first approach are covered in the [MEMORY_MANAGEMENT BSOD guide](/articles/memory-management-bsod-windows-11-fix/).

### Fix 6: Update chipset and storage drivers

Outdated chipset drivers can mishandle the hardware error reporting path itself.

1. Intel users: run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for chipset, RST storage, and management engine updates.
2. AMD users: get the latest chipset drivers from [AMD's support page](https://www.amd.com/en/support/download/drivers.html).
3. Also update your SSD firmware from the drive manufacturer's utility — firmware bugs in the storage stack are a known WHEA source.
4. Restart and monitor.

### Fix 7: Run manufacturer hardware diagnostics

When you've done everything software-side, let the OEM's own tests judge the hardware.

1. Dell: run **SupportAssist** > **Hardware Checkup**, or press **F12** at boot and choose **Diagnostics**.
2. Lenovo: **Lenovo Vantage** > **Device** > **Run diagnostics**, or use the Novo button menu.
3. HP: press **F2** at boot for **HP PC Hardware Diagnostics**.
4. If any component fails these tests, screenshot the failure code — it's your warranty claim evidence.
5. If all tests pass but WHEA crashes continue at stock settings with good thermals, suspect the motherboard itself and contact support with your documented steps.

## Closing

`WHEA_UNCORRECTABLE_ERROR` demands respect because the hardware is genuinely reporting trouble — but "reporting trouble" and "dead component" aren't the same thing. Heat, bad tuning, and old firmware cause most of these crashes, and all three are free to fix. Work the list in order, read the WHEA-Logger entries instead of guessing, and you'll either fix it or walk into the repair shop with a documented diagnosis — which is the next best thing.
