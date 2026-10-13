---
title: "Realtek Audio Not Working? A Step-by-Step Repair Guide"
slug: how-to-fix-realtek-audio-not-working-step-by-step
date: 2026-09-09
categories: ["drivers"]
tags: ["realtek audio", "no sound", "audio driver", "windows 11", "speakers not working"]
description: "No sound from Realtek audio on Windows 11? Follow this step-by-step guide through output checks, driver reinstalls, and Windows audio service repairs."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-step-by-step.webp"
faqs:
  - q: "Why is there a red X on my speaker icon?"
    a: "The red X means Windows sees no working audio output device. The Realtek driver is usually missing, corrupted, or disabled. Reinstalling the audio driver from your laptop maker's support site clears it in most cases — the X disappears as soon as a working driver binds to the codec."
  - q: "Why do my speakers work but headphones don't (or vice versa)?"
    a: "Speakers and the headphone jack are separate endpoints in the Realtek driver, and one can fail while the other works. Check that the correct device is set as default, and look in the Realtek Audio Console for jack-detection settings — a stuck jack sensor can mute the speakers permanently."
  - q: "Can Windows Update break Realtek audio?"
    a: "It is one of the most common causes. Windows Update replaces manufacturer-tuned Realtek drivers with generic builds that may not match your laptop's codec configuration. The result ranges from no sound to missing enhancements. Rolling back or reinstalling the OEM driver fixes it."
  - q: "What is the difference between Realtek Audio and Realtek Audio Universal?"
    a: "Realtek Audio Universal (UAD) is the modern driver model using Microsoft Store console apps; the older HDA model used a desktop control panel. They are not interchangeable — install whichever type your laptop maker's support page offers for your model, or the console app will not work."
---

No sound. The speaker icon shows a red X, or everything looks normal but silence comes out of the speakers. Realtek audio chips power the sound on the vast majority of Windows laptops, which makes Realtek driver problems the single most common audio failure in the Windows world.

The tricky part: 'no sound' has at least six distinct causes — wrong output device, muted at a hidden layer, dead driver, stopped Windows service, jack detection stuck, or enhancements crashing the pipeline. Each needs a different fix, and reinstalling drivers blindly only helps one of them.

This guide diagnoses first. You will verify the output path, check every mute layer, repair the driver properly, and fix the Windows audio services — step by step, in the order that finds the fault fastest.

## Why this happens


- **Wrong default output device:** Sound routes to a monitor, USB headset, or disconnected Bluetooth device instead of the Realtek speakers.
- **Generic driver replaced the OEM build:** Windows Update swaps the tuned Realtek driver for a generic one mismatched to the laptop's codec.
- **Windows Audio service stopped:** The AudioSrv or AudioEndpointBuilder service can stop after updates, silencing everything.
- **Jack detection stuck:** A worn headphone jack sensor tells the driver headphones are plugged in forever, muting the speakers.
- **Enhancement pipeline crash:** Corrupt audio enhancements can crash the processing chain, producing silence despite normal-looking settings.
- **Realtek device disabled in BIOS:** Firmware updates can disable the HD Audio controller, removing the device from Windows entirely.
- **Corrupt driver installation:** Partial updates leave the driver half-installed — Device Manager looks fine, but no sound emerges.
- **Muted at the app or mixer layer:** Individual apps or the volume mixer can be muted while the master volume looks normal.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Verify the output device and every mute layer


Half of all 'no sound' reports are routing or mute issues, not driver failures. This check walks every layer where sound can be silenced — it takes three minutes and needs no downloads.

1. Click the speaker icon in the taskbar and confirm the output device is your Realtek speakers — not a monitor or old Bluetooth device.
2. Right-click the speaker icon, Open volume mixer, and check that no app is muted and the master is up.
3. Open Settings, System, Sound, and confirm the correct output and that volume is above zero.
4. In the Realtek Audio Console (Microsoft Store), check speaker configuration and jack status.
5. Play the Windows test sound: Sound settings, More sound settings, your device, Properties, Advanced, Test.

### Fix 2: Restart the Windows audio services


When the output device looks right but the test sound produces silence, the Windows audio engine itself may be stalled. Restarting its services rebuilds the pipeline without touching drivers.

1. Press Windows + R, type services.msc, and press Enter.
2. Find Windows Audio, right-click, Restart.
3. Find Windows Audio Endpoint Builder, right-click, Restart.
4. Set both Startup types to Automatic.
5. Replay the test sound. If sound returns, a stalled service was the culprit.

### Fix 3: Reinstall the Realtek driver from your laptop maker


The definitive driver fix. Your laptop maker's Realtek package matches your exact codec and includes the console app integration that generic drivers lack. The driver-removal checkbox is essential — otherwise Windows keeps the broken version.

1. In Device Manager, expand Sound, video and game controllers.
2. Right-click Realtek Audio (or Realtek(R) Audio), Uninstall device — check Attempt to remove the driver for this device.
3. Restart the laptop.
4. Download the Audio driver for your exact model from your maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)).
5. Install it, restart, and run the test sound.
6. Confirm the Realtek Audio Console now opens and shows your devices.

### Fix 4: Roll back a bad driver update


If sound died right after an update, the previous driver worked and the new one does not. Rolling back is the fastest possible fix — seconds, not minutes.

1. In Device Manager, right-click the Realtek device, Properties, Driver tab.
2. If Roll Back Driver is available, click it, choose a reason, and confirm.
3. Restart and test sound.
4. If rollback is greyed out, use Microsoft's wushowhide troubleshooter to hide the bad audio update, then reinstall your maker's driver.
5. Consider disabling automatic driver updates afterward to prevent a repeat.

### Fix 5: Disable enhancements and test


Corrupt audio enhancements can crash the entire output pipeline while every setting looks normal. Disabling them isolates whether the raw driver works.

1. Right-click the speaker icon, Sound settings, More sound settings.
2. Double-click the Realtek speakers, Enhancements tab — check Disable all enhancements, Apply.
3. On the Advanced tab, uncheck Allow applications to take exclusive control of this device (exclusive mode can also silence output).
4. Test sound. If it works now, re-enable enhancements one at a time to find the crashing one — or leave them off.

### Fix 6: Check BIOS and rule out hardware


When Device Manager shows no Realtek device at all — not even hidden — the audio controller may be disabled in firmware. And when correct drivers on every endpoint still produce silence, hardware is the remaining suspect.

1. Enter BIOS/UEFI and verify the HD Audio Controller is enabled under Advanced settings.
2. Test with wired headphones and a Bluetooth speaker to split speaker-specific from pipeline-wide failure.
3. Boot a Linux live USB and test audio there — working sound in Linux proves a Windows/driver problem.
4. If no endpoint produces sound with correct drivers, the codec chip may have failed — contact your maker's support.
5. For the Dolby-flavored version of this problem, see our [Lenovo Dolby Audio fix](/articles/how-to-fix-dolby-audio-not-working-on-lenovo-laptop/) or the general [Realtek driver troubleshooting](/articles/realtek-audio-driver-not-working-windows-11/).

## Closing


Realtek audio failures reward methodical diagnosis: output routing first, services second, drivers third, firmware last. Most cases end at step one or three — a wrong default device or a generic driver Windows Update installed over your maker's tuned build. Keep the OEM driver pinned afterward, and your sound stays where it belongs.
