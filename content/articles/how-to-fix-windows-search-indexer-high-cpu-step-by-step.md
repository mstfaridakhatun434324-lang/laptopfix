---
title: "Windows Search Indexer High CPU? A Step-by-Step Fix"
slug: how-to-fix-windows-search-indexer-high-cpu-step-by-step
date: 2026-09-05
categories: ["performance"]
tags: ["searchindexer.exe high cpu", "windows search fix", "indexing slow", "step by step", "cpu 100%"]
description: "SearchIndexer.exe eating your CPU? Follow this ordered, step-by-step repair: diagnose, exclude, rebuild, and verify — no guesswork."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu-step-by-step.webp"
faqs:
  - q: "What is SearchIndexer.exe?"
    a: "It is the Windows Search indexing engine. It scans your files and builds a searchable database so Start menu and File Explorer searches return instantly. It should use CPU heavily only during its initial pass, then drop to near zero."
  - q: "How do I know if my search index is corrupted?"
    a: "The classic symptom is indexing that never finishes: Settings shows 'Indexing in progress' for days, the item count barely moves, and SearchIndexer.exe holds high CPU the entire time. A healthy index completes its pass and goes quiet. If yours has been 'indexing' for more than 24 hours on a normal file collection, the database is almost certainly damaged."
  - q: "Will rebuilding the index delete my files?"
    a: "No — rebuilding only deletes and recreates the search database, which is just a catalog. Your documents, photos, and emails are completely untouched. The only temporary downside is slower search results until the rebuild finishes. Think of it as reprinting a library's card catalog: the books never leave the shelves."
  - q: "Can I stop indexing for specific folders only?"
    a: "Yes, and it is the recommended approach. Open Indexing Options from Control Panel, click Modify, and uncheck any folder you never search — network drives, developer repos, VM folders. The indexer skips excluded folders entirely, shrinking its workload without disabling search. Most users can safely exclude far more than they expect."
---

When SearchIndexer.exe goes rogue, it does not do it quietly — CPU spikes, fans spin, and the laptop feels sluggish for hours or days. The process has one job: build a catalog of your files so searches are instant. When something breaks that job, it retries forever instead of finishing, and you pay the CPU bill.

The good news is that this problem has a reliable, ordered fix. There is no need to randomly toggle settings from forum threads. Each step below builds on the last: first confirm the indexer is truly stuck, then shrink what it has to index, then rebuild its database, then verify it stays quiet.

Set aside an evening — the rebuild step runs best overnight — and work the list from top to bottom.

## Why this happens

- **Corrupted index database:** Damage to the catalog makes the indexer restart its scan endlessly instead of completing it.

- **Oversized indexing scope:** Network drives, external drives, and giant project folders multiply the work beyond what the indexer can finish.

- **Rapidly changing folders:** Sync folders that change every few minutes force constant re-indexing of the same files.

- **Large Outlook data files:** Mail archives are among the most expensive items to index, and they re-index on mail changes.

- **Stuck Windows Search service:** The service hosting the indexer can wedge independently of the database.

- **Disk errors in indexed areas:** Read errors force retries that look like endless indexing. The HP-specific variant of this fix is at [SearchIndexer high CPU on HP laptops](/articles/how-to-fix-windows-search-indexer-high-cpu-on-hp-laptop/).

- **Post-update full rebuild:** Feature updates invalidate the index, triggering a legitimate but long rebuild.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1 — Confirm the indexer is stuck, not working

A fresh rebuild after an update is legitimate heavy work. Confirm it is actually stuck before you intervene.

1. Open Settings, Privacy and security, Searching Windows.
2. Read the indexing status: note whether it says indexing is in progress and the item count.
3. Wait 20 minutes and check the count again.
4. If the count rises steadily, it is working — let it finish.
5. If the count is frozen and CPU stays high, it is stuck — continue to Step 2.

### Fix 2: Step 2 — Shrink the indexing scope

Every excluded folder is work the indexer never has to do again. Do this before rebuilding so the rebuild itself is faster.

1. Open Control Panel and search for Indexing Options.
2. Click Modify to see the included folder tree.
3. Uncheck network locations, external drives, and folders you never search.
4. Uncheck developer repositories, VM folders, and game libraries.
5. Click OK.
6. Wait 30 minutes and check CPU — sometimes this alone breaks the loop.

### Fix 3: Step 3 — Rebuild the index database

If the database is corrupted, exclusions cannot help. Rebuilding creates a clean catalog from scratch.

1. In Indexing Options, click Advanced.
2. Under Troubleshooting, click Rebuild and confirm.
3. Plug the laptop into AC power.
4. Let the rebuild run for several hours — overnight is ideal.
5. Expect high CPU during the rebuild; this is normal temporary work.
6. Check Settings afterward: status should read 'Indexing complete'.

### Fix 4: Step 4 — Trim expensive file types and mail

If the indexer is slow even when healthy, it is indexing things that cost more than they are worth. Trim them.

1. In Indexing Options, Advanced, open the File Types tab.
2. Uncheck extensions you never search for — archives, disk images, installer packages.
3. In Outlook, go to File, Options, Search, and review what mail stores are indexed.
4. Consider excluding the OST file if you can tolerate slower mail search.
5. Restart the Windows Search service from services.msc after changes.

### Fix 5: Step 5 — Restart and repair the Search service

A wedged service can survive a database rebuild. Restarting it with repaired system files clears the wedge. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers additional Search repair tools if the service will not stabilize.

1. Press Win plus R, type `services.msc`, and press Enter.
2. Right-click Windows Search and choose Restart.
3. If problems persist, set its Startup type to Automatic (Delayed Start).
4. Run `sfc /scannow` in an admin Command Prompt.
5. Check for disk errors with `chkdsk C: /f` on the indexed drive.
6. Restart the laptop and observe for an hour.

### Fix 6: Step 6 — Verify and set up monitoring

The fix is only done when the indexer stays quiet. Verify over a full day, including a reboot.

1. After the rebuild, confirm Settings shows 'Indexing complete'.
2. Open Task Manager and confirm SearchIndexer.exe idles near zero.
3. Reboot and check that no new indexing storm starts.
4. Add any new giant folders to the exclusion list proactively.
5. If the loop ever returns, repeat from Step 2 — the scope almost always grew again.
6. For the 24H2-specific variant, see [SearchIndexer high CPU in Windows 11 24H2](/articles/how-to-fix-windows-search-indexer-high-cpu-in-windows-11-24h2/).

### Fix 7: Step 7 — Rule out disk errors under the index

The indexer reads every file it catalogs. If the drive has bad sectors in indexed areas, reads fail and retry endlessly — which looks exactly like a stuck indexer. One disk check rules this possibility out for good.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f` and confirm the scan on next restart.
3. Restart the laptop and let the scan complete without interrupting it.
4. Check the results in Event Viewer, under Windows Logs, Application, for the Wininit entry.
5. If bad sectors are reported, back up immediately — the drive may be failing.
6. Re-check the indexer afterward; with a healthy disk it should complete normally.

## Closing

SearchIndexer.exe is either working or stuck, and the steps above tell you which within half an hour. Shrink its territory, rebuild its database, and verify it finishes — and Windows Search goes back to being the instant, invisible tool it was designed to be.
