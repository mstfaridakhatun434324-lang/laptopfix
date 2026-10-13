---
title: "Search Indexing High CPU on Your Laptop? Tame the Indexer"
slug: how-to-fix-search-indexing-high-cpu-windows-11-on-laptop
date: 2026-10-01
categories: ["performance"]
tags: ["search indexing", "searchindexer", "high cpu", "windows 11"]
description: "SearchIndexer.exe burning CPU on your Windows 11 laptop? Understand Windows Search indexing and tame it without losing fast search."
thumbnail: "/images/thumbs/how-to-fix-search-indexing-high-cpu-windows-11-on-laptop.webp"
faqs:
  - q: "What is Windows Search indexing and why does it use CPU?"
    a: "The indexer (SearchIndexer.exe) crawls your files' contents and metadata to build a database, so Start-menu and File Explorer searches return instantly instead of scanning the disk live. Crawling is CPU- and disk-intensive by nature. It's supposed to run mostly when the system is idle and then go quiet — persistent high CPU means it's stuck, misconfigured, or endlessly re-crawling."
  - q: "Can I just disable Windows Search indexing entirely?"
    a: "You can, but you'll lose instant search — Start-menu file searches and Explorer searches become slow live scans. A better middle ground: switch to Classic indexing (Start menu and libraries only) and prune indexed locations, which cuts 90% of the workload while keeping the searches you actually use fast. Full disable is the last resort for machines where even Classic mode misbehaves."
  - q: "Why does indexing spike after Windows updates?"
    a: "Feature updates change thousands of files and sometimes reset the index database, forcing a full rebuild crawl. This is legitimate and temporary — typically 24–72 hours of elevated activity while plugged in. If it never settles after a week, the migrated index is likely corrupt, and rebuilding it fresh (Advanced indexing options > Rebuild) usually fixes it permanently."
  - q: "Does indexing drain laptop battery?"
    a: "Yes, when it's actively crawling — sustained CPU and disk activity is one of the bigger background battery drains. Windows is supposed to throttle indexing on battery, but a stuck indexer ignores those limits. If your battery life tanked and SearchIndexer is constantly busy, fixing the indexer often restores hours of battery life. Check Settings > System > Power & battery > Battery usage to confirm it's the drain."
---

`SearchIndexer.exe` camped at 25–40% CPU, the fan humming during what should be idle time, battery draining faster than it should. Windows Search indexing is one of those features that's invisible when healthy and infuriating when stuck — and "stuck" is its favorite state after updates, location changes, or index corruption.

The goal isn't to kill search; it's to make the indexer do its job and then shut up. That means scoping what it indexes, fixing corrupt indexes, and knowing when to throttle it. Instant search is genuinely useful — let's keep it without the CPU tax.

Related: the [Dell indexer guide](/articles/how-to-fix-windows-search-indexer-high-cpu-on-dell-laptop/) and how to [fully manage indexing in 24H2](/articles/how-to-disable-windows-search-indexing-in-windows-11-24h2/).

## Why this happens

- **Post-update index rebuild**: Feature updates reset or invalidate the index, triggering full recrawls.
- **Enhanced indexing scope**: Indexing the entire PC (including program files and system areas) instead of just user locations.
- **Corrupt index database**: A damaged index that the service re-crawls endlessly without completing.
- **Constantly changing locations**: Sync folders (OneDrive/Dropbox) or dev directories churning faster than the indexer can keep up.
- **Stuck on a problem file**: A corrupt or pathological file (giant PST, malformed archive) that the indexer chokes on repeatedly.
- **Misconfigured throttling**: Indexer ignoring idle/battery backoff rules due to policy or corruption.
- **Outlook integration**: Indexing massive mailboxes, especially with cached Exchange OST files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the indexer is the problem (and what it's chewing on)

Evidence before action.

1. Task Manager > **Processes** — confirm **Microsoft Windows Search Indexer** (`SearchIndexer.exe`) is the sustained CPU consumer, not a one-off spike.
2. Open **Indexing Options** (search it in Start) — check the **Indexing Status**. "Indexing in progress" with a count that's barely moving, or perpetual "indexing" for days, indicates a stuck crawl.
3. Note the **included locations** count at the bottom — if it says tens of thousands of items or "Enhanced" mode is on, scope is likely the issue.
4. Check timing: constant since a recent update, or correlated with adding a new synced folder or mailbox? The trigger tells you which fix applies.
5. Click **Advanced** > **File Types** tab and glance — hundreds of registered extensions is normal; the issue is rarely here, but note any odd custom types.

### Fix 2: Switch to Classic mode and prune locations

The 90%-fix: index less.

1. **Settings** > **Privacy & security** > **Searching Windows** — under **Find my files**, select **Classic** (searches Documents, Pictures, Music, Desktop) instead of **Enhanced** (entire PC).
2. Still in that page, click **Advanced indexing options** (or open Indexing Options directly) > **Modify**.
3. Uncheck everything you don't search: Program Files, Windows folder, external drives you rarely search, old archives, and especially high-churn folders (sync roots, dev directories, VM folders).
4. Keep checked: your user profile folders where your actual documents live — that's what instant search is for.
5. Click OK and let the indexer adjust — CPU should drop within the hour as it stops crawling the pruned locations. This single change resolves most cases outright.

### Fix 3: Rebuild a corrupt index

When the crawler is stuck, give it a clean database.

1. Open **Indexing Options** > **Advanced** > **Troubleshooting** section > **Rebuild**.
2. Confirm the warning — rebuilding deletes the index and starts over. Searches will be slow/incomplete during the rebuild.
3. Plug in the charger, connect to power, and leave the laptop on and idle for several hours (overnight is ideal) — the rebuild is I/O-heavy and you want it done fast.
4. Monitor **Indexing Options** status: the item count should climb steadily and eventually show "Indexing complete." If it stalls at the same count repeatedly, a problem file is blocking it (Fix 4).
5. After "Indexing complete," watch Task Manager for a full day — a healthy rebuilt index idles at ~0% CPU. Microsoft documents the indexer at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 4: Find and exclude the file that's choking it

One bad file can stall the whole crawl.

1. If the rebuild stalls at a consistent item count, suspect a pathological file: enormous Outlook PST/OST files, corrupt archives, or files with malformed metadata.
2. In **Indexing Options** > **Advanced** > **File Types**, temporarily uncheck problematic types you don't need indexed (e.g., old `.pst` archives, giant log files) — or better, exclude their folders via **Modify**.
3. For Outlook: **File** > **Options** > **Search** > **Indexing Options** — consider excluding Outlook from indexing if your mailbox is huge and you search mail rarely, or let Outlook's own search handle it.
4. Move or archive the suspect files out of indexed locations, then trigger a rebuild (Fix 3).
5. Re-add locations gradually if needed — but honestly, most users never miss the excluded behemoths.

### Fix 5: Exclude high-churn folders

Stop indexing what changes faster than it can be crawled.

1. List your churn: OneDrive/Dropbox/Google Drive sync roots (if you don't search them via Start), code project folders, download staging areas, game mod folders, video render outputs.
2. **Indexing Options** > **Modify** — uncheck each churn folder. You can still search them with Everything (voidtools) or Explorer's non-indexed search when needed.
3. For developers: exclude `node_modules`, `build`, `dist`, `.git` directories specifically — thousands of tiny files that change constantly are the indexer's worst workload.
4. If you rely on Start-menu search for apps only (not files), you can prune even further — app shortcuts live in a tiny location set.
5. Give it a few hours — the indexer stops re-crawling churn and CPU collapses. For the nuclear option on 24H2, see [disabling search indexing entirely](/articles/how-to-disable-windows-search-indexing-in-windows-11-24h2/).

### Fix 6: Enforce idle and battery throttling

Make the indexer respect boundaries.

1. **Settings** > **Privacy & security** > **Searching Windows** — verify **Respect power settings when indexing** (or "Index only when on AC power" wording) is enabled — the indexer should back off on battery.
2. Open **Task Scheduler** > **Microsoft** > **Windows** > **Shell** — check the indexer-related tasks' **Conditions** tabs for idle requirements.
3. In **Indexing Options** > **Advanced**, there's no direct throttle slider in modern Windows — throttling is automatic, so if the indexer ignores idle/battery, that's a symptom of corruption (rebuild, Fix 3) not a setting.
4. Check **Settings** > **System** > **Power & battery** > **Battery usage** — confirm SearchIndexer was actually the battery drain before and after your fixes.
5. On laptops, also verify **Power mode** isn't **Best performance** 24/7 — that mode tells background services (including the indexer) that power is no object.

### Fix 7: Disable the Windows Search service (last resort)

When scoping and rebuilding both fail.

1. `services.msc` > **Windows Search** > **Stop**, then set **Startup type** to **Disabled**.
2. Understand the cost: Start-menu file search and Explorer search become slow non-indexed scans; app launching by name still works (that's a separate small index).
3. Alternative middle ground: leave the service on **Manual** — it won't run at boot but starts if something explicitly needs it.
4. Install **Everything** (voidtools) as a replacement for file search — it's dramatically faster than even a healthy Windows indexer for filename searches (it doesn't index contents, which is the expensive part).
5. Revisit this decision after each feature update — updates sometimes re-enable the service, and a fresh update occasionally fixes whatever was corrupting the index.

## Closing

A healthy search indexer is a ghost — it crawls quietly when you're idle and vanishes when you're not. When it won't vanish, the fix is almost always scope (Classic mode, pruned locations), a fresh database (rebuild), or evicting the churn folders and problem files that keep it spinning. Keep the instant search you actually use; starve the crawling you never asked for. Your CPU — and your battery — will thank you.
