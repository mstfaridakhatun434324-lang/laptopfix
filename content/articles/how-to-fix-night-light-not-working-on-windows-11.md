---
title: "Repair Night Light That Refuses to Turn On"
slug: how-to-fix-night-light-not-working-on-windows-11
date: 2026-09-07
categories: ["drivers"]
tags: ["night light", "blue light", "display", "windows 11", "troubleshooting"]
description: "Night Light not working on Windows 11? Fix the greyed-out toggle, broken schedule, and missing warm tint with these repairs."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-on-windows-11.webp"
faqs:
  - q: "Why is Night Light greyed out in Windows 11?"
    a: "The toggle greys out when the display driver does not report color-temperature control support, or when a group policy or registry setting has disabled the feature. Reinstalling the display driver and checking the relevant registry keys usually restores the toggle."
  - q: "Why does Night Light turn on but the screen does not change color?"
    a: "The schedule or toggle is active but the color transform is not being applied, usually because the display driver is mishandling the gamma ramp. Updating the display driver or toggling the feature off and on forces Windows to reapply the color profile."
  - q: "Can HDR break Night Light?"
    a: "Yes. On some systems, enabling HDR disables the Night Light color transform because the two features conflict in the display pipeline. Turning off HDR in Settings lets Night Light apply its warm tint normally. Some monitors also have their own blue-light mode that conflicts; disable one or the other."
  - q: "Why does my Night Light schedule never trigger?"
    a: "A corrupted schedule in the registry or a conflicting power state can prevent the timed activation. Deleting the Night Light schedule registry keys and recreating the schedule forces Windows to rebuild the trigger cleanly. Back up the registry key before deleting anything, so you can restore it if needed."
---

Night Light is one of those features you do not appreciate until it breaks. One evening you notice the screen never warmed up, and from then on every night is harsh blue-white. The toggle may be greyed out, the schedule may silently do nothing, or the switch flips on with zero visible change to the display.

Night Light works by applying a color-temperature transform through the display driver — it shifts the gamma ramp toward warm tones. That means it depends on the driver cooperating. Display driver updates, HDR settings, and corrupted schedule data are the three usual suspects, and each produces a distinct symptom.

These fixes are ordered by likelihood. The first two solve the greyed-out toggle; the middle ones fix the schedule; the last ones handle the 'on but no effect' case.

Night Light's schedule data lives in a notoriously fragile registry hive, and it corrupts more often than any other display feature's settings. If your Night Light breaks on a schedule — works manually but never automatically — skip straight to the schedule rebuild fix; it is the targeted cure. The full toggle-greyed-out case, by contrast, is almost always the display driver.

## Why this happens

- **Display driver not supporting the color transform:** A generic or corrupted driver may not expose the gamma-ramp control Night Light needs.
- **Greyed-out toggle from policy or registry:** Group policy or a stuck registry value can disable the feature at the system level.
- **HDR conflicting with the color pipeline:** HDR mode bypasses the color transform path Night Light relies on.
- **Corrupted schedule registry data:** The sunrise/sunset or custom schedule can corrupt, leaving the timer firing into the void.
- **Location services disabled:** The automatic sunset-to-sunrise schedule needs your location; without it, the schedule never triggers.
- **Graphics control panel overriding color:** Intel, NVIDIA, or AMD color settings can override Windows' gamma adjustments.
- **Fast Startup preserving a bad state:** A corrupted display state can survive reboots via Fast Startup's hibernation file.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle Night Light and reset its strength

Sometimes the feature is simply in a confused state. A full off-on cycle with a strength reset clears it.

1. Open **Settings > System > Display > Night light**.
2. Turn the toggle **Off**, wait ten seconds, then turn it **On**.
3. Drag the **Strength** slider to maximum and check whether the screen warms visibly.
4. If the tint appears at max strength, lower it to your preference — the feature was working, just set too subtly. If the display also flickers while adjusting color, check the [screen flickering guide](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/).

### Fix 2: Reinstall the display driver

The color transform runs through the GPU driver. A fresh driver restores the gamma-ramp path Night Light depends on.

1. Open **Device Manager > Display adapters**, right-click your GPU, and choose **Uninstall device**.
2. Restart and let Windows reinstall the driver.
3. Return to **Settings > System > Display > Night light** and test the toggle.
4. If it works now, install the latest driver from your vendor to stay current.

### Fix 3: Turn off HDR

HDR and Night Light fight over the same display pipeline on many laptops, and HDR usually wins.

1. Open **Settings > System > Display** and find the **HDR** toggle.
2. Turn **HDR** off for the built-in display.
3. Enable Night Light and check for the warm tint.
4. If you need HDR for specific content, toggle it per-session rather than leaving it always on.

### Fix 4: Rebuild the Night Light schedule

A corrupted schedule never fires. Deleting it forces Windows to build a fresh one.

1. Press **Win + R**, type **regedit**, and navigate to **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current**.
2. Find the Night Light related subkeys (names containing **nightlight** or **bluelightreduction**) and delete them.
3. Restart, then open Night Light settings and set your schedule to **Sunset to sunrise** or custom hours.
4. Enable **Location services** in **Settings > Privacy & security > Location** if using the automatic schedule.

### Fix 5: Check graphics vendor color settings

Vendor color controls can override the Windows gamma ramp, silently canceling the Night Light tint.

1. Open the Intel Graphics Command Center, NVIDIA Control Panel, or AMD Software.
2. Look for color, display, or video color settings and reset them to defaults.
3. Disable any **night mode** or **blue light** feature in the vendor software to avoid conflicts.
4. Return to Windows Night Light and verify the tint now applies.

### Fix 6: Disable Fast Startup

Fast Startup can preserve a corrupted display state across reboots, making the problem look permanent.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup**, save, and perform a full shutdown.
4. Power on fresh and test Night Light. Microsoft documents display features on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Create a new user profile as a test

If Night Light works in a new profile, your user registry hive is corrupt and a profile rebuild is cleaner than surgery.

1. Open **Settings > Accounts > Other users** and add a new local user.
2. Sign in as the new user and test Night Light.
3. If it works there, migrate your files to the new profile.
4. This is a last resort, but it definitively separates user corruption from system problems.

### Fix 8: Repair Windows with an in-place upgrade

When the feature is broken at the system level across all user profiles, an in-place repair reinstalls Windows while keeping everything.

1. Download the Windows 11 ISO from the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run **setup.exe**, and choose **Keep personal files and apps**.
3. Let the repair complete — it refreshes system components including the display stack.
4. Test Night Light afterward; this resolves corruption no targeted fix can reach.

## Closing

Night Light failures come down to three things: a driver that will not apply the color transform, HDR hogging the display pipeline, or a corrupted schedule. Fix those in order and the warm evening tint returns. The feature itself is simple — it just needs a cooperative driver and a clean schedule to do its job. For general driver hygiene behind display features, the [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/) covers the standard process.
