---
title: "Presence Sensing Not Working on Your AI Laptop? Fix It"
slug: "presence-sensing-not-working"
date: 2026-10-25
categories: ["ai-pc"]
tags: ["presence sensing", "human presence", "ai laptop", "windows 11", "camera", "copilot plus pc"]
description: "Presence sensing not detecting you on your AI laptop? Learn why human presence detection fails and how to restore wake, lock, and dimming."
thumbnail: "/images/thumbs/presence-sensing-not-working.webp"
faqs:
  - q: "What is presence sensing on an AI laptop?"
    a: >
      Presence sensing uses the camera or a dedicated sensor to detect whether you are in front of the laptop. It can wake the screen when you approach, dim it when you look away, and lock it when you leave.
  - q: "Does presence sensing need Windows Hello?"
    a: >
      No, presence sensing and Windows Hello are separate features, but they often share the same camera. A camera driver problem can break both at once, so fixing one sometimes fixes the other.
  - q: "Is presence sensing a privacy risk?"
    a: >
      Presence data is processed on the device and is not sent to Microsoft or your manufacturer as video. If you are uncomfortable, you can turn the feature off entirely in Settings.
  - q: "Why does presence sensing work sometimes but not always?"
    a: >
      Lighting, distance, camera angle, and background apps using the camera all affect reliability. Inconsistent behavior usually means a driver or settings issue rather than a dead sensor.
---

Presence sensing is one of those AI laptop features you stop noticing until it breaks. You walk away expecting the screen to lock, and it stays on. You sit down expecting it to wake, and nothing happens. The screen no longer dims when you glance away, and the whole hands-free experience quietly falls apart.

The feature depends on a chain of components: a sensor or camera, a driver, a Windows service, and the right privacy permissions. If any link breaks, presence sensing fails, often silently. The good news is that the chain is short, and most breaks are driver or settings problems you can fix yourself.

Presence issues often appear alongside other AI feature problems. Extensions that misbehave under emulation, such as [VS Code extensions on ARM](/articles/vscode-extensions-arm-issues/), can hold the camera or sensor stack busy. A [Copilot Pro feature that will not activate](/articles/copilot-pro-features-not-activating/) can signal account or licensing trouble that also affects AI services. And if your laptop has [Copilot+ sleep and wake problems](/articles/copilot-plus-pc-sleep-wake-problems/), presence sensing failures may share the same driver root cause.

## Why this happens

- **Sensor or camera driver missing:** Without the human presence driver, Windows cannot see presence data at all.
- **Camera privacy blocked:** If camera access is denied for system features, presence sensing cannot function.
- **Feature turned off:** Presence sensing can be disabled in Settings, BIOS, or the manufacturer utility without you realizing it.
- **Another app using the camera:** A video call app holding the camera can block presence sensing from accessing it.
- **Poor lighting or positioning:** Low light, a tilted lid, or sitting too far away reduces detection reliability.
- **Outdated BIOS:** Presence features often depend on firmware support that arrives in BIOS updates.
- **Windows service stopped:** The human presence or sensor service may be disabled after an update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm presence sensing is enabled

1. Open Settings, then System, then Power & battery, and look for presence options.
2. Also check Settings, then Bluetooth & devices, then Cameras, for presence settings.
3. Open your manufacturer's utility and check for presence or smart sense toggles.
4. Make sure every presence toggle is on, including wake on approach and lock on leave.
5. Restart the laptop so the settings apply cleanly.

### Fix 2: Check camera privacy permissions

1. Open Settings, then Privacy & security, then Camera.
2. Make sure camera access is on for the device and for system features.
3. Close any video call or camera app that might be holding the camera.
4. Test presence sensing with no other camera app open.
5. If it works now, the other app was blocking the sensor.

### Fix 3: Reinstall the presence and camera drivers

1. Open Device Manager and expand System devices and Cameras.
2. Look for human presence, sensor, or IR camera entries with warning icons.
3. Right-click each problem device and choose Uninstall device.
4. Restart the laptop and let Windows reinstall the drivers.
5. If Windows does not find them, download them from your manufacturer's support site.

### Fix 4: Update BIOS and chipset drivers

1. Visit your manufacturer's support site for your exact model.
2. Install the latest BIOS, chipset, and sensor drivers.
3. Restart and check whether presence options appear or behave better.
4. Test wake on approach and lock on leave separately.
5. Note which functions return, since they can fail independently.

### Fix 5: Improve detection conditions

1. Sit directly in front of the laptop at normal working distance.
2. Make sure your face is lit, avoiding strong backlight from a window behind you.
3. Open the lid to a normal angle so the camera points at your face.
4. Remove any camera cover or privacy shutter during testing.
5. Test in a well-lit room to separate environment problems from driver problems.

### Fix 6: Reset sensor services and Windows settings

1. Open Services, find the Sensor Service and Sensor Monitoring Service, and make sure both are running.
2. Open Settings and toggle presence sensing off, restart, then toggle it back on.
3. Install all pending Windows updates.
4. If presence still fails, run the Camera troubleshooter from Settings, then System, then Troubleshoot.
5. If the sensor is physically faulty, contact manufacturer support for a hardware check.

For official Windows camera and presence help, visit [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows).

### Fix 7: Test presence sensing with a different user profile

A corrupted user profile can break presence sensing in ways that look exactly like a driver problem, because the feature's settings and calibration data are stored per user. If presence sensing works for one Windows user but not another, the hardware and drivers are fine, and the problem lives in your profile's settings or registry state. This test is quick and decisive, and it saves you from reinstalling drivers that were never broken. It also explains cases where presence sensing worked until a settings change or a failed update, after which it never recovered.

1. Create a new local user account from Settings, then Accounts, then Other users.
2. Sign into the new account and check whether presence options appear and work.
3. If presence works in the new account, your original profile is the problem.
4. In the original account, toggle all presence features off, restart, and toggle them back on.
5. As a last resort, migrate your files to the new account and use it going forward.
6. If presence fails in both accounts, return to driver and BIOS fixes, since the problem is system-wide.

## Closing

Presence sensing should feel effortless, and when it does not, the cause is usually a driver, a privacy toggle, or a setting buried in a utility app. Work through the chain from settings to drivers to environment, and most laptops start noticing you again. If the sensor itself has failed, you will know quickly, because nothing in software will bring it back. It is also worth rechecking presence settings after every major Windows feature update, since updates sometimes reset camera privacy or sensor permissions without warning. A quick monthly check of wake, lock, and dimming behavior takes less than a minute and catches regressions before they become habits you work around. When presence sensing works properly, it quietly protects your privacy and saves battery at the same time, which is exactly the kind of invisible help an AI laptop should provide.
