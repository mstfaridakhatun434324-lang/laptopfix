---
title: "Feature Update Stuck at 61% on a Lenovo Laptop: Unstick It"
slug: how-to-fix-feature-update-stuck-at-61-percent-on-lenovo-laptop
date: 2026-10-12
categories: ["windows-update"]
tags: ["stuck at 61", "feature update", "lenovo laptop", "frozen", "installation"]
description: "A Windows feature update frozen at 61% on your Lenovo laptop? Learn what the installer is doing at that point and how to get it moving."
thumbnail: "/images/thumbs/how-to-fix-feature-update-stuck-at-61-percent-on-lenovo-laptop.webp"
faqs:
  - q: "What is the installer actually doing at 61%?"
    a: "Around 61%, a feature update is typically in the driver and feature migration phase — moving drivers, migrating user profiles and settings, and configuring the new OS image. It's one of the slowest phases because it touches thousands of files and every installed driver. Apparent freezes here are often just very slow progress, which is why the waiting test in this guide comes first."
  - q: "How long is too long at 61%?"
    a: "Give it at least two hours at a fixed percentage before acting, longer on older spinning drives or very full systems. Check Task Manager for setup disk activity — if the disk is actively working, it's progressing. Only treat it as stuck when there's zero setup-related disk or CPU activity for a full hour and the percentage hasn't budged."
  - q: "Will interrupting a stuck 61% update break my laptop?"
    a: "Interrupting triggers Windows' automatic rollback, which returns you to your previous version — that's the designed safety net, not a disaster. The risk is small: occasionally the rollback itself needs help via the Recovery Environment. Never interrupt before confirming a genuine stall, because killing a working migration is what causes the rare bad outcomes."
  - q: "Why 61% specifically and not some other number?"
    a: "The percentages map to internal setup phases, and the early-60s correspond to the migration phase where the installer moves the most data and touches every driver. It's the phase most likely to hit a blocking condition — a hanging driver, a locked file, a full disk — so stalls cluster there. Different updates may stall at slightly different numbers for the same underlying reasons."
---

Sixty-one percent. The progress bar has not moved in two hours. Your Lenovo laptop sits there, fans occasionally spinning up, giving you no indication whether the feature update is crawling or dead. This is one of the most reported stall points in Windows upgrades, and it has a specific explanation.

At 61%, the installer is deep in the migration phase — moving drivers, user profiles, and settings into the new OS image. It is the most I/O-heavy, driver-touching part of the whole upgrade, which makes it both the slowest phase and the one most likely to wedge on a bad driver or a locked file.

This guide shows you how to tell slow from stuck, how to recover without damage, and how to fix the blocker so the retry sails through. Work through these in order — diagnose first, then act.

## Why this happens

- **Driver hanging during migration.** A Lenovo driver that will not migrate stalls the entire phase.
- **Antivirus locking migrated files.** Real-time protection blocking the file moves migration requires.
- **Disk I/O bottleneck.** A nearly-full or degrading drive turns migration into a crawl that looks frozen.
- **Corrupted migration data.** Damaged user profile or driver store entries the migrator cannot process.
- **Insufficient working space.** Migration needs temp room; exhaustion mid-phase stalls instead of erroring.
- **Lenovo utility interference.** Vantage or system utilities locking components being migrated.
- **Failing storage hardware.** Bad sectors in the migration path causing retries that never complete.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The two-hour rule — verify before you touch

Do nothing for at least two hours from the moment you noticed the freeze. During that time, check Task Manager (if you can reach it via Ctrl+Shift+Esc) for setuphost.exe disk activity, and watch the drive activity light.

Sustained disk activity means migration is working — slowly. The migration phase on a full 512 GB drive with years of accumulated drivers can legitimately take hours. Only proceed when you have a full hour of zero setup-related activity with an unmoving percentage. This discipline is what separates a successful slow upgrade from a self-inflicted rollback.

### Fix 2: Force shutdown and let rollback or resume happen

After confirming the stall, hold the power button 5-10 seconds until the machine powers off. Wait 30 seconds, then power on. Windows detects the interrupted upgrade and either resumes it or rolls back with "Undoing changes" / "Restoring your previous version."

Let whichever process starts finish completely — do not interrupt the rollback. If it boots normally to your old version, the safety net worked. If it loops or fails to boot, interrupt boot three times to reach the Recovery Environment and use "Uninstall latest feature update." The rollback experience is detailed in the [undoing changes guide](/articles/what-to-do-if-we-couldn-t-complete-the-updates-undoing-changes/).

### Fix 3: Update Lenovo drivers and BIOS before retrying

The 61% stall is a migration stall, and migration stalls are driver stalls. Open Lenovo Vantage — or [Lenovo support](https://support.lenovo.com/us/en/) — and install every pending BIOS and driver update: chipset, storage, graphics, network.

Storage drivers deserve special attention at this stall point, since migration is I/O-heavy and a flaky storage driver wedges exactly here. Keep the charger connected during the BIOS flash. Restart normally once and confirm clean booting before you let the feature update try again. Current drivers migrate; outdated ones hang.

### Fix 4: Remove antivirus and free substantial disk space

Uninstall third-party antivirus with its removal tool — file locks during the file-move-heavy migration phase are a direct stall cause. Then free space aggressively: target 25+ GB free on C: for a feature update retry, using Storage Sense, temp-file cleanup, and removing the previous Windows installation.

Migration stages enormous amounts of data; a drive with 8 GB free will stall where a drive with 30 GB free sails through. Verify the free space in File Explorer — do not estimate. These two steps (no file locks, plenty of room) remove the most common non-driver stall causes.

### Fix 5: Check disk health thoroughly

A degrading drive stalls migration on bad sectors with endless retries. Run `chkdsk C: /f /r` from an elevated Command Prompt — the /r locates bad sectors and recovers readable information; schedule it at restart and let it complete (it takes a while on large drives).

Check SMART status via Lenovo's diagnostics or a third-party SMART tool. Reallocated sectors or pending-sector counts trending upward mean the drive is the problem, not the update — and no software fix will make migration reliable on failing storage. If the disk is healthy and chkdsk is clean, you have eliminated the hardware angle. Microsoft documents disk checking in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 6: Clean boot and minimal peripherals for the retry

Strip the migration path to essentials: unplug all USB devices, SD cards, docks, and external displays. Then clean boot — Win+R, `msconfig`, Services tab, hide Microsoft services, disable all; Task Manager Startup tab, disable all; restart.

Fewer drivers in the migration set means fewer chances for one to hang the phase. Retry the feature update in this minimal state. If it passes 61% this time, re-enable services in halves afterward to identify what was hanging — the culprit is usually a third-party driver or utility you can then update or remove. For the broader retry checklist, the [feature update failure guide for Lenovo](/articles/how-to-fix-feature-update-to-windows-11-failed-on-lenovo-laptop/) is the companion piece.

### Fix 7: ISO-based upgrade with the migration bottleneck removed

If the Windows Update path stalls at 61% twice despite preparation, switch to the ISO method: download the Windows 11 ISO from the [official Microsoft download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run setup.exe keeping files and apps.

Before launching, do one more targeted cleanup: in Device Manager, uninstall any devices showing warnings (with driver removal), letting Windows use baseline drivers for the migration. The ISO setup engine handles the migration phase more robustly, and fewer exotic drivers in the set means less to hang on. This combination gets past 61% in nearly all remaining cases.

## Closing

The 61% stall is the migration phase hitting something it cannot move past — usually a hanging driver, sometimes a full or failing disk. Verify the stall with the two-hour rule before interrupting, let the rollback safety net do its job, then fix the actual blocker: current Lenovo drivers and BIOS, no antivirus locks, 25 GB free, healthy disk, minimal peripherals. Migration is the hardest part of the upgrade; give it a clean path and it completes.
