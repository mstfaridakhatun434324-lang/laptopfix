---
title: "How to Fix Low Disk Space on the C Drive on an HP Laptop"
slug: how-to-fix-low-disk-space-on-c-drive-on-hp-laptop
date: 2026-10-06
categories: ["performance"]
tags: ["low disk space", "hp laptop", "c drive full", "disk cleanup", "hp storage"]
description: "HP laptop warning about low disk space on C:? Reclaim gigabytes with HP-specific cleanup steps — recovery partitions, preinstalled software, and Windows storage tools."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-on-hp-laptop.webp"
faqs:
  - q: "Why do HP laptops run out of C: drive space so quickly?"
    a: "HP laptops ship with a large set of preinstalled utilities, recovery partitions, and bundled software that consume space from day one. Budget HP models also commonly have small 128 GB or 256 GB drives, so Windows, updates, and HP's own software leave little room for your files. The combination of a small drive and heavy preinstalled software is the core issue."
  - q: "Can I delete the HP recovery partition to free space?"
    a: "You can, but think carefully first. The recovery partition lets you factory-reset the laptop without installation media, typically using 10 to 20 GB. If you have created HP recovery media on a USB drive first, deleting the partition is reasonably safe. Without recovery media, keep the partition — losing your only reset path to gain space is a bad trade."
  - q: "Which HP preinstalled programs are safe to remove?"
    a: "Generally safe to remove: HP JumpStart, HP games and trials, bundled antivirus trials you do not use, and duplicate utilities. Keep: HP Support Assistant (for driver updates), audio and graphics control panels, and anything related to fingerprint readers or special hardware buttons. When in doubt, research the specific program name before uninstalling."
  - q: "How much free space does an HP laptop need to update Windows?"
    a: "Feature updates typically need 10 to 20 GB of free space to download and stage, plus headroom for the Windows.old rollback copy. If an update fails with a space error, free at least 20 GB before retrying. Persistent update failures on small drives are one of the most common HP support complaints."
---

HP laptops have a particular relationship with full C: drives. Many ship with modest 128 GB or 256 GB SSDs, and HP preloads them generously — Support Assistant, JumpStart, audio software, recovery partitions, and bundled trials all claim their share before you install a single program of your own. The result is the red drive bar appearing far sooner than on a clean Windows install, often accompanied by failed updates and mysterious slowdowns.

The fix combines standard Windows cleanup with HP-specific steps: trimming the preinstalled software, dealing with the recovery footprint, and setting up automatic maintenance so the problem stays solved.

## Why this happens

- **Small factory SSDs:** 128 GB and 256 GB drives are common on HP consumer laptops, leaving little headroom once Windows and updates are accounted for.
- **Heavy preinstalled software:** HP's utility suite, bundled trials, and partner software can consume 10–20 GB before you add anything.
- **Recovery partition reservation:** The factory recovery environment permanently reserves 10–20 GB of the drive.
- **Windows Update staging:** Feature updates need large staging areas plus the Windows.old rollback copy — brutal on small drives.
- **HP Support Assistant caches:** Driver downloads, update packages, and diagnostic logs accumulate in HP's folders over time.
- **Hibernation and page files:** On HP laptops with 8–16 GB RAM, these hidden system files lock away many gigabytes.
- **OneDrive folder backup:** HP's setup flow encourages OneDrive backup of Desktop, Documents, and Pictures, mirroring cloud data onto the small C: drive.
- **Growing user caches:** Browser profiles, Teams, and chat apps cache gigabytes with no automatic ceiling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map where the space went

1. Open **Settings → System → Storage** and let it scan C: completely.
2. Note the biggest categories — on HP laptops the usual leaders are **Apps & features** (preinstalled software), **Temporary files**, and **System & reserved**.
3. Open **HP Support Assistant** and check its storage or tune-up section for HP-specific cleanup recommendations.
4. This map decides which fixes below earn your time; do not start deleting blindly.

### Fix 2: Remove HP bloatware you do not need

1. Go to **Settings → Apps → Installed apps** and sort by size.
2. Uninstall **HP JumpStart**, bundled game trials, antivirus trials you replaced, and any duplicate utilities (two photo apps, two cloud backups).
3. Keep **HP Support Assistant**, audio control panels, and hardware-specific tools (fingerprint, pen, special keys).
4. Restart after each batch of uninstalls. Typical savings: 5–15 GB. For the general technique, see [how to free up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/).

### Fix 3: Run the full Disk Cleanup pass

1. Search **Disk Cleanup**, run it as administrator, select C:, then click **Clean up system files**.
2. Check everything safe: **Temporary files**, **Recycle Bin**, **Delivery Optimization Files**, **Device driver packages**, **Temporary Windows installation files**, and **Previous Windows installations**.
3. The Previous Windows installations entry alone often frees 15–25 GB after a feature update.
4. Click OK and let it finish — do not interrupt it, or it may need to redo the pass.

### Fix 4: Clear HP Support Assistant's caches

1. Open **HP Support Assistant → Settings** and look for options to clear downloaded update files and diagnostic data.
2. Check `C:\ProgramData\HP` and `C:\SWSetup` (HP's driver staging folder) — SWSetup can often be deleted entirely after drivers are installed, freeing several gigabytes.
3. Empty the Recycle Bin afterward, since large deletions route through it.
4. Keep Support Assistant itself installed — it is genuinely useful for driver updates from [HP's official support site](https://support.hp.com/us-en).

### Fix 5: Decide on the recovery partition

1. Open **Disk Management** (right-click Start) and identify the **Recovery** partition — typically 10–20 GB at the end of the disk.
2. First, create recovery media: search **"Create a recovery drive"** in Windows or use HP's Cloud Recovery tool to build a bootable USB.
3. Only after verifying the USB boots and contains the recovery image, consider deleting the on-disk partition — and only if you desperately need the space.
4. For most users, keeping it is the right call. Deleting it is a one-way door without that USB in hand.

### Fix 6: Shrink the hidden system files

1. If you never hibernate: open an **admin Terminal** and run `powercfg /hibernate off` to delete hiberfil.sys (several GB).
2. Reduce System Restore: search **"Create a restore point"** → Configure → lower max usage to a few percent and delete old points.
3. For the page file on 16 GB+ systems: **Advanced system settings → Performance → Advanced → Virtual memory** — a fixed 2–4 GB page file frees space versus automatic sizing.
4. Never eliminate the page file completely; some HP utilities and crash diagnostics expect it to exist.

### Fix 7: Tame OneDrive and cloud sync

1. During HP's first-boot setup, OneDrive often enables folder backup silently. Open **OneDrive settings → Sync and backup → Manage backup** and review what is syncing.
2. Set large synced folders to **online-only** (right-click → Free up space) so they do not consume C: drive space.
3. If you do not use OneDrive at all, unlink it — but back up the local copies of Desktop/Documents/Pictures first, since unlinking can strand files.
4. Change your browser download folder to a second drive or external storage so downloads stop refilling C:.

### Fix 8: Automate so it stays fixed

1. Enable **Storage Sense** at **Settings → System → Storage** — weekly runs, 30-day Recycle Bin emptying, online-only aging for cloud files.
2. Schedule a monthly reminder to check **Settings → Storage** for new growth; HP updates and Windows updates are the usual re-fillers.
3. If the drive is a 128 GB model and you regularly fight for space, consider upgrading to a larger SSD — HP's [support site](https://support.hp.com/us-en) lists compatible parts for your exact model.
4. After upgrades or big cleanups, verify Windows Update runs successfully — a healthy update cycle is the real proof the space crisis is over. For update-specific bloat, see [low disk space after Windows 11 update](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/).

## Closing

HP laptops run out of C: space faster than most because they start with less and carry more — small factory drives plus a full preload. The remedy is equally specific: strip the HP software you do not need, sweep with Disk Cleanup, make a deliberate decision about the recovery partition, and let Storage Sense keep it clean afterward. The red bar disappears, updates install again, and the laptop stops feeling like it is running on fumes.
