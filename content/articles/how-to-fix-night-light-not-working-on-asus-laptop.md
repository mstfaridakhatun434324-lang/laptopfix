---
title: "Night Light Not Working on Your ASUS Laptop? Here's the Fix"
slug: how-to-fix-night-light-not-working-on-asus-laptop
date: 2026-10-08
categories: ["drivers"]
tags: ["night light", "asus laptop", "blue light filter", "display driver", "windows 11"]
description: "Night Light won't turn on or has no effect on your ASUS laptop? Fix it with graphics driver updates, Night Light registry resets, and ASUS color profile checks."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why is Night Light greyed out on my ASUS laptop?"
    a: "A greyed-out Night Light toggle usually means the graphics driver is not reporting display capabilities correctly, or an ASUS utility like Armoury Crate or Splendid is overriding color controls. Updating the graphics driver from ASUS support and disabling third-party color profiles typically restores the toggle."
  - q: "Does Night Light work with HDR enabled?"
    a: "Not reliably. HDR takes over the display pipeline and Night Light's color-temperature shift often has no visible effect while HDR is active. If Night Light seems broken, turn off HDR under Settings, System, Display and test again before troubleshooting further."
  - q: "Why does Night Light turn on but the screen barely changes?"
    a: "The strength slider may be set too low, or an ICC color profile from ASUS Splendid is flattening the effect. Drag the Strength slider toward the warmer end in Night Light settings, and remove custom color profiles under Color management to let Night Light's shift show through."
  - q: "Can Armoury Crate break Night Light?"
    a: "Yes. Armoury Crate's GameVisual modes and Splendid color presets apply their own color transformations that can override or conflict with Night Light. Switch GameVisual to Default and disable Splendid's vivid modes when diagnosing Night Light problems. You can restore your preferred visual mode once Night Light is confirmed working."
---

Night Light is supposed to be the simplest feature in Windows: flip a toggle, and your screen shifts warm at sunset. On ASUS laptops it has a habit of doing nothing at all — the toggle moves, the schedule is set, sunset comes and goes, and the display stays exactly the same cold blue-white. Or worse, the toggle is greyed out entirely.

ASUS laptops add extra layers between Windows and your display that most troubleshooting guides ignore. Armoury Crate's GameVisual modes, Splendid color profiles, and ASUS-customized graphics drivers all touch the same color pipeline Night Light uses. When any of them conflicts, Night Light loses silently.

This guide is written specifically for ASUS machines. You will check the ASUS-specific culprits first, then work through the standard Windows Night Light repairs — driver refreshes, registry resets, and schedule fixes — in the order that actually resolves the problem on these laptops.

## Why this happens


- **ASUS Splendid/GameVisual overriding color:** Armoury Crate's display modes apply their own color matrices that sit downstream of Night Light and can cancel its effect.
- **Corrupt Night Light registry state:** The CloudStore registry keys that hold Night Light's schedule and strength can corrupt, leaving the toggle disconnected from the actual feature.
- **Outdated or generic graphics driver:** If Windows replaced ASUS's graphics driver with a generic one, Night Light may lose the display-driver hooks it needs.
- **HDR taking over the pipeline:** With HDR enabled, Windows hands color management to the HDR pipeline and Night Light's temperature shift stops having visible effect.
- **Custom ICC color profiles:** ASUS factory color profiles under Color Management can flatten or override Night Light's warm shift.
- **Fast Startup caching a bad display state:** Hybrid shutdown can preserve a broken color-pipeline state across reboots, making the problem look permanent.
- **Location services disabled:** The sunset-to-sunrise schedule depends on location. Without it, the automatic schedule never triggers.
- **Stuck schedule from a Windows update:** Updates occasionally leave the Night Light scheduler in a state where manual toggles and schedules fight each other.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Reset ASUS display modes to Default


Before touching Windows settings, neutralize the ASUS layer. GameVisual and Splendid are the most common Night Light killers on these laptops, and resetting them takes under a minute.

1. Open Armoury Crate (install it from the Microsoft Store if missing).
2. Go to the GameVisual section.
3. Set the mode to Default — avoid Vivid, Eye Care, or Cinema while testing.
4. In MyASUS or the Splendid utility, turn off any active color enhancement.
5. Toggle Night Light off and on again in Settings, System, Display, Night Light.
6. Check whether the screen now shifts warm. If it does, the ASUS profile was the culprit.

### Fix 2: Update the graphics driver from ASUS support


Night Light depends on the graphics driver exposing display controls correctly. The ASUS-validated driver — not the generic one Windows Update prefers — is what you want here. Use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics or your GPU vendor's tool as a secondary check.

1. Find your exact ASUS model on the sticker or in MyASUS.
2. Download the latest graphics driver (Intel, AMD, or NVIDIA as applicable) from ASUS support.
3. In Device Manager, expand Display adapters, right-click your GPU, and choose Uninstall device with driver removal checked.
4. Restart, then install the ASUS driver package you downloaded.
5. Restart once more and test Night Light at maximum strength.

### Fix 3: Reset Night Light's registry state


When the toggle moves but nothing happens, the CloudStore registry data behind Night Light is usually corrupt. Deleting those keys forces Windows to rebuild them from defaults — this is the fix that resolves the majority of stubborn cases.

1. Press Windows + R, type regedit, and press Enter.
2. Navigate to HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current.
3. Expand the long key starting with default$windows.data.bluelightreduction.bluelightreductionstate.
4. Right-click the Data subkey inside it and delete it.
5. Do the same for the key starting with default$windows.data.bluelightreduction.settings.
6. Restart your laptop. Open Night Light settings — the toggle and schedule will be reset to defaults.
7. Reconfigure your schedule and strength, then test.

### Fix 4: Remove conflicting color profiles


ICC profiles installed by ASUS utilities or calibration tools can sit between Night Light and the panel and mute its effect. Clearing them lets Night Light drive the display directly.

1. Open Settings and search for Color management, then open it.
2. Select your laptop display at the top.
3. Check Use my settings for this device.
4. Remove any ASUS or custom profiles, leaving only the system default (sRGB) if present.
5. Click OK and restart.
6. Test Night Light again at full strength.

### Fix 5: Disable HDR and Fast Startup


Two Windows features that quietly sabotage Night Light: HDR reroutes color management, and Fast Startup can cache a broken display state across reboots. Turning both off isolates the problem cleanly.

1. Go to Settings, System, Display and turn off Use HDR if it is enabled.
2. Open Control Panel, Power Options, then Choose what the power buttons do.
3. Click Change settings that are currently unavailable.
4. Uncheck Turn on fast startup and click Save changes.
5. Shut down fully (not restart), wait ten seconds, then power on.
6. Test Night Light. Re-enable Fast Startup later only if you miss it.

### Fix 6: Fix the schedule and location settings


If Night Light works manually but never activates automatically, the scheduler — not the feature — is broken. The sunset-to-sunrise mode needs location access, and a corrupt schedule entry can jam the whole mechanism.

1. Open Settings, System, Display, Night Light.
2. Turn off Schedule night light temporarily and use the Turn on now button to confirm manual mode works.
3. Go to Settings, Privacy & security, Location and make sure Location services is on.
4. Return to Night Light settings, enable Schedule night light, and choose Sunset to sunrise.
5. If it still fails, set explicit hours (for example 9 PM to 7 AM) instead of the location-based schedule.

### Fix 7: Run a clean boot to find conflicting software


If everything above checks out, some third-party utility — screen dimmers, overlay tools, or display managers — is intercepting the color pipeline. A clean boot strips Windows down to essentials so you can identify the offender.

1. Press Windows + R, type msconfig, and press Enter.
2. On the Services tab, check Hide all Microsoft services, then click Disable all.
3. On the Startup tab, click Open Task Manager and disable all startup items.
4. Restart and test Night Light.
5. If it works, re-enable services in halves until the culprit returns — display utilities and overlays are the usual suspects.
6. Uninstall or reconfigure the offending program. Similar display-driver conflicts are covered in our [Lenovo Night Light fix](/articles/how-to-fix-night-light-not-working-on-lenovo-laptop/) and [Dell Night Light fix](/articles/how-to-fix-night-light-not-working-on-dell-laptop/).

## Closing


On ASUS laptops, Night Light failures are almost always a conflict rather than a broken feature — an Armoury Crate mode, a stale color profile, or a corrupt registry key sitting between the toggle and your panel. Work the list top to bottom and you will find which layer is interfering. Once it is working, leave GameVisual on Default and let Windows handle the color temperature on its own.
