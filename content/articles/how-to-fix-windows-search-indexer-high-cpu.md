---
title: "How to Fix Windows Search Indexer High CPU Usage"
slug: how-to-fix-windows-search-indexer-high-cpu
date: 2026-10-08
categories: ["performance"]
tags: ["search indexer", "high cpu", "windows search", "windows 11", "performance"]
description: "SearchIndexer.exe hogging your CPU? Find out why Windows Search is indexing so aggressively and apply the fixes that calm it down without killing search."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu.webp"
faqs:
  - q: "Why does SearchIndexer.exe use so much CPU?"
    a: "The indexer builds and maintains a database of your files so Start-menu and File Explorer searches return instantly. It works hard when that database is being built for the first time, after a Windows update resets it, or when it's choking on a folder it shouldn't be indexing — like a game library with tens of thousands of tiny files. Sustained high CPU means it's stuck or misconfigured, not just busy."
  - q: "Can I just disable Windows Search to stop the CPU usage?"
    a: "You can, but it's a blunt instrument: disabling the Windows Search service kills Start-menu search, File Explorer search, and Outlook search integration. The smarter move is trimming what gets indexed (Fix 3) or rebuilding the index (Fix 4) — you keep instant search and lose the CPU spike. Disable the service only as a last resort on very old hardware."
  - q: "How long does a full index rebuild take?"
    a: "On a typical laptop with a few hundred thousand files, a rebuild takes anywhere from thirty minutes to several hours, running hardest in the first phase. Let it run while the laptop is plugged in and idle — overnight is ideal. Interrupting the rebuild repeatedly is what creates the endless half-indexed state that burns CPU forever."
  - q: "Does the indexer slow down gaming or video editing?"
    a: "Yes, when it's actively indexing — it competes for disk I/O and CPU with whatever you're doing. Windows is supposed to throttle indexing during user activity, but it doesn't always succeed. The fixes in this guide reduce the indexer's workload permanently, and pausing indexing during heavy sessions (Fix 6) handles the immediate conflict."
---

You open Task Manager and there it is: SearchIndexer.exe or Microsoft Windows Search Indexer sitting at 25–40% CPU, hour after hour. Your laptop runs warm, the battery drains faster, and all you wanted was to search for a file. Windows Search is genuinely useful — but when its indexer goes rogue, it becomes one of the most annoying background CPU hogs in Windows 11.

The indexer's job is straightforward: crawl your files, build a searchable database, update it when files change. Problems start when it's asked to index too much, when its database corrupts, or when a Windows update sends it back to square one. The fixes below go from diagnosis to the permanent configuration that keeps search fast without the CPU tax.

## Why this happens

- **First-time or post-update indexing:** Building the index from scratch is legitimately CPU-intensive for hours.
- **Overly broad indexed locations:** Indexing entire drives, game folders, or developer directories with hundreds of thousands of files.
- **Corrupted index database:** A damaged index makes the crawler redo work endlessly instead of tracking changes.
- **A file it can't parse:** Certain files hang the filter handlers, causing retry loops.
- **Outlook integration:** Large mailboxes add enormous indexing load, especially with cached Exchange data.
- **Indexing while on battery:** Default settings sometimes let heavy indexing run unplugged, draining battery.
- **Antivirus scanning indexed files:** The indexer touches files, the scanner intercepts, and both burn CPU together.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's indexing, not something else

Open **Settings → Privacy & security → Searching Windows** and check the indexing status — it tells you whether indexing is complete, in progress, or how many items are pending. Then check Task Manager: is SearchIndexer.exe high right now, and does it correlate with the "indexing in progress" status? If indexing shows complete but CPU is still high, you have a stuck indexer (skip to Fix 4). If it's genuinely mid-index after an update, the honest fix may be patience — let it finish overnight while plugged in. This status check prevents you from "fixing" normal behavior.

1. Open Settings → Privacy & security → Searching Windows.
2. Note whether indexing is complete or in progress, and the item count.
3. Compare with SearchIndexer.exe CPU in Task Manager.
4. If complete but CPU high → stuck indexer; if in progress → consider letting it finish.

### Fix 2: Pause indexing temporarily to confirm the culprit

In the same Searching Windows settings page, there's an option to pause indexing — use it for a few hours and watch your CPU and fan. If the laptop goes quiet, you've confirmed the indexer is your performance problem (not a coincidence). This is diagnostic, not a solution: pausing forever just trades CPU for broken search. But it gives you a clean before/after measurement, and it gives you immediate relief while you apply the permanent fixes below. Note the difference in Task Manager's CPU graph so you can verify each later fix actually helped.

1. Pause indexing in Searching Windows settings.
2. Watch CPU and fan noise for 15–30 minutes.
3. Confirm the improvement is real, not placebo.
4. Resume indexing and continue with permanent fixes.

### Fix 3: Trim indexed locations to what you actually search

This is the highest-value fix. In **Searching Windows → Advanced indexing options → Modify**, uncheck everything you never search: game install folders, the Downloads archive, developer folders with node_modules, video collections. Keep Documents, Desktop, and your working folders. Fewer indexed locations means a smaller database, faster updates, and dramatically less CPU. Most users can cut their indexed file count by half or more without noticing any search degradation — because they never searched those locations anyway. The [HP slow-laptop guide](/articles/how-to-fix-windows-11-lagging-on-hp-laptop/) covers this alongside other brand-agnostic speedups.

1. Open Advanced indexing options → Modify.
2. Uncheck game folders, archives, and other never-searched locations.
3. Keep Documents, Desktop, and active project folders.
4. Click OK and let the indexer adjust to the smaller scope.

### Fix 4: Rebuild the index when it's corrupted

If CPU stays high with a "complete" status, or the item count looks wrong, the database is likely corrupt. In **Advanced indexing options → Advanced → Troubleshooting**, click Rebuild. This deletes the index and starts over — search will be degraded for a few hours while it rebuilds, so start it before bed with the laptop plugged in. A rebuild fixes the "indexer spins forever on a complete database" pattern that trimming can't touch, because the corruption was in the database itself. Don't rebuild twice in a row; one clean pass is the test.

1. Open Advanced indexing options → Advanced.
2. Click Rebuild under Troubleshooting.
3. Leave the laptop plugged in and idle for several hours.
4. Check CPU after the status shows complete.

### Fix 5: Exclude problem file types and Outlook if needed

Certain file types cause the indexer's filter handlers to hang. In **Advanced → File Types**, uncheck exotic formats you never need to search inside (old database formats, proprietary archives). If you have a massive Outlook mailbox, consider the tradeoff: in Outlook's own search options you can reduce what's indexed, or in Indexing Options remove Microsoft Outlook entirely if you search mail inside Outlook anyway (its own search still works, just slower). Also exclude any single folder you suspect contains the hanging file — binary search by halves: exclude half your locations, test, narrow down. Microsoft documents index troubleshooting in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Review indexed file types and uncheck exotic formats.
2. Decide whether Outlook's mailbox belongs in the index.
3. If a specific folder seems to hang the indexer, exclude it.
4. Use binary search (halve locations) to isolate a problem folder.

### Fix 6: Tune when indexing is allowed to run hard

Make the indexer a better citizen. In **Searching Windows** settings, ensure indexing respects power mode — it should throttle on battery. In Task Scheduler, find **Microsoft → Windows → Windows Search** tasks and adjust conditions so heavy indexing favors idle time. And for gaming or editing sessions, remember the pause toggle from Fix 2 as a session tool. The permanent configuration (trimmed locations + healthy database + sane schedule) should make manual pausing unnecessary, but it's a fine stopgap. For the full startup-and-background cleanup, see the [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/).

1. Confirm indexing throttles on battery power.
2. Adjust Windows Search scheduled tasks to favor idle time.
3. Use the pause toggle during gaming or editing sessions.
4. Re-check sustained CPU after a full day of the new configuration.

## Closing

A healthy search indexer is invisible — it idles near zero and only works when files actually change. If yours is a permanent CPU resident, it's either indexing too much, working from a corrupt database, or choking on a specific file. Trim the locations, rebuild once, and tune the schedule. Search stays instant, and your CPU stays yours.
