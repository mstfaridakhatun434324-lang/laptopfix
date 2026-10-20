---
title: "Live Captions Microphone Not Working? Fix It Fast"
slug: live-captions-microphone-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["live captions", "microphone", "speech to text", "troubleshooting", "ai pc", "windows 11"]
description: "Live Captions ignoring your microphone on a Copilot+ PC? Learn why mic captions fail while system audio captions work, and fix the input path step by step."
thumbnail: "/images/thumbs/live-captions-microphone-not-working.webp"
faqs:
  - q: "Why do Live Captions work for videos but not my microphone?"
    a: "They use different audio paths. Video captions tap the system playback stream, which needs no permission. Microphone captions need mic privacy permission plus the correct input device selected. The system-audio side working proves the caption engine is fine — the mic path is the problem."
  - q: "Which microphone does Live Captions use?"
    a: "Live Captions uses the Windows default input device, with a toggle in the captions panel to switch between system audio and microphone. If Windows' default input is a disconnected headset, captions hear silence. Set the built-in mic array as default."
  - q: "Do I need a language pack for microphone captions?"
    a: "Yes — the same speech recognition pack that system-audio captions need. If the pack never downloaded, neither path works. If system audio captions work but mic does not, the pack is fine and the problem is permissions or device selection."
  - q: "Can background noise break microphone captions?"
    a: "Heavy noise reduces accuracy but rarely causes total failure. If captions show nothing at all, the cause is configuration, not acoustics. Fix the input path first; worry about noise only if words appear but are wrong."
---

Here is a confusing one: Live Captions transcribes YouTube videos perfectly, but captions your own voice as nothing at all. The caption engine is clearly working — it just cannot hear your microphone. This split behavior is actually good news, because it narrows the problem to the microphone input path: permissions, device selection, or the mic-mode toggle in the captions panel.

On Copilot+ PCs the mic path also passes through the NPU audio pipeline, so a stalled AI audio stack can mute captions even when the mic works in other apps. This guide isolates each layer, from the captions toggle down to the driver. If the whole caption feature reports no audio at all, start with our [no audio detected fix](/articles/live-captions-no-audio-detected/) instead.

Test by speaking a clear sentence after each fix and watching for words to appear.

## Why this happens

- **Mic mode not enabled in captions:** The captions panel defaults to system audio; microphone input is a separate toggle many users never flip.
- **Microphone privacy blocked:** Windows privacy settings deny the caption engine mic access.
- **Wrong default input device:** Windows listens to a disconnected headset instead of the built-in array.
- **NPU audio pipeline stalled:** The on-device recognition path needs the NPU; a driver failure silences mic captions specifically. Confirm the hardware with our [NPU detection guide](/articles/npu-not-detected-windows-11/).
- **Mic muted at hardware level:** A function-key mute or physical shutter disables input before Windows sees it.
- **Exclusive mode lock:** Another app holds the mic exclusively, starving the caption engine.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Enable microphone mode in the captions panel

The captions window defaults to monitoring system audio. Microphone input is a separate toggle, and without it your voice never enters the pipeline.

1. Open the Live Captions window and look at its toolbar.
2. Click the microphone icon to enable microphone input mode.
3. When Windows asks for microphone permission, allow it.
4. Speak a test sentence and watch for words to appear.

### Fix 2: Grant microphone privacy permission

Even with mic mode on, Windows privacy settings can block the caption engine silently. This is the most common real blocker.

1. Open Settings > Privacy & security > Microphone.
2. Turn on "Microphone access" and "Let desktop apps access your microphone."
3. Restart the Live Captions window so it picks up the permission.
4. Speak again — captions should now track your voice.

### Fix 3: Set the correct default input device

Live Captions uses the Windows default input. If that default is a disconnected headset, the engine listens to silence.

1. Open Settings > System > Sound and check the Input device.
2. Select your laptop's built-in microphone array.
3. Speak and confirm the input volume bar moves.
4. Return to Live Captions with mic mode on and test again.

### Fix 4: Check the hardware mute and exclusive mode

A physical mute or an exclusive-mode lock stops the mic before captions ever see it. Rule both out quickly.

1. Press the microphone mute function key (often F4) to ensure the hardware mute is off.
2. In Sound settings > your mic > Properties, uncheck exclusive-mode options.
3. Close apps that might hold the mic (Teams, Zoom, Discord).
4. Test captions with mic mode — if words appear now, a background app was the thief.

### Fix 5: Reset the NPU audio pipeline

On Copilot+ PCs, mic recognition runs through the NPU audio path. A stall here mutes captions while the mic works everywhere else.

1. Close the Live Captions window.
2. Restart the laptop to reset NPU driver state.
3. Reopen captions, enable mic mode, and test.
4. If the problem returns, update the NPU driver from your maker's support page — and confirm the hardware is present with our [NPU detection guide](/articles/npu-not-detected-windows-11/). System-audio caption issues have their own fixes in [no audio detected](/articles/live-captions-no-audio-detected/).

### Fix 6: Reinstall the speech pack and update Windows

A damaged speech model breaks mic recognition specifically, since mic audio exercises different model paths than system audio. If the pack itself will not download, see [Live Captions language pack download failed](/articles/live-captions-language-pack-download-failed/).

1. Remove and re-add the speech language in Settings > Time & language > Language & region.
2. Let the pack fully download, then restart.
3. Install all pending Windows updates — caption components improve every build (see the [Windows support hub](https://support.microsoft.com/en-us/windows)).
4. Final test: speak continuously for ten seconds and confirm captions keep up.

## Closing

Microphone captions fail at the handoff points: the mic-mode toggle, the privacy permission, the default input device, or the NPU audio path. Because system-audio captions work, you know the engine is healthy — so walk the mic path step by step until your voice appears on screen. Once it does, Live Captions becomes a genuinely useful accessibility and productivity tool, not just a video feature. If AI file search is also broken, see [semantic search not finding files](/articles/semantic-search-not-finding-files/).
