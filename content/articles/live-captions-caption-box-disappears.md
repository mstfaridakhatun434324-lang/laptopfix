---
title: "How to Fix the Live Captions Box Disappearing in Windows 11"
slug: live-captions-caption-box-disappears
date: 2026-10-21
categories: ["ai-pc"]
tags: ["live captions box disappears", "captions window vanishing", "windows 11 live captions", "caption overlay bug", "ai pc troubleshooting", "captions not showing"]
description: "Fix the live captions box disappearing in Windows 11 with six step-by-step methods covering pinning, fullscreen apps, multi-monitor bugs, and drivers."
thumbnail: "/images/thumbs/live-captions-caption-box-disappears.webp"
faqs:
  - q: "Why does my live captions box keep disappearing?"
    a: >
      The caption box is an overlay window that loses its place when a fullscreen app takes exclusive control of the screen, when display scaling changes, or when the captions process loses focus. Pinning the window usually stops it.
  - q: "Do live captions hide when there is no audio?"
    a: >
      The box itself should stay visible even during silence — only the text area goes blank. If the whole window vanishes during quiet moments, that is a bug, not a feature, and the pinning and settings fixes below address it.
  - q: "Why do captions disappear on my second monitor?"
    a: >
      Multi-monitor setups with different scaling percentages confuse the caption window's position memory. It can end up parked off-screen or on the wrong display after sleep, wake, or a cable reconnect.
  - q: "Can a game or video app hide live captions?"
    a: >
      Yes. Apps running in true exclusive fullscreen take over the display output, which hides every overlay including captions. Switching the app to borderless windowed mode keeps captions visible.
---

You have live captions working — words are flowing — and then the caption box just vanishes. No error, no warning. Sometimes it blinks out when you open a game or a fullscreen video; sometimes it disappears after your laptop wakes from sleep; sometimes it is gone the moment you click another window.

The caption box is a special overlay window, and overlays live at the mercy of whatever else wants the screen. Fullscreen apps, display scaling changes, multi-monitor reshuffles, and focus quirks can all knock it off its perch. The fixes below pin it down, starting with the settings that control its visibility.

If captions produce no words at all before vanishing, check the [no audio detected guide](/articles/live-captions-no-audio-detected/) first — a caption box with nothing to transcribe can look like a disappearing act.

## Why this happens

- **Exclusive fullscreen apps:** Games and video players in exclusive fullscreen mode take over the display output entirely, hiding all overlays — including the caption box — until you leave fullscreen.
- **Pinning turned off:** The "always on top" style pin for captions is what keeps the box above other windows. Without it, any new window can cover or push captions aside.
- **Multi-monitor position bug:** With monitors at different scaling levels, the caption window can be placed off-screen or on a disconnected display after sleep, wake, or a cable change.
- **Focus and click-through quirks:** Clicking through or around the box can send it behind the taskbar or collapse it to a sliver, making it look like it disappeared.
- **Display scaling changes:** Docking, undocking, or changing resolution mid-session recalculates overlay positions, and the caption box sometimes lands outside the visible area.
- **Graphics driver glitches:** A buggy GPU driver can fail to composite the overlay layer after wake or during HDR transitions, so the box exists but never renders.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pin the caption box so it stays on top

Pinning is the captions equivalent of "always on top." It is the single most effective setting for a box that vanishes when other windows open, and it takes five seconds to enable.

1. Launch captions with **Win+Ctrl+L** so the box is visible.
2. Click the **pin icon** in the caption box's toolbar to lock it above other windows.
3. Drag the box to a corner where it will not fight your main content — top-center works well for videos.
4. Open the app that used to make it vanish and confirm the box stays put.

### Fix 2: Switch the fullscreen app to borderless windowed

Exclusive fullscreen is the top killer of overlay windows. Borderless windowed looks identical on modern displays but lets Windows keep compositing overlays like captions on top.

1. Open the game or video app's display/video settings.
2. Change the display mode from **Fullscreen** (or Exclusive Fullscreen) to **Borderless Windowed** / **Windowed Fullscreen**.
3. Apply the change and relaunch captions with **Win+Ctrl+L** if needed.
4. Confirm the caption box stays visible while the app fills the screen.

### Fix 3: Hunt down the box on multi-monitor setups

If the box vanished after sleep, docking, or a monitor change, it is probably parked off-screen rather than gone. A quick monitor shuffle usually brings it home.

1. Press **Win+P** and switch to **PC screen only**, then back to **Extend** — this forces Windows to recalculate window positions.
2. Check every monitor, including ones you forgot were connected, for the caption box.
3. If it appears, drag it to your primary monitor and pin it there.
4. To prevent repeats, set all monitors to the same scaling percentage under **Settings > System > Display** if you can tolerate it.

### Fix 4: Reset the caption box position and appearance

Corrupt position or transparency settings can render the box invisible or microscopic. Resetting its appearance returns it to a known-good state.

1. Open **Settings > Accessibility > Live captions** and open **Caption style**.
2. Switch to a different style, then back — this rewrites the box's stored settings.
3. Toggle captions off and on with **Win+Ctrl+L** twice to force a fresh window.
4. If the box reappears tiny or transparent, set opacity back to solid in the style editor.

### Fix 5: Rule out VPN and virtual machine quirks

Caption overlays misbehave inside some remote and virtualized environments. If the box only vanishes inside your work VPN's tunneled apps, check the [Copilot with VPN guide](/articles/copilot-not-working-with-vpn/) — tunneled display pipelines cause similar overlay issues. And if you run captions inside a virtual machine that keeps losing its overlays, the VM's display adapter is the suspect — see the [Hyper-V setup guide for ARM laptops](/articles/hyper-v-setup-arm-laptop/) for getting the virtual display stack healthy.

1. Disconnect the VPN temporarily and test whether the caption box stays visible.
2. If you use a VM, test captions on the host OS as a control case.
3. Update the VPN client or VM guest additions to their latest versions.
4. Reconnect and retest — if the problem follows the tunnel, keep captions on the host side.

### Fix 6: Update the graphics driver

When the overlay layer itself fails to composite — box exists in Task Manager but never renders — the GPU driver is the prime suspect. Grab the latest driver from your GPU maker; NVIDIA users can find theirs at [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx).

1. Download and install the latest graphics driver for your GPU.
2. Choose a **clean installation** if the installer offers it, to clear old overlay hooks.
3. Restart, launch captions, and test across sleep/wake and fullscreen apps.
4. If the box now survives everything, the old driver was failing to composite overlays.

## Closing

A disappearing caption box is a window-management problem, not a transcription problem — the words are fine, the box just loses its place on screen. Pin it, keep fullscreen apps in borderless windowed mode, and watch out for multi-monitor position bugs after sleep. With those three handled, the caption box stays where you put it for the whole session.
