---
title: "How to Fix Speakers Crackling on a Laptop in Windows 11"
slug: "how-to-fix-speakers-crackling-on-laptop-on-windows-11"
date: "2026-09-17"
categories: ["drivers"]
tags: ["speakers crackling", "audio distortion", "realtek audio", "windows 11", "sound driver"]
description: "Laptop speakers crackling, popping, or distorting on Windows 11? Fix it with audio format tweaks, enhancement disabling, driver reinstalls, and DPC latency checks."
thumbnail: "/images/thumbs/how-to-fix-speakers-crackling-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why do my laptop speakers crackle on Windows 11 but not with headphones?"
    a: "When headphones sound fine but speakers crackle, the issue is usually in the speaker-specific audio path: the built-in speaker tuning, audio enhancements applied only to speakers, or the speaker amplifier being overdriven. Check the speaker properties in the Sound control panel, disable all enhancements for the speaker device specifically, and lower the volume slightly to test whether the amplifier is clipping."
  - q: "Can the audio sample rate cause crackling?"
    a: "Yes. Mismatched or unstable sample rates are a classic cause of crackling and popping. In the speaker's Properties > Advanced tab, try setting the default format to 24-bit, 48000 Hz, which is the most broadly compatible studio-quality setting. Avoid exclusive-mode applications forcing unusual rates, and uncheck exclusive-mode boxes so no single app can hijack the audio format."
  - q: "What is DPC latency and how does it cause audio crackling?"
    a: "DPC latency measures how long drivers take to handle hardware interrupts. A misbehaving driver — often Wi-Fi, storage, or graphics — can delay audio processing enough to cause dropouts that you hear as crackling. Free tools like LatencyMon identify the offending driver. Updating or disabling that driver, rather than the audio driver, is the real fix in these cases."
  - q: "Should I update or roll back my audio driver for crackling?"
    a: "Try rolling back first if crackling started after an update: Device Manager > audio device > Properties > Driver tab > Roll Back Driver. If there was no recent update, install the latest audio driver from your laptop maker's support site. Generic Windows audio drivers are a frequent cause of crackling, so the manufacturer's Realtek or Waves-tuned package usually sounds cleaner."
---

Crackling, popping, or stuttering laptop speakers make everything from video calls to music unpleasant, and the cause is rarely the speakers themselves. On Windows 11, audio crackling is usually a driver or configuration problem: the wrong sample rate, overzealous enhancements, a generic audio driver, or another misbehaving driver stealing processing time. This guide works through each cause in order, with a simple test after every fix so you know exactly when it is solved.

Test consistently as you go: play the same audio clip or video at the same volume after each fix. Crackling that changes character between fixes is telling you something — note whether it improves, worsens, or moves between apps.

## Why this happens

- **Audio enhancements distorting output:** Loudness equalization and bass boost effects can clip the signal, producing crackle at higher volumes.
- **Wrong sample rate or bit depth:** An incompatible default format causes the audio engine to resample badly, creating pops.
- **Generic Windows audio driver:** The basic Microsoft driver lacks the manufacturer's tuning and often crackles where the Realtek package does not.
- **DPC latency from another driver:** Wi-Fi, storage, or graphics drivers hogging interrupt time starve the audio stream.
- **Exclusive mode conflicts:** One app seizing exclusive audio control can force format changes that crackle.
- **Corrupted audio driver:** Partial updates leave the driver in a state that mostly works but distorts.
- **Power management throttling:** CPU or bus power saving can interrupt the steady data flow audio needs.
- **Failing speaker hardware:** Blown or loose speaker cones crackle physically — the last thing to check, and easy to distinguish.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable all audio enhancements

Enhancements are the number-one software cause of speaker crackling.

1. Press Win + R, type `mmsys.cpl`, and press Enter, then go to the Playback tab.
2. Double-click your Speakers device (the Realtek or laptop-speaker entry, not headphones).
3. On the Enhancements tab, check "Disable all enhancements". On newer driver builds, find the equivalent toggle in the Realtek Audio Console app.
4. Click Apply and play your test audio immediately.
5. If the crackling stops, re-enable enhancements one at a time only if you actually want them — most are safe to leave off permanently.

### Fix 2: Change the default audio format

A mismatched sample rate produces exactly the popping and crackling you are hearing.

1. In the speaker's Properties window from Fix 1, go to the Advanced tab.
2. Change the Default Format to "24 bit, 48000 Hz (Studio Quality)" — the most compatible setting.
3. Uncheck both boxes under Exclusive Mode so no app can force format changes.
4. Click Apply, then test your audio clip.
5. If 48 kHz does not help, try "16 bit, 44100 Hz (CD Quality)" as a second option — some older codecs prefer it.
6. Leave the format at whichever setting plays cleanly; there is no benefit to higher rates for laptop speakers.

### Fix 3: Lower the volume and test for clipping

Speakers crackle physically when overdriven, which is a different problem from driver crackle.

1. Set Windows volume to 50% and play your test audio — note whether the crackling disappears.
2. Gradually raise the volume and find the threshold where crackling starts.
3. If crackling only appears above 80-90%, the amplifier is clipping; keep volume below that threshold.
4. Check the app's own volume too — a maxed-out app feeding a maxed-out Windows mixer distorts badly.
5. If crackling persists even at 30% volume, it is a driver or processing issue, not clipping — continue below.
6. Also test with headphones: clean headphone audio plus crackling speakers at all volumes points to the speaker path specifically.

### Fix 4: Reinstall the audio driver

A clean driver reinstall fixes corruption that settings cannot reach.

1. Press Win + X, open Device Manager, and expand "Sound, video and game controllers".
2. Right-click your Realtek (or other) audio device, choose Uninstall device, and tick "Attempt to remove the driver for this device".
3. Restart the laptop and let Windows install its basic audio driver.
4. Test with the basic driver — if crackling is gone, the old driver was corrupt.
5. Then install the manufacturer's audio package for the permanent fix (next step), since the basic driver lacks proper tuning.

### Fix 5: Install the manufacturer's tuned audio driver

Laptop makers tune audio drivers for their specific speaker hardware — generic drivers miss this.

1. Visit your laptop maker's support site — for example [Dell's official support](https://www.dell.com/support) — and download the audio driver for your exact model.
2. Install it, restart, and open the Realtek Audio Console or Waves MaxxAudio app if one is included.
3. Reset any equalizer to flat and disable effects while testing.
4. Retest your audio clip at several volume levels.
5. If your model uses Waves MaxxAudio and the console itself seems to cause distortion, compare symptoms with the [Windows 11 24H2 crackling variant](/articles/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2/), which covers newer driver builds.

### Fix 6: Check DPC latency for driver interference

When audio crackling persists through every audio fix, another driver is usually the culprit.

1. Download the free LatencyMon tool and run it while playing audio.
2. Let it run for five minutes, then check the Drivers tab for the highest DPC count.
3. Common offenders: wireless network drivers (ndis.sys), storage drivers (storport.sys), and graphics drivers.
4. Update the offending driver from the manufacturer's site — do not just update the audio driver again.
5. As a quick test, temporarily disable Wi-Fi and Bluetooth and replay your audio; if crackling stops, the wireless driver is interfering.
6. Microsoft documents audio troubleshooting basics at [Windows support](https://support.microsoft.com/en-us/windows), though DPC diagnosis goes beyond their guides.

### Fix 7: Disable CPU and bus power saving

Power-state transitions can interrupt the audio data stream just enough to crackle.

1. Open Control Panel > Power Options and switch to the High performance plan (or create one).
2. Go to Change advanced power settings and set Processor power management > Minimum processor state to 50% or higher on plugged-in.
3. Expand PCI Express > Link State Power Management and set it to Off.
4. In Device Manager, check the audio device's Power Management tab and disable power saving if the option exists.
5. Test audio on AC power — if crackling only happens on battery, power management is confirmed as the cause.

### Fix 8: Test for physical speaker damage

If software is exhausted and crackling persists identically everywhere, inspect the hardware.

1. Play a sine-wave sweep video (easily found online) and listen for buzzing or rattling at specific frequencies — that indicates a damaged cone.
2. Press gently around the speaker grilles while audio plays; changes in the crackle suggest a loose speaker or debris.
3. Boot a Linux live USB and play audio there — identical crackling across operating systems means hardware.
4. For confirmed hardware failure, speaker modules are inexpensive on most laptops but require opening the machine (check warranty first).
5. A USB or Bluetooth speaker is a perfectly good workaround while you decide on repair.

## Closing

Speaker crackling on Windows 11 is a diagnosis problem more than a repair problem — enhancements, sample rates, generic drivers, and DPC latency each produce similar-sounding distortion with very different fixes. Work the list in order, test with the same clip each time, and you will find the layer responsible. If your speakers produce no sound at all rather than distorted sound, see our [laptop speakers not working guide](/articles/how-to-fix-laptop-speakers-not-working-on-windows-11/). In most cases it is software, and the manufacturer's audio driver plus disabled enhancements is the combination that finally silences the crackle.
