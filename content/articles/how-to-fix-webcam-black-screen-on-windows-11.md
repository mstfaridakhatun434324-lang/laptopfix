---
title: "Webcam Black Screen on Windows 11? Fix Your Camera Feed"
slug: how-to-fix-webcam-black-screen-on-windows-11
date: 2026-09-07
categories: ["drivers"]
tags: ["webcam black screen", "camera not working", "windows 11 camera", "camera app"]
description: "Webcam shows only a black screen on Windows 11? Find out why the camera feed goes dark and fix it with privacy, driver, and app repairs."
thumbnail: "/images/thumbs/how-to-fix-webcam-black-screen-on-windows-11.webp"
faqs:
  - q: "Why is my webcam showing a black screen but the light is on?"
    a: "The camera sensor is powered but no frames are reaching the app — a classic driver or permission failure. The app opened the device, the LED lit, but the driver failed to deliver frames, so you see black. Reinstalling the camera driver and checking privacy permissions resolves this in most cases, since the hardware path is clearly alive."
  - q: "Can another app block my webcam and cause a black screen?"
    a: "Yes. Only one app can hold the camera at a time, and a background app — a previous video call, a camera utility, even a browser tab — can keep the device locked. The second app then shows black. Closing all camera-using apps, or rebooting to release the lock, restores the feed. This is why a reboot mysteriously fixes so many black-screen webcams."
  - q: "Do I need a driver for my laptop's built-in webcam?"
    a: "Usually the driver comes from Windows or the laptop maker and installs automatically, but it can break or go missing after updates. Built-in webcams appear under Cameras or Imaging devices in Device Manager. If the entry is flagged or missing, reinstalling the camera driver from the laptop maker's support page restores the video pipeline the Camera app depends on."
  - q: "Why does my webcam work in one app but show black in another?"
    a: "That split points at the failing app, not the camera. The working app proves the driver and hardware deliver frames. The broken app usually has its camera permission revoked, is pointed at the wrong device (an OBS virtual camera, for example), or has a corrupted cache. Check that app's camera permission and device selection before touching drivers."
---

A black webcam screen with the camera light on is one of the most misleading symptoms in Windows 11. The light says the camera has power; the black frame says no video is arriving. The gap between those two facts is where the fault lives — in the driver, the app's permission, or another program holding the camera hostage.

The diagnostic split is clean: if the camera works in one app but not another, the failing app is at fault. If it is black everywhere, the driver or a system-level block is at fault. Start with the app-level checks, because they take seconds, then move down the stack to permissions, drivers, and the BIOS.

## Why this happens

- **Camera privacy permission revoked** for the app or for all desktop apps.
- **Another app holding the camera**, blocking every other app from frames.
- **Corrupted or missing camera driver** after a Windows update.
- **Wrong camera selected** in the app (virtual camera, OBS, or disconnected USB cam).
- **Camera disabled in Device Manager** or by the laptop's privacy shutter/key.
- **Camera app cache corrupted**, showing black despite a working feed.
- **BIOS camera setting disabled**, cutting the device at the firmware level.
- **Antivirus privacy shield** blocking camera access silently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Close every app that might hold the camera

Only one app can use the camera at a time. Close Zoom, Teams, Discord, OBS, browser tabs with video calls — everything — then open the Windows Camera app alone. If the feed appears, one of the closed apps was holding the device. Reopen apps one at a time to find the culprit, and check that app's settings for an option like 'keep camera on in background' to disable. A reboot achieves the same release if you cannot find the holder.

1. Close all video-call, streaming, and browser apps completely.
2. Open the Windows Camera app by itself.
3. If the feed works, reopen apps one by one to find the holder.
4. Disable background camera use in the offending app.

### Fix 2: Check camera privacy permissions

Windows 11 can revoke camera access per app or system-wide, and the symptom is exactly a black screen. Go to Settings > Privacy & security > Camera: make sure camera access is on, 'Let apps access your camera' is on, and the specific app is allowed. Scroll down to 'Let desktop apps access your camera' too — classic desktop programs like Zoom need that separate toggle. Microsoft documents the permission model in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings > Privacy & security > Camera.
2. Enable camera access and 'Let apps access your camera'.
3. Enable the specific failing app in the list.
4. Enable 'Let desktop apps access your camera' for desktop programs.

### Fix 3: Select the right camera in the app

Apps remember camera selections, and they remember wrong ones — an OBS virtual camera left selected after streaming, or a USB webcam that is no longer plugged in, produces a black preview. Open the failing app's video settings and explicitly choose the built-in camera (usually named after the laptop or 'Integrated Camera'). In the Windows Camera app, use the switch-camera button if it shows a second device. This step resolves the 'works in Teams, black in Zoom' split instantly.

1. Open the failing app's video/camera settings.
2. Explicitly select the built-in/integrated camera.
3. Remove or disable virtual-camera devices you no longer use.
4. Restart the app and check the preview.

### Fix 4: Reinstall the camera driver

A black feed in every app means the driver layer is suspect. In Device Manager, find the camera under Cameras or Imaging devices, uninstall it (deleting the driver software if offered), then reboot and let Windows reinstall. For a definitive fix, download the camera driver from the laptop maker's support page for your exact model and install that instead — maker drivers include the sensor tuning Windows' generic driver lacks. The [dedicated black-screen walkthrough](/articles/how-to-fix-webcam-black-screen-in-windows-11-24h2/) covers driver variants per brand.

1. Uninstall the camera device in Device Manager.
2. Reboot and let Windows reinstall the driver.
3. If still black, install the maker's camera driver package.
4. Test in the Windows Camera app.

### Fix 5: Check the privacy shutter, kill switch, and Device Manager state

Many laptops have a physical privacy shutter over the lens, a sliding cover, or an Fn-key camera kill switch — any of which produces a black feed with the light behaving oddly. Slide the shutter open and press the camera Fn key. Then check Device Manager: if the camera shows a down-arrow (disabled), right-click and enable it. If it is missing entirely, choose 'Show hidden devices' — a greyed-out camera means Windows sees it but something disabled it. Camera detection failures have their own checklist in the [camera-not-detected guide](/articles/how-to-fix-laptop-camera-not-detected-in-windows-11-24h2/).

1. Open any physical privacy shutter or lens cover.
2. Press the camera Fn-key toggle if your laptop has one.
3. In Device Manager, enable the camera if it shows as disabled.
4. Show hidden devices to find a greyed-out camera entry.

### Fix 6: Reset the Camera app and check antivirus shields

A corrupted Camera app cache can show black even with a healthy driver. Go to Settings > Apps > Installed apps > Camera > Advanced options and use Repair, then Reset. Also check your antivirus: many suites (Norton, Bitdefender, Kaspersky) have a webcam-protection shield that silently blocks apps, and its block looks exactly like a black screen. Temporarily disable the webcam shield and retest — if the feed returns, add your video apps to the shield's allow list.

1. Repair then Reset the Camera app in Settings > Apps.
2. Check your antivirus for a webcam-privacy shield.
3. Temporarily disable the shield and retest.
4. Allow-list your video apps in the shield.

### Fix 7: Check the BIOS camera setting and test hardware

Enter the BIOS and verify the integrated camera is enabled — some BIOS versions expose a camera toggle that updates can flip. If the camera is enabled in the BIOS but absent from Device Manager even with hidden devices shown, boot a Linux live USB: a working camera there proves Windows is at fault; no camera there means the sensor module or its ribbon cable has failed. Camera modules are inexpensive parts, but the cable runs through the display hinge, so hinge-area damage is the usual cause.

1. Enter the BIOS and confirm the integrated camera is enabled.
2. Check Device Manager with hidden devices shown.
3. Boot a Linux live USB and test the camera.
4. No camera in Linux means a hardware repair.

## Closing

The black webcam screen is a pipeline symptom: power reaches the sensor (the light proves it), but frames never reach the app. The blockage is almost always above the hardware — another app holding the camera, a revoked privacy permission, the wrong device selected, or a broken driver. Work the stack from the app downward and you will find the blockage quickly, because each layer has a clean test: one-app-works means the app, all-apps-black means the driver, missing-device means the BIOS or hardware. And once the feed is back, glance at the physical shutter first the next time it goes dark — the simplest cause is also the easiest to forget.
