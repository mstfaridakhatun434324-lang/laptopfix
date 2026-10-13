---
title: "How to Free Up Disk Space in Windows 11 24H2"
slug: how-to-free-up-disk-space-in-windows-11-24h2
date: 2026-09-15
categories: ["performance"]
tags: ["free up disk space", "windows 11 24h2", "storage", "disk cleanup", "c drive"]
description: "Running out of space on Windows 11 24H2? Free up gigabytes with the 24H2 storage tools, cleanup passes, and smart file moves."
thumbnail: "/images/thumbs/how-to-free-up-disk-space-in-windows-11-24h2.webp"
faqs:
  - q: "What's new for disk cleanup in Windows 11 24H2?"
    a: "24H2 continues the shift from the legacy Disk Cleanup tool toward Settings > System > Storage as the primary cleanup interface, with improved Storage Sense automation and better cleanup recommendations. The classic cleanmgr.exe still works in 24H2, but the Settings-based Temporary files cleanup and Storage Sense scheduling are the maintained path forward."
  - q: "How much space can I realistically recover?"
    a: "On a neglected system: 20–60 GB is typical. Windows Update cleanup and previous installations alone often yield 15–30 GB; temp files and caches another 5–15 GB; and user files (downloads, videos, installers) are unbounded — some people find 100+ GB of forgotten files. A well-maintained system might only yield a few GB, which is fine — it means there's nothing wrong."
  - q: "Is it safe to delete everything in Temporary files?"
    a: "The categories Windows lists under Settings > System > Storage > Temporary files are safe to remove — Windows only offers deletable categories there. The Downloads folder appears in that list too, so uncheck it if you store files there intentionally. Never manually delete the contents of C:\\Windows\\Temp or system folders outside these tools."
  - q: "Why does my disk fill up again after cleaning?"
    a: "Because the inflow never stopped: Windows Update staging, growing app caches (browsers, creative apps), cloud sync re-downloading, game updates, and restore points all refill the drive. Enable Storage Sense for automatic maintenance, move growing folders (game libraries, sync folders) off C:, and check monthly. Cleanup without changing habits is mopping with the tap running."
---

Windows 11 24H2 doesn't change the fundamentals of disk cleanup, but it does refine the tools — and on a version this mature, the old advice ("run Disk Cleanup") needs updating with the current best path through Settings. Whether you're fighting the red C: bar or just doing preventive maintenance, this is the complete 24H2 cleanup workflow: measure, clean system junk, triage your files, automate.

The order matters because each step is safer than the next: built-in tools first (zero risk), then your own files (your judgment), then structural changes (planning required). For the Acer-focused variant see [low disk space on Acer laptops](/articles/how-to-fix-low-disk-space-on-c-drive-on-acer-laptop/); for the related high-disk-usage-at-startup problem see [fixing high disk usage on startup](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-youtube/).

## Why this happens

- **24H2 update staging and rollback data**: Feature update payloads plus Windows.old consuming 20–30 GB.
- **Delivery Optimization cache**: Peer-to-peer update sharing hoarding gigabytes.
- **App caches growing unbounded**: Browsers, creative suites, and launchers caching without limits.
- **Hibernation file**: hiberfil.sys sized to a fraction of RAM, often 6–16 GB.
- **Restore points accumulating**: System Protection data growing on small drives.
- **Cloud sync set to always-local**: OneDrive/Dropbox mirroring cloud storage onto the disk.
- **Forgotten user files**: Downloads, installers, and videos accumulating for years.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map the drive with 24H2's Storage settings

Know before you delete.

1. Go to **Settings** > **System** > **Storage** — 24H2 shows a categorized bar: System & reserved, Apps & features, Temporary files, and your folders.
2. Click **Temporary files** and let it calculate — 24H2 itemizes Windows Update Cleanup, Delivery Optimization Files, thumbnails, and caches with individual sizes.
3. Click **Cleanup recommendations** (under Storage) — 24H2 suggests large unused files, unused apps, and synced-to-cloud files eligible for online-only status.
4. For the complete picture including hidden system folders, scan with **WizTree** (free, instant) — the treemap reveals hogs Settings doesn't itemize.
5. List your top space consumers — this drives every deletion decision below. Screenshot or note the numbers now; you'll compare against them after each cleanup pass to confirm what actually freed space versus what merely looked big.

### Fix 2: Run the 24H2 cleanup passes

The safe, official reclamation.

1. In **Settings** > **System** > **Storage** > **Temporary files**, check everything except **Downloads** (unless you've reviewed it), then **Remove files**.
2. The legacy tool still works: `cleanmgr.exe` > **Clean up system files** — select **Windows Update Cleanup**, **Previous Windows installation(s)** (if past rollback needs), **Device driver packages**.
3. In **Cleanup recommendations**, act on the suggestions: remove unused large files, uninstall unused apps directly from the list.
4. Typical first-pass yield on neglected 24H2 systems: 15–40 GB. Verify in File Explorer, and re-open the Storage page to confirm the Temporary files category actually dropped — occasionally a pending update lock prevents cleanup of some categories until after a reboot.
5. If Windows.old doesn't appear as removable, you're inside the 10-day rollback window — it auto-deletes after, or wait and re-run.

### Fix 3: Configure Storage Sense properly

Automate the maintenance.

1. **Settings** > **System** > **Storage** > **Storage Sense** → **On**.
2. Set it to run **Every week**; configure Recycle Bin auto-empty (30 days) and Downloads cleanup only if you don't use Downloads as archive (else **Never**).
3. Enable **OneDrive** cloud-content handling in Storage Sense — files unused locally become online-only automatically.
4. Click **Run Storage Sense now** for an immediate pass.
5. Storage Sense is maintenance, not rescue — it prevents recurrence after you've done the manual cleanup above.

### Fix 4: Shrink Windows' own footprint

Reclaim system-reserved gigabytes.

1. **Hibernation**: `powercfg /h off` in an elevated prompt deletes hiberfil.sys (frees ~40% of RAM size). Only if you never hibernate — note this disables Fast Startup too.
2. **Delivery Optimization**: **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** > **Advanced options** — cap the cache size; it defaults to hoarding gigabytes for peer sharing.
3. **System Protection**: `sysdm.cpl` > **System Protection** > **Configure** — reduce max usage to ~5% and delete all but the latest restore point.
4. **Optional features**: **Settings** > **System** > **Optional features** — remove language packs, handwriting, and features you never use.
5. Check **Settings** > **Apps** > **Installed apps** sorted by size — uninstall the big unused ones; 24H2's list makes the worst offenders obvious.

### Fix 5: Triage your personal files

The unbounded category.

1. Sort **Downloads** by size — delete installers for already-installed software; they're re-downloadable.
2. Search the drive for large media (`*.mp4`, `*.mkv`, `*.iso`) sorted by size — move keepers to external/secondary storage.
3. Right-click OneDrive/Dropbox heavy folders > **Free up space** (online-only) — files stay accessible, disk space returns.
4. Check game launchers: move Steam libraries to another drive (**Settings** > **Storage** > per-game **Move**); reinstall Epic games to the new location.
5. Empty the Recycle Bin last — deletions don't free space until you do — then confirm the new free-space total.

### Fix 6: Structural moves for small drives

When the drive is simply too small for the workload.

1. Move user folders: right-click **Documents**, **Pictures**, **Videos** > **Properties** > **Location** > **Move** to a second drive — future files land there automatically.
2. If C: has adjacent unallocated space, extend it in **Disk Management** (`diskmgmt.msc` > right-click C: > **Extend Volume**).
3. Consider a larger SSD — 256 GB is cramped for 24H2 plus apps in 2026; 512 GB is the comfort minimum, 1 TB the sweet spot.
4. After any drive change, re-run the storage analysis — confirm the new layout actually solved the pressure.
5. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the 24H2 storage tools officially if you want the reference details.

## Closing

Freeing disk space on 24H2 is a workflow, not a button: map with Storage settings, clean with the built-in passes, shrink Windows' footprint, triage your files, automate with Storage Sense. Most systems recover 30–80 GB in an hour. And the maintenance lesson: check **Settings** > **System** > **Storage** monthly, keep Storage Sense on, move growing libraries off C: before they become emergencies, and never let C: be the everything drive — the red bar is optional.
