---
title: "Windows 11 Freezing Randomly? Diagnose and Stop the Lockups"
slug: how-to-fix-windows-11-freezing-randomly
date: 2026-10-11
categories: ["performance"]
tags: ["windows 11 freezing", "random freezes", "system hang", "troubleshooting", "lockup fix"]
description: "Windows 11 freezing randomly — screen locks, mouse dead, then recovers (or doesn't)? Find whether it's drivers, storage, RAM, or heat, and fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-11-freezing-randomly.webp"
faqs:
  - q: "What is the difference between a freeze and a crash?"
    a: "A freeze (hang) means the system stops responding but stays powered — the screen is static, input does nothing, and it may recover on its own or need a forced restart. A crash means Windows itself gave up, usually producing a blue screen with a stop code. Freezes point at drivers, storage stalls, or resource exhaustion; blue screens point at kernel bugs or hardware faults. The distinction matters because each has different diagnostic tools."
  - q: "Why does my laptop freeze but the mouse still moves?"
    a: "A moving cursor with an otherwise frozen screen usually means the GPU/compositor path is alive but the application or shell thread is blocked — often on disk I/O or a deadlocked process. Check Task Manager (Ctrl+Shift+Esc) if it opens: 100% disk active time with high response times is the classic cause. True full freezes where even the cursor dies point deeper — at drivers, storage controller stalls, or hardware."
  - q: "Can RAM cause random freezing without blue screens?"
    a: "Yes. Marginal RAM often causes freezes and application hangs rather than clean blue screens, because corrupted data silently derails running programs instead of tripping a kernel check. If freezes are truly random — no pattern with specific apps — and software fixes haven't helped, run Windows Memory Diagnostic overnight. Memory faults are also worth suspecting when freezes started after a RAM upgrade or on a laptop that runs hot."
  - q: "Should I force-shutdown during a freeze or wait it out?"
    a: "Wait 2 to 5 minutes first — many freezes are actually extreme slowdowns (100% disk, runaway process) that resolve on their own, and a forced shutdown during disk writes risks file-system corruption. Try Ctrl+Shift+Esc for Task Manager or Ctrl+Alt+Del for the security screen; if either responds, the system is alive and you can end the offending process. Only hold the power button when absolutely nothing responds after several minutes."
---

Random freezes are the worst kind of computer problem: no error message, no blue screen, no pattern you can point to — just a screen that stops, mid-sentence, mid-game, mid-meeting. The randomness is usually an illusion, though. Freezes have causes: a storage device stalling for seconds at a time, a driver deadlocking, RAM corrupting silently, or heat pushing a component over the edge. The trick is converting "random" into "reproducible-ish" with observation and logging.

This guide treats freezing as a diagnostic problem with four suspect families — storage, drivers, memory, and thermals — and gives you the tests that separate them. You'll learn what to observe during a freeze, which logs to read after one, and the fixes ordered by likelihood. If your issue is general slowness rather than hard lockups, start with [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) instead.

## Why this happens

- **Storage stalls**: SSD/HDD freezing for seconds on bad blocks or controller issues — the whole system waits on disk.
- **Driver deadlocks**: Two drivers (or a driver and the kernel) waiting on each other forever, often graphics or storage drivers.
- **Failing RAM**: Bit errors corrupting running code, causing hangs instead of clean crashes.
- **Overheating**: Thermal shutdown of individual components (GPU, chipset) freezing the system without a full power-off.
- **100% disk active time**: The disk queue saturated so every app blocks on I/O simultaneously.
- **Corrupt system files**: Damaged Windows components hanging when called.
- **Third-party antivirus deadlocks**: Filter drivers deadlocking with the file system during scans.
- **Power delivery issues**: Failing charger/battery causing voltage droops that freeze the CPU without powering off.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Observe the freeze like a technician

What happens *during* the freeze is diagnostic gold.

1. Next time it freezes, note precisely: does the **mouse cursor** still move? Does **Caps Lock** toggle its light? Does **Ctrl+Alt+Del** do anything? Can you hear audio continuing?
2. Cursor moves + Ctrl+Alt+Del works = application/shell-level hang (Fixes 2-3 territory). Nothing responds at all = driver/storage/hardware level (Fixes 4-6).
3. Note what you were doing: specific app? Heavy file copy? Gaming? On battery or charger? Waking from sleep? Patterns hide in these details — keep a note on your phone for a week.
4. Check the clock: if freezes cluster in the first 10 minutes after boot, suspect startup/servicing load; if after hours of use, suspect heat or a slow leak.
5. This observation costs nothing and prevents the most common mistake: reinstalling Windows for a hardware problem, or replacing hardware for a software problem.

### Fix 2: Read the logs after the freeze

Windows usually writes down what happened — if you know where to look.

1. After recovering (or rebooting), open **Event Viewer** > **Windows Logs** > **System** and look at events timestamped just before the freeze: disk errors (IDs 7, 11, 153), driver warnings, or **Kernel-Power** 41 (unexpected shutdown — meaning *you* force-powered-off, not Windows).
2. Check **Windows Logs** > **Application** for application hangs (Event ID 1002, "Application Hang") naming the frozen program.
3. Open **Reliability Monitor** (search Start for "reliability") — its timeline shows freezes, app failures, and driver/hardware failures on a calendar, making patterns visible at a glance.
4. If Event Viewer shows **disk** errors before freezes, jump to Fix 4 (storage). If it shows **nvlddmkm** or **amdkmdap** errors, jump to Fix 5 (GPU driver). If it shows nothing at all before a hard freeze, hardware becomes more likely (Fix 6).
5. Also check **C:\Windows\Minidump** — if any `.dmp` files exist from the freeze dates, the system *did* partially crash, and analyzing them (or just noting their existence) reframes the problem toward drivers.

### Fix 3: Eliminate resource-exhaustion freezes

The most common and most fixable family.

1. Open Task Manager > **Performance** and leave it visible on a second monitor (or check immediately after recovering from a "soft" freeze): **Disk** at 100% active time with high response time = disk-saturation freeze. See [fixing 100% disk active time](/articles/how-to-fix-disk-active-time-100-percent/).
2. **Memory** at 100% = the system is thrashing; identify the consumer in the Processes tab and see [high memory usage fixes](/articles/windows-11-high-memory-usage-fix/).
3. A single app's memory climbing without bound = a leak; update or replace that app.
4. Disable **SysMain** (Services > SysMain > Disabled + Stop) as a test — on some systems its preloading collides badly with real workloads and causes I/O storms.
5. If freezes happen specifically when the disk is hammered, also check SSD health with CrystalDiskInfo — a healthy SSD shouldn't stall the system, and a degraded one explains everything.

### Fix 4: Test storage as the freeze source

Storage stalls freeze everything because everything waits on disk.

1. Run CrystalDiskInfo and check **Health Status**: anything but **Good** means back up now and replace the drive — bad blocks cause multi-second stalls that present exactly as random freezes.
2. From an elevated prompt, run `chkdsk C: /scan` — file-system corruption forces retry loops that stall I/O.
3. Update the storage/NVMe driver and check for SSD **firmware** updates on your laptop maker's support page (Dell, HP, Lenovo) — firmware bugs causing controller stalls are a known freeze source.
4. If you have a spinning HDD (or hybrid), listen during freezes: repetitive clicking or seeking sounds are the drive struggling physically.
5. Test with a different drive if possible — even a cheap SATA SSD with a fresh Windows install from the Windows 11 download page — to definitively separate drive faults from everything else.

### Fix 5: Fix driver-level deadlocks (GPU first)

Graphics drivers are the leading deadlock suspects.

1. If freezes happen during video, gaming, or with external monitors, clean-install the GPU driver: download from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) (Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)), choose Custom install + **clean installation**.
2. Disable hardware acceleration in your browser (Settings > System) as a test — browser GPU-process deadlocks freeze the whole desktop on some driver versions.
3. Disconnect external monitors/docks for a few days as a test — multi-display driver paths and dock firmware are disproportionately represented in freeze reports.
4. Update the **chipset** driver from your laptop maker's support page — chipset drivers mediate between the CPU and everything else, and stale ones deadlock under load.
5. If a specific driver version started the freezes, roll it back (Device Manager > device > Driver tab > **Roll Back Driver**) and block driver updates for that device until a fixed version ships.

### Fix 6: Check thermals, RAM, and power hardware

When software is innocent, test the physical machine.

1. Install HWiNFO and log temperatures during normal use up to a freeze: CPU/GPU consistently near thermal limits before freezing = cooling failure. Clean vents with compressed air, replace dried thermal paste if you're comfortable (or have a shop do it), and verify fans actually spin up under load.
2. Run **Windows Memory Diagnostic** overnight (search Start > Restart and test with the Extended option) — RAM faults cause exactly this symptom class.
3. Test on **charger only** (battery removed if possible) and **battery only**: freezes that follow the power source implicate the charger, battery, or power circuitry — voltage droops freeze CPUs without triggering a shutdown.
4. Strip to minimal hardware: undock, unplug all USB devices, remove SD cards — retest for a day. Add things back one at a time.
5. If freezes persist through a clean Windows install with minimal hardware and healthy thermals/RAM/drive, it's a motherboard-level fault — document your testing (this log is what warranty support needs) and contact your laptop maker's support.

## Closing

Random freezes feel unsolvable because they give you nothing — but observation (Fix 1) and logs (Fix 2) almost always convert "random" into a suspect family, and each family has a decisive test. Work the list in order, give each fix a day or two of real use before judging it, and resist the urge to reinstall Windows on day one: it's the right move only after storage, drivers, thermals, and RAM have been checked, and doing it first just destroys the evidence.
