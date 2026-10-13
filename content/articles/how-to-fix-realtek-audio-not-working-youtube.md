---
title: "Realtek Audio Not Working? Fix Your Laptop's Sound in Minutes"
slug: how-to-fix-realtek-audio-not-working-youtube
date: 2026-09-03
categories: ["drivers"]
tags: ["realtek audio", "realtek driver", "no sound laptop", "audio not working"]
description: "Realtek audio gone silent? Learn why your laptop lost sound and fix it with the right Realtek HD audio driver, correct playback settings, and simple service restarts."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-youtube.webp"
faqs:
  - q: "Why does Realtek audio stop working after a Windows update?"
    a: "Windows Update frequently replaces the laptop maker's tuned Realtek driver with a generic Microsoft High Definition Audio driver that lacks the codec configuration for your machine. The generic driver can silence speakers, disable the microphone array, or kill audio enhancements. Reinstalling the Realtek driver from the laptop maker restores the correct codec setup."
  - q: "Should I use the Realtek driver from Windows Update or my laptop maker?"
    a: "Use the laptop maker's Realtek driver. Realtek ships reference drivers, but each laptop maker customizes the driver package for its specific audio codec, speaker tuning, and microphone array. The maker's package includes the correct INF files and control panel. Windows Update's generic version is only a stopgap when no maker driver exists."
  - q: "What is the difference between Realtek HD Audio and High Definition Audio Device?"
    a: "Realtek HD Audio is the full vendor driver with codec-specific tuning, the Realtek Audio Console, and advanced effects. High Definition Audio Device is Microsoft's generic class driver — it produces sound on most hardware but misses vendor tuning, microphone beamforming, and jack detection. If Device Manager shows the generic name, your Realtek driver was replaced."
  - q: "Can a corrupted Realtek driver cause no sound at all?"
    a: "Yes. A partially installed or corrupted Realtek driver can leave the audio endpoint in a failed state where Windows shows the speaker icon with a red X or reports no output device installed. Uninstalling the driver completely — including deleting the driver software — then installing a fresh copy from the laptop maker clears the corrupted state."
---

Realtek audio chips handle sound on the vast majority of Windows laptops, and when the Realtek driver breaks, the silence is total: no speakers, no headphone jack output, sometimes no microphone either. The pattern is so consistent that most cases trace back to one event — a Windows Update that swapped the working Realtek driver for a generic one, or a driver install that went wrong halfway.

The good news is that Realtek audio failures are almost never hardware. The codec is a tiny chip soldered to the board and it rarely dies; what dies is the driver package sitting on top of it. Because the failure is software, it is fixable, and the fix order matters: verify the simple output settings first, then repair the driver, then dig into services and the BIOS if needed.

## Why this happens

- **Windows Update replaced the Realtek driver** with the generic High Definition Audio driver, losing codec tuning.
- **Corrupted or half-installed Realtek driver** leaves the audio endpoint in a failed state.
- **Wrong default playback device** selected, so audio routes to a phantom or disconnected output.
- **Audio enhancements or exclusive mode** conflicting with the Realtek codec and muting output.
- **Windows Audio services (Audiosrv) stopped or stuck**, so no sound engine runs at all.
- **Microphone privacy settings blocking all audio apps**, which looks like a hardware failure.
- **BIOS audio controller disabled** or a firmware bug after a BIOS update.
- **Failed Realtek Audio Console / app**, breaking jack detection and speaker configuration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the output device and volume basics

Before touching drivers, confirm Windows is sending audio to the right place. Right-click the speaker icon, open Sound settings, and verify the Realtek speakers are the default output. Check that the volume slider is up and that the app you are testing is not muted in the volume mixer. This takes thirty seconds and catches the cases where audio is simply routed to a disconnected monitor or Bluetooth device.

1. Right-click the speaker icon and open Sound settings.
2. Set Realtek speakers (or your laptop's speakers) as the default output.
3. Open the volume mixer and unmute the app you are testing.
4. Play a test tone from Settings > System > Sound.

### Fix 2: Restart the Windows Audio services

If the basics check out, restart the audio engine itself. The Windows Audio service and the Windows Audio Endpoint Builder occasionally wedge after updates or sleep cycles, and a restart clears the jam without changing any files. If the service refuses to stay running, that points at a deeper driver problem — which the later fixes address. Microsoft's official audio troubleshooting guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Press Win + R, type `services.msc`, and press Enter.
2. Restart the Windows Audio service.
3. Restart the Windows Audio Endpoint Builder service.
4. Test sound immediately after the restart.

### Fix 3: Disable audio enhancements and exclusive mode

Realtek drivers ship with enhancements (bass boost, virtualization, loudness equalization) that can corrupt the audio stream on some codec revisions. In the speaker properties, turn enhancements off entirely, and on the Advanced tab uncheck both exclusive-mode boxes. These two checkboxes are responsible for a surprising share of silent-speaker cases, especially after driver updates that reset them.

1. Open Sound settings > the speaker device > Properties.
2. On the Enhancements tab, check 'Disable all enhancements'.
3. On the Advanced tab, uncheck both exclusive-mode options.
4. Apply, then test with a video or music file.

### Fix 4: Reinstall the Realtek driver from the laptop maker

This is the highest-yield fix. Download the audio driver from the laptop maker's support page for your exact model — not from Realtek directly and not from Windows Update. In Device Manager, uninstall the Realtek audio device and tick 'Delete the driver software', then install the maker's package and reboot. If your speakers produce distorted sound rather than silence, the companion guide on [speaker crackling after updates](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/) covers the distortion-specific settings.

1. Download the Realtek audio driver from the laptop maker's support page.
2. In Device Manager, uninstall the Realtek device, deleting the driver software.
3. Install the downloaded driver package and reboot.
4. Verify the device name now reads 'Realtek HD Audio' or similar.

### Fix 5: Roll back or update via the driver store

If the latest maker driver is the problem (rare but possible), roll back: in Device Manager, open the Realtek device properties and use Roll Back Driver. Conversely, if the maker driver is years old, grab a newer reference build from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) by searching for your codec (ALC2xx/ALC8xx). Pick the newest package matching your Windows version and architecture, install it, and reboot.

1. Try Roll Back Driver first if the option is available.
2. Otherwise search the Update Catalog for your Realtek codec number.
3. Download the newest package for your Windows version (x64).
4. Install it and reboot, then retest audio.

### Fix 6: Check privacy settings and the Realtek Audio Console

Windows privacy settings can block every app from using audio input, which mimics a dead microphone — and a broken Realtek Audio Console can break jack detection so headphones are never recognized. Go to Settings > Privacy & security > Microphone and make sure access is on. Then open the Microsoft Store version of Realtek Audio Console (or reinstall it from the maker's site) and confirm the jack is detected when you plug in headphones. For microphone-specific trouble, see the [Realtek driver overview](/articles/realtek-audio-driver-not-working-windows-11/).

1. Enable microphone access in Settings > Privacy & security > Microphone.
2. Reinstall Realtek Audio Console from the maker or Microsoft Store.
3. Plug in headphones and confirm jack detection in the console.
4. Re-run the app that had no sound.

### Fix 7: Check the BIOS and test for hardware failure

If Device Manager shows no audio device at all — not even with hidden devices shown — enter the BIOS and confirm the onboard audio/HD audio controller is enabled. A BIOS update sometimes flips this setting. If the controller is enabled and the driver still will not bind, boot a Linux live USB: sound there proves the codec works and Windows is at fault; no sound there means the codec or its board circuitry has failed, which is a board-level repair.

1. Enter the BIOS and verify onboard/HD audio is enabled.
2. In Windows, show hidden devices and look for any audio device.
3. Boot a Linux live USB and test the speakers.
4. No sound in Linux either means a hardware repair is needed.

## Closing

Realtek audio failures look dramatic but are software problems in roughly nine cases out of ten. The recurring villain is the driver swap: Windows Update replaces the laptop maker's tuned Realtek package with a generic driver, and the codec's specific configuration goes with it. The cure is equally consistent — delete the wrong driver completely and install the maker's package for your exact model. Once sound is back, take two preventive steps: keep a copy of the working driver installer on the machine, and consider pausing Windows' automatic driver updates if you have been burned twice. Audio drivers are small files, and the known-good installer turns the next silent morning into a five-minute fix instead of another round of guesswork.
