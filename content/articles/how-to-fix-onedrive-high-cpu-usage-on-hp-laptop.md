---
title: "How to Fix OneDrive High CPU Usage on an HP Laptop"
slug: how-to-fix-onedrive-high-cpu-usage-on-hp-laptop
date: 2026-09-26
categories: ["performance"]
tags: ["onedrive", "high cpu", "hp laptop", "cloud sync"]
description: "OneDrive chewing CPU on your HP laptop even when you're not syncing? Fix the 'Processing changes' loop, trim synced folders, and reset the sync client."
thumbnail: "/images/thumbs/how-to-fix-onedrive-high-cpu-usage-on-hp-laptop.webp"
faqs:
  - q: "Why is OneDrive using CPU when it says 'Up to date'?"
    a: "Even at 'Up to date,' OneDrive's file watcher monitors every synced folder for changes in real time. If another program constantly touches files in those folders — backups, antivirus scans, HP utilities, or apps writing temp files there — OneDrive re-hashes and re-evaluates them endlessly. The fix is finding which program is churning files in synced folders, or moving that program's working folders outside OneDrive."
  - q: "Does the number of files in OneDrive affect CPU usage?"
    a: "Directly. OneDrive tracks each synced file individually, so a library of 100,000+ small files means 100,000 items to watch, hash, and reconcile. Users with huge photo libraries or node_modules folders inside OneDrive see the worst CPU. Selective sync (Choose folders) and Files On-Demand dramatically cut the tracked set — sync only what you need on the laptop."
  - q: "Should I unlink OneDrive to fix high CPU?"
    a: "Unlinking is a legitimate troubleshooting step, not a defeat — it stops all sync activity so you can confirm OneDrive was the cause, and signing back in rebuilds the sync database cleanly. Your files remain in the cloud and (by default) locally. Only use 'Unlink this PC' after trying selective sync and a reset; it's the deeper fix when the sync database itself is corrupt."
  - q: "Can HP software make OneDrive use more CPU?"
    a: "Indirectly, yes. HP Support Assistant scans, HP backup features, and preinstalled utilities that write logs or temp files into synced folders (Documents, Desktop) trigger OneDrive re-syncs. Check HP Support Assistant's automation schedule on [HP's support site](https://support.hp.com/us-en) guidance and keep HP tools' working folders outside your OneDrive-synced directories."
---

There's a special kind of annoyance in watching `OneDrive.exe` burn 25% CPU while the tray icon cheerfully reports "Up to date." Nothing is uploading, nothing is downloading — yet the sync engine is working hard. On HP laptops this usually traces to the same root as on any PC: OneDrive is reacting to constant file churn from other programs, tracking far too many files, or stuck in a "Processing changes" loop it can't exit. The difference from a plain sync workload is that pausing doesn't help for long — the CPU comes back the moment you resume. Here's how to fix the underlying churn. If your issue is specifically heavy syncing (large uploads), see our [Dell OneDrive sync guide](/articles/how-to-fix-onedrive-sync-high-cpu-on-dell-laptop/) for the transfer-side fixes; for general background load, [startup program cleanup](/articles/how-to-disable-startup-programs-windows-11/) helps.

## Why this happens

- **"Processing changes" loop**: The sync engine re-scans the library repeatedly without making progress.
- **Too many tracked files**: 100k+ files means 100k items under constant watch.
- **Other apps churning synced folders**: Antivirus, backups, and HP utilities touching files OneDrive monitors.
- **Known Folder Move syncing everything**: Desktop/Documents/Pictures backup pulling in huge, churn-heavy folders.
- **Files locked by running apps**: Open databases and Outlook files that OneDrive retries constantly.
- **Corrupt sync database**: Damaged local state causing endless re-reconciliation.
- **Old OneDrive client**: Sync-engine efficiency fixes you don't have yet.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the churn source

Find out what's actually keeping OneDrive busy.

1. Right-click the **OneDrive tray icon** > **Pause syncing** > **2 hours**, then watch Task Manager: if OneDrive.exe CPU drops to zero, sync activity is definitively the cause (not the updater or a stuck installer).
2. Resume syncing and open **Resource Monitor** (`resmon`) > **Disk** tab, filter by `OneDrive.exe` — the files with constant read activity are the churn set.
3. Note the paths: if it's `node_modules`, `.git`, temp folders, or app caches inside synced directories, those should never have been synced.
4. Check the tray icon status text over 30 minutes: "Processing changes" that never resolves is the loop signature.
5. Open **Settings** (gear icon) > **Account** and look for sync errors — files listed here are retried forever and must be dealt with individually.

### Fix 2: Get churn-heavy folders out of OneDrive

The most impactful fix: stop syncing what shouldn't be synced.

1. Move developer folders (`node_modules`, build outputs, `.git` repos), VM images, and app cache directories **out** of OneDrive-synced folders entirely.
2. In OneDrive **Settings** > **Account** > **Choose folders**, uncheck entire folder trees you don't need on this laptop.
3. Review **Sync and backup** > **Manage backup** (Known Folder Move): if Desktop/Documents/Pictures backup is on, check what's actually in those folders — game saves, screen recordings, and installer downloads don't belong in cloud backup.
4. For folders you want in the cloud but not watched constantly, use **Free up space** (right-click > in File Explorer) to make them online-only — OneDrive tracks placeholders far more cheaply.
5. After trimming, restart OneDrive (tray icon > Pause > Quit OneDrive, then relaunch) so it rebuilds its watch list from the smaller set.

### Fix 3: Fix the "Processing changes" loop

When the engine is stuck rather than just busy.

1. First, the gentle reset: run `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset` from `Win + R` — this rebuilds the sync database without touching files.
2. If the tray icon doesn't return in 5 minutes, launch `%localappdata%\Microsoft\OneDrive\onedrive.exe` manually.
3. Still looping? **Unlink and relink**: Settings > **Account** > **Unlink this PC**, then sign back in. Choose **"Use this folder"** with the existing location to avoid re-downloading everything.
4. During the post-relink scan, CPU will be legitimately high for a while — judge only after the first full pass completes (check the tray status).
5. If a specific file always blocks progress, the sync report names it: rename it (remove `#`, `%`, trailing spaces), shorten the path, or move it out of OneDrive.

### Fix 4: Separate HP utilities from synced folders

HP-specific churn sources on HP laptops.

1. Open **HP Support Assistant** and check its automated tasks — disable automatic tune-ups/scans or schedule them for times you're not working; each scan touches files OneDrive then re-evaluates.
2. Check where HP utilities write logs and temp files — if any point into Documents or Desktop (synced via Known Folder Move), redirect them to a non-synced location like `C:\HP_Temp`.
3. Review other preinstalled HP software (HP Smart, HP Wolf Security logs) for folder-monitoring features pointed at synced directories.
4. Update HP Support Assistant itself from [HP's support site](https://support.hp.com/us-en) — older versions were chattier with the filesystem.
5. After separating them, monitor for a full day: OneDrive should settle to near-zero CPU between actual file changes.

### Fix 5: Reduce OneDrive's background footprint

Make the client lighter even during legitimate syncing.

1. **Settings** > **Network**: cap the **upload rate** — unlimited uploading on a slow connection keeps the CPU busy with retries and hashing.
2. Disable **Office file collaboration** caching if you don't co-author: Settings > **Office** tab > uncheck "Use Office applications to sync Office files that I open."
3. Turn off **"Start OneDrive automatically when I sign in"** (Settings > Settings tab) if you only need sync on demand — launch it manually when you want files backed up.
4. Exclude the OneDrive folder from **Windows Security** real-time scanning of its internal database (not your files): add `%localappdata%\Microsoft\OneDrive` as an exclusion — AV scanning the sync engine's own files doubles the work.
5. Keep the client current: **Settings** > **About** shows the version; the standalone updater sometimes lags behind the [Microsoft Store](https://support.microsoft.com/en-us/windows) release.

### Fix 6: Reinstall OneDrive cleanly as a last resort

When resets and relinks don't stick.

1. **Unlink first**: Settings > Account > Unlink this PC — this protects the cloud state.
2. Uninstall OneDrive via **Settings** > **Apps** > **Installed apps** > Microsoft OneDrive > **Uninstall**.
3. Delete leftover state: `%localappdata%\Microsoft\OneDrive` and `%localappdata%\Microsoft\OneDriveSetup` (your actual synced files in `C:\Users\<you>\OneDrive` stay untouched — verify before deleting anything).
4. Download a fresh OneDrive from Microsoft's site and install, then sign in and choose your existing folder.
5. Let the initial scan finish completely before judging CPU — then confirm the idle state is quiet. If CPU is still high with a fresh client and trimmed folders, the churn is coming from another program — revisit Fix 1's Resource Monitor trace.

## Closing

OneDrive high CPU with "nothing syncing" means something is churning files under the sync engine's watch — usually too many tracked files, another program touching synced folders, or a stuck sync database. Trim the watched set, separate HP utilities' working folders, reset the database, and OneDrive goes back to sipping CPU instead of gulping it.
