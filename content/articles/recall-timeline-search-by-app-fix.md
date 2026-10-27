---
title: "How to Fix Recall Timeline Search by App Not Working on Your AI PC"
slug: recall-timeline-search-by-app-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["recall", "timeline", "search by app", "copilot plus pc", "snapshots", "troubleshooting"]
description: "Fix Recall timeline search by app not working on your Copilot+ PC with filter checks, app exclusions, snapshot verification, and an index repair step by step."
thumbnail: "/images/thumbs/recall-timeline-search-by-app-fix.webp"
faqs:
  - q: "Why does Recall find an app in general search but not in app search?"
    a: "General search scans snapshot text across all apps, while app search filters by the app recorded for each snapshot. If the app was excluded, renamed, or recorded under a different name, the filter misses snapshots that general search still finds."
  - q: "Can an excluded app still appear in Recall app search?"
    a: "No. Excluded apps and websites are never captured, so they produce no snapshots and cannot appear in app-filtered results. Remove the app from the exclusion list to capture it going forward."
  - q: "Does reinstalling an app break Recall app search for it?"
    a: "It can. Reinstalling can change the app's recorded identity, so older snapshots stay filed under the old identity while new snapshots file under the new one. Searching both names, or without a filter, finds the full set."
  - q: "Will resetting Recall fix app search?"
    a: "It can fix a corrupted app index, but it deletes existing snapshots. Try the filter, exclusion, and restart fixes first, and reset only if app search fails for every app, not just one."
---

You know you were working in a particular app — a browser, a document editor, a chat window — but Recall's search by app returns nothing for it, or shows only a fraction of the sessions you remember. General Recall search still finds the content, which proves the snapshots exist; the app filter just refuses to see them.

App-filtered search depends on a separate piece of bookkeeping: every snapshot must be tagged with the app that was in the foreground when it was taken.

This guide restores that sync in order: filter and exclusion checks first, then snapshot verification, then index repair and a careful reset for the case where every app is affected.

## Why this happens

- **App filter combined with another filter:** A leftover keyword, date range, or snapshot-type filter narrows app results to nothing even though the app has snapshots.
- **App or website excluded from Recall:** An excluded app is never captured, so it correctly — but confusingly — returns no app-filtered results.
- **App renamed, reinstalled, or updated:** A changed app identity splits snapshots between the old and new names, so filtering by the current name misses the older half.
- **Snapshot tagging failed for that app:** Full-screen apps, elevated apps, and some browser windows can be captured without a reliable app tag, leaving them invisible to app search.
- **Timeline index corrupted for app metadata:** If the app-tag index is damaged, app filtering fails while text search, which uses a different index, keeps working.
- **Searching the wrong scope or view:** An app filter applied inside a single-day view, or inside another filtered view, hides snapshots from other days that belong to the same app.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear all other filters and test the app filter alone

Prove the app filter itself is the problem before blaming the app or the index.

1. Open **Recall** and clear the search box, the date range, and any snapshot-type filter completely.
2. Apply only the app filter for the app in question, with no keyword at all.
3. Scroll the full timeline for that app and note whether any snapshots appear.
4. If snapshots appear without a keyword but not with one, the keyword was the blocker — refine it and stop here.

### Fix 2: Check whether the app is excluded from Recall

An excluded app produces exactly this symptom by design, and exclusions are easy to set accidentally when dismissing a prompt.

1. Open **Settings > Privacy & security > Recall & snapshots** and review the excluded apps and websites list.
2. If your app is listed, remove it from the exclusion list.
3. Confirm **Save snapshots** is still **On** after changing the list.
4. Use the app normally for a while, then check app search again — only new snapshots will appear, since excluded periods were never captured.

### Fix 3: Verify snapshots for that app exist without the filter

General search is your ground truth here: if it finds the app's content, the snapshots exist and only the app tag is missing or mismatched.

1. Clear the app filter and search Recall for a distinctive word or phrase you know appeared in that app.
2. Open a matching snapshot and check which app Recall says it belongs to — a generic label or a different app name explains the filter failure.
3. Try filtering by that recorded name instead of the app's current name; a renamed or reinstalled app often hides under its old identity.
4. If general search finds nothing for the app either, the app was not captured at all — return to Fix 2 and check for a broader exclusion.

### Fix 4: Restart Recall and let the app index rebuild

A restart clears stuck Recall processes and gives the timeline index a chance to rebuild its app tags.

1. Close Recall completely and restart the PC to clear any stuck snapshot service.
2. Reopen Recall and wait several minutes before testing — index rebuilding is not instant.
3. Test the app filter alone, with no keyword, for an app you know has recent snapshots.
4. If that app now works, test your original app; a staggered recovery means indexing is still catching up — see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for current guidance.

### Fix 5: Handle a renamed or reinstalled app's split history

When an app was reinstalled or renamed, its snapshots split across two identities, and no single filter shows the whole history.

1. Search without any app filter for content from the app, and note the different app names Recall assigns to old and new snapshots.
2. Filter by each recorded name in turn and note which periods each one covers.
3. Going forward, use the current name for new work and the old name when hunting older sessions.
4. Avoid reinstalling the app again unnecessarily — each reinstall risks another identity split.
5. If the split history is unacceptable and the old snapshots are not valuable, only then consider the reset in Fix 6.

### Fix 6: Reset Recall when app search fails for every app

A reset is justified when app filtering fails across the board, not for a single app — that pattern points to a corrupted app index rather than one app's tagging. A related viewer fault with its own repair path is described in [Recall snapshot viewer zoom not working](/articles/recall-snapshot-viewer-zoom-fix/), and a separate ARM app problem is covered in [Slack issues on ARM Windows](/articles/slack-arm-windows-issues-fix/). For a language-related Copilot+ fault, see [Click to Do language support missing](/articles/click-to-do-language-support-missing/).

1. Confirm app search fails for at least three unrelated apps, each tested alone with no keyword.
2. Open **Settings > Privacy & security > Recall & snapshots** and delete the existing snapshots.
3. Restart the PC, re-enable **Save snapshots**, and use several apps normally for a day.
4. Test app search for each of those apps — all of them should now filter correctly on fresh snapshots.
5. If even fresh snapshots fail app filtering, the fault is in the device image: update Windows fully and contact your PC maker's support with the multi-app test result.

## Closing

Recall search by app fails when the filter, the exclusion list, or the app's recorded identity disagrees with the snapshots themselves. Clear the other filters, check exclusions, and verify the snapshots with general search before you touch the index — and reset only when app filtering fails for every app, not just one.
