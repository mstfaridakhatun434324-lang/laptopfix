---
title: "Realtek Audio Not Working on Your Laptop? Here's the Fix"
slug: how-do-i-fix-realtek-audio-not-working
date: 2026-10-09
categories: ["drivers"]
tags: ["realtek audio", "no sound laptop", "audio driver", "windows 11"]
description: "No sound from your laptop's Realtek audio? Work through driver, service, and settings fixes to restore speakers and headphones on Windows 11."
thumbnail: "/images/thumbs/how-do-i-fix-realtek-audio-not-working.webp"
faqs:
  - q: "Why is there no sound even though Realtek shows in Device Manager?"
    a: "The device being present only means the driver loaded, not that audio is routing correctly. The default playback device may be wrong, the Realtek Audio Service may be stopped, or Windows may be sending sound to a disabled HDMI output. Check the sound output selector first, then verify the Windows Audio services are running before assuming the driver is broken."
  - q: "Should I install the Realtek driver from my laptop maker or Realtek directly?"
    a: "Start with your laptop maker's driver package. It includes the correct codec configuration and the Realtek Audio Console tuning for your exact speaker hardware. Generic Realtek reference drivers sometimes work but can disable features like Waves MaxxAudio or Nahimic enhancements. Only try the reference driver if the maker's package fails repeatedly."
  - q: "Can a Windows update break Realtek audio?"
    a: "Yes, this is one of the most common triggers. Feature updates frequently replace the manufacturer's audio driver with a generic High Definition Audio driver that lacks the correct pin configuration for your speakers. The fix is usually to reinstall the maker's driver and then tell Windows not to include drivers with future updates."
  - q: "What does error code 10 on Realtek audio mean?"
    a: "Code 10 means the device failed to start, usually because the installed driver doesn't match the hardware or its files are corrupted. Uninstall the device with the driver software removed, reboot, and install a fresh driver from the laptop maker. If the error persists across clean driver installs, the audio codec chip itself may have failed."
---

Realtek audio powers the speakers, headphone jack, and microphone on the vast majority of Windows laptops, which is why a Realtek failure feels like the whole laptop went silent. The good news: in the overwhelming majority of cases the codec chip is fine and the problem is a driver mismatch, a stopped audio service, or a misrouted output. This guide walks you through the fixes in the order a repair bench would use.

A useful first distinction is whether the failure is total or partial. If system sounds, browser audio, and headphones are all dead, you are looking at a driver or service problem. If only one application is silent, the issue is almost certainly in that app's output settings or Windows' per-app volume mixer. Pin that down before you start reinstalling drivers. For the sibling problem of distorted playback, see our guide on [crackling sound on a laptop](/articles/how-to-fix-crackling-sound-on-laptop-after-windows-11-update/).

## Why this happens

- **Windows Update swapped the driver:** A generic High Definition Audio driver replaced the maker's Realtek package, and the speaker pin mapping no longer matches.
- **Windows Audio services stopped:** The Windows Audio and Windows Audio Endpoint Builder services can fail to start, killing all sound system-wide.
- **Wrong default playback device:** Sound routes to a disconnected HDMI monitor, a disabled Bluetooth headset, or a phantom device instead of the speakers.
- **Realtek Audio Console misconfiguration:** The app can apply a broken EQ profile, enable a feature the hardware doesn't support, or mute outputs.
- **Corrupted driver files:** An interrupted update or disk error leaves the driver package half-installed, producing Code 10 or Code 39 in Device Manager.
- **Exclusive mode conflicts:** An app grabbed the audio device in exclusive mode, blocking everything else from producing sound.
- **BIOS audio toggle disabled:** Rare, but some BIOS setups include an onboard audio switch that updates can reset.
- **Codec hardware failure:** The Realtek chip or its supporting circuitry failed — uncommon, but it happens after liquid damage or power surges.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the correct output device and volume mixer

Right-click the speaker icon in the taskbar and open Sound settings. Under Output, make sure "Speakers (Realtek(R) Audio)" is selected, not an HDMI or Bluetooth device. Click the volume mixer and confirm no app is muted. Then run the built-in audio troubleshooter from the same page — it checks the default device, driver state, and services in one pass and fixes simple routing mistakes automatically.

1. Right-click the taskbar speaker icon and choose Sound settings.
2. Under Output, select Speakers (Realtek(R) Audio).
3. Open the volume mixer and unmute any silenced apps.
4. Click Troubleshoot next to the output device and apply its fixes.
5. Play a test sound to confirm routing is correct.

### Fix 2: Restart the Windows Audio services

Press Win + R, type `services.msc`, and find "Windows Audio" and "Windows Audio Endpoint Builder." Both must be Running with Startup type Automatic. If either is stopped, start it; if they are running but sound is still dead, restart both in order — Endpoint Builder first, then Windows Audio. This clears stuck audio sessions without touching any drivers. Also check "Remote Procedure Call (RPC)," which Windows Audio depends on.

1. Open Services with Win + R and `services.msc`.
2. Find Windows Audio Endpoint Builder and start or restart it.
3. Find Windows Audio and start or restart it.
4. Set both Startup types to Automatic.
5. Confirm Remote Procedure Call (RPC) is running.

### Fix 3: Reinstall the manufacturer's Realtek driver

Download the audio driver for your exact model from the laptop maker — [Lenovo's support site](https://support.lenovo.com/us/en/) carries per-model Realtek packages, as do Dell and HP. In Device Manager, under "Sound, video and game controllers," right-click Realtek(R) Audio, choose Uninstall device, and tick "Attempt to remove the driver for this device." Reboot, install the downloaded package, and reboot again. Skipping the removal step is the most common reason this fix fails.

1. Download the Realtek audio driver for your exact laptop model.
2. In Device Manager, right-click Realtek(R) Audio under Sound controllers.
3. Choose Uninstall device and tick the remove-driver checkbox.
4. Restart the laptop.
5. Install the downloaded driver package and restart once more.

### Fix 4: Check Device Manager error codes and hidden devices

If the driver reinstall didn't help, look closer at what Device Manager reports. Double-click the Realtek entry and read the Device status. Code 10 or Code 39 means driver corruption — try the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a newer signed driver if the maker's package fails. Enable View, Show hidden devices, and remove any grayed-out duplicate Realtek entries that could be confusing the audio stack.

1. Double-click the Realtek entry and read the Device status code.
2. Note Code 10, 39, or 45 for targeted troubleshooting.
3. Enable View, Show hidden devices in Device Manager.
4. Uninstall grayed-out duplicate Realtek devices.
5. Scan for hardware changes and retest.

### Fix 5: Reset the Realtek Audio Console and disable enhancements

Open the Realtek Audio Console app (install it from the Microsoft Store if missing). Reset any custom EQ to flat, turn off all sound effects, and switch speaker configuration back to Stereo if it was changed. Then go to Sound settings, the device properties for the speakers, and under Advanced, uncheck "Enable audio enhancements." Enhancements and broken console profiles are a frequent cause of silence after driver updates. If the microphone is the actual casualty, see [Realtek microphone troubleshooting](/articles/how-to-fix-realtek-microphone-not-working-in-windows-11-24h2/).

1. Open the Realtek Audio Console app.
2. Reset EQ and effects to defaults or Off.
3. In Sound settings, open the Speakers device properties.
4. Under Advanced, uncheck Enable audio enhancements.
5. Disable "Allow applications to take exclusive control" while testing.

### Fix 6: Stop Windows from replacing the working driver

Once audio works, protect it. Windows Update's habit of pushing generic audio drivers is the top cause of repeat failures — the same pattern behind [crashing audio drivers after updates](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update). Use Group Policy (Windows 11 Pro) or the registry to exclude drivers from Windows Update, or use the "Show or hide updates" troubleshooter to hide the specific audio driver update. [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) document the current steps for managing optional driver updates.

1. Press Win + R, type `gpedit.msc`, and press Enter.
2. Navigate to Windows Update, Manage updates offered from Windows Update.
3. Enable "Do not include drivers with Windows Updates."
4. On Home edition, pause updates for a week after fixing audio.
5. Reinstall the maker's driver manually after any major feature update.

### Fix 7: Rule out hardware failure

Plug in wired headphones — if they work but the speakers don't, the speaker hardware or its cable is suspect. If nothing produces sound across a clean driver install, boot into the BIOS or a Linux live USB: if there's no beep or test tone even there, the codec chip or amplifier circuit has likely failed. Also inspect for past liquid spills near the keyboard, a common killer of audio codecs. At that stage, a repair shop quote is the honest next step — no driver trick will revive dead silicon.

1. Test wired headphones in the 3.5mm jack.
2. Check whether BIOS beeps or a live USB produces any sound.
3. Look for liquid damage around the keyboard and palm rest.
4. Try an external USB sound card as a workaround.
5. Get a repair quote if the codec itself is dead.

## Closing

Realtek silence is almost always a software problem — wrong driver, wrong output, or a stopped service — and this sequence resolves it in the vast majority of cases. Keep the working driver installer saved somewhere accessible, exclude audio drivers from automatic updates, and you will rarely see this problem twice. When every software fix fails and even a live USB stays silent, you have done your due diligence and it is time for hardware service.
