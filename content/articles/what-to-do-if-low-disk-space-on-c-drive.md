---
title: "Low Disk Space on C: Drive? Reclaim Gigabytes Safely"
slug: what-to-do-if-low-disk-space-on-c-drive
date: 2026-10-13
categories: ["performance"]
tags: ["low disk space", "c drive full", "free up space", "disk cleanup", "windows 11"]
description: "C: drive full or nearly full? Reclaim tens of gigabytes safely with Disk Cleanup, Storage Sense, and targeted cleanup — without deleting anything important."
thumbnail: "/images/thumbs/what-to-do-if-low-disk-space-on-c-drive.webp"
faqs:
  - q: "How much free space should I keep on the C: drive?"
    a: "Aim for at least 15 to 20 percent of the drive free, or a minimum of 20 to 30 GB on typical 256 to 512 GB drives — whichever is larger. Below about 10 percent free, Windows can't defragment or TRIM effectively, updates may fail, virtual memory gets constrained, and SSD performance degrades. The red drive bar in File Explorer is a genuine warning, not decoration."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you're sure you don't want to roll back the recent Windows update — Windows.old is the previous installation kept for 10 days for rollback purposes. Delete it via Disk Cleanup (Clean up system files > Previous Windows installation(s)), never by manually deleting the folder, which can leave broken permissions. After deletion the rollback option is gone, so wait until the new version proves stable."
  - q: "Why does my C: drive keep filling up by itself?"
    a: "The usual silent fillers are Windows Update working files, growing pagefile and hibernation files, restore points accumulating, app caches (browsers, Spotify, Teams), and the WinSxS component store growing with each update. Delivery Optimization can also cache update files for sharing with other PCs. Storage Sense plus periodic Disk Cleanup handles all of these automatically once configured."
  - q: "Can I just move programs to another drive instead?"
    a: "For Microsoft Store apps, yes — Settings > Apps > Installed apps lets you move supported apps to another drive. For traditional desktop programs, reinstalling to the other drive is the clean method; manually dragging program folders breaks them. Steam, Epic, and other game launchers have built-in library-move features. Moving large games off C: is often the single biggest space win available."
---

That red bar under C: in File Explorer isn't just ugly — a nearly-full system drive makes everything worse. Windows needs breathing room for updates, virtual memory, temporary files, and SSD maintenance; below ~10% free, you get failed updates, mysterious slowdowns, and apps crashing on launch. The good news: most "full" C: drives are 30-50% reclaimable junk — update leftovers, caches, temp files, and forgotten downloads — and the cleanup is safe if you use the right tools in the right order.

This guide walks the cleanup from safest to most aggressive: built-in tools first (Disk Cleanup, Storage Sense), then the big-ticket items (Windows.old, hibernation, restore points), then the judgment calls (what to move, what to uninstall). Nothing here touches your documents, photos, or installed programs' ability to run. For the Windows 10-specific version, see [freeing up disk space on Windows 10](/articles/how-to-free-up-disk-space-on-windows-10/).

## Why this happens

- **Windows Update leftovers**: Each update leaves superseded components and cleanup files behind.
- **Windows.old from feature updates**: A full copy of the previous installation (15-30 GB) kept for rollback.
- **Hibernation file**: `hiberfil.sys` sized at ~40% of RAM — 6+ GB on a 16 GB machine.
- **Restore points accumulating**: System Protection snapshots growing unchecked, especially with the default 10%+ allocation.
- **App and browser caches**: Teams, Spotify, browsers, and creative apps caching gigabytes silently.
- **Delivery Optimization cache**: Update files stored to share with other PCs on your network.
- **WinSxS growth**: The component store growing with every update (cleanable, not deletable manually).
- **User folder sprawl**: Downloads folders with years of installers, and Desktop-as-storage habits.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what's eating the space

Target the big chunks instead of guessing.

1. Open **Settings** > **System** > **Storage** — Windows breaks down usage by category (Apps, Temporary files, System & reserved, Other). Click each for detail.
2. Click **Temporary files** and check the boxes for safe deletions: **Windows Update Cleanup**, **Delivery Optimization Files**, **Temporary files**, **Recycle Bin**, **Thumbnails**, **DirectX Shader Cache**. Note the sizes — Update Cleanup alone is often 5-15 GB.
3. Click **Remove files** and let it work — this is the safest multi-gigabyte cleanup available.
4. For a visual map of everything, the free tool **WizTree** (or WinDirStat) scans the drive in seconds and shows exactly which folders are huge — invaluable for finding that forgotten 40 GB video export or game.
5. Write down your free space before and after each fix — watching the number climb keeps you motivated through the boring parts.

### Fix 2: Run Disk Cleanup as administrator (the deep clean)

The classic tool still finds gigabytes Storage Sense misses.

1. Search Start for **Disk Cleanup**, right-click > **Run as administrator** — the admin mode unlocks system-file categories.
2. Select **C:**, then click **Clean up system files** and select C: again — now check **Windows Update Cleanup**, **Previous Windows installation(s)** (that's Windows.old, 15-30 GB — only if you're past the rollback window and stable), **Device driver packages**, and **Delivery Optimization Files**.
3. Click OK and let it run — Update Cleanup can take 10-20 minutes; that's normal.
4. Repeat for the **More Options** tab > **System Restore and Shadow Copies** > **Clean up** — this removes all but the most recent restore point (see Fix 5 before doing this if you rely on restore points).
5. This single tool routinely reclaims 10-30 GB on neglected systems. For ongoing automation, see [Storage Sense setup](/articles/how-to-free-up-disk-space-on-windows-11/) to keep it clean without thinking about it.

### Fix 3: Shrink the hibernation file or disable hibernation

Hiberfil.sys is pure overhead if you never hibernate.

1. Check the current size: open File Explorer > **View** > **Show** > **Hidden items**, then look at `C:\hiberfil.sys` — on a 16 GB RAM machine it's roughly 6-7 GB.
2. If you use Sleep but never Hibernate: open an elevated Command Prompt and run `powercfg /hibernate off` — this deletes hiberfil.sys entirely and frees the space immediately. (This also disables Fast Startup, which depends on hibernation — only do this if you've decided Fast Startup isn't helping you.)
3. If you want hibernation but smaller: `powercfg /hibernate /size 50` shrinks it to 50% of RAM instead of the default ~75-100%.
4. Verify the space reclaimed in File Explorer or Settings > Storage.
5. Laptops that travel benefit from keeping hibernation (it survives dead batteries; Sleep doesn't) — weigh the gigabytes against your usage. Desktop-replacement laptops that live plugged in can safely drop it.

### Fix 4: Tame System Restore and the pagefile

Two system files that grow without asking.

1. Press **Win + R**, type `SystemPropertiesProtection.exe`, select C:, click **Configure** — note the **Current Usage**. If restore points are eating 20+ GB, drag **Max Usage** down to 5% (or ~10 GB) and click **Delete** to clear old points (keep this only if you don't depend on them — see the warning in Fix 2).
2. For the pagefile: `SystemPropertiesPerformance.exe` > **Advanced** tab > **Virtual memory** > **Change**. If it's **System managed** on a machine with 16+ GB RAM and plenty of free space, leave it — but if C: is critically full and you have another drive, you can move the pagefile there (select C: > **No paging file** > Set; select D: > **System managed size** > Set).
3. Never disable the pagefile entirely — Windows and some applications expect it to exist, and "no pagefile" causes crashes that are mystifying to diagnose.
4. Restart after pagefile changes for them to take effect.
5. These two tweaks together often free 10-20 GB on systems where defaults were left to grow for years.

### Fix 5: Move the big stuff off C:

The structural fix for chronically full drives.

1. **Games first**: Steam > Settings > Storage > add a library folder on D: and move games; Epic and other launchers have similar move features. Games are 50-150 GB each — moving two solves most "full drive" crises permanently.
2. **Store apps**: **Settings** > **Apps** > **Installed apps** > click **...** on large apps > **Move** (only offered for apps that support it).
3. **User folders**: right-click **Documents/Downloads/Pictures** > **Properties** > **Location** tab > **Move** — point them at D:. Do this for Downloads especially; it's where installers go to die.
4. **OneDrive/Dropbox**: if cloud sync folders live on C:, relocate them in the sync client's settings — synced folders quietly consume enormous space.
5. **Uninstall the forgotten**: **Settings** > **Apps** > **Installed apps**, sort by **Size** — the top of that list always contains surprises (old printer suites, trial software, games you finished). Uninstall ruthlessly.

### Fix 6: Automate with Storage Sense and verify

Make "full C:" a once-ever problem.

1. **Settings** > **System** > **Storage** > **Storage Sense** > turn it **On**, then open **Configure cleanup schedules**: set it to run **Every month** (or **During low free disk space**), delete files in Recycle Bin after 30 days, and clean Downloads if you don't use it as an archive.
2. Run **Disk Cleanup** (admin) once more as a final pass, then record your new free-space number.
3. Verify the target: at least 15-20% free or 20-30 GB, whichever is larger. If you're still below that after all six fixes, the drive is genuinely too small for the workload — time to clone to a larger SSD rather than fight physics.
4. Set a calendar reminder to glance at Storage > Temporary files quarterly — five minutes, four times a year, prevents recurrence.
5. Microsoft's storage management guidance in the [Windows support hub](https://support.microsoft.com/en-us/windows) covers Storage Sense policies if you manage multiple machines.

## Closing

A full C: drive is a maintenance problem, not a hardware problem — and the fix is methodical, not scary. Map the usage (Fix 1), run the built-in deep clean (Fix 2), reclaim the system files (Fixes 3-4), move the giants (Fix 5), and automate (Fix 6). Most people recover 20-50 GB in under an hour. Keep Storage Sense on and glance at the red bar's absence with satisfaction — then get back to actually using the laptop.
