---
title: "Windows Update Error 0x80246007: A Complete Step-by-Step Repair Guide"
slug: how-to-fix-windows-update-error-0x80246007-step-by-step
date: 2026-09-10
categories: ["windows-update"]
tags: ["windows update", "error 0x80246007", "windows 11", "troubleshooting", "step by step"]
description: "Error 0x80246007 means the Windows Update database is corrupted. Follow this ordered 7-step guide to rebuild it, verify the repair, and resume updating."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-step-by-step.webp"
faqs:
  - q: "What exactly is the Windows Update database?"
    a: "It is a small local database Windows maintains to track update metadata: which packages are downloaded, installed, pending, or failed. The engine consults it before every operation. When the file is corrupted, the engine cannot trust its own records and aborts with 0x80246007 until the database is rebuilt."
  - q: "Is it safe to rename the catroot2 folder?"
    a: "Yes, when the cryptographic services are stopped first. Windows regenerates catroot2 automatically with fresh signature catalogs. Never delete it while services are running, and never delete it permanently — renaming keeps a fallback copy in case you need to revert. The .old copy lets you revert in the unlikely event something goes wrong."
  - q: "How long does the database rebuild take?"
    a: "The first update scan after a rebuild typically takes 10 to 20 minutes because Windows re-scans the entire system to reconstruct the index. Let it finish uninterrupted. Subsequent scans return to normal speed once the fresh database is populated."
  - q: "Can third-party antivirus cause this error?"
    a: "Yes. Real-time scanners that lock the database file during a write can corrupt it. If you see 0x80246007 repeatedly, add the SoftwareDistribution folder to your antivirus exclusions or test with the third-party scanner temporarily disabled to identify the culprit."
---

Error 0x80246007 translates to a corrupted Windows Update database. Deep inside Windows, a small database file tracks every update transaction — what is downloaded, what is installed, what is pending. When that file is damaged, the update engine cannot reconcile its own state and aborts with this code. The trigger is usually an interrupted update: a forced shutdown, a sleep event during install, or a disk error at exactly the wrong moment.

Here is the reassuring part: the database is disposable. Windows rebuilds it automatically whenever it is missing, re-scanning your system to reconstruct the index. So the core repair is simple — delete the corrupted file and let Windows start over. The steps below add verification at each stage so you know the rebuild actually happened, plus deeper repairs for cases where the corruption runs further than one file.

Do not waste time retrying the update before fixing the database. Every retry reads the same broken index and fails the same way.

## Why this happens

- **Torn database writes:** A shutdown, crash, or sleep event during a database write leaves the file structurally inconsistent.
- **Failed update leaving debris:** An update that installs halfway and rolls back can leave transaction records pointing at files that no longer exist.
- **File-system corruption:** Chkdsk-repairable errors on the system drive often manifest first as update database damage.
- **Security software file locks:** Real-time scanners occasionally lock the database file while the engine is writing to it.
- **Concurrent updaters:** Running a manufacturer updater and Windows Update at the same time can produce conflicting database entries.
- **Orphaned pending.xml entries:** The pending-operations list can reference updates that were already removed, confusing the engine.
- **Disk nearly full:** Database maintenance operations need scratch space; without it, they fail midway and corrupt the index.
- **Service crashes:** If the Windows Update service itself crashes mid-transaction, the database is left in an unknown state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the symptom and stop retrying blindly

Retrying against a corrupted database never succeeds — each attempt reads the same broken index. Confirm the diagnosis once, then commit to the rebuild. One failed retry is enough evidence.

1. Open Settings, then Windows Update, and note the exact error code 0x80246007.
2. Click Retry once and watch it fail the same way — this confirms a persistent, not transient, fault.
3. Do not click Retry again. Move to the troubleshooter step below.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter detects several database-corruption signatures and can reset components automatically. It is worth the two minutes before doing manual surgery. If the troubleshooter itself misbehaves, see [How to fix windows 11 stuck on restarting screen reddit](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-reddit/) for a dedicated walkthrough.

1. Go to Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its recommendations.
3. Restart the laptop.
4. Check for updates. If the code returns, proceed to the manual rebuild.

### Fix 3: Stop the update services in the right order

The database files are locked while services run, so they must be stopped before you can archive them. Stopping in dependency order avoids hangs.

1. Open Terminal (Admin).
2. Run: net stop wuauserv and wait for confirmation.
3. Run: net stop bits, then net stop cryptsvc.
4. Verify each reports that it stopped successfully before continuing.

### Fix 4: Archive the corrupted database folders

Renaming — never deleting — preserves a fallback copy. Windows notices the missing folders and regenerates a clean database and fresh signature catalogs automatically.

1. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
2. Run: ren C:\Windows\System32\catroot2 catroot2.old
3. Confirm both renames succeeded with no access-denied errors.
4. If a rename fails, reboot and repeat the service stops — something still holds a lock.

### Fix 5: Restart the services and trigger a rebuild

Starting the services with the old folders archived forces Windows to build a new database from scratch by re-scanning the system. The first scan is slow; that is normal.

1. Run: net start wuauserv, then net start bits, then net start cryptsvc.
2. Open Settings, then Windows Update, and click Check for updates.
3. Allow the scan to run to completion even if it takes 10 to 15 minutes.
4. Confirm 0x80246007 no longer appears.

### Fix 6: Repair underlying file damage with DISM and SFC

If corruption recurs, the damage extends beyond the database. DISM restores the component store from Windows Update, then SFC repairs protected system files against it. [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com) covers these tools in depth.

1. In Terminal (Admin), run: DISM /Online /Cleanup-Image /RestoreHealth
2. Wait for 100 percent — do not close the window early.
3. Run: sfc /scannow and let it finish.
4. Restart, then check for updates again.

### Fix 7: Install the failed KB manually, then verify

Finish the job by installing the update that originally triggered the corruption, using the [Microsoft's servicing guidance](https://support.microsoft.com/en-us/windows) standalone package, and confirm the system is healthy.

1. Find the failed KB number in Update history.
2. Download the matching x64 package from the Update Catalog.
3. Install it, restart, and confirm success in Update history.
4. Run one final Check for updates to confirm the queue is clear.

## Closing

With 0x80246007 cleared, the rebuilt database should serve you reliably from here on. Prevent a repeat by never forcing the laptop off during updates, keeping generous free disk space, and letting each update finish before starting another. For related failures, see [How to fix we couldn't complete the updates undoing changes on hp laptop](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop/) and [How to fix superfetch high disk usage on hp laptop](/articles/how-to-fix-superfetch-high-disk-usage-on-hp-laptop/). Treat the rebuilt database as a fresh start: adopt proper shutdown habits and generous free space from today onward, and it will stay healthy for years. One last habit seals the repair: after every Patch Tuesday, open Update history and confirm the new entries show success instead of assuming silence meant success — silent failures are how databases rot unnoticed. Caught early, a repeat is a five-minute cache clear; caught late, it is another full rebuild.
