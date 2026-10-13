---
title: "How to Disable Search Indexing on Windows 11 (Step-by-Step)"
slug: "how-to-disable-search-indexing-on-windows-11"
date: "2026-09-03"
categories: ["performance"]
tags: ["search indexing", "windows 11", "searchindexer.exe", "performance"]
description: "SearchIndexer.exe eating CPU and disk on your Windows 11 laptop? Learn how to pause, limit, or fully disable Windows Search indexing safely, step by step."
thumbnail: "/images/thumbs/how-to-disable-search-indexing-on-windows-11.webp"
faqs:
  - q: "Is it safe to disable Windows Search indexing?"
    a: "Yes, for most people it is completely safe. Disabling indexing does not remove the search box; it only stops Windows from maintaining a prebuilt catalog of file names and contents. Searches become slower because Windows scans folders live instead of consulting the catalog. If you rarely search inside documents, you will not notice any difference, and you can re-enable indexing at any time by restarting the service."
  - q: "How much CPU should SearchIndexer.exe normally use?"
    a: "On a healthy system, SearchIndexer.exe idles near 0 percent CPU and only spikes briefly when new files are added. Sustained usage above 10 to 15 percent for more than an hour usually means the index database is corrupted, a huge folder was just added, or a removable drive is being scanned repeatedly. Rebuilding the index or excluding the offending folder normally returns usage to idle levels within a day."
  - q: "Will disabling indexing break Start menu search?"
    a: "No. Start menu search for apps, settings, and pinned items uses a separate fast cache, not the file-content index. Installed programs and system settings will still appear instantly when you type. The only searches that slow down are deep file-content searches across the whole drive, which fall back to a slower live scan instead of returning instant indexed results."
  - q: "Should I disable the service or just exclude folders?"
    a: "Disabling the Windows Search service stops all indexing system-wide and is the most aggressive option. Excluding folders keeps the service running but tells it to skip locations like game libraries or video archives that slow it down. Folder exclusion is the better middle ground: Start menu and document search stay fast while the indexer stops churning through terabytes of media you never search."
---

Windows 11 keeps a searchable catalog of your files through a background process called SearchIndexer.exe. Every time you create, rename, or download a file, the indexer reads its name, metadata, and often its contents, then stores that data in a database under C:\ProgramData\Microsoft\Search\Data. The payoff is that Start menu searches return results in milliseconds. The cost is CPU time, disk activity, and battery life while that catalog is being built or rebuilt.

On many laptops the indexer misbehaves. It can pin CPU usage at 15 to 40 percent and keep the disk busy for hours, especially after a fresh install, a feature update such as 24H2, or when you connect an external drive full of photos. On machines with a spinning hard drive or only 8 GB of RAM, that background churn turns into visible stutter, loud fans, and shorter battery life. If you almost never use Windows to search inside documents, the index is pure overhead.

Below are three levels of control, from lightest to strongest: pausing indexing temporarily, trimming the list of indexed folders, and switching the Windows Search service off entirely. Every step is reversible, and you will verify the indexer is actually quiet afterward with Task Manager. Indexing is only one background consumer, so if the machine is still slow you may also want to [trim programs that launch at startup](/articles/how-to-disable-startup-apps-on-windows-11/).

## Why this happens

- **A fresh install or feature update:** After setup or a 24H2 upgrade, Windows rebuilds the entire index from scratch, which can mean several hours of heavy disk reads and writes on a laptop drive.
- **Large folders added to the index:** Dropping a 200 GB photo or video library into Documents triggers a full re-index of every file's contents, not just its name.
- **A corrupted search database:** If the index database under ProgramData is damaged, SearchIndexer.exe can loop, retrying the same files endlessly without ever finishing.
- **Removable drives being scanned:** USB drives and SD cards included in indexed locations force a fresh scan every time they are reconnected.
- **Outlook mailbox indexing:** The indexer also catalogs Outlook PST and OST mailbox files, and a multi-gigabyte mailbox adds serious sustained load.
- **OneDrive files kept on the device:** Folders marked Always keep on this device multiply the number of files the indexer must track and re-check.
- **Search highlights and web integration:** Features that pull online content into the search box keep background search tasks active even when you are not searching for anything.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm SearchIndexer.exe is the real culprit

Before changing anything, verify the indexer is actually responsible for the slowdown. Task Manager shows per-process CPU and disk usage, so you can confirm in two minutes rather than guessing.

1. Press Ctrl+Shift+Esc to open Task Manager.
2. Click the Processes tab and sort by the CPU column.
3. Look for SearchIndexer.exe or Microsoft Windows Search Indexer near the top.
4. Watch it for two to three minutes; brief spikes are normal, sustained load is not.
5. Also check the Disk column, since the indexer is often disk-bound rather than CPU-bound.

### Fix 2: Pause indexing for 15 minutes

If you need immediate relief, for example during a presentation, you can pause indexing without changing any settings. It resumes automatically after 15 minutes.

1. Press Win+R, type control srchadmin.dll, and press Enter to open Indexing Options.
2. Click the Pause button near the bottom of the window.
3. Confirm the status line shows indexing as paused.
4. Continue your work; indexing resumes on its own after 15 minutes.

### Fix 3: Trim the list of indexed locations

Most of the indexer's work comes from folders you never search. Removing them from the index keeps search fast for the places that matter while eliminating most of the background churn.

1. Open Indexing Options again with Win+R and control srchadmin.dll.
2. Click Modify, then expand the folder tree.
3. Uncheck large media libraries, game folders, and any external drives.
4. Keep essentials checked, such as the Start Menu folder and your active Documents folder.
5. Click OK and let the indexer settle for about 30 minutes.

### Fix 4: Switch from Enhanced to Classic search

Windows 11 defaults to Enhanced search, which indexes your entire PC. Classic mode indexes only your libraries and desktop, which is dramatically less work for the indexer.

1. Open Settings with Win+I, then go to Privacy and security.
2. Select Searching Windows in the right pane.
3. Under Find my files, choose Classic instead of Enhanced.
4. Restart the laptop so the change takes full effect.

### Fix 5: Disable the Windows Search service entirely

This is the strongest option and stops all indexing. Start menu search for apps and settings keeps working, but file-content search becomes a slower live scan. Microsoft documents the service behavior in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Press Win+R, type services.msc, and press Enter.
2. Scroll to Windows Search in the services list.
3. Right-click it and choose Stop to halt indexing immediately.
4. Right-click again, choose Properties, and set Startup type to Disabled.
5. Click OK. To reverse this later, set Startup type back to Automatic and start the service.

### Fix 6: Rebuild a corrupted index

If the indexer never finishes and CPU stays high for days, the database itself is likely damaged. Rebuilding creates a fresh catalog, which takes several hours, so keep the laptop plugged in and idle overnight.

1. Open Indexing Options with Win+R and control srchadmin.dll.
2. Click the Advanced button, then open the Index Settings tab.
3. Under Troubleshooting, click Rebuild and confirm the prompt.
4. Leave the laptop plugged in and avoid heavy work while it rebuilds.
5. Check Task Manager the next day; SearchIndexer.exe should be near idle.

### Fix 7: Exclude Outlook and unneeded file types

If you never search email from the Start menu, removing Outlook from the index can cut indexer load dramatically on machines with large mailboxes.

1. Open Indexing Options and click Modify.
2. Expand Microsoft Outlook and uncheck it, then click OK.
3. For file types, click Advanced and open the File Types tab.
4. Uncheck extensions you never search inside, such as video or archive formats.
5. Click OK, then close Indexing Options.

## Closing

Search indexing is a convenience feature, not a requirement, so do not hesitate to tame it if it is costing you performance. Start with trimming indexed locations, since that preserves fast search where it counts, and only disable the service if the indexer keeps misbehaving. If high CPU persists after indexing is quiet, the likely culprit is a different background process, and our guide to [fixing search-indexing-related high CPU](/articles/best-way-to-fix-search-indexing-high-cpu-windows-11/) walks through the next suspects.
