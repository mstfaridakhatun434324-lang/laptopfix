---
title: "Windows Update Database Error? Repair It Step by Step"
slug: how-to-fix-windows-update-database-error-step-by-step
date: 2026-09-27
categories: ["windows-update"]
tags: ["database error", "datastore", "0x80070490", "step by step"]
description: "Seeing a Windows Update database error like 0x80070490? Follow this exact step-by-step repair sequence to rebuild the update database and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-database-error-step-by-step.webp"
faqs:
  - q: "What causes a Windows Update database error?"
    a: "The update database (the DataStore.edb file) tracks every update's state. It corrupts when updates are interrupted mid-write, when disk errors hit the file, when antivirus locks it during writes, or when failed updates leave inconsistent entries. Once corrupt, Windows Update misreads what's installed and every operation fails."
  - q: "What does error 0x80070490 mean?"
    a: "Error 0x80070490 (E_ELEMENT_NOT_FOUND) is the most common database error code — it means Windows Update looked for an update element in its database and couldn't find it. It typically appears when installing updates or upgrading, and it almost always traces back to a corrupted DataStore."
  - q: "Will resetting the update database delete my installed updates?"
    a: "No. Renaming SoftwareDistribution only clears the local tracking database and cached downloads — your actually-installed updates remain installed. Windows rebuilds the database by re-scanning the system. You'll need to re-download pending updates, but nothing already installed is ever lost."
  - q: "How do I prevent the update database from corrupting again?"
    a: "Avoid interrupting updates (no forced shutdowns mid-install), keep the system drive healthy with occasional chkdsk runs, don't let the drive fill completely, and be cautious with aggressive 'cleaner' tools that touch the SoftwareDistribution folder. Clean shutdowns during updates are the single biggest prevention."
---

# Windows Update Database Error? Repair It Step by Step

The Windows Update database is the ledger that records which updates are installed, which are pending, and which failed. When that ledger gets corrupted, Windows Update loses track of reality: it tries to install things already installed, can't find things it needs, and throws errors like 0x80070490 that send you in circles. Everything *looks* like it should work, but the bookkeeping is broken.

The repair is refreshingly mechanical. Unlike driver mysteries or hardware faults, a database error has a defined fix sequence: stop the services, replace the corrupt database files, restart, and re-scan. Follow the steps below exactly, in order, and the database rebuilds itself cleanly.

## Why this happens

- **Interrupted updates.** Forced shutdowns or power loss during an install leave the database half-written and inconsistent.
- **Disk errors.** Bad sectors or file system corruption hitting `DataStore.edb` damage the ledger directly.
- **Antivirus file locks.** Real-time scanners occasionally lock the database file mid-write, corrupting the transaction.
- **Failed updates leaving orphan entries.** An update that fails partway can leave database rows pointing at files that don't exist.
- **Aggressive cleaner tools.** Third-party cleaners that purge the SoftwareDistribution folder can delete files the database still references.
- **Running out of disk space mid-update.** When the drive fills during a database write, the write truncates and corrupts.
- **Aging database never rebuilt.** Years of update history accumulate cruft; the database grows fragile until something finally breaks it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm It's a Database Error and Run the Troubleshooter

Make sure you're fixing the right problem before rebuilding anything.

1. Note the exact error code in **Settings > Windows Update** — 0x80070490, 0x80070003, and 0x80248007 are classic database errors.
2. Run the Windows Update troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**. If the troubleshooter itself misbehaves, see [how to fix the update troubleshooter](/articles/how-do-i-fix-windows-update-troubleshooter-not-working/) first.
3. The troubleshooter specifically checks database consistency and repairs minor corruption automatically.
4. If it reports "Windows Update database error detected" and claims to fix it, retry the update immediately — minor corruption sometimes yields here.
5. If the troubleshooter fails or the error persists, continue — you'll be doing manually what it couldn't.

### Fix 2: Stop the Update Services Cleanly

You can't repair the database while services are writing to it — stop everything first.

1. Open an elevated Command Prompt.
2. Run these four commands, one at a time:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptsvc`
   `net stop msiserver`
3. Confirm each reports "stopped successfully" — if one hangs, wait 60 seconds; don't proceed with a service still writing.
4. Leave the Command Prompt open; you'll need it for the next steps.
5. Do not reboot between stopping and renaming — a reboot restarts the services and re-locks the files.

### Fix 3: Rename the Corrupt Database Folders

This is the core repair: move the damaged database aside so Windows builds a fresh one.

1. In the same elevated Command Prompt, run:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
2. Then rename the cryptography catalog store:
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. If a rename fails with "access denied," a service is still running — recheck Fix 2 and also stop any third-party service holding the folder.
4. Don't delete the `.old` folders yet — they contain your update history and serve as a backup if anything goes wrong.
5. These two folders hold the entire local update database; renaming them is the sanctioned way to force a rebuild.

### Fix 4: Restart Services and Trigger a Fresh Scan

With the corrupt database out of the way, restart the pipeline and let it rebuild.

1. In the elevated Command Prompt, restart the services:
   `net start wuauserv`
   `net start bits`
   `net start cryptsvc`
   `net start msiserver`
2. Open **Settings > Windows Update** and click **Check for updates**.
3. The first scan takes noticeably longer than usual — it's rebuilding the database by re-inventorying every installed update. Be patient.
4. Let the scan complete fully, even if it sits at a percentage for a while.
5. Check that the previous error code is gone; if updates now download, the database repair worked.

### Fix 5: Repair the Component Store Underneath

Sometimes the database was corrupted *by* deeper damage — fix the foundation so it doesn't recur.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` (15–40 minutes).
3. Follow with `sfc /scannow`.
4. Restart the laptop after both finish.
5. Run **Check for updates** once more to confirm the rebuilt database survives a full scan cycle on a healthy store. Database errors that keep returning usually mean the component store or disk is the real culprit — see our guide to [servicing stack failures](/articles/how-to-fix-servicing-stack-update-failed-step-by-step/) if the store itself won't repair.

### Fix 6: Check Disk Health

A database that corrupts repeatedly is often sitting on a disk that's failing underneath it.

1. Open an elevated Command Prompt and run `chkdsk C: /f`.
2. Agree to run at next restart, reboot, and let the full check complete.
3. Review the summary: bad sectors or file system errors found here explain recurring database corruption.
4. If chkdsk finds bad sectors, back up your data immediately and plan a drive replacement — no software fix outlasts dying storage.
5. On a healthy disk with a one-time corruption, you're done — the rebuilt database should serve for years.

### Fix 7: Reinstall Pending Updates and Clean Up

Finish the job: install what was blocked and remove the leftover backup folders.

1. With the database rebuilt, install all pending updates from **Settings > Windows Update**.
2. Restart when prompted and verify success in **Update history**.
3. Wait a week of normal update cycles to be sure the database stays healthy.
4. Then delete the backup folders: `C:\Windows\SoftwareDistribution.old` and `C:\Windows\System32\catroot2.old` — they can be several gigabytes.
5. Going forward, never force-shutdown during updates, and keep at least 15GB free on the system drive — the two habits that prevent most database corruption. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the current recommended update maintenance practices.

## Closing

Windows Update database errors look intimidating because the codes are cryptic, but the fix is one of the most reliable in all of Windows troubleshooting: stop the services, rename the corrupt stores, restart, and let Windows rebuild. It's mechanical, it's safe, and it works — your installed updates stay put while the bookkeeping gets a fresh start.
