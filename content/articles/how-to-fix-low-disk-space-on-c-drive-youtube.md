---
title: "How to Fix Low Disk Space on the C: Drive (Reclaim Gigabytes)"
slug: how-to-fix-low-disk-space-on-c-drive-youtube
date: 2026-09-06
categories: ["performance"]
tags: ["low disk space", "c drive", "disk cleanup", "storage", "windows 11"]
description: "C: drive full? Reclaim gigabytes safely with Disk Cleanup, Storage Sense, and targeted large-file removal — without deleting anything important."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-youtube.webp"
faqs:
  - q: "How much free space should I keep on the C: drive?"
    a: "Aim for at least 15–20% of the drive free — on a 512 GB SSD, that's roughly 75–100 GB. Below 10% free, Windows can't manage the pagefile, updates fail, SSD performance degrades as garbage collection struggles, and temp-file operations start failing. The 'low disk space' warning itself appears around 10% on most configurations."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you're sure you don't want to roll back the last feature update. Windows.old is the previous Windows installation kept for 10 days for rollback purposes. Delete it via Disk Cleanup (select 'Previous Windows installation(s)') rather than deleting the folder manually — the proper tool also cleans associated metadata. It typically frees 15–30 GB."
  - q: "What is taking up all my disk space and how do I find it?"
    a: "Use Settings > System > Storage to see a categorized breakdown (apps, temporary files, system). For the full picture including hidden folders, a visual tool like WinDirStat or WizTree maps the entire drive and shows exactly which folders are huge. Common surprises: the SoftwareDistribution update cache, hibernation file, pagefile, game launchers, and forgotten downloads."
  - q: "Can I move programs from C: to another drive?"
    a: "Some — Settings > Apps lets you move Microsoft Store apps to another drive, and many game launchers (Steam, Epic) support moving game libraries. Traditional desktop programs generally can't be moved after installation; they must be uninstalled and reinstalled to the new location. Moving program folders manually breaks registry paths and shortcuts."
---

The red bar on the C: drive is Windows' way of saying the walls are closing in. Updates start failing, the system slows down, apps crash saving files, and eventually Windows itself can't function — all because the drive that hosts the operating system ran out of room. The fix isn't mysterious, but the order matters: safe system cleanups first, then your own large files, then structural changes.

Think of it in three buckets: Windows' own junk (update leftovers, temp files, old installs — safe to remove with built-in tools), your forgotten files (downloads, installers, videos — safe once identified), and structural fixes (moving data, extending the partition). For the Acer-specific variant see [low disk space on Acer laptops](/articles/how-to-fix-low-disk-space-on-c-drive-on-acer-laptop/); for checking the drive's health while you're at it see [checking for disk errors](/articles/how-to-check-disk-for-errors-in-windows-11-24h2/).

## Why this happens

- **Windows Update leftovers**: Staged updates, cleanup caches, and Windows.old from feature upgrades — often 20–40 GB.
- **Hibernation and pagefile**: hiberfil.sys (up to 40% of RAM) and pagefile.sys consuming fixed multi-GB chunks.
- **Temp file accumulation**: App caches, installer leftovers, and logs that nothing ever cleans.
- **Forgotten downloads and installers**: The Downloads folder as a multi-GB archive of installers you'll never run again.
- **Game and app libraries**: Launchers defaulting to C: for tens of gigabytes of games.
- **System Restore points**: Restore data growing unchecked on the system drive.
- **OneDrive/Dropbox local copies**: Cloud files synced locally "just in case," duplicating cloud storage on disk.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what's eating the space

Measure before deleting.

1. Go to **Settings** > **System** > **Storage** and wait for the breakdown — note the sizes of **Temporary files**, **Apps & features**, and **System & reserved**.
2. Click **Temporary files** — Windows itemizes what's safe to remove and the total is often shocking (10–30 GB).
3. For the full map including hidden folders, install **WizTree** (fast, free) and scan C: — it shows every folder by size in seconds. The visual treemap instantly reveals the hogs.
4. Common revelations: `C:\Windows\SoftwareDistribution` (update cache), `$Windows.~BT` (staging), `C:\Users\<you>\AppData` (app caches), and game folders under Program Files.
5. Write down the top 5 space hogs — this list drives every step below.

### Fix 2: Run Disk Cleanup as administrator

The safe, official first pass.

1. Press **Win+R**, type `cleanmgr.exe`, and when prompted choose **C:** — then click **Clean up system files** and choose C: again (the second scan finds the big system categories).
2. Check: **Windows Update Cleanup**, **Delivery Optimization Files**, **Device driver packages**, **Temporary files**, **Thumbnails** — and **Previous Windows installation(s)** if you're past wanting a rollback.
3. Click OK and let it run — the Windows Update Cleanup phase alone can take 20+ minutes on neglected systems. Don't interrupt it.
4. Typical yield: 5–25 GB. Re-check free space in File Explorer afterward.
5. If "Previous Windows installation(s)" doesn't appear, you're within the 10-day rollback window or it was already cleaned — check again after the next feature update.

### Fix 3: Turn on Storage Sense for ongoing maintenance

Automate so this never happens again.

1. Go to **Settings** > **System** > **Storage** > **Storage Sense** and toggle it **On**.
2. Configure it: run **Every week**, delete temp files unused apps leave, empty the Recycle Bin after 30 days, and clean the Downloads folder after 60 days (only if you don't use Downloads as storage — set to **Never** if you do).
3. Click **Run Storage Sense now** for an immediate cleanup pass.
4. Storage Sense won't fix a crisis alone, but it prevents the slow re-accumulation that causes the next crisis.
5. Pair it with the habit from Fix 1: glance at **Settings** > **System** > **Storage** monthly.

### Fix 4: Clear your own large files

Your files, your decisions — but be systematic.

1. Open the Downloads folder, sort by **Size**, and delete installers for software you already installed — they're re-downloadable and often gigabytes each.
2. Hunt video files: search File Explorer for `*.mp4`, `*.mkv`, `*.mov` sorted by size — move keepers to an external drive or second partition, delete the rest.
3. Check `Documents` and `Desktop` for forgotten large archives, ISOs, and disk images.
4. Empty the Recycle Bin (deleted files still occupy space until you do) — then verify the space actually freed.
5. For cloud-synced folders (OneDrive), right-click heavy folders > **Free up space** to make them online-only — the files stay accessible but stop occupying local disk.

### Fix 5: Move apps and games off C:

Relocate the legitimate giants.

1. **Settings** > **Apps** > **Installed apps** — Microsoft Store apps often show a **Move** option; relocate the big ones to another drive.
2. **Steam**: **Settings** > **Storage** > add a library folder on another drive, then move games via **Properties** > **Installed Files** > **Move install folder**.
3. **Epic Games**: no built-in move — uninstall and reinstall choosing the new location (your saves are cloud-synced).
4. For traditional desktop apps, uninstall from C: and reinstall selecting the other drive during setup (choose **Custom install** when offered).
5. Never drag program folders between drives manually — registry paths, services, and shortcuts all break.

### Fix 6: Trim Windows' reserved space

Reclaim the system's own allocations.

1. **Hibernation**: if you never hibernate, run `powercfg /h off` in an elevated Command Prompt — this deletes hiberfil.sys, freeing up to 40% of your RAM size (6+ GB on 16 GB systems). Note: this also disables Fast Startup.
2. **System Restore**: `sysdm.cpl` > **System Protection** > **Configure** — reduce **Max Usage** to 5% or delete old restore points (keep at least one recent).
3. **Pagefile**: only touch this if it's abnormally large — generally leave it system-managed (see our virtual memory guide).
4. Check **Delivery Optimization**: **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** — limit its cache, which can hoard gigabytes of update data for peer sharing.
5. Microsoft documents these storage tools at [Windows support](https://support.microsoft.com/en-us/windows) if you want the official details.

### Fix 7: Structural fixes for chronic cases

When cleanup isn't enough because the drive is just small.

1. **Extend C:** — if unallocated space or a shrinkable adjacent partition exists, use **Disk Management** (`diskmgmt.msc`) > right-click C: > **Extend Volume**.
2. **Move the user folders**: right-click **Documents/Downloads/Pictures** > **Properties** > **Location** tab > **Move** — point them at another drive. New files land there automatically.
3. **Add storage**: a second internal SSD or a fast external drive for data, keeping C: for Windows and apps only.
4. **Last resort — clean install**: back up, reinstall Windows with only the space you need, and this time put data folders on a separate partition from day one.
5. Going forward, treat C: as the OS drive, not the everything drive — the red bar should never return.

## Closing

Low disk space on C: is a maintenance problem with a maintenance solution: Disk Cleanup for Windows' junk, honest triage of your own files, Storage Sense to keep it clean, and structural moves for small drives. Work the list in order and most systems recover 30–80 GB in under an hour. The drives that stay full are the ones where nobody ever looked at what was actually on them — and now you have.
