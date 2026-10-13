---
title: "Windows 11 Freezing Randomly? Troubleshoot It Like a Technician"
slug: "windows-11-freezing-randomly-troubleshooting"
date: "2026-10-05"
categories: ["performance"]
tags: ["windows 11 freezing", "random freeze", "troubleshooting", "system hang", "diagnose"]
description: "Windows 11 freezing at random moments? Follow a technician's diagnostic process to find whether it's drivers, RAM, storage, or software — then fix it."
thumbnail: "/images/thumbs/windows-11-freezing-randomly-troubleshooting.webp"
faqs:
  - q: "How do I figure out what's causing random freezes?"
    a: "Work like a technician: check Reliability Monitor (search 'reliability' in Start) for the pattern — app crashes, driver failures, and hardware errors are logged with timestamps you can match to freezes. Then check Event Viewer > Windows Logs > System for critical errors (Kernel-Power 41, WHEA errors) around freeze times. The pattern in those two tools narrows it to software, drivers, or hardware before you change anything."
  - q: "Can RAM cause random freezing in Windows 11?"
    a: "Yes — faulty RAM is one of the top hardware causes of truly random freezes, especially freezes with no blue screen and no error logged. Windows Memory Diagnostic (search it in Start) runs a decent basic test; MemTest86 from a USB boot is the thorough option. If freezes started after a RAM upgrade or only happen with both sticks installed, test each stick alone — one bad module in a pair is the classic pattern."
  - q: "Why does Windows 11 freeze but the mouse still moves?"
    a: "Mouse-moving-but-nothing-responds means the input subsystem is alive while something else is wedged — usually the storage stack waiting on a non-responsive drive, the graphics driver hung, or DWM stuck compositing. It's actually a useful clue: total lockups (not even mouse) point more toward CPU/RAM/hardware, while mouse-alive freezes point toward disk or GPU drivers. Note which kind you have before troubleshooting."
  - q: "Is random freezing a sign my SSD is failing?"
    a: "It can be. An SSD with failing NAND or a dying controller causes exactly the mouse-moves-but-nothing-loads freeze pattern as read requests time out. Check the SSD's health with CrystalDiskInfo and the manufacturer's own tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) — SSDs report wear percentage and spare-block counts that predict failure. Back up immediately if health is below 80% or warnings appear."
---

Random freezes are the worst kind of computer problem: no error message, no blue screen, no pattern you can see — just a machine that locks up whenever it feels like it. Mid-email, mid-video, mid-nothing. And because there's no message, most advice degenerates into 'update your drivers' soup. This guide doesn't do that.

Instead, you'll troubleshoot like a technician: gather evidence first (Windows logs every freeze's fingerprints), classify the freeze type, then work a decision tree that separates software, driver, and hardware causes. Random freezes have a finite set of real causes — bad RAM, dying storage, driver hangs, overheating, and corrupted system files cover nearly all of them — and each leaves distinct evidence.

Start with evidence (Fixes 1-2), then follow where it points. If your issue is high CPU rather than freezes, our [high CPU in 24H2 guide](/articles/how-to-fix-high-cpu-usage-in-windows-11-24h2/) is the right companion — and once you've diagnosed, the [best fix order for random freezing](/articles/best-way-to-fix-windows-11-freezing-randomly/) prioritizes what to try first.

## Why this happens

- **Faulty RAM** — Bad memory cells corrupt data randomly — freezes with no pattern, no blue screen, often no log entry. The king of 'random' hardware causes.
- **Dying SSD or HDD** — Storage that stops responding for seconds at a time freezes everything waiting on it; mouse often keeps moving. SMART warnings confirm it.
- **Graphics driver hangs** — A hung GPU driver freezes the display pipeline; sometimes recovers with a screen blink (TDR), sometimes locks the session.
- **Overheating CPU/GPU** — Thermal shutdown protection triggers hard freezes or sudden power-offs under load — pattern: freezes during games, video renders, or hot rooms.
- **Corrupted system files** — Damaged Windows components crash critical processes; often leaves Event Viewer error trails pointing at specific DLLs or services.
- **Driver conflicts (audio/network)** — Bad audio (Conexant, Realtek) and network filter drivers cause DPC-latency freezes — micro-freezes of 1-5 seconds, audio crackling alongside.
- **Failing power delivery** — A dying charger or battery on laptops causes voltage dips under load — freezes or shutdowns that only happen unplugged or under heavy load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the logs: Reliability Monitor + Event Viewer

Windows recorded your freezes. Ask it what happened.

1. Search Start for **'reliability'**, open **View reliability history**, and look for red X marks matching your freeze times — note the faulting module names.
1. Open **Event Viewer > Windows Logs > System**; filter for **Critical** and **Error** around freeze times. **Kernel-Power 41** = unexpected shutdown (power/thermal); **WHEA-Logger** = hardware error (note the component); **nvlddmkm/amdkmdap** = GPU driver crash.
1. Three freezes with the same faulting driver = your culprit. Random different faults each time = suspect RAM or power.
1. This evidence directs every step below — don't skip it.

### Fix 2: Classify your freeze type

The freeze's behavior is diagnostic.

1. **Total lockup** (nothing moves, needs hard reset): points to RAM, CPU thermal, or power.
1. **Mouse moves, nothing responds**: points to storage or GPU driver — the input stack is alive but data stopped flowing.
1. **Brief 1-5 second stutters with audio crackle**: DPC latency — audio/network drivers; measure with LatencyMon.
1. **Freeze then recover with screen blink**: GPU driver TDR — update or clean-install graphics drivers.
1. Write down your type; it tells you which hardware test matters most.

### Fix 3: Test the RAM properly

The number-one 'random' cause deserves a real test, not a guess.

1. Search Start for **Windows Memory Diagnostic**, choose **Restart now and check** — let the full pass complete (20-40 minutes).
1. For a definitive test, boot **MemTest86** from USB and run at least 2 full passes (several hours, ideally overnight).
1. Any red error = bad RAM. If you have two sticks, test each alone to find the bad one — replace just it.
1. Freezes that vanish on one stick confirm the diagnosis; no errors after 4+ MemTest86 passes largely rules RAM out.

### Fix 4: Check storage health

For the mouse-moves-but-frozen pattern, the drive is suspect number one.

1. Install CrystalDiskInfo — check **Health Status** and reallocated/pending sector counts on HDDs, wear percentage on SSDs.
1. Run the SSD manufacturer's own tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) for the authoritative health read.
1. Run `chkdsk C: /f /r` from admin Command Prompt to map out bad sectors.
1. If health is degraded: back up immediately, then replace the drive — no software fix saves failing storage.

### Fix 5: Rule out overheating

Heat freezes follow load — pattern-match before testing.

1. Install HWMonitor; note idle temps, then stress with a game or video render while watching.
1. CPU persistently above 95°C or GPU above 90°C under load = thermal problem: clean vents with compressed air, elevate the laptop, consider repaste on 2+ year old machines.
1. Freezes only in hot rooms or only under sustained load that vanish when cool = thermal, confirmed.
1. Laptop cooling pads help marginally; cleaning dust helps dramatically.

### Fix 6: Update or roll back the suspect driver

Your logs named a driver — act on it.

1. For GPU TDRs: DDU-clean-install the graphics driver ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html)) — don't just 'update' over the old one.
1. For audio/network DPC freezes: update from your laptop maker's support page (Dell, HP, or Lenovo) — these drivers are model-tuned.
1. If freezes started with a specific driver update, roll back: **Device Manager > device > Properties > Driver > Roll Back Driver**.
1. Change one driver at a time and test for 48 hours between changes.

### Fix 7: Repair Windows itself

When logs point at system components rather than hardware.

1. Admin Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`, then restart.
1. If freezes persist, do an in-place repair install from the Windows 11 download page — keeps files and apps while refreshing Windows.
1. Still freezing after clean hardware tests + repaired Windows? It's hardware beyond RAM/drive — motherboard or power delivery — time for professional diagnosis.
1. Microsoft's Windows support hub documents the recovery options if you want the official walkthrough.

## Closing

Random freezes stop being random once you read the logs — they become a named driver, a bad RAM stick, or a dying drive, and each has a fix. The technician's rule holds: evidence first, changes second, one change at a time. Follow it and you'll find the cause instead of reinstalling Windows on a hunch.
