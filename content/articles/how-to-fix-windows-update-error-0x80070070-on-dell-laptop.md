---
title: "How to Fix Windows Update Error 0x80070070 on a Dell Laptop (Disk Full)"
slug: "how-to-fix-windows-update-error-0x80070070-on-dell-laptop"
date: 2026-09-22
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "disk full", "dell laptop", "update error"]
description: "Error 0x80070070 means Windows Update ran out of disk space on your Dell laptop. Learn how to free the 20–30 GB it needs and get the update installed cleanly."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-on-dell-laptop.webp"
faqs:
  - q: "How much free space does Windows Update need?"
    a: >
      Microsoft recommends keeping at least 20 to 32 GB free on the system
      drive for feature updates, because the installer downloads,
      extracts, and stages files before swapping them in. Monthly
      cumulative updates need less, but running tight on space still
      causes failures.
  - q: "Is it safe to delete the Windows.old folder?"
    a: >
      Yes, once you are sure the current Windows version works correctly.
      It exists only to let you roll back within ten days of an upgrade.
      Deleting it through Disk Cleanup frees 15 to 30 GB and is fully
      supported by Microsoft.
  - q: "Why does the update fail even though I have 10 GB free?"
    a: >
      Ten gigabytes sounds like a lot, but the updater needs headroom for
      extraction, driver staging, and the WinRE environment. Falling below
      roughly 20 GB free is exactly what triggers 0x80070070 on many Dell
      laptops. Feature updates temporarily expand to several times their
      download size while installing, so Microsoft recommends 20 to 32 GB
      of free space before starting.
  - q: "Can I install the update to an external drive instead?"
    a: >
      No, Windows feature updates must install to the system drive. You
      can, however, plug in a USB drive with at least 10 GB free during
      setup — Windows will use it for temporary staging files, which
      sometimes lets a cramped C: drive squeak through.
---

Error 0x80070070 is one of the more honest error codes Windows Update produces: translated, it is ERROR_DISK_FULL. Your Dell laptop simply does not have enough free space on the system drive for the update to download, expand, and install. Feature updates in particular need a surprising amount of elbow room — often 20 to 32 GB of free space — even though the final installed footprint is smaller.

This crops up most often on Dell laptops with smaller drives: 128 GB SSDs in entry-level Inspirons and Latitudes, or machines where years of Windows.old folders, delivery optimization caches, and forgotten downloads have quietly eaten the drive. The good news is that the fix rarely requires deleting anything you care about. Windows ships with purpose-built cleanup tools, and most of the space hogs are temporary files the system no longer needs.

Before you start, check exactly where you stand: open File Explorer, click This PC, and note the free space on your C: drive. If it is under 20 GB, you have found your culprit. The steps below walk you through freeing space safely, expanding it if cleanup is not enough, and re-running the update so it completes without the 0x80070070 failure. If you are dealing with a related symptom instead, see [Windows Update stuck while downloading on an Acer machine](/articles/how-to-fix-windows-update-stuck-downloading-on-acer-laptop/) and [update errors after a clean install on a Dell](/articles/how-to-fix-windows-update-error-after-clean-install-on-dell-laptop/).

## Why this happens

- **Insufficient free space on C:** the update needs far more working space than the download size suggests.

- **Stale Windows.old folder** previous installation files kept for rollback can occupy 15–30 GB.

- **Bloated SoftwareDistribution cache** failed and partial downloads accumulate in the update cache.

- **Delivery Optimization files** cached update parts shared with other PCs on your network pile up.

- **Large temporary and log files** months of temp files, crash dumps, and setup logs quietly grow.

- **Full recovery or EFI-adjacent partitions** a crowded drive layout can also block the WinRE staging step.

- **OneDrive or Dropbox sync folders** cloud files set to ‘always keep on this device’ consume local disk.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free up space with Disk Cleanup

Disk Cleanup is the fastest safe way to reclaim gigabytes. It targets exactly the files Windows no longer needs, and with the ‘Clean up system files’ option it can remove old update backups and the Windows.old folder.

1. Press Win + S, type Disk Cleanup, and open it.

2. Select the C: drive and click OK.

3. Click ‘Clean up system files’ and select C: again.

4. Check Previous Windows installation(s), Windows Update Cleanup, Temporary files, and Delivery Optimization Files.

5. Click OK, then Delete Files, and let it finish.

6. Re-check free space in This PC — aim for at least 25 GB.

### Fix 2: Run Storage Sense for an automatic sweep

Storage Sense automates the cleanup so temporary files and Recycle Bin contents do not silently refill the drive between update attempts.

1. Open Settings > System > Storage.

2. Turn on Storage Sense.

3. Click Storage Sense and enable ‘Delete temporary files that my apps aren’t using’.

4. Click ‘Run Storage Sense now’ and wait for it to finish.

5. Re-run Windows Update from Settings > Windows Update.

### Fix 3: Clear the SoftwareDistribution download cache

If previous failed attempts left a large half-downloaded payload, deleting it both frees space and removes the corrupted cache that can cause repeat failures.

1. Open Command Prompt as administrator.

2. Run: net stop wuauserv and net stop bits.

3. Open C:\Windows\SoftwareDistribution\Download and delete everything inside.

4. Back in Command Prompt, run: net start wuauserv and net start bits.

5. Retry the update — it will download a fresh copy.

### Fix 4: Move personal files off the system drive

Photos, videos, and installers often live on the desktop or in Downloads out of habit. Moving them to another partition, an external drive, or the cloud can free several gigabytes in minutes.

1. Open Settings > System > Storage and review the largest categories.

2. Move large videos and installers to an external drive or second partition.

3. Uninstall programs you no longer use via Settings > Apps > Installed apps.

4. Empty the Recycle Bin after deleting.

5. Set OneDrive folders to ‘Free up space’ so they stay cloud-only.

### Fix 5: Check what is eating the disk with a visual scan

When cleanup does not add up, a disk-usage scan shows the real hogs — sometimes a single forgotten folder is the whole problem.

1. Install a free disk analyzer such as WizTree or WinDirStat.

2. Run it on C: and sort by folder size.

3. Look for oversized folders outside Windows and Program Files — old backups, game captures, virtual machines.

4. Move or delete what you no longer need, then empty the Recycle Bin.

5. Confirm at least 25 GB free, then retry Windows Update.

### Fix 6: Extend the C: partition if the drive has unallocated space

Some Dell laptops ship with unallocated space or a large D: partition. Giving C: more room is a permanent fix for recurring 0x80070070 errors.

1. Right-click Start and open Disk Management.

2. Check for unallocated space next to the C: partition, or shrink D: to create some.

3. Right-click the C: partition and choose Extend Volume.

4. Follow the wizard to add the unallocated space to C:.

5. Reboot and re-run Windows Update.

### Fix 7: Use Dell’s cleanup guidance and retry

Dell documents storage-related update failures for its lineup, and their support tooling can flag driver-level disk issues that generic cleanup misses.

1. Visit [Dell’s support site](https://www.dell.com/support) and run the storage diagnostics for your model.

2. Install any pending Dell firmware updates offered there — some fix NVMe reporting bugs that mislead Windows Update.

3. With 25+ GB free, open Settings > Windows Update and click Retry.

4. If it still fails, run the Windows Update troubleshooter from Settings > System > Troubleshoot.

## Closing

Error 0x80070070 is almost always a storage problem rather than a broken update, so once the drive has real breathing room the installation usually completes on the next attempt. Keep Storage Sense enabled afterward and the same failure is unlikely to return for the next feature update. For official guidance, see [Microsoft's Windows update support hub](https://support.microsoft.com/en-us/windows).
