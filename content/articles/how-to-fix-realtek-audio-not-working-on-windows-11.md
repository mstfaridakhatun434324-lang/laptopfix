---
title: "Realtek Audio Not Working on Windows 11? 7 Fixes That Work"
slug: how-to-fix-realtek-audio-not-working-on-windows-11
date: 2026-09-23
categories: ["drivers"]
tags: ["realtek audio", "no sound", "windows 11", "audio driver"]
description: "No sound from Realtek audio on Windows 11? Restore it with these 7 fixes — Realtek driver reinstall, Audio Console repair, and service restarts."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-on-windows-11.webp"
faqs:
  - q: "Why is my Realtek audio not working on Windows 11?"
    a: "The most common causes are Windows 11 replacing the manufacturer's Realtek driver with an incompatible generic version, the Realtek Audio Console app failing to initialize the codec, the wrong playback device set as default, or the Windows Audio service being stuck. Realtek codecs are highly hardware-specific, so the generic Windows HD Audio driver often produces silence or broken output where the manufacturer's driver works fine."
  - q: "Where do I download the Realtek audio driver for Windows 11?"
    a: "From your laptop manufacturer's support site — Dell, HP, Lenovo, ASUS, or Acer — for your exact model. Laptop makers customize Realtek drivers for their specific codec revision and speaker tuning, so their version beats both Windows Update and Realtek's generic reference driver. Avoid third-party driver download sites; they frequently bundle outdated or wrong-revision drivers with adware."
  - q: "What is Realtek Audio Console and do I need it?"
    a: "Realtek Audio Console is the UWP control app for Realtek codecs on Windows 11 — it manages enhancements, equalizer, and jack detection. You don't strictly need it for basic sound, but some features (front-panel jack detection, DTS/Dolby processing) require it. If it's broken or missing, reinstall it from the Microsoft Store after installing the manufacturer's Realtek driver; the two are version-matched."
  - q: "Why does Realtek audio break after every Windows 11 update?"
    a: "Windows Update aggressively pushes Realtek driver updates that may not match your codec revision, and feature updates sometimes reset the audio device configuration. The defense: install the manufacturer's driver, then pause updates or use Device Installation Settings to stop automatic driver updates. If it just broke, roll back the driver in Device Manager — the previous version was working. Related enhancement conflicts are covered in the [Dolby audio guide](/articles/best-way-to-fix-dolby-audio-not-working/)."
---

No sound at all, or sound from the wrong device, or the speaker icon shows everything fine while silence comes out — Realtek audio failures on Windows 11 are common precisely because Realtek codecs are everywhere and Windows Update keeps "upgrading" their drivers into brokenness.

Realtek audio depends on three matched pieces: the driver, the Audio Console app, and the codec configuration. When Windows swaps one piece for a mismatched version, sound dies. This guide repairs the stack in order.

## Why this happens

- **Windows Update replaced the OEM Realtek driver:** A generic or wrong-revision driver that can't drive your codec.
- **Realtek Audio Console broken or mismatched:** The control app failing to initialize the audio pipeline.
- **Wrong default playback device:** Sound routing to a disconnected HDMI or Bluetooth device.
- **Windows Audio service stuck:** The service layer wedged, silencing all output.
- **Corrupt driver installation:** Partial update leaving the driver half-installed.
- **Enhancement/DSP conflict:** Broken processing modules muting or distorting output.
- **Front-panel jack detection stuck:** The codec thinking headphones are plugged in when they aren't.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the default device and restart audio services

Half of "no sound" cases are routing, not drivers.

1. Right-click the speaker icon and choose **Sound settings**.
2. Under **Output**, make sure your **Speakers (Realtek Audio)** is selected — not HDMI, not a disconnected Bluetooth device.
3. Click the device and confirm volume isn't muted and **Enhance audio** is off for testing.
4. Press **Win + R**, type `services.msc`, and **Restart** both **Windows Audio** and **Windows Audio Endpoint Builder**.
5. Test with a system sound.

If sound returns, the service was stuck. If the Realtek device isn't listed at all, the driver is the problem — continue. For the broader no-sound case where no output device works, the [no-sound troubleshooting guide](/articles/best-way-to-fix-no-sound-on-laptop/) covers the full routing checklist.

### Fix 2: Install the manufacturer's Realtek driver

This is the core fix — the OEM driver matched to your codec revision.

1. Go to your laptop maker's support site and download the **audio driver** for your exact model.
2. In **Settings > Apps**, uninstall any existing **Realtek Audio Driver** and **Realtek Audio Console**.
3. Restart, then install the downloaded driver package.
4. Restart again and test sound before reinstalling the Console app.

Do not use Realtek's generic reference driver from random download sites — codec revisions differ, and the wrong one installs silently but produces no sound. For Dell machines, [Dell support](https://www.dell.com/support) is the source; other brands have equivalent pages.

### Fix 3: Reinstall Realtek Audio Console from the Store

A broken Console app can mute the entire pipeline.

1. After the driver is installed (Fix 2), open the **Microsoft Store** and install **Realtek Audio Console**.
2. Open it and verify it detects your codec — if it shows "not supported," the driver and app versions are mismatched.
3. In the Console, check the speaker/headphone configuration matches your actual setup.
4. Disable any enhancements inside the Console while testing.

Driver and Console must be version-matched — that's why installing both fresh from the manufacturer + Store works when piecemeal updates don't. General driver-crash patterns are covered in the [audio crash guide](/articles/how-do-i-fix-audio-driver-keeps-crashing/).

### Fix 4: Uninstall and clean-reinstall the audio driver

When installing over the top fails, wipe and rebuild.

1. In Device Manager, expand **Sound, video and game controllers**, right-click **Realtek Audio**, and choose **Uninstall device**, ticking **Attempt to remove the driver**.
2. Also uninstall **Intel Smart Sound Technology** entries if present (they interact with Realtek on Intel platforms).
3. Restart — Windows installs a base HD Audio driver. Test: basic sound should work.
4. Install the manufacturer's Realtek driver on top and restart again.

Test at each stage — if the base Windows driver produces sound but the Realtek driver doesn't, the Realtek package is the wrong revision for your codec.

### Fix 5: Fix jack detection and disable front-panel confusion

Stuck jack detection routes all audio to phantom headphones.

1. In Realtek Audio Console, look for **jack detection** or **connector settings** and disable automatic detection temporarily.
2. Plug and unplug headphones firmly a few times — the mechanical switch in the jack can stick.
3. In the classic Sound dialog (**Playback** tab), right-click empty space and tick **Show Disabled Devices** and **Show Disconnected Devices**.
4. If duplicate Realtek outputs appear, disable the ones you don't use and set the correct one as **Default Device**.

If sound only works through headphones and never speakers (or vice versa), jack detection is the prime suspect.

### Fix 6: Roll back and block bad driver updates

If sound died right after a Windows update, go back and stay there.

1. In Device Manager, open the Realtek device's **Properties > Driver** tab and click **Roll Back Driver**.
2. Restart and verify sound.
3. Go to **Settings > Windows Update** and pause updates, then use the **Show or hide updates** troubleshooter to block the audio driver update.
4. Alternatively: **System > About > Advanced system settings > Hardware > Device Installation Settings > No** stops all automatic driver installs.

This is maintenance, not just repair — without it, Windows will re-break the driver on its own schedule.

### Fix 7: Repair system files and check BIOS audio

The last layer: system corruption and firmware.

1. Open Command Prompt as administrator: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart into BIOS and check for an **Audio** / **Onboard Audio** toggle under **Advanced** or **Devices** — make sure it's enabled.
3. Check for a BIOS update from the manufacturer — some fix audio codec initialization.
4. Test with a Linux live USB: sound in Linux proves the hardware works and isolates the fault to Windows.

Sound in Linux but silence in Windows after all driver work means a deep Windows issue — a repair install (keeping files) rebuilds the audio stack. Silence everywhere means the codec or speaker hardware failed — run the manufacturer's hardware diagnostics.

## Closing

Realtek audio on Windows 11 breaks in a predictable way: Windows Update swaps the driver, the Console mismatches, sound dies. The repair is equally predictable — manufacturer's driver, matched Console app, correct default device — and blocking future automatic driver swaps keeps it fixed. Once the right driver is in place, Realtek codecs are perfectly reliable.
