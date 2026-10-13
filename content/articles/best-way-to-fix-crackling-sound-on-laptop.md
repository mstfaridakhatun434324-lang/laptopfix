---
title: "Crackling Sound on Your Laptop? The Best Way to Fix It for Good"
slug: best-way-to-fix-crackling-sound-on-laptop
date: 2026-09-01
categories: ["drivers"]
tags: ["crackling audio", "sound driver", "realtek", "dpc latency", "audio fix"]
description: "Pops, crackles, and distortion ruining your laptop audio? Find out whether it's a driver, a setting, or latency — and silence it permanently."
thumbnail: "/images/thumbs/best-way-to-fix-crackling-sound-on-laptop.webp"
faqs:
  - q: "What causes crackling sound on a laptop?"
    a: "The usual causes are audio enhancements processing overloading the driver, a mismatched sample rate between Windows and the app, DPC latency spikes from misbehaving drivers stealing CPU time, or a damaged audio driver. Hardware causes like failing speakers or loose cables are possible but less common."
  - q: "Why does my audio only crackle on battery power?"
    a: "Power-saving features throttle the CPU and put audio hardware into low-power states, which can starve the audio pipeline. If crackling appears only on battery, disable CPU power-saving for audio and set the power mode to Best performance while testing to confirm."
  - q: "Can a Windows update cause crackling audio?"
    a: "Yes, and it's common. Updates can replace a working audio driver with a generic one, reset audio enhancements to defaults, or change the default sample rate. If crackling started right after an update, roll back or reinstall the audio driver and re-check your audio settings."
  - q: "Is crackling always a driver problem?"
    a: "No. If crackling persists with headphones, through Bluetooth, and after a clean driver reinstall, suspect DPC latency from another driver — commonly network or storage drivers — or actual speaker hardware damage. Testing multiple outputs is how you tell these apart, and the free LatencyMon tool can name the exact offending driver when latency is the cause."
---

Crackling, popping, stuttering — audio distortion on a laptop is maddening because it ruins everything: calls, music, video, games. And it's rarely obvious whether the speakers are dying, the driver is broken, or some invisible setting is mangling the sound. The good news is that the vast majority of crackling is software, and software can be fixed without opening the machine.

The diagnostic key is pattern: crackling that follows the speakers everywhere points at the audio pipeline; crackling that appears only on certain outputs or power states narrows the suspect list fast. Here's the full path.

## Why this happens

- **Audio enhancements are overloading the driver.** Bass boost, loudness equalization, and vendor effects (MaxxAudio, DTS, Dolby) process every sound in real time. When they glitch, you get crackle.
- **Sample rate mismatch.** Windows is set to 48000 Hz while the app outputs 44100 Hz (or vice versa), forcing constant resampling that can introduce artifacts.
- **DPC latency spikes.** A misbehaving network, storage, or USB driver can monopolize the CPU for milliseconds at a time, starving the audio stream. This is the classic cause of crackle that survives driver reinstalls. Compare with [audio drivers that crash outright](/articles/how-to-fix-realtek-audio-not-working-in-windows-11-24h2/).
- **Corrupted or generic audio driver.** Windows Update replacing your vendor driver with a generic High Definition Audio driver is a top cause of new-onset crackling.
- **Power-saving CPU throttling.** On battery, aggressive power plans can starve the audio pipeline of CPU time, producing crackle that vanishes when plugged in.
- **Failing speakers or loose internal cables.** Physical causes exist: blown speaker cones buzz at certain frequencies, and a loose speaker connector crackles when you move the laptop.
- **Exclusive mode conflicts.** An app grabbing exclusive control of the audio device can fight with system sounds and other apps.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Isolate where the crackling lives

Two minutes of testing saves an hour of wrong fixes.

1. Play the same audio through **headphones** (wired). If the crackle disappears, the problem is the built-in speakers or their amplifier — skip to Fix 7.
2. Try a **Bluetooth** speaker or headset. Crackle on all outputs points to the audio pipeline (Fixes 2–5); crackle only on built-in speakers points to hardware.
3. Test on **battery vs. plugged in**. Crackle only on battery = power management (Fix 5).
4. Test in **Safe Mode with Networking**. Clean audio in Safe Mode means a third-party driver or app is interfering.

### Fix 2: Disable all audio enhancements

The single highest-yield software fix for crackling.

1. Right-click the **speaker icon** in the taskbar > **Sound settings** > scroll to **More sound settings**.
2. In the Sound window, select your output device and click **Properties**.
3. Go to the **Enhancements** tab and check **Disable all enhancements** (or **Disable all sound effects**).
4. If your laptop has vendor audio software (Waves MaxxAudio, DTS, Dolby Access, Bang & Olufsen), open it and turn off all effects there too — these process audio independently of Windows.
5. Retest. If the crackle is gone, re-enable effects one at a time to find the offender.

### Fix 3: Fix the sample rate and exclusive mode

Resampling artifacts and mode fights both sound like crackle.

1. In the same device **Properties** window, go to the **Advanced** tab.
2. Set **Default Format** to **24 bit, 48000 Hz (Studio Quality)** — this matches what most apps and streaming services output.
3. **Uncheck** both boxes under **Exclusive Mode** ("Allow applications to take exclusive control of this device"). This stops apps from fighting over the audio device.
4. Click **Apply**, then retest with your usual apps.
5. If you use a DAW or pro audio app, set its internal sample rate to match 48000 Hz to avoid its own resampling layer.

### Fix 4: Reinstall the audio driver cleanly

When enhancements and formats aren't the cause, the driver is next.

1. Open **Device Manager** > **Sound, video and game controllers**. Right-click your audio device (often Realtek) and choose **Uninstall device**, checking "Attempt to remove the driver" if offered.
2. Restart. Windows will install a generic driver — test with it. Generic drivers lack enhancements, which conveniently also tests Fix 2's theory.
3. If the generic driver is clean, download the proper driver from your laptop maker's support site — for example [Dell support](https://www.dell.com/support) — and install it manually.
4. After installing the vendor driver, immediately re-verify that enhancements are still disabled (driver installs re-enable them).

### Fix 5: Kill DPC latency and power throttling

For crackle that survives a driver reinstall.

1. Download the free **LatencyMon** utility and run it for a few minutes while playing audio. It names the specific driver causing latency spikes — often `ndis.sys` (network), `storport.sys` (storage), or a USB driver.
2. Update or disable the offending driver per LatencyMon's report. Network drivers are the most common culprits; update them from the vendor, not Windows Update.
3. Go to **Settings** > **System** > **Power & battery** > **Power mode** and set **Best performance** while testing.
4. In **Device Manager**, check the audio device's **Power Management** tab and disable "Allow the computer to turn off this device to save power."
5. Our guide on [persistent speaker crackling](/articles/how-to-fix-speakers-crackling-on-laptop-in-windows-11-24h2/) covers additional latency-hunting techniques.

### Fix 6: Check for app-specific and browser causes

Sometimes only one app crackles.

1. If crackle happens only in a browser, disable hardware acceleration in the browser's settings and test again.
2. In **Settings** > **System** > **Sound** > **Volume mixer**, check per-app volumes — an app maxed at 100% with system volume also high can clip and crackle.
3. For music apps, disable any in-app equalizer or normalization as a test.
4. Update the app itself; audio pipeline bugs in specific app versions are common and get fixed quietly.

### Fix 7: Verify speaker hardware

The last resort — only after the software path is clean.

1. Play a **frequency sweep** (search for one online) at moderate volume. Buzzing or rattling at specific frequencies indicates a damaged speaker cone.
2. Press gently around the speaker grilles while audio plays. If the crackle changes with pressure, a speaker is loose or its mount is broken.
3. Open the laptop (if you're comfortable) and reseat the speaker connector on the motherboard — a partially seated connector crackles with vibration.
4. Replacement internal speakers are usually inexpensive parts; the labor is the cost. For most users, quality external speakers or headphones are the pragmatic fix.

Microsoft's audio troubleshooting steps are documented on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Crackling audio is almost always the pipeline, not the speakers: enhancements overprocessing, sample-rate mismatches, a replaced driver, or latency spikes from an unrelated driver. Isolate the output first, then strip the processing, then rebuild the driver, then hunt latency. That sequence resolves the overwhelming majority of cases — and the few that survive it have identified themselves as hardware, which is its own answer.
