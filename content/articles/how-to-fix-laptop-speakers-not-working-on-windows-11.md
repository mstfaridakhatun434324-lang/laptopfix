---
title: "Laptop Speakers Not Working on Windows 11? Get Sound Back"
slug: "how-to-fix-laptop-speakers-not-working-on-windows-11"
date: "2026-10-07"
categories: ["drivers"]
tags: ["laptop speakers", "no sound", "windows 11", "audio driver", "realtek"]
description: "No audio from laptop speakers on Windows 11? Follow Windows 11-specific diagnosis to restore sound, from quick settings checks to driver repair."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working-on-windows-11.webp"
faqs:
  - q: "Why is there no sound from my laptop speakers on Windows 11?"
    a: "The usual Windows 11 culprits are the wrong output device selected after an update, the 24H2 update replacing the OEM audio driver with a generic one, the Windows Audio service failing to start, or the speakers being disabled in the new Sound settings. Because Windows 11 reorganized audio settings, the fix is often in a different place than Windows 10 users expect — the steps below map the new locations."
  - q: "Where are speaker settings in Windows 11?"
    a: "Go to Settings > System > Sound. Your output device is selected at the top — click it to access volume, enhancements, and advanced properties including the classic device Properties dialog. The old Sound control panel still exists too: search for 'Change system sounds' or run mmsys.cpl. Both paths reach the same devices; the Settings app is just the new front door."
  - q: "Why does Windows 11 keep switching my audio output?"
    a: "Windows 11 aggressively switches output when devices connect or disconnect — plugging in HDMI, docking, or connecting Bluetooth can reroute audio and not switch back. The 24H2 update also resets default devices during upgrades. After any such event, recheck Settings > System > Sound and reselect your speakers. Disabling unused playback devices in mmsys.cpl reduces unwanted switching."
  - q: "Can 24H2 break previously working laptop speakers?"
    a: "Yes, through its driver servicing: 24H2 frequently replaces manufacturer audio drivers with generic versions that don't properly drive the laptop's codec, silencing the speakers. The speakers are unharmed. Reinstalling the Windows 11 OEM audio package from the manufacturer and blocking automatic driver replacement restores sound and prevents the update from breaking it again."
---

Windows 11 moved the audio settings around, made output switching more aggressive, and — with the 24H2 update — got bolder about replacing your audio drivers. The result: speakers that worked yesterday produce nothing today, and the familiar Windows 10 fix locations have shifted. This guide is built for Windows 11's actual settings layout and its specific failure modes.

As always, the fastest path is isolation: confirm the right output is selected in the new Sound settings, verify the audio services, then repair the driver with the Windows 11-specific package. Work the steps in order and you'll find the break quickly.

## Why this happens

- **Output auto-switched:** Windows 11 reroutes audio to HDMI, dock, or Bluetooth and doesn't switch back.
- **24H2 replaced the OEM audio driver:** Generic driver can't properly drive the laptop codec.
- **Windows Audio service not starting:** Service failure silences all output with a normal-looking UI.
- **Speakers disabled in settings:** Device disabled during update or by misconfiguration.
- **Enhancement and exclusive-mode conflicts:** Processing layers crashing the output chain.
- **Corrupted driver from update:** Half-updated driver leaving the device non-functional.
- **Hardware speaker failure:** Least common; isolated via headphone and live-USB tests.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Select the correct output in Windows 11 Sound settings
Open Settings > System > Sound and check the Output section at the top — select your internal speakers explicitly, not a monitor or disconnected device. Click the device name to open its properties: verify volume, and under Advanced, check the output format. Then click "More sound settings" to open the classic panel and use the Test button. Windows 11's auto-switching is the top cause of sudden silence, and this explicit selection fixes it in seconds — recheck it after every update.

### Fix 2: Check the volume mixer and app-level mutes
Click the speaker icon in the taskbar, then open the full volume mixer (Settings > System > Sound > Volume mixer). Verify the master output isn't muted and that your specific app has volume. Windows 11 remembers per-app volumes, and an app muted months ago stays muted. Also check the physical mute key (often F1/F3 with a speaker icon) — a stuck mute state at the hardware level overrides everything in software, and it is easy to overlook.

### Fix 3: Restart the audio services
Press Windows key + R, type `services.msc`, and restart "Windows Audio" and "Windows Audio Endpoint Builder," setting both to Automatic. On Windows 11 these services occasionally fail to start after updates, producing total silence with no error. If they stop again immediately, the underlying audio driver is broken — continue to the driver fix. Test sound after the restart before moving on.

### Fix 4: Install the Windows 11 OEM audio driver
Download the Windows 11 audio package for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). In Device Manager, uninstall the audio device under "Sound, video and game controllers" with driver deletion, install the package, and reboot. Then set Device Installation Settings to "No" so 24H2 doesn't swap it again. The Windows 11-specific package matters — Windows 10 drivers can misbehave under the new audio stack, producing anything from silence to intermittent cutouts. After reinstalling, play audio from two different apps to confirm the driver is stable across the system. For Realtek-specific detail, see our [Realtek Windows 11 guide](/articles/how-to-fix-realtek-audio-not-working-on-windows-11/).

### Fix 5: Disable unused devices, enhancements, and exclusive mode
In the classic Sound panel (mmsys.cpl), Playback tab: right-click and show disabled/disconnected devices, enable the speakers if disabled, and disable outputs you never use (duplicate monitors, old Bluetooth entries) to stop auto-switching. In the speakers' Properties: Enhancements tab > "Disable all enhancements"; Advanced tab > uncheck Exclusive Mode, set 24-bit 48000 Hz. These cleanups remove the processing conflicts and routing confusion behind much Windows 11 silence. If distortion rather than silence is the issue, our [crackling repair guide](/articles/how-to-fix-crackling-sound-on-laptop-step-by-step/) applies.

### Fix 6: Isolate hardware with headphones and a live USB
Plug in wired headphones — working headphones with dead speakers isolates the fault to the speaker path. Then boot a Linux live USB: speaker silence there too means hardware failure (blown speakers or disconnected cable), while sound in Linux proves Windows is at fault and a repair install will fix it. This isolation takes fifteen minutes and definitively answers the hardware question.

### Fix 7: Repair the system and run the troubleshooter
Run Settings > System > Troubleshoot > Other troubleshooters > Audio — Windows 11's troubleshooter repairs service registrations and device state. Then run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` elevated to fix system-file damage from updates. If all software is exonerated, get a repair quote for the speakers — parts are cheap, labor is the disassembly. Microsoft's official audio flow at Windows support supports warranty documentation.

## Closing
Windows 11 speaker silence is usually the OS outsmarting itself: auto-switched outputs, reorganized settings hiding the real device, or 24H2 swapping the driver. Explicitly selecting the speakers, restarting the audio services, and installing the proper Windows 11 OEM driver restores sound in nearly every case — with hardware failure a distant, testable last resort. Windows 11 rewards vigilance more than Windows 10 did: recheck the output device after every system update and every new peripheral connection, because both love to reroute your audio silently. Keep the Windows 11-specific OEM audio installer archived — 24H2's driver servicing makes the generic-driver swap a recurring event rather than a one-time accident. In the classic Sound panel, leave unused playback devices disabled to reduce the auto-switching chaos. If you use Bluetooth audio regularly, get comfortable with the quick-settings output switcher; fast manual switching beats fighting the automatic behavior. And preserve the isolation habit from this repair: headphones first, then live USB — those two tests answer the hardware question definitively every time, on this laptop and any future one. Sound problems feel mysterious until you test the layers; after that, they are just plumbing.
