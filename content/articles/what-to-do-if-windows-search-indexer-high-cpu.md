---
title: "What to Do If Windows Search Indexer Is Using High CPU"
slug: "what-to-do-if-windows-search-indexer-high-cpu"
date: 2026-09-29
categories: ["performance"]
tags: ["search indexer", "high cpu", "windows search", "indexing", "windows 11"]
description: "Windows Search indexer pinning your CPU? Learn when indexing is normal, how to shrink what it watches, and how to rebuild a corrupted index."
thumbnail: "/images/thumbs/what-to-do-if-windows-search-indexer-high-cpu.webp"
faqs:
  - q: "Is it normal for the search indexer to use high CPU?"
    a: "Yes, temporarily. After a Windows install, a feature update, or adding a large folder to the index, the indexer legitimately works hard for several hours building its database — high CPU during that window is expected. It becomes abnormal when high CPU persists for days with no new files, returns after every reboot, or never finishes the “indexing” status. Duration without progress is what separates normal indexing from a stuck indexer."
  - q: "Can I just disable Windows Search indexing?"
    a: "You can, but you will lose fast Start menu and File Explorer search — searches fall back to slow filename crawling. A better middle ground is narrowing the indexed locations to just the folders you actually search, which cuts indexer workload dramatically while keeping search instant where it matters. Full disable is reasonable only on very old hardware where every CPU cycle counts."
  - q: "How long does rebuilding the search index take?"
    a: "On a modern laptop SSD with a typical user profile, a rebuild takes 1 to 4 hours of background work — longer on mechanical drives or with huge file collections. CPU will be elevated during the rebuild itself; that is expected and not a sign of failure. Start the rebuild in the evening, leave the laptop plugged in and awake, and check the Indexing Status in the morning."
  - q: "Does the indexer slow down gaming or work apps?"
    a: "It can, on two fronts: CPU contention during heavy indexing, and disk I/O contention while it reads files to catalog them. Windows is supposed to throttle the indexer when you are active, but the throttling is imperfect — many users notice micro-stutters during the initial indexing phase. Pausing indexing during gaming sessions or work hours (via the indexer's pause option) is a legitimate workaround."
---
SearchIndexer.exe — the engine behind Start menu and File Explorer search — is supposed to be invisible. It catalogs your files quietly in the background so searches return instantly. But when the index corrupts or the scope balloons, it turns into a CPU hog: 30–70 percent usage for hours, a hot laptop, and an indexing status that never says “complete.”

The instinct is to kill it. The smarter move is to understand its two states: building (legitimate, temporary, leave it alone) and stuck (corrupted or misconfigured, needs intervention). Telling them apart takes one glance at the indexing status — and this guide shows you exactly where to look.

Below: how to check whether the indexer is actually progressing, how to shrink what it watches, how to rebuild a corrupted index, and when to throttle or disable it. For update-related indexer spikes specifically, see our [post-update indexer guide](/articles/how-to-fix-windows-search-indexer-high-cpu-after-windows-11-update/).

## Why this happens

- **Initial index build:** a fresh install or feature update triggers hours of legitimate cataloging — patience, not repair.

- **Corrupted index database:** damage makes the indexer re-scan the same files forever without completing.

- **Overly broad scope:** Enhanced indexing mode watches the entire drive, including caches and folders you never search.

- **Outlook mailbox indexing:** large PST/OST files add an enormous, constantly changing corpus to the index.

- **Network locations indexed:** slow or sleeping NAS drives make the indexer wait, retry, and churn.

- **File churn from apps:** caches, build outputs, or sync folders that change constantly force endless re-indexing.

- **Third-party IFilters:** buggy document filters (PDF, CAD) can hang the indexer on specific files.

- **Interrupted indexing:** forced shutdowns mid-index leave the database inconsistent and the indexer confused.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the indexer is actually progressing

This one check prevents every misdiagnosis. An indexer that is moving — even slowly — should be left alone; only a frozen one needs repair.

1. Open Settings > Privacy & security > Searching Windows.
2. Click Advanced indexing options, then note the status line: it shows items indexed and whether indexing is complete.
3. Wait 30 minutes and check again — a rising item count means real progress.
4. If the count climbs steadily, plug in the laptop, prevent sleep, and let it finish overnight.
5. Only continue below if the count is frozen for hours or indexing never completes across days.

### Fix 2: Narrow the indexed locations

Most indexers watch far more than necessary. Cutting the scope to folders you actually search is the highest-leverage change: less to catalog, less to re-scan, less CPU forever. Microsoft documents these options on its [Windows support site](https://support.microsoft.com/en-us/windows).

1. In Advanced indexing options, click Modify.
2. Uncheck everything you never search: game libraries, download caches, temp folders, synced cloud folders.
3. Keep checked only your documents, projects, and media folders.
4. In Settings > Privacy & security > Searching Windows, prefer Classic over Enhanced unless you truly search the whole drive.
5. Click OK and let the indexer adjust — CPU should drop within the hour.

### Fix 3: Rebuild a corrupted index

When the item count is frozen or indexing never completes, the database itself is usually corrupt. Rebuilding wipes it and starts clean — the definitive fix for stuck indexers, at the cost of one long rebuild.

1. In Advanced indexing options, click the Advanced button.
2. On the Index Settings tab, click Rebuild and confirm the warning.
3. Plug in the laptop and leave it awake for several hours (overnight is ideal).
4. Expect high CPU during the rebuild — that is normal and temporary.
5. Check the status in the morning: “Indexing complete” with a calm SearchIndexer means success.

### Fix 4: Exclude Outlook or problem file types

Two classic indexer traps: a giant Outlook mailbox and a single file type with a buggy filter. Excluding them surgically beats nuking the whole index.

1. In Advanced indexing options > Modify, uncheck Microsoft Outlook if you search mail inside Outlook anyway (its own search still works).
2. In Advanced > File Types, uncheck extensions tied to third-party filters you do not need indexed (CAD formats, old archives).
3. If the indexer always stalls on the same folder, exclude that folder in Modify and investigate its files separately.
4. A corrupted PDF or media file hanging the filter is a real phenomenon — move suspects out and re-test.
5. Rebuild the index after exclusions so the change takes full effect.

### Fix 5: Pause indexing during heavy work

You do not have to choose between search and performance. Windows lets you pause indexing — perfect for gaming sessions, video renders, or long compile jobs.

1. In Advanced indexing options, use the Pause button to halt indexing immediately.
2. Choose a pause duration that covers your session; indexing resumes automatically after.
3. For gaming, also set your power plan to Best performance so background tasks stay deprioritized.
4. Alternatively, schedule heavy file operations (photo imports, backups) for times you are away from the laptop.
5. Remember to let indexing run overnight occasionally so the database does not go stale.

### Fix 6: Restart the Windows Search service

A service that has been running for weeks can develop the software equivalent of a cramp — a stuck thread no configuration change clears. A clean restart is the safe reset button.

1. Press Win + R, type services.msc, and press Enter.
2. Find Windows Search, right-click it, and choose Restart.
3. If Restart is unavailable, choose Stop, wait 30 seconds, then Start.
4. Watch Task Manager for 15 minutes to see whether the indexer resumes normal behavior.
5. If high CPU returns immediately with no progress, the index is corrupt — rebuild it per Fix 3.

### Fix 7: Throttle or disable as a last resort

On very old hardware, even a healthy indexer costs too much. Throttling its resource usage — or disabling search indexing entirely — are legitimate last resorts with clear trade-offs.

1. To throttle: the indexer respects system activity automatically, but you can also limit background work via Group Policy (Computer Configuration > Administrative Templates > Windows Components > Search).
2. To disable: in services.msc, set Windows Search startup to Disabled and stop the service.
3. Understand the trade-off: Start menu and Explorer searches become slow filename scans.
4. Our [Lenovo indexer guide](/articles/how-to-fix-search-indexing-high-cpu-windows-11-on-lenovo-laptop/) covers vendor-specific background interactions too.
5. Re-enable any time by setting the service back to Automatic (Delayed Start).

## Closing

The search indexer is a background servant, not a master — when it starts acting like the latter, check its progress, narrow its scope, and rebuild its database if it is corrupt. Those three steps resolve the overwhelming majority of indexer CPU problems without sacrificing the instant search that makes Windows usable. Reserve the disable option for genuinely ancient hardware; on anything modern, a tuned indexer is invisible and invaluable.
