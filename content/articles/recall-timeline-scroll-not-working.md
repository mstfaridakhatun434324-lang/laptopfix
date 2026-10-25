---
title: "Recall Timeline Scroll Not Working? Fix It Step by Step"
slug: recall-timeline-scroll-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "timeline", "scrolling"]
description: "Can't scroll the Recall timeline? Learn why scrolling freezes or jumps and how to restore smooth timeline navigation on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-timeline-scroll-not-working.webp"
faqs:
  - q: "Why won't my Recall timeline scroll?"
    a: >
      Scrolling can break when the timeline is loading a large snapshot set,
      the app is busy indexing, the graphics driver glitches, or the app
      window itself is frozen. Touchpad and mouse settings can also make
      scrolling feel broken when the app is actually fine.
  - q: "Is my timeline data lost if scrolling fails?"
    a: >
      No. A scrolling problem is a display issue, not a data issue. Your
      snapshots remain stored and searchable even while the timeline view
      refuses to scroll, and search still works as a workaround.
  - q: "Does timeline scrolling depend on my mouse or touchpad?"
    a: >
      Partly. If scrolling works in other apps but not Recall, the app is at
      fault. If scrolling fails everywhere, the input device or its driver
      is the problem and Recall is innocent.
  - q: "Can I navigate the timeline without scrolling?"
    a: >
      Yes. Use Recall search, jump to a specific date, or use keyboard
      navigation where available. These workarounds keep your history
      accessible while you fix the scrolling problem.
---

You open Recall, try to scroll back through your timeline, and nothing happens — or the view jumps, stutters, and snaps back to where it started. It is a maddening failure because the whole point of a timeline is browsing it, and being stuck at one point in time makes the feature feel broken even when your snapshots are perfectly safe.

Scrolling failures are usually interface problems, not data problems. The timeline may be struggling to load thousands of snapshots, the app may be frozen mid-index, or the graphics pipeline may be glitching. Input devices add another layer: a touchpad driver problem can look exactly like a Recall bug. Sorting out which layer is at fault tells you which fix to apply.

It helps to check whether the problem is Recall-only or system-wide, and whether other AI features are affected. If [Qualcomm NPU driver installation failed](/articles/qualcomm-npu-driver-install-failed/) on your machine, or you own an [MSI Prestige 13 with AI issues](/articles/msi-prestige-13-ai-issues/), broader driver trouble may be involved. And if Copilot's Outlook features are also off, see our guide to [Copilot Outlook draft coaching missing](/articles/copilot-outlook-draft-coaching-missing/) for the overlapping service checks.

## Why this happens

- **Timeline still loading:** A large snapshot store takes time to load, and scrolling during load feels frozen or jumpy.
- **App frozen during indexing:** Heavy background indexing can make the Recall window unresponsive to scroll input.
- **Graphics driver glitch:** A driver problem can break smooth scrolling and rendering in the timeline view.
- **Input device driver issue:** Touchpad or mouse driver faults break scrolling in Recall and often in other apps too.
- **Corrupted timeline cache:** A damaged local cache can make the timeline view misbehave while search still works.
- **Window size or display scaling problem:** Odd window sizes and non-standard scaling can break the timeline's scroll calculations.
- **Too many snapshots in one view:** Very dense days with thousands of snapshots can overwhelm the timeline renderer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test whether scrolling works elsewhere

This one test splits the problem in half. If scrolling fails in every app, fix the input device; if it fails only in Recall, fix Recall. Skipping this test leads to fixing the wrong thing.

1. Open a browser or File Explorer window.
2. Try scrolling with the same mouse or touchpad.
3. If scrolling fails everywhere, update the touchpad or mouse driver first.
4. If scrolling works elsewhere, the problem is Recall-specific — continue below.
5. Try a different input device, such as an external mouse, to confirm.
6. Note the result before proceeding, since it directs the rest of the fix.

### Fix 2: Restart the Recall app and wait for loading

A frozen or half-loaded timeline often recovers with a clean restart and a little patience. Close Recall fully, reopen it, and give it time to load before touching the scroll — impatience during load is itself a common cause of the jumpy behaviour.

1. Close the Recall app completely.
2. Wait 30 seconds.
3. Reopen Recall and do not scroll immediately.
4. Wait for the timeline to finish loading its current view.
5. Try scrolling slowly, one section at a time.
6. If scrolling works after loading, the issue was load timing.

### Fix 3: Narrow the timeline view

Very dense days overwhelm the renderer. Narrowing the view — by date, by app filter, or by searching first — reduces what the timeline must render and restores smooth scrolling even on a large snapshot store.

1. Open Recall and use search to find a specific item first.
2. Use the date navigation to jump to a single day.
3. Apply an app filter to reduce the visible snapshots.
4. Scroll within the narrowed view.
5. If scrolling works, the problem was renderer overload.
6. Keep using filters for very busy days going forward.

### Fix 4: Update the graphics driver

Scrolling and rendering glitches often come from the display driver. Updating it fixes the rendering path Recall's timeline depends on, and it is a safe, standard maintenance step.

1. Open Settings, go to Windows Update, and install pending updates.
2. Open Device Manager and expand Display adapters.
3. Right-click your graphics adapter and choose Update driver.
4. Restart after installing.
5. Reopen Recall and test scrolling.
6. If the driver was already current, try the manufacturer's support tool for a newer version.

### Fix 5: Reset the window size and display scaling

Odd window geometries and non-standard scaling can break scroll math in the timeline view. Restoring defaults — maximised window, recommended scaling — removes this whole class of glitch.

1. Maximise the Recall window.
2. Open Settings, go to System, then Display.
3. Set scaling to the recommended value.
4. Set the display to its native resolution.
5. Sign out and back in if prompted.
6. Reopen Recall and test timeline scrolling.

### Fix 6: Clear the timeline cache

A corrupted local cache can make the timeline view misbehave while leaving search and snapshots intact. Clearing it forces Recall to rebuild the view, which usually restores scrolling without touching your snapshot data.

1. Close the Recall app completely.
2. Restart the snapshot service from the Services console.
3. Reopen Recall and let it rebuild the timeline view.
4. Wait several minutes for large timelines to reload.
5. Test scrolling across several days.
6. If scrolling remains broken, consider a snapshot store reset as a last resort.

### Fix 7: Check for Windows updates and app repairs

Recall is a system feature, so its fixes arrive through Windows Update. If scrolling broke after an update, a follow-up patch may already exist; if the app itself is damaged, a system repair can restore it.

1. Open Settings, go to Windows Update, and check for updates.
2. Install everything offered and restart.
3. Test Recall scrolling after the update.
4. If the problem persists, run System File Checker from an administrator terminal.
5. Restart once more and retest.
6. For ongoing issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

A Recall timeline that will not scroll is almost never a data problem — your snapshots are safe, and search still reaches them. The fix is usually a restart, a narrower view, or a driver update, applied in that order. Once scrolling is smooth again, browsing your history feels natural, which is exactly what a timeline is for.
