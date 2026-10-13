---
title: "How to Fix the Realtek Microphone Not Working on an HP Laptop"
slug: how-to-fix-realtek-microphone-not-working-on-hp-laptop
date: 2026-10-05
categories: ["drivers"]
tags: ["realtek microphone", "hp laptop", "mic not working", "audio input"]
description: "Realtek microphone not picking up sound on your HP laptop? Fix privacy, driver, and enhancement issues to get your mic working."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop microphone show as working but record no sound?"
    a: "This usually means the wrong input device is set as default, the mic level is turned down to zero, or an enhancement layer is muting the signal. Open Sound settings, confirm the Realtek internal mic is the default input, and watch the input level bar while speaking — a flat bar with correct selection points to a driver problem."
  - q: "Can Windows privacy settings block my Realtek microphone?"
    a: "Yes, and it is one of the most common causes. If microphone access is off for the device or for desktop apps, the mic appears in Device Manager but no app receives audio. Check Settings, Privacy and security, Microphone after every major Windows update, since updates sometimes reset these toggles."
  - q: "Should I disable audio enhancements to fix the microphone?"
    a: "Yes, try it early. Noise suppression and beamforming enhancements in the Realtek/HD Audio stack can malfunction and silence the mic entirely. Disabling all enhancements on the recording device is a quick test that resolves the issue on many HP models."
  - q: "Do I need the HP audio driver or will the Windows one work?"
    a: "Use HP's audio driver for your exact model. HP customizes the Realtek package for its microphone arrays and noise-cancellation tuning, and the generic Windows driver often leaves the internal mics non-functional or severely degraded even when it installs without errors."
---

A Realtek microphone that appears in Device Manager, shows as the default recording device, and yet captures absolute silence is a classic HP laptop complaint. The mic is not broken — in the overwhelming majority of cases it is muted somewhere in a long chain of privacy toggles, default-device selections, enhancement layers, and driver bindings. The trick is checking the chain in the right order instead of reinstalling drivers at random.

Start with the input level meter in **Settings → System → Sound**, under Input. Speak and watch: a bouncing bar means the mic works and the problem is app-specific; a flat bar means the system is not receiving audio at all. That single observation directs everything that follows.
HP's microphone setup has a wrinkle worth knowing: most HP laptops use a dual-microphone array with noise-cancellation tuning baked into the Realtek driver package. The generic Windows audio driver can drive the speakers while leaving the mic array completely non-functional — Device Manager looks healthy, but no application hears anything. That's why the HP-specific driver matters more for the microphone than for almost any other component.

## Why this happens

- **Microphone privacy disabled:** Windows privacy settings block mic access for the device or for desktop apps, silently starving all apps of audio.
- **Wrong default input device:** A headset, webcam mic, or virtual device is set as default instead of the internal Realtek microphone array.
- **Mic level at zero or muted:** The recording device's level slider sits at zero or the mute box is ticked — often changed by an app and never restored.
- **Enhancement layer silencing the signal:** Broken noise-suppression or beamforming in the Realtek stack mutes the mic while appearing active.
- **Driver mismatch:** A generic Windows audio driver replaces HP's tuned Realtek package, leaving the mic array non-functional.
- **App-specific permission or device selection:** The conferencing app has its own mic selector pointed at the wrong device, independent of Windows defaults.
- **BIOS audio settings:** Some HP BIOS versions include microphone toggles that updates can reset.
- **Hardware mic failure:** Rare; usually affects one mic of the array or follows physical damage near the hinge.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check privacy and the input meter

1. Open **Settings → Privacy & security → Microphone** and confirm **Microphone access** and **Let desktop apps access your microphone** are on.
2. Go to **Settings → System → Sound**, scroll to **Input**, and select the internal microphone (Realtek Audio).
3. Speak at normal volume and watch the input volume bar — note whether it moves at all.
4. If the bar moves here but not in your app, skip to Fix 6; the system side is fine.
5. Also try the **Test your microphone** button and speak for a full five seconds — some mics show a delayed response on the live bar but register fine on the recorded test, which means the mic works and the meter rendering is just sluggish.

### Fix 2: Verify levels and unmute the device

1. In Sound settings, click the microphone → **Properties**, and set the input volume to at least **75**.
2. Open the classic **Sound** control panel (**More sound settings → Recording** tab), double-click the mic → **Levels** tab.
3. Confirm the level is up and the speaker icon next to it is not muted.
4. On the **Listen** tab, you can tick **Listen to this device** briefly to hear the mic through your speakers — a direct hardware-path test.

### Fix 3: Disable all enhancements on the mic

1. In the mic's **Properties → Enhancements** (or **Audio enhancements** dropdown in Windows 11 Sound settings), choose **Off**.
2. Also disable any **Noise suppression** or **Acoustic echo cancellation** toggles on the **Advanced** tab.
3. In HP's audio utility (Bang & Olufsen / HP Audio Control), turn off noise cancellation for the microphone temporarily.
4. Retest the input meter — enhancement layers are a leading cause of "present but silent" mics.
5. If disabling enhancements fixes it, re-enable them one at a time afterward to find the specific offender — usually it's the noise suppression module, and knowing which one lets you keep the others.

### Fix 4: Clean-reinstall HP's Realtek audio driver

1. Download the exact audio driver for your model from [HP support](https://support.hp.com/us-en).
2. In **Device Manager → Sound, video and game controllers** and **Audio inputs and outputs**, uninstall the Realtek devices with driver removal ticked.
3. Restart and install the HP package, then restart again.
4. Recheck the input meter. This is the same clean-driver approach used for [crashing Lenovo audio drivers](/articles/how-to-fix-audio-driver-keeps-crashing-on-lenovo-laptop/) — the Realtek stack fails the same way across brands.
5. If the mic works in Windows but not in one specific app, the app's own audio engine is suspect — our [general Realtek audio guide](/articles/realtek-audio-driver-not-working-windows-11/) covers app-level audio routing issues that Device Manager can't show you.

### Fix 5: Check the BIOS microphone setting

1. Restart and press **F10** to enter HP BIOS Setup.
2. Look under **Advanced** or **System Configuration** for integrated microphone or audio device toggles.
3. Ensure the internal microphone is enabled, then save and exit.
4. A BIOS-disabled mic is invisible to every Windows-level fix, so confirm this before suspecting hardware.

### Fix 6: Fix app-level mic selection

1. In your conferencing app's audio settings, open the microphone dropdown and explicitly choose the internal mic — do not leave it on "Default" or "Same as system."
2. In the browser, click the lock/camera icon in the address bar during a call and confirm microphone permission is **Allow**.
3. Close other apps that might hold the mic exclusively (voice recorders, other conferencing tools).
4. Test with Windows **Voice Recorder** — if it records fine, the OS and driver are good and the original app was the problem.

### Fix 7: Test hardware with HP diagnostics

1. Restart and press **F2** to enter HP PC Hardware Diagnostics.
2. Run the **Audio** / microphone test and speak during it.
3. If the diagnostic records your voice, the hardware is fine and the issue is purely Windows-side — revisit driver and privacy fixes.
4. If the diagnostic hears nothing, the mic array or its cable is faulty — a service repair, since internal mics sit in the display assembly on most HP models.

## Closing

A silent Realtek mic on an HP laptop is a chain-of-settings problem far more often than a hardware failure: privacy toggles, default device selection, muted levels, enhancements, and the HP-specific driver each get a vote. Work the chain in order and test with the input meter after every step — when the bar starts bouncing, you have found your fix. Keep HP's audio driver installed and block generic replacements to prevent recurrence.
