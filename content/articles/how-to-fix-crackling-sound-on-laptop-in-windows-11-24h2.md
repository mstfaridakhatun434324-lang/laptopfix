---
title: "Crackling Sound on Laptop in Windows 11 24H2: Audio Repair Guide"
slug: how-to-fix-crackling-sound-on-laptop-in-windows-11-24h2
date: 2026-10-11
categories: ["drivers"]
tags: ["crackling sound", "audio distortion", "windows 11 24h2", "realtek", "latency"]
description: "Audio crackling and popping after the Windows 11 24H2 update? Fix driver, latency, and enhancement issues with this guide."
thumbnail: "/images/thumbs/how-to-fix-crackling-sound-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the 24H2 update cause audio crackling on my laptop?"
    a: "The 24H2 update changed audio driver handling and power management behavior, which exposed latency problems in older Realtek drivers and broke some manufacturer audio enhancements. The crackling is typically buffer underruns — the audio pipeline not delivering samples fast enough — caused by driver inefficiency or DPC latency spikes from other drivers. Updating the audio driver and disabling enhancements resolves most 24H2 crackling."
  - q: "What is DPC latency, and how does it cause crackling?"
    a: "DPC latency measures how long deferred procedure calls from drivers delay the system. Audio needs a steady stream of samples delivered on tight deadlines; when a misbehaving driver (often network, storage, or GPU) hogs the CPU with long DPCs, audio buffers run dry and you hear pops and crackles. Tools like LatencyMon identify the offending driver so you can update or disable it."
  - q: "Does changing the audio sample rate fix crackling?"
    a: "Sometimes. Mismatched sample rates force real-time resampling that adds CPU load and can glitch on weak audio pipelines. Setting the output to 24-bit 48000 Hz — the native rate for most laptop codecs and Windows' internal mixer — removes a resampling stage. It is a worthwhile test, though persistent crackling usually needs the driver or latency fix underneath."
  - q: "Can Bluetooth cause crackling on the built-in speakers too?"
    a: "Indirectly. A struggling Bluetooth stack can generate DPC latency spikes that affect all audio, and some systems route audio processing through shared pipelines. But crackling isolated to the built-in speakers with no Bluetooth devices connected is a local driver or latency issue. Test with Bluetooth fully disabled to separate the two causes cleanly."
---

Crackling, popping, and stuttering audio after the Windows 11 24H2 update is a special kind of maddening — the speakers are fine, the files are fine, but every song, call, and video is peppered with glitches. This is a real-time processing problem, not a broken speaker: somewhere in the chain from application to audio codec, samples are arriving late. The 24H2 update is a frequent trigger because it reshuffles drivers and power behavior, exposing latency weaknesses that older builds tolerated.

The diagnostic approach here differs from "no sound" troubleshooting. You are hunting for what steals the CPU's attention at the wrong moment: an outdated audio driver, a latency-spiking network or storage driver, aggressive power saving, or conflicting enhancements. For the pre-24H2 version of this problem, see our [post-update crackling guide](/articles/how-to-fix-crackling-sound-on-laptop-after-windows-11-update/), and the [speaker crackling repair](/articles/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2/) covers hardware-adjacent causes.

## Why this happens

- **The 24H2 update left an incompatible audio driver** that cannot keep up with the new audio stack's timing.
- **DPC latency spikes from another driver** (network, storage, GPU) starve the audio pipeline of CPU time.
- **Audio enhancements add processing** that glitches under the new driver and power conditions.
- **Aggressive CPU power saving** lets cores sleep too deeply between audio callbacks, causing underruns on wake.
- **Sample rate mismatches** force real-time resampling that the pipeline cannot sustain.
- **Bluetooth stack activity** generates latency spikes affecting even the built-in speakers.
- **Corrupted audio driver components** from the update produce intermittent buffer failures.

- **The 24H2 update re-enabled audio enhancements you had previously disabled**, silently restoring the processing layer that was causing buffer glitches before the upgrade.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable audio enhancements

The fastest test with the highest hit rate. Recheck enhancements after every feature update — Windows loves to turn them back on.

1. Right-click the volume icon, choose Sound settings, then More sound settings.
2. On the Playback tab, double-click your speakers/headphones and open Properties.
3. On the Enhancements tab, tick Disable all enhancements.
4. Play audio for several minutes — if the crackling stops, the enhancements were the cause.

### Fix 2: Set the sample rate to 24-bit 48000 Hz

Remove the resampling stage from the pipeline. Some apps override the shared sample rate with exclusive mode — the exclusive-mode untick prevents that.

1. In the same device Properties, open the Advanced tab.
2. Set Default Format to 24 bit, 48000 Hz (Studio Quality).
3. Untick Allow applications to take exclusive control of this device.
4. Click Apply and test with the same audio that crackled before.

### Fix 3: Reinstall the manufacturer's audio driver

The core 24H2 fix — replace whatever the update left behind. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents driver reinstallation. Get the 24H2-specific audio package from the manufacturer, not the generic Windows 11 one.

1. In Device Manager, expand Sound, video and game controllers.
2. Uninstall the Realtek (or Conexant/IDT) audio device, ticking Delete the driver software.
3. Restart the laptop.
4. Install the audio driver from your laptop manufacturer's support page for Windows 11 24H2 specifically.

### Fix 4: Measure DPC latency with LatencyMon

Find the driver that is actually stealing the CPU. Let LatencyMon run during your actual workload, not idle — spikes often need load to appear.

1. Download LatencyMon from its official site and run it as administrator.
2. Press the play button and let it monitor for five minutes while playing crackling audio.
3. Check the Drivers tab for the highest DPC execution times.
4. Update or disable the offending driver — network and storage drivers are the usual culprits.

### Fix 5: Disable CPU power saving for audio

Deep sleep states and audio deadlines do not mix. Test on AC power first to separate power-saving crackle from driver crackle.

1. Open Power Options advanced settings and expand Processor power management.
2. Set Minimum processor state to 50 percent or higher on plugged in.
3. Expand PCI Express and set Link State Power Management to Off as a test.
4. In the BIOS, consider disabling the deepest C-states if the option exists and crackling persists.

### Fix 6: Update the chipset and storage drivers

The latency often originates outside the audio driver entirely. Storage drivers cause some of the worst audio latency spikes despite having nothing to do with sound.

1. Install the latest chipset driver from your laptop manufacturer's support page.
2. Update storage controller drivers (Intel RST or the NVMe driver) to current versions.
3. Update the network drivers — Wi-Fi and Ethernet drivers are notorious DPC offenders.
4. Re-run LatencyMon after each update to confirm the spikes are gone.

### Fix 7: Test with Bluetooth disabled and a clean boot

Isolate software interference systematically. A clean boot that fixes crackling proves software interference — then bisect the startup items.

1. Turn Bluetooth fully off in Settings and test the speakers.
2. Run msconfig, choose Selective startup, and disable all non-Microsoft services.
3. Restart and test audio in the clean state.
4. Re-enable services in halves to identify the interfering program.

## Closing

24H2 audio crackling is a latency problem wearing a driver problem's clothes: disable enhancements, set a sane sample rate, reinstall the manufacturer's 24H2-era audio driver, and hunt DPC spikes with LatencyMon. That sequence resolves the overwhelming majority of cases. If crackling persists in a clean boot with fresh drivers and low DPC latency, the audio codec hardware itself may be failing — rare, but the remaining explanation once software is exhausted. Once the audio is clean, stress-test it the way you actually listen: play music for half an hour, join a video call, and scrub through a video timeline. Crackling that only appears under specific loads points at the remaining bottleneck — often a single latency-spiking driver that LatencyMon can still identify. Keep LatencyMon installed; it is the fastest way to check if a future update reintroduces the problem.
