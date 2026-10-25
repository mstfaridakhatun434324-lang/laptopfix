---
title: "Recall Delete Snapshots Not Working? Fix It Step by Step"
slug: recall-delete-snapshots-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "snapshots", "privacy"]
description: "Can't delete Recall snapshots? Learn why deletion fails and how to clear snapshots safely, completely, and permanently on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-delete-snapshots-not-working.webp"
faqs:
  - q: "Why won't Recall delete my snapshots?"
    a: >
      Deletion can fail when the snapshot service is stuck, the database is
      locked by another process, disk space is too low to complete the
      operation, or your account permissions changed. The snapshots may also
      appear deleted in the app while files remain until the service restarts.
  - q: "Are deleted Recall snapshots really gone?"
    a: >
      When deletion completes properly, snapshots are removed from local
      storage and cannot be recovered through Recall. If deletion appears to
      succeed but entries reappear, the delete operation never actually
      finished, and the fixes in this guide address that.
  - q: "Can I delete only some Recall snapshots?"
    a: >
      Yes. Recall lets you delete snapshots for a specific app, website, or
      date range, as well as clearing everything. Use targeted deletion when
      you only need to remove sensitive periods rather than your whole history.
  - q: "Does deleting snapshots affect other AI features?"
    a: >
      No. Deleting Recall snapshots only affects Recall's timeline. Other
      Copilot+ features, Windows Search, and your files are untouched.
---

Deleting Recall snapshots should be simple: pick a range, confirm, and they are gone. When deletion fails, though, it becomes a privacy worry as well as an annoyance — you asked for data to be removed and it is still sitting there. Sometimes the app claims success while entries quietly reappear; other times the delete button seems to do nothing at all. Either way, the problem deserves a proper fix, not just repeated clicking.

Deletion failures usually trace back to a stuck service, a locked database, or a permissions change rather than to the snapshots themselves. The delete operation needs the snapshot service to be healthy and the storage to have enough free space to rewrite its index. When any of those conditions fail, the operation aborts partway and leaves the timeline looking untouched.

It is also worth checking whether the problem is isolated to Recall. If your machine is showing other odd behaviour, such as an [NPU showing 0 TOPS](/articles/npu-showing-0-tops/) or [HP OmniBook X battery issues](/articles/hp-omnibook-x-battery-issues/), a broader system problem may be interfering with background services. And if you want to verify how your NPU is set up before deeper fixes, our guide on how to [check the NPU firmware version in Windows](/articles/check-npu-firmware-version-windows/) is a useful companion.

## Why this happens

- **Snapshot service stuck:** A frozen service cannot process deletions, so requests queue up and never complete.
- **Database locked by another process:** Backup tools, antivirus scans, or a second Recall window can lock the snapshot database during deletion.
- **Insufficient free disk space:** Deletion rewrites the snapshot index, which needs temporary free space; a full drive can abort the operation.
- **Corrupted snapshot index:** A damaged index may refuse to drop entries, leaving them visible even after a delete command.
- **Permission or account changes:** Changing your PIN, account, or Windows Hello setup can leave some snapshots owned by a previous identity state.
- **App still running during deletion:** Deleting snapshots for an app that is actively being captured can recreate entries as fast as you delete them.
- **UI delay mistaken for failure:** Large deletions take time to process, and the timeline may not refresh until the operation fully completes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Close everything and retry a small deletion

Before assuming a deep fault, rule out timing and contention. Close the apps involved, wait for background activity to settle, and delete a single day's snapshots. If a small deletion works, the problem is scale or contention, not a broken delete function.

1. Close the Recall app and any app whose snapshots you want to delete.
2. Wait two minutes for background processes to settle.
3. Reopen Recall and select a single day to delete.
4. Confirm and wait for the operation to finish without closing Recall.
5. Refresh the timeline and check whether that day is gone.
6. If it worked, repeat for larger ranges in smaller batches.

### Fix 2: Restart the snapshot service

A stuck service is the most common cause of failed deletions. Restarting it releases locks and lets queued delete operations complete, often clearing the backlog on its own.

1. Press Windows + R, type `services.msc`, and press Enter.
2. Find the Recall snapshot service.
3. Right-click it and choose Restart.
4. If Restart is unavailable, stop it, wait 10 seconds, then start it.
5. Reopen Recall and retry the deletion.
6. Check the timeline after a few minutes to confirm entries are gone.

### Fix 3: Free up disk space before deleting

It sounds backwards — you are deleting to free space — but the delete operation itself needs temporary room to rewrite its index. On a nearly full drive, that rewrite fails and nothing is deleted. Clearing even a few gigabytes elsewhere can unblock the whole process.

1. Open Settings, go to System, then Storage, and check free space.
2. Delete large temporary files, downloads, or unused apps.
3. Empty the Recycle Bin.
4. Confirm at least a few gigabytes are now free.
5. Retry the Recall deletion.
6. Confirm the timeline reflects the deletion.

### Fix 4: Pause snapshots while you delete

If Recall is actively capturing while you delete, new snapshots for the same period can repopulate the timeline and make deletion look like it failed. Pausing capture first gives the delete operation a clean window to finish.

1. Open Settings, go to Privacy & security, then Recall & snapshots.
2. Temporarily turn off "Save snapshots".
3. Perform the deletion in the Recall app.
4. Wait for it to complete and verify the timeline.
5. Turn snapshots back on.
6. Confirm no deleted entries reappear over the next hour.

### Fix 5: Check for locking software

Antivirus, backup, and sync tools can lock the snapshot database. If deletion consistently fails at the same point, temporarily pause real-time scanning or backup for the snapshot location, retry the deletion, and then restore protection with an appropriate exception.

1. Open your antivirus or backup tool's settings.
2. Temporarily pause scanning or backup of the Recall snapshot folder.
3. Retry the deletion in Recall.
4. If it succeeds, add the snapshot folder as a managed exception.
5. Re-enable scanning and backup protection.
6. Verify the deletion held after protection resumes.

### Fix 6: Repair the snapshot index

A corrupted index can refuse to drop entries no matter how many times you click delete. Resetting the snapshot store clears the corruption, though it also removes remaining snapshots, so use this only after the gentler fixes have failed and you genuinely want the data gone anyway.

1. Note that this step deletes all remaining snapshots.
2. Close the Recall app completely.
3. Open Settings, go to Privacy & security, then Recall & snapshots.
4. Choose the option to delete all snapshot data.
5. Confirm and wait for the reset to finish.
6. Reopen Recall and confirm the timeline is empty.
7. For persistent problems, check the official [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Verify deletion with a fresh sign-in

Account and identity changes can leave snapshots tied to an older sign-in state that the current session cannot delete. Signing out and back in refreshes the identity binding and can make previously undeletable snapshots deletable.

1. Save your work and sign out of Windows.
2. Sign back in with the same Microsoft account.
3. Confirm Windows Hello is working normally.
4. Open Recall and retry the deletion.
5. If entries persist, try deletion from a different administrator account on the same PC.
6. Confirm the timeline is clear after the successful deletion.

## Closing

Failed snapshot deletion is usually a stuck service, a locked database, or a full drive — not a sign that Recall is keeping your data against your will. Work through the service restart and space fixes first, and reserve the full reset for cases where nothing else works. Once deletion works reliably, you can manage your timeline with confidence, keeping what is useful and removing what is private.
