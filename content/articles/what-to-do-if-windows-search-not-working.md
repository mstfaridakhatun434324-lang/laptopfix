---
title: "Windows Search Not Working? Get It Back in 8 Steps"
slug: what-to-do-if-windows-search-not-working
date: 2026-10-12
categories: ["windows-errors"]
tags: ["windows search not working", "search bar", "windows 11", "indexing"]
description: "Windows 11 search bar dead, blank results, or won't open? Restart SearchHost, rebuild the index, and fix it step by step."
thumbnail: "/images/thumbs/what-to-do-if-windows-search-not-working.webp"
faqs:
  - q: "Why is Windows Search not working on Windows 11?"
    a: "The usual causes: the SearchHost.exe process crashed or hung, the search index is corrupt, a Windows update broke the search components, or Cortana/Search integration services are disabled. Third-party 'debloating' tools that strip Windows components are another frequent cause. The fixes below address each in order of likelihood."
  - q: "How do I restart Windows Search?"
    a: "Open Task Manager with Ctrl+Shift+Esc, go to the Details tab, find SearchHost.exe, right-click it, and choose End task. Windows restarts it automatically within seconds. This clears hung search states instantly and is the fastest first fix when the search box opens but shows no results."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. Rebuilding only recreates the database Windows uses to find files quickly — your files themselves are never touched. The rebuild runs in the background and can take several hours on large drives, during which search results may be incomplete. Leave the laptop on and plugged in until it finishes."
  - q: "What if Windows Search broke after a Windows update?"
    a: "Updates sometimes corrupt search components or reset indexing settings. Run the Search and Indexing troubleshooter first, then restart the Windows Search service, then rebuild the index. If it still fails, uninstall the most recent quality update from Settings > Windows Update > Update history and test before reinstalling it."
---

When the Windows 11 search box stops working — blank results, the panel won't open, typing does nothing, or it crashes instantly — it feels like a small problem until you realize how much you depend on it. The good news: Windows Search is a self-contained set of processes and a database, and nearly every failure is one of a handful of repeat causes: a hung **SearchHost.exe** process, a corrupt search index, broken components after an update, or services that got disabled.

Start with the quick wins. A hung search process restarts in seconds; a corrupt index takes hours to rebuild, so you want to rule out the fast fixes before committing to the slow ones. If search is also eating CPU while broken, our guide on [SearchApp high CPU usage](/articles/how-to-fix-searchapp-exe-high-cpu-reddit/) covers that variant; for the update-specific angle, see [search not working in 24H2](/articles/how-to-fix-windows-search-not-working-in-windows-11-24h2/).

## Why this happens

- **Hung or crashed SearchHost.exe**: The search UI process hangs and stops responding to input — the most common cause, and the fastest to fix.
- **Corrupt search index**: The index database that powers instant results gets damaged, returning nothing or crashing the search panel.
- **Broken components after a Windows update**: Updates replace search files and reset indexing options; a bad update breaks search outright.
- **Disabled Windows Search service**: The underlying `WSearch` service gets disabled by "optimization" guides or debloating tools.
- **Third-party debloaters and "privacy" tools**: Scripts that rip out Cortana, Bing integration, or search components break dependencies search needs.
- **Corrupt user profile**: Search works in a new account but not yours — the profile's search data is damaged.
- **Conflicting shell extensions or Start menu mods**: Third-party Start menu replacements and shell tweaks hook into search and break it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the SearchHost.exe process

Thirty seconds, fixes the majority of "search does nothing" cases.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. Go to the **Details** tab and find **SearchHost.exe**.
3. Right-click it and choose **End task**. Windows relaunches it automatically within seconds.
4. Press **Win + S** and test. If search works now, the process had simply hung.

### Fix 2: Restart the Windows Search service

The engine behind the UI.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Search** in the list. If its status is blank or Stopped, double-click it.
3. Set **Startup type** to **Automatic (Delayed Start)** and click **Start**.
4. If it was already running, right-click and choose **Restart**. Test search again — a stale service state clears with a restart.

### Fix 3: Run the Search and Indexing troubleshooter

Let Windows diagnose its own search stack.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Search and Indexing** troubleshooter.
3. Check the boxes matching your symptom (e.g. "Files don't appear in search results") and let it apply fixes.
4. Test search. The troubleshooter commonly restarts services and repairs permissions you'd otherwise fix manually.

### Fix 4: Rebuild the search index

For corrupt-index symptoms: empty results, missing files, or search that worked yesterday.

1. Open **Control Panel** > **Indexing Options** (switch to Large icons if you don't see it).
2. Click **Advanced**, then under Troubleshooting click **Rebuild**.
3. Confirm. The rebuild runs in the background — expect several hours on a full drive, during which results will be incomplete.
4. Keep the laptop plugged in and powered on until **Indexing Options** shows "Indexing complete." Then test with a filename you know exists.

### Fix 5: Toggle search highlights and online integration

Bing integration and highlights are frequent breakage points.

1. Open **Settings** > **Privacy & security** > **Search permissions**.
2. Under **Cloud content search**, toggle **Microsoft account** and **Work or School account** off, test search, then toggle back on if you want them.
3. In **Settings** > **Privacy & security** > **Search** (Windows permissions), toggle **Show search highlights** off and test.
4. If search works with cloud content off, the problem is the online component — leave it off or sign out and back into your Microsoft account to refresh its tokens.

### Fix 6: Re-register the search app package

Repairs broken search components after updates.

1. Open **Terminal (Admin)** or **PowerShell (Admin)**.
2. Run: `Get-AppXPackage -AllUsers -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for completion (red "already registered" warnings are normal).
4. Restart and test. This restores search files that updates sometimes leave in a broken state.

### Fix 7: Test in a new user account

Isolates profile corruption quickly.

1. Go to **Settings** > **Accounts** > **Other users** > **Add account** and create a local account.
2. Sign into it and press **Win + S**. If search works there, your main profile's search data is corrupt.
3. You can try deleting the corrupt search database in the old profile (`%USERPROFILE%\AppData\Local\Packages\Microsoft.Windows.Search_cw5n1h2txyewy`), but migrating to the new account is more reliable.
4. If search fails in the new account too, the problem is system-wide — continue to Fix 8.

### Fix 8: Repair system files and check for bad updates

The last-resort software layer.

1. Open **Terminal (Admin)**. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, and restart.
2. If search broke right after an update, go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates** and remove the most recent quality update, then test.
3. Check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known search issues with your Windows build before reinstalling the update.
4. If you previously ran a debloating script, consider an in-place upgrade repair (Windows 11 ISO > setup > **Keep personal files and apps**) to restore removed components properly.

## Closing

Windows Search failures are annoying but shallow — a hung process, a corrupt index, or a broken component, in that order of likelihood. Work the quick fixes first (process restart, service restart, troubleshooter) before committing to the index rebuild, and resist "fixes" that involve registry hacks from random forums; the supported steps above resolve essentially every search failure without risking the rest of the system.
