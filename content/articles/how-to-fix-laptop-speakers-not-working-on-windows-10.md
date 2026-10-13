---
title: "Laptop Speakers Not Working on Windows 10? Restore Your Sound"
slug: "how-to-fix-laptop-speakers-not-working-on-windows-10"
date: "2026-10-03"
categories: ["drivers"]
tags: ["laptop speakers", "no sound", "windows 10", "audio driver", "realtek"]
description: "No sound from your laptop speakers on Windows 10? Learn how to tell software from hardware failure and follow proven steps to restore audio."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working-on-windows-10.webp"
faqs:
  - q: "Why do my laptop speakers suddenly have no sound on Windows 10?"
    a: "Sudden silence usually comes from a driver change (Windows Update replacing the audio driver), the wrong playback device being set as default, the audio service crashing, or the speakers being muted at a hidden level. Hardware failure is possible but less common — if sound vanished overnight without drops or trauma, software is the likely culprit and the fixes below address each cause."
  - q: "How do I know if my laptop speakers are physically broken?"
    a: "Plug in headphones: if they work perfectly, the audio system is fine and the problem is isolated to the speakers or their wiring. Boot a Linux live USB — silence there too, with working headphones, points to dead speakers. Crackling that worsens with volume, or sound from only one speaker, also suggests hardware. Total silence across all outputs is almost always software."
  - q: "Why does the speaker icon show a red X?"
    a: "The red X means Windows cannot start the audio device — usually a failed or missing audio driver, a disabled device, or a stopped Windows Audio service. Right-clicking the icon and running the troubleshooter sometimes resolves it, but the reliable fix is reinstalling the manufacturer's audio driver and confirming the audio services are running."
  - q: "Can Windows 10 updates break laptop speakers?"
    a: "They break the audio driver, which silences the speakers — the speakers themselves are unaffected. Feature updates are notorious for installing generic audio drivers that don't match the laptop's codec. Reinstalling the OEM driver from the manufacturer's support page restores sound, and blocking automatic driver replacement prevents the update from breaking it again."
---

Silence from laptop speakers is disorienting — especially when everything looks normal: volume is up, nothing is muted, and the speaker icon shows no error. On Windows 10, this "everything looks fine but no sound" scenario is overwhelmingly a software problem hiding behind a healthy-looking interface.

The diagnostic approach is simple isolation: determine whether any audio output works (headphones?), whether Windows sees the audio device (Device Manager?), and whether the failure is total or partial. Each answer eliminates whole categories of causes. The steps below follow that isolation order so you fix the actual break instead of reinstalling drivers for a muted app.

## Why this happens

- **Wrong default playback device:** Sound routes to a monitor, Bluetooth device, or disabled output instead of the speakers.
- **Generic audio driver from Windows Update:** Replaces the tuned OEM driver with one that can't drive the codec properly.
- **Windows Audio service stopped:** The background service crashes or fails to start, silencing everything.
- **Speakers disabled in Sound settings:** The device gets disabled and vanishes from the output list.
- **Corrupted audio driver:** Failed updates leave the driver in a non-functional state.
- **Muted at the app or mixer level:** Per-app volume sliders or the mixer mute the output invisibly.
- **Failed speaker hardware:** Blown speakers or a disconnected internal cable, least common but real.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Verify output routing and the volume mixer
Right-click the speaker icon, open Sound settings, and confirm the output device is "Speakers" (your Realtek/internal device) — not a monitor or disconnected Bluetooth device. Then right-click the speaker icon, open the Volume Mixer, and check that neither the master nor your app is muted or at zero. Test with the "Test" button in the classic Sound panel. Misrouted output is the most common cause of "no sound" and takes ten seconds to rule out — always start here before touching drivers.

### Fix 2: Run the built-in audio troubleshooter
Right-click the speaker icon and choose "Troubleshoot sound problems," or go to Settings > Update & Security > Troubleshoot. The troubleshooter checks the audio service, device state, and default device, and it actually fixes simple misconfigurations automatically. If it reports it couldn't fix the problem, note what it found — that information directs the deeper steps. It's a quick, non-destructive first pass worth the two minutes.

### Fix 3: Restart the Windows Audio services
Press Windows key + R, type `services.msc`, and restart "Windows Audio" and "Windows Audio Endpoint Builder" (set both to Automatic). If they won't stay running, the audio driver beneath them is likely broken — proceed to the driver fix. Services that crash on start produce total silence with a healthy-looking interface, which matches the classic symptom exactly. After restarting, play a test sound before moving on.

### Fix 4: Reinstall the manufacturer's audio driver
Download the audio driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). In Device Manager, uninstall the device under "Sound, video and game controllers" with driver deletion, install the downloaded package, and reboot. Then set Device Installation Settings to "No" so Windows Update can't replace it. This resolves the large share of cases caused by generic-driver swaps, and it also restores any manufacturer-specific audio control panels that the generic driver removed. Our [Realtek repair guide](/articles/how-to-fix-realtek-audio-not-working-on-windows-10/) covers driver details.

### Fix 5: Check for disabled devices and enhancement conflicts
In the classic Sound panel's Playback tab, right-click empty space and tick "Show Disabled Devices" and "Show Disconnected Devices." If your speakers appear disabled, right-click and enable them. Then open the speakers' Properties: on Enhancements, tick "Disable all enhancements," and on Advanced, uncheck Exclusive Mode boxes. Enhancement layers and exclusive-mode grabs are frequent silent-sound culprits. If crackling accompanies the problem rather than silence, see our [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop-step-by-step/).

### Fix 6: Test with headphones and a live USB to isolate hardware
Plug in wired headphones: working headphone audio with silent speakers isolates the fault to the speakers or their internal path. For final confirmation, boot a Linux live USB and test the speakers there — silence in Linux with the correct driver loaded means the speakers or their cable have failed. This two-test isolation is what a repair shop does first, and it prevents wasting hours on software fixes for dead hardware.

### Fix 7: Repair system files and consider professional repair
Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt to fix OS-level audio damage. If software is fully exonerated and the speakers are dead, get a repair quote — internal speaker replacement is usually inexpensive in parts but requires disassembly. Document your isolation tests for the technician. Microsoft's audio troubleshooting at Windows support provides the official diagnostic flow for warranty claims.

## Closing
Silent laptop speakers on Windows 10 are a routing, service, or driver problem far more often than dead hardware. Confirming the output device, restarting the audio services, and reinstalling the proper OEM driver restores sound in the great majority of cases — and the headphone test tells you honestly when it's time for a repair shop instead. Keep the sound working with minimal effort: save the OEM audio driver installer alongside your other drivers, because Windows 10's feature updates remain the leading cause of sudden silence and the fix is always the same reinstall. Check the default playback device after connecting anything new — docks, monitors, and Bluetooth devices all trigger Windows' enthusiastic output switching. If the household shares the laptop, show other users the volume mixer; half of all "no sound" reports are a muted browser tab or a zeroed app slider. Periodically confirm the speakers are still enabled in the Sound panel, since updates occasionally disable devices. And maintain the headphone test as your permanent first diagnostic: working headphones with silent speakers means the audio system is healthy and the fault is isolated — that single observation will keep saving you time for the life of the machine.
