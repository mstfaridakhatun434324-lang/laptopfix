---
title: "How to Fix Live Captions Not Working in Teams Meetings on Windows 11"
slug: live-captions-teams-meeting
date: 2026-10-22
categories: ["ai-pc"]
tags: ["live captions teams", "teams meeting captions", "windows live captions", "teams captions fix", "copilot plus pc", "windows 11"]
description: "Live Captions dead in Teams meetings on Windows 11? Get Windows Live Captions working alongside Teams on your Copilot+ PC with these six proven fixes."
thumbnail: "/images/thumbs/live-captions-teams-meeting.webp"
faqs:
  - q: "Should I use Teams captions or Windows Live Captions in meetings?"
    a: >
      Use one, not both. Teams' built-in captions are server-side with translation options; Windows Live Captions run on-device and work across all apps. For Teams-only meetings, Teams' own captions are usually the smoother choice.
  - q: "Why are Windows captions delayed in Teams meetings?"
    a: >
      Delay usually means the engine is struggling with the audio: heavy Teams noise suppression, an emulated Teams build on ARM, or NPU/CPU contention. Tune processing down and use the native Teams build.
  - q: "Can Live Captions translate Teams meetings?"
    a: >
      On Copilot+ PCs, Windows Live Captions can translate captions into English on-device. Teams' own live translated captions are a separate server-side feature with broader language options.
  - q: "Do meeting participants know I'm using Live Captions?"
    a: >
      Windows Live Captions are local to your PC — other participants are not notified. Teams' built-in captions may show indicators per meeting policy. When in doubt, mention it as a courtesy.
---

Teams has its own built-in live captions — and Windows has system-wide Live Captions. Running both, or expecting Windows' to handle a Teams call, produces the classic mess: duplicate captions, no captions, or captions that lag minutes behind.

The two systems fight over the same audio: Teams' server-side captions and Windows' on-device engine both try to transcribe the meeting. Add Teams' audio processing (noise suppression, echo cancellation) reshaping the stream, and Windows' engine may receive audio it cannot use. It is the same two-clients-one-resource contention as [NPU exclusive-mode app conflicts](/articles/npu-exclusive-mode-app-conflict/), where exclusive access by one app starves the other.

Six fixes below: choosing one caption system, configuring Teams audio correctly, and repairing the pipeline. Join a test meeting (or a recorded one) to verify each step.

## Why this happens

- **Teams and Windows captions conflicting:** Running both caption systems simultaneously causes duplicates, lag, and sometimes a complete stall as they contend for the audio stream.
- **Teams audio processing distorting the stream:** Aggressive noise suppression can strip speech characteristics the on-device recognizer needs — clean to human ears, unusable to the engine.
- **Wrong audio source for the meeting:** Windows Live Captions must monitor the device carrying the meeting audio; Teams' own virtual devices confuse the source selection.
- **Teams running emulated on ARM:** An x64-emulated Teams on Snapdragon handles audio through translation layers that degrade the stream for capture — the native-vs-emulated split [VS Code native versus x64 builds](/articles/vscode-arm-native-vs-x64/) documents.
- **Outdated Teams client:** Caption-related Teams bugs get fixed in client updates; old builds have known incompatibilities with system captioning.
- **Permissions blocking audio capture:** Microphone privacy settings can block the loopback/capture path Windows Live Captions needs for meeting audio.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pick ONE caption system per meeting

Two caption engines is worse than one. Choose deliberately.

1. If you want Teams' built-in captions: turn them on in the Teams meeting controls (**More > Language and speech > Turn on live captions**) and turn Windows Live Captions off (**Win + Ctrl + L** toggle).
2. If you want Windows' on-device captions: turn Teams' captions off and enable Windows Live Captions instead.
3. Never run both — the contention causes exactly the duplicates and stalls users complain about.
4. Teams' captions need internet and support translation server-side; Windows' work on-device. Pick based on your needs.

### Fix 2: Set Windows Live Captions to the meeting audio device

Point the engine at the actual meeting audio, not a guess.

1. In Windows Live Captions settings, set the source to your current output device (the one carrying Teams audio).
2. If using a headset for the meeting, select that headset explicitly.
3. Play a Teams test call (**Settings > Devices > Make a test call**) and confirm captions track it.
4. Re-select the source whenever you switch audio devices mid-day.

### Fix 3: Tune Teams audio processing down

Over-aggressive Teams processing can mangle the stream for the caption engine.

1. In Teams **Settings > Devices**, set **Noise suppression** to Low instead of High/Auto for the test.
2. Disable any vendor 'AI noise cancellation' or voice-focus effects during the test — [NPU exclusive-mode app conflicts](/articles/npu-exclusive-mode-app-conflict/)-style exclusive processing conflicts apply here too.
3. Make a test call and check caption accuracy with processing minimized.
4. Restore your preferred suppression afterward if captions work — you will know the tradeoff.

### Fix 4: Update Teams and run the native build

Client version and architecture both matter for audio fidelity.

1. Update Teams to the latest version via the profile menu or Microsoft Store.
2. On Snapdragon PCs, verify Teams is the native ARM64 build (Task Manager > Details > Architecture column).
3. Reinstall as ARM64 if you find the emulated x64 build — audio routing improves markedly.
4. Retest captions in a real meeting after the update.

### Fix 5: Check microphone privacy permissions

Windows privacy settings can silently block the capture path.

1. Go to **Settings > Privacy & security > Microphone** and confirm microphone access is on.
2. Confirm **Let desktop apps access your microphone** is enabled — Windows Live Captions counts as a desktop component.
3. The [Live Captions microphone not working](/articles/live-captions-microphone-not-working/) guide covers the same permission repairs for the microphone path specifically.
4. Restart Live Captions after changing permissions.

### Fix 6: Repair and isolate with a clean test

When configuration is right but captions still fail, repair the stack and isolate variables.

1. Install all pending Windows updates and restart.
2. Test Windows Live Captions on a YouTube video first — if that works, the engine is fine and Teams is the variable.
3. Try a different headset or speakers to rule out device-specific routing bugs.
4. Report persistent Teams-specific failures via Teams **Help > Give feedback** with your client version.

## Closing

Windows Live Captions in Teams meetings fail from contention: two caption systems fighting, Teams' audio processing reshaping the stream, or the wrong source selected. Pick one caption system, point Windows at the right device, calm Teams' processing, run the native ARM64 client, and check permissions. Meetings are hard enough without fighting your captions — set it up once and let it run. If meeting captions stay broken, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) covers both Windows and Teams audio paths.
