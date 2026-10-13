---
title: "How to Fix USB Headset Not Working in Windows 11 24H2"
slug: "how-to-fix-usb-headset-not-working-in-windows-11-24h2"
date: "2026-09-26"
categories: ["drivers"]
tags: ["usb headset", "headset not working", "windows 11 24h2", "usb audio", "microphone"]
description: "USB headset not detected or no sound on Windows 11 24H2? Fix it with USB power tweaks, audio device resets, driver reinstalls, and exclusive-mode fixes."
thumbnail: "/images/thumbs/how-to-fix-usb-headset-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my USB headset not detected on Windows 11 24H2?"
    a: "The 24H2 update changed USB power management and audio device enumeration, which breaks detection for some USB headsets. The usual causes are USB selective suspend cutting power to the headset, a corrupted USB audio driver, or the headset being disabled in Sound settings. Trying a different USB port, disabling selective suspend, and reinstalling the USB audio driver resolves most cases."
  - q: "My USB headset is detected but has no sound. What's wrong?"
    a: "Detection without sound usually means the headset is not set as the default playback device, its volume is muted at the device level, or an app has seized exclusive control. Open mmsys.cpl, set the headset as both Default Device and Default Communication Device, check its Levels tab, and disable exclusive mode. Also check the headset's own inline mute and volume controls."
  - q: "The microphone on my USB headset doesn't work but audio does. Why?"
    a: "USB headsets expose separate playback and recording devices, and Windows treats them independently. The mic side is often disabled by default, blocked by privacy settings, or set to zero level. Check Settings > Privacy & security > Microphone for app permissions, enable the headset mic in mmsys.cpl's Recording tab, and raise its level. Some headsets also have a physical mic mute switch on the cable."
  - q: "Should I plug my USB headset into USB 2.0 or USB 3.0 ports?"
    a: "Try both. Some USB audio chipsets are pickier about USB 3.x ports and their power management, while others misbehave on USB 2.0 hubs. A direct port on the laptop (not through a hub or dock) is the most reliable test. If the headset works on one port type but not the other, use the working port and investigate that port's driver and power settings."
---

USB headsets should be the simple audio option — one plug, no drivers to hunt — but Windows 11 24H2 introduced USB and audio enumeration changes that broke that simplicity for many headsets. The symptoms vary: the headset does not appear at all, appears but produces no sound, the mic side is dead while audio works, or it disconnects randomly. This guide covers all four failure modes in order, since they share the same underlying systems.

Test methodically: after each fix, check both playback and recording, since USB headsets are two devices in one and fixes often heal only one side.

## Why this happens

- **USB selective suspend cutting power:** 24H2's aggressive USB power management suspends the headset's port, breaking detection.
- **Corrupted USB audio driver:** The generic USB audio class driver can corrupt during the 24H2 upgrade.
- **Headset disabled in Sound settings:** Windows sometimes disables the newly enumerated headset by default after the update.
- **Wrong default device:** Audio keeps routing to the laptop speakers because the headset was never set as default.
- **Exclusive mode seizure:** Communication apps grab exclusive control, muting everything else.
- **Privacy settings blocking the mic:** The recording side needs microphone permission like any other mic.
- **Faulty USB port or hub:** The port's own driver or power delivery fails the headset while other devices work.
- **Headset firmware incompatibility:** Older headset firmware clashing with 24H2's USB audio handling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Try different ports and check the basics

Eliminate the physical layer before touching software.

1. Unplug the headset and plug it directly into a different USB port on the laptop — avoid hubs and docks for testing.
2. Try both USB-A and USB-C ports if you have them, using an adapter if needed.
3. Check the headset's inline controls for a mute switch and volume wheel — set volume to mid-range and unmute.
4. Listen for the Windows device-connection sound when plugging in — no sound means no detection at all.
5. Test the headset on another computer or phone to confirm the headset itself works.

### Fix 2: Verify the headset in Sound settings

The classic Sound panel shows the true state of both headset sides.

1. Press Win + R, type `mmsys.cpl`, and press Enter.
2. On the Playback tab, right-click empty space and tick "Show Disabled Devices" and "Show Disconnected Devices".
3. If the USB headset appears greyed out, right-click it and choose Enable.
4. Right-click it and choose "Set as Default Device" and "Set as Default Communication Device".
5. Switch to the Recording tab and repeat: enable the headset microphone and set it as default.
6. Double-click each side and check the Levels tab — drag both to at least 70.

### Fix 3: Disable USB selective suspend

This is the highest-yield 24H2-specific fix for USB headsets.

1. Open Control Panel > Power Options > Change plan settings > Change advanced power settings.
2. Expand USB settings > USB selective suspend setting and set it to Disabled for both battery and plugged-in.
3. In Device Manager, expand Universal Serial Bus controllers.
4. For each "USB Root Hub" and "Generic USB Hub", open Properties > Power Management and uncheck "Allow the computer to turn off this device to save power".
5. Unplug and replug the headset, then test both audio and mic.
6. If your [USB devices show 'not recognized' errors](/articles/how-to-fix-usb-device-not-recognized-on-windows-11/) on the same ports, the port drivers need attention too.

### Fix 4: Reinstall the USB audio and controller drivers

Clear corrupted driver state on both the audio and USB sides.

1. In Device Manager, expand "Sound, video and game controllers" and "Audio inputs and outputs".
2. Uninstall the USB headset entries, ticking driver removal if offered.
3. Expand Universal Serial Bus controllers, right-click each USB Root Hub, and choose Uninstall device (do not tick driver removal here).
4. Restart the laptop — Windows rebuilds the USB stack and redetects the headset on boot.
5. Replug the headset after login and check `mmsys.cpl` for both sides.
6. Do not use third-party driver tools for USB audio — the Windows inbox driver is almost always the correct one.

### Fix 5: Fix exclusive mode and default format

Format fights and exclusive locks produce the "detected but silent" symptom.

1. In `mmsys.cpl`, double-click the headset on the Playback tab and go to Advanced.
2. Set the Default Format to 16-bit 48000 Hz — the safest baseline for USB headsets.
3. Uncheck both Exclusive Mode boxes.
4. Repeat on the Recording tab for the headset microphone.
5. Close all communication apps (Teams, Zoom, Discord), then reopen only your test app.
6. In the app's audio settings, explicitly select the USB headset rather than leaving it on Default.

### Fix 6: Check microphone privacy settings

The mic side of a USB headset is gated by Windows privacy controls.

1. Open Settings > Privacy & security > Microphone.
2. Confirm "Microphone access" and "Let apps access your microphone" are both On.
3. Scroll down and enable access for your specific communication app.
4. Test with Windows Sound Recorder — if it records from the headset mic, the system side is fine and the problem is app permissions.
5. Microsoft documents these privacy controls on their [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Update the chipset driver and headset firmware

The USB controller driver and the headset's own firmware both matter on 24H2.

1. Download the latest chipset driver for your laptop model from the manufacturer's support site — for example [Dell's official support](https://www.dell.com/support) — and install it.
2. Check the headset manufacturer's site or app for firmware updates for your specific model.
3. Install any available firmware update following the maker's instructions exactly.
4. After both updates, unplug the headset, restart, and replug it.
5. Retest detection, playback, and recording as three separate checks.

### Fix 8: Reset audio services and test a clean profile

When everything looks right but the headset still misbehaves, reset the audio subsystem.

1. Press Win + R, type `services.msc`, and restart "Windows Audio" and "Windows Audio Endpoint Builder".
2. Open an elevated Command Prompt and run `sfc /scannow` to repair system audio files.
3. Create a new local user account and test the headset there — a corrupted user audio profile can cause persistent per-user failures.
4. If it works in the new account, migrate to it or reset your audio settings; if it fails there too, the issue is system-wide.
5. As a final comparison, test the laptop's built-in audio path with our [Realtek audio guide](/articles/realtek-audio-driver-not-working-windows-11/) to determine whether the problem is USB-specific or audio-wide.

## Closing

USB headset problems on Windows 11 24H2 cluster around three things: USB power management suspending the device, enumeration leaving it disabled or non-default, and privacy or exclusive-mode settings silencing one side. Work the list in order, testing playback and recording separately each time, and you will isolate the layer at fault. Once it works, leave selective suspend disabled — it is the setting most likely to break USB audio again silently.
