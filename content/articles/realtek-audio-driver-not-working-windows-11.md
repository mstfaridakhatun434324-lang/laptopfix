---
title: "Realtek Audio Driver Not Working in Windows 11: Fix Guide"
slug: realtek-audio-driver-not-working-windows-11
date: 2026-09-20
categories: ["drivers"]
tags: ["realtek audio", "audio driver", "no sound", "windows 11", "sound fix"]
description: "No sound from your Realtek audio on Windows 11? Fix the driver with clean reinstalls, service restarts, and enhancement conflicts — 7 steps."
thumbnail: "/images/thumbs/realtek-audio-driver-not-working-windows-11.webp"
faqs:
  - q: "Why is there no sound after updating the Realtek driver?"
    a: "New Realtek driver builds sometimes mismatch your laptop's audio codec customization or conflict with enhancement software like Waves MaxxAudio or DTS. Roll back to the manufacturer's driver version in Device Manager, or download the exact build from your laptop maker's support page rather than using the generic Realtek release."
  - q: "Should I use the Realtek driver from Windows Update or my laptop maker?"
    a: "Your laptop maker's version, almost always. Manufacturers customize Realtek drivers for their specific codec, speakers, and enhancement software. Generic Realtek or Windows Update builds may install but produce no sound, missing enhancements, or broken microphone input on customized hardware — so stick with the build tested for your model."
  - q: "Why does the troubleshooter say no audio device is installed?"
    a: "That means Windows can't see the audio hardware at all — the driver failed to load or the device is disabled. Check Device Manager under Sound, video and game controllers for a yellow warning or a missing Realtek entry, then reinstall the manufacturer's driver package."
  - q: "Can I just use the generic High Definition Audio driver?"
    a: "As a diagnostic step, yes — the Microsoft generic driver confirms the hardware works. But it lacks your laptop's speaker tuning, microphone array support, and jack detection. Use it to prove the hardware is fine, then install the proper manufacturer driver for full functionality."
---

No sound, crackling audio, a microphone that stopped working, or the dreaded "no audio output device is installed" — Realtek audio problems on Windows 11 are almost always driver problems, and specifically driver-identity problems. Laptop makers customize Realtek's drivers for their exact codec chip, speaker tuning, and bundled enhancement software (Waves MaxxAudio, DTS, Dolby). When Windows Update swaps in a generic build, or an enhancement app conflicts with the driver, sound breaks in ways that look like hardware failure but aren't.

The fix sequence below respects that reality: it starts with the manufacturer's driver (not the generic one), clears enhancement conflicts, and uses the generic Microsoft driver only as a diagnostic stepping stone.

## Why this happens

- **Generic driver replaced the manufacturer's customized build.** Windows Update's favorite way to break laptop audio.
- **Enhancement software conflicts.** Waves MaxxAudio, DTS, or Dolby apps fighting the driver after updates.
- **Corrupted driver installation.** Partial updates leaving the audio stack half-migrated.
- **Disabled audio device or service.** The device disabled in Device Manager/Sound settings, or the Windows Audio service stopped.
- **Wrong default device.** Updates resetting the output to a disconnected HDMI or Bluetooth device.
- **Front-panel jack detection bugs.** Driver misreading headphone jack state, muting speakers permanently.
- **Actual codec hardware failure.** Rare — but the generic-driver test in Fix 5 settles it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the basics and the default device

Don't skip the two-minute checks.

1. Right-click the **speaker icon** in the taskbar → **Sound settings** → verify the correct **Output** device is selected (not a disconnected monitor or old Bluetooth device).
2. Check the volume mixer for the specific app — Windows 11 has per-app volumes that updates sometimes zero out.
3. Run the audio troubleshooter: **Settings > System > Sound > Troubleshoot** common sound problems.
4. Check **Device Manager > Sound, video and game controllers** — a yellow warning on Realtek means driver trouble (Fix 3); a missing entry means it's disabled or failed (Fix 2).
5. Unplug all USB/Dock audio devices and test the built-in speakers alone — docks and USB headsets hijack the default device constantly.

### Fix 2: Re-enable the device and restart audio services

The silent-disable problem.

1. **Device Manager** → **Sound, video and game controllers** → if Realtek shows a down-arrow, right-click → **Enable device**.
2. `services.msc` → **Windows Audio** and **Windows Audio Endpoint Builder** → Running, Automatic. Restart both.
3. **Settings > System > Sound > More sound settings** → Playback tab → right-click empty space → **Show Disabled Devices** → enable your speakers if disabled.
4. Set the correct device as **Default** (and Default Communication Device for calls).
5. Test with the built-in **Test** button in the device properties.

### Fix 3: Install the manufacturer's Realtek driver

The core fix — the right driver, not just a newer one.

1. Find your exact model on the laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Download their **Audio** driver package — this is the customized Realtek build with the right codec support.
3. **Device Manager** → uninstall the current Realtek device (check "delete driver software").
4. Install the manufacturer's package and restart.
5. If Windows Update immediately replaces it, pause driver updates or block that specific driver update until the maker catches up.

The 24H2-specific audio guide: [how to fix Realtek audio not working in Windows 11 24H2](/articles/how-to-fix-realtek-audio-not-working-in-windows-11-24h2/).

### Fix 4: Resolve enhancement software conflicts

Waves, DTS, and Dolby vs. the driver.

1. Open your enhancement app (Waves MaxxAudioPro, DTS Sound Unbound, Dolby Access) and check for updates — outdated enhancers break with new drivers.
2. In the Realtek device **Properties > Enhancements** (or **Advanced**), try disabling all enhancements temporarily — if sound returns, the enhancer was the conflict.
3. Reinstall the enhancement app from the laptop maker's support page (not the Microsoft Store version, which may mismatch).
4. If you don't use the enhancements, leave them disabled — fewer moving parts, fewer breakages.
5. After any Realtek driver update, re-verify the enhancement app still launches — reinstall it if it silently broke.

Related: [how to fix audio driver keeps crashing in Windows 11 24H2](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/).

### Fix 5: Test with the generic Microsoft driver

Isolate hardware vs. driver.

1. **Device Manager** → Realtek device → **Update driver > Browse my computer > Let me pick** → choose **High Definition Audio Device** (the Microsoft generic).
2. Restart and test sound. If the generic driver produces sound, your hardware is fine and the Realtek driver package is the problem — return to Fix 3 with a different version.
3. If the generic driver also produces nothing, suspect deeper issues: BIOS audio settings, or hardware.
4. Check BIOS/UEFI for an audio controller toggle — ensure onboard audio is enabled.
5. Don't stay on the generic driver permanently — no speaker tuning, no mic array, no jack detection.

### Fix 6: Fix microphone-specific failures

When output works but input doesn't.

1. **Settings > Privacy & security > Microphone** → microphone access **On**, and per-app access allowed for your calling apps.
2. **Sound settings > Input** → select the correct microphone (not a disconnected headset mic).
3. In the mic's **Properties > Levels**, unmute and raise the level; in **Advanced**, uncheck "Allow applications to take exclusive control" for testing.
4. Reinstall the manufacturer's audio package (Fix 3) — mic array support lives in the customized driver, and generic builds often break it.
5. Test with Voice Recorder (built-in) to separate app-specific from system-wide mic failure.

### Fix 7: Repair system files and update

The foundation beneath the audio stack.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending Windows updates.
3. Update the BIOS/chipset from the maker's support page — audio codec initialization fixes ship in firmware.
4. If a specific update broke audio, check the Microsoft Update Catalog for a superseding fix or roll back the KB.
5. Persistent failure across manufacturer drivers, generic driver, and clean Windows = hardware; the codec or speaker path needs service.

## Closing

Realtek audio on Windows 11 breaks along one fault line: the wrong driver build for customized hardware. The manufacturer's package — not Windows Update's generic, not Realtek's reference release — is the fix in most cases, with enhancement-software conflicts as the runner-up. Work the sequence, use the generic driver as a diagnostic rather than a destination, and keep the working driver installer somewhere safe. Laptop audio is too customized for generic drivers, and every update season proves it again.
