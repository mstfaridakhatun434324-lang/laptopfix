---
title: "OneDrive High CPU Usage on an ASUS Laptop: How to Fix It"
slug: how-to-fix-onedrive-high-cpu-usage-on-asus-laptop
date: 2026-09-10
categories: ["performance"]
tags: ["onedrive", "high cpu", "asus laptop", "sync issue", "windows 11"]
description: "OneDrive syncing endlessly and eating CPU on your ASUS laptop? Diagnose sync loops, file conflicts, and settings that cause it — then fix them in order."
thumbnail: "/images/thumbs/how-to-fix-onedrive-high-cpu-usage-on-asus-laptop.webp"
faqs:
  - q: "Why is OneDrive using so much CPU when I'm not doing anything?"
    a: "OneDrive works in the background: indexing files for sync, uploading changes, downloading shared updates, and generating thumbnails. High idle CPU usually means it's stuck — syncing the same files repeatedly due to conflicts, trying to upload files that are locked open, or choking on a corrupted local cache. The fixes below break each of these loops."
  - q: "Is it safe to unlink OneDrive to stop the CPU usage?"
    a: "Unlinking is safe for your files: it stops syncing but leaves both the cloud copies and your local files intact. It's a valid diagnostic step and a reasonable permanent choice if you don't use OneDrive. Just verify at onedrive.com that your important files are in the cloud before unlinking, so nothing exists only on the laptop."
  - q: "Does OneDrive high CPU happen because of ASUS software?"
    a: "Partly. ASUS utilities and updaters write logs and temp files into synced folders (especially Desktop and Documents), and every write triggers OneDrive to re-scan and attempt upload. MyASUS backups pointed at synced folders are a classic trigger. The ASUS-specific steps below address these interactions directly."
  - q: "How long should a normal OneDrive sync take?"
    a: "A healthy sync of a few gigabytes over decent broadband finishes in minutes to an hour, then OneDrive idles at near-zero CPU. If the sync icon has been spinning for days, or CPU stays high with the status stuck on 'Syncing' with no progress in file count, it's not slow — it's stuck, and needs the intervention in this guide."
---

OneDrive is supposed to be invisible infrastructure — files just appear everywhere. But when it goes wrong on an ASUS laptop, it's anything but invisible: OneDrive.exe holding 20–40% CPU for hours, the sync icon spinning endlessly, fans running while the machine sits idle. You're paying a constant performance tax for a sync that never finishes.

The usual causes are sync loops (the same files uploading forever), files that can't sync blocking the queue, and ASUS utilities writing into synced folders. This guide diagnoses which one you have, then fixes it in order — from quick resets to a clean relink.

## Why this happens

- **Sync loops on conflicted files:** Files with sync conflicts get retried indefinitely, burning CPU on every attempt.
- **Locked or open files:** Databases, Outlook PSTs, or app files locked open can't upload, jamming the queue behind them.
- **ASUS utilities writing to synced folders:** MyASUS logs and backups landing in Desktop/Documents trigger constant re-syncs.
- **Corrupted local cache:** A damaged OneDrive cache makes the client re-scan everything repeatedly.
- **Too many files:** Hundreds of thousands of small files (dev folders, photo libraries) overwhelm the sync engine.
- **Files On-Demand churn:** Constant downloading and evicting of cloud files on limited disk space.
- **Network interruptions:** Unstable Wi-Fi causes repeated sync restarts, each one re-scanning from scratch.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the sync status before touching anything

Click the OneDrive cloud icon in the system tray and actually read what it says. "Syncing 1,247 files" that never decreases, specific filenames with error icons, or "Upload blocked" messages tell you exactly where it's stuck. Let it run 30 minutes and check whether the file count moves — a moving count is slow but working; a frozen count is stuck. Note any named files with errors; they're your targets for Fix 2. The [general OneDrive high-CPU guide](/articles/best-way-to-fix-onedrive-high-cpu-usage/) covers the same diagnostic for non-ASUS machines.

1. Click the OneDrive tray icon and read the full status.
2. Note error files and whether the pending count decreases.
3. Wait 30 minutes to distinguish slow from stuck.
4. Record the stuck filenames for the next fix.

### Fix 2: Clear the blocked files from the queue

Files that can't sync — over the size limit, invalid characters, locked open — jam everything behind them. For each error file in the status panel: close the app holding it open (Outlook for PSTs, databases for DB files), rename files with unsupported characters (#, %), or move giant files out of the synced folder. OneDrive processes its queue in order, so a single blocked 50GB file can stall thousands of small files behind it. Clearing blockers often unjams the whole queue within minutes.

1. Identify blocked files from the OneDrive status panel.
2. Close apps locking those files, or move them out of synced folders.
3. Rename files with unsupported characters.
4. Watch the queue drain over the next 15 minutes.

### Fix 3: Pause syncing, then reset OneDrive

If the queue is clear but CPU stays high, the client's local state is likely corrupted. First try the soft reset: right-click the tray icon → **Pause syncing** for 2 hours, then resume — this sometimes breaks a stuck loop. If that fails, do the full reset: press Win+R and run `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset`, which clears the local cache and re-establishes sync without deleting files. Your files stay put; only the sync database rebuilds. Microsoft documents the reset command in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Pause syncing for 2 hours, then resume, as a first attempt.
2. If still stuck, run `onedrive.exe /reset` from Win+R.
3. Wait for OneDrive to restart and rebuild its database.
4. Monitor CPU for an hour after the rebuild.

### Fix 4: Move ASUS utility output out of synced folders

This is the ASUS-specific fix that matters most. Check whether MyASUS, Armoury Crate, or ASUS updaters are writing logs, backups, or temp files into Desktop, Documents, or Pictures — the default synced folders. Every write triggers a re-scan and upload attempt. Redirect those outputs to a non-synced folder (create `C:\ASUS_Data` and point the utilities there), or exclude the specific subfolders from sync via **OneDrive Settings → Account → Choose folders**. Constant-write folders and cloud sync are fundamentally incompatible.

1. Check synced folders for ASUS log/backup/temp output.
2. Redirect utility output to a non-synced folder.
3. Or uncheck those subfolders in Choose folders.
4. Verify sync activity drops in the tray icon.

### Fix 5: Trim what syncs and enable Files On-Demand properly

Fewer synced files means less work, permanently. Go to **OneDrive Settings → Account → Choose folders** and uncheck bulky folders you don't need on this laptop (old photo archives, video projects). Enable **Files On-Demand** so files stay in the cloud until opened — but on a machine with plenty of disk, consider the opposite for your working folders: right-click → **Always keep on this device** for active projects, which stops download-evict churn. Also exclude developer folders with tens of thousands of tiny files (node_modules, .git) — they're sync poison. For machines where you barely use OneDrive, the [disable OneDrive at startup guide](/articles/how-to-disable-onedrive-startup-on-laptop/) removes it from the equation entirely.

1. Open Choose folders and uncheck bulky unneeded folders.
2. Configure Files On-Demand for your disk situation.
3. Exclude dev folders and other tiny-file masses.
4. Let the new sync scope settle for a few hours.

### Fix 6: Unlink and relink as the clean-slate fix

When resets don't hold, unlinking gives you a truly clean slate. **OneDrive Settings → Account → Unlink this PC**, then reboot, then sign back in and relink — choosing a fresh local folder if the old one was messy. Before unlinking, verify your files at onedrive.com so nothing exists only locally. The relink re-downloads the sync database cleanly and re-establishes every file's state. This resolves the deep corruption cases that survive a simple reset, and afterward OneDrive should idle at essentially zero CPU.

1. Verify important files exist at onedrive.com.
2. Unlink this PC in OneDrive Settings → Account.
3. Reboot, then sign in and relink cleanly.
4. Confirm idle CPU stays near zero over a full day.

## Closing

OneDrive high CPU is a queue problem or a corruption problem, and on ASUS laptops there's often an ASUS utility feeding the queue. Read the status, clear the blockers, reset the client, and tame the ASUS output — in that order. Done right, OneDrive goes back to being the invisible infrastructure it was meant to be.
