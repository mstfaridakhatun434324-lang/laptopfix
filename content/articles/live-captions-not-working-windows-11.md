---
title: "Live Captions Not Working on Windows 11? Fix It Step by Step"
slug: live-captions-not-working-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: [live-captions, windows-11, accessibility, troubleshooting, captions, audio]
description: "Live Captions not working on Windows 11? Fix the silent caption bar with our language pack, audio source, microphone, and service troubleshooting steps."
thumbnail: "/images/thumbs/live-captions-not-working-windows-11.webp"
faqs:
  - q: "What is the shortcut to turn on Live Captions?"
    a: >
      Press Win + Ctrl + L anywhere in Windows 11. You can also toggle it in Settings > Accessibility > Live captions.
  - q: "Do Live Captions need internet?"
    a: >
      No. Captioning runs fully on-device, which is why it works offline and keeps your audio private. Only the initial language pack download needs a connection.
  - q: "Why are my captions empty even though audio plays?"
    a: >
      Usually the speech language pack is missing, the audio is rerouted by third-party software, or the wrong audio source (microphone vs system) is selected.
  - q: "Can Live Captions transcribe my microphone?"
    a: >
      Yes — switch the audio source in the Live Captions settings from system audio to microphone. Useful for in-person conversations near the laptop.
---
You press Win + Ctrl + L and... nothing. Or the caption box appears but stays stubbornly empty while audio plays. Live Captions is one of Windows 11's best accessibility features — on-device, real-time captions for any audio — so when it goes silent, it cuts off people who genuinely depend on it.

Unlike Recall and Click to Do, Live Captions works on far more hardware; the base feature does not need a Copilot+ PC. That broader support means the failure modes are more mundane: missing language packs, muted audio pipelines, and services that did not start.

This guide fixes Live Captions from the most common causes down. If translation specifically fails while base captions work, see [Live Captions translation not working](/articles/live-captions-translation-not-working/). If camera-based AI effects are also failing, the NPU may be the common cause — see [Windows Studio Effects not working](/articles/windows-studio-effects-not-working/). For the battery cost, read [Live Captions draining battery](/articles/live-captions-draining-battery/).

## Why this happens

- **Language pack not downloaded:** Live Captions needs the speech language pack for your language. Without it, the caption engine has nothing to work with.
- **Audio not reaching the caption engine:** Muted system audio, exclusive-mode apps, or broken audio drivers starve Live Captions of input.
- **Live Captions toggle off:** The feature has its own master switch in Accessibility settings, independent of the shortcut.
- **Corrupt caption components:** Failed updates can damage the caption pipeline while the rest of Windows looks fine.
- **Microphone vs system audio confusion:** Live Captions captions system audio by default; expecting it to caption your microphone without switching the source fails.
- **Third-party audio software interference:** Virtual audio cables, enhancers, and some conferencing tools reroute audio away from the caption engine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn it on properly and set the language
Live Captions fails most often at the starting line: the master toggle is off, or the speech language pack was never downloaded. The shortcut does nothing without the toggle, and the caption engine has nothing to work with without the pack. Both live in obvious places once you know to look, and the first-run experience is supposed to handle them — but skipped setups leave them undone.
1. Press Win + Ctrl + L. If a first-run prompt appears, complete it.
2. Go to Settings > Accessibility > Live captions and confirm the toggle is On.
3. In the caption bar's settings gear, check the caption language and download it if offered.
4. Play audio and watch for text — the language pack download can take a few minutes.

### Fix 2: Verify audio is actually flowing
Captions cannot transcribe what never reaches the engine. Muted system audio, a wrong output device, or third-party audio tools rerouting the stream all starve Live Captions of input while everything looks normal. The diagnostic is simple: play clear speech through the default output with enhancers disabled. If captions appear, the engine was fine and the audio path was the problem.
1. Unmute system volume and play something with clear speech, like a video.
2. Right-click the volume icon > Sound settings and confirm the right output device.
3. Temporarily disable audio enhancers or virtual audio devices to rule out rerouting.
4. If captions appear now, re-enable your audio tools one by one to find the conflict.

### Fix 3: Switch the caption source if needed
System audio and microphone are separate inputs, and Live Captions defaults to system audio. Users expecting it to caption their own voice — or a room conversation — get silence because the engine is listening to the wrong source. Switching the source in the caption settings is a five-second fix for a genuinely confusing design choice.
1. Open the Live Captions settings gear.
2. Confirm the audio source: system audio for videos and calls you hear, microphone for speech around you.
3. Test each source with appropriate audio.
4. Most 'not working' cases are simply the wrong source selected.

### Fix 4: Repair the caption pipeline
When settings are correct and audio is flowing but captions stay empty, the caption pipeline components themselves are damaged — usually by a failed update. Toggling the feature off and on re-registers it, System File Checker repairs the underlying files, and pending updates deliver Microsoft's own fixes. This is the standard repair ladder for a healthy-looking but dead feature.
1. Install all pending Windows updates — caption fixes ship regularly.
2. Run sfc /scannow in an elevated terminal to repair system files.
3. Toggle Live Captions off, restart, and toggle it back on to re-register.
4. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues on your build.

### Fix 5: Check for app-specific blocks
Some apps deliberately opt out of audio capture, and DRM-protected content is off-limits by design. When captions work in Edge and Media Player but not in one specific app, you have found a content restriction, not a Windows bug. No troubleshooter overrides it, and recognizing that saves real time.
1. Test captions with a plain video in Edge or Media Player.
2. If they work there but not in your app, the app may block audio capture.
3. For DRM-protected content, captions are often unavailable by design.
4. This is a content restriction, not a Windows bug — nothing to fix.

### Fix 6: Test with a different audio output
Ruling out the output device takes minutes and catches a real category of failures: a broken headphone driver or misbehaving HDMI audio path can starve the caption engine while the system volume looks fine. Testing the same content across outputs isolates the bad device fast, and reinstalling its driver is the fix.
1. Switch output between speakers, headphones, and HDMI in Sound settings.
2. Test captions on each output with the same video.
3. If captions work on one output but not another, the failing device's driver is the issue.
4. Reinstall that device's driver from the laptop maker's support page.

### Fix 7: Reset the caption language pack
A corrupt speech language pack fails silently — no error, just empty captions. Removing and reinstalling the pack is the clean fix, and it is worth doing before deeper surgery whenever captions broke without any settings change. Fresh packs, fully downloaded, behave; damaged ones do not, and there is no repair short of replacement.
1. Go to Settings > Time & language > Language & region.
2. Remove the speech language, restart, and reinstall it.
3. Reopen Live Captions and let the pack finish downloading.
4. Test with clear speech audio to confirm the fresh pack works.

## Closing

Live Captions failures are usually the language pack, the audio path, or the source selection — all quick fixes. Work through them in order and captions come back fast. If captions work in Edge but not in one specific app, you have found an app restriction rather than a Windows problem, and no amount of troubleshooting will override it.
