---
title: "Night Light Not Working in Windows 11 24H2? 7 Fixes That Work"
slug: how-to-fix-night-light-not-working-in-windows-11-24h2
date: 2026-09-11
categories: ["drivers"]
tags: ["night light", "display", "windows 11", "24h2", "blue light"]
description: "Night Light greyed out or not working after the Windows 11 24H2 update? 7 fixes — registry repairs, graphics driver updates, and schedule fixes."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is Night Light greyed out after the 24H2 update?"
    a: "The 24H2 update commonly corrupts the Night Light registry keys or breaks the graphics driver's color-management handshake that Night Light depends on. A greyed-out toggle almost always means the underlying mechanism is broken, not just switched off — the fixes below repair the registry state and driver communication that the toggle needs."
  - q: "Does Night Light actually help with sleep?"
    a: "It helps somewhat. Night Light reduces blue light emission by shifting the display toward warmer colors, and blue light does suppress melatonin. But it's not a complete solution — screen brightness, content stimulation, and overall bedtime habits matter more. Think of Night Light as one useful piece of sleep hygiene, not a cure for late-night scrolling."
  - q: "Why does Night Light turn on at the wrong times?"
    a: "The schedule depends on your location settings for sunset-to-sunrise mode — if location is off or wrong, the timing breaks. Check Settings > Privacy & security > Location to make sure location access is enabled. Alternatively, switch to a manual schedule with explicit on/off times, which doesn't depend on location at all."
  - q: "Can I use f.lux instead of fixing Night Light?"
    a: "Yes — f.lux is a respected free alternative that many people prefer for its finer control. But it hooks into the same graphics driver color pipeline, so if Night Light is broken due to a driver problem, f.lux may misbehave too. Fix the underlying driver issue first, then choose whichever blue-light tool you prefer."
---

You toggle Night Light and nothing happens — or the toggle is greyed out entirely, mocking you from the Display settings page. After the Windows 11 24H2 update, Night Light failures are widespread: the warm color shift that used to kick in at sunset just... doesn't. Your eyes notice at 11 PM when the screen is still blasting cool blue-white light.

Night Light works by asking the graphics driver to shift the display's color temperature — which means it breaks when the 24H2 update corrupts the relevant registry keys or installs a graphics driver that mishandles the color request. The seven fixes below repair both layers. If your display has broader problems like flickering, our [screen flicker guide](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) covers those.

## Why this happens

- **24H2 corrupted the Night Light registry keys** — the CloudStore data Night Light depends on got mangled in the update.
- **The graphics driver mishandles color temperature** — the new driver fails the color-shift request silently.
- **Location services are off** — sunset-to-sunrise scheduling can't work without location data.
- **The schedule is misconfigured** — the toggle works but the automatic timing never triggers.
- **A third-party blue-light app conflicts** — f.lux or monitor utilities fight Night Light for color control.
- **Display color profile is corrupted** — a broken ICC profile blocks the temperature shift.
- **Fast Startup preserved a broken display state** — the color pipeline never reinitializes properly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle Night Light manually and check the schedule

First, establish what exactly is broken. Turn the Night Light toggle on manually in **Settings > System > Display** — if the screen warms immediately, the mechanism works and only the schedule is wrong. Then check the schedule settings: verify the on/off times, or switch from sunset-to-sunrise to a manual schedule. A surprising number of "not working" reports are just scheduling confusion.

1. Go to **Settings > System > Display** and click **Night light**.
2. Turn the main toggle **On** manually — does the screen warm up?
3. If yes, check **Schedule night light** — verify times or switch to manual hours.
4. If sunset-to-sunrise is wrong, enable **Location** in Privacy settings or use manual times.

### Fix 2: Reset the Night Light registry keys

The 24H2 update's most common Night Light damage is corrupted CloudStore registry data — this causes the greyed-out toggle. Deleting the corrupted keys forces Windows to rebuild them cleanly on next access. This is a safe, well-documented procedure: you're removing two specific subkeys under the CloudStore hive, and Windows regenerates them automatically. Back up the registry first if you're cautious.

1. Press **Windows + R**, type `regedit`, and press **Enter**.
2. Navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Cloud`.
3. Delete the subkeys named `default$windows.data.bluelightreduction.bluelightreductionstate` and `...settings` (the two bluelight entries).
4. Restart the laptop — Windows rebuilds the keys, and the toggle should work.

### Fix 3: Update the graphics driver

Night Light's color shift is executed by the graphics driver — if the 24H2-installed driver mishandles it, no registry fix will help. Download the graphics driver for your exact laptop model from the manufacturer's support site (not Windows Update's generic version) and install it clean. Intel, NVIDIA, and AMD all fixed 24H2 color-pipeline issues in driver releases following the update. For driver-level display problems generally, our [display driver guide](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) covers the technique.

1. Download the graphics driver for your exact model from the manufacturer's site.
2. Install it, choosing **Clean install** if the option appears.
3. Restart the laptop.
4. Toggle Night Light manually and check whether the screen warms.

### Fix 4: Check location settings for sunset scheduling

Sunset-to-sunrise mode needs your location — without it, the schedule silently never triggers. Go to **Settings > Privacy & security > Location**, make sure Location services are on, and verify the system can determine your location. If you'd rather not enable location, switch Night Light to a manual schedule with fixed times — it works identically without any location data.

1. Open **Settings > Privacy & security > Location**.
2. Turn **Location services** to **On**.
3. In Night light settings, confirm **Sunset to sunrise** is selected.
4. Alternatively, choose **Set hours** and enter your preferred on/off times.

### Fix 5: Remove conflicting blue-light software

Only one program can control display color temperature at a time. If f.lux, your monitor's utility, or the GPU control panel's own night mode is active, it can block or fight Night Light — sometimes greying out the toggle. Uninstall or fully disable third-party blue-light tools, restart, and test Night Light alone. You can always reinstall your preferred tool afterward once you've confirmed the mechanism works.

1. Check for **f.lux**, monitor utilities, or GPU night-mode features running.
2. Uninstall or completely disable them (not just pause — fully exit).
3. Restart the laptop.
4. Test the Night Light toggle in Display settings.

### Fix 6: Reset the display color profile

A corrupted ICC color profile can block the temperature shift Night Light requests. Open Color Management (search for it in Start), select your display, and check the profiles assigned. Remove any custom profile and revert to the system default (sRGB), then test Night Light. A clean default profile eliminates the profile layer as a suspect.

1. Search for **Color Management** in the Start menu and open it.
2. Select your laptop display in the Device dropdown.
3. Remove custom profiles and ensure the default **sRGB** profile is set.
4. Restart and test the Night Light toggle.

### Fix 7: Do a full shutdown to reset the display pipeline

Fast Startup can preserve a broken color-pipeline state across restarts — the graphics driver's color management never truly reinitializes. A full shutdown (Shift + Shut down) forces the entire display stack to cold-boot. This is particularly effective when Night Light broke suddenly without an update, suggesting a wedged state rather than corruption. General display troubleshooting background is at [Windows support](https://support.microsoft.com/en-us/windows).

1. Hold **Shift** while clicking **Start > Power > Shut down**.
2. Wait 60 seconds with the laptop fully off.
3. Power on and log into Windows.
4. Toggle Night Light and verify the warm shift applies.

## Closing

Night Light failing after 24H2 is a registry-or-driver problem, not a missing feature — the greyed-out toggle is Windows telling you the mechanism underneath is broken. The registry reset in Fix 2 handles the update's corruption; the driver reinstall in Fix 3 handles the color pipeline. One of the two restores that warm evening glow for nearly everyone.
