---
title: "Recall App Exclusions Not Working? Fix It Step by Step"
slug: recall-app-exclusions-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "exclusions", "privacy"]
description: "Recall still capturing excluded apps? Learn why exclusions fail and how to make Recall respect your app and website exclusions on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-app-exclusions-not-working.webp"
faqs:
  - q: "Why is Recall still capturing an excluded app?"
    a: >
      The usual reasons are that the app was added under a different name or
      process, the exclusion needs an app restart to take effect, snapshots
      were taken before the exclusion was added, or the snapshot service has
      not picked up the new settings yet.
  - q: "Do exclusions delete old snapshots of that app?"
    a: >
      No. Adding an exclusion only stops future snapshots. Snapshots taken
      before the exclusion remain in your timeline until you delete them
      separately, which is an important privacy detail to know.
  - q: "Can I exclude websites as well as apps?"
    a: >
      Yes. Recall has separate exclusion lists for apps and websites. A
      browser exclusion does not automatically cover sites visited in it, so
      add sensitive websites to the website list as well.
  - q: "How do I check whether an exclusion is working?"
    a: >
      Use the excluded app actively for 15 minutes, then search your Recall
      timeline for that period. If no new snapshots of the app appear, the
      exclusion is working; older snapshots do not count against it.
---

You added an app to Recall's exclusion list for privacy — maybe a banking app, a chat tool, or a work system — and then found it in your timeline anyway. That is more than an annoyance; exclusions exist so sensitive content stays out of Recall, and when they fail, the privacy promise fails with them. The fix matters, and fortunately the causes are usually straightforward.

Exclusion failures fall into a few buckets. Sometimes the app is listed under a different executable name than the one you excluded, so Recall keeps capturing it under its real process name. Sometimes the exclusion is correct but has not taken effect yet because the app or the service needs a restart. And sometimes the snapshots you are seeing predate the exclusion, which looks like failure but is actually expected behaviour. Telling these apart is the first step.

Check the wider system too, since a stuck service can ignore new settings entirely. If your NPU is hidden in Device Manager, see our guide to [NPU hidden in Device Manager](/articles/npu-hidden-device-manager/), and Samsung users should check [Samsung Galaxy Book5 Pro AI issues](/articles/samsung-galaxy-book5-pro-ai-issues/). If you also use Copilot's canvas features, our guide to [Copilot canvas not working](/articles/copilot-canvas-not-working/) covers related settings-sync problems.

## Why this happens

- **Wrong process name excluded:** Apps can run under helper processes or renamed executables, so the exclusion misses the actual capturing process.
- **Exclusion needs an app restart:** Recall reads exclusions when an app launches, so already-running apps keep being captured until restarted.
- **Snapshots predate the exclusion:** Old snapshots remain in the timeline and look like the exclusion failed.
- **Snapshot service not refreshed:** A stuck service may not pick up new exclusion settings until restarted.
- **Browser vs website confusion:** Excluding a browser does not exclude specific sites, and vice versa.
- **Multiple app editions installed:** Store and desktop versions of the same app can have different identities, and only one may be excluded.
- **Settings reset by an update:** A Windows update can silently clear or alter exclusion lists.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the exclusion and delete pre-existing snapshots

First, confirm what you are actually seeing. Check the exclusion list, note when the snapshots were taken, and delete any that predate the exclusion. If only old snapshots appear, the exclusion may already be working fine.

1. Open Settings, go to Privacy & security, then Recall & snapshots.
2. Confirm the app is on the exclusion list, spelled exactly as installed.
3. Open Recall and check the dates on the snapshots of that app.
4. Delete snapshots from before the exclusion date.
5. Use the app actively for 15 minutes.
6. Recheck Recall to see whether any new snapshots appear.

### Fix 2: Restart the app and the snapshot service

Exclusions often need a fresh app launch to take effect, and a stuck service may need a restart to notice the change. Doing both together covers the two most common timing problems in one pass.

1. Close the excluded app completely, including its system tray icon.
2. Press Windows + R, type `services.msc`, and press Enter.
3. Restart the Recall snapshot service.
4. Relaunch the excluded app and use it for 15 minutes.
5. Open Recall and check for new snapshots of it.
6. If none appear, the exclusion is now working.

### Fix 3: Exclude the correct process

Some apps run under launcher or helper processes with different names. If the exclusion seems right but capture continues, identify the app's actual process in Task Manager and exclude that name instead.

1. Launch the app and open Task Manager.
2. Find the app's main process and note its exact name.
3. Compare it with the name on your exclusion list.
4. If they differ, add the correct process name to the exclusion list.
5. Restart the app and test again for 15 minutes.
6. Repeat for helper processes if capture persists.

### Fix 4: Handle Store vs desktop editions

Installing both the Microsoft Store and desktop versions of an app creates two identities. Recall may be excluding one while capturing the other, which looks like a broken exclusion. Exclude both editions or standardise on one.

1. Check whether the app is installed from both the Store and a desktop installer.
2. Add both editions to the exclusion list.
3. Alternatively, uninstall the edition you do not use.
4. Restart the remaining app and the snapshot service.
5. Test for 15 minutes and confirm no new snapshots appear.
6. Keep a note of which edition you kept for future exclusion checks.

### Fix 5: Exclude websites separately from browsers

If the leak is a website rather than an app, the website exclusion list is the right tool. A browser exclusion alone will not stop a specific site from being captured, and a site exclusion alone will not stop the browser's other tabs.

1. Open Recall & snapshots settings.
2. Open the website exclusion list.
3. Add the full domain of the site you want excluded.
4. Close all browser tabs for that site and reopen them fresh.
5. Browse the site for 10 minutes.
6. Confirm no new snapshots of that site appear in Recall.

### Fix 6: Rebuild exclusions after an update

Updates can reset exclusion lists without warning. If exclusions stopped working right after an update, re-check the lists, re-add missing entries, and delete any snapshots captured during the gap.

1. Open Recall & snapshots settings after any major update.
2. Review both the app and website exclusion lists.
3. Re-add any entries that disappeared.
4. Delete snapshots captured while exclusions were missing.
5. Restart the snapshot service.
6. Test each exclusion again over the next day.

### Fix 7: Reset Recall settings if exclusions are ignored entirely

When every exclusion is ignored despite correct names and restarts, the settings store itself may be corrupt. Resetting Recall preferences restores default behaviour; you then rebuild your exclusion lists from scratch, which is tedious but reliable.

1. Export or note your current exclusion lists first.
2. Close the Recall app.
3. Open Settings, go to Privacy & security, then Recall & snapshots.
4. Reset Recall preferences to defaults.
5. Re-add your app and website exclusions.
6. Restart the snapshot service and test each exclusion.
7. For persistent issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Exclusions are a privacy control, so when they fail, treat it seriously — but the fix is usually a restart, a correct process name, or a cleaned-up old snapshot. Verify with a timed test rather than assuming, delete anything captured during the gap, and re-check your lists after every major update. Done properly, your exclusions become trustworthy again, and sensitive apps stay out of your timeline for good.
