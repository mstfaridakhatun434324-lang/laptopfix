---
title: "Fix a USB Headset That Won't Work on Windows 10"
slug: how-to-fix-usb-headset-not-working-on-windows-10
date: 2026-09-01
categories: ["drivers"]
tags: ["usb headset", "windows 10", "no sound", "audio driver", "troubleshooting"]
description: "USB headset not working on Windows 10? Fix playback, microphone, and detection problems with these step-by-step audio repairs."
thumbnail: "/images/thumbs/how-to-fix-usb-headset-not-working-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 detect my USB headset but produce no sound?"
    a: "Detection without audio usually means the wrong playback device is selected, or the headset's volume is muted at the device level. Open Sound settings, set the headset as the default device, and check both the app volume mixer and the headset's own inline controls."
  - q: "Can a USB port cause a headset to stop working?"
    a: "Yes. A port with damaged data pins still delivers power, so the headset lights up but never enumerates. Front-panel ports and worn connectors are frequent culprits. Moving the headset to a rear motherboard USB port often resolves it instantly. If the rear ports also fail, test the headset on another computer to rule out the headset itself."
  - q: "Why does my USB headset microphone not work but audio does?"
    a: "USB headsets expose separate playback and recording endpoints, and each has its own default assignment and privacy permission. Grant microphone access in Settings and set the headset mic as the default recording device to fix one-sided failures. Also check the app's own audio settings, since many apps override the Windows default device."
  - q: "Do USB headsets need drivers on Windows 10?"
    a: "Most use the built-in USB Audio class driver and need nothing extra. Gaming headsets with surround features may require the vendor's software. If the vendor driver fails, the headset usually still works in basic stereo mode on the generic driver."
---

A USB headset that refuses to work on Windows 10 is uniquely frustrating because the device seems half-alive: the LEDs glow, Windows may even show its name, but no sound comes out and no voice goes in. Meetings become a scramble of unplugging, replugging, and apologizing. The failure usually lives in one of three places — the USB port, the audio device routing, or Windows privacy settings — and each has a fast, definitive test.

Windows 10 treats a USB headset as its own sound card, which means it bypasses your laptop's Realtek audio entirely. That isolation is actually helpful for diagnosis: if the laptop speakers work but the headset does not, the problem is confined to the USB audio path. Problems after Windows updates are common because updates reset default devices and microphone permissions without warning.

The fixes below start with the thirty-second checks and move toward driver-level repairs. By the end, your headset will either be working or you will know exactly which component is at fault.

Windows 10 also has a power feature called USB selective suspend that puts individual USB ports to sleep to save power. On some laptops it suspends the headset's port mid-call, producing the classic symptom of audio that works for a few minutes and then dies. The fixes below include disabling it, because it is one of those settings that causes intermittent failures people chase for weeks.

## Why this happens

- **Wrong default playback or recording device:** Windows routes audio to the last-used device. After an update or a device swap, sound may be going to speakers while you wear the headset.
- **Microphone privacy settings blocking access:** Windows 10 privacy controls can revoke microphone access system-wide, silently muting every headset mic.
- **USB port enumeration failure:** Damaged or underpowered ports provide power but fail data handshake, so the headset never registers as an audio device.
- **Corrupted USB Audio driver:** The generic usbaudio driver can be left in a bad state by a failed update, breaking both playback and capture.
- **Exclusive mode conflicts:** An app that grabs the headset in exclusive mode locks other apps out, producing silence everywhere else.
- **Inline mute or volume controls engaged:** Many headsets ship with hardware mute buttons or volume wheels set to zero that are easy to trigger accidentally.
- **Conflicting audio software:** Vendor surround suites and equalizers can misroute the USB audio stream or crash the audio engine on startup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the headset as the default device

Windows will not switch automatically. Explicitly assigning the headset as default for both playback and recording fixes the majority of cases.

1. Right-click the speaker icon in the taskbar and choose **Sounds**, then open the **Playback** tab.
2. Right-click your USB headset and choose **Set as Default Device**, then **Set as Default Communication Device**.
3. Switch to the **Recording** tab and repeat both assignments for the headset microphone.
4. Click OK, then test with a YouTube video and the built-in Voice Recorder.

### Fix 2: Try a different USB port, preferably on the back

Ports fail in subtle ways. Moving the headset rules out the port in seconds and is the fastest hardware test you have.

1. Unplug the headset and connect it to a USB port directly on the motherboard (rear ports on desktops, the opposite side on laptops).
2. Avoid USB hubs, front-panel ports, and worn ports that feel loose.
3. Wait ten seconds for Windows to enumerate the device, then check **Device Manager > Audio inputs and outputs**.
4. If the headset appears on the new port, the old port is damaged — this is also a classic trigger for [USB-related device dropouts](/articles/how-to-fix-airplane-mode-stuck-on-on-asus-laptop/).

### Fix 3: Grant microphone access in privacy settings

Windows 10 can silently revoke mic access after updates, which mutes the headset microphone in every app at once.

1. Open **Settings > Privacy > Microphone**.
2. Turn on **Allow apps to access your microphone**.
3. Scroll down and enable access for the specific apps you use, such as Teams, Zoom, or Discord.
4. Restart the app and test the mic. Also confirm the mic is not muted on the headset's inline control.

### Fix 4: Reinstall the USB audio driver

A corrupted usbaudio driver breaks both directions of the headset. Reinstalling forces a clean rebind.

1. Open **Device Manager** and expand **Audio inputs and outputs**.
2. Right-click the USB headset entries and choose **Uninstall device** for each.
3. Expand **Sound, video and game controllers** and uninstall any headset-related entry there too.
4. Unplug the headset, restart Windows, then plug it back in and let Windows reinstall the driver.

### Fix 5: Disable exclusive mode on the headset

Exclusive mode lets one app seize the headset and starve everything else. Turning it off restores shared access.

1. Right-click the speaker icon, choose **Sounds**, and double-click the USB headset on the Playback tab.
2. Go to the **Advanced** tab and uncheck **Allow applications to take exclusive control of this device**.
3. Repeat on the Recording tab for the headset microphone.
4. Click OK and restart your audio apps.

### Fix 6: Remove conflicting audio software

Vendor audio suites can crash the Windows audio engine or reroute the USB stream into a dead virtual device.

1. Open **Settings > Apps** and uninstall third-party audio enhancers, equalizers, or surround suites one at a time.
2. After each removal, restart and test the headset before removing the next.
3. If the headset works after a removal, reinstall only that vendor's latest version from its official site.
4. As a reference, Microsoft documents the built-in audio troubleshooters on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Test the headset on another computer

This is the definitive hardware test. It separates a dead headset from a Windows problem with no ambiguity.

1. Plug the headset into a different PC or a phone with a USB adapter.
2. If it works there, the fault is in your Windows 10 installation — consider a driver rollback or a repair install.
3. If it fails everywhere, the headset cable, USB plug, or internal DAC has failed and needs replacement.
4. For headsets under warranty, record the failure symptoms before contacting support. If Windows also fails to detect wired headphones, see the [headphone detection guide](/articles/how-to-fix-laptop-not-detecting-headphones-after-windows-11-update/).

### Fix 8: Disable USB selective suspend

Selective suspend powers down idle USB ports, and headsets are frequent victims. Disabling it keeps the port awake permanently.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both battery and plugged-in.
3. Click OK and restart.
4. Test with a long call — dropouts that previously appeared after minutes of use should be gone.

## Closing

USB headsets fail in predictable ways: wrong defaults, blocked microphones, bad ports, or corrupted drivers. Work the list in order and you will either fix it or prove the headset itself is dead — and in practice, it is a settings problem far more often than a hardware one.
