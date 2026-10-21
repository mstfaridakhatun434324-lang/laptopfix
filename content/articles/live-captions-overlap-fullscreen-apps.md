---
title: "How to Stop Live Captions Overlapping Fullscreen Apps in Windows 11"
slug: live-captions-overlap-fullscreen-apps
date: 2026-10-21
categories: ["ai-pc"]
tags: ["live captions overlap fullscreen", "captions over games", "caption box on top", "windows 11 overlay", "ai pc troubleshooting", "fullscreen captions"]
description: "Stop live captions overlapping fullscreen apps in Windows 11 with six step-by-step methods covering pinning, exclusive fullscreen, sizing, and drivers."
thumbnail: "/images/thumbs/live-captions-overlap-fullscreen-apps.webp"
faqs:
  - q: "Why do live captions stay on top of my fullscreen game?"
    a: >
      The caption box is pinned as an always-on-top overlay, so it renders above everything including fullscreen apps. Unpinning it or toggling captions off before launching the game removes it from the screen.
  - q: "Can I keep captions visible but smaller during fullscreen video?"
    a: >
      Yes — shrink the box, drag it to a corner, and reduce its opacity in the caption style settings. In borderless windowed mode most apps leave room for a slim caption bar without covering content.
  - q: "Do live captions work in exclusive fullscreen games?"
    a: >
      Not reliably. Exclusive fullscreen hands the display directly to the game, which usually hides captions entirely or causes flickering. Borderless windowed mode is the practical compromise.
  - q: "How do I quickly hide captions when a fullscreen app starts?"
    a: >
      Press Win+Ctrl+L to toggle captions off instantly, and press it again when you are done. It is faster than digging through Settings every time.
---

You launch a game or a fullscreen movie, and there is the caption box — parked right over the subtitles, the HUD, or the action. You want captions for the cutscenes but not covering the gameplay, and right now it is all or nothing.

This is the flip side of the always-on-top overlay: the same pinning that keeps captions visible over your browser keeps them visible over everything else too. The fixes below give you real control — quick toggles, proper fullscreen modes, and sizing tricks — so captions appear when you want them and get out of the way when you do not.

If captions overlap because the box is frozen and will not respond at all, the [immovable caption window fix](/articles/live-captions-window-wont-move/) addresses that separately. And if the microphone pipeline feeding those captions is dead, see the [Copilot+ PC microphone guide](/articles/copilot-plus-pc-microphone-not-working/).

## Why this happens

- **Always-on-top pinning:** The pin feature exists precisely to keep captions above other windows — including fullscreen ones. It does its job too well during games and movies.
- **Exclusive vs borderless fullscreen:** In exclusive fullscreen the app owns the display, while in borderless windowed Windows still composites overlays — so the same caption box behaves differently per mode.
- **Oversized caption box:** A box stretched wide for desktop use covers a huge chunk of a game HUD or movie frame.
- **No auto-hide on idle:** The box stays rendered even during long silent stretches, covering content for no benefit.
- **Z-order bugs after alt-tabbing:** Alt-tabbing in and out of fullscreen apps can leave the caption layer stuck above the app even after unpinning.
- **GPU overlay compositing quirks:** On some AI laptops, driver bugs keep the caption overlay composited above fullscreen surfaces — Acer Swift 16 AI owners seeing system-wide overlay weirdness should check the [Acer Swift 16 AI NPU problems](/articles/acer-swift-16-ai-npu-problems/) guide.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle captions off before fullscreen, on after

The fastest workflow is also the simplest: captions are one hotkey away at all times, so there is no need to let them sit over your game.

1. Before launching the game or fullscreen video, press **Win+Ctrl+L** to toggle captions off.
2. Play in peace with a clean screen.
3. When you want captions back — for a story cutscene or dialogue-heavy section — press **Win+Ctrl+L** again.
4. The box returns to its last position, so park it somewhere sensible beforehand.

### Fix 2: Unpin the box so fullscreen apps cover it

If you want captions available but not forced on top, unpinning lets a fullscreen app naturally cover the box while keeping it alive underneath.

1. Launch captions and click the **pin icon** to unpin the box.
2. Launch your fullscreen app — it should now render over the caption area.
3. Alt-tab out when you need to read back captions, then return to the app.
4. Re-pin only for desktop apps where you want captions glued on top.

### Fix 3: Run the app in borderless windowed mode

Borderless windowed gives you the best of both worlds: the app fills the screen like fullscreen, but Windows keeps compositing the caption overlay properly so you can position it deliberately instead of fighting it.

1. Open the game's or video app's display settings.
2. Switch from **Exclusive Fullscreen** to **Borderless Windowed** (or Windowed Fullscreen).
3. Shrink the caption box and drag it to a low-distraction spot, like bottom-center below the HUD.
4. Confirm the app still fills the screen and the captions sit where you placed them.

### Fix 4: Shrink the box and fade it

A slim, semi-transparent caption bar is far less intrusive than the default box. This is the best option when you want captions during fullscreen video without them dominating the frame.

1. Open **Settings > Accessibility > Live captions > Caption style**.
2. Reduce the text size and set the background opacity lower so the box fades into the video.
3. Drag the box's edges to make it narrow — a single-line strip works for most dialogue.
4. Test with a fullscreen video and adjust until the captions are readable but unobtrusive.

### Fix 5: Fix the stuck overlay layer after alt-tabbing

Sometimes unpinning does not help because the overlay layer got wedged above the fullscreen app during an alt-tab. A quick toggle cycle rebuilds the layer order.

1. With the fullscreen app running and captions wrongly on top, press **Win+Ctrl+L** twice (off, then on).
2. If the box still renders above, alt-tab to the desktop and back to the app once.
3. As a deeper reset, end **LiveCaptions** in Task Manager and relaunch it after the app is already fullscreen.
4. The fresh overlay should now respect the unpinned z-order.

### Fix 6: Update the GPU driver for overlay compositing bugs

When captions render above fullscreen apps even unpinned, in exclusive fullscreen, and after every toggle — that is a compositor bug, not a settings issue. Intel owners can use the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) to get the right graphics package.

1. Install the latest GPU driver for your hardware and choose a clean install if offered.
2. Restart and test the exact scenario that used to break: unpinned captions plus exclusive fullscreen.
3. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for known overlay issues on your build.
4. If the driver update fixes it, the old driver was miscompositing the overlay layer.

## Closing

Overlapping captions are a feature working as designed — always-on-top means always on top. The practical answer is workflow, not warfare: toggle captions with Win+Ctrl+L around fullscreen sessions, unpin the box so apps can cover it, and run games in borderless windowed when you want captions and gameplay at once. Shrink and fade the box for movies, and it stops being an obstruction and goes back to being a tool. (Side note for multitaskers: if Copilot's side pane is also misbehaving in the same corner — for instance [suggested prompts going missing](/articles/copilot-suggested-prompts-missing/) — sort the overlay stack with these same steps before assuming the app itself is broken.)
