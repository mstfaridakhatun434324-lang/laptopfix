---
title: "How to Clean Temporary Files on Windows 10"
slug: how-to-clean-temporary-files-on-windows-10
date: 2026-09-08
categories: ["performance"]
tags: ["temporary files", "disk cleanup", "windows 10", "storage", "maintenance"]
description: "Free up gigabytes on Windows 10 by cleaning temporary files safely — Disk Cleanup, Storage Sense, manual temp folders, and what to leave alone."
thumbnail: "/images/thumbs/how-to-clean-temporary-files-on-windows-10.webp"
faqs:
  - q: "Is Disk Cleanup still available on Windows 10?"
    a: "Yes. Despite Microsoft promoting Storage Sense as its successor, the classic Disk Cleanup tool (cleanmgr.exe) is fully present and functional in Windows 10, including the 'Clean up system files' mode that reveals Windows Update leftovers and previous installations. It's the deepest built-in cleaner on Windows 10 and the right tool for the big wins like Windows.old removal."
  - q: "Does Windows 10 have Storage Sense?"
    a: "Yes — Windows 10 introduced Storage Sense, and it works much like the Windows 11 version: automatic cleanup of temporary files, Recycle Bin aging, and optional Downloads folder cleanup on a schedule you configure. On Windows 10 it's under Settings → System → Storage. It's less prominent than on Windows 11, which is why many Windows 10 users never turn it on."
  - q: "Can I delete the Windows.old folder on Windows 10?"
    a: "Yes, once you're confident you won't roll back to the previous Windows version — Windows.old is the backup of your old installation kept for ten days after an upgrade. The safe way to remove it is Disk Cleanup's 'Clean up system files' mode (check 'Previous Windows installation(s)'), not manual deletion, which can leave permission problems. It typically frees fifteen to twenty-five gigabytes."
  - q: "How often should I clean temporary files on Windows 10?"
    a: "With Storage Sense enabled on a monthly schedule, manual cleaning becomes a once-or-twice-a-year task. Without automation, every two to three months keeps accumulation under control. The real answer depends on your drive size: on a 128–256GB drive, check quarterly; on larger drives, twice a year is plenty."
---

Windows 10 accumulates temporary files exactly like its successor — update leftovers, delivery optimization caches, thumbnail databases, and the temp folders that programs fill and forget. On older Windows 10 laptops, which often have smaller drives to begin with, this accumulation hits the "mysteriously full disk" wall sooner. The cleanup playbook is nearly identical to Windows 11's, with a few Windows 10-specific notes on where the settings live.

This guide walks the full cleanup on Windows 10: measuring the junk, the deep Disk Cleanup pass, manual temp folder clearing, per-app caches, and the Storage Sense automation that makes it a one-time job. Fifteen minutes now, gigabytes back, and a maintenance habit that runs itself.

## Why this happens

- **Legacy update leftovers:** Years of feature updates leave staged files and Windows.old folders behind.
- **Programs never self-clean:** The temp-folder problem is version-independent — apps litter everywhere.
- **Delivery Optimization sharing:** Windows 10's peer-to-peer update sharing caches gigabytes by default.
- **Smaller stock drives:** Many Windows 10-era laptops shipped with 128–256GB drives that fill fast.
- **Storage Sense never enabled:** The automatic option exists but is buried and off by default.
- **Thumbnail and font caches:** Rebuilt constantly, pruned never.
- **Error reporting archives:** Years of Windows Error Reporting data sitting in ProgramData.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure the junk with Storage settings

Open **Settings → System → Storage**, select the system drive, and let Windows categorize — Temporary files shows the total with a breakdown. Click through to see the components: Windows Update Cleanup, Delivery Optimization Files, Temporary files, Thumbnails. Note the numbers; they decide how aggressive to be. If the total is under a gigabyte and your disk isn't full, temp files aren't your problem — look at real data (apps, documents) instead. If it's multiple gigabytes, continue: the cleanup will be worth it.

1. Open Settings → System → Storage → Temporary files.
2. Note the total and the largest categories.
3. Decide whether temp files are actually your problem.
4. Continue to cleanup if the total is significant.

### Fix 2: Run Disk Cleanup with system files

Search "Disk Cleanup" in the Start menu, select C:, then click "Clean up system files" and reselect C: — this elevated mode reveals the heavy categories: Windows Update Cleanup, Previous Windows installation(s), Delivery Optimization Files, Device driver packages. Check them (leave Downloads and Recycle Bin unchecked unless you're sure), and run. The Previous Windows installation entry alone is often 15–25GB — remove it only once you're settled past the 10-day rollback window and sure the current build is stable. This single pass is usually the biggest space recovery on a long-neglected Windows 10 machine.

1. Run Disk Cleanup → Clean up system files.
2. Check Windows Update Cleanup and Delivery Optimization Files.
3. Remove Previous Windows installation(s) only if rollback isn't needed.
4. Run and record how much space was reclaimed.

### Fix 3: Clear the Temp folders manually

Press Win+R, type `%temp%`, Ctrl+A, Delete — skip files Windows reports as in use. Then do `C:\Windows\Temp` with admin approval. For the update download cache, stop the Windows Update service (services.msc), empty `C:\Windows\SoftwareDistribution\Download`, and restart the service. Also check `C:\Windows\Logs` and `C:\ProgramData\Microsoft\Windows\WER` (error reporting archives) — safe to clear old contents. Manual clearing catches what the automated tools leave, and the "skip in-use" rule keeps it safe. Never delete the folders themselves, only their contents.

1. Empty %temp% and C:\Windows\Temp (skip in-use files).
2. Stop Windows Update service, clear its download cache, restart it.
3. Clear old Windows Logs and error reporting archives.
4. Verify the folders themselves remain intact.

### Fix 4: Clear Windows 10's per-app and thumbnail caches

Windows 10's thumbnail cache lives in `%localappdata%\Microsoft\Windows\Explorer` (thumbcache_*.db) — delete these with Explorer closed via Task Manager, then restart Explorer. Clear browser caches through each browser's settings. Check `%localappdata%` sorted by size for bloated app caches — old Teams, Slack, and Electron apps are notorious gigabyte-scale offenders on Windows 10. Use each app's own cache-clear option where it exists; manual deletion only for folders explicitly named Cache. One forgotten app cache can dwarf all system temp files combined.

1. Delete thumbnail cache files with Explorer closed.
2. Clear each browser's cache via its settings.
3. Hunt bloated app caches in %localappdata% by size.
4. Prefer in-app cache clearing over manual deletion.

### Fix 5: Enable Storage Sense for automatic maintenance

Go to **Settings → System → Storage** and turn on Storage Sense, then click "Configure Storage Sense or run it now": set it to run monthly, delete temporary files apps aren't using, and configure Recycle Bin aging (30 days is sensible). Leave Downloads cleanup off unless you're disciplined about that folder. Storage Sense on Windows 10 is slightly less capable than the Windows 11 version but handles the core job — temp files and update leftovers — automatically. Check back in a month to confirm the Temporary files total stays low. The [scheduling guide](/articles/how-to-schedule-disk-cleanup-on-windows-11/) covers the Task Scheduler alternative for finer control.

1. Turn on Storage Sense in Storage settings.
2. Configure monthly runs and Recycle Bin aging.
3. Keep Downloads cleanup off unless you're certain.
4. Verify temp totals stay low after a month.

### Fix 6: Address real data if the disk is still full

Temp cleaning done but C: still nearly full? The issue is real data, not junk. Check **Settings → System → Storage** for the breakdown by Apps, Documents, and Other — then use a visual tool like WizTree to find the actual giants: old game installs, VM images, video projects, duplicate downloads. Uninstall unused programs via Settings → Apps, move media libraries to external storage, and consider a larger drive if the laptop supports it. Temp maintenance keeps the system healthy; this step keeps it spacious. Microsoft's storage guidance lives in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Identify what's actually consuming space via Storage settings.
2. Map large folders visually with WizTree.
3. Uninstall or relocate the real space hogs.
4. Maintain 15–20% free space as the ongoing target.

## Closing

Windows 10 temp cleanup is the same honest work as on any Windows version: measure, deep-clean with Disk Cleanup's system-files mode, hand-clear the stubborn folders, then automate with Storage Sense. The gigabytes return in one session, and with the schedule on, the slow creep of junk becomes a problem you solved once instead of a chore you dread. Windows 11 users should follow the [Windows 11 temp-cleaning guide](/articles/how-to-clean-temporary-files-in-windows-11-24h2/) for the newer Storage Sense layout.
