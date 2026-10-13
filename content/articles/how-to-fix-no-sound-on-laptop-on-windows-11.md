---
title: "No Sound on Your Windows 11 Laptop? Complete Audio Fix Guide"
slug: how-to-fix-no-sound-on-laptop-on-windows-11
date: 2026-09-03
categories: ["drivers"]
tags: ["no sound", "windows 11", "audio fix", "speaker issue", "sound settings"]
description: "No sound on your Windows 11 laptop? This complete guide fixes silent speakers, missing audio devices, and driver problems on Windows 11."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why is my Windows 11 laptop suddenly silent?"
    a: "The usual suspects are the wrong output device selected in Quick Settings, a muted volume mixer entry, the Windows Audio service hanging, or a driver replaced by Windows Update. Windows 11's Quick Settings panel makes it easy to accidentally switch outputs — click the speaker icon and check the output selector first. If the icon shows a red X, it's a device/driver problem rather than settings."
  - q: "How do I open sound settings in Windows 11?"
    a: "Right-click the speaker icon in the taskbar and choose 'Sound settings,' or go to Settings → System → Sound. For the classic Sound control panel with the Playback/Recording tabs, click 'More sound settings' at the bottom of the Sound page. The volume mixer lives at Settings → System → Sound → Volume mixer, with per-app sliders."
  - q: "What should I do if Windows 11 says no output devices found?"
    a: "Open Device Manager and check 'Sound, video and game controllers' for missing or flagged audio devices. Reinstall the audio driver from your laptop maker's site, enable 'Show hidden devices' to clear ghosted entries, and verify onboard audio is enabled in BIOS. A full shutdown (not restart) with Fast Startup disabled also helps when the codec fails to enumerate."
  - q: "How do I reset all audio settings in Windows 11?"
    a: "There's no single reset button, but you can get close: Settings → System → Sound → Volume mixer → 'Reset' restores mixer levels; the classic Sound panel lets you reset device defaults per endpoint. For a full reset, uninstall the audio driver in Device Manager (deleting driver software), reboot, and reinstall the maker's driver — that rebuilds the entire audio configuration from scratch."
---

Windows 11 moved the audio furniture around — Quick Settings, a redesigned Sound page, per-app volume in a new mixer — and its update machinery is just as enthusiastic about replacing your working audio driver as Windows 10's was. When a Windows 11 laptop goes silent, you need the Windows 11-specific paths, because the old Control Panel routes still exist but the defaults have changed.
This guide is the Windows 11 edition: Quick Settings output switching, the new Sound page, the resettable volume mixer, and the driver behaviors unique to Windows 11's update model. If you're still on Windows 10, our [Windows 10 no-sound guide](/articles/how-to-fix-no-sound-on-laptop-on-windows-10/) uses that OS's interface instead. The underlying causes overlap — drivers, services, routing — but the buttons moved.
As with all audio troubleshooting, start by classifying the symptom: silent with a normal icon (routing/mute), red X on the icon (device/driver), or 'no output devices found' (enumeration). Each has its own fix section below. For crackling rather than silence, see our [audio crackling guide](/articles/how-to-fix-crackling-sound-on-laptop-after-windows-11-update/).

## Why this happens

- **Wrong output in Quick Settings.** The Win+A quick panel's output switcher silently routes audio to HDMI or Bluetooth.
- **Volume mixer mutes.** Windows 11's per-app mixer mutes individual apps with no taskbar indication.
- **Audio device disabled.** Disabled endpoints hide in the new Sound page just like the old one.
- **Windows Audio service hang.** Same old service, same old stall — total silence, normal-looking UI.
- **Driver replaced by Windows Update.** Windows 11's update cadence keeps swapping OEM audio drivers for generics.
- **Spatial sound / enhancement conflicts.** Windows Sonic or third-party spatial processing wedges the pipeline.
- **Exclusive-mode app hogging.** An app grabs exclusive control and everything else goes silent.
- **Codec enumeration failure.** Fast Startup and driver state combine to hide the audio hardware entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Quick Settings output and volume

Windows 11's fastest audio fix lives in the Quick Settings panel — thirty seconds, no digging.

1. Click the speaker/network/battery cluster (or press Windows + A) to open Quick Settings.
2. Click the arrow (>) next to the volume slider to open the output list.
3. Select your laptop's speakers explicitly — not HDMI, not a disconnected Bluetooth device.
4. Drag the volume slider up and confirm nothing shows as muted.
5. Play any audio — if it works now, an accidental output switch was the entire problem.

### Fix 2: Reset the volume mixer

Windows 11's per-app mixer is a stealth mute source — apps get muted individually with zero taskbar feedback.

1. Open Settings → System → Sound → Volume mixer.
2. Check every app slider — unmute anything muted and raise anything at zero.
3. Confirm the Output device at the top of the mixer page is your speakers.
4. Scroll down and click 'Reset' to restore all mixer levels and devices to defaults.
5. Retest with both a system sound and a browser video to cover app-level and system-level paths.

### Fix 3: Run the Windows 11 audio troubleshooter

The redesigned troubleshooter handles the common device and service faults automatically.

1. Settings → System → Sound → scroll to Advanced → Troubleshoot common sound problems → Output devices → run it.
2. Alternatively: Settings → System → Troubleshoot → Other troubleshooters → Playing Audio.
3. Let it apply recommended fixes — it re-enables devices and restarts services.
4. If it suggests a driver reinstall, let it try, but verify the result — manual reinstall (Fix 5) is more thorough.
5. Test audio immediately after it completes.

### Fix 4: Restart audio services and disable Fast Startup

Two classic fixes in one: the service restart for hangs, Fast Startup disable for enumeration gremlins.

1. Windows + R → services.msc → restart 'Windows Audio' and 'Windows Audio Endpoint Builder' (both set to Automatic).
2. Control Panel → Power Options → 'Choose what the power buttons do' → uncheck 'Turn on fast startup.'
3. Do a full Shutdown (not Restart) and power back on.
4. Check whether audio returned — Fast Startup is a notorious cause of 'no output devices found.'
5. If the speaker icon still shows a red X, continue to the driver fix.

### Fix 5: Clean-reinstall the audio driver

The heavy artillery for Windows 11 audio: strip the driver completely and install the maker's package.

1. Device Manager (Windows + X) → 'Sound, video and game controllers' → right-click audio device → Uninstall device → check 'Attempt to remove the driver for this device.'
2. Uninstall the speaker/headphone entries under 'Audio inputs and outputs' too.
3. Restart — Windows installs a base driver.
4. Install the audio driver from your laptop maker's Windows 11 support page for your exact model.
5. Confirm in the Driver tab that the OEM version is active, then test — and see our [driver-crashing guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) if the driver misbehaves after install.

### Fix 6: Tame spatial sound and enhancements

Windows 11's spatial audio and enhancement layers are frequent silence sources when they glitch.

1. Settings → System → Sound → select your speakers → set Spatial sound to Off as a test.
2. In 'More sound settings' → Playback → speakers → Properties → Enhancements → 'Disable all enhancements.'
3. Advanced tab → uncheck 'Allow applications to take exclusive control of this device.'
4. Set Default Format to 24-bit 48000 Hz or 16-bit 48000 Hz.
5. Uninstall third-party audio utilities temporarily (Nahimic, MaxxAudio, Dolby Access trials) to isolate them.

### Fix 7: Fix 'no output devices' and lock in the solution

Enumeration failures need the hardware-software boundary treatment, then protection against recurrence.

1. Device Manager → View → 'Show hidden devices' → remove ghosted audio entries → Action → 'Scan for hardware changes.'
2. Check BIOS for onboard audio enabled; install the chipset driver from the maker's site.
3. Once working, block the bad driver update via 'Show or hide updates' or the 'Do not include drivers' policy.
4. Create a System Restore point labeled with the working audio config.
5. For deeper reference, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents audio recovery options, and our [speaker crackling fixes](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/) cover the distortion side.

## Closing

Windows 11 audio troubleshooting is mostly about knowing where Microsoft moved things: Quick Settings for routing, the new Sound page for devices, the mixer reset for stealth mutes. Beyond that it's the timeless trio — restart the service, reinstall the maker's driver, block the bad update.
