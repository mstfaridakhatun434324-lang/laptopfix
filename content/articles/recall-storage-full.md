---
title: "Recall Storage Full? Free Up Space Without Losing Your Timeline"
slug: recall-storage-full
date: 2026-10-19
categories: ["ai-pc"]
tags: ["recall", "storage full", "disk space", "snapshots", "windows 11"]
description: "Recall storage full on Windows 11? Learn how snapshot storage works, how to shrink the allocation, delete old snapshots, and stop disk-full warnings now."
thumbnail: "/images/thumbs/recall-storage-full.webp"
faqs:
  - q: "How much disk space does Windows Recall actually use?"
    a: >
      By default, Recall can allocate up to 150GB on large drives (less on smaller ones), storing encrypted screen snapshots and their AI-generated text indexes. Most users accumulate tens of gigabytes within weeks. The allocation is configurable — you can shrink it dramatically in Settings.
  - q: "Is it safe to delete Recall snapshots?"
    a: >
      Yes, completely. Deleting snapshots only erases Recall's visual timeline and its searchable index — your files, apps, settings, and Windows itself are untouched. Think of it as clearing a browser history, not deleting documents.
  - q: "Why does Recall say storage is full when I have free disk space?"
    a: >
      Recall has its own storage allocation cap separate from overall free space. When snapshots hit that cap, Recall warns "storage full" even with gigabytes free elsewhere. Raising the allocation or deleting old snapshots resolves it — it's a quota, not a disk crisis.
  - q: "Can I move Recall storage to another drive?"
    a: >
      No — Recall stores snapshots on the system drive only, in an encrypted, access-controlled location. You can't relocate it. Your controls are: shrink the allocation, delete snapshots periodically, or disable snapshot saving entirely.
---

"Recall storage is full." It's a confusing warning — your drive might show plenty of free space, yet Windows insists Recall has run out of room. Welcome to quota-based storage: Recall gets its own allocation, and when snapshots fill it, you get the warning regardless of what the rest of the disk looks like.

Recall's appetite is real. Continuous screenshots plus AI-generated text indexes accumulate fast — tens of gigabytes in weeks of heavy use is normal, and the default allocation can reach 150GB on big drives. On a 512GB laptop that's a third of your disk eaten by a timeline you may never scroll. This guide explains the storage model, shows you how to shrink it, clear it, and stop the warnings — without breaking anything. For the broader Recall troubleshooting picture (not working, not saving), our Recall guides cover those; here it's purely about disk space. If you're considering the nuclear option, [how to disable Recall in Windows 11](/articles/how-to-disable-recall-windows-11/) is the off switch.

And if the storage pressure comes with heat and noise, [AI PC running hot fix](/articles/ai-pc-running-hot-fix/) addresses the thermal side of heavy snapshot processing.

## Why this happens

- **Snapshots accumulate relentlessly:** Every few seconds of screen time becomes a stored snapshot — thousands per day of active use.
- **AI indexes double the cost:** Each snapshot also gets an AI-generated text description and searchable index, roughly doubling storage per snapshot.
- **Default allocation is generous:** Windows grants Recall a large quota by default (scaled to drive size), normalizing huge usage you'd otherwise notice.
- **Quota ≠ free space:** The "storage full" warning triggers at the Recall quota, independent of overall disk free space — hence the confusion.
- **No automatic aggressive pruning:** Recall prunes oldest-first only when hitting limits, and its retention is longer than most users expect.
- **Encryption overhead:** Snapshots are encrypted and access-controlled, adding metadata overhead versus plain image files.

## How to fix it

Work through these in order — understand, shrink, clear, then prevent.

### Fix 1: See exactly what Recall is storing

Before changing anything, look at the numbers. The Settings page shows allocation, usage, and options in one place.

1. Open Settings > Privacy & security > Recall & snapshots.
2. Note "Storage" section: current usage vs. maximum allocation.
3. Check your overall disk: Settings > System > Storage to see total free space for context.
4. Decide your target: most users are happy with 10–25GB allocation instead of the default.
5. Remember this page — you'll return here for every fix below.

### Fix 2: Shrink Recall's storage allocation

The highest-leverage change: cap how much disk Recall may ever consume. Windows enforces the new cap by pruning oldest snapshots first.

1. On the Recall & snapshots page, find "Maximum storage for snapshots" (or similarly worded control).
2. Lower it to 25GB (or 10GB if you rarely use the timeline).
3. Confirm — Windows will delete oldest snapshots to fit the new cap.
4. Wait a few minutes for the pruning to complete, then re-check usage.
5. The "storage full" warning should clear once usage drops below the new cap.

### Fix 3: Delete snapshots selectively or entirely

Pruning by age is automatic under a cap, but manual deletion gives immediate relief and a clean slate.

1. On the Recall & snapshots page, click "Delete snapshots."
2. Choose a range if offered (last week, last month) or delete all for maximum space.
3. Confirm — deletion is quick but the index rebuild afterwards can take a few minutes of background work.
4. Verify the freed space in Settings > System > Storage.
5. Set a monthly reminder if you're a heavy Recall user — a periodic purge beats quota warnings.

### Fix 4: Exclude apps and websites from snapshots

Not everything needs snapshotting. Exclusions reduce both storage growth and privacy exposure in one move.

1. On the Recall & snapshots page, find "Filter" or exclusion lists for apps and websites.
2. Add apps with sensitive or high-churn content (banking, password managers, video players).
3. Add websites similarly — streaming and social feeds generate enormous snapshot volume.
4. Excluded content is never captured, so it never consumes storage.
5. Review exclusions quarterly — your app mix changes, and so should the list.

### Fix 5: Pause snapshotting during storage crunches

When disk space is tight overall, pausing snapshot capture stops the bleeding immediately.

1. Toggle "Save snapshots" off on the Recall & snapshots page.
2. Existing snapshots remain searchable until you delete them — pausing only stops new captures.
3. Free up general disk space too: Settings > System > Storage > Cleanup recommendations.
4. Re-enable snapshotting once you've cleared room, with the smaller allocation from Fix 2.
5. Consider leaving it paused permanently if you never actually use the timeline — many users don't.

### Fix 6: Disable Recall storage entirely

If the timeline isn't worth any disk space to you, the clean answer is off — not a tiny quota you keep hitting.

1. Toggle "Save snapshots" off permanently.
2. Click "Delete snapshots" and remove everything.
3. Set the storage allocation to its minimum if the control remains.
4. Confirm in Storage settings that Recall's footprint is zero.
5. For the complete AI teardown (services and all), follow [disable Windows AI services](/articles/disable-windows-ai-services/).

## Closing

Recall's "storage full" warning is a quota message, not a disk emergency — but the tens of gigabytes behind it are real. Shrink the allocation to what your actual timeline usage justifies (10–25GB for most), exclude high-churn apps and sites, and purge periodically. If you never scroll the timeline, the honest answer is off entirely — zero gigabytes, zero warnings, zero background processing. (On a Surface, storage pressure sometimes tags along with broader AI issues — see [Surface Laptop AI features not working](/articles/surface-laptop-ai-features-not-working/) if that's your machine.)
