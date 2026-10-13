---
title: "How to Increase Virtual Memory in Windows 11 24H2"
slug: how-to-increase-virtual-memory-in-windows-11-24h2
date: 2026-09-20
categories: ["performance"]
tags: ["virtual memory", "pagefile", "windows 11 24h2", "ram", "performance"]
description: "Running out of memory on Windows 11 24H2? Learn how to increase virtual memory (pagefile) safely, what size to set, and when RAM is the real answer."
thumbnail: "/images/thumbs/how-to-increase-virtual-memory-in-windows-11-24h2.webp"
faqs:
  - q: "What is virtual memory and how does the pagefile work?"
    a: "Virtual memory is disk space Windows uses as overflow for RAM: when physical memory fills up, Windows moves idle data to the pagefile (pagefile.sys) to free RAM for active work. It's dramatically slower than RAM — it's an emergency spillover, not an extension. Increasing it prevents out-of-memory crashes on RAM-limited machines but doesn't make anything faster."
  - q: "What size should I set the pagefile to?"
    a: "The classic guidance: initial size 1.5× your RAM, maximum 3× your RAM — so 12GB initial / 24GB max on an 8GB machine. On SSDs with 16GB+ RAM, letting Windows manage it automatically is usually fine. Never set it below 800MB–1GB (crash dumps need space), and don't set enormous fixed sizes on small SSDs — you're just wasting disk."
  - q: "Will increasing virtual memory make my laptop faster?"
    a: "No — and anyone promising that is mistaken. The pagefile is orders of magnitude slower than RAM; more of it only means the system can survive deeper memory pressure without crashing, while running slower during that pressure. If your laptop is slow because RAM is full, the fixes are: use less RAM (close things), or add physical RAM. The pagefile is a safety net, not a performance upgrade."
  - q: "Should I disable the pagefile if I have lots of RAM?"
    a: "No. Even with 32GB+ RAM, some Windows components and applications expect a pagefile to exist and misbehave without one — including crash dump generation and certain memory-mapped operations. Leave at least a small system-managed pagefile. Disabling it entirely is an old tweaking myth that causes more problems than it solves."
---

"Your computer is low on memory" — the warning nobody wants, usually appearing mid-project with a dozen browser tabs open on an 8GB laptop. Windows 11 24H2 manages virtual memory automatically, and for most machines that's fine. But on RAM-limited laptops, or when the automatic sizing goes wrong, manually increasing the pagefile is the difference between a working session and a crash.

This guide shows exactly where the setting lives in 24H2, what sizes make sense for your RAM and disk, and — just as important — when virtual memory isn't the answer and physical RAM is.

## Why this happens

- **Automatic sizing too conservative:** Windows sometimes sets a pagefile too small for the actual workload.
- **RAM fully committed:** Browsers, creative apps, and VMs genuinely exceeding physical memory.
- **Memory leaks:** Buggy apps or drivers slowly consuming RAM until the pagefile is the only relief.
- **Pagefile on a full disk:** No free space for the pagefile to grow into.
- **Pagefile fragmented or capped:** A manually set tiny pagefile from old tweaking advice.
- **Crash dumps needing space:** Too-small pagefiles break dump generation, hiding the real problem.
- **SSD vs HDD placement:** A pagefile on a slow HDD makes paging painfully slow.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm memory pressure is the real problem

Open Task Manager's Performance tab → Memory during your heaviest workload. If **Committed** is near the **Commit limit** (RAM + pagefile), you're genuinely out of virtual memory — increasing the pagefile helps. If RAM is only half-used when the warning appears, something else is wrong (a per-process limit or a leak), and a bigger pagefile won't help. Also check the Processes tab sorted by Memory to find the hog. Diagnose first: the [high memory usage fix](/articles/windows-11-high-memory-usage-fix/) covers the RAM-side investigation in depth.

1. Open Task Manager → Performance → Memory under heavy load.
2. Compare Committed against the Commit limit.
3. Sort Processes by Memory to find the biggest consumers.
4. Proceed only if committed memory is near the limit.

### Fix 2: Increase the pagefile in 24H2's settings

The path: **Settings → System → About → Advanced system settings** (link on the right) → **Advanced tab → Performance → Settings → Advanced tab → Virtual memory → Change**. Uncheck **Automatically manage paging file size for all drives**, select your system drive (ideally the SSD), choose **Custom size**, and set Initial to 1.5× your RAM in MB and Maximum to 3× (e.g., 12288 / 24576 for 8GB). Click Set, OK, and reboot. Windows allocates the new pagefile on restart. The [general virtual memory guide](/articles/how-to-increase-virtual-memory-on-laptop/) covers the same steps for all Windows versions.

1. Open Advanced system settings → Performance Settings → Advanced.
2. Click Change under Virtual memory.
3. Uncheck automatic management; select the system drive.
4. Set Custom size (1.5× / 3× RAM in MB), click Set, reboot.

### Fix 3: Put the pagefile on the fastest drive with free space

If you have multiple drives, placement matters. The pagefile should live on your fastest drive — the NVMe/SATA SSD, never a spinning HDD or a nearly-full disk. In the same Virtual memory dialog, you can set **No paging file** on slow drives and a **System managed** or custom size on the SSD. Ensure at least 15–20% free space remains on that drive afterward; a pagefile fighting for the last gigabytes of disk is a new problem. On single-drive laptops, just make sure C: has breathing room via Storage Sense.

1. Identify your fastest drive in Task Manager → Performance.
2. Move the pagefile there; set No paging file on slow drives.
3. Keep 15–20% free space on the pagefile drive.
4. Reboot and verify the new size in the dialog.

### Fix 4: Find and fix the memory hog or leak

A bigger pagefile treats the symptom; the hog is the disease. In Task Manager's Details tab, add the **Commit size** column and watch for a process whose commit grows unboundedly over hours — that's a leak. Update or replace the leaking app; for browser leaks, disable extensions one by one (they're the usual suspects). For driver leaks (non-paged pool growth visible in Performance → Memory), update the associated driver — network and audio drivers are classic leakers. Microsoft documents pool monitoring in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Add the Commit size column in Task Manager Details.
2. Watch for processes growing without bound.
3. Update/replace leaking apps; test browser extensions.
4. Update drivers if non-paged pool is growing.

### Fix 5: Reduce memory demand before upgrading

Free RAM is the cheapest RAM. Close browser tabs aggressively (each tab is a process), quit apps instead of minimizing, and disable startup programs you don't need (**Task Manager → Startup apps**). In **Settings → Apps**, uninstall software you forgot existed. For 8GB machines, these habits genuinely determine whether the pagefile gets hit: the difference between 30 tabs and 10 tabs is often the difference between smooth and paging. The [speed-up guide](/articles/how-to-speed-up-windows-11-laptop/) bundles these demand-reduction steps with other quick wins.

1. Cut browser tabs and quit unused apps.
2. Disable unneeded startup programs.
3. Uninstall forgotten software.
4. Re-check committed memory under load.

### Fix 6: Upgrade physical RAM when the pagefile isn't enough

The honest endpoint: if committed memory routinely exceeds RAM even after cleanup, and the machine feels slow during paging (disk thrashing, stuttering), no pagefile size fixes the speed — you need more RAM. Check your laptop's maximum RAM and slot availability (Task Manager → Performance → Memory shows slots used). An 8GB→16GB upgrade is the single most transformative change for a paging laptop, and on many models it's a 15-minute job. Until then, the bigger pagefile from Fix 2 keeps you crash-free.

1. Check slots used and maximum RAM in Task Manager.
2. Look up your model's RAM specs and upgrade procedure.
3. Install matched RAM sticks.
4. Revert the pagefile to automatic management afterward.

## Closing

Virtual memory is a safety net, not a speed upgrade: size it correctly (1.5×/3× RAM), put it on the fastest drive, and fix the hog that's filling it. On RAM-starved laptops it prevents crashes; for actual speed, nothing beats using less RAM or installing more of it. Set the pagefile right, then address the real demand.
