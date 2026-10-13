---
title: "Realtek Microphone Not Working? Step-by-Step Fix for Windows Laptops"
slug: "how-to-fix-realtek-microphone-not-working-step-by-step"
date: "2026-09-12"
categories: ["drivers"]
tags: ["realtek microphone", "mic not working", "audio driver", "windows 11", "recording device"]
description: "Realtek microphone not picking up sound? Step-by-step fixes for driver issues, privacy settings, disabled devices, and audio enhancements that silence your mic."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-step-by-step.webp"
faqs:
  - q: "Why is my Realtek microphone detected but not picking up any sound?"
    a: "The most common cause is Windows privacy settings blocking microphone access, followed by the device being disabled in Sound settings and audio enhancements interfering with the input stream. A corrupted Realtek driver can also leave the mic visible but silent. Check Settings > Privacy & security > Microphone first, then verify the device is enabled and set as default in the classic Sound control panel."
  - q: "Should I use the Realtek driver from my laptop maker or a generic one?"
    a: "Use your laptop maker's Realtek audio package. Manufacturers customize it with the correct pin configurations for your specific microphone hardware, and a generic Realtek driver can map the inputs wrong, leaving the mic silent. Download the audio driver for your exact model from the manufacturer's support site and do a clean install over the existing driver."
  - q: "Can Windows updates break the Realtek microphone?"
    a: "Yes, this is one of the most reported causes. Windows Update frequently replaces the manufacturer's Realtek driver with a newer generic build that mishandles the microphone array or disables the front-panel jack detection. Rolling back the driver in Device Manager or reinstalling the manufacturer's package resolves it. Disabling automatic driver updates prevents recurrence."
  - q: "My mic works in one app but not another. What causes that?"
    a: "This is an app-permission or exclusive-mode issue, not a driver failure. Check Settings > Privacy & security > Microphone and confirm the specific app is allowed. Then open the mic's Properties in the Sound control panel, go to the Advanced tab, and uncheck exclusive-mode options that let one app lock the microphone. Restarting the app after these changes usually fixes it."
---

A Realtek microphone that is detected but silent — or missing entirely — breaks video calls, voice recording, and gaming chat in one stroke. Realtek audio chips handle the microphone on the vast majority of Windows laptops, so when the Realtek driver glitches, the mic is usually the first casualty. The fixes below move from quick settings checks to full driver surgery, and one of them will almost certainly get you heard again.

Keep in mind that "microphone not working" has two very different flavors: the mic is missing from the device list, or it is listed but records silence. The first points to drivers and disabled devices; the second points to privacy settings, levels, and enhancements. This guide covers both, in order.

## Why this happens

- **Microphone privacy settings blocking access:** Windows can revoke mic access globally or per-app after an update, leaving the device visible but silent.
- **Device disabled in Sound settings:** The microphone can be disabled in the recording devices list, hiding it from apps entirely.
- **Corrupted Realtek driver:** A bad update leaves the driver installed but unable to process the microphone input stream.
- **Wrong default device:** Windows may default to a disconnected headset or webcam mic instead of the Realtek array.
- **Audio enhancements interfering:** Noise suppression and enhancement effects can mute or garble the mic input.
- **Exclusive mode lock:** One application can seize exclusive control of the mic, starving every other app.
- **Front-panel jack detection bug:** Plugging and unplugging headsets can confuse the Realtek jack sensing and mute the internal mic.
- **BIOS or hardware mute:** Some laptops have a mic mute key or BIOS toggle that kills the microphone at a low level.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check privacy settings and the mute key

Start with the two fastest checks — they solve a surprising share of cases.

1. Open Settings > Privacy & security > Microphone and confirm "Microphone access" and "Let apps access your microphone" are both On.
2. Scroll down and verify your specific app (Teams, Zoom, Discord) is allowed.
3. Check for a microphone mute function key on your keyboard (often F4 with a mic icon) and press it to unmute.
4. Open the app's own audio settings and confirm the input device is set to the Realtek microphone, not Default.
5. Test with Windows' built-in Sound Recorder to isolate app-specific versus system-wide problems.

### Fix 2: Verify the mic in Sound settings

The classic Sound control panel shows the truth about disabled and disconnected devices.

1. Press Win + R, type `mmsys.cpl`, and press Enter, then go to the Recording tab.
2. Right-click the empty area and tick "Show Disabled Devices" and "Show Disconnected Devices".
3. If the Realtek microphone appears greyed out, right-click it and choose Enable.
4. Right-click the correct microphone and choose "Set as Default Device" and "Set as Default Communication Device".
5. Double-click the mic, go to the Levels tab, and drag the level to at least 70 with Microphone Boost around +10 dB.
6. Speak and watch the green level meter — movement here means Windows hears you and the problem is app-side.

### Fix 3: Disable audio enhancements and exclusive mode

Enhancement processing is a notorious mic-killer on Realtek chips.

1. In the Recording tab of `mmsys.cpl`, double-click the Realtek microphone.
2. Go to the Enhancements tab (or the Advanced tab on newer driver builds) and check "Disable all enhancements".
3. On the Advanced tab, uncheck both boxes under Exclusive Mode.
4. Click Apply and OK, then test the mic in Sound Recorder.
5. If your driver shows a Realtek Audio Console app instead, open it and turn off all microphone effects there.
6. Restart the application you were having trouble with — enhancement changes often need an app restart to take effect.

### Fix 4: Run the recording audio troubleshooter

Windows can automatically re-enable devices and reset the audio service.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the "Recording Audio" troubleshooter and follow its prompts.
3. If it offers to re-enable the microphone or restart audio services, accept.
4. After it finishes, open `mmsys.cpl` again and confirm the mic is enabled and default.
5. Microsoft documents these steps further on their [Windows support pages](https://support.microsoft.com/en-us/windows) if you want the official walkthrough.

### Fix 5: Reinstall the Realtek audio driver

A clean driver reinstall fixes corruption that settings cannot touch.

1. Press Win + X, open Device Manager, and expand "Sound, video and game controllers".
2. Right-click the Realtek audio device, choose Uninstall device, and tick "Attempt to remove the driver for this device".
3. Also check "Audio inputs and outputs" and uninstall the microphone entries the same way.
4. Restart the laptop — Windows will reinstall a basic audio driver on boot.
5. Test the mic with the basic driver; if it works, the old driver was corrupt.
6. For the permanent fix, install the manufacturer's Realtek package next.

### Fix 6: Install the manufacturer's Realtek driver package

Generic Realtek drivers can mis-map your laptop's specific microphone hardware.

1. Visit your laptop maker's support site — for example [Dell's official support](https://www.dell.com/support) — and download the audio driver for your exact model.
2. Run the installer and choose a clean or full installation if offered.
3. Restart when prompted, then open the Realtek Audio Console from the Start menu.
4. Confirm the microphone is detected and the input level responds to your voice.
5. Re-check the Enhancements and Exclusive Mode settings from Fix 3, since a fresh driver resets them.
6. If you also have speaker issues, our guide on [Realtek audio driver problems](/articles/realtek-audio-driver-not-working-windows-11/) covers the output side of the same chip.

### Fix 7: Reset the Windows audio service and jack detection

Stuck audio services and confused jack sensing can mute the mic persistently.

1. Press Win + R, type `services.msc`, and restart the "Windows Audio" and "Windows Audio Endpoint Builder" services.
2. In the Realtek Audio Console, look for jack detection or connector retasking settings and make sure the internal mic is not muted when nothing is plugged in.
3. Try plugging in a headset and unplugging it firmly once — this can reset stuck jack detection.
4. Open an elevated Command Prompt and run `sfc /scannow` to repair corrupted system audio files.
5. Restart and test the mic in two different apps to confirm the fix is system-wide.

### Fix 8: Check BIOS settings and test the hardware

If the mic is invisible even in Device Manager with hidden devices shown, look below the OS.

1. Restart into the BIOS and look for an integrated microphone or audio device toggle — make sure it is enabled.
2. Boot from a Linux live USB and test the microphone there to rule out Windows entirely.
3. If the mic works in Linux, consider a Windows repair install; if it fails everywhere, the microphone module or its cable has likely failed.
4. As a workaround, any USB headset bypasses the Realtek mic path completely.
5. For persistent output-side audio trouble on the same chip, see [laptop speakers not working](/articles/how-to-fix-laptop-speakers-not-working-on-windows-11/).

## Closing

Realtek microphone failures are almost never the microphone itself — they are privacy settings, disabled devices, enhancements, or a driver that Windows Update mangled. Work the list in order, install the manufacturer's driver as your final software step, and you will have a working mic again in the vast majority of cases. Once it is fixed, lock in the manufacturer's audio driver and keep Windows Update from swapping it out behind your back.
