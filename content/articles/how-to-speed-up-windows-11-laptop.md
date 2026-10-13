---
title: "Windows 11 Laptop Running Slow? Speed It Up the Right Way"
slug: how-to-speed-up-windows-11-laptop
date: 2026-10-05
categories: ["performance"]
tags: ["speed up", "windows 11", "slow laptop", "performance", "optimization"]
description: "Windows 11 laptop running slow? Proven, safe speed-ups: trim startup apps, remove bloatware, tune visual effects, and fix the real bottlenecks."
thumbnail: "/images/thumbs/how-to-speed-up-windows-11-laptop.webp"
faqs:
  - q: "Why is my new Windows 11 laptop already slow?"
    a: "New laptops are rarely slow because of hardware — the usual causes are preinstalled bloatware running at startup, a nearly full drive, Windows Update working in the background, or the laptop running in a power-saving mode that caps CPU speed. A 30-minute cleanup of startup programs and manufacturer bloatware typically transforms a sluggish new machine, which points to software rather than weak hardware."
  - q: "Does disabling visual effects actually speed up Windows 11?"
    a: "On very old or low-end hardware with weak integrated graphics, disabling transparency and animations frees measurable GPU and CPU resources. On any modern laptop, the difference is negligible, so it is not a magic fix. It is worth doing as one small part of a broader tune-up, but if your laptop is genuinely slow, the real culprits are startup bloat, a full drive, or a runaway background process."
  - q: "Will more RAM speed up my Windows 11 laptop?"
    a: "Only if RAM is actually your bottleneck. Open Task Manager while working normally — if memory sits above 85 percent consistently, more RAM will help noticeably. If RAM is fine but the disk is pegged at 100 percent, an SSD upgrade matters far more. Doubling RAM on a machine that never runs out of it changes almost nothing, so diagnose before spending money."
  - q: "Are Windows optimizer or PC cleaner apps safe to use?"
    a: "Most third-party optimizer and registry-cleaner apps are unnecessary at best and harmful at worst, and some bundle adware or nagware. Windows 11 already includes everything you need: Storage Sense, Disk Cleanup, Task Manager startup management, and the built-in troubleshooters. Registry cleaning provides no measurable speed benefit on modern Windows and risks breaking things, so skip that entire category."
---

A Windows 11 laptop that takes a minute to boot, stutters opening File Explorer, and spins up its fans doing nothing is maddening — especially when it felt fast on day one. The slowdown is almost always software, not hardware: startup bloat, preinstalled junk, background updaters, a nearly full drive, or one greedy process eating resources. That means it's fixable without spending money.

The trap most people fall into is chasing exotic "speed tweaks" — registry hacks, debloat scripts of dubious origin, mystery optimizer apps — while ignoring the basics that deliver 90% of the improvement. This guide does the opposite: it works through the high-impact, safe optimizations in order, from diagnosing the actual bottleneck to trimming what loads at boot, cleaning house, and tuning the settings that genuinely matter. Measure first, then fix.

Before changing anything, get a baseline so you can tell what helped. Open **Task Manager** (Ctrl+Shift+Esc), click **Performance**, and note which resource — CPU, memory, or disk — is under pressure during your normal use. That one observation guides everything below. For a deep dive on startup specifically, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/); for reclaiming drive space, see [freeing up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/).

## Why this happens

- **Too many startup programs**: Every app that launches at boot competes for CPU and disk in the first critical minutes.
- **Preinstalled bloatware**: Manufacturer utilities, trials, and game launchers run background services you'll never use.
- **A nearly full drive**: Windows slows measurably when the system drive drops below ~10% free space.
- **Runaway background processes**: A stuck updater, indexer, or antivirus scan can pin CPU or disk for hours.
- **Power-saving mode throttling**: Battery-saver and efficiency power plans cap CPU speed to save energy.
- **Outdated or generic drivers**: Missing chipset and graphics drivers leave performance on the table.
- **Mechanical hard drive**: Laptops still shipping with spinning HDDs are slow in ways no tweak can fully fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the actual bottleneck

Speed up the right thing.

1. Open **Task Manager** > **Performance** and watch CPU, Memory, and Disk while you do your normal work for a few minutes.
2. If **Disk** sits at 90–100% constantly, your bottleneck is storage — skip to Fix 4 and seriously consider an SSD upgrade; nothing else will matter as much.
3. If **Memory** is above 85% with your usual apps open, you need fewer background apps (Fix 2) or more RAM — check what's using it under **Processes**, sorted by Memory.
4. If **CPU** is pinned by a single process, click it, note the name, and search the process name — it may be a stuck updater or a known hog with a specific fix.
5. If nothing is pegged but everything feels slow, the cause is death-by-a-thousand-cuts: startup bloat plus a full drive plus background noise. Fixes 2–4 will handle it. Microsoft's own [Windows performance guidance](https://support.microsoft.com/en-us/windows) covers these diagnostics too.

### Fix 2: Cut startup programs ruthlessly

The single biggest boot-time and idle-performance win.

1. Open **Task Manager** > **Startup apps** — every entry shows its startup impact rating.
2. Disable anything rated **High** impact that you don't need within seconds of logging in: chat apps, game launchers, cloud storage clients you rarely use, updater helpers.
3. Keep your antivirus, audio driver utilities, and anything related to your laptop's function keys or trackpad enabled.
4. In **Settings** > **Apps** > **Startup**, double-check for entries Task Manager missed.
5. Restart and time the difference — also notice how much snappier the first five minutes feel. Fewer startup apps means less background CPU and memory pressure all day, not just at boot.

### Fix 3: Remove bloatware and unused apps

Every preinstalled utility is a background service waiting to slow you down.

1. Go to **Settings** > **Apps** > **Installed apps**, sort by size, and remove manufacturer utilities you never open, antivirus trials (Windows Defender is already there), and preinstalled games.
2. Remove duplicate apps: you don't need two photo editors, three cloud clients, or a manufacturer's "assistant" plus Windows' own tools.
3. Check the **Startup** impact again after uninstalling — some bloatware leaves scheduled tasks behind; open **Task Scheduler** and disable tasks from uninstalled vendors.
4. Don't remove: chipset/graphics/audio drivers, the manufacturer's power or thermal control app if you actually use it, and anything you're unsure about — search the name first.
5. This isn't a one-time job: new bloat arrives with major updates and new app installs, so repeat the review every few months.

### Fix 4: Free disk space and check drive health

A full drive is a slow drive.

1. Follow the full cleanup process in our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) — target at least 15% free on C:.
2. Enable **Storage Sense** (**Settings** > **System** > **Storage**) so temp files and the Recycle Bin clean themselves automatically.
3. If your laptop still has a spinning hard drive, check its health: open **Command Prompt** as admin and run `wmic diskdrive get status` — anything but "OK" means replace it urgently.
4. For HDD owners, run **Defragment and Optimize Drives** (search it in Start) — never defrag an SSD; Windows handles SSD optimization automatically.
5. The honest truth: upgrading an HDD to even a budget SSD is the single most transformative upgrade possible for an old laptop — boot times drop from minutes to seconds.

### Fix 5: Fix the power and thermal situation

Your laptop may be deliberately holding back.

1. Click the battery icon and set the power mode slider to **Best performance** when plugged in (and **Balanced** on battery — Best performance on battery drains it fast).
2. In **Settings** > **System** > **Power & battery** > **Power mode**, confirm the plugged-in behavior matches what you want.
3. Check thermals: if fans scream constantly and the chassis is hot, the CPU is thermal-throttling — blow dust out of the vents with compressed air (laptop off, short bursts).
4. Make sure vents aren't blocked — using the laptop on a bed or couch smothers intake vents; a hard surface or cheap cooling stand helps measurably.
5. In manufacturer apps (Lenovo Vantage, MyASUS, Dell Power Manager), check for a **Performance** or **Turbo** thermal profile — many laptops ship in a quiet/balanced mode that caps speed.

### Fix 6: Update drivers and Windows properly

Stale drivers cause stutter that feels like slowness.

1. Install all pending updates in **Settings** > **Windows Update** — but do it when you can spare the time, since updates themselves slow the machine while installing.
2. Get graphics drivers from the source: Intel/NVIDIA/AMD directly, not just Windows Update — use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or the [NVIDIA driver page](https://www.nvidia.com/Download/index.aspx) for your GPU.
3. Get chipset and power-management drivers from your laptop manufacturer's support site — these control how the CPU boosts and sleeps.
4. After major updates, give Windows a day to finish indexing and background optimization before judging performance.
5. If a specific update made things worse, **Settings** > **Windows Update** > **Update history** > **Uninstall updates** lets you roll back the suspect one.

### Fix 7: Tune the settings that actually matter

Small, safe tweaks — skip the registry hacks.

1. **Settings** > **System** > **Notifications** — turn off **tips and suggestions**; they're background noise.
2. **Settings** > **Privacy & security** > **General** — disable **tailored experiences** and ad ID options to reduce background telemetry.
3. **Settings** > **Accessibility** > **Visual effects** — turn off **transparency effects** and **animation effects** if your GPU is weak; skip this on modern hardware where it changes nothing.
4. **Settings** > **Gaming** > **Game Mode** — leave it on; it deprioritizes background tasks while gaming.
5. Avoid "debloater" scripts and registry tweak packs from forums — they break Windows Update and Defender more often than they help, and undoing the damage takes longer than any speed gained.

## Closing

Speeding up a Windows 11 laptop isn't about secret tweaks — it's about removing what's in the way: startup bloat, junk apps, a full drive, power limits, and stale drivers. Work through the fixes above, measure against your baseline, and you'll usually find the machine you thought you bought. If one specific process is the hog, hunt it down by name — targeted fixes beat blanket optimization every time.
