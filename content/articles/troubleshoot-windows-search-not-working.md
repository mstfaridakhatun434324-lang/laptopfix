---
title: "Windows Search Not Working? A Troubleshooter's Diagnostic Guide"
slug: troubleshoot-windows-search-not-working
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windows search", "search not working", "troubleshooter", "indexing", "windows 11"]
description: "Windows Search returns nothing, shows a blank box, or won't open at all? Use this systematic diagnostic approach to find the root cause and fix it."
thumbnail: "/images/thumbs/troubleshoot-windows-search-not-working.webp"
faqs:
  - q: "Why does Windows Search suddenly stop working?"
    a: "The usual suspects are a crashed SearchHost.exe process, a corrupted search index, a broken Windows Search service, or a recent update that damaged search components. Third-party antivirus and system 'debloater' tools are also frequent culprits because they disable the services Search depends on. The diagnostic steps below isolate which of these is responsible on your machine."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. The index is just a catalog Windows builds to find files quickly — rebuilding it deletes and recreates the catalog, never the files themselves. Your documents stay exactly where they are. The only cost is time: a full rebuild can take several hours on a drive with hundreds of thousands of files, during which search results stay incomplete."
  - q: "Is Windows Search broken by a Windows update?"
    a: "It happens more often than it should. Several Windows 11 updates have temporarily broken the search UI or the indexing service. If search died within a day of an update, the built-in Search and Indexing troubleshooter or a servicing-stack repair with DISM usually resolves it. Check Microsoft's support site for known issues with that specific update before rolling it back."
  - q: "Should I just replace Windows Search with a third-party tool?"
    a: "Tools like Everything are excellent for finding files by name, but they don't replace Start menu search, Settings search, or Outlook integration. Fix the built-in search properly using the steps below — it also powers features you use without realizing. A third-party tool is a fine supplement, not a substitute."
---

Windows Search is one of those features you only notice when it breaks. One day the Start menu search box returns nothing, shows a blank white panel, or refuses to open entirely — and suddenly finding a file or launching an app becomes a chore. The frustration is compounded by how vague the symptoms are: "search doesn't work" can mean half a dozen different failures under the hood.

Rather than throwing random fixes at it, this guide takes the troubleshooter's approach: reproduce the symptom precisely, isolate which component failed, then apply the targeted fix. Search in Windows 11 is actually several pieces working together — the SearchHost.exe UI process, the Windows Search indexing service, the index database itself, and the system files they all depend on. Each fails differently, and each has a different fix. Identify yours first.

Before you start, note exactly what you see: a blank search window, no response when typing, results that never load, or an error message. That observation determines which fix below is yours. If you want the straight step-by-step repair sequence instead of the diagnostic method, our [direct fix guide](/articles/how-to-fix-windows-search-not-working-in-windows-11-24h2/) covers the same repairs in a different order.

## Why this happens

- **SearchHost.exe has crashed or hung**: The search UI is a separate process. When it crashes, the search box opens blank or not at all while everything else works fine.
- **Corrupted search index**: The index database can be damaged by sudden shutdowns, disk errors, or failed updates, leaving search unable to return results.
- **Windows Search service disabled or failing**: Tweaking tools, "debloater" scripts, and some third-party antivirus products disable the WSearch service that powers indexing.
- **Broken system files from an update**: A bad Windows update can damage the AppX packages or system components that the search experience depends on.
- **Cortana/Search app package corruption**: In Windows 11, search functionality ships as system app packages that can break independently of the OS.
- **Third-party shell or Start menu replacements**: Tools that replace the Start menu sometimes hook into search and break it when they malfunction or update.
- **User profile corruption**: Occasionally the problem is confined to one user account — search works fine for a new user, pointing at profile-level damage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Characterize the failure precisely

Diagnosis starts with observation. Don't skip this — it saves you from applying the wrong fix.

1. Press **Windows + S**. Does the search window open? Note whether it's blank, frozen, or shows an error.
2. Type a filename you know exists. Do results appear slowly, partially, or not at all?
3. Open **Task Manager** (**Ctrl + Shift + Esc**), go to **Details**, and check whether **SearchHost.exe** is running.
4. Match your symptom: no window at all points to SearchHost or app package issues (Fixes 2–3); a window with no results points to the index or service (Fixes 4–5); results that are wrong or stale point to index corruption (Fix 5).

### Fix 2: Restart the search processes

The quickest win — a hung SearchHost often just needs a restart.

1. Open **Task Manager** with **Ctrl + Shift + Esc** and go to the **Details** tab.
2. Find **SearchHost.exe**, right-click it, and choose **End task**. Also end **SearchIndexer.exe** if present.
3. Press **Windows + S** again — Windows relaunches SearchHost automatically.
4. If search works now, the process had simply hung. If it breaks again after reboot, something is crashing it at startup — continue to Fix 3.

### Fix 3: Run the Search and Indexing troubleshooter

Windows includes a dedicated troubleshooter that checks the common failure points automatically.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Search and Indexing** and click **Run**.
3. Check the boxes matching your symptoms (e.g., "Files don't appear in search results") and let it diagnose.
4. Apply whatever fixes it recommends, then test search. Microsoft documents additional manual steps on their [Windows support pages](https://support.microsoft.com/en-us/windows) if the troubleshooter can't resolve it.

### Fix 4: Verify the Windows Search service

If the indexing service is disabled, no amount of UI restarting will help.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **Windows Search** in the list. Its **Status** should be **Running** and **Startup type** should be **Automatic (Delayed Start)**.
3. If it's stopped or disabled, double-click it, set the startup type to **Automatic (Delayed Start)**, click **Start**, then **OK**.
4. Think about what disabled it: if you ran a debloater script or privacy tool, it may re-disable the service on every boot — whitelist Windows Search in that tool or stop using it.

### Fix 5: Rebuild the search index

When results are missing, incomplete, or stale, the index database is usually corrupt.

1. Open **Control Panel** > **Indexing Options** (switch to icon view if you don't see it).
2. Click **Advanced**, then under **Troubleshooting** click **Rebuild**.
3. Confirm and let it run — this takes anywhere from thirty minutes to several hours depending on how many files you have. Your PC stays usable during the rebuild.
4. Check **Indexing Options** afterward to confirm the indexed locations still include your user folders; updates sometimes silently drop locations.

### Fix 6: Re-register the search app packages

If the search window won't open at all, the underlying AppX packages may be broken.

1. Right-click **Start** and open **Windows Terminal (Admin)** or **PowerShell (Admin)**.
2. Run: `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to complete — errors in red about already-registered packages are normal and harmless.
4. Restart and test. If search still won't open, create a new local user account (**Settings** > **Accounts** > **Other users**) and test search there — working search in a new profile confirms your original profile is corrupt, and migrating to the new profile is the cleanest fix.

### Fix 7: Repair system files with DISM and SFC

Update-damaged system components need servicing-stack repair, not just a process restart.

1. Open **Windows Terminal (Admin)**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish — this downloads clean replacements for damaged components.
3. Then run `sfc /scannow` and restart when done.
4. Test search after the reboot. If a specific Windows update caused the damage, consider pausing updates temporarily while Microsoft ships a fix — and check the [update catalog](https://www.catalog.update.microsoft.com/) for a revised version of the problematic KB.

### Fix 8: Reset Windows Search via the registry (advanced)

When everything else fails, a full reset of search settings can clear corruption the other fixes miss.

1. Press **Windows + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search`.
2. Right-click the **Windows Search** key and export it first as a backup (File > Export).
3. Look for a `SetupCompletedSuccessfully` DWORD — setting it to `0` forces Windows to reinitialize search on next boot. Alternatively, rename the `Windows Search` key (with the service stopped) to force full reinitialization.
4. Restart the PC. Windows rebuilds the search configuration from scratch, which takes several minutes on first boot — be patient before testing.

## Closing

Windows Search failures feel mysterious because the symptom — "nothing happens when I type" — hides which of several components actually broke. The diagnostic habit is what separates a five-minute fix from an afternoon of frustration: characterize the symptom, check the process, check the service, check the index, in that order. Nine times out of ten, the culprit is a hung SearchHost, a disabled service from a tweaking tool, or a corrupt index — all fixable without touching your files. And if search works fine for a new user account but not yours, stop fighting the old profile and migrate; some corruptions aren't worth the archaeology. For the related case where the whole Start menu misbehaves alongside search, our [Safe Mode diagnostic guide](/articles/how-to-boot-windows-11-in-safe-mode/) helps you test whether third-party software is interfering.
