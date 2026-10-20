---
title: "Copilot+ PC Microphone Not Working? Fix It in Minutes"
slug: copilot-plus-pc-microphone-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "microphone", "audio issues", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot+ PC microphone not picking up your voice in calls? Find out why the mic goes silent on AI laptops and restore it with these step-by-step fixes."
thumbnail: "/images/thumbs/copilot-plus-pc-microphone-not-working.webp"
faqs:
  - q: "Why is my Copilot+ PC microphone not working in Teams?"
    a: "Teams may be using the wrong input device, or Windows privacy settings may be blocking it. Copilot+ PCs also run AI noise suppression on the NPU, which can fail silently and produce a dead or garbled mic. Check the input device in Teams first, then verify Windows privacy toggles."
  - q: "Do I need special ARM64 audio drivers on Snapdragon Copilot+ PCs?"
    a: "Yes. Snapdragon X laptops need ARM64-native audio drivers from the laptop maker. x64 drivers installed under emulation can load but behave erratically — including a mic that records silence. Always use the driver package on your manufacturer's support page."
  - q: "Can Windows Studio Effects break the microphone?"
    a: "Indirectly. Studio Effects runs on the NPU and shares the audio pipeline with voice focus features. When the NPU effects pipeline stalls, voice enhancement can mute or distort your mic. Disabling Studio Effects in the Camera quick settings often restores audio immediately."
  - q: "Why does the mic work in the Camera app but not in Zoom?"
    a: "That points to a per-app permission problem or Zoom selecting the wrong device. The built-in Camera app uses system defaults, while Zoom keeps its own audio device list. Open Zoom settings, pick the correct microphone, and confirm Zoom is allowed in Windows privacy settings."
---

Nobody can hear you on a call, and you only discover it mid-meeting. Microphone failures on Copilot+ PCs are frustrating because everything looks right — the mic icon is lit, levels even flicker — yet your voice never reaches the other side. In most cases the microphone hardware is fine; the problem sits in device selection, privacy permissions, or the AI audio pipeline.

Copilot+ PCs complicate audio more than older laptops do. Features like voice focus and AI noise removal run on the NPU instead of the CPU, which is great for battery life but adds a layer that can fail silently. If your [Copilot+ PC camera is also not working](/articles/copilot-plus-pc-camera-not-working/), read that guide too — camera and mic frequently break together after the same driver or firmware update, since Studio Effects ties them into one pipeline.

Work through the fixes below in order, and test with the built-in Voice Recorder app after each step so you know exactly which fix worked.

## Why this happens

- **Wrong input device selected:** Windows or your call app is listening to a disconnected headset or the wrong mic instead of the built-in array.
- **Microphone privacy is off:** Windows 11 blocks all apps from the mic if the master toggle or the per-app permission is disabled.
- **AI noise suppression stalls on the NPU:** The NPU audio pipeline can hang after sleep or an update, producing silence or robotic distortion. Our guide to the [NPU not being used by apps](/articles/npu-not-used-by-apps-windows-11/) covers how to reset that pipeline.
- **ARM64 audio driver mismatch:** Snapdragon X systems need native ARM64 audio drivers; emulated x64 drivers cause erratic behavior.
- **Exclusive mode locks the mic:** One app grabs the microphone in exclusive mode, leaving nothing for the app you are actually using.
- **Muted at the hardware level:** A function-key mute or a physical mic shutter on the laptop disables input before Windows ever sees it.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Select the correct input device

Windows often listens to the wrong device after you plug and unplug a headset. The built-in mic array sits idle while Windows records silence from a disconnected Bluetooth headset, so the first fix is always to confirm the active input.

1. Right-click the speaker icon in the taskbar and open Sound settings.
2. Under Input, select your laptop's built-in microphone array instead of any headset or USB device.
3. Speak and watch the volume bar — it should bounce. If it stays flat, the wrong device is still selected.
4. In Teams or Zoom, open audio settings and set the microphone to the same built-in device explicitly.

### Fix 2: Check microphone privacy permissions

Windows 11 privacy toggles are the single most common cause of a dead mic. One flipped switch after an update blocks every app at once, and the app's own settings will still look normal.

1. Open Settings > Privacy & security > Microphone and turn on "Microphone access."
2. Enable "Let desktop apps access your microphone" below the main toggle.
3. Scroll through the app list and make sure Teams, Zoom, and your browser are each allowed.
4. Restart the call app and test with Voice Recorder before rejoining the meeting.

### Fix 3: Disable AI noise suppression temporarily

The NPU-based voice focus pipeline can stall after sleep or a driver update, muting or garbling your audio. Turning it off proves whether the AI layer is the culprit.

1. Open your call app's audio settings and set noise suppression to Off or Low instead of High.
2. In Windows Settings > System > Sound > your microphone > Properties, disable any "voice focus" or enhancement toggle.
3. Test the mic in Voice Recorder — clear audio means the NPU pipeline was at fault.
4. If the mic works without suppression, reinstall your audio driver (Fix 5) before re-enabling AI features. Background reading: [NPU not used by apps in Windows 11](/articles/npu-not-used-by-apps-windows-11/).

### Fix 4: Turn off exclusive mode

Exclusive mode lets one app seize the microphone and lock everyone else out. Disabling it shares the mic fairly across apps, which fixes the classic "works in one app, silent in another" symptom.

1. Open Settings > System > Sound, select your microphone, and open Properties or Advanced.
2. Uncheck "Allow applications to take exclusive control of this device."
3. Close all apps that might use the mic, then reopen only the one you need.
4. Test again — if audio returns, the culprit was a background app hoarding the device.

### Fix 5: Reinstall the ARM64 audio driver

On Snapdragon X Copilot+ PCs, an x64 audio driver running under emulation is a common source of silent-mic bugs. A clean reinstall with the correct ARM64 driver from your maker fixes the underlying mismatch.

1. Open Device Manager, expand "Sound, video and game controllers," and uninstall the audio device (tick "remove the driver").
2. Restart — Windows will attempt a reinstall. Test the mic.
3. If it still fails, download the audio driver from your manufacturer's support page (for example [Lenovo Support](https://support.lenovo.com/us/en/)) and install it manually.
4. Prefer the maker's package over generic Windows Update drivers, which may lack the NPU audio path.

### Fix 6: Run the audio troubleshooter and check the hardware mute

When everything looks right but the mic stays silent, the built-in troubleshooter catches misconfigurations you might miss, and a quick hardware check rules out a physical mute.

1. Go to Settings > System > Troubleshoot > Other troubleshooters and run "Recording Audio."
2. Apply whatever fix it suggests, then test with Voice Recorder.
3. Press the mic-mute function key (often F4) to make sure the hardware mute is off.
4. If a headset mic works but the built-in array does not, the internal mic cable may be loose — contact support rather than opening the chassis.

## Closing

A silent microphone on a Copilot+ PC is almost always device selection, privacy, or the AI audio pipeline — not broken hardware. Work through input device, privacy, suppression, exclusive mode, and the driver in that order, testing with Voice Recorder after each step. Once your voice comes back clear, re-enable noise suppression and enjoy the NPU doing the heavy lifting quietly in the background. Competitive anti-cheat software is another common ARM headache — see [Valorant Vanguard on ARM](/articles/valorant-vanguard-arm-not-supported/). Storage upgrades are another common Copilot+ PC project — see our [Copilot+ PC SSD upgrade guide](/articles/copilot-plus-pc-ssd-upgrade-guide/).
