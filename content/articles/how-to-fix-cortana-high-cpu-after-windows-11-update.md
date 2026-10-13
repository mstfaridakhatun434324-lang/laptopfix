---
title: "Cortana High CPU After a Windows 11 Update? Shut It Down"
slug: how-to-fix-cortana-high-cpu-after-windows-11-update
date: 2026-09-05
categories: ["performance"]
tags: ["cortana high cpu", "windows 11 update", "cortana disable", "searchhost cpu"]
description: "Cortana (SearchHost) burning CPU after a Windows 11 update? Disable or tame the search assistant and reclaim your processor."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "Is Cortana still part of Windows 11?"
    a: "Cortana as a standalone assistant app was retired by Microsoft, but its remnants live on inside Windows Search — the SearchHost.exe process that powers the Start menu search box. When people report Cortana high CPU on Windows 11, they are almost always seeing SearchHost.exe or SearchIndexer activity triggered by the update. The fixes below target the search subsystem that inherited Cortana's old job, which is why they work even though the Cortana app itself is gone."
  - q: "Why would a Windows update make Cortana/Search use more CPU?"
    a: "Feature updates rebuild the search index from scratch, re-register search components, and sometimes re-enable search features (web search integration, search highlights) that you had previously turned off. Until the fresh index completes — which can take many hours of idle time on large drives — SearchHost and the indexer work overtime. If your settings were reset by the update, the search box is also fetching web suggestions and highlight content continuously."
  - q: "Will disabling Cortana/Search break Windows search?"
    a: "It depends what you disable. Turning off web search integration, search highlights, and Cortana's cloud features leaves local file and app search working normally — that is the safe, recommended tuning. Fully disabling the SearchHost process or ripping out Windows Search breaks the Start menu search box and taskbar search. The guide below keeps local search intact while removing the CPU-expensive cloud and highlight features most people never use."
  - q: "How do I tell SearchHost CPU apart from SearchIndexer CPU?"
    a: "In Task Manager, SearchHost.exe is the interactive search UI process (the search box experience), while SearchIndexer.exe (Windows Search service) builds the index database in the background. High SearchHost CPU usually means the search UI is doing something expensive — web suggestions, highlights rendering, or a stuck query. High SearchIndexer CPU means index building or rebuilding. Both commonly spike after updates, but they have different fixes, so identifying which one is hot matters."
---

After the Windows 11 update finished, something called Cortana — or its modern incarnation, SearchHost.exe — started eating 15-25% of your CPU nonstop. The search box may feel laggy, the fans spin during idle, and Task Manager shows the search subsystem working hard while you do nothing. Microsoft retired the Cortana app, but its DNA lives on in Windows Search, and updates have a habit of waking it up.

The update typically does two things: it invalidates the search index (forcing a full rebuild) and it re-enables the cloud-connected search features you may have switched off long ago. Both are fixable without breaking local search. For the indexer's side of this story, see [Windows Search indexer high CPU](/articles/how-to-fix-windows-search-indexer-high-cpu-in-windows-11-24h2/); for the broader slow-after-update picture, [Windows 11 slow after update](/articles/windows-11-slow-after-update-how-to-fix/).

## Why this happens

- **Search index rebuilt by the update**: Feature updates invalidate the index; rebuilding it means hours of SearchIndexer CPU on large drives.

- **Re-enabled web search integration**: Updates switch Bing web results back on, so every keystroke in the search box triggers network fetches and rendering.

- **Search highlights content**: The rotating highlight stories in the search box fetch and render fresh content continuously.

- **Corrupt search database**: A half-migrated index from the update loops on errors instead of completing.

- **Stuck SearchHost process**: The search UI process can wedge after the update, spinning on a failed initialization.

- **Excessive indexed locations**: Enhanced indexing mode watching the entire drive multiplies rebuild work after every feature update.

- **Cloud clipboard / activity history sync**: Update-reset sync features add background search-related traffic.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which search process is hot

Cortana, SearchHost, and SearchIndexer are different processes with different fixes.

1. Open **Task Manager > Processes** and sort by CPU; note whether **SearchHost.exe**, **SearchIndexer** (under Background processes), or both are consuming CPU.
2. If SearchHost.exe is the hot one, the problem is the search UI experience (fixes 3-4); if SearchIndexer, it is index building (fix 2).
3. Open the search box (Win + S) and watch Task Manager — if SearchHost spikes the moment the box opens, web content/highlights are the trigger.
4. Check **Settings > Privacy & security > Searching Windows** to see the current indexing mode and indexed locations count.
5. Note your findings; the remaining fixes split along this diagnosis.

### Fix 2: Let the index rebuild — or shrink what gets indexed

If SearchIndexer is the hog right after an update, it may just need time — or a smaller job.

1. Give it one full cycle first: leave the laptop plugged in and idle for a few hours; check **Indexing Options > Indexing Status** for progress.
2. If the status shows the same file count stuck for hours, the index is corrupt — click **Advanced > Rebuild** to start clean.
3. Reduce the workload: **Settings > Privacy & security > Searching Windows** — switch from **Enhanced** to **Classic** mode.
4. Click **Advanced Search Indexer Settings > Modify** and uncheck folders that do not need instant search (game libraries, downloads, archives).
5. Exclude file types you never search: in **Advanced > File Types**, uncheck exotic extensions clogging the index.

### Fix 3: Turn off web search and highlights

The cloud-connected search features are the biggest SearchHost CPU drivers — and the least missed.

1. Go to **Settings > Privacy & security > Search permissions** and turn off **Cloud content search** (both Microsoft account and Work/School).
2. In the same page, under **More settings**, turn off **Show search highlights**.
3. Open the search box, click the **...** menu > **Search settings**, and disable any remaining web/highlight toggles.
4. Restart the SearchHost process: **Task Manager > Details > SearchHost.exe > End task** (it restarts automatically).
5. Test the search box: local apps and files should still appear instantly, but the CPU-hungry web fetching is gone.

### Fix 4: Restart and repair the search subsystem

For a wedged SearchHost, a clean restart of the whole search stack clears the jam.

1. Open **services.msc**, find **Windows Search**, right-click > **Restart**.
2. In **Task Manager > Details**, end **SearchHost.exe** and **SearchUI.exe** if present; they respawn fresh.
3. Run the troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Search and Indexing > Run**.
4. If the troubleshooter reports a corrupt index, let it rebuild (this takes hours — plan overnight).
5. Verify over the next day: SearchHost should idle near 0% except for brief pulses when you actually search.

### Fix 5: Disable Cortana remnants and startup entries

Leftover Cortana components can still launch and consume resources.

1. Check **Task Manager > Startup apps** for anything Cortana-related and disable it.
2. In **Settings > Apps > Installed apps**, look for the Cortana app — if present, uninstall it (Microsoft retired it; it serves no purpose now).
3. Review **Settings > Privacy & security > Speech** and turn off **Online speech recognition** if you do not use voice features.
4. Check **Task Scheduler > Microsoft > Windows > Windows Search** for odd tasks and disable any third-party additions (leave Microsoft's defaults).
5. These remnants are small individually, but on an update-disturbed system each one adds to the pile.

### Fix 6: Check what the update changed in your settings

Feature updates reset preferences silently; audit the search-related ones.

1. Revisit **Settings > Privacy & security > Searching Windows** and confirm your indexing mode survived the update.
2. Check **Search permissions** (Fix 3's toggles) — updates are notorious for re-enabling cloud search.
3. Look at **Settings > Personalization > Taskbar** — if **Search** was reset to **Search box** from **Search icon only**, the always-visible box encourages the highlights feature; set it to icon-only.
4. Review **Settings > Accounts > Windows backup** — update-enabled sync of settings can re-push old search configurations.
5. Document your preferred settings; the next feature update will likely try to reset them again.

### Fix 7: Repair Windows if search stays broken

When the search subsystem is corrupt beyond settings, repair the OS components.

1. Run **DISM /Online /Cleanup-Image /RestoreHealth** then **sfc /scannow** in an elevated terminal and restart.
2. Re-register the search app package: in elevated PowerShell, run **Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}**.
3. Test in a new local user account — if search behaves there, your profile's search database is corrupt and migrating profiles is cleaner than further repair.
4. As a final measure, an in-place upgrade via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) rebuilds search cleanly while keeping files and apps.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the search troubleshooters if you want the official walkthrough.

## Closing

Cortana high CPU after a Windows 11 update is really the search subsystem rebuilding and re-enabling its cloud features: let or shrink the index rebuild, switch off web search and highlights, and restart the wedged processes. Local search stays fast and instant — it is the cloud-connected extras that were eating your CPU, and you will not miss them.
