---
title: "Microphone Not Working on Laptop: Step-by-Step Fix"
slug: how-to-fix-microphone-not-working-on-laptop-step-by-step
date: 2026-09-18
categories: ["drivers"]
tags: ["microphone not working", "laptop mic troubleshooting", "mic not detected"]
description: "Microphone not working on your laptop? Step-by-step fix for dead mics — permissions, levels, drivers, and hardware tests in the right order."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "What is the first step when a laptop mic stops working?"
    a: "Open Settings > System > Sound and check the Input section: confirm the right microphone is selected, the input volume is up, and the level bar moves when you speak. This thirty-second check identifies routing and mute problems, which are the most common causes."
  - q: "Why would privacy settings block my microphone?"
    a: "Windows requires explicit permission for apps to use the microphone, and these toggles can be reset by updates or turned off accidentally. If the mic works in the Settings test but not in your call app, the app's individual permission toggle is almost certainly the blocker."
  - q: "How do I know if it is a driver problem?"
    a: "Driver problems show a pattern: the mic vanished from Settings entirely, it broke immediately after a Windows update, or Device Manager shows the audio device with a warning. In those cases, reinstalling the manufacturer's audio driver is the fix. When in doubt, reinstall the manufacturer's audio driver anyway; it is quick, safe, and resolves a wide range of capture problems."
  - q: "When should I suspect the microphone hardware?"
    a: "Only after software is exhausted: permissions correct, levels up, driver reinstalled, and an external USB mic works fine while the built-in one stays dead across all apps. Built-in mic arrays rarely fail, so reach this conclusion last, not first."
---

A dead laptop microphone derails calls, recordings, and voice commands — and the fix depends entirely on which layer failed. The mic might be blocked by privacy settings, muted in a hidden control panel, routed to the wrong device, broken by a driver update, or (rarely) physically dead. Each layer has a telltale symptom, and checking them in order turns a confusing problem into a short one.

This step-by-step guide is the complete microphone diagnostic, from the thirty-second Settings check to the hardware fork at the end. Test the mic after each step — most people find their voice back well before the end.

## Why this happens

- **Privacy permissions blocking apps:** Windows denies mic access per app; one toggle silences everything.
- **Wrong input device selected:** Capture routes to a disconnected headset instead of the built-in array.
- **Hidden mute in Sound control panel:** The legacy Levels tab mutes the mic invisibly from modern Settings.
- **Exclusive mode lock:** One application captures the mic exclusively, starving others.
- **Audio driver broken by update:** The update's driver mishandles the microphone endpoint.
- **Enhancements corrupting capture:** Buggy APO processing silences or distorts the mic stream.
- **Disabled device in Device Manager:** The mic array gets disabled during driver migrations.
- **Hardware failure:** Dead mic array or detached ribbon cable — the last-resort diagnosis.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the input device, volume, and live level

The foundational check — do this before anything else.

1. Go to **Settings > System > Sound**. Under **Input**, select your built-in microphone (**Microphone Array** or similar).
2. Set **Input volume** to 80–100.
3. Speak at normal volume and watch the level bar — movement means Windows hears you and the problem is app-specific (skip to Fix 2).
4. If no input device is listed at all, jump to Fix 5 (Device Manager) — the driver is not loading the mic.

A moving level bar with no sound in your app is actually good news: the hardware and driver work, and only routing or permissions stand in the way.

### Fix 2: Grant microphone privacy permissions

Windows 11's permission model is the top mic blocker.

1. Go to **Settings > Privacy & security > Microphone**.
2. Turn on **Microphone access**, **Let apps access your microphone**, and **Let desktop apps access your microphone**.
3. Enable the toggle for your specific app (Zoom, Teams, Discord, browser).
4. Restart the app and test.

Corporate-managed laptops may have these locked by policy — if toggles are grayed out, your IT admin controls them. For the Windows 11-specific walkthrough, see our [Windows 11 microphone guide](/articles/how-to-fix-microphone-not-working-on-laptop-on-windows-11/).

### Fix 3: Unmute in the legacy Sound panel and disable exclusive mode

The classic hidden-mute hunt.

1. Open **Settings > System > Sound > More sound settings** and go to the **Recording** tab.
2. Double-click your microphone. On the **Levels** tab, drag the slider up and click the speaker icon if it shows muted.
3. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device** and uncheck **Give exclusive mode applications priority**.
4. Click **Apply** and test in your app.

Exclusive mode is the stealthiest mic killer: everything looks configured, the level bar moves in Settings, but the call app hears silence because another app holds the mic hostage.

### Fix 4: Disable enhancements and restart audio services

Two quick software resets.

1. In the microphone's properties (**Enhancements** tab), check **Disable all enhancements**.
2. Press **Win + R**, type `services.msc`, and restart **Windows Audio** and **Windows Audio Endpoint Builder**.
3. Retest the mic.

If the mic worked, then died after sleep or hibernate, the service restart is your clue — something in the resume path breaks audio capture, and the driver reinstall in Fix 6 is the durable cure.

### Fix 5: Re-enable the mic in Device Manager

For mics missing from Settings entirely.

1. Open Device Manager, expand **Audio inputs and outputs**.
2. Right-click any grayed-out microphone and choose **Enable device** (click **View > Show hidden devices** first).
3. Also check **Sound, video and game controllers** for the audio device — enable it if disabled.
4. Restart the audio services from Fix 4 and recheck Settings.

A mic that appears here but not in Settings is a service/endpoint problem; a mic missing here too is a driver problem — which is Fix 6.

### Fix 6: Clean-reinstall the manufacturer's audio driver

The durable fix for update-broken microphones.

1. Download the audio driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. In Device Manager, uninstall the audio device under **Sound, video and game controllers**, checking **Attempt to remove the driver for this device**.
3. Restart, install the downloaded driver, restart again.
4. Re-verify input device selection and levels (Fix 1), since a fresh driver resets them.

Vendor drivers include mic-array beamforming tuning that generic drivers lack — this is why manufacturer drivers specifically fix "mic too quiet or dead" complaints. If your mic issues involve [Realtek-specific problems](/articles/best-way-to-fix-realtek-microphone-not-working/), that guide goes deeper on the codec side.

### Fix 7: Hardware isolation with an external mic

The final fork, done properly.

1. Plug in a USB headset or USB microphone. If it works perfectly, Windows' capture pipeline is healthy and the built-in array is the suspect.
2. Test the built-in mic in the BIOS diagnostics or manufacturer hardware test if available.
3. Try a Linux live USB: if the built-in mic works there, a Windows software issue remains (consider an in-place repair install); if dead there too, it is hardware.
4. For confirmed hardware failure, use the USB mic as your workaround and get a repair quote — mic arrays live under the bezel or palmrest and need professional replacement.

The Linux live-USB test is decisive because it bypasses your entire Windows driver stack — whatever happens there is about the hardware, full stop.

## Closing

Microphone failures yield to ordered diagnosis: verify input selection and live levels, grant privacy permissions, hunt hidden mutes and exclusive-mode locks, then reinstall the manufacturer's audio driver if the trail points at software. The external-mic and Linux tests at the end give you a definitive hardware verdict — so you never replace a laptop over a problem a driver reinstall would have fixed.
