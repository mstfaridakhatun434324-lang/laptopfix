---
title: "File Explorer High CPU in Windows 11 24H2? Fix It"
slug: how-to-fix-file-explorer-high-cpu-in-windows-11-24h2
date: 2026-09-25
categories: ["performance"]
tags: ["file explorer high cpu", "explorer.exe", "windows 11 24h2", "shell extensions"]
description: "File Explorer (explorer.exe) eating CPU on Windows 11 24H2 even when idle? Trace it to shell extensions, thumbnails, or cloud sync — and fix it."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Why is File Explorer using so much CPU when I'm not doing anything?"
    a: "Explorer does background work even when no window is visible: generating thumbnails, syncing cloud files, indexing, and loading third-party shell extensions. High idle CPU almost always means one of these is stuck — a corrupt thumbnail cache, a cloud file stuck syncing, or a buggy context-menu extension. The 24H2 update made this more common by changing Explorer internals that older shell extensions weren't built for."
  - q: "Is it safe to restart File Explorer from Task Manager?"
    a: "Yes, completely safe — it's the standard fix for a glitched Explorer. Right-click Windows Explorer in Task Manager's Processes tab and choose Restart; your taskbar and desktop briefly disappear and return. Open apps and unsaved work are unaffected. If high CPU returns immediately after the restart, the trigger is persistent and needs the deeper fixes below."
  - q: "Can shell extensions really cause high CPU?"
    a: "Absolutely — they're the leading cause. Every right-click menu entry from third-party software loads code into Explorer's process, and a single buggy or outdated extension can burn CPU constantly. The 24H2 update broke compatibility with several older extensions. Disabling non-Microsoft extensions with a tool like ShellExView and re-enabling selectively is the definitive test."
  - q: "Why did Explorer get worse after the 24H2 update?"
    a: "24H2 reworked parts of File Explorer, including its XAML-based interface components, which invalidated assumptions some third-party extensions and tweaks relied on. Corrupt thumbnail caches and search indexes migrated badly can also leave Explorer churning. Most post-24H2 Explorer CPU issues trace to either an incompatible extension or a corrupt cache — both fixable without reinstalling Windows."
---

**File Explorer** burning CPU while you're not even browsing files is disorienting — `explorer.exe` isn't just the file manager, it's the Windows shell: taskbar, desktop, Start menu. When it misbehaves, the whole interface feels sick. On Windows 11 24H2, Explorer CPU spikes trace to a familiar lineup: third-party shell extensions, thumbnail generation gone wrong, cloud sync churn, and caches corrupted by the update.

The diagnostic approach is elimination: restart Explorer to clear transient glitches, then strip away the add-ons until the culprit shows itself. For related shell-adjacent issues, see [SearchApp.exe high CPU](/articles/how-to-fix-searchapp-exe-high-cpu-in-windows-11-24h2/); for general system load, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Buggy third-party shell extensions**: Context-menu handlers from old software loading broken code into Explorer.
- **Corrupt thumbnail cache**: Damaged thumbnails.db files causing endless regeneration attempts.
- **Cloud sync churn**: OneDrive/Dropbox constantly syncing or stuck on a file, with Explorer monitoring every change.
- **24H2 extension incompatibility**: Older shell extensions conflicting with reworked Explorer internals.
- **Corrupt search index**: Explorer querying a broken index for every folder view.
- **Network folder timeouts**: Explorer hanging on unreachable network locations, retrying constantly.
- **Quick Access corruption**: A damaged Quick Access cache making Explorer work on every open.
- **Malware hiding in the shell**: Malicious shell extensions are a real (if uncommon) persistence technique.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and check the pattern

Clear the transient states first.

1. Open **Task Manager** > **Processes**, right-click **Windows Explorer** > **Restart** — the taskbar blinks and returns.
2. Watch CPU for 10 minutes: if it stays low, it was a transient glitch — done.
3. If CPU climbs again, note the trigger: does it spike when you open a specific folder (thumbnails/shell extensions for that file type), or is it constant even with no Explorer window open (background cause)?
4. Check whether CPU correlates with network activity — constant network + Explorer CPU suggests cloud sync or unreachable network paths.
5. Open **Task Manager** > **Details** to confirm it's actually **explorer.exe** and not a similarly-named process.

### Fix 2: Disable third-party shell extensions

The highest-probability permanent fix.

1. Download **ShellExView** (NirSoft, free) — run it (no install needed).
2. Go to **Options** > **Hide All Microsoft Extensions** — you're now looking at third-party code injected into Explorer.
3. Select all non-Microsoft extensions, right-click > **Disable Selected Items**, then restart Explorer via Task Manager.
4. If CPU normalizes, re-enable extensions in small groups (3–4 at a time), restarting Explorer each round, until the culprit returns.
5. Uninstall or update the offending program — pay special attention to old archivers, cloud tools, and "tweaker" utilities whose extensions predate 24H2.

### Fix 3: Clear the thumbnail cache

Corrupt thumbnails make Explorer regenerate endlessly.

1. Open **Disk Cleanup** (`cleanmgr`), select C:, check **Thumbnails**, and click OK.
2. For a deeper clear, open an elevated Command Prompt and run: `taskkill /f /im explorer.exe`, then `del /f /s /q /a %LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db`, then restart Explorer via Task Manager (**File** > **Run new task** > `explorer.exe`).
3. Reopen your photo/video folders and let thumbnails regenerate once — this should be a one-time cost.
4. If thumbnail CPU returns, the source folder may contain a corrupt media file that crashes the thumbnail generator — isolate by testing folders one at a time.
5. Consider setting photo folders to **Details** view instead of large thumbnails if regeneration keeps being expensive.

### Fix 4: Calm cloud sync integration

Explorer watches every cloud file change.

1. Check OneDrive/Dropbox sync status — a file stuck **Sync pending** keeps Explorer notified constantly; resolve or remove the stuck file.
2. In OneDrive **Settings**, use **Choose folders** to sync only what you need — fewer synced files means less Explorer overhead.
3. Pause syncing temporarily (**OneDrive icon** > **Pause syncing**) and watch Explorer CPU — a dramatic drop confirms sync as the trigger.
4. For folders with tens of thousands of small files, consider excluding them from sync or moving them out of synced locations.
5. Keep the sync client updated — sync-engine CPU bugs get fixed regularly.

### Fix 5: Fix Quick Access and folder options

Corrupt Explorer state causes constant background work.

1. Open **File Explorer** > **...** > **Options** (or **View** > **Options**).
2. Under **Privacy**, click **Clear** next to "Clear File Explorer history."
3. Change **Open File Explorer to** from **Home** to **This PC** — the Home view with its cloud and recent-file widgets generates more background activity.
4. Uncheck **Show recently used files** and **Show frequently used folders** in Quick Access — test whether CPU drops.
5. If a specific pinned Quick Access folder points to a network or removed location, unpin it — dead paths cause retry loops.

### Fix 6: Disconnect problematic network locations

Unreachable paths make Explorer hang and retry.

1. In **File Explorer**, check **This PC** for mapped network drives with red X icons — right-click > **Disconnect** the dead ones.
2. Remove stale network shortcuts from Quick Access.
3. Test Explorer CPU with Wi-Fi/Ethernet disconnected briefly — if it drops, network path resolution is the cause.
4. In **Folder Options** > **View**, uncheck **Automatically search for network folders and printers** — this stops background network discovery.
5. Re-map only the network drives you actively use, with **Reconnect at sign-in** unchecked for rarely-used ones.

### Fix 7: Repair the shell and scan for malware

The deep fixes for persistent cases.

1. Open an elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — Explorer is a core Windows component these repair.
2. Run a full Defender scan (**Windows Security** > **Virus & threat protection** > **Scan options** > **Full scan**) plus an **Offline scan** — malicious shell extensions are a known persistence method.
3. Install all pending Windows updates — Explorer fixes ship in cumulative updates; check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for known 24H2 Explorer issues.
4. Test in a new local user account — clean Explorer behavior there means your profile's shell configuration is corrupt; migrate to the new profile.
5. Final resort: in-place upgrade via the [Windows 11 installer](https://www.microsoft.com/en-us/software-download/windows11) keeping files and apps — this reinstalls Explorer cleanly.

## Closing

File Explorer high CPU in 24H2 is almost always an add-on or a cache, not Explorer itself — a broken shell extension, a corrupt thumbnail cache, or cloud sync churn. Restart to clear the transient, strip the extensions to find the culprit, and clear the caches. Explorer should be invisible when idle; these steps make it so.
