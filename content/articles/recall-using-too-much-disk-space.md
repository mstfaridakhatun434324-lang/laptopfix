---
title: "Recall Using Too Much Disk Space? Reclaim It Now"
slug: recall-using-too-much-disk-space
date: 2026-10-19
categories: ["ai-pc"]
tags: ["recall disk space", "snapshots", "storage", "windows 11", "copilot plus pc"]
description: "Recall using too much disk space on Windows 11? Learn where Recall hides gigabytes and reclaim your SSD with safe cleanup and storage limits."
thumbnail: "/images/thumbs/recall-using-too-much-disk-space.webp"
faqs:
  - q: "How much disk space does Recall normally use?"
    a: "It varies with usage, but tens of gigabytes is typical for active users — Microsoft lets you cap it in settings. If Recall is consuming 50GB+ on a 256GB drive, that is excessive and worth trimming."
  - q: "Where are Recall snapshots stored?"
    a: "In a protected system location on your C: drive, managed by Windows. You cannot (and should not) delete the files manually — always use Recall's own Delete snapshots control to avoid corrupting the database."
  - q: "Does limiting storage delete my old snapshots?"
    a: "Yes, effectively. When you lower the cap, Windows prunes the oldest snapshots first to fit. Lowering the limit is a safe way to trim usage without wiping everything at once."
  - q: "Will Recall warn me before filling the disk?"
    a: "It respects its configured cap, so it should not fill the disk entirely — but the cap defaults can be generous on large drives. Check your allocation if space is tight."
---

Recall is a disk hog by design — every snapshot is an image plus AI index data, captured every few seconds all day. On a 1TB drive you might never notice; on a 256GB SSD, Recall can quietly eat a quarter of your storage. The fix is not mysterious, but manual file deletion will corrupt things — use Recall's own controls.

If snapshots are not saving at all (a different problem), see [Recall snapshots not saving](/articles/recall-snapshots-not-saving/). For pure storage pressure, work through these.

## Why this happens

- **Snapshots accumulate relentlessly:** Every few seconds of active use adds another image plus metadata — it compounds fast.
- **AI index overhead:** Beyond images, the semantic index Recall builds for natural-language search adds significant bulk.
- **Generous default cap:** The default storage allocation is sized for large drives, not 256GB SSDs.
- **Old snapshots never pruned aggressively:** Recall keeps history long; without a cap change, old data lingers.
- **Multiple user profiles:** Each Windows user with Recall enabled gets their own snapshot store — multiply accordingly.

## How to fix it

Work through these in order — measure first, then trim.

### Fix 1: See exactly how much Recall uses

You cannot manage what you do not measure — get the number first.

1. Settings, System, Storage — look for the Recall/snapshot entry and note the gigabytes.
2. Compare against your total drive size — 10%+ on a small SSD deserves action.
3. Note the figure before changing anything so you can verify savings after.
4. Check per-user: switch users (if applicable) and repeat — each profile has its own store.
5. If the number seems absurdly high (100GB+), suspect a runaway capture bug and continue to Fix 4.

### Fix 2: Lower the storage cap

The single most effective control.

1. Settings, Privacy & security, Recall & snapshots — find the storage allocation slider.
2. Lower it to a comfortable level (25-50GB is plenty for most users' searchable history).
3. Windows prunes oldest snapshots first to fit the new cap — this happens automatically.
4. Recheck Settings, System, Storage after an hour to confirm the reduction.
5. Revisit the cap if you find yourself wishing for older history — it is a tradeoff, not a punishment.

### Fix 3: Delete snapshots selectively

Bulk-delete when the cap alone is not enough.

1. In Recall settings, use "Delete snapshots" — choose a time range to keep recent history while clearing the old.
2. For a full reset, delete all snapshots — the nuclear option that reclaims everything.
3. Never delete snapshot files manually from disk — always use Recall's controls to avoid database corruption.
4. After deletion, empty Recycle Bin and check Storage to confirm the space returned.
5. Our [delete snapshots guide](/articles/delete-recall-snapshots/) covers selective strategies in detail.

### Fix 4: Check for runaway capture

Abnormal usage signals a bug, not normal operation.

1. If usage grows gigabytes per day with light PC use, something is wrong.
2. Check whether snapshots are saving during idle — they should pause when the screen locks.
3. Temporarily [disable saving](/articles/how-to-disable-recall-windows-11/), reboot, re-enable — this resets a stuck capture loop.
4. Install all Windows updates — Microsoft has fixed snapshot-duplication bugs in cumulative updates.
5. If runaway persists, delete all snapshots and rebuild the database from scratch.

### Fix 5: Exclude high-churn content

Reduce what gets captured in the first place.

1. In Recall settings, add apps and websites with rapidly changing content to the exclusion list.
2. Video calls, games, and dashboards generate enormous snapshot volumes — excluding them saves gigabytes.
3. Remember private windows and DRM content are already excluded by design.
4. Fewer captured apps means a smaller database and faster Recall search too.
5. Review exclusions quarterly — your app mix changes.

### Fix 6: Long-term storage hygiene

Keep it from creeping back.

1. Set a calendar reminder to review Recall storage every few months.
2. Keep the cap conservative — you rarely need more than a month or two of searchable history.
3. If disk pressure is chronic, consider whether you need Recall at all — [disabling it](/articles/how-to-disable-recall-windows-11/) reclaims everything permanently.
4. Monitor after each Windows feature update — updates sometimes reset storage caps upward.
5. For full-drive situations, our [Recall storage full guide](/articles/recall-storage-full/) handles the emergency case.

## Closing

Recall's disk appetite is manageable once you treat it like any other storage consumer: measure it, cap it, prune it, and exclude the noise. The storage slider plus selective deletion handles nearly every case without losing the feature's value. If the disk pressure makes you question the feature entirely, weigh that against [Recall's availability requirements](/articles/recall-not-available-on-my-pc/) — a machine that barely qualifies may not be worth the storage cost. And if the numbers never add up — usage far beyond what your activity justifies, or [snapshots missing](/articles/recall-snapshots-missing/) while space keeps growing — treat it as a bug (Fix 4), not a bill you must pay. A quarterly five-minute storage review keeps Recall useful without letting it quietly colonize your SSD.
