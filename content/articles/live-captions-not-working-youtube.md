---
title: "How to Fix Live Captions Not Working on YouTube in Windows 11"
slug: live-captions-not-working-youtube
date: 2026-10-21
categories: ["ai-pc"]
tags: ["live captions youtube", "captions not working youtube", "browser captions windows 11", "youtube cc vs live captions", "ai pc troubleshooting", "chrome captions"]
description: "Fix live captions not working on YouTube with six step-by-step methods covering browser audio routing, tab muting, hardware acceleration, and permissions."
thumbnail: "/images/thumbs/live-captions-not-working-youtube.webp"
faqs:
  - q: "Should I use YouTube captions or Windows live captions?"
    a: >
      Use one or the other, not both. YouTube's own captions are more accurate for YouTube videos; Windows live captions shine for videos without any captions at all. Running both at once just stacks two text boxes.
  - q: "Why do Windows live captions ignore my YouTube video?"
    a: >
      Usually the browser tab is muted, the video plays through a different audio device than captions are listening to, or the browser blocked microphone access that captions rely on for routing.
  - q: "Do live captions work on YouTube in every browser?"
    a: >
      They should work in any Chromium-based browser and Firefox, since captions read the system audio output rather than the browser itself. If one browser fails, testing another quickly isolates a browser-specific problem.
  - q: "Can ad blockers break live captions on YouTube?"
    a: >
      Ad blockers do not break captions directly, but aggressive extensions can mute or reroute audio elements. If captions fail only with extensions enabled, test in an incognito window with extensions off.
---

You open a YouTube video with no subtitles, press **Win+Ctrl+L**, and… nothing. The caption box sits empty while the video plays, or it transcribes everything except the video. Meanwhile captions work fine in your meeting app, which makes the whole thing feel personal.

The confusion usually starts with there being two caption systems fighting over the same video: YouTube's built-in captions and Windows live captions. Add browser audio routing — muted tabs, per-site permissions, hardware acceleration grabbing the audio pipeline — and it is easy for the video's sound to take a path captions never see.

These six fixes untangle the two systems and make sure the video's audio reaches captions. If captions appear but lag seconds behind the video, the [caption delay fix](/articles/live-captions-delay-fix/) is the right follow-up.

## Why this happens

- **Muted or low-volume tab:** A muted browser tab produces no audio stream, so captions have nothing to transcribe — the video looks like it is playing normally.
- **Wrong audio device in the browser:** The browser can route audio to a different output than the system default, so captions listening to the default device hear silence.
- **YouTube captions vs Windows captions confusion:** With YouTube's own captions on, people assume Windows captions are broken when really the Windows box is empty and YouTube's box is doing the work — or vice versa.
- **Browser microphone permission denied:** Captions' audio routing depends on browser media permissions. A denied prompt blocks the stream captions need.
- **Hardware acceleration capturing audio:** The browser's hardware-accelerated media pipeline can bypass the software audio path that captions monitor.
- **Outdated or corrupt browser profile:** A damaged browser installation or profile can break media playback just enough that the audio stream never reaches the system mixer properly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decide which caption system you want and unmute the tab

Half of all "YouTube captions broken" reports are a muted tab or two caption systems cancelling each other out visually. Sort the basics first before touching anything deeper.

1. Right-click the YouTube tab and make sure **Unmute tab** is not showing (if it is, click it).
2. Turn the video volume up and confirm you can actually hear the audio.
3. Turn YouTube's own **CC button off** so only the Windows caption box is active — this removes all ambiguity about which system is working.
4. Press **Win+Ctrl+L** and watch the Windows box for 10 seconds of clear speech.

### Fix 2: Check the volume mixer routing for your browser

Windows lets each app use its own output device. If your browser is sending YouTube audio to a headset while captions listen to the speakers, the box stays empty.

1. Right-click the speaker icon and open **Volume mixer**.
2. Find your browser in the app list and confirm its output device matches your actual speakers or headset.
3. Make sure the browser's volume slider is up and not muted in the mixer.
4. Replay the video and relaunch captions to confirm words appear.

### Fix 3: Re-allow microphone access for the browser

If you ever dismissed a microphone permission prompt in the browser, captions' audio path can stay blocked. The [microphone permission denied guide](/articles/copilot-microphone-permission-denied/) walks through re-triggering blocked prompts if the steps below do not surface one.

1. Click the lock/tune icon in the browser's address bar while on YouTube.
2. Set **Microphone** (and camera, if listed) to **Allow** for the site.
3. Also check **Settings > Privacy & security > Microphone** in Windows and confirm the browser is allowed.
4. Reload the YouTube page, relaunch captions, and test again.

### Fix 4: Toggle hardware acceleration in the browser

Hardware-accelerated video decoding can route audio through a path captions cannot monitor. Toggling it forces the browser back onto the standard software audio pipeline.

1. Open your browser settings and search for **hardware acceleration**.
2. Turn it **off**, then fully quit and restart the browser.
3. Play the YouTube video and launch captions — check whether words now appear.
4. If captions work with it off, leave it off for caption sessions, or update the GPU driver and try turning it back on later.

### Fix 5: Test in a clean browser profile or a different browser

Extensions and corrupt profiles break media pipelines in subtle ways. A clean test separates browser problems from system problems in under two minutes.

1. Open an **incognito/private window** (extensions off by default) and play the same video.
2. If captions work there, disable extensions one by one in your normal profile to find the culprit.
3. If incognito fails too, install or open a second browser (Edge if you use Chrome, or vice versa) and test.
4. Captions working in browser B but not browser A means reinstalling or resetting browser A.

### Fix 6: Update the browser and check for system audio issues

An outdated browser may use deprecated audio APIs that captions cannot hook. And if no browser produces captions while other apps do, the problem may be system audio capture rather than YouTube at all. Note one special case: if the "video" is actually playing inside an Android emulator on your ARM laptop and you hear silence, the emulator itself may be broken — check the [Android emulator on ARM guide](/articles/android-emulator-not-working-arm-laptop/) before chasing caption settings.

1. Update your browser to the latest version and restart it.
2. In **Settings > Windows Update**, install pending updates, then check **optional driver updates** in the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if audio drivers look old.
3. Play a local video file (not in the browser) with captions on as a control test.
4. If local files caption fine but YouTube never does, the issue is isolated to the browser — reset its settings to default.

## Closing

YouTube caption failures are almost never about YouTube itself — they are about the audio path between the browser and Windows. Unmute the tab, confirm the browser's output device in the volume mixer, settle on one caption system, and make sure permissions are allowed. Once the video's audio takes the normal system route, Windows live captions pick it up like any other sound.
