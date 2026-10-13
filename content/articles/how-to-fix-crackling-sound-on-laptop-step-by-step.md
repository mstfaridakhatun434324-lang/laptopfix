---
title: "Crackling Sound on Laptop? Step-by-Step Audio Fix"
slug: how-to-fix-crackling-sound-on-laptop-step-by-step
date: 2026-09-23
categories: ["drivers"]
tags: ["audio", "crackling sound", "realtek", "drivers", "troubleshooting"]
description: "Audio crackling, popping, or stuttering on your laptop? Fix crackling sound step by step — audio drivers, sample rates, enhancements, and DPC latency."
thumbnail: "/images/thumbs/how-to-fix-crackling-sound-on-laptop-step-by-step.webp"
faqs:
  - q: "Why does my laptop audio crackle only sometimes?"
    a: "Intermittent crackling usually points to DPC latency — background drivers briefly starving the audio stream — or power management throttling the audio hardware. It often appears when the CPU ramps up or down, when Wi-Fi is active, or on battery. Consistent crackling, by contrast, usually means a sample-rate mismatch or a bad driver."
  - q: "Can a Windows update cause audio crackling?"
    a: "Yes, and it's one of the most common triggers. Windows updates frequently replace vendor audio drivers with generic ones or reset sample rates and enhancements. If crackling started right after an update, rolling back the audio driver or reinstalling the vendor driver usually fixes it immediately."
  - q: "Does Bluetooth audio crackle for different reasons?"
    a: "Bluetooth crackling is usually about the wireless link — interference, distance, or codec negotiation — rather than the laptop's audio driver. If wired audio is clean but Bluetooth crackles, troubleshoot the Bluetooth connection and audio codec instead of the steps in this guide."
  - q: "Will a USB DAC fix laptop audio crackling?"
    a: "Often yes, because a USB DAC bypasses the laptop's internal audio hardware and its driver entirely. If crackling persists through a USB DAC or USB headset, the problem is in the audio stream itself — sample rate, app, or system latency — rather than the onboard audio chip."
---

Crackling, popping, and stuttering audio is one of those problems that makes a laptop feel broken even when everything else works. Music stutters, video calls pop, and every notification sounds like it's coming through a broken speaker. The maddening part is the inconsistency: it might happen only on battery, only in one app, or only when the Wi-Fi is busy.

Audio crackling is almost never a broken speaker — it's the audio *stream* getting interrupted before it reaches the speaker. Something in the chain — the driver, the sample rate, a background process hogging the CPU, or power management — starves the audio buffer for a few milliseconds, and you hear it as a pop. Fix the starvation and the crackle disappears.

## Why this happens

- **Sample rate mismatch:** app and device disagree on sample rate, causing resampling glitches.
- **Audio enhancements:** vendor "enhancement" processing introduces latency and distortion.
- **DPC latency spikes:** misbehaving drivers briefly block the audio thread.
- **Outdated or generic audio driver:** Windows replaced the vendor driver with a basic one.
- **Power management throttling:** CPU or audio hardware downclocks starve the audio buffer.
- **Exclusive mode conflicts:** an app grabs exclusive control and fights other audio.
- **Corrupt audio stack:** the Windows audio service or driver binding is damaged.
- **Electromagnetic interference:** Wi-Fi and power circuits induce noise in analog audio paths.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable audio enhancements

1. Right-click the speaker icon in the taskbar and choose **Sound settings**.
2. Select your output device, then click into its properties and find the **Enhancements** or **Audio enhancements** section.
3. Turn enhancements **off**. Realtek, Waves MaxxAudio, and Dolby processing are frequent crackle sources.
4. Test audio immediately — this single toggle fixes a large share of crackling cases.
5. If your vendor utility (Dell Audio, Lenovo Smart Performance) has its own enhancement toggles, disable those too.
6. Re-enable features one at a time later if you miss them; you'll find which one crackles.

### Fix 2: Match the sample rate

1. In the device properties, go to **Advanced** and look at **Default Format** (sample rate and bit depth).
2. Set it to **24-bit, 48000 Hz** — the most compatible choice for modern Windows audio.
3. Avoid exotic rates like 192000 Hz unless your hardware genuinely supports them; they increase the chance of resampling glitches.
4. In your audio apps (DAW, media player), set the output sample rate to match 48000 Hz.
5. Uncheck both **Exclusive mode** options on the Advanced tab during testing — exclusive-mode grabs cause conflicts.
6. Crackling that disappears after this was a resampling problem, not a hardware problem.

### Fix 3: Reinstall the audio driver properly

1. Open **Device Manager**, expand **Sound, video and game controllers**, and note your audio device (usually Realtek).
2. Right-click it, choose **Uninstall device**, and check "Attempt to remove the driver for this device."
3. Reboot — Windows will install a basic driver. Test: if crackling is gone, the vendor driver was the problem.
4. For the permanent fix, download the audio driver from your laptop manufacturer's support page rather than relying on Windows Update's version.
5. Realtek driver issues are common enough to have their own guide — see [Realtek audio driver not working on Windows 11](/articles/realtek-audio-driver-not-working-windows-11/) for the deep version.
6. Avoid "driver updater" utilities; they frequently install mismatched audio drivers.

### Fix 4: Hunt down DPC latency spikes

1. Download LatencyMon (free) and run it for a few minutes while audio crackles.
2. Look at the **Drivers** tab sorted by DPC count — the top offender is starving your audio.
3. Common culprits: network drivers (Wi-Fi especially), storage drivers, and GPU drivers.
4. Update the offending driver from the manufacturer's site. Wi-Fi driver updates fix a surprising amount of audio crackling.
5. As a test, disable Wi-Fi temporarily — if crackling stops, you've confirmed a network-driver DPC issue.
6. Persistent high DPC from `storport` or `ndis` after updates may need the specific driver version that predates the problem.

### Fix 5: Fix power management behavior

1. Test on charger vs. battery — crackling that appears only on battery is a power-plan issue.
2. Go to **Settings > System > Power & battery** and set power mode to **Best performance** for testing.
3. In Device Manager, find your audio device's **Power Management** tab (if present) and uncheck "Allow the computer to turn off this device to save power."
4. Check the vendor power utility for audio or USB power-saving features and disable them.
5. In advanced power settings, set **USB selective suspend** to Disabled — USB audio devices are sensitive to it.
6. If the crackling follows the power state this reliably, you've found a configuration issue, not broken hardware.

### Fix 6: Restart the Windows audio stack

1. Press **Win + R**, type `services.msc`, and restart the **Windows Audio** and **Windows Audio Endpoint Builder** services.
2. If crackling stops after a restart but returns later, something is corrupting the audio stack over time — usually a driver leak.
3. Run the built-in troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Audio**.
4. As a deeper reset, open an admin Command Prompt and run `sfc /scannow` to repair corrupted system audio components. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in audio troubleshooters as well.
5. Audio stack corruption often travels with other driver issues — [audio driver crashes](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) cover the case where the driver itself keeps dying.

### Fix 7: Isolate hardware vs. software

1. Test with wired headphones, then with Bluetooth, then with the built-in speakers — note exactly which outputs crackle.
2. If only the speakers crackle but headphones are clean, it's the speaker hardware or its amplifier path.
3. Try a USB headset or USB DAC: clean audio there proves the internal audio hardware/driver is the problem.
4. Boot into BIOS and check for beep-test or audio diagnostics — some vendors include them.
5. If every output crackles identically even through USB, the problem is upstream: sample rate, app, or system latency.
6. Genuine speaker failure is rare compared to driver issues, so only conclude hardware after the software steps fail.

## Closing

Audio crackling feels like broken hardware, but the statistics say otherwise — it's overwhelmingly drivers, sample rates, enhancements, and DPC latency. The fastest wins are disabling enhancements and matching the sample rate, which take two minutes combined and resolve a huge fraction of cases. If those don't do it, LatencyMon will name the misbehaving driver for you, which beats guessing every time. Work the list, trust the evidence of which outputs crackle and when, and you'll get clean audio back without replacing anything.
