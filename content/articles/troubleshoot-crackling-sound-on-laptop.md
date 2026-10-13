---
title: "How to Troubleshoot Crackling Sound on a Laptop"
slug: "troubleshoot-crackling-sound-on-laptop"
date: "2026-10-05"
categories: ["drivers"]
tags: ["crackling sound", "audio", "latency", "windows 11", "troubleshooting"]
description: "Hearing crackling, popping, or static from your laptop? Diagnose DPC latency, driver issues, and interference with this systematic guide."
thumbnail: "/images/thumbs/troubleshoot-crackling-sound-on-laptop.webp"
faqs:
  - q: "What causes crackling sound on a laptop?"
    a: "Crackling is usually caused by DPC latency from misbehaving drivers, audio sample rate mismatches, corrupted audio drivers, or electrical interference. It can also come from a failing speaker or a loose audio connection. Testing with headphones helps determine whether the problem is in the speakers or the audio pipeline."
  - q: "What is DPC latency and how does it affect audio?"
    a: "DPC stands for Deferred Procedure Call. When a driver monopolizes the CPU too long, audio processing misses its deadlines and you hear crackles and pops. Network, storage, and GPU drivers are common culprits. The free LatencyMon tool identifies which driver is causing the excessive latency."
  - q: "Can Wi-Fi cause audio crackling?"
    a: "Yes. Wi-Fi drivers are notorious DPC latency offenders, and their power-saving features can cause periodic crackles that seem unrelated to networking. If crackling correlates with downloads or network activity, update the Wi-Fi driver from the manufacturer's support page and disable power-saving features on the wireless adapter as a diagnostic test."
  - q: "Why does crackling happen only on battery power?"
    a: "Power-saving features throttle the CPU and devices aggressively on battery, which can starve the audio pipeline. Switch to the Best performance power mode as a test. If crackling stops, adjust the power plan's processor and device power settings to be less aggressive on battery."
---

Crackling, popping, static: whatever you call it, distorted laptop audio ruins music, calls, and videos alike. The maddening part is how intermittent it can be, fine for an hour, then a burst of crackle every few seconds, then fine again.

Crackling has two families of causes. The first is digital: drivers hogging the CPU (DPC latency), sample rate mismatches, or corrupted audio drivers starving the audio pipeline. The second is physical: dying speakers, interference, or bad connections. A headphone test splits the two instantly. The [post-update crackling guide](/articles/how-to-fix-crackling-sound-on-laptop-after-windows-11-update/) covers the update-triggered variant.

Run the headphone test first, then follow the fixes for your result.

## Why this happens

- **DPC latency from misbehaving drivers:** A driver hogging the CPU makes audio processing miss deadlines.
- **Sample rate mismatch:** Apps and the driver disagreeing on sample rate causes resampling artifacts.
- **Corrupted audio driver:** Damaged driver files produce intermittent distortion.
- **Wi-Fi driver interference:** Wireless drivers are classic DPC latency offenders.
- **Aggressive power saving:** CPU throttling on battery can starve the audio pipeline.
- **Failing speakers:** Worn speaker cones distort at certain frequencies, sounding like crackle.
- **Electrical interference:** Poorly shielded chargers and nearby devices inject noise.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with headphones to isolate the cause

This test divides the problem cleanly. If headphones are clean, the issue is the speakers or their amplifier path. If headphones crackle too, the problem is in the digital audio pipeline.

1. Plug in wired headphones or earbuds.
2. Play the same audio that crackled through the speakers.
3. If headphones are clean, suspect the speakers or speaker wiring.
4. If headphones crackle too, continue with the driver and latency fixes below.
5. Also test Bluetooth audio separately, since it uses a different pipeline.

### Fix 2: Check DPC latency with LatencyMon

LatencyMon is the definitive tool for digital crackling. It shows exactly which driver is hogging the CPU and starving the audio pipeline.

1. Download and install the free LatencyMon utility.
2. Run it and press the play button to start monitoring.
3. Play audio until crackling occurs, watching the driver latency list.
4. Note which driver shows the highest DPC execution times.
5. Update or reinstall that specific driver; Wi-Fi and storage drivers are frequent offenders.

### Fix 3: Set a consistent sample rate

When apps request one sample rate and the driver runs another, constant resampling introduces artifacts. Locking everything to a standard rate eliminates this class of crackle.

1. Open the Sound control panel and open your playback device's Properties.
2. On the Advanced tab, set the default format to 16-bit, 44100 Hz.
3. In your audio apps, match their output sample rate to the same value.
4. Disable any app-level resampling or enhancement features.
5. Test for an extended period before trying higher rates.

### Fix 4: Update the audio and Wi-Fi drivers

The two drivers most implicated in crackling are the audio driver itself and the Wi-Fi driver behind DPC latency. Updating both covers the common cases.

1. Download the latest audio driver from your laptop maker's support page.
2. Uninstall the current audio device with driver deletion, restart, and install the fresh driver.
3. Update the Wi-Fi driver the same way, since it is a frequent latency offender.
4. Update the chipset driver as well for good measure.
5. Retest with LatencyMon running to confirm improvement. Related [speaker crackling](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/) follows the same repair path.

### Fix 5: Adjust power settings for audio stability

If crackling appears on battery but not on AC power, aggressive power saving is starving the audio pipeline. Relaxing it is a quick, free fix.

1. Open Power Options and switch to the Best performance mode for testing.
2. In advanced power settings, set Minimum processor state higher on battery.
3. Disable USB selective suspend and PCI Express link-state power management as a test.
4. On the Wi-Fi adapter's Power Management tab, disable power saving.
5. If crackling stops, tune the settings to a balance of battery life and clean audio.

### Fix 6: Rule out interference and failing speakers

When the digital pipeline checks out, look at the physical world. Interference and worn speakers produce crackle that no driver update will fix.

1. Unplug the charger and test on battery to rule out charger interference.
2. Move phones and other electronics away from the laptop.
3. Play a frequency sweep video and note at which frequencies crackle appears; consistent spots suggest speaker damage.
4. If one speaker crackles and the other does not, that speaker is likely failing.
5. For confirmed speaker failure, contact the manufacturer's repair service for a replacement.

### Fix 7: Disable unused audio devices

Every enabled audio device adds a stream the system must mix and manage. Disabling the outputs and inputs you never use reduces driver contention and eliminates a surprising number of crackle sources, particularly on laptops with many virtual devices installed.

1. Open the Sound control panel and go to the Playback tab.
2. Right-click and disable every output device you do not actively use.
3. Do the same on the Recording tab for unused microphones and line inputs.
4. Restart your audio app and test for crackling.
5. Re-enable devices only as you actually need them.

### Fix 8: Test audio in Safe Mode

Safe Mode loads a minimal driver set, which makes it a powerful diagnostic. If crackling vanishes in Safe Mode, a third-party driver is definitely the cause, and you can hunt it down by systematic elimination.

1. Boot into Safe Mode using the standard recovery method.
2. Play audio and listen carefully for crackling.
3. If it is clean, return to normal mode and disable non-Microsoft startup services in groups.
4. Re-enable groups one at a time until crackling returns to identify the culprit.
5. Update or permanently remove the offending software.

## Closing

Crackling sound is a pipeline problem until proven otherwise: latency, sample rates, drivers, and power settings. The headphone test and LatencyMon turn guesswork into diagnosis, and the fixes that follow are straightforward. Only when the digital side is clean should you blame the speakers themselves.
