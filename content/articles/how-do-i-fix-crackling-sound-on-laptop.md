---
title: "Crackling Sound on a Laptop: Eliminate the Noise"
slug: how-do-i-fix-crackling-sound-on-laptop
date: 2026-09-19
categories: ["drivers"]
tags: ["crackling sound", "audio distortion", "latency", "realtek fix"]
description: "Crackling or popping audio on your laptop? Fix DPC latency, driver, and settings causes of distorted sound on Windows 11."
thumbnail: "/images/thumbs/how-do-i-fix-crackling-sound-on-laptop.webp"
faqs:
  - q: "What causes crackling sound on a laptop?"
    a: "Crackling is usually the audio stream being interrupted: high DPC latency from a misbehaving driver starves the audio buffer, causing pops and crackles. Other causes include mismatched sample rates, audio enhancements gone wrong, Wi-Fi/Bluetooth driver interference, and failing speakers. The key diagnostic is whether Bluetooth or USB audio crackles too — if not, the built-in audio path is the problem."
  - q: "How do I check DPC latency on my laptop?"
    a: "Download LatencyMon (free) and run it while playing audio. It shows which drivers have the highest execution times — network, storage, and GPU drivers are frequent offenders. If a specific driver shows huge latency spikes coinciding with crackles, updating or disabling that driver often fixes the audio without touching the audio driver at all."
  - q: "Why does crackling get worse when I move the mouse or open programs?"
    a: "That's the signature of DPC latency or interrupt conflicts: system activity from the mouse, disk, or network drivers delays audio processing, and the audio buffer underruns. Updating the chipset, network, and storage drivers — not just the audio driver — is the fix, since those are the drivers stealing the CPU time."
  - q: "Can Bluetooth cause crackling in my laptop speakers?"
    a: "Indirectly, yes. A struggling Bluetooth driver can generate high DPC latency that disrupts all audio, including the built-in speakers. As a diagnostic, turn Bluetooth off entirely and test the speakers. If crackling stops, update the Bluetooth driver from your laptop maker's support page or leave Bluetooth off when not needed."
---

Crackling, popping, and stuttering audio is different from no audio at all — the sound path works, but something keeps interrupting it. The culprit is usually timing: the audio buffer isn't fed smoothly because some driver is hogging the CPU, or the audio settings mismatch the hardware's expectations. This guide finds the interruption and removes it.

The critical diagnostic: does the crackling affect Bluetooth headphones and USB audio too, or only the built-in speakers? If everything crackles, it's a system-level latency or settings issue. If only the built-in speakers crackle, it's the Realtek path or the speakers themselves. Run that test first — it halves the checklist. For total audio loss instead, see [Realtek audio repair](/articles/how-do-i-fix-realtek-audio-not-working/).

## Why this happens

- **High DPC latency:** A misbehaving driver (network, storage, GPU) delays audio processing, starving the buffer.
- **Sample rate mismatch:** Apps and Windows disagree on sample rate, causing resampling artifacts.
- **Audio enhancements:** Broken EQ or effects in the Realtek console distort the output.
- **Bluetooth/Wi-Fi driver interference:** Wireless drivers generate latency spikes that hit audio.
- **Power management throttling:** CPU power states cause timing jitter in the audio pipeline.
- **Corrupted audio driver:** Damaged driver files produce glitches rather than silence.
- **Failing speakers:** Physically damaged speaker cones crackle at certain frequencies.
- **Electrical interference:** Poorly shielded audio paths pick up noise from other components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Scope the problem across outputs

Play the same audio through built-in speakers, wired headphones, Bluetooth headphones, and (if available) a USB headset. Note exactly which outputs crackle. Speakers-only crackling points at the Realtek codec path or the speaker hardware; everything-crackling points at system latency or shared settings. Also test with local media files versus streaming — streaming-only crackle can be network buffering, not audio at all. Write down the pattern; it determines which fixes below apply.

1. Test speakers, wired, Bluetooth, and USB outputs.
2. Compare local files against streaming audio.
3. Note which combinations crackle.
4. Speakers-only means codec/speaker path.
5. Everything means system latency or settings.

### Fix 2: Disable audio enhancements and reset the console

Open Sound settings, the Speakers device properties, and on the Advanced or Enhancements tab, check "Disable all enhancements." In the Realtek Audio Console, reset EQ to flat and turn off all effects. Set the default format to 24-bit, 48000 Hz (or 44100 Hz) — a common stable choice — and uncheck "Allow applications to take exclusive control of this device" during testing. These settings changes fix a large share of crackling outright, especially after driver updates that enable enhancements by default; Microsoft's support pages document the sound device properties involved.

1. Disable all enhancements on the playback device.
2. Reset Realtek Audio Console EQ and effects.
3. Set default format to 24-bit, 48000 Hz.
4. Disable exclusive mode during testing.
5. Retest with the same audio.

### Fix 3: Measure and fix DPC latency

Download LatencyMon and run it for several minutes while playing audio and using the laptop normally. Check the Drivers tab for the highest DPC execution times — common offenders are network drivers (ndis.sys with a bad Wi-Fi driver underneath), storage drivers, and GPU drivers. Update the offending driver from the laptop maker: [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel-based drivers, or the maker's support page for MediaTek/Realtek wireless. Rerun LatencyMon after each update to confirm the spikes dropped.

1. Run LatencyMon while playing audio.
2. Identify drivers with the highest DPC times.
3. Update the offending drivers from the maker.
4. Rerun LatencyMon to verify improvement.
5. Correlate latency spikes with audible crackles.

### Fix 4: Update the full driver stack, not just audio

Crackling blamed on the audio driver is often caused by the chipset, network, or storage drivers. Install the latest chipset driver from your laptop maker, update Wi-Fi and Bluetooth drivers ([Dell's support portal](https://www.dell.com/support), for example), and update the graphics driver — GPU drivers are notorious DPC latency sources. Reinstall the Realtek audio driver from the maker last, so it layers onto a healthy stack. Reboot between major driver installs and retest audio each time.

1. Install the latest chipset driver and reboot.
2. Update Wi-Fi and Bluetooth drivers.
3. Update the graphics driver.
4. Reinstall the Realtek audio driver last.
5. Retest audio after each major update.

### Fix 5: Stabilize power management

Open Power Options and switch to High performance (or Best performance) as a test — aggressive CPU power-state transitions cause audio timing jitter. In the advanced plan settings, set Minimum processor state to 50%+ on plugged in, and disable USB Selective Suspend. In Device Manager, uncheck power-saving on the audio device and network adapters. If crackling vanishes on High performance, you've confirmed power management as the cause; you can then tune a custom plan that keeps the fix without maximum battery drain.

1. Switch to High performance power plan as a test.
2. Raise minimum processor state in advanced settings.
3. Disable USB Selective Suspend.
4. Uncheck power-saving on audio and network devices.
5. Build a custom plan balancing fix and battery life.

### Fix 6: Isolate wireless interference

Turn off Bluetooth entirely and test the speakers — then turn off Wi-Fi (use Ethernet or offline media) and test again. If either toggle stops the crackling, that wireless driver is generating the latency. Update it from the maker's support page, and check its Advanced properties for power-saving modes to disable. As a lasting workaround, some users keep Bluetooth off when doing critical audio work. If the crackling is in Bluetooth audio itself rather than caused by it, see [Bluetooth troubleshooting](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/) for the wireless side.

1. Turn Bluetooth off and test speakers.
2. Turn Wi-Fi off and test with local media.
3. Update whichever wireless driver is implicated.
4. Disable power-saving in its Advanced properties.
5. Consider Bluetooth-off for critical listening.

### Fix 7: Test the speakers themselves

If only the built-in speakers crackle across all drivers and settings, play a sine sweep (search for one online) at moderate volume and listen: crackling at specific frequencies, buzzing, or rattling indicates physically damaged speaker cones — common after drops or age. Try pressing gently around the speaker grilles; a change in the crackle confirms a mechanical issue. Speaker replacement on most laptops is a modest repair — the modules are inexpensive, though access varies by model. External speakers or headphones remain a fine workaround.

1. Play a frequency sweep at moderate volume.
2. Listen for frequency-specific crackling or buzzing.
3. Press gently around speaker grilles for changes.
4. Confirm it's mechanical, not electrical.
5. Replace speaker modules or use external audio.

## Closing

Crackling audio is a timing problem until proven mechanical: kill the enhancements, measure the latency, update the drivers that actually cause it (often not the audio driver), and stabilize power management. That sequence silences the vast majority of cases. When only the built-in speakers crackle through every driver and setting, trust the sweep test — worn speakers are honest hardware failures with straightforward replacements.
