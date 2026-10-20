---
title: "Copilot Voice Mode Not Working? How to Fix It"
slug: copilot-voice-mode-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot", "voice mode", "voice assistant", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot voice mode not responding on your AI laptop? Find out why voice conversations fail and fix microphone, permission, and app issues step by step."
thumbnail: "/images/thumbs/copilot-voice-mode-not-working.webp"
faqs:
  - q: "Why does Copilot voice mode not hear me?"
    a: "The usual chain: microphone permission denied, wrong input device selected, or the mic muted at the hardware level. Copilot's voice mode needs mic access just like any voice app — check Settings > Privacy & security > Microphone first, then confirm the right input device."
  - q: "Does Copilot voice mode work offline?"
    a: "No. Unlike on-device features such as Live Captions, Copilot voice conversations process in the cloud and need an internet connection. If voice mode fails only offline, that is expected behavior, not a bug."
  - q: "Why does voice mode work on my phone but not my laptop?"
    a: "Different apps, different permission models. The Windows Copilot app has its own microphone permission and audio pipeline. Phone success proves your account is fine — the laptop's local audio path is where the problem lives."
  - q: "Can Copilot voice mode work with Bluetooth headsets?"
    a: "Yes, but Bluetooth adds a failure point: the headset must be the active input device in Windows, and some headsets expose separate 'headset' and 'hands-free' profiles with very different mic quality. Set the headset as the input device explicitly in Sound settings."
---

Talking to Copilot should feel natural — you tap the mic, speak, and it answers. Instead you get silence, an error, or Copilot cheerfully transcribing nothing. Voice mode failures on AI laptops are almost always audio-path problems rather than Copilot problems: the app never receives your voice, so it has nothing to respond to.

The diagnostic shortcut is simple: if Copilot's text chat works but voice does not, your account and connection are fine — the microphone path is broken. This guide fixes that path from permissions to drivers. If the mic is dead everywhere, our broader [Copilot+ PC microphone guide](/articles/copilot-plus-pc-microphone-not-working/) covers the system-wide repair; here we focus on the Copilot-specific layer.

Test by asking Copilot a simple spoken question after each fix.

## Why this happens

- **Microphone permission denied for Copilot:** The Copilot app needs its own mic permission grant.
- **Wrong input device:** Windows routes Copilot's listening to a disconnected device.
- **Voice feature not available in region:** Copilot voice rolls out by region; some regions get text-only Copilot.
- **Outdated Copilot app:** Voice mode improved across app updates; old versions have broken voice pipelines.
- **Network blocking voice traffic:** Firewalls or VPNs can block the real-time audio streams voice mode needs.
- **Corrupted Copilot app data:** A bad cache breaks the voice session handshake.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Grant the Copilot app microphone permission

Voice mode cannot start without mic access. This single permission fixes most cases.

1. Open Settings > Privacy & security > Microphone.
2. Ensure "Microphone access" and "Let desktop apps access your microphone" are on.
3. Find Microsoft Copilot in the app list and make sure its toggle is enabled.
4. Restart the Copilot app and tap the microphone button again.

### Fix 2: Set the correct input device

Copilot listens to the Windows default input. A wrong default means it hears silence.

1. Open Settings > System > Sound and check the Input device.
2. Select your built-in microphone array (or your headset, if that is what you use).
3. Speak and confirm the input level bar moves.
4. Return to Copilot voice mode and try a spoken question.

### Fix 3: Check the hardware mute

Laptops love hiding mic mutes. A function-key mute kills input before any app sees it.

1. Press the mic-mute function key (often F4, sometimes with Fn).
2. Look for an on-screen indicator confirming the mic is unmuted.
3. Check for a physical mic shutter or kill switch on the chassis.
4. Test voice mode again.

### Fix 4: Update the Copilot app

Voice mode is under active development; older app builds have known voice bugs.

1. Open the Microsoft Store, go to Library, and update Microsoft Copilot.
2. Fully close and reopen the Copilot app after updating.
3. If the Store version lags, check for Windows updates too — Copilot ships with the OS on some builds.
4. Test voice mode with a simple question like "What time is it?"

### Fix 5: Test your network path

Voice mode streams audio to the cloud in real time. VPNs, strict firewalls, and captive portals break that stream while text chat keeps working.

1. Disconnect your VPN temporarily and test voice mode.
2. Try a different network (phone hotspot) to rule out firewall filtering.
3. If on corporate Wi-Fi, the voice endpoints may be blocked — use another network.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) lists current Copilot requirements if issues persist.

### Fix 6: Reset the Copilot app

Corrupted app data breaks the voice session handshake even when everything else is configured correctly.

1. Go to Settings > Apps > Installed apps > Microsoft Copilot > Advanced options.
2. Click Repair first and test voice mode.
3. If repair fails, click Reset (this signs you out — have your credentials ready).
4. Sign back in and test voice mode. For a mic that is dead system-wide, see [Copilot+ PC microphone not working](/articles/copilot-plus-pc-microphone-not-working/).

## Closing

Copilot voice mode fails at the microphone handoff: permissions, input device, hardware mute, or the network path for its cloud stream. Because text chat proves your account works, the fix is always local — grant the permission, pick the right mic, unmute the hardware, update the app, and clear the network path. Then just talk; that is the whole point. ASUS AI laptops have their own quirks — see [ASUS Zenbook A14 AI issues](/articles/asus-zenbook-a14-ai-issues/) — and if the NPU itself is missing, start with [NPU not detected in Windows 11](/articles/npu-not-detected-windows-11/). For Copilot's visual features, see [Copilot Vision not working on Windows 11](/articles/copilot-vision-not-working-windows/).
