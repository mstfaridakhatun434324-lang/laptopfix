---
title: "File Explorer Slow on Windows 11 24H2? Speed It Back Up"
slug: how-to-fix-file-explorer-slow-in-windows-11-24h2
date: 2026-09-11
categories: ["performance"]
tags: ["file explorer", "windows 11 24h2", "slow performance", "explorer.exe", "folder lag"]
description: "File Explorer crawling after the Windows 11 24H2 update? Clear Quick Access history, fix folder view settings, and tune indexing to make it snappy again."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-in-windows-11-24h2.webp"
faqs:
  - q: "Why is File Explorer slow in Windows 11 24H2 specifically?"
    a: "Version 24H2 changed several Explorer behaviors: richer thumbnails, tighter OneDrive integration, and the tabbed interface's memory overhead all add latency. On machines upgraded rather than clean-installed, old thumbnail caches and carried-over view settings often conflict with the new rendering pipeline. The slowness is usually worst on first open and in folders with many media files, which points to cache and indexing issues rather than a failing drive."
  - q: "Will clearing Quick Access history actually make a difference?"
    a: "Often yes. Quick Access stores your recent files and frequent folders, and a bloated or corrupted history file can stall Explorer's launch by seconds. Clearing it forces Explorer to rebuild a leaner list, and many users report an immediate improvement on window open time. It's a thirty-second fix with no downside, so it's worth trying early — though if the lag happens when browsing deep folder trees, you'll need the cache and indexing fixes too."
  - q: "Is my hard drive dying, or is it just Windows 11 24H2?"
    a: "Start with software causes: open Task Manager while Explorer lags and check disk activity. If disk usage sits at 100% with low read/write throughput, suspect the drive; if disk is quiet while Explorer still stutters, it's a software issue. A healthy SSD with a clean thumbnail cache should open any folder near-instantly, so persistent multi-second delays on an SSD almost always trace back to Explorer settings, shell extensions, or search indexing."
  - q: "Can I go back to the old File Explorer if 24H2 broke it?"
    a: "There is no official way to revert only File Explorer — the Windows 10-style ribbon explorer was fully retired, and registry hacks to restore it no longer work reliably on 24H2. A full OS rollback within ten days of the update is possible, but it's a heavy hammer. In practice, clearing caches, disabling the preview pane, and trimming context-menu extensions solve the problem without leaving 24H2's security improvements behind."
---

Opening a folder shouldn't feel like booting up a machine from 2005, yet after the Windows 11 24H2 update plenty of laptops greet every Explorer window with a spinning cursor and a green progress bar that inches across the address bar. If you're a technician, this is a familiar pattern: the operating system changed, but your cache files, view settings, and third-party shell extensions carried over — and the combination fights the new rendering pipeline.

The good news: a slow File Explorer on 24H2 is almost never a hardware problem. In my experience it comes down to four things — a bloated thumbnail cache, Quick Access history gone stale, an over-aggressive search indexer rebuilding after the update, and shell extensions from uninstalled software still hooking into every right-click. Work through the fixes below in order and you'll typically find the culprit within twenty minutes.

One quick diagnostic before you start: time how long a new Explorer window takes to open versus how long it takes to navigate *within* it. Slow opens point at Quick Access and launch settings; slow navigation inside folders points at thumbnails, previews, and shell extensions. If Explorer also shows high CPU in Task Manager, the related guide on [taming File Explorer's CPU usage](/articles/how-to-fix-file-explorer-high-cpu-after-windows-11-update/) pairs well with this one, and our broader [File Explorer slow troubleshooting](/articles/best-way-to-fix-file-explorer-slow-windows-11/) covers edge cases like network folders.

## Why this happens

- **Stale thumbnail cache**: The 24H2 update changed thumbnail handling; the old cache becomes partially invalid and forces regeneration on the fly.
- **Bloated Quick Access history**: Corrupted or oversized `Recent` and `Frequent` data delays every new window's launch.
- **Search indexer rebuilding**: After a feature update, Windows re-indexes your files — Explorer queries hit an unfinished index and wait.
- **Dead shell extensions**: Uninstalled programs leave context-menu handlers that time out before Explorer finishes drawing.
- **Preview pane overhead**: The preview and details panes render rich previews for every selected file, multiplying per-folder latency.
- **OneDrive Files On-Demand**: Cloud placeholders with slow sync states make Explorer poll each file's status before showing the folder.
- **Folder view template mismatches**: Folders stuck on the wrong template (e.g., Pictures view on a documents folder) trigger expensive thumbnail generation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the thumbnail cache and Quick Access history

This resolves the majority of 24H2 Explorer slowness in one pass.

1. Open **Disk Cleanup** (search for it in Start), select your system drive, check **Thumbnails**, and click **OK** — this dumps the stale cache so 24H2 rebuilds it cleanly.
2. Open **File Explorer** > **...** menu (or View) > **Options** > **General** tab. Under **Privacy**, click **Clear** next to "Clear File Explorer history."
3. In the same Options window, set **Open File Explorer to** to **This PC** instead of Quick Access — this removes the slow frequent-files render from launch.
4. Still in Folder Options, go to the **View** tab and check **Always show icons, never thumbnails** temporarily — if folders now fly open, thumbnails were the bottleneck and you can re-enable them after the cache rebuilds.
5. Restart Explorer from Task Manager (right-click **Windows Explorer** > **Restart**) and test a few folders.

### Fix 2: Wait out — or tame — the search indexer

Right after 24H2 installs, the indexer can churn for hours.

1. Go to **Settings** > **Privacy & security** > **Searching Windows** and check the indexing status. If it says "Indexing in progress," give it time — plugging in and leaving the laptop idle speeds it up.
2. If indexing seems stuck for more than a day, click **Advanced Search Indexer Settings** > **Troubleshoot**, or use **Rebuild** to start fresh on a clean database.
3. Consider narrowing scope: under **Find my files**, switch from **Enhanced** to **Classic** mode so only libraries and Desktop are indexed — this dramatically cuts index churn on data-heavy machines.
4. Exclude folders you rarely search (large media archives, game installs) via **Add an excluded folder**. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the full indexer settings if you want the official walkthrough.
5. Restart the **Windows Search** service from `services.msc` after making changes and observe Explorer behavior for ten minutes.

### Fix 3: Prune dead shell extensions

Every right-click and every folder draw calls these handlers.

1. Download **ShellExView** from NirSoft (free, no install) and run it as administrator.
2. Sort by **Type** and look at **Context Menu** handlers from companies you don't recognize or software you uninstalled.
3. Select suspicious third-party extensions, right-click, and choose **Disable Selected Items** — disabling is reversible, unlike deleting.
4. Restart Explorer and test both folder navigation and right-click speed.
5. Re-enable extensions one batch at a time to identify the offender; leave the guilty one disabled or update/reinstall that program.

### Fix 4: Turn off the preview and details panes

These panes are convenient but expensive in media-heavy folders.

1. In File Explorer, press **Alt+P** to toggle the preview pane off and check the **View** menu to hide the **Details pane**.
2. Test navigation in a folder that was previously slow — image and video folders should respond noticeably faster.
3. For a deeper cut, in **Folder Options** > **View**, check **Display file icon on thumbnails** off is not needed, but do uncheck **Show preview handlers in preview pane** if you rarely use previews.
4. If you live in the preview pane, compromise: keep it off globally and enable it per-session only when reviewing documents.

### Fix 5: Fix OneDrive placeholder lag

OneDrive's cloud icons make Explorer query sync state per file.

1. Click the **OneDrive** cloud icon in the taskbar > **Settings** > **Sync and backup** > **Advanced settings** and review which folders are set to **Files On-Demand**.
2. For folders you browse constantly, right-click them in Explorer and choose **Always keep on this device** — local files render instantly.
3. If OneDrive is perpetually syncing, pause syncing for a few hours and see whether Explorer speeds up; a stuck sync queue is a classic cause.
4. As a last resort for heavy local workflows, **Unlink this PC** from OneDrive settings and access files purely locally.

### Fix 6: Reset folder views and templates

Wrong templates force Explorer to generate thumbnails it doesn't need.

1. Open **Folder Options** > **View** tab and click **Reset Folders** — this returns all folders of each type to sane defaults.
2. For a problem folder, right-click it > **Properties** > **Customize** tab and set **Optimize this folder for** to the correct type (General items, Documents, Pictures, Music, Videos).
3. Check **Also apply this template to all subfolders** before clicking OK.
4. Delete the hidden `desktop.ini` in folders that misbehave (enable **Show hidden files** first) — corrupt ones can force wrong templates back.

### Fix 7: Check the drive and update Windows

Rule out hardware and grab Microsoft's latest Explorer fixes.

1. Open **Task Manager** > **Performance** > your drive: if **Average response time** is consistently high while Explorer lags, run `chkdsk C: /f /r` from an elevated Command Prompt (schedule the reboot scan).
2. Check **Settings** > **Windows Update** — 24H2 has received multiple cumulative updates addressing Explorer performance; install everything pending. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you grab a specific cumulative update manually if Windows Update stalls.
3. Update your storage/chipset drivers from your laptop maker's support page — stale AHCI/NVMe drivers are a real cause of I/O stalls that look like Explorer bugs.
4. If nothing helps and the problem started exactly with 24H2, consider **Settings** > **System** > **Recovery** > **Go back** (available for ten days post-update) as a final option.

## Closing

File Explorer slowness after 24H2 is frustrating because the machine is clearly fast — it's one app dragging its feet. In nearly every case the fix is maintenance, not hardware: clear the caches, let the indexer finish, cut dead shell extensions, and stop OneDrive from interrogating every file. Do those and Explorer goes back to opening folders the instant you double-click them.
