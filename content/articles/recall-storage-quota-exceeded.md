---
title: "How to Fix Windows Recall Storage Quota Exceeded"
slug: recall-storage-quota-exceeded
date: 2026-10-21
categories: ["ai-pc"]
tags: ["recall storage quota exceeded", "windows recall", "recall disk space", "ai pc", "recall troubleshooting", "snapshot storage"]
description: "Fix the Windows Recall storage quota exceeded warning with six methods: trim old snapshots, fix runaway capture, resize your allocation, and stop the loop."
thumbnail: "/images/thumbs/recall-storage-quota-exceeded.webp"
faqs:
  - q: "What does the Recall storage quota exceeded message mean?"
    a: >
      Recall has filled the disk allocation you gave it — it can no longer save new snapshots. Old snapshots are safe, but the timeline freezes until you free space or raise the allocation.
  - q: "How much storage should I give Recall?"
    a: >
      As a rule of thumb: 25 GB covers light use, 50 GB is comfortable for daily work, and 150 GB suits heavy multitaskers. The right number depends on capture frequency and how far back you want to search.
  - q: "Does Recall delete old snapshots automatically?"
    a: >
      Yes — near the quota, Recall deletes the oldest snapshots first to make room. But under runaway capture (duplicates, broken exclusions), deletions cannot keep up and the warning appears anyway.
  - q: "Will raising the quota slow down my PC?"
    a: >
      No. A bigger quota just keeps more history. Performance is driven by capture frequency and indexing, not by how much old history sits in the store.
---

The "storage quota exceeded" warning is Recall telling you its tank is full: every byte of the disk allocation you granted it is spoken for, so new snapshots stop being saved and your timeline freezes at the moment it ran out. Your existing history is intact — nothing is lost — but Recall is effectively paused until space is made.

Quota exhaustion has two distinct causes, and the fix depends on which one you have. Sometimes the allocation is simply too small and raising it is the honest answer. More often, something is burning through storage far faster than normal — and raising the quota just delays the same warning by a week.

This guide gives you six fixes in technician order: measure what consumes the space, trim it safely, fix the runaway behavior underneath, then size the quota properly. Work through them in sequence.

## Why this happens

- **Allocation too small for your habits:** The default quota suits average use. Heavy multitaskers with multiple monitors generate snapshots several times faster than the default assumes.
- **Duplicate or redundant snapshots:** A broken snapshot index or crashed cleanup task stores every capture as a new entry, multiplying storage consumption without adding history.
- **Exclusions stopped working:** Websites or apps you meant to exclude get captured anyway, filling the store with unwanted content — video playback pages are the classic space hog.
- **Capture frequency set too high:** Shorter snapshot intervals generate proportionally more data. A frequency meant for testing can quietly stay on for months.
- **Automatic oldest-first deletion lagging:** Recall deletes the oldest snapshots as it approaches the quota, but under runaway conditions the deletion cycle cannot keep up and the exceeded warning appears anyway.
- **Other disk pressure misattributed to Recall:** Sometimes the real problem is a nearly-full system drive, and Recall is simply the first component to complain because it writes constantly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what is consuming the quota

Guessing wastes time — you might raise the quota when the real problem is duplicates, or delete history when the allocation was simply undersized. Two minutes of measurement tells you which fix to apply.

1. Open **Settings > Privacy & security > Recall & snapshots** and note the exact storage figure and your current maximum allocation.
2. Check the date range your timeline covers — a healthy store spans weeks or months; one spanning only days signals runaway capture.
3. Open **Settings > System > Storage** and check overall free space on the system drive; if the whole drive is nearly full, Recall is a symptom, not the cause.
4. Compare your usage pattern against the [disk space usage guide](/articles/recall-using-too-much-disk-space/) if consumption looks abnormally high for your workload.
5. With numbers in hand, you can now choose between trimming (Fix 2–4) and resizing (Fix 5) instead of doing both blindly.

### Fix 2: Delete old or unwanted snapshots safely

Recall's built-in deletion controls let you prune history by time range, which is the fastest way to get capturing again when the quota is genuinely full of real — but old — history.

1. In **Settings > Privacy & security > Recall & snapshots**, open the **Delete snapshots** section.
2. Delete snapshots for a time range you no longer need — start with the oldest months, since Recall deletes oldest-first automatically anyway.
3. Confirm, wait a few minutes for the store to compact, and verify in the same page that usage dropped and capturing resumed.
4. Check that the timeline's earliest date moved forward as expected — that confirms deletion worked rather than just reporting it did.
5. If the freed space vanishes again within days, stop deleting and move to Fix 3 — you have a runaway consumption problem, not a history problem.

### Fix 3: Stop runaway capture: duplicates, exclusions, and filters

When the quota refills suspiciously fast, something is generating snapshots it should not be. This fix hunts the three most common runaway causes: duplicates, broken exclusions, and stale filters.

1. Scroll the timeline for identical back-to-back captures — if you find them, the [duplicate snapshots issue](/articles/recall-duplicate-snapshots-issue/) has its own dedicated repair sequence.
2. Review your **filter lists** in Recall settings and re-add websites and apps that should be excluded, especially video-heavy pages that generate constant screen changes.
3. Check that your app exclusions survived recent Windows updates — feature updates can silently reset them to defaults.
4. Monitor storage for 48 hours after these corrections; steady, slow growth means the runaway is fixed.
5. For extra headroom context, [Copilot app notification problems](/articles/copilot-app-notifications-not-working/) are unrelated to storage but worth checking separately if Copilot has been noisy while Recall was paused.

### Fix 4: Lower the snapshot frequency and tighten capture rules

Every capture interval you shorten doubles (or worse) the data rate. If your frequency was set aggressively during initial setup and never revisited, dialing it back is a permanent reduction in consumption.

1. In **Settings > Privacy & security > Recall & snapshots**, find the snapshot frequency setting and move it to a longer interval.
2. Reconsider whether every connected display needs capturing — multi-monitor setups multiply consumption per interval.
3. Confirm filters for high-change content (video, animations, live dashboards) are active so each capture actually represents meaningful change.
4. Watch storage over the next few days: you should see the growth curve flatten noticeably compared to your Fix 1 baseline.
5. Do not drop frequency to the absolute minimum out of frustration — the goal is useful history at sustainable cost, not a sparse timeline.

### Fix 5: Resize the quota to match your real usage

Once runaway behavior is fixed, size the allocation honestly. Undersizing just recreates this warning; the quota should fit your measured consumption with comfortable headroom.

1. Use your Fix 1 baseline: take your weekly consumption, multiply by how many weeks of history you want, then add 50% headroom.
2. In **Settings > Privacy & security > Recall & snapshots**, raise the maximum storage allocation to that figure.
3. If your system drive is small overall, consider whether freeing space elsewhere is smarter than growing Recall's share — Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents how the allocation interacts with drive capacity.
4. Confirm the new limit took effect and that capturing resumed without the exceeded warning.
5. A disappearing [caption box in live captions](/articles/live-captions-caption-box-disappears/) is a separate rendering issue — do not confuse it with anything storage-related here.

## Closing

Storage quota exceeded is a budgeting problem with a diagnostic step: measure consumption, fix runaway behavior first, then size the quota to your real needs. Deleting history without fixing the cause is a treadmill; raising the quota without measuring is a guess. Done in this order, one pass keeps Recall capturing smoothly for months.
