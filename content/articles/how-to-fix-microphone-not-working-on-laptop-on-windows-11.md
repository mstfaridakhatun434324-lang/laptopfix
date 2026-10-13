---
title: "How to Fix a Microphone Not Working on a Laptop (Windows 11)"
slug: how-to-fix-microphone-not-working-on-laptop-on-windows-11
date: 2026-09-11
categories: ["drivers"]
tags: ["microphone not working", "laptop mic fix windows 11", "mic driver reinstall"]
description: "Microphone not working on your Windows 11 laptop? Fix muted mics, permission blocks, and driver failures with this step-by-step repair guide."
thumbnail: "/images/thumbs/how-to-fix-microphone-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why is my laptop microphone not working on Windows 11?"
    a: "The top causes are microphone privacy permissions blocking apps, the wrong input device selected, the mic muted at the driver level, or a broken audio driver after an update. Hardware failure of the built-in mic array is uncommon — work through the software fixes first."
  - q: "How do I test if Windows detects my microphone?"
    a: "Go to Settings > System > Sound and look at the Input section. Speak normally — the volume bar next to the input device should move. If no input device appears at all, the driver is not loading the mic, and you should jump to the driver fixes below."
  - q: "Why does my mic work in one app but not another?"
    a: "That pattern points to per-app privacy permissions or exclusive-mode capture. Check Settings > Privacy & security > Microphone to confirm the app is allowed, and disable exclusive mode in the mic's advanced properties so one app cannot lock out the others."
  - q: "Can a Windows update break the microphone?"
    a: "Yes. Updates frequently replace the audio driver with a version that mishandles the microphone array, or reset privacy permissions. If the mic died right after an update, rolling back or clean-reinstalling the audio driver usually restores it. Also check that the update did not flip your microphone privacy toggles off, since updates occasionally reset those permissions silently."
---

You join a call and nobody can hear you. The microphone level bar in Settings sits dead flat no matter how loudly you speak — or worse, the input device has vanished entirely. On Windows 11, microphone failures are rarely the tiny built-in mic hardware giving up; they are permission blocks, wrong default devices, muted driver levels, or an audio driver the latest update broke.

The diagnostic order matters: verify Windows sees the mic and which app is blocked, then fix permissions and levels, then repair the driver. Each step below includes the exact clicks, so follow them in sequence.

## Why this happens

- **Microphone privacy permissions:** Windows 11 blocks apps from the mic by default-ish granularity — one denied toggle silences everything.
- **Wrong input device selected:** The system routes capture to a disconnected headset or virtual device instead of the built-in array.
- **Mic muted at driver level:** The microphone is muted or set to zero in the legacy Sound control panel, invisible from the modern Settings UI.
- **Broken audio driver after update:** The update's audio driver mishandles the microphone endpoint while speakers work fine.
- **Exclusive mode capture:** One app locks the mic exclusively, starving every other app.
- **Audio enhancements interfering:** Enhancement APOs can corrupt the capture stream on some driver versions.
- **Disabled mic in Device Manager:** The microphone array device gets disabled during driver migrations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone privacy permissions

The most common Windows 11 mic killer — and the fastest to check.

1. Go to **Settings > Privacy & security > Microphone**.
2. Ensure **Microphone access** is **On** and **Let apps access your microphone** is **On**.
3. Scroll the app list and confirm your specific app (Teams, Zoom, Discord) is toggled **On**.
4. Also enable **Let desktop apps access your microphone** for non-Store applications.

Retest immediately. If the mic works in the Settings test but not in your app, permissions were the entire problem.

### Fix 2: Select the correct input device and unmute it

Routing and hidden mutes are the next most common causes.

1. Go to **Settings > System > Sound**. Under **Input**, select your built-in microphone (often **Microphone Array** or **Realtek Audio**).
2. Click the **>** arrow next to it, confirm the **Input volume** slider is up (75–100), and test — the bar should move as you speak.
3. Click **More sound settings**, open the **Recording** tab, double-click the mic, and check the **Levels** tab for a mute button or zeroed slider.
4. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**.

The legacy Sound panel exposes mute states the modern UI hides — always check both. For headset-specific issues, see our [USB headset troubleshooting guide](/articles/best-way-to-fix-usb-headset-not-working/).

### Fix 3: Run the recording-audio troubleshooter

Windows' automated pass catches configuration tangles quickly.

1. Go to **Settings > System > Sound**, scroll to **Advanced**, and click **Troubleshoot** next to the input device — or go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Recording Audio**.
2. Apply every recommended fix and retest.

The troubleshooter resets the audio endpoint builder state and driver flags in one pass, which resolves the "mic visible but dead" cases that manual checks miss.

### Fix 4: Disable audio enhancements on the input

Enhancement processing on the capture path corrupts or silences the mic on buggy drivers.

1. In **More sound settings > Recording**, double-click your microphone.
2. On the **Enhancements** tab, check **Disable all enhancements** (or uncheck **Enable audio enhancements** on the Advanced tab).
3. Click **Apply** and test.

If the mic springs to life, keep enhancements off — the slight quality difference is not worth an unreliable microphone.

### Fix 5: Re-enable the mic in Device Manager

A disabled capture device vanishes from Settings entirely.

1. Open Device Manager and expand **Audio inputs and outputs**.
2. If the microphone shows a down arrow, right-click and choose **Enable device**.
3. Click **View > Show hidden devices** and enable any grayed-out microphone entries.
4. Restart the audio stack: in **Services**, restart **Windows Audio** and **Windows Audio Endpoint Builder**.

If the mic appears here but not in Settings, enabling it plus the service restart almost always restores it.

### Fix 6: Clean-reinstall the audio driver

When the mic died with a Windows update, the driver is the prime suspect.

1. Download the audio driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. In Device Manager, under **Sound, video and game controllers**, right-click the audio device, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart, then run the manufacturer's installer and restart again.

Vendor audio packages include the correct microphone-array tuning that generic drivers lack. If the whole audio subsystem is unstable, our [audio driver crash guide](/articles/best-way-to-fix-audio-driver-keeps-crashing/) addresses the deeper driver problem.

### Fix 7: Test with an external mic and check the BIOS

The final fork between software and hardware.

1. Plug in a USB or 3.5mm external microphone. If it works, Windows' capture stack is fine and the built-in array is the problem.
2. Check the BIOS/UEFI setup for an internal microphone toggle — rare, but some business laptops have one.
3. Run the manufacturer's hardware diagnostics to test the mic array.
4. If diagnostics fail and no software fix helps, the mic array or its ribbon cable needs service — a repair-shop job, since mic arrays sit under the display bezel or palmrest.

External mics bypass the internal array entirely, so a working USB mic also serves as your immediate workaround for important calls while you arrange a repair.

## Closing

A silent laptop microphone on Windows 11 is a permissions, routing, or driver problem in nearly every case — not a dead mic. Check privacy toggles first, verify the input device and hidden mute states second, and clean-reinstall the manufacturer's audio driver if the failure followed an update. Your voice comes back at one of those stages on the vast majority of laptops.
