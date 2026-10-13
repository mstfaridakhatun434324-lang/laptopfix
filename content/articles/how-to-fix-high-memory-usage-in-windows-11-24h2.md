---
title: "How to Fix High Memory Usage in Windows 11 24H2"
slug: how-to-fix-high-memory-usage-in-windows-11-24h2
date: 2026-09-22
categories: ["performance"]
tags: ["high memory usage", "ram", "windows 11 24h2", "memory leak"]
description: "RAM pinned at 80-90% on Windows 11 24H2? Identify the real memory hogs — compressed memory, driver leaks, and startup bloat — and bring usage back down."
thumbnail: "/images/thumbs/how-to-fix-high-memory-usage-in-windows-11-24h2.webp"
faqs:
  - q: "Is 70-80% memory usage normal on Windows 11?"
    a: "Often, yes. Windows 11 deliberately uses free RAM for caching (SuperFetch/SysMain, standby memory) to speed things up — Task Manager's headline percentage includes this cache. What's abnormal is the system feeling sluggish, heavy disk thrashing from paging, or the 'Committed' memory far exceeding physical RAM. Judge by responsiveness and the Memory composition in Task Manager's Performance tab, not the raw percentage alone."
  - q: "What is 'non-paged pool' and why does it grow?"
    a: "The non-paged pool is kernel memory that drivers lock and can never page to disk. Drivers with memory leaks allocate from it and never release, so it grows the longer the system runs — sometimes to multiple gigabytes. A non-paged pool over 1-2 GB on a typical laptop is a red flag for a leaking driver. Updating network, storage, and graphics drivers is the usual fix; poolmon can identify the exact culprit."
  - q: "Should I disable SysMain to reduce memory usage?"
    a: "Rarely needed on modern systems. SysMain (formerly SuperFetch) preloads frequently-used apps into otherwise-idle RAM — Windows drops this cache instantly when apps need memory, so it doesn't cause real shortages. Disabling it mainly helps on old HDD-based systems or when a buggy SysMain is implicated in 100% disk usage. On SSD systems with 8GB+ RAM, leave it enabled and look for actual leaks instead."
  - q: "How much RAM does Windows 11 24H2 actually need?"
    a: "Microsoft's minimum is 4GB, but that's barely functional. For comfortable daily use — browser with multiple tabs, Office, video calls — 8GB is the practical minimum and 16GB is the sweet spot where memory pressure largely disappears. If your laptop has 8GB soldered and you're constantly at 90%+, adding RAM (where the slot allows) is the only fix that addresses the root cause rather than managing symptoms."
---

Seeing 85% or 90% memory usage in Task Manager on Windows 11 24H2 feels wrong — like something is eating your RAM. Sometimes something is: a leaking driver, a runaway browser, or a pile of startup apps. But often the number is misleading, because Windows 11 deliberately fills "free" RAM with cache to make things faster, and that cache doesn't actually starve your apps. This guide shows you how to tell the difference — real memory pressure versus healthy caching — and fix the cases that are genuinely broken. For CPU-side pressure, see our [high CPU diagnostic approach](/articles/troubleshoot-search-indexing-high-cpu-windows-11/); for trimming what loads at boot, [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) pairs well with this.

## Why this happens

- **Memory compression working as designed**: Windows compresses idle pages instead of paging them — shows as "System and compressed memory" and is healthy.
- **Standby cache inflating the percentage**: SuperFetch/SysMain preloads apps into free RAM; it's released instantly when needed.
- **Driver memory leaks (non-paged pool growth)**: Buggy network, storage, or audio drivers allocate kernel memory and never free it.
- **Browser tab sprawl**: Modern browsers with dozens of tabs easily consume 3–6 GB on their own.
- **Startup app pile-up**: Chat clients, updaters, and utilities all resident from boot, each holding hundreds of MB.
- **Memory-hungry background services**: Search indexer, antivirus scans, and cloud sync clients during heavy operations.
- **Too little RAM for the workload**: 8GB laptops running Teams + browser + Office genuinely run out, forcing paging to disk.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read Task Manager's memory numbers correctly

Don't chase the headline percentage — read the composition.

1. Open **Task Manager** > **Performance** tab > **Memory** and look at the breakdown: **In use**, **Available**, **Committed**, **Cached**, and **Paged/Non-paged pool**.
2. Healthy sign: high "Cached" with plenty "Available" — Windows is just using free RAM smartly. Not a problem.
3. Real problem signs: "Available" under 1GB, "Committed" far above physical RAM (heavy paging), or non-paged pool above ~1.5GB on a normal laptop.
4. Switch to the **Processes** tab, sort by **Memory**, and identify the top consumers — note whether it's user apps (browser, Teams) or system processes.
5. Check the **Startup apps** tab and note the "Startup impact" column — high-impact apps are your trim candidates for Fix 5.

### Fix 2: Find and update the leaking driver

A growing non-paged pool is the classic driver-leak signature.

1. In Task Manager > **Performance** > **Memory**, record the **Non-paged pool** value, then check again after a few hours of use — steady growth means a leak.
2. Open **Device Manager** and look for warning icons; then update the usual suspects: network adapters (Wi-Fi and Ethernet), storage controllers, and audio drivers.
3. Get drivers from the right place: your laptop maker's support page (Dell, HP, Lenovo) or the chip vendor — Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) handles Intel Wi-Fi, Bluetooth, and graphics cleanly.
4. For a definitive identification, use **poolmon** (in the Windows Driver Kit) or **RAMMap** (Sysinternals) to see which driver tag is consuming non-paged pool, then update or roll back that specific driver.
5. If a leak appeared right after a driver update, roll it back: **Device Manager** > device > **Properties** > **Driver** tab > **Roll Back Driver**.

### Fix 3: Tame the browser — the usual biggest consumer

Browsers are the #1 RAM consumer on most laptops.

1. In your browser's task manager (Chrome/Edge: `Shift + Esc`), sort by memory — extensions and individual tabs are listed separately from the main process.
2. Remove or disable memory-heavy extensions you don't use daily; ad-blockers and shopping extensions are frequent offenders.
3. Enable tab sleeping/discarding: Edge has **Sleeping tabs** under Settings > System; Chrome has **Memory Saver** — both park inactive tabs.
4. If you routinely keep 30+ tabs open, use a session manager or bookmarks instead — no setting fully compensates for that habit.
5. Restart the browser daily if you never close it; browsers accumulate memory over multi-day sessions (extension leaks are common).

### Fix 4: Adjust virtual memory and check for paging storms

When RAM genuinely runs out, bad pagefile settings make it worse.

1. Open **Settings** > **System** > **About** > **Advanced system settings** > **Performance** > **Settings** > **Advanced** tab > **Virtual memory** > **Change**.
2. Keep **"Automatically manage paging file size for all drives"** checked in almost all cases — manual sizes from old guides usually hurt more than help.
3. Exception: if the pagefile is on a nearly-full drive, Windows can't grow it — free up disk space or move the pagefile to a drive with room.
4. In Task Manager > Performance > Memory, watch **Committed** vs. your RAM size during heavy use — if committed exceeds ~1.5x physical RAM regularly, you're paging hard and need more RAM or fewer concurrent apps.
5. Never disable the pagefile entirely to "save SSD wear" — Windows expects it to exist, and some apps crash without one.

### Fix 5: Cut startup and background bloat

Every resident app holds memory from the moment you log in.

1. In **Task Manager** > **Startup apps**, disable everything with **High** startup impact that you don't need immediately at login (updaters, chat clients, game launchers).
2. Go to **Settings** > **Apps** > **Installed apps** and uninstall utilities you don't recognize — OEM laptops often ship a dozen background helpers.
3. In **Settings** > **Privacy & security** > **Background apps** (or per-app Advanced options), set apps you rarely use to **Never** run in background.
4. Check **Task Scheduler** (`taskschd.msc`) for vendor tasks that launch memory-resident helpers at logon — Dell, HP, and Lenovo each add several.
5. Reboot and compare: a clean boot should show 35–50% memory use at idle on 8GB (mostly cache); if it's still 80%+ at idle with nothing open, suspect the driver leak from Fix 2. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the built-in memory diagnostic if you suspect faulty RAM hardware.

### Fix 6: Decide whether you need more RAM

Sometimes the honest fix is hardware.

1. Run **Windows Memory Diagnostic** (search for it in Start) if you suspect bad RAM — faulty modules cause the system to work around bad pages, inflating usage oddly.
2. Check if your laptop's RAM is upgradeable: many thin-and-lights solder it, but business and gaming laptops often have a free SO-DIMM slot — check the manual or maker's specs.
3. 8GB → 16GB is the upgrade that eliminates memory pressure for typical office/browsing workloads; 32GB only matters for VMs, video editing, or heavy development.
4. If RAM is soldered and insufficient, mitigate: keep browser tabs lean, close Teams/Slack when not in them, and avoid running Docker/VMs alongside everything else.
5. As a stopgap, **Storage Sense** and closing the biggest consumers before heavy tasks (video calls, games) keeps paging storms away.

## Closing

High memory usage in 24H2 is usually either healthy caching you can ignore, a fixable driver leak, or simply too many apps for the installed RAM. Read the composition numbers first, fix leaks at the driver level, trim the startup pile — and if the math still doesn't work, more RAM is the real answer, not another tweak.
