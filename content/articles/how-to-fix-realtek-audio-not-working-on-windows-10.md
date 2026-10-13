---
title: "How to Fix Realtek Audio Not Working on Windows 10"
slug: how-to-fix-realtek-audio-not-working-on-windows-10
date: 2026-10-07
categories: ["drivers"]
tags: ["realtek audio not working", "windows 10", "realtek driver", "no sound", "audio driver"]
description: "Realtek audio not working on Windows 10? Restore sound with 7 proven fixes — driver reinstalls, service restarts, and settings repairs."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-on-windows-10.webp"
faqs:
  - q: "Why is there no sound from Realtek audio on Windows 10?"
    a: "The most common causes are a corrupt Realtek driver after a Windows update, the Windows Audio service stopped, the wrong playback device set as default, or the Realtek device disabled in Device Manager. Start with the volume mixer and default device checks — they take a minute — then reinstall the Realtek driver from your laptop maker's site, which fixes the majority of no-sound cases."
  - q: "Should I download the Realtek driver from Realtek or my laptop maker?"
    a: "From your laptop maker, always. Realtek's generic driver lacks the customizations for your laptop's speaker tuning, jack detection, and microphone array — installing it can actually break things that worked. Your manufacturer's support site hosts the Realtek package validated for your exact model's audio codec and speaker configuration."
  - q: "What does reinstalling the Realtek driver actually fix?"
    a: "A clean reinstall replaces corrupt driver files, rebuilds the driver's registry configuration, restarts its detection services, and clears stale audio endpoint data that confuses Windows' sound stack. It resolves no-sound, crackling, missing enhancements, and jack-detection failures in one pass — which is why technicians reach for it early rather than as a last resort."
  - q: "Why does my Realtek audio break after every Windows update?"
    a: "Windows Update periodically replaces your manufacturer's Realtek driver with its own generic build, which lacks the custom tuning and sometimes breaks entirely on certain codecs. After reinstalling the maker's driver, use the Show or hide updates troubleshooter to block the audio driver update, so Windows stops downgrading it after each feature update."
---

No sound at all is the bluntest audio failure: no system sounds, no music, no video audio. On Windows 10 laptops, Realtek provides the audio codec on the overwhelming majority of machines, so "Realtek audio not working" and "no sound" are usually the same problem. The causes cluster tightly — driver corruption from updates, a stopped audio service, or a wrong default device — which makes the fix sequence short and high-yield.

Work through these seven fixes in order. The first three take under five minutes combined and resolve most cases.

## Why this happens

- **Corrupt Realtek driver after Windows Update.** The top cause — a half-applied or replaced driver.
- **Windows Audio service stopped.** The service the entire sound stack depends on.
- **Wrong default playback device.** Sound routing to a disconnected HDMI or Bluetooth device.
- **Realtek device disabled.** Disabled in Device Manager or Sound settings.
- **Generic driver lacking codec support.** Windows' basic driver can't drive the specific Realtek codec.
- **Audio enhancements crashing.** Broken DSP effects silencing the output.
- **Failed audio codec hardware.** Rare — the Realtek chip itself, last on the list.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check volume, mixer, and the default device

The thirty-second checks that catch the simple cases.

1. Click the **speaker icon** — confirm volume is up and not muted, and check the **output device** dropdown at the top of the quick settings.
2. Right-click the speaker icon, open **Volume Mixer**, and make sure the app you're testing isn't muted or at zero.
3. Open **Sound settings** (right-click speaker > **Sounds** > **Playback** tab) — right-click **Speakers / Realtek Audio** and **Set as Default Device**.
4. If Realtek doesn't appear, right-click the empty list and enable **Show Disabled Devices** and **Show Disconnected Devices**.
5. Click the device and hit **Test** — a working test tone means the driver is fine and it was purely routing.

### Fix 2: Restart the Windows Audio services

The services the sound stack needs — updates and optimizers stop them.

1. Press **Windows + R**, type `services.msc`, press Enter.
2. Find **Windows Audio**, **Windows Audio Endpoint Builder**, and **Remote Procedure Call (RPC)**.
3. Set **Windows Audio** and **Endpoint Builder** to **Automatic** and **Start** them if stopped; RPC should already be running.
4. If they were stopped, restart the laptop after starting them.
5. Check **Task Manager > Startup** for anything that might be killing them at boot — some "optimizer" tools do.

### Fix 3: Run the audio troubleshooter

Windows' automated repair for common sound misconfigurations.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Playing Audio > Run the troubleshooter**.
2. Select the Realtek device when asked.
3. Let it apply fixes — it commonly re-enables devices and resets defaults.
4. Restart and test with a known-good audio source (a local file, not a browser tab, to rule out browser issues).
5. If it reports a driver issue it can't fix, continue to Fix 4 — that's your cue for the reinstall.

### Fix 4: Reinstall the Realtek driver from your laptop maker

The central fix — replace the corrupt driver with the validated package.

1. Open **Device Manager > Sound, video and game controllers**, right-click **Realtek Audio**, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
2. Restart — Windows falls back to the generic driver.
3. Download the **audio driver** from your **laptop maker's support site** (Dell, HP, Lenovo, ASUS, Acer) for your exact model — not from Realtek's generic downloads.
4. Install it as administrator, restart again.
5. Verify: **Device Manager** should show **Realtek Audio** with a recent driver date, and the **Realtek Audio Console** should open from the Start menu.

Microsoft's audio troubleshooting reference is on [Windows support](https://support.microsoft.com/en-us/windows) if you want the official steps alongside these.

### Fix 5: Disable audio enhancements

Broken DSP effects are a classic silent-output cause.

1. Open **Sound settings > More sound settings > Playback tab**, right-click **Speakers/Realtek Audio > Properties**.
2. Go to the **Enhancements** tab and check **Disable all enhancements**.
3. On the **Advanced** tab, set **Default Format** to **24 bit, 48000 Hz** and uncheck **Allow applications to take exclusive control of this device** as a test.
4. Click OK and test — if sound returns, an enhancement was crashing the pipeline.
5. You can re-enable enhancements one by one later if you miss them, but most users never notice them gone.

### Fix 6: Check for conflicting devices and driver rollback

HDMI and Bluetooth devices hijack the default output — and bad updates need rolling back.

1. In the **Playback** tab, disable devices you don't use (HDMI outputs to monitors, old Bluetooth entries) — right-click > **Disable**.
2. If sound broke right after a Windows update: **Device Manager > Realtek Audio > Properties > Driver > Roll Back Driver**.
3. Use the **Show or hide updates** troubleshooter to block the bad audio driver update from reinstalling.
4. Disconnect **HDMI cables and Bluetooth audio devices** during testing — Windows loves defaulting to them.
5. For the broader "audio driver keeps dying" pattern, see [how to fix audio driver keeps crashing after Windows 11 update](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/).

### Fix 7: System-level repairs and the hardware verdict

When the driver is correct and there's still no sound.

1. Run **Command Prompt as administrator**: `sfc /scannow` — corrupt system files can break the audio stack.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and restart.
3. Test sound in **Safe Mode** — working sound there means third-party software interference.
4. Check the **BIOS** for an audio/codec toggle (some business laptops have one) and make sure it's enabled.
5. If Device Manager never shows any audio device even with **Show hidden devices**, and a Linux live USB also has no sound, the codec chip has failed — a USB sound adapter is the practical workaround.

Our Windows 11 companion covers the same failure on newer systems: [Realtek audio driver not working on Windows 11](/articles/realtek-audio-driver-not-working-windows-11/).

## Closing

Realtek audio failures on Windows 10 are a short story: check the routing, restart the services, reinstall the manufacturer's driver. That sequence restores sound in the vast majority of cases. Only when the device won't appear in Device Manager at all — even as hidden — should you start considering hardware.
