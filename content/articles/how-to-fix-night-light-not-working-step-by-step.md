---
title: "How to Fix Night Light Not Working — Step by Step"
slug: how-to-fix-night-light-not-working-step-by-step
date: 2026-10-01
categories: ["drivers"]
tags: ["night light not working", "windows 11", "windows 10", "blue light filter", "display fix"]
description: "Night Light not working, greyed out, or not turning on? A universal step-by-step repair: driver fixes, registry reset, schedule checks, and conflicts."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-step-by-step.webp"
faqs:
  - q: "Why is Night Light greyed out and unclickable?"
    a: "A greyed-out toggle means the Night Light settings cache in the registry (the CloudStore bluelightreduction keys) is corrupt, or a conflicting program has seized color control. Deleting those registry keys and restarting restores the toggle. If it greys out again immediately, a corrupt graphics driver or a tool like f.lux is re-breaking it — reinstall the GPU driver and remove competing color apps."
  - q: "Does Night Light actually help with sleep?"
    a: "Research suggests reducing blue light exposure in the evening supports natural melatonin production, though the effect size is debated and screen brightness and content matter too. Night Light is a reasonable, zero-cost part of evening screen hygiene — dim the display as well, since total light exposure matters more than color temperature alone. It is not a medical treatment for sleep disorders."
  - q: "Why does Night Light turn off by itself?"
    a: "Usually the schedule: a sunset-to-sunrise schedule with location off never fires correctly, or manual hours were set unintentionally. Also check Fast Startup — hibernated driver states can drop the tint after sleep. Less commonly, a GPU driver crash resets the color pipeline and Night Light with it; if the tint dies alongside display flicker, suspect the graphics driver."
  - q: "Can I schedule Night Light without enabling location?"
    a: "Yes — use 'Set hours' instead of 'Sunset to sunrise.' The sunset schedule needs your location to compute local sunset; manual hours need nothing. Enter your preferred on/off times and Night Light fires reliably without location services. This is also the workaround on desktops without location hardware and for users who keep location off for privacy."
---

Night Light not working takes several forms: the toggle is greyed out, the schedule never fires, the tint turns on but flickers, or it works manually but ignores sunset times. Because Night Light is rendered through the GPU driver's color pipeline — not as a simple screen overlay — every one of these symptoms traces back to the driver, its settings cache, or a conflicting color tool. The hardware is never at fault.

This is the universal step-by-step edition: it works on Windows 10 and 11, any laptop brand. Brand-specific wrinkles (HP's Display Manager, ASUS utilities) are covered in our companion guides, including the [HP Night Light fix](/articles/how-to-fix-night-light-not-working-on-hp-laptop/). If the underlying [display brightness controls](/articles/how-to-fix-display-brightness-not-working-in-windows-11-24h2/) are also broken, fix the graphics driver first — Night Light depends on it.

Follow the steps in order. Each is quick, and the sequence is arranged so the most common causes come first.

## Why this happens

- **Graphics driver color pipeline broken** — Night Light is applied by the GPU driver; corruption kills the tint specifically.
- **Night Light registry cache corrupt** — The CloudStore cache greys out the toggle permanently until reset.
- **Conflicting color software** — f.lux, vendor low-blue-light modes, and GPU control panels fight Night Light.
- **Location off for sunset schedule** — Sunset-to-sunrise needs location services; without it the schedule never fires.
- **Fast Startup stale driver state** — Hibernated graphics state can wedge Night Light off across 'shutdowns'.
- **Wrong color profile / HDR** — Custom ICC profiles and HDR can override or wash out the Night Light tint.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart properly and toggle manually

Clear any wedged state with a true restart, then test the manual toggle.

1. Choose **Restart** (not Shut down) from the Start menu.
2. Open Settings > System > Display > **Night light**.
3. Turn the toggle on manually and drag the Strength slider — confirm the tint visibly applies.
4. If manual works but the schedule does not, skip to Fix 5.

### Fix 2: Update or reinstall the graphics driver

The highest-yield fix: Night Light lives in the driver.

Match the driver source to your machine: laptop makers validate graphics drivers against their specific panels, and the maker's driver is the safest first try. If the maker's driver is years old and the problem started with a Windows feature update, the chip vendor's current generic driver (Intel/AMD/NVIDIA) is the better second attempt — newer color-pipeline code with the same Night Light hooks.

1. Open Device Manager > Display adapters and note your GPU.
2. Download the latest graphics driver from the laptop maker's support site (or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) / [AMD](https://www.amd.com/en/support/download/drivers.html) / [NVIDIA](https://www.nvidia.com/Download/index.aspx) for the chip).
3. Uninstall the current GPU driver (tick 'delete driver'), install the fresh package, restart.
4. Test the Night Light toggle again.

### Fix 3: Reset the Night Light registry cache

The definitive fix for a permanently greyed-out toggle.

Export the CloudStore key before deleting it (right-click > Export) so you can restore it if needed — though in practice a rebuilt cache is always healthier than a corrupt one. If the bluelightreduction keys regenerate as corrupt again after a reboot, a startup program is rewriting them; clean-boot to find it.

1. Open regedit and navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\Cache\DefaultAccount`.
2. Delete the subkeys beginning with `$$windows.data.bluelightreduction` (there are usually two).
3. Restart the PC.
4. Reopen Display settings — the toggle should be live. Reconfigure your schedule and strength.

### Fix 4: Remove conflicting color tools

Two programs fighting over gamma ramps means neither works right.

1. Uninstall f.lux / SunsetScreen or similar blue-light apps.
2. Turn off the monitor's built-in Low Blue Light mode in its OSD while testing.
3. Reset GPU control panel color settings (NVIDIA Control Panel / AMD Adrenalin / Intel Graphics) to defaults.
4. Restart and test Night Light alone.

### Fix 5: Fix the schedule: location or manual hours

'Never turns on by itself' is a scheduling problem, not a Night Light problem.

1. For **Sunset to sunrise**: Settings > Privacy & security > Location > turn **Location services** on; verify time zone is correct.
2. Alternatively, choose **Set hours** and enter manual on/off times — no location needed.
3. Confirm the schedule shows the correct next-trigger time under the Night light settings.
4. Wait for (or temporarily set) a trigger time a few minutes out to verify it fires.

### Fix 6: Check HDR and color profiles

HDR and custom ICC profiles can override the Night Light tint.

Remember that HDR and Night Light are philosophically opposed: HDR wants maximum dynamic range and color volume, Night Light wants to squash blue. Most panels cannot do both at once, so Windows prioritizes HDR. If you need Night Light for evening use, consider leaving HDR off and enabling it only for HDR content — a small inconvenience for reliable warm evenings.

1. Settings > System > Display > **HDR**: turn it off temporarily and test Night Light.
2. Search Start for **Color Management** > check the display's profile — remove custom ICC profiles added by calibration tools while testing.
3. If Night Light works with HDR off, the two are conflicting on your panel — use one or the other.
4. Also test with [screen flicker fixes](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) if the tint flickers rather than staying steady.

### Fix 7: Test on a new user profile

Isolates per-user settings corruption as the last software variable.

1. Settings > Accounts > Other users > add a local account.
2. Sign in and test Night Light there.
3. If it works, migrate to the new profile — your old profile's settings cache is corrupt beyond practical repair.
4. Microsoft's official display-settings support documentation covers profile-level troubleshooting if you prefer to repair.

## Closing

Night Light's step-by-step repair is short because the suspect list is short: the graphics driver's color pipeline, the CloudStore settings cache, a conflicting color tool, or the schedule's location dependency. The driver reinstall and registry reset in Fixes 2–3 resolve the large majority of cases on any brand and either Windows version.
