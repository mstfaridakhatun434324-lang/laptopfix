---
title: "Live Captions Says No Audio Detected? How to Fix It"
slug: live-captions-no-audio-detected
date: 2026-10-20
categories: ["ai-pc"]
tags: ["live captions", "no audio detected", "accessibility", "troubleshooting", "ai pc", "windows 11"]
description: "Live Captions showing 'no audio detected' on your Copilot+ PC? Learn why the NPU caption engine misses playing audio and restore live captions step by step."
thumbnail: "/images/thumbs/live-captions-no-audio-detected.webp"
faqs:
  - q: "Why does Live Captions say no audio detected when sound is playing?"
    a: "Live Captions listens to a specific audio endpoint. If Windows is routing sound to a different device than the one captions monitor — a Bluetooth headset versus speakers, for example — the caption engine hears silence. Matching the playback device to the captions' monitored device fixes it instantly."
  - q: "Does Live Captions need the NPU to work?"
    a: "On Copilot+ PCs, Live Captions with translation uses the NPU for on-device speech recognition. Basic English captions can fall back to CPU. If the NPU driver is broken, advanced caption features fail while basic ones limp along — check that your [NPU is detected and used by apps](/articles/npu-not-used-by-apps-windows-11/)."
  - q: "Why do captions work for videos but not for my microphone?"
    a: "System-audio captions and microphone captions are separate paths. Video captions tap the playback stream; mic captions need microphone permission and the correct input device. Grant the mic permission and select the right input to fix the mic side."
  - q: "Do I need to download anything for Live Captions?"
    a: "Yes, the first launch downloads a speech recognition language pack (a few hundred megabytes). Without it, captions cannot start. If the download stalls, see our guide on the language pack download failing — and once captions run, a related fix covers [caption delay problems](/articles/live-captions-delay-fix/)."
---

Live Captions is one of the best Copilot+ PC features — real-time, on-device captions for any audio — until it greets you with "no audio detected" while sound is clearly playing. The message is misleading: Windows can hear the audio fine. The caption engine is just listening to the wrong place, or it never got the language model it needs to start working.

On AI PCs the caption pipeline runs through the NPU, which adds a driver layer that can silently break. This guide covers both sides: the audio routing mismatches that cause most "no audio detected" errors, and the NPU and language-pack issues behind the rest.

Work through the fixes in order, testing with the same YouTube video each time so results are comparable. The moment captions appear, you will know exactly which layer was at fault — and you will know how to fix it next time.

## Why this happens

- **Wrong audio endpoint monitored:** Captions listen to one playback device; your audio plays through another.
- **Language pack missing:** The speech model never downloaded, so the engine cannot process anything it hears.
- **NPU pipeline stalled:** On-device recognition needs the NPU; a driver failure kills advanced captions. Our guide on the [NPU not being used by apps](/articles/npu-not-used-by-apps-windows-11/) covers the reset.
- **Microphone permission denied:** Mic-based captions need mic access, which is a separate toggle from system audio.
- **Audio enhancements interfere:** Third-party audio effects can alter the stream the caption engine expects.
- **Captions monitoring the wrong input:** The captions panel can be set to microphone mode when you want system audio, or vice versa.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Match the playback device to what captions monitor

This fixes the majority of "no audio detected" cases. Captions monitor one audio endpoint; if your sound plays elsewhere, the engine hears silence.

1. Play audio (a YouTube video works well) and open Settings > System > Sound.
2. Note which device is the output — speakers, headphones, or Bluetooth.
3. In the Live Captions panel, open settings and check whether it monitors system audio for the current device.
4. Switch Windows output to the built-in speakers temporarily — if captions start working, you found a routing mismatch.

### Fix 2: Install the speech language pack

No language pack means no recognition engine. The captions panel prompts for the download, but it sometimes needs a nudge.

1. Open the Live Captions panel and click the download prompt for your language.
2. Keep the laptop awake and connected until the download completes (a few hundred MB).
3. If it stalls, open Settings > Time & language > Speech and install the pack manually.
4. Restart Live Captions after installation and test with the same video.

### Fix 3: Toggle between system audio and microphone mode

The captions panel has a mic/system-audio switch that is easy to overlook. Being in the wrong mode produces exactly this error.

1. Open the Live Captions window and find the microphone icon in its toolbar.
2. For video/system audio, make sure microphone mode is OFF so captions monitor playback.
3. For transcribing your own speech, turn microphone mode ON and grant permission when asked.
4. Test the matching scenario: video with system mode, speech with mic mode.

### Fix 4: Reset the NPU caption pipeline

On Copilot+ PCs, on-device recognition runs on the NPU. A stalled driver kills recognition while audio plays fine.

1. Close the Live Captions window completely.
2. Restart the laptop to reset the NPU driver state.
3. Reopen Live Captions and test with a video.
4. If captions work after restart but break again later, the NPU driver needs updating — see our guide on the [NPU not being used by apps](/articles/npu-not-used-by-apps-windows-11/). For mic-specific failures, our [microphone captions fix](/articles/live-captions-microphone-not-working/) goes deeper.

### Fix 5: Disable audio enhancements

Third-party audio enhancements (Dolby, Waves MaxxAudio, Nahimic) can reshape the audio stream in ways the caption engine does not expect.

1. Open Settings > System > Sound > your output device > Properties.
2. Turn off "Audio enhancements" or "Enable audio enhancements."
3. In any OEM audio app, disable effects temporarily.
4. Replay the test video and check whether captions now detect audio.

### Fix 6: Repair the caption components

If routing, packs, and drivers are all fine, the caption components themselves may be corrupted. A repair reinstalls them cleanly.

1. Open Settings > Apps > Installed apps and search for speech or caption components.
2. Run `sfc /scannow` in an elevated Command Prompt to repair system files.
3. Check Settings > Windows Update and install all pending updates — caption fixes ship regularly (see the [Windows support hub](https://support.microsoft.com/en-us/windows) for current guidance).
4. As a last resort, remove and re-add the speech language in Settings > Time & language > Language & region.

## Closing

"No audio detected" is a routing or setup message, not a verdict on your hardware. Match the monitored device to your actual output, install the language pack, set the right captions mode, reset the NPU pipeline, and strip interfering audio enhancements. Once the engine hears what you hear, Live Captions on a Copilot+ PC is genuinely impressive — fast, private, and offline. Gaming AI features share the NPU — see [Auto Super Resolution in games not working](/articles/auto-super-resolution-games-not-working/).
