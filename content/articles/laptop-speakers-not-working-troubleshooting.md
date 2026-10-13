---
title: "Laptop Speakers Not Working? Troubleshooting Guide That Works"
slug: "laptop-speakers-not-working-troubleshooting"
date: "2026-09-23"
categories: ["drivers"]
tags: ["laptop speakers", "no sound", "speaker fix", "windows 11"]
description: "No sound from your laptop speakers? Work through this guide — from output-device mix-ups to driver reinstalls — and get audio back without guesswork."
thumbnail: "/images/thumbs/laptop-speakers-not-working-troubleshooting.webp"
faqs:
  - q: "Why do my headphones work but laptop speakers do not?"
    a: "When headphones work, the audio system is fundamentally healthy — the problem is specific to the speaker path. The usual causes are the wrong default output device, muted speaker levels, crashed enhancement software affecting only the speaker endpoint, or failed speaker hardware. Check output selection and enhancements first."
  - q: "How do I know if my laptop speakers are blown?"
    a: "Blown speakers distort at all volumes, produce rattling or buzzing on bass, or stay silent on one side. Test with the maker's built-in audio diagnostics (available in BIOS on Dell and HP) — if diagnostics also produce no sound or distortion, the speaker hardware has failed and needs replacement."
  - q: "Can Windows updates break laptop speakers?"
    a: "Yes. Updates frequently replace the vendor audio driver with a generic version that misconfigures the speaker endpoint or breaks enhancement software. Reinstalling the audio driver from your laptop maker's support site is the standard fix for update-related speaker failures, and blocking future driver replacements keeps it fixed."
  - q: "Why is there no sound after unplugging HDMI?"
    a: "Windows often fails to switch the default output back from the HDMI device to the internal speakers when you disconnect the display. Open the taskbar quick settings and manually reselect Speakers. If it recurs, disable the HDMI audio device in the classic Sound panel when not in use."
---

No sound from laptop speakers is one of those problems with a dozen possible causes and a very short list of likely ones. In repair-shop experience, the top three are: Windows sending audio to the wrong output device, the audio driver in a broken state after an update, and audio enhancements crashing the pipeline. All three are fixable in minutes once identified.

The key diagnostic is the headphone test. Plug in wired headphones or connect a Bluetooth headset: if they produce sound, your audio system fundamentally works and the problem is specific to the speaker path — output routing, speaker drivers, or the speakers themselves. If nothing produces sound anywhere, the problem is system-wide and points at the audio driver or Windows audio services.

This guide walks the full sequence from instant checks to driver surgery. If your issue is specifically crackling rather than silence, our [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/) targets that symptom directly.

## Why this happens

- ****Wrong default output device**:** Windows routes audio to HDMI monitors, USB headsets, or Bluetooth devices and never switches back. The speakers are fine — they are just not selected.
- ****Muted or zeroed volume layers**:** Volume exists at multiple layers: the master control, per-app mixer, the device's own level, and sometimes a physical mute key. Any single layer at zero means silence.
- ****Corrupted audio driver**:** A damaged Realtek, Intel, or Conexant driver can kill speaker output while leaving the device apparently healthy in Device Manager.
- ****Audio enhancements crashing**:** Vendor DSP software (Waves, Dolby, Nahimic) can crash the audio pipeline for the speaker endpoint specifically.
- ****Windows Audio service stopped**:** If the Windows Audio service or its Endpoint Builder companion stops, all audio dies system-wide.
- ****BIOS-disabled audio**:** Some business laptops can disable the onboard audio controller in BIOS. Firmware updates occasionally reset this.
- ****Blown or disconnected speakers**:** Rare but real: a failed speaker, a pinched speaker wire from a previous repair, or liquid damage to the speaker assembly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the Output Device and Volume Layers

Click the speaker icon in the taskbar and check which output device is selected in the quick-settings panel — switch it to your laptop's Speakers explicitly. Then right-click the speaker icon, open the Volume mixer, and check the master volume plus each app's level. Press the physical mute key (often Fn+F1 or a dedicated key) to rule out a hardware mute.

Volume problems hide in layers, so check all of them: quick settings, mixer, the device's own properties level, and the physical key. This two-minute check resolves a large share of 'no sound' reports with zero technical work.

1. 1. Select Speakers explicitly in the taskbar quick-settings panel.
2. 2. Open Volume mixer and check master and per-app levels.
3. 3. Press the mute function key to rule out hardware mute.
4. 4. Check the speaker device's own level in Sound settings.
5. 5. Play a test sound after each check.

### Fix 2: Run the Audio Troubleshooter

Open Settings, System, Sound, and click Troubleshoot under the output device section — or search for 'troubleshoot audio' in Settings. The troubleshooter checks the audio service state, driver health, default device, and enhancement settings automatically, and it fixes the simple cases itself.

It will not fix driver corruption or hardware faults, but it is fast and occasionally catches things humans miss, like a disabled device or a service stuck in a stopping state. Run it before manual driver work.

1. 1. Open Settings, System, Sound.
2. 2. Click Troubleshoot next to the output device.
3. 3. Answer the troubleshooter's prompts.
4. 4. Apply any fixes it recommends.
5. 5. Retest speaker audio.

### Fix 3: Restart the Windows Audio Services

Press Windows key + R, type services.msc, and restart both Windows Audio and Windows Audio Endpoint Builder. If either service is stopped or set to Manual, set it to Automatic and start it. These two services are the foundation of all Windows audio — when they fail, nothing plays anywhere.

If the services stop again after a restart, a corrupted driver is usually crashing them — proceed to the driver reinstall. Note the failure pattern: services that die within minutes of starting point squarely at driver trouble.

1. 1. Open services.msc.
2. 2. Restart Windows Audio and Windows Audio Endpoint Builder.
3. 3. Set both to Automatic startup.
4. 4. Test speaker audio.
5. 5. If they stop again, continue to driver fixes.

### Fix 4: Reinstall the Audio Driver

In Device Manager, expand Sound, video and game controllers, right-click the audio device, and choose Uninstall device with driver deletion. Restart — Windows installs a basic driver — then install the audio driver from your laptop maker's support site. The vendor driver includes the correct codec configuration and enhancement components for your exact model.

This is the definitive fix for system-wide silence with no hardware cause. For Realtek-specific issues, our [Realtek audio driver guide](/articles/realtek-audio-driver-not-working-windows-11/) goes deeper. Microsoft documents driver reinstallation in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. In Device Manager, uninstall the audio device with driver deletion.
2. 2. Restart the laptop.
3. 3. Install the vendor audio driver from the maker's site.
4. 4. Restart again if prompted.
5. 5. Test speakers, then headphones, then both.

### Fix 5: Disable Audio Enhancements

Right-click the speaker icon, open Sound settings, select Speakers, and turn off audio enhancements. In the classic Sound panel, open the Speakers properties and uncheck everything on the Enhancements tab. Then disable or uninstall vendor audio apps (Waves MaxxAudio, Dolby, Nahimic) temporarily as a test.

Enhancement DSP runs in the audio pipeline, and when it crashes it takes the speaker endpoint down with it — often while headphones keep working, since they may use a different processing path. If sound returns with enhancements off, reinstall the matched vendor driver-plus-app package.

1. 1. Turn off audio enhancements for the Speakers device.
2. 2. Uncheck all options on the Enhancements tab.
3. 3. Disable vendor audio apps temporarily.
4. 4. Test speaker audio.
5. 5. Reinstall the matched vendor package if this was the cause.

### Fix 6: Check BIOS and Physical Causes

Restart into the BIOS/UEFI setup and verify the onboard audio controller is enabled — usually under Advanced or Integrated Peripherals. While investigating, consider the physical history: did sound die after a drop, a spill, or a repair? Liquid damage and pinched speaker wires from bottom-panel removals are the real-world hardware causes.

Test the speakers in the BIOS diagnostics if your maker offers audio tests there (Dell and HP both include them) — sound in diagnostics with silence in Windows proves a software problem definitively.

1. 1. Enter BIOS/UEFI and confirm onboard audio is enabled.
2. 2. Run the maker's built-in audio diagnostics if available.
3. 3. Recall any drops, spills, or recent repairs.
4. 4. Sound in diagnostics but not Windows means software fault.
5. 5. No sound anywhere means speaker hardware failure — arrange repair.

## Closing

Speaker silence is a routing problem until proven otherwise: check the output device, the volume layers, and the audio services before you touch drivers. The driver reinstall is the heavy fix that resolves the stubborn cases, and the BIOS diagnostics test gives you a definitive software-versus-hardware verdict when you need one.
