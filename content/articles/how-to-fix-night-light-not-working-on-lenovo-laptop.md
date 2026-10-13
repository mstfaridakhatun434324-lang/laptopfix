---
title: "Night Light Not Working on Lenovo Laptop? Here's the Fix"
slug: "how-to-fix-night-light-not-working-on-lenovo-laptop"
date: 2026-09-17
categories: ["drivers"]
tags: ["night light", "lenovo laptop", "blue light filter", "display driver", "windows 11"]
description: "Night Light greyed out or not turning on in Windows on your Lenovo? Fix it with display driver updates, registry checks, and schedule settings."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why is Night Light greyed out on my Lenovo laptop?"
    a: "A greyed-out Night Light toggle almost always means the display driver is not exposing the color-temperature controls Windows needs. This happens with generic Microsoft Basic Display drivers, corrupted graphics drivers, or drivers replaced by Windows Update. Reinstalling the Lenovo-validated graphics driver for your exact model restores the toggle in nearly every case."
  - q: "Night Light turns on but the screen does not change color. Why?"
    a: "That means the toggle works but the color transform is not applying, which points to the graphics driver or a conflicting color profile. Update the graphics driver from Lenovo support, remove custom ICC color profiles in Color Management, and check that HDR is off, since HDR and Night Light can conflict on some Lenovo panels."
  - q: "Can the registry fix a broken Night Light?"
    a: "Yes, for cases where the feature's state is corrupted. Deleting the CloudStore cache entries for Night Light under the HKCU registry hive forces Windows to rebuild the settings, which fixes toggles stuck off or schedules that never trigger. Back up the registry key first, since incorrect edits elsewhere can cause other problems."
  - q: "Does Night Light work with external monitors on Lenovo laptops?"
    a: "Night Light applies to the built-in display reliably, but external monitor support depends on the graphics driver and connection type. It generally works over HDMI and DisplayPort with current drivers but can fail over some USB-C docks. If Night Light works on the laptop screen but not the external monitor, update the graphics driver and test with a direct cable connection."
---

Night Light is the blue-light filter built into Windows, and when it stops working on a Lenovo laptop the symptom is specific: the toggle is greyed out, the schedule never triggers, or the screen never warms no matter what the settings say. It is a small feature, but people who rely on it for evening work notice immediately.

Night Light depends on the graphics driver exposing color-temperature controls to Windows. That dependency is why the feature breaks after driver updates and why the fix is almost always driver-related. Lenovo's validated graphics drivers include the necessary support; generic drivers often do not.

This guide fixes the driver layer, clears corrupted Night Light state, and checks the settings that silently disable it. The same steps repair [Night Light on other brands](/articles/how-to-fix-night-light-not-working-in-windows-11-24h2/), since the mechanism is identical across Windows.

## Why this happens

- **Generic display driver:** the Microsoft Basic Display Adapter does not support Night Light color controls.
- **Corrupted graphics driver:** a bad install breaks the color-temperature interface Windows uses.
- **Driver replaced by update:** Windows Update swaps in a driver version without Night Light support.
- **Corrupted CloudStore settings:** the cached Night Light state in the registry is stuck or invalid.
- **Location services off:** the sunset-to-sunrise schedule needs location to know when sunset is.
- **HDR enabled:** HDR mode can override or conflict with Night Light on some panels.
- **Custom color profile:** an ICC profile can block the Night Light color transform.
- **Group policy restriction:** managed devices may have Night Light disabled by policy.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Check the display driver in Device Manager

Confirming which driver is installed tells you immediately whether Night Light can work at all. The generic basic driver is the giveaway.

1. Open Device Manager and expand Display adapters.
2. If it shows Microsoft Basic Display Adapter, the real driver is missing.
3. Note the GPU model for the driver download step.
4. Check the driver date; very old drivers may predate Night Light support.
5. Continue to the driver reinstall below if anything looks wrong.

### Fix 2: Reinstall the Lenovo graphics driver

The definitive fix for greyed-out Night Light. Lenovo's validated driver restores the color controls Windows needs.

1. Go to Lenovo support and enter your model or serial number.
2. Download the latest graphics driver for your Windows version.
3. In Device Manager, uninstall the display adapter with driver removal checked.
4. Restart, then install the downloaded Lenovo graphics driver.
5. Restart again and check whether the Night Light toggle is active.

### Fix 3: Toggle and reschedule Night Light

Once the driver is healthy, resetting the Night Light configuration clears stuck states in the schedule and strength settings.

1. Open Settings, System, Display, and find Night light.
2. Turn it off, wait ten seconds, and turn it back on.
3. Drag the Strength slider and watch the screen for color change.
4. Set a manual schedule with specific on and off times for testing.
5. Confirm the screen warms at the scheduled time.

### Fix 4: Clear the corrupted CloudStore state

When the toggle works but schedules never fire, the cached settings are usually corrupt. Deleting the cache forces Windows to rebuild it cleanly.

1. Press Windows + R, type regedit, and press Enter.
2. Back up the registry with File, Export before making changes.
3. Go to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\Cache.
4. Find entries related to night light or blue light and delete that subkey.
5. Restart and reconfigure Night Light from scratch.

### Fix 5: Enable location services for sunset scheduling

The sunset-to-sunrise option is silently disabled without location access. If you prefer automatic scheduling, location must be on.

1. Open Settings, Privacy and security, Location.
2. Turn on Location services.
3. In Night light settings, choose Sunset to sunrise for the schedule.
4. Verify Windows detects your time zone correctly.
5. Test by setting a manual schedule first to confirm the feature works.

### Fix 6: Disable HDR and remove custom color profiles

HDR and custom ICC profiles both compete with Night Light for control of the display pipeline. Removing the competition lets Night Light apply cleanly.

1. In Display settings, turn off Use HDR if it is enabled.
2. Open Color Management from the Start menu.
3. On the Advanced tab, remove custom ICC profiles for the display.
4. Set the device profile back to the system default.
5. Toggle Night Light and confirm the warming effect appears.

### Fix 7: Check for Windows updates and policy blocks

A final pass ensures the OS side is current and no policy is suppressing the feature, particularly on work-issued Lenovo machines.

1. Run Windows Update and install all pending updates.
2. Restart and retest Night Light.
3. On managed devices, ask IT whether display policies restrict Night Light.
4. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current Night Light guidance.
5. If all else fails, test in a new user profile to rule out profile corruption.

## Closing

Night Light on Lenovo laptops is a driver feature wearing a settings disguise. Get Lenovo's graphics driver installed cleanly and the toggle comes back to life. Clear the cached state if schedules misbehave, and keep location on for automatic sunset timing. For related symptoms, see our guide on [Night Light issues on HP laptops](/articles/how-to-fix-night-light-not-working-on-hp-laptop/). Once Night Light is reliable, fine-tune the strength slider to a level that warms the screen without making color work impossible; most people land somewhere in the middle rather than at full intensity. If you do color-sensitive work in the evening, remember to toggle it off manually for that session instead of fighting the schedule. And if a future graphics driver update greys out the toggle again, you now know the drill: the Lenovo-validated graphics driver is the fix, not the settings page.
