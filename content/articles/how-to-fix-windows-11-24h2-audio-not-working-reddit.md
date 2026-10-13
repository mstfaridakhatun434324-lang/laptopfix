---
title: "No Sound After the Windows 11 24H2 Update? Restore Your Audio"
slug: how-to-fix-windows-11-24h2-audio-not-working-reddit
date: 2026-09-16
categories: ["windows-update"]
tags: ["audio not working", "windows 11 24h2", "no sound", "realtek"]
description: "Fix audio not working after the Windows 11 24H2 update: restore the correct driver, re-enable devices, and get sound back on your laptop."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-reddit.webp"
faqs:
  - q: "Why does every major Windows update seem to break audio?"
    a: "Audio drivers are deeply integrated with power management and the OS audio stack, and both change in feature updates. The update migrates, replaces, or resets the driver, and any mismatch — wrong driver version, disabled device, muted enhancement — silences the output. The hardware is almost never the problem."
  - q: "Should I use the laptop maker's audio driver or Realtek's generic one?"
    a: "The laptop maker's, in nearly every case. Makers customize Realtek drivers for their specific speaker and microphone hardware, including the audio enhancements and jack detection. Generic Realtek drivers often produce sound but lose features — or produce nothing at all on heavily customized designs."
  - q: "My Bluetooth audio works but speakers do not — what does that mean?"
    a: "It means the OS audio stack is fine and the problem is isolated to the onboard audio device or its driver. Bluetooth audio bypasses the Realtek/Conexant hardware entirely. Focus your troubleshooting on the onboard audio driver in Device Manager, not on Windows' sound settings generally."
  - q: "Can Windows Update be stopped from breaking audio again?"
    a: "After restoring the working manufacturer driver, hide the audio driver offerings with the show/hide updates troubleshooter so Windows Update stops replacing it. This is a legitimate, targeted use of driver hiding — the audio driver is one of the few where the manufacturer's version is consistently better than the catalog's."
---

The 24H2 update finishes, you open a video, and there is silence. No error, no warning — just no sound, or a red X on the speaker icon, or audio devices that vanished from the list entirely. Before you assume the speakers died coincidentally, know this: post-update audio failure is a driver and configuration problem in the overwhelming majority of cases, and it is fixable in minutes once you find the right layer.

Audio has more layers than people expect — the driver, the Windows audio services, the output device selection, enhancements, and app-level routing. This guide checks them in the order that finds the break fastest.

## Why this happens

- **Driver replaced or migrated badly:** 24H2 swaps the working audio driver for a generic or mismatched one.
- **Output device reset:** The update changes the default output to a disconnected HDMI or disabled device.
- **Audio service stalled:** The Windows Audio service fails to start cleanly on the new build.
- **Enhancements conflict:** Manufacturer audio enhancements (Dolby, Waves MaxxAudio) break against the new audio stack.
- **Device disabled in migration:** The update's device migration leaves the audio device disabled.
- **Exclusive mode / format mismatch:** Sample rate and exclusive-mode settings that the new driver rejects.
- **Third-party audio software:** Old Nahimic, Sonic Studio, or similar utilities crashing the audio pipeline.
- **BIOS audio settings reset:** Rare, but firmware updates bundled with the OS update can reset HD Audio settings. Related driver-level audio faults are covered in the [Realtek 24H2 audio guide](/articles/how-to-fix-realtek-audio-not-working-in-windows-11-24h2/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious output routing first

1. Click the speaker icon and confirm the correct output device is selected (Speakers, not a disconnected HDMI monitor).
2. Turn the volume up and check the mixer (**right-click speaker → Open volume mixer**) for muted apps.
3. **Settings → System → Sound**: verify the output device and run the **Test** tone.
4. Check for a physical mute key or function-key toggle on the laptop — updates do not press them, but users do mid-update.
5. Five minutes here resolves the embarrassing cases before you touch any driver.

### Fix 2: Restart the Windows audio services

1. Press **Win + R**, type `services.msc`, and find **Windows Audio** and **Windows Audio Endpoint Builder**.
2. Restart both services; set their startup type to **Automatic** if changed.
3. Test sound immediately — a stalled audio service is the quickest genuine fix.
4. If they will not stay running, note any error — that points at the driver layer below.
5. Also restart any manufacturer audio service (e.g., Waves, Dolby) listed nearby.

### Fix 3: Re-enable the audio device

1. Open **Device Manager → Sound, video and game controllers** and look for disabled (down-arrow) audio devices.
2. Right-click → **Enable device** on anything disabled.
3. Check **Audio inputs and outputs** too — microphones and speakers list separately.
4. Test sound after each enable; the update sometimes disables rather than breaks.
5. If the device is missing entirely rather than disabled, continue to the driver fixes.

### Fix 4: Roll back or reinstall the audio driver

1. **Device Manager → audio device → Properties → Driver**: use **Roll Back Driver** if available, then reboot and test.
2. If rollback is unavailable, uninstall the device (check **remove driver**), reboot, and let Windows reinstall.
3. Test with the stock driver before installing anything else — it establishes the baseline.
4. If stock works but lacks features, you know the hardware and stack are fine; the manufacturer's driver adds the polish.
5. Driver state is the cause in most post-update audio failures — this step resolves them.

### Fix 5: Install the manufacturer's audio driver

1. Download the audio driver for your exact model from the laptop maker's support site.
2. Uninstall the current audio driver fully (remove driver software), reboot.
3. Install the manufacturer's package, reboot again, and test speakers, headphones, and microphone.
4. Reinstall the bundled enhancement software (Dolby/Waves) only from the maker's package — not from third-party sites.
5. The maker's driver includes the hardware-specific tuning that generic drivers lack; for persistent crashes, the [audio crash diagnostics](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) go deeper.

### Fix 6: Disable enhancements and exclusive mode

1. **Settings → System → Sound → your output → Advanced**: turn off **Audio enhancements**.
2. In the classic **Sound control panel → Playback → Properties → Advanced**, uncheck **exclusive mode** options.
3. Set the default format to **24-bit, 48000 Hz** — the most compatible setting.
4. Test after each change; enhancements breaking against the new stack is extremely common after 24H2.
5. Re-enable enhancements one at a time later if you miss them — find the specific offender.

### Fix 7: Remove conflicting audio utilities

1. Uninstall old Nahimic, Sonic Studio, or third-party equalizer apps via **Settings → Apps**.
2. Reboot and test with the plain manufacturer driver.
3. These utilities hook the audio pipeline at a low level and break across build upgrades regularly.
4. Reinstall only current versions from the laptop maker if you need their features.
5. Test thoroughly — utility conflicts can be intermittent, so give it a day of normal use.

### Fix 8: Block future driver replacement and verify hardware

1. With audio working, use the show/hide updates troubleshooter to hide audio driver offerings from Windows Update.
2. Test speakers, wired headphones, Bluetooth audio, and the microphone — confirm every path.
3. Boot a Linux live USB as a hardware check: no sound there either means a hardware fault, not a driver issue.
4. Check the BIOS for HD Audio settings if a bundled firmware update ran alongside 24H2.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the sound troubleshooter for anything this sequence missed.

## Closing

Audio dying after 24H2 is a stack problem with a short stack: output routing, audio services, the device state, and the driver — in that order. Check the obvious first, restart the services, re-enable the device, then work the driver from rollback to manufacturer package, and strip the enhancements and utilities that break against the new build. Then lock in the fix by hiding the audio driver from Windows Update's well-meaning replacements. Sound is one of those things you only notice when it is gone; ten minutes of ordered troubleshooting brings it back, and a minute of driver hiding keeps it back.
