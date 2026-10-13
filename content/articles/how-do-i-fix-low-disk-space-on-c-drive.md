---
title: "Low Disk Space on the C Drive: How Do I Fix It Permanently?"
slug: how-do-i-fix-low-disk-space-on-c-drive
date: 2026-09-22
categories: ["performance"]
tags: ["low disk space c drive", "c drive full", "free up disk space", "windows 11 storage", "troubleshooting"]
description: "C: drive full on Windows 11? Learn how to reclaim gigabytes safely and stop low disk space warnings from coming back."
thumbnail: "/images/thumbs/how-do-i-fix-low-disk-space-on-c-drive.webp"
faqs:
  - q: "How much free space should I keep on the C: drive?"
    a: "Aim for at least 15 to 20 percent of the drive free — on a 512 GB SSD that is roughly 75 to 100 GB. Below 10 percent, Windows cannot defragment, create restore points, or install updates reliably, and SSD performance degrades because the controller lacks spare blocks. Treat 20 GB free as the emergency floor, not the target."
  - q: "Is it safe to delete everything in the Temp folder?"
    a: "Yes, with the laptop restarted first and no programs running. Files in `C:\\Windows\\Temp` and your user Temp folder are by definition disposable; Windows recreates what it needs. Use Disk Cleanup rather than manual deletion when possible, and skip any file Windows says is in use — it is protecting an active process."
  - q: "Why does my C: drive fill up again after I clean it?"
    a: "Something is writing continuously: runaway log files, a stuck Windows Update cache, hibernation and page files sized for large RAM, or an app dumping data into AppData. Cleaning without finding the writer is mopping without fixing the leak. Use a disk analyzer to find which folder grows between cleanups, then fix the source."
  - q: "Can a full C: drive actually slow down my laptop?"
    a: "Absolutely. Windows needs free space for the page file, temporary files, update staging, and search indexing. A nearly full drive also cripples SSD write performance since the controller has fewer empty blocks to work with. Many 'my laptop got slow' cases are really 'my C: drive hit zero bytes free' cases."
---

The red bar in File Explorer is Windows waving a flag: your **C: drive** is nearly full, and everything from updates to app installs is about to start failing. On modern laptops the C: drive fills quietly — Windows Update backups, hibernation files, temp data, and app caches accumulate for months until one day there is no room left to breathe.

Fixing it permanently means two jobs, not one: reclaim space now, and stop the leak that filled it. The quick wins (Disk Cleanup, Storage Sense, moving user folders) recover gigabytes in an afternoon. The lasting fix is identifying what keeps growing — old update backups, a bloated WinSxS folder, or an app writing logs — and putting it on a diet.

This guide covers both. You will free space safely without deleting anything Windows needs, then set up automatic maintenance so the red bar never comes back. For a broader cleanup checklist beyond the C: drive, the [free up disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) pairs well with these steps.

## Why this happens

- **Windows Update backup files:** Every feature update keeps a copy of the old Windows installation (Windows.old) plus update backups, often 15–30 GB that linger for weeks.
- **Hibernation and page files:** Hiberfil.sys can equal 40% of your RAM and pagefile.sys several more gigabytes — huge on laptops with 16–32 GB of memory.
- **Bloated WinSxS component store:** The servicing store grows with every update; without periodic cleanup it can exceed 10 GB of superseded components.
- **App caches and temp data:** Browsers, installers, thumbnail caches, and delivery-optimization files accumulate gigabytes of disposable data.
- **Runaway logs or stuck downloads:** A crashing app writing logs in a loop or a stuck update cache can silently consume tens of gigabytes.
- **User files defaulting to C::** Documents, Downloads, and Desktop all live on C: by default and grow unchecked for years.
- **Restore points and shadow copies:** System protection can reserve up to 10% of the drive for restore points that pile up unnoticed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Disk Cleanup as administrator for the big wins

The built-in Disk Cleanup, run elevated, is the safest first pass — it targets exactly the categories Windows knows are disposable, including previous Windows installations and update backups that Settings alone sometimes misses. On a laptop that has been through a feature update, this one tool routinely recovers 15–30 GB in minutes. Run it before anything manual.

1. Search "Disk Cleanup", right-click it, and choose Run as administrator.
2. Select C:, then click "Clean up system files" and select C: again.
3. Check Previous Windows installation(s), Windows Update Cleanup, and Temporary files.
4. Click OK, confirm, and let it finish — do not interrupt it.

### Fix 2: Turn on Storage Sense and empty the recycle bin properly

Storage Sense is Windows built-in janitor: it auto-deletes temp files, empties the recycle bin on a schedule, and clears Downloads files older than a chosen age. Most users have it off by default, which is why the leak never stops. Enable it with aggressive-but-safe settings and it prevents the next fill-up without you thinking about it. For a full settings walkthrough, see the [step-by-step low disk space guide](/articles/how-to-fix-low-disk-space-on-c-drive-step-by-step/).

1. Open Settings → System → Storage and turn on Storage Sense.
2. Click Storage Sense and set it to run weekly, deleting recycle bin files older than 30 days.
3. Set Downloads cleanup to 60 days only if you do not store important files there.
4. Run it once manually with "Clean now" to get the immediate benefit.

### Fix 3: Move user folders and large apps off C:

Documents, Pictures, Videos, and Downloads do not have to live on C:. If your laptop has a second drive or partition, relocate these folders via each folder Properties → Location tab — Windows updates all references automatically. Also move large games and apps in Settings → Apps → Installed apps where the Move option appears. This is the structural fix for users whose files, not Windows, fill the drive.

1. Right-click Documents → Properties → Location → Move, and choose a folder on the other drive.
2. Repeat for Downloads, Pictures, Videos, and Desktop.
3. In Settings → Apps, move large movable apps to the second drive.
4. Verify the old locations are empty before deleting anything manually.

### Fix 4: Shrink the hibernation and page files if RAM is large

On a 16 GB laptop, hiberfil.sys alone can eat 6–7 GB. If you never use hibernation (as opposed to sleep), disabling it reclaims that space instantly with one command. The page file can also be capped sensibly rather than system-managed on machines with plenty of RAM — but never disable it entirely, or crashes and out-of-memory errors follow. Microsoft documents these trade-offs in [Windows support](https://support.microsoft.com/en-us/windows).

1. Open Terminal as administrator and run `powercfg /hibernate off` to remove hiberfil.sys.
2. For the page file: System → Advanced system settings → Performance Settings → Advanced → Virtual memory.
3. Set a custom size (e.g. 4096–8192 MB on 16 GB RAM machines) instead of system-managed.
4. Restart and confirm the freed space in File Explorer.

### Fix 5: Clean the WinSxS store and delivery optimization cache

The component store cannot be deleted manually — doing so breaks servicing — but Windows can compact it safely on command. The DISM StartComponentCleanup task removes superseded update components, often freeing several gigabytes. Pair it with clearing the Delivery Optimization cache, which stores update files shared with other PCs on your network and can balloon unnoticed.

1. Run `DISM /Online /Cleanup-Image /StartComponentCleanup` in an elevated prompt.
2. Then run `DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase` (irreversible — only on a stable system).
3. In Settings → Windows Update → Advanced → Delivery Optimization, clear the cache.
4. Consider turning off "Allow downloads from other PCs" to stop re-accumulation.

### Fix 6: Find the real leak with a disk analyzer

If space vanishes again within weeks, stop cleaning blindly and find the writer. Tools like WinDirStat or WizTree scan the drive and show exactly which folders are biggest; run one now and again in two weeks, and the folder that grew is your leak. Common finds: a game writing crash dumps, an app log folder, or a stuck installer cache. Fix the program, not just the symptom.

1. Download WizTree (portable, fast) and scan the C: drive.
2. Note the top five folders by size and their exact paths.
3. Re-scan in two weeks; the folder that grew fastest is the leak.
4. Address the source: update, reconfigure, or uninstall the offending app.

### Fix 7: Cap restore points and run a final verification

System Protection silently reserves disk for restore points; on a space-starved drive, cap it. Set max usage to 3–5% of the drive and delete all but the latest restore point — one recent point is enough for rollback purposes. Finish by confirming at least 15% free space and re-running Windows Update, which is the ultimate test that the drive can now service itself.

1. Open System Protection settings for C: and click Configure.
2. Set max disk space usage to 3–5% and delete all but the most recent point.
3. Confirm 15%+ free space in File Explorer.
4. Run Windows Update to verify updates can now stage and install.

## Closing

Low disk space on C: is a maintenance problem, not a mystery: update backups, hibernation files, caches, and growing user folders fill the drive on a predictable schedule. Reclaim space with elevated Disk Cleanup, move what does not belong on C:, automate with Storage Sense, and hunt the leak with a disk analyzer if it refills. Do that, and the red bar stays gone.
