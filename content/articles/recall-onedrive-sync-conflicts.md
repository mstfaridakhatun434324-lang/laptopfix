---
title: "How to Fix Recall and OneDrive Sync Conflicts on Windows 11"
slug: recall-onedrive-sync-conflicts
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall onedrive conflict", "recall sync error", "windows recall", "onedrive troubleshooting", "copilot plus pc", "windows 11"]
description: "Recall clashing with OneDrive sync on your Copilot+ PC? Learn why the two fight over files and storage, and the step-by-step fixes that end the conflict."
thumbnail: "/images/thumbs/recall-onedrive-sync-conflicts.webp"
faqs:
  - q: "Do Recall snapshots get uploaded to OneDrive?"
    a: >
      No. Recall snapshots stay on your local drive and are protected by encryption tied to your device. OneDrive never syncs the snapshot store — the conflict is about disk activity and file locks, not your snapshots leaving the PC.
  - q: "Can I exclude Recall from OneDrive backup?"
    a: >
      There is nothing to exclude: Recall's snapshot database lives outside the folders OneDrive backs up. Focus on pausing sync during heavy batches and keeping free space healthy instead.
  - q: "Will pausing OneDrive delete my files?"
    a: >
      Pausing sync only stops transfers temporarily. Your local files stay exactly where they are, and syncing resumes from where it stopped. It is one of the safest troubleshooting steps you can take.
  - q: "Should I move my OneDrive folder to another drive?"
    a: >
      On PCs with a second drive, relocating the OneDrive folder can genuinely reduce contention on the system SSD. It is optional, though — throttling sync and freeing space solves most conflicts without the move.
---

Recall is meant to run quietly in the background, capturing snapshots while you work. OneDrive is meant to run quietly in the background, syncing your files to the cloud. Most of the time they ignore each other — but on some Copilot+ PCs the two end up fighting over the same files, and Recall capture starts stuttering, pausing, or throwing errors.

The clash usually centers on file locks and storage pressure: OneDrive syncing a large batch of files can spike disk activity just as Recall tries to write snapshots, or Known Folder Move can relocate folders Recall was monitoring. It is a resource conflict, not a fundamental incompatibility — and the same kind of background-service pileup also shows up as [Studio Effects in Discord calls](/articles/studio-effects-discord-calls/), where two camera features compete for one pipeline.

This guide walks you through six fixes: confirming the conflict is real, calming OneDrive down, protecting Recall's storage, and stabilizing both services so they can coexist. You will not lose files or snapshots if you follow the order below.

## Why this happens

- **File locks during heavy sync:** When OneDrive syncs large uploads or downloads, it locks files and folders it is processing. If Recall tries to snapshot an app reading those files, the capture can fail or stall — [Recall snapshots not saving](/articles/recall-snapshots-not-saving/) has the same underlying pattern when any background process interrupts capture.
- **Disk I/O saturation:** A big OneDrive sync batch plus Recall snapshot writes can saturate a slower SSD. Capture timing slips, snapshots get skipped, and Recall may report itself paused.
- **Known Folder Move relocating watched folders:** If OneDrive's backup feature moved your Desktop, Documents, or Pictures folders, apps and their file paths change — and Recall's timeline entries can point at locations that no longer exist locally.
- **Files On-Demand placeholders:** Cloud-only placeholder files force a download the moment something touches them. A snapshot-triggered read of a placeholder can hang the capture briefly while OneDrive fetches the file.
- **Storage pressure from both sides:** OneDrive keeping local copies plus Recall's snapshot allocation can squeeze free space on 256 GB drives. Low space pauses Recall and can also stall OneDrive with sync errors.
- **Antivirus scanning synced files:** Real-time scanning of a busy OneDrive sync folder adds a third layer of file access, multiplying the chance of a lock collision during snapshot capture.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm OneDrive is actually the trigger

Before changing anything, verify the conflict pattern: Recall problems that appear only while OneDrive is actively syncing, and vanish when sync is idle. A quick pause test settles it.

1. Right-click the OneDrive cloud icon in the taskbar and choose **Pause syncing** for 2 hours.
2. Use your PC normally for 20–30 minutes with OneDrive paused and watch Recall — do new snapshots appear on schedule?
3. If capture improves, resume syncing and watch for the problem to return. That on/off pattern confirms the conflict.
4. If nothing changes with OneDrive paused, the cause lies elsewhere — skip to Fix 5 and check Recall's own storage health.

### Fix 2: Throttle OneDrive's bandwidth and sync scope

A calmer OneDrive is a better neighbor. Limiting how aggressively it syncs removes the disk-I/O spikes that collide with snapshot capture.

1. Open OneDrive **Settings > Sync and backup > Advanced settings** and set upload/download rate limits to a moderate value instead of unlimited.
2. Uncheck folders you do not need locally under **Manage backup** — fewer synced folders means fewer file locks.
3. Turn on **Files On-Demand** so rarely used files stay cloud-only instead of churning the disk.
4. Restart the PC so the new limits apply cleanly, then monitor Recall capture for a day.

### Fix 3: Give Recall storage breathing room

Even a mild sync conflict becomes a real failure when disk space is tight. Recall pauses captures under storage pressure, and OneDrive errors compound it.

1. Go to **Settings > System > Storage** and make sure at least 25–50 GB is free on the system drive.
2. Open **Settings > Privacy & security > Recall & snapshots** and check the snapshot storage allocation — reduce the allocation if it is set very high on a small drive.
3. Delete old snapshots you no longer need from the Recall timeline to free its store quickly.
4. Empty the Recycle Bin and clear temporary files, then resume snapshots and confirm new captures appear.

### Fix 4: Stagger heavy sync away from active work hours

If you regularly sync large folders — video projects, photo libraries — schedule that churn for times you are not relying on Recall capture.

1. Pause OneDrive syncing manually before starting a big upload batch, then resume when it finishes.
2. Move huge one-off uploads to overnight: start them before bed and let them complete while the PC is idle.
3. For developers hitting toolchain snags on ARM machines at the same time, [installing Python on Windows on ARM](/articles/python-arm-windows-install-issues/) covers a parallel class of background-install headaches.
4. Keep an eye on the OneDrive icon: a spinning sync badge during your workday is your cue to pause it.

### Fix 5: Reset the OneDrive sync state

A stuck sync engine holds file locks far longer than it should. Resetting OneDrive clears its local state without deleting your files.

1. Back up nothing extra — a reset keeps your files; but confirm important files show a green checkmark, not a sync error, first.
2. Press **Win + R**, type `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset`, and press Enter. OneDrive will restart after a minute or two.
3. Sign back in if prompted and let it re-scan your folders. Watch that previously errored files now sync cleanly.
4. Test Recall capture during the re-scan. A clean sync engine should no longer collide with snapshot writes.

### Fix 6: Repair Windows file and system health

Persistent conflicts after the above steps point to deeper file-system or component damage. Windows has built-in repair tools for exactly this.

1. Open an elevated Command Prompt and run `sfc /scannow` — then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. If Windows Update itself is unhealthy, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) walks through the built-in troubleshooters.
3. Restart, then verify both OneDrive sync and Recall capture run side by side for a full workday.
4. As a last resort, reinstall OneDrive from Microsoft's site and re-link your account rather than fighting a damaged install.

## Closing

Recall and OneDrive are both well-behaved services that simply get in each other's way when disk activity peaks. Throttle sync, keep free space comfortable, reset a stuck sync engine, and repair system health if the conflict persists. With those four layers handled, snapshots and syncs can run side by side without either one noticing the other.
