---
title: "How to Fix Wake on Approach Not Working on Your AI Laptop"
slug: wake-on-approach-not-working-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["wake on approach", "presence sensing", "human presence detection", "camera", "ai laptop", "troubleshooting"]
description: "Fix wake on approach not working on your AI laptop with checks for presence sensing settings, camera drivers, BIOS options, and Windows Hello conflicts."
thumbnail: "/images/thumbs/wake-on-approach-not-working-fix.webp"
faqs:
  - q: "What is wake on approach?"
    a: >
      Wake on approach uses the laptop's camera or presence sensor to detect when you sit down in front of it and wakes the machine from sleep automatically, often signing you in with Windows Hello at the same time. It is a Copilot+ PC feature tied to human presence detection.
  - q: "Does wake on approach work with any camera?"
    a: >
      No. It requires a camera or sensor that supports human presence detection, which is a specific hardware capability. A standard webcam without presence sensing cannot provide wake on approach, even with the right software.
  - q: "Why does wake on approach stop working after an update?"
    a: >
      Updates can reset presence settings, replace the camera driver with one that lacks presence support, or change BIOS defaults for the sensor. Re-enabling the setting and reinstalling the camera driver usually restores it.
  - q: "Does wake on approach drain the battery?"
    a: >
      It uses some power because the sensor stays alert during sleep, but a properly working implementation costs only a few percent overnight. Large drain usually means the sensor or a related device is misbehaving during standby.
---

You walk up to your AI laptop expecting it to wake and sign you in, but the screen stays dark until you press a key or open the lid further. Wake on approach is one of those features that feels like magic when it works and is easy to assume is broken when it does not — but it depends on a chain of hardware, BIOS, driver, and Windows settings that all have to agree.

The chain is: a presence-capable camera or sensor, BIOS support for presence detection, a camera driver that exposes it, Windows presence settings turned on, and a sleep state shallow enough for the sensor to wake the machine. Break any link and the laptop simply stays asleep.

This guide checks the chain from the Windows setting down to the hardware, so you find the broken link without guessing.

## Why this happens

- **Presence sensing turned off in Windows or the maker app:** The setting lives in more than one place, and an update or a settings reset can turn it off silently.
- **Camera driver without presence support:** A generic Windows camera driver may run the webcam fine for calls while lacking the presence-detection interface wake on approach needs.
- **BIOS presence detection disabled:** Some BIOS versions ship with human presence detection off, or an update resets it, which removes the sensor from Windows entirely.
- **Sleep state too deep:** If the laptop enters hibernate instead of modern standby, the presence sensor cannot wake it — hibernate powers the sensor off.
- **Windows Hello or camera privacy conflict:** Camera privacy settings or a Windows Hello configuration problem can block the camera from operating during the wake sequence.
- **Sensor blocked or lighting conditions poor:** A covered camera, a privacy shutter left closed, or very dark conditions can prevent the sensor from detecting a person at all.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the feature exists and is enabled in Windows

Start with the setting itself — and confirm your hardware actually supports the feature before chasing drivers.

1. Open **Settings > System > Power & battery** and look for presence or wake on approach options; on some builds they live under **Settings > Bluetooth & devices** or in your maker's control app.
2. Turn on **Wake on approach** and **Lock on leave** if you want both behaviors, or just wake on approach alone.
3. Check your laptop's specifications for human presence detection support — if the model lacks a presence sensor, the feature cannot work regardless of settings.
4. Open the camera privacy shutter if your laptop has one, and make sure nothing covers the camera.
5. Test by putting the laptop to sleep, stepping away for thirty seconds, then approaching — give the sensor a few seconds to react. If it wakes but does not sign you in, [Windows Hello face issues](/articles/windows-hello-face-ai-laptop-fix/) are the next layer to check.

### Fix 2: Reinstall the camera and sensor drivers

A webcam that works for video calls can still lack presence support if its driver is generic. The maker's camera driver package is what exposes presence detection.

1. Open **Device Manager > Cameras** and note the camera model listed.
2. Download the camera driver and any sensor or human-presence driver for your exact model from your maker's support page.
3. Uninstall the camera device in Device Manager, restart, and install the maker driver package.
4. Also check **Device Manager > Biometric devices** and **System devices** for presence sensor entries with warnings.
5. Test wake on approach again after the reinstall — presence support often returns immediately once the proper driver loads.

### Fix 3: Check BIOS presence detection settings

If Windows shows no presence option at all, the BIOS may have the sensor disabled, which hides it from Windows completely.

1. Restart into the BIOS setup and look for human presence detection, presence sensing, or camera configuration sections.
2. Enable presence detection if it is off, and save the change.
3. While in the BIOS, confirm the camera itself is enabled — some BIOS versions have a separate camera toggle.
4. Boot into Windows and check Device Manager again for a presence sensor entry.
5. Re-enable the Windows wake on approach setting from Fix 1, since a BIOS change can reset Windows-side toggles.

### Fix 4: Fix the sleep state so the sensor can wake the machine

Wake on approach only works from modern standby. If the laptop hibernates or fully powers off, the sensor is off and cannot detect you.

1. Open **Settings > System > Power & battery** and confirm the sleep timeout is set to Sleep, not Hibernate, for the test.
2. Run `powercfg /a` in Terminal to see which sleep states your laptop supports — S0 low-power idle is the modern standby state presence needs.
3. If the laptop is set to hibernate on lid close, change the lid-close action to Sleep for testing.
4. Close the lid or press the sleep key, wait thirty seconds, then approach and watch for the screen waking.
5. If wake on approach works from sleep but not from a lid-closed state, check the lid sensor behavior in your maker's app — some laptops disable presence sensing when the lid is fully closed.

### Fix 5: Resolve camera privacy and Windows Hello conflicts

The wake sequence often ends with a Windows Hello face sign-in. A privacy block or Hello problem can stall the whole sequence at a dark screen.

1. Open **Settings > Privacy & security > Camera** and confirm camera access is on for the device.
2. Open **Settings > Accounts > Sign-in options** and confirm Windows Hello face is set up and working when you wake the laptop manually.
3. If Hello fails, remove and re-enroll your face, since a corrupted enrollment can block the wake-and-sign-in flow.
4. Temporarily disable any third-party camera privacy software that might block the camera at the driver level.
5. Test wake on approach again — the screen should wake and Hello should sign you in without further input.

### Fix 6: Update the BIOS and test sensor behavior directly

If every setting and driver checks out, the sensor firmware or BIOS may be at fault, and a direct test proves whether the sensor sees you at all.

1. Check your maker's support page for a BIOS update mentioning presence, camera, or standby fixes.
2. Install the BIOS update on AC power and re-check the BIOS presence setting afterward.
3. Sit in front of the sleeping laptop in normal room lighting and move slightly — the sensor needs a visible person, not a still room.
4. Try approaching from directly in front rather than from the side, since presence sensors have a limited field of view.
5. If the sensor never reacts even after BIOS and driver updates, contact your maker with the camera model and BIOS version — a faulty sensor module is the remaining explanation. For related standby behavior, see [sleep study battery drain fixes](/articles/sleep-study-report-battery-drain-fix/) and [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Wake on approach fails when one link in its chain breaks: the setting, the camera driver, the BIOS toggle, the sleep state, or the sensor itself. Check the Windows setting and the privacy shutter first, repair the camera driver second, and verify the BIOS and sleep state before suspecting hardware. When the chain is intact, the laptop wakes as you sit down — no key press needed. If this fix did not fully resolve the issue, related troubleshooting for [Samsung Galaxy Book4 Edge Ai Issues](/articles/samsung-galaxy-book4-edge-ai-issues-fix/) and [Copilot Account Switching Issues](/articles/copilot-account-switching-issues/) covers neighboring causes that can produce the same symptom on AI laptops.
