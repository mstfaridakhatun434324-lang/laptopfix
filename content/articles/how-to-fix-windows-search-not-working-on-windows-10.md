---
title: "Windows Search Not Working on Windows 10: How to Fix It"
slug: how-to-fix-windows-search-not-working-on-windows-10
date: 2026-10-06
categories: ["windows-errors"]
tags: ["windows 10", "windows search", "cortana", "indexing"]
description: "Windows 10 search not finding files or Cortana search dead? Fix SearchUI crashes, broken indexes, and empty results with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-search-not-working-on-windows-10.webp"
faqs:
  - q: "Why is search not working on Windows 10?"
    a: "Windows 10 search runs through SearchUI.exe (tied to Cortana) plus the Windows Search indexing service. The common failures are a crashed SearchUI process, a corrupt index, the indexing service disabled by optimizer tools, or Bing integration hanging the results pane."
  - q: "What's the difference between Windows 10 and 11 search problems?"
    a: "Windows 11 moved search to SearchHost.exe, a separate process from the old Cortana-tied SearchUI.exe on Windows 10. The symptoms overlap but the process names and package registrations differ — see our [Windows 11 search fix guide](/articles/how-to-fix-windows-search-not-working-on-windows-11/) for the newer architecture."
  - q: "Will rebuilding the index delete anything?"
    a: "No. Rebuilding only recreates the search database; files, apps, and settings are untouched. It runs in the background and can take several hours on large drives, during which search results may be incomplete."
  - q: "Can I disable Bing in Windows 10 search?"
    a: "Yes, via a well-known registry setting (BingSearchEnabled = 0), and it often speeds up local search noticeably. But only do it after confirming search itself works — disabling Bing masks symptoms rather than fixing a broken SearchUI process."
---

Windows 10 search has its own personality compared to Windows 11: it runs through `SearchUI.exe`, historically tangled up with Cortana, and it leans on Bing for web results in a way that can hang the entire results pane when the network hiccups. When it breaks, you get the familiar symptoms — type in the taskbar box and nothing happens, results never appear, or the search window opens blank.

The architecture matters for the fix: on Windows 10 you're restarting SearchUI (not SearchHost), re-registering the Cortana package (not the Windows 11 search package), and dealing with Bing integration as a potential culprit. The steps below are built for exactly this setup.

## Why this happens

- **SearchUI.exe crashes**: The search/Cortana UI process dies and doesn't recover cleanly, leaving the taskbar search box dead.
- **Corrupt search index**: The index database gets damaged, so file and app searches return nothing or outdated results.
- **Windows Search service disabled**: Debloat scripts and "privacy" tools disable the indexing service, killing search.
- **Bing integration hanging**: The web-results pane waits on a network response that never comes, freezing the whole search UI.
- **Cortana package corruption**: SearchUI lives inside the Cortana app package; if its registration breaks, search breaks with it.
- **Corrupt system files**: Update or disk damage to search components.
- **Profile-specific corruption**: Search works in a new account but not yours — the per-user search database is damaged.

## How to fix it

Work through these in order — the process restart and troubleshooter resolve most cases.

### Fix 1: Restart the SearchUI process

The Windows 10 equivalent of the quick fix.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. On the **Processes** tab, find **Search** (listed as Search/Cortana) — or go to **Details** and find `SearchUI.exe`.
3. Right-click and choose **End task**. Windows restarts it automatically.
4. Click the taskbar search box and test. If it was just a crashed process, you're done in under a minute.

### Fix 2: Run the Search and Indexing troubleshooter

Built-in diagnosis before manual surgery.

1. Open **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters**.
2. Select **Search and Indexing** and click **Run the troubleshooter**.
3. Tick the symptoms that match and apply its fixes.
4. Microsoft documents further search repairs at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Verify the Windows Search service

Optimizer tools disable this constantly.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Windows Search** — set **Startup type** to **Automatic (Delayed Start)** and make sure it's **Running**.
3. If you recently ran a debloating or "privacy" script, review everything it changed — they often disable several services search depends on.

### Fix 4: Rebuild the search index

For missing results, stale results, or new files never appearing.

1. Open **Control Panel** > **Indexing Options** > **Advanced** > **Rebuild**.
2. Let it run — it takes 30 minutes to several hours. Search will be incomplete meanwhile; that's normal.
3. When **Indexing Options** reports "Indexing complete," test thoroughly: apps, settings, and files.

### Fix 5: Disable Bing web results (if search hangs)

When the results pane freezes, Bing is often the anchor.

1. Press **Win + R**, type `regedit`, press Enter.
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search`.
3. Create a DWORD (32-bit) value named `BingSearchEnabled` set to `0`. Also set `CortanaConsent` to `0` if present.
4. Restart `SearchUI.exe` via Task Manager (Fix 1) and test. Local search becomes noticeably faster, and network hangs stop freezing results.
5. Only use this after confirming the basics work — it's an optimization, not a repair for a dead SearchUI.

### Fix 6: Re-register the Cortana/Search package

For a search box that won't open or crashes instantly.

1. Open **PowerShell as administrator** (**Win + X** > **Windows PowerShell (Admin)**).
2. Run: `Get-AppXPackage -Name Microsoft.Windows.Cortana | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Ignore errors about already-registered components.
4. Restart and test. This repairs the package registration updates sometimes damage.

### Fix 7: Repair system files and install the latest cumulative update

Deeper corruption in search components — plus the updates that fix them.

1. In an elevated PowerShell, run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart.
4. Then open **Settings** > **Update & Security** > **Windows Update** and install everything offered, including optional updates. Microsoft ships search fixes in cumulative updates — several notorious search breakages were fixed this way, and staying current is genuine prevention.
5. After updating, re-run the troubleshooter (Fix 2) once, since updates sometimes reset the configurations it repairs.
6. If the Start menu is misbehaving too, the [Start menu fix guide](/articles/how-to-fix-start-menu-not-working-on-windows-11-on-lenovo-laptop/) covers the shared shell infrastructure.

### Fix 8: Reset the per-user search data or try a new profile

Final isolation: profile vs. system.

1. Stop the **Windows Search** service, then delete the contents of `C:\ProgramData\Microsoft\Search\Data\Applications\Windows`.
2. Restart the service and let the index rebuild from scratch.
3. If that fails, create a new local account (**Settings** > **Accounts** > **Family & other users** > **Add someone else to this PC**) and test search there.
4. Working in the new account means your old profile's search data is unrecoverable — migrate your files over.

## Closing

Windows 10 search failures come down to its three moving parts: the SearchUI process, the index, and the Windows Search service — with Bing integration as the bonus troublemaker. Restart the process, verify the service, rebuild the index, and only then reach for package re-registration and profile surgery. Match the fix to the symptom and the taskbar search box goes back to being the fastest way to launch anything on your PC. On a Windows 11 machine the architecture differs (SearchHost instead of SearchUI), so use the [Windows 11 search fix guide](/articles/how-to-fix-windows-search-not-working-on-windows-11/) there instead of these steps.

And keep Windows Update current afterward. A surprising number of "search suddenly broke" cases are fixed by the very next cumulative update, because Microsoft keeps patching this subsystem. The troubleshooter plus an updated system resolves nearly everything this component can throw at you.
