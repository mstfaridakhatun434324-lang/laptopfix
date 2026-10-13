---
title: "What to Do If You Hear Crackling Sound on Your Laptop"
slug: what-to-do-if-crackling-sound-on-laptop
date: 2026-09-11
categories: ["drivers"]
tags: ["crackling sound", "audio popping", "sound distortion", "dpc latency", "windows audio"]
description: "Hearing crackling, popping, or static on your laptop? Trace the audio pipeline — sample rates, DPC latency, drivers, and interference — to silence it."
thumbnail: "/images/thumbs/what-to-do-if-crackling-sound-on-laptop.webp"
faqs:
  - q: "What is the difference between speaker crackling and audio pipeline crackling?"
    a: "Speaker crackling comes from the physical speakers — it is present on speakers but absent in headphones, and often tied to volume level. Audio pipeline crackling comes from the digital path before the speakers — it appears in headphones too, affects all volumes equally, and often stutters in rhythm with system activity. The headphone test separates them instantly: crackling in headphones means the pipeline, clean headphones mean the speakers. Each has completely different fixes."
  - q: "What is DPC latency and why does it cause crackling?"
    a: "DPC (Deferred Procedure Call) latency measures how long drivers monopolize the CPU. Audio needs tiny slices of CPU time at exact intervals; when a misbehaving driver — often Wi-Fi, storage, or GPU — hogs the CPU for milliseconds too long, the audio buffer runs dry and you hear a pop or crackle. LatencyMon is the free tool that identifies the offending driver."
  - q: "Why does crackling start when I open certain programs?"
    a: "Because that program changes the audio pipeline or system load. Games and DAWs request exclusive audio access and different sample rates, triggering resampling glitches. Browsers with many tabs increase DPC latency through network and GPU driver activity. Video calls engage echo cancellation and noise suppression DSP that can glitch. Note which programs trigger it — the trigger identifies whether you are dealing with sample-rate conflicts, latency, or DSP bugs, and each has its specific fix."
  - q: "Can Bluetooth cause crackling in wired audio?"
    a: "Indirectly, yes. Active Bluetooth — especially connected Bluetooth audio devices — consumes CPU and radio resources that can increase DPC latency, and on combo Wi-Fi/Bluetooth cards the coexistence handling can glitch the whole wireless subsystem. If crackling correlates with Bluetooth activity, try disabling Bluetooth temporarily as a diagnostic. Some users also find that disconnecting unused paired Bluetooth audio devices stops the crackling, because Windows stops polling them."
---

Crackling sound on a laptop — pops, static bursts, and stutters riding over your audio — is an audio-pipeline problem until proven otherwise. Unlike speaker damage (which stays in the speakers), pipeline crackling infects every output: speakers, wired headphones, sometimes even Bluetooth. This guide traces the pipeline from the app to the driver to the hardware, because the crackle you hear is just the audible symptom of a timing glitch somewhere along that path.

The pipeline view matters because the fixes are scattered across unrelated settings: sample rates in Sound properties, latency in unrelated drivers, power states in USB hubs. Random fixes fail; systematic pipeline tracing works.

## Why this happens

- **Sample rate mismatches:** App, Windows, and driver disagreeing on sample rate forces real-time resampling, which glitches audibly under load.
- **DPC latency spikes:** Misbehaving non-audio drivers starving the audio pipeline of CPU time — the most underdiagnosed cause of crackling.
- **Buffer underruns:** Audio buffers set too small for the system's latency characteristics, common in pro-audio apps with wrong settings.
- **Corrupted audio driver:** Driver state corruption producing periodic glitches that survive reboots and settings changes.
- **Power management throttling:** CPU or device power states changing mid-stream, disrupting the precise timing audio needs.
- **USB audio instability:** For USB headsets and DACs, USB power management or hub issues interrupting the isochronous audio stream.
- **Electromagnetic interference:** CPU/GPU load coupling into poorly shielded onboard audio paths — crackling that tracks system activity.
- **Conflicting audio processing:** Multiple enhancement layers (Windows effects + manufacturer DSP + app processing) stacking into glitchy output.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine the scope with output tests

Map where the crackling lives before touching settings.

1. Test the same audio on **built-in speakers**, **wired headphones**, and **Bluetooth** (if available). Note exactly which outputs crackle.
2. All outputs crackling = pipeline problem (continue here). Only speakers = speaker hardware (see our [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop/)). Only Bluetooth = wireless issue.
3. Test with the charger unplugged and plugged in. Crackling that changes with charger state indicates grounding or charger noise.
4. Test in **Safe Mode** with audio. No crackling in Safe Mode means a third-party driver or startup program is the cause — a powerful narrowing step.

### Fix 2: Fix sample rates and audio format

The most common pipeline misconfiguration.

1. Right-click the speaker icon → **Sound settings** → output device → **Properties → Advanced** (or **Control Panel → Sound → Playback → Properties → Advanced**).
2. Set **Default Format** to **16 bit, 44100 Hz (CD Quality)** — the universal baseline. Test thoroughly.
3. If clean, try **24 bit, 48000 Hz**. Avoid 192000 Hz settings unless you have a specific reason — many onboard codecs glitch at rates they nominally support.
4. In the apps you use most (music players, DAWs, games, conferencing), set explicit output devices and matching sample rates rather than leaving everything on Default. Mismatched app/system rates are the classic resampling-glitch source.

### Fix 3: Hunt down DPC latency

The deep fix for crackling that ignores all audio settings.

1. Download **LatencyMon** (free) and run it for 5–10 minutes while playing audio that crackles. Let it measure — do not just glance at the first minute.
2. Note the drivers with the highest DPC counts. Common offenders: network drivers (`ndis.sys` with a bad Wi-Fi driver behind it), storage drivers, and GPU drivers.
3. Update or roll back the offending driver — for Wi-Fi-caused latency, the manufacturer's wireless driver usually outperforms the generic one dramatically.
4. In **Device Manager**, check the offending device's **Power Management** — devices that aggressively sleep/wake generate latency spikes. Disable power-saving on the culprit device.

### Fix 4: Disable audio enhancements and processing layers

Stacked DSP is a frequent glitch source.

1. In **Sound → Playback → device → Properties → Enhancements**, check **Disable all enhancements**.
2. In **Sound settings → device → Properties**, turn off **Enhance audio** if present.
3. Disable manufacturer audio utilities' effects (Waves MaxxAudio, Nahimic, Dolby processing) one at a time — these run their own DSP that can conflict with Windows'.
4. In conferencing apps, disable their noise suppression and echo cancellation temporarily as a test. If the crackling stops, re-enable app features one at a time. App-level processing bugs are surprisingly common. Persistent driver-level audio faults are covered in our [audio driver crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-on-windows-11/).

### Fix 5: Reinstall the audio driver cleanly

For corruption that settings cannot reach.

1. Download the audio driver for your exact model from the manufacturer's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. In **Device Manager → Sound, video and game controllers**, uninstall the audio device with **Delete the driver software** checked.
3. Restart and install the manufacturer driver. Do not let Windows Update substitute its generic driver first — disconnect from the network during install if needed.
4. After reinstalling, redo Fixes 2 and 4 — driver installs reset formats and re-enable enhancements, which can reintroduce the exact glitch you just fixed.

### Fix 6: Stabilize power states

Timing glitches from power management.

1. Set the Windows power plan to **Best performance** (or High performance) temporarily. If crackling stops, power-state transitions were disrupting audio timing.
2. In **advanced power settings**, set **Processor power management → Minimum processor state** to **50%+** on plugged in — deep CPU sleep states cause the worst audio timing disruption.
3. Disable **USB selective suspend** if you use USB audio devices — the isochronous stream cannot survive port power cycling.
4. For a permanent setup that keeps battery life: use the high-performance plan only when doing audio-critical work, and the balanced plan otherwise. The crackling/power tradeoff is real but manageable.

### Fix 7: Address interference and hardware

When the crackling tracks physical activity.

1. If crackling intensifies with CPU/GPU load (scrolling, gaming, compiling), suspect electromagnetic interference in the onboard audio path — a design limitation, not a fault.
2. Mitigations: use a **USB DAC or USB headset** (moves audio conversion outside the noisy chassis), keep the charger on a different outlet, and disable Wi-Fi temporarily as a test.
3. For USB audio devices specifically, connect directly to the laptop (no hubs), try different ports, and disable USB power management per Fix 6.
4. If crackling persists identically across all outputs, all drivers, Safe Mode, and a USB DAC, the audio codec hardware is suspect — rare, but the exclusion is now rigorous enough to justify a repair assessment.

## Closing

Pipeline crackling is a timing problem wearing an audio disguise, which is why the fixes live in such unintuitive places — Wi-Fi drivers, CPU power states, sample rates. The output-scope test tells you whether you are even in the pipeline; LatencyMon tells you which driver is stealing the CPU time; and the sample-rate baseline gives the pipeline a stable foundation. Work the chain in order and the static gives way to silence — the good kind.
