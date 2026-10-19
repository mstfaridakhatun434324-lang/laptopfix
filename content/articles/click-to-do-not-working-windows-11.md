---
title: "Click to Do Not Working on Windows 11? Fix It Now"
slug: click-to-do-not-working-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: [click-to-do, windows-11, copilot-plus-pc, npu, troubleshooting, ai-features]
description: "Click to Do not working on Windows 11? Fix Microsoft's Copilot+ text-action feature with our NPU, settings, gesture, and update troubleshooting guide."
thumbnail: "/images/thumbs/click-to-do-not-working-windows-11.webp"
faqs:
  - q: "What is the keyboard shortcut for Click to Do?"
    a: >
      Press Win + left-click on selected text, or press Win + Q to open Click to Do directly. Both invoke the same AI action menu for text and images.
  - q: "Does Click to Do work on all apps?"
    a: >
      No. It depends on apps exposing their text selection to Windows. It works reliably in Notepad, Edge, and most standard apps, but apps with custom text rendering may not support it.
  - q: "Why does Click to Do need an NPU?"
    a: >
      Its text and image understanding runs on-device through AI models that require a 40+ TOPS neural processor. That is also why it is limited to Copilot+ PCs.
  - q: "Click to Do worked yesterday and stopped today. What happened?"
    a: >
      Most often a Windows update disturbed the NPU driver or left the feature half-registered. Toggle it off and on, update the NPU driver, and install pending Windows updates.
---
Click to Do is one of those features you miss immediately when it breaks: highlight text, hit Win + Click, and get instant actions — summarize, rewrite, search, open. When it stops responding, the gesture does nothing, the menu never appears, or it flashes and vanishes. Your workflow loses a shortcut you had started to depend on.

Like its sibling Recall, Click to Do is a Copilot+ exclusive that leans on the NPU for on-device text and image understanding. That dependency chain — hardware eligibility, NPU driver, Windows build, feature toggle — gives us a clean diagnostic ladder.

This guide runs that ladder from the toggle to the driver. If the feature is entirely absent, see [Click to Do missing](/articles/click-to-do-missing/). If basic captions are also failing, the shared AI stack may be at fault — see [Live Captions not working](/articles/live-captions-not-working-windows-11/). For text-selection-specific issues, our [Click to Do not showing on text select](/articles/click-to-do-not-showing-on-text-select/) guide goes deeper.

## Why this happens

- **Feature toggle is off:** Click to Do has its own setting. Updates and new user profiles can leave it disabled.
- **NPU driver problems:** The on-device models behind Click to Do need a working NPU. Driver issues silently disable the feature.
- **Unsupported hardware:** Click to Do requires a Copilot+ PC. On lesser hardware the gesture simply does nothing.
- **Wrong invocation gesture:** It is Win + Click (or Win + Q), not a plain right-click. Muscle memory from other tools misleads.
- **App incompatibility:** Click to Do hooks into text selection; some apps with custom text rendering do not expose selections to it.
- **Corrupt feature state after update:** Updates can leave the Click to Do component half-registered, so the gesture fires into the void.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the Click to Do toggle
Click to Do has its own master toggle, separate from Recall and from general AI settings, and updates plus new user profiles have a habit of leaving it off. Because the gesture then does absolutely nothing — no error, no feedback — users assume deep breakage when the fix is a single switch. Toggling it off and on also re-registers the feature, which repairs the half-registered states updates leave behind.
1. Open Settings > Privacy & security > Click to Do (or search 'Click to Do' in Settings).
2. Make sure the main toggle is On.
3. Toggle it off and back on to re-register the feature.
4. Test immediately with Win + Click on selected text in Notepad.

### Fix 2: Use the correct gesture in the right app
Before blaming Windows, confirm the gesture itself: hold Win and left-click directly on selected text, or press Win + Q. Plain right-clicks and Ctrl + Click do nothing, and muscle memory from other tools misleads constantly. Testing in Notepad establishes whether the feature works at all — if it does, the problem is app-specific and no system repair will change that.
1. Select some text in Notepad or Edge, then press Win + left-click on the selection.
2. Alternatively press Win + Q to invoke Click to Do directly.
3. If it works in Notepad but not your app, the app's text rendering is the blocker — not Windows.
4. Note which apps fail; the pattern matters for the next steps.

### Fix 3: Check NPU driver health
Click to Do's text and image understanding runs on-device through NPU-backed models, so a sick neural processor kills the feature silently — no error dialog, just a dead gesture. Device Manager shows the truth in seconds, and the OEM driver matched to your exact laptop model is the fix far more often than any Windows setting. This is the hardware layer everything else stands on.
1. Open Device Manager > Neural processors and confirm no warning icons.
2. Update the NPU driver from your laptop maker's support page.
3. Open Task Manager > Performance and confirm the NPU appears and is not erroring.
4. Retry the gesture after the driver update and a restart.

### Fix 4: Repair the feature after an update
Post-update breakage of Click to Do is almost always a registration problem, not a missing feature: the update left components half-registered so the gesture fires into the void. The repair sequence — pending updates, toggle cycle, System File Checker — addresses exactly that damage in order of likelihood. Microsoft documents the known bad builds, so checking the support pages can confirm you are in a known-bad cohort.
1. Install all pending Windows updates — Click to Do fixes ship in cumulative updates.
2. Toggle the feature off, restart, toggle it back on.
3. Run System File Checker (sfc /scannow in an admin terminal) to repair component damage.
4. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for any known issues on your build.

### Fix 5: Confirm hardware eligibility
If nothing software-side revives it, verify the premise: Click to Do requires Copilot+ hardware — 40+ TOPS NPU, 16GB RAM, 256GB storage, 24H2+. On lesser hardware the gesture will never do anything, and no toggle, driver, or hack changes that. It is better to get this answer definitively than to chase a feature your machine was never meant to run.
1. Verify Copilot+ status per our [Copilot+ PC check guide](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).
2. Click to Do needs 40+ TOPS NPU, 16GB RAM, 256GB storage, Windows 11 24H2+.
3. On ineligible hardware, the feature will never activate regardless of settings.
4. Do not chase bypasses — they break with updates and are not worth it.

### Fix 6: Check for conflicting AI utilities
OEM AI hubs, third-party assistants, and clipboard utilities can all register competing text hooks that swallow the Win + Click gesture before Windows sees it. The symptom is maddening — the toggle is on, the NPU is healthy, Notepad works for everyone else — but your machine stays silent. Disabling the overlapping tools one by one exposes the thief quickly.
1. Review installed apps for OEM AI utilities or assistant tools you do not use.
2. Temporarily disable them and retest Win + Click in Notepad.
3. Check Task Manager Startup for helpers that inject into text handling.
4. Keep only the tools you actively use; overlapping AI hooks cause exactly this symptom.

### Fix 7: Repair with an in-place upgrade
When targeted repairs all fail, an in-place upgrade reinstalls Windows while keeping your files and apps, refreshing every system component Click to Do depends on. It is the heavy artillery — an hour of your time — but it resolves the deep component damage that toggle cycles cannot. Afterward the feature behaves like a fresh install, because structurally it is one.
1. Download the Windows 11 installer from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup and choose to keep personal files and apps.
3. Let it complete — this refreshes every system component Click to Do depends on.
4. Re-enable Click to Do afterward and test the gesture.

## Closing

Click to Do failures are usually the toggle, the gesture, or the NPU driver — in that order. Verify the setting, use Win + Click in a cooperative app like Notepad, and keep the NPU driver healthy. If it works in Notepad but nowhere else, you have an app-compatibility answer, not a Windows problem.
