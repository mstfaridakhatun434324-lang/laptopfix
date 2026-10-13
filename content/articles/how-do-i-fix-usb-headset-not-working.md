---
title: "USB Headset Not Working? Here's How to Fix It"
slug: how-do-i-fix-usb-headset-not-working
date: 2026-09-11
categories: ["drivers"]
tags: ["usb headset", "headset not working", "audio", "microphone"]
description: "USB headset not detected or no sound? Fix detection, driver, and default-device issues with this step-by-step laptop audio guide."
thumbnail: "/images/thumbs/how-do-i-fix-usb-headset-not-working.webp"
faqs:
  - q: "Why is my USB headset not showing up in sound settings?"
    a: "The most common causes are the headset not being fully enumerated by the USB bus, a corrupted USB audio driver, or USB selective suspend keeping the port asleep. Unplugging the headset, reinstalling the USB controller drivers, and disabling selective suspend resolve most detection failures. Also try a different USB port — some ports enumerate audio devices more reliably than others."
  - q: "My USB headset is detected but there is no sound — why?"
    a: "Detection without sound usually means the headset is not set as the default playback device, an application is outputting to a different device, or exclusive mode is misbehaving. Right-click the speaker icon, open Sound settings, and explicitly set the headset as the default for both output and input, then test with the built-in test tone."
  - q: "Why does my USB headset microphone not work while the speakers do?"
    a: "Windows treats the headset's playback and recording sides as separate devices with separate default assignments and privacy permissions. Check Sound settings > Input to confirm the headset mic is the default recording device, and check Settings > Privacy & security > Microphone to confirm apps are allowed to use it."
  - q: "Can a USB headset conflict with my laptop's built-in audio?"
    a: "Yes, particularly with manufacturer audio suites like Waves MaxxAudio or Dolby that try to process all audio. These can misroute or degrade USB headset audio. Disabling audio enhancements for the USB headset device in its Properties, and ensuring the headset is the explicit default device, usually resolves the conflict."
---

USB headsets should be the simplest audio setup on a laptop — plug in, and they work. When they do not, the problem sits at the intersection of USB and audio, which gives you twice the usual suspects: USB enumeration, USB power management, audio drivers, default-device routing, and privacy permissions for the microphone. The fix order below separates these layers so you test each one cleanly.

Start by defining the exact symptom, because "not working" covers three different failures: not detected at all (a USB problem), detected but silent (an audio routing problem), and speakers work but the mic does not (a recording/privacy problem). Each has its own fix path below. For general USB detection issues, our [USB device not recognized guide](/articles/how-to-fix-usb-device-not-recognized/) covers the bus-level fixes, and for Bluetooth audio trouble, see the [Bluetooth on Windows 11 guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/).

## Why this happens

- **USB enumeration failure.** The headset never completes the USB handshake, so Windows never creates the audio device.
- **USB selective suspend.** Power management puts the port to sleep and the headset never wakes properly.
- **Wrong default device.** Windows keeps routing audio to the speakers even though the headset is connected.
- **Corrupted USB audio driver.** The generic USB audio driver (usbaudio.sys) can corrupt and fail to start the headset's audio endpoints.
- **Microphone privacy settings.** Windows privacy controls can block all apps from using the headset mic while playback works fine.
- **Manufacturer audio suite conflicts.** Dolby, Waves MaxxAudio, and similar suites can hijack or degrade USB headset audio.
- **Faulty headset or cable.** The headset's own USB cable or DAC can fail, especially at the strain-relief near the plug.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the failure type

Define the symptom before touching settings.

1. Plug in the headset and open **Settings > System > Sound**. Check whether the headset appears under **Output** and under **Input**.
2. If it appears in neither: you have a detection problem — focus on Fixes 2–4.
3. If it appears but produces no sound: a routing problem — jump to Fix 5, then come back if needed.
4. If output works but the mic does not: a recording problem — go to Fix 6.

### Fix 2: Test ports, and rule out the headset hardware

Quick physical isolation.

1. Unplug the headset, wait 10 seconds, and plug it into a **different USB port** — preferably a port directly on the laptop, not a hub.
2. If the headset has a detachable cable, try a different cable.
3. Test the headset on another computer or phone (with an adapter if needed). If it fails everywhere, the headset itself is dead — no software fix will help.
4. Listen for the Windows device-connection sound when plugging in. No sound at all suggests a USB-level failure; the connection sound with no audio device suggests a driver failure.

### Fix 3: Reinstall USB controllers and disable selective suspend

Fix the USB layer underneath the audio.

1. Open Device Manager, expand **Universal Serial Bus controllers**, and uninstall every **USB Root Hub** and **USB Host Controller** (no driver-deletion checkboxes).
2. Restart the laptop and let Windows reinstall the controllers.
3. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **USB settings**, and set **USB selective suspend** to **Disabled**.
4. Reconnect the headset and check Sound settings for its appearance.

### Fix 4: Reinstall the USB audio device driver

Target the headset's audio driver specifically.

1. With the headset plugged in, open Device Manager and expand **Sound, video and game controllers** and **Audio inputs and outputs**.
2. Right-click the headset entries and choose **Uninstall device** (check **Attempt to remove the driver** if offered).
3. Unplug the headset, restart, then plug it back in and let Windows install fresh drivers.
4. If Windows fails to find a driver, check the headset manufacturer's site for a dedicated driver or firmware updater — gaming headsets from major brands often have one.

### Fix 5: Set the headset as the explicit default device

Windows does not always switch automatically.

1. Right-click the speaker icon, choose **Sound settings**, and under **Output**, select the USB headset explicitly — do not rely on it auto-switching.
2. Click the arrow next to the headset and run the **Test** tone. If the tone plays, the device works and the issue was routing.
3. Open the headset's **Properties**, go to the **Enhancements** tab, and check **Disable all enhancements** — manufacturer suites degrading USB audio is common.
4. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**, which fixes apps that hijack the headset.

### Fix 6: Fix the microphone side

Playback and recording are separate devices with separate permissions.

1. In **Sound settings**, scroll to **Input** and select the headset microphone explicitly. Speak and watch the input volume meter move.
2. Go to **Settings > Privacy & security > Microphone** and confirm **Microphone access** is on and **Let desktop apps access your microphone** is enabled.
3. In **Control Panel > Sound > Recording tab**, right-click the headset mic, choose **Properties > Levels**, and make sure it is not muted or set to zero.
4. Test in two different apps (e.g., Voice Recorder and a browser mic test) — if it works in one but not the other, the problem is that app's permission, not the headset.

### Fix 7: Update firmware and check for conflicts

The last software layer.

1. Check the headset manufacturer's app or website for a **firmware update** — headset firmware bugs cause exactly these intermittent failures.
2. Temporarily disable third-party audio software (Dolby Access, Waves MaxxAudio, Voicemeeter, virtual audio cables) and retest — these intercept the audio path.
3. As a final isolation, test the headset in a **clean boot** (**msconfig > Services > Hide all Microsoft services > Disable all**) to rule out third-party interference. For persistent system-level audio trouble, [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) documents the built-in audio troubleshooters.

## Closing

USB headset failures split cleanly into USB problems (not detected), routing problems (detected but silent), and permission problems (mic dead) — and identifying which one you have at Fix 1 saves you from applying the wrong fixes. The USB controller reinstall plus selective-suspend disable handles the detection side, explicit default-device assignment handles the routing side, and the privacy settings handle the mic side. When all three layers check out and the headset still fails on multiple computers, you have your answer: it is the hardware.
