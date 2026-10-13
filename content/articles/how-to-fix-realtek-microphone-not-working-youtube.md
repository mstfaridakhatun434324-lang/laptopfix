---
title: "How to Fix a Realtek Microphone Not Working on a Laptop"
slug: how-to-fix-realtek-microphone-not-working-youtube
date: 2026-10-05
categories: ["drivers"]
tags: ["realtek microphone", "mic not working", "laptop microphone", "audio input"]
description: "Fix a Realtek microphone not working on a laptop: unblock privacy settings, restore the mic device, and repair the Realtek audio driver."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-youtube.webp"
faqs:
  - q: "Why is my laptop microphone not picking up any sound?"
    a: "The most common reasons are Windows privacy settings blocking microphone access, the microphone being disabled or not set as default in Sound settings, or the Realtek audio driver being corrupted. Work through privacy first — it is the fastest check — then device defaults, then driver repair."
  - q: "My mic works in one app but not another. What is wrong?"
    a: "That is almost certainly a privacy or per-app permission issue, not a driver fault. Check Settings, Privacy and security, Microphone and confirm the non-working app is allowed. Also check the app's own audio settings — it may be listening to the wrong input device."
  - q: "The microphone is very quiet even at 100% volume. How do I boost it?"
    a: "Open More sound settings, Recording tab, right-click the microphone, Properties, Levels — raise both the volume and the Microphone Boost slider if present. Disable audio enhancements, which can suppress input gain, and make sure nothing is physically covering the mic pinhole on the laptop."
  - q: "Should I reinstall the Realtek driver to fix the microphone?"
    a: "Yes, if privacy and settings checks do not help. The microphone is an input endpoint of the Realtek audio device, and driver corruption can kill input while output keeps working — which is exactly why mic failures confuse people. Reinstalling the laptop maker's Realtek driver package restores both sides together, so download it from your model's support page and install it as administrator."
---

A dead laptop microphone announces itself at the worst moments — the meeting where nobody hears you, the voice call where you are talking into the void, the recording that captured silence. Microphone failures are particularly tricky because the fault can sit in four different places: Windows privacy controls, the Sound device configuration, the Realtek driver, or the physical mic — and each produces the same symptom of silence.

This guide works the layers from fastest to deepest. Privacy settings take thirty seconds to check and fix an enormous share of cases; device defaults and levels come next; then the Realtek driver repair that fixes the stubborn ones; and finally the hardware checks that confirm the mic itself.

Laptop microphones are more sophisticated than the pinhole suggests. Most modern laptops use a dual-microphone array with beamforming — two mics whose signals are combined to focus on your voice and reject keyboard noise — and the Realtek codec applies noise suppression and echo cancellation on top. This processing chain has more configurable stages than the speaker output path, which is why microphone problems have causes (privacy blocks, enhancement conflicts, app-level device selection) that never affect playback. When diagnosing, treat the input path as its own system: the fact that speakers work tells you almost nothing about why the mic does not, because they share only the driver package and diverge everywhere else.

## Why this happens

- **Privacy settings blocking access:** Windows denies microphone access globally or per-app — the number-one cause.
- **Microphone disabled:** The recording device is disabled in Sound settings.
- **Wrong default input:** Apps listen to a disconnected headset mic or virtual device instead of the built-in array.
- **Realtek driver corruption:** Kills the input endpoint while output keeps working, which confuses diagnosis.
- **Low levels / boost missing:** The mic works but is inaudible without proper gain.
- **Enhancement interference:** Noise suppression and enhancements can gate or distort input.
- **App-specific misconfiguration:** Meeting apps pointed at the wrong device.
- **Physical blockage or failure:** Covered mic holes, or a dead mic array — the hardware end.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone privacy settings

1. Open **Settings → Privacy & security → Microphone**.
2. Ensure **Microphone access** is **On** and **"Let apps access your microphone"** is **On**.
3. Scroll through the app list and confirm your meeting/recording app is individually allowed.
4. Test immediately — privacy blocks are the single most common cause and the fastest fix. This mirrors the headset-mic checks in [USB headset troubleshooting](/articles/how-to-fix-usb-headset-not-working-on-windows-10/).

### Fix 2: Set the correct default recording device

1. Right-click the speaker icon → **Sound settings** → under **Input**, select **Microphone Array (Realtek Audio)** or similar built-in mic.
2. Speak and watch the input volume bar — movement means the mic hears you.
3. Open **More sound settings → Recording**, right-click the Realtek mic → **Set as Default Device** and **Set as Default Communication Device**.
4. Right-click empty space → **Show Disabled Devices**; if the mic appears greyed, right-click → **Enable**.

### Fix 3: Raise levels and boost

1. In **Recording → microphone → Properties → Levels**, set volume to **100** and raise **Microphone Boost** (+10 to +30 dB) if available.
2. On the **Enhancements** tab, check **"Disable all enhancements"** for testing — enhancements can suppress quiet input.
3. On the **Advanced** tab, uncheck **"Allow applications to take exclusive control"** temporarily.
4. Retest in Sound settings and in your app — many "dead" mics are just whisper-quiet.

### Fix 4: Check the app's own audio settings

1. Open your meeting app's settings → Audio, and explicitly select the Realtek microphone — not "Default" or "System."
2. Check the app's input volume slider independently of Windows.
3. Test with Windows' built-in **Voice Recorder** app — working there but not in your meeting app proves the issue is app configuration.
4. Sign out and back into the meeting app after changing devices; some apps cache the device list.

### Fix 5: Reinstall the Realtek audio driver

1. Open **Device Manager → Sound, video and game controllers**, right-click **Realtek Audio** → **Uninstall device** (check driver removal if offered).
2. Restart — Windows reinstalls a basic driver; test the mic.
3. For the full fix, download the **Realtek audio driver** for your exact model from your laptop maker's support site and install it.
4. Driver corruption that kills input while sparing output is a known Realtek pattern — the same repair behind [Realtek audio output failures](/articles/how-to-fix-realtek-audio-not-working-on-windows-10/) applies to the mic side.

### Fix 6: Run the recording audio troubleshooter

1. Open **Settings → System → Sound**, scroll to **Input**, and run **Troubleshoot** on the microphone.
2. Also try **Settings → System → Troubleshoot → Other troubleshooters → Recording Audio → Run**.
3. Apply recommended fixes and restart if prompted.
4. The troubleshooter catches disabled devices and service issues you may have missed.

### Fix 7: Check physical factors

1. Locate the microphone pinholes (usually near the webcam or along the top edge) and ensure no sticker, case, or debris covers them.
2. Clean gently with a dry soft brush — never poke into the holes.
3. Test in a quiet room close to the laptop; beamforming arrays need reasonable proximity.
4. If an external mic or headset mic works fine but the built-in array never does across all software, the array or its cable has likely failed.

### Fix 8: Services, updates, and final repair

1. Restart **Windows Audio** and **Windows Audio Endpoint Builder** in **services.msc** (both Automatic).
2. Install pending Windows updates including optional audio drivers — then verify they did not regress the mic.
3. If a specific update broke the mic, roll back the Realtek driver in Device Manager and block the bad update per [Microsoft support](https://support.microsoft.com/en-us/windows) guidance.
4. As a last resort, a Windows repair install rebuilds the audio stack while keeping files — appropriate when the mic fails across every app, user account, and driver version.

## Closing

Realtek microphone failures are privacy settings and configuration problems far more often than broken hardware: a blocked permission, the wrong default device, or levels set too low. Check privacy first, set explicit defaults, boost the gain, then repair the Realtek driver — and the mic that captured silence starts capturing you again.
