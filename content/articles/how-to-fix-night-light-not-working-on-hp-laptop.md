---
title: "How to Fix Night Light Not Working on an HP Laptop"
slug: how-to-fix-night-light-not-working-on-hp-laptop
date: 2026-09-12
categories: ["drivers"]
tags: ["night light not working", "hp laptop", "windows night light", "display driver", "blue light filter"]
description: "Night Light stuck off or greyed out on your HP laptop? These seven fixes — from graphics driver repair to registry resets — restore the warm display schedule."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why is the Night Light toggle greyed out on my HP laptop?"
    a: "A greyed-out toggle almost always means the Night Light settings cache in the registry is corrupt, or HP Display Manager / OMEN Gaming Hub has seized color control. Delete the $$windows.data.bluelightreduction keys under the CloudStore registry path and restart, and set HP's color tools to their defaults. A corrupt graphics driver can also cause it, so reinstall the HP graphics driver if the registry reset does not help."
  - q: "Does Night Light need location services to work?"
    a: "Only for the 'Sunset to sunrise' schedule, which calculates local sunset from your location. If location services are off, that schedule silently never triggers. Either enable location services or switch to 'Set hours' with a manual on/off time. The manual on/off toggle itself never needs location."
  - q: "Can I use f.lux and Night Light together?"
    a: "You should not. Both programs adjust the display's gamma ramps, and running them together causes flickering, fighting over color temperature, and sometimes disables Night Light entirely. Pick one: uninstall f.lux to use Night Light, or leave Night Light permanently off and use f.lux. Most users find Night Light sufficient once it works."
  - q: "Why does Night Light turn on but the screen flickers?"
    a: "Flicker usually means two color-management systems fighting — HP Display Manager, OMEN Gaming Hub, f.lux, or the monitor's own low-blue-light mode running alongside Night Light. Turn the competing tools off one by one. If flicker persists with everything else disabled, reinstall the graphics driver, since a damaged color pipeline in the driver can also produce unstable tinting."
---

Night Light is supposed to be simple: a warm tint that fades in on schedule. When it stops working on an HP laptop, the toggle is usually greyed out in Settings, the schedule never triggers, or the screen flickers between warm and cool without settling. Because Night Light is implemented in the display driver pipeline rather than as a simple overlay, 'not working' almost always means the graphics driver or its color pipeline is in a bad state.

HP laptops add wrinkles: HP Display Manager and OMEN Gaming Hub can fight Windows over color temperature, and HP's customized Intel/AMD/NVIDIA graphics drivers sometimes lag behind Windows feature updates that change how Night Light hooks into the compositor. The result is a feature that worked last month and silently died after an update.

Before diving in, confirm your display driver is healthy — our guide to [display brightness problems](/articles/how-to-fix-display-brightness-not-working-in-windows-11-24h2/) covers the adjacent driver issues, and [checking your driver version](/articles/how-to-check-driver-version-in-device-manager-on-windows-11/) helps you know whether an update broke things. Now the fixes, in order.

## Why this happens

- **Corrupt graphics driver color pipeline** — Night Light is applied by the GPU driver; a damaged install breaks the tint while everything else looks normal.
- **HP Display Manager / OMEN Hub conflict** — HP's color tools can override or disable Windows' Night Light control silently.
- **Night Light registry state corruption** — The CloudStore registry cache for Night Light settings can corrupt, greying out the toggle permanently.
- **Location services disabled** — The sunset-to-sunrise schedule needs location; with it off, scheduled Night Light never triggers.
- **Outdated HP-customized graphics driver** — HP's validated drivers sometimes predate the Windows build's Night Light expectations after a feature update.
- **Fast Startup hibernation state** — A stale hibernated driver state can leave Night Light stuck off until a true restart.
- **Third-party blue-light apps conflicting** — f.lux and similar tools hook the same gamma ramps and can disable Night Light.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a full restart (not shutdown)

Fast Startup means Shutdown is really hibernation. A true restart reloads the graphics driver and often un-sticks Night Light by itself.

1. Click Start > Power, then hold **Shift** and click **Restart** — or simply choose Restart instead of Shut down.
2. After reboot, open Settings > System > Display > Night light.
3. Toggle it on manually and check whether the tint applies.
4. If it works now, consider disabling Fast Startup later to prevent recurrence.

### Fix 2: Update or reinstall the graphics driver

Because Night Light lives in the driver, this is the highest-yield fix. Use HP's driver for your exact model first.

1. Open Device Manager > Display adapters, note your GPU (Intel UHD/Iris Xe, AMD Radeon, or NVIDIA).
2. Download the latest graphics driver for your exact HP model from HP's official support site ([support.hp.com](https://support.hp.com/us-en)).
3. In Device Manager, right-click the GPU > Uninstall device (tick 'delete driver' if offered), then install the HP driver.
4. Restart and test Night Light. If HP's driver is old, the generic Intel/AMD/NVIDIA driver is a reasonable fallback.

### Fix 3: Reset the Night Light registry state

A corrupted CloudStore entry greys out the toggle no matter what the driver does. Deleting the cached state forces Windows to rebuild it.

1. Press Win + R, type `regedit`, and go to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\Cache\DefaultAccount`.
2. Expand it and delete the two subkeys starting with `$$windows.data.bluelightreduction` (one for settings, one for state).
3. Restart the PC.
4. Reopen Settings > Display — the Night Light toggle should be active again. Reconfigure your schedule.

### Fix 4: Check HP Display Manager and OMEN Gaming Hub

HP's utilities can seize color control. If either is installed, make sure it is not overriding Night Light.

1. Open HP Display Manager (or OMEN Gaming Hub > Display).
2. Look for Low Blue Light, Night Mode, or color temperature settings and set them to Off or default.
3. In OMEN Hub, check that no display profile is forcing a color mode.
4. Return to Windows Settings and toggle Night Light on — it should now respond.

### Fix 5: Enable location services for the schedule

'Sunset to sunrise' scheduling silently does nothing when location is off. Manual schedules do not need it, but the automatic one does.

1. Open Settings > Privacy & security > Location.
2. Turn on **Location services**.
3. Set Night Light schedule to **Sunset to sunrise** and confirm your time zone is correct.
4. If you prefer location off, use **Set hours** with a manual schedule instead.

### Fix 6: Remove conflicting blue-light software

f.lux, SunsetScreen, and monitor-vendor utilities all fight Night Light for the same gamma ramps.

1. Uninstall f.lux or similar apps via Settings > Apps.
2. Check your monitor's on-screen menu for a built-in Low Blue Light mode and turn it off while testing.
3. Restart and toggle Night Light.
4. If you prefer f.lux, keep Night Light off permanently — running both causes flicker.

### Fix 7: Create a new user profile as a test

If Night Light works on a fresh profile, your main profile's settings cache is corrupt beyond the registry fix — migrating is faster than further surgery.

1. Open Settings > Accounts > Other users > Add account (choose 'I don't have sign-in info' > 'Add a user without a Microsoft account').
2. Sign into the new account and test Night Light.
3. If it works there, move your files to the new profile and make it your daily account.
4. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document profile-repair steps if you want to attempt a repair instead.

## Closing

Night Light failures on HP laptops are driver and state problems, not hardware: the graphics driver's color pipeline, HP's display utilities, or a corrupted settings cache. The driver reinstall and the CloudStore registry reset resolve the overwhelming majority of cases, and the manual schedule option sidesteps the location dependency entirely.
