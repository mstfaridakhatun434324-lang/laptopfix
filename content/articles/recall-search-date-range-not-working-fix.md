---
title: "How to Fix Recall Search by Date Range Not Working on Your AI PC"
slug: recall-search-date-range-not-working-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["recall", "search", "date range", "copilot plus pc", "timeline", "troubleshooting"]
description: "Fix Recall search by date range not working on your Copilot+ PC with checks for filters, snapshots, indexing, time settings, and a clean Recall reset."
thumbnail: "/images/thumbs/recall-search-date-range-not-working-fix.webp"
faqs:
  - q: "Why does Recall search work for keywords but not for dates?"
    a: "Keyword search scans snapshot text, while date search depends on snapshot timestamps and the timeline index. If timestamps are wrong or the index is incomplete, keywords still work but date filters return nothing."
  - q: "Can a wrong system clock break Recall date search?"
    a: "Yes. Recall stamps each snapshot with the system time, so a clock that jumped after travel, a battery change, or a time-zone error puts snapshots on the wrong dates and makes date filters miss them."
  - q: "Will resetting Recall delete my snapshots?"
    a: "Resetting Recall through its settings clears the snapshot store on that PC. Export or note anything important first, and only reset after the gentler fixes in this guide have failed."
  - q: "Does Recall date search need an internet connection?"
    a: "No. Recall search runs locally on your Copilot+ PC using the NPU. A missing internet connection should not affect date filtering, though Windows Update can still be needed to fix a broken Recall component."
---

You remember roughly when you saw that document — last Tuesday, or sometime in the second week of the month — but Recall's date filter returns nothing, shows the wrong days, or greys out the range entirely. Keyword search still works, which makes the failure more confusing: the snapshots are clearly there, yet the calendar refuses to find them.

Date-range search is a different mechanism from keyword search. It depends on accurate snapshot timestamps, a healthy timeline index, and a date picker that is actually talking to that index.

This guide works through the problem in order: filter and clock checks first, then snapshot health, then index repair and a careful reset. Test the same date range after each fix so you can tell exactly which step restored it.

## Why this happens

- **Date filter applied on top of another filter:** A leftover app filter, keyword, or snapshot-type filter narrows the results so far that the date range appears empty even though snapshots exist.
- **System clock or time-zone error:** Snapshots stamped with the wrong time land on the wrong dates, so the range you pick contains no snapshots at all.
- **Timeline index incomplete or corrupted:** If Recall stopped indexing, paused during an update, or hit a corrupted entry, the date index falls behind the snapshot store.
- **Snapshots paused, deleted, or filtered out:** A paused Recall, an excluded app or website, or an automatic cleanup rule can remove exactly the days you are searching for.
- **Recall component outdated or damaged:** A failed Windows update or a damaged Recall package can break the date picker while leaving keyword search untouched.
- **Search window set to the wrong scope:** Searching within a single app or a filtered view, rather than the full timeline, hides snapshots from other days that should match.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear every filter and test a wide date range

Before assuming anything is broken, prove the snapshots are actually missing from the range.

1. Open **Recall** and clear the search box, the app filter, and any snapshot-type filter completely.
2. Set the date range deliberately wide — a full month that definitely includes recent activity.
3. Search with no keyword at all and scroll the timeline to see whether snapshots appear on the expected days.
4. If snapshots appear in the wide range but not the narrow one, your original range was simply off — adjust it and stop here.

### Fix 2: Correct the system clock and time zone

Recall trusts the system clock completely, so even a small drift can shift snapshots across midnight and out of your range.

1. Open **Settings > Time & language > Date & time** and turn **Set time automatically** and **Set time zone automatically** both **On**.
2. Click **Sync now** to force an immediate correction from the time server.
3. Compare the displayed date and time with a known-good source, such as your phone.
4. Reopen Recall and search the corrected range — snapshots taken under the wrong clock will still sit on their stamped dates, so also search a day either side.

### Fix 3: Confirm Recall is running and snapshots exist for those dates

Date search cannot return what was never captured.

1. Open **Settings > Privacy & security > Recall & snapshots** and confirm **Save snapshots** is turned **On**.
2. Check the storage figure — if it is very low or zero, snapshots may have been cleared or never started.
3. Scroll the Recall timeline manually, without any search, across the missing dates to see whether snapshots exist at all.
4. Look for excluded apps or websites in the Recall settings that might cover exactly what you are looking for.

### Fix 4: Restart Recall and rebuild its timeline index

When snapshots exist but date search misses them, the timeline index is the prime suspect.

1. Close Recall completely, then restart the PC to clear any stuck Recall process.
2. Reopen Recall and wait a few minutes before searching — re-indexing is not instant after a restart.
3. Search a single known date that definitely has snapshots, using no keyword, to test the index directly.
4. If that date now works, test your original range; a partial recovery usually means indexing is still catching up, so wait longer.

### Fix 5: Repair Recall with a Windows update and component check

A damaged Recall component can break date filtering while keyword search limps along on a separate path.

1. Open **Settings > Windows Update** and install every pending update, including optional updates that mention Recall or Copilot+ features.
2. Restart the PC even if Windows does not prompt you — Recall components only reload on a full restart.
3. Reopen Recall and test the same date range with no other filters applied.
4. If the date picker itself is greyed out or unresponsive, try a different user profile briefly to rule out profile corruption — see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for current guidance.
5. A greyed-out picker on every profile points to a system component problem, not your data — note it before attempting Fix 6, since a reset will not fix a broken package.

### Fix 6: Reset Recall snapshots as a last resort

When every gentler fix fails and snapshots exist but date search still returns nothing, the snapshot store itself may be corrupted. The same careful, last-resort logic applies when snapshots vanish entirely, as covered in [Recall snapshots missing after a password change](/articles/recall-snapshots-after-password-change-fix/), and a related display-timing fault is fixed in [Dynamic refresh rate problems on AI laptops](/articles/dynamic-refresh-rate-ai-laptop-fix/). If you are setting up a fresh machine instead, the walkthrough in [Copilot+ PC setup stuck](/articles/copilot-plus-pc-setup-stuck/) helps avoid the misconfiguration that leads here.

1. Open **Settings > Privacy & security > Recall & snapshots** and choose the option to delete snapshots.
2. Confirm the deletion, then restart the PC before doing anything else.
3. Re-enable **Save snapshots** and use the PC normally for a day so a fresh, healthy store builds up.
4. Test date search on the new snapshots — a narrow range, a wide range, and a single day — before concluding the fix worked.
5. If even fresh snapshots fail date search, contact your PC maker's support with the update history from Fix 5, since the fault is then in the device image rather than your data.

## Closing

Recall date search fails when the filter, the clock, or the timeline index disagrees with the snapshots themselves. Clear the filters, fix the clock, and confirm snapshots exist before you touch the index — and only reset the store when every gentler step has proven the data itself is the problem.
