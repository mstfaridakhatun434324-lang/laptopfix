---
title: "How to Fix a Microphone Not Working on a Laptop in Windows 11 24H2"
slug: how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-15
categories: ["drivers"]
tags: ["microphone not working", "mic not detected", "windows 11 24h2", "audio input fix"]
description: "Laptop microphone not working or not detected on Windows 11 24H2? Six fixes covering privacy settings, driver reinstalls, and the Intel SST audio stack."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my microphone stop working after the Windows 11 24H2 update?"
    a: "The 24H2 upgrade reinstalls the audio driver stack, and the microphone array driver or its Intel SST bus driver can come out broken, disabled, or replaced with a generic build that doesn't expose the mic. Privacy settings can also reset during major updates, silently denying apps microphone access. Because the mic worked before the update, the hardware is almost certainly fine — the fix is in drivers and settings."
  - q: "My mic shows up but the input level never moves. What's wrong?"
    a: "A detected-but-silent mic usually means the wrong device is set as default, the input volume is at zero, the mic is muted at the driver level, or an enhancement is swallowing the signal. Check Sound settings > Input: confirm the right device is selected, the volume slider is up, and the test bar moves when you speak. If the bar moves in Settings but not in your app, the app's own input selection is wrong."
  - q: "Can privacy settings really block the microphone completely?"
    a: "Yes — Windows 11's microphone privacy toggle is a hard block at the OS level. If 'Microphone access' is off, no app can capture audio, and the mic appears dead everywhere even though the driver is perfect. Major updates occasionally flip this setting. Always check Settings > Privacy & security > Microphone before touching drivers; it's a ten-second check that saves an hour of driver work."
  - q: "Should I update the BIOS for a microphone problem?"
    a: "Only if the vendor's release notes mention microphone or audio fixes for your model. The mic array connects through the audio codec and Intel SST bus, both driver-level components — BIOS is rarely involved. Exhaust the driver and settings fixes first; treat BIOS as a later step, and if the mic also fails in the vendor's pre-boot diagnostics, then it's a hardware issue regardless of BIOS version."
---

Your mic worked in yesterday's call. Today, nobody can hear you — or the microphone has vanished from the input list entirely. On Windows 11 24H2, microphone failures sit at the crossroads of three systems: the audio driver stack, Windows' privacy controls, and the app's own device selection. That means the fix could be a ten-second privacy toggle or a full driver reinstall, and diagnosing which one saves you from doing both.

Start with the fastest discriminator: open **Settings** > **System** > **Sound** > **Input** and speak. If the input volume bar moves, Windows hears you and the problem is app-level (wrong mic selected in Zoom/Teams/Discord). If the bar doesn't move, or no input device is listed at all, the problem is at the OS/driver level — which is what this guide fixes. We'll go from the instant checks to the driver surgery. If output audio is broken too, the [audio driver crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) covers the shared stack.

## Why this happens

- **Microphone privacy access got revoked.** The 24H2 update or a settings sync turned off system-wide or per-app mic access — an OS-level block that looks like dead hardware.
- **The audio driver update broke the mic array.** The new driver build doesn't properly expose the internal microphone array, or the mic's driver component failed to install.
- **The Intel SST bus driver failed.** On Intel laptops the mic array data travels over Smart Sound Technology; a broken SST driver kills mic input while leaving the codec superficially healthy.
- **The wrong input device is default.** A headset, webcam mic, or virtual device grabbed default status, and apps are listening to the wrong source.
- **The mic is muted at the driver level.** The update reset the mic's gain to zero or engaged a driver-level mute that the app can't override.
- **Enhancements or APOs swallow the signal.** Noise suppression and array-processing effects from the old driver misbehave under the new build and mute the input.
- **The mic array was disabled in Device Manager.** The update flipped the internal mic to disabled status, removing it from the input list.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone privacy settings

The ten-second check that solves a surprising number of cases.

1. Go to **Settings** > **Privacy & security** > **Microphone**.
2. Ensure **Microphone access** is **On**.
3. Scroll down and confirm **Let apps access your microphone** is **On**, and that your specific app (Teams, Zoom, Discord) is allowed.
4. Also check **Let desktop apps access your microphone** — classic Win32 apps need this separate toggle. Test the mic now.

### Fix 2: Verify the input device and levels

Make sure Windows is listening to the right mic at the right volume.

1. **Settings** > **System** > **Sound** > **Input** — select your internal microphone array as the input device.
2. Drag the **Input volume** slider up and speak — the test bar should move.
3. Click the device > **More sound settings** > **Recording** tab > double-click the mic > **Levels** tab — ensure the level is up and not muted (no red circle).
4. On the **Enhancements** tab, check **Disable all enhancements** to rule out APO interference.

### Fix 3: Re-enable and reinstall the microphone driver

Repair the driver layer for the mic specifically.

1. Device Manager > **Audio inputs and outputs** — if the internal mic shows a down arrow, right-click > **Enable device**.
2. Right-click the mic > **Uninstall device**, then restart — Windows rediscovers it.
3. Also check **Sound, video and game controllers** for the audio codec; uninstall/reinstall it the same way if the mic is still missing.
4. If the mic entry is absent entirely, click **View** > **Show hidden devices** — a grayed-out mic can be uninstalled and will reappear on reboot.

### Fix 4: Repair the Intel SST driver

The hidden bus driver behind most Intel laptop mic failures.

1. Device Manager > **System devices** > find **Intel(R) Smart Sound Technology** entries.
2. Right-click each > **Update driver** > **Search automatically for drivers**.
3. If the mic still fails, uninstall the SST entries and restart — Windows rebuilds the bus stack on boot.
4. For a definitive version, download the audio/chipset package from your vendor: [Dell Support](https://www.dell.com/support), HP's support site, or [Lenovo Support](https://support.lenovo.com/us/en/) — the SST driver ships inside it.

### Fix 5: Check app-level device selection

When Windows hears you but the app doesn't.

1. In your calling app's audio settings, explicitly select the internal mic array — don't leave it on "Default" or "Same as system."
2. In Discord/Teams, disable any "automatic input sensitivity" or AI noise removal temporarily for testing.
3. Close other apps that might hold the mic exclusively (voice assistants, recording tools).
4. In **Sound settings** > **Input** > device properties, uncheck **Allow applications to take exclusive control** if present.

### Fix 6: Run the recording troubleshooter and verify hardware

Confirm the fix and rule out hardware.

1. **Settings** > **System** > **Sound** > **Troubleshoot** > run the **Recording Audio** troubleshooter.
2. Test with the built-in **Voice Recorder** app — if it records cleanly, the OS-level mic is fixed and any remaining issue is app-specific.
3. Boot into your vendor's pre-boot diagnostics and run the microphone test — if it fails there too, the mic array hardware is faulty.
4. If the mic works in diagnostics but not Windows after all fixes, consider an in-place repair install via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) as a final resort — and confirm your working driver version with the [driver version check guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) for future reference.

## Closing

Microphone failures on 24H2 are usually one of three things: a privacy toggle the update flipped, the wrong input selected, or the Intel SST/audio driver stack needing a reinstall. Check them in that order — settings before drivers, drivers before hardware — and the mic that went silent will be picking up your voice again before the next call.
