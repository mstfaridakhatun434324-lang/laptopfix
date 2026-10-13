---
title: "How to Fix Laptop Speakers Not Working on Windows 11 24H2"
slug: how-to-fix-laptop-speakers-not-working-in-windows-11-24h2
date: 2026-10-13
categories: ["drivers"]
tags: ["laptop speakers not working", "no sound windows 11", "realtek speaker fix"]
description: "Laptop speakers not working on Windows 11 24H2? Restore sound with these step-by-step audio driver, settings, and service fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my laptop speakers stop working after the 24H2 update?"
    a: "The 24H2 update often replaces your audio driver with a version that mishandles speaker output or breaks enhancement integration. The speaker hardware is almost certainly fine. Reinstalling the manufacturer's audio driver restores normal sound in the vast majority of cases."
  - q: "My speakers show as working but produce no sound. What is wrong?"
    a: "This usually means the wrong output device is selected, the audio service is stuck, or enhancements are corrupting the stream. Check the default output device first, then disable enhancements, then restart the Windows Audio service — one of those three fixes it most of the time."
  - q: "Should I update or roll back the audio driver?"
    a: "If sound broke right after an update, roll back first — it restores the last working driver instantly. If sound never worked or broke gradually, do a clean install of the newest driver from your laptop maker. Both paths are covered step by step below."
  - q: "Can a Windows setting mute speakers without showing it?"
    a: "Yes. Per-app volume levels, the communications ducking feature, and exclusive-mode application control can all silence speakers while the main volume looks normal. The fixes below check each of these hidden mute paths The communications tab's ducking option, which lowers volume during calls, is another quiet culprit worth checking in the same Sound control panel."
---

No sound from your laptop speakers after the Windows 11 24H2 update is one of those problems that makes you question the hardware — until you plug in headphones and they work fine. That contrast is actually good news: it proves the audio system is alive and the issue is specific to the speaker output path, which is almost always a driver or settings problem.

Speaker failures on 24H2 trace back to a handful of causes: a driver the update broke, the wrong default device, a stuck audio service, or enhancement software gone wrong. The fixes below start with the thirty-second checks and escalate to full driver reinstallation.

## Why this happens

- **24H2 replaced the audio driver:** The update installs a generic or mismatched driver that drives headphones but not the internal speaker path.
- **Wrong default output device:** Windows routes audio to a disconnected HDMI, Bluetooth, or USB device instead of the internal speakers.
- **Broken audio enhancements:** Waves MaxxAudio or vendor EQ packs corrupt the speaker stream while leaving headphone output untouched.
- **Windows Audio service stuck:** The core audio service can hang after the update, producing silence despite normal-looking settings.
- **Exclusive mode hijack:** An app takes exclusive control of the audio device and never releases it, muting everything else.
- **Speaker disabled in Sound settings:** Updates occasionally disable the speaker device outright in the playback list.
- **Corrupted driver files:** Partial driver updates leave mismatched Realtek or Intel Smart Sound files that fail on the speaker endpoint.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the correct output device is selected

The most common "no sound" cause is audio routed to the wrong device.

1. Click the speaker icon in the taskbar, then click the **>** arrow (or **Sound output** selector) next to the volume slider.
2. Select **Speakers** (your internal audio device, often labeled Realtek Audio).
3. Play a test sound. If you hear it, the problem was routing all along.
4. For permanence, go to **Settings > System > Sound**, select your speakers, and set them as default.

If speakers do not appear in the list at all, the driver is not loading them — skip ahead to Fix 5.

### Fix 2: Check hidden mute states and volume mixer

Several Windows features mute audio without touching the main volume slider.

1. Right-click the speaker icon and open **Volume mixer**. Check that no app is muted and the **System sounds** slider is up.
2. Go to **Settings > System > Sound > More sound settings**, double-click **Speakers**, and open the **Levels** tab — confirm nothing is muted there.
3. In the same properties window, open the **Advanced** tab and uncheck **Allow applications to take exclusive control of this device**.

Exclusive mode is a frequent silent-audio culprit: a game or call app grabs the speakers and never lets go.

### Fix 3: Restart the Windows Audio services

A stuck audio service produces exactly this symptom — everything looks fine, no sound comes out.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Audio**, right-click it, and choose **Restart**.
3. Do the same for **Windows Audio Endpoint Builder**.
4. Test your speakers immediately.

If the service fails to restart or stops again within minutes, the underlying driver is crashing — continue to the driver fixes. Our broader [no-sound troubleshooting guide](/articles/best-way-to-fix-no-sound-on-laptop/) covers service-level issues in more depth.

### Fix 4: Disable audio enhancements

Enhancement packs process the speaker stream separately from headphones, so they can kill speaker audio while headphones work.

1. Open **Settings > System > Sound > More sound settings**.
2. Double-click **Speakers**, open the **Enhancements** tab, and check **Disable all enhancements**.
3. On drivers without that tab, look on the **Advanced** tab for an **Enable audio enhancements** checkbox and uncheck it.
4. Click **Apply** and test.

If sound returns, keep enhancements off or reinstall the enhancement pack (Waves MaxxAudio, Dolby) fresh from your laptop maker's driver page.

### Fix 5: Roll back the audio driver

If speakers died immediately after the 24H2 update, undo the driver change.

1. Open **Device Manager**, expand **Sound, video and game controllers**.
2. Right-click your audio device, choose **Properties**, and open the **Driver** tab.
3. Click **Roll Back Driver**, pick a reason, and restart.

This restores the pre-update driver in under two minutes. If the button is unavailable, proceed to the clean reinstall in Fix 6.

### Fix 6: Clean-reinstall the manufacturer's audio driver

The permanent fix for most 24H2 speaker failures.

1. Download the audio driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. In Device Manager, right-click the audio device, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart — Windows loads a basic driver.
4. Run the manufacturer's installer and restart again.

Vendor packages include the speaker-specific tuning and enhancement integration that generic drivers lack. If your audio driver also [keeps crashing](/articles/best-way-to-fix-audio-driver-keeps-crashing/), this same clean reinstall addresses both symptoms.

### Fix 7: Run the audio troubleshooter and check for BIOS updates

Two final automated options before suspecting hardware.

1. Go to **Settings > System > Sound**, scroll to **Advanced**, and click **Troubleshoot** next to **Output device**. Apply any recommended fixes.
2. Check your laptop maker's support page for a BIOS update — some 24H2 audio issues trace to firmware-level audio codec initialization that a BIOS update corrects.
3. As a last check, boot into the BIOS setup and listen for beep codes, or run the built-in hardware diagnostics (Dell, HP, and Lenovo all ship these) to confirm the speakers physically work.

If diagnostics play sound but Windows does not, the problem is 100% software — repeat Fix 6 with a different driver version.

## Closing

Silent laptop speakers on Windows 11 24H2 are a software problem in nearly every case: wrong output device, a stuck audio service, broken enhancements, or a driver the update replaced. Check routing first, then work through the service and enhancement fixes, and finish with a clean manufacturer driver reinstall — sound comes back at one of those stages for the vast majority of laptops.
