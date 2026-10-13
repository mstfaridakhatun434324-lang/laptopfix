---
title: "File Explorer Running Slow? Fix It Step by Step"
slug: how-to-fix-file-explorer-slow-step-by-step
date: 2026-09-18
categories: ["performance"]
tags: ["file explorer slow", "windows explorer", "step by step", "performance", "windows 11"]
description: "A step-by-step fix sequence for a sluggish File Explorer in Windows 11, from Quick Access clutter to shell extensions and corrupted caches."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-step-by-step.webp"
faqs:
  - q: "Why is File Explorer slow even on a fast computer?"
    a: "File Explorer's speed depends on what it's loading, not your CPU. Network locations, disconnected mapped drives, giant folders with thousands of files, broken shell extensions, and a bloated Quick Access history all delay every window. A brand-new laptop can show these symptoms if a mapped drive from an old network is timing out — Explorer waits for the network before it draws the window."
  - q: "Does clearing Quick Access history really help?"
    a: "Yes, in many real cases. Quick Access pins and frequent folders are re-evaluated every time a window opens, and stale entries pointing to removed drives or offline network paths force timeout waits. Clearing the history and removing dead pins is a one-minute job that fixes a surprising share of 'Explorer takes forever to open' complaints."
  - q: "Can third-party programs slow down File Explorer?"
    a: "Absolutely — shell extensions are the most common hidden cause. Archive tools, cloud storage apps, and antivirus products inject entries into Explorer's right-click menu and property handlers. A single badly written extension can add seconds to every window and right-click. ShellExView lets you disable them selectively to find the offender without uninstalling anything."
  - q: "Is restarting Explorer the same as restarting the laptop?"
    a: "No. Restarting the Explorer process clears its in-memory caches, stuck COM objects, and leaked handles without rebooting. It fixes slowness caused by a degraded session — the kind that builds up over days of uptime. A full restart additionally resets drivers and services. Use the process restart as your quick test; if it helps but the problem returns within hours, something is loading badly each session."
---

File Explorer should snap open. When double-clicking a folder feels like sending a letter — click, wait, watch the green address bar crawl — the problem is almost always something Explorer is trying to load, not something wrong with Windows itself. Every window opening triggers a cascade: Quick Access pins, network locations, shell extensions, thumbnail generation, and search indexing all compete to finish before the window draws.

The fix sequence below is ordered by payoff. Start at the top, test after each fix, and stop when windows open instantly. Most people never get past Fix 3.

## Why this happens

- **Quick Access clutter:** Dead pins and a long frequent-folders history force Explorer to resolve paths that no longer exist, with timeout waits each time.
- **Disconnected network drives:** Mapped drives to offline machines make Explorer wait for network timeouts before rendering anything.
- **Broken shell extensions:** Third-party context-menu and property handlers from archive tools, cloud apps, or antivirus stall every window and right-click.
- **Thumbnail generation overload:** Folders full of photos or videos trigger on-demand thumbnail rendering that blocks the view.
- **OneDrive sync churn:** Files stuck syncing or set to Files On-Demand show placeholder states Explorer must query.
- **Corrupted icon/thumbnail cache:** Damaged cache databases cause Explorer to rebuild them repeatedly, freezing folders.
- **Search indexing a huge drive:** The indexer competing for disk I/O while you browse slows both activities.
- **A degraded Explorer session:** Days of uptime with leaked handles and stuck COM objects gradually make everything sluggish.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Explorer process (the 30-second test)

Open Task Manager, find **Windows Explorer** under Processes, right-click it, and choose Restart. Your taskbar will flicker and come back. Now open a folder and time it. If windows now open quickly, the slowness was session degradation — leaked handles or stuck components — and you have a working baseline. If nothing changed, the cause is persistent configuration, and you keep going.

1. Open Task Manager (Ctrl + Shift + Esc).
2. Find **Windows Explorer** under Processes.
3. Right-click it and choose **Restart**.
4. Open a folder immediately and judge the speed.

### Fix 2: Clean up Quick Access

Open Folder Options (search "Folder Options" in Start), and under the General tab click **Clear** next to "Clear File Explorer history." Then, in the Explorer navigation pane, right-click any dead or unwanted pins under Quick Access and choose **Unpin**. Change "Open File Explorer to" from Quick Access to **This PC** if you want windows to open without resolving your history at all. This one fix resolves the majority of slow-open complaints. For related Windows 11 Explorer issues, the [Windows 11 Explorer slow guide](/articles/how-do-i-fix-file-explorer-slow-windows-11/) covers additional angles.

1. Search Start for **Folder Options** and open it.
2. Under General, click **Clear** next to Clear File Explorer history.
3. In Explorer's navigation pane, right-click dead pins and choose **Unpin from Quick access**.
4. Optionally set "Open File Explorer to" to **This PC** and click OK.

### Fix 3: Disconnect stale network drives

Open This PC and look for mapped drives showing a red X or hanging when clicked. Right-click each suspect drive and choose **Disconnect**. If you need the mapping, remap it fresh with the "Reconnect at sign-in" option unchecked until you confirm it's stable. Explorer waits on network timeouts for every dead mapping before it will draw a window — this is the single biggest hidden cause of Explorer slowness on laptops that move between networks. Microsoft documents mapped drive behavior in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open **This PC** in File Explorer.
2. Identify mapped drives with a red X or that hang when opened.
3. Right-click each and choose **Disconnect**.
4. Open a new Explorer window and check the speed.

### Fix 4: Disable misbehaving shell extensions

Download ShellExView (free, from NirSoft), run it, and sort by Type. Select all non-Microsoft context menu and property sheet extensions, right-click, and choose **Disable Selected Items**. Restart Explorer. If speed returns, re-enable extensions a few at a time until the lag returns — the last batch contains your culprit. This is surgical: you're disabling the hook, not uninstalling the program, so nothing else breaks.

1. Download and run ShellExView.
2. Filter to non-Microsoft shell extensions (context menu, property sheet types).
3. Disable them all, then restart the Explorer process.
4. Re-enable in small batches to identify the specific offender.

### Fix 5: Rebuild the thumbnail and icon caches

In Disk Cleanup (cleanmgr), check **Thumbnails** and run it to clear the cache. For a deeper rebuild, delete the icon cache database at `%localappdata%\IconCache.db` and the thumbnail cache files in `%localappdata%\Microsoft\Windows\Explorer\` (the `thumbcache_*.db` files) after ending the Explorer process, then restart it. Windows rebuilds the caches fresh on next browse. Corrupted caches cause Explorer to freeze while repeatedly failing to read them — a fresh rebuild ends the loop.

1. Run Disk Cleanup and check **Thumbnails**; let it finish.
2. End the Explorer process in Task Manager (don't restart it yet).
3. Delete `thumbcache_*.db` files in `%localappdata%\Microsoft\Windows\Explorer\`.
4. Restart Explorer from Task Manager (**File → Run new task → explorer.exe**).

### Fix 6: Pause OneDrive sync during testing

Right-click the OneDrive cloud icon in the system tray and choose **Pause syncing** for 2 hours. Browse your folders and compare. If speed recovers, the problem is sync-related: files stuck in "sync pending," a huge pending queue, or Files On-Demand placeholders on a slow connection. Fix the sync queue (resolve errors in the OneDrive panel) rather than pausing forever. Persistent Explorer hangs tied to sync are also covered in the [troubleshooting walkthrough](/articles/troubleshoot-file-explorer-slow-windows-11/).

1. Right-click the OneDrive tray icon.
2. Choose **Pause syncing** → 2 hours.
3. Browse folders and compare speed.
4. If faster, open the OneDrive panel and resolve any sync errors or stuck files.

### Fix 7: Narrow Windows Search indexing

Open **Indexing Options** from Start, click Modify, and uncheck locations you never search — entire secondary drives, developer folders with hundreds of thousands of files, archives. Indexing competes for the same disk I/O Explorer needs. Then run the Search and Indexing troubleshooter. This won't make Explorer instant on its own, but on machines where the indexer is always active, it removes a constant drag that amplifies every other cause.

1. Open **Indexing Options** from Start.
2. Click **Modify** and uncheck drives/folders you never search.
3. Click OK, then run the **Search and Indexing** troubleshooter.
4. Give the indexer an hour to settle, then re-test Explorer.

## Closing

Explorer slowness is additive: a little Quick Access clutter, one dead network drive, and a bad shell extension combine into an experience that feels like a broken computer. Working top-down — restart, declutter, disconnect, disable, rebuild — peels the layers off in order of likelihood. When the window snaps open again, you'll know exactly which layer was the problem, and you'll recognize it instantly if it ever comes back.
