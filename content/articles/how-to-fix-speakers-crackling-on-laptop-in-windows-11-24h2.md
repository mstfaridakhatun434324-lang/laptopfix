---
title: "Speakers Crackling on Windows 11 24H2? Clean Up the Audio"
slug: how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2
date: 2026-09-26
categories: ["drivers"]
tags: ["speakers crackling", "audio distortion", "windows 11 24h2", "realtek audio"]
description: "Fix crackling laptop speakers on Windows 11 24H2: disable audio enhancements, fix sample-rate mismatches, and reinstall the audio driver."
thumbnail: "/images/thumbs/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why do my laptop speakers crackle after the 24H2 update?"
    a: "The 24H2 update migrates audio drivers and can enable enhancement processing that the new driver mishandles, or install a generic audio driver with wrong default sample rates. Crackling that starts immediately after the update is a software problem in the vast majority of cases — the speakers did not physically degrade overnight."
  - q: "How do I tell software crackling from blown speakers?"
    a: "Software crackling changes with settings: it varies with volume, disappears with enhancements off, or affects only certain apps. Blown speakers distort consistently regardless of settings, often with a rattling quality on bass notes at any volume. If the crackling vanishes in the BIOS beep test or with headphones, the speakers themselves are likely fine."
  - q: "What sample rate should I set to stop crackling?"
    a: "Start with 24-bit, 48000 Hz (DVD quality) in the device's advanced properties — it is the most broadly compatible setting. Mismatches between the app, Windows, and driver sample rates force resampling that can introduce crackle. Avoid the highest rates unless your hardware and content genuinely need them."
  - q: "Can audio enhancements really cause crackling?"
    a: "Yes, frequently. Loudness equalization, bass boost, and virtual surround all process the audio stream in real time, and buggy enhancement implementations clip or stutter the output. Disabling all enhancements is one of the highest-yield troubleshooting steps for post-update crackling, so try it before reinstalling any drivers."
---

Crackling speakers turn music into a bowl of breakfast cereal and make video calls sound like a bad radio signal. When the crackling starts right after the Windows 11 24H2 update, the timing is the biggest clue you will get: the speakers were fine yesterday, nothing physically changed, and now every sound has static riding on top of it. That pattern screams software — a driver migration, a flipped enhancement setting, or a sample-rate mismatch introduced by the update.

Laptop audio runs through a chain: the app, the Windows audio engine, enhancement processing, the audio driver, and finally the codec chip feeding the speakers. The 24H2 update can disturb any link — installing a generic driver over the vendor's tuned one, re-enabling enhancements the old driver had quietly disabled, or resetting the default format to a rate the hardware handles poorly. Each produces the same audible symptom with a different fix.

The steps below attack the chain in order of likelihood: enhancements and format settings first, then the driver, then the deeper power and hardware checks. Test audio after each change so you know exactly which link was broken.

## Why this happens

- **Audio enhancements re-enabled by the update:** 24H2 can turn loudness equalization and other processing back on. Buggy enhancement code clips the signal, producing crackle that tracks with volume.
- **Sample rate mismatch:** When Windows, the app, and the driver disagree on sample rate, constant resampling introduces artifacts that sound like static or crackling.
- **Generic driver replacing the vendor's:** The update may substitute a generic High Definition Audio driver for the vendor-tuned Realtek or Waves package, losing hardware-specific fixes.
- **Exclusive mode conflicts:** Apps taking exclusive control of the audio device at odd sample rates can destabilize shared-mode playback for everything else.
- **Power management throttling the codec:** The audio codec being power-gated aggressively causes dropouts that manifest as crackle, especially at the start of sounds.
- **DPC latency from other drivers:** A misbehaving network or storage driver can delay audio processing enough to cause dropouts. Post-update driver churn makes this more likely.
- **Physically damaged speakers:** Blown or loose speakers distort regardless of software settings. Crackling that survives every software fix and sounds rattly on bass points here.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable all audio enhancements

Enhancement processing is the highest-yield first step. Turn it all off and listen before changing anything else.

1. Right-click the speaker icon, choose Sound settings, then open your output device's properties.
1. Under Enhancements or Advanced, disable all enhancements and turn off any spatial sound.
1. Play the same audio that crackled before and compare. If the crackle is gone, re-enable enhancements one by one only if you miss them.

### Fix 2: Set a sane default sample rate

Lock Windows to a broadly compatible format so no resampling fights happen behind the scenes.

1. In the device properties, open the Advanced tab.
1. Set the default format to 24-bit, 48000 Hz.
1. Uncheck Allow applications to take exclusive control of this device while testing, then retest your audio.

### Fix 3: Reinstall the audio driver cleanly

When settings do not fix it, the migrated driver is the suspect. Replace it with the vendor's package.

1. In Device Manager, expand Sound, video and game controllers and uninstall the audio device, checking Delete the driver software.
1. Restart and install the audio driver for your exact model from the vendor's support site.
1. Test before letting Windows Update offer alternatives. For the older-update variant of this problem, see [crackling after Windows updates](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/), and for driver-level audio crashes the [Realtek driver guide](/articles/realtek-audio-driver-not-working-windows-11/) covers the deeper repair.

### Fix 4: Stop the codec from being power-managed

Dropouts at the start of sounds are the signature of an over-eager power policy on the audio hardware.

1. In Device Manager, find the audio controller under System devices as well as the audio device itself.
1. On each Power Management tab, uncheck Allow the computer to turn off this device to save power.
1. Play audio after a period of silence and check whether the opening crackle is gone.

### Fix 5: Check DPC latency for driver interference

If crackling persists across drivers and settings, another driver may be starving the audio pipeline.

1. Download a DPC latency checker and run it while playing audio.
1. Spikes correlating with the crackle point at the offending driver — often network or storage drivers updated alongside 24H2.
1. Update or roll back the flagged driver and retest. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in audio troubleshooter as a complementary check.

### Fix 6: Test with headphones and isolate the speakers

Determine whether the problem is in the signal chain or the physical speakers.

1. Plug in wired headphones or USB audio and play the same content.
1. Clean headphone audio with crackling speakers means the chain is fine and the speakers or their wiring are suspect.
1. If both crackle identically, the issue remains in software — repeat the driver step with an older vendor driver version known to work.

### Fix 7: Check for BIOS and firmware audio fixes

Audio codec behavior is partly governed by firmware, and vendors ship BIOS updates that fix crackling, popping, and power-management issues in the audio subsystem. When driver and settings fixes fail, the remaining suspect below the operating system is firmware. This is especially worth checking on laptops where the crackling started after a BIOS update arrived alongside the Windows update.

1. Compare your BIOS version with the newest for your model on the vendor's support page, reading the release notes for audio mentions.
1. Apply the update with the charger connected and audio devices idle.
1. After booting, retest the exact audio that crackled before changing anything else.

## Closing

Post-24H2 speaker crackling is a settings-and-driver problem far more often than a speaker problem: enhancements, sample rates, and migrated drivers account for nearly every case. Work the chain from the Windows settings outward to the driver, and test with headphones to keep hardware suspicion honest. The static that appeared overnight with the update can disappear just as quickly once the right link in the chain is repaired.
