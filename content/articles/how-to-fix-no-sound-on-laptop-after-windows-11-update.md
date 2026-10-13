---
title: "No Sound on Your Laptop After a Windows 11 Update? 7 Fixes That Work"
slug: how-to-fix-no-sound-on-laptop-after-windows-11-update
date: 2026-10-06
categories: ["drivers"]
tags: ["no sound", "audio", "windows 11", "update", "realtek"]
description: "Lost all sound after a Windows 11 update? 7 fixes to restore laptop audio — driver rollbacks, audio service restarts, and default device checks."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-after-windows-11-update.webp"
faqs:
  - q: "Why does a Windows 11 update break my laptop's sound?"
    a: "Updates frequently replace your manufacturer's tuned audio driver with a newer generic one that doesn't match your laptop's speaker hardware. Updates can also reset the default playback device, disable the audio service, or change privacy settings so apps can't access the microphone and speakers. The hardware is almost never damaged — it's a software configuration the update disturbed."
  - q: "Should I uninstall the Windows 11 update to get sound back?"
    a: "Only as a last resort. In the vast majority of cases, rolling back just the audio driver or restarting the audio services restores sound without touching the update. Uninstalling a security update leaves your laptop exposed, so treat it as the final option after every driver and settings fix has failed — and usually you won't need it."
  - q: "Why does Device Manager say my audio device is working but there's no sound?"
    a: "Device Manager only reports whether the driver loaded, not whether audio actually flows. The update may have switched the default output to a disconnected HDMI monitor, muted the device at the system level, or broken the link between the driver and the Windows audio service. Check the default playback device and the volume mixer before assuming the driver is the problem."
  - q: "How do I stop Windows Update from breaking my audio again?"
    a: "After restoring sound, use Microsoft's 'Show or hide updates' troubleshooter to block the specific audio driver update that caused the problem. You can also pause driver updates in Windows Update settings. Keep a copy of the working driver installer from your laptop manufacturer's site so you can reinstall it in minutes if a future update overwrites it."
---

The update finished, the laptop restarted, and now there's silence. Videos play with no audio, the speaker icon shows a red X or looks normal but produces nothing, and the troubleshooter shrugs. Sound breaking after a Windows 11 update is one of the most reported post-update problems there is — and it's almost never the speakers. The update disturbed the audio driver, the default device, or the audio service, and all three are repairable.

Start with the quick checks before the driver surgery: updates love to switch your default output to a monitor you aren't using, or mute things quietly. The seven fixes below move from those one-minute checks to the driver rollback that solves most stubborn cases. If your audio driver is crashing repeatedly rather than silent, our [audio crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) tackles that specific failure.

## Why this happens

- **The update installed a generic audio driver** — it replaced your manufacturer's tuned Realtek driver with one that doesn't drive your speakers.
- **The default playback device changed** — audio is now routing to a disconnected HDMI monitor or a disabled device.
- **The Windows Audio service failed to start** — the update left the audio service disabled or stuck, so no driver can produce sound.
- **The audio device was muted or disabled at system level** — updates occasionally disable the playback device in Sound settings.
- **Privacy settings blocked audio access** — the update reset app permissions so nothing can use the audio hardware.
- **The driver is corrupted from the update process** — an interrupted driver migration leaves files that load but can't output sound.
- **Enhancement and format settings were reset** — the update changed the sample rate or re-enabled enhancements that this driver build can't handle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the default playback device and volume

This sounds too simple, but it fixes a large share of cases. Updates frequently switch the default output to an HDMI display or a Bluetooth device that isn't connected, and Windows happily sends all audio into the void. Right-clicking the speaker icon and opening Sound settings shows you exactly where audio is going — make sure it's your laptop's speakers and that nothing is muted at the system level.

1. Right-click the speaker icon in the taskbar and choose **Sound settings**.
2. Under **Output**, make sure your laptop speakers (not an HDMI or Bluetooth device) are selected.
3. Click the device and confirm it isn't **Disabled** — enable it if it is.
4. Drag the volume slider up and click the speaker icon to unmute if it shows a mute symbol.

### Fix 2: Run the Windows audio troubleshooter

The built-in troubleshooter is smarter than its reputation suggests for post-update audio failures. It checks the audio service state, the default device, driver problems, and enhancement conflicts in sequence, and it can restart services and reset devices on its own. Let it run fully — it takes about a minute and occasionally fixes the problem outright with no further work.

1. Go to **Settings > System > Sound** and scroll to **Advanced**.
2. Click **Troubleshoot** next to **Output devices** (or search "troubleshoot" in Settings).
3. Select your speakers when asked which device to diagnose.
4. Apply any fix it recommends, then test audio before moving on.

### Fix 3: Restart the Windows audio services

The update can leave the Windows Audio service disabled or crashed, and without it running, no driver on earth will produce sound. Restarting both the Windows Audio and Windows Audio Endpoint Builder services re-establishes the pipeline between applications and the driver. While you're in the Services console, set both to **Automatic** startup so the next update can't leave them off.

1. Press **Windows + R**, type `services.msc`, and press **Enter**.
2. Double-click **Windows Audio**, set **Startup type** to **Automatic**, and click **Start** if it isn't running.
3. Do the same for **Windows Audio Endpoint Builder**.
4. Restart the laptop and test sound.

### Fix 4: Roll back the audio driver

If the update installed a new audio driver, rolling back restores the version that was producing sound yesterday. Open Device Manager, find the audio device under Sound, video and game controllers, and check the Driver tab — if Roll Back Driver is clickable, the update changed the driver and this fix is very likely to work. Our [Realtek-specific guide](/articles/realtek-audio-driver-not-working-windows-11/) covers the same technique with screenshots for Realtek hardware.

1. Open **Device Manager** and expand **Sound, video and game controllers**.
2. Right-click your audio device (usually Realtek Audio) and choose **Properties**.
3. Open the **Driver** tab and click **Roll Back Driver** if available.
4. Pick a reason, confirm, restart, and test your speakers.

### Fix 5: Reinstall the audio driver from your manufacturer

When rollback isn't available, do a clean reinstall with the driver from your laptop maker's support site — Dell, HP, Lenovo, or ASUS all publish tuned audio drivers for each model. The generic driver Windows Update installed is the problem; the manufacturer's version is the cure. Uninstall the current driver with the "delete driver software" option so Windows can't just reinstall the same broken one.

1. Download the audio driver for your exact model from your manufacturer's support site.
2. In **Device Manager**, right-click the audio device, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart the laptop — Windows will load a basic driver or none at all.
4. Run the manufacturer's installer, restart once more, and test sound.

### Fix 6: Check app volume and privacy permissions

Sometimes the system produces sound but every app is silent — the update reset per-app volumes or revoked microphone and speaker access. Open the volume mixer and check that your browser and media apps aren't muted individually. Then check **Settings > Privacy & security > Microphone** (and the app permissions for audio) to make sure the update didn't lock apps out of the audio hardware.

1. Right-click the speaker icon and open the **Volume mixer**.
2. Make sure your browser, media player, and **System sounds** aren't muted or set to zero.
3. Go to **Settings > Privacy & security** and confirm apps have audio/microphone access.
4. Test with a local media file to rule out a browser-specific issue.

### Fix 7: Block the bad driver update and check for a newer one

Once sound is back, prevent a repeat. Use Microsoft's "Show or hide updates" troubleshooter — linked from [Windows support](https://support.microsoft.com/en-us/windows) — to hide the audio driver update that broke things. Then check your manufacturer's support page for a genuinely newer driver; sometimes the real fix is a driver released after the update that resolves the incompatibility properly.

1. Download and run the **Show or hide updates** troubleshooter from Microsoft.
2. Hide the audio driver update that caused the silence.
3. Check your laptop manufacturer's support site for a newer audio driver than the one installed.
4. Install it if available, restart, and confirm sound survives a reboot.

## Closing

Post-update silence is a configuration problem, not a hardware failure: the wrong driver, the wrong default device, or a stalled audio service. The rollback or clean reinstall in Fixes 4 and 5 resolves the overwhelming majority of cases, and blocking the bad update keeps it fixed. Your speakers were fine all along — they were just waiting for Windows to talk to them properly again.
