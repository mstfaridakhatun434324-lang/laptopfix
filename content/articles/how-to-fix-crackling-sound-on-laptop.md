---
title: "How to Fix Crackling Sound on Your Laptop"
slug: how-to-fix-crackling-sound-on-laptop
date: 2026-09-09
categories: ["drivers"]
tags: ["crackling sound", "audio", "realtek", "stuttering audio"]
description: "Audio crackling, popping, or stuttering on your laptop? Fix it with this guide to audio drivers, enhancements, latency, and power settings."
thumbnail: "/images/thumbs/how-to-fix-crackling-sound-on-laptop.webp"
faqs:
  - q: "Why does my laptop audio crackle but headphones sound fine?"
    a: "That split points at the laptop's built-in speakers or their specific driver path rather than the audio system as a whole. Built-in speakers run through the Realtek codec with manufacturer audio enhancements applied, while USB or Bluetooth headphones use a separate driver. Try disabling audio enhancements for the speakers first — that resolves the majority of speaker-only crackling."
  - q: "Can a Windows update cause audio crackling?"
    a: "Yes, and it is one of the most common triggers. Windows updates can replace your audio driver with a generic version, re-enable audio enhancements you had turned off, or change power management behavior. If crackling started right after an update, reinstalling the manufacturer's audio driver and re-disabling enhancements usually restores clean sound."
  - q: "What is DPC latency and does it cause crackling?"
    a: "DPC latency measures how long drivers take to process deferred procedure calls. When a misbehaving driver — often Wi-Fi, storage, or GPU — hogs the CPU for too long, audio processing misses its deadline and you hear a pop or crackle. Tools like LatencyMon identify the offending driver, and updating or disabling it fixes crackling that survives every audio-specific fix."
  - q: "Will crackling damage my laptop speakers?"
    a: "Occasional software crackling will not damage speakers, but sustained loud popping at high volume can stress them over time. More importantly, persistent crackling is a symptom worth fixing rather than enduring. Turn the volume down while troubleshooting and work through the driver and enhancement fixes — the cause is software in the vast majority of cases."
---

Crackling, popping, and stuttering audio is one of the most irritating laptop problems because it ruins everything — music, calls, videos — and the cause is rarely obvious. The good news is that laptop audio crackling is a software problem the vast majority of the time. The audio hardware in modern laptops is simple and robust; the complexity lives in the driver stack, the audio enhancements layered on top, and the timing-sensitive way Windows processes sound.

Think of audio playback as a real-time assembly line: Windows must deliver sound samples to the hardware on a strict schedule, and anything that delays that delivery — a misbehaving driver, a power-saving CPU state, a pile of audio effects — produces an audible glitch. This guide attacks the problem from the most likely causes down. For the no-sound-at-all variant, see our [no sound on laptop guide](/articles/how-to-fix-no-sound-on-laptop-in-windows-11-24h2/), and for Dolby-specific issues, the [Dolby audio troubleshooting guide](/articles/how-to-fix-dolby-audio-not-working-in-windows-11-24h2/).

## Why this happens

- **Audio enhancements enabled.** Manufacturer sound effects (Dolby, Waves MaxxAudio, DTS) process every sample in real time and are the top cause of crackling.
- **Corrupted or generic audio driver.** A Windows Update-installed generic driver often performs worse than the manufacturer's tuned Realtek driver.
- **DPC latency from another driver.** Wi-Fi, storage, or GPU drivers hogging CPU time starve the audio pipeline and cause pops.
- **Mismatched sample rate.** When the system sample rate conflicts with what the app or hardware expects, resampling glitches appear as crackling.
- **CPU power-saving states.** Aggressive C-state transitions delay audio processing, especially on battery power.
- **Exclusive mode conflicts.** Apps fighting over exclusive control of the audio device cause stuttering and dropouts.
- **Failing speaker hardware.** The rarest cause — but speakers can develop voice-coil rub or loose connections that sound like crackling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable all audio enhancements

This single step fixes more crackling than everything else combined.

1. Right-click the speaker icon in the taskbar and choose **Sound settings**, then click your output device and open its **Properties** (or **Control Panel > Sound > Playback tab**, right-click the device, **Properties**).
2. On the **Enhancements** tab, check **Disable all enhancements** (or **Disable all sound effects** on Windows 11).
3. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device** and **Give exclusive mode applications priority**.
4. Click **Apply** and test. If the crackling stops, re-enable enhancements one at a time only if you miss them — most users never notice they are gone.

### Fix 2: Change the default format (sample rate)

A mismatched sample rate causes subtle, persistent crackling.

1. In the same device **Properties > Advanced** tab, look at the **Default Format** dropdown.
2. Change it to **24 bit, 48000 Hz** (or **16 bit, 44100 Hz** if 48000 is already selected) and click **Apply**.
3. Test audio after each change. The correct setting depends on your hardware; there is no universal best value, so let your ears decide.
4. If one specific app crackles while others do not, check that app's own audio output settings for a conflicting sample rate.

### Fix 3: Reinstall the manufacturer's audio driver

Replace the generic driver with the tuned one.

1. Open Device Manager, expand **Sound, video and game controllers**, right-click your audio device (usually **Realtek(R) Audio**), and choose **Uninstall device**. Check **Attempt to remove the driver** if offered.
2. Restart the laptop, then install the audio driver from your laptop manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). The manufacturer's Realtek package includes the correct codec configuration for your speakers.
3. After installing, re-check that enhancements stayed disabled — manufacturer installers sometimes re-enable them.
4. If the manufacturer's driver is old, try the newer generic Realtek driver from a reputable source as a second option, but the tuned manufacturer driver usually wins.

### Fix 4: Check DPC latency with LatencyMon

When audio fixes fail, another driver is usually the real culprit.

1. Download and run **LatencyMon** (free) and let it monitor for several minutes while playing audio.
2. Check the **Drivers** tab sorted by **DPC count** or **highest execution** — the top entries are your suspects. Common offenders: Wi-Fi drivers (ndis.sys), storage drivers (storport.sys), and GPU drivers.
3. Update the offending driver from the manufacturer's site. For Wi-Fi-related latency, our [Intel Wi-Fi fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) may help.
4. If a driver cannot be updated into good behavior, try disabling the device temporarily in Device Manager as a test — if crackling stops, you have found it.

### Fix 5: Adjust power management

Power saving and real-time audio are natural enemies.

1. Plug the laptop into AC power and set the power mode to **Best performance** (**Settings > System > Power & battery**) while testing.
2. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **Processor power management**, and raise the **Minimum processor state** to 50% or higher on AC.
3. In Device Manager, check the audio device's **Power Management** tab and uncheck power-saving options.
4. If crackling only happens on battery, the cause is confirmed as power management — keep the performance settings for AC use and accept slightly reduced battery life.

### Fix 6: Disable audio for unused devices and update the BIOS

Reduce contention and fix firmware-level timing issues.

1. In **Control Panel > Sound > Playback**, right-click every output device you do not use and choose **Disable**. Fewer active audio endpoints means less driver contention.
2. Check your laptop manufacturer's support page for a BIOS update — BIOS updates sometimes fix interrupt routing issues that manifest as audio glitches.
3. Also update the chipset driver package while you are on the support page; the audio codec hangs off the chipset.

### Fix 7: Test speakers vs. headphones to isolate hardware

The final split between software and hardware.

1. Plug in wired headphones (3.5mm, not USB/Bluetooth). If headphones are clean while speakers crackle, the problem is in the speaker path — driver, enhancements, or the speakers themselves.
2. If both crackle identically, it is system-level: driver, DPC latency, or sample rate.
3. If only the speakers crackle after every software fix, play a sine-wave test tone at moderate volume and listen for buzzing or rattling that indicates physical speaker damage — a repair shop can replace laptop speakers relatively cheaply.

## Closing

Laptop audio crackling is a timing problem wearing a sound problem's clothes, and the fix order reflects that: kill the enhancements first, fix the sample rate, reinstall the proper driver, then hunt DPC latency from other drivers. The vast majority of cases resolve in the first three steps — enhancements alone account for a remarkable share. Only when software is fully exonerated should you suspect the speakers themselves, and the headphone test gives you that answer in seconds.
