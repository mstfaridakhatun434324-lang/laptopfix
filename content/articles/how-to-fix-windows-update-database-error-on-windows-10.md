---
title: "Fix Windows Update Database Error on Windows 10 (7 Proven Repairs)"
slug: how-to-fix-windows-update-database-error-on-windows-10
date: 2026-09-27
categories: ["windows-update"]
tags: ["database error", "windows update", "windows 10", "0x80070490", "repair"]
description: "Windows 10 reporting a Windows Update database error? These 7 repairs fix the corrupted update database — from cache rebuilds to component store surgery."
thumbnail: "/images/thumbs/how-to-fix-windows-update-database-error-on-windows-10.webp"
faqs:
  - q: "What does 'Windows Update database error' actually mean?"
    a: "It means the local database Windows Update uses to track available and installed updates — stored in the SoftwareDistribution folder and related catalogs — has become corrupted. Windows can no longer reliably determine what is installed or what it needs, so update checks fail or produce database-related error codes like 0x80070490."
  - q: "What causes the update database to corrupt?"
    a: "Interrupted updates (force reboots mid-install), disk errors, third-party 'cleaner' tools deleting update files, antivirus quarantining update components, and failing storage are the common causes. On older Windows 10 laptops with aging drives, bad sectors in the update database area are a frequent underlying trigger."
  - q: "Will fixing the database delete my installed updates?"
    a: "No. The repairs in this guide rebuild the tracking database, not the installed updates themselves. Your installed updates remain in place; Windows simply re-registers them cleanly. In the worst case, Windows re-downloads update metadata — a minor bandwidth cost, not a system rebuild."
  - q: "How do I prevent the database error from coming back?"
    a: "Never force-reboot during updates, keep at least 20 GB free on C:, run periodic disk health checks, avoid aggressive third-party cleaner tools, and keep your storage drivers current. Recurring database corruption on the same machine often points to a failing drive — check its SMART health if the error returns."
---

The "Windows Update database error" message on Windows 10 is Windows telling you its bookkeeping is broken. Behind every update check is a local database — download metadata in the SoftwareDistribution folder, the update catalog, registration entries — that tracks what is installed, what is available, and what each package needs. When that bookkeeping corrupts, Windows Update cannot figure out what to do: checks fail, error codes like 0x80070490 appear, and the troubleshooter may report it detected a "database error" it cannot fix. Your installed updates are fine; it is the ledger that is damaged.

The corruption sources are familiar: an update interrupted by a force reboot, disk errors, an overzealous cleaner tool deleting update files, or antivirus quarantining components. The repairs rebuild the ledger from scratch — Windows re-downloads clean metadata and re-registers everything. Work through the seven below in order; the early ones fix most cases, and the later ones handle the stubborn corruption that survives a cache reset.

## Why this happens

- **Interrupted updates.** Force reboots mid-install leave the database half-written.
- **Disk errors or bad sectors.** Physical storage damage in the database files.
- **Aggressive cleaner tools.** Third-party utilities deleting SoftwareDistribution contents mid-operation.
- **Antivirus quarantine.** Security software removing update components it misidentified.
- **Corrupted DataStore.** The DataStore.edb file itself damaged beyond automatic repair.
- **Service state corruption.** The update services' registration data inconsistent.
- **Failing drive.** Recurring corruption is often the first symptom of dying storage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter and note the exact error

Start with the automated diagnosis and capture the details you will need.

1. Run **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update**.
2. Note exactly what it reports — "database error detected" versus "database error fixed" changes the plan.
3. Also note any error code from **Settings > Update & Security > Windows Update > View update history** (0x80070490 is the classic database code).
4. If the troubleshooter fixed it, run one manual update check to confirm. If it detected but could not fix the error, continue — the manual rebuild below does what the automated tool cannot.

### Fix 2: Rebuild the update cache (the core fix)

This is the repair that resolves most database errors: delete the corrupted database files and let Windows rebuild them clean.

1. Open Command Prompt as administrator.
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
4. Restart all four services with `net start`, then check for updates. Windows rebuilds the database from scratch — the first check takes longer than usual while it re-downloads metadata. This single fix resolves the large majority of database errors.

### Fix 3: Check disk health

If the database corrupted once, make sure the disk is not the reason — especially on older laptops.

1. In an elevated prompt, run `chkdsk C: /f /r` — schedule it for the next restart if prompted, then reboot and let it complete (it can take an hour or more on large drives).
2. Check SMART health: in an elevated prompt, run `wmic diskdrive get status` — anything other than "OK" means the drive is failing.
3. If chkdsk found and repaired bad sectors in the Windows folder area, the database error was likely physical — monitor for recurrence.
4. Recurring database corruption after a clean rebuild is a strong failing-drive signal: back up your data and plan a drive replacement (ideally an SSD upgrade) rather than fighting symptoms.

### Fix 4: Re-register the update components

Database errors sometimes come with corrupted component registration. Re-register the DLLs the update engine depends on.

1. In an elevated Command Prompt, run these one at a time:
   ```
   regsvr32 wuapi.dll
   regsvr32 wuaueng.dll
   regsvr32 wups.dll
   regsvr32 wuwebv.dll
   regsvr32 atl.dll
   ```
2. Confirm each reports success before continuing.
3. Then reset the BITS queue: `bitsadmin /reset /allusers`.
4. Restart and check for updates. Re-registration fixes the cases where the database files are fine but the engine reading them is broken.

### Fix 5: Repair the component store with DISM

When cache rebuilds and re-registration fail, the corruption extends into the component store.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt (15–30 minutes).
2. Follow with `sfc /scannow` to full completion.
3. Restart, then repeat the Fix 2 cache rebuild — in that order: healthy store first, then fresh database.
4. If DISM cannot find sources, use a Windows 10 ISO as the source via `/Source:`. For related store-level failures, our [servicing stack repair guide](/articles/how-to-fix-servicing-stack-update-failed-on-windows-10/) covers the deeper machinery — and the [Windows 11 database error guide](/articles/how-to-fix-windows-update-database-error-on-windows-11/) documents the same repair pattern on the newer OS.

### Fix 6: Remove interfering third-party software

Cleaners and aggressive antivirus are repeat offenders for database corruption — remove the cause, not just the symptom.

1. Uninstall any third-party "PC cleaner" or "optimizer" tools — these are the most common deleters of update database files.
2. Temporarily disable third-party antivirus real-time protection and check whether updates now succeed; if so, add exclusions for the update paths or switch to Windows Security.
3. Rebuild the cache once more (Fix 2) after removing the interfering software, so the new database is built in a clean environment.
4. Going forward, let Windows manage its own update files — manual or third-party deletion of SoftwareDistribution contents while services run is a classic corruption recipe.

### Fix 7: In-place upgrade as the final rebuild

For database corruption that survives everything, rebuild the Windows installation while keeping your data.

1. Back up your important files (the process preserves them, but a backup is mandatory before system-level surgery).
2. Download the Windows 10 ISO via Microsoft's media creation tool from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) (select the Windows 10 tool).
3. Mount the ISO, run `setup.exe`, choose **Keep personal files and apps**, and let the upgrade complete.
4. Afterward, verify updates work with a manual check. An in-place upgrade reinstalls every system component including the update database — corruption cannot survive it. If problems persist even after this, the drive itself is the prime suspect (see Fix 3).

## Closing

The Windows Update database error is a bookkeeping failure, and the fix is re-ledgering: rebuild the SoftwareDistribution cache, verify the disk underneath it, re-register the components, and repair the store if needed. The cache rebuild alone fixes most cases in ten minutes. And the prevention is simple — never interrupt updates, keep disk space healthy, and keep cleaner tools away from Windows' own files — so the database never corrupts again.
