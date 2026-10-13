---
title: "Windows Search Indexer High CPU? Fix It for Good"
slug: how-to-fix-windows-search-indexer-high-cpu-youtube
date: 2026-09-19
categories: ["performance"]
tags: ["search indexer", "searchindexer.exe", "high cpu", "windows search", "indexing"]
description: "SearchIndexer.exe constantly using high CPU? Fix the Windows Search indexer permanently — rebuild, trim, or tame it."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu-youtube.webp"
faqs:
  - q: "What does the Windows Search Indexer do?"
    a: "SearchIndexer.exe builds and maintains a database of your files' names, contents, and metadata so that Start menu search, taskbar search, and File Explorer search return instant results. Without it, every search would slowly scan the disk live. It's supposed to work quietly in the background, indexing new and changed files as they appear. High CPU means it's doing far more work than that quiet maintenance — usually rebuilding, stuck on corrupt data, or indexing far more than it should."
  - q: "Can I just disable Windows Search indexing?"
    a: "You can, but you'll feel it: Start menu and File Explorer searches become slow disk scans instead of instant index lookups. A better approach for most people is taming it — switching to Classic indexing scope, excluding folders you never search, and rebuilding a corrupt index — which keeps fast search while eliminating the CPU problem. Full disabling is the last resort, and it's easily reversible if you change your mind."
  - q: "Why is the indexer rebuilding constantly?"
    a: "The usual reasons: the index database is corrupt (so it never completes and restarts), an indexed location contains constantly-changing files (developer directories, download folders, sync folders mid-sync), or a Windows update reset the index state. Less commonly, disk errors corrupt the index files repeatedly — in which case the drive itself needs attention, not the indexer."
  - q: "How long should initial indexing take?"
    a: "On an SSD with a typical file collection: 30 minutes to a few hours. On a hard drive with hundreds of thousands of files: several hours to a full day. During initial indexing, high CPU is normal and expected — the fix is letting it finish uninterrupted, not interrupting it. Only treat it as a problem if indexing never completes after 24+ hours, or if high CPU returns constantly after a completed build."
---

`SearchIndexer.exe` grinding away at 30–60% CPU, day after day, is Windows Search stuck in a loop it can't escape. The indexer is supposed to be a quiet background librarian, cataloging your files once and then just noting changes. When it's constantly at high CPU, the library is on fire: the catalog is corrupt, the scope is absurdly large, or something keeps invalidating its work faster than it can finish.

The critical first question: is it doing its *initial* build, or is it stuck? An initial build after a Windows reinstall, major update, or adding a huge file collection legitimately takes hours — interrupting it just restarts the clock. A stuck indexer never finishes and needs the fixes below. This guide covers both, in the right order.

For the search UI process specifically, see [SearchApp.exe high CPU on Lenovo](/articles/how-to-fix-searchapp-exe-high-cpu-on-lenovo-laptop/). The post-update variant is covered in [search indexer high CPU after Windows update](/articles/how-to-fix-windows-search-indexer-high-cpu-after-windows-11-update/).

## Why this happens

- **Initial index build in progress**: Legitimate heavy work after reinstalls, updates, or large file additions.
- **Corrupt index database**: Damaged catalog that never completes, restarting endlessly.
- **Overly broad indexing scope**: Enhanced mode indexing entire drives including locations you never search.
- **High-churn indexed folders**: Developer dirs, sync folders, and download folders invalidating the index constantly.
- **Disk errors corrupting index files**: Failing storage damaging the database repeatedly.
- **Stuck on a specific file**: A corrupt or locked file the indexer can't process, retrying forever.
- **Outlook PST/OST indexing**: Large mail databases being indexed (and re-indexed) continuously.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check indexing status — building or stuck?

The distinction that determines everything.

1. Open **Control Panel** > **Indexing Options** (search "indexing" in Start) — the top of the window shows status: "Indexing complete," "Indexing in progress," or a file count.
2. If it shows progress with the count climbing: it's building. Note the count, wait an hour, check again — climbing counts mean working; frozen counts mean stuck.
3. If it says "Indexing complete" but SearchIndexer.exe is still at high CPU, something is re-triggering work constantly — skip to Fix 4 (scope trimming).
4. Check how many items are indexed — hundreds of thousands on Enhanced mode is normal-ish; millions suggests absurd scope.
5. Rule: building + progressing = leave it alone (plugged in, idle time helps). Anything else = continue with the fixes.

### Fix 2: Give the initial build a clean window

If it's genuinely building, help it finish.

1. Plug in the laptop — indexing is throttled on battery, stretching a 2-hour build into an 8-hour one.
2. Leave the system as idle as possible for a few hours — every new file you create during the build adds to its workload.
3. Don't reboot repeatedly — each restart interrupts the build and it resumes (not restarts, but still loses momentum).
4. Temporarily pause cloud sync (OneDrive/Dropbox) during the build — sync churn fights the indexer for the same files.
5. Once Indexing Options shows "Indexing complete," CPU should drop to near-zero — if it doesn't within a day, the index is corrupt (Fix 3).

### Fix 3: Rebuild the corrupt index

The definitive fix for the never-completing indexer.

1. In **Indexing Options**, click **Advanced** > **Rebuild** > OK — this deletes the entire catalog and starts fresh.
2. Let the rebuild run to completion without interruption (see Fix 2's conditions) — a rebuild interrupted halfway just creates a fresh corrupt state.
3. After "Indexing complete," monitor SearchIndexer.exe for 48 hours — a healthy fresh index idles at 0% CPU with only brief blips when files change.
4. If the fresh index *also* never completes, the problem isn't the database — it's the scope or the disk (Fix 4 and Fix 6).
5. Don't rebuild repeatedly as a habit — one clean rebuild is diagnostic; if it doesn't hold, the cause is elsewhere.

### Fix 4: Shrink the indexing scope permanently

The highest-leverage long-term fix.

1. In **Indexing Options** > **Modify**, uncheck everything you never search: secondary drives, game libraries, VM folders, media archives, and developer directories (especially ones with `node_modules` or build outputs — tens of thousands of tiny files each).
2. Go to **Settings** > **Privacy & security** > **Searching Windows** — switch from **Enhanced** (whole PC) to **Classic** (libraries + desktop only). For most users, Classic finds everything they actually search for.
3. Under **Exclude folders from enhanced search**, add high-churn paths even if you stay on Enhanced.
4. If you use Outlook with a huge mailbox, consider excluding the Outlook data files — mail search still works via Outlook's own search, and the indexer stops churning on gigabytes of mail.
5. After trimming, rebuild once (Fix 3) so the lean scope takes effect — then enjoy an indexer with a fraction of its former workload.

### Fix 5: Run the Search troubleshooter

The automated check for configuration problems.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Search and Indexing** > **Run**.
2. Check the boxes matching your symptoms ("Search is slow," "Results are incomplete") and let it diagnose — it checks service state, permissions, and index integrity.
3. Apply its recommended fixes and restart the **Windows Search** service if prompted (**services.msc** > **Windows Search** > **Restart**).
4. If the troubleshooter reports it fixed permissions issues, monitor for a day — permission problems on indexed folders cause exactly the retry-loop CPU pattern.
5. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) for indexer guidance specific to your build if the troubleshooter can't resolve it.

### Fix 6: Check the disk and the stuck file

When the index keeps corrupting.

1. Run `chkdsk C: /scan` in an elevated terminal — file system errors corrupt the index database; fix them with `chkdsk C: /f` (requires restart).
2. Check drive health with `wmic diskdrive get status` and CrystalDiskInfo — a failing drive corrupts the index faster than you can rebuild it. Replace failing drives; no indexer fix survives bad hardware.
3. To find a stuck file: open **Event Viewer** > **Applications and Services Logs** > **Microsoft** > **Windows** > **Search** > **Operational** — look for repeated errors naming a specific file path. Exclude or delete that file.
4. Temporarily exclude recently added large folders — if the indexer calms down, something in that folder was the trigger; add files back in batches to isolate it.
5. Ensure 15%+ free space on the indexed drive — critically full drives cause index write failures that look like corruption.

### Fix 7: Disable indexing (last resort, reversible)

When you've decided fast search isn't worth the CPU.

1. Press **Win + R** > `services.msc` > find **Windows Search** > double-click > **Stop**, then set **Startup type** to **Disabled** > OK.
2. Understand the trade-off: Start menu and File Explorer searches become slow live disk scans. If you search rarely, you won't care; if you search constantly, you'll hate it.
3. Alternative middle ground: keep the service but set indexing to **Classic** with a minimal location set (Fix 4) — near-zero CPU with functional basic search.
4. To re-enable: set **Startup type** back to **Automatic (Delayed Start)** and start the service — then rebuild the index once.
5. Note: some Windows features (like certain Start menu experiences) expect the indexer; on Windows 11 disabling it is safe but search-dependent features degrade gracefully rather than breaking.

## Closing

The Search indexer is a librarian — when it's calm, your searches are instant; when it's panicking, your CPU pays. Determine whether it's building or stuck, rebuild corruption cleanly, trim its territory to what you actually search, and check the disk underneath it. A healthy indexer is one you never notice, which is exactly the goal.
