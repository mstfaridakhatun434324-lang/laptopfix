---
title: "How to Fix Windows Search Not Working, Step by Step"
slug: how-to-fix-windows-search-not-working-step-by-step
date: 2026-09-20
categories: ["windows-errors"]
tags: ["windows search", "windows 11", "troubleshooting"]
description: "Windows Search returns nothing or won't open? Follow this step-by-step guide to rebuild the index and repair search on Windows 11."
thumbnail: "/images/thumbs/how-to-fix-windows-search-not-working-step-by-step.webp"
faqs:
  - q: "Why is Windows Search not finding my files?"
    a: "The search index is usually corrupted, paused, or incomplete. Rebuilding the index forces Windows to recatalog everything. Third-party antivirus, disabled search services, and corrupted system files are the other common causes."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. Rebuilding only deletes the search catalog, not your documents. Windows recreates the catalog by scanning your files again, which can take anywhere from minutes to a few hours depending on how much data you have."
  - q: "Why does the search box not open at all when I click it?"
    a: "That is usually the SearchHost process crashing or the shell experience host failing. Restarting the Windows Explorer process or re-registering the search package typically restores it immediately."
  - q: "Can I just use a third-party search tool instead?"
    a: "You can, and many people do, but the built-in search also powers the Start menu and Settings search. Fixing the underlying problem is worth it even if you prefer another tool for file searches."
---

You press the Windows key, type the name of a program you use every day, and Windows Search shows nothing. Or the search box opens to a blank panel, or it opens and instantly closes. When search breaks, the whole operating system feels broken, because the Start menu, Settings, and File Explorer all depend on the same search backend.

The usual villain is the search index, the catalog Windows maintains of your files. When it corrupts, goes stale, or stops building, results vanish. The fixes below walk you through restarting the search machinery, rebuilding the index from scratch, and repairing the deeper components, in the order that wastes the least of your time.

## Why this happens

- **Corrupted search index.** The catalog of your files gets damaged, often after a crash or an interrupted update, and returns wrong or empty results.
- **Search services stopped.** The Windows Search service or the SearchHost process can crash or be disabled by system cleaners.
- **Corrupted system files.** Damage to the shell components that host the search interface breaks the search box itself.
- **Third-party interference.** Antivirus and privacy tools sometimes block the indexing process or the search backend.
- **Broken search package.** The AppX package behind Windows Search can corrupt, especially after feature updates.
- **Disk errors.** Filesystem damage in the folders being indexed produces a perpetually broken catalog.
- **Too many indexed locations.** Indexing entire drives with hundreds of thousands of files can overwhelm the indexer and stall it indefinitely.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Restart the search and shell processes

The fastest fix for a search box that will not open.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. On the **Details** tab, find **SearchHost.exe**. Right-click it and choose **End task**. It restarts automatically.
3. On the **Processes** tab, right-click **Windows Explorer** and choose **Restart**.
4. Try the search box again. If it opens, you are done.

### Fix 2: Run the Search and Indexing troubleshooter

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Search and Indexing**.
3. Check the boxes that describe your problem, such as files not appearing in results, and let it diagnose.
4. Apply any fixes it recommends and restart.

### Fix 3: Restart the Windows Search service

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Windows Search** in the list. If its status is not **Running**, right-click it and choose **Start**.
3. Right-click it again, choose **Properties**, and set **Startup type** to **Automatic (Delayed Start)**.
4. Click **OK** and test search. Some aggressive system cleaners set this service to Disabled, which breaks search permanently until you revert it.

### Fix 4: Rebuild the search index

This is the definitive fix for wrong or missing results, and it is worth the wait.

1. Press **Windows key + R**, type `control srchadmin.dll`, and press Enter to open Indexing Options.
2. Click **Advanced**, then click **Rebuild** under Troubleshooting. Confirm when asked.
3. Leave the laptop plugged in and powered on. Rebuilding can take from twenty minutes to several hours depending on your files. The laptop may feel slightly slower during the rebuild because the indexer is working hard in the background.
4. Check the status at the top of Indexing Options. Wait until it says indexing is complete before judging the results. Testing too early, while the catalog is half-built, will make it look like the rebuild failed when it simply is not finished.

### Fix 5: Re-register the Windows Search package

If the search box itself is broken, rebuild its app package.

1. Press **Windows key + X** and open **Terminal (Admin)**.
2. Run this command: `Get-AppxPackage -AllUsers Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
3. Wait for completion, ignoring red text, then restart the laptop.
4. Open search and confirm the panel renders and accepts typing.

### Fix 6: Check disk health and trim indexed locations

1. In an elevated Terminal, run `chkdsk C: /f`. Type **Y** to schedule it and restart.
2. Open Indexing Options again with `control srchadmin.dll`.
3. Click **Modify** and uncheck locations you do not need searched, like program folders or entire secondary drives full of archives.
4. A smaller, focused index builds faster and corrupts less often.

### Fix 7: Repair system files

1. In an elevated Terminal, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` if SFC reports unfixable damage.
3. Restart. System file damage is a common reason the search interface breaks after updates.

### Fix 8: Create a new user profile as a final test

1. Open **Settings** > **Accounts** > **Other users** and add a new local account.
2. Sign in to it and test search. If search works there, your original profile's search configuration is corrupted beyond easy repair.
3. Migrate your files to the new account rather than continuing to fight the old one.
4. Related shell fixes: [start menu not working on Windows 11](/articles/what-to-do-if-start-menu-not-working-on-windows-11/) and the step-by-step [taskbar repair guide](/articles/how-to-fix-taskbar-not-working-on-windows-11-step-by-step/). Microsoft's search help is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

Windows Search breaks in predictable ways, and the index rebuild in Fix 4 resolves the majority of cases where results go missing. When the search box itself will not open, the process restart and package re-registration do the job. Keep the Windows Search service on automatic, avoid cleaners that promise to disable it for performance, and let the index finish building after big file changes. Search is one of those features you only notice when it is gone, and these fixes bring it back for good. If results ever go stale again in the future, you now know the drill: restart the service, check the troubleshooter, and rebuild the index before assuming anything is seriously wrong.
