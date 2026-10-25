---
title: "Copilot Suggested Prompts Not Showing? Fix It Step by Step"
slug: copilot-prompt-suggestions-not-appearing
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Copilot", "prompts", "Copilot+ PC", "Windows 11", "suggestions"]
description: "Copilot suggested prompts missing? Learn why prompt suggestions vanish and how to bring back helpful Copilot starters on your Copilot+ PC."
thumbnail: "/images/thumbs/copilot-prompt-suggestions-not-appearing.webp"
faqs:
  - q: "Why aren't Copilot suggested prompts showing?"
    a: >
      Suggestions can disappear when the feature is disabled, the app is
      outdated, the window is too narrow to display them, history is empty
      so there is nothing to base suggestions on, or a policy disables
      personalised suggestions.
  - q: "Are suggested prompts personalised?"
    a: >
      Partly. Copilot shows a mix of general starter prompts and suggestions
      based on your recent activity and context. With no recent history,
      suggestions are generic or absent until you build up usage.
  - q: "Can I turn suggested prompts off?"
    a: >
      Yes, in Copilot settings you can usually hide suggestions if you
      prefer a blank input box. The same settings area is where you would
      re-enable them if they vanished unintentionally.
  - q: "Do suggested prompts work in all Copilot versions?"
    a: >
      Availability varies by app version, platform, and rollout stage. The
      web version often shows suggestions before the Windows app does, so
      comparing the two helps identify whether the feature is missing or
      just not yet rolled out to your app.
---

Copilot's suggested prompts are the gentle nudge that gets a conversation started — a few relevant starters under the input box that save you from staring at a blank field. When they vanish, Copilot still works, but it feels emptier and less helpful, especially for new users who relied on those starters to discover what Copilot can do. The disappearance is usually a settings, version, or context issue rather than a real failure.

The key question is whether suggestions are disabled, unavailable in your version, or simply have nothing to base themselves on yet. A brand-new account with no history shows fewer suggestions by design. An outdated app may not show them at all. And a narrow window or a policy block can hide them even when everything else is fine. The fixes below separate these cases cleanly.

Related presence and Paint AI issues can share settings causes. If presence sensing is also off, see our guide to [presence sensing not working](/articles/presence-sensing-not-working/), and if Paint's AI features are missing, check [Paint layers AI features missing](/articles/paint-layers-ai-features-missing/). For performance problems on ARM machines, our guide to [JetBrains IDE slow on ARM Windows](/articles/jetbrains-ide-arm-windows-slow/) covers the resource layer that can delay suggestion rendering.

## Why this happens

- **Suggestions disabled:** The setting may have been turned off, intentionally or accidentally.
- **Outdated app version:** Older Copilot versions may not include the suggestions feature at all.
- **Empty history:** With no recent conversations, Copilot has little context to generate personalised suggestions.
- **Window too narrow:** A small or snapped window can hide the suggestions row to save space.
- **Policy or privacy block:** Work policies or strict privacy settings can disable personalised suggestions.
- **Feature not rolled out:** Suggestions roll out gradually, so they may be absent in your region or app version.
- **Corrupted app state:** A damaged cache can break the suggestions panel while the rest of Copilot works fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the suggestions setting

Start with the toggle. If suggestions were disabled — by you, by an update, or by a settings reset — re-enabling them is instant.

1. Open Copilot settings.
2. Find the suggestions, starters, or personalisation options.
3. Confirm suggested prompts are turned on.
4. If already on, toggle them off and back on.
5. Restart Copilot.
6. Check whether suggestions appear under the input box.

### Fix 2: Maximise the window

Interface space matters: a narrow or snapped Copilot window may hide suggestions to prioritise the input box. Maximising the window is a trivial test that rules out a layout cause.

1. Maximise the Copilot window.
2. Check whether suggestions appear.
3. If they do, the issue was window size.
4. Try different window widths to find the threshold.
5. Keep Copilot wide enough for suggestions during normal use.
6. If suggestions stay absent even maximised, continue below.

### Fix 3: Build up some history first

With a fresh account or after clearing history, Copilot has no context for personalised suggestions. Having a few real conversations gives it material to work with, and suggestions typically appear afterwards.

1. Start several conversations on topics you care about.
2. Ask follow-up questions so Copilot learns your interests.
3. Return to the home screen after a few chats.
4. Check whether suggestions now appear.
5. If only generic starters appear, that is normal for a young account.
6. Keep using Copilot normally — suggestions improve with history.

### Fix 4: Update the Copilot app

Suggestions are a newer feature, and older app versions may lack them entirely. Updating to the latest version is the most reliable way to gain a feature that has not arrived yet.

1. Open the Microsoft Store and update Copilot.
2. Open Settings, go to Windows Update, and install pending updates.
3. Restart after updating.
4. Open Copilot and check for suggestions.
5. Compare with the web version, which often gets features first.
6. If web shows suggestions but the app does not, the app update is still pending.

### Fix 5: Check privacy and policy settings

Strict privacy settings or work policies can suppress personalised suggestions, since suggestions depend on activity data. Reviewing these settings tells you whether suppression is intentional.

1. Open Copilot settings and review privacy options.
2. Confirm personalisation is allowed if you want suggestions.
3. On a work device, check for greyed-out personalisation options.
4. If managed, ask IT whether suggestions are policy-disabled.
5. On a personal PC, disable third-party privacy tools temporarily and retest.
6. Re-enable personalisation and check for suggestions.

### Fix 6: Repair the app

When settings, window size, history, and version all check out but suggestions remain absent, the app's own state may be corrupt. A repair clears the bad state without losing your account data.

1. Open Settings, go to Apps, then Installed apps.
2. Find Copilot and open Advanced options.
3. Choose Repair.
4. Relaunch Copilot and sign in.
5. Check the home screen for suggestions.
6. If Repair fails, choose Reset and repeat the check.

### Fix 7: Use the web version while waiting for rollout

If suggestions are simply not rolled out to your app version or region yet, the web version is the practical workaround — and the proof that the feature exists for your account.

1. Open Copilot on the web and sign in.
2. Check whether suggestions appear there.
3. If they do, the feature is available to your account and the app is behind.
4. Use the web version for suggestion-driven discovery in the meantime.
5. Keep the app updated so suggestions arrive when rolled out.
6. For ongoing issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Missing Copilot suggestions are usually a toggle, a version, or an empty history — not a broken assistant. Enable suggestions, maximise the window, build a little history, and update the app, and the starters usually return. If they appear on the web but not in the app, rollout timing is the honest answer, and the next update is the most likely fix.
