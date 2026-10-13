---
title: "Microphone Not Working on Windows 10? Restore Recording"
slug: how-to-fix-microphone-not-working-on-laptop-on-windows-10
date: 2026-10-03
categories: ["drivers"]
tags: ["microphone", "mic not working", "windows 10", "recording"]
description: "Fix a dead microphone on Windows 10: enable recording devices, fix privacy settings, reinstall audio drivers, and test the hardware."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop-on-windows-10.webp"
faqs:
  - q: "Where is the microphone setting in Windows 10?"
    a: "Right-click the speaker icon and choose Sounds, then open the Recording tab — that is the classic control panel for microphones. The modern path is Settings, then Privacy, then Microphone for permissions, and Settings, then System, then Sound for device selection. Both paths matter: the old panel manages device state, the new one manages permissions."
  - q: "Why does my mic work in Zoom but not in Chrome?"
    a: "Browser microphone permission is separate from Windows permission. Chrome asks for mic access per site, and a denied or dismissed prompt leaves the browser silent while desktop apps work fine. Click the lock icon in Chrome's address bar on the site and set the microphone to Allow."
  - q: "How do I test my microphone on Windows 10?"
    a: "Open Voice Recorder from the Start menu and record a few seconds — the waveform shows whether input arrives. Alternatively, in the Sound control panel's Recording tab, speak and watch the green level bars next to the device. Moving bars mean the system path works and the problem is app-specific."
  - q: "Can a Windows 10 update disable my microphone?"
    a: "Yes. Cumulative updates have reset microphone privacy permissions and replaced audio drivers with versions that mishandle capture. When the mic dies right after Patch Tuesday, check privacy settings first and the audio driver second — the timing is rarely a coincidence."
---

A microphone that stops working on Windows 10 tends to reveal itself embarrassingly: you join a call, speak confidently, and learn minutes later that nobody heard a word. The speakers work, the camera works, but your voice goes nowhere. Windows 10 manages microphones through an older dual system — the classic Sound control panel for device state and the modern Settings app for privacy — and a failure in either half silences you completely.

The usual suspects are well known to anyone who has maintained Windows 10 machines: privacy permissions reset by an update, the wrong recording device set as default, the microphone disabled in the Recording tab, or an audio driver that handles playback fine while the capture path stays broken. Hardware failure is possible but sits at the bottom of the probability list.

The order below separates the layers efficiently: device state in the classic panel, privacy in Settings, app-level selection, driver repair, and finally hardware verification.

## Why this happens

- **Microphone disabled in the Recording tab:** The classic Sound panel lets recording devices be disabled independently. A disabled mic never appears in modern Settings, making it invisible to casual checks.
- **Privacy permissions reset by an update:** Windows 10 updates can revoke microphone access globally or per app. The driver is healthy; Windows is simply refusing to share the mic.
- **Wrong default recording device:** With multiple inputs — headset, webcam, built-in array — Windows may default to an unplugged or wrong device while the real mic sits idle.
- **App-level device or permission wrong:** Browsers and conferencing apps have their own mic selectors and permission prompts, independent of Windows settings.
- **Audio driver capture path broken:** A corrupted or generic audio driver can play sound perfectly while the recording side fails silently.
- **Microphone level set to zero or muted:** The Recording tab's level slider and mute checkbox are easy to disturb accidentally and hard to notice afterward.
- **Hardware failure:** A damaged mic array or loose cable kills input in every OS. Failure after a drop or spill points here.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the mic in the classic Recording tab

The old Sound panel is where device state lives. Start here, not in Settings.

1. Right-click the speaker icon and choose Sounds, then open the Recording tab.
1. Right-click the empty area and check Show Disabled Devices and Show Disconnected Devices.
1. Right-click your microphone, choose Enable, then Set as Default Device. Speak and watch the level bars move.

### Fix 2: Check levels and mute state

A working but silent mic is often just turned down to nothing.

1. In the Recording tab, double-click the microphone and open the Levels tab.
1. Set the level to 80 or above and confirm the speaker icon shows unmuted.
1. Test again. If the bars move now, the fix was embarrassingly simple.

### Fix 3: Verify Windows 10 privacy permissions

Windows can gate the mic even when the device is perfect. Clear the gate.

1. Open Settings, then Privacy, then Microphone.
1. Turn on Allow apps to access your microphone.
1. Review the per-app list and enable your specific apps. Desktop apps need the Allow desktop apps toggle as well.

### Fix 4: Set the right device in your app

With Windows configured, make sure the app is listening to the right input.

1. Open the app's audio or voice settings — not just the system settings.
1. Explicitly select your microphone rather than Default communications device.
1. In browsers, click the lock icon in the address bar and set the microphone to Allow for the site. If audio output devices also misbehave, the [headphone detection guide](/articles/how-to-fix-laptop-not-detecting-headphones-after-windows-11-update/) covers the adjacent output-side troubleshooting.

### Fix 5: Reinstall the audio driver

When the device is enabled, permissions are granted, and still nothing records, the driver's capture path is the suspect.

1. In Device Manager, expand Sound, video and game controllers.
1. Uninstall the audio device, checking Delete the driver software, then restart.
1. Install the audio driver for your exact model from the vendor's support site — not the generic Windows pick. For the newer OS with its own permission model, see [microphone fixes on Windows 11](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/).

### Fix 6: Test with Voice Recorder to isolate

Use the simplest possible app to separate system problems from app problems.

1. Open Voice Recorder and record ten seconds of speech.
1. A visible waveform means the system path works — the original app was at fault.
1. A flat line after all the fixes above means the problem is below the apps: driver or hardware.

### Fix 7: Verify the hardware outside Windows

The definitive test removes Windows from the equation entirely.

1. Boot a live Linux USB and test the microphone there.
1. Working in Linux proves the hardware is fine and the issue is Windows configuration or drivers.
1. Dead in Linux too means the mic array or its connection needs service. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in recording troubleshooter for any remaining software checks.

### Fix 8: Run the Recording Audio troubleshooter

Windows 10 includes an automated troubleshooter for recording audio that checks device state, levels, driver problems, and permissions in one pass. It occasionally catches misconfigurations that manual checks miss, such as a device disabled in a way the Sound panel does not show clearly. It costs two minutes and is worth running before hardware tests.

1. Open Settings, then Update and Security, then Troubleshoot, then Additional troubleshooters.
1. Run the Recording Audio troubleshooter and apply any fixes it recommends.
1. Test with Voice Recorder afterward to confirm the system path works.

## Closing

Windows 10 microphone failures are almost always found in the gap between the two settings systems: the classic Recording tab says disabled while modern Settings says everything is fine, or privacy silently revokes what the driver happily provides. Check device state, permissions, app selection, and the driver in that order, and confirm with Voice Recorder. The mic that missed the meeting is usually back before the next one — no new hardware required.
