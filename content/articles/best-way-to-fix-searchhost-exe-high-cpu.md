---
title: "SearchHost.exe High CPU? Fix Windows Search Eating Your Processor"
slug: best-way-to-fix-searchhost-exe-high-cpu
date: 2026-09-19
categories: ["performance"]
tags: ["searchhost.exe", "high cpu", "windows search", "search indexer"]
description: "SearchHost.exe spiking your CPU? Fix Windows Search host high CPU usage with indexing tweaks, rebuilds, and safe disable options."
thumbnail: "/images/thumbs/best-way-to-fix-searchhost-exe-high-cpu.webp"
faqs:
  - q: "What is SearchHost.exe?"
    a: "SearchHost.exe is the Windows Search user-interface host process — it powers the search box in the taskbar and Start menu, handling your queries and displaying results. It's separate from SearchIndexer.exe, which builds the search database in the background. When SearchHost uses high CPU, it's usually struggling with a corrupt index, web-search integration, or constantly re-querying as you type."
  - q: "Why does SearchHost.exe use CPU when I'm not searching?"
    a: "SearchHost can stay busy due to background search features: Bing web integration pre-fetching results, search highlights updating content, or a damaged index causing repeated failed queries. On some systems it also gets stuck after updates. If it's active with no search box open, one of these background behaviors is the cause."
  - q: "Can I disable SearchHost.exe?"
    a: "You can't cleanly disable SearchHost.exe alone — it's tied to the Windows shell. But you can calm it down: turn off Bing web search integration, disable search highlights, rebuild the search index, or disable Windows Search indexing entirely. Ending the task in Task Manager is safe and it restarts automatically, but that's temporary relief, not a fix."
  - q: "Is SearchHost.exe related to SearchIndexer.exe?"
    a: "They're partners: SearchIndexer.exe builds and maintains the search database in the background, while SearchHost.exe handles the interactive search UI you see. High CPU from the indexer means it's cataloging files; high CPU from SearchHost means the UI layer is struggling. Fixes differ — indexer issues need index rebuilds or scope reduction, while SearchHost issues usually need its web features turned off."
---

Type in the Windows search box and watch Task Manager: `SearchHost.exe` leaps to 20–40% CPU, and sometimes it never comes back down — sitting there burning processor long after you've closed the search. SearchHost is the UI layer of Windows Search, and when it's misbehaving, the usual culprits are its internet-connected features: Bing integration fetching web results for every keystroke, search highlights pulling daily content, or a corrupt index it keeps tripping over. The fixes are quick and mostly in Settings.

If the indexer itself (SearchIndexer.exe) is your problem instead, see our [search indexer CPU guide](/articles/how-to-fix-windows-search-indexer-high-cpu-on-windows-11/); for overall slowness, [speeding up Windows 11](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Bing web search integration**: Every keystroke in the search box triggers web queries — constant network and CPU activity.
- **Search highlights**: The daily rotating content in the search box refreshes in the background, keeping SearchHost busy.
- **Corrupt search index**: A damaged index makes every query fail and retry, pinning the host process.
- **Massive indexed locations**: Indexing entire drives or network folders gives SearchHost an enormous database to query.
- **Post-update search bugs**: Windows updates periodically break SearchHost, causing stuck high CPU until patched or reset.
- **Animated search UI elements**: The highlights carousel and thumbnail previews add rendering load to the host.
- **Third-party shell extensions**: Bad context-menu or preview handlers can hang the search UI thread.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm SearchHost is the problem, not the indexer

Target the right process.

1. Open **Task Manager** > **Details** tab and sort by CPU — identify whether it's **SearchHost.exe**, **SearchIndexer.exe**, or **SearchUI-adjacent** processes like StartMenuExperienceHost.
2. Open the search box (Win+S), type a few letters, and watch: SearchHost spiking only while the box is open points to its UI/web features.
3. If SearchHost stays high with the box closed, background features (highlights, web integration) are the cause.
4. Note the pattern for 5 minutes — intermittent spikes while typing are less urgent than constant 20%+ at idle.
5. This distinction matters: indexer fixes (rebuilds, scope) won't help a SearchHost web-integration problem.

### Fix 2: Disable Bing web search in the search box

The single most effective SearchHost fix.

1. Press **Win+R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer` (create the Explorer key if missing).
2. Create a new **DWORD (32-bit) Value** named `DisableSearchBoxSuggestions` and set it to `1`.
3. Alternatively, on Pro editions: **Group Policy Editor** (`gpedit.msc`) > **User Configuration** > **Administrative Templates** > **Windows Components** > **File Explorer** > enable **Turn off display of recent search entries**.
4. Restart or sign out and back in — the search box now searches locally only, with no web queries per keystroke.
5. Test by typing in search: results appear faster and SearchHost CPU stays flat. This is the fix most people need.

### Fix 3: Turn off search highlights

Kill the background content carousel.

1. Go to **Settings** > **Privacy & security** > **Search permissions**.
2. Under **More settings**, toggle off **Show search highlights**.
3. This stops the daily content downloads and animations that keep SearchHost active in the background.
4. The search box becomes a plain, fast local search — many users prefer it anyway.
5. Check Task Manager over the next hour — background SearchHost activity should drop to near zero.

### Fix 4: Rebuild the search index

For SearchHost tripping over a corrupt index.

1. Open **Control Panel** > **Indexing Options** (search for it in the Start menu if needed).
2. Click **Advanced** > **Troubleshoot** section > **Rebuild** — confirm the prompt.
3. Rebuilding takes a while (possibly hours on large drives) — let it run overnight while plugged in. The indexer will be busy; that's expected.
4. During the rebuild, SearchHost may still act up — judge the result only after the index status shows **Indexing complete**.
5. If the classic Control Panel path is hidden, use **Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** instead.

### Fix 5: Reduce indexed locations

A smaller index is a faster, calmer search.

1. Open **Indexing Options** > **Modify** and uncheck locations you never search — entire secondary drives, game libraries, VM folders.
2. Keep indexed: Start Menu, Users folder essentials. Uncheck: bulky media archives, developer folders with thousands of files.
3. Click **OK** — the indexer prunes the database, which reduces what SearchHost queries against.
4. Our [disable indexing guide](/articles/how-to-disable-windows-search-indexing-on-windows-11/) covers going further if you barely use file search.
5. After pruning, allow a few hours for the index to settle, then test search responsiveness and CPU.

### Fix 6: Restart and reset the search components

Clear stuck states without registry edits.

1. Open Task Manager > **Details**, right-click **SearchHost.exe** > **End task** — it restarts automatically within seconds, clearing any stuck state.
2. For a deeper reset, open PowerShell as admin and run: `Get-AppxPackage -Name "Microsoft.Windows.Search" | Reset-AppxPackage` (Windows 11).
3. Alternatively, run the built-in troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Search and Indexing**.
4. Check **Settings** > **Windows Update** — Microsoft periodically ships SearchHost fixes in cumulative updates; install everything pending.
5. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the search troubleshooter if you need the guided flow.

### Fix 7: Disable Windows Search indexing entirely

The last resort for search you don't need.

1. Press **Win+R**, type `services.msc`, find **Windows Search**, double-click it.
2. Click **Stop**, set **Startup type** to **Disabled**, and click **OK**.
3. SearchHost.exe will go quiet — the Start menu search still works for apps, just slower for file contents.
4. This is ideal for users who navigate by folders or use third-party search tools like Everything.
5. Re-enable anytime by reversing the steps — nothing is deleted, the index just goes dormant.

## Closing

SearchHost.exe high CPU is Windows' search box trying too hard — phoning Bing with every keystroke and animating content you didn't ask for. Turn off the web integration and highlights, rebuild a corrupt index, and the search box goes back to being instant and invisible. Local search doesn't need the internet to find your files.
