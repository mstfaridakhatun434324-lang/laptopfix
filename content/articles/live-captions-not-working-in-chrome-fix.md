---
title: "How to Fix Live Captions Not Working in Chrome on Windows 11"
slug: live-captions-not-working-in-chrome-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["live captions", "chrome", "windows 11", "accessibility", "audio", "troubleshooting"]
description: "Fix Windows Live Captions not appearing in Chrome with audio, browser, and accessibility checks that restore captions for videos and calls quickly today."
thumbnail: "/images/thumbs/live-captions-not-working-in-chrome-fix.webp"
faqs:
  - q: "Do Windows Live Captions work inside Chrome at all?"
    a: "Yes. Windows Live Captions capture system audio, so they should caption any sound Chrome plays — videos, calls, and streams — as long as the correct output device is selected and captions are enabled."
  - q: "Why do captions work in other apps but not Chrome?"
    a: "Chrome may be routing audio through a different output device, a Bluetooth headset, or an exclusive-mode device that Live Captions is not listening to. Matching the output device usually fixes it."
  - q: "Does Chrome's own caption setting conflict with Windows Live Captions?"
    a: "Chrome has its own Live Caption feature in accessibility settings, and the two can interfere. Use one at a time — preferably Windows Live Captions for system-wide coverage — and turn the other off."
  - q: "Can a muted tab still produce captions?"
    a: "No. If the tab is muted, or Chrome's site sound permission is blocked, there is no audio for Live Captions to transcribe. Unmute the tab and allow sound for the site first."
---

You press play on a video in Chrome, the sound comes through clearly, but the Windows Live Captions bar stays blank — or never appears at all. The same captions work fine in a media player, which makes the Chrome failure feel especially confusing, as if the browser is somehow exempt from the feature.

It is not exempt, but it is a special case. Windows Live Captions listen to system audio, and Chrome routes its audio through the browser's own output path, site permissions, and sometimes a different device entirely. A muted tab, a Bluetooth headset, or Chrome's competing built-in caption setting can each break the chain without any error message.

This guide works through the chain in order: the captions toggle, the audio device, Chrome's own settings, and finally the system components underneath. Test with the same Chrome video after each fix so you know exactly which change brought the captions back.

## Why this happens

- **Live Captions listening to the wrong output device:** Windows captions follow one audio device. If Chrome plays through a headset while captions listen to the speakers, the bar hears silence.
- **Chrome's built-in Live Caption conflicting:** Chrome's own caption engine and Windows Live Captions can fight over the same audio, leaving both blank or flickering.
- **Muted tab or blocked site sound:** A muted tab, a blocked sound permission, or Chrome's "mute site" option produces no audio for the caption engine to transcribe.
- **Live Captions turned off or collapsed:** The caption bar can be minimised, moved off-screen, or disabled by an update, so captions are running but invisible.
- **Audio enhancement or exclusive mode interfering:** Spatial sound, enhancements, or an app taking exclusive control of the audio device can change the stream that Live Captions capture.
- **Outdated Chrome or Windows speech components:** Live Captions depend on Windows speech and language components. A stale Chrome build or a failed component update can break transcription even when audio plays normally.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn Live Captions on and make the bar visible

Start with the obvious, because the caption bar is easy to dismiss or minimise by accident. Confirming it is on, visible, and set to caption system audio saves you from chasing an audio problem that does not exist.

1. Press **Windows + Ctrl + L** to toggle Live Captions on.
2. If the bar appears but is empty, click it and check it is not paused or minimised to the taskbar.
3. Open **Settings > Accessibility > Captions** and make sure **Live captions** is switched on.
4. Play a Chrome video with clear speech and watch the bar for at least ten seconds — transcription takes a moment to start.
5. If captions appear now, pin the bar's position so it is not accidentally dismissed again.

### Fix 2: Match Chrome's output device to the captions device

This is the fix that solves most Chrome caption failures. Windows captions capture one device, and Chrome can silently choose another, especially after you connect or disconnect a headset.

1. Click the speaker icon in the taskbar and note which output device is selected.
2. In Chrome, play your test video, then open the Windows volume mixer and check which device Chrome is actually using.
3. Set both to the same device — for example, your laptop speakers — and disconnect Bluetooth headsets for the test.
4. Restart the video and watch the Live Captions bar.
5. If captions return, reconnect your headset and reselect it in both places; the mismatch, not the headset, was the problem. The same device-matching logic applies when [live captions fail in a Zoom meeting](/articles/live-captions-zoom-meeting-not-working-fix/), where the meeting app picks yet another device.

### Fix 3: Unmute the tab and allow sound for the site

No audio means no captions, and Chrome hides mute controls in several places. Check every layer — the tab, the site permission, and Chrome's sound setting — before assuming the caption engine is broken.

1. Right-click the Chrome tab and make sure **Unmute tab** or **Unmute site** is not offered — if it is, click it.
2. Click the lock or tune icon in the address bar, open **Site settings**, and set **Sound** to **Allow**.
3. Open **chrome://settings/content/sound** and confirm sound is allowed by default, not blocked.
4. Turn the video volume up in the player itself; a player muted to zero produces silence even with everything else correct.
5. Replay the video and check the captions bar — a previously muted source is a common silent culprit.

### Fix 4: Turn off Chrome's own Live Caption to stop the conflict

Running two caption engines at once is a recipe for a blank bar. Chrome's built-in feature is useful on its own, but when you want Windows Live Captions, Chrome's version should be off so the system engine owns the audio.

1. Open **chrome://settings/accessibility** in Chrome.
2. Find **Live Caption** and switch it **Off**.
3. Restart Chrome completely — close every window, not just the tab.
4. Turn Windows Live Captions back on with **Windows + Ctrl + L**.
5. Play your test video again; with only one engine running, transcription usually resumes immediately. A similar single-engine rule helps other AI features too, as [Click to Do summarise](/articles/click-to-do-summarize-not-working/) shows when two handlers compete.

### Fix 5: Disable audio enhancements and exclusive mode

Enhancements and exclusive-mode access reshape the audio stream before Live Captions can read it. Disabling them gives the caption engine a clean, standard stream to transcribe.

1. Open **Settings > System > Sound**, select your output device, and open its properties.
2. Turn off **Audio enhancements** and any spatial sound option.
3. Scroll to **Advanced** and uncheck **Allow applications to take exclusive control of this device**.
4. Restart Chrome and replay the video.
5. If captions return, re-enable enhancements one at a time to find the specific offender, rather than leaving them all off permanently.

### Fix 6: Update Chrome, Windows, and the speech components

When every setting is correct but captions still fail, the transcription components themselves may be stale or damaged. Updating Chrome and Windows together, then resetting the caption language, clears most component-level failures.

1. Open **chrome://settings/help** and let Chrome update to the latest version, then relaunch it.
2. Open **Settings > Windows Update** and install all pending updates, including optional driver updates, then restart.
3. Go to **Settings > Accessibility > Captions**, turn Live Captions off and back on, and confirm the caption language matches the video's language.
4. If your language pack is missing, add it under **Settings > Time & language > Language & region** and download the speech components.
5. Test again in Chrome; if captions still fail system-wide, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the latest Live Captions repair steps, and note that a broken local AI install — such as [Automatic1111 on ARM Windows](/articles/automatic1111-arm-windows-install-fix/) — follows the same update-and-repair pattern.

## Closing

Live Captions in Chrome fail most often not because the feature is broken, but because the audio takes a different path than the captions expect. Match the output device, unmute the source, run only one caption engine, and the bar usually starts transcribing again within minutes.
