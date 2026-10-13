---
title: "Windows 10 Laptop Not Detecting Headphones: Step-by-Step Repair"
slug: how-to-fix-laptop-not-detecting-headphones-on-windows-10
date: 2026-10-06
categories: ["drivers"]
tags: ["headphones not detected", "windows 10", "audio driver", "realtek", "sound settings"]
description: "Headphones ignored by your Windows 10 laptop? Work through jack detection, driver, and sound-setting fixes in the right order."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-detecting-headphones-on-windows-10.webp"
faqs:
  - q: "Why did my headphones stop being detected after a Windows 10 update?"
    a: "Windows 10 updates frequently replace the manufacturer's Realtek audio driver with the generic Microsoft HD Audio driver, which handles jack detection poorly on many laptop models. Updates also reset the default playback device to the speakers. The fix is to check the playback device selection first, then reinstall the audio driver from your laptop manufacturer's support page for Windows 10."
  - q: "The headphones show in Device Manager but not in Sound settings. What now?"
    a: "Device Manager shows the audio hardware while Sound settings shows playback endpoints — a device can exist in one without appearing in the other. If the headphones are missing from the Playback tab, right-click in the tab and enable Show Disabled Devices and Show Disconnected Devices. Headphones disabled by a driver change hide there, and re-enabling them restores the endpoint immediately."
  - q: "Is the headphone jack broken if wiggling the plug changes the sound?"
    a: "Intermittent sound when wiggling the plug points to a physical problem — a worn jack, a damaged plug, or lint packed in the socket — rather than a driver issue. Try a different pair of headphones first to rule out the plug, then clean the jack gently with a dry cotton swab. If multiple headphones all cut in and out, the jack itself likely needs replacement."
  - q: "Can I make Windows 10 ask me what I plugged in like it used to?"
    a: "Yes — that popup comes from the Realtek HD Audio Manager's jack detection, and it disappears when the generic Microsoft driver replaces the Realtek one. Reinstalling the manufacturer's Realtek driver package restores the Realtek Audio Console with its connector settings, including the 'which device did you plug in' dialog and front-panel jack detection options."
---

Windows 10 has handled headphone jacks for a decade, yet headphone detection still breaks with depressing regularity — usually right after an update. The symptom set is familiar: plug in wired headphones and the sound stays on the speakers, no device appears in the playback list, or the headphones appear but produce silence. On Windows 10 the culprit is almost always the audio driver or the playback device configuration, both of which you can repair in minutes once you know where to look.

This guide is ordered as a true diagnostic sequence: confirm the hardware, fix the routing, then repair the driver. Each step eliminates a cause before you move on. For the Windows 11 version of this problem, see our [Windows 11 headphone guide](/articles/how-to-fix-laptop-not-detecting-headphones-on-windows-11/), and the [step-by-step headphone repair plan](/articles/how-to-fix-laptop-not-detecting-headphones-step-by-step/) covers the full methodical approach across both systems.

## Why this happens

- **A Windows 10 update replaced the manufacturer's Realtek driver** with the generic Microsoft HD Audio driver that detects jacks poorly.
- **The headphones are disabled in the Playback tab**, hidden from view until disabled devices are shown.
- **The speakers remained the default playback device** after the headphones were plugged in.
- **Jack detection is misconfigured or broken** in the Realtek control panel.
- **The Windows Audio service glitched** and stopped enumerating newly connected devices.
- **The headphone plug or jack is physically worn**, causing intermittent or absent detection.
- **A third-party audio utility** (equalizers, virtual surround tools) hijacked the audio pipeline.

- **Windows 10's 'default communication device' vs 'default device' split** sends call audio to the headphones while media keeps playing on the speakers, which looks like partial detection failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the headphones and the jack physically

Eliminate hardware before spending time in software. Test both earbud channels — single-ear failures indicate a damaged cable, not a laptop problem.

1. Try the headphones on a phone or another computer to confirm they work.
2. Try a different pair of headphones in the laptop's jack.
3. Inspect the jack for lint or debris and clean it gently with a dry cotton swab.
4. If the known-good headphones fail in the laptop but work elsewhere, the problem is software — continue.

### Fix 2: Select the right playback device

Windows 10 does not always switch outputs automatically. Set the headphones as both Default Device and Default Communication Device to avoid split routing.

1. Click the speaker icon in the system tray and use the dropdown to pick your headphones.
2. If they are not listed, right-click the speaker icon and choose Sounds.
3. In the Playback tab, right-click empty space and tick Show Disabled Devices and Show Disconnected Devices.
4. Right-click the headphones, choose Enable, then Set as Default Device.

### Fix 3: Reinstall the audio driver

The core fix for detection failures — restore the manufacturer's driver. On older laptops the audio vendor may be IDT or Conexant rather than Realtek — the same steps apply.

1. Press Win + X, open Device Manager, and expand Sound, video and game controllers.
2. Right-click the Realtek (or IDT/Conexant) audio device and choose Uninstall device.
3. Tick Delete the driver software for this device if offered, then restart.
4. Download the audio driver from your laptop manufacturer's support page for Windows 10 and install it. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents the Device Manager workflow.

### Fix 4: Restore the Realtek jack-detection popup

The "what did you plug in" dialog is a Realtek feature that vanishes with the generic driver. If the Realtek manager never appears after installing the driver, reinstall with antivirus temporarily disabled.

1. After installing the manufacturer's driver, open Realtek HD Audio Manager or Realtek Audio Console.
2. Open Device advanced settings or the connector settings (wrench/folder icon).
3. Enable front panel jack detection and the plug-in dialog option.
4. Plug in the headphones and confirm the dialog appears and the device switches.

### Fix 5: Restart the Windows Audio services

A stuck audio service ignores newly plugged hardware. Restart both audio services together — restarting only one sometimes leaves the pipeline half-reset.

1. Press Win + R, type services.msc, and press Enter.
2. Restart the Windows Audio service.
3. Restart the Windows Audio Endpoint Builder service.
4. Unplug and replug the headphones, then check the Playback tab.

### Fix 6: Remove interfering audio software

Third-party audio tools can seize the output pipeline. VoIP apps install virtual audio devices that can become the default — check the full playback list.

1. Check for installed equalizers, virtual surround apps, or VoIP tools with audio drivers (check [mic-related conflicts](/articles/how-to-fix-microphone-not-working-on-laptop-on-windows-10/) too if voice apps are involved).
2. Temporarily uninstall or disable them one at a time.
3. Test headphone detection after each removal.
4. Keep only the tools you actively use, updated to their latest versions.

### Fix 7: Run the audio troubleshooter

Windows 10's troubleshooter still catches configuration errors reliably. Run the troubleshooter with the headphones plugged in so it can see the actual device state.

1. Go to Settings, Update and Security, Troubleshoot, Additional troubleshooters.
2. Run Playing Audio and follow every prompt.
3. Apply its recommended fixes even when they seem obvious.
4. Retest with the headphones plugged in from the start.

## Closing

On Windows 10, headphone detection comes down to three things: the physical jack, the playback device selection, and the manufacturer's audio driver. Work them in that order and you will find the fault quickly — most cases end at Fix 2 or Fix 3. Reserve hardware suspicion for jacks that behave intermittently with multiple known-good headphones, which is the signature of a worn socket, not a driver. Keep a known-good pair of earbuds as your diagnostic reference — having proven hardware on hand turns every future audio problem into a five-minute isolation test. And once detection works, avoid third-party 'audio enhancer' tools that hook the output pipeline, since they are a recurring source of the exact problem you just fixed.
