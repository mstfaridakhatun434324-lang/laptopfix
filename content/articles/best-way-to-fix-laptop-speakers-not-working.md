---
title: "Laptop Speakers Not Working? The Best Way to Fix Them (Windows 10/11)"
slug: best-way-to-fix-laptop-speakers-not-working
date: "2026-10-09"
categories: ["drivers"]
tags: ["laptop speakers", "no audio", "speaker driver", "sound settings", "windows audio"]
description: "Laptop speakers suddenly silent? This guide walks through the best way to fix speakers not working on Windows 10 and 11, from quick checks to driver repair."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-speakers-not-working.webp"
faqs:
- q: "Why did my laptop speakers suddenly stop working?"
  a: "The most common triggers are a Windows update replacing the audio driver, the wrong output device selected after unplugging headphones or HDMI, or the Windows Audio service stalling. Physical speaker failure is comparatively rare. Because software causes dominate, running through output selection, the audio troubleshooter, and a driver reinstall resolves the problem in most cases without any hardware repair."
- q: "How can I tell if my laptop speakers are physically broken?"
  a: "Boot into the BIOS or run the manufacturer's built-in speaker test, which plays sound independently of Windows. If the test tone plays, the speakers and their wiring are fine and the fault is software. You can also boot a Linux live USB — sound in Linux proves the hardware works. Silence in both tests points to failed speakers or a disconnected cable, which needs physical repair."
- q: "Will reinstalling the audio driver delete my sound settings?"
  a: "It may reset volume levels, enhancements, and equalizer presets to defaults, so note any custom settings first. Your files and applications are untouched. After reinstalling the manufacturer's audio driver and restarting, reopen the Sound settings to restore your preferred volume and re-enable any enhancements you were using before the problem started."
- q: "Why do my speakers work with headphones but not on their own?"
  a: "This usually means Windows is still routing audio to the headphone jack even after unplugging, often because jack detection failed or the driver did not switch back. Manually setting the internal speakers as the default playback device fixes it. If unplugging never switches output, the headphone jack's detection switch may be stuck, and the driver reinstall in this guide typically recalibrates it."
---

One moment your laptop plays sound normally; the next, total silence. No error message, no warning — videos play mute, system sounds vanish, and the volume slider moves as if everything is fine. It is one of the most common Windows complaints, and also one of the most fixable, because the speakers themselves are rarely the problem.

Audio on a laptop passes through a chain: application, Windows mixer, audio service, driver, and finally the speaker hardware. A break at any link produces the same symptom — silence — which is why random setting-tweaking feels so hopeless. The method that works is walking the chain in order, from the easiest checks to the driver repair that fixes most stubborn cases.

This guide does exactly that. Each fix below targets one link in the chain, starting with the thirty-second checks and ending with the deeper repairs. Follow them in order and stop when sound returns.

## Why this happens

- **Wrong output device selected**: Unplugging headphones or HDMI can leave Windows routing audio to a device that is no longer there.
- **Windows Audio service stalled**: The background service that mixes all sound can hang after updates or sleep, muting everything.
- **Corrupted or replaced audio driver**: Updates frequently swap the vendor driver for a generic one that fails to drive the speakers.
- **Muted at the driver or app level**: Per-app volume in the mixer can mute a single application while everything else looks normal.
- **Broken audio enhancements**: A corrupted enhancement chain in the driver can silence output entirely.
- **Headphone jack detection stuck**: A worn jack can convince the driver headphones are still plugged in, keeping speakers off.
- **Failed speaker hardware**: Least common, but blown speakers or a loose internal cable produce silence no software fix can cure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check volume, mute, and the output device

Start with the obvious, because it is the cause more often than anyone admits. The system volume, a per-app mute in the volume mixer, or audio routed to a phantom device (a disconnected monitor, a long-gone Bluetooth speaker) all produce convincing silence. This check takes under a minute and resolves a surprising share of cases.

1. Click the speaker icon and confirm the volume is up and not muted.
2. Right-click the speaker icon, open the Volume Mixer, and check no individual app is muted.
3. In Sound settings, confirm the Output device is your laptop's internal speakers.
4. If headphones or a monitor is listed instead, switch output to the speakers manually.
5. Play a test sound — if you hear it, the problem was routing, not hardware.

### Fix 2: Run the Windows audio troubleshooter

Windows includes a troubleshooter that audits the whole audio chain automatically — device status, default selection, driver state, and service health. It is not magic, but it catches misconfigurations quickly and applies safe fixes on its own. Run it before manual driver work; when it works, it saves ten minutes.

1. Open Settings, go to System, Sound, and scroll to the Advanced section.
2. Click "Troubleshoot common sound problems" next to Output.
3. Select your speakers when prompted and let the scan complete.
4. Apply any recommended fix and restart if the troubleshooter asks.
5. Test playback afterward; if silence persists, continue below.

### Fix 3: Update or reinstall the audio driver

This is the fix that resolves most stubborn cases. The audio driver translates Windows' digital stream into signals the speakers understand, and when an update corrupts or replaces it, output dies silently. Reinstalling the manufacturer's driver restores the full, matched audio stack. Microsoft's [update catalog](https://www.catalog.update.microsoft.com/) can supply specific driver versions if your maker's page is missing one.

1. Press Win + X, open Device Manager, and expand "Sound, video and game controllers."
2. Right-click your audio device (Realtek, Intel, or similar) and choose "Update driver," then automatic search.
3. If that fails, choose "Uninstall device," tick "Attempt to remove the driver," and restart.
4. After restart, if sound is still absent, download the audio driver from your laptop maker's support page, install it, and restart again.
5. Confirm the device shows no warning icon and test playback.

### Fix 4: Restart the Windows Audio services

If the driver is healthy but no application produces sound, the mixing services themselves may be hung. Windows Audio and its endpoint builder service sit between every app and the driver; when they stall — common after sleep/wake cycles — the entire chain goes quiet. Restarting them rebuilds the audio graph without touching drivers or settings.

1. Press Win + R, type `services.msc`, and press Enter.
2. Right-click "Windows Audio" and choose Restart.
3. Right-click "Windows Audio Endpoint Builder" and choose Restart.
4. Set both services' startup type to Automatic if they are not already.
5. Play audio to confirm the services are mixing sound again.

### Fix 5: Disable audio enhancements

Driver-level enhancements — bass boost, virtual surround, loudness equalization — process every sound before it reaches the speakers. When that processing chain corrupts, the result is silence rather than merely bad sound. Disabling enhancements bypasses the broken layer; if sound returns, you have found the culprit and can leave them off or reinstall the driver.

1. Right-click the speaker icon, choose Sound settings, then "More sound settings."
2. On the Playback tab, double-click your speakers.
3. Open the Enhancements tab and tick "Disable all enhancements."
4. Click Apply and test playback immediately.
5. If sound returns, keep enhancements off or reinstall the driver to repair them.

### Fix 6: Test the speakers outside Windows

Before concluding the hardware is dead, prove it. Manufacturer diagnostics and a Linux live USB play sound without involving your Windows installation at all. Sound in either test means the speakers, amplifier, and cables are fine and the fault is purely software — which keeps you on the repair path instead of shopping for a repair shop.

1. Restart and open your manufacturer's built-in diagnostics (often F12 at boot) and run the speaker/audio test.
2. Alternatively, boot a Linux live USB and play any audio file.
3. If you hear sound in either test, return to Windows and continue with Fix 7.
4. If both are silent, the speakers or their internal cable have likely failed.
5. For hardware failure, check warranty status before paying for repair — speaker replacement is usually inexpensive.

### Fix 7: Reset the audio stack with a system restore

When every targeted fix fails, the damage may be spread across the registry and system files in ways no single reinstall reaches. A system restore rolls the audio subsystem back to a point when sound worked, undoing whatever update or install broke it. It leaves personal files alone while reverting drivers and system configuration.

1. Search for "Create a restore point," open System Protection, and click "System Restore."
2. Choose a restore point dated before the sound stopped working.
3. Complete the wizard and let the laptop restart.
4. Test the speakers after the restore finishes.
5. If no restore point exists, use Settings, System, Recovery, "Reset this PC" with the keep-my-files option as a last resort.

If sound works through headphones but the speakers stay silent, our guide on [laptops not detecting headphones](/articles/how-to-fix-laptop-not-detecting-headphones/) covers the jack-detection side of the same problem. For the complete silence scenario with no output device at all, see the [step-by-step no-sound guide](/articles/how-to-fix-no-sound-on-laptop-step-by-step/).

## Closing

Silent laptop speakers are a software problem far more often than a hardware one — wrong output device, stalled audio service, or a driver an update mangled. Walk the chain from the volume mixer to the driver reinstall, prove the hardware with an outside-Windows test before giving up, and sound comes back on the great majority of machines.
