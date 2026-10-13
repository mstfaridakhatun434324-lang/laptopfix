---
title: "OneDrive Sync High CPU in Windows 11 24H2? Fix It"
slug: how-to-fix-onedrive-sync-high-cpu-in-windows-11-24h2
date: 2026-09-03
categories: ["performance"]
tags: ["onedrive sync high cpu", "windows 11 24h2", "onedrive fix", "cloud sync cpu"]
description: "OneDrive syncing constantly and eating CPU on Windows 11 24H2? Stop the sync storms with Files On-Demand tuning, selective sync, and throttling fixes."
thumbnail: "/images/thumbs/how-to-fix-onedrive-sync-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Why does OneDrive use so much CPU when syncing?"
    a: "Syncing is genuinely CPU-intensive work: OneDrive hashes every changed file to detect differences, encrypts transfers, maintains a local database of sync state, and on 24H2 integrates with new Windows backup and recall-adjacent features that expand what gets watched. A few hundred changed files is trivial; tens of thousands — common with photo libraries, dev folders, or game mods — means sustained hashing that pins a CPU core. The CPU cost scales with file count far more than with total gigabytes."
  - q: "Should I just uninstall OneDrive to stop the CPU usage?"
    a: "Uninstalling is effective but usually overkill, and you lose file backup, cross-device sync, and the Files On-Demand placeholders many people rely on. The fixes below — selective sync, Files On-Demand, pausing, and excluding high-churn folders — eliminate the CPU problem while keeping the useful parts. Uninstall only if you genuinely never use cloud sync; otherwise you are amputating for a splinter. If you do uninstall, first move synced files out of the OneDrive folder so local copies remain."
  - q: "What is Files On-Demand and does it reduce CPU usage?"
    a: "Files On-Demand keeps placeholder stubs instead of full local copies, downloading content only when you open it. It sharply reduces sync CPU because fewer local files need hashing, watching, and reconciling — a 200GB cloud library may keep only 5GB locally. Enable it under OneDrive Settings > Sync and backup > Advanced settings. The tradeoff: you need internet for non-downloaded files, fine for archives but not for offline work."
  - q: "Why does OneDrive resync everything after the 24H2 update?"
    a: "Feature updates can reset OneDrive's sync database, change file identity metadata, or toggle backup settings (Documents/Desktop backup) that suddenly queue your entire user profile for upload. The result looks like OneDrive going insane — hours of syncing files that never changed. Let the initial reconciliation finish once (it is usually a one-time event), then apply the selective-sync and On-Demand settings below so it never has that much local state to reconcile again."
---

OneDrive.exe is camped at 20-30% CPU, your fans are spinning, and the little cloud icon in the system tray shows the eternal spinning arrows. On Windows 11 24H2, OneDrive sync storms have become a familiar complaint: the client watches more folders, hashes more files, and sometimes gets stuck re-syncing libraries that never changed.

Sync CPU scales with file count, not file size — so the fix is about reducing what OneDrive watches and how aggressively it works, not about your internet speed. For the broader disk-usage picture this often accompanies, see [disk active time at 100%](/articles/how-to-fix-disk-active-time-100-percent-step-by-step/); for taming what launches at boot generally, [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Huge file counts under sync**: Tens of thousands of small files (photos, node_modules, game mods) mean constant hashing and database churn.

- **Files On-Demand disabled**: Full local copies of everything multiply the files OneDrive must watch and reconcile.

- **High-churn folders synced**: Dev build outputs, downloads, and temp folders change constantly, triggering endless sync cycles.

- **Post-24H2 sync database reset**: Feature updates can invalidate OneDrive's sync state, forcing full re-reconciliation.

- **Backup of Documents/Desktop enabled**: Folder backup silently queues your entire user profile, including app data that changes constantly.

- **Sync conflicts and stuck files**: A handful of un-syncable files (long paths, illegal characters) keep the engine retrying forever.

- **Bandwidth and CPU throttling absent**: Default settings let OneDrive use full CPU and network, starving everything else during big syncs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pause syncing and assess the queue

Stop the storm first, then decide what should actually be syncing.

1. Click the **OneDrive cloud icon** in the system tray > **Pause syncing** > **2 hours** for immediate relief.
2. With sync paused, check CPU: if OneDrive drops to near zero, sync activity (not the app itself) is the cost — proceed to reduce the sync scope.
3. Click the OneDrive icon > **Settings (gear) > View sync problems** to see stuck files and conflicts.
4. Note the pending file count — tens of thousands pending means scope reduction will help enormously; a handful of stuck files means Fix 6 is your answer.
5. Do not unpause until you have applied at least the selective-sync changes below.

### Fix 2: Enable Files On-Demand and selective sync

The two highest-impact settings: fewer local files, fewer watched folders.

1. Open **OneDrive Settings > Sync and backup > Advanced settings** and ensure **Files On-Demand** is turned on.
2. In the same area, use **Choose folders** (selective sync) to uncheck top-level folders you rarely need locally — archives, old projects, media libraries.
3. For folders you keep, right-click them in File Explorer and use **Free up space** to convert full copies back to placeholders.
4. Keep only actively-used working folders as **Always keep on this device**; everything else stays as on-demand stubs.
5. Unpause syncing and watch CPU over the next hour — reduced scope usually cuts sync CPU by more than half.

### Fix 3: Remove high-churn folders from sync

Some folders should never be synced; their churn rate makes sync engines miserable.

1. Move developer build outputs, **node_modules**, and package caches OUT of synced folders — or add them to OneDrive's exclusion via selective sync unchecking.
2. Relocate your **Downloads** folder contents regularly; a Downloads folder with 10,000 installers is a sync tax you pay daily.
3. Check **OneDrive Settings > Sync and backup > Manage backup** — if Documents/Desktop backup is on and dragging in app data, turn it off or curate what lives there.
4. Game mod folders and video render outputs belong on a non-synced drive.
5. After moving folders out, let OneDrive reconcile once (a final busy period), then enjoy the calm.

### Fix 4: Throttle OneDrive's resource usage

OneDrive can be told to use less CPU and network; the defaults are aggressive.

1. In **OneDrive Settings > Sync and backup**, set upload/download rate limits if your connection or CPU is saturated during syncs.
2. Prevent OneDrive from starting with Windows if you sync manually: **Settings > General > uncheck Start OneDrive automatically** — launch it only when you need to sync.
3. In **Task Manager > Details**, you can lower OneDrive.exe's priority as a temporary measure during heavy work sessions (it resets on restart).
4. Schedule big sync sessions: unpause OneDrive when you step away, pause it during focused work — manual sync hygiene beats constant background churn.
5. On laptops, this scheduling also protects battery life, since sync hashing is a meaningful power draw.

### Fix 5: Fix the 24H2-specific sync reset

If the storm started right after the feature update, the sync database likely needs a clean reconciliation.

1. Ensure OneDrive is updated: **Settings > About** — the Store/MSIX version updates independently of Windows.
2. Run the OneDrive reset: press **Win + R**, type **%localappdata%\Microsoft\OneDrive\onedrive.exe /reset**, press Enter, wait 2 minutes, then launch OneDrive again from Start.
3. The reset rebuilds the sync database without deleting files; expect one thorough reconciliation pass afterward.
4. Re-verify **Files On-Demand** and selective sync settings after the reset — resets can revert them.
5. Check **Settings > Windows Update** for OneDrive-related updates; 24H2's early builds had sync bugs fixed in cumulative updates.

### Fix 6: Clear stuck files and sync conflicts

A few poison files can keep the engine at high CPU indefinitely.

1. In **OneDrive Settings > View sync problems**, address each item: rename files with illegal characters (#, %, overly long paths), or move them out of synced folders.
2. For persistent **sync pending** on specific files, copy them out of OneDrive, let sync complete, then copy back in small batches.
3. Check for files open/locked by other apps (Outlook PSTs, databases) — exclude their folders from sync.
4. Look for the **OneDrive - Personal** vs work account confusion: ensure files are syncing to the intended account.
5. After clearing the queue, CPU should fall to idle; if the icon still spins with zero pending files, run the /reset from Fix 5.

### Fix 7: Decide OneDrive's role deliberately

The final option set: keep it lean, pause it strategically, or remove it.

1. If you need sync: keep the lean configuration from Fixes 2-4 and use **Pause syncing** during demanding work — 2/8/24-hour pauses are built for this.
2. To stop OneDrive starting at boot but keep it installed: **Task Manager > Startup apps > Microsoft OneDrive > Disable**.
3. To fully uninstall: **Settings > Apps > Installed apps > Microsoft OneDrive > Uninstall** — first move any files you need out of the OneDrive folder to a non-synced location.
4. After uninstalling, verify your files: check **onedrive.live.com** to confirm cloud copies exist before deleting anything local.
5. Microsoft documents OneDrive controls in the [Windows support hub](https://support.microsoft.com/en-us/windows); whatever you choose, make it deliberate rather than letting a bloated default configuration tax your CPU forever.

## Closing

OneDrive's CPU hunger on 24H2 is almost always a scope problem: too many files watched, high-churn folders synced, or a post-update database reset churning through everything. Shrink what it watches with Files On-Demand and selective sync, evict the churn factories, throttle its resources — and the cloud icon goes back to being a quiet checkmark instead of a spinning CPU tax.
