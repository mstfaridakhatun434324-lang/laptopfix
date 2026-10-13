---
title: "Best Way to Fix No Sound on a Laptop: Audio Repair Guide"
slug: best-way-to-fix-no-sound-on-laptop
date: 2026-09-03
categories: ["drivers"]
tags: ["no sound", "audio not working", "speakers", "realtek", "sound driver"]
description: "No sound on your laptop? Fix silent speakers and headphones with output checks, driver repair, service restarts, and audio stack resets."
thumbnail: "/images/thumbs/best-way-to-fix-no-sound-on-laptop.webp"
faqs:
  - q: "Why is there no sound on my laptop even though nothing is muted?"
    a: "The audio may be routing to the wrong output — a disconnected Bluetooth device, an HDMI monitor, or a USB headset Windows still prefers. Open Sound settings and check the output device list. Wrong-output routing is the most common cause of 'not muted but silent' and takes seconds to fix."
  - q: "Should I update or reinstall my audio driver first?"
    a: "Reinstall first. Uninstall the audio device in Device Manager, restart, and let Windows redetect it — this clears corrupted driver state. Only update to a newer driver from the manufacturer if the clean reinstall does not restore sound. Updating over corruption often preserves the problem."
  - q: "My headphones work but the speakers do not. What does that mean?"
    a: "The audio stack itself is healthy, since headphones prove it. The fault is speaker-specific: the speaker output may be disabled, its driver component may be corrupted, or the speakers themselves may have failed. Check that Speakers is the default device and enabled, then test with the manufacturer's audio driver."
  - q: "Can Windows updates break laptop audio?"
    a: "Yes, regularly. Updates replace working audio drivers with generic ones or reset the default output device. If sound died right after an update, reinstall the manufacturer's audio driver and re-check the default output device. This pattern is common enough to check first whenever timing matches."
---

No sound on a laptop is a routing problem until proven otherwise. Windows juggles multiple outputs — internal speakers, Bluetooth, HDMI, USB headsets — and it loves to send audio to a device you are not listening to. The best fix sequence starts with "where is the sound going," moves through services and drivers, and only then considers hardware. Most silent laptops are fixed in the first three steps.

Work through this guide in order. Each step eliminates a class of cause, and the order reflects what repair benches see most often.

## Why this happens

- **Wrong default output device:** Audio routes to a disconnected Bluetooth device, HDMI monitor, or USB headset instead of the speakers.
- **Corrupted audio driver:** Updates or crashes corrupt the Realtek or Intel audio driver, silencing all output.
- **Windows Audio service stopped:** The core audio services can be disabled by updates or tune-up utilities.
- **Output device disabled:** The speakers themselves can be disabled in Sound settings, hiding them from apps.
- **Application-level mute:** Individual apps can be muted in the volume mixer while the system volume looks fine.
- **Audio enhancements conflicting:** Enhancement DSPs from the OEM or Windows can break the pipeline on some driver versions.
- **Failed speaker hardware:** Blown speakers or a disconnected internal cable — real, but far less common than software causes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the output device and volume mixer

Right-click the speaker icon in the taskbar and open Sound settings. At the top, confirm the Output device is your laptop's Speakers — not a Bluetooth device, HDMI monitor, or USB headset. Click the volume icon and make sure nothing is muted. Then open the volume mixer (right-click speaker icon, Open volume mixer) and check that your specific app is not muted or set to zero there — app-level mutes are invisible in the main volume control. Play a test sound from Settings, System, Sound. If sound appears on the correct output, the "fault" was routing all along.

### Fix 2: Restart the Windows Audio services

Press Win + R, type `services.msc`, and find Windows Audio. Restart it, and set Startup type to Automatic. Do the same for Windows Audio Endpoint Builder — the Audio service depends on it, and it must be running first. These services are the foundation of all sound on the machine; when an update or utility stops them, every output goes silent simultaneously. Restart both, then test sound before touching any driver. Total silence across all outputs is the signature of a service problem, and this two-minute fix resolves it outright.

### Fix 3: Reinstall the audio driver cleanly

Open Device Manager (Win + X), expand "Sound, video and game controllers," right-click your audio device (Realtek, Intel, or similar), choose Uninstall device, and check "delete the driver software" if offered. Also expand "Audio inputs and outputs" and uninstall the speaker entries. Restart — Windows redetects the audio hardware and installs fresh drivers. Test with the built-in speakers first. This clears the corrupted driver state that updates leave behind, the state where Device Manager looks healthy but no samples reach the speakers. For persistent audio-driver crashes beyond simple silence, our guide to [audio driver crashes](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/) goes deeper.

### Fix 4: Install the manufacturer's audio driver

The generic driver Windows installs is a fallback. Go to [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/), enter your exact model, and download the audio driver package — usually Realtek with the OEM's tuning and control app. Install it and reboot. OEM audio packages include the DSP configuration matched to your laptop's speaker hardware; without it, sound can be absent, tinny, or distorted. If your model lists separate "audio driver" and "audio software" packages, install both. For Realtek-specific failures, see our focused guide on [Realtek audio not working](/articles/realtek-audio-driver-not-working-windows-11/).

### Fix 5: Disable audio enhancements and exclusive mode

In Sound settings, select Speakers, open Properties, and on the Enhancements tab check "Disable all enhancements" (or turn off Audio enhancements in Windows 11's device properties). On the Advanced tab, uncheck "Allow applications to take exclusive control of this device." Enhancement DSPs and exclusive-mode grabs are documented causes of silence and distortion on specific driver builds. Test after each change. If sound returns with enhancements off, leave them off — or update the audio driver and retest, since newer drivers sometimes fix the enhancement pipeline. This step catches the subtle software faults that survive driver reinstalls.

### Fix 6: Check disabled devices and BIOS audio

Right-click the speaker icon, choose Sound settings, then "More sound settings" to open the classic panel. On the Playback tab, right-click empty space and enable "Show Disabled Devices" — if Speakers appears greyed out, right-click and Enable it, then Set as Default Device. Then restart into the BIOS and confirm onboard audio is enabled; some firmware exposes an audio toggle that updates can flip. Save and exit. A device disabled at either level is invisible to apps but trivially fixable once found — which is why this check comes before any hardware conclusions. Microsoft's Windows support hub documents the sound-settings layout for reference.

### Fix 7: Test hardware and rule out speaker failure

Plug in wired headphones: sound in headphones but never in speakers, after all software fixes, points to the speakers or their internal cable. Run the manufacturer's hardware diagnostics audio test, which plays tones outside Windows — failure there confirms hardware. Also test a Bluetooth speaker to confirm the audio stack is fully healthy end to end. Failed internal speakers need replacement — usually a modest part but requiring chassis disassembly, a warranty job when covered. If diagnostics pass and software is clean yet speakers stay silent, an in-place Windows repair install is the final software resort before hardware service.

## Closing

Laptop silence is a routing and driver problem far more often than a speaker problem. Check the output device, restart the audio services, reinstall the driver cleanly, install the OEM package, tame enhancements, unhide disabled devices — that ladder restores sound in the overwhelming majority of cases. Keep the manufacturer's audio driver installed and glance at the output selector whenever silence strikes; it is usually just sending your sound somewhere you are not.
