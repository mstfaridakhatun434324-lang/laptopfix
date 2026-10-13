---
title: "How to Disable Search Indexing on Windows 10 (Step by Step)"
slug: "how-to-disable-search-indexing-on-windows-10"
date: "2026-10-08"
categories: ["performance"]
tags: ["disable search indexing", "windows 10", "windows search", "indexing options", "performance"]
description: "Want to disable Windows Search indexing on Windows 10? Step-by-step for the service method, plus when to just limit locations instead."
thumbnail: "/images/thumbs/how-to-disable-search-indexing-on-windows-10.webp"
faqs:
  - q: "What do I lose by disabling search indexing?"
    a: "You lose instant file-content search. With indexing off, Start-menu and taskbar searches for files fall back to slow live crawling — searching a large drive can take minutes instead of seconds. App, settings, and web searches still work normally; only file search degrades. If you navigate by folders and rarely search file contents, you'll barely notice. If you search constantly, limit indexed locations instead of disabling."
  - q: "Is it better to disable indexing or just reduce indexed locations?"
    a: "Reducing locations is better for almost everyone. Keeping Documents, Desktop, and Start Menu indexed while excluding video archives, game libraries, and secondary drives gives you fast search where it matters with a fraction of the background cost. Full disable is for mechanical-HDD laptops where even a small index never finishes, or for users who genuinely never use file search."
  - q: "Will disabling indexing stop SearchIndexer.exe high CPU permanently?"
    a: "Yes — with the Windows Search service disabled, SearchIndexer.exe doesn't run at all, so its CPU usage drops to zero permanently. That's the appeal. But first confirm the indexer was actually your problem (Task Manager sorted by CPU/Disk), because disabling it to fix slowness caused by something else just costs you search for nothing. Our [search indexer high CPU guide](/articles/how-do-i-fix-windows-search-indexer-high-cpu/) helps you decide."
  - q: "Can I re-enable indexing later if I change my mind?"
    a: "Easily. Set the Windows Search service back to Automatic (Delayed Start), start it, and open Indexing Options > Advanced > Rebuild to build a fresh index. Within a few hours of plugged-in idle time, instant search is back. Disabling is fully reversible — nothing is deleted except the index database, which rebuilds itself."
---

Windows Search indexing is one of those features that's wonderful on an SSD and miserable on a struggling hard drive — constantly churning in the background, pinning disk usage, and making an already-slow laptop feel broken. If Task Manager keeps showing SearchIndexer.exe near the top, or your HDD never idles, disabling indexing is a legitimate, supported fix.

But it's also irreversible-by-inconvenience: once it's off, file search gets slow, and many guides skip that tradeoff. This walkthrough gives you the full disable method plus the smarter middle path — because for most people, shrinking what gets indexed beats killing the feature outright.

Note: these steps are written for Windows 10 but work identically on Windows 11 — the dialogs haven't changed. If the indexer is misbehaving rather than merely busy, read our [search indexer high CPU fix](/articles/how-do-i-fix-windows-search-indexer-high-cpu/) first; a rebuild may serve you better than a shutdown.

One reassurance before you start: every method below is fully reversible. Disabling the service deletes only the index database — your files are untouched — and re-enabling plus one rebuild restores instant search within hours. You're not burning any bridges; you're just parking a feature your hardware can't currently afford.

## Why this happens

- **Mechanical HDD can't keep up** — Indexing is random-read heavy — the exact workload HDDs handle worst. On old laptop drives the indexer and your apps fight for the same slow disk, and everything loses.
- **Enormous indexed scope** — Default indexing covers the entire user profile plus Start Menu; users with 500 GB+ of files give the indexer a job it can never finish on weak hardware.
- **Corrupted index looping** — A damaged database makes the indexer rescan forever — all of the CPU cost, none of the search benefit. (Fix: rebuild, not disable.)
- **Post-update rebuild storms** — Feature updates invalidate the index and trigger full rebuilds — days of heavy indexing on HDDs, right when you're trying to use the PC.
- **Outlook data file churn** — Huge or corrupted PST/OST files keep the indexer re-crawling mail — common on work laptops, invisible to the user.
- **Cleaner apps wiping the index** — Overzealous 'privacy' cleaners delete the search database on schedule, forcing perpetual rebuilds — the indexer never gets to rest.
- **Windows Search service stuck in a start loop** — A corrupted service configuration can leave the indexer starting, crashing, and restarting every few minutes — constant CPU with the index never progressing past zero.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Try the middle path first: shrink indexed locations

Keep instant search; cut 90% of the workload. Do this before disabling.

1. Open **Control Panel > Indexing Options** and click **Modify**.
1. Uncheck everything except: **Start Menu**, **Users > <yourname> > Documents**, and **Desktop**. Uncheck secondary drives, game folders, video archives, and cloud roots.
1. Click **OK**, then **Advanced > Rebuild** to build a clean small index.
1. Also trim indexed file types: **Advanced > File Types** — uncheck extensions you never search (.zip, .iso, .exe, .dll) to shrink the database further.
1. Confirm the location count dropped on the main Indexing Options window, then give it one plugged-in idle session.
1. For most users, this ends the indexer problem while keeping search instant where it counts.

### Fix 2: Method 1: Disable the Windows Search service

The clean, reversible, supported disable — recommended over registry hacks.

1. Press **Win + R**, type `services.msc`, and press Enter.
1. Scroll to **Windows Search**, double-click it, and click **Stop**.
1. Set **Startup type** to **Disabled** and click **OK**.
1. SearchIndexer.exe exits immediately. File search in Start now crawls live (slower); app and settings search are unaffected.

### Fix 3: Method 2: Disable via Command Prompt (scriptable)

Same result as Method 1, for remote machines or scripts.

1. Open Command Prompt as administrator.
1. Run: `sc stop "wsearch"` then `sc config "wsearch" start=disabled` (note the space after `start=`).
1. Verify with `sc query "wsearch"` — STATE should read STOPPED.
1. To re-enable later: `sc config "wsearch" start=delayed-auto` then `sc start "wsearch"`.

### Fix 4: Verify the indexer is actually gone

Confirm the fix took — and that it was the right fix.

1. Open Task Manager and confirm **SearchIndexer.exe** no longer appears in Processes.
1. Watch the **Performance > Disk** graph at idle for 10 minutes — it should sit near 0%.
1. If disk is still pinned, the indexer wasn't your problem: re-enable it (Method 2's reversal) and investigate the real hog via our [100% disk active time guide](/articles/best-way-to-fix-disk-active-time-100-percent/).
1. Test Start-menu file search once so you know what 'slow search' feels like — informed tradeoff, no surprises.

### Fix 5: Stop cleaner apps from fighting the index

If you keep indexing on (middle path), protect the database.

1. Open your cleaner app (CCleaner, etc.) and exclude the search index location from cleaning.
1. Never schedule registry/file cleaners to run at boot — they compete with the indexer's own startup work.
1. If a 'privacy' tool offers to wipe the search index, decline — that's what causes perpetual rebuilds.
1. This applies whether you shrunk or kept the default scope.

### Fix 6: Address the underlying disk problem

Disabling indexing treats the symptom. The disease is often the drive.

1. Check SMART health with CrystalDiskInfo — a failing HDD makes every background service look guilty.
1. If the drive is healthy but slow, the honest long-term fix is an SSD — after which you can re-enable indexing with zero penalty.
1. Keep C: above 15% free space; a full disk makes indexing (and everything else) dramatically worse.
1. If the Windows Search service itself is crash-looping (Event Viewer > System shows repeated service errors), run `sfc /scannow` before disabling — a corrupted service binary needs repair, not a shutdown.
1. Microsoft documents search and indexing behavior in the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Disabling search indexing is a valid fix when the hardware can't carry it — but try the shrunken index first. Most people get 90% of the relief with 0% of the regret, keeping instant search for the folders they actually use. And if you ever upgrade to an SSD, turn it back on and enjoy the feature as designed.
