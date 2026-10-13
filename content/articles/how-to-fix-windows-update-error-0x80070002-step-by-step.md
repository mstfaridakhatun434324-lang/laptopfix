---
title: "Fix Windows Update Error 0x80070002: Complete Step-by-Step Guide"
slug: how-to-fix-windows-update-error-0x80070002-step-by-step
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows update", "0x80070002", "step by step", "troubleshooting"]
description: "A complete step-by-step walkthrough to fix Windows Update error 0x80070002 — from diagnosis to permanent repair, no guesswork."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070002-step-by-step.webp"
faqs:
  - q: "What does 0x80070002 mean in plain English?"
    a: "It means 'the system cannot find the file specified.' During Windows Update, the installer looks for the downloaded update packages it expects in its cache; when those files are corrupted, partial, or missing, it reports this error instead of a helpful message. The fix is to remove the damaged files and let Windows download fresh copies, which is exactly what the step-by-step sequence above does."
  - q: "Do I need to repeat these steps for every update?"
    a: "No. The repair targets the shared update cache and database that all updates use, so one successful pass fixes the pipeline for every pending update at once. After the repair, Windows re-downloads all queued updates cleanly. Only if the error returns for new updates later would you repeat the process — and recurrence points to a disk or network cause worth investigating."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes. It contains only temporary update downloads and the tracking database — no personal files, no installed updates, no settings. Windows recreates the folder structure automatically on the next update scan. Renaming it to .old instead of deleting is the cautious variant used in this guide; either way, the effect is a clean slate for the update engine."
  - q: "What if 0x80070002 appears during a feature update?"
    a: "The same repair sequence applies, because feature updates use the same download cache and servicing machinery. Clear the cache and reset the components first, then retry the feature update. If it still fails, the manual route — the Installation Assistant or installation media from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) — bypasses the cache entirely."
---

If you want the definitive, no-guesswork procedure for error 0x80070002, this is it. Rather than a menu of things to try, this guide is a single ordered sequence: each step builds on the last, each has a clear success check, and you stop the moment the error is gone. No step is destructive, and none touches your personal files.

Error 0x80070002 means the update installer cannot find files it expects — in practice, a corrupted download cache. The sequence below clears that corruption, verifies the repair held, and then hardens the system against recurrence. Follow it top to bottom and the error resolves.

This sequence assumes a standard single-drive Windows installation with no exotic configuration — which covers the vast majority of laptops. If your system uses a dual-boot setup, a heavily customized partition layout, or third-party disk encryption, mention that to anyone helping you, because those setups add variables this sequence does not cover.

## Why this happens

- **Corrupted files in the download cache:** Partial or damaged update packages in the SoftwareDistribution folder fail verification, producing the missing-file error on every install attempt.
- **Inconsistent update database:** The DataStore index can point at files that no longer exist, so the installer looks for packages that are not really there.
- **Interrupted first download:** Sleep, network loss, or shutdown during the initial download leaves fragments that poison subsequent retries.
- **Disk-level corruption:** File system errors damage cached packages after successful download, recreating the error even with a perfect network.
- **Security software interference:** Quarantined or blocked update components vanish from the cache, and the installer reports them as missing.
- **Wrong system time:** Clock skew breaks the secure download verification, so packages arrive in a state the installer rejects as invalid.
- **Stuck BITS jobs:** Jammed Background Intelligent Transfer Service jobs leave downloads in limbo, neither complete nor restartable, until the queue is reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1 — Record the error and affected updates

Precision first. Open Settings, Windows Update, Update history, and write down every update showing 0x80070002. Consistent failure across multiple updates confirms the cache diagnosis; a single failing update might instead be a bad package you can install manually. If just one package fails while everything else succeeds, [cumulative update install failures](/articles/how-to-fix-cumulative-update-fails-to-install-after-windows-11-update/) covers package-specific causes.

1. Open Update history and list each failed update with its code.
2. Confirm 0x80070002 is the consistent error.
3. Note the update types — cumulative, driver, or feature — for later reference.
4. Do not click Retry yet; you will retry after the repair.

### Fix 2: Step 2 — Stop the update services

Files in use cannot be deleted reliably. Stopping the four update-related services releases every lock on the cache folders so the cleanup in the next step is complete.

1. Open Command Prompt as administrator.
2. Run net stop wuauserv.
3. Run net stop cryptSvc.
4. Run net stop bits and net stop msiserver.

### Fix 3: Step 3 — Clear the download cache and reset the database

This is the core repair. Deleting the corrupted downloads and renaming the tracking database forces Windows to rebuild both from scratch — clean files, clean index, no inherited corruption.

1. Delete all contents of C:\Windows\SoftwareDistribution\Download.
2. Rename C:\Windows\SoftwareDistribution\DataStore to DataStore.old.
3. Rename C:\Windows\System32\catroot2 to catroot2.old.
4. Leave the folders otherwise intact; Windows recreates what it needs.

### Fix 4: Step 4 — Restart the services and rescan

With clean folders in place, restart the services and let Windows Update perform a full fresh scan. This scan rebuilds the database and queues clean downloads of everything pending.

1. Run net start wuauserv, net start cryptSvc, net start bits, net start msiserver.
2. Open Settings, Windows Update, and click Check for updates.
3. Allow the scan to complete without putting the laptop to sleep.
4. Install the offered updates and confirm 0x80070002 no longer appears.

### Fix 5: Step 5 — Verify the disk if the error returns

A recurring 0x80070002 after a clean rebuild means something is re-damaging the files. The disk check finds file system corruption or bad sectors doing exactly that.

1. In an elevated prompt, run chkdsk C: /f.
2. Restart when prompted and let the check finish.
3. After booting, repeat steps 2 through 4 once.
4. If the error stays gone, the disk was the root cause.

### Fix 6: Step 6 — Repair system files and harden the setup

The final hardening pass repairs the update engine itself and removes the common recurrence triggers: wrong clock, jammed BITS queue, and interfering security software. Finish with one automated pass: the [Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) catches anything the manual sequence missed. Microsoft’s [Windows support pages](https://support.microsoft.com/en-us/windows) publish error-code-specific guidance worth checking against your code.

1. Run DISM /Online /Cleanup-Image /RestoreHealth, then sfc /scannow.
2. Enable Set time automatically in Date and time settings.
3. Run bitsadmin /reset /allusers to clear any jammed transfer jobs.
4. Check the antivirus quarantine for update files and add exclusions if it keeps flagging them.

### Fix 7: Step 7 — Install the last stubborn package manually

Occasionally the repair succeeds generally but one specific package still fails with 0x80070002 because that package's metadata is bad on Microsoft's side rather than yours. For that last holdout, bypass the pipeline: download the package directly from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it by hand.

1. Note the KB number of the remaining failing update.
2. Search for it on the Microsoft Update Catalog site.
3. Download the x64 package and run it as administrator.
4. Verify the install in Update history afterward.

## Closing

Error 0x80070002 yields to procedure: record, stop, clear, restart, rescan, and verify. Each step has a purpose, none risks your data, and the success check at step 4 tells you immediately whether the repair held. Follow the sequence exactly as written and this error stops being a recurring headache — permanently.
