---
title: "How to Fix Live Captions Not Capturing System Audio on Windows 11"
slug: live-captions-system-audio-not-working
date: 2026-10-22
categories: ["ai-pc"]
tags: ["live captions system audio", "live captions no audio", "windows live captions", "captions not working", "copilot plus pc", "windows 11"]
description: "Live Captions silent on system audio in Windows 11? Fix captions that won't capture PC sound on your Copilot+ PC with these six step-by-step solutions."
thumbnail: "/images/thumbs/live-captions-system-audio-not-working.webp"
faqs:
  - q: "Can Live Captions caption system audio and microphone at the same time?"
    a: >
      Live Captions uses one audio source at a time — you pick microphone or a system output device in its settings. Switch sources depending on whether you are captioning a call you are in or media you are watching.
  - q: "Why do captions work for YouTube but not my media player?"
    a: >
      Your media player may be using exclusive-mode audio output, which bypasses the loopback Live Captions monitors. Switch the player to shared/WASAPI-shared output or disable exclusive mode as in Fix 4.
  - q: "Do I need the NPU for system-audio captions?"
    a: >
      Basic Live Captions run on CPU; on Copilot+ PCs, translation and some processing leverage the NPU. System-audio capture itself is an audio-routing matter, not a compute one.
  - q: "Will Live Captions work with Bluetooth headphones?"
    a: >
      Yes, once you select the Bluetooth device as the caption source. Bluetooth adds latency, so captions may lag the audio slightly more than with wired output.
---

Live Captions can caption two very different things: your microphone, and your PC's own system audio — videos, calls, anything playing through your speakers. When microphone captioning works but system audio produces nothing, the captions window sits empty while sound plays merrily on.

System-audio capture uses a virtual audio loopback: Windows routes a copy of the output stream to the captioning engine. If that loopback tap is muted, misrouted, or blocked by exclusive-mode audio, the engine hears silence. It is the same 'tap the stream' architecture as [Slack on ARM Windows](/articles/slack-arm-windows-slow/)-style audio routing, where one misconfigured endpoint silences an entire pipeline.

Six fixes below: selecting the right audio source, unmuting the loopback, fixing exclusive-mode blocks, and repairing the captioning stack. Play a YouTube video as your test signal throughout.

## Why this happens

- **Wrong audio source selected:** Live Captions may be listening to the microphone while you expect system audio — the source selector is the first thing to check.
- **System audio muted in the volume mixer:** The loopback tap respects mute states. A muted browser tab or muted system sounds starve the caption engine.
- **Exclusive-mode audio bypassing the tap:** Apps using WASAPI exclusive mode (some media players, DAWs) bypass the shared audio path where the loopback listens — captions get nothing, the classic [Live Captions no audio detected](/articles/live-captions-no-audio-detected/) trigger.
- **Wrong output device selected:** If audio plays through a device the caption engine is not monitoring (Bluetooth vs speakers), the tap hears silence.
- **Audio enhancements interfering:** Vendor audio enhancements can alter the stream path enough to break the loopback capture.
- **Captioning speech components damaged:** Corrupt speech-recognition components fail on any input — but system-audio-only failure usually exonerates them; still worth verifying.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Select system audio as the caption source

The caption engine can only caption what it is told to listen to.

1. Open Live Captions with **Win + Ctrl + L** and open its settings gear.
2. Set the audio source to your system output device (speakers/headphones), not the microphone.
3. Play your test video and watch for captions to start within a few seconds.
4. If captions appear, you had a source-selection issue — done. If not, continue.

### Fix 2: Unmute every link in the audio chain

A mute anywhere upstream silences the loopback. Check them all.

1. Unmute the browser tab or app playing the audio (right-click the tab).
2. Open the volume mixer (**right-click speaker icon > Open volume mixer**) and unmute the app and system sounds.
3. Confirm the master volume is up and audio actually plays through speakers.
4. Retest captions — the engine cannot caption a stream that never reaches the output.

### Fix 3: Match the output device the engine monitors

Bluetooth switches and multi-device setups routinely desync the tap from the actual output.

1. Play audio and confirm which device it comes from (speakers, headset, Bluetooth).
2. In Live Captions settings, set the source to that exact device.
3. Avoid switching output devices mid-test; each switch can require reselecting the source.
4. On ARM systems with unusual audio routing, [Qualcomm AI Hub models](/articles/qualcomm-ai-hub-models-not-running/)-adjacent driver notes sometimes explain device-enumeration quirks.

### Fix 4: Disable exclusive mode and audio enhancements

Exclusive-mode streams bypass the shared path where captioning listens.

1. Open **Settings > System > Sound**, select your output device, and open its properties.
2. Under **Advanced**, uncheck **Allow applications to take exclusive control of this device**.
3. Disable **Audio enhancements** on the same page temporarily.
4. Restart the audio app and retest captions with exclusive mode off.

### Fix 5: Restart the audio and captioning stack

Stuck audio services wedge the loopback. Bounce them cleanly.

1. In **Services** (services.msc), restart **Windows Audio** and **Windows Audio Endpoint Builder**.
2. Close and reopen Live Captions with **Win + Ctrl + L**.
3. Replay your test video from the start.
4. If captions now work, a wedged audio service was the cause — note it in case it recurs.

### Fix 6: Repair speech components and update drivers

Persistent failure across clean audio paths points at the captioning stack or audio drivers.

1. Install all pending Windows updates — Live Captions components ship with the OS.
2. Update audio drivers from the laptop maker's support page (Realtek, Qualcomm, Intel SST).
3. Run `sfc /scannow` elevated to verify system file integrity.
4. Test microphone captioning too: if both sources fail, the speech stack needs the repair; if only system audio fails, stay focused on routing.

## Closing

System-audio captions fail at the routing layer: wrong source, a mute upstream, the wrong output device, or exclusive mode bypassing the loopback. Select the right source, unmute the chain, align the output device, disable exclusive mode, and restart the audio stack. The caption engine is almost never broken — it is just listening to the wrong silence. For audio-stack problems beyond these steps, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) has the official audio troubleshooters.
