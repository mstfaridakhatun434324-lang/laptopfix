---
title: "Audio Driver Keeps Crashing on Windows? Fix It Step by Step"
slug: how-to-fix-audio-driver-keeps-crashing-step-by-step
date: 2026-09-08
categories: ["drivers"]
tags: ["audio driver", "sound crashing", "realtek", "windows 11"]
description: "Sound cuts out and the audio driver keeps crashing? Follow this step-by-step driver repair — disable enhancements, reinstall the audio stack, and stop the crashes for good."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-step-by-step.webp"
faqs:
  - q: "Why does my audio driver keep crashing on Windows 11?"
    a: "The usual causes are a corrupt audio driver installation, conflicting audio enhancement software like Dolby or Waves MaxxAudio, an unstable Windows update to the driver, or the wrong sample rate set for your playback device. Power management can also crash audio: Windows turning off the audio device to save power causes dropouts that look like driver crashes. The step-by-step fixes below address each cause in order."
  - q: "Will reinstalling the audio driver delete my sound settings?"
    a: "Yes, a full reinstall resets volume levels, default device choices, and enhancement settings to factory defaults. That's usually desirable when the driver is crashing, since corrupt settings can be part of the problem. Take a screenshot of your Sound settings first if you have a complex setup with multiple outputs, so you can restore your preferred configuration afterward."
  - q: "Can Windows Update cause audio driver crashes?"
    a: "Absolutely — Windows Update regularly replaces manufacturer audio drivers with newer generic versions that conflict with enhancement software or firmware. If crashes started right after an update, roll back the driver in Device Manager under Properties then Driver, or download the previous version from your laptop maker's support site. Pausing updates for a week prevents the bad version from reinstalling immediately."
  - q: "Is it safe to disable audio enhancements?"
    a: "Completely safe. Enhancements are post-processing effects like bass boost, virtual surround, and loudness equalization applied by the driver. Disabling them only changes how audio sounds — it doesn't affect driver stability negatively; in fact, buggy enhancement modules are a leading cause of crashes. If you rely on Dolby or similar, reinstall it fresh from the [Microsoft Store or manufacturer](https://support.microsoft.com/en-us/windows) rather than running the old version."
---

Your sound works, then it doesn't. The speaker icon shows a red X, or audio stutters into silence, and Device Manager shows the audio device with a warning — until you restart, and the whole cycle repeats an hour later. When the audio driver keeps crashing, every video call, song, and system sound becomes unreliable.

Audio crashes are driver problems in the vast majority of cases — not blown speakers. The Windows audio stack (the driver, the Windows Audio service, and enhancement layers like Dolby or Waves) has several fragile points, and this guide repairs them step by step, starting with the least invasive.

## Why this happens

- **Corrupt audio driver files:** Partial updates or disk errors leave the driver in a state where it loads, then faults under load.
- **Conflicting enhancement software:** Dolby Access, Waves MaxxAudio, DTS, and Nahimic hook into the audio pipeline and crash the driver when they misbehave.
- **Windows Update driver replacement:** A newer-but-buggier driver pushed by Windows Update breaks a previously stable setup.
- **Wrong default format / sample rate:** Mismatched sample rates between the device and applications cause the driver to reset repeatedly.
- **Power management suspending audio:** USB and PCI power-saving features cut power to the audio device mid-use, appearing as crashes.
- **Multiple audio drivers fighting:** Realtek, Intel Display Audio, and NVIDIA HD Audio can conflict when all try to manage the same output.
- **Failing Windows Audio service:** The AudioSrv service itself can get stuck, taking every audio device down with it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Windows Audio services

A stuck audio service mimics a driver crash perfectly. Restarting it is the fastest possible fix.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click it, and choose **Restart**.
3. Do the same for **Windows Audio Endpoint Builder**.
4. Test sound immediately — play a video or system sound.
5. If the services were stuck, set both **Startup type** to **Automatic** in their Properties.

If sound returns but crashes again later, the driver underneath is the real problem — continue to Fix 2. For general no-sound issues, the [no-sound troubleshooting guide](/articles/best-way-to-fix-no-sound-on-laptop/) covers the service layer in more depth.

### Fix 2: Disable all audio enhancements

Enhancement modules are the single most common crash trigger. Turning them off isolates the problem instantly.

1. Right-click the speaker icon in the taskbar and choose **Sound settings**.
2. Under **Output**, click your speakers, then scroll to **Enhance audio** and turn it **Off**.
3. Click **Advanced** and open **More sound settings** to reach the classic dialog.
4. On the **Playback** tab, double-click your speakers, go to the **Enhancements** tab, and tick **Disable all enhancements**.
5. On the **Advanced** tab, untick **Allow applications to take exclusive control of this device**.

Test for a day with enhancements off. If crashes stop, the culprit was an enhancement module — reinstall it fresh (Dolby, Waves, or your manufacturer's audio app) rather than re-enabling the old one. The [audio crash reference](/articles/audio-driver-keeps-crashing-troubleshooting/) documents which enhancement suites conflict most.

### Fix 3: Set the correct default format

Sample-rate mismatches make drivers reset in a loop, especially with external DACs and Bluetooth devices in the mix.

1. In the classic Sound dialog (**Playback** tab), double-click your output device.
2. Go to the **Advanced** tab and set **Default Format** to **24 bit, 48000 Hz (Studio Quality)** — the most compatible setting.
3. Click **Test** to confirm clean playback, then **Apply**.
4. In your most-used apps (browser, media player, conferencing app), make sure no app is forcing a different rate.

Avoid exotic rates like 192000 Hz unless your hardware specifically supports them — they destabilize marginal drivers.

### Fix 4: Update the audio driver from the manufacturer

Windows' automatic driver is often the problem. The laptop maker's driver is tuned for your exact audio codec.

1. In Device Manager, expand **Sound, video and game controllers**.
2. Note the exact device name (e.g., Realtek High Definition Audio, Intel Smart Sound).
3. Go to your manufacturer's support site — Dell, HP, or Lenovo — and download the audio driver for your exact model.
4. Install it, restart, and test.

Manufacturer drivers include the correct codec configuration and matched enhancement software. Microsoft's generic HD Audio driver works but lacks the tuning that prevents crashes on specific hardware.

### Fix 5: Fully reinstall the audio driver

When updating over the top doesn't help, wipe the driver and let Windows rebuild it cleanly.

1. In Device Manager, right-click the audio device under **Sound, video and game controllers** and choose **Uninstall device**.
2. Tick **Attempt to remove the driver for this device** and confirm.
3. Also uninstall any **Intel Display Audio** or **NVIDIA High Definition Audio** entries you don't use, to remove conflicts.
4. Restart. Windows installs a fresh base driver.
5. Then install the manufacturer's driver from Fix 4 on top.

This clears corrupt driver state, stale registry entries, and conflicting virtual devices in one pass. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the same reinstall flow if you want a second reference.

### Fix 6: Stop power management from suspending audio

Power-saving features cutting the audio device cause dropouts that look exactly like crashes.

1. In Device Manager, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub**, open **Properties > Power Management** and untick **Allow the computer to turn off this device to save power**.
3. Under **Sound, video and game controllers**, do the same for your audio device if it has a Power Management tab.
4. Go to **Settings > System > Power & battery > Power mode** and set it to **Best performance** while testing.
5. For USB headsets specifically, see the [USB selective suspend guide](/articles/best-way-to-turn-off-usb-selective-suspend/).

If crashes only happen on battery, power management is almost certainly the cause.

### Fix 7: Repair system files and check for conflicting software

If the driver is clean and crashes persist, look at the system around it.

1. Open Command Prompt as administrator and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Uninstall third-party audio tools you don't need — old versions of Nahimic, Sonic Studio, or Realtek Audio Console from unofficial sources.
3. Check **Settings > Apps** for duplicate audio drivers (two Realtek entries, for example) and remove the older one.
4. As a last resort, create a new local user account and test audio there — a corrupt user profile can carry broken audio settings.

Persistent crashes across a fresh driver, clean services, and a new user profile point to hardware — but that's rare. Most cases resolve by Fix 5.

## Closing

Audio driver crashes follow a predictable ladder: restart the service, kill the enhancements, fix the format, then reinstall the driver from the manufacturer. The enhancement layer is the surprise villain in most cases — audio that's stable with enhancements off but crashes with them on tells you exactly where to focus. Keep the manufacturer's driver pinned through Windows updates and the crashes stay gone.
