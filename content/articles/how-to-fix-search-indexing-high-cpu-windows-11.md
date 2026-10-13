---
title: "How to Fix Search Indexing's High CPU Usage in Windows 11"
slug: how-to-fix-search-indexing-high-cpu-windows-11
date: 2026-10-13
categories: ["performance"]
tags: ["search indexing", "high cpu", "windows search", "indexer", "performance"]
description: "Windows Search indexing eating your CPU? Learn why the indexer runs wild and how to tame it — without losing Start menu search."
thumbnail: "/images/thumbs/how-to-fix-search-indexing-high-cpu-windows-11.webp"
faqs:
  - q: "What is Windows Search indexing and why does it use CPU?"
    a: "The indexer (SearchIndexer.exe / SearchHost.exe) reads your files and builds a database so Start menu and File Explorer searches return instantly. Building and maintaining that database costs CPU — heavily during the initial index of a new system or after big file changes, then lightly during ongoing maintenance. Sustained high CPU means it's stuck, misconfigured, or churning on files that change constantly."
  - q: "Can I just disable Windows Search indexing completely?"
    a: "You can, but you'll lose fast file search — Start menu searches become slow and File Explorer content search stops working well. A better middle ground: switch from Enhanced to Classic indexing (which only indexes libraries and Start menu), exclude high-churn folders, or rebuild a corrupt index. Full disable is the last resort for systems where you genuinely never search files."
  - q: "How long should the initial search index take?"
    a: "On an SSD with a typical file collection, the initial index completes within a few hours of idle, plugged-in time. If SearchIndexer has been burning CPU for more than two to three days, it's not still indexing — it's stuck in a loop, usually on a corrupted index, a file it can't read, or a folder with constantly changing contents. That's when the fixes below apply."
  - q: "Why does search indexing spike after Windows updates?"
    a: "Feature updates move, replace, and touch thousands of files, which invalidates large parts of the index — so the indexer essentially starts over on much of the system. Defender re-baselining and .NET optimization running simultaneously compound the load. This post-update indexing storm is normal and should settle within 48 to 72 hours; persistent spikes beyond that need investigation."
---

Windows Search is one of those features you only notice when it misbehaves. When it's healthy, the Start menu finds your files instantly and you never think about the indexer. When it's sick, SearchIndexer.exe camps at the top of Task Manager, your fans spin up, and everything feels sluggish — all for a feature you might not even use that day.

The indexer goes rogue for understandable reasons: a corrupted index it keeps retrying, folders full of constantly-changing files, or a scope so broad it's indexing things that should never be indexed. The fixes below tame it while keeping search working. For the step-by-step variant, see [fixing search indexing CPU step by step](/articles/how-to-fix-search-indexing-high-cpu-windows-11-step-by-step/); for the related SearchHost process, our [SearchHost.exe guide](/articles/how-to-fix-searchhost-exe-high-cpu-after-windows-11-update/).

## Why this happens

- **Corrupted index database**: A damaged index causes endless retry loops — the most common cause of perpetual high CPU.
- **Overly broad indexing scope**: Enhanced mode indexes the entire PC, including folders that churn constantly.
- **High-churn folders**: Developer build outputs, downloads, game libraries, and sync folders invalidate the index continuously.
- **Post-update re-indexing**: Feature updates touch thousands of files, forcing massive re-indexing.
- **Unreadable or locked files**: The indexer repeatedly retries files it can't read (corrupt files, permission issues).
- **Outlook/PST indexing**: Large mail archives are notoriously expensive to index.
- **Indexing network or external drives**: Slow or disconnected locations cause timeouts and retries.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the indexer is actually the problem

Don't tune what isn't broken.

1. Open **Task Manager** > **Processes**, sort by **CPU**, and confirm **SearchIndexer.exe** (or **SearchHost.exe** / **SearchFilterHost.exe**) is the sustained consumer — not a similarly-named third-party process.
2. Check duration: if a major update or large file copy happened in the last 48 hours, the indexer may be doing legitimate catch-up work.
3. Open **Settings** > **Privacy & security** > **Searching Windows** — it shows indexing status and whether the index is complete.
4. Note your indexing mode: **Enhanced** (entire PC) vs. **Classic** (libraries + desktop + Start menu) — Enhanced on a file-heavy machine is a common self-inflicted wound.
5. Only proceed if high CPU has persisted beyond 72 hours post-change or the status shows the index never completing — otherwise, let it finish.

### Fix 2: Rebuild the search index

The definitive fix for corruption-driven loops.

1. Go to **Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** (link at the bottom).
2. In the Indexing Options dialog, click **Advanced**, then under **Troubleshooting** click **Rebuild**.
3. Confirm the warning — rebuilding deletes the index and starts fresh, which takes several hours on large collections.
4. Leave the laptop plugged in and idle (overnight is ideal) so the rebuild completes without contention.
5. Check status the next day — a successful rebuild shows as complete, and SearchIndexer CPU should drop to near zero at idle. If it immediately starts looping again, the trigger is in your indexed locations (Fix 3).

### Fix 3: Exclude high-churn and pointless folders

Stop indexing what shouldn't be indexed.

1. In **Indexing Options** > **Modify**, review every checked location — uncheck folders with constantly changing contents: build/output directories, game libraries, video editing scratch disks, VM folders.
2. Uncheck sync folders (OneDrive, Dropbox) if you search them rarely — sync churn is a top indexer trigger.
3. Uncheck archive locations: old backups, disk images, and installer repositories don't need content search.
4. In **Advanced** > **File Types**, uncheck extensions you never search inside (e.g., `.log`, `.tmp`, binary formats) — fewer file types means less parsing work.
5. After trimming, trigger a rebuild (Fix 2) so the slimmer scope takes effect cleanly — then watch CPU over the next day.

### Fix 4: Switch from Enhanced to Classic indexing

The scope fix for most home users.

1. Go to **Settings** > **Privacy & security** > **Searching Windows**.
2. Under **Find my files**, select **Classic** instead of **Enhanced** — Classic indexes your libraries, desktop, and Start menu, which covers what most people actually search.
3. If specific extra folders matter to you, add just those via **Customize search locations** rather than indexing the whole drive.
4. Rebuild the index after switching so the old Enhanced data is discarded.
5. Test Start menu search for your daily needs — if everything you look for still appears instantly, Enhanced was pure overhead for you. Microsoft's [Windows search documentation](https://support.microsoft.com/en-us/windows) details these modes.

### Fix 5: Handle Outlook and mail archive indexing

A special case worth checking.

1. If you use classic Outlook with large PST/OST files, the indexer spends enormous effort on mail — check **Indexing Options** > **Modify** for **Microsoft Outlook** entries.
2. In Outlook, go to **File** > **Options** > **Search** > **Indexing Options** and consider removing mail from the index if you search mail within Outlook anyway (Outlook has its own search).
3. Compact oversized PST files (**File** > **Account Settings** > **Data Files** > **Settings** > **Compact Now**) — bloated archives index slowly and repeatedly.
4. If you use the new Outlook or web mail, mail indexing may not apply — verify before changing anything.
5. After excluding mail, rebuild the index and compare CPU — mail-heavy indexes are a frequent hidden cause of perpetual indexer activity.

### Fix 6: Restart and reset the Windows Search service

For a stuck service rather than a stuck index.

1. Open `services.msc`, find **Windows Search**, right-click > **Restart** — a wedged service sometimes just needs a kick.
2. If restarts don't hold, set the service to **Automatic (Delayed Start)** so it doesn't contend with boot-time load.
3. As a deeper reset, stop the service, delete the index data at `%ProgramData%\Microsoft\Search\Data\Applications\Windows`, and start the service — it rebuilds from scratch.
4. Check **Event Viewer** > **Windows Logs** > **Application** for **Search** errors — repeated errors naming a specific file point to an unreadable file you should move or delete.
5. If the service won't stay running at all, run `sfc /scannow` — Search is a Windows component and corruption here needs system-file repair.

### Fix 7: Disable indexing as the last resort

When you've decided fast file search isn't worth the cost.

1. First try the middle ground: Classic mode + trimmed locations (Fixes 3–4) — most people who think they want indexing off actually just want it scoped properly.
2. To fully disable: `services.msc` > **Windows Search** > **Stop**, then set **Startup type** to **Disabled**.
3. Alternatively, in **Indexing Options** > **Modify**, uncheck every location — this keeps the service but gives it nothing to do.
4. Understand the tradeoff: Start menu file search becomes slow, File Explorer content search degrades, and Outlook search may suffer.
5. Re-enable anytime by reversing the steps — disabling is fully reversible, so it's a safe experiment. For systems where the whole machine is slow (not just the indexer), see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) and our [disable indexing guide](/articles/how-to-disable-windows-search-indexing-in-windows-11-24h2/).

## Closing

Search indexing should be invisible — a background helper you never notice. When SearchIndexer.exe becomes the loudest process on your system, it's telling you the index is corrupt, the scope is bloated, or a churn-heavy folder is defeating it. Rebuild, scope down to Classic, exclude the churn, and the indexer goes back to silence.
