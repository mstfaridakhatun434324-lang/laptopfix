---
title: "Realtek Microphone Not Working on Windows 11? Here's the Fix"
slug: how-to-fix-realtek-microphone-not-working-on-windows-11
date: 2026-09-23
categories: ["drivers"]
tags: ["realtek microphone", "windows 11", "mic not working", "audio driver"]
description: "Your Realtek mic picks up nothing on Windows 11? Fix privacy blocks, driver faults, and input settings with this step-by-step troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-on-windows-11.webp"
faqs:
  - q: "Why is my microphone not working but speakers are fine?"
    a: "Speakers and microphone share the Realtek driver but use separate capture and render paths — one can break while the other works. The usual mic-specific culprits are privacy permissions blocking input, the wrong input device selected, the mic muted or at zero level, or the capture side of the driver corrupted. The fixes below address each in order."
  - q: "Where are the microphone privacy settings on Windows 11?"
    a: "Go to Settings, then Privacy & security, then Microphone. Make sure Microphone access and Let apps access your microphone are both on, and that the specific app is allowed in the list below. Windows updates frequently reset these toggles, which produces the classic symptom of a mic that tests fine in Windows but is silent in every app."
  - q: "What does it mean if the mic level bar doesn't move?"
    a: "The level bar in Settings, then System, then Sound, under Input, shows live input. A flat bar means no signal is reaching Windows at all — the mic is muted, disabled, disconnected, or its driver capture path is broken. A moving bar with silent apps means the signal reaches Windows but privacy or app settings block it. That distinction tells you which half of this guide applies."
  - q: "Can audio enhancements break the microphone?"
    a: "Yes. Noise suppression and echo cancellation APOs in the Realtek chain can malfunction after driver updates and gate the mic signal entirely. Disabling audio enhancements for the input device is a legitimate diagnostic step — if the mic springs to life, the enhancement layer was the problem and the driver likely needs reinstalling."
---

The meeting hears nothing. The voice recorder captures silence. The input level bar in Sound settings sits flat no matter how loudly you talk — yet the speakers play fine and Device Manager insists the Realtek device is working properly.

Microphone failures split neatly: either no signal reaches Windows (driver, mute, disabled device), or the signal reaches Windows but apps cannot use it (privacy permissions, wrong device selected). The level-bar test tells you which in ten seconds. Work the matching half of this guide. If the speakers are dead too, the whole audio stack needs repair — see our [Realtek audio guide](/articles/how-to-fix-realtek-audio-not-working-in-windows-11-24h2/) first.

## Why this happens

- **Microphone privacy access revoked.** An update turned off the master mic permission toggle.
- **Wrong input device selected.** Windows defaulted to a disconnected headset or monitor mic.
- **Microphone muted or level at zero.** The input level got dragged to zero or muted by an app.
- **Realtek capture driver corrupted.** The driver's input path broke while output kept working.
- **Audio enhancements gating the signal.** Broken noise-suppression APO blocks the mic entirely.
- **Exclusive mode seized by an app.** A conferencing app holds the mic exclusively and blocks others.
- **Front-panel jack misconfigured.** The Realtek console treats the plugged mic as the wrong device type.
- **BIOS audio settings changed.** Firmware updates can disable the internal mic array.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the level-bar test and check the input device

Go to **Settings > System > Sound**, scroll to **Input**, and select your microphone — it should be **Microphone (Realtek Audio)** or your array mic, not a disconnected headset. Talk and watch the **input volume** bar. Moving bar: signal reaches Windows — skip to Fix 3 for the app/permission side. Flat bar: no signal — continue with Fix 2. Also drag the input volume slider up past 70 while testing; updates love to reset it near zero. This single screen diagnoses the entire problem class.

### Fix 2: Unmute and enable the microphone

In the same Sound settings, click the input device arrow to open its properties and confirm it is **Allowed** (not "Don't allow"). Then open the classic **Sound** control panel (search "sound"), go to the **Recording** tab, right-click the Realtek mic, and check **Enable** if it is disabled — right-click again, choose **Properties > Levels**, and make sure the level is up and the speaker icon is not muted. A disabled or muted mic at the system level produces the flat-bar symptom with zero errors anywhere.

### Fix 3: Verify microphone privacy permissions

Go to **Settings > Privacy & security > Microphone** and ensure **Microphone access** and **Let apps access your microphone** are both on. Scroll through the app list and confirm your conferencing app is allowed. Toggle the master switch off and back on to force re-registration. This is the fix when the level bar moves in Settings but Teams, Zoom, or the browser hear nothing — Windows is receiving the mic, but permission blocks the apps. Retest in the actual app after changing permissions, not just in Settings.

### Fix 4: Disable enhancements and exclusive mode

Open the classic **Sound** control panel, **Recording** tab, open the mic's **Properties**. On the **Enhancements** tab, check **Disable all enhancements**. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**. Broken enhancement APOs — noise suppression, echo cancellation — can gate the entire mic signal after a driver update, and exclusive-mode grabs by one app silence all others. Test the level bar after each change to see which one mattered.

### Fix 5: Reinstall the Realtek driver

Open **Device Manager**, expand **Sound, video and game controllers** and **Audio inputs and outputs**. Right-click the Realtek entries, choose **Uninstall device** (check driver deletion for the main Realtek device), and restart. Windows reinstalls on boot — test the mic. For the definitive version, install the **Realtek audio driver** for your exact model from [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en), since the vendor package includes the matched capture-path components. Restart after installing and recheck both the level bar and app permissions.

### Fix 6: Check the Realtek Audio Console and jack detection

Open the **Realtek Audio Console** from the Start menu. If you use a plugged-in headset mic, check what the console thinks is connected — set the jack to **Mic In** explicitly if it misdetected the device type. For the internal mic array, verify the console shows it active and not muted. Some Lenovo and Dell models route mic selection through this console, and its settings survive driver reinstalls — a stale console configuration can keep a fresh driver muted. Reset the console to defaults if anything looks wrong.

### Fix 7: Check BIOS audio settings and test hardware

Restart into the BIOS (F2, Del, or your brand's key) and look for integrated audio or microphone array toggles — ensure they are enabled. Check for a **BIOS update** on the manufacturer's site, since mic-array initialization fixes ship in firmware. As a final test, try a USB headset or a phone-earbud mic: if external mics work but the internal array never does across driver versions, the array's cable or the codec's capture path has a hardware fault. If no mic works anywhere including a Linux live USB, the audio codec needs professional diagnosis.

## Closing

Mic failures are signal-path problems: confirm the signal with the level bar, then fix whichever half is broken — device and driver for a flat bar, privacy and app settings for a moving one. The Realtek vendor driver plus correct permissions resolves the large majority. If you are on Windows 10 instead, our [Windows 10 Realtek mic guide](/articles/how-to-fix-realtek-microphone-not-working-on-windows-10/) covers the older Sound control panel layout. A quick level-bar check after every major update catches regressions early. Ten seconds of prevention beats another round of troubleshooting.
