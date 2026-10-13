---
title: "Fix Windows Update Error 0x80070070 on Windows 10: Free Up Space"
slug: how-to-fix-windows-update-error-0x80070070-on-windows-10
date: 2026-09-18
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "disk space", "storage", "windows 11"]
description: "Error 0x80070070 on Windows 10 means the update ran out of disk space. Free space safely with these steps so installation can proceed."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-on-windows-10.webp"
faqs:
  - q: "How much free space does Windows Update need?"
    a: "For cumulative updates on Windows 10, keep at least 10GB free; for cumulative and feature updates, maintain 20–32GB. The installer stages files, holds a rollback copy, and needs working room all at once. Error 0x80070070 appears when the drive cannot supply that room, so treat 20GB free as the practical minimum."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are certain you will not roll back to the previous Windows version. Windows.old exists purely as a rollback safety net, and Windows removes it automatically after roughly ten days. Deleting it through Disk Cleanup's Previous Windows installation(s) option is the supported route and typically frees 15–30GB."
  - q: "Why does the error persist after I freed several gigabytes?"
    a: "Because the update needs more than you freed, or temp files and retry downloads consumed the gains. Recheck free space after cleaning — failed attempts refill SoftwareDistribution — and aim decisively above the minimum. If space looks healthy but the error continues, the drive may be misreporting from file-system errors, so run `chkdsk C: /f`."
  - q: "Can I install updates with everything on an external drive?"
    a: "No — Windows itself must stay on the internal drive, but the installer can park temporary staging files on an external USB drive during cumulative and feature updates. When space is tight, the setup wizard offers this option itself. Apps, documents, and the Windows installation stay put; only transient working files go external."
---
Error 0x80070070 on Windows 10 means the update literally ran out of room. Feature updates are the usual trigger — they stage nearly a full copy of Windows alongside the old one — but even cumulative updates choke on drives reduced to their last gigabyte or two. Nothing is damaged; the disk is simply full.

View this as decluttering with a purpose: Windows hoards gigabytes it no longer needs — retired update backups, temporary files, superseded installations — and reclaiming that space is safe. Work from the biggest wins downward, and you can often recover tens of gigabytes in under half an hour.

Our [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80070070-on-windows-11/) tackles the same error on Windows 11, while the [companion guide for 0x800f0988](/articles/how-to-fix-windows-update-error-0x800f0988-on-windows-10/) handles component failures that sometimes ride along with a full drive. Survey the disk first, then start cleaning.

## Why this happens

- **The drive is genuinely almost full:** 0x80070070 means writes ran out of space mid-operation. Below a few gigabytes free, even routine cumulative updates cannot stage their files.
- **Feature updates demand far more room than they admit:** cumulative and feature updates may need 20GB or more of working space, since the new OS image is staged beside the old one before the switchover.
- **WinSxS has grown without bound:** years of updates pile superseded components into WinSxS; left uncleaned, this folder alone can swallow tens of gigabytes on older installations.
- **A previous installation lingers after upgrading:** the Windows.old folder holds 15–30GB and only removes itself after roughly ten days — until then it keeps blocking new updates.
- **Temp and Delivery Optimization files accumulate:** failed and retried downloads, peer-to-peer Delivery Optimization caches, and heaps of temp files quietly devour the room updates need.
- **Hibernation and paging reserve huge chunks:** on a 16GB laptop, hiberfil.sys plus pagefile.sys can reserve over 20GB that the update engine cannot borrow.
- **Personal files filled a small SSD:** on 128GB drives, a photo library, game installs, or a synced cloud folder can leave Windows almost nothing to work with — and updates are the first casualty.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map exactly where the space went

Note the top three categories before moving on; the fixes below target them directly. Knowing whether temp files, apps, or documents dominate tells you which fix will pay off most.

1. Open Settings > System > Storage.
2. Select the system drive to view its category breakdown.
3. Identify the leaders: Temporary files, Apps, and Documents usually top the list.
4. Open Temporary files to see which safe-to-delete subcategories Windows offers.
5. Keep this window handy as your scoreboard while you work through the fixes.

### Fix 2: Run Disk Cleanup including system files

Everything offered under system files is safe to remove — Windows only lists data it can regenerate or no longer needs.

1. Find Disk Cleanup via search, right-click it, and select Run as administrator.
2. Pick the system drive, then click Clean up system files.
3. Tick all the bulky categories: Previous Windows installation(s), Windows Update Cleanup, Delivery Optimization Files, Temporary files.
4. Click OK, then Delete Files, and wait — slow drives can take 15 minutes.
5. Recheck free space; retry the update in Settings > Update & Security > Windows Update once you have 20GB+ free.

### Fix 3: Clear the update download cache itself

Combine this with Disk Cleanup for maximum effect — together they routinely recover the room a feature update demands.

1. Open a Command Prompt with admin rights.
2. Run `net stop wuauserv` and `net stop bits`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `net start wuauserv` and `net start bits`.
5. Remove the SoftwareDistribution.old folder after the update succeeds.

### Fix 4: Relocate personal files and drop the heavy apps

Think in giants: sort by size and move the biggest items first — ten small deletions never beat one 40GB game.

1. In Settings > Apps > Installed apps, sort by Size and remove games and apps you no longer use.
2. Shift large media folders to an external USB drive or a second partition.
3. For OneDrive or Dropbox, set big folders to online-only (Files On-Demand) so local copies leave the small SSD.
4. Empty the Recycle Bin — deleted files still occupy space until then.
5. Recheck free space; target at least 20GB free before retrying cumulative and feature updates.

### Fix 5: Stage the feature update on an external drive

This is Microsoft's designed answer for 64GB and 128GB devices, not a hack: the external drive temporarily hosts what the internal SSD cannot.

1. Connect a USB drive with 16–32GB free (back up its contents first).
2. Launch the update from Settings > Update & Security > Windows Update or via the Windows 10 Media Creation Tool.
3. When the installer flags low space, choose the external drive as the temporary storage location.
4. Keep the drive attached and the laptop on power for the entire install.
5. Disconnect it only after the update completes and the desktop returns.

### Fix 6: Switch on Storage Sense for ongoing defense

Configure it once and it guards silently — especially valuable on small-SSD laptops under chronic space pressure.

1. Open Settings > System > Storage and enable Storage Sense.
2. Open its settings and pick a schedule — weekly suits most laptops.
3. Turn on temporary-file deletion and set the Recycle Bin to empty after 30 days.
4. Enable OneDrive Files On-Demand cleanup for files untouched in 30 days.
5. For Microsoft's official space-freeing guidance, see the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

On Windows 10, a full disk is the most gratifying update error to fix because every reclaimed gigabyte is visible progress. Disk Cleanup with system files plus a cleared update cache settles most cases; an external drive covers the remainder. Leave Storage Sense switched on, and the next feature update will install instead of protesting.
