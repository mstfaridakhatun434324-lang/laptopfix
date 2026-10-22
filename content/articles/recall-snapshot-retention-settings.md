---
title: "Recall Snapshot Retention Settings Explained: How to Configure Them"
slug: recall-snapshot-retention-settings
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall retention", "recall snapshot settings", "windows recall storage", "recall history length", "copilot plus pc", "windows 11"]
description: "Confused by Recall snapshot retention settings? Learn what each option controls, how retention affects disk space, and the best settings for your Copilot+ PC."
thumbnail: "/images/thumbs/recall-snapshot-retention-settings.webp"
faqs:
  - q: "How long does Recall keep snapshots by default?"
    a: >
      It depends on your drive size and build — Windows scales the default storage allocation with available disk space. Check Settings > Privacy & security > Recall & snapshots on your PC for the actual values in effect.
  - q: "Can I keep Recall snapshots forever?"
    a: >
      Not practically. Even with generous settings, the allocation cap and eventual storage pressure will age out old snapshots. Recall is designed as a rolling recent history, not an archive.
  - q: "Does shorter retention improve performance?"
    a: >
      Indirectly. A smaller store means less disk I/O during indexing and search, which you may notice as snappier timeline searches on slower SSDs.
  - q: "Will changing retention delete my current snapshots?"
    a: >
      Lowering the limits ages out snapshots that exceed them — that is the point. Raising limits never deletes anything. If you need old history, export or note anything critical before tightening retention.
---

Recall keeps every snapshot until something tells it not to — and that something is the retention settings. Get them right and your timeline holds exactly as much history as you need; get them wrong and you either run out of disk or lose history you wanted to keep.

Retention in Recall is really two controls working together: how long snapshots are kept (age) and how much space they may occupy (allocation). Windows manages the interplay, aging out the oldest snapshots when either limit bites. Understanding that interplay is the whole game — much like [reducing Studio Effects battery impact](/articles/studio-effects-battery-impact-reduce/), where one slider affects both quality and battery life simultaneously.

This guide explains each retention control, shows you how to configure them for different needs, and fixes the common problems when retention does not behave as expected.

## Why this happens

- **Two overlapping controls confusing users:** Age-based retention and space-based allocation interact, and most users only discover one of them — then wonder why history disappears 'early' or the disk stays full, the same confusion behind [Recall using too much disk space](/articles/recall-using-too-much-disk-space/) complaints.
- **Defaults tuned for large drives:** Default allocation scales with drive size, which is generous on 1 TB machines and painful on 256 GB ones.
- **Retention changed by updates or sync:** Windows updates and settings sync can occasionally reset Recall storage options to defaults without notice.
- **No per-app retention:** Retention is global — you cannot keep a year's worth of one app and a week's of another, which surprises users expecting finer control.
- **Deleted snapshots still counted briefly:** After mass deletion, the store can take time to compact, making it look like retention settings did nothing.
- **Misreading the timeline as the store:** The visible timeline may show less than the store holds (or vice versa) due to filtering and processing lag, muddying retention troubleshooting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find and understand both retention controls

You cannot configure what you cannot find. Locate both the age and allocation controls first.

1. Open **Settings > Privacy & security > Recall & snapshots**.
2. Identify the snapshot storage allocation (space cap) and any retention-duration option your build offers.
3. Note the current values before changing anything — you will want a baseline.
4. Read any explanatory text on the page; Microsoft occasionally renames these controls between builds.

### Fix 2: Choose retention for your actual needs

There is no universally correct retention — only the right one for how you use the timeline.

1. If you search Recall for things from last week, 30 days of retention is plenty and keeps the store lean.
2. If you genuinely revisit months-old work, raise the allocation cap and accept the disk cost — but monitor free space.
3. On 256 GB drives, favor shorter retention; the disk will thank you.
4. Network-dependent workflows have their own retention-like quirks — [Cisco AnyConnect on ARM64](/articles/cisco-anyconnect-arm64-windows/) covers VPN session persistence as a parallel lesson in 'how long is my history kept'.

### Fix 3: Apply the allocation cap deliberately

The space cap is the control that actually protects your drive. Set it as a conscious decision.

1. Set the snapshot storage allocation to a fixed value rather than leaving an aggressive default.
2. A good rule: allocation should never exceed one-third of your typical free space.
3. Confirm the change and watch over the following days as Recall ages out excess snapshots to fit.
4. If the disk is still tight, the cap is not the problem — something else is eating space.

### Fix 4: Verify retention is actually working

Settings that do not take effect are a real failure mode. Verify with a before-and-after check.

1. Note the oldest snapshot date visible in your timeline today.
2. Set a shorter retention period and wait 48 hours of normal PC use.
3. Check whether snapshots older than the new limit have been aged out.
4. If old snapshots persist past the limit, continue to Fix 5 — the store needs attention.

### Fix 5: Clear the store when retention seems stuck

A store that ignores retention usually has a damaged database. Clearing it restores normal aging behavior.

1. Delete all snapshots from Recall settings and confirm the timeline is empty.
2. Toggle **Save snapshots** off, restart, and toggle it back on.
3. Let new snapshots accumulate for a few days, then verify the oldest ones age out on schedule.
4. This reset also fixes most cases where the allocation display shows incorrect numbers.

### Fix 6: Keep Windows updated for retention fixes

Retention behavior is implemented in OS components, and Microsoft refines it in updates.

1. Install all pending Windows updates — Recall storage logic has changed across builds.
2. After major updates, re-check your retention settings; defaults occasionally reset.
3. If retention controls are missing entirely on your build, an update is the most likely way to gain them — check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for your build's documented options.
4. Document your chosen settings somewhere so you can restore them quickly after any reset.

## Closing

Recall retention is two controls — age and allocation — and the art is setting both deliberately for your drive size and your actual memory needs. Thirty days suits most people; larger drives can afford more. Verify the settings take effect, reset the store if they do not, and re-check after major updates. A well-tuned retention setup means the timeline always holds what you need and never threatens your disk.
