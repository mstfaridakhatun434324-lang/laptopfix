---
title: "Laptop Camera Not Working? Get Video Back in Minutes"
slug: how-to-fix-laptop-camera-not-working-youtube
date: 2026-09-20
categories: ["drivers"]
tags: ["laptop camera", "camera not working", "webcam", "camera app black"]
description: "Laptop camera not working in calls or the Camera app? Get video back fast with this practical guide to camera permissions, drivers, and app fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-camera-not-working-youtube.webp"
faqs:
  - q: "Why is my laptop camera not working in Zoom but works elsewhere?"
    a: "That split proves the camera hardware and driver are fine — the fault is inside Zoom. Check Zoom's video settings to confirm the right camera is selected, verify Zoom has camera permission in Windows privacy settings, and update or reinstall Zoom. Apps cache camera selections, so a previously selected virtual camera or disconnected USB cam is the usual culprit."
  - q: "What should I check first when the camera stops working?"
    a: "Check the physical layer first: the privacy shutter or sliding lens cover, the Fn-key camera toggle, and whether another app is holding the camera. Those three take thirty seconds and resolve a large share of cases. Then check privacy permissions in Settings, then the driver in Device Manager. Physical before software is the rule."
  - q: "Can antivirus software break my webcam?"
    a: "Yes. Many security suites include a webcam-protection shield that blocks applications from accessing the camera, and its blocks are silent — the app just shows black or reports no camera. Temporarily disable the webcam shield and retest; if video returns, add your video apps to the shield's allow list instead of leaving protection off."
  - q: "Why does Device Manager not show my camera at all?"
    a: "A completely missing camera (even with hidden devices shown) means Windows cannot see the hardware: it may be disabled in the BIOS, disconnected internally, or failed. Check the BIOS camera toggle first, then boot a Linux live USB — no camera there confirms hardware. A camera that appears flagged is a driver problem; one that appears nowhere is hardware or firmware."
---

The laptop camera fails in two distinct ways, and telling them apart saves an hour. In one, the camera works somewhere — the Camera app shows video but Zoom does not — which means the hardware and driver are fine and the failing app is at fault. In the other, no app gets video, which means the fault is in permissions, the driver, or the hardware. The first question to answer is always: does it work anywhere?

This guide starts with the thirty-second physical checks (shutter, Fn toggle, app conflicts), because they resolve an embarrassing share of 'broken' cameras, then moves through permissions, app settings, drivers, and hardware. Each step narrows the fault.

## Why this happens

- **Privacy shutter or lens cover** closed over the camera.
- **Fn-key camera toggle** switched the camera off.
- **Another app holding the camera**, blocking all others.
- **Camera permission revoked** in Windows privacy settings.
- **Wrong camera selected** in the app's video settings.
- **Corrupted or missing camera driver** after an update.
- **Antivirus webcam shield** silently blocking access.
- **Camera disabled in BIOS** or failed hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the shutter, toggle, and app conflicts

Look for a physical privacy shutter or sliding cover over the lens and open it. Press the camera Fn-key combination (often Fn+F8 or a dedicated key) and watch for an on-screen indicator. Then close every app that might use the camera — Teams, Zoom, Discord, browsers — and open only the Windows Camera app. If video appears, one of the closed apps was holding the device; reopen them one at a time to find it. These physical checks take seconds and fix the cases that feel most mysterious.

1. Open the physical privacy shutter or lens cover.
2. Press the camera Fn-key toggle.
3. Close all camera-capable apps completely.
4. Test in the Windows Camera app alone.

### Fix 2: Verify camera privacy permissions

Windows 11 gates camera access per app, and a revoked permission shows as black video or 'no camera'. Go to Settings > Privacy & security > Camera: enable camera access, enable 'Let apps access your camera', allow the specific failing app, and — crucially — enable 'Let desktop apps access your camera' for classic desktop programs like Zoom. Test after each toggle so you know which one mattered. Microsoft documents the permission model in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings > Privacy & security > Camera.
2. Enable camera access and app access.
3. Allow the specific failing app.
4. Enable desktop-app camera access for programs like Zoom.

### Fix 3: Fix the app's camera selection

Open the failing app's video settings and explicitly select the built-in camera ('Integrated Camera' or the laptop's camera name). Apps remember stale selections — an OBS virtual camera from a streaming session, or a USB webcam that is unplugged — and show black when the remembered device is gone. Remove virtual-camera software you no longer use. If the camera works in the Windows Camera app but not in one specific program, this step is almost certainly the fix, and no driver work is needed.

1. Open the app's video/camera settings.
2. Explicitly choose the built-in integrated camera.
3. Remove unused virtual-camera devices.
4. Restart the app and check the preview.

### Fix 4: Reinstall the camera driver

When no app gets video, reinstall the driver. In Device Manager, find the camera under Cameras or Imaging devices, uninstall it (deleting the driver software if offered), and reboot to let Windows reinstall. For the definitive fix, install the camera driver from the laptop maker's support page for your exact model — maker drivers include sensor tuning the generic driver lacks. The [Windows 11 camera walkthrough](/articles/how-to-fix-laptop-camera-not-working-in-windows-11-24h2/) covers per-brand driver packages.

1. Uninstall the camera in Device Manager.
2. Reboot and let Windows reinstall the driver.
3. If still broken, install the maker's camera driver.
4. Test in the Windows Camera app.

### Fix 5: Reset the app and check the antivirus shield

A corrupted app cache can break video even with a healthy driver. For the Windows Camera app: Settings > Apps > Camera > Advanced options > Repair, then Reset. For third-party apps, clear their cache or reinstall. Then check your antivirus for a webcam-protection shield (Norton, Bitdefender, Kaspersky all have one) — temporarily disable it and retest. If video returns, allow-list your video apps in the shield. Black-screen-specific variants of this fault are detailed in the [webcam black screen guide](/articles/how-to-fix-webcam-black-screen-in-windows-11-24h2/).

1. Repair then Reset the Camera app.
2. Reinstall the failing third-party app if needed.
3. Temporarily disable the antivirus webcam shield.
4. Allow-list video apps in the shield.

### Fix 6: Check Device Manager state and the BIOS

If the camera is missing from Device Manager, choose View > Show hidden devices — a greyed-out camera can be right-clicked and enabled. Then reboot into the BIOS and confirm the integrated camera is enabled; updates sometimes flip this toggle. If the camera is absent from both Device Manager (hidden shown) and the BIOS, the hardware is not enumerating — note that for the hardware test. Detection-specific diagnostics continue in the [camera-not-detected guide](/articles/how-to-fix-laptop-camera-not-detected-in-windows-11-24h2/).

1. Show hidden devices and enable any greyed-out camera.
2. Enter the BIOS and confirm the camera is enabled.
3. Save, boot, and re-check Device Manager.
4. Reinstall the driver if the camera reappears.

### Fix 7: Test the hardware with a live USB

Boot a Linux live USB and open its camera app (Cheese on Ubuntu). Video there proves the sensor and its connection are healthy and convicts Windows — return to the driver and permission fixes with confidence. No video there means the sensor module or its ribbon cable through the display hinge has failed. Camera modules are cheap parts, but the cable run through the hinge makes this a fiddly repair; a shop handles it quickly. Hinge-area damage from drops is the usual cause.

1. Boot a Linux live USB and open its camera app.
2. Working video = Windows software fault; return to driver fixes.
3. No video = sensor or cable hardware failure.
4. Get a repair quote for module/cable replacement.

## Closing

Laptop camera failures are almost never the sensor. The physical checks — shutter, Fn toggle, app conflicts — resolve the quick cases; permissions and app device selection resolve the 'works here, not there' cases; the driver reinstall resolves the 'black everywhere' cases. The diagnostic question that organizes everything is whether video works anywhere: anywhere-yes means the app, everywhere-no means the stack below it. Keep that question in mind and the fix follows in minutes. And the next time the camera dies right before a call, check the shutter first — it is always the shutter, right up until the one time it is not.
