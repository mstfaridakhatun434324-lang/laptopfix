---
title: "Laptop Speakers Not Working? How to Fix Them"
slug: how-to-fix-laptop-speakers-not-working-youtube
date: 2026-09-06
categories: ["drivers"]
tags: ["laptop speakers not working", "no sound laptop", "speakers no audio", "windows 11 sound fix"]
description: "No sound from your laptop speakers? Fix silent speakers with output device checks, Realtek driver reinstalls, and Windows audio service repairs."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working-youtube.webp"
faqs:
  - q: "Why do my laptop speakers show as working but produce no sound?"
    a: "When the volume mixer shows activity but nothing comes out, the audio is routing to the wrong device, the speakers are disabled at a lower level, or the driver is sending silence. Check that the Realtek speakers are the default output, disable audio enhancements, and reinstall the audio driver — in that order."
  - q: "Why do headphones work but laptop speakers do not?"
    a: "That split means the audio subsystem is healthy and the problem is specific to the speaker path: the speaker device disabled, a stuck headphone-jack detection muting the speakers, or a failed speaker driver component. Reinstalling the Realtek driver and checking the jack for debris address the software and mechanical causes."
  - q: "Can Windows Update break laptop speakers?"
    a: "Yes — updates frequently replace the laptop maker's tuned audio driver with a generic one that does not drive the speakers correctly, or break the enhancement pipeline. Reinstalling the audio driver from the laptop maker's support page for your exact model is the standard fix."
  - q: "Do I need to restart the Windows Audio service?"
    a: "It is worth trying: a hung Windows Audio service silences everything. Restart 'Windows Audio' and 'Windows Audio Endpoint Builder' in services.msc. If sound returns, the service had crashed; if the problem recurs often, a driver reinstall usually stops the crashes."
---

Silent laptop speakers are maddening because everything looks right — the volume icon is normal, the mixer dances, YouTube plays — but no sound comes out. The audio pipeline has several stages where sound can silently die: the output routing, the driver, the Windows Audio service, and the enhancement layer.

The diagnosis writes itself once you check the splits: headphones work but speakers do not, or nothing works at all. The fixes below start with routing — the most common cause — then repair the driver and services, and finish with the hardware verdict.

## Why this happens

- **Wrong default output device** — audio routing to a disconnected HDMI or Bluetooth device.
- **Speakers disabled** in the Sound control panel.
- **Corrupted or generic audio driver** after a Windows update.
- **Windows Audio service hung or crashed**.
- **Broken audio enhancements** muting the output pipeline.
- **Stuck headphone-jack detection** keeping the speakers muted.
- **Failed speaker hardware** — blown speakers or a disconnected cable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the correct default output

Click the volume icon and check which output is selected in Quick Settings — Windows loves switching to a disconnected monitor's HDMI audio. Open Settings > System > Sound and set the laptop's Realtek speakers as the default output. Play a test sound and watch the volume bar; if the bar moves on the wrong device, routing was the whole problem.

1. Click the volume icon and note the selected output.
2. Open Settings > System > Sound.
3. Set the internal speakers as the default output.
4. Play audio and confirm sound.

### Fix 2: Enable the speakers in the Sound control panel

Open the classic Sound panel (search 'Change system sounds'), go to Playback, right-click empty space, and tick 'Show Disabled Devices'. If the speakers appear greyed out, right-click and enable them. Also check the speaker Properties > Levels tab — a muted or zeroed level here silences everything regardless of the taskbar volume.

1. Open the Sound control panel > Playback tab.
2. Show disabled devices and enable the speakers.
3. Check Properties > Levels for mutes or zeroed sliders.
4. Set as default and test.

### Fix 3: Restart the Windows Audio services

Open services.msc and restart 'Windows Audio' and 'Windows Audio Endpoint Builder' (restart the Endpoint Builder first, then Windows Audio). If sound returns immediately, a hung service was the cause. Microsoft covers audio service troubleshooting in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open services.msc.
2. Restart 'Windows Audio Endpoint Builder'.
3. Restart 'Windows Audio'.
4. Test sound immediately.

### Fix 4: Reinstall the audio driver

Download the audio driver from the laptop maker's support page for your exact model. In Device Manager, uninstall the Realtek (or equivalent) audio device under Sound, video and game controllers, deleting the driver software. Reboot, install the maker's package, and reboot again. This fixes the generic-driver swaps that Windows Update performs. For crackling rather than silence, the [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2/) targets that specific symptom.

1. Download the audio driver from the laptop maker.
2. Uninstall the audio device in Device Manager, deleting its driver.
3. Reboot and install the maker's driver package.
4. Reboot again and test the speakers.

### Fix 5: Disable audio enhancements

In the speaker Properties > Enhancements tab, tick 'Disable all enhancements'. The enhancement pipeline — equalizers, loudness, virtual surround — can break and output silence after driver updates. If sound returns with enhancements off, keep them off or reinstall the driver to repair the pipeline properly.

1. Open speaker Properties > Enhancements tab.
2. Tick 'Disable all enhancements'.
3. Test audio.
4. Reinstall the driver if this was the fix.

### Fix 6: Check the headphone jack

A stuck headphone-jack switch tells Windows headphones are plugged in forever, muting the speakers. Plug headphones in and out firmly several times to free the mechanical switch. Shine a light into the jack and remove any lint with a wooden toothpick — never metal. If the jack is damaged, disabling jack detection in the Realtek control panel is a software workaround.

1. Plug and unplug headphones firmly several times.
2. Inspect the jack for lint or debris and clean it.
3. Test the speakers after each attempt.
4. Disable jack detection in the audio control panel as a workaround.

### Fix 7: Test for dead speakers

Boot a Linux live USB and play audio. Sound in Linux means Windows software is at fault — keep working the driver side. Silence everywhere, with headphones working, means the speakers or their cable failed. Internal speakers are inexpensive parts but require opening the laptop; get a quote and consider a good Bluetooth speaker as the pragmatic alternative.

1. Boot a Linux live USB and test speaker audio.
2. Sound in Linux = Windows problem; silence = hardware.
3. Confirm headphones work to isolate the speaker path.
4. Repair or replace with external speakers.

### Fix 8: Test in a new user profile

Corrupted per-profile audio settings can silence the speakers for one Windows account while others work fine. Create a new local user account, sign into it, and test audio there. If sound works in the new profile, your main profile's audio configuration is corrupt — you can migrate to the new profile or reset audio settings in the old one. If neither profile has sound, the problem is system-wide and the driver and service fixes above are the right battleground.

1. Create a new local user via Settings > Accounts > Other users.
2. Sign into the new account and play audio.
3. Sound in the new profile means profile-level corruption.
4. No sound anywhere means a system-wide driver or service fault.

## Closing

Silent speakers are a routing or driver problem far more often than dead hardware: the default-output check and the driver reinstall from the laptop maker resolve the great majority. The headphone-jack check catches the sneaky mechanical cause, and the Linux test gives you the final hardware verdict. Work the pipeline in order — routing, services, driver, jack, hardware — and the sound comes back. Since the microphone shares the same Realtek chip on most laptops, [Realtek microphone fixes](/articles/how-to-fix-realtek-microphone-not-working-on-windows-11/) are worth a look if the mic misbehaves too.
