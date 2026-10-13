---
title: "Troubleshooting a USB Headset That Is Not Working"
slug: usb-headset-not-working-troubleshooting
date: 2026-10-09
categories: ["drivers"]
tags: ["usb headset", "headset not working", "usb audio", "microphone not working", "windows 11"]
description: "USB headset not working — no sound, dead mic, or not detected at all? Troubleshoot the USB audio chain from port to driver to app settings."
thumbnail: "/images/thumbs/usb-headset-not-working-troubleshooting.webp"
faqs:
  - q: "Why is my USB headset not showing up in sound settings?"
    a: "If the headset does not appear as a playback or recording device at all, Windows is not enumerating it as an audio device. Check Device Manager under Sound and Universal Serial Bus controllers for the headset or an unknown device — its location tells you whether USB sees it but audio does not, or USB does not see it either. Try a different USB port first, because underpowered or damaged ports commonly cause exactly this symptom with USB audio devices."
  - q: "Why does my USB headset work for sound but the microphone does not?"
    a: "A USB headset presents itself to Windows as two separate devices — a playback device and a recording device — and they can fail independently. Check Settings, then System, then Sound, and look at the input section separately from output. Also verify app permissions under Privacy and security, then Microphone, since Windows blocks microphone access independently of speaker output. Many 'dead mic' cases are just the wrong input device selected in the app."
  - q: "Do USB headsets need drivers?"
    a: "Most USB headsets use the standard USB Audio Class driver built into Windows and need no manufacturer driver. However, headsets with surround sound, sidetone controls, or EQ features often need the manufacturer's software for full functionality — the basic audio works without it, but the extras do not. If your headset has a companion app, install it after confirming basic audio works, so you can tell which layer any problem belongs to."
  - q: "Why does my USB headset disconnect randomly?"
    a: "Random disconnections are almost always USB power management or a marginal connection. Windows USB selective suspend powers down idle ports, which resets the audio stream and sounds like a disconnect. A loose connector, a failing cable, or an underpowered hub causes the same symptom. Disable selective suspend first, then test the headset plugged directly into the laptop with no hub or extension cable in between."
---

A USB headset that is not working sits at the intersection of two systems — USB and audio — which means twice the usual places for things to break. The headset might not be detected at all, it might play sound but record nothing, or it might cut in and out. Each symptom points to a different layer, and this guide helps you read those symptoms correctly instead of reinstalling drivers at random.

USB headsets are actually simpler than they feel. They are standard USB audio devices: the headset contains its own tiny sound card, and Windows talks to it over USB. Troubleshooting means verifying each link in that chain — the USB connection, the audio device enumeration, the driver, and the app configuration — in order.

## Why this happens

- **Underpowered or faulty USB port:** USB headsets need stable power and clean data. A damaged port or an overloaded hub causes detection failures and dropouts.
- **USB selective suspend resetting the device:** Windows powers down the port during quiet moments, and the headset re-enumerates — or fails to — producing disconnects.
- **Wrong default device selected:** Windows keeps the old default when you plug in the headset. Sound goes to the speakers while you wonder why the headset is "not working."
- **Microphone privacy blocked:** Windows treats mic access separately. The headset's speakers can work perfectly while the mic is blocked by privacy settings.
- **Corrupted USB audio driver:** The USB Audio Class driver or the headset's custom driver can corrupt, especially after Windows updates.
- **App-level device selection:** Zoom, Teams, and Discord each remember their own audio devices and do not always follow the Windows default when you plug in the headset.
- **Conflicting audio software:** Manufacturer audio utilities and virtual audio devices (Voicemeeter, OBS) can hijack the headset's audio stream.
- **Failing headset hardware:** Frayed cables at the earcup joint and worn USB connectors cause intermittent failures that look exactly like driver problems.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify USB detection in Device Manager

Find out whether the problem is USB-level or audio-level — the fixes diverge completely from here.

1. Plug the headset in and open **Device Manager**. Check **Audio inputs and outputs** for the headset name.
2. If it is missing there, check **Sound, video and game controllers** and **Universal Serial Bus controllers** for the headset or an **Unknown USB Device**.
3. Unknown USB Device under USB controllers means USB sees something but cannot identify it — a port, cable, or headset hardware issue. Continue with Fix 2.
4. Headset present everywhere but silent means the audio layer is the problem — skip to Fix 4. Port-level detection issues overlap with our [USB device not recognized guide](/articles/what-to-do-if-usb-device-not-recognized/).

### Fix 2: Fix the physical USB connection

USB audio is unforgiving of marginal connections.

1. Plug the headset directly into the laptop — no hubs, no extension cables, no front-panel ports. Test every port.
2. If the headset has a detachable cable, reseat both ends firmly. Try a different cable if one is available.
3. For USB-C connections via an adapter, try a different adapter. Cheap adapters are a notorious source of USB audio problems.
4. Listen for the Windows device-connection sound when plugging in. No sound at all means USB enumeration failed; a sound followed by silence means enumeration succeeded and the problem is audio-layer.

### Fix 3: Disable USB selective suspend

The classic fix for headsets that disconnect or go silent after idle periods.

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Set **USB settings → USB selective suspend setting** to **Disabled** for both battery and plugged in.
3. In **Device Manager → Universal Serial Bus controllers**, open each **USB Root Hub → Properties → Power Management** and uncheck **Allow the computer to turn off this device to save power**.
4. Restart and test through a full workday. If random disconnects stop, power management was the cause — a pattern also seen with other USB audio gear.

### Fix 4: Set the headset as the default device

The most common "not working" report is really a routing problem.

1. Right-click the speaker icon → **Sound settings**. Under **Output**, select the headset. Under **Input**, select the headset's microphone — separately.
2. Click the arrow next to each device name to open its properties and confirm the volume is up and the device is enabled.
3. In the legacy **Control Panel → Sound** tabs, set the headset as **Default Device** (not just Default Communication Device) on both Playback and Recording tabs.
4. Test with the **Test** button in the Recording tab — speak and watch the green level meter. Movement means the mic path works and the problem is app configuration (Fix 6). Broader audio-driver issues are covered in our [Realtek audio guide](/articles/realtek-audio-driver-not-working-windows-11/).

### Fix 5: Fix microphone privacy and levels

For the "I can hear but nobody hears me" variant.

1. Go to **Settings → Privacy & security → Microphone**. Ensure **Microphone access** and **Let apps access your microphone** are on, plus **Let desktop apps access your microphone**.
2. Confirm your calling app is allowed in the list. Restart the app after changing permissions.
3. In **Sound settings → Input → headset mic → Properties**, check the input volume slider — Windows sometimes sets USB mics to near-zero after driver changes.
4. In the app itself (Zoom: **Settings → Audio**; Teams: **Settings → Devices**), explicitly select the headset microphone rather than leaving it on default.

### Fix 6: Reinstall the USB audio driver

When the headset is detected but produces no sound or distorted sound.

1. In **Device Manager → Audio inputs and outputs**, right-click the headset and choose **Uninstall device**.
2. Also check **Sound, video and game controllers** for a headset entry and uninstall it the same way.
3. Unplug the headset, restart, then plug it back in. Windows installs a fresh USB Audio Class driver.
4. If the manufacturer provides a driver or companion app (for surround, EQ, or sidetone), install it only after basic audio works. If generic audio drivers keep breaking, [Microsoft's support pages](https://support.microsoft.com/en-us/windows) document the official audio troubleshooting flow, and our [audio driver crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) covers persistent cases.

### Fix 7: Eliminate software conflicts and test the hardware

The final layer: conflicting software and the headset itself.

1. Temporarily disable or uninstall virtual audio software (Voicemeeter, OBS virtual devices, Discord's Krisp processing) and manufacturer audio utilities, then retest.
2. In **Sound settings**, disable **Enhance audio** for the headset — processing effects can conflict with the headset's internal DSP.
3. Test the headset on another computer or a phone with an adapter. Works elsewhere means your laptop's USB/audio stack is the problem; fails elsewhere means the headset is dying.
4. Check the cable carefully — the most common hardware failure point is where the cable enters the earcup or the USB plug. Intermittent cutouts when the cable moves confirm a hardware fault, and no driver fix will help.

## Closing

USB headset troubleshooting is really about locating which of the two systems — USB or audio — is failing, because the fixes live in completely different places. Device Manager tells you in thirty seconds. From there it is usually port power, default-device routing, or mic privacy — three settings that resolve the large majority of "not working" headsets without a single driver download.
