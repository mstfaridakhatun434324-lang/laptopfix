---
title: "Microphone Not Working on Laptop? Fixes That Actually Work"
slug: how-to-fix-microphone-not-working-on-laptop-reddit
date: 2026-10-10
categories: ["drivers"]
tags: ["microphone not working", "laptop mic", "realtek microphone", "windows 11", "mic driver"]
description: "Microphone not working on your laptop? Fix silent mics with 7 proven repairs — privacy settings, Realtek drivers, and app permissions."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop-reddit.webp"
faqs:
  - q: "Why is my laptop microphone not working in Zoom but works elsewhere?"
    a: "That pattern means the driver is fine and the problem is app-level: Zoom's audio settings are pointed at the wrong input, Windows privacy settings block desktop apps, or another app is holding the mic exclusively. Check Zoom's Settings, Audio, microphone dropdown first, then Windows Settings, Privacy and security, Microphone — desktop-app access must be on for Zoom, Teams, and Discord."
  - q: "How do I test if my laptop microphone hardware works?"
    a: "Open Settings, System, Sound, scroll to Input, select your microphone, and watch the input volume bar while you speak — movement means the hardware and driver work. You can also use the Voice Recorder app for a quick recording test. If the bar moves in Settings but an app hears nothing, it's a permission or app-settings problem, not hardware."
  - q: "Can privacy settings mute my laptop microphone completely?"
    a: "Yes — Windows' microphone privacy master switch blocks every app at once, and updates sometimes flip it off silently. Check Settings, Privacy and security, Microphone: the master 'Microphone access' toggle, the per-app list, and 'Let desktop apps access your microphone' must all be on. This is the single most common cause of a mic that 'suddenly stopped working.'"
  - q: "Why is my laptop mic so quiet even at 100% volume?"
    a: "A quiet mic usually means the wrong input device is selected (a distant webcam mic instead of the array mic), Microphone Boost is at zero in the device properties, or enhancements are misconfigured. In Sound settings, open the mic's Properties, go to Levels, and raise Microphone Boost to +20 or +30 dB. Also confirm the correct device is the default — not a headset or monitor mic."
---

A dead laptop microphone announces itself at the worst moment — mid-call, when nobody can hear you. The mic worked yesterday, nothing changed (that you know of), and now the input meter sits flat. Before assuming hardware failure: laptop mics are simple devices, and Windows' privacy model plus the Realtek driver account for nearly every "mic not working" report.

This guide runs the full diagnostic order: the input-meter test that splits hardware from software in ten seconds, privacy toggles, driver repairs, and the app-permission hunt.

It's worth internalizing the order because mic problems recur — every major Windows update is an opportunity for privacy toggles to reset and drivers to be replaced. Once you've run this sequence once, the second time takes five minutes: input meter, privacy toggles, input device selection. Those three checks resolve the large majority of repeat incidents.

## Why this happens

- **Privacy settings blocking mic access.** The master toggle flipped off by an update — the top cause.
- **Wrong input device selected.** Windows defaulting to a headset, webcam, or monitor mic.
- **Realtek driver corruption.** The audio driver failing to expose the mic array.
- **App holding exclusive control.** One app locking the mic so others get silence.
- **Microphone disabled in Sound settings.** Disabled device hidden from the input list.
- **Microphone Boost at zero.** Levels misconfigured so the mic is technically working but inaudible.
- **Failed mic hardware.** The array mic or its connection — genuinely rare.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the mic with the input meter

Ten seconds that split the problem in half.

1. Open **Settings > System > Sound**, scroll to **Input**.
2. Select your microphone (usually **Microphone Array** or **Realtek Audio**) and speak — watch the **input volume bar**.
3. **Bar moves:** hardware and driver work — the problem is permissions or app settings (Fixes 2–3).
4. **Bar flat:** driver, disabled device, or hardware — continue to Fixes 4–5.
5. Try the **Voice Recorder** app as a second test — if it records, the mic works and a specific app is the blocker.

### Fix 2: Check microphone privacy settings

The number-one cause of sudden mic death.

1. Open **Settings > Privacy & security > Microphone**.
2. Turn **Microphone access** **On** (the master switch).
3. Turn **Let apps access your microphone** **On** and enable the apps you use.
4. Scroll down and turn **Let desktop apps access your microphone** **On** — Zoom, Teams, Discord, and Chrome need this separate toggle.
5. Close and reopen the app that couldn't hear you — permission changes need an app restart to take effect.

### Fix 3: Set the correct input device and levels

Wrong device or zeroed levels mimic a dead mic.

1. In **Settings > System > Sound > Input**, make sure the **correct microphone** is selected — not a webcam mic, monitor mic, or disconnected headset.
2. Click the device, then **open its Properties** — set **Input volume** to 80–100.
3. Go to **More sound settings > Recording tab**, right-click the mic > **Properties > Levels** — raise **Microphone Boost** to **+20 dB** if the mic is quiet.
4. On the **Advanced** tab, uncheck **Allow applications to take exclusive control** as a test — exclusive mode lets one app starve the others.
5. Right-click in the Recording tab and enable **Show Disabled Devices** — your mic may be disabled and hiding.

### Fix 4: Reinstall the Realtek audio driver

The mic array is part of the Realtek codec — its driver owns the input path.

1. Open **Device Manager > Sound, video and game controllers**, right-click **Realtek Audio**, **Uninstall device** — check **Attempt to remove the driver for this device**.
2. Also check **Audio inputs and outputs** for the microphone entries and uninstall those.
3. Restart, then install the **audio driver** from your **laptop maker's support site** for your exact model.
4. Restart again, then repeat the Fix 1 input-meter test.
5. For Realtek-mic-specific breakage patterns, see [how to fix Realtek microphone not working in Windows 11 24H2](/articles/how-to-fix-realtek-microphone-not-working-in-windows-11-24h2/).

### Fix 5: Check the app's own audio settings

When the system test passes but one app hears nothing.

1. Open the app's settings: **Zoom > Settings > Audio**, **Teams > Settings > Devices**, **Discord > Voice & Video**.
2. Set the **microphone dropdown** explicitly to your laptop mic — never leave it on "Same as System" while diagnosing.
3. In Zoom, uncheck **Automatically adjust microphone volume** during testing — it can drive the level to zero.
4. In Teams, check **Devices** for a muted mic icon.
5. Close other apps that might hold the mic (OBS, Voice Recorder, browser tabs with mic permission).

### Fix 6: Run the recording-audio troubleshooter

Windows' automated check for input-path problems.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters > Recording Audio > Run**.
2. Select your microphone when prompted.
3. Let it apply fixes — it re-enables disabled devices and resets levels.
4. Retest with the input meter.
5. Microsoft's mic troubleshooting reference is on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: BIOS, system repair, and the hardware verdict

The last layer before concluding hardware.

1. Check the **BIOS** for a microphone/camera privacy toggle — some business laptops have a hardware mic kill (Lenovo, HP, Dell) that must be **Enabled**.
2. Run **Command Prompt as administrator**: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, restart.
3. Test the mic in **Safe Mode** or from a **Linux live USB** — working there proves the hardware is fine.
4. If the input meter never moves in any OS, with the correct driver installed and BIOS enabled, the mic array or its cable has failed.
5. A **USB headset or USB microphone** bypasses the internal mic entirely — the practical fix on an out-of-warranty laptop.

For the Windows 11 24H2-specific variant, see [how to fix microphone not working on laptop in Windows 11 24H2](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/).

## Closing

Laptop mic failures are privacy toggles, wrong input devices, and Realtek drivers — in that order of likelihood. The input-meter test tells you which half of the problem you're in within ten seconds, and from there the fixes are short. Hardware failure is the rare exception, so exhaust the software side first.
