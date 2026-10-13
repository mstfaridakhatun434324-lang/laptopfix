---
title: "Microphone Not Working on Your Laptop? Troubleshoot It Here"
slug: troubleshoot-microphone-not-working-on-laptop
date: 2026-09-29
categories: ["drivers"]
tags: ["microphone not working", "laptop mic not detected", "mic not picking up voice", "realtek microphone fix", "windows 11 microphone"]
description: "Nobody can hear you on calls? Work through mic privacy settings, default device selection, and driver fixes to get your laptop microphone working again."
thumbnail: "/images/thumbs/troubleshoot-microphone-not-working-on-laptop.webp"
faqs:
  - q: "Why is my laptop microphone not picking up my voice at all?"
    a: "Start with the input volume slider in Settings > System > Sound — it sometimes sits at zero after driver updates. Then confirm the correct microphone is selected as the input device, since Windows may have switched to a webcam mic or a disconnected headset. If the level meter doesn't move when you speak, check privacy settings to make sure apps can access the microphone, then reinstall the audio driver."
  - q: "How do I test if my laptop microphone hardware is broken?"
    a: "Open Settings > System > Sound, select the microphone under Input, and watch the volume meter while you speak or tap near the mic hole. If the meter moves, the hardware works and the problem is software — routing, permissions, or drivers. If it never moves across every app and after a driver reinstall, and an external USB mic works fine, the internal mic or its connection has likely failed."
  - q: "Why does my mic work in one app but not another?"
    a: "Windows 11 controls microphone access per app under Settings > Privacy & security > Microphone. The failing app probably lacks permission while the working one has it. Also check the app's own audio settings — Zoom, Teams, and Discord each have independent input device selections that override the Windows default. A third possibility is exclusive mode: one app holding the mic exclusively blocks others."
  - q: "Can a Windows update break my microphone?"
    a: "Yes, particularly Realtek audio driver updates delivered through Windows Update. They can reset input levels to zero, switch the default input device, or install a driver version with broken mic array support for your specific laptop. Rolling back the audio driver in Device Manager is the quickest test — if the mic returns, block that driver version and install the manufacturer's package instead."
---

When your microphone stops working on a laptop, the symptom is always reported by someone else: "we can't hear you." The internal mics on modern laptops are tiny holes flanking the webcam, driven by the Realtek audio stack, gated by Windows privacy settings, and individually configured inside every conferencing app. Any one of those layers can mute you silently.

This guide works from the outside in: confirm the hardware responds, check Windows routing and privacy, then repair the driver layer. Test with the built-in Voice Recorder or the Sound settings meter as you go — it gives you instant feedback without needing a call participant.

One thing that trips people up: Windows 11 treats microphone access as a privacy gate, not an error condition. When an app is denied mic access, you do not get a helpful "microphone blocked" message — you get silence, and the app behaves as if the mic simply picked up nothing. That is why the privacy check comes before driver surgery in this guide: reinstalling drivers cannot fix a permission denial, and the symptom looks identical. If your mic problem appeared right after a Windows update or after installing a new conferencing app, permissions are the prime suspect. Keep the Sound settings meter open as you test each fix — immediate visual feedback beats guessing whether anything changed.

Microsoft documents the official microphone troubleshooting steps at the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the baseline reference alongside this guide.

## Why this happens

- **Input volume set to zero** or the mic muted, often after a driver update reset.
- **Wrong input device selected** — Windows switched to a disconnected headset or webcam mic.
- **Microphone privacy settings** blocking the app in Windows 11.
- **The app's own audio settings** pointing at the wrong input.
- **Corrupted Realtek audio driver** after a Windows update.
- **Exclusive mode** letting one app monopolize the microphone.
- **Physical obstruction** — a case, sticker, or debris over the mic holes.
- **Failed mic array** hardware (rare, but it happens).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the mic holes and input volume

Physical first, then the slider everyone forgets.

1. Find the mic holes (tiny pinholes near the webcam or on the side edge). Remove any case, skin, or sticker covering them.
2. Go to **Settings > System > Sound**, scroll to **Input**, and select your internal microphone.
3. Drag the **Input volume** slider up and speak — watch the meter. If it moves, the mic works and something downstream was wrong.
4. Click the mic, then **Test your microphone** and speak at normal volume to confirm a healthy percentage reading.

### Fix 2: Verify Windows privacy settings

Windows 11 denies mic access silently — no error, just silence.

1. Go to **Settings > Privacy & security > Microphone**.
2. Enable **Microphone access** and **Let apps access your microphone**.
3. Scroll down and toggle on your specific apps (Teams, Zoom, Discord, Chrome).
4. Enable **Let desktop apps access your microphone** for classic desktop programs.

### Fix 3: Check the app's own audio settings

Every conferencing app has independent device selection.

1. Open the app's settings (Zoom: Settings > Audio; Teams: Settings > Devices; Discord: Voice & Video).
2. Set the **Input device** explicitly to your internal microphone — don't leave it on "Default" or "System."
3. Run the app's built-in mic test while speaking.
4. Turn off the app's "automatic volume adjustment" temporarily — it can overcorrect a quiet mic into silence.

### Fix 4: Disable exclusive mode and audio enhancements

These "features" cause more mic failures than they fix.

1. Go to **Settings > System > Sound**, select the microphone, and open its properties.
2. Under **Advanced**, uncheck **Allow applications to take exclusive control of this device**.
3. Turn off any **Audio enhancements** toggle.
4. In the classic Sound panel (**More sound settings > Recording** tab), double-click the mic, go to the **Enhancements** tab, and tick **Disable all enhancements**.

### Fix 5: Reinstall the audio driver

The definitive driver-layer fix.

1. Press **Win + X**, open **Device Manager**, and expand **Sound, video and game controllers** and **Audio inputs and outputs**.
2. Uninstall the **Realtek Audio** device (and the microphone entries), ticking driver deletion if offered.
3. Restart. Windows installs a baseline driver — test the mic now.
4. If it works, install your laptop maker's full audio driver package for the complete feature set.

For Realtek-specific mic issues, see [how to fix Realtek microphone problems](/articles/how-to-fix-realtek-microphone-not-working-on-windows-11/).

### Fix 6: Run the recording-audio troubleshooter

Worth two minutes.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run **Recording Audio** (or **Audio**) and apply its fixes.
3. Restart and retest with the Sound settings meter.

### Fix 7: Test with an external mic to isolate hardware

The final diagnostic split.

1. Plug in a USB headset or USB microphone.
2. If the external mic works perfectly, your internal mic array or its ribbon connection has likely failed — a repair-shop job on most laptops.
3. As a workaround, a $20 USB mic or headset gives you full call quality without opening the machine.

## Closing

Microphone failures are a chain — holes, volume, routing, privacy, app settings, drivers — and the break is usually in the middle, not at the ends. The Sound settings input meter is your best diagnostic tool: if it moves, keep working downstream through privacy and app settings; if it doesn't, work upstream through drivers toward hardware. If your camera is giving you trouble alongside the mic, our [webcam black screen guide](/articles/how-to-fix-webcam-black-screen-after-windows-11-update/) covers the other half of video calls. For Bluetooth headset mics specifically, the [Bluetooth troubleshooting guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) addresses the wireless pairing layer. One last tip: after any major Windows update, recheck the input volume slider first — updates resetting it to zero is the single most common "it worked yesterday" mic complaint, and it takes five seconds to rule out before you touch anything else.
