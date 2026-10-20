---
title: "How to Fix Recall Not Filtering Sensitive Information on Your Copilot+ PC"
slug: recall-not-filtering-sensitive-info
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall", "sensitive information", "copilot+ pc", "privacy", "troubleshooting", "ai pc"]
description: "Recall should hide passwords and card numbers from its snapshots. Here is why sensitive-information filtering fails and how to restore it on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-not-filtering-sensitive-info.webp"
faqs:
  - q: "Why is Recall saving my passwords even though filtering is on?"
    a: "The filter runs on an on-device AI model that must be active and current. If the model has not finished downloading, the NPU is unavailable, or the app draws password fields unusually, Recall may capture the text. Toggle the filter off and on, then install the latest Windows updates to refresh the model."
  - q: "Does the sensitive information filter work in every app?"
    a: "It works across most desktop apps and browsers, but it is not perfect. Apps with custom-drawn controls or unusual text rendering can slip past detection. For apps that consistently leak sensitive text, add them to the Recall app filter list so their windows are never snapshotted."
  - q: "Can I delete snapshots that already contain sensitive information?"
    a: "Yes. Open Settings, go to Privacy and security, then Recall and snapshots, and delete snapshots from a date range or clear everything. If you are also thinking about relocating storage, read our guide to [Recall snapshots on an external drive](/articles/recall-snapshots-external-drive/) before moving anything."
  - q: "Does Recall filter credit card numbers typed into websites?"
    a: "Yes, card numbers and common ID formats are part of what the filter detects, and private browsing windows are excluded from snapshots entirely. Filtering applies at capture time, so a card number typed before the filter was enabled stays in old snapshots until you delete them."
---

Windows Recall on Copilot+ PCs is supposed to be privacy-aware, with an on-device filter that keeps passwords, credit card numbers, and ID numbers out of your snapshots. When that filter stops working, you open your timeline to find your banking password or card details sitting in plain text.

A failed filter is worse than a typical glitch: Recall keeps a searchable visual history of everything you do, so sensitive data ends up stored exactly where you expected it hidden. The good news is that most causes are simple — a stalled toggle, an outdated AI model, or an app needing exclusion — each with a clear fix.

This guide explains why Recall stops filtering sensitive information and how to get it working again, plus which apps the filter struggles with and how to exclude them. The same on-device AI pipeline drives other Copilot+ features, so if [Copilot stops remembering your conversation](/articles/copilot-not-remembering-conversation/), a healthy filter stack often helps there too.

## Why this happens

- **The filter toggle is off:** Updates and setup flows can leave the "Filter sensitive information" switch disabled, so Recall snapshots everything unfiltered.
- **The on-device AI model is stale or missing:** The filter runs on a small model delivered through Windows Update. If it never finished downloading, filtering silently does nothing.
- **The NPU is not running the model:** Filtering is accelerated by your laptop's neural processing unit. If the [NPU is not being used by apps](/articles/npu-not-used-by-apps-windows-11/), the filter can degrade or fail without an error.
- **The app renders text unusually:** Custom-drawn password fields, virtualized lists, and game-style overlays can bypass the text detection the filter depends on.
- **Old snapshots predate the fix:** Filtering applies at capture time. Snapshots taken while the filter was broken keep their sensitive content until deleted.
- **A managed device policy overrides it:** On work laptops, IT policy can control Recall behavior and conflict with the filter setting you see.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the filter toggle is actually on

Start with the obvious: open Settings, go to Privacy and security, then Recall and snapshots, and check the "Filter sensitive information" switch. If it is off, turn it on. If it is already on, toggle it off, wait ten seconds, and back on — this reloads the filtering model and clears stuck states. Then test: type a dummy password into a login field and search Recall for it. If the switch is greyed out, a device policy is in control — see Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows).

1. Press Windows key + I to open Settings.
2. Go to Privacy and security, then Recall and snapshots.
3. Find the "Filter sensitive information" toggle.
4. If off, turn it on. If on, toggle it off and back on after ten seconds.
5. Test with a dummy password, then search Recall for it.

### Fix 2: Update Windows to refresh the filtering model

The filter depends on an AI model delivered through Windows Update, separately from Recall itself. A stale model misses newer card and ID formats, and a partially downloaded one can fail silently. Install every pending update including optional drivers, restart, then stay connected for ten minutes so model components finish downloading. Confirm new snapshots are still being captured on schedule, since capture and filtering share the same pipeline.

1. Open Settings and go to Windows Update.
2. Click Check for updates and install everything offered.
3. Install optional driver updates under Advanced options.
4. Restart and stay online for ten minutes.
5. Retest filtering with a sample card number in a text field.

### Fix 3: Make sure the NPU is running Recall's AI work

Recall's detection is designed to run on your Copilot+ PC's neural processing unit. When the NPU driver is broken or the NPU is disabled, the filter can degrade with no error message. Open Task Manager with Ctrl + Shift + Esc, go to the Performance tab, and confirm the NPU entry is present and shows activity. If it is missing, reinstall the driver via Windows Update or your laptop maker's support site. Avoid starving the AI stack: heavy background AI tasks can delay filtering enough that a snapshot saves before analysis finishes.

1. Open Task Manager (Ctrl + Shift + Esc), Performance tab, and check for the NPU.
2. If the NPU is missing, reinstall its driver via Windows Update.
3. Close unnecessary apps to free AI processing capacity.
4. Retest filtering once the NPU shows normal activity.

### Fix 4: Add problem apps to the exclusion list

Some apps defeat the text detector no matter how healthy your system is — password managers with secure desktops, remote desktop clients, and apps with custom rendering are typical offenders. Recall lets you exclude entire apps and websites from snapshots. In the Recall and snapshots settings, use the Filter apps and Filter websites options to add every app where you handle sensitive data. This is a stronger guarantee than the sensitive-info filter because excluded apps are never captured at all. Be generous: banking apps, password managers, and work tools showing personal data all belong on the list.

1. Open Settings, Privacy and security, Recall and snapshots.
2. Under Filter apps, add apps that handle sensitive data.
3. Under Filter websites, add sensitive sites.
4. Delete old snapshots that captured sensitive content.
5. Verify new activity in those apps no longer appears.

### Fix 5: Purge old snapshots and reset Recall's state

Snapshots captured while the filter was broken keep their sensitive content until deleted, and a corrupted snapshot database can keep Recall misbehaving after the cause is fixed. Delete snapshots from the affected date range — or clear everything — in the Recall and snapshots settings. Then turn Recall off, restart, and turn it back on to rebuild the database and re-initialize the filter. Only do this after the earlier fixes, since deletion is irreversible.

1. Go to Settings, Privacy and security, Recall and snapshots.
2. Delete snapshots from the affected period, or all snapshots.
3. Turn Recall off entirely and restart your PC.
4. Turn Recall back on and re-enable the sensitive information filter.
5. Confirm new snapshots filter correctly with a quick test.

## Closing

Recall's sensitive-information filter is only as reliable as the toggle, the AI model, and the NPU underneath it. Most failures trace to a disabled switch, a stale model, or an app needing exclusion — all fixable in minutes. Work through the fixes in order, delete snapshots captured while the filter was down, and keep Windows updated.
