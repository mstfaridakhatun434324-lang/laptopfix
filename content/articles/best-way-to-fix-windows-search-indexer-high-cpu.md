---
title: "The Best Way to Fix Windows Search Indexer High CPU"
slug: best-way-to-fix-windows-search-indexer-high-cpu
date: 2026-09-05
categories: ["performance"]
tags: ["search indexer", "high cpu", "windows search", "indexing"]
description: "Windows Search indexer burning CPU nonstop? Here's the most effective fix order: scope it down, rebuild it, and keep it quiet for good."
thumbnail: "/images/thumbs/best-way-to-fix-windows-search-indexer-high-cpu.webp"
faqs:
  - q: "What is the Windows Search indexer and why does it use CPU?"
    a: "The indexer (SearchIndexer.exe) crawls your files, emails, and settings to build a catalog that makes Start menu and File Explorer searches instant. Crawling means opening, reading, and parsing files, which costs CPU and disk. It is supposed to work mostly at idle and back off when you are busy — when it does not back off, you get the high-CPU problem this guide fixes."
  - q: "Should I just disable Windows Search entirely?"
    a: "You can, but you lose instant search across files, emails, and settings — the Start menu becomes noticeably slower. A better approach is the one in this guide: narrow the index scope and rebuild the database. You keep fast search with a fraction of the CPU cost, which beats disabling the feature outright for almost everyone."
  - q: "How long should a search index rebuild take?"
    a: "Anywhere from 30 minutes to several hours, depending on how many files are indexed and how fast your disk is. An SSD with a trimmed scope often finishes in under an hour; a full mechanical drive with everything indexed can take most of a day. Let it run plugged in and uninterrupted, and judge the result only after it completes."
  - q: "Why does the indexer start over after every Windows update?"
    a: "Feature updates change file locations, add new system files, and sometimes reset index settings, so Windows re-crawls to keep the catalog accurate. Cumulative updates are lighter but can still trigger partial rebuilds. If the indexer behaves for weeks and only spikes after Patch Tuesday, that is normal — give it a day before treating it as broken."
---

The Windows Search indexer is supposed to be invisible. It crawls your files in the background, builds its catalog, and gets out of the way — and on a well-configured system, that is exactly what happens. But when the index corrupts, the scope balloons, or something keeps churning your files, SearchIndexer.exe turns into a permanent CPU tenant, and search results do not even improve for the trouble.

There is a "best way" to fix this because the causes stack in a predictable order. Randomly toggling settings wastes an afternoon; working the stack top-down fixes it in one pass. That is what this guide does: diagnose the state, shrink the workload, rebuild cleanly, and lock in settings that keep it quiet.

## Why this happens

- **Corrupted index database:** A damaged catalog makes the indexer re-crawl the same files endlessly, burning CPU without ever finishing.
- **Indexing scope far too broad:** Whole drives, program folders, and cloud-synced directories multiply the crawl workload far beyond what search needs.
- **Constant file churn underneath it:** Cloud sync, backups, developer tools, and chat apps modifying files continuously force endless re-indexing.
- **Post-update rebuild loops:** A failed or interrupted rebuild after a Windows update leaves the indexer retrying the same batch forever.
- **File-type handlers misbehaving:** Broken IFilters for PDFs, archives, or email stores make the indexer hang on individual files, spiking CPU per file.
- **Antivirus fighting the crawler:** Real-time scanning of every file the indexer touches doubles the work and can deadlock the crawl on large files.
- **Outlook's massive data files:** Huge PST/OST files get re-indexed in large chunks, and a corrupted mail store keeps the indexer busy for days.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the indexer's actual state

1. Open **Control Panel → Indexing Options** and look at the top line: it should say **Indexing complete**. If it says **Indexing...** with a count that never decreases, the crawl is stuck.
2. Open Task Manager and confirm **SearchIndexer.exe** (or **Microsoft Windows Search Indexer**) is the process holding CPU.
3. Note how many items are indexed — anything over 200,000 on a typical laptop suggests the scope is too broad.
4. If indexing claims to be complete yet CPU stays high, the database is likely corrupt — proceed to Fix 3 after scoping down in Fix 2.

### Fix 2: Shrink the indexing scope to what you actually search

1. In **Indexing Options**, click **Modify**.
2. Uncheck entire drives, **Program Files**, **Windows**, Downloads, and any cloud-synced folders (OneDrive, Dropbox). These are the biggest CPU sinks and the least useful to search.
3. Keep only your real document locations: **Users** folders for documents and pictures, plus **Start Menu** and **Offline Files** defaults.
4. Click **OK**. Fewer locations means a smaller database, faster rebuilds, and permanently lower CPU.
5. For the search host process that surfaces these results, our [SearchHost.exe fix](/articles/how-to-fix-searchhost-exe-high-cpu-step-by-step/) is the companion piece when the host — not the indexer — is the hot process.

### Fix 3: Rebuild the index cleanly

1. In **Indexing Options**, click **Advanced** → **Rebuild** under Troubleshooting, and confirm.
2. Plug in the charger — the rebuild is CPU and disk intensive, and you do not want the laptop sleeping mid-rebuild.
3. Let it run to **Indexing complete**. Do not judge CPU during the rebuild; judge it for a full day after.
4. If the count stalls at the same number for hours, a specific file is hanging the crawler — note the count, then move to Fix 4.

### Fix 4: Remove problematic file types and locations

1. In **Indexing Options → Advanced → File Types**, uncheck extensions tied to broken handlers — especially PDF, ZIP, and email archive types if you installed third-party filters for them.
2. If you use Outlook with a huge mailbox, consider unchecking **Microsoft Outlook** under Modify → Show all locations, and rely on Outlook's own search instead.
3. Exclude folders with constant churn: code repositories, build output folders, game mod directories, and download staging areas.
4. Rebuild once more after these exclusions so the database drops the problematic entries.

### Fix 5: Stop the antivirus feedback loop

1. Add `C:\ProgramData\Microsoft\Search` to your antivirus exclusions — this is the index database location, and scanning it during writes creates a costly loop.
2. If you run a third-party suite, check whether it has its own "search integration" or file-shield feature interacting with the indexer, and test with it briefly disabled.
3. Windows Security's built-in exclusions guidance is documented on the [Microsoft support site](https://support.microsoft.com/en-us/windows) if you need the exact steps.
4. Restart the **Windows Search** service (`services.msc` → right-click → Restart) after changing exclusions and observe for an hour.

### Fix 6: Set the indexer to back off properly

1. In `services.msc`, double-click **Windows Search** and set **Startup type** to **Automatic (Delayed Start)** so indexing waits until boot settles.
2. In **Indexing Options → Advanced**, uncheck **Index encrypted files** if you do not use EFS — encrypted files cost extra CPU per file.
3. On laptops, go to **Settings → Privacy & security → Searching Windows** and set **Find my files** to **Classic** instead of Enhanced — Classic indexes far fewer locations by default.
4. These three settings together are what "well-behaved indexing" looks like on a laptop.

### Fix 7: Nuclear option — reset the search database files

1. Stop the **Windows Search** service in `services.msc`.
2. Navigate to `C:\ProgramData\Microsoft\Search\Data\Applications\Windows` and delete the contents (database files only — your documents are untouched).
3. Start the service again; it rebuilds the catalog from zero with your trimmed scope from Fix 2.
4. If even a clean database with a minimal scope still burns CPU, the cause is external churn — check cloud sync clients and backup tools, and see our [100% disk guide](/articles/how-to-fix-disk-active-time-100-percent-youtube/) for the disk-side version of this same investigation.

## Closing

The indexer is a good servant and a terrible master. Scope it to the files you actually search, rebuild it cleanly once, exclude the database from antivirus scans, and let it back off at boot — and SearchIndexer.exe goes back to the background where it belongs, with search staying instant.
