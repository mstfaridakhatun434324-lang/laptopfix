---
title: "Realtek Audio Not Working on ASUS Laptop: Complete Fix Guide"
slug: "how-to-fix-realtek-audio-not-working-on-asus-laptop"
date: 2026-10-12
categories: ["drivers"]
tags: ["realtek audio", "asus laptop", "no sound", "audio driver", "speakers not working"]
description: "No sound from your ASUS laptop speakers or headphone jack? This guide fixes Realtek audio driver failures with clean reinstalls, service checks, and ASUS-specific driver sources."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why does Realtek audio disappear after a Windows 11 update on ASUS laptops?"
    a: "Windows Update sometimes replaces the ASUS-customized Realtek driver with a generic Microsoft HD Audio driver that does not match the laptop's audio hardware configuration. The generic driver may install without error yet produce no sound, or the Realtek device may vanish from Device Manager entirely. Reinstalling the Realtek driver package from the ASUS support page for your exact model restores the correct hardware-specific configuration."
  - q: "Should I use the Realtek driver from ASUS or the generic one from Realtek?"
    a: "Use the ASUS version. ASUS customizes the Realtek driver with the correct codec settings, speaker tuning, and jack-detection behavior for each model. The generic Realtek reference driver can work but often breaks the headphone jack auto-switching or the built-in microphone array. Only try the generic driver as a last resort when the ASUS package repeatedly fails to install."
  - q: "My speakers work but the headphone jack does not. Is that a driver issue?"
    a: "Very often, yes. The headphone jack relies on jack-detection logic inside the Realtek driver and the Realtek Audio Console app. If the driver is generic or the console app is missing, plugging in headphones does nothing. Reinstall the full ASUS Realtek package including the Audio Console, and check the console's device advanced settings for the jack-detection and playback device options."
  - q: "What does the red X on the speaker icon mean?"
    a: "The red X means Windows cannot start any audio output device. Common causes are a disabled audio device, a crashed Windows Audio service, or a driver that failed to load after an update. Right-click the icon and run the troubleshooter first, then check Device Manager for the Realtek device status, and restart the Windows Audio and Windows Audio Endpoint Builder services."
---

Realtek audio chips power the speakers, headphone jack, and microphones on nearly every ASUS laptop, which makes a Realtek driver failure feel like the whole machine went mute. One day the speakers work, the next there is a red X on the volume icon, or sound plays from the wrong device, or the headphone jack stops responding when you plug in. The hardware is almost never dead; the driver stack just needs repair.

ASUS laptops are picky about audio drivers because ASUS customizes the Realtek package for each model's speaker tuning and jack behavior. That is why generic driver updaters and Windows Update's automatic driver so often make things worse instead of better. The fix that works reliably is a clean install of the ASUS-specific Realtek driver for your exact model number.

This guide covers the full sequence: quick Windows checks, service restarts, and the proper clean reinstall that resolves the stubborn cases. If your audio trouble extends to [crashing audio drivers](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/) or [microphone problems](/articles/how-to-fix-realtek-microphone-not-working-in-windows-11-24h2/), those guides pick up where this one leaves off.

## Why this happens

- **Windows Update replaced the ASUS driver:** a generic Microsoft HD Audio driver gets installed over the customized ASUS Realtek package and mismatches the hardware.
- **Corrupted driver installation:** an interrupted update or failed install leaves the Realtek driver in a half-installed state that produces no sound.
- **Audio services stopped:** the Windows Audio and Windows Audio Endpoint Builder services must both run; if either stops, all audio dies.
- **Wrong default playback device:** Windows may route sound to a disconnected HDMI monitor or Bluetooth device instead of the speakers.
- **Disabled audio device:** the Realtek device can end up disabled in Device Manager or in the Sound control panel after updates.
- **Realtek Audio Console missing:** the UWP console app handles jack detection and enhancements; without it, headphones and mic switching misbehave.
- **Fast Startup driver conflict:** Fast Startup can reload a stale driver state on boot, causing audio to fail until a full restart.
- **BIOS audio setting changed:** rare, but a BIOS reset can disable the onboard HD audio controller entirely.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows audio troubleshooter first

The built-in troubleshooter is genuinely useful for audio because it checks services, default devices, and driver state in one pass. It resolves simple misconfigurations in a couple of minutes.

1. Right-click the speaker icon in the taskbar and choose Troubleshoot sound problems.
2. Select the Realtek speakers when asked which device to diagnose.
3. Apply every fix the troubleshooter suggests and let it finish.
4. Test with a YouTube video or system sound after it completes.
5. If it reports it could not fix the issue, continue with the steps below.

### Fix 2: Verify the correct playback device is default

Windows sometimes silently switches output to an HDMI display or a long-forgotten Bluetooth headset. Confirming the Speakers (Realtek) device is default takes seconds and fixes a surprising number of no-sound complaints.

1. Right-click the speaker icon and open Sound settings.
2. Under Output, select Speakers (Realtek Audio) from the device list.
3. Click the arrow next to it and confirm the volume slider is up and not muted.
4. Scroll to Advanced and run a test tone from the device properties.
5. Disable unused output devices like HDMI audio to prevent future switching.

### Fix 3: Restart the Windows audio services

Both audio services must be running for any sound to work. Restarting them clears hung states without touching drivers, and setting them to Automatic prevents recurrence after reboots.

1. Press Windows + R, type services.msc, and press Enter.
2. Find Windows Audio, right-click it, and choose Restart.
3. Find Windows Audio Endpoint Builder and restart it the same way.
4. Double-click each service and set Startup type to Automatic.
5. Play a test sound to confirm audio is back.

### Fix 4: Re-enable the Realtek device in Device Manager

Updates can leave the Realtek controller disabled, which Device Manager shows with a small down arrow. Re-enabling is instant and often the entire fix when the device is present but silent.

1. Press Windows + X and open Device Manager.
2. Expand Sound, video and game controllers.
3. If Realtek Audio shows a down arrow, right-click it and choose Enable device.
4. Also expand System devices and check the Realtek or Intel Smart Sound entry the same way.
5. Restart the laptop and test the speakers and headphone jack.

### Fix 5: Clean-reinstall the ASUS Realtek driver

This is the definitive fix for most ASUS Realtek failures. Remove the current driver completely, including the driver software, then install the ASUS-customized package for your exact model so jack detection and speaker tuning work as designed.

1. In Device Manager, right-click Realtek Audio and choose Uninstall device.
2. Check the box for Attempt to remove the driver for this device, then confirm.
3. Restart the laptop. Do not let Windows install its generic driver yet.
4. Download the Audio driver from the ASUS support page for your exact model number.
5. Run the installer, restart again, and verify sound plus headphone jack switching.

### Fix 6: Install the Realtek Audio Console and check enhancements

The Realtek Audio Console from the Microsoft Store controls jack detection, and the legacy enhancements tab can conflict with the new driver. Getting both right finishes the repair.

1. Open the Microsoft Store and install Realtek Audio Console if it is missing.
2. Open the console and check Device advanced settings for jack-detection options.
3. In Sound settings, open the Realtek device properties and the Enhancements tab.
4. Disable all enhancements temporarily to rule out processing glitches.
5. Test speakers, wired headphones, and the built-in microphone array.

### Fix 7: Disable Fast Startup and check for BIOS updates

Fast Startup's hybrid shutdown can preserve a broken driver state across boots, which is why audio sometimes fails on startup but works after a restart. A BIOS update from ASUS can also fix low-level audio controller issues.

1. Open Control Panel, go to Power Options, and click Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Uncheck Turn on fast startup and save changes.
4. Check the ASUS support page for a BIOS update mentioning audio fixes.
5. For background reading, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents audio troubleshooting steps officially.

## Closing

Realtek audio on ASUS laptops fails in software far more often than in hardware. The pattern to remember is simple: check the output device, restart the services, then clean-install the ASUS-specific driver. Do those three in order and the speakers come back in nearly every case.
