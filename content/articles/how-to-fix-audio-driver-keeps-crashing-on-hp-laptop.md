---
title: "Audio Driver Keeps Crashing on HP Laptop? How to Stop It"
slug: "how-to-fix-audio-driver-keeps-crashing-on-hp-laptop"
date: 2026-09-09
categories: ["drivers"]
tags: ["audio driver crashing", "hp laptop", "sound cutting out", "realtek crash", "audio stutter"]
description: "Sound cutting out or the audio driver crashing repeatedly on your HP laptop? Stabilize the Realtek driver with clean installs, enhancement fixes, and BIOS updates."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop audio keep cutting out and coming back?"
    a: "Intermittent audio that drops and returns usually means the audio driver is crashing and Windows is restarting it. Common triggers are corrupted driver files, conflicting audio enhancement software, aggressive power management suspending the audio device, and DPC latency from another misbehaving driver. A clean reinstall of HP's audio driver plus disabled enhancements resolves most intermittent cases."
  - q: "Can audio enhancements crash the driver?"
    a: "Yes. Enhancement DSP from HP, Waves, Bang and Olufsen, or third-party apps runs inside the audio pipeline, and buggy enhancement modules are a known crash source. If crashes correlate with specific apps or with enabling spatial sound, disable all enhancements in the speaker properties as a test. Stable audio with enhancements off confirms the enhancement layer was the problem."
  - q: "Does updating the BIOS help with audio driver crashes?"
    a: "It can. The BIOS configures the audio controller's power states and interrupts, and HP BIOS updates sometimes fix the underlying power-management bugs that destabilize the audio driver. If driver reinstalls do not stop the crashes, check HP support for a BIOS update whose changelog mentions audio, and install it with the charger connected."
  - q: "What is DPC latency and how does it affect audio?"
    a: "Deferred Procedure Call latency measures how long drivers take to service hardware interrupts. When another driver hogs the CPU with high DPC latency, the audio driver misses its real-time deadlines, causing stuttering, dropouts, and sometimes crashes. Tools like LatencyMon identify the offending driver, which is often a network, storage, or GPU driver rather than the audio driver itself."
---

Audio that stutters, drops out for seconds at a time, or dies until a restart is maddening because it strikes during calls, videos, and games. On HP laptops this pattern usually means the audio driver is crashing and Windows is silently restarting it. The Device Manager may look normal between crashes, which makes the problem feel ghostly.

HP's audio stack has more moving parts than most: the Realtek base driver, HP's customizations, Waves or Bang and Olufsen enhancement layers, and sometimes third-party audio apps all share the pipeline. Any one of them can destabilize the rest. Add Windows power management suspending the audio device and you have the full recipe for intermittent crashes.

This guide stabilizes the stack from the top down: remove the enhancement conflicts, clean-install HP's driver, fix power management, then look at BIOS and latency. If the underlying symptom is [MaxxAudio failing](/articles/how-to-fix-waves-maxxaudio-not-working-on-hp-laptop/) rather than crashes, that guide covers it specifically.

## Why this happens

- **Corrupted audio driver files:** partial updates leave the driver crashing under load or at random intervals.
- **Enhancement software conflicts:** Waves, B and O, or third-party DSP modules crash inside the audio pipeline.
- **Power management suspending audio:** the audio device is powered down mid-playback and fails to resume cleanly.
- **Generic driver from Windows Update:** a non-HP driver mismatches the audio hardware and behaves unstably.
- **DPC latency from another driver:** a misbehaving network or storage driver starves the audio driver of CPU time.
- **Sample rate conflicts:** apps fighting over exclusive mode and format changes destabilize the stream.
- **BIOS power-state bugs:** firmware mishandles the audio controller's sleep states.
- **Failing audio hardware:** rare, but possible after liquid damage or board-level faults.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Disable all audio enhancements

Enhancement DSP is the most common crash trigger in the HP audio stack. Disabling it is a fast, reversible test that immediately tells you whether the enhancement layer is at fault.

1. Open Sound settings and open the speaker device properties.
2. On the Enhancements tab, check Disable all enhancements.
3. Turn off spatial sound in the Windows sound settings.
4. Close third-party audio apps like equalizers and virtual surround tools.
5. Use the laptop normally for a day and note whether crashes stop.

### Fix 2: Set a fixed audio format

Format negotiation between apps and the driver is another instability source. Locking a standard format removes the negotiation entirely.

1. In the speaker properties, open the Advanced tab.
2. Set Default Format to 24 bit, 48000 Hz.
3. Uncheck Allow applications to take exclusive control of this device.
4. Uncheck Give exclusive mode applications priority.
5. Apply and test with your usual apps.

### Fix 3: Clean-reinstall HP's audio driver

The definitive software repair. Fully remove the unstable driver and install HP's validated package for your exact model, which includes the correct enhancement integration.

1. In Device Manager, uninstall the audio device with Attempt to remove the driver checked.
2. Restart the laptop.
3. Download the Audio driver from HP support using your model or serial number.
4. Install the package and restart again.
5. Test thoroughly before reinstalling any third-party audio software.

### Fix 4: Stop power management from suspending audio

When Windows powers the audio device down to save battery, some HP configurations fail to resume it cleanly, producing the drop-and-recover pattern. Disabling the suspension stops the cycle.

1. In Device Manager, open the audio controller properties.
2. On the Power Management tab, uncheck Allow the computer to turn off this device.
3. In Power Options advanced settings, disable USB selective suspend if using USB audio.
4. Set the power plan's PCI Express Link State Power Management to Moderate or Off for testing.
5. Observe whether dropouts stop on both battery and charger.

### Fix 5: Check DPC latency for driver conflicts

If the audio driver itself is healthy, another driver may be starving it. LatencyMon reveals which driver has excessive DPC times so you can update or disable the real culprit.

1. Download and run LatencyMon while playing audio.
2. Let it run for ten minutes of normal use.
3. Check the Drivers tab for any driver with very high DPC counts.
4. Update or roll back the offending driver, often network or storage related.
5. Retest audio stability after addressing the flagged driver.

### Fix 6: Update the BIOS

HP BIOS updates sometimes fix the audio controller power sequencing that underlies repeated driver crashes. This is worth doing when driver work alone has not stabilized things.

1. Check your current BIOS version in System Information.
2. Compare with the latest on HP support for your model.
3. Download and run the BIOS update with the charger connected.
4. Do not interrupt the update process.
5. After completion, test audio on battery and on AC power.

### Fix 7: Reset audio stack and check official sources

As a final software step, reset the audio configuration to defaults and consult HP's official guidance for model-specific known issues.

1. In Sound settings, reset all devices to their default configurations.
2. Remove third-party audio devices and virtual cables you no longer use.
3. Check [HP support](https://support.hp.com/us-en) for audio advisories for your model.
4. Review audio troubleshooting on the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. If crashes persist across all of this, suspect hardware and check warranty.

## Closing

Repeated audio driver crashes on HP laptops almost always trace to the enhancement layer, a bad driver install, or power management. Disable enhancements, clean-install HP's driver, and stop the OS from suspending the audio device. That sequence stabilizes sound in the large majority of cases. For related symptoms, see our guide on [Realtek audio failures on Acer laptops](/articles/how-to-fix-realtek-audio-not-working-on-acer-laptop/). If you want extra confidence the fix holds, stress the audio path deliberately for a day: video calls, music playback, and a game session cover the different ways the driver gets exercised. Crashes that only appear under one of those point at format or exclusive-mode handling worth revisiting in the device properties. And when HP publishes a new audio driver months from now, install it manually from HP support rather than letting a generic updater do it, since the validated package is what keeps the enhancement stack and the base driver agreeing with each other.
