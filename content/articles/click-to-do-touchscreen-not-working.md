---
title: "How to Fix Click to Do Not Working on Touchscreens in Windows 11"
slug: click-to-do-touchscreen-not-working
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do touchscreen", "click to do touch", "windows click to do", "touchscreen ai actions", "copilot plus pc", "windows 11"]
description: "Click to Do ignoring your touchscreen taps? Get AI text actions working with touch on your Copilot+ PC using these practical fixes. Full guide inside."
thumbnail: "/images/thumbs/click-to-do-touchscreen-not-working.webp"
faqs:
  - q: "Is there a touch-only way to open Click to Do?"
    a: >
      Yes — press and hold on selected text on supported builds, or open the touch keyboard and use its Windows key before tapping the selection. Both avoid needing a physical keyboard or mouse.
  - q: "Does Click to Do work with a pen?"
    a: >
      Pen selection followed by the press-and-hold or barrel-button gesture can trigger it on builds where pen input is fully integrated. Behavior varies by device and build — test on yours.
  - q: "Why does touch selection work but Click to Do never appears?"
    a: >
      The app is likely handling touch selection with custom code that does not notify Windows' text pipeline. Try the same gesture in Edge or Notepad; if it works there, the app is the limitation.
  - q: "Can I use Click to Do in tablet mode without a keyboard?"
    a: >
      Yes, via press-and-hold on the selection. The touch keyboard's Windows key is the fallback when press-and-hold is unreliable on your device.
---

Click to Do was designed mouse-first: select text, hold Windows key, click. On a touchscreen Copilot+ PC — a Surface Pro, a 2-in-1 in tablet mode — there is no Windows key + click, and the touch invocation is far less discoverable.

Touch support exists but depends on press-and-hold gestures and the touch keyboard's Windows key, both of which users rarely discover and which break when touch drivers or tablet-mode behaviors misbehave. It is the same discoverability gap as [Copilot app stuck in dark mode](/articles/copilot-app-dark-mode-stuck/), where the feature works but the path to it is hidden.

This guide covers six fixes: the correct touch gestures, touch driver health, tablet-mode settings, and workarounds. Test each gesture on selected text in Edge after every step.

## Why this happens

- **Unknown touch gesture:** Most users never learn the touch invocation — press-and-hold on a selection, or the touch keyboard's Windows key — and conclude touch is unsupported.
- **Touch driver issues:** A degraded touchscreen driver can drop the long-press events Click to Do relies on, while taps and swipes keep working normally.
- **Tablet posture behaviors interfering:** Detaching the keyboard or folding into tablet mode changes input routing; some builds handle the transition poorly for system gestures.
- **Palm rejection eating the gesture:** Aggressive palm rejection on 2-in-1s can cancel the press-and-hold before Click to Do recognizes it.
- **App not exposing touch selections:** Some apps handle touch selection through custom code that never notifies Windows' text pipeline — the [Click to Do not showing on text selection](/articles/click-to-do-not-showing-on-text-select/) problem in touch form.
- **NPU-gated feature unavailable:** On devices where the NPU is unhealthy, the whole feature — touch and mouse alike — stays dark; [NPU shared memory allocation](/articles/npu-shared-memory-allocation-fix/)-style resource faults can gate it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Learn the correct touch invocation

Touch has its own path to Click to Do. Learn it before diagnosing.

1. Select text with touch: tap-and-drag the selection handles in Edge or Notepad.
2. Press and hold on the selected text — on supported builds this summons the Click to Do menu.
3. Alternative: open the touch keyboard, tap its **Windows key**, then tap the selection.
4. If either gesture works, touch support is fine — practice the gesture rather than troubleshooting further.

### Fix 2: Verify the touchscreen driver is healthy

Dropped long-press events are a driver symptom. Check the driver before blaming Windows.

1. Open **Device Manager > Human Interface Devices** and look for warning icons on touch entries.
2. Right-click the touchscreen device and check for driver updates.
3. If touch was recently problematic, roll the driver back or reinstall it from the laptop maker's support page.
4. Test the press-and-hold gesture again after any driver change.

### Fix 3: Test in different postures

Isolate whether the failure is touch-wide or posture-specific.

1. Test with the keyboard attached (laptop mode) using touch on the screen.
2. Detach or fold into tablet mode and test again.
3. If it works in one posture but not the other, the posture-transition handling is the bug — report it via Feedback Hub.
4. Note your findings; posture-specific bugs are prime candidates for Windows Update fixes.

### Fix 4: Adjust touch and pen settings

Overzealous touch filtering can eat the exact gesture Click to Do needs.

1. Go to **Settings > Bluetooth & devices > Touch** and review touchpad/touchscreen options.
2. If using a pen, check **Pen & Windows Ink** settings for press-and-hold configuration.
3. Temporarily disable palm-rejection-adjacent features to test whether the gesture gets through.
4. Re-enable protections afterward — the goal is diagnosis, not permanently weakening touch filtering.

### Fix 5: Confirm the feature works with mouse/keyboard

Establish whether touch specifically is broken or the whole feature is down.

1. Attach a mouse or use the touchpad: select text and use **Windows key + click**.
2. If the menu appears with mouse but never with touch, the issue is touch-input-specific — continue with driver and build updates.
3. If it fails with mouse too, stop touch troubleshooting and fix Click to Do generally.
4. The [Click to Do not showing on text selection](/articles/click-to-do-not-showing-on-text-select/) guide is the right next step for a general failure.

### Fix 6: Update Windows and the touch firmware

Touch gesture handling improves with both OS and firmware updates.

1. Install all pending Windows updates — input-stack fixes ship regularly.
2. Check the laptop maker's support page for touchscreen firmware updates (Surface, Lenovo, HP, and Dell all ship these).
3. After updating, recalibrate touch via **Control Panel > Tablet PC Settings** if offered.
4. Retest all three touch invocations: press-and-hold, touch-keyboard Win key, and pen long-press.

## Closing

Click to Do on touchscreens fails from obscurity more than breakage: the gestures exist but nobody discovers them, and touch drivers occasionally drop the long-press events they need. Learn press-and-hold, verify the touch driver, test across postures, and update both Windows and touch firmware. The AI actions are just as available to your fingertip as to your mouse — once the gesture lands. For touch-driver level problems, your laptop maker's support page plus [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) are the right resources.
