---
title: "How to Disable Windows Search Indexing in Windows 11 24H2"
slug: how-to-disable-windows-search-indexing-in-windows-11-24h2
date: 2026-09-16
categories: ["performance"]
tags: ["windows search", "indexing", "disable indexing", "windows 11 24h2", "searchindexer"]
description: "Windows Search indexing hammering your disk and CPU on 24H2? Learn how to disable, limit, or tame the indexer without losing search."
thumbnail: "/images/thumbs/how-to-disable-windows-search-indexing-in-windows-11-24h2.webp"
faqs:
  - q: "What does Windows Search indexing actually do?"
    a: "The indexer (SearchIndexer.exe) crawls your files, emails, and Start menu items to build a searchable database, so Start menu and File Explorer searches return instant results instead of scanning the disk live. The initial index build and re-indexing after updates are disk- and CPU-intensive — that's when users notice it. Once the index is built, maintenance is light, but on 24H2 the indexer has been known to re-index aggressively after updates, causing prolonged high resource usage."
  - q: "Will disabling indexing break Windows search?"
    a: "No — search still works, it just gets slower for file contents. Start menu app search (the most common use) barely depends on the file indexer, and File Explorer falls back to a live 'slow' search of the current folder. What you lose is instant full-text search across your entire drive and indexed Outlook email search. If you mostly search for apps and settings, you'll never notice indexing is off."
  - q: "Should I disable indexing on an SSD?"
    a: "On SSDs the indexer is rarely a problem — indexing is fast and the disk handles it easily. If SearchIndexer is hammering an SSD on 24H2, something is wrong (corrupt index, a runaway folder like a constantly-changing developer directory, or a stuck re-index loop) and the fix is rebuilding or limiting the index, not necessarily disabling it. Disabling makes most sense on HDDs, where indexing visibly degrades the whole machine."
  - q: "How do I re-enable Windows Search indexing later?"
    a: "Reverse whatever you did: set the Windows Search service back to Automatic (Delayed Start) in services.msc and start it, or re-check 'Allow files on this drive to have contents indexed' on the drive. Then open Indexing Options > Advanced > Rebuild to regenerate the index from scratch. The rebuild takes a few hours on large drives — let it run overnight while plugged in, and search will be fully functional again by morning."
---

The Windows Search indexer is one of those services that's wonderful when it behaves and miserable when it doesn't. After the Windows 11 24H2 update, a lot of users found **SearchIndexer.exe** or **Microsoft Windows Search Indexer** chewing through CPU and disk for hours — sometimes days — re-indexing everything from scratch. On a hard drive, that turns the whole laptop into molasses; even on SSDs, the constant activity is annoying.

You have three levels of response: tame it (limit what it indexes), pause it (stop the service temporarily), or disable it entirely. Most people should start with taming — full disable is for HDD machines where the indexer is a proven, persistent problem. This guide covers all three, plus how to rebuild a corrupted index, which is the actual fix more often than people expect. For related search-process CPU issues, see [SearchApp.exe high CPU](/articles/how-to-fix-searchapp-exe-high-cpu-after-windows-11-update/) and [search indexer high CPU on ASUS](/articles/how-to-fix-windows-search-indexer-high-cpu-on-asus-laptop/).

## Why this happens

- **Post-24H2 full re-index**: Major updates invalidate the index, triggering a complete rebuild.
- **Corrupted index database**: A damaged index makes the indexer loop — re-crawling without ever finishing.
- **High-churn folders indexed**: Developer directories, game libraries, and download folders change constantly, keeping the indexer permanently busy.
- **HDD bottleneck**: Indexing's random read pattern is worst-case for spinning drives.
- **Outlook/OneDrive integration**: Large mailboxes and cloud-synced folders multiply indexed content.
- **Enhanced search mode**: "Enhanced" indexes the entire PC instead of just libraries — far more work.
- **Stuck index merge**: The indexer's background merge process occasionally wedges, pinning CPU indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the indexer is actually the problem

Verify before disabling.

1. Open **Task Manager** > **Processes**, sort by CPU or Disk — look for **Microsoft Windows Search Indexer** or **SearchIndexer.exe**.
2. Open **Settings** > **Privacy & security** > **Searching Windows** — check **Indexer status**: "Indexing complete" means it's idle and not your problem; "Indexing in progress" with a count stuck for days means it's wedged.
3. Click **Advanced indexing options** (or search "Indexing Options" in Start) — the dialog shows items indexed and whether indexing is running.
4. If indexing completed and resources are normal, the indexer isn't your issue — look at SysMain or antivirus instead.
5. Time-box it: if 24H2 installed within 72 hours, some indexing is expected — proceed to taming rather than disabling.

### Fix 2: Switch from Enhanced to Classic search

The biggest single reduction in indexer workload.

1. Go to **Settings** > **Privacy & security** > **Searching Windows**.
2. Under **Find my files**, select **Classic** instead of **Enhanced** — Classic indexes only Documents, Pictures, Music, Desktop, and Start menu; Enhanced crawls the entire drive.
3. This alone can cut indexing work by 80%+ for users with large drives full of games, VMs, and archives.
4. Note: File Explorer searches outside those locations become slow (live search) — an acceptable trade for most.
5. After switching, give the indexer an hour to trim the index down, then check Task Manager.

### Fix 3: Exclude high-churn and heavy folders

Surgical pruning beats blanket disabling.

1. Open **Indexing Options** (search it in Start) > **Modify**.
2. Expand the tree and uncheck: developer folders (especially `node_modules`, build outputs), game libraries (Steam, Epic), VM folders, video editing scratch disks, and Downloads.
3. Keep checked: Start Menu, Users' document folders you actually search, and Outlook if you use desktop email search.
4. Click OK — the indexer will drop the excluded locations from the index over the next hour or so.
5. This is the fix for "indexing never finishes" on machines with constantly-changing directories — the indexer was chasing a moving target. Microsoft documents these options at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Rebuild a corrupted index

When the indexer loops forever, the database is usually damaged.

1. Open **Indexing Options** > **Advanced** (requires admin approval).
2. Under **Troubleshooting**, click **Rebuild** — this deletes the index and starts over. It takes several hours on large drives.
3. Let it run overnight, plugged in, with the laptop awake (set **Sleep** to **Never** temporarily, or just leave it on).
4. Check progress in **Settings** > **Privacy & security** > **Searching Windows** — the indexed count should climb steadily, not stall.
5. A clean rebuild fixes the majority of "indexer stuck at X items for a week" cases.

### Fix 5: Disable file-content indexing on the drive

A middle ground — filenames still indexed, contents not.

1. Open File Explorer, right-click **C:** > **Properties** > **General** tab.
2. Uncheck **Allow files on this drive to have contents indexed in addition to file properties**.
3. Choose **Apply changes to drive C:\, subfolders and files** — this takes a while as Windows touches every file's attribute.
4. Filename search keeps working; only full-text content search slows down.
5. Repeat for other data drives if desired.

### Fix 6: Disable the Windows Search service entirely

The full off switch — for HDD machines and persistent cases.

1. Open **Services** (`services.msc`), find **Windows Search**.
2. Double-click > **Stop** the service, then set **Startup type** to **Disabled**.
3. Alternatively, elevated Terminal: `sc stop WSearch` then `sc config WSearch start=disabled`.
4. Effects: Start menu app/settings search still works fine; File Explorer file search becomes slow live-search; Outlook desktop search degrades.
5. To re-enable later: set back to **Automatic (Delayed Start)**, start the service, and rebuild the index (Fix 4).

### Fix 7: Reduce indexer resource priority (advanced)

Keep search but make it polite.

1. In **Indexing Options** > **Advanced**, uncheck **Respect power settings** only if you want indexing to finish faster while plugged in — or leave it checked to keep indexing from running on battery.
2. The indexer already backs off when you're actively using the PC (it uses idle priority I/O), but you can reinforce this: **Settings** > **Privacy & security** > **Searching Windows** > turn off **Search online and include web results** to reduce search-time network stalls.
3. For Outlook users: **Indexing Options** > **Modify** — uncheck Microsoft Outlook if you don't search old emails; it's one of the heaviest indexed sources.
4. Consider scheduling: there's no built-in indexer schedule, but disabling the service (Fix 6) and enabling it overnight via a scheduled task is a workable manual schedule for the determined.
5. After any change, monitor for 24 hours before judging — the indexer needs a full idle cycle to settle.

## Closing

Windows Search indexing on 24H2 is a resource hog with an off switch — but the smart move is taming before disabling. Switch to Classic search, exclude your high-churn folders, rebuild once if it's stuck, and for most machines the indexer fades into the background where it belongs. Full disable remains the right call for spinning hard drives, where every indexed file is a tiny tax on an already-slow disk.
