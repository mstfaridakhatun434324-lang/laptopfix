---
title: "USB Headset Not Working on Your Laptop? Try These Fixes"
slug: how-to-fix-usb-headset-not-working
date: 2026-09-08
categories: ["drivers"]
tags: ["usb headset", "headset not working", "audio", "microphone", "usb audio"]
description: "USB headset not working on your Windows laptop? Fix silent playback and dead microphones with device selection, driver repair, and USB audio resets."
thumbnail: "/images/thumbs/how-to-fix-usb-headset-not-working.webp"
faqs:
  - q: "Why does my USB headset show up but produce no sound?"
    a: "Windows is likely sending audio to a different output, or the headset's own volume is muted. Open Sound settings and confirm the USB headset is the selected output device, then check the volume mixer for app-level mutes. USB headsets are separate audio devices, so the speaker volume setting does not affect them."
  - q: "My USB headset microphone is not detected. How do I fix it?"
    a: "Open Sound settings, go to Input, and select the headset's microphone explicitly — Windows often keeps the laptop's internal mic selected. Also check Privacy & security, Microphone, to confirm apps may access the microphone. USB headsets expose playback and recording as separate devices that must each be selected."
  - q: "The USB headset works on another computer. What does that mean?"
    a: "The headset is fine and the fault is in your laptop: its USB audio driver, USB port power management, or sound settings. Work through the driver reinstall and port fixes in this guide. Testing on another machine is the single most useful isolation step because it halves the problem instantly."
  - q: "Should I install the headset manufacturer's software?"
    a: "Only if you need its extra features like surround profiles or EQ. For basic functionality, Windows' built-in USB audio driver is reliable and simpler. Install the manufacturer's suite after the headset works natively — adding it to a broken setup just adds another suspect to the investigation."
---

A USB headset is two devices in one: a USB audio output and a USB microphone input, each independently selectable, mutable, and breakable. That is why USB headset failures are so confusing — the headphones can work while the mic is dead, or the mic works while playback stays silent. Each half has its own device entry, its own default selection, and its own driver path.

The fix sequence handles both halves: prove the headset on another machine, fix device selection, repair the USB audio driver, tame power management, and test the ports. Work both halves deliberately instead of assuming one fix covers both.

## Why this happens

- **Wrong device selected:** Windows keeps the old output or input selected after the headset is plugged in.
- **USB audio driver corruption:** The generic USB audio driver corrupts, killing one or both halves.
- **USB selective suspend:** Power saving suspends the headset's USB port, dropping audio mid-call.
- **App-level mute or wrong device:** Meeting apps keep their own device selections that override system defaults.
- **Privacy settings blocking the mic:** Microphone access denied globally or per-app silences the input half.
- **Underpowered USB port:** Some headsets need more current than a strained port delivers, causing dropouts.
- **Faulty headset or cable:** The headset itself fails — proven or ruled out by testing elsewhere.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Isolate with another computer and another port

Plug the headset into a different computer or a phone with a USB adapter. Fully working there proves the headset is good and aims everything at the laptop. Back on the laptop, try a different USB port — preferably a rear or opposite-side port on the other USB controller — and avoid unpowered hubs for testing. Note exactly which half fails: playback, microphone, or both. "Mic dead, playback fine" is a selection or privacy issue; "both dead" is driver or port. This isolation takes five minutes and prevents fixing the wrong half of the problem.

### Fix 2: Select the headset as output and input explicitly

Right-click the speaker icon, open Sound settings, and set the USB headset as the Output device — play a test tone. Then scroll to Input and set the headset's microphone as the input device — speak and watch the input level meter move. Open the volume mixer and confirm your apps are not muted or routed elsewhere. Then open your meeting app's own audio settings (Teams, Zoom) and select the headset there too — apps cache their own device choices independently of Windows. Wrong-device selection is the most common cause of "headset connected but silent," and it hides in three separate places.

### Fix 3: Check microphone privacy permissions

Open Settings, Privacy & security, Microphone. Confirm "Microphone access" is on, "Let apps access your microphone" is on, and your specific apps are allowed. USB headset mics are gated by these permissions exactly like the built-in mic — a denied permission produces a "mic not working" with no error message. After enabling, fully close and reopen the app; permission changes do not always reach running apps. Test with Windows' built-in Voice Recorder first to separate a system-level mic failure from an app-level one. For broader mic failures, our guide to [microphone not working](/articles/how-to-fix-microphone-not-working-on-laptop-on-windows-11/) covers the built-in side.

### Fix 4: Reinstall the USB audio driver

Open Device Manager (Win + X), expand "Sound, video and game controllers" and "Audio inputs and outputs," and uninstall the USB headset entries with driver deletion. Unplug the headset, restart, plug it back into a different port, and let Windows install the USB audio driver fresh. This clears the corrupted driver state behind headsets that appear in Device Manager with warnings or as unknown devices. Avoid installing third-party "USB audio enhancer" drivers during testing — use the plain Windows USB audio driver first, and add manufacturer software only after the basics work. For related USB device failures, see our guide to [USB devices not recognized](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

### Fix 5: Disable USB power management for the headset

In Device Manager, under Universal Serial Bus controllers, open each USB Root Hub's Properties and uncheck "Allow the computer to turn off this device to save power" on the Power Management tab. Also disable USB selective suspend in Power Options advanced settings. USB headsets are notorious victims of power saving: audio drops mid-call or the mic vanishes after the laptop sleeps, because the port never properly resumes the headset. Retest across a sleep cycle after making these changes. If dropouts stop, power management was the cause — leave it off for the hubs the headset uses.

### Fix 6: Update chipset drivers and test port power

The USB audio path depends on the chipset's USB controller. Install the latest chipset driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) for your exact model and reboot. Then consider power: if the headset crackles or disconnects on one port but works on another, the weak port may not deliver enough current — use the stronger port or a powered hub. High-end headsets with built-in DACs and amplifiers draw more power than basic ones. After the chipset update, re-verify the headset on the previously failing port; controller-level fixes often resolve what looked like a headset fault. Microsoft's Windows support hub documents USB audio troubleshooting as supplementary reference.

### Fix 7: Reset the app audio and test hardware failure

In Settings, System, Sound, open the Volume mixer and choose "Reset" to return all app sound devices to system defaults — this clears per-app routings that survive device changes. Then test the headset's hardware honestly: does it fail identically on two computers and two cables (if detachable)? Do the earcups or mic boom show damage? A headset that fails everywhere is simply broken — cables fray at strain reliefs, and USB connectors wear. If it is under warranty, the isolation evidence from Fix 1 makes the claim straightforward. If it works everywhere except one app, reinstall that app — its audio engine, not the headset, is the fault.

## Closing

USB headsets fail in halves, and each half — playback device, input device, driver, port power — gets its own check. Isolate on another machine, select both halves explicitly, clear privacy blocks, reinstall the USB audio driver, tame power management, and update the chipset. Run both halves through the sequence and the headset either works or has earned a warranty claim with a clean test log to back it.
