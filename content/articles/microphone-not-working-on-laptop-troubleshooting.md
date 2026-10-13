---
title: "Diagnose a Laptop Microphone That Picks Up Nothing"
slug: microphone-not-working-on-laptop-troubleshooting
date: 2026-09-17
categories: ["drivers"]
tags: ["microphone", "mic not working", "audio input", "privacy settings", "troubleshooting"]
description: "Laptop microphone not picking up sound? Diagnose dead mics systematically — privacy, drivers, hardware — and get voice input working again."
thumbnail: "/images/thumbs/microphone-not-working-on-laptop-troubleshooting.webp"
faqs:
  - q: "How do I know if my laptop microphone is broken or just misconfigured?"
    a: "Open Settings > System > Sound and speak while watching the input volume meter. If the meter moves, the mic works and the problem is app-level routing or permissions. If it never moves across every app, the issue is driver, privacy, or hardware."
  - q: "Why does my mic work in one app but not another?"
    a: "Per-app microphone permissions in Windows privacy settings. An app denied access hears nothing while others work fine. Check Settings > Privacy & security > Microphone and enable access for the specific app. Apps read permissions at launch, so restart the app after changing any privacy toggle."
  - q: "Can a Windows update disable my microphone?"
    a: "Yes. Updates reset privacy permissions and replace audio drivers, either of which can silence the mic. Re-granting microphone access and reinstalling the audio driver are the two standard post-update fixes. Check the physical mute key first; updates never cause that, but it is the most common culprit."
  - q: "Does the physical mic mute key affect all apps?"
    a: "Yes. The Fn mute key or a dedicated mic-mute button cuts the microphone at the hardware or driver level, so no app can hear anything until it is unmuted. The mute LED is the indicator — if it is lit, the mic is off regardless of software settings."
---

You join a call, speak, and get the dreaded 'we can't hear you.' The microphone that worked yesterday now picks up nothing — not in Teams, not in the voice recorder, not anywhere. Microphone failures feel total because every app fails identically, which actually helps: a problem affecting all apps lives below the apps, in Windows settings, drivers, or hardware.

Diagnosing a dead mic is a process of elimination across four layers: the physical mute state, Windows privacy permissions, the audio driver and device routing, and finally the microphone hardware itself. Each layer has a quick decisive test, and you should never reinstall drivers before checking the mute key — the simplest cause is the most embarrassing to miss.

This guide is the systematic version of that elimination. Follow it top to bottom and you will find the layer where your mic went silent.

The single most useful diagnostic in microphone troubleshooting is the input volume meter in Settings > System > Sound. It sits below every app and every permission, showing you the raw signal from the hardware. Meter moves but apps hear nothing? Software problem. Meter dead everywhere? Driver or hardware problem. Let that meter be your compass through the entire sequence below.

## Why this happens

- **Physical mute key engaged:** The Fn mic-mute key or a dedicated button silences the mic below the software level.
- **Microphone privacy permissions revoked:** Windows privacy settings can block some or all apps from the microphone.
- **Wrong input device selected:** Windows may route input from a disconnected headset or webcam mic instead of the built-in array.
- **Audio driver corrupted:** The capture side of the audio driver fails while playback keeps working, producing the confusing 'speakers fine, mic dead' state.
- **Microphone disabled in Sound settings:** The device can be disabled outright, removing it from every app's device list.
- **BIOS audio input disabled:** Rare, but firmware can disable the mic array, hiding it from Windows entirely.
- **Failed microphone hardware:** The mic array or its connection to the motherboard can fail, usually after drops or liquid exposure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the mute key and LED indicator

Hardware mute overrides everything. This thirty-second check saves enormous wasted effort.

1. Look for a microphone icon on your function keys or a dedicated mute button near the keyboard.
2. Press **Fn** plus the mic key and watch for the mute LED to turn off.
3. Open **Settings > System > Sound** and confirm the input device is not showing as muted.
4. Speak and watch the input volume meter for movement.

### Fix 2: Verify privacy permissions

Windows can revoke mic access silently during updates. Permissions are the top software cause.

1. Open **Settings > Privacy & security > Microphone**.
2. Ensure **Microphone access** and **Let apps access your microphone** are both **On**.
3. Scroll through the app list and enable access for every app that needs the mic.
4. Restart the affected app and test again.

### Fix 3: Select the correct input device

Windows often defaults to a phantom device — a disconnected headset mic or a monitor's mic — instead of the built-in array.

1. Open **Settings > System > Sound** and expand the **Input** section.
2. Select your laptop's built-in microphone array explicitly.
3. Click the device and run **Test your microphone** while speaking.
4. If the correct device is missing from the list, continue to the driver fix.

### Fix 4: Enable the microphone in Sound settings

A disabled capture device is invisible to apps. The classic Sound panel reveals it.

1. Right-click the speaker icon and choose **Sounds**, then open the **Recording** tab.
2. Right-click empty space and enable **Show Disabled Devices**.
3. If your microphone appears greyed, right-click it and choose **Enable**.
4. Set it as the **Default Device** and test. USB headset mics have their own routing quirks covered in the [USB headset guide](/articles/how-to-fix-usb-headset-not-working-on-windows-11/). Windows 11's reorganized mic settings are walked through in the [Windows 11 mic guide](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/).

### Fix 5: Reinstall the audio driver

When playback works but capture is dead, the driver's recording path is corrupt. Reinstalling rebuilds it.

1. Open **Device Manager > Audio inputs and outputs**.
2. Right-click the microphone device and choose **Uninstall device**.
3. Expand **Sound, video and game controllers** and reinstall the Realtek or Intel audio driver the same way.
4. Restart and let Windows reinstall, then retest the input meter. Microsoft documents the sound settings path on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Check the BIOS for the microphone setting

Some business laptops let firmware disable the mic array for security. A reset can flip it unexpectedly.

1. Restart and enter the BIOS setup.
2. Look for **Microphone**, **Audio**, or **Internal Mic** under Security or Devices.
3. Ensure it is **Enabled**, save, and boot into Windows.
4. If the mic appears in Device Manager now, firmware was the blocker.

### Fix 7: Test with an external microphone

A USB or 3.5mm mic bypasses the internal array completely, proving whether the hardware is dead.

1. Plug in any external microphone and select it as the input device.
2. If the external mic works, the internal array or its motherboard connection has failed.
3. If no mic works on the machine, the audio capture subsystem needs a driver-level repair or OS refresh.
4. For internal array failure, a USB mic is a perfectly good permanent workaround.

### Fix 8: Run System File Checker for audio stack damage

Corrupted system files in the audio stack can silence capture while leaving playback intact. SFC repairs them.

1. Open an elevated Command Prompt.
2. Run **sfc /scannow** and wait for it to complete.
3. If it reports unfixable damage, follow with **DISM /Online /Cleanup-Image /RestoreHealth** and run SFC again.
4. Restart and retest the input meter.

## Closing

A silent laptop mic is a layer problem: mute key, privacy permissions, device routing, driver, then hardware. Test each layer's decisive check — the input meter never lies — and the failure point reveals itself. Most mics are muted or permission-blocked, not broken.
