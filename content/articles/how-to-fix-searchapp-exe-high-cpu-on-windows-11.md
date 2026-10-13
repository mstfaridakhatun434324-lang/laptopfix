---
title: "How to Fix SearchApp.exe High CPU on Windows 11"
slug: how-to-fix-searchapp-exe-high-cpu-on-windows-11
date: 2026-09-28
categories: ["performance"]
tags: ["searchapp.exe", "searchhost", "high cpu", "windows 11"]
description: "SearchHost.exe (SearchApp) spiking CPU on Windows 11? Repair the search UI, tame web integration, and stop the Start menu search from burning cycles."
thumbnail: "/images/thumbs/how-to-fix-searchapp-exe-high-cpu-on-windows-11.webp"
faqs:
  - q: "Is it SearchApp.exe or SearchHost.exe on Windows 11?"
    a: "Windows 11 uses SearchHost.exe for the Start menu search UI — SearchApp.exe is the Windows 10 name. People still say 'SearchApp' out of habit, and some upgraded systems briefly show the old name. The fixes are the same family: both are the search UI process, both spike from web integration and corrupt app data, and both are repaired by re-registering the package and clearing its cache."
  - q: "Can I end SearchHost.exe in Task Manager?"
    a: "Yes — ending SearchHost.exe is safe and it restarts automatically the next time you open search. It's actually a useful diagnostic: if CPU drops to zero after ending it and stays low until you next press the Windows key, the process itself is fine and something about the search UI session (a hung query, a stuck content fetch) was the problem. If it immediately respawns at high CPU, the trigger is persistent."
  - q: "Does disabling web search break anything important?"
    a: "Only the Bing results inside the Start menu search box. Local file search, app launching, Settings search, and File Explorer search all keep working exactly as before — they never used the web layer. Most power users prefer it disabled: results appear instantly with no network delay, no CPU spikes from hung web calls, and no Microsoft account content mixed into local searches."
  - q: "Why does search use CPU even when I'm not searching?"
    a: "The search UI pre-loads in the background and periodically refreshes search highlights, news content, and Microsoft account suggestions. On Windows 11, the Widgets board and search highlights share infrastructure, so one's refresh can wake the other. Disabling search highlights and background app permissions for search components stops nearly all idle CPU from this process."
---

Windows 11 renamed the process to `SearchHost.exe`, but everyone still calls it SearchApp — and whatever you call it, when the Start menu search UI starts burning 15–30% CPU, the whole laptop feels broken. Every Windows-key press lags, the fans spin at idle, and Task Manager points at a process you barely knew existed. On Windows 11 the triggers are familiar: web search integration hanging, search highlights fetching content, and corrupt per-user search data. (On Windows 10, where it's genuinely called SearchApp.exe, see [our Windows 10 guide](/articles/how-to-fix-searchapp-exe-high-cpu-on-windows-10/).) For indexer-side CPU rather than UI-side, [our search indexing guide](/articles/how-do-i-fix-search-indexing-high-cpu-windows-11/) covers that.

## Why this happens

- **Web search calls hanging**: Bing integration fires network requests per keystroke; stalled calls spin the UI thread.
- **Search highlights content fetch stuck**: The rotating highlight content fails to download cleanly on some networks.
- **Corrupt SearchHost app data**: Damaged local state causes render loops in the search flyout.
- **Microsoft account content sync**: Cloud suggestions and history sync adding per-keystroke round-trips.
- **Widgets board cross-talk**: Widgets and search share infrastructure; one's refresh wakes the other.
- **Broken package registration**: A half-updated SearchHost package misbehaves after feature updates.
- **Background preloading**: The UI pre-loads aggressively and doesn't always idle properly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: End the task and observe the pattern

The quickest diagnostic in the book.

1. Open **Task Manager** > **Details** tab, find **SearchHost.exe**, right-click > **End task**. (It restarts on next search — this is safe.)
2. Watch CPU for 10 minutes without pressing the Windows key: stays at zero? The process idles fine; the trigger is search-session related.
3. Now press the Windows key and type a query: instant results with a brief small spike is normal; a sustained 20%+ means the query pipeline is stuck.
4. If SearchHost.exe respawns immediately at high CPU without any search, something is programmatically invoking search — check Widgets and background apps (Fix 5).
5. Note whether spikes correlate with network state: VPNs, proxies, and captive portals are notorious for hanging the web-search calls.

### Fix 2: Disable web search and highlights

Removes the most common CPU trigger entirely.

1. Go to **Settings** > **Privacy & security** > **Search permissions** and turn off **Cloud content search** (Microsoft account, OneDrive, SharePoint, Outlook).
2. Under **More settings** on the same page, turn off **Show search highlights**.
3. For the full policy-level block on Pro: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search** > enable **"Don't search the web or display web results in Search"** and **"Don't use web results"**.
4. On Home, the registry equivalent: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search`, DWORD `DisableWebSearch` = `1`.
5. Restart Explorer (Task Manager > Windows Explorer > Restart) and test: Windows-key searches should now be instant, local-only, and CPU-flat.

### Fix 3: Re-register and reset the SearchHost package

Fixes corruption in the search UI itself.

1. Open **PowerShell as Administrator** and run: `Get-AppxPackage Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
2. Clear its cached data: with SearchHost ended, rename `C:\Users\<you>\AppData\Local\Packages\Microsoft.Windows.Search_cw5n1h2txyewy\LocalState` to `LocalState.old`.
3. Restart the **Windows Search** service (`services.msc`) — SearchHost depends on the underlying service.
4. Press the Windows key: the UI rebuilds fresh state. Test several queries, including ones that previously spiked CPU.
5. If the package won't re-register, run `sfc /scannow` first — a damaged component store breaks AppX registration. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the search troubleshooter as a companion step.

### Fix 4: Run the Search and Indexing troubleshooter

The built-in automated pass before deeper surgery.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Search and Indexing** > **Run**.
2. Check the boxes matching your symptoms ("Search doesn't return results," "Search is slow") — the troubleshooter resets permissions and restarts services.
3. Let it complete and apply any fixes it offers, then reboot.
4. Test search behavior for a day — the troubleshooter fixes permission and service-state issues but not corrupt app data (that's Fix 3).
5. If the troubleshooter reports it couldn't fix something, note the exact message — it often names the failing component, which focuses the next steps.

### Fix 5: Silence Widgets and background search activity

Stops the idle-time wake-ups.

1. **Settings** > **Personalization** > **Taskbar** > turn off **Widgets** — the Widgets board shares backend services with search and its refreshes wake SearchHost.
2. **Settings** > **Apps** > **Installed apps** > search for any search-related entries > **Advanced options** > set **Background apps permissions** to **Never** where you don't need background activity.
3. **Settings** > **Privacy & security** > **General** > turn off **"Let websites show me locally relevant content"** and ad-ID options — these feed the content pipeline search highlights use.
4. In **Task Scheduler** (`taskschd.msc`), check **Microsoft** > **Windows** > **Shell** for search-related tasks erroring on run and disable the broken ones.
5. Monitor Task Manager at idle for 30 minutes: SearchHost.exe should now sit at 0% until you actually invoke search.

### Fix 6: Repair Windows underneath

When the search stack is fine but the OS isn't.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` from an elevated prompt — in that order.
2. Install all pending updates at **Settings** > **Windows Update** — search-stack fixes ship in cumulative updates; check the [Update Catalog](https://www.catalog.update.microsoft.com/) for specific KBs if Update itself is broken.
3. Test in a **new local user account**: if search is calm there, your profile's search data is corrupt beyond the LocalState reset — migrate to the new profile.
4. As a heavier repair, do an **in-place upgrade** using the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) (keep files and apps) — it refreshes every system component including search.
5. After any repair, re-verify Fixes 2 and 3 — feature updates and repairs can reset search policies and reintroduce web integration.

## Closing

On Windows 11, "SearchApp" CPU is really SearchHost.exe — the Start menu search UI — and it's almost always the web layer (Bing integration, highlights) or corrupt app data. Disable the web features, re-register the package, silence Widgets, and the search UI drops back to the near-zero idle it should have had all along.
