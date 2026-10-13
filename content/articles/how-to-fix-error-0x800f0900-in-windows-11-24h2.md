---
title: "How to Fix Windows 11 Update Error 0x800f0900 (24H2)"
slug: how-to-fix-error-0x800f0900-in-windows-11-24h2
date: 2026-09-26
categories: ["windows-errors"]
tags: ["update error", "0x800f0900", "Windows 11 24H2"]
description: "Error 0x800f0900 blocking your Windows 11 24H2 update? Repair the component store corruption behind it with these steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x800f0900-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x800f0900 mean?"
    a: "It signals corruption in the Windows component store (CBS) — the internal database Windows uses to track system components. When update metadata or manifests are damaged, the installer can't verify what it's installing and fails with 0x800f0900."
  - q: "How is 0x800f0900 different from 0x800f081f?"
    a: "They're neighbors: 0x800f081f means repair source files are missing, while 0x800f0900 means the component store's own data is corrupted. In practice the fixes overlap heavily — DISM repairs both — but 0x800f0900 sometimes needs the store reset more aggressively."
  - q: "Will DISM fix 0x800f0900?"
    a: "Usually, yes — DISM /RestoreHealth is purpose-built for component store corruption. If it fails, point DISM at a Windows 11 ISO as an explicit source, which bypasses the damaged store's self-repair limitations."
  - q: "Can 0x800f0900 damage my personal files?"
    a: "No. Component store corruption affects Windows' internal bookkeeping, not your documents. And every repair here — DISM, SFC, update reset, in-place upgrade — is designed to preserve personal files and installed programs."
---
Error 0x800f0900 lives in the engine room of Windows Update: the Component-Based Servicing (CBS) store, the database that tracks every Windows component, its version, and its files. When that database gets corrupted — manifests damaged, metadata inconsistent — updates can't install because Windows can no longer verify the integrity of what it's doing. The installer gives up with 0x800f0900.

On 24H2, this tends to surface during cumulative updates or when enabling Windows features. The repair path is well-established: DISM exists precisely to heal the component store, and when DISM needs help, a Windows ISO provides it. Work the list below and the store will be healthy again.

## Why this happens

- **Interrupted updates or repairs.** A DISM run or update killed halfway through leaves the component store half-written — manifests updated but files not staged, or vice versa. The inconsistency then blocks everything after it.
- **Disk errors in the WinSxS area.** The component store lives in `C:\Windows\WinSxS`. Bad sectors or file-system corruption there damage exactly the metadata this error complains about.
- **Third-party cleaners stripping WinSxS.** "Debloating" tools and aggressive disk cleaners that delete component-store files to save space destroy the manifests Windows needs. The few gigabytes saved are never worth the resulting corruption.
- **Failed feature updates.** Major version upgrades rewrite large parts of the component store. If one fails midway and rolls back imperfectly, the store is left in the inconsistent state that produces 0x800f0900 on subsequent updates.
- **Malware or antivirus damage.** Malware targeting system files, or antivirus quarantining store components it misidentified, both corrupt the store's bookkeeping.
- **Manifest mismatches after manual tweaks.** Manually deleting files from WinSxS, editing the registry's component keys, or using unofficial "lite" Windows builds creates inconsistencies no automatic tool can fully reconcile.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Run DISM RestoreHealth

The purpose-built fix — let it do its job before anything exotic.

1. Press **Win + X** and open **Terminal (Admin)**.
2. First assess: `DISM /Online /Cleanup-Image /ScanHealth`. This reports whether the store is actually corrupted — no point repairing a healthy store.
3. If corruption is found, run: `DISM /Online /Cleanup-Image /RestoreHealth`. Stay online and give it 20–30 minutes without closing the terminal.
4. Follow with `sfc /scannow` to verify system files against the repaired store, then restart and retry the update.

### Fix 2: Run DISM with an ISO source

When the store is too damaged to repair itself from Windows Update, hand DISM pristine files.

1. Download the Windows 11 24H2 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) — it must match your installed build (**Settings > System > About**).
2. Double-click the ISO to mount it and note the drive letter (for example `E:`).
3. Check the image index: `dism /Get-WimInfo /WimFile:E:\sources\install.wim` — note the number for your edition.
4. Run the repair (adjust drive letter and index):
   `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\sources\install.wim:1 /LimitAccess`
5. On success, run `sfc /scannow`, restart, and retry the update. This ISO-source repair is also the answer to its close cousin [error 0x800f081f](/articles/how-to-fix-error-0x800f081f-in-windows-11-24h2/) if you ever meet that one.

### Fix 3: Reset the Windows Update components

A broken update pipeline can both cause and perpetuate store corruption — fix the pipeline too.

1. In **Terminal (Admin)**, stop the services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
2. Rename the caches:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
4. Retry `DISM /Online /Cleanup-Image /RestoreHealth` — with a clean pipeline, the default repair source may now work even if it failed before.

### Fix 4: Run chkdsk on the system drive

If disk errors caused the corruption, repair the disk or it'll corrupt the store again.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`.
2. Type `Y` when asked to schedule for next restart, then reboot and let it run fully — over an hour on large drives.
3. After chkdsk completes, re-run the DISM repair from Fix 1. Repairs done on a still-damaged disk don't stick; repairs done after chkdsk do.
4. If chkdsk reports many bad sectors, check the drive's SMART health (`wmic diskdrive get status`) — recurring store corruption on a failing drive means the drive needs replacing, not more repairs.

### Fix 5: Uninstall the update that triggered it, then reinstall cleanly

Sometimes one specific update's payload conflicts with your store state.

1. Go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update.
2. Restart, then run the DISM ISO-source repair (Fix 2) to get the store fully healthy.
3. Download the update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) via its KB number and install the `.msu` directly.
4. Installing onto a repaired store avoids the mismatch that triggered 0x800f0900 in the first place. Manual catalog installs also bypass the download-failure [error 0x80240034](/articles/how-to-fix-error-0x80240034-in-windows-11-24h2/).

### Fix 6: Remove the offending cleaner or debloater

If a third-party tool caused this, stop it from causing it again.

1. Think back: did you run a "PC cleaner," "debloater," or "Windows lite" tool before the errors started? If so, uninstall it via **Settings > Apps > Installed apps**.
2. Check whether it has an "undo" or "restore" function — some keep backups of what they removed.
3. After removal, run the DISM repair again to heal whatever the tool damaged.
4. Going forward, let Windows manage WinSxS itself — the built-in **Storage Sense** and `dism /online /cleanup-image /startcomponentcleanup` handle cleanup safely without breaking manifests.

### Fix 7: In-place upgrade as the definitive repair

When the store is beyond DISM's reach, reinstall Windows over itself.

1. Mount the 24H2 ISO and run **setup.exe**.
2. Choose **Keep personal files and apps** — the upgrade rebuilds the entire component store from the ISO's pristine files while preserving everything of yours.
3. Allow 30–60 minutes for the upgrade to complete.
4. Run Windows Update afterward. With a factory-fresh component store, 0x800f0900 has nothing left to complain about — this resolves it essentially every time.

## Closing

Error 0x800f0900 is Windows' bookkeeping going wrong, and like all bookkeeping problems, it's fixed by reconciling against a trusted source — which is exactly what DISM with an ISO does. The one habit I'd change after fixing this: stop letting third-party cleaners touch the WinSxS folder. Windows' component store looks like wasted space, but it's the spare-parts department for the entire operating system. Delete the spare parts and the next repair fails — which is precisely how many people meet 0x800f0900 in the first place.
