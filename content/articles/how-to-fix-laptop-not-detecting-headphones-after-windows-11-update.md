---
title: "Laptop Not Detecting Headphones After a Windows 11 Update"
slug: "how-to-fix-laptop-not-detecting-headphones-after-windows-11-update"
date: "2026-10-08"
categories: ["drivers"]
tags: ["headphones not detected", "windows 11 update", "audio driver", "realtek", "no sound"]
description: "Headphones not detected after a Windows 11 update? Fix the audio driver, jack detection, and default-device issues that silence wired and Bluetooth headphones alike."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-detecting-headphones-after-windows-11-update.webp"
faqs:
  - q: "Why did my laptop stop detecting headphones after a Windows 11 update?"
    a: "Updates commonly replace the audio driver (often Realtek) with a version whose jack-detection or device-switching logic is broken, reset the default playback device to the speakers, or change privacy permissions for the microphone on headset combos. The headphones are usually fine — the update disturbed the audio routing."
  - q: "Should I test wired and Bluetooth headphones differently?"
    a: "Yes. Wired headphone detection depends on the audio codec driver and physical jack sensing, while Bluetooth headphone issues involve the Bluetooth stack and audio profiles. If wired works but Bluetooth does not, troubleshoot Bluetooth; if neither works, the system audio driver or Windows audio service is the suspect."
  - q: "What is jack detection and why does it break?"
    a: "Jack detection is the audio driver's ability to sense when a plug enters the 3.5mm socket and switch output accordingly. Driver updates can break the sensing logic or disable the front-panel jack detection setting in the Realtek Audio Console, so the laptop never realizes headphones were plugged in."
  - q: "Can I just use a USB audio adapter instead of fixing the driver?"
    a: "A USB audio adapter or USB headset bypasses the onboard audio codec entirely and works immediately — it is a fine workaround. But fixing the underlying driver is better long-term, since the broken audio driver can cause other issues like microphone failures and audio service crashes."
---

Plug in your headphones after a Windows 11 update and... nothing. No popup, no device switch, sound keeps coming from the speakers — or worse, total silence. Sometimes Device Manager and Settings do not even acknowledge the headphones exist. It is a maddeningly common post-update regression, and it hits wired and Bluetooth headphones through different mechanisms.

The unifying theme is audio routing. Windows 11 decides where sound goes through a chain: the audio driver detects the device, Windows lists it as a playback endpoint, and the default-device setting routes audio to it. An update can break any link — replacing the Realtek/Conexant audio driver with a faulty build, resetting default devices, or breaking Bluetooth audio profiles. Diagnose which link failed before reinstalling drivers at random.

Work through the fixes in order, testing headphone detection after each step.

## Why this happens

- **Audio driver replaced by the update**: the new Realtek or Intel audio driver has broken jack-detection or endpoint-switching logic.
- **Default playback device reset**: the update silently switches the default output back to the internal speakers.
- **Front-panel jack detection disabled**: the Realtek Audio Console setting that enables plug sensing gets toggled off by the driver update.
- **Bluetooth audio profile failure**: the update breaks A2DP or Hands-Free profiles, so Bluetooth headphones pair but never appear as audio devices.
- **Windows Audio service disruption**: the update leaves the audio service or its dependencies in a stopped state.
- **Privacy permission reset**: microphone access for headset combos gets revoked, breaking headset functionality in calls.
- **Corrupted audio endpoint cache**: Windows caches playback devices, and stale entries can block new endpoints from appearing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical basics and the default device

A surprising number of "not detected" cases are routing, not detection: the headphones are detected but Windows sends audio elsewhere. Verify the obvious first — it takes a minute.

1. Plug the headphones firmly into the correct 3.5mm jack (headphone, not microphone-only) — try unplugging and reseating twice.
2. Right-click the speaker icon in the taskbar and open **Sound settings**; check whether the headphones appear in the output list.
3. If they appear, select them and click **Set as default** (and default communications device for headsets).
4. Test with another pair of headphones or earbuds to rule out a broken plug or cable.
5. For Bluetooth headphones, confirm they are paired in **Settings > Bluetooth & devices** before expecting them in the sound list — pairing and audio-profile connection are separate steps, as in [our Bluetooth troubleshooting guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/).

### Fix 2: Enable jack detection in the audio console

Realtek-based laptops (the majority) manage plug sensing through the Realtek Audio Console. Driver updates frequently disable front-panel jack detection, so the codec never notices the plug.

1. Open **Realtek Audio Console** from the Start menu (install it from the Microsoft Store if missing).
2. Go to **Device advanced settings** and ensure jack detection / "enable auto popup dialog when device is plugged in" is on.
3. Check that the front-panel/headphone jack is not set to "mute" or disabled in the connector settings.
4. Plug in the headphones while the console is open and watch for the detection popup — its appearance confirms sensing works.
5. If your laptop uses Intel, Conexant, or Waves MaxxAudio instead, check the equivalent panel for jack-sensing options.

### Fix 3: Roll back or reinstall the audio driver

If detection broke with the update, the update's audio driver is the prime suspect. Roll back to the previously working driver first.

1. Open Device Manager, expand **Sound, video and game controllers**, right-click your audio device (Realtek, Intel, or Conexant), and open **Properties > Driver**.
2. Click **Roll Back Driver** if available, then restart with a full shutdown.
3. If rollback is unavailable, choose **Uninstall device** (ticking driver deletion), restart, and let Windows reinstall — then test.
4. For a definitive fix, download the audio driver from your laptop manufacturer's support page and install it over the Windows version.
5. After installing, verify the driver date in the Driver tab matches the manufacturer's package, then block driver replacement via Device Installation Settings.

### Fix 4: Restart Windows audio services

The driver can be fine while the audio plumbing is stalled. Windows routes all audio through the Windows Audio service, and updates sometimes leave it — or its dependencies — stopped.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, set it to **Automatic**, and start it if stopped; do the same for **Windows Audio Endpoint Builder**.
3. Right-click **Windows Audio** and choose **Restart** even if it shows as running — a hung service reports "running" falsely.
4. Run **Settings > System > Troubleshoot > Other troubleshooters > Audio > Run** and apply its fixes.
5. Retest headphone detection — service restarts frequently restore endpoints that driver reinstalls did not, a pattern also seen with [Bluetooth services](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/).

### Fix 5: Fix Bluetooth headphone audio profiles

For Bluetooth headphones that pair but produce no sound device, the A2DP (stereo audio) or HFP (headset) profile failed to connect — a distinct problem from pairing itself.

1. In **Settings > Bluetooth & devices**, remove the headphones (**Remove device**), then re-pair them fresh.
2. After pairing, click the device entry and ensure it connects — some headphones need a second tap to establish the audio profile.
3. In **Sound settings**, check that the headphones appear both as an output (Stereo) and, for headsets, as an input device.
4. In Device Manager (**View > Show hidden devices**), look for the headphones under **Bluetooth** and **Audio inputs and outputs** — missing audio entries mean the profile failed.
5. Update the Bluetooth driver from the manufacturer's support page, since profile handling lives in the Bluetooth stack, not the audio driver.

### Fix 6: Check microphone privacy for headset combos

Headsets combine headphones and a microphone, and Windows 11's privacy model can block the microphone half — which some apps interpret as the whole headset failing, especially in calls.

1. Open **Settings > Privacy & security > Microphone** and ensure microphone access is on.
2. Enable **Let desktop apps access your microphone** — this is the toggle Zoom, Teams, and Discord depend on.
3. In **Sound settings > Input**, verify the headset microphone is selected when the headset is connected.
4. Test the full headset in the built-in **Sound Recorder** or **Camera** app rather than only in calls.
5. If the mic works in system apps but not in calls, the issue is per-app permission — check the app's own audio device settings, as covered in [our camera privacy guide](/articles/laptop-camera-not-working-windows-11/).

### Fix 7: Repair the audio stack and test with USB audio

If no driver or service fix restores detection, repair Windows' audio components — and use a USB audio adapter as both diagnostic and workaround.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
2. Check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known audio regressions in your Windows 11 build.
3. Plug in a USB headset or USB-to-3.5mm audio adapter: if it works instantly, the onboard codec driver/stack is the fault, not Windows audio generally.
4. As a last software step, perform an in-place Windows repair from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.
5. If USB audio works but the 3.5mm jack never detects anything across all drivers, the jack's sensing pin or codec has a hardware fault — USB audio remains a perfectly good permanent workaround.

## Closing

Headphones not detected after a Windows 11 update is a routing problem until proven otherwise: check the default device, the jack-detection setting, and the audio services before assuming the driver is broken — and when the driver is broken, the manufacturer's package beats Windows Update's every time. Bluetooth headphones add the profile layer, and headsets add the privacy layer, but the diagnostic order stays the same: physical, routing, sensing, driver, services. Work it in order and the silence ends at one of those layers.
