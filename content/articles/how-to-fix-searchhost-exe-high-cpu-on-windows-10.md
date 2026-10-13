---
title: "SearchHost.exe High CPU on Windows 10? Restore a Snappy Start Menu"
slug: how-to-fix-searchhost-exe-high-cpu-on-windows-10
date: 2026-09-18
categories: ["performance"]
tags: ["searchhost.exe", "high cpu", "windows 10", "windows search", "start menu"]
description: "SearchHost.exe spiking CPU on Windows 10? Rebuild the search index, disable web search hooks, and make Start menu search instant again."
thumbnail: "/images/thumbs/how-to-fix-searchhost-exe-high-cpu-on-windows-10.webp"
faqs:
  - q: "What is SearchHost.exe on Windows 10?"
    a: "SearchHost.exe (formerly SearchUI.exe, the Cortana search host) is the process behind the Start menu search box and taskbar search on Windows 10. Every keystroke you type into search runs through it as it queries the local index and — unless disabled — Bing. Sustained high CPU from it means the search pipeline is stuck: usually a corrupt index, a broken web-search integration, or the indexer re-crawling files endlessly after an update."
  - q: "Is SearchHost.exe safe to end in Task Manager?"
    a: "Yes, ending it is safe — it's just the search interface, and Windows restarts it automatically the next time you use search. But ending it only provides temporary relief; if the underlying index corruption or stuck web query remains, CPU spikes return within minutes. Use End Task as a quick test to confirm SearchHost is the consumer, then apply the permanent fixes below so it stays quiet."
  - q: "Why does SearchHost.exe spike when I type in the Start menu?"
    a: "Each keystroke triggers a fresh query against both the local search index and Microsoft's online search service. If the local index is corrupt, every query becomes expensive; if the machine is offline or Bing integration is glitching, the web portion can hang and retry, burning CPU. Disabling web search results and rebuilding the index together eliminate both halves of this problem for most users."
  - q: "Will disabling Windows Search break the Start menu?"
    a: "Disabling the Windows Search service removes indexed searching — Start menu search falls back to a slower non-indexed scan or stops returning file results, depending on configuration. That's why the recommended approach is fixing search, not killing it: rebuild the index and disable only the web-search integration. You keep fast local results while eliminating the two components that cause nearly all SearchHost CPU spikes."
---

Type a letter into the Windows 10 Start menu and watch Task Manager: `SearchHost.exe` leaps to 30–60% CPU, the fan spins up, and search results trickle in seconds late. Close the Start menu and it settles — until the next keystroke. This is one of Windows 10's most persistent annoyances, and it has a clear anatomy: every keystroke fires a query at both the local search index and Bing's web integration, and when either half is broken, the process burns CPU retrying.

The fix has two halves to match: repair the local index, and cut the web-search integration that causes most of the hangs. Neither requires third-party tools, and neither breaks search — you'll end up with a Start menu that answers instantly from local results only, which is what most people actually want.

Quick confirmation: open Task Manager, type in Start, and watch SearchHost.exe. If it spikes only while the search UI is open, this guide is for you. For the broader search-CPU picture, see our [SearchHost troubleshooting hub](/articles/searchhost-exe-high-cpu-troubleshooting/); if you want the nuclear option of disabling indexing entirely, the [best SearchHost fixes](/articles/best-way-to-fix-searchhost-exe-high-cpu/) weigh the tradeoffs.

## Why this happens

- **Corrupt search index**: A damaged index database makes every query expensive instead of instant.
- **Bing web integration hanging**: Online search queries timing out and retrying, burning CPU per keystroke.
- **Indexer re-crawling endlessly**: Post-update re-indexing stuck on a corrupt file or permission loop.
- **Cortana remnants**: Legacy Cortana components still hooked into the search pipeline on older installs.
- **Overly broad index scope**: Indexing entire drives including archives and game folders multiplies query cost.
- **Corrupt SearchHost app package**: The search UI's own AppX package damaged by an update.
- **Third-party shell/search tools**: Start-menu replacements or search utilities conflicting with the pipeline.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm SearchHost and test a quick restart

Verify the culprit and get temporary relief to prove the diagnosis.

1. Open **Task Manager**, go to **Details**, and sort by CPU — type in the Start menu and confirm **SearchHost.exe** is the spiker.
2. Right-click **SearchHost.exe** > **End task** — search UI closes and the process restarts fresh next time you search.
3. If CPU stays normal for a while after the restart but creeps back, the process isn't broken — its data (index, cache) is.
4. Note whether spikes happen only when typing (query problem) or also at idle (indexer problem) — this directs the next steps.
5. Keep Task Manager open during the following fixes to watch the effect live.

### Fix 2: Disable Bing web search integration

This single change fixes the majority of per-keystroke spikes.

1. Press **Win+R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer` (create the **Explorer** key if missing).
2. Create a DWORD (32-bit) value named **DisableSearchBoxSuggestions** and set it to **1**.
3. Also navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search` and set **BingSearchEnabled** to **0** (create as DWORD if missing), and **CortanaConsent** to **0**.
4. Restart SearchHost via Task Manager (End task) or reboot — Start menu search now queries only local results.
5. Test by typing several queries: results should appear instantly with no CPU spike. Microsoft documents search policy options on the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official reference.

### Fix 3: Rebuild the search index

Repair the local half of the pipeline.

1. Open **Control Panel** > **Indexing Options** (or search "Indexing Options").
2. Click **Advanced** > **Troubleshoot** first — let it attempt an automatic repair.
3. If that doesn't resolve it, click **Advanced** > **Rebuild** — this deletes the index database and re-crawls from scratch. It takes 30 minutes to several hours; keep the laptop plugged in and idle.
4. While it rebuilds, narrow the scope: in Indexing Options click **Modify** and uncheck locations you never search (game folders, archives, external drives).
5. After the rebuild completes (status shows "Indexing complete"), test Start menu searches — they should be instant with minimal CPU.

### Fix 4: Reset the SearchHost app package

When the search UI itself is corrupt, re-register it.

1. Open **PowerShell as administrator**.
2. Re-register the search package: `Get-AppxPackage -AllUsers Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
3. If that errors, try the broader re-registration for the Start menu experience host as well — search and Start share components on Windows 10.
4. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt to repair any system files the package depends on.
5. Reboot and test — a clean package plus a clean index resolves nearly all remaining cases.

### Fix 5: Check for update damage and install fixes

Windows updates both cause and cure search problems.

1. Go to **Settings** > **Update & Security** > **Windows Update** > **View update history** — note any failed updates around when the problem started.
2. Install all pending updates; Microsoft has shipped multiple SearchHost fixes in cumulative updates. If Windows Update is stuck, grab the specific KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. If the problem *started* with a specific update, use **Uninstall updates** in update history to remove it as a test — you can reinstall later once confirmed.
4. Run the **Search and Indexing troubleshooter**: Settings > Update & Security > Troubleshoot > Additional troubleshooters > Search and Indexing.
5. Re-test after each change; update-related search bugs often vanish with the next cumulative patch.

### Fix 6: Remove conflicting third-party search tools

Start-menu replacements and search utilities hook the same pipeline.

1. Check **Settings** > **Apps** for Start-menu replacements (StartIsBack, Open-Shell, Start11) or search tools (Everything with shell integration, Listary).
2. Temporarily disable or uninstall them one at a time, testing Start menu search after each.
3. Check Task Manager's **Startup** tab for search-related helpers and disable them during testing.
4. If you use **Everything** (the search tool), its own indexing is fine — but its Start-menu or shell integration can conflict; keep the app, drop the integration.
5. Once the offender is found, check for an updated version — most conflicts get fixed upstream eventually.

### Fix 7: Reduce index scope permanently

A lean index is a fast index.

1. Open **Indexing Options** > **Modify** and uncheck everything except **Users** folders and **Start Menu** — the two locations that matter for daily search.
2. Click **Advanced** > **File Types** tab and uncheck obscure file extensions you never search for — each indexed type adds query cost.
3. Under **Indexing Options**, confirm **Index encrypted files** and similar extras are off unless you need them.
4. Consider switching Outlook (if used) out of Windows Search indexing if its PST churns constantly — Outlook has its own search.
5. Rebuild once more after narrowing scope, then enjoy a Start menu that answers before you finish typing.

## Closing

SearchHost.exe high CPU on Windows 10 is a two-part problem with a two-part fix: kill the Bing integration that hangs on every keystroke, and rebuild the local index so queries are instant again. Do both and the Start menu goes back to being the fastest way to launch anything — no fan noise, no waiting, no Task Manager drama.
