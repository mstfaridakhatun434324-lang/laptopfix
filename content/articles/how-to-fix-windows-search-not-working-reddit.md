---
title: "How to Fix Windows Search When It Stops Working"
slug: how-to-fix-windows-search-not-working-reddit
date: 2026-09-13
categories: ["windows-errors"]
tags: ["windows search", "start menu", "troubleshooting"]
description: "Windows Search showing nothing but a blank box? These fixes rebuild the search index and get results appearing again."
thumbnail: "/images/thumbs/how-to-fix-windows-search-not-working-reddit.webp"
faqs:
  - q: "Why is Windows Search suddenly blank or not finding anything?"
    a: "The search index — the database Windows queries — is corrupt, the Search service has stalled, or a recent update broke the SearchHost process. Rebuilding the index and restarting the search services resolves the large majority of cases."
  - q: "Will rebuilding the index delete my files?"
    a: "No. Rebuilding only recreates the search catalog; your files are untouched. It can take 30 minutes to several hours on large drives, during which search results will be incomplete — let it finish."
  - q: "Does this fix Start menu search too?"
    a: "Yes. Start menu search and the taskbar search box use the same SearchHost process and index. Fixes here apply to both, including the 'type and nothing happens' symptom."
  - q: "What if search works but is very slow?"
    a: "Slow search usually means a bloated or fragmented index, or the indexer competing with heavy disk activity. Rebuilding the index (Fix 3) plus excluding unneeded folders from indexed locations typically restores speed."
---
You press the Windows key, type the name of a program you use every day, and... nothing. Or a blank box. Or results that never load. Windows Search breaking is one of those small failures that makes the whole laptop feel broken, because reaching for the mouse to hunt through menus feels like going back in time.

The good news: search failures are almost always the index or the search service, both repairable without touching your files. Work through these fixes in order.

## Why this happens

- **Corrupt search index:** The catalog Windows queries gets damaged by forced shutdowns, disk errors, or bad updates.
- **Stalled Windows Search service:** The `WSearch` service hangs or fails to start, so nothing gets indexed or returned.
- **Broken SearchHost process:** The UI process behind the search box crashes or fails to launch after updates.
- **Windows Update regressions:** Feature updates periodically break search components until a cumulative update fixes them.
- **Third-party "debloating" tools:** Scripts that strip Windows components often damage search irreparably.
- **Corrupt user profile:** Search settings and index state stored per-user can break for one account only.
- **Disk errors:** Bad sectors in the index database location corrupt it repeatedly.
- **Stuck "searching" after major updates:** Feature updates sometimes leave the indexer in a half-migrated state that only a rebuild clears.

## How to fix it

Work through these in order, testing search after each.

### Fix 1: Restart the search processes

The quickest fix — a stalled SearchHost often just needs a restart. This takes thirty seconds and resolves the "search box does nothing at all" symptom surprisingly often, because the SearchHost process is prone to hanging after sleep/wake cycles and cumulative updates. If you find yourself doing this weekly, treat it as a symptom and move on to the index rebuild in Fix 3 rather than living with the workaround.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. On the **Details** tab, find **SearchHost.exe**, right-click it, and choose **End task**. Windows restarts it automatically.
3. Also restart **Windows Explorer** from the **Processes** tab (right-click > **Restart**).
4. Try searching again. If the box works now, you are done — but run Fix 3 later if it was slow, since a crash can signal index damage.

### Fix 2: Run the Search and Indexing troubleshooter

Windows includes a troubleshooter that fixes common search problems automatically.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Search and Indexing** troubleshooter and check the boxes matching your symptoms.
3. Apply whatever fixes it recommends and test. This resolves permission and service-configuration issues quickly.

### Fix 3: Rebuild the search index

The definitive fix for corrupt-index problems.

1. Open **Control Panel** (search for it in the Start menu — ironic, but the Control Panel window has its own search) and go to **Indexing Options**.
2. Click **Advanced**, then under **Troubleshooting** click **Rebuild**.
3. Confirm and let it run — it takes 30 minutes to several hours depending on drive size and file count. Search results will be incomplete until it finishes, so start it when you can leave the laptop alone.
4. While you are in Indexing Options, click **Modify** and uncheck folders you never search (like program caches) to keep the index lean.

### Fix 4: Restart the Windows Search service

If the service itself is the problem, reset it.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Search**, right-click it, and choose **Restart**. Double-click it and set **Startup type** to **Automatic (Delayed Start)** if it is not already.
3. If the service will not start, note the error message — "access denied" points to permission damage (Fix 6), while dependency errors point to deeper system damage.

### Fix 5: Re-register the search app package

On Windows 11 especially, the search UI is an app package that can break.

1. Open **Windows PowerShell as administrator** (right-click Start > **Terminal (Admin)**).
2. Run: `Get-AppxPackage -Name "MicrosoftWindows.Client.CBS" | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Reboot and test. This reinstalls the shell components that include the search box without affecting your data.

### Fix 6: Repair system files

Corrupt search components get replaced by SFC.

1. Open an elevated **Command Prompt** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Reboot. If search broke immediately after a Windows update, also check for newer cumulative updates — Microsoft frequently ships search fixes in them. See [Microsoft Support](https://support.microsoft.com/en-us/windows) for the latest known search issues.

### Fix 7: Test with a new user profile

If search works in a new account, your profile's search state is corrupt.

1. Go to **Settings > Accounts > Other users > Add account** and create a local account.
2. Sign into it and test search. If it works there, migrate your files to the new profile — repairing per-user search corruption in place is rarely worth the effort.
3. Before migrating, try one in-place repair: in your original account, delete the contents of `%ProgramData%\Microsoft\Search\Data\Applications\Windows` (with the Windows Search service stopped), then restart the service to force a clean index rebuild.

### Fix 8: Check the disk for errors

A drive with bad sectors will keep corrupting the index no matter how often you rebuild it.

1. In an elevated Command Prompt, run `chkdsk C: /f /r` and reboot to let it scan.
2. Check SMART health for reallocated sectors. If the drive is deteriorating, replace it — recurring index corruption is an early warning sign of drive failure.

## Closing

Windows Search failures are index or service problems, not mysteries: restart SearchHost, run the troubleshooter, rebuild the index, and repair system files. In that order, these four steps fix search on the overwhelming majority of machines — no reinstall required. If the Start menu itself is also misbehaving alongside search, the two share infrastructure, and our [Start menu repair guide](/articles/how-to-fix-start-menu-not-working-on-windows-11-on-lenovo-laptop/) covers the shell side; for the Windows 11-specific search variants, see [Windows Search not working on Windows 11](/articles/how-to-fix-windows-search-not-working-on-windows-11/).
