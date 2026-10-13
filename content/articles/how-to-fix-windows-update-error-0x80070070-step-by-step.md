---
title: "How to Fix Windows Update Error 0x80070070 Step by Step"
slug: how-to-fix-windows-update-error-0x80070070-step-by-step
date: 2026-10-13
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "disk full", "windows 11"]
description: "Error 0x80070070 means your disk is too full for Windows Update. Follow this step-by-step guide to free space safely and install the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-step-by-step.webp"
faqs:
  - q: "How much free space does Windows Update actually need?"
    a: "Plan on 10 GB as the absolute minimum and 20 GB for comfortable headroom. A cumulative update downloads a multi-gigabyte package, extracts it, stages the new system files, and retains a complete rollback copy before committing anything. Feature updates need even more. Below 10 GB free, 0x80070070 is the expected outcome, not a surprise."
  - q: "What is safe to delete when freeing space?"
    a: "Windows Update Cleanup, temporary files, Delivery Optimization files, the Recycle Bin contents, thumbnails, and — after a week of stable use — the Windows.old previous-installation folder are all safe via Disk Cleanup. Your personal documents, photos, and installed programs should be moved or uninstalled deliberately, never bulk-deleted. When in doubt, move files to external storage rather than deleting them."
  - q: "Will Storage Sense prevent this error in the future?"
    a: "Largely, yes. Storage Sense automatically clears temporary files, empties the Recycle Bin on a schedule, and can remove unused cloud-backed files. It won't move your video collection or uninstall games, so it can't fix a drive that's fundamentally too small for its contents — but it prevents the slow accumulation of junk that causes most 0x80070070 cases."
  - q: "Can I install the update to a different drive?"
    a: "Windows itself must stay on its current drive, but feature updates can use external USB storage as scratch space during installation when offered. For a permanently cramped drive, the real solutions are moving personal files off C:, uninstalling large unused apps, or upgrading to a larger SSD. The update cannot relocate your Windows installation for you."
---

Error 0x80070070 is the rare Windows error that tells you exactly what's wrong: ERROR_DISK_FULL. The update did its space math, came up short, and stopped. No corruption, no conspiracy — the drive is simply too full for the operation, which needs far more room than the update's advertised size suggests.

That size gap surprises people. A "3 GB update" downloads its package, unpacks it, stages an entire new system image alongside the old one, and keeps a rollback copy — easily 10–20 GB of working space for a big update. Laptops that have run for years without a cleanup accumulate the perfect storm: update backups, a Windows.old folder, hibernation files, temp data, and full media libraries. The sequence below audits the space, reclaims it safely, and keeps it reclaimed. One principle runs through every fix: never delete what you can't identify. Disk Cleanup's categories are all safe by design, but personal files should be moved to external or cloud storage rather than deleted in a hurry. A surprising number of "disk full" emergencies are really "Downloads folder full" emergencies — five minutes in File Explorer sorting by size often reveals a single forgotten folder holding tens of gigabytes. Find that folder first, and the rest of the cleanup becomes easy. That single habit — sorting by size before deleting anything — prevents nearly every cleanup regret.

## Why this happens

- **Accumulated update backups.** Every major update leaves rollback data that compounds over the years.
- **The Windows.old folder.** A complete previous installation, typically 15–25 GB, retained for rollback.
- **Hibernation file.** `hiberfil.sys` scales with installed RAM — 16 GB of RAM means a 16 GB file.
- **Oversized page file.** Manual virtual-memory settings that balloon far beyond need.
- **Delivery Optimization cache.** Shared update chunks that linger after serving their purpose.
- **Temp files and an overflowing Downloads folder.** Years of small accumulations becoming gigabytes.
- **Personal media and games.** The legitimate occupants that outgrow small SSDs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Audit the drive with Storage settings

Start with measurements, not deletions.

1. Open **Settings > System > Storage** and record the free space on C:; anything under 10 GB confirms 0x80070070.
2. Open the category breakdown — System, Apps & features, Temporary files, Documents — and identify the top two consumers.
3. Note whether the bulk is system-generated (cleanable) or personal files (movable); the strategy differs.
4. Set your target now: 20 GB free is comfortable, 10 GB is the minimum viable.

### Fix 2: Disk Cleanup with system files

The highest safe yield per minute of effort.

1. Search **Disk Cleanup**, right-click, **Run as administrator**, and select C:.
2. Click **Clean up system files**, reselect C:, and wait for the full category list.
3. Check **Windows Update Cleanup**, **Temporary files**, **Delivery Optimization Files**, **Recycle Bin**, **Thumbnails**, and **DirectX Shader Cache**.
4. Check **Previous Windows installation(s)** only if the last feature update has been stable for at least a week. Click OK — expect 10–30 GB back on a long-neglected system.

### Fix 3: Disable hibernation if you don't use it

One command can return a RAM-sized chunk of disk.

1. Decide honestly: do you ever hibernate, or do you just sleep and shut down? Most laptop users never hibernate.
2. If hibernation is unused, run `powercfg /hibernate off` in an administrator Command Prompt — `hiberfil.sys` vanishes immediately.
3. If you do hibernate, keep it; the space is working for you. Instead, check the page file at **System Properties > Advanced > Performance > Advanced > Virtual memory** and return it to system-managed if someone set it manually huge.
4. Recheck free space after the restart.

### Fix 4: Uninstall large apps you don't use

Programs are the second-biggest discretionary consumer after media.

1. In **Settings > Apps > Installed apps**, sort by size, largest first.
2. Remove games you finished, trial software, duplicate utilities, and manufacturer bloat you never open.
3. For apps you might want later, note their names — reinstalling from the official source beats hoarding gigabytes "just in case."
4. Check free space again; it's common to recover 5–20 GB here alone.

### Fix 5: Relocate personal files

Your files deserve a bigger home than the system drive.

1. Identify the heavy personal folders — Videos and Pictures are the usual winners.
2. Move them to an external drive, a secondary internal drive, or cloud storage (removing local copies for cloud-archived items).
3. Set **Settings > System > Storage > Advanced storage settings > Where new content is saved** so future files land elsewhere by default.
4. Keep C: reserved for Windows, applications, and working headroom.

### Fix 6: Clean the component store properly

WinSxS grows with every update; shrink it the supported way.

1. Run `DISM /Online /Cleanup-Image /StartComponentCleanup` in an administrator Command Prompt.
2. On a stable system you can follow with `/ResetBase` for maximum recovery — understanding it removes update-uninstall capability.
3. Never touch WinSxS manually; its hardlink structure means "deleting" files there corrupts Windows while freeing almost nothing real.
4. Retry the update once free space exceeds 10 GB.

### Fix 7: Enable Storage Sense and retry

Make the fix stick, then run the update.

1. Turn on **Storage Sense** at **Settings > System > Storage** and configure it to clear temp files and empty the Recycle Bin automatically.
2. Retry the failing update at **Settings > Windows Update**.
3. For feature updates on marginal space, attach a USB drive when Windows offers to use external storage for the install.
4. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the space requirements behind this error.

## Closing

Error 0x80070070 is arithmetic, and the audit-then-clean sequence above fixes it without risking a single personal file. For HP-specific notes on preinstalled software and recovery images, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80070070-on-hp-laptop/), and if space is fine but downloads keep failing in transit, the [0x80240034 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80240034-step-by-step/) covers that separate failure.
