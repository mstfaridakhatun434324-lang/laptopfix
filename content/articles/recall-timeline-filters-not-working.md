---
title: "How to Fix Recall Timeline Filters Not Working on Windows 11"
slug: recall-timeline-filters-not-working
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall timeline filters", "recall filter not working", "windows recall search", "recall timeline", "copilot plus pc", "windows 11"]
description: "Recall timeline filters not working on your Copilot+ PC? Fix broken date, app, and website filters with these step-by-step repairs for the Recall timeline."
thumbnail: "/images/thumbs/recall-timeline-filters-not-working.webp"
faqs:
  - q: "Why do Recall filters show no results for yesterday?"
    a: >
      The most common reasons are a wrong system clock shifting timestamps, a stale filter combination still applied, or unprocessed snapshots missing their metadata labels. Clear filters, check the clock, then let the PC idle so processing catches up.
  - q: "Can I filter the Recall timeline by a specific app?"
    a: >
      Yes — the timeline supports filtering by app and by website, plus date ranges and text search. If the app filter is empty for an app you used, that app may be in your exclusion list or its snapshots may not have finished processing yet.
  - q: "Do filters work on old snapshots after an update?"
    a: >
      Usually yes, since the metadata index survives updates. But a major Windows update can invalidate parts of the index; if filters broke right after an update, rebuilding the index as described above is the fix.
  - q: "Are filtered-out snapshots deleted?"
    a: >
      No. Filters only change what you see, never what is stored. Excluded apps and websites simply are not captured in the first place — but filtering the timeline view deletes nothing.
---

The Recall timeline is only useful if you can slice it: filter by date, by app, by website, and find the moment you need in seconds. When those filters stop working — showing everything, showing nothing, or spinning forever — the timeline turns into an unsearchable pile of screenshots.

Broken filters usually mean the timeline's underlying index or metadata is damaged, not that your snapshots are gone. The pictures are still there; the labels Recall uses to sort them are not. A similar metadata-versus-content split causes [Studio Effects automatic framing](/articles/studio-effects-auto-framing-zoom/), where the camera feed is fine but the effect layer on top misbehaves.

This guide gives you six fixes in order: verify the filters are truly broken, repair the search index, reset the filter state, and rebuild the timeline metadata. Work through them and test the filters after each step.

## Why this happens

- **Corrupt timeline metadata index:** Recall keeps metadata — app names, URLs, timestamps — alongside snapshots. If that index corrupts, filters return wrong results or none at all while the images themselves are intact.
- **Incomplete snapshot processing:** New snapshots get processed by the on-device AI to extract filterable metadata. If processing stalled, recent snapshots have no labels and vanish from filtered views — the same stalled-pipeline pattern behind [slow Recall timeline search](/articles/recall-timeline-search-slow/).
- **Filter state stuck in the UI:** Sometimes the timeline UI itself holds a stale filter combination that no longer matches anything, making it look like filtering is broken when the data is fine.
- **Time zone or clock changes:** Date filters depend on accurate timestamps. A wrong system clock or a time-zone change while traveling shifts snapshots out of the date range you are filtering for.
- **Website exclusions hiding results:** Recall's website exclusion list can silently filter out whole sites. If your filter targets a site you once excluded, the results will be empty by design.
- **Windows Search integration failure:** Recall leans on Windows Search components. If search indexing is broken system-wide, Recall's filters degrade along with it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out a stuck filter combination

Before repairing anything, make sure the UI is not holding a filter set that legitimately matches nothing. This thirty-second check saves a lot of unnecessary repair work.

1. Open Recall and clear every active filter — dates, apps, websites — back to the unfiltered timeline.
2. Type a broad search term you know appears in recent snapshots and confirm results show up unfiltered.
3. Re-apply one filter at a time: date first, then app, then website. Note exactly which filter breaks the results.
4. If all filters work individually, you had a stale combination — not a broken feature. If one specific filter fails, continue below.

### Fix 2: Check the system clock and time zone

Date filters are only as accurate as the system clock. A drifted clock silently moves snapshots out of the range you are browsing.

1. Open **Settings > Time & language > Date & time** and turn on **Set time automatically** and **Set time zone automatically**.
2. If you recently traveled, verify the time zone actually updated — Windows sometimes lags a day behind.
3. Restart Recall and re-test the date filter with **Today** selected.
4. For developers who also fight environment quirks on ARM hardware, [Node.js on Windows on ARM](/articles/nodejs-arm64-windows-problems/) is a useful companion read on keeping tooling clocks and caches sane.

### Fix 3: Review app and website exclusions

Recall deliberately hides excluded apps and websites from the timeline. An old exclusion can masquerade as a broken filter.

1. Go to **Settings > Privacy & security > Recall & snapshots** and open the app and website exclusion lists.
2. Remove any exclusion you added experimentally and no longer need.
3. Note that InPrivate and incognito windows are never captured — filtering for them will always return nothing, by design.
4. Re-test the filter with a normal browsing session you know was captured.

### Fix 4: Restart Recall's background services

Stalled metadata processing often just needs its services bounced. A clean restart lets the pipeline catch up on unprocessed snapshots.

1. Close the Recall window completely.
2. Open **Task Manager > Services** and restart the Windows AI and Recall-related services you find there.
3. Alternatively, do a full **Restart** (not shutdown) from the Start menu — this cleanly restarts all background services.
4. Use the PC for 30 minutes, then check whether new snapshots now appear correctly under filters.

### Fix 5: Rebuild the Recall search index

When metadata is corrupt, the fix is to throw it away and rebuild. Recall reprocesses snapshots and regenerates the filter labels.

1. In **Settings > Privacy & security > Recall & snapshots**, find the option to delete snapshots — this clears both images and their index.
2. Confirm deletion, then toggle **Save snapshots** off and on to force a fresh capture cycle.
3. Let the PC run for a few hours of normal use so new snapshots accumulate and get processed.
4. Test filters against the new snapshots only. Working filters on fresh data confirm the old index was the problem.

### Fix 6: Repair Windows Search and install updates

Recall filters depend on the same plumbing as Windows Search. If the system-wide search stack is damaged, Recall filters suffer with it.

1. Open **Settings > Privacy & security > Searching Windows** and run the search troubleshooter.
2. Go to **Settings > Windows Update** and install all pending updates, then restart.
3. If updates fail or search stays broken, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) covers the deeper repair paths.
4. After updating, give Recall a full day of capture and re-test every filter type.

## Closing

Recall filters break when the metadata behind them breaks — a stale UI state, a drifted clock, an old exclusion, or a corrupt index. Clear the state first, check the clock, review exclusions, then rebuild the index if needed. The snapshots were almost certainly fine all along; once the labels are healthy again, the filters snap back to working exactly as they should.
