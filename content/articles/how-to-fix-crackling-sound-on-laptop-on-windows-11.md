---
title: "Crackling Sound on Your Windows 11 Laptop? How to Fix It"
slug: how-to-fix-crackling-sound-on-laptop-on-windows-11
date: 2026-09-17
categories: ["drivers"]
tags: ["crackling audio", "sound distortion", "realtek", "windows 11"]
description: "Audio crackling and popping on your Windows 11 laptop? Eliminate the distortion with these driver and settings fixes — DPC latency, sample rates, and enhancement tweaks."
thumbnail: "/images/thumbs/how-to-fix-crackling-sound-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why is my laptop audio crackling on Windows 11?"
    a: "Crackling is usually caused by DPC latency — a misbehaving driver delaying audio processing — or by mismatched sample rates, buggy audio enhancements, or power management throttling the audio device. Realtek drivers with outdated versions are frequent offenders. The fixes below isolate each cause: disabling enhancements and correcting the sample rate resolve most cases, while DPC latency tracing catches the stubborn ones caused by network or storage drivers."
  - q: "Can a Windows 11 update cause audio crackling?"
    a: "Yes. Updates regularly replace stable manufacturer audio drivers with newer generic versions that introduce crackling, particularly on Realtek codecs. If crackling started immediately after an update, roll back the audio driver in Device Manager or reinstall the manufacturer's version. Pausing updates afterward prevents Windows from reinstalling the problematic driver overnight."
  - q: "What is DPC latency and how does it cause crackling?"
    a: "Deferred Procedure Call latency measures how long drivers take to finish interrupt processing. Audio needs a steady stream of tiny data buffers; if any driver hogs the CPU for too long, audio buffers arrive late and you hear crackles or pops. Tools like LatencyMon identify the offending driver — commonly network, storage, or GPU drivers. Updating or disabling the culprit driver eliminates the crackling at its source."
  - q: "Will disabling audio enhancements reduce sound quality?"
    a: "Disabling enhancements removes post-processing effects like virtual surround and bass boost, so audio sounds flatter — but clean. If crackling disappears with enhancements off, the enhancement module was the problem; reinstall it fresh from the manufacturer rather than running the old version. Many users prefer the unprocessed sound anyway. For persistent Realtek-specific issues, see the [Realtek audio fix guide](/articles/best-way-to-fix-realtek-audio-not-working/)."
---

Crackling, popping, stuttering — your laptop's audio sounds like a worn vinyl record instead of a digital device. It happens in YouTube, in Spotify, in video calls; sometimes only on battery, sometimes only with certain apps. It's not your speakers dying. In the large majority of cases, it's a driver or settings problem with a concrete fix.

Audio crackling has a specific technical signature: the audio pipeline isn't getting its data on time. The causes range from a wrong sample rate to a completely unrelated driver hogging the CPU. This guide hunts them in order of likelihood.

## Why this happens

- **DPC latency from a misbehaving driver:** Network, storage, or GPU drivers delaying audio buffer delivery — the top cause of persistent crackle.
- **Buggy audio enhancements:** Dolby, Waves MaxxAudio, or DTS processing introducing distortion into the stream.
- **Sample rate mismatch:** Device set to a rate the driver or app handles poorly, causing resampling artifacts.
- **Outdated or generic Realtek driver:** Windows' inbox driver lacking the codec-specific fixes in the manufacturer's version.
- **Power management throttling:** CPU or device power saving starving the audio pipeline, especially on battery.
- **Exclusive mode conflicts:** Apps grabbing exclusive audio control and fighting over format.
- **Bluetooth codec issues:** For wireless audio, low-quality codec negotiation or interference causes crackle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable audio enhancements

Enhancement modules are the fastest thing to test and a leading crackle source.

1. Right-click the speaker icon and choose **Sound settings**.
2. Click your output device, then turn **Enhance audio** **Off**.
3. Open **More sound settings**, double-click the device on the **Playback** tab, go to the **Enhancements** tab, and tick **Disable all enhancements**.
4. Play the same audio that was crackling and listen.

If the crackle vanishes, an enhancement module was distorting the stream. Reinstall your manufacturer's audio app fresh if you want the effects back — don't just re-enable the old ones. The [crackling reference guide](/articles/crackling-sound-on-laptop-troubleshooting/) lists which suites cause this most.

### Fix 2: Set the correct sample rate and disable exclusive mode

Resampling and format fights produce exactly this kind of distortion.

1. In the device's **Properties > Advanced** tab, set **Default Format** to **24 bit, 48000 Hz**.
2. Untick both boxes under **Exclusive Mode** — **Allow applications to take exclusive control** and **Give exclusive mode applications priority**.
3. Click **Apply** and test.
4. If crackling persists, try **16 bit, 44100 Hz** — some codecs are cleaner at CD quality.

Avoid 192kHz and other exotic rates unless your hardware is designed for them; they stress marginal drivers.

### Fix 3: Update the audio driver from the manufacturer

Windows 11's generic driver is a frequent crackle source on Realtek codecs.

1. Identify your audio device in Device Manager under **Sound, video and game controllers**.
2. Download the audio driver for your exact laptop model from the manufacturer's support site.
3. Install it, restart, and test with enhancements still off.
4. If crackling started after a Windows update, use **Roll Back Driver** instead.

Manufacturer drivers contain codec-specific timing fixes that the generic HD Audio driver lacks. Keep this driver pinned through future updates.

### Fix 4: Trace DPC latency with LatencyMon

If the basics don't help, find which driver is delaying audio.

1. Download **LatencyMon** (free, from Resplendence) and run it as administrator.
2. Click the play button and let it monitor for 5–10 minutes while playing audio.
3. Check the **Drivers** tab sorted by **DPC count** — the top entries are your suspects.
4. Common culprits: network drivers (`ndis.sys` — update WiFi driver), storage drivers (`storport.sys` — update chipset/storage driver), GPU drivers.

Update or reinstall the offending driver. If `ndis.sys` dominates, the WiFi driver is the real villain — update it from the manufacturer's site, or test with WiFi disabled to confirm.

### Fix 5: Disable power saving on audio and CPU

Throttling starves the audio pipeline, producing crackle that worsens on battery.

1. In Device Manager, find your audio device and any USB audio entries — **Properties > Power Management** > untick **Allow the computer to turn off this device**.
2. Set **Settings > System > Power & battery > Power mode** to **Best performance** while testing.
3. In **Control Panel > Power Options > Change plan settings > Change advanced power settings**, set **Processor power management > Minimum processor state** to 50%+ on battery as a test.
4. Disable **USB selective suspend** under USB settings.

If crackling only happens on battery, you've found it — keep the audio-relevant power settings at maximum.

### Fix 6: Test with different outputs and clean boot

Isolate whether the problem is the device, the driver, or a conflicting program.

1. Plug in wired headphones or USB speakers — if they sound clean, the issue is specific to the internal speakers' driver path.
2. Test Bluetooth audio separately; Bluetooth crackle is usually codec or interference, not the system driver.
3. Perform a clean boot (`msconfig` > hide Microsoft services > disable all) and test — success means a third-party program interferes.
4. Re-enable startup items in halves to find the offender (audio routing tools, VPNs, and RGB software are common).

This step prevents you from reinstalling drivers endlessly when a background app is the actual cause.

### Fix 7: Reinstall the audio stack completely

The deep clean for stubborn crackle.

1. In Device Manager, uninstall the audio device under **Sound, video and game controllers**, ticking **Attempt to remove the driver**.
2. Uninstall related entries: **Intel Smart Sound**, **Intel Display Audio**, **NVIDIA HD Audio** if unused.
3. Restart — Windows installs base drivers.
4. Install the manufacturer's audio driver, then the chipset driver, then test.
5. Run `sfc /scannow` in an admin Command Prompt to repair any corrupt system audio files.

If crackle survives a full stack reinstall, clean boot, and LatencyMon-guided driver updates, suspect the speaker hardware — but test with the manufacturer's hardware diagnostics before concluding that. For Realtek-specific persistent issues, the [Realtek guide](/articles/best-way-to-fix-realtek-audio-not-working/) goes deeper. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) also documents the system-file repair commands used above.

## Closing

Crackling audio is a timing problem, and timing problems have findable causes: enhancements distorting the stream, wrong sample rates, or a rogue driver hogging DPC time. The enhancement toggle and LatencyMon resolve the vast majority of cases — and once the audio runs clean, keeping the manufacturer's driver installed stops Windows Update from reintroducing the crackle.
