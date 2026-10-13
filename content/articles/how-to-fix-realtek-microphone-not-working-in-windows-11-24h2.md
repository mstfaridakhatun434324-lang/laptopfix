---
title: "Fix a Realtek Microphone That Stopped Working in Windows 11 24H2"
slug: how-to-fix-realtek-microphone-not-working-in-windows-11-24h2
date: 2026-10-08
categories: ["drivers"]
tags: ["realtek microphone", "mic not working", "windows 11 24h2", "audio input", "privacy settings"]
description: "Fix a Realtek microphone not working after Windows 11 24H2: privacy permissions, driver rollback, exclusive-mode conflicts, and jack detection."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my Realtek microphone not working after 24H2?"
    a: "The update commonly replaces the vendor Realtek driver with a generic one that mishandles the capture path, resets microphone privacy permissions so apps are silently blocked, or breaks the audio service's recording endpoint. Checking privacy settings first, then rolling back the driver, resolves the majority of post-24H2 microphone failures."
  - q: "How do I check if Windows is blocking my microphone?"
    a: "Go to Settings, then Privacy and security, then Microphone, and confirm both Microphone access and Let apps access your microphone are turned on. Scroll down to enable individual apps, and check Let desktop apps access your microphone at the bottom — classic Win32 programs need that separate toggle."
  - q: "What does 'allow applications to take exclusive control' do to a mic?"
    a: "It grants one application exclusive ownership of the microphone at its own audio format, blocking every other app from capturing. Disabling exclusive mode on the Recording device's Advanced tab fixes the classic pattern where the mic works in exactly one app but stays silent everywhere else."
  - q: "Why does my mic work in the test but not in calls?"
    a: "The Windows sound test uses the shared capture path, while conferencing apps may request exclusive mode or latch onto a different default device than you expect. Open the app's own audio settings and manually select the Realtek microphone instead of Default, and disable exclusive mode on the device to stop one app starving the others."
---

A Realtek microphone that goes silent after the Windows 11 24H2 update creates a special kind of frustration: video calls where nobody hears you, voice recorders capturing nothing, and a mic that worked perfectly yesterday. The hardware — the MEMS microphone soldered to your laptop's board — does not fail coincidentally with an update. What fails is the capture chain: privacy permissions reset by the migration, a generic driver replacing the vendor one, or an exclusive-mode lock from a single app.

Diagnosis starts with one question: does Windows see any input signal at all? Open **Settings → System → Sound**, scroll to Input, select the microphone, and watch the volume bar while you speak. A moving bar means capture works and the problem is app-level; a flat bar means the driver or privacy layer is blocking input. That single test aims every fix below.

## Why this happens

- **Microphone privacy permissions reset:** 24H2's migration can turn off microphone access globally or per-app, silently blocking all capture.
- **Vendor Realtek driver replaced:** Windows installs a generic High Definition Audio driver that mishandles the Realtek codec's capture path.
- **Wrong default input device:** The update can switch the default to a disconnected headset, a monitor's mic, or a disabled array mic.
- **Exclusive mode lock:** One app (often a conferencing tool) grabs the mic exclusively, starving every other app.
- **Audio service capture path broken:** The Windows Audio service's recording endpoint fails to initialize after the driver swap.
- **Front-panel/jack detection confusion:** On laptops with combo jacks, the Realtek control panel's jack-detection state can mute the internal mic array.
- **Enhancements breaking capture:** Noise suppression and AEC processing re-enabled by the update can gate the mic signal to silence.
- **Corrupted driver from partial update:** Mismatched driver and Realtek Audio Console components after a half-applied update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone privacy settings

1. Go to **Settings → Privacy & security → Microphone**.
2. Turn on **Microphone access** and **Let apps access your microphone**.
3. Scroll down and enable access for each app you need (Teams, Zoom, browser, etc.).
4. Also check **Let desktop apps access your microphone** at the bottom — classic Win32 apps need this separate toggle. Retest with the input volume bar in **Settings → System → Sound**.

### Fix 2: Set the correct default input device

1. Go to **Settings → System → Sound → Input** and select the **Realtek microphone / Microphone Array** explicitly.
2. Click the arrow next to it → **Test your microphone** and speak — watch the input level bar.
3. Disable devices you do not use (right-click in **More sound settings → Recording** → **Disable**) so apps cannot grab the wrong one.
4. In your call app's own settings, manually select the Realtek microphone instead of "Default" — apps cache device IDs that change across updates.

### Fix 3: Disable exclusive mode and enhancements

1. Open **More sound settings → Recording**, double-click the Realtek microphone.
2. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**.
3. On the **Enhancements** tab, check **Disable all enhancements** (noise suppression and AEC can mute quiet mics).
4. Set **Default Format** to **2 channel, 16 bit, 48000 Hz**. Apply and retest — this resolves the "works in test, silent in calls" pattern. The same audio-stack logic applies to output problems covered in the [general audio driver guide](/articles/realtek-audio-driver-not-working-windows-11/).

### Fix 4: Roll back or reinstall the Realtek driver

1. Open **Device Manager → Sound, video and game controllers**, right-click the Realtek device → **Properties → Driver → Roll Back Driver**.
2. If rollback is unavailable: **Uninstall device** (check **Attempt to remove the driver**), reboot, and install the audio driver from your vendor — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the **Realtek Audio Console** from the Microsoft Store afterward — the console manages jack detection and mic array settings the driver needs.
4. Retest the input bar after each step to identify which one restored capture.

### Fix 5: Restart the audio services and reset the stack

1. Press **Win + R** → `services.msc` → restart **Windows Audio** and **Windows Audio Endpoint Builder**.
2. In an elevated Command Prompt, run `sfc /scannow` to repair corrupted audio system files.
3. Go to **Settings → System → Troubleshoot → Other troubleshooters → Recording Audio → Run** for Microsoft's automated checks, documented further in [Windows support](https://support.microsoft.com/en-us/windows).
4. Reboot and retest.

### Fix 6: Check jack detection and the Realtek Audio Console

1. Open **Realtek Audio Console** from the Start menu.
2. Under device advanced settings, check the jack-detection options — a stuck "headset plugged in" state mutes the internal mic array on some models.
3. If you use a combo-jack headset, plug and unplug it once to reset the detection state.
4. Try the headset's own mic: if it works while the internal array does not, the array's capture path (driver) is the problem, not system-wide audio.

### Fix 7: Rule out hardware with a live USB test

1. Boot a Linux live USB and test the microphone in its sound settings.
2. Working mic in Linux = Windows driver/permission problem, keep troubleshooting software.
3. Dead mic in Linux too = the MEMS mic or its board connection failed — a service repair, since laptop mics are soldered.
4. As a workaround, any USB or Bluetooth headset bypasses the internal mic entirely.

## Closing

A silent Realtek mic after 24H2 is a permissions-or-driver problem in nearly every case: the update reset privacy toggles, swapped the driver, or let one app lock the device exclusively. If the microphone works in some apps but stays silent in others even after these fixes, the app-level routing needs attention — the [general microphone troubleshooting guide](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/) covers per-application capture issues in depth. Check the privacy page, set the right default device, kill exclusive mode, and put the vendor driver back — the input bar in Sound settings tells you the moment capture is restored.
