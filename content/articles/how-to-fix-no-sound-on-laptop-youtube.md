---
title: "No Sound on YouTube? Fix Laptop Audio That Works Everywhere Except YouTube"
slug: how-to-fix-no-sound-on-laptop-youtube
date: 2026-09-22
categories: ["drivers"]
tags: ["no sound youtube", "youtube no audio", "laptop sound not working", "browser audio", "realtek"]
description: "YouTube has no sound but everything else works? Fix browser-specific audio muting, HTML5 player glitches, and driver issues with this targeted troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-youtube.webp"
faqs:
  - q: "Why is there no sound on YouTube but sound works elsewhere?"
    a: "When only YouTube is silent, the problem is almost never the audio driver — it is the browser tab muted, the YouTube player volume at zero, a broken browser audio process, or an extension interfering. Check the tab mute icon first, then the player's volume slider, then restart the browser. System-wide driver fixes are the wrong tool for a single-site problem."
  - q: "Can a browser extension mute YouTube?"
    a: "Yes. Ad blockers, volume boosters, and tab-management extensions can break YouTube's audio pipeline or mute the player silently. Test in a private/incognito window with extensions disabled. If sound returns, re-enable extensions one by one until the culprit appears, then remove or reconfigure it."
  - q: "Why does YouTube lose sound after I plug in headphones?"
    a: "Windows sometimes fails to move the browser's audio stream to the new default device. The browser keeps playing to the old device while everything else switches correctly. Fix it per-app in Settings, System, Sound, Volume mixer — set the browser's output to the headphones explicitly — or restart the browser after plugging in."
  - q: "Does clearing browser cache fix YouTube audio?"
    a: "Occasionally. Corrupted cached player files can break the HTML5 audio path while video keeps playing. Clearing cached images and files for youtube.com, or a hard refresh with Ctrl+F5 on the video page, forces the player to reload cleanly. It is a quick, harmless step worth trying before driver work."
---

This is one of the most misdiagnosed audio problems on laptops: YouTube plays video perfectly but produces zero sound, while Spotify, system sounds, and local files all work fine. The moment you realize the silence is YouTube-only, you can throw out half the usual audio troubleshooting — the speakers, the sound card, and the audio driver are all demonstrably working. What is broken is the path between the YouTube player and Windows audio, which runs through the browser's audio process, the tab's mute state, and per-app volume settings.

The fixes below stay in that lane. We check the embarrassingly simple stuff first (tab mute, player volume), then the browser layer, then Windows' per-app mixer, and only at the end touch drivers — because reinstalling Realtek to fix a muted tab is the classic time-waster here.

## Why this happens

- **Browser tab muted.** The speaker icon on the tab is the single most common cause.
- **YouTube player volume at zero.** The player's own slider is independent of Windows volume.
- **Broken browser audio process.** The browser's audio service crashed while the page kept running.
- **Extension interference.** Ad blockers and audio extensions hijacking the media pipeline.
- **Per-app output device mismatch.** Windows routed the browser to a disconnected device.
- **Corrupted cached player files.** A bad cached HTML5 player breaking the audio path.
- **Outdated or glitched audio driver.** Rare for YouTube-only silence, but possible after updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the tab mute and player volume

Thirty seconds that solve most cases.

1. Look at the YouTube **tab** — a muted-speaker icon means the tab is muted. Right-click the tab → **Unmute tab** (or click the icon).
2. Check the YouTube player's **volume slider** (bottom-left of the video) — drag it up; also press **M** on the video, which toggles the player's own mute.
3. Verify the video itself has audio — try a different video to rule out a silent upload.
4. Press your laptop's hardware **volume keys** and confirm the on-screen display shows the level rising, not a mute icon.
5. Right-click the speaker icon in the taskbar → **Open volume mixer** → confirm the browser's slider is up and not muted.

### Fix 2: Restart the browser's audio path

When the tab isn't muted but stays silent anyway.

1. Close the YouTube tab completely and reopen it in a **new tab** — don't just refresh.
2. If that fails, fully quit the browser (all windows) and relaunch it. Browser audio processes can die silently in the background.
3. Open YouTube in a **private/incognito window** — this disables extensions and uses a clean cache, isolating the cause instantly.
4. Try a **different browser** (Edge if you use Chrome, or vice versa). Sound in the other browser proves your system audio is fine and the problem is browser-specific.
5. Update the browser to the latest version — media pipeline bugs get fixed in browser updates, not Windows updates.

### Fix 3: Disable interfering extensions

Extensions are a top-three cause of YouTube-only silence.

1. Open your browser's extensions page (`chrome://extensions` or `edge://extensions`).
2. Disable **all** extensions, restart the browser, and test YouTube.
3. If sound returns, re-enable extensions one at a time, testing YouTube after each, until the silence returns — that's your culprit.
4. Prime suspects: ad blockers, volume boosters/normalizers, "enhancer for YouTube" style add-ons, and tab suspenders.
5. Either remove the offending extension or check its settings for an audio/media option to disable.

### Fix 4: Fix Windows' per-app volume routing

Windows can send the browser's audio to the wrong device.

1. Go to **Settings > System > Sound > Volume mixer**.
2. Find your browser in the app list and check two things: its volume slider and its **Output device** dropdown.
3. If the output device points to something disconnected (an unplugged HDMI monitor, old Bluetooth headphones), set it to your actual speakers or headphones.
4. Set the browser's output to **Default** only after confirming the system default is correct under **Settings > System > Sound > Choose where to play sound**.
5. This mismatch commonly appears after plugging/unplugging headphones or docking — Windows moves most apps but leaves the browser behind.

If other apps are also silent, the problem is system-wide rather than YouTube-specific — see [how to fix the Realtek audio driver not working on Windows 11](/articles/realtek-audio-driver-not-working-windows-11/) for the full driver-level repair.

### Fix 5: Clear the browser cache for YouTube

A corrupted cached player can mute audio while video plays on.

1. In the browser, open **Settings > Privacy > Clear browsing data** (or `Ctrl+Shift+Del`).
2. Select **Cached images and files** only — leave passwords and history alone.
3. Alternatively, on the YouTube page itself, press **Ctrl+F5** for a hard refresh that bypasses cache.
4. For a surgical approach: open DevTools (F12) → Application/Storage tab → clear **site data for youtube.com** specifically.
5. Reload the video and test. If a bad cached player file was the cause, audio returns immediately.

### Fix 6: Update or repair the audio driver

The rare case where a driver glitch manifests only in the browser.

1. Open **Device Manager > Sound, video and game controllers**, right-click your audio device (Realtek, Intel Smart Sound, etc.), and choose **Update driver**.
2. If the problem started after a Windows update, use **Roll back driver** instead — updates sometimes ship broken audio drivers.
3. Download the audio driver from your laptop maker's support page (Dell, HP, Lenovo) rather than relying on the generic Windows one.
4. In the driver's properties, check for an **Enhancements** tab and disable all audio enhancements — these process browser audio differently and can mute it.
5. Restart after any driver change and retest YouTube before touching anything else.

The full driver-repair sequence for stubborn audio failures is covered in [how to fix the audio driver keeps crashing after a Windows 11 update](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/).

### Fix 7: Reset the browser and check for system issues

The last-resort tier.

1. Reset the browser to defaults (**Settings > Reset settings**) — this clears bad flags and experimental media settings while keeping bookmarks.
2. Check `chrome://flags` (or `edge://flags`) for any enabled media/audio experiments and reset them to default.
3. Run **Windows Update** and install everything — OS-level media framework fixes ship in cumulative updates.
4. Run the audio troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Audio**.
5. If YouTube is silent across all browsers and the troubleshooter finds nothing, check [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows) for known media playback issues with your build.

## Closing

YouTube-only silence is a browser problem wearing an audio problem's clothes, and the diagnosis takes ten seconds: if any other app makes sound, your speakers and drivers are innocent. Tab mute, the player's own volume, a dead browser audio process, and extension interference cover nearly every case — in that order. Save the driver reinstalls for the day when the silence spreads beyond YouTube; until then, the fix lives in the browser, not in Device Manager.
