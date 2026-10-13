---
title: "How to Fix a Laptop Running Slow on Windows 10"
slug: how-to-fix-laptop-running-slow-on-windows-10
date: 2026-09-02
categories: ["performance"]
tags: ["slow laptop", "windows 10", "speed up", "performance", "lagging"]
description: "Windows 10 laptop running slow? Speed it up with startup trimming, visual effects tuning, disk cleanup, and driver updates — no reinstall needed."
thumbnail: "/images/thumbs/how-to-fix-laptop-running-slow-on-windows-10.webp"
faqs:
  - q: "Why is my Windows 10 laptop so slow all of a sudden?"
    a: "Sudden slowness usually has a trigger: a Windows update installing in the background, antivirus running a full scan, disk space dropping below 10%, a runaway process eating CPU, or a browser with dozens of tabs consuming all RAM. Check Task Manager first — sort by CPU, memory, and disk to spot the immediate cause before changing any settings."
  - q: "Will upgrading to Windows 11 make my slow laptop faster?"
    a: "Rarely. Windows 11 has slightly higher system requirements and won't fix the underlying causes of slowness — startup bloat, full disks, old drivers, or insufficient RAM. Fix the actual problems on Windows 10 first. Only upgrade if your hardware meets the requirements and you want the newer OS; don't expect a performance miracle."
  - q: "How much RAM do I need for Windows 10 to run well?"
    a: "8 GB is the practical minimum for comfortable multitasking in 2026 — web browsing, Office, and streaming simultaneously. 4 GB machines will constantly hit the pagefile and feel sluggish no matter how much you tune. If Task Manager shows memory regularly above 85%, a RAM upgrade gives the biggest per-dollar speed improvement of any change."
  - q: "Is it safe to disable all startup programs?"
    a: "Disabling third-party startup programs is safe — you can always launch them manually. Leave Microsoft services and your antivirus enabled. The risk is minor inconvenience: a cloud sync client won't auto-sync, a chat app won't auto-launch. If something you need stops working as expected, re-enable that one entry."
---

Windows 10 still runs on hundreds of millions of laptops, and a huge share of them have gotten slow over the years — not because the hardware aged, but because the software piled up. Every installed app adds a startup entry, every update adds background work, and the disk fills with years of cruft. The good news: a slow Windows 10 laptop is almost always fixable in an afternoon, and the fixes are the same ones technicians have used for a decade.

The approach is layered: stop the bleeding (runaway processes, full disk), cut the fat (startup apps, visual effects), then tune the engine (drivers, power plan, storage). For Windows 11-specific speedups see [speeding up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/); for browser-caused slowdowns see [fixing Chrome high CPU](/articles/how-do-i-fix-chrome-high-cpu-windows-11/).

## Why this happens

- **Startup program accumulation**: Years of installs each adding auto-launch entries that fight for resources at boot and linger forever.
- **Full or fragmented system drive**: Under 10–15% free space, Windows can't manage the pagefile or temp files efficiently.
- **Insufficient RAM for modern workloads**: 4 GB machines constantly paging to disk; browsers alone can eat 6 GB.
- **Spinning hard drive instead of SSD**: The single biggest hardware bottleneck — HDD laptops feel slow doing anything disk-related.
- **Outdated drivers**: Old chipset, storage, and graphics drivers that waste CPU on inefficient I/O.
- **Background Windows Update activity**: Update downloads, staging, and the TiWorker process consuming CPU and disk for hours.
- **Visual effects on weak hardware**: Transparency and animations taxing old integrated graphics.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find what's slow right now

Start with the live evidence.

1. Open Task Manager (**Ctrl+Shift+Esc**) and check the **Processes** tab sorted by **CPU**, then **Memory**, then **Disk** — the top consumer in any column at 80%+ sustained is your immediate problem.
2. Check the **Performance** tab: memory consistently above 85% means you need more RAM or fewer apps; disk at 100% on an HDD means the drive is the bottleneck.
3. Note whether slowness is constant or situational — constant points to system-wide causes (startup bloat, full disk); situational points to a specific app or trigger.
4. Check free space on C: in File Explorer — under 15% free is a red flag for multiple slowdown mechanisms at once.
5. This five-minute diagnosis tells you which of the fixes below will actually matter for your machine.

### Fix 2: Gut the startup list

The classic fix because it works.

1. In Task Manager, go to the **Startup** tab (Windows 10's name for it) and sort by **Startup impact**.
2. Disable everything rated **High** that isn't your antivirus or something you need within a minute of booting — updaters, chat clients, game platforms, cloud storage, printer utilities.
3. Be thorough: right-click > **Disable** on each. Disabling never uninstalls — the app still works when you launch it.
4. Check the Startup folders too: `Win+R` > `shell:startup` — delete shortcuts for things you don't want auto-launching.
5. Restart (not shut down — with Fast Startup, restart gives a cleaner test) and feel the difference at login.

### Fix 3: Free disk space and clean up

Give Windows room to breathe.

1. Run **Disk Cleanup** (`cleanmgr.exe`) as administrator — check **Windows Update Cleanup**, **Temporary files**, **Delivery Optimization Files**, and **Previous Windows installations** (this last one can free 20+ GB).
2. Go to **Settings** > **System** > **Storage** and turn on **Storage Sense** — set it to run automatically and clear temp files and the Recycle Bin on a schedule.
3. Uninstall programs you haven't used in a year: **Settings** > **Apps** > **Apps & features**, sort by size, and remove the big forgotten ones.
4. Move large personal files (videos, installers, downloads) off C: to an external drive or second partition.
5. Aim for at least 20% free on C: — below that, everything from updates to the pagefile starts struggling.

### Fix 4: Tune visual effects for the hardware

Free GPU and CPU cycles on older machines.

1. Press **Win+R**, type `sysdm.cpl`, go to **Advanced** > **Performance** > **Settings**.
2. Choose **Adjust for best performance**, then re-check just **Smooth edges of screen fonts** and **Show thumbnails instead of icons** — this keeps Windows usable-looking while killing the expensive effects.
3. Go to **Settings** > **Personalization** > **Colors** and turn off **Transparency effects**.
4. On very old hardware, also reduce the display scaling if it's set unusually high — less compositing work.
5. The visual difference is minor; the responsiveness difference on weak integrated graphics is immediately noticeable.

### Fix 5: Update drivers and Windows

Old drivers waste cycles; pending updates burn resources in the background.

1. Install all pending Windows updates (**Settings** > **Update & Security** > **Windows Update**) — a system stuck "preparing" updates stays slow until they're done.
2. Update the chipset driver from your laptop maker's support page — since Windows Update's chipset drivers lag behind the vendor's releases.
3. Update the graphics driver from the vendor ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD) — old display drivers are a quiet source of UI lag.
4. In **Device Manager**, resolve any yellow-warning devices — broken drivers cause retries that show up as mysterious CPU usage.
5. After updates, give the system one full idle hour (plugged in) to finish background optimization, then judge performance.

### Fix 6: Set the right power plan and check the drive

Two hardware-adjacent checks with big payoffs.

1. Go to **Control Panel** > **Power Options** and select **High performance** (or **Balanced** at minimum) — **Power saver** throttles the CPU aggressively and makes everything feel slow.
2. Check whether you have an HDD or SSD: Task Manager > **Performance** > **Disk** shows the type. If it's an HDD, upgrading to an SSD is the single biggest speed upgrade possible — more impactful than RAM or CPU on old laptops.
3. On HDDs, run **Defragment and Optimize Drives** (`dfrgui.exe`) — on SSDs, make sure it's set to TRIM (retrim), never defrag.
4. Run `chkdsk C: /scan` from an elevated prompt to catch file-system issues.
5. If the HDD is old, check its SMART health with the maker's tool — a failing drive gets progressively slower before it dies.

### Fix 7: Reset the software pile (without losing data)

When years of cruft resist piecemeal fixes.

1. Back up your personal files (this is non-negotiable before any reset).
2. Go to **Settings** > **Update & Security** > **Recovery** > **Reset this PC** > **Get started** > **Keep my files** — this reinstalls Windows while preserving personal data.
3. Choose **Cloud download** if your internet is decent — it fetches a clean, current Windows image.
4. After the reset, install drivers from the vendor first, then apps one by one — resist reinstalling everything at once, or you'll rebuild the same bloat.
5. Microsoft documents the reset options fully at [Windows support](https://support.microsoft.com/en-us/windows) if you want the fine print on what "keep my files" preserves.

## Closing

Windows 10 slowness is accumulated, not inherent — startup bloat, a full drive, old drivers, and underpowered hardware for modern workloads. Work the list in order and most laptops feel dramatically faster by Fix 4; the SSD upgrade in Fix 6 is the one purchase that transforms old machines. And if the laptop has 4 GB of RAM and a spinning drive in 2026, no amount of tuning beats the honest hardware answer: SSD first, RAM second.
