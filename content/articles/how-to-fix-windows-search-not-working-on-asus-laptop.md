---
title: "How to Fix Windows Search Not Working on an ASUS Laptop"
slug: how-to-fix-windows-search-not-working-on-asus-laptop
date: 2026-09-11
categories: ["windows-errors"]
tags: ["windows-search", "asus", "search-indexer"]
description: "Windows Search not working on your ASUS laptop? This step-by-step guide repairs the search service, rebuilds the index, and gets results working again."
thumbnail: "/images/thumbs/how-to-fix-windows-search-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why does the search box open but show no results on my ASUS laptop?"
    a: "In most cases the SearchHost.exe process has crashed or the search index is corrupted. Restarting the process through Task Manager fixes it instantly for many people. If results come back briefly and then vanish again, the index database itself is damaged and needs a rebuild, which takes 15 to 60 minutes depending on how many files you have."
  - q: "Can Armoury Crate or MyASUS break Windows Search?"
    a: "They rarely break it directly, but ASUS utilities ship with background services and the bundled McAfee trial can interfere with Windows Search indexing. If the problem started right after installing or updating ASUS software, try temporarily disabling the McAfee trial and restarting the Windows Search service to see whether search recovers."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. Rebuilding only deletes and recreates the search database; your documents, photos, and apps are untouched. Windows recreates the index in the background. During the rebuild, search results may be incomplete, so let the laptop finish the job before judging whether the fix worked."
  - q: "How long does the Search and Indexing troubleshooter take?"
    a: "Usually 3 to 10 minutes. It checks the Windows Search service status, index permissions, and common misconfigurations, then applies repairs automatically. You may be asked whether search is slow, missing results, or not working at all; pick the symptom closest to yours for the most accurate repair."
---
You press the Windows key, type the name of a document you know is there, and Windows Search just stares back at you. Maybe it shows a spinning circle, maybe the search box opens completely empty, or maybe you get the message "Search results aren't quite ready yet" for days on end. On ASUS laptops this tends to show up right after a Windows update or a fresh driver install.

The good news is that Windows Search is almost never truly broken beyond repair. The service that powers it is separate from the rest of Windows, and the fixes below target each layer in order — from a quick process restart up to a full repair install. If you also see problems on the wider platform, our guide to [Windows Search not working in Windows 11 24H2](/articles/how-to-fix-windows-search-not-working-in-windows-11-24h2/) covers the same fixes from the operating-system side, and owners of other brands can check [the HP version of this fix](/articles/how-to-fix-windows-search-not-working-on-hp-laptop/).

## Why this happens

- **The SearchHost.exe process has crashed or frozen.** This is the process behind the search box. When it hangs, the box opens but nothing renders.
- **The Windows Search service is disabled or stuck.** Some "debloat" scripts and third-party optimizers turn this service off, and a failed update can leave it in a stopped state.
- **The search index is corrupted.** The index database can be damaged by a power loss during indexing, a failing drive, or an interrupted Windows update.
- **Conflicting ASUS or security software.** The bundled McAfee trial and some ASUS background services hook into file operations and can block the indexer from reading folders.
- **Broken system files.** A bad update can corrupt the AppX package files that Windows Search depends on.
- **Indexing exclusions or a wrong location.** If your user folder was moved or permissions were changed, the indexer may be scanning an empty or inaccessible path.

## How to fix it

Work through these in order, testing search after each one. Most people are fixed by step 3.

### Fix 1: Restart the Search process in Task Manager

This is the quickest fix and resolves a surprising number of cases.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. Switch to the **Details** tab and find **SearchHost.exe**.
3. Right-click it and choose **End task**. It restarts automatically within a few seconds.
4. If the search box also looks frozen, find **explorer.exe** in the **Processes** tab, right-click it, and choose **Restart**.
5. Press the **Windows key**, type something, and check whether results appear.

### Fix 2: Run the Search and Indexing troubleshooter

Windows ships a dedicated troubleshooter that catches common misconfigurations.

1. Open **Settings** (press **Win + I**) and go to **System > Troubleshoot**.
2. Click **Other troubleshooters**, then find **Search and Indexing** and click **Run**.
3. Select the problems you're seeing — usually "Files don't appear in search results" or "Search doesn't work" — and click **Next**.
4. Apply any recommended repairs and restart the laptop if asked.
5. Microsoft's [Windows Search support page](https://support.microsoft.com/en-us/windows) has additional background if the troubleshooter reports it couldn't fix everything.

### Fix 3: Restart the Windows Search service

The service itself can get wedged even when everything else looks fine.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Scroll to **Windows Search**, right-click it, and choose **Restart**. If it's stopped, choose **Start** instead.
3. Right-click it again, choose **Properties**, and set **Startup type** to **Automatic (Delayed Start)**.
4. Click **OK** and test the search box again.

### Fix 4: Rebuild the search index

If the process and service are healthy but results are wrong or missing, the index database is the culprit.

1. Open the **Control Panel**, switch the view to **Large icons**, and open **Indexing Options**.
2. Click **Advanced**, then under the **Troubleshooting** section click **Rebuild**.
3. Confirm by clicking **OK**. Windows starts recreating the index in the background.
4. Leave the laptop plugged in and give it time — a large drive can take up to an hour.
5. You can watch progress in the **Indexing Options** window, which shows how many items are indexed.

### Fix 5: Re-register the Windows Search app package

When a Windows update damages the Search package files, re-registering them repairs the app without touching your data.

1. Right-click the **Start** button and choose **Terminal (Admin)** or **Windows PowerShell (Admin)**.
2. Paste this command and press **Enter**:
   `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to finish — it usually takes under a minute and shows no errors when it succeeds.
4. Restart the laptop and test search.

### Fix 6: Repair system files with SFC and DISM

Corrupt system files are a common root cause after a bad update.

1. Right-click the **Start** button and choose **Terminal (Admin)**.
2. Run the System File Checker: `sfc /scannow`
3. Let it finish (this takes 10 to 20 minutes), then run the DISM repair:
   `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart the laptop when both finish, then check whether search works.

### Fix 7: Temporarily disable conflicting ASUS and security software

If the problem started after installing ASUS utilities or antivirus software, isolate the conflict.

1. Open **Settings > Apps > Installed apps** and look for the McAfee trial that ships on many ASUS laptops.
2. Temporarily disable it from its own settings, or uninstall it with **Uninstall** (Windows Defender takes over protection automatically).
3. Restart the laptop and test search. If it works, reinstall McAfee afterward and add an exclusion, or leave it uninstalled.
4. As a last resort, use the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) to perform an in-place upgrade, which reinstalls Windows while keeping your files and apps.

## Closing

Windows Search failures on ASUS laptops almost always trace back to a crashed process, a stopped service, or a corrupted index — all fixable without losing data. Work through the steps in order, give the index rebuild time to finish, and search should be back to instant results within the hour. If the issue returns after every reboot, check your startup programs and recently installed software, since something is repeatedly breaking the search service.
