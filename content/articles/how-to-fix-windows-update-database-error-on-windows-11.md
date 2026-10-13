---
title: "Windows Update Database Error on Windows 11? 7 Repairs That Work"
slug: how-to-fix-windows-update-database-error-on-windows-11
date: 2026-10-05
categories: ["windows-update"]
tags: ["database error", "windows update", "windows 11", "0x80070490", "repair"]
description: "Hitting a Windows Update database error on Windows 11? Rebuild the corrupted update database with these 7 repairs — most take under 20 minutes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-database-error-on-windows-11.webp"
faqs:
  - q: "What causes the Windows Update database error on Windows 11?"
    a: "The local update database — metadata in SoftwareDistribution, the DataStore, and component registrations — corrupts from interrupted updates, disk errors, overzealous cleaner tools, antivirus quarantining update files, or failing storage. Windows then cannot track what is installed or available, so checks fail with database-related codes like 0x80070490."
  - q: "Will resetting the update cache delete my installed updates?"
    a: "No. The cache reset deletes the tracking database and downloaded files, not the installed updates themselves. Windows rebuilds the database and re-registers existing updates automatically. You lose nothing except the downloaded copies, which re-download as needed — a small bandwidth cost for a clean ledger."
  - q: "How can I tell if my drive is causing the database corruption?"
    a: "Run chkdsk C: /f /r and check SMART status with wmic diskdrive get status. If chkdsk repairs bad sectors in the Windows folder area, or SMART reports anything but OK, the drive is implicated. A single corruption event after a force reboot is usually just the interruption; recurring corruption after clean rebuilds points at hardware."
  - q: "The database error keeps returning after I fix it. Why?"
    a: "Recurrence means the cause is still active: a failing drive re-corrupting the files, a cleaner tool or antivirus re-deleting them, or an interrupted update pattern repeating. Fix the cause — replace the drive, remove the cleaner, exclude update paths from antivirus, stop force-rebooting updates — not just the symptom."
---

On Windows 11, the "Windows Update database error" means Windows has lost track of its own updates. Every update check consults a local database — the DataStore, download metadata, package registrations — to decide what is installed, what is available, and what each package requires. When that database corrupts, the symptoms are distinctive: update checks fail outright, the troubleshooter reports a database error it may or may not fix, and error codes like 0x80070490 appear. Your actual installed updates are untouched; it is the record-keeping that broke.

The corruption triggers are well known: updates interrupted by force reboots, disk errors, third-party cleaner tools deleting update files, antivirus quarantines, and — on aging laptops — failing drives. The repair is a rebuild: clear the corrupted database, let Windows reconstruct it from clean metadata, and fix whatever corrupted it so it stays fixed. The seven steps below go from the quick rebuild to the deep repairs for stubborn cases.

## Why this happens

- **Interrupted updates.** Force reboots mid-install leaving the database half-written.
- **Disk errors.** Bad sectors or file-system damage in the database files.
- **Cleaner tool damage.** Third-party optimizers deleting update database files.
- **Antivirus quarantine.** Update components misidentified and removed.
- **DataStore corruption.** The DataStore.edb file damaged beyond self-repair.
- **Service registration issues.** The update engine's own registration data inconsistent.
- **Failing storage.** Hardware-level damage re-corrupting rebuilt databases.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter and capture the details

Start automated, but collect the evidence you will need for manual repair.

1. Run **Settings > System > Troubleshoot > Other troubleshooters > Windows Update**.
2. Note whether it reports the database error as detected-and-fixed or detected-but-unfixed.
3. Check **Settings > Windows Update > Update history** for the error code on recent failures (0x80070490 is the signature database code).
4. If the troubleshooter fixed it, run a manual update check to confirm. An unfixed detection means the corruption exceeds automated repair — the manual rebuild in Fix 2 is next.

### Fix 2: Rebuild the update database (the core repair)

Delete the corrupted database files and let Windows reconstruct them cleanly.

1. Open Terminal as administrator (right-click Start > **Terminal (Admin)**).
2. Stop the services:
   ```
   net stop wuauserv
   net stop bits
   net stop cryptsvc
   net stop msiserver
   ```
3. Rename the database folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
4. Restart all four services and check for updates. The first check is slower while metadata re-downloads. This single procedure fixes the large majority of database errors — if it worked, skip to Fix 7's prevention notes.

### Fix 3: Verify disk health

A corrupted database can be a symptom of a sick disk. Check the hardware.

1. Run `chkdsk C: /f /r` elevated — reboot to let it run if prompted; allow up to an hour on large drives.
2. Check SMART: `wmic diskdrive get status` — anything but "OK" means replace the drive.
3. Review chkdsk's results for bad sectors in Windows system areas — repaired sectors there explain the corruption.
4. If the disk is healthy and this was a one-time event after an interrupted update, the cause was the interruption, not hardware. If corruption recurs after Fix 2's clean rebuild, treat the drive as suspect and back up immediately.

### Fix 4: Re-register update engine components

Sometimes the database files are fine but the engine reading them is broken. Re-register its DLLs.

1. In an elevated prompt, run:
   ```
   regsvr32 wuapi.dll
   regsvr32 wuaueng.dll
   regsvr32 wups.dll
   regsvr32 wuwebv.dll
   ```
2. Confirm each success dialog before continuing.
3. Reset BITS: `bitsadmin /reset /allusers`.
4. Restart and check for updates. This fixes the cases where the troubleshooter reports database errors that survive a cache rebuild — the reader was broken, not the book.

### Fix 5: Repair the component store with DISM

Deep corruption that survives cache rebuilds and re-registration lives in the component store.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` elevated (15–30 minutes, uninterrupted).
2. Follow with `sfc /scannow` to 100%.
3. Restart, then redo the Fix 2 cache rebuild — healthy store first, fresh database second, in that order.
4. If DISM needs a source, mount a Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) and use `/Source:`. For the full store-repair context, our [servicing stack guide](/articles/how-to-fix-servicing-stack-update-failed-on-windows-11/) covers the related machinery.

### Fix 6: Eliminate the corruption source

A rebuilt database re-corrupts if the cause is still active. Remove it.

1. Uninstall third-party **cleaner/optimizer** tools — the leading deleters of update database files.
2. Test with third-party antivirus real-time protection temporarily disabled; if updates succeed, add permanent exclusions for update paths or switch to Windows Security.
3. Commit to never force-rebooting during updates — interruptions are the most common corruption cause and the most avoidable.
4. After removing the cause, rebuild the cache once more (Fix 2) so the new database is born clean. Our [troubleshooter repair guide](/articles/troubleshoot-windows-update-troubleshooter-not-working/) covers the diagnostic tools for verifying the pipeline stays healthy.

### Fix 7: In-place upgrade for unkillable corruption

When the database error survives every targeted repair, rebuild Windows around your data.

1. Back up important files first — the process preserves them, but verify the backup.
2. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run `setup.exe`, and choose **Keep personal files and apps**.
3. Let the upgrade complete — it reinstalls every system component, including the entire update database infrastructure.
4. Verify with a manual update check. Corruption cannot survive an in-place upgrade; if errors persist past this point, the storage hardware is at fault (return to Fix 3 and plan a drive replacement).

## Closing

The Windows 11 update database error is corrupted bookkeeping with a reliable fix sequence: rebuild the cache, check the disk, re-register the engine, repair the store, and eliminate whatever caused the corruption. The cache rebuild alone resolves most cases in minutes. And the long-term prevention is behavioral — no interrupted updates, no cleaner tools near system files, healthy disks — so the database stays clean and updates stay boring.
