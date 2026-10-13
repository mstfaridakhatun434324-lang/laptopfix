---
title: "How to Increase Virtual Memory on Windows 10 (Page File Guide)"
slug: "how-to-increase-virtual-memory-on-windows-10"
date: "2026-09-22"
categories: ["performance"]
tags: ["virtual memory", "page file", "windows 10", "ram", "performance"]
description: "Running out of memory on Windows 10? Learn how to safely increase virtual memory (the page file), what sizes to use, and when more RAM is the real answer."
thumbnail: "/images/thumbs/how-to-increase-virtual-memory-on-windows-10.webp"
faqs:
  - q: "What is virtual memory in Windows 10?"
    a: "Virtual memory is disk space that Windows 10 uses as an extension of physical RAM. When your RAM fills up, Windows moves less-used data to a hidden file called pagefile.sys so active programs keep running. It prevents out-of-memory crashes, but because disks are far slower than RAM, heavy paging makes the system feel sluggish. Increasing the page file gives Windows more breathing room, at the cost of disk space."
  - q: "How big should I set the page file on Windows 10?"
    a: "For most laptops, the classic guidance still works: set the initial size to 1.5 times your installed RAM and the maximum to 3 times your RAM. So with 8 GB of RAM, use 12288 MB initial and 24576 MB maximum. If you have 16 GB or more of RAM and an SSD, leaving Windows on automatic management is usually the better choice, since manual sizes rarely beat the system's own tuning."
  - q: "Will increasing virtual memory make my PC faster?"
    a: "Only if your PC is actually running out of RAM. If Task Manager shows memory usage constantly above 85-90% and the disk churning, a bigger page file reduces crashes and stuttering. But virtual memory is roughly a thousand times slower than RAM, so it never makes anything faster than adding real RAM would. If memory pressure is constant, the honest fix is a RAM upgrade, not a bigger page file."
  - q: "Is it safe to disable the page file completely?"
    a: "No, not on Windows 10. Some guides suggest disabling it on systems with lots of RAM, but Windows and many applications expect a page file to exist — crash dumps, memory-mapped files, and certain drivers depend on it. Disabling it can cause mysterious application crashes and prevents proper blue-screen diagnostics. At minimum, keep a small system-managed page file on the C: drive."
---

The dreaded 'Your computer is low on memory' warning usually arrives at the worst moment — mid-project, with a dozen browser tabs open and no time for a reboot. Windows 10 handles memory pressure with virtual memory: a slice of your disk that acts as overflow for RAM. When it's configured too small, programs crash, tabs die, and the whole system stutters.

Increasing virtual memory (the page file) is a legitimate, free fix — but it's widely misunderstood. It does not make your PC faster the way more RAM does; it gives Windows more room to juggle when RAM runs out, trading disk space for stability. Done wrong — a page file on a nearly full drive, or absurd manual sizes — it can actually make performance worse.

This guide walks you through checking whether virtual memory is really your problem, setting the right size, and knowing when the honest answer is a RAM upgrade instead. If your disk is the bottleneck rather than memory, our guide on [fixing 100% disk active time](/articles/best-way-to-fix-disk-active-time-100-percent/) covers that side of the problem.

## Why this happens

- **Too little RAM for the workload** — 8 GB of RAM with Chrome, Teams, and a photo editor open will exhaust physical memory fast. Virtual memory is the safety net, and the default automatic size sometimes lags behind sudden demand.
- **Page file set to a tiny custom size** — Old tweaking guides recommended small fixed page files. On modern Windows 10 with memory-hungry apps, a 2 GB fixed page file is a crash waiting to happen.
- **Page file on a nearly full drive** — The page file needs contiguous free space to work efficiently. On a C: drive with under 10% free, Windows may fail to grow the page file when it needs to, producing out-of-memory errors despite the setting.
- **Memory leaks in buggy drivers or apps** — A driver or program that slowly consumes RAM without releasing it will eventually exhaust both RAM and page file. No page file size survives a real leak — the fix is updating or removing the culprit.
- **Hibernation file competing for space** — On laptops, hiberfil.sys can consume RAM-sized chunks of the C: drive, leaving less room for the page file to grow. Disabling hibernation (if you never use it) frees that space.
- **SSD vs HDD page file performance** — Paging to a mechanical hard drive is painfully slow; paging to an SSD is merely slow. Where the page file lives matters almost as much as how big it is.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm memory pressure with Task Manager

Don't change the page file on a hunch. Verify that memory — not CPU or disk — is the constraint.

1. Press **Ctrl + Shift + Esc**, open the **Performance** tab, and click **Memory**.
1. Use the PC normally for 15 minutes, then check the **In use** figure and the **Committed** value.
1. If Committed regularly exceeds physical RAM and In use sits above 85%, you have genuine memory pressure — proceed.
1. If memory looks fine but the disk is pegged, see [fixing 100% disk active time](/articles/best-way-to-fix-disk-active-time-100-percent/) instead.

### Fix 2: Open the virtual memory settings

The page file settings live in the old System Properties dialog — here's the direct route.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
1. Go to the **Advanced** tab and click **Settings** under Performance.
1. In Performance Options, open the **Advanced** tab and click **Change** under Virtual memory.
1. Note the current settings before changing anything — screenshot them in case you need to revert.

### Fix 3: Set a sensible custom page file size

This is the core fix. Use the 1.5x/3x rule unless you have a specific reason not to.

1. Uncheck **Automatically manage paging file size for all drives**.
1. Select your **C:** drive, choose **Custom size**.
1. Set **Initial size (MB)** to 1.5 × your RAM in MB (8 GB RAM → 12288; 16 GB → 24576).
1. Set **Maximum size (MB)** to 3 × your RAM in MB (8 GB → 24576; 16 GB → 49152).
1. Click **Set**, then **OK**, and restart when prompted — the change takes effect on reboot.

### Fix 4: Move the page file to a faster or roomier drive

If C: is cramped but you have a second drive with space, the page file can live there.

1. In the same Virtual memory dialog, select **C:**, choose **No paging file**, and click **Set**.
1. Select the other drive, choose **System managed size** or a custom size, and click **Set**.
1. Keep a small (800 MB–2 GB) page file on C: as well — Windows needs one there for crash dumps.
1. Restart. Never put the page file on a USB flash drive or SD card; they're too slow and wear out.

### Fix 5: Free C: drive space so the page file can breathe

A page file can't grow on a full disk. Reclaim space before blaming the setting.

1. Run **Settings > System > Storage > Temporary files** and delete everything checked.
1. Uninstall large programs you don't use via **Settings > Apps**.
1. Aim for at least 20 GB free on C: after cleanup — the page file maximum plus headroom.

### Fix 6: Rule out a memory leak

If memory usage climbs steadily even when you're doing nothing, a bigger page file just delays the crash.

1. In Task Manager's **Processes** tab, sort by **Memory** and watch for a process whose usage grows unbounded over an hour.
1. Common culprits: outdated printer drivers, RGB control software, and browser extensions.
1. Update or uninstall the offender; check the manufacturer's support page for fixed drivers — for example [Dell's support site](https://www.dell.com/support) or [HP's](https://support.hp.com/us-en) for your model.
1. If a driver is the leaker, [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) can update Intel chipset and graphics drivers automatically.

### Fix 7: Know when to buy RAM instead

Virtual memory is a crutch, not a cure. If Task Manager shows constant memory pressure even after these fixes, price a RAM upgrade.

1. Check your laptop's manual or the manufacturer's specs for maximum RAM and slot count.
1. Most Windows 10 laptops accept DDR4 SODIMMs; a jump from 8 GB to 16 GB typically costs less than a dinner out.
1. After upgrading, you can usually return the page file to **Automatically manage** — Windows will size it appropriately. More RAM also speeds up [slow app launches](/articles/how-to-fix-apps-opening-slowly-on-windows-11/) across the board.

## Closing

Increasing virtual memory is a ten-minute job that stops out-of-memory crashes and smooths over RAM shortages — just remember it's buying stability, not speed. If you followed Fix 6 and found a leak, or Fix 7 and ordered RAM, you've fixed the actual problem rather than masking it.
