---
title: "How to Fix Realtek Audio Not Working on an HP Laptop"
slug: how-to-fix-realtek-audio-not-working-on-hp-laptop
date: 2026-09-13
categories: ["drivers"]
tags: ["realtek audio", "hp laptop", "no sound", "audio driver"]
description: "Fix Realtek audio not working on an HP laptop: restore the sound device, repair the Realtek driver, and fix the red X on the speaker icon."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why is there a red X on the speaker icon on my HP laptop?"
    a: "The red X means Windows cannot find a working audio output device. Usually the Realtek audio device is disabled, its driver is corrupted, or Windows Update installed an incompatible driver. Re-enabling the device in Device Manager or reinstalling the HP-provided Realtek driver clears it in most cases."
  - q: "Should I install the Realtek driver from HP or from Realtek directly?"
    a: "Install it from HP. HP customizes the Realtek package with the correct codec configuration, speaker tuning, and hotkey support for your exact model. Generic Realtek drivers sometimes install but leave speakers silent or break the audio function keys. Get it from your model's page on HP's support site."
  - q: "My headphones work but the laptop speakers do not. Is that a driver issue?"
    a: "It can be. Headphones and internal speakers are separate endpoints driven by the same Realtek chip, and a misconfigured driver can mute one while the other works. Check the playback device list, make sure Speakers is the default, and reinstall the driver before assuming the speakers are physically dead."
  - q: "Can a Windows update really break my audio?"
    a: "Yes, and it is one of the most common causes. Feature updates sometimes replace the vendor audio driver with a generic one that does not match the codec, or reset the default playback device. The fix is to reinstall the HP Realtek driver and block the bad update from reinstalling itself."
---

No sound from an HP laptop is disorienting — videos play silently, calls go nowhere, and the speaker icon wears a red X like a badge of failure. Realtek audio chips power the sound on the vast majority of HP laptops, so when the Realtek driver breaks, everything audio-related breaks with it: speakers, headphone jack, and sometimes the microphone.

The encouraging part is that dead speakers are rarely the cause. In most cases the audio device is disabled, the driver is wrong, or Windows routed sound to a phantom device. This guide works from the fastest checks to full driver repair, and you will know at each step whether you are making progress.

Realtek's HD audio codec is the heart of sound on nearly every HP laptop, handling everything from the built-in speakers to the 3.5mm headphone jack through a single driver package. HP layers its own tuning on top — some models carry Bang & Olufsen branding, others use Waves MaxxAudio processing — which is why the generic Windows audio driver so often fails as a substitute. When that carefully matched stack breaks, the symptoms are total: no playback devices, a red X on the speaker icon, or sound that routes nowhere. Understanding that the codec, the HP customizations, and Windows' audio services form one chain is what makes the fixes below work in the right order.

## Why this happens

- **Realtek device disabled:** The audio device can be disabled in Device Manager or in Sound settings, muting everything at the source.
- **Driver replaced by Windows Update:** Updates frequently swap HP's tuned Realtek driver for a generic one that does not drive the speakers.
- **Corrupted driver files:** A failed update or a bad shutdown can corrupt the driver, leaving the device with a yellow warning in Device Manager.
- **Wrong default playback device:** Sound may be routing to a disconnected HDMI monitor or a disabled Bluetooth device instead of the speakers.
- **Audio service stopped:** The Windows Audio service can stall, especially after updates, silencing all output.
- **Enhancement conflicts:** Audio enhancements and third-party audio apps can conflict with the Realtek driver and kill output.
- **BIOS audio disabled:** Rare, but some HP BIOS versions allow disabling the onboard audio controller.
- **Headphone jack stuck in "plugged" state:** Lint or a worn jack can trick the codec into thinking headphones are connected, muting the speakers permanently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious output settings

1. Click the speaker icon in the taskbar and confirm volume is up and not muted.
2. Click the **>** arrow (or sound output selector) next to the volume slider and make sure **Speakers (Realtek Audio)** is selected — not an HDMI display or a disconnected Bluetooth device.
3. Right-click the speaker icon → **Sound settings → More sound settings → Playback**, right-click empty space, and enable **Show Disabled Devices** and **Show Disconnected Devices**.
4. If Speakers appears greyed out, right-click and choose **Enable**, then **Set as Default Device**.

### Fix 2: Restart the Windows Audio services

1. Press **Win + R**, type **services.msc**, and press Enter.
2. Find **Windows Audio**, right-click → **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. Set both services' **Startup type** to **Automatic** if they are not already.
4. Test sound. A stalled audio service is a quick win and costs nothing to check.

### Fix 3: Run the built-in audio troubleshooter

1. Open **Settings → System → Sound → Troubleshoot** (or **Advanced → Output devices → Troubleshoot**).
2. Let it run fully and apply any fixes it suggests.
3. The troubleshooter sometimes re-enables disabled devices or restarts services you missed — worth the two minutes even if you are skeptical.

### Fix 4: Re-enable and reinstall the Realtek device

1. Open **Device Manager → Sound, video and game controllers**, right-click **Realtek Audio**, and choose **Enable device** if available.
2. If it is already enabled, right-click → **Uninstall device**, check **"Attempt to remove the driver"**, and restart.
3. Windows will reinstall a driver automatically. Test sound; if the red X is gone but quality is poor or enhancements are missing, proceed to install HP's driver. Similar device-vanishing behavior affects [Wi-Fi adapters](/articles/how-to-fix-wifi-adapter-not-showing-up/) too, and the reinstall logic is the same.

### Fix 5: Install the official HP Realtek driver

1. Go to [HP's support site](https://support.hp.com/us-en), enter your model, and download the **Realtek High-Definition Audio driver** for your Windows version.
2. Run the installer as administrator and restart when prompted.
3. In Device Manager, confirm the driver provider is **Realtek Semiconductor Corp.** with a recent date.
4. Retest speakers and the headphone jack separately — both endpoints should now work.

### Fix 6: Disable audio enhancements

1. Go to **Sound settings → More sound settings → Playback**, right-click **Speakers → Properties → Enhancements** (or **Advanced**).
2. Check **"Disable all enhancements"** and click OK.
3. On the **Advanced** tab, uncheck **"Allow applications to take exclusive control of this device"** temporarily for testing.
4. Enhancements are a frequent silent killer, especially after driver updates change how they interact with the codec.

### Fix 7: Check the headphone jack and BIOS

1. Plug headphones in and out firmly a few times — if the speakers suddenly return, the jack's detection switch was stuck.
2. Inspect the jack with a flashlight for lint; remove debris gently with a wooden toothpick, never metal.
3. Restart into BIOS (**F10** on HP) and verify onboard audio is enabled if such an option exists.
4. If speakers work in BIOS diagnostics (HP's **F2** hardware diagnostics include an audio test) but not Windows, the problem is definitively software.

### Fix 8: Block the bad driver from returning

1. Once sound works, open **Settings → Windows Update → Advanced options** and pause updates briefly while you stabilize.
2. Use **Device Installation Settings** (**System → About → Advanced system settings → Hardware**) set to **No** to stop Windows replacing your working driver.
3. Guidance from [Microsoft support](https://support.microsoft.com/en-us/windows) covers hiding specific driver updates if one particular update keeps breaking audio. This step prevents the monthly recurrence many users report with [audio driver crashes](/articles/how-to-fix-audio-driver-keeps-crashing-on-windows-10/).

## Closing

Realtek audio failures on HP laptops follow a predictable script: the wrong driver, a disabled device, or sound routed to the wrong endpoint. Restore the correct output device, reinstall HP's Realtek driver, and protect it from Windows Update's well-meaning interference — and the red X becomes a distant memory rather than a recurring appointment.
