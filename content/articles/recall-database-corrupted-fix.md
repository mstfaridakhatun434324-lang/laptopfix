---
title: "How to Fix a Corrupted Recall Database on Your Copilot+ PC"
slug: recall-database-corrupted-fix
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall database corrupted", "recall timeline blank", "troubleshooting", "ai pc", "windows 11 recall fix"]
description: "Recall showing a corrupted database error or a blank timeline? Follow this step-by-step guide to repair or rebuild Recall's snapshot database on Windows 11."
thumbnail: "/images/thumbs/recall-database-corrupted-fix.webp"
faqs:
  - q: "What causes the Recall database to become corrupted?"
    a: "The most common causes are interrupted Windows updates, forced shutdowns during snapshot writes, antivirus software locking database files, and disk errors. Because snapshots are written every few seconds, any crash mid-write can leave the file inconsistent."
  - q: "Will fixing the database delete my saved Recall snapshots?"
    a: "Repair operations preserve your snapshots whenever possible. But if the database is too damaged to repair, the rebuild step deletes it and Recall starts a fresh timeline. Note any important snapshots before the rebuild step, since old ones cannot be recovered afterward."
  - q: "How long does it take to rebuild the Recall database?"
    a: "Deleting and re-enabling Recall takes about five minutes, but the timeline starts empty. It can take several days of normal use before the new database becomes as searchable and useful as the old one."
  - q: "Can a corrupted database happen again after I fix it?"
    a: "Yes, if the underlying cause is not addressed. Keeping Windows updated, avoiding forced shutdowns, excluding Recall's data folder from third-party antivirus scans, and fixing disk errors all reduce the chance of it happening again."
---

When Recall stops opening its timeline or throws an error about its snapshot database, the culprit is often a corrupted database file. Recall stores your screenshots, text extractions, and searchable index in a local database on your Copilot+ PC. If it gets damaged, the timeline may load blank or the app may refuse to open — but the underlying snapshots are usually fine and only the index needs repair.

The stakes are straightforward: a broken database means Recall is useless until you act. The good news is that Windows 11 gives you a graduated path from gentle repair to full rebuild, so you can usually save your history without starting from scratch. This guide covers the most likely causes first, then walks you through six fixes.

Everything here applies to Copilot+ PCs running Windows 11 version 24H2 or later, which is where Recall is supported. If your PC doesn't meet the requirements in the first place, you may see a different failure entirely — for example, some users report [Recall not working with BitLocker enabled](/articles/recall-not-working-bitlocker-enabled/), which is a requirements issue rather than corruption, so check that article if the prerequisites sound unfamiliar.

## Why this happens

- **Interrupted Windows updates:** An update that reboots the PC while Recall is writing snapshots can leave the database file half-written and unreadable.
- **Forced shutdowns:** Holding the power button or a dead battery mid-write interrupts the database transaction, which is the single most common trigger.
- **Disk errors:** Bad sectors or file-system corruption on the drive holding the snapshot folder can silently damage database pages over time.
- **Antivirus interference:** Third-party security tools that lock or quarantine files in Recall's data folder can corrupt the index mid-operation.
- **Failed service restarts:** If the Recall background service crashes and restarts repeatedly, each aborted write increases the chance of inconsistency.
- **Disk-space pressure:** When the drive fills up during a snapshot write, the database cannot complete its transaction and may corrupt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Recall service and your PC

Many "corrupted database" errors are really a stuck service holding a lock on the file. A clean restart of both the service and the PC releases the lock and lets Recall reopen the database normally.

1. Press Ctrl + Shift + Esc to open Task Manager and look for Recall or related background processes.
2. End any Recall-related tasks, then restart your PC from the Start menu — do not use the power button.
3. After signing in, wait two minutes for startup services to settle before opening Recall.
4. Open Recall and check whether the timeline loads or the error is gone.

### Fix 2: Run a disk check on the system drive

If the file system itself has errors, the database file may be unreadable even though its contents are intact. Running Windows' built-in check repairs logical file-system problems safely.

1. Open Command Prompt as administrator by searching for "cmd" and choosing Run as administrator.
2. Type `chkdsk C: /f` and press Enter, replacing C: with your system drive letter if different.
3. If prompted to schedule the check at the next restart, type Y and press Enter.
4. Restart the PC and let the disk check complete — do not skip it.
5. After Windows boots, open Recall and verify the timeline loads.

### Fix 3: Repair the snapshot folder permissions

Recall's service runs under a specific account and needs full access to its snapshot folder. If permissions were changed by a migration, restore, or overzealous cleanup tool, the service may fail to write and report the database as corrupt when it is actually just inaccessible.

1. Open File Explorer and navigate to `%LocalAppData%` by typing it into the address bar.
2. Locate the folder holding Recall's data and right-click it, then choose Properties.
3. Go to the Security tab and confirm your user account and the SYSTEM account have full control.
4. If access looks wrong, click Advanced, then enable inheritance and apply the change to all subfolders.
5. Restart the PC and open Recall to test the timeline again.

### Fix 4: Exclude Recall data from third-party antivirus

Security software that scans or locks files while Recall is writing is a repeat offender for index corruption. Telling your antivirus to leave Recall's folder alone stops new damage from occurring and often lets the built-in repair complete successfully. Microsoft's own guidance covers [Windows security settings](https://support.microsoft.com/en-us/windows) if you need the official reference.

1. Open your third-party antivirus and find its exclusions or allow-list settings.
2. Add an exclusion for Recall's snapshot data folder under `%LocalAppData%`.
3. Also exclude the Recall service executable if the antivirus offers process exclusions.
4. Restart the PC so the exclusion takes effect before the service writes again.
5. Open Recall and check whether the error persists.

### Fix 5: Toggle Recall off and on to trigger a repair

Windows 11 can detect a damaged snapshot store when the feature is re-enabled and will attempt an automatic repair. Turning Recall off and back on forces this self-healing path.

1. Open Settings, then go to Privacy & security and find the Recall & snapshots page.
2. Toggle Recall off and wait for the status to fully update.
3. Return to the same Settings page and toggle Recall back on.
4. Open the timeline and confirm your snapshots and search are working again.

### Fix 6: Rebuild the database from scratch

When repair fails, deleting the snapshot store and letting Recall build a fresh database is the definitive fix. You will lose your old timeline, but a clean database restores full functionality. Some users confuse this with unrelated features misbehaving, like the [Copilot sidebar in Edge not working](/articles/copilot-edge-sidebar-not-working/), so make sure your actual problem is the database before taking this step.

1. In Settings, go to the Recall & snapshots page and toggle Recall off.
2. Open File Explorer, navigate to the Recall data folder under `%LocalAppData%`, and back up anything you want to keep.
3. Delete the snapshot database files from that folder.
4. Restart the PC, then return to Settings and toggle Recall back on.
5. Let Recall run for a few hours of normal use to start building the new index.
6. Confirm the timeline opens and new snapshots appear, then leave old errors behind.

## Closing

A corrupted Recall database is usually repairable without losing your history — most cases resolve with a service restart, a disk check, or the toggle-off-and-on repair. Only use the full rebuild when the earlier fixes have genuinely failed, and take prevention seriously afterward: keep Windows updated, shut down cleanly, and keep your antivirus away from Recall's data. For broader background on how Recall depends on your hardware, the guide on [NPU detection problems in Windows 11](/articles/npu-not-detected-windows-11/) is a useful companion read.
