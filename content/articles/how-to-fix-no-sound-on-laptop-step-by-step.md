---
title: "No Sound on Laptop? A Step-by-Step Fix for Windows 10 and 11"
slug: how-to-fix-no-sound-on-laptop-step-by-step
date: "2026-09-02"
categories: ["drivers"]
tags: ["no sound", "audio fix", "windows audio", "sound troubleshooting", "silent laptop"]
description: "Complete silence from your laptop? Follow this step-by-step guide to diagnose exactly where audio breaks and fix no sound on Windows 10 and 11."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-step-by-step.webp"
faqs:
- q: "How do I figure out where my laptop sound is breaking?"
  a: "Start with the symptom pattern. No output device listed at all points to a driver problem. A device listed but silent points to routing, volume, or service issues. Sound in some apps but not others points to the volume mixer or app settings. Matching your symptom to one of these three patterns tells you which section of this guide to focus on, instead of trying fixes at random."
- q: "Why is there no sound even though nothing is muted?"
  a: "Mute is only one link in the chain. The audio may be routed to a disconnected device like an unplugged HDMI monitor, the Windows Audio service may have stalled, or the driver may be corrupted — all while every visible mute indicator shows unmuted. Work through output device selection, the audio troubleshooter, and the service restart in this guide; one of them almost always explains the silent-but-unmuted mystery."
- q: "Can headphones break my laptop speakers' sound?"
  a: "They can appear to. If the headphone jack's detection switch sticks, the driver believes headphones are still connected and keeps the speakers muted after unplugging. Manually selecting the speakers as the default device usually overrides it. Plugging and unplugging the headphones firmly a few times can also free a stuck switch, and a driver reinstall recalibrates jack detection."
- q: "Is it worth using Windows' built-in audio troubleshooter?"
  a: "Yes, as an early step. It automatically checks device state, default device selection, driver health, and service status, and it applies safe fixes on its own. It will not fix deep driver corruption, but it resolves misconfiguration quickly and its report sometimes pinpoints the fault — for example, identifying that the audio service is stopped — saving you manual diagnosis time."
---

Total silence from a laptop is disorienting because there is no error to google — just videos playing mute and a volume slider that moves as if everything works. The instinct is to start changing settings at random, which occasionally works by luck and usually wastes an hour. There is a better approach: diagnose first, using the symptom pattern to aim at the right link in the audio chain.

Audio travels a fixed path on every Windows laptop: application, volume mixer, Windows audio services, audio driver, output device, and finally the physical speakers or jack. Each fix in this guide targets exactly one link, in the order that finds the break fastest. You stop the moment sound returns — no need to finish the list.

Before starting, note which of these matches you: no playback device listed anywhere, a device listed but silent, or sound in some apps only. That pattern is your compass for the steps below.

## Why this happens

- **Audio routed to a phantom device**: Unplugged HDMI monitors and forgotten Bluetooth speakers keep receiving "sound" that goes nowhere.
- **Windows Audio service stalled**: The mixing services hang after updates or sleep, silencing every application at once.
- **Corrupted or replaced audio driver**: Updates swap the vendor driver for a generic one that cannot drive the output hardware.
- **Per-app mute in the volume mixer**: Individual applications can be muted while the system volume looks normal.
- **Broken enhancement processing**: A corrupted driver enhancement chain produces silence instead of merely poor quality.
- **Exclusive mode hijack**: One application can seize exclusive control of the audio device and block everything else.
- **Hardware failure**: Failed speakers or a damaged audio codec are the least common cause but the hardest to fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Match your symptom to the fault

Two minutes of diagnosis here saves twenty of random fixes. Open Sound settings (right-click the speaker icon) and observe: is any output device listed? Does the volume meter move when audio plays? Does sound work in any app? Your answers aim the rest of the guide — no device means driver trouble (skip to Fix 5), a silent listed device means routing or services (Fixes 2–4), app-specific silence means the mixer (Fix 2).

1. Right-click the speaker icon and open Sound settings.
2. Check whether any output device appears in the list.
3. Play audio and watch the device's volume meter for movement.
4. Test two different apps (a browser video and a system sound).
5. Note your pattern: no device, silent device, or app-specific silence.

### Fix 2: Correct the output device and volume mixer

The most common "no sound" is sound going somewhere else. Windows remembers output devices aggressively — that monitor you unplugged last week may still be the default. Meanwhile the volume mixer can mute a single application while everything else looks healthy. Both checks take a minute and resolve a large share of total-silence complaints.

1. In Sound settings, set the Output device explicitly to your speakers or headphones — not a monitor or Bluetooth device.
2. Click the volume icon and confirm it is unmuted and raised.
3. Right-click the speaker icon, open Volume Mixer, and unmute any muted applications.
4. In "More sound settings," on the Playback tab, right-click your device and choose "Test."
5. If the test tone plays, the fault was routing — if not, continue.

### Fix 3: Run the audio troubleshooter

With routing confirmed, let Windows audit the chain automatically. The troubleshooter checks device state, driver health, default selection, and service status in one pass, and applies its own safe fixes. It is particularly good at catching stopped services and misconfigured defaults that manual checks overlook.

1. Go to Settings, System, Sound, Advanced, and run "Troubleshoot common sound problems."
2. Select the silent output device when prompted.
3. Let the scan finish and apply any recommended fix.
4. Restart if the troubleshooter requests it.
5. Retest with the same audio you used in Fix 1.

### Fix 4: Restart the Windows Audio services

When the device is present, unmuted, correctly routed, and still silent across all apps, the mixing services are the likely break. Windows Audio and the Audio Endpoint Builder sit between every application and the driver; when they stall, nothing gets through. Restarting them rebuilds the entire audio graph without touching drivers or settings.

1. Press Win + R, type `services.msc`, and press Enter.
2. Right-click "Windows Audio" and choose Restart (start it if stopped).
3. Right-click "Windows Audio Endpoint Builder" and do the same.
4. Set both to Automatic startup type.
5. Play audio immediately — restored sound confirms the services were hung.

### Fix 5: Reinstall the audio driver

No output device listed, a device with a warning icon, or silence surviving all the above means the driver is corrupt or mismatched. This is the heavy fix that resolves most stubborn cases: remove the broken driver completely and install the manufacturer's package. Specific driver versions are also available from Microsoft's [update catalog](https://www.catalog.update.microsoft.com/) when the maker's site is missing your model.

1. Open Device Manager (Win + X) and expand "Sound, video and game controllers."
2. Right-click the audio device, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart — Windows will attempt automatic reinstallation.
4. If sound is still absent, install the audio driver from your laptop maker's support page and restart again.
5. Verify the device appears without warnings and test playback.

### Fix 6: Disable enhancements and exclusive mode

Driver-level enhancements and exclusive-mode access can both silence output when they malfunction — enhancements by corrupting the processing chain, exclusive mode by letting one app monopolize the device. Disabling both strips the path down to raw driver output, which isolates whether either layer is the culprit.

1. In "More sound settings," double-click your playback device.
2. On the Enhancements tab, tick "Disable all enhancements."
3. On the Advanced tab, untick both "Exclusive mode" options.
4. Click Apply and test playback.
5. If sound returns, leave these off or reinstall the driver to repair the enhancement chain.

### Fix 7: Prove the hardware with an outside-Windows test

If software fixes all fail, verify the speakers themselves before concluding anything. Your manufacturer's boot diagnostics (often F12 at startup) play test tones without Windows; a Linux live USB does the same. Sound in either proves the hardware is fine and the fault is a deep Windows issue — at which point System Restore to a working date, or a Windows reset keeping your files, is the final software step.

1. Restart into the manufacturer's diagnostics and run the audio/speaker test.
2. Alternatively, boot a Linux live USB and play audio there.
3. Sound in either test means working hardware — use System Restore to roll back Windows.
4. Silence in both means failed speakers, jack, or audio codec — a hardware repair.
5. Check warranty status before paying; audio codec issues sometimes qualify for board-level repair programs.

If the silence is limited to the built-in speakers while headphones work, the [laptop speakers guide](/articles/best-way-to-fix-laptop-speakers-not-working/) goes deeper on that split. Enhancement-suite problems have their own fixes too — see [Waves MaxxAudio](/articles/best-way-to-fix-waves-maxxaudio-not-working/) and [Dolby Audio](/articles/how-to-fix-dolby-audio-not-working-youtube/) for those.

## Closing

No sound is a chain problem, and chains are diagnosed link by link: identify your symptom pattern, fix routing and mixer issues, restart the audio services, then reinstall the driver. Prove the hardware with an outside-Windows test before giving up on software. Followed in order, these steps restore audio on the vast majority of silent laptops.
