---
title: "Recall Storage Quota Full Error? Fix It Step by Step"
slug: recall-storage-quota-full
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "storage", "quota"]
description: "Recall says its storage quota is full? Learn how to free snapshot space, raise the limit, and stop the quota error returning on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-storage-quota-full.webp"
faqs:
  - q: "What does the Recall storage quota full error mean?"
    a: >
      It means Recall has reached the disk space allocated for snapshots, or
      your system drive is too full for it to save more. Recall then stops
      capturing new snapshots and may start deleting the oldest ones to stay
      within the limit.
  - q: "Will increasing the quota delete my old snapshots?"
    a: >
      No. Raising the allocation gives Recall more room and protects older
      entries. Deleting snapshots is a separate action you choose yourself in
      Recall settings, and it is not required just to clear the quota error.
  - q: "How much space does Recall need?"
    a: >
      Recall's usage grows with how much you use your PC, but keeping at least
      25 GB free on the system drive and giving Recall a reasonable allocation
      in settings is enough for most users to avoid quota errors entirely.
  - q: "Can I stop Recall from filling my disk?"
    a: >
      Yes. Lower the storage allocation in Recall settings, add exclusions for
      apps you do not need captured, and periodically delete old snapshots.
      Recall will then prune itself instead of growing without limit.
---

The "storage quota full" error is Recall's way of saying it has run out of room. New snapshots stop, and if you ignore the warning, Recall may begin deleting your oldest entries to make space — quietly erasing the very history you wanted to keep. It is an annoying message, but it is also a useful one: it tells you exactly where the pressure is, and the fix is usually straightforward.

Quota errors come from two places that are easy to confuse. One is Recall's own storage allocation, a limit you set in settings. The other is your system drive itself: if the whole drive is nearly full, Recall cannot save snapshots no matter how generous its allocation is. Checking both, in the right order, keeps you from raising a limit that the disk cannot honour.

This kind of storage pressure can also affect other AI features that depend on local models and drivers. If you have recently dealt with an [NPU driver rollback](/articles/npu-driver-rollback-fix/) or a missing [human presence detection driver](/articles/human-presence-detection-driver-missing/), treat storage as part of the same health check. Gamers hitting similar limits should also see our guide to [Auto Super Resolution games not working](/articles/auto-super-resolution-games-not-working/), since that feature shares the same NPU and storage constraints.

## Why this happens

- **Recall allocation reached:** Snapshots have filled the disk space assigned to Recall in settings, so no new snapshots can be saved.
- **System drive nearly full:** When C: drops below a safe threshold, Windows restricts Recall even if its own allocation is not technically full.
- **Heavy PC usage:** Long workdays with many apps and browser tabs generate snapshots faster than a small allocation can hold.
- **Old snapshots never pruned:** If automatic deletion is off or set to a very long retention, snapshots accumulate indefinitely.
- **Large display or high snapshot frequency:** Bigger screens and frequent snapshots consume storage faster than expected.
- **Other apps consuming the drive:** Games, video files, and downloads can eat the free space Recall depends on.
- **Storage Sense or cleaner misconfiguration:** Aggressive cleanup rules can confuse Recall's accounting or delete space it needs for new snapshots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check both the quota and the free drive space

Open Recall settings and your storage settings side by side. This tells you whether Recall hit its own limit or the whole drive is full, and that distinction decides which fix actually clears the error.

1. Open Settings, go to Privacy & security, then Recall & snapshots.
2. Note the current storage allocation and usage.
3. Open Settings, go to System, then Storage, and check free space on C:.
4. If the drive has under 25 GB free, the drive is the problem — skip to Fix 2.
5. If the drive is healthy but Recall is at its allocation, go to Fix 3.
6. Record both numbers so you can confirm the fix worked afterwards.

### Fix 2: Free up space on the system drive

Freeing real disk space helps every scenario, including ones where Recall's allocation looks fine on paper. Remove large files you no longer need, uninstall unused apps, and move media off the system drive before touching Recall's own settings.

1. In Storage settings, use the cleanup recommendations to remove temporary files.
2. Uninstall large apps you no longer use.
3. Move videos, installers, and downloads to an external drive or cloud storage.
4. Empty the Recycle Bin.
5. Confirm at least 25 GB is now free on C:.
6. Restart Recall and check whether the quota error clears.

### Fix 3: Raise Recall's storage allocation

If the drive has room, raising Recall's allocation is the direct fix. Give it enough headroom for your usage pattern — a modest increase is fine for light users, while heavy multitaskers should go higher so the error does not return within days.

1. Open Settings, go to Privacy & security, then Recall & snapshots.
2. Find the storage allocation control.
3. Increase it to a level your free drive space comfortably supports.
4. Save and close settings.
5. Wait a few minutes, then open Recall to confirm snapshots resume.
6. Recheck after a day of normal use to ensure the error stays gone.

### Fix 4: Delete old snapshots you no longer need

If you would rather keep the allocation small, pruning old snapshots is the alternative. Delete by date range, keeping recent history intact while removing months-old entries you are unlikely to revisit. This is also good hygiene even when the quota is not full.

1. Open the Recall app and go to its snapshot management options.
2. Choose a date range of old snapshots to delete.
3. Confirm the deletion and wait for it to complete.
4. Check that the quota error clears and new snapshots resume.
5. Repeat monthly, or set automatic deletion to a retention you are comfortable with.
6. Keep a note of what you deleted in case you need it later.

### Fix 5: Reduce how much Recall captures

Exclusions are the smartest long-term fix: every app you exclude is storage Recall never spends. Add games, video players, and other high-churn apps you do not need in your timeline, and the quota will fill far more slowly.

1. Open Recall & snapshots settings.
2. Add apps with rapidly changing screens to the exclusion list.
3. Add websites you visit for video or social feeds.
4. Restart the excluded apps so the exclusion takes effect.
5. Monitor usage over a week to confirm growth has slowed.
6. Adjust exclusions further if the quota still fills quickly.

### Fix 6: Fix Storage Sense conflicts

Storage Sense is helpful, but if it is configured to aggressively clear system data it can fight with Recall's storage management. Review its settings to make sure it is not deleting data Recall needs or misreporting free space.

1. Open Settings, go to System, then Storage.
2. Open Storage Sense settings and review its cleanup schedule.
3. Turn off any option that clears AI or temporary system data aggressively.
4. Run Storage Sense manually once and confirm Recall still works.
5. Restart your PC and recheck the quota error.
6. For persistent issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Reset snapshot storage if accounting is stuck

Sometimes Recall's usage counter gets stuck and reports a full quota even after you free space. A careful reset of the snapshot store clears the bad accounting. Only use this after freeing space and raising the allocation, since it deletes existing snapshots.

1. Back up anything important and note that old snapshots will be lost.
2. Open Settings, go to Privacy & security, then Recall & snapshots.
3. Choose the option to delete snapshot data.
4. Confirm and wait for the reset to complete.
5. Reopen Recall and confirm fresh snapshots begin saving.
6. Set a sensible allocation and exclusions before heavy use resumes.

## Closing

A full Recall quota is a storage problem, not a Recall failure, and it responds well to the basics: free drive space, set a realistic allocation, and exclude apps you do not need captured. Do those three things and the error should stay away. If it keeps returning within days, your drive is simply too full for your usage, and a larger drive or stricter exclusions is the honest long-term answer.
