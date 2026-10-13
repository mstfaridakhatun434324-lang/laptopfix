---
title: "Laptop Microphone Not Working? How to Fix It"
slug: "how-to-fix-microphone-not-working-on-laptop"
date: "2026-09-29"
categories: ["drivers"]
tags: ["microphone not working", "mic fix", "audio input", "windows 11"]
description: "Laptop mic not picking up sound in calls or recordings? Fix privacy blocks, driver issues, and wrong-device routing with this ordered guide."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop.webp"
faqs:
  - q: "Why can nobody hear me on calls but my mic tests fine?"
    a: "If the Settings input-level bar moves but apps hear nothing, the problem is app-level: per-app microphone permissions in Privacy settings, the wrong mic selected inside the app, or the app's own mute. Enable the app in Settings, Privacy and security, Microphone, and set the mic explicitly in the app's audio settings."
  - q: "How do I know if my laptop mic is muted?"
    a: "Check four layers: the taskbar quick-settings mic icon, the mic's properties in Sound settings, the physical mic-mute key (often F4 with an LED on business laptops), and the mute button inside your calling app. Any single layer muted silences the mic everywhere."
  - q: "Can a Windows update break my microphone?"
    a: "Yes. Feature updates can reset microphone privacy toggles, replace the audio driver with a version that mishandles the capture path, or change the default input device. Recheck privacy settings and the default mic selection after every major update, and reinstall the vendor audio driver if the capture path broke."
  - q: "Why does my mic work in one app but not another?"
    a: "Each app has independent microphone permission and its own device selection. Grant the app access in Settings, Privacy and security, Microphone, set the correct mic inside the app's audio settings, and disable exclusive mode so one app cannot monopolize the microphone."
---

Laptop microphone failures have a cruel signature: everything looks fine — the mic is listed, levels seem configured — but nobody can hear you, or recordings capture silence. The cause is usually one of four things: Windows privacy settings blocking the mic, the wrong input device selected, the mic muted at some hidden layer, or a corrupted audio driver. Actual microphone hardware failure is uncommon.

The fastest diagnostic is the Settings sound test: open Settings, System, Sound, scroll to Input, select your microphone, and speak. If the input volume bar moves, the mic hardware and driver work — your problem is app permissions or app settings. If the bar stays flat, the problem is at the system level: privacy, device selection, mute, or driver.

Run that test first, then follow the fixes matching your result. For Realtek-specific microphone issues, our [Realtek mic guide](/articles/how-do-i-fix-realtek-microphone-not-working/) goes deeper on that driver's quirks.

## Why this happens

- ****Microphone privacy settings blocking access**:** Windows 11 gates mic access at system and per-app levels. Updates can reset these, silently muting every app.
- ****Wrong input device selected**:** With USB headsets, webcams, and monitors all offering microphones, Windows often defaults to the wrong one.
- ****Microphone muted at a hidden layer**:** Mute exists in the taskbar quick settings, the Sound panel device properties, app settings, and sometimes a physical mute key — any one silences everything.
- ****Corrupted audio driver**:** The same Realtek/Intel driver that handles output handles input; its corruption kills the mic path while speakers keep working.
- ****App-specific permission or settings**:** Zoom, Teams, and browsers each have their own mic selection and permission — system-level health does not guarantee app-level access.
- ****Exclusive mode conflicts**:** An app holding the mic in exclusive mode blocks every other app from capturing.
- ****Physical mic mute switch or Fn key**:** Many business laptops have a dedicated mic-mute key (often F4 with an LED) that is easy to hit accidentally.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Input Level Test

Open Settings, System, Sound, and under Input select your microphone and speak normally. Watch the input volume bar: movement means the mic, driver, and Windows capture path all work — skip to the app-permission fixes. No movement means a system-level block — continue with the privacy and device fixes below.

While here, click the arrow next to the mic for its properties and confirm the input volume slider is up (not zero) and the device is not disabled. This single screen diagnoses half of all mic failures in thirty seconds.

1. 1. Open Settings, System, Sound, Input.
2. 2. Select your microphone and speak.
3. 3. Bar moves: the problem is app-level — check permissions.
4. 4. Bar flat: continue with system-level fixes below.
5. 5. Confirm the input volume slider is raised.

### Fix 2: Check Privacy Settings Thoroughly

Open Settings, Privacy and security, Microphone. Turn on 'Microphone access' and 'Let apps access your microphone,' then enable each app that needs the mic. Scroll to 'Let desktop apps access your microphone' and make sure it is on — Zoom, Teams, and most conferencing tools are desktop apps governed by this separate toggle.

This is the fix for 'mic works in Settings test but no app hears me' more often than anything else. Recheck after every Windows feature update, which can reset these toggles silently.

1. 1. Open Settings, Privacy and security, Microphone.
2. 2. Enable microphone access globally and per app.
3. 3. Enable the desktop-apps microphone toggle.
4. 4. Retest with the Settings input level bar.
5. 5. Test in your actual calling app.

### Fix 3: Select the Correct Input Device Everywhere

In Settings, System, Sound, set the Input device explicitly to your laptop's internal microphone (usually 'Microphone Array'). Then open each calling app's audio settings — Zoom, Teams, Discord — and set the microphone there too, because apps remember their own device selections independently of Windows.

Also check the classic Sound panel's Recording tab: the correct mic should show green bars when you speak and be set as default. Disable microphone devices you never use (monitor mics, old headset entries) to stop Windows from switching to them.

1. 1. Set the internal mic array as Input in Sound settings.
2. 2. Set the microphone explicitly inside each calling app.
3. 3. In the Recording tab, confirm green bars on the right device.
4. 4. Set it as the default device.
5. 5. Disable unused microphone entries.

### Fix 4: Hunt Down Every Mute Layer

Check the taskbar quick settings for a muted mic icon. Open the mic's properties in Sound settings and confirm it is not muted or at zero. Press the physical mic-mute key (common on ThinkPads and EliteBooks — look for the LED) to toggle it. Check the calling app's own mute button and its audio settings for a software mute.

Mute layers stack silently: the number of 'mic not working' cases caused by a single overlooked mute toggle is enormous. Check all four layers — Windows, device properties, physical key, app — before concluding anything is broken.

1. 1. Check the taskbar quick-settings mic mute.
2. 2. Verify the device is not muted in its Sound properties.
3. 3. Toggle the physical mic-mute key and watch its LED.
4. 4. Check the calling app's mute button and audio settings.
5. 5. Retest the input level bar after each check.

### Fix 5: Reinstall the Audio Driver

In Device Manager, expand Sound, video and game controllers, right-click the audio device, and choose Uninstall device with driver deletion. Restart, then install the audio driver from your laptop maker's support site. The microphone capture path runs through this same driver — its corruption kills mic input while leaving output untouched.

After reinstalling, rerun the Settings input-level test before opening any apps. If the bar moves now, the driver was the problem. For deeper Realtek issues, see our [Realtek microphone troubleshooting](/articles/how-to-fix-realtek-microphone-not-working-in-windows-11-24h2/). Microsoft documents audio driver reinstallation in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. Uninstall the audio device in Device Manager with driver deletion.
2. 2. Restart the laptop.
3. 3. Install the vendor audio driver from the maker's site.
4. 4. Rerun the Settings input-level test.
5. 5. Reconfigure app mic selections afterward.

### Fix 6: Disable Exclusive Mode and Enhancements

In the classic Sound panel, open the microphone's properties. On the Advanced tab, uncheck both exclusive-mode boxes — exclusive mode lets one app monopolize the mic and silently block others. On the Enhancements tab (if present), disable all enhancements, since mic DSP can crash the capture path on some drivers.

This fix targets the pattern where the mic works in exactly one app but no others, or works until a specific app opens. It is a small settings change with an outsized effect on multi-app mic conflicts.

1. 1. Open the mic's properties in the classic Sound panel.
2. 2. Uncheck both exclusive-mode boxes on the Advanced tab.
3. 3. Disable all enhancements on the Enhancements tab.
4. 4. Apply and restart your calling apps.
5. 5. Test the mic across multiple apps.

## Closing

Microphone failures are routing and permission problems far more often than hardware faults: the Settings input-level test tells you in seconds whether the mic itself works, and from there it is privacy toggles, device selection, mute layers, or the audio driver. Work that sequence and the mic comes back.
