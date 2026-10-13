---
title: "How to Fix a USB Headset Not Working — Step by Step"
slug: how-to-fix-usb-headset-not-working-step-by-step
date: 2026-09-14
categories: ["drivers"]
tags: ["usb headset not working", "headset no sound", "usb audio", "microphone not working", "windows audio fix"]
description: "USB headset not working on your laptop? Follow this step-by-step guide through default-device settings, USB power issues, and driver reinstalls to restore sound and mic."
thumbnail: "/images/thumbs/how-to-fix-usb-headset-not-working-step-by-step.webp"
faqs:
  - q: "Why does my USB headset show up but produce no sound?"
    a: "Almost always because Windows is routing audio to a different device. Open Sound settings and set the headset as the default output device, and check the classic Sound panel for a disabled or muted headset entry. If the volume meter moves but you hear nothing, check the headset's own inline mute/volume controls and try a different USB port — some ports do not deliver stable power."
  - q: "Why does my USB headset stop working after a few minutes?"
    a: "This is the signature of USB selective suspend: Windows powers down the 'idle' USB audio endpoint and the headset fails to wake. Disable USB selective suspend in the advanced power plan settings and uncheck power-saving on USB Root Hubs in Device Manager. Also connect directly to the laptop rather than through an unpowered hub, which worsens the problem."
  - q: "Do I need drivers for a USB headset?"
    a: "Basic USB headsets work with Windows' built-in usbaudio.sys driver and need nothing extra. Gaming headsets from SteelSeries, Logitech, Razer, or Corsair usually need the vendor's app for microphone, surround, EQ, and firmware updates — without it, the headset may appear but the mic stays dead. Check the manufacturer's site for a model-specific app if basic audio works but advanced features do not."
  - q: "My headset mic works but I hear no audio (or vice versa). Why?"
    a: "A USB headset exposes separate playback and recording endpoints, and Windows can default each to different devices. Set the headset as default on both the Output and Input sides of Sound settings. Also check per-app settings — browsers and games remember their own audio devices independently of the Windows default, so a game may still be sending audio to the laptop speakers."
---

A USB headset that produces no sound — or whose microphone is dead while the speakers work — is failing at one of three layers: Windows' audio device selection, the USB connection itself, or the headset's own driver/firmware. USB headsets are their own sound cards, so they bypass your laptop's Realtek audio entirely; that is why the laptop speakers can work perfectly while the headset stays silent.

The most common pattern is Windows routing audio to the wrong device after the headset is unplugged and replugged, or a USB power-saving feature suspending the headset's audio endpoint. Less often, the headset needs its vendor driver (common with gaming headsets) or the USB port is not delivering stable power.

Step through these in order — each step takes a couple of minutes and isolates one layer. If the headset is not detected as a USB device at all, pair this guide with our [USB device recognition walkthrough](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/); for laptop-speaker issues instead, see the [Realtek audio driver guide](/articles/realtek-audio-driver-not-working-windows-11/).

## Why this happens

- **Wrong default playback/recording device** — Windows keeps routing audio to speakers or another device after the headset reconnects.
- **Headset disabled in Sound settings** — The device can be disabled at the OS level and vanish from the device list.
- **USB selective suspend powering down the headset** — Windows suspends 'idle' USB audio devices; some headsets never wake properly.
- **Faulty USB port, hub, or cable** — Unpowered hubs and worn ports cause dropouts and failed enumeration.
- **Missing vendor driver or firmware** — Gaming headsets (SteelSeries, Logitech, Razer) often need their app/driver for full function.
- **Application-exclusive mode conflicts** — An app holding exclusive control of the headset blocks all other audio.
- **Corrupt USB audio driver stack** — The generic usbaudio.sys driver state can corrupt, especially after Windows updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the headset as the default device

In most 'no sound' cases the headset is fine — Windows is simply sending audio elsewhere. This is always step one.

1. Right-click the speaker icon in the taskbar and choose **Sound settings**.
2. Under Output, select your USB headset. Under Input, select its microphone.
3. Click the headset, then confirm the volume slider is up and not muted.
4. Play audio and watch the volume meter — movement means sound is routing correctly now.
5. If the headset does not appear, click **More sound settings** and check the Playback tab for disabled devices (right-click > Show Disabled Devices).

### Fix 2: Enable the headset if it is disabled

Headsets disabled in the classic Sound panel stay invisible in the new Settings UI, which confuses diagnosis.

1. Right-click the speaker icon > **Sounds** (or Sound settings > More sound settings).
2. In the Playback tab, right-click empty space and tick **Show Disabled Devices**.
3. If your headset appears greyed out, right-click it > **Enable**, then **Set as Default Device**.
4. Repeat on the Recording tab for the headset microphone.

### Fix 3: Try a different USB port — no hubs

Power and signal integrity matter for USB audio. This step eliminates the physical layer.

1. Unplug the headset from any USB hub or dock and connect it directly to the laptop.
2. Prefer a USB port on the opposite side of the machine (different internal hub).
3. Try both USB-A and USB-C ports if you have an adapter — avoid USB 2.0-only ports for headsets with high-power DACs.
4. If it works on one port but not another, the original port or hub is the problem, not the headset.

### Fix 4: Disable USB selective suspend

This power feature is the classic cause of headsets that work for a few minutes then die, or fail after sleep.

1. Open Control Panel > Power Options > Change plan settings > **Change advanced power settings**.
2. Expand **USB settings** > USB selective suspend setting and set it to **Disabled** for both battery and plugged-in.
3. In Device Manager, expand Universal Serial Bus controllers; for each **USB Root Hub**, open Properties > Power Management and uncheck 'Allow the computer to turn off this device'.
4. Restart and retest the headset over an extended session.

### Fix 5: Reinstall the USB audio device

A corrupt driver state for the headset's audio endpoint is fixed by a clean re-enumeration.

1. With the headset plugged in, open Device Manager.
2. Expand **Sound, video and game controllers**, right-click the headset entry, and choose **Uninstall device**.
3. Expand **Audio inputs and outputs** and uninstall the headset's speaker/mic entries too.
4. Unplug the headset, wait 10 seconds, plug it back in, and let Windows reinstall. Test both playback and mic.

### Fix 6: Install the vendor app and update firmware

Gaming and premium headsets often expose their mic, sidetone, and EQ only through the vendor's software, and firmware updates fix known USB issues.

1. Install the maker's app (SteelSeries GG, Logitech G Hub, Razer Synapse, Corsair iCUE).
2. Check for **firmware updates** for the headset inside the app and apply them.
3. In the app, verify the mic is not muted and sidetone/monitoring is configured sanely.
4. Microsoft's [Windows audio support pages](https://support.microsoft.com/en-us/windows) cover the OS-side audio settings if the app side is healthy.

### Fix 7: Disable exclusive mode for the headset

When one app grabs exclusive control, everything else goes silent — a common cause of 'headset works in Discord but nowhere else'.

1. Open Sound settings > More sound settings > Playback tab.
2. Double-click the headset > **Advanced** tab.
3. Uncheck **Allow applications to take exclusive control of this device**.
4. Click OK, restart your audio apps, and confirm system-wide audio works.

## Closing

USB headset failures are layer problems: device selection first, then USB power and ports, then drivers and vendor software. Because the headset is its own sound card, the laptop's internal audio is irrelevant to the diagnosis — keep your focus on the headset's own device entries, and most cases resolve by Fix 4 without ever touching the Realtek driver.
