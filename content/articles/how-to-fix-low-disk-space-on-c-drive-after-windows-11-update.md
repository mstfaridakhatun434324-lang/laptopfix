---
title: "Low Disk Space on C: After a Windows 11 Update? Free It Up"
slug: how-to-fix-low-disk-space-on-c-drive-after-windows-11-update
date: 2026-09-11
categories: ["performance"]
tags: ["low disk space", "c drive", "windows 11 update", "storage", "disk cleanup"]
description: "C: drive full after a Windows 11 update? Reclaim gigabytes from update leftovers, temp files, and hidden space hogs safely."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update.webp"
faqs:
  - q: "Why does a Windows 11 update eat so much disk space?"
    a: "Feature updates stage a full new OS copy (several gigabytes), keep the previous Windows installation in Windows.old for 10 days as a rollback safety net, accumulate update cache files, and expand the WinSxS component store with new component versions. A single feature update can easily consume 15–30 GB. Most of this is temporary or removable — the system just never volunteers to clean it up."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are confident the update is stable — typically after a week or two of normal use. Windows.old exists solely to let you roll back to the previous build within 10 days; after that window, Windows deletes it automatically anyway. Removing it early via Disk Cleanup (never by manual deletion) is safe and often frees 15–25 GB instantly. Only keep it if you are still evaluating whether to roll back."
  - q: "How much free space does Windows 11 need on C:?"
    a: "Aim to keep at least 15–20 GB free at all times, more before feature updates. Below ~10 GB, Windows Update servicing struggles (TiWorker needs scratch space), System Restore cannot create points, hibernation may fail, and the system gets noticeably sluggish as it cannot cache and stage files. Treat 10 GB free as the red line, not the target."
  - q: "Will Disk Cleanup delete anything important?"
    a: "The built-in Disk Cleanup and Storage Sense only offer categories that are safe to remove: temporary files, recycle bin, thumbnails, delivery optimization files, and previous Windows installations. They never touch your documents, installed apps, or personal settings. The one category to consider carefully is Downloads — Cleanup can empty it, so move anything you want to keep out of Downloads first."
---

Nothing announces a Windows 11 feature update quite like the red bar in File Explorer: C: drive suddenly, mysteriously full. Tens of gigabytes vanish overnight — swallowed by the staged update files, the Windows.old rollback copy, an expanded component store, and caches nobody asked you about. The update giveth features and taketh disk space, and on 256 GB laptops it taketh enough to matter.

Reclaiming it is safe and methodical if you use the right tools in the right order. This guide walks the space hogs from biggest to smallest: the rollback copy, update caches, the component store, temp files, and the hidden consumers most cleaners miss — plus how to keep it from happening again. If updates themselves are failing from the cramped quarters, see [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/); for a misbehaving updater, read [fixing the Windows Update troubleshooter](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/).

## Why this happens

- **Windows.old rollback copy retained**: The previous OS build is kept for 10 days as a rollback safety net — typically 15–25 GB.
- **Staged update and download caches**: SoftwareDistribution and Delivery Optimization caches hold gigabytes of downloaded payloads after installing.
- **WinSxS component store growth**: Each update adds new component versions to the side-by-side store; old versions linger until cleaned.
- **Temporary and log file accumulation**: Update processes generate massive temp files, logs, and error reports that are never auto-removed.
- **Hibernation file sized to RAM**: hiberfil.sys reserves disk equal to a large fraction of installed RAM — significant on 16–32 GB machines.
- **System Restore points piling up**: Each update creates restore points, and old ones accumulate against the allocated quota.
- **User data drift onto C:**: Downloads, desktop files, and app caches quietly migrate the biggest personal storage onto the system drive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove Windows.old with Disk Cleanup

The biggest single reclaim, and the safest — when done through the proper tool.

1. Wait until the update has proven stable — a week of normal use is the prudent minimum before removing your rollback path.
2. Open **Disk Cleanup** (search it in Start), select C:, then click **Clean up system files** and re-select C:.
3. Check **Previous Windows installation(s)** — this is the Windows.old entry, often 15–25 GB — plus **Temporary Windows installation files**.
4. Click OK and let it work; large removals take several minutes and the progress bar may appear stuck — let it finish.
5. Verify in File Explorer that C:\Windows.old is gone and note your new free space. Never delete Windows.old manually — permissions break.

### Fix 2: Purge update caches and delivery optimization files

The update's leftover downloads are pure waste once installation succeeds.

1. In the same **Disk Cleanup** > **Clean up system files** pass, check **Windows Update Cleanup** and **Delivery Optimization Files**.
2. Manually clear the cache too: stop the Windows Update service (`net stop wuauserv` elevated), rename `C:\Windows\SoftwareDistribution` to `.old`, restart the service.
3. Go to **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** and clear its cache; consider limiting its bandwidth and cache size.
4. Check **Settings** > **System** > **Storage** > **Temporary files** for additional removable categories Disk Cleanup missed.
5. Re-check free space — update caches commonly yield another 3–8 GB on post-feature-update systems.

### Fix 3: Slim the WinSxS component store

The component store only grows; scheduled cleanup is the sanctioned way to shrink it.

1. Open an elevated terminal and run `DISM /Online /Cleanup-Image /AnalyzeComponentStore` to see the reclaimable size.
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup` for the safe cleanup pass — this takes a while; let it complete.
3. Only if you are certain you will never uninstall updates or remove roles, add `/ResetBase` — this is irreversible, so weigh it carefully.
4. Never delete WinSxS files manually — the store uses hard links and manual deletion corrupts servicing.
5. Verify with a second AnalyzeComponentStore run; the reclaimable figure should have collapsed. Microsoft documents these tools at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 4: Enable and configure Storage Sense

Automate the janitorial work so the drive never gets this full again.

1. Go to **Settings** > **System** > **Storage** > **Storage Sense** and toggle it **On**.
2. Click into its settings: set temporary file cleanup to run **Every month**, and recycle bin auto-empty to **30 days** (or 14 if you are disciplined).
3. Enable **Delete files in my Downloads folder if they have been there for over** 60 days — only after moving anything precious out of Downloads.
4. Turn on **OneDrive Files On-Demand** cleanup so unused cloud files revert to online-only placeholders automatically.
5. Run Storage Sense manually once via **Run Storage Sense now** to feel the immediate effect.

### Fix 5: Shrink hibernation and pagefile reservations

Two hidden giants: hiberfil.sys and pagefile.sys reserve gigabytes most users never think about.

1. Check their size: open an elevated terminal and look at C: root with `dir /a:h C:\` — hiberfil.sys and pagefile.sys are usually the largest files.
2. If you never hibernate, run `powercfg /h off` to delete hiberfil.sys entirely (frees RAM-sized space); use `powercfg /h /type reduced` for a smaller hybrid.
3. For the pagefile: **System** > **About** > **Advanced system settings** > **Performance Settings** > **Advanced** > **Virtual memory** — keep it **System managed** on small drives, or set a modest custom range (e.g., 2–4 GB) if RAM is 16 GB+.
4. Do not disable the pagefile entirely — Windows and many apps expect it to exist.
5. Reboot after changes and confirm the new free space; these two files alone can free 8–20 GB.

### Fix 6: Find the hidden hogs with a disk analyzer

When the standard cleanups do not explain the usage, visualize it.

1. Install a trusted disk-space visualizer (WizTree is fast and free) and scan C: as administrator.
2. Look for the unexpected giants: forgotten VM images, game installs, phone backups, runaway log folders, duplicate downloads.
3. Check `C:\Users\<you>\AppData` — app caches (browsers, Electron apps, installers) hide gigabytes here; clear them from within the apps, not by deleting blindly.
4. Move large personal media and archives to a secondary drive, external disk, or cloud — C: is for the system and apps.
5. Uninstall large unused programs from **Settings** > **Apps** sorted by size — be honest about the games you finished in 2023.

### Fix 7: Prevent the next update from filling the drive

Make the next feature update a non-event for your free space.

1. Keep a standing 20 GB buffer on C: — treat it as untouchable, not as usable space.
2. Before each feature update, run Disk Cleanup's system-files pass and Storage Sense manually to start from the cleanest state.
3. Move your user folders (Documents, Downloads, Pictures) to a secondary drive via folder **Properties** > **Location** tab, if you have one.
4. Consider a larger SSD at the next upgrade opportunity — 256 GB is simply tight for a modern Windows 11 machine's lifecycle.
5. After each future update, repeat Fix 1 within two weeks: remove Windows.old once stability is confirmed, every time.

## Closing

A full C: drive after a Windows 11 update is not a mystery — it is the itemized bill for the update's safety nets and staging areas, and almost all of it is collectible. Windows.old, update caches, and the component store hand back tens of gigabytes through the proper tools, and Storage Sense keeps them from piling up again. The red bar in File Explorer is a to-do list, not a verdict.
