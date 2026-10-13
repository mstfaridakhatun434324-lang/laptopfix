---
title: "Fix OneDrive High CPU Usage in Windows 11 24H2"
slug: "how-to-fix-onedrive-high-cpu-usage-in-windows-11-24h2"
date: "2026-09-12"
categories: ["performance"]
tags: ["onedrive high cpu", "windows 11 24h2", "onedrive sync", "cpu usage", "cloud sync"]
description: "OneDrive syncing at 100% CPU in Windows 11 24H2? Diagnose the sync loop and apply these fixes to calm OneDrive down."
thumbnail: "/images/thumbs/how-to-fix-onedrive-high-cpu-usage-in-windows-11-24h2.webp"
faqs:
  - q: "Why is OneDrive using so much CPU in Windows 11 24H2?"
    a: "The 24H2 update re-registers OneDrive's sync engine and often triggers a full re-scan of every synced folder. Large file counts, sync conflicts, corrupted cache, or a handful of constantly-changing files (like Outlook PSTs or database files) keep the sync engine in a permanent high-CPU loop instead of settling to idle."
  - q: "Will pausing OneDrive sync delete my files?"
    a: "No. Pausing only stops synchronization temporarily; all files remain both locally and in the cloud exactly as they are. It is a safe diagnostic step. When you resume, OneDrive picks up where it left off and syncs any changes made during the pause."
  - q: "Should I unlink OneDrive to fix high CPU?"
    a: "Unlinking is a valid troubleshooting step, not a deletion — your cloud files stay in OneDrive online and local copies remain on disk. Re-linking rebuilds the sync database from scratch, which fixes corruption-based CPU loops. Only do this after trying pause, selective sync, and cache reset, since re-linking a large library takes time."
  - q: "Does Files On-Demand reduce OneDrive CPU usage?"
    a: "Yes, significantly for large libraries. With Files On-Demand, files stay as cloud placeholders until opened, so the sync engine tracks metadata instead of hashing gigabytes of file contents. Enabling it is one of the most effective fixes for OneDrive CPU loops on laptops with big synced folders."
---

OneDrive is supposed to be invisible: a quiet background sync you never think about. In Windows 11 24H2 it has developed a habit of being anything but — **OneDrive.exe** pinning a CPU core at 100% for hours, fans roaring, battery draining, long after any plausible sync should have finished. The 24H2 update is a common trigger because it re-registers the sync engine, which kicks off a full re-scan of your entire synced library.

The key insight for diagnosing OneDrive CPU problems is that legitimate syncing and broken syncing look identical in Task Manager — both show high CPU. The difference is progress: legitimate syncing shows file counts changing and eventually finishes; a broken sync spins forever on the same files. This guide teaches you to tell them apart, then fixes the broken cases in order of increasing disruptiveness.

A note on expectations: if you just added 50 GB to OneDrive or just installed 24H2, give it time — initial syncs and post-update re-scans are genuinely CPU-heavy and can take hours on large libraries. Only troubleshoot when the load never ends.

## Why this happens

- **Post-24H2 full re-scan:** The update re-registers the sync engine, forcing a hash-and-compare pass over every synced file.
- **Sync conflicts or stuck files:** A file that cannot upload (bad name, permission issue, 0-byte lock) retries forever in a tight loop.
- **Corrupted sync cache:** A damaged local sync database makes the engine re-verify files it already synced, repeatedly.
- **Constantly-changing files:** Outlook PST/OST files, databases, or VM images change continuously, re-triggering sync on every write.
- **Huge file counts:** Tens of thousands of small files multiply the hashing and bookkeeping work per sync cycle.
- **Files On-Demand disabled:** With full local copies of everything, the engine hashes gigabytes instead of tracking placeholders.
- **Antivirus scanning synced files:** Real-time protection re-scans every file OneDrive touches, doubling the I/O and CPU.
- **Multiple accounts syncing:** Personal plus work/school accounts double the sync engines and their overhead.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check sync status and distinguish syncing from stuck

Click the OneDrive cloud icon in the system tray and read the status. "Syncing X files" with changing counts and visible progress is legitimate work — let it finish, preferably plugged in. "Syncing" with the same file count for hours, or an error badge on specific files, means stuck. Click the status to see which files are problematic; files with sync errors are your prime suspects. Do not apply any fix until you have made this distinction — interrupting a legitimate large sync just restarts it. For the general post-update settling picture, see our [post-24H2 slowdown guide](/articles/what-to-do-if-laptop-slow-after-windows-11-24h2-update/).

1. Click the OneDrive tray icon and read the sync status.
2. Watch for 10 minutes: changing file counts = working; frozen counts = stuck.
3. Note any files flagged with sync errors.
4. Only proceed if the sync is genuinely stuck, not merely slow.

### Fix 2: Pause syncing to confirm OneDrive is the cause

Pause syncing for 2 hours from the tray menu and watch CPU. If OneDrive.exe drops to zero and total system CPU normalizes, you have confirmed the diagnosis and bought yourself a quiet window to apply the deeper fixes. This is purely diagnostic and fully reversible — resume syncing afterward and the queue picks up where it left off. If CPU stays high with sync paused, something else is the problem and OneDrive is a bystander.

1. Right-click the OneDrive tray icon > **Pause syncing** > **2 hours**.
2. Watch Task Manager for 5 minutes.
3. If CPU normalizes, OneDrive is confirmed as the cause.
4. Resume syncing before applying the remaining fixes.

### Fix 3: Enable Files On-Demand and use selective sync

Two settings multiply OneDrive's efficiency on large libraries. **Files On-Demand** keeps unopened files as cloud placeholders so the engine tracks metadata instead of hashing gigabytes. **Selective sync** (Choose folders) removes folders you do not need locally from the sync set entirely. Together they can cut the sync engine's workload by an order of magnitude. Apply both, then restart OneDrive and observe — this resolves a large share of persistent CPU loops without touching the sync database.

1. Open OneDrive **Settings > Sync and backup**.
2. Ensure **Files On-Demand** is turned on.
3. Click **Manage backup / Choose folders** and deselect folders you do not need locally.
4. Restart OneDrive and monitor CPU for 30 minutes.

### Fix 4: Remove constantly-changing files from the sync set

Outlook data files (PST/OST), virtual machine disks, database files, and active project caches change on every write, and each change re-triggers hashing and upload attempts — a permanent CPU treadmill. Move these out of synced folders: relocate your Outlook data file via the Mail control panel, and keep VMs and databases in an unsynced directory. This is not a OneDrive bug; no sync engine can efficiently track files that change constantly. One relocated PST has fixed more OneDrive CPU complaints than any other single change I have seen.

1. Identify constantly-changing files in synced folders (PST/OST, VHDX, MDB/DB).
2. Move them to a folder outside OneDrive's sync scope.
3. For Outlook: relocate the data file in **Control Panel > Mail > Data Files**.
4. Restart OneDrive and verify the CPU loop ends.

### Fix 5: Reset OneDrive's sync cache

When the local sync database is corrupted, the engine re-verifies already-synced files endlessly. The built-in reset command (`OneDrive.exe /reset`) clears the cache and rebuilds it without touching your files — local copies stay, cloud copies stay, only the bookkeeping is rebuilt. OneDrive restarts automatically after a reset and performs a fresh scan, which is CPU-heavy for a while but then settles. This is the standard Microsoft-recommended repair for stuck sync, documented on the official [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Press **Win + R** and run `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset`.
2. Wait 2 minutes; if OneDrive does not restart, launch it manually.
3. Allow the fresh scan to complete (plugged in, be patient).
4. Verify CPU settles to near-zero when idle afterward.

### Fix 6: Unlink and re-link the PC

If the reset does not break the loop, the sync relationship itself may be damaged. Unlinking the PC (Settings > Account > Unlink this PC) stops all sync without deleting anything — your files remain in the cloud and the local copies stay on disk. Then sign back in and let OneDrive re-establish sync fresh. For large libraries this takes time, so do it when you can leave the laptop plugged in for a few hours. This is the deepest software repair short of reinstalling OneDrive, and it resolves corruption the reset cannot. A related post-update OneDrive variant is covered in our [OneDrive CPU after-update guide](/articles/how-to-fix-onedrive-high-cpu-usage-after-windows-11-update/).

1. Open OneDrive **Settings > Account > Unlink this PC** and confirm.
2. Restart the laptop.
3. Open OneDrive and sign back in with your Microsoft account.
4. Let the fresh sync complete fully before judging CPU.

### Fix 7: Reinstall OneDrive as a last resort

If unlinking fails, the OneDrive installation itself may be damaged — particularly after the 24H2 re-registration. Uninstall OneDrive from **Settings > Apps**, restart, then download the latest installer from Microsoft and reinstall. Your cloud files are untouched; after signing in, choose your sync folders carefully (apply the Files On-Demand and selective-sync lessons from Fix 3 from the start). A clean install with a lean folder selection gives the sync engine the smallest possible job.

1. Uninstall OneDrive via **Settings > Apps > Installed apps**.
2. Restart the laptop.
3. Download and install the latest OneDrive from Microsoft.
4. Sign in, enable Files On-Demand, and select only needed folders.

## Closing

OneDrive high CPU in 24H2 is usually a stuck sync rather than a heavy sync — and stuck syncs have a clear repair ladder: confirm it is stuck, lighten the sync set with Files On-Demand and selective sync, evict constantly-changing files, then reset, unlink, or reinstall the engine. Work the ladder in order and the fans go quiet.
