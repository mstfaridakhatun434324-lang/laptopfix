---
title: "Click to Do Gesture Not Working? Fix Win + Click on Your Copilot+ PC"
slug: click-to-do-gesture-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, gesture-fix, copilot-plus-pc, windows-11, troubleshooting, keyboard-shortcut]
description: "Click to Do gesture not working on your Copilot+ PC? Fix the Win + Click shortcut, settings, and driver issues with this complete step-by-step guide today."
thumbnail: "/images/thumbs/click-to-do-gesture-not-working.webp"
faqs:
  - q: "What is the correct Click to Do gesture?"
    a: >
      Hold the Windows key and left-click on selected text, or press Win + Q. A plain right-click, a plain left-click, and Ctrl + Click do not invoke Click to Do, and using them is the single most common cause of a gesture that seems broken.
  - q: "Why does Win + Q work but Win + Click does not?"
    a: >
      Win + Q bypasses the mouse click entirely, so a split result points at the mouse, the click target, or an app intercepting clicks. If Win + Q works, Click to Do itself is healthy and the fault lies in how clicks are delivered or intercepted.
  - q: "Can another app steal the Win + Click shortcut?"
    a: >
      Yes. Screen-capture tools, clipboard managers, mouse utilities, and some security software intercept the Windows key or mouse clicks before Click to Do sees them. Closing such tools one at a time is the quickest way to find the culprit.
  - q: "Does Click to Do gesture work on a touchscreen?"
    a: >
      Touch input is less reliable for this gesture, because it depends on a precise key-plus-click combination. A physical keyboard and mouse, or the Win + Q shortcut, give a far more dependable test than tapping on a touchscreen.
---

You press Win, you click on selected text, and absolutely nothing happens. No menu, no flash, no error — just the same highlighted text staring back at you. The gesture that is supposed to be the front door to Click to Do feels completely dead.

That silence is the key diagnostic clue, because a dead gesture has a short list of causes: the wrong combination, a disabled feature, another program intercepting the shortcut, a mouse or keyboard problem, or an NPU driver fault that leaves the feature unable to respond. Each cause is easy to test once you separate the key from the click and the feature from the hardware.

This guide does exactly that separation, starting with the combination itself and ending with the driver. If the laptop is also running hot or locking oddly while you test, check [AI laptop overheating fix](/articles/ai-laptop-overheating-fix/) and [Dynamic Lock not working on AI PCs](/articles/dynamic-lock-not-working-ai/) for those separate symptoms.

## Why this happens

- **Wrong combination is used:** Click to Do needs Win + Click or Win + Q. Plain right-clicks, plain left-clicks, and Ctrl + Click all do nothing, and muscle memory from other tools constantly substitutes them.
- **Feature toggle is off:** With the master toggle disabled, the gesture is ignored entirely. There is no error, because Windows is not listening for the combination at all.
- **Another app intercepts the shortcut:** Capture tools, clipboard managers, mouse utilities, and security software can swallow the Windows key or the click before Click to Do receives it.
- **Mouse or keyboard fault:** A failing mouse button or sticky Windows key can break the combination.
- **Click lands on unselectable content:** Clicking on an image, a blank area, or text an app does not expose to Windows gives Click to Do nothing to act on, so it stays hidden.
- **NPU driver or feature state is broken:** If the on-device models cannot run, or the feature is half-registered after an update, the gesture fires into a feature that cannot answer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the exact gesture in Notepad

The first test must remove every variable except the gesture itself, and Notepad is the cleanest place to do it. It uses standard text selection, no custom rendering, and no app-level shortcut interception, so a success there proves the gesture, the keyboard, and the mouse all work.

1. Open Notepad and type a sentence, then select the whole sentence with the mouse.
2. Hold down the Windows key firmly, then left-click directly on the selected text.
3. Release both and check whether the Click to Do menu appears.
4. If nothing appears, press Win + Q while the text is still selected.
5. Note which combination, if either, worked, since that split guides the next steps.

### Fix 2: Verify the Click to Do toggle and restart the feature

A disabled toggle is the quietest cause of a dead gesture, because Windows simply stops listening for the combination and offers no feedback whatsoever. Toggling it off and on also re-registers the feature.

1. Open Settings, then Privacy and security, and select Click to Do.
2. Confirm the main toggle is switched on.
3. Switch it off, wait about ten seconds, then switch it back on.
4. Return to Notepad, reselect a sentence, and test Win + Click again.
5. If the gesture now works, test your original app to confirm the repair held.

### Fix 3: Close apps that intercept the Windows key or clicks

Shortcut-stealing software is the most overlooked cause. Screen-capture utilities, clipboard managers, mouse gesture tools, and some security programs all hook the same key and click events Click to Do needs.

1. Close screen-capture, clipboard, and mouse-utility apps running in the system tray.
2. Test Win + Click in Notepad after closing each one, not just at the end.
3. If the gesture returns after closing a particular app, that app was intercepting it.
4. Check that app's settings for a shortcut or overlay option you can disable.
5. Keep the interfering app closed or reconfigured while you use Click to Do.

### Fix 4: Test the keyboard and mouse separately

Hardware faults hide well behind a gesture failure, because a Windows key that works for opening Start can still fail in combination, and a mouse button that clicks normally can still misfire under a held key. Separating the two inputs — testing the key with Win + Q, and the click with a different mouse or a wired connection — isolates the faulty half quickly.

1. Test Win + Q with the text still selected, since it needs the key but not the click.
2. If Win + Q works but Win + Click does not, suspect the mouse or the click path.
3. Try a different mouse, or switch a wireless mouse to a wired connection, and retest.
4. Try the on-screen keyboard's Windows key combined with a mouse click.
5. Replace batteries or reseat the wireless receiver if the mouse behaves inconsistently.

### Fix 5: Check the NPU driver and Windows build

When the gesture, the toggle, the intercepting apps, and the hardware all check out, the feature itself may be unable to answer because its on-device models have no working neural processor to run on. A faulty NPU driver produces no error dialog — the gesture simply does nothing. Device Manager shows the driver state in seconds, and the correct driver comes from your laptop maker's support page.

1. Open Device Manager and expand Neural processors to check for warning icons.
2. Update the NPU driver from your laptop maker's support site, or see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
3. Open Settings, then Windows Update, and install every pending update.
4. Restart the laptop after any driver or system update to activate the changes.
5. Retest Win + Click in Notepad with a freshly selected sentence.

### Fix 6: Retest in a clean state and adjust the shortcut

If the gesture works in Notepad but fails in one app, or works only intermittently, the remaining explanation is usually app-specific interception or an unreliable click target, and a clean retest proves it. Testing with a fresh boot, no tray utilities, and a large, clear selection removes the background noise that makes intermittent faults so hard to chase.

1. Restart the laptop and do not open any capture or clipboard utilities.
2. Open Notepad, select a clear sentence, and test Win + Click immediately.
3. If it works now, reopen your usual apps one at a time to find the interferer.
4. Test in your original app with a large, clearly selected block of text.
5. If Win + Click remains awkward, use Win + Q as your primary shortcut.
6. To make that shortcut your own, [customise the Click to Do keyboard shortcut](/articles/customize-click-to-do-keyboard-shortcut/) for a combination that fits your keyboard, and note the contrasting [Fortnite not launching on ARM laptops](/articles/fortnite-arm-laptop-not-launching/) app-launch fault.

## Closing

A dead gesture almost always has a nameable cause — the wrong combination, a disabled toggle, an intercepting app, a tired mouse, or a sick driver — and the Notepad test plus the Win + Q split will name it for you. Once Win + Click answers reliably in Notepad, carry it back to your daily apps one at a time, and the one that breaks it will reveal itself instead of hiding behind a silent screen.
