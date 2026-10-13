---
title: "How to Fix Low Disk Space on the C: Drive (Windows 11)"
slug: "how-to-fix-low-disk-space-on-c-drive-reddit"
date: "2026-09-18"
categories: ["performance"]
tags: ["low disk space", "c drive full", "disk cleanup", "windows 11"]
description: "C: drive constantly full? Reclaim gigabytes safely with Disk Cleanup, Storage Sense, and the community's favorite space hogs to delete."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-reddit.webp"
faqs:
  - q: "How much free space should I keep on the C drive?"
    a: "Aim for at least 15 to 20 percent free, or 20 to 30 GB on a typical 256 GB drive, whichever is larger. Below 10 percent free, Windows struggles with updates, the page file cannot grow, search indexing stalls, and SSD performance degrades because the controller lacks spare blocks for wear leveling. Treat the red drive bar in File Explorer as a genuine warning, not decoration."
  - q: "What is safe to delete when the C drive is full?"
    a: "Safe targets include the Recycle Bin, temporary files via Disk Cleanup, previous Windows installations after an update settles, delivery optimization files, and the contents of your Downloads folder after review. Never delete the Windows, Program Files, or System32 folders, and do not delete the WinSxS folder directly; use the DISM component cleanup instead."
  - q: "Why does my C drive keep filling up by itself?"
    a: "The usual self-filling culprits are Windows Update staging files, system restore points accumulating without a cap, hibernation file growth, browser caches, and applications like Teams or chat clients storing gigabytes of cache. Storage Sense automates cleanup of several of these, and setting a max usage cap on System Protection stops restore points from growing unbounded."
  - q: "Should I move programs to the D drive?"
    a: "Moving installed desktop programs by hand breaks them. The correct approaches are uninstalling and reinstalling with a custom path on D, using the app's own move feature under Settings for Store apps, or relocating your user folders like Documents and Downloads to D. Steam and other game launchers offer proper library-folder relocation that is fully supported."
---

The red bar in File Explorer is Windows telling you the truth: a full C drive makes everything slower. Updates fail, the page file cannot expand, search indexing chokes, virtual memory thrashes, and SSDs lose performance when they have no spare blocks to work with. On a 128 or 256 GB laptop drive, it does not take much to get there.

The good news is that most full C drives are full of deletable stuff, not your actual data. Previous Windows installations from updates, gigabytes of temporary files, delivery optimization caches, hibernation files on machines that never hibernate, and restore points with no cap are the repeat offenders. This is the cleanup the tech community recommends first, and it is all built into Windows.

This guide works through the safe big wins in order of gigabytes recovered, then sets up automation so the drive stays healthy instead of filling up again next month.

## Why this happens

- **Previous Windows installations:** Windows.old from feature updates can occupy 15 to 25 GB until cleaned up.
- **Uncapped system restore points:** System Protection with no max usage keeps snapshots until the disk is nearly full.
- **Hibernation file on non-hibernating PCs:** hiberfil.sys reserves gigabytes equal to a large fraction of RAM even if you never hibernate.
- **Delivery Optimization cache:** Update files shared with other PCs on your network accumulate in a hidden cache.
- **Temporary and thumbnail caches:** Months of temp files, update leftovers, and thumbnail caches add up to many gigabytes.
- **App caches run wild:** Browsers, Teams, and chat clients each store gigabytes of cache with no built-in limit.
- **User folders on the system drive:** Documents, Downloads, and Desktop default to C and silently consume the system partition.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Disk Cleanup with system files

The built-in Disk Cleanup, run with system files included, is the single biggest safe reclaim for most users.

1. Press Win+R, type cleanmgr, and press Enter.
2. Select the C drive and click OK.
3. Click Clean up system files and select C again.
4. Check Previous Windows installations, Windows Update Cleanup, Temporary files, and Delivery Optimization Files.
5. Click OK and confirm; expect several gigabytes back.

### Fix 2: Turn on Storage Sense for automation

Storage Sense automatically clears temp files and empties the Recycle Bin on a schedule, preventing the slow refill.

1. Open Settings with Win+I, then System, then Storage.
2. Toggle Storage Sense to On.
3. Click Storage Sense to configure its schedule.
4. Set it to run monthly and to delete files in the Recycle Bin after 30 days.
5. Enable cleanup of the Downloads folder only if you are sure you do not hoard files there.

### Fix 3: Cap System Protection storage

Restore points are valuable, but an uncapped allocation can eat tens of gigabytes. A 5 percent cap is plenty.

1. Press Win+R, type sysdm.cpl, and press Enter.
2. Open the System Protection tab and select the C drive.
3. Click Configure.
4. Set Max Usage to around 5 percent with the slider.
5. Click OK; Windows will trim old restore points to fit.

### Fix 4: Disable hibernation if you never use it

If you always shut down or sleep, hiberfil.sys is dead weight equal to a large fraction of your RAM.

1. Open Terminal as administrator with Win+X.
2. Type powercfg /hibernate off and press Enter.
3. Verify hiberfil.sys is gone from the C drive root.
4. This also removes the Hibernate option from the power menu, which is expected.
5. If you miss hibernation later, run powercfg /hibernate on to restore it.

### Fix 5: Move user folders to another drive

Relocating Documents, Downloads, and Desktop to a D drive or external storage permanently moves growth off the system partition.

1. Open File Explorer and right-click your Documents folder, then Properties.
2. Open the Location tab and click Move.
3. Choose or create a folder on the D drive and confirm the move.
4. Repeat for Downloads, Desktop, Pictures, and Videos.
5. Windows handles the redirection; apps keep working normally.

### Fix 6: Find the real hogs with a disk analyzer

If the drive is still tight after cleanup, a visual analyzer shows exactly which folders are eating space.

1. Install the free WizTree or WinDirStat.
2. Run it as administrator and scan the C drive.
3. Look for unexpectedly large folders under AppData or ProgramData.
4. Research any unfamiliar large folder before deleting anything inside it.
5. Uninstall the largest unused programs via Settings, Apps.

### Fix 7: Remove optional features and language packs

Windows ships with optional features and language components many users never touch. Each consumes hundreds of megabytes in the component store.

1. Open Settings, Apps, Optional features.
2. Review the installed list for languages and features you never use.
3. Remove unneeded language packs and handwriting or speech components.
4. Also check Installed apps for manufacturer utilities you never opened.
5. Re-run Disk Cleanup afterward to clear the leftover payloads.

### Fix 8: Remove optional features and language packs

Windows ships with optional features and language components many users never touch. Each consumes hundreds of megabytes in the component store.

1. Open Settings, Apps, Optional features.
2. Review the installed list for languages and features you never use.
3. Remove unneeded language packs and handwriting or speech components.
4. Also check Installed apps for manufacturer utilities you never opened.
5. Re-run Disk Cleanup afterward to clear the leftover payloads.

## Closing

A full C drive is a maintenance problem, not a capacity problem, for most laptop owners. The built-in cleanup tools reclaim the update leftovers, Storage Sense prevents the refill, and moving user folders off C removes the structural cause. Check the drive monthly until you trust the automation. If you are also battling the mysterious WinSxS folder specifically, our guide to [cleaning up WinSxS safely](/articles/how-to-clean-up-winsxs-folder-on-windows-10/) covers that particular space hog in depth. After the cleanup, keep Storage Sense enabled so the drive never fills silently again. For the fastest summary of these steps, see [this low-disk-space checklist](/articles/best-way-to-fix-low-disk-space-on-c-drive/), and Microsoft documents storage management in its [Windows support hub](https://support.microsoft.com/en-us/windows). After the cleanup, keep Storage Sense enabled so the drive never fills silently again. For the fastest summary of these steps, see [this low-disk-space checklist](/articles/best-way-to-fix-low-disk-space-on-c-drive/), and Microsoft documents storage management in its [Windows support hub](https://support.microsoft.com/en-us/windows). Revisit these steps after each feature update, since updates are the fastest way a clean drive fills up again.
