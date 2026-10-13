---
title: "Fix Windows Update Error 0x80070070 on Windows 11 (Not Enough Disk Space)"
slug: how-to-fix-windows-update-error-0x80070070-on-windows-11
date: 2026-09-17
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "disk space", "storage", "windows 11"]
description: "Error 0x80070070 means your Windows 11 laptop ran out of disk space during the update. Reclaim gigabytes safely and get the update installed."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-on-windows-11.webp"
faqs:
  - q: "How much free space does Windows Update need?"
    a: "For cumulative updates on Windows 11, aim for at least 10GB free; for feature updates such as 24H2, keep 20–32GB free. The installer stages files, keeps a rollback copy, and needs working room simultaneously. Error 0x80070070 appears when the drive cannot provide that working room, so treat 20GB free as your practical minimum."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are sure you will not roll back to the previous Windows version. Windows.old holds your old installation purely as a rollback safety net and Windows deletes it automatically after about ten days. Removing it via Disk Cleanup's Previous Windows installation(s) option is the supported way and commonly frees 15–30GB."
  - q: "Why does the error persist after I freed several gigabytes?"
    a: "Because the update needs more than you freed, or new temp files and retry downloads consumed the gains. Check free space again after cleanup — failed attempts refill SoftwareDistribution — and aim decisively above the minimum. If space looks fine but the error continues, the drive may be misreporting due to file-system errors, so run `chkdsk C: /f`."
  - q: "Can I install updates with everything on an external drive?"
    a: "No — Windows itself must live on the internal drive, but the installer can use an external USB drive for temporary staging files during feature updates such as 24H2. When space is tight, the setup wizard offers this option itself. Your apps, documents, and the Windows installation stay where they are; only the transient working files go external."
---
Error 0x80070070 is refreshingly honest: ERROR_DISK_FULL. Your Windows 11 laptop simply ran out of room while staging or installing the update, and the engine stopped rather than write into space that does not exist. Laptops with 128GB or 256GB drives hit this regularly, especially when a large feature update needs tens of gigabytes of working room.

The fix is a space-reclamation project, not a repair: audit what is eating the drive, remove what Windows can safely discard, move what you want to keep, and give the update the elbow room it needs. Every step below targets the biggest, safest wins first.

If disk pressure is a theme on your other machines too, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80070070-on-windows-10/) covers the same error on Windows 10, and the [companion guide for 0x800f0988](/articles/how-to-fix-windows-update-error-0x800f0988-on-windows-11/) helps when the space problem is tangled up with corrupted components. Start by measuring what you actually have.

## Why this happens

- **The system drive is genuinely nearly full:** 0x80070070 means the disk ran out of space during the write. When free space drops under a few gigabytes, even routine cumulative updates cannot stage their files.
- **Feature updates need far more room than they admit:** feature updates such as 24H2 can require 20GB or more of free working space because the new OS image is staged alongside the old one before the switch-over.
- **The WinSxS component store has grown unchecked:** Years of updates accumulate superseded components in WinSxS. Without periodic cleanup, this folder alone can consume tens of gigabytes on older installations.
- **Old Windows installations linger after upgrades:** The Windows.old folder from a previous upgrade holds 15–30GB and is only auto-removed after about ten days — until then it sits there blocking new updates.
- **Temporary and delivery-optimization files pile up:** Failed and retried downloads, Delivery Optimization caches shared with other PCs, and mountains of temp files silently eat the free space updates need.
- **Hibernation and page files reserve large chunks:** On laptops with 16GB of RAM, hiberfil.sys and pagefile.sys together can reserve over 20GB — space the update engine cannot borrow.
- **Personal files filled a small SSD:** On 128GB drives, a photo library, game installs, or a synced cloud folder can leave Windows with almost nothing to work with, and updates are the first casualty.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly where the space went

You cannot clean what you cannot see. Windows' built-in storage view breaks the drive down by category — apps, temporary files, documents, system — so you attack the biggest categories first instead of deleting blindly. Two minutes here directs the next twenty productively.

1. Open Settings > System > Storage (Windows 11) or Settings > System > Storage (Windows 10).
2. Click the system drive to see the category breakdown.
3. Note which categories dominate: Temporary files, Apps, and Documents are the usual leaders.
4. Click Temporary files to see the safe-to-delete subcategories Windows offers.
5. Keep this window open as a scoreboard while you work through the fixes.

### Fix 2: Run Disk Cleanup with system files

Disk Cleanup is the heavy artillery for update-blocking clutter: run as administrator with the system-files option, it can remove previous Windows installations, old update backups, Delivery Optimization files, and device driver packages — often 10–30GB in one pass on neglected machines.

1. Search for Disk Cleanup, right-click it, and choose Run as administrator.
2. Select the system drive and click Clean up system files.
3. Check every large category: Previous Windows installation(s), Windows Update Cleanup, Delivery Optimization Files, Temporary files.
4. Click OK, then Delete Files, and let it finish — this can take 15 minutes on slow drives.
5. Re-check free space in Settings > Windows Update afterward; retry the update if you now have 20GB+ free.

### Fix 3: Empty the update download cache itself

Ironically, failed update attempts consume the very space the next attempt needs: each retry stages more files into SoftwareDistribution. Clearing that cache both removes gigabytes of dead downloads and gives the next attempt a clean staging area.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv` and `net stop bits`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `net start wuauserv` and `net start bits`.
5. Delete the SoftwareDistribution.old folder once the update succeeds.

### Fix 4: Move personal files and uninstall the heavy apps

System cleaning has limits — at some point the space hog is your own data. Large games, video projects, and synced cloud folders are the big three on laptops. Moving them to an external drive or a second partition frees gigabytes that no cleanup tool can touch, because the tools correctly refuse to delete your files.

1. In Settings > Apps > Installed apps, sort by Size and uninstall games and apps you no longer use.
2. Move large media folders to an external USB drive or a second partition.
3. For OneDrive or Dropbox, switch large folders to online-only (Files On-Demand) to keep local copies off the small SSD.
4. Empty the Recycle Bin — deleted files still occupy space until you do.
5. Re-check free space; aim for at least 20GB free before retrying feature updates such as 24H2.

### Fix 5: Use an external drive for the feature update

Windows explicitly supports attaching a USB drive to supply the missing working space during a feature update — the installer will offer this itself when space is tight. A 32GB or larger USB stick or external SSD is enough to carry the staging files.

1. Connect a USB drive with at least 16–32GB free (back up anything on it first).
2. Start the update from Settings > Windows Update or the Windows 11 installation media.
3. When the installer warns about low space, choose the external drive as the temporary storage location.
4. Keep the drive connected and the laptop plugged into power for the entire install.
5. Remove the drive only after the update completes and the desktop returns.

### Fix 6: Enable Storage Sense for ongoing protection

Storage Sense is Windows' automatic janitor: it clears temp files, empties the recycle bin on a schedule, and can offload unused cloud files. Enabling it after your manual cleanup prevents 0x80070070 from returning the next time a big update arrives.

1. Open Settings > System > Storage and turn on Storage Sense.
2. Click Storage Sense to configure its schedule — weekly cleanup suits most laptops.
3. Enable deletion of temporary files and set the Recycle Bin to empty after 30 days.
4. Turn on OneDrive Files On-Demand cleanup for files unused in 30 days.
5. For Microsoft's official guidance on freeing space, see the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Error 0x80070070 is a capacity problem with a capacity solution: measure, clean the system clutter, move your own giants, and let Storage Sense keep the pressure off. On Windows 11 laptops with small drives, treating 20GB of free space as a hard floor — not a nice-to-have — keeps updates flowing and keeps this error from ever coming back.
