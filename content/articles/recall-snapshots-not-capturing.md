---
title: "Recall Snapshots Not Capturing Apps? Fix It Step by Step"
slug: recall-snapshots-not-capturing
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Recall", "Copilot+ PC", "Windows 11", "snapshots", "apps"]
description: "Recall not capturing certain apps? Learn why snapshots skip programs and how to get full timeline coverage back on your Copilot+ PC with simple fixes."
thumbnail: "/images/thumbs/recall-snapshots-not-capturing.webp"
faqs:
  - q: "Why is Recall not capturing some of my apps?"
    a: >
      The most common reasons are app exclusions, private browsing sessions,
      DRM-protected content, or apps that block screen capture. Recall also
      skips snapshots when the PC is idle, locked, or running on a filtered
      account, so not every open window is guaranteed a snapshot.
  - q: "Does Recall capture everything on screen?"
    a: >
      No. Recall intentionally skips private browsing windows, DRM-protected
      video, and any app or website you add to the exclusion list. It also
      pauses during remote sessions and when the device is locked, by design.
  - q: "Can I force Recall to capture a specific app?"
    a: >
      Yes, if the app is not excluded and does not block capture. Remove it from
      the exclusion list in Recall settings, restart the app, and use it actively
      for a few minutes — snapshots are taken while you interact, not for idle
      background windows.
  - q: "Will reinstalling Recall fix missing app snapshots?"
    a: >
      Reinstalling is rarely needed. Checking exclusions, filters, and the
      snapshot service usually restores capture faster and without losing your
      existing timeline. Only reset snapshot data if corruption is confirmed.
---

Recall is meant to quietly record what you were doing so you can find it later, but sometimes it skips apps entirely. You might find snapshots of your browser and documents while your design tool, chat app, or code editor never appears in the timeline. That gap defeats the purpose of Recall, and it is natural to wonder whether the feature is broken or just picky about what it records.

In most cases Recall is not broken — it is following rules you may not know about. Exclusions, DRM protection, private sessions, and capture-blocking apps all create blind spots by design. Other times the snapshot service is paused, the app is running in a mode Recall ignores, or a setting was changed by an update. Sorting out which category your missing app falls into tells you whether a fix exists or whether the gap is expected.

It also helps to rule out wider AI problems before blaming Recall alone. If [live captions keep crashing](/articles/live-captions-crashing-fix/) or [Windows Hello reports that the camera cannot be found](/articles/windows-hello-camera-not-found-ai/), a shared service or driver issue may be affecting several features at once. And if your whole machine has slowed down, our guide to fixing [an AI PC that is slow after a Windows update](/articles/ai-pc-slow-after-windows-update/) covers the update-related causes that can stall snapshot capture too.

## Why this happens

- **App or website exclusions:** Anything on Recall's exclusion list is deliberately skipped, and exclusions can be added accidentally or carried over from an earlier setup.
- **DRM-protected content:** Video players and streaming apps that use digital rights management block screen capture, so Recall cannot snapshot them.
- **Private browsing sessions:** InPrivate and incognito windows are never captured, even if the same browser is captured in normal mode.
- **Capture-blocking apps:** Some security tools, banking apps, and remote desktop clients actively block screen capture for privacy reasons.
- **Idle or locked screen:** Recall only snapshots while you are actively using the PC; idle, locked, and sleeping states produce no snapshots.
- **Snapshot service paused:** If the service is paused, stopped, or stuck after an update, no new snapshots appear for any app.
- **App running as administrator or in a protected mode:** Elevated or sandboxed windows can sit outside Recall's normal capture path.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the exclusion list first

Exclusions are the number one cause of missing app snapshots. Open Recall settings and review every entry on the app and website exclusion lists. Remove anything you do not recognise or no longer need, then use the app normally for a while and check whether snapshots start appearing.

1. Open Settings, go to Privacy & security, then Recall & snapshots.
2. Open the app exclusion list and scan it carefully.
3. Remove the app that is missing from your timeline.
4. Do the same for the website exclusion list.
5. Restart the app and use it actively for 10 minutes.
6. Open Recall and confirm new snapshots of that app appear.

### Fix 2: Confirm the app is not DRM-protected or capture-blocked

Some apps simply cannot be captured, and no setting will change that. Streaming video, certain banking apps, and remote desktop sessions block capture at the system level. Test with a normal app side by side: if other apps capture fine but one never does, the block is almost certainly inside that app.

1. Open the problem app and a normal app such as Notepad together.
2. Use both actively for several minutes.
3. Check Recall for snapshots of each.
4. If only the problem app is missing, check its own privacy settings.
5. Look for a "block screen capture" option in the app and disable it if present.
6. Accept that DRM video and private sessions will remain uncaptured by design.

### Fix 3: Restart the snapshot service

When no app is being captured, the service itself is the suspect. Restarting it clears stuck states and forces a fresh capture cycle. This is a safe, quick step that fixes many cases where Recall silently stopped after an update or a long sleep.

1. Press Windows + R, type `services.msc`, and press Enter.
2. Locate the Recall snapshot service.
3. Right-click it and choose Restart.
4. If Restart is unavailable, stop it, wait 10 seconds, then start it.
5. Use your PC normally for 15 minutes.
6. Open Recall and verify that fresh snapshots are appearing.

### Fix 4: Make sure the PC is active and unlocked while you work

Recall deliberately skips idle and locked screens, so a workflow that involves long pauses, frequent locking, or remote sessions will produce gaps. If you step away often, snapshots resume when you return and interact again — but nothing is captured while you are gone, and that is normal behaviour, not a fault.

1. Keep the PC awake and unlocked while you expect snapshots.
2. Interact with the app — click, scroll, or type — rather than leaving it idle.
3. Avoid remote desktop sessions for work you want Recall to capture.
4. Check Power settings so the screen does not sleep after a minute.
5. After active use, confirm snapshots appear for that time window.

### Fix 5: Update Windows and the app

Capture bugs are regularly fixed in Windows updates, and app developers also patch capture-blocking behaviour over time. If your missing-app problem started recently, an update on either side may already contain the fix, so bringing both up to date is worth doing before deeper troubleshooting.

1. Open Settings, go to Windows Update, and install all pending updates.
2. Restart your PC after updating.
3. Update the problem app from the Microsoft Store or the developer's site.
4. Re-enable snapshots in Recall settings if the update changed them.
5. Test the app again for 15 minutes and check the timeline.
6. For known issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Reset snapshot settings without deleting history

If exclusions look clean and the service is running, a settings reset can clear a hidden misconfiguration. Do this carefully: choose the option that resets preferences, not the one that deletes all snapshots, so your existing timeline survives while capture behaviour returns to defaults.

1. Close the Recall app.
2. Open Settings, go to Privacy & security, then Recall & snapshots.
3. Review and reset snapshot preferences to defaults.
4. Remove and re-add any exclusions you genuinely want to keep.
5. Restart your PC and use the problem app actively.
6. Confirm new snapshots appear within half an hour.

### Fix 7: Check for conflicting security software

Some antivirus and privacy tools block screen capture across the whole system, which looks exactly like Recall failing. Temporarily disabling such a tool's screen-protection feature — not the whole antivirus — and testing capture will tell you whether it is the culprit.

1. Open your security software's settings.
2. Look for screen capture, anti-screenshot, or privacy protection options.
3. Temporarily disable the screen-capture protection only.
4. Use the problem app for 10 minutes and check Recall.
5. If snapshots return, add Recall as a trusted exception in the security tool.
6. Re-enable protection with the exception in place.

## Closing

When Recall skips an app, the cause is usually an exclusion, a capture block, or a paused service — all fixable in a few minutes once you know where to look. Work through the checks above in order, and remember that DRM content and private browsing will always stay out of the timeline by design. Once capture is flowing again, your timeline becomes the reliable memory it was meant to be.
