---
title: "How to Fix a Laptop Running Slow on Windows 11"
slug: how-to-fix-laptop-running-slow-on-windows-11
date: 2026-09-11
categories: ["performance"]
tags: ["slow laptop", "windows 11", "speed up", "lagging", "performance"]
description: "Windows 11 laptop running slow? A complete speedup workflow: diagnose the bottleneck, trim startup, tune settings, and upgrade smart."
thumbnail: "/images/thumbs/how-to-fix-laptop-running-slow-on-windows-11.webp"
faqs:
  - q: "What is the first thing to check on a slow Windows 11 laptop?"
    a: "Task Manager. Press Ctrl+Shift+Esc and look at the Performance tab: if memory is constantly above 85%, you need more RAM or fewer apps; if disk sits at 100%, the drive is the bottleneck; if CPU is pegged by a single process, that's your culprit. Five minutes of observation directs every fix that follows — skipping diagnosis is why generic speedup guides fail."
  - q: "Do debloating scripts make Windows 11 faster?"
    a: "Marginally at best, riskily at worst. Aggressive debloat scripts remove components Windows expects, breaking updates and features for a speed gain you can't measure. The legitimate wins — disabling startup apps, uninstalling unused programs, turning off transparency — are all available in Settings without scripts. Never run a script that disables Windows Update or Defender."
  - q: "How often should I restart my laptop?"
    a: "At least every few days. Windows accumulates memory leaks, stuck processes, and driver cruft over long uptimes — a restart clears all of it in two minutes. Laptops that 'never get restarted, only slept' are disproportionately represented in slowdown complaints. If your uptime is measured in weeks, restart before troubleshooting anything."
  - q: "Will more RAM or an SSD help more?"
    a: "It depends on the bottleneck. If Task Manager shows the disk at 100% during slowness, an SSD is transformative. If memory is maxed while the disk idles, RAM is the answer. On old laptops with both an HDD and 4 GB RAM, the SSD comes first — it improves boot, app launches, and paging all at once. Diagnose with Task Manager before spending."
---

A slow Windows 11 laptop is rarely one problem — it's a stack of small ones. Ten startup apps, a full drive, an old driver, a browser eating 6 GB of RAM, and a power plan set to efficiency: each costs a little, together they cost everything. That's why random tips fail and workflows succeed. This guide is the workflow: diagnose the actual bottleneck, fix the big contributors in order, and know when the answer is hardware.

The honest framing: software fixes recover the performance your hardware is capable of; they can't exceed it. A 4 GB RAM laptop with a spinning drive will never feel fast running modern workloads — but it can feel dramatically better than it does now. For the focused speedup checklist see [speeding up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/); for app-launch slowness specifically see [fixing apps opening slowly](/articles/how-do-i-fix-apps-opening-slowly-on-windows-11/).

## Why this happens

- **Startup overload**: Dozens of auto-launching apps permanently resident, consuming CPU and RAM from boot.
- **RAM exhaustion**: Modern browsers and apps exceeding available memory, forcing constant paging.
- **Full system drive**: Under 15% free space crippling the pagefile, updates, and temp operations.
- **Spinning hard drive**: HDDs making every disk operation — boot, launch, search — an order of magnitude slower.
- **Power plan throttling**: Efficiency modes clamping CPU/GPU well below their capability.
- **Outdated drivers**: Old chipset, storage, and GPU drivers wasting cycles on inefficient paths.
- **Background churn**: Updaters, indexers, sync tools, and telemetry competing with your work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Diagnose the real bottleneck

Everything follows from this.

1. Restart the laptop (a real restart), wait 5 minutes, then open Task Manager > **Performance** and record idle CPU, memory, and disk percentages — healthy idle is under 10% CPU, memory well below max, disk near 0%.
2. Reproduce the slowness (open your usual apps) and watch which resource saturates first — the first to hit 90%+ is the bottleneck.
3. In **Processes**, sort by CPU, memory, and disk in turn — name the top 3 consumers in each. Specific names beat vague "it's slow."
4. Check C: free space in File Explorer — under 15% free is itself a slowdown cause regardless of other symptoms.
5. Write down the verdict: CPU-bound (which process?), memory-bound (how much RAM? how much used?), or disk-bound (HDD or SSD? at 100%?). Now the fixes below have targets.

### Fix 2: Eliminate startup bloat

The biggest software win available.

1. Task Manager > **Startup apps** — disable everything you don't need within a minute of login. Be aggressive: updaters, chat, launchers, cloud sync, utilities.
2. **Settings** > **Apps** > **Startup** — catch entries Task Manager missed.
3. `Win+R` > `shell:startup` — delete leftover shortcuts.
4. **Task Scheduler** — review **At log on** triggers for updaters and telemetry hiding from the startup lists.
5. Restart and compare: boot-to-usable time and idle resource usage should both drop sharply. This single fix resolves a large plurality of "slow laptop" complaints.

### Fix 3: Free RAM pressure

Stop the paging that makes everything stutter.

1. In Task Manager sorted by **Memory**, identify the giants — browsers, Teams/Slack/Discord, and creative apps.
2. Enable your browser's memory saver / tab suspension features; close tabs ruthlessly or use a session manager.
3. Quit Electron apps you're not actively using — each is a full Chromium instance eating hundreds of MB.
4. If memory still sits above 85% in normal use, price a RAM upgrade — it's the highest-value hardware fix for memory-bound machines.
5. Leave the pagefile system-managed — shrinking it to "save SSD wear" causes crashes; it doesn't speed anything up.

### Fix 4: Reclaim disk space and health

A full or failing drive slows everything.

1. Run **Disk Cleanup** as admin — **Windows Update Cleanup**, **Delivery Optimization Files**, **Previous Windows installations**; expect 5–25 GB back.
2. Enable **Storage Sense** for ongoing automatic cleanup.
3. Uninstall unused large programs (**Settings** > **Apps** > sort by size); move personal media off C:.
4. Verify the drive type (Task Manager > Performance > Disk): HDD → plan the SSD upgrade (Fix 7); SSD → check health with the maker's tool and confirm TRIM is on (`fsutil behavior query DisableDeleteNotify` should be 0).
5. Target: 20%+ free on C:. Below that, treat disk space as the primary problem until fixed.

### Fix 5: Set performance-oriented power and visual settings

Stop Windows from holding back the hardware.

1. **Settings** > **System** > **Power & battery** > **Power mode** → **Best performance** (plugged in).
2. `sysdm.cpl` > **Advanced** > **Performance Settings** > **Custom**: uncheck animation and fade entries, keep font smoothing and thumbnails.
3. **Settings** > **Personalization** > **Colors** → transparency **Off**.
4. **Settings** > **System** > **Display** > **Advanced display** → confirm the refresh rate matches your panel's maximum.
5. These are small individually; together they remove the "death by a thousand cuts" UI lag on modest hardware.

### Fix 6: Update the driver and system stack

Old software wastes new hardware.

1. Install all pending Windows updates — then update the chipset driver from the laptop vendor's support page.
2. Update the GPU driver from [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or AMD.
3. Update Wi-Fi and Bluetooth drivers too — flaky wireless drivers cause stalls that feel like general slowness.
4. Update the BIOS if the changelog mentions performance or stability — especially on laptops 2+ years old.
5. In **Device Manager**, clear any yellow-warning devices — broken drivers cause retry loops that surface as mystery CPU usage. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) covers driver update procedures officially.

### Fix 7: Make the hardware call

When software fixes hit the hardware ceiling.

1. **SSD first**: if the laptop still has a spinning HDD, cloning to an SSD is the single most transformative upgrade — boot, launches, and responsiveness all change character.
2. **RAM second**: 8 GB minimum for comfortable 2026 workloads; 16 GB if you multitask heavily. Check your model's max and whether RAM is soldered before buying.
3. **Thermals**: if HWiNFO shows throttling under load, clean the vents; on old machines consider a repaste.
4. **The honest assessment**: a 7-year-old dual-core with 4 GB soldered RAM and no SSD slot has a ceiling — at some point the money goes toward replacement, not upgrades.
5. After any hardware change, reinstall or at least re-verify drivers — new SSDs want fresh chipset/storage drivers, new RAM wants a memory test (`mdsched.exe`).

## Closing

Slow Windows 11 laptops are fixed by workflow, not tips: diagnose the bottleneck, gut startup, relieve RAM and disk pressure, set performance power options, update the driver stack, and upgrade the hardware that's actually limiting you. Most machines are transformed by Fixes 1–4 alone — no purchases, no reinstalls, just removing the accumulated weight. The laptop you bought is still in there; it's just buried.
