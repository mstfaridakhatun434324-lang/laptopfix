---
title: "Realtek Microphone Not Working? Troubleshooting Guide for Windows Laptops"
slug: troubleshoot-realtek-microphone-not-working
date: "2026-10-08"
categories: ["drivers"]
tags: ["realtek microphone", "mic not working", "audio input", "recording devices", "microphone driver"]
description: "Realtek microphone not working or not detected on your laptop? Follow this troubleshooting guide to fix privacy settings, recording devices, and driver issues on Windows 10 and 11."
thumbnail: "/images/thumbs/troubleshoot-realtek-microphone-not-working.webp"
faqs:
- q: "Why is my Realtek microphone not detected in Windows?"
  a: "The most common reasons are Windows privacy settings blocking microphone access, the wrong recording device set as default, or a corrupted Realtek audio driver after a Windows update. The microphone may also be disabled in the Sound control panel. Working through privacy settings first, then the recording device list, then the driver resolves the issue in the large majority of cases without any hardware involvement."
- q: "How do I give apps permission to use my microphone?"
  a: "Open Settings, go to Privacy and security, then Microphone, and turn on microphone access for the device as well as for desktop apps. Windows 10 and 11 block microphone access by default for privacy, which silently breaks Teams, Zoom, Discord, and browser-based calls. After enabling access, restart the affected app so it picks up the permission change."
- q: "Should I use the generic Windows audio driver or Realtek's?"
  a: "Use the Realtek driver from your laptop manufacturer whenever possible. The generic Microsoft High Definition Audio driver provides basic recording, but it lacks the vendor's microphone array processing, noise suppression, and jack-detection logic. If the manufacturer's driver is causing the problem, a clean reinstall of that same package usually fixes it better than switching to the generic driver permanently."
- q: "Can a Windows update break my laptop microphone?"
  a: "Yes, this is one of the most common triggers. Feature updates sometimes replace the manufacturer's Realtek driver with a generic version that does not initialize the microphone array correctly, or they reset privacy settings that revoke app access. If the microphone stopped working immediately after an update, reinstalling the manufacturer's audio driver and rechecking privacy permissions are the two fastest fixes."
---

You join a call, say hello, and nobody hears you. The microphone on your laptop — which worked fine last week — now records nothing, does not appear in the recording devices list, or shows up but stays stubbornly flat on the input meter. Few things are more disruptive to a workday, and the cause is rarely the physical microphone itself.

Realtek audio chips handle both output and input on nearly every Windows laptop, which means microphone failures usually trace back to the same handful of culprits: Windows privacy settings silently blocking access, the wrong input selected as default, a driver that a Windows update replaced or corrupted, or an enhancement layer muting the signal. Each produces a slightly different symptom, and knowing which you have points straight at the fix.

This guide troubleshoots the problem in the order a technician would — permissions first, then device selection, then the driver stack. Work through it top to bottom and your microphone will almost certainly be recording again before you reach the end.

## Why this happens

- **Microphone privacy settings blocking access**: Windows 10 and 11 gate microphone access per-app; an update can revoke permissions silently.
- **Wrong recording device set as default**: With a headset or USB mic once connected, Windows may keep routing input to the absent device.
- **Corrupted or replaced Realtek driver**: Windows updates frequently swap the vendor driver for a generic one that mishandles the mic array.
- **Microphone disabled in Sound settings**: The device can be disabled at the OS level, hiding it from every application.
- **Conflicting audio enhancements**: Noise suppression and "improvements" from the driver or third-party apps can mute or distort input.
- **App-specific permission denied**: Browsers and desktop apps each need individual permission; one denial breaks calls in that app only.
- **BIOS or hardware fault**: Rare, but a disabled internal mic in BIOS or a damaged mic flex cable produces a device that never appears.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone privacy settings

This is the number-one cause and the fastest to check. Windows treats microphone access as a privacy gate, and major updates have a habit of flipping it off. The cruel part is that everything looks normal — the mic appears in settings, levels just never move, and apps report "no microphone found." Enable access at both the system and app level before touching anything else.

1. Open Settings, then Privacy and security, then Microphone.
2. Turn on "Microphone access" and "Let desktop apps access your microphone."
3. Scroll down and confirm your calling app (Teams, Zoom, Discord) is allowed.
4. Restart the app completely so it re-requests the microphone.
5. Test with Voice Recorder — if it records, the problem was permissions.

### Fix 2: Set the correct default recording device

Windows does not always switch input back when you unplug a headset or USB microphone. The internal Realtek mic can be present and working while all audio routes to a device that is no longer connected. Explicitly setting the internal microphone as the default communications and recording device clears this confusion instantly.

1. Right-click the speaker icon and choose Sound settings, then "More sound settings."
2. Open the Recording tab and look for "Microphone" or "Microphone Array" (Realtek).
3. If it is missing, right-click the empty area and tick "Show Disabled Devices."
4. Right-click the Realtek microphone, choose Enable, then "Set as Default Device."
5. Speak and watch the green level meter — movement means input is flowing.

### Fix 3: Reinstall the Realtek audio driver

When the mic is missing from the recording list entirely or the level meter stays flat despite correct settings, the driver is the prime suspect. A clean reinstall replaces corrupted files and restores the vendor's mic-array processing that the generic driver lacks. Get the package from your laptop maker's support page for the best results.

1. Open Device Manager and expand "Sound, video and game controllers."
2. Right-click the Realtek audio device, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart the laptop and let Windows reinstall a driver automatically.
4. If the mic still fails, download the audio driver from your maker's support page — for example [Dell Support](https://www.dell.com/support) — install it, and restart.
5. Recheck the Recording tab; the Realtek microphone should now appear and respond.

### Fix 4: Unmute the mic and raise its levels

Sometimes the fix is embarrassingly simple: the microphone is muted at the driver level or its boost is set so low that input is inaudible. This happens after driver reinstalls, which reset levels to defaults, or when a headset's inline mute button was the last thing touched. Checking the Levels tab takes thirty seconds.

1. In the Recording tab of Sound settings, double-click the Realtek microphone.
2. Open the Levels tab and drag the Microphone slider to 80–100.
3. If a Microphone Boost slider exists, set it to +10 or +20 dB.
4. Check the speaker icon next to the slider is not muted.
5. Speak normally — the level meter should now bounce well into the green.

### Fix 5: Disable audio enhancements on the microphone

Realtek's enhancement suite — noise suppression, acoustic echo cancellation, beam forming — usually helps, but a corrupted enhancement chain can silence the mic completely. Disabling all enhancements isolates whether the processing layer is the culprit. If the mic springs to life, you can re-enable features one by one to find the offender.

1. Double-click the Realtek microphone in the Recording tab.
2. Open the Enhancements tab (on some drivers it is under "Advanced").
3. Tick "Disable all enhancements" and click Apply.
4. Test recording in Voice Recorder.
5. If it works, re-enable enhancements individually to identify the broken one.

### Fix 6: Run the recording audio troubleshooter

Windows ships a dedicated troubleshooter that checks the exact chain you have been verifying manually — device state, default selection, driver health, and service status. It occasionally catches something subtle, like a stopped audio service dependency, that manual checks miss. It is automated, safe, and worth the two minutes.

1. Open Settings, go to System, then Troubleshoot, then "Other troubleshooters."
2. Click Run next to "Recording Audio."
3. Select the Realtek microphone when prompted and follow the steps.
4. Apply any fix the troubleshooter recommends and restart if asked.
5. Test the mic in your calling app afterward.

### Fix 7: Check BIOS and rule out hardware failure

If the microphone does not appear even with hidden devices shown, and no driver will make it appear, look below the OS. Some laptops have a BIOS toggle for the internal microphone array, and a damaged flex cable (common after screen repairs) disconnects it electrically. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the software side, but this step covers what software cannot reach.

1. Restart into BIOS/UEFI setup and look for an internal microphone or audio toggle — ensure it is enabled.
2. Boot to a Linux live USB and test the mic there; working in Linux proves a Windows software issue.
3. If it fails in Linux too, the mic hardware or its cable is faulty.
4. For out-of-warranty machines, a USB microphone is a cheap, reliable workaround.
5. For in-warranty machines, contact the manufacturer — mic cable replacement is a standard repair.

If the problem is on the output side instead — speakers silent or distorted — our guide to [fixing laptop speakers not working](/articles/best-way-to-fix-laptop-speakers-not-working/) covers that chain. USB headset users with mic trouble should also see [fixing a USB headset not working](/articles/how-to-fix-usb-headset-not-working-youtube/).

## Closing

A dead Realtek microphone is almost never a dead microphone — it is a permission revoked, a wrong default device, or a driver that an update mangled. Check privacy settings first, confirm the recording device, then reinstall the manufacturer's audio driver. That sequence restores input on the overwhelming majority of laptops without opening the machine.
