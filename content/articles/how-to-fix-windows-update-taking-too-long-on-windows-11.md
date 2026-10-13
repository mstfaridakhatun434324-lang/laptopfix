---
title: "Windows Update Taking Too Long on Windows 11? Speed It Up"
slug: how-to-fix-windows-update-taking-too-long-on-windows-11
date: 2026-09-30
categories: ["windows-update"]
tags: ["windows 11", "windows update", "slow", "performance"]
description: "Windows Update crawling for hours on Windows 11? Diagnose why it's slow and apply these fixes to get updates downloading and installing faster."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-on-windows-11.webp"
faqs:
  - q: "How long should a Windows 11 update normally take?"
    a: "A typical monthly cumulative update takes 15 to 45 minutes total on a modern laptop with an SSD and decent broadband — most of that in the install and restart phases. Feature updates take one to three hours. Times beyond that, especially a progress bar frozen for over an hour with no disk or network activity, indicate a stuck process rather than a slow one."
  - q: "Is it safe to restart during a slow update?"
    a: "If the update is genuinely progressing — disk and CPU active — do not interrupt it; forced restarts during the install phase can corrupt the component store. If Task Manager shows zero update-related activity for over an hour, the process is stuck and a restart is reasonable. After restarting, clear the update cache before retrying so the stuck state does not resume."
  - q: "Why is the download fast but the install slow?"
    a: "Download speed depends on your network; install speed depends on your disk and CPU. The install phase expands compressed files, verifies signatures, and updates the component store — all disk-intensive operations. On laptops with older SATA SSDs or limited RAM, this phase dominates the total time. Keeping the system idle and the drive defragmented-healthy helps."
  - q: "Does Delivery Optimization slow down my updates?"
    a: "Delivery Optimization can actually speed downloads by sourcing pieces from local PCs, but its default bandwidth limits throttle foreground and background download speeds. If your updates crawl on a fast unmetered connection, raising or removing those caps in Advanced options often produces an immediate, dramatic speedup."
---

There is slow, and then there is Windows Update slow: the progress bar that has not moved in two hours, the 'working on updates' screen that outlasts a movie, the download stuck at 37% since lunch. Some slowness is normal — updates are big and installs are complex — but multi-hour stalls usually signal a bottleneck you can actually fix.

The key distinction is between genuinely slow progress and a stuck process pretending to work. This guide helps you tell the difference, then addresses the real bottlenecks: throttled bandwidth, fragmented caches, competing background work, and underpowered staging. Your updates will not become instant, but they will stop taking all day.

It is also worth calibrating expectations by update type. Monthly cumulative updates should take under an hour on a healthy Windows 11 laptop; anything beyond two hours with no progress is abnormal. Feature updates are a different animal — two to four hours can be perfectly normal. Knowing which kind you are waiting on tells you whether to act or to make coffee.

## Why this happens

- **Bandwidth throttling:** Delivery Optimization limits update bandwidth by default, and metered flags or background limits can throttle downloads to a crawl without any visible warning.
- **Competing background activity:** Antivirus scans, cloud sync, and Dell or HP utilities running simultaneously steal the CPU and disk I/O the update installer needs.
- **Fragmented update cache:** A cache full of stale partial downloads forces the engine to verify and reconcile junk before making progress on the real update.
- **Slow storage:** Updates hammer the disk with random writes. Older SATA SSDs — and especially spinning drives — make the install phase dramatically slower than on NVMe drives.
- **Low memory:** Laptops with 4 GB of RAM page heavily during large updates, turning the install phase into a swap-bound crawl.
- **Corrupted download resuming:** A damaged partial file that Windows keeps resuming instead of replacing produces the classic symptom: progress that never advances.
- **Pending restart backlog:** Multiple queued updates install serially. What looks like one slow update is often several updates waiting their turn behind a deferred restart.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is slow or stuck

Do not intervene in a healthy-but-slow update. Open Task Manager and check whether the update processes are actually consuming CPU, disk, and network. Active resource use means progress; flatlined resources for over an hour mean stuck — and only stuck updates need the fixes below. Screenshot the Task Manager graphs when you check — if you later need help, that evidence distinguishes a slow update from a stuck one instantly.

1. Open Task Manager with Ctrl + Shift + Esc.
2. Watch CPU, disk, and network usage for several minutes.
3. Steady activity means the update is working — give it more time.
4. Zero activity for over an hour means it is stuck; proceed with the repairs.

### Fix 2: Remove bandwidth limits

Windows may be politely throttling itself. Delivery Optimization bandwidth caps and metered connection flags both slow downloads dramatically, and lifting them is instant and safe on unmetered networks.

1. Open Settings, Windows Update, Advanced options, Delivery Optimization, Advanced options.
2. Uncheck or raise the bandwidth limits for downloads.
3. Check that your network is not flagged as metered in Wi-Fi settings.
4. Restart the download and compare the speed.

### Fix 3: Clear the stale update cache

A cache cluttered with partial and failed downloads slows every new update as the engine verifies the mess. Clearing it gives the current update a clean, fast path. Guidance from [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) lists cache corruption among the top causes of stalled updates. Relentless background disk activity during updates is often the [Windows Modules Installer worker](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-on-dell-laptop/) doing its job slowly.

1. Open Command Prompt as administrator.
2. Run net stop wuauserv and net stop bits.
3. Empty C:\Windows\SoftwareDistribution\Download.
4. Run net start wuauserv and net start bits, then check for updates.

### Fix 4: Free up CPU and disk during the update

Updates compete for resources with everything else running. Pausing the competition — cloud sync, antivirus scans, OEM utilities — hands the installer the CPU and disk headroom it needs to finish faster. When slowness is really a stall at the restart screen, the [update stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update/) guide applies.

1. Pause OneDrive, Dropbox, or other cloud sync during the update.
2. Postpone manual antivirus scans until the update completes.
3. Close heavy applications and browser tabs.
4. Let the update run with the system otherwise idle.

### Fix 5: Install the update in smaller pieces

A massive queued backlog installs serially and feels endless. Installing the latest cumulative update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) collapses the backlog into a single package, which is often faster than letting Windows chew through the queue one item at a time.

1. Check Update history to see how many updates are queued.
2. Download the latest cumulative update for your build from the catalog.
3. Install it manually and restart.
4. Let Windows Update handle only the small remainder afterward.

### Fix 6: Address hardware bottlenecks

If updates are always slow on the same laptop, the bottleneck is hardware. The honest fixes: more free disk space so staging is not cramped, and avoiding sleep during installs so the process is never interrupted mid-write.

1. Keep at least 20 GB free on the system drive.
2. Set the power plan to never sleep while plugged in during updates.
3. On older laptops, consider the update an overnight task rather than fighting it.
4. For persistently slow machines, an SSD upgrade is the single biggest speedup.

## Closing

Windows Update slowness is usually a bottleneck, not a mystery: throttled bandwidth, a cluttered cache, resource competition, or hardware limits. Diagnose stuck versus slow first, then clear the path — bandwidth caps off, cache cleaned, background work paused. Updates will never be instant, but they will stop consuming your entire day.
