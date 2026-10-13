---
title: "How to Fix Windows Update Error 0x80070070 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070070-in-windows-11-24h2
date: 2026-10-09
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "error code", "windows 11", "disk space"]
description: "Error 0x80070070 means your disk is too full for the update. Free gigabytes fast with Disk Cleanup, hibernation tweaks, and these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-in-windows-11-24h2.webp"
faqs:
  - q: "How much free space does Windows 11 24H2 actually need to update?"
    a: "For monthly cumulative updates, 8 to 10 GB of free space on C: is usually enough. Feature updates like 24H2 need much more — Microsoft recommends around 20 GB free for staging, installation files, and the rollback copy. The 0x80070070 error appears when the update engine's space calculation comes up short."
  - q: "Is it safe to delete Windows.old?"
    a: "Yes, once you are sure the current Windows version works fine. Windows.old exists only so you can roll back within ten days of a feature update. Deleting it via Disk Cleanup's Previous Windows installation(s) option simply removes the rollback path; your files, apps, and settings are unaffected."
  - q: "Will disabling hibernation break Sleep mode?"
    a: "No. Sleep (S3/modern standby) and hibernation are separate. Disabling hibernation with powercfg /hibernate off only removes the hiberfil.sys file and the Hibernate option from the power menu. Sleep, lid-close behavior, and fast startup alternatives all keep working normally."
  - q: "My SSD is only 128 GB and always nearly full. Any long-term fix?"
    a: "Treat it as a storage-management habit: keep large media on external or cloud storage, install big games on a second drive if the laptop has one, run Storage Sense automatically, and clear Delivery Optimization files after each Patch Tuesday. If the laptop supports it, upgrading to a larger SSD is the real permanent fix."
---

Error 0x80070070 is refreshingly honest: your disk is too full for the update. Windows 11 24H2 feature updates can demand 20 GB or more of free space for staging, installation, and the rollback copy — and laptops with 128 GB or 256 GB SSDs hit this wall regularly, especially when old Windows installations and hibernation files are squatting on gigabytes.

Under the hood, 0x80070070 means there is not enough free disk space for the update to download and install. Technically it is ERROR_DISK_FULL: the update engine calculated the space it needs — download staging plus install workspace plus rollback reserve — and the system drive came up short. Windows aborts early rather than failing halfway through the install.

The encouraging part: 0x80070070 is one of the better-understood update errors, and the fixes below are ordered from quickest to most thorough. Work through them in sequence — most readers never need the last two.

## Why this happens

- **A nearly full system drive.** The straightforward cause: C: simply does not have the 15–20 GB the update wants.
- **Old Windows installations retained.** Each feature update keeps a Windows.old folder (10–20 GB) for rollback for ten days.
- **A huge hibernation file.** hiberfil.sys typically matches a large fraction of installed RAM — 8–16 GB on modern laptops.
- **Delivery Optimization cache bloat.** Staged update files from previous attempts pile up in the servicing cache.
- **Temp files and recycle bin.** Gigabytes of installers, downloads, and deleted-but-not-emptied files eat the margin.
- **Large apps and games on C:.** A few big titles or creative suites can leave the drive permanently near capacity.
- **A small SSD with no headroom.** 128 GB drives were marginal for Windows 11 from day one and get worse with every feature update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure exactly how much space you need

Do not guess — measure. Knowing the gap tells you whether a quick cleanup suffices or whether files must move off the drive.

1. Open **Settings > System > Storage** and check free space on C: — note the exact number.
2. For a cumulative update you generally need 8–10 GB free; for a 24H2 feature update, aim for 20 GB.
3. Click **Temporary files** in Storage settings to see the breakdown of reclaimable space.
4. If the gap is under 10 GB, Fixes 2 and 3 will likely close it. If it is larger, also do Fix 4.

### Fix 2: Run Disk Cleanup with system files

The built-in Disk Cleanup, run with system-files mode, reclaims the biggest single chunks: old Windows installations, delivery optimization files, and update leftovers.

1. Search for **Disk Cleanup**, right-click it, and choose **Run as administrator**.
2. Select C:, then click **Clean up system files** and select C: again.
3. Check **Previous Windows installation(s)**, **Delivery Optimization Files**, **Temporary Windows installation files**, and **Recycle Bin**.
4. Click OK, confirm the deletion, and recheck free space in Settings > Storage.

### Fix 3: Disable hibernation to reclaim gigabytes instantly

If you never use hibernation — most laptop users just use Sleep — the hiberfil.sys file is pure waste. Disabling it returns RAM-sized disk space in seconds.

1. Open Command Prompt as administrator.
2. Run `powercfg /hibernate off` — hiberfil.sys is deleted immediately.
3. Verify the freed space in Settings > System > Storage.
4. If you later miss hibernation, `powercfg /hibernate on` restores it. Sleep mode is unaffected either way.

### Fix 4: Move personal files and trim big apps

When system cleanup is not enough, the next gigabytes come from your own data. Moving it off C: is the durable fix for chronically full small SSDs.

1. In **Settings > System > Storage**, use the category breakdown to find what is actually consuming space.
2. Move large videos, photos, and downloads to an external drive or a second partition.
3. Uninstall games and apps you no longer use via **Settings > Apps > Installed apps** (sort by size).
4. Empty the Recycle Bin afterward — deleted files do not free space until you do.

### Fix 5: Use external storage for the update staging (feature updates)

For 24H2 upgrades on cramped drives, Windows lets you attach a USB drive as scratch space so the staging does not have to fit on C:.

1. Plug in a USB flash drive or external drive with at least 10 GB free (16 GB is safer).
2. Start the feature update from **Settings > Windows Update**.
3. When Windows warns about low disk space, choose the external drive when it offers to use connected storage.
4. Keep the drive connected until the entire update — including all restarts — is finished.

### Fix 6: Turn on Storage Sense so it stays fixed

A one-time cleanup solves today's update, but Storage Sense prevents the next 0x80070070 by automatically removing temp files, emptying the recycle bin on a schedule, and cleaning the Downloads folder of stale files.

1. Open **Settings > System > Storage** and toggle **Storage Sense** on.
2. Click **Storage Sense** to configure it: set it to run **Every week** and to delete files in the recycle bin after 30 days.
3. Enable **Delete temporary files that my apps aren't using** in the same screen.
4. Run it once manually with **Run Storage Sense now**, then confirm your free space holds steady over the following weeks.

### Fix 7: Run the Windows Update troubleshooter

The built-in troubleshooter knows the usual suspects behind 0x80070070: it checks the service state, the update cache, and the network path to Microsoft's servers, then applies safe automatic repairs. It will not fix deep corruption, but it clears the simple causes in a few minutes and is worth trying before anything manual.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the on-screen prompts.
3. Restart the PC when it finishes, then check for updates again at **Settings > Windows Update**. If 0x80070070 is still there, move on to the next fix.

## Closing

0x80070070 is the most honest error in this guide — it tells you exactly what is wrong. Free the space and the update proceeds. After updating, keep Storage Sense on so the problem does not return. If a different error appears next, our [Windows 11 24H2 update error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) covers the rest, and the [troubleshooter guide](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the basics. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official space requirements.
