---
title: "No Sound on Your Windows 10 Laptop? Fix It Step by Step"
slug: how-to-fix-no-sound-on-laptop-on-windows-10
date: 2026-09-02
categories: ["drivers"]
tags: ["no sound", "windows 10", "audio fix", "speaker not working", "sound driver"]
description: "No sound on your Windows 10 laptop? Fix silent speakers with these Windows 10-specific steps for drivers, services, and sound settings."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-on-windows-10.webp"
faqs:
  - q: "Why is there no sound on my Windows 10 laptop?"
    a: "The most common causes on Windows 10 are a muted or wrongly selected output device, the Windows Audio service stalling, or a broken audio driver after an update. Start with the volume mixer and the Playback devices panel — a surprising number of cases are just the wrong default device. If the speaker icon shows a red X, the audio device is disabled or its driver failed."
  - q: "How do I fix no audio output device is installed on Windows 10?"
    a: "That message means Windows sees no working audio hardware. Open Device Manager → 'Sound, video and game controllers' and look for missing or flagged devices. Reinstall the audio driver from your laptop maker's support site, enable 'Show hidden devices' to find ghosted entries, and check BIOS for a disabled onboard audio option. A full power drain also helps when the codec fails to enumerate."
  - q: "Where is the sound troubleshooter in Windows 10?"
    a: "Right-click the speaker icon in the taskbar and choose 'Troubleshoot sound problems.' You can also find it at Settings → Update & Security → Troubleshoot → Additional troubleshooters → Playing Audio. The troubleshooter re-enables disabled devices, restarts audio services, and resets misconfigured endpoints automatically — always worth running before manual fixes."
  - q: "Can a Windows 10 update break laptop sound?"
    a: "Yes — Windows 10 feature updates are notorious for replacing working audio drivers with generic ones or resetting output selections. If sound died right after an update, reinstall the audio driver from your laptop maker's site and check that the correct playback device is still set as default. You can also roll back the driver in Device Manager if the option is available."
---

Windows 10 still runs on countless laptops, and its audio stack has its own personality — the classic Sound control panel, the volume mixer, and update behaviors that differ from Windows 11. When sound dies on a Windows 10 laptop, the troubleshooting path uses these Windows 10-specific tools, and knowing where they live saves real time.
The diagnostic order is the same as any audio failure: confirm the output selection, check for mutes, restart the audio services, then reinstall the driver. What makes Windows 10 special is mostly where the buttons are — and how aggressively its feature updates reshuffle audio drivers. This guide is written for Windows 10's actual interface, not generic advice. If you've moved to Windows 11, see our [Windows 11 no-sound guide](/articles/how-to-fix-no-sound-on-laptop-on-windows-11/) instead.
Before starting, note the exact symptom: red X on the speaker icon (device/driver problem), icon normal but silent (settings/routing problem), or 'no audio output device is installed' (enumeration problem). Each routes to different fixes below. For microphone-specific silence, our [Windows 10 mic guide](/articles/how-to-fix-microphone-not-working-on-laptop-on-windows-10/) covers the input side.

## Why this happens

- **Wrong default playback device.** Windows 10 keeps playing to HDMI or a disconnected USB device after it's unplugged.
- **Output muted in the mixer.** Per-app or master mutes persist silently; the icon doesn't always make it obvious.
- **Audio device disabled.** Updates disable the playback device; disabled devices are hidden in the Sound panel by default.
- **Windows Audio service stalled.** The service hangs and produces total silence until restarted.
- **Driver replaced by feature update.** Windows 10's twice-yearly updates are famous for swapping working audio drivers.
- **Corrupted driver installation.** Partial updates leave the audio stack half-installed.
- **'No audio output device' enumeration failure.** The codec fails to enumerate — driver, BIOS, or hardware level.
- **Enhancement software conflicts.** Third-party audio utilities wedge the pipeline on Windows 10's older audio stack.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the right playback device and unmute

Windows 10's Sound panel is the control center — get the routing right before suspecting drivers.

1. Right-click the speaker icon → 'Open Sound settings' → under Output, select your laptop's speakers explicitly.
2. Click 'Device properties' and confirm the device isn't disabled there.
3. Right-click the speaker icon → 'Open Volume mixer' → check that no app and no device slider is muted or at zero.
4. Open the classic panel: right-click speaker icon → Sounds → Playback tab → right-click → 'Show Disabled Devices' → enable the speakers and 'Set as Default.'
5. Click the speakers → Properties → 'Test' — if the test tone plays, routing was the whole problem.

### Fix 2: Run the Windows 10 sound troubleshooter

Windows 10's troubleshooter is genuinely competent at audio — let it do the easy wins first.

1. Right-click the speaker icon → 'Troubleshoot sound problems.'
2. If it asks which device, select your laptop's speakers.
3. Apply any fixes it recommends — it commonly re-enables devices and restarts services.
4. Alternatively: Settings → Update & Security → Troubleshoot → Additional troubleshooters → Playing Audio → Run.
5. Retest immediately; if it found nothing, continue — manual steps go deeper.

### Fix 3: Restart the audio services

Twenty seconds, no reboot — a stalled Windows Audio service is a classic Windows 10 silence cause.

1. Press Windows + R → type services.msc → Enter.
2. Right-click 'Windows Audio' → Restart.
3. Right-click 'Windows Audio Endpoint Builder' → Restart.
4. Set both Startup types to Automatic.
5. Play a test sound — YouTube or the Sounds panel test tone both work.

### Fix 4: Reinstall the audio driver (Windows 10 method)

The definitive driver fix, using Windows 10's Device Manager paths.

1. Right-click Start → Device Manager → expand 'Sound, video and game controllers.'
2. Right-click your audio device (Realtek, Conexant, IDT) → Uninstall device → check 'Delete the driver software for this device.'
3. Expand 'Audio inputs and outputs' and uninstall the speaker entries the same way.
4. Restart — Windows 10 reinstalls a base driver automatically.
5. Install the audio driver from your laptop maker's Windows 10 support page for your exact model — the OEM package restores full functionality.

### Fix 5: Fix 'No audio output device is installed'

This specific message means enumeration failed — work the hardware-software boundary.

1. Device Manager → View → 'Show hidden devices' → look for grayed-out audio devices and uninstall them.
2. Action → 'Scan for hardware changes' to force re-enumeration.
3. Restart into BIOS/UEFI and verify onboard/HD audio is Enabled.
4. Install the chipset driver from your laptop maker's site — the codec depends on it.
5. Shut down, unplug everything, hold power 30 seconds (power drain), then boot and recheck — this revives codecs that failed to enumerate.

### Fix 6: Disable enhancements and exclusive mode

Windows 10's enhancement pipeline is a frequent silence/crackle source when utilities misbehave.

1. Sounds → Playback → speakers → Properties → Enhancements tab → check 'Disable all enhancements.'
2. Advanced tab → uncheck 'Allow applications to take exclusive control of this device.'
3. Set Default Format to '16 bit, 48000 Hz (DVD Quality)' — the safest universal setting.
4. Temporarily uninstall third-party audio tools (Nahimic, MaxxAudio, equalizers) to rule them out.
5. Apply, retest, and reintroduce tools one at a time if sound returns.

### Fix 7: Handle post-update breakage and prevent repeats

Windows 10 feature updates break audio regularly — fix it now and reduce the odds next time.

1. If sound died right after an update, try Device Manager → audio device → Properties → Driver → 'Roll Back Driver' first.
2. Check the maker's site for a Windows 10-specific driver newer than what Update installed.
3. Use the 'Show or hide updates' troubleshooter to block the specific bad driver update.
4. Create a System Restore point once audio works, labeled clearly.
5. For persistent issues, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents advanced audio recovery, and our [Realtek-specific guide](/articles/realtek-audio-driver-not-working-windows-11/) covers the most common codec in depth.

## Closing

Windows 10 audio failures are almost always routing, services, or the driver Windows Update swapped in. Work the Sound panel first, restart the services, reinstall the maker's driver — and you'll have sound back without ever needing to understand why it left.
