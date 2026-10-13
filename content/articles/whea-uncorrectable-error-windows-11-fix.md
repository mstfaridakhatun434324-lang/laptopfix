---
title: "How to Fix the WHEA Uncorrectable Error on Windows 11"
slug: whea-uncorrectable-error-windows-11-fix
date: 2026-09-17
categories: ["windows-errors"]
tags: ["bsod", "whea-uncorrectable-error", "windows-11"]
description: "WHEA_UNCORRECTABLE_ERROR means your hardware reported a fatal fault. Here's how to find which component is failing and fix it."
thumbnail: "/images/thumbs/whea-uncorrectable-error-windows-11-fix.webp"
faqs:
  - q: "What does WHEA_UNCORRECTABLE_ERROR actually mean?"
    a: "WHEA stands for Windows Hardware Error Architecture. This blue screen means a hardware component — CPU, RAM, SSD, GPU, or motherboard — reported an error so serious that Windows couldn't recover. It's one of the few stop codes that points at hardware first and software second."
  - q: "Can a driver cause WHEA_UNCORRECTABLE_ERROR?"
    a: "Yes, occasionally. Outdated chipset drivers or a bad BIOS can mishandle hardware error reports and turn a recoverable glitch into a fatal one. But if drivers and BIOS are current and it still crashes, treat it as a genuine hardware fault and test each component."
  - q: "Why does it only happen when gaming or under heavy load?"
    a: "Because that's when your CPU and GPU draw the most power and generate the most heat. An unstable overclock, a failing power delivery circuit, or overheating only shows up under load. Monitor temperatures during a stress test to confirm."
  - q: "Is my laptop dying if I get this error?"
    a: "Not necessarily — it can be as simple as an outdated BIOS or an unstable overclock setting. But don't ignore it: back up your important files now, then work through the diagnostics below to identify the failing part."
---
WHEA_UNCORRECTABLE_ERROR (stop code 0x00000124) is the blue screen Windows shows when your hardware itself reports a fatal problem. WHEA — Windows Hardware Error Architecture — is the system that lets components like your CPU, RAM, and SSD tell Windows when something goes wrong at the hardware level. When the error is uncorrectable, Windows has no choice but to crash.

This is one of the few stop codes where hardware is the prime suspect. That said, don't panic — outdated BIOS firmware, bad drivers, and unstable overclocks cause it too, and those are free to fix. Work through the software causes first, then test the hardware methodically.

## Why this happens

- **Failing CPU or motherboard.** The processor's internal error detection caught a fault in a core, cache, or the memory controller — the most common hardware cause.
- **Bad or unstable RAM.** Memory errors that ECC or the memory controller can't correct trigger WHEA reports directly.
- **Overheating.** A CPU or GPU running past its thermal limits produces hardware errors, especially under sustained load like gaming or video rendering.
- **Unstable overclock or undervolt.** Aggressive tuning that seemed stable can degrade over time and start producing hardware errors.
- **Outdated BIOS or chipset drivers.** Old firmware misreads hardware error signals or mishandles power delivery, creating errors that aren't really there — or failing to handle real ones gracefully.
- **Failing SSD or GPU.** Storage controllers and graphics cards also report through WHEA, so don't rule them out.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Back up your important files before you start — if this is a real hardware fault, you want your data safe.

### Fix 1: Reset any overclock or undervolt to stock

If you've tuned your CPU or GPU at all, this is step one.

1. Open your tuning tool (Intel XTU, Throttlestop, MSI Afterburner, or your BIOS) and restore **all settings to default**.
2. In the BIOS, load **Optimized Defaults** if you're unsure what was changed.
3. Save, reboot, and stress the laptop the way that used to trigger the crash. If the crashes stop, your tuning had become unstable — leave it at stock or retune conservatively.

### Fix 2: Check temperatures under load

Overheating is a top cause of load-triggered WHEA errors.

1. Install a monitoring tool like HWMonitor or HWiNFO64.
2. Run a demanding task — a game, a video export, or a stress test like Cinebench — and watch the CPU and GPU temperatures.
3. Sustained temperatures above **95°C** on the CPU indicate a cooling problem: clean the vents and fans with compressed air, replace dried-out thermal paste if you're comfortable opening the laptop, or use a cooling pad.
4. Check that the fans actually spin up under load. A dead fan on a thin laptop will cause exactly these symptoms.

### Fix 3: Update BIOS and chipset drivers

Firmware updates frequently include fixes for hardware error handling.

1. Find your exact model on the manufacturer's support site and download the latest **BIOS** update. Flash it with the charger plugged in and nothing else running.
2. Install the latest **chipset driver** for your model from the same site.
3. Intel users can also run [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch chipset and management engine updates.
4. Restart and test under load again.

### Fix 4: Test your RAM thoroughly

Memory faults are a classic WHEA trigger.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If Windows Memory Diagnostic reports errors, test further with MemTest86 from a bootable USB — run at least two full passes.
3. On laptops with removable RAM, test one stick at a time to identify the bad module, then replace it.
4. Also try reseating the RAM — a stick that worked loose from thermal cycling can produce intermittent errors.

### Fix 5: Check the drive and run system repairs

Rule out the storage side of the hardware equation.

1. Open an elevated **Command Prompt** and run `chkdsk C: /f /r` (type **Y** to schedule, then restart).
2. After booting, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check drive health in **PowerShell (Admin)**: `Get-PhysicalDisk | Select FriendlyName, HealthStatus, OperationalStatus`. Anything other than **Healthy** means the drive is suspect. Our companion piece on [what to do when WHEA uncorrectable error strikes](/articles/what-to-do-if-whea-uncorrectable-error/) walks through additional drive diagnostics.

### Fix 6: Update or reinstall device drivers

A bad driver can provoke hardware error reports.

1. Press **Win + X** and open **Device Manager**.
2. Update drivers under **Display adapters**, **Processors**, and **System devices** (right-click > **Update driver > Search automatically for drivers**).
3. Pay special attention to anything with a yellow warning icon.
4. If the crashes started after a driver update, use **Properties > Driver tab > Roll Back Driver** on the suspect device instead.

### Fix 7: Identify the failing component and plan the repair

If software fixes didn't help, you need to know which part is dying.

1. Open **Event Viewer** (**Win + X > Event Viewer**) and go to **Windows Logs > System**. Look for **WHEA-Logger** entries — the details often name the component (processor core, memory, PCI Express device).
2. Note the pattern: crashes only in games point at the GPU or its power delivery; crashes at idle point at RAM or the CPU.
3. For laptops under warranty, contact the manufacturer with the WHEA-Logger details — this is exactly the evidence they need. Out of warranty, a repair shop can test components individually. Errors in the same family, like [machine check exceptions](/articles/machine-check-exception-bsod-windows-11/), follow the same diagnostic logic.

## Closing

WHEA_UNCORRECTABLE_ERROR is Windows telling you the hardware reported a serious fault — but "hardware reported" doesn't always mean "hardware is dead." Reset your tuning to stock, check temperatures, update the BIOS and chipset drivers, and test the RAM before assuming the worst. If those steps don't resolve it, the Event Viewer's WHEA-Logger entries will tell you (and your repair shop) exactly which component to focus on. Either way, back up your data first — that's the one step you should never skip with this error.
