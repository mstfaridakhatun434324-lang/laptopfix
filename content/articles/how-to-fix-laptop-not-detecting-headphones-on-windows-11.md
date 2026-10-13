---
title: "Laptop Not Detecting Headphones on Windows 11: Wired & Bluetooth Fixes"
slug: how-to-fix-laptop-not-detecting-headphones-on-windows-11
date: 2026-10-04
categories: ["drivers"]
tags: ["headphones not detected", "windows 11", "audio driver", "realtek", "bluetooth headphones"]
description: "Plugged in headphones but no sound on Windows 11? Fix wired jack detection and Bluetooth pairing with these audio driver repairs."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-detecting-headphones-on-windows-11.webp"
faqs:
  - q: "Why does my laptop not detect wired headphones when I plug them in?"
    a: "The usual cause is the Realtek audio driver failing to sense the jack insertion — the HD Audio driver handles jack detection, and when it is corrupted or replaced by a generic driver, plugging in produces no popup and no device switch. Front-panel jack detection settings, a disabled audio device in Sound settings, or Windows routing audio to the wrong output also produce the same symptom."
  - q: "My Bluetooth headphones pair but don't appear as an audio device. Why?"
    a: "Pairing and audio are separate steps: the headphones can pair over Bluetooth while the audio profiles (A2DP for music, HSP/HFP for calls) fail to connect. This happens when Bluetooth drivers are outdated, when the headphones are stuck in headset mode from a previous call, or when Windows' Bluetooth audio service glitched. Removing the device, updating Bluetooth drivers, and re-pairing fresh usually restores the audio profiles."
  - q: "Should I disable front panel jack detection in Realtek settings?"
    a: "Only as a diagnostic step, not a permanent fix. Disabling jack detection forces the audio driver to treat the jack as always connected, which can restore sound when the detection circuit is faulty. But it also breaks automatic speaker/headphone switching. If disabling it fixes your audio, the real problem is the jack detection logic — update the Realtek driver from your laptop manufacturer's site for a proper fix."
  - q: "Can Windows 11 updates break headphone detection?"
    a: "Yes, regularly. Updates replace manufacturer-tuned Realtek drivers with generic Microsoft HD Audio drivers that handle jack detection poorly on many laptop models, and they sometimes reset the default audio device to the speakers. After any update that kills headphone detection, check the default output device first, then reinstall the manufacturer's audio driver."
---

Plug in your headphones, and... nothing. The sound keeps coming from the laptop speakers, no popup asks what you plugged in, and the headphones do not appear in the sound settings. Or your Bluetooth headphones pair successfully but never show up as a playback device. On Windows 11, both failures trace to the audio driver stack — the Realtek HD Audio driver for wired jacks, the Bluetooth stack for wireless — and both are fixable without new hardware in the large majority of cases.

Wired and Bluetooth headphones fail for completely different reasons, so this guide treats them as two diagnostic tracks after the shared first checks. For the deeper 24H2-specific variant, see our [headphones guide for Windows 11 24H2](/articles/how-to-fix-laptop-not-detecting-headphones-in-windows-11-24h2/), and the [post-update audio repair](/articles/how-to-fix-laptop-not-detecting-headphones-after-windows-11-update/) covers cases where an update caused the regression.

## Why this happens

- **The Realtek audio driver is corrupted or generic**, so jack insertion is never detected and no device switch occurs.
- **The headphones are disabled as a playback device** in Sound settings, hiding them from the output list entirely.
- **Windows kept the speakers as the default output** after the headphones were connected, so audio never routes to them.
- **Bluetooth audio profiles failed to connect** even though pairing succeeded, leaving no playback device.
- **Front-panel jack detection is misconfigured** in the Realtek control panel after a driver change.
- **The audio service or Bluetooth service glitched**, requiring a restart to re-enumerate devices.
- **A Windows update replaced the manufacturer's audio driver** with a generic one that handles detection poorly.

- **Windows 11's per-app volume mixer routed the app to the wrong device**, so the headphones are detected and selected system-wide while the specific application still plays through the speakers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the default output device

The most common "not detected" is actually "detected but not selected." The quick-settings output picker is the fastest routing check and takes five seconds.

1. Click the volume icon in the taskbar and click the arrow next to the volume slider.
2. Look for your headphones in the output list and select them.
3. If they appear but produce no sound, the detection worked and the issue is routing or volume.
4. Right-click the volume icon, open Sound settings, and confirm the headphones show under Output.

### Fix 2: Reveal disabled playback devices

Windows hides disabled devices, and headphones often end up disabled after driver changes. Manufacturer audio drivers often come bundled with the chipset package — install chipset first if audio setup complains.

1. Right-click the volume icon and choose Sound settings, then More sound settings.
2. In the Playback tab, right-click empty space and tick Show Disabled Devices.
3. If your headphones appear greyed out, right-click them and choose Enable.
4. Right-click again and set them as the default device.

### Fix 3: Reinstall the Realtek audio driver

The core fix for wired jack detection failures. Microsoft documents audio troubleshooting on the [Windows support site](https://support.microsoft.com/en-us/windows). The Realtek Audio Console sometimes needs a Microsoft Store update before its settings pages appear.

1. Press Win + X, open Device Manager, and expand Sound, video and game controllers.
2. Right-click the Realtek audio device and choose Uninstall device, ticking Delete the driver software if offered.
3. Restart — Windows will reinstall a driver automatically.
4. For the best results, download the audio driver from your laptop manufacturer's support page and install it over the automatic one.

### Fix 4: Check Realtek jack detection settings

The detection logic itself can be toggled off. After re-pairing, wait for Windows to finish 'setting up device' before testing audio.

1. Open the Realtek Audio Console from the Start menu (install it from the Microsoft Store if missing).
2. Go to Device advanced settings.
3. Ensure jack detection is enabled rather than forced to a fixed state.
4. Plug and unplug the headphones while watching the console to confirm it registers the insertion.

### Fix 5: Restart the audio services

A glitched audio service can stop enumerating new devices.

1. Press Win + R, type services.msc, and press Enter.
2. Find Windows Audio and restart it.
3. Find Windows Audio Endpoint Builder and restart it as well.
4. Replug the headphones and check the output list again.

### Fix 6: Fix Bluetooth headphones that pair but produce no audio

For wireless headphones, remove and re-pair cleanly.

1. Go to Settings, Bluetooth and devices, and remove the headphones from the device list.
2. Put the headphones in pairing mode (usually a long press on the power button).
3. Re-pair them and wait a full thirty seconds for the audio profiles to connect.
4. In Sound settings, confirm they appear as both an output device and, if applicable, a headset device — then set the stereo (A2DP) entry as default for music.

### Fix 7: Update Bluetooth drivers and reset the stack

Stubborn Bluetooth audio failures live in the Bluetooth driver.

1. In Device Manager, expand Bluetooth and update the drivers for your Bluetooth adapter and any headphone entries.
2. Download the latest Bluetooth driver from your laptop manufacturer's support page if Windows finds nothing newer.
3. As a last resort, remove all Bluetooth devices, uninstall the Bluetooth adapter with driver deletion, restart, and re-pair everything fresh.

## Closing

Headphone detection on Windows 11 is a routing and driver problem far more often than a hardware problem: check the output list, reveal disabled devices, and reinstall the manufacturer's audio driver before suspecting the jack. Bluetooth headphones that pair without audio need a clean re-pair and profile reconnect, not a new headset. If a wired jack never registers insertion even in the Realtek console after a driver reinstall, the jack's detection pin may be physically damaged — a repair-shop job, but an uncommon one. After restoring detection, test with both a system sound and your actual application, since per-app routing can diverge from the system default. If one application stubbornly uses the speakers, its internal output selector — not Windows — is the remaining setting to change.
