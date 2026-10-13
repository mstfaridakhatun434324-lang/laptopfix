---
title: "Realtek Microphone Not Working? Fix It in Minutes"
slug: how-to-fix-realtek-microphone-not-working
date: 2026-09-07
categories: ["drivers"]
tags: ["realtek", "microphone", "mic not working", "audio input", "troubleshooting"]
description: "Nobody can hear you on calls? Fix a dead Realtek microphone with privacy, driver, and jack-detection steps in the right order."
thumbnail: "/images/thumbs/how-to-fix-realtek-microphone-not-working.webp"
faqs:
  - q: "Why is my Realtek microphone not detected at all?"
    a: "The usual reasons are the microphone being disabled in Sound settings, the Realtek driver being replaced by a generic Windows one that doesn't expose the mic array, or privacy settings blocking microphone access. Check Settings > Privacy & security > Microphone first, then the Recording tab in Sound settings."
  - q: "My mic works in the Sound test but not in Zoom or Teams. Why?"
    a: "That means the hardware and driver are fine — the problem is app-level. Check the app's own audio input selection (it may be pointed at the wrong device), the app's permission in Windows privacy settings, and whether another app has grabbed exclusive control of the microphone."
  - q: "Should the microphone be set as the default device?"
    a: "Yes — right-click the speaker icon, open Sound settings, and under Input make sure your Realtek microphone or mic array is selected as the input device. Many 'mic not working' cases are simply Windows listening to the wrong device, like a disconnected headset."
  - q: "Can a Windows update break the Realtek microphone?"
    a: "Very commonly. Updates replace the vendor Realtek driver with a generic one that may not expose the internal mic array correctly, or they reset privacy permissions. If the mic died right after an update, reinstall the manufacturer's Realtek driver package."
---

"Can you hear me? ...Hello?" — the dead-microphone experience is uniquely frustrating because everything else works. Speakers fine, camera fine, but you're mute to the world. Realtek microphone failures on laptops cluster around a few well-understood causes: privacy blocks, wrong default device, driver replacement, and jack-detection confusion. Each has a distinct signature, and this guide reads them in order.

Start with the fastest checks. Most dead mics are a setting, not a failure.

## Why this happens

- **Microphone privacy is blocked.** Windows has a master mic switch plus per-app permissions. Updates and "privacy" tweaks flip these off silently.
- **The wrong input device is selected.** Windows may be listening to a disconnected headset, a monitor's mic, or a disabled device instead of the Realtek mic array.
- **The microphone is disabled in Sound settings.** Disabled recording devices don't appear by default — the mic can be present but invisible and inactive.
- **The Realtek driver was replaced.** A generic Windows audio driver often fails to expose the internal microphone array properly. See [Realtek audio failures after updates](/articles/how-to-fix-realtek-microphone-not-working-on-windows-11/).
- **Jack detection confusion.** Plugging and unplugging headsets can leave the Realtek driver thinking an external mic is connected when it isn't, muting the internal array.
- **Exclusive mode lock.** An app holding exclusive control of the mic blocks every other app — and sometimes doesn't release it when closed.
- **Corrupted driver or hardware fault.** The last suspects: a genuinely broken driver install or a failed mic array, which is rare but real.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check privacy and the selected input device

The two settings that cause most dead mics.

1. Go to **Settings** > **Privacy & security** > **Microphone**. Make sure **Microphone access** is **On**, **Let apps access your microphone** is **On**, and your calling apps are individually allowed.
2. Go to **Settings** > **System** > **Sound**. Under **Input**, make sure the correct device is selected — usually "Microphone Array (Realtek Audio)" for the built-in mics.
3. Click the input device and check the **input volume** slider — drag it up and watch the test bar while you talk. If the bar moves, Windows hears you and the problem is app-level (skip to Fix 5).
4. If the bar doesn't move, continue below.

### Fix 2: Reveal and enable hidden recording devices

Disabled devices hide by default.

1. Right-click the speaker icon > **Sound settings** > scroll down > **More sound settings**. Go to the **Recording** tab.
2. Right-click empty space in the device list and check **Show Disabled Devices** and **Show Disconnected Devices**.
3. If your Realtek microphone appears grayed out, right-click it and choose **Enable**, then **Set as Default Device**.
4. Speak and watch the green level meter — movement means the mic is alive and the issue was just its disabled state.
5. If the mic is enabled, selected, and the meter moves, but apps still can't hear you, jump to Fix 5.

### Fix 3: Fix jack-detection confusion

For mics that died after headset use.

1. Open the **Realtek Audio Console** (search in Start; install it from the Microsoft Store if missing).
2. Look for **jack detection** or **connector settings** — disable automatic jack detection as a test.
3. Unplug all headsets, earbuds, and USB audio devices. Restart the laptop with nothing plugged in.
4. Retest the internal mic array. If it works now, the driver was stuck thinking an external mic was connected.
5. Re-enable jack detection afterward if you regularly switch between internal mics and headsets.

### Fix 4: Reinstall the Realtek driver properly

The core repair for driver-level mic failures.

1. Open **Device Manager** > **Sound, video and game controllers**. Right-click the Realtek device > **Uninstall device**, checking "Attempt to remove the driver" if offered.
2. Also check **Audio inputs and outputs** in Device Manager — uninstall any grayed-out or duplicate microphone entries.
3. Restart the laptop and test with the generic driver Windows installs.
4. Then download the **Realtek audio driver for your exact model** from the manufacturer's support page — for HP laptops, [HP support](https://support.hp.com/us-en) — and install it as administrator.
5. After installation, redo Fixes 1 and 2 — driver reinstalls reset privacy-adjacent defaults and device enablement.

### Fix 5: Fix app-level capture problems

When Windows hears you but the app doesn't.

1. Open the app's own settings (Zoom: Settings > Audio; Teams: Settings > Devices) and set the **Microphone** dropdown explicitly to the Realtek device — don't leave it on "Default" or "Same as System."
2. In the app, use its **Test Mic** feature while watching Windows' input level bar — this tells you whether the app is even opening the device.
3. Close other apps that might hold the mic: in **More sound settings** > **Recording** > mic **Properties** > **Advanced**, uncheck **Exclusive Mode** boxes.
4. Check the app's permission again in **Settings** > **Privacy & security** > **Microphone** — some apps need re-authorizing after updates.
5. As a test, try the mic in the built-in **Sound Recorder** or **Camera** app. Working there but not in Zoom = 100% app configuration.

### Fix 6: Run the troubleshooter and check for conflicts

Automated help plus conflict hunting.

1. Go to **Settings** > **System** > **Sound**, scroll to **Input**, select your mic, and click **Troubleshoot** if offered — or run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Recording Audio**.
2. Temporarily uninstall VoIP-related extras: virtual audio cables, old headset software, Discord/OBS audio plugins — then retest.
3. Check **Device Manager** > **View** > **Show hidden devices** for duplicate mic entries and remove the ghosts.
4. Our broader [microphone troubleshooting guide](/articles/how-to-fix-microphone-not-working-on-laptop-on-windows-11/) covers USB and Bluetooth mic variants of these steps.

### Fix 7: Verify the hardware

The final check, only after software is exhausted.

1. Boot a **Linux live USB** and test the mic there. Working in Linux = Windows driver/config issue (revisit Fix 4 with different driver versions).
2. Inspect the mic pinholes along the laptop's top bezel or keyboard deck — blocked holes (stickers, cases, debris) genuinely mute mics. Clear them gently.
3. If the mic array is dead in Linux too and the holes are clear, the array or its cable has failed — a board-level repair.
4. Practical fallback: a USB or Bluetooth headset bypasses the internal array entirely and usually sounds better anyway.

General audio input help is also on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Dead Realtek mics are a settings problem far more often than a hardware problem: privacy master switch, wrong input device, hidden disabled device, jack-detection stuck on a phantom headset, or a replaced driver. Work outside-in — privacy and selection first, then jack logic, then the driver reinstall, then app configuration. The mic is almost certainly still in there, just muted by something you can unmute in under ten minutes.
