---
title: "How to Clean Temporary Files on Windows 11"
slug: how-to-clean-temporary-files-on-windows-11
date: 2026-09-06
categories: ["performance"]
tags: ["temporary files", "disk cleanup", "windows 11", "storage", "maintenance"]
description: "Reclaim gigabytes by cleaning temporary files on Windows 11 — the safe locations, the right tools, and what never to delete."
thumbnail: "/images/thumbs/how-to-clean-temporary-files-on-windows-11.webp"
faqs:
  - q: "Is it safe to delete everything in the Temp folder?"
    a: "Almost. The contents of C:\\Windows\\Temp and your user %temp% folder are scratch files that programs are supposed to clean up themselves — deleting them is safe. The one exception: files currently in use by running programs can't be deleted anyway (Windows will tell you), so the practical rule is to skip anything that refuses to delete and remove the rest. Never delete the Temp folders themselves, only their contents."
  - q: "How much space can cleaning temporary files actually free?"
    a: "It varies enormously: a well-maintained system might yield a few hundred megabytes, while a laptop that hasn't been cleaned in years can surrender ten to thirty gigabytes — mostly Windows Update leftovers, delivery optimization files, and ancient temp data. The Storage settings page shows the exact number under Temporary files before you commit, so you'll know before you delete anything."
  - q: "What's the difference between Temp files and the Recycle Bin?"
    a: "Temp files are invisible scratch data created by Windows and applications during operation — you never put them there deliberately. The Recycle Bin holds files you personally deleted, kept recoverable just in case. Cleaning temp files is always safe; emptying the Recycle Bin is safe only if you're sure you won't need those deleted files back. Treat them as separate decisions."
  - q: "Do I need a third-party cleaner like CCleaner?"
    a: "No. Windows 11's built-in tools — Storage Sense, Disk Cleanup, and the Storage settings page — clean every safe temp location a third-party cleaner touches, without the bundled offers, upsells, or registry-cleaning risks. Third-party cleaners made sense fifteen years ago; today they're redundant at best and occasionally harmful when their aggressive 'deep clean' modes delete things they shouldn't."
---

Temporary files are the dust bunnies of Windows: every program creates them, almost none clean up after themselves, and over months they accumulate into gigabytes of dead weight. The slowdown is real but indirect — a nearly-full drive makes everything from updates to virtual memory work harder. Cleaning temp files is the highest-return, lowest-risk maintenance you can do on Windows 11.

The good news: Windows 11 has three built-in ways to do it, no third-party cleaner required. This guide covers the safe locations, the right tool for each, and — just as important — what not to delete. Done right, it's fifteen minutes for gigabytes back and a noticeably happier drive.

## Why this happens

- **Programs don't self-clean:** Most applications create temp files and never delete them.
- **Update leftovers accumulate:** Each Windows update stages gigabytes of temporary installation files.
- **Delivery Optimization cache:** Downloaded update packages shared with other PCs pile up silently.
- **Thumbnail and icon caches:** Regenerated constantly, rarely pruned.
- **Browser and app caches:** Every browser and Electron app keeps its own growing cache.
- **Crash dumps and logs:** Error reports and memory dumps saved "just in case," forever.
- **No automatic cleanup configured:** Storage Sense off means nothing ever cleans without manual action.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See what you're dealing with in Storage settings

Open **Settings → System → Storage → Temporary files** and let Windows calculate — it lists every category with its size: Windows Update Cleanup, Delivery Optimization Files, Temporary files, Thumbnails, Recycle Bin, and more. This inventory is your map: check the categories that are genuinely disposable, note the total, and you'll know exactly what the cleanup is worth before deleting anything. Don't check Downloads or Recycle Bin unless you're certain — those hold your files, not system junk. This measured approach beats blindly running cleaners.

1. Open Settings → System → Storage → Temporary files.
2. Review each category and its size.
3. Check only genuinely disposable categories.
4. Click Remove files and note the reclaimed space.

### Fix 2: Run the classic Disk Cleanup for deep categories

The Storage page misses some legacy categories that Disk Cleanup (cleanmgr.exe) still handles. Search "Disk Cleanup" in Start, select C:, then click "Clean up system files" to reveal the full list — including Windows Update Cleanup and Previous Windows installations, which are often the biggest wins (several GB each). Check the safe categories, uncheck anything you're unsure about, and run it. The "Previous Windows installations" entry (Windows.old) is safe to remove once you're settled on the current version and don't plan to roll back — it's often 15–25GB alone.

1. Run Disk Cleanup and click "Clean up system files."
2. Check Windows Update Cleanup and Delivery Optimization Files.
3. Remove Windows.old only if you won't roll back.
4. Run and verify the freed space.

### Fix 3: Manually clear the Temp folders

For the temp files the tools miss, do it by hand: press Win+R, type `%temp%`, select all, delete — skip anything Windows says is in use. Repeat with `C:\Windows\Temp` (you'll need admin approval). Then clear `C:\Windows\SoftwareDistribution\Download` (stop the Windows Update service first via services.msc, restart it after) — this is the update download cache, safe to empty when no update is actively installing. Manual clearing catches the stubborn leftovers automated tools skip, and the "skip in-use files" rule keeps it safe. The [scheduled cleanup guide](/articles/how-to-schedule-disk-cleanup-on-windows-11/) automates all of this going forward.

1. Delete contents of %temp% (skip in-use files).
2. Delete contents of C:\Windows\Temp with admin approval.
3. Stop Windows Update service, clear SoftwareDistribution\Download, restart service.
4. Never delete the Temp folders themselves — only their contents.

### Fix 4: Clear per-app caches that balloon silently

Some apps keep enormous private caches: browsers (clear via browser settings → browsing data), Microsoft Teams and Electron apps (their caches live in %appdata% and can reach gigabytes), and the thumbnail cache (`%localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db`, delete while Explorer is closed). Check `%localappdata%` sorted by size for surprises — one forgotten app cache can outweigh all system temp files combined. Don't go scorched-earth in AppData: only clear folders clearly labeled Cache, and leave anything else alone. When in doubt, use the app's own cache-clearing setting rather than deleting folders manually.

1. Clear browser caches via each browser's settings.
2. Check %localappdata% sorted by size for bloated app caches.
3. Clear only folders explicitly labeled as cache.
4. Prefer each app's built-in cache clearing when available.

### Fix 5: Turn on Storage Sense so it stays clean

Manual cleaning is a one-time win; Storage Sense is the permanent one. Go to **Settings → System → Storage → Storage Sense**, turn it on, and configure it: run monthly, delete temporary files apps aren't using, empty the Recycle Bin of files older than 30 days. Storage Sense then silently maintains everything Fixes 1–4 handled, forever. Verify it's working by checking the Temporary files total a month later — it should stay small instead of climbing. Microsoft documents Storage Sense in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Enable Storage Sense in Storage settings.
2. Set monthly runs and 30-day Recycle Bin cleanup.
3. Enable deletion of unused temporary files.
4. Verify the temp total stays small after a month.

### Fix 6: Handle the "disk still full" aftermath

If temp cleaning freed little and the drive is still nearly full, the problem isn't temp files — it's real data. Use **Settings → System → Storage** to see what's actually consuming space: installed apps, documents, or "Other." Run WinDirStat or WizTree (free, safe) for a visual map of the biggest folders — it often reveals a forgotten VM image, game install, or video project eating 50GB+. Move those to external storage or uninstall them. Temp cleaning was the right first step; this is the honest second step when junk wasn't the issue. For the performance angle of a full drive, see the [Windows 11 speed-up guide](/articles/how-to-speed-up-windows-11-laptop/).

1. Check Storage settings for what's actually consuming space.
2. Run WizTree for a visual map of large folders.
3. Move or uninstall the real space hogs.
4. Keep 15–20% free going forward.

## Closing

Temporary files are a solved problem once you stop doing it manually: inventory with Storage settings, deep-clean with Disk Cleanup, hand-clear the stubborn Temp folders, then let Storage Sense maintain it forever. The gigabytes come back in an afternoon, and with automation on, they never quietly accumulate again.
