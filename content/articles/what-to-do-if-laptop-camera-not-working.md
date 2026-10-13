---
title: "What to Do If Your Laptop Camera Is Not Working"
slug: what-to-do-if-laptop-camera-not-working
date: 2026-10-05
categories: ["drivers"]
tags: ["laptop camera", "webcam not working", "camera app", "camera privacy", "windows 11"]
description: "Laptop camera not working in Zoom, Teams, or the Camera app? Check permissions, drivers, and privacy settings in the right order to get video back."
thumbnail: "/images/thumbs/what-to-do-if-laptop-camera-not-working.webp"
faqs:
  - q: "Why is my camera not working in Zoom but works in the Camera app?"
    a: "When the camera works in one app but not another, the hardware and driver are fine — the problem is app permissions or settings. Check Settings, then Privacy and security, then Camera, and confirm the specific app is allowed to access the camera. Also check inside the app: Zoom and Teams each have their own camera selector, and they sometimes latch onto a virtual camera or the wrong device after updates. Re-selecting the built-in camera there fixes it."
  - q: "Should the camera light turn on when an app uses it?"
    a: "Yes. On virtually all laptops, a small LED next to the camera lights up whenever the camera is active, and Windows shows a camera icon in the taskbar. If the light is on but the app shows black, the camera is working and the app is mishandling the feed. If the light never comes on, the app is not reaching the camera at all — focus on permissions, the driver, and whether another app has the camera locked."
  - q: "Can antivirus software block my laptop camera?"
    a: "Yes. Many security suites include webcam protection that blocks all camera access by default or prompts the first time an app requests it. If the camera works with the antivirus disabled but not with it enabled, open the antivirus settings and look for webcam or camera protection, then whitelist your video apps. This is a common cause of sudden camera failure right after installing or updating security software."
  - q: "Why does my camera show a black screen instead of an error?"
    a: "A black screen usually means the app opened the camera successfully but is receiving no frames. Common causes include another app holding the camera open, a privacy shutter left closed, the wrong camera device selected, or a driver that initialized partially. Close all other apps that might use the camera, check for a physical shutter slider, and verify the correct camera is selected in the app before suspecting a driver problem."
---

A dead laptop camera always fails at the worst moment — two minutes before a job interview, a class, or a client call. The screen shows black, the app says "camera not found," or everything looks fine until you join the meeting and nobody can see you. The good news: laptop cameras rarely die. In the overwhelming majority of cases, the camera is fine and something in software is blocking it.

Camera troubleshooting has a specific order that matters. Permissions and privacy shutters cause most failures, driver issues cause most of the rest, and hardware failure is genuinely rare. Work through the steps below in sequence and you will find the block quickly.

## Why this happens

- **App lacks camera permission:** Windows privacy settings can block individual apps or all desktop apps from the camera. This is the single most common cause.
- **Privacy shutter closed:** Many laptops have a physical shutter slider or a function key that kills the camera. It is easy to close and forget.
- **Another app holding the camera:** Only one app can use the camera at a time. A background app holding it open makes every other app see black.
- **Corrupted camera driver:** Windows updates can break the camera driver, leaving Device Manager showing the device with an error or not at all.
- **Antivirus webcam protection:** Security suites increasingly block camera access by default, and their prompts are easy to dismiss permanently by accident.
- **Wrong camera selected in the app:** Virtual cameras from OBS, Snap Camera remnants, or phone-as-webcam apps can become the default, showing black when they are not running.
- **Camera disabled in Device Manager or BIOS:** The device can be disabled in software or switched off at the firmware level, especially after BIOS updates.
- **Hardware failure or disconnected cable:** Rare, but the camera cable runs through the display hinge — the most flexed cable in the laptop — and can fail after years of opening and closing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the privacy shutter and function key

The most embarrassing cause is also the most common on business laptops.

1. Look for a physical shutter slider above the camera — a tiny plastic tab. Slide it open; you should see the lens glass, not a red or black cover.
2. Check for a camera kill key (often **Fn + F8** or a key with a camera icon). Press it and watch for an on-screen notification.
3. Some Lenovo ThinkPads and HP EliteBooks have the shutter integrated into the key itself — a tap toggles a physical cover. Confirm it is open.
4. Open the **Camera** app from the Start menu. If you now see yourself, the shutter was the whole problem. Our broader camera guide at [laptop camera not working](/articles/laptop-camera-not-working-windows-11/) covers related scenarios.

### Fix 2: Grant camera permission to the app

Windows privacy settings are the top software cause, and they change silently during updates.

1. Go to **Settings → Privacy & security → Camera**. Make sure **Camera access** is on.
2. Scroll to **Let apps access your camera** and confirm it is on, then check that your specific app (Zoom, Teams, Camera) is allowed in the list.
3. Scroll further to **Let desktop apps access your camera** — classic desktop programs like older Zoom builds need this separate toggle. Turn it on.
4. Restart the app after changing permissions. Apps only check camera access at launch, so a running app will not pick up the change until restarted.

### Fix 3: Close whatever is holding the camera

One open camera blocks all others, and the holder is often invisible.

1. Close every app that might use the camera: Zoom, Teams, Skype, Discord, OBS, browser tabs with video calls, and the Camera app itself.
2. Open **Task Manager** and end any lingering processes for those apps — video apps often keep running in the system tray.
3. Check the taskbar for the camera indicator icon. If it is showing, something is still using the camera. If you cannot find what, restart the laptop — a clean boot guarantees nothing holds it.
4. Reopen only your target app and test. If the camera works now, the problem was contention, and you know to fully quit video apps rather than minimizing them.

### Fix 4: Select the right camera inside the app

Apps do not always pick the camera you expect.

1. In Zoom: **Settings → Video → Camera** — select the integrated camera explicitly, not "Same as System" or a virtual device.
2. In Teams: **Settings → Devices → Camera** — same check. Remove or disable virtual cameras (OBS Virtual Camera, Snap Camera) you no longer use.
3. In browsers: click the camera icon in the address bar during a call and verify the correct device is chosen; browsers remember per-site device choices.
4. If the integrated camera does not appear in the app's list at all, the driver is the problem — continue to Fix 5. Black-screen issues specifically are covered in our [webcam black screen guide](/articles/how-to-fix-webcam-black-screen-after-windows-11-update/).

### Fix 5: Reinstall the camera driver

Driver breakage is the leading cause when permissions and shutters check out.

1. Open **Device Manager → Cameras** (or **Imaging devices** on older Windows). Right-click the camera and choose **Uninstall device**, checking **Delete the driver software** if offered.
2. Restart the laptop. Windows will detect the camera and reinstall a driver automatically.
3. If Windows installs a generic driver that misbehaves, download the camera driver from the manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — using your exact model number.
4. After reinstalling, re-check the privacy settings from Fix 2, because driver reinstalls can reset app permissions. Microsoft's official camera support documentation also walks through these permission checks.

### Fix 6: Check antivirus webcam protection

Security software is a frequent silent blocker.

1. Open your antivirus or security suite and look for **webcam protection**, **camera protection**, or **privacy** settings.
2. If camera access is set to block by default, change it to **ask** or add your video apps to the allowed list.
3. Test with the antivirus's webcam protection temporarily disabled. If the camera works, you have found the culprit — re-enable protection with proper exceptions rather than leaving it off.
4. Windows Security itself does not block cameras, so if you only use Microsoft Defender, this fix does not apply to you.

### Fix 7: Check Device Manager status and BIOS

For cameras that do not appear anywhere, go deeper.

1. In Device Manager, enable **View → Show hidden devices**. A grayed-out camera with an error code points to a driver or enumeration failure — try **Uninstall** on the hidden entry, then **Action → Scan for hardware changes**.
2. Check for a camera toggle in BIOS/UEFI setup (under **Security → I/O Port Access** on many business laptops). Make sure the integrated camera is enabled.
3. If the camera appears in Device Manager with **Code 45** (device disconnected), the internal cable or module is the suspect — this sometimes follows drops or hinge repairs.
4. As a workaround while diagnosing, a USB webcam bypasses the internal camera entirely and confirms the rest of your video-call setup works.

## Closing

Camera failures follow a clear hierarchy: shutter, permissions, contention, app selection, driver, security software, firmware. Almost every case resolves in the first five steps, which is worth remembering the next time the screen goes black two minutes before a meeting. Check the physical things first, the permission things second, and the driver things third — in that order, every time.
