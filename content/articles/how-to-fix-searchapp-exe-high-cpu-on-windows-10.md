---
title: "How to Fix SearchApp.exe High CPU on Windows 10"
slug: how-to-fix-searchapp-exe-high-cpu-on-windows-10
date: 2026-09-25
categories: ["performance"]
tags: ["searchapp.exe", "high cpu", "windows 10", "cortana"]
description: "SearchApp.exe burning CPU on Windows 10? Fix the tied-together Search/Cortana process: disable Bing search, rebuild the index, and repair the search app."
thumbnail: "/images/thumbs/how-to-fix-searchapp-exe-high-cpu-on-windows-10.webp"
faqs:
  - q: "What is SearchApp.exe on Windows 10?"
    a: "SearchApp.exe is the Windows 10 process behind the Start menu search box and Cortana interface. Unlike Windows 11 (which splits this into SearchHost.exe), Windows 10 bundles search UI and Cortana remnants into this single process. High CPU from SearchApp.exe usually means the search UI is stuck — a hung web query, a corrupt search database, or Cortana hooks looping against retired services."
  - q: "Can I disable SearchApp.exe permanently?"
    a: "You can rename or block it, but that's not recommended — the Start menu search box depends on it, and Windows File Protection may restore it. Better approaches: disable Bing/web search integration (the most common CPU trigger), turn off Cortana via policy, or repair the app package. These stop the CPU burning while keeping local search functional."
  - q: "Why does SearchApp.exe spike when I just press the Windows key?"
    a: "Pressing the Windows key launches the search UI, which immediately fires off web/Bing queries, news content fetches, and search-highlight downloads — even before you type. If any of those network calls hang (proxy issues, metered connections, Microsoft service hiccups), SearchApp.exe spins waiting. Disabling web search integration eliminates this entire class of spikes."
  - q: "Will these fixes work after Windows 10's end of support?"
    a: "Yes — the fixes are configuration changes, not updates, so they work regardless of support status. That said, Windows 10 reached end of support in October 2025, so an unpatched Windows 10 no longer receives security fixes. If your hardware supports it, upgrading to Windows 11 (via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) is the safer long-term move."
---

On Windows 10, `SearchApp.exe` is the process behind the Start menu search box — and on many systems it's also where the remnants of Cortana live. When it starts burning 15–30% CPU, every press of the Windows key feels sluggish and the laptop runs warm at idle. The usual trigger isn't local file search (that's the indexer, a different process) but the web-connected parts: Bing integration, search highlights, and Cortana hooks phoning home to services that no longer fully exist. Here's how to fix it properly on Windows 10. For the Windows 11 equivalent (SearchHost.exe), see [our Windows 11 guide](/articles/how-to-fix-searchapp-exe-high-cpu-on-windows-11/); for indexer-side CPU, [taming the search indexer](/articles/how-do-i-fix-search-indexing-high-cpu-windows-11/) covers that.

## Why this happens

- **Bing/web search integration hanging**: Network calls for web results stall and the UI thread spins waiting.
- **Search highlights downloading content**: The daily highlight content fetch gets stuck on metered or proxied connections.
- **Cortana hooks looping**: Retired Cortana service calls retry and time out repeatedly.
- **Corrupt search app data**: Damaged per-user search database makes the UI re-render in a loop.
- **News and interests feed**: The taskbar feed (same backend) keeps the search process warm.
- **Third-party Start menu tools conflicting**: Classic Shell/Open-Shell hooks can fight the native search UI.
- **Pending Windows updates**: The search app package waiting on a half-installed update misbehaves.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm SearchApp.exe and its trigger

Verify the process and find what sets it off.

1. Open **Task Manager** > **Details** tab, sort by CPU, and confirm **SearchApp.exe** (not SearchIndexer.exe or SearchHost.exe) is the consumer.
2. Note the trigger: spikes when pressing the **Windows key**, when typing in search, at idle, or when the taskbar news feed refreshes.
3. Press the Windows key and type slowly — if CPU jumps the instant the UI opens (before results), it's the web/highlights fetch, not your query.
4. Check **Settings** > **Search** > **Permissions & History** and note whether cloud/search-history options are on — these add network round-trips.
5. Disconnect from the network briefly as a test: if SearchApp.exe calms down offline, you've confirmed a network-dependent trigger (web search/highlights).

### Fix 2: Disable Bing and web search integration

The single most effective fix for SearchApp.exe CPU issues.

1. Press `Win + R`, type `regedit`, and go to `HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer` (create keys as needed).
2. Create a **DWORD (32-bit)** named `DisableSearchBoxSuggestions` with value `1` — this stops web suggestions in the search box.
3. For a machine-wide block, go to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search` and create DWORD `DisableWebSearch` = `1` and DWORD `ConnectedSearchUseWeb` = `0`.
4. Alternatively on Pro: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search** > enable **"Don't search the web or display web results in Search"**.
5. Sign out and back in (or restart Explorer). Test: pressing the Windows key should now show instant local results with no CPU spike.

### Fix 3: Turn off search highlights and news feeds

Kill the content-fetching that keeps the process warm.

1. Right-click the taskbar > **Search** > uncheck **"Show search highlights"** — this stops the daily content download that frequently hangs.
2. Right-click the taskbar > **News and interests** > **Turn off** — the feed shares backend components with search.
3. Go to **Settings** > **Search** > **Permissions & History** and turn off **Cloud content search** (Microsoft account/OneDrive/Outlook/SharePoint results) if you don't need them — each is a network call per keystroke.
4. Under **Settings** > **Privacy** > **Activity history**, uncheck **"Store my activity history on this device"** if search feels tied to timeline data.
5. Restart Explorer via Task Manager and verify idle CPU — with highlights and feeds off, SearchApp.exe should sit at 0% until you actually search.

### Fix 4: Repair the SearchApp package and its data

For cases where the app itself is corrupt.

1. Open **PowerShell as Administrator** and re-register the search package: `Get-AppxPackage -AllUsers Microsoft.Windows.Cortana | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`. (On Windows 10 the search UI still ships inside the Cortana package.)
2. Clear its local data: navigate to `C:\Users\<you>\AppData\Local\Packages\Microsoft.Windows.Cortana_cw5n1h2txyewy\` and rename the **LocalState** folder to **LocalState.old** (do this from another admin account or after ending SearchApp.exe).
3. Restart the **Windows Search** service in `services.msc`.
4. Press the Windows key and test — the UI rebuilds its data fresh, which resolves render-loop CPU burns.
5. If it still spins, run the **Search and Indexing troubleshooter**: Settings > Update & Security > Troubleshoot > Additional troubleshooters. Microsoft documents it in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Disable Cortana remnants via policy

Stop the retired assistant hooks from looping.

1. On Pro: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search** > set **Allow Cortana** to **Disabled**.
2. On Home: registry at `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search`, DWORD `AllowCortana` = `0`.
3. Also disable the taskbar Cortana button: right-click taskbar > uncheck **Show Cortana button**.
4. In **Settings** > **Privacy** > **Speech, inking, & typing**, turn off **Online speech recognition** and click **"Stop getting to know me"** if present — this cuts the cloud sync the hooks retry.
5. Reboot and confirm in Task Manager that SearchApp.exe stays at 0% CPU at idle and only blips briefly during actual searches.

### Fix 6: Address underlying system issues

When the app is fine but the system underneath isn't.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt — SearchApp depends on system components these repair.
2. Install all pending **Windows Updates** (Settings > Update & Security) — search-app fixes shipped in cumulative updates through end of support; the [Update Catalog](https://www.catalog.update.microsoft.com/) has specific KBs if Update is stuck.
3. Check proxy/VPN settings: a misconfigured proxy makes every web-search call hang — **Settings** > **Network & Internet** > **Proxy**, ensure it's correct or off.
4. If you use a third-party Start menu replacement, update or temporarily disable it to rule out hook conflicts.
5. Consider the upgrade path: with Windows 10 out of support, a clean move to Windows 11 (where search is SearchHost.exe, a cleaner architecture) permanently leaves this class of bug behind.

## Closing

SearchApp.exe high CPU on Windows 10 is almost always the web-connected features misbehaving — Bing integration, search highlights, and dead Cortana hooks — not local search. Disable the web layer, repair the package, and the process drops back to near-zero where it belongs.
