---
title: "Copilot+ PC Camera Not Working? Here's How to Fix It"
slug: copilot-plus-pc-camera-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "webcam", "camera not working", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot+ PC camera showing a black screen in Teams or Zoom? Learn why the webcam fails on Snapdragon and Intel AI laptops and fix it with these proven steps."
thumbnail: "/images/thumbs/copilot-plus-pc-camera-not-working.webp"
faqs:
  - q: "Why does my Copilot+ PC camera show a black screen in Teams?"
    a: "A black camera feed usually means another process — often Windows Studio Effects running on the NPU — has locked the camera stream. It can also be a driver that failed to load after an update. Closing the conflicting app and re-seating the driver fixes most cases."
  - q: "Is the camera problem worse on Snapdragon Copilot+ PCs?"
    a: "Slightly. Snapdragon X laptops use ARM64 camera drivers, and some third-party video apps still ship x64-only camera filters that misbehave under emulation. Native ARM64 apps like Teams and the built-in Camera app work best. Always install camera drivers from your laptop maker's support page rather than Windows Update alone."
  - q: "Should I reinstall the camera driver?"
    a: "Yes, if the camera appears in Device Manager with a warning or as an unknown device. A clean reinstall removes the corrupted driver and forces Windows to load a fresh copy. Do this after ruling out privacy settings and app-level blocks, since a working driver can be disturbed by aggressive reinstalls."
  - q: "Will resetting the Camera app delete my photos or videos?"
    a: "No. Resetting the Camera app only clears its settings, cache, and permissions. Photos and videos you already captured stay in your Pictures > Camera Roll folder. It is one of the safest first steps you can take."
---

You open Teams for a meeting, and your video feed is black — or the camera app says it cannot find your camera at all. On a brand-new Copilot+ PC this feels especially wrong, because the hardware is barely months old. The good news: camera failures on AI PCs are almost never dead hardware. They are driver, privacy, or stream-conflict problems, and they resolve quickly once you find the right layer.

Copilot+ PCs add one wrinkle you will not see on older laptops. Many of them route the camera through the NPU for Windows Studio Effects — background blur, automatic framing, and eye contact correction. If that NPU pipeline stalls, the whole camera feed can freeze even though the sensor itself is fine. A related guide covers what to do when your [Copilot+ PC microphone stops working](/articles/copilot-plus-pc-microphone-not-working/) at the same time, since audio and video often break together after the same update.

This guide walks you through every layer in order: privacy toggles, app conflicts, the driver stack, and firmware.

## Why this happens

- **Camera privacy is switched off:** Windows 11 has both a master camera toggle and per-app permissions. One flipped switch silently blocks every app.
- **Windows Studio Effects locks the stream:** The NPU-powered effects pipeline can crash and hold the camera hostage, so other apps see a black feed. If apps are not using your AI hardware correctly, our guide on [NPU not used by apps in Windows 11](/articles/npu-not-used-by-apps-windows-11/) explains the underlying cause.
- **Driver failed after a Windows update:** A feature update can replace your working camera driver with a generic or incompatible one.
- **Another app is holding the camera:** Zoom, Teams, Discord, or a browser tab can keep an exclusive lock on the device.
- **Physical privacy shutter is engaged:** Many AI laptops have a hardware shutter or a function-key camera kill switch that software cannot override.
- **Camera filter or virtual camera software conflicts:** Third-party virtual cameras (OBS, Snap Camera leftovers) intercept the feed and break it.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Check the physical shutter and function keys

Start with the hardware, because no software fix can help if the lens is physically covered. Many Copilot+ PCs ship with a sliding privacy shutter above the display, and some add a dedicated camera kill switch or an Fn key combo that disables the camera at the firmware level.

1. Look above the display for a small sliding shutter and make sure it is fully open.
2. Check your function keys for a camera icon (often F8 or F9) and press Fn + that key to toggle the camera on.
3. On Lenovo models, confirm the ThinkShutter is not slid closed; on HP models, check the physical kill switch on the side.
4. Open the built-in Camera app and test again before touching any software settings.

### Fix 2: Verify Windows camera privacy settings

Windows 11 can silently block camera access after an update resets privacy toggles. If the master switch is off, every app reports a black or missing camera even though the device is healthy.

1. Open Settings > Privacy & security > Camera and turn on "Camera access."
2. Scroll down and enable "Let desktop apps access your camera" as well.
3. Confirm Teams, Zoom, and your browser each have their individual toggle enabled.
4. Restart the video app and re-test the camera feed.

### Fix 3: Close apps holding the camera hostage

Only one app can cleanly own the camera at a time — a background Zoom session or a crashed Studio Effects process can hold the stream open, leaving other apps with a black feed.

1. Close Teams, Zoom, Discord, and any browser with video tabs open.
2. Open Task Manager, end any leftover processes for those apps, and look for "Windows Camera Frame Server" to restart.
3. Open the Camera app — if it works there, the problem was an app conflict, not the driver.
4. For a related audio conflict, see our guide on the [Copilot+ PC microphone not working](/articles/copilot-plus-pc-microphone-not-working/) and clear both pipelines together.

### Fix 4: Restart the Studio Effects pipeline

Windows Studio Effects routes the camera through the NPU. When that pipeline stalls, the feed freezes or goes black across all apps.

1. Open Settings > Bluetooth & devices > Cameras and select your built-in camera.
2. Turn off all Studio Effects (background blur, eye contact, automatic framing) and test the raw feed.
3. If the feed returns, re-enable effects one at a time to find the one that crashes.
4. Sign out and back in (or restart) to fully reset the NPU effects pipeline if the freeze persists.

### Fix 5: Reinstall the camera driver cleanly

If Device Manager shows the camera with a warning icon, or as an unknown device, the driver is corrupted. A clean reinstall forces Windows to load a fresh copy from the driver store.

1. Open Device Manager, expand "Cameras," right-click your camera, and choose Uninstall device.
2. Tick "Attempt to remove the driver for this device" and confirm.
3. Restart the laptop — Windows will reinstall a driver automatically.
4. If it still fails, download the camera driver from your maker's support page (for example [Dell Support](https://www.dell.com/support) or [HP Support](https://support.hp.com/us-en)) and install it manually.

### Fix 6: Reset the Camera app and check for firmware updates

When the driver is healthy but the Camera app itself misbehaves, a reset clears its corrupted state. Pair this with a firmware check, since several Copilot+ PC makers fixed camera bugs in BIOS updates.

1. Go to Settings > Apps > Installed apps > Camera > Advanced options and click Reset.
2. Check Settings > Windows Update for pending updates and install them.
3. Visit your manufacturer's support site and apply any camera or BIOS updates listed for your model — Microsoft documents general camera fixes on the [Windows support hub](https://support.microsoft.com/en-us/windows).
4. As a last resort, roll back the most recent Windows update from Settings > Windows Update > Update history > Uninstall updates.

## Closing

Camera failures on Copilot+ PCs look dramatic but are rarely hardware problems. Work from the shutter to privacy to the Studio Effects pipeline to the driver, testing after each step, and you will isolate the fault fast. If nothing here restores video, the camera module itself may have failed — contact your manufacturer's support while the warranty is active, and mention that you already ruled out software causes. See also our guide to [Steam games on ARM laptops](/articles/steam-games-arm-laptop/) for gaming-side driver quirks.
