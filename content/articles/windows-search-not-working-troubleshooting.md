---
title: "Windows Search Not Working? Complete Troubleshooting Guide"
slug: windows-search-not-working-troubleshooting
date: 2026-09-02
categories: ["windows-errors"]
tags: ["windows search", "search broken", "troubleshooting", "windows 11"]
description: "Windows Search not finding files or showing a blank panel? Work through this complete troubleshooting order to get search working again."
thumbnail: "/images/thumbs/windows-search-not-working-troubleshooting.webp"
faqs:
  - q: "Why did Windows Search suddenly stop working?"
    a: "The most common triggers are a corrupted search index, a crashed SearchHost.exe process, a Windows update that broke the Search app package, or corrupted system files. Third-party system cleaners that aggressively delete index files can also break it overnight. The fixes below address each cause in order of likelihood."
  - q: "How long does rebuilding the search index take?"
    a: "It depends on how many files you have: typically twenty minutes to a few hours on an SSD, longer on a spinning hard drive. You can use the laptop normally while it rebuilds — search results improve gradually. Avoid shutting down mid-rebuild if you can; let it finish for the most reliable results."
  - q: "Will resetting Windows Search delete my files or settings?"
    a: "No. Resetting the Search app only clears the app's own data and preferences — your files, installed programs, and Windows settings are untouched. You'll lose custom search preferences like excluded folders, which you can reconfigure afterward in Indexing Options."
  - q: "What if search works in a new user account but not mine?"
    a: "That confirms your user profile's search data is corrupted. The practical fix is to migrate to the new account: copy your files over and reinstall your programs there. Trying to surgically repair a corrupted profile usually takes longer than migrating, and the new profile gives you a clean slate."
---
Windows Search failing is one of those problems that slowly drives you mad — you press the Windows key, type, and get nothing, or a blank panel, or results that clearly miss files you know exist. Before you install a third-party search tool, know that the built-in Search is very fixable; it just has several layers (service, index, app package, system files) and you have to work them in the right order.

This guide goes from the thirty-second checks to the deeper repairs. Most people are fixed by the third step — and even the deeper steps are safe, since none of them touch your personal files. The index rebuild in particular looks intimidating but is fully automated; you just start it and let Windows do the work in the background while you get on with your day.

## Why this happens

- **The SearchHost process crashed.** SearchHost.exe can hang or crash, leaving the search panel blank or frozen.
- **Corrupted search index.** The index database can be damaged by hard shutdowns, disk errors, or aggressive system cleaners.
- **Broken Search app package.** Windows updates occasionally damage the Search app's registration.
- **Windows Search service stopped.** The underlying WSearch service can be disabled by tweaking tools or fail to start.
- **Corrupted system files.** Damaged core files break the components Search depends on.
- **Corrupted user profile.** Profile-specific search data and settings can break in ways that affect only one account.
- **Pending Windows updates.** An update that's downloaded but not yet installed can leave Search components in a half-migrated state until the restart completes.

## How to fix it

Work through these in order.

### Fix 1: Restart the Search process and check the service

The quickest possible fix — takes under a minute.

1. Press **Ctrl + Shift + Esc** to open Task Manager, go to the **Details** tab, find **SearchHost.exe**, right-click it, and choose **End task**. It restarts automatically.
2. Press **Win + R**, type `services.msc`, and find **Windows Search**.
3. Make sure its **Startup type** is **Automatic** and its status is **Running** — if not, start it.
4. Test search. If it works now, a crashed process was the whole story.

### Fix 2: Run the Search and Indexing troubleshooter

Windows has a dedicated troubleshooter for exactly this.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Search and Indexing** troubleshooter.
3. Check the boxes matching your symptoms (files not appearing, slow search) and let it apply fixes.
4. Test search before moving on — the troubleshooter resolves permission and configuration issues automatically.

### Fix 3: Rebuild the search index

A corrupted index is the most common deep cause of missing or wrong results.

1. Press **Win + R**, type `control /name Microsoft.IndexingOptions`, and press Enter.
2. Click **Advanced**, then under Troubleshooting click **Rebuild**. Confirm the prompt.
3. Let the rebuild run — use the laptop normally; results improve as it progresses.
4. If the rebuild button is greyed out, the Windows Search service isn't running — go back to Fix 1 first.

### Fix 4: Repair and reset the Search app

If the search panel is blank or won't open, the app package itself is likely damaged.

1. Go to **Settings > Apps > Installed apps** and find **Search** (listed as "Windows Search" on some builds).
2. Click the three dots, choose **Advanced options**, and click **Repair**. Test.
3. If repair doesn't help, return to the same screen and click **Reset**.
4. Restart the laptop and test the search panel again.

### Fix 5: Re-register Search with PowerShell

When reset isn't enough, re-register the app package.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run: `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to complete — it produces little output on success.
4. Restart and test. This fixes package registration damage that the Settings reset can't reach.

### Fix 6: Repair system files

If Search broke alongside other Windows features, the foundation is damaged.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and test search thoroughly — try file names, settings, and apps.
4. If system file corruption was the cause, other flaky Windows behaviors often clear up at the same time.

### Fix 7: Test a new user profile

Profile-level corruption is the last software layer.

1. Go to **Settings > Accounts > Other users** and create a new local administrator account.
2. Sign into it and test search.
3. If search works there, your old profile's search data is corrupt — migrate your files to the new account.
4. If search fails in the new profile too, the problem is system-wide: consider a repair install using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) media, choosing the keep-files-and-apps option.

### Fix 8: Check for a bad update

If search broke right after Patch Tuesday, say so with your actions.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update and restart.
3. Test search. If it returns, pause updates for a couple of weeks while Microsoft fixes the regression.
4. You can verify fixed builds on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) before unpausing.

## Closing

Windows Search has a reputation for being fragile, but it's really just layered — process, service, index, app package, system files, profile — and each layer has a concrete fix. Work them in order and you'll find the broken one instead of reinstalling Windows in frustration.

Once it's healthy, leave the index alone: resist "PC cleaner" tools that promise to speed things up by deleting index files, because they're a top cause of the exact problem you just fixed. If you ever need to exclude folders from search (large video collections, game libraries), do it properly in Indexing Options rather than with third-party tools — proper exclusions speed up the index without breaking it. If your search broke specifically after the 24H2 update, the [24H2 search fix guide](/articles/how-to-fix-windows-search-not-working-in-windows-11-24h2/) covers update-specific causes. If search broke at the same time as blue screens appeared, read the [combined Search-plus-BSOD guide](/articles/windows-search-not-working-bsod-windows-11/) instead — that points to a shared root cause.
