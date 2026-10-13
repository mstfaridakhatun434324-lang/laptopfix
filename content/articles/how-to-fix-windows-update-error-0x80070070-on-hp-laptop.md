---
title: "How to Fix Windows Update Error 0x80070070 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x80070070-on-hp-laptop
date: 2026-10-12
categories: ["windows-update"]
tags: ["windows update", "0x80070070", "hp laptop", "windows 11"]
description: "Error 0x80070070 on your HP laptop means the disk is too full for the update. This HP-focused guide frees space safely and gets updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070070-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070070 mean on an HP laptop?"
    a: "It is ERROR_DISK_FULL: the update needs more free space than the drive has available. Windows updates need room to download the package, unpack it, stage the new files, and keep a rollback copy — often several gigabytes total. On HP laptops with smaller SSDs, the culprits are usually accumulated update backups, HP recovery images, hibernation files, and large personal media libraries."
  - q: "How much free space does Windows Update need?"
    a: "Microsoft recommends at least 10 GB free, but large feature updates are happiest with 20 GB or more of headroom. The update downloads a multi-gigabyte package, extracts it, and stages both the new system and a complete rollback image before it touches your running Windows. Running with less than 10 GB free invites 0x80070070 and other space-related failures."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are confident the last major update works correctly. Windows.old is the rollback copy of your previous Windows installation, and Disk Cleanup's system-files mode can remove it safely. Only delete it after a week or so of stable use following the update, because it is your only built-in path back if the new version misbehaves."
  - q: "Can HP's recovery partition cause this error?"
    a: "Indirectly. HP's factory recovery image consumes disk space that could otherwise serve the update, but you should never delete the recovery partition to fix 0x80070070 — the space math rarely works out and you lose your factory reset option. Free space on the Windows partition itself with the cleanup steps below; the recovery partition is not the place to economize."
---

Error 0x80070070 is refreshingly honest: ERROR_DISK_FULL. The update needs more room than your drive has, so it stops before it starts. There's no corruption, no misconfiguration, no mystery — just arithmetic. Windows updates are big operations: the package downloads, unpacks, stages new system files, and keeps a full rollback copy, which means a "3 GB update" can easily demand 10–20 GB of working space.

HP laptops with 256 GB or smaller SSDs hit this wall first, especially machines that have been in service for years accumulating update backups, HP recovery data, hibernation files, and the usual drift of downloads and media. The fix is a space audit followed by safe cleanup — and knowing which big-ticket items are safe to remove and which aren't. The good news is that most of the reclaimable space on a neglected laptop is genuinely disposable — update leftovers, temp files, and caches — so you can usually hit the 10 GB target without deleting anything you care about.

## Why this happens

- **Years of accumulated Windows Update backups.** Each major update leaves rollback data that piles up silently.
- **The Windows.old folder.** A full copy of the previous installation, often 15–25 GB, kept for rollback.
- **Hibernation and page files.** `hiberfil.sys` can equal your RAM size; the page file grows with it.
- **HP recovery images and bloat.** Factory recovery data and preinstalled apps consuming tens of gigabytes.
- **Delivery Optimization cache.** Downloaded update chunks shared with other PCs, rarely cleaned automatically.
- **Temp files and downloads.** The humble Downloads folder and temp directories, grown unchecked for years.
- **Large personal media.** Photos, videos, and game installs crowding a small SSD.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure exactly what you're dealing with

A space problem deserves numbers before action.

1. Open **Settings > System > Storage** and note the free space on C: — under 10 GB confirms the diagnosis.
2. Click into the storage breakdown to see which categories dominate: System, Apps, Temporary files, Documents.
3. Check the single biggest surprise — it's usually Windows.old, hibernation, or a forgotten video folder.
4. Set a target: 20 GB free for comfort, 10 GB minimum. Everything below aims at that number.

### Fix 2: Run Disk Cleanup with system files

The safest big win, built into Windows.

1. Search for **Disk Cleanup**, right-click it, and choose **Run as administrator**.
2. Select C:, then click **Clean up system files** and select C: again.
3. Check **Windows Update Cleanup**, **Temporary files**, **Delivery Optimization Files**, **Recycle Bin**, and **Thumbnails**.
4. Only check **Previous Windows installation(s)** (Windows.old) if your last major update has been stable for a week or more. Click OK and let it work — this alone often frees 10–30 GB.

### Fix 3: Trim hibernation and virtual memory

Reclaim gigabytes most laptop users never miss.

1. If you never use hibernation, open an administrator Command Prompt and run `powercfg /hibernate off` — this deletes `hiberfil.sys`, often 8–16 GB.
2. If you do use hibernation, leave it on; the space is serving a purpose.
3. For the page file, open **System Properties > Advanced > Performance Settings > Advanced > Virtual memory** and let Windows manage it — manual oversized settings are a common silent hog.
4. Restart and recheck free space in **Settings > System > Storage**.

### Fix 4: Uninstall what HP preinstalled and you never use

HP laptops ship with software many owners never open.

1. Open **Settings > Apps > Installed apps** and sort by size.
2. Remove trial antivirus suites (if you've chosen another), preinstalled games, and HP utilities you demonstrably never use — keep **HP Support Assistant** and core drivers.
3. Be conservative: if you're unsure what something is, search its name before uninstalling. HP's drivers are recoverable from the [HP support site](https://support.hp.com/us-en) if you over-prune.
4. Recheck your free space; bloatware removal commonly yields several gigabytes.

### Fix 5: Move personal files off the system drive

Your files are the legitimate occupants — give them a bigger home.

1. In Storage settings, identify your largest personal folders — usually Videos, Pictures, or game libraries.
2. Move them to an external drive, a second internal drive, or cloud storage with local copies removed.
3. Use **Settings > System > Storage > Advanced storage settings > Where new content is saved** to route future downloads and documents elsewhere.
4. Aim to keep C: for Windows, apps, and working space — personal archives belong on cheaper bulk storage.

### Fix 6: Shrink the WinSxS component store

The component store grows with every update; clean it officially.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /StartComponentCleanup` to remove superseded components.
2. For a deeper clean, add `/ResetBase` — but know this removes the ability to uninstall updates, so only do it on a stable system.
3. Never delete WinSxS files manually; the store is a hardlink farm and manual deletion corrupts Windows.
4. Verify the freed space and retry the update once you're above 10 GB free.

### Fix 7: Retry the update — and consider external storage for the install

With room made, let the update use it.

1. Go to **Settings > Windows Update** and retry the previously failing update.
2. If space is still marginal, Windows may offer to use external storage during a feature update — accept with a USB drive attached.
3. After success, keep 10+ GB free going forward; enable **Storage Sense** at **Settings > System > Storage** to automate temp cleanup.
4. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents space requirements if you want the official numbers.

## Closing

Error 0x80070070 is pure arithmetic, and the Disk Cleanup plus hibernation steps above resolve it on most HP laptops without touching a single personal file. For the generic walkthrough, see the [step-by-step 0x80070070 guide](/articles/how-to-fix-windows-update-error-0x80070070-step-by-step/), and if your drive has space but updates fail on corrupted data instead, the [0x8007000D guide for HP laptops](/articles/how-to-fix-windows-update-error-0x8007000d-on-hp-laptop/) addresses that different problem.
