---
title: "How to Change Live Captions Font Size on Windows 11"
slug: live-captions-font-size-customization
date: 2026-10-22
categories: ["ai-pc"]
tags: ["live-captions", "font-size", "caption-style", "accessibility", "windows-11", "copilot-plus-pc"]
description: "Live Captions text too small or too big on your Copilot+ laptop? Resize caption fonts with built-in styles or a custom theme, and fix styles that won't apply."
thumbnail: "/images/thumbs/live-captions-font-size-customization.webp"
faqs:
  - q: "Where is the font size setting for Live Captions?"
    a: "Open Settings > Accessibility > Captions > Caption style. The presets change text size among other things, or choose Custom to set the text size slider yourself. The Live Captions window follows whichever caption style is active."
  - q: "Why doesn't my new caption font size apply?"
    a: "The caption window sometimes caches the old style. Close and reopen Live Captions after changing the style; if it still ignores the change, reset the caption style to a default and re-customize, as covered in the fixes below."
  - q: "Can I make captions bigger without enlarging everything on screen?"
    a: "Yes — caption styles are independent of display scaling. Changing the caption text size affects only captions, while display scaling (Settings > System > Display) affects the whole screen."
  - q: "Do custom caption styles work in all apps?"
    a: "They work in the Live Captions window and in most apps that use the system caption renderer. Some video players use their own subtitle engines, which follow the player's settings instead — see our [caption overlap fix](/articles/live-captions-overlap-fullscreen-apps/) for player-specific quirks."
---

Squinting at tiny caption text — or being shouted at by giant letters — ruins the whole point of Live Captions. Windows 11 has a proper caption style system with a text-size control, but it lives under Accessibility rather than in the caption window itself, so many people never find it.

Even when you find it, the setting sometimes refuses to apply: the window keeps the old size, a custom style silently reverts, or oversized text collides with fullscreen video. If captions are fighting your fullscreen apps, our [overlap fix](/articles/live-captions-overlap-fullscreen-apps/) handles the positioning side; this guide is about the text itself.

Below is how to resize caption fonts properly, build a custom style that sticks, and repair the cases where Windows ignores your choice.

## Why this happens

- **Setting lives elsewhere:** Font size is under Accessibility > Captions, not in the Live Captions window.
- **Style cache not refreshing:** The caption window can keep rendering the old style until restarted.
- **Preset styles too coarse:** The built-in presets jump between sizes with no middle ground.
- **Custom style corruption:** A damaged custom theme reverts to defaults or stops applying.
- **Per-app subtitle engines:** Some players ignore system caption styles entirely.
- **Display scaling confusion:** Users change global scaling when only captions need resizing.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Resize captions with the built-in caption styles

Start with the presets — for many people one of them is exactly right, and it takes thirty seconds.

1. Open Settings > Accessibility > Captions.
2. In the Caption style dropdown, try each preset (Default, White on black, Small caps, Large text, Yellow on blue) and watch the preview.
3. Open the Live Captions window and play audio to see the style live.
4. Pick the preset whose text size feels comfortable at your normal viewing distance.
5. Leave it — presets apply system-wide to the system caption renderer with no extra steps.

### Fix 2: Create a custom caption style with your exact size

When no preset fits, build your own. The custom editor gives you a proper text-size slider plus color and background control.

1. In Settings > Accessibility > Captions, choose Custom under Caption style.
2. Click Edit (or Create) to open the custom style editor.
3. Drag the Text size slider until the preview text looks right — check it against your actual viewing distance, not just the preview box.
4. Set text color, background opacity, and font to taste; high contrast (light text, dark background) reads best.
5. Save, then close and reopen the Live Captions window so it picks up the new style.

### Fix 3: Force a stuck style to apply

The classic complaint: you changed the size, but the caption window did not. This is a refresh problem, not a settings problem.

1. Close the Live Captions window completely after changing the style.
2. Reopen it and test — most of the time the new size appears now.
3. If not, switch the caption style to a different preset, close captions, then switch back to your custom style.
4. Still stuck? Delete the custom style and recreate it from scratch (corruption is common after Windows updates).
5. As a final reset, toggle Live Captions off and on in Settings > Accessibility > Captions.

### Fix 4: Balance large text with window positioning

Bigger fonts mean a taller caption box, which can cover video controls or subtitles from the player itself. Size and position are one problem.

1. After enlarging text, drag the caption window to a clear area (top of the screen works well for bottom control bars).
2. In the caption window's settings, try the "caption box" display options to reduce padding around large text.
3. If captions overlap the player's own subtitles, turn the player's subtitles off and rely on Live Captions.
4. For fullscreen video, consider docking captions at the very top edge where controls never appear.
5. Pen or touchscreen users who struggle to drag the box: a glitchy pen driver fights window moves, so check our [Wacom driver fix for Arm Windows](/articles/wacom-tablet-driver-arm-windows/) if drags misbehave.

### Fix 5: Fix styles that revert after reboot

A custom style that resets itself on every restart points to a permissions or sync problem with the settings store.

1. Confirm you are signed in with the same user account that created the style (styles are per-user).
2. Turn off Settings sync for accessibility options if you use a Microsoft account across PCs — a second PC can overwrite your style.
3. Recreate the custom style once more and restart immediately to test persistence.
4. Run a Windows Update check — Microsoft has fixed caption-style persistence bugs in cumulative updates ([support hub](https://support.microsoft.com/en-us/windows) for troubleshooting guides).
5. If it still reverts, use a preset instead; presets are stored more robustly than custom themes.

### Fix 6: Rule out rendering stalls that mimic style problems

Sometimes the text size is fine but captions update sluggishly, making the style feel broken. On Copilot+ PCs this can be the NPU stalling rather than a font issue.

1. Watch whether captions lag or freeze along with the size complaint — lag points to the pipeline, not the style.
2. Restart Live Captions; if rendering smooths out temporarily, the NPU path was stalling.
3. Check Task Manager to see whether caption processing fell back to the CPU.
4. For persistent pipeline stalls, our [NPU power state fix](/articles/npu-power-state-stuck-fix/) covers the driver-level repair.
5. Retest your font size after the pipeline is healthy — style changes are much easier to judge on smooth captions.

## Closing

Caption font size is a thirty-second fix when you know where it lives — Settings > Accessibility > Captions, with a custom style for the in-between sizes the presets skip. The real work is in the edge cases: styles that need a caption restart to apply, custom themes that revert, and big text that needs repositioning. Get the size right for your eyes and your viewing distance, make sure the style survives a reboot, and Live Captions becomes genuinely comfortable to read for hours.
