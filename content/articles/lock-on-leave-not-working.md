---
title: "Lock on Leave Not Working in Windows 11? Fix It Now"
slug: "lock-on-leave-not-working"
date: 2026-10-25
categories: ["ai-pc"]
tags: ["lock on leave", "presence sensing", "security", "windows 11", "ai laptop", "privacy"]
description: "Lock on leave not locking your Windows 11 laptop when you walk away? Learn why auto-lock fails and how to restore this security feature."
thumbnail: "/images/thumbs/lock-on-leave-not-working.webp"
faqs:
  - q: "Is lock on leave the same as dynamic lock?"
    a: >
      No. Dynamic lock uses a Bluetooth phone's distance to lock the PC, while lock on leave uses the laptop's own presence sensor to detect that you walked away. They are separate features with separate settings.
  - q: "How long should lock on leave take?"
    a: >
      Most laptops lock within a few seconds to a minute after you leave, depending on the sensor delay setting. If it takes several minutes or never locks, the feature is not working properly.
  - q: "Does lock on leave work if I am on a video call?"
    a: >
      It should still work, but some implementations delay locking while the camera is actively used by a call. Test with no call running to separate the two behaviors.
  - q: "Is lock on leave safe to rely on alone?"
    a: >
      Treat it as a convenience layer, not your only security. Always lock manually with Windows + L when leaving a laptop in a public place, since no sensor is perfect.
---

Lock on leave is a quiet security feature: you walk away from your laptop, and it locks itself. When it stops working, the risk is real — anyone passing by can see your open screen. It is also easy to miss, because nothing announces the failure. You only discover it when you return and find the screen still unlocked.

The feature depends on the same presence sensor chain as wake on approach, but with an added twist: it must decide you have actually left, not just glanced away. That decision involves a delay timer, sensor confidence, and Windows lock policy. Any of those can break, and the symptom is always the same: the screen stays unlocked.

Lock failures often appear with other setup problems. A Python environment that struggles on ARM, like [Python on ARM64 Windows](/articles/python-arm64-windows-setup-issues/), is a sign of a system with rough edges. A [Copilot prompt suggestions feature that does not appear](/articles/copilot-prompt-suggestions-not-appearing/) can indicate AI services in a bad state. And if you own a Dell AI machine, our guide to [Dell Inspiron 14 Plus AI problems](/articles/dell-inspiron-14-plus-ai-problems/) covers model-specific presence quirks.

## Why this happens

- **Lock on leave disabled:** The toggle can be off in Settings, the manufacturer utility, or BIOS.
- **Sensor not detecting departure:** Poor lighting, distance, or a blocked camera can prevent the sensor from confirming you left.
- **Delay timer too long:** Some implementations wait minutes before locking, which feels like failure.
- **Camera held by another app:** A video app using the camera can block presence detection.
- **Driver fault:** A broken sensor or camera driver stops departure detection entirely.
- **Group policy restrictions:** Work laptops may have lock policies that override presence locking.
- **Screen timeout conflicts:** A long screen timeout can mask lock behavior, since the display stays on anyway.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm lock on leave is enabled everywhere

1. Open Settings and search for "presence" to find lock on leave options.
2. Turn on lock on leave and set the delay to the shortest option for testing.
3. Open your manufacturer's utility and check its presence or security section.
4. Make sure dynamic lock is not confusing the test; turn it off temporarily.
5. Restart and test by walking away for two minutes.

### Fix 2: Test sensor detection conditions

1. Sit in front of the laptop, then stand up and step clearly out of camera view.
2. Make sure the room is well lit and no bright window is behind you.
3. Remove any camera cover or privacy shutter.
4. Test from a normal seating distance, not from across the room.
5. If locking works in good conditions but not in dim light, environment is the limiter.

### Fix 3: Fix the sensor and camera drivers

1. Open Device Manager and check System devices, Sensors, and Cameras for warnings.
2. Update or reinstall any problem driver.
3. Download the latest sensor driver from your manufacturer's site if Windows cannot find one.
4. Restart and retest lock on leave.
5. Also update the BIOS, since presence locking often depends on firmware.

### Fix 4: Clear app and camera conflicts

1. Close all video call, camera, and recording apps.
2. Open Settings, then Privacy & security, then Camera, and confirm system access is on.
3. Test lock on leave with no other apps running.
4. If it works, reopen apps one at a time to find the blocker.
5. Restrict the blocking app's camera access or close it when leaving your desk.

### Fix 5: Check lock policy and screen settings

1. Open Settings, then Accounts, then Sign-in options, and confirm require sign-in is set appropriately.
2. Set the screen timeout to a short value, such as 2 minutes, for testing.
3. On Pro editions, run `gpedit.msc` and check lock and presence policies.
4. If the laptop is managed by work or school, ask IT whether lock policies are enforced.
5. Use Windows + L manually as a backup habit while you fix the automatic behavior.

### Fix 6: Reset presence settings completely

1. Turn lock on leave and all presence features off in Settings.
2. Restart the laptop.
3. Turn presence features back on one at a time, testing lock on leave after each.
4. Install all pending Windows updates.
5. If it still never locks, contact manufacturer support, since the sensor may be faulty.

For official Windows security guidance, visit [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows).

### Fix 7: Use dynamic lock as a backup layer

While you troubleshoot the presence sensor, dynamic lock offers a second automatic locking method that does not depend on the sensor at all. It pairs your laptop with your phone over Bluetooth and locks the PC when the phone moves out of range, which covers the same walk-away scenario through a completely different mechanism. It is not perfect — Bluetooth range varies and it can be slow to trigger — but as a stopgap it restores most of the security you lost when lock on leave failed. Running both features together, once presence locking is fixed, gives you two independent layers of protection.

1. Open Settings, then Accounts, then Sign-in options, then Dynamic lock.
2. Pair your phone over Bluetooth if it is not already paired.
3. Check the box to allow Windows to automatically lock your device when you are away.
4. Test by walking away with your phone and timing how long locking takes.
5. Adjust your expectations for range: Bluetooth lock typically triggers within a minute of leaving range.
6. Keep dynamic lock enabled even after fixing presence lock, so a future sensor failure does not leave you unprotected.

## Closing

Lock on leave is a security feature, so a failure deserves prompt attention. Work through toggles, sensor conditions, drivers, and policy settings, and most laptops start locking reliably again. Until it works, make Windows + L a reflex every time you stand up — it takes a second and protects everything on your screen.
