---
title: "Wake on Approach Not Working? Fix It on Your AI Laptop"
slug: "wake-on-approach-not-working"
date: 2026-10-25
categories: ["ai-pc"]
tags: ["wake on approach", "presence sensing", "ai laptop", "windows 11", "sleep", "copilot plus pc"]
description: "Wake on approach not waking your AI laptop? Learn why your screen stays dark when you sit down and how to fix approach detection."
thumbnail: "/images/thumbs/wake-on-approach-not-working.webp"
faqs:
  - q: "How is wake on approach different from presence sensing?"
    a: >
      Wake on approach is one use of presence sensing: it wakes the screen when you come near. Presence sensing also covers dimming when you look away and locking when you leave, which can fail separately.
  - q: "Does wake on approach work from sleep or only screen-off?"
    a: >
      It depends on the model. Most laptops wake the screen from display-off reliably, while waking from full sleep requires Modern Standby support and the right BIOS settings.
  - q: "Why does wake on approach drain battery?"
    a: >
      The sensor must stay partly awake to watch for you, which uses a small amount of power. If drain is severe, the sensor may be keeping the whole system awake rather than just itself.
  - q: "Can I use wake on approach without Windows Hello?"
    a: >
      Yes, waking the screen does not require face sign-in. Windows Hello only controls whether you still need to enter a PIN or password after the screen wakes.
---

You sit down at your laptop, expecting the screen to light up as it used to, and nothing happens. You have to press the power button or lift the lid like it is an ordinary machine. Wake on approach is a small convenience, but once you are used to it, losing it feels like a step backward.

Wake on approach is more demanding than other presence features because it has to work while the system is mostly asleep. The sensor stays alert, detects you, and tells Windows to wake the display — all without fully waking the machine first. That chain crosses sensor hardware, BIOS, Modern Standby, and Windows, so there are several places it can break.

The failure often comes with companion symptoms. A development tool that misbehaves on ARM, like [Git on ARM64 Windows](/articles/git-arm64-windows-issues/), is unlikely to be the cause but indicates a system with configuration drift. A [Copilot app that keeps signing you out](/articles/copilot-app-signing-out-fix/) can signal account or service trouble that affects AI features broadly. And if [Copilot voice wake word is not working](/articles/copilot-voice-wake-word-not-working/), the always-listening and always-watching features may share a driver or permission problem.

## Why this happens

- **Wake on approach disabled:** The toggle can be off in Settings, the manufacturer utility, or BIOS.
- **Sensor driver fault:** A missing or outdated presence sensor driver breaks approach detection entirely.
- **Modern Standby limitations:** Some sleep states do not support sensor wake, so the screen cannot wake until you press a key.
- **Camera privacy or app conflict:** Another app holding the camera can block the sensor from detecting approach.
- **Lid or power settings:** Lid-close actions and power plans can override sensor wake behavior.
- **BIOS sensor settings:** The sensor may be disabled at firmware level even when Windows shows it as on.
- **Low battery or battery saver:** Aggressive power saving can shut the sensor down to preserve battery.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify every wake toggle

1. Open Settings and search for "presence" to find all presence options.
2. Turn on wake on approach, and also wake on touch if offered.
3. Open your manufacturer's utility and check its presence or smart sense section.
4. Make sure no toggle contradicts another, such as a quiet mode that disables sensors.
5. Restart the laptop and test by walking away for a minute, then returning.

### Fix 2: Check the sensor driver

1. Open Device Manager and look under System devices and Sensors.
2. Check for warning icons on human presence or sensor devices.
3. Right-click any problem device, choose Update driver, then search automatically.
4. If that fails, download the sensor driver from your manufacturer's site.
5. Restart and test wake on approach again.

### Fix 3: Adjust sleep and lid settings

1. Open Settings, then System, then Power & battery.
2. Set the screen to turn off after a short time but keep sleep at a longer interval.
3. Check lid-close action: set it to Sleep, not Hibernate or Shutdown, for testing.
4. Disable hibernate temporarily to rule out hibernate overriding sensor wake.
5. Test wake on approach from display-off first, then from sleep.

### Fix 4: Update BIOS and firmware

1. Visit your manufacturer's support site for your exact model.
2. Install the latest BIOS and any sensor firmware updates.
3. Restart into BIOS and confirm presence or sensor wake options are enabled.
4. Save and exit, then test wake on approach from both display-off and sleep.
5. Note which state works, since BIOS updates often fix one but not the other.

### Fix 5: Clear camera and app conflicts

1. Close all video call, camera, and recording apps.
2. Open Settings, then Privacy & security, then Camera, and confirm system access is on.
3. Test wake on approach with no other apps running.
4. If it works, reopen apps one at a time to find the one blocking the sensor.
5. Update or restrict the blocking app's camera access.

### Fix 6: Test power conditions

1. Plug the laptop into AC power and test wake on approach.
2. If it works on AC but not battery, check battery saver and power plan settings.
3. Turn off battery saver temporarily and retest on battery.
4. Set the power mode to Balanced rather than Best power efficiency for the test.
5. If it only fails on battery, accept a small battery trade-off or keep the sensor on AC only.

For official Windows presence help, visit [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows).

### Fix 7: Check whether an external monitor or dock breaks sensor wake

Many laptop users work with the lid closed or half-open while connected to a dock and external monitor, and that setup can silently disable wake on approach. Some laptops turn off the built-in sensor when an external display is primary, while others route presence detection through the dock, which may not support it at all. The result is a feature that works perfectly on the road but never at your desk, which looks like a random failure until you spot the pattern. Testing with and without the dock takes a minute and immediately tells you whether your desk setup is the cause.

1. Undock the laptop and test wake on approach with only the built-in display.
2. If it works undocked, reconnect the dock and test again to confirm the dock is the variable.
3. Check the dock manufacturer's documentation for presence sensor support.
4. Try waking with the laptop lid open rather than closed while docked.
5. In display settings, set the built-in display as the primary display for testing.
6. If the dock blocks sensor wake, use a keyboard tap or mouse movement to wake at your desk instead.

## Closing

Wake on approach should just work, and when it does not, the fix is usually a toggle, a driver, or a sleep setting rather than broken hardware. Check every presence toggle, fix the sensor driver, and test display-off separately from full sleep to narrow the problem. Once it works again, sitting down and seeing your screen light up feels like the future working properly.
