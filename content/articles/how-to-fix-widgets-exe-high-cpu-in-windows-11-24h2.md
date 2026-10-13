---
title: "Widgets.exe High CPU in Windows 11 24H2? Fix It"
slug: how-to-fix-widgets-exe-high-cpu-in-windows-11-24h2
date: 2026-09-13
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "windows 11 24h2", "widgets board", "news feed"]
description: "Widgets.exe eating CPU in Windows 11 24H2? Stop the Widgets board's background news feed from hogging your processor."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is Widgets.exe and why is it running?"
    a: "Widgets.exe is the backend process for the Windows 11 Widgets board — the panel that slides out from the left showing weather, news, stocks, sports scores, and calendar items. It runs in the background to keep that content fresh, periodically fetching updates from Microsoft's services. High CPU usually means the feed is refreshing aggressively, a widget is stuck updating, or the WebView2 content it renders has a misbehaving script."
  - q: "Can I just disable the Widgets board entirely?"
    a: "Yes, and it's completely safe — the Widgets board is optional chrome, not a system component. Disabling it removes the taskbar button and stops Widgets.exe from running, with zero effect on Windows functionality. If you actually use the weather widget, you can keep the board but tame its refresh behavior instead. Both paths are covered below."
  - q: "Why did Widgets.exe start using high CPU after the 24H2 update?"
    a: "The 24H2 update re-enabled and expanded Widgets for many users — including users who had previously disabled the board — and introduced new widget providers and a more aggressive content refresh cycle. If Widgets.exe appeared in Task Manager only after 24H2, the update likely turned the feature back on. The fixes below put it back under your control."
  - q: "Does Widgets.exe use internet data in the background?"
    a: "Yes — it periodically fetches news, weather, and stock content from Microsoft's servers, which uses both bandwidth and battery on metered or mobile connections. If you're on a capped connection, disabling the Widgets board (or at least its background refresh) saves data as well as CPU. The metered-connection trick in Fix 5 addresses this directly."
---

`Widgets.exe` sitting at 15–40% CPU in Task Manager is Windows 11's news-and-weather panel misbehaving in the background — fetching, rendering, and refreshing content for a Widgets board you may never even open. It's particularly common after the 24H2 update, which re-enabled Widgets for many users who thought they'd turned it off long ago.

The good news: this is one of the easiest high-CPU problems to solve, because the Widgets board is entirely optional. You can tame its refresh behavior if you like glancing at the weather, or remove it completely if you don't — either way, Widgets.exe stops being a problem in under ten minutes.

For trimming other background consumers, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) and [removing bloatware](/articles/how-to-remove-bloatware-from-windows-11-laptop/).

## Why this happens

- **Aggressive content refresh**: The news/weather feed updating frequently, especially with many widgets pinned.
- **A stuck widget**: One widget's content failing to load and retrying in a tight loop.
- **Re-enabled by the 24H2 update**: The feature update turning Widgets back on for users who'd disabled it.
- **WebView2 rendering issues**: The embedded browser engine hitting a misbehaving script in feed content.
- **Too many widgets pinned**: Each pinned widget is an independent refresh workload.
- **Corrupt widget cache**: Damaged cached content causing repeated failed refresh attempts.
- **Background refresh on metered connections**: Fetching content even when bandwidth is precious.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the problem and check the board

Verify before changing anything.

1. In Task Manager's **Processes** tab, confirm **Widgets.exe** CPU usage — note whether it's constant or spikes periodically (periodic spikes = refresh cycle; constant = stuck widget).
2. Open the Widgets board (**Win + W** or click the taskbar widget button) — look for any widget showing loading spinners, error states, or blank content. A stuck widget is your prime suspect.
3. Note how many widgets you have pinned — each one adds refresh work. A board crammed with a dozen widgets works much harder than weather-only.
4. Check whether CPU correlates with network activity (Task Manager > **Performance** > **Wi-Fi/Ethernet**) — correlated spikes confirm the refresh cycle is the load.
5. Decision: if you never use the board, skip to Fix 4 (disable it). If you like it, continue with taming steps.

### Fix 2: Trim the Widgets board to essentials

Fewer widgets, less work.

1. Open the board (**Win + W**), click the **...** on each widget you don't need > **Remove widget** (or **Unpin**).
2. Keep only what you actually glance at — weather and calendar are the common keepers; news, stocks, esports, and "discover" feeds are the CPU-expensive ones.
3. For the news feed specifically: click the settings gear on the board > **Show or hide feeds** > turn off **Microsoft Start** feed content you don't read — the news feed is the heaviest refresher.
4. Personalize remaining widgets to update less: weather widget settings often allow reducing animation and detail level.
5. Close the board and watch Widgets.exe for 10 minutes — a trimmed board usually drops to near-zero CPU between refreshes.

### Fix 3: Repair the WebView2 runtime and widget cache

For stuck widgets and rendering loops.

1. Widgets render via **Microsoft Edge WebView2** — a corrupt runtime causes exactly these symptoms. Go to **Settings** > **Apps** > **Installed apps**, find **Microsoft Edge WebView2 Runtime**, click **...** > **Modify** > **Repair**.
2. Clear the widget cache: the board stores cached content in your user profile — signing out and back in often clears transient stuck states.
3. Check for Edge/WebView2 updates — the runtime updates through Windows Update; install all pending updates.
4. If a specific widget is stuck (spinning loader forever), remove that widget specifically and re-add it fresh — this clears its individual corrupted state.
5. Test for an hour after repair — a fixed runtime shows brief CPU blips during refresh, not sustained load.

### Fix 4: Disable the Widgets board completely

The definitive fix for non-users.

1. Go to **Settings** > **Personalization** > **Taskbar** — toggle **Widgets** to **Off**. This removes the taskbar entry point.
2. To stop the background process too: open **Task Manager** > **Startup apps**, find any Widgets-related entry, and disable it.
3. For a thorough disable via Group Policy (Pro/Enterprise): **Win + R** > `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > set **Allow widgets** to **Disabled**.
4. Alternatively via registry (Home edition): `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh` — create DWORD **AllowNewsAndInterests** = **0** (create the Dsh key if missing). Restart afterward.
5. Verify: Widgets.exe should no longer appear in Task Manager after a reboot. The **Win + W** shortcut will do nothing — which is the point.

### Fix 5: Control background refresh and data usage

For users who keep the board but want it calmer.

1. Set your connection as metered (**Settings** > **Network & internet** > connection > **Metered connection** On) — Widgets reduces background fetching on metered connections.
2. In **Settings** > **Apps** > **Installed apps** > find Widgets-related entries > **Advanced options** — set **Background apps permissions** to **Power optimized** or **Never** where available.
3. Turn off **Background apps** generally for apps you don't need refreshing: **Settings** > **Apps** > **Installed apps** > per-app **Advanced options**.
4. Use **Battery saver** mode when on battery — Windows throttles background refresh activity including Widgets.
5. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) for Widgets documentation if behavior seems off after 24H2 — Microsoft occasionally changes refresh semantics in updates.

### Fix 6: Check for the 24H2-specific issues

The update brought its own quirks.

1. Confirm you're on 24H2: **Settings** > **System** > **About** > **Version** — Widgets behavior changed notably in this release.
2. Install all pending cumulative updates — Microsoft shipped several Widgets-related fixes in post-24H2 cumulative updates.
3. If Widgets.exe high CPU *started* with 24H2 and none of the above helps, check **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — note the KB numbers and search them for known Widgets issues.
4. Re-register the Widgets experience: in **Terminal (Admin)**, run `Get-AppxPackage *WebExperience* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` — this is the package behind the Widgets board.
5. Restart and test — re-registration fixes the corrupted-state cases that survive simple toggling.

### Fix 7: The nuclear option — remove the Web Experience Pack

When you want it gone at the package level.

1. **Warning**: this removes the Widgets board entirely and is harder to reverse — only do this if you've decided you never want Widgets.
2. Open **Terminal (Admin)** and run: `Get-AppxPackage *WebExperience* -AllUsers | Remove-AppxPackage`
3. Restart — Widgets.exe should be permanently gone, along with the board.
4. To restore later, you'd need to reinstall the package from the Microsoft Store (search "Windows Web Experience Pack") or via a repair install.
5. For most users, Fix 4 (Group Policy/registry disable) is sufficient and easily reversible — prefer it over package removal unless you have a specific reason.

## Closing

Widgets.exe high CPU is an optional feature consuming non-optional resources. Trim the board if you use it, disable it if you don't — either path takes minutes and the CPU savings are immediate. Your taskbar gets cleaner, your battery lasts longer, and Task Manager loses one more mystery entry.
