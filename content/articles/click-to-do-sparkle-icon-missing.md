---
title: "How to Fix the Click to Do Sparkle Icon Missing on Windows 11"
slug: click-to-do-sparkle-icon-missing
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do sparkle icon", "sparkle icon missing", "windows click to do", "click to do indicator", "copilot plus pc", "windows 11"]
description: "The Click to Do sparkle icon not appearing on selected text? Restore the missing sparkle indicator on your Copilot+ PC with these fixes. Six fixes inside."
thumbnail: "/images/thumbs/click-to-do-sparkle-icon-missing.webp"
faqs:
  - q: "What does the Click to Do sparkle icon look like?"
    a: >
      It is a small sparkle/stars icon that appears near selected text or images on Copilot+ PCs, signaling that AI text actions are available. Clicking it (or using the keyboard trigger) opens the action menu.
  - q: "Can I use Click to Do without the sparkle icon?"
    a: >
      Yes. The keyboard triggers — Windows key + click on a selection, or Win + Q — open the same menu regardless of whether the sparkle appears. The icon is a convenience, not a requirement.
  - q: "Does the sparkle appear in every app?"
    a: >
      It appears where Windows can detect selectable text or images. Some apps with custom rendering do not trigger it even when the keyboard shortcut still works — app support varies.
  - q: "Will the sparkle ever come to non-Copilot+ PCs?"
    a: >
      Click to Do's on-device AI actions require a Copilot+ PC's NPU. Microsoft has not announced plans to bring the full experience, sparkle included, to PCs without one.
---

On a healthy Copilot+ PC, selecting text or an image summons a small sparkle icon — Click to Do's visual invitation. When that icon never appears, the feature might as well not exist, even if the underlying engine is fine.

The sparkle is just an indicator; its absence means the detection layer that watches your selections is not firing, not necessarily that the AI actions are broken. Distinguishing 'icon missing' from 'feature broken' focuses the fix enormously — the same indicator-versus-engine split behind [exporting Copilot app chats](/articles/copilot-app-chat-export/), where the data exists but the UI affordance vanished.

Six fixes below: verifying the feature is on, checking the visual prerequisites, repairing the detection layer, and confirming with the keyboard trigger. Test by selecting text in Notepad after each step.

## Why this happens

- **Click to Do disabled entirely:** If the feature is off, there is no sparkle — the icon's absence is correct behavior. Always check the master toggle first.
- **Feature present but indicator suppressed:** Some builds and configurations run the engine without the floating icon, requiring the keyboard trigger instead.
- **Hardware not meeting Copilot+ requirements:** The sparkle only appears on PCs with the required NPU and build. Non-Copilot+ hardware never shows it — [AMD XDNA2 NPU driver issues](/articles/amd-xdna2-npu-driver-issues/)-class NPU detection failures produce the same symptom from underneath.
- **Display scaling or overlay conflicts:** Third-party overlay tools, custom cursors, and unusual DPI scaling can hide or misposition the floating icon.
- **Corrupt feature state:** A damaged Click to Do configuration can kill the indicator while leaving the engine responsive to keyboard triggers.
- **Policy hiding the indicator:** Managed devices may allow the feature but suppress its UI affordances.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Click to Do is enabled

The icon cannot appear for a disabled feature. Check the master switch first.

1. Open **Settings > Privacy & security > Click to Do** and confirm the feature is turned on.
2. Check for any 'managed by your organization' notice that might restrict it.
3. If the whole feature is absent from Settings, [Click to Do missing entirely](/articles/click-to-do-missing/) is your guide — the icon is the least of it.
4. If enabled, continue: the engine is on but the indicator is not firing.

### Fix 2: Test whether the engine works without the icon

Determine whether you have an indicator problem or a feature problem — the fixes diverge completely.

1. Select text in Notepad and press **Win + Q** (or **Windows key + click**).
2. If the Click to Do menu appears, the engine is healthy and only the sparkle indicator is missing — continue below.
3. If nothing appears, the feature itself is broken; treat it as a full Click to Do failure instead.
4. This test takes ten seconds and prevents fixing the wrong layer.

### Fix 3: Check NPU and hardware prerequisites

The sparkle is a Copilot+ exclusive. Confirm the hardware qualifies and is detected.

1. Open **Task Manager > Performance** and verify the NPU tab exists.
2. Check **Device Manager > Neural processors** for a healthy device with no warnings.
3. Confirm you are on a current Windows 11 build via **Settings > System > About**.
4. If the NPU is undetected, fix that first — no NPU, no sparkle, no debate.

### Fix 4: Disable overlay and customization tools temporarily

Third-party UI tools are notorious for swallowing floating indicators.

1. Temporarily disable screen-annotation tools, custom cursor software, and overlay utilities.
2. If you use multiple monitors with different DPI scaling, test on the primary display at 100% scaling.
3. Restart Windows Explorer from Task Manager to refresh the shell overlay layer.
4. Retest text selection in Notepad after each change to identify the culprit.

### Fix 5: Reset the Click to Do configuration

A corrupt feature state can suppress the indicator while the engine answers keyboard triggers.

1. Toggle Click to Do off and on in Settings.
2. Restart the PC — the indicator service initializes at startup.
3. Select text in Notepad and watch for the sparkle near the selection.
4. If it appears, the reset fixed it; if not, continue to the repair step.

### Fix 6: Repair Windows components

Persistent indicator failure with a working engine points to damaged shell or AI components.

1. Install all pending Windows updates — the indicator ships with the OS.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` elevated.
3. Create a new local user account and test there to rule out profile-level corruption.
4. If the icon works in the new profile, migrate to it rather than fighting the old one's corruption.

## Closing

A missing sparkle icon is an indicator problem until proven otherwise — and the ten-second keyboard test proves it either way. Confirm the feature is enabled, verify the NPU, clear overlay interference, reset the configuration, and repair Windows if needed. Even in the worst case, the keyboard trigger keeps every AI action within reach while you sort the icon. Persistent indicator failures are covered in depth at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
