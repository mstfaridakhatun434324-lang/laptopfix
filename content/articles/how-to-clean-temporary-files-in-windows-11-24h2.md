---
title: "How to Clean Temporary Files in Windows 11 24H2"
slug: how-to-clean-temporary-files-in-windows-11-24h2
date: 2026-09-08
categories: ["performance"]
tags: ["temporary files", "disk cleanup", "windows 11 24h2", "storage"]
description: "Reclaim gigabytes from temp files in Windows 11 24H2: manual cleanup, Storage Sense, and the deep-clean categories most people miss."
thumbnail: "/images/thumbs/how-to-clean-temporary-files-in-windows-11-24h2.webp"
faqs:
  - q: "Where are temporary files stored in Windows 11?"
    a: "The main locations are C:\\Windows\\Temp for system temp files, C:\\Users\\[you]\\AppData\\Local\\Temp for per-user temp files, plus the SoftwareDistribution download cache, thumbnail caches, and delivery optimization files. Disk Cleanup and Storage Sense know all of these locations, which is why the built-in tools beat manual folder-deleting."
  - q: "Is it safe to delete everything in the Temp folder?"
    a: "Mostly yes, with one rule: skip files that are in use. Windows will refuse to delete locked files anyway, showing a 'file in use' prompt — just check 'do this for all current items' and skip them. Never delete the Temp folder itself, only its contents, and close running programs first to minimize locked files."
  - q: "How much space can cleaning temp files actually free?"
    a: "Anywhere from a few hundred megabytes to 20GB or more. Typical laptops hold 2–8GB of cleanable temp data. The biggest wins come right after feature updates (Windows.old and update backups) and on systems that have never been cleaned. Monthly automated cleaning keeps it in the low hundreds of megabytes."
  - q: "Do I still need Disk Cleanup if Storage Sense is on?"
    a: "For day-to-day temp files, Storage Sense is enough. But Disk Cleanup reaches categories Storage Sense handles inconsistently — Windows Update Cleanup, old device driver packages, and delivery optimization files. Running Disk Cleanup monthly alongside Storage Sense covers everything, which is why this guide sets up both."
---

Temporary files are the dust bunnies of Windows: individually tiny, collectively enormous. Every installer extracts to Temp and forgets to clean up. Every update stages gigabytes and leaves the scaffolding behind. Thumbnail caches, shader caches, delivery optimization chunks, error reports — they all accumulate in corners you never look at, until the drive is full and the laptop slows down.

Windows 11 24H2 gives you good tools for this, but they are scattered across Settings, the classic Disk Cleanup, and Task Scheduler. This guide pulls them together: a manual deep clean you can do today, the automated setup that prevents buildup, and the hidden categories that hold the real gigabytes.

## Why this happens

- **Installers never clean up:** Setup programs extract hundreds of megabytes to Temp and leave them when they finish — or crash midway.
- **Windows Update staging:** Updates download, extract, and install in stages, and the staging files linger until a cleanup pass removes them.
- **Rollback data is kept by design:** Feature updates keep the entire previous Windows installation for ten days in case you roll back.
- **Caches regenerate and bloat:** Thumbnail, icon, font, and shader caches grow with use and are never trimmed automatically.
- **Delivery Optimization peer cache:** Update chunks downloaded for sharing with other PCs sit on disk until cleaned.
- **Crash dumps and error reports:** Memory dumps from a single blue screen can be gigabytes, and queued error reports pile up silently.
- **Per-user Temp folders multiply:** Every user account has its own Temp folder, so shared laptops accumulate several copies of the same waste.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what you are carrying

1. Go to **Settings → System → Storage** and wait for the bar to populate, then click **Temporary files**.
2. Windows lists every category with its size — note the biggest three. **Windows Update Cleanup** and **Delivery Optimization Files** are usually the giants.
3. Check the total at the top. Under 1GB means temp files are not your problem; several gigabytes means this guide will pay off immediately.
4. Do not click Remove yet — you will do a more thorough pass with Disk Cleanup in Fix 3.

### Fix 2: Clear the Temp folders manually

1. Press **Win + R**, type `%temp%`, and press Enter. This opens your user's Temp folder.
2. Press **Ctrl + A** to select all, then **Delete**. When Windows warns about files in use, check **Do this for all current items** and click **Skip**.
3. Press **Win + R** again, type `temp` (no percent signs), approve the admin prompt, and repeat the select-all-delete-skip process for the system Temp folder.
4. Empty the Recycle Bin afterward — deleted temp files sit there holding space until you do. If your disk is still pinned at 100% after cleaning, our [100% disk guide](/articles/how-to-fix-disk-active-time-100-percent-youtube/) covers the deeper causes.

### Fix 3: Run the deep Disk Cleanup pass

1. Press **Win + R**, type `cleanmgr`, press Enter, select C:, then click **Clean up system files** and select C: again.
2. Check **Windows Update Cleanup**, **Delivery Optimization Files**, **Device driver packages**, **Temporary files**, **Thumbnails**, and **DirectX Shader Cache**.
3. Click **OK → Delete Files** and let it run — the Windows Update Cleanup portion can take 10–20 minutes on its first run in ages.
4. Restart the laptop when it finishes so Windows rebuilds the caches it needs at healthy sizes.

### Fix 4: Remove Windows.old after feature updates

1. Open File Explorer → **This PC**, right-click C: → **Properties → Disk Cleanup → Clean up system files**.
2. Check **Previous Windows installation(s)** — this is the Windows.old folder, often 15–25GB.
3. Only remove it if you are sure you will not roll back the feature update (you have ten days from the update to decide).
4. Never delete Windows.old by hand in File Explorer — permissions will fight you and you will leave fragments behind. Always use Disk Cleanup.

### Fix 5: Turn on Storage Sense for ongoing maintenance

1. Go to **Settings → System → Storage** and enable **Storage Sense**.
2. Click into its settings: set it to run **Every week**, auto-delete Recycle Bin contents older than **30 days**, and clean the Downloads folder on a schedule you are comfortable with.
3. Enable **Delete previous versions of Windows** so future Windows.old folders vanish automatically after the rollback window.
4. Storage Sense handles the weekly trickle; for the monthly deep categories, set up the automated run described in our [scheduled Disk Cleanup guide](/articles/how-to-schedule-disk-cleanup-in-windows-11-24h2/).

### Fix 6: Clear the caches Disk Cleanup misses

1. **Delivery Optimization:** Settings → Windows Update → Advanced options → Delivery Optimization → **Clear cache** is not a button, so use Disk Cleanup's Delivery Optimization Files category (Fix 3) — it is the supported path.
2. **Microsoft Store cache:** Press **Win + R**, type `wsreset.exe`, and press Enter. A blank Command Prompt window appears for a minute, then the Store opens — the cache is cleared.
3. **Thumbnail cache rebuild:** In Disk Cleanup, checking **Thumbnails** forces a rebuild at a sane size next time you browse folders.
4. Background details on what each category contains are documented on the [Microsoft support site](https://support.microsoft.com/en-us/windows) if you want to verify before deleting.

### Fix 7: Stop the buildup at the source

1. Uninstall programs you no longer use (**Settings → Apps → Installed apps**) — fewer installers means fewer abandoned temp files.
2. If a specific program recreates gigabytes of temp data daily (video editors and some games are notorious), check its settings for a custom temp location and point it at a secondary drive.
3. Keep at least 15% of C: free — Windows cleans and stages updates far more efficiently with breathing room, and low space itself causes slowdowns.
4. Revisit **Settings → System → Storage → Temporary files** monthly for a 30-second sanity check that automation is keeping up.

## Closing

Temp files are not mysterious — they are just neglected. One manual deep clean today, Storage Sense weekly, and Disk Cleanup monthly, and the gigabytes stop accumulating. Your C: drive stays lean, updates install cleanly, and "disk full" becomes a warning you never see again.
