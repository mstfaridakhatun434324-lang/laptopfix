---
title: "SearchHost.exe High CPU? Troubleshoot Windows Search Properly"
slug: searchhost-exe-high-cpu-troubleshooting
date: 2026-09-06
categories: ["performance"]
tags: ["searchhost.exe", "high cpu", "windows search", "search indexer", "troubleshooting"]
description: "SearchHost.exe burning CPU every time you search? Troubleshoot Windows Search: rebuild the index, fix SearchHost crashes, and tame background search activity."
thumbnail: "/images/thumbs/searchhost-exe-high-cpu-troubleshooting.webp"
faqs:
  - q: "What is SearchHost.exe?"
    a: "SearchHost.exe is the process behind the Windows 11 search user interface — the flyout you see when you press the Windows key and type. It's separate from SearchIndexer.exe, which builds the index in the background. SearchHost renders results, shows search highlights, and fetches web suggestions. High CPU from SearchHost usually means the UI layer is struggling: corrupted index data, a broken search package, or web-content features misbehaving."
  - q: "Why does SearchHost.exe spike when I just open the Start menu?"
    a: "Pressing the Windows key launches the search UI, and SearchHost immediately queries the index, renders recent apps, and loads search highlights (the rotating images and stories). If the index is corrupted, the package is damaged, or the highlights feed hangs, that brief launch turns into sustained CPU. Disabling search highlights is the quickest test — if spikes stop, the feed was the problem."
  - q: "Is it safe to disable SearchHost.exe?"
    a: "You can't cleanly disable just SearchHost — it's part of the integrated Search experience. But you can reduce its workload dramatically: turn off search highlights, disable cloud/web search content, and rebuild a corrupt index. These keep local file and app search working while removing the features that cause most SearchHost CPU spikes. The search box keeps functioning; it just gets quieter."
  - q: "What's the difference between SearchHost.exe and SearchIndexer.exe high CPU?"
    a: "SearchIndexer.exe builds and maintains the search database in the background — its CPU means indexing work (often legitimate after adding files). SearchHost.exe is the UI process — its CPU means the interface layer is struggling when you search or open Start. Indexer problems are fixed by rebuilding or scoping the index; SearchHost problems are fixed by disabling highlights, repairing the package, or fixing the UI's data sources."
---

You press the Windows key, type three letters, and Task Manager shows **SearchHost.exe** chewing 15-25% CPU — sometimes for seconds, sometimes until you reboot. Search was supposed to be instant. Instead the search UI itself has become a performance problem, and the usual "rebuild the index" advice only helps when the *indexer* is the problem. When SearchHost — the UI process — is the hog, the causes live in its world: search highlights, web content, a corrupted search package, or a damaged index it can't read cleanly.

This guide troubleshoots the SearchHost layer specifically: disabling the highlights feed, scoping web search, repairing the search app package, and rebuilding the index when corruption is the root cause. For the indexer-background-work side, see [search indexing high CPU fixes](/articles/how-to-fix-search-indexing-high-cpu-windows-11-step-by-step/).

## Why this happens

- **Search highlights feed hanging**: The rotating Start-menu content failing to load and retrying in a loop.
- **Web search integration struggling**: Bing-backed suggestions stalling on slow or filtered networks.
- **Corrupt search index**: Damaged index database making every query expensive for the UI to process.
- **Damaged SearchHost app package**: Corrupted package files causing crash-restart CPU cycles.
- **Excessive indexed locations**: Network drives or giant folders making queries slow.
- **Third-party Start/search replacements conflicting**: Start menu mods fighting the native search UI.
- **Sync issues with Microsoft account**: Search personalization sync looping on corrupt cloud state.
- **Recent feature update breaking search**: Update-damaged search components needing repair or re-registration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's SearchHost, not the indexer

Target the right layer.

1. Open Task Manager > **Details** during a spike and note the exact process: `SearchHost.exe` (UI) vs. `SearchIndexer.exe` (background indexing) — they need different fixes.
2. Test the trigger: does CPU spike when you **open Start/search UI** (SearchHost) or does it run constantly in the background regardless (indexer)?
3. Right-click SearchHost.exe > **Open file location** to verify legitimacy — it should be under `C:\Windows\SystemApps\MicrosoftWindows.Client.CBS_*`.
4. Check **Event Viewer** > **Windows Logs** > **Application** for **SearchHost.exe** crash entries — repeated crashes with auto-restart look like sustained CPU.
5. If the indexer is the actual hog, pivot to [search indexing CPU fixes](/articles/how-to-fix-search-indexing-high-cpu-windows-11-step-by-step/); the fixes below are for the UI process.

### Fix 2: Disable search highlights (the quick win)

The highlights feed is the top SearchHost CPU cause.

1. Open **Settings** > **Privacy & security** > **Search permissions**.
2. Under **More settings**, turn off **Show search highlights** — this kills the rotating images, stories, and moments in the search box and Start.
3. Test immediately: open Start, type a query, watch Task Manager — for most sufferers the spikes stop here.
4. While you're in Search permissions, consider turning off **cloud content search** (Microsoft account and work/school account toggles) if you only ever search local files — less data for the UI to fetch and render.
5. This is fully reversible; if you miss the pretty search box art, turn highlights back on — but most people never notice it's gone.

### Fix 3: Repair or reset the SearchHost package

For crash-looping or corrupted search UI.

1. The signature: SearchHost.exe appears, CPU spikes, the process vanishes and reappears — check Event Viewer's Application log for the crash pattern.
2. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Search and Indexing** > **Run** — let the built-in troubleshooter attempt repairs first.
3. If the troubleshooter doesn't resolve it, re-register the search package from an elevated PowerShell: `Get-AppxPackage MicrosoftWindows.Client.CBS -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
4. Restart and test search thoroughly — open Start, type queries, scroll results. The re-registration fixes package corruption that survives updates.
5. If problems began right after a feature update, also check [Windows Update](/articles/windows-11-slow-after-update-how-to-fix/) for a follow-up cumulative update — Microsoft frequently ships search fixes in the weeks after a feature release.

### Fix 4: Rebuild the search index

When corruption makes every query expensive.

1. Open **Indexing Options** (search Start for it) and click **Advanced** > **Troubleshooting** > **Rebuild** — this deletes the index database and rebuilds from scratch.
2. The rebuild takes anywhere from 30 minutes to several hours depending on file count — during the rebuild, SearchHost may actually use *more* CPU. Let it finish; judging mid-rebuild is meaningless.
3. While waiting, scope the index sensibly: **Indexing Options** > **Modify** — uncheck locations you never search (old archives, game installs, node_modules folders). A smaller index is a faster index.
4. **Exclude** network drives and removable media from indexing — these are the classic "index never finishes" causes, and a perpetually-churning index keeps SearchHost busy serving partial results.
5. After the rebuild completes (Indexing Options shows "Indexing complete"), test search responsiveness — queries against a clean, scoped index should return instantly with minimal SearchHost CPU.

### Fix 5: Remove conflicting Start menu / search mods

Third-party tools fight the native UI.

1. If you use Start11, Open-Shell, ExplorerPatcher, or similar Start menu/search modifications, **temporarily uninstall** (not just disable) the tool and reboot.
2. Test native search for a day — if SearchHost calms down, the mod was conflicting (often after a Windows update changed the search UI underneath it).
3. Check the mod's site for an updated version compatible with your Windows build before reinstalling — running an outdated shell mod on a new Windows build is asking for exactly this.
4. Also disable any "search enhancer" utilities or clipboard managers that hook into the search UI.
5. Prefer mods with explicit per-build compatibility statements; the Windows search UI changes frequently and silent breakage is the norm, per discussions in the Windows support hub community.

### Fix 6: Reset search-related system components

The deep reset when nothing else worked.

1. Run the full system file check: `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt — search UI depends on system components these repair.
2. Clear the search UI's local state: navigate to `%LOCALAPPDATA%\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\` and rename the **LocalState** folder to **LocalState.old** (with SearchHost not running — end it in Task Manager first). It regenerates on next launch.
3. Sign out of your Microsoft account in **Settings** > **Accounts** > **Your info** (switch to local account temporarily) as a test — if SearchHost calms down, corrupt synced search personalization was the cause; you can sign back in after the local state rebuilds.
4. As a final measure, create a fresh user profile and test search there — instant search in a new profile with a broken old one means profile-level corruption, and migration beats repair.
5. Persistent SearchHost CPU across profiles on a clean system is rare — at that point, check your laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for known issues with your model, since vendor shell customizations occasionally interfere.

## Closing

SearchHost.exe CPU is the search *interface* struggling, and the interface's struggles have interface-level causes: the highlights feed (Fix 2), a damaged package (Fix 3), a corrupt index it can't read (Fix 4), or a mod fighting it (Fix 5). Work the list in order and test actual searches after each change — the goal isn't just lower Task Manager numbers, it's a search box that answers before you finish typing.
