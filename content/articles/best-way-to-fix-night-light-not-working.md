---
title: "The Best Way to Fix Night Light Not Working in Windows"
slug: best-way-to-fix-night-light-not-working
date: 2026-09-04
categories: ["drivers"]
tags: ["night light not working", "blue light filter", "night light greyed out", "display driver", "windows 11"]
description: "Night Light not working or greyed out? Fix it the right way — graphics driver, registry, and location settings — in the order that actually works."
thumbnail: "/images/thumbs/best-way-to-fix-night-light-not-working.webp"
faqs:
  - q: "Why is Night Light greyed out in Settings?"
    a: "A greyed-out Night Light toggle almost always means the graphics driver is not reporting display color capabilities to Windows — usually because a generic Microsoft Basic Display Adapter is in use instead of the proper GPU driver. Less commonly, a corrupted Night Light registry key or a group policy disables it. The fix path is reinstalling the manufacturer's graphics driver first; if the toggle is still greyed out with a correct driver, the registry repair in this guide restores it."
  - q: "Does Night Light need location services to work?"
    a: "Only for the automatic sunset-to-sunrise schedule. Night Light itself — the manual toggle and custom schedule — works fine without location. If you want the sunset-to-sunrise option, enable location services and set a default location. Many users who think Night Light is broken actually just have the schedule set to sunset-to-sunrise with location disabled, so it never triggers. Switching to a manual time schedule bypasses the location requirement entirely."
  - q: "Why does Night Light turn off by itself?"
    a: "The usual cause is a conflicting schedule — Night Light turning off at the scheduled end time while you expected it on, or a second schedule from a manufacturer utility fighting the Windows one. Fullscreen games and some video apps also disable color filters. Check the Night Light schedule in Settings, then Display, then Night Light, and look for manufacturer display utilities with their own blue-light features. Having two systems fight over color temperature produces exactly this on-off behavior."
  - q: "Is Night Light the same as the blue light filter in my laptop's utility?"
    a: "No, though they do the same job. Night Light is Windows' built-in color-temperature filter. Manufacturer utilities (Lenovo Vantage Eye Care, ASUS Splendid, Dell CinemaColor) have their own independent filters that adjust the display through the GPU driver. Running both simultaneously can double-apply the effect or cause flickering. Pick one system and disable the other — and when troubleshooting Night Light, disable the manufacturer filter first to rule out conflicts."
---

Night Light is one of those features you do not appreciate until it breaks — then every evening at the screen feels harsher. The toggle is greyed out, or it turns on but nothing changes, or it worked yesterday and does nothing today. The best way to fix it is not random toggling: it is a specific sequence that addresses the three real causes — graphics driver, registry state, and schedule/location configuration — in order of likelihood.

Night Light depends on the graphics driver exposing color-calibration capabilities to Windows. That dependency is why driver problems are the root cause of most Night Light failures, and why the fix starts there rather than in Settings.

## Why this happens

- **Generic graphics driver in use:** The most common cause. Microsoft Basic Display Adapter does not report the color capabilities Night Light needs, so Windows greys out the toggle.
- **Corrupted Night Light registry state:** The feature's settings live in the registry. Corrupted values there can break the toggle or make it appear to work while changing nothing.
- **Location disabled with sunset schedule:** The sunset-to-sunrise schedule needs location. Without it, Night Light never triggers and looks broken.
- **Manufacturer blue-light filter conflict:** OEM utilities with their own eye-care modes fight Night Light for control of display color temperature.
- **Graphics driver update resetting color pipeline:** Driver updates can temporarily break the color-calibration path Night Light depends on.
- **Group policy or registry disable:** Some managed or debloated systems have Night Light disabled by policy, greying out the toggle permanently.
- **External monitor limitations:** Night Light applies per-display, and some external monitor/driver combinations do not support the color transform.
- **Fullscreen app overrides:** Games and video players that take exclusive fullscreen control can bypass or disable the color filter while running.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the graphics driver — the root cause most of the time

If Night Light is greyed out, start here. Do not touch the registry yet.

1. Open **Device Manager → Display adapters**. If you see **Microsoft Basic Display Adapter**, you have found the problem — install the real GPU driver now.
2. Download the graphics driver for your exact model from the manufacturer's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install it, restart, and check **Settings → System → Display → Night Light**. The toggle should be active.
4. Even if the driver looks correct, a clean reinstall fixes cases where the driver's color pipeline is corrupted — use **Display Driver Uninstaller (DDU)** in Safe Mode for a thorough clean before reinstalling. If the adapter is missing entirely, see our [display adapter recovery guide](/articles/best-way-to-fix-display-adapter-missing/).

### Fix 2: Repair the Night Light registry state

For toggles that do nothing, or settings that will not stick.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Cloud`.
2. Find the keys related to Night Light (they contain `nightlight` in the data blobs under the CloudStore hierarchy). The reliable repair is to delete the corrupted Night Light state: export the key as backup first, then delete the Night Light-related entries.
3. Restart the laptop. Windows rebuilds the Night Light registry state from defaults on next launch of the Settings page.
4. Reconfigure your Night Light schedule from scratch. If the toggle now works, the registry was the problem. (Alternative: create a new Windows user profile — Night Light state is per-user, so a fresh profile with working Night Light confirms registry corruption in the old one.)

### Fix 3: Fix the schedule and location settings

For Night Light that never turns on automatically.

1. Go to **Settings → System → Display → Night Light → Schedule**. If it is set to **Sunset to sunrise**, either enable location services (**Settings → Privacy & security → Location**) or switch to **Set hours** with manual times.
2. For manual hours, set a start time (e.g., 9:00 PM) and end time (e.g., 7:00 AM) and verify the **Turn on now** button works — this tests the filter independent of the schedule.
3. Drag the **Strength** slider while Night Light is on. If the screen does not change at all, the problem is the driver/color pipeline (Fix 1), not the schedule.
4. Check that the schedule's end time is not immediately after the start time — a common misconfiguration where users set 9 PM to 9 PM and Night Light appears to never activate.

### Fix 4: Eliminate manufacturer filter conflicts

Two color filters fighting looks exactly like a broken Night Light.

1. Open your manufacturer's utility (Lenovo Vantage, MyASUS, Dell CinemaColor, HP Display Control) and look for eye-care, blue-light, or color-temperature features. Disable them.
2. Check the GPU control panel too — Intel Graphics Command Center and NVIDIA Control Panel both have color settings that can override Windows.
3. With all third-party filters off, test Night Light alone. If it works now, pick one system permanently: Night Light for simplicity, or the manufacturer filter if you prefer its scheduling.
4. Also check **Settings → Accessibility → Color filters** — a different Windows feature that can interact with Night Light unexpectedly. Display-color issues more broadly connect to our [HDR troubleshooting guide](/articles/how-to-fix-hdr-not-working-on-laptop-in-windows-11-24h2/).

### Fix 5: Check policies and the color pipeline

For systems where the toggle is greyed out despite a correct driver.

1. Press **Win + R**, type `gpedit.msc` (Pro editions), and check **User Configuration → Administrative Templates** for anything disabling Night Light or display color features.
2. In the registry, check `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore` for policy-pushed Night Light disables — debloating scripts sometimes add these.
3. Run `sfc /scannow` in an elevated Command Prompt. Corrupted system files in the display/color pipeline are rare but real, and SFC repairs them.
4. Test Night Light on the built-in display with no external monitors connected. If it works there but not on the external monitor, the limitation is the external display's driver path — use the monitor's own low-blue-light mode instead.

### Fix 6: Update everything display-related

The comprehensive pass for stubborn cases.

1. Update the **graphics driver** to the latest manufacturer version (not just a working version — newer releases fix color-pipeline bugs).
2. Update the **chipset driver** and **BIOS**. Display color management touches firmware more than people expect, and BIOS updates have fixed Night Light in several manufacturers' release notes.
3. Install all pending **Windows updates** — Night Light itself has received bug fixes in cumulative updates.
4. After updating, re-verify Fixes 1–3 in order. Updates can re-break the registry state or reset the schedule, so the sequence matters more than any single step.

## Closing

Night Light failures are almost never about Night Light itself — they are about the graphics driver not exposing color capabilities, a corrupted per-user registry state, or a schedule fighting its own configuration. Fix the driver first, repair the registry second, and sort the schedule third. That order resolves essentially every case, and it takes less time than the random toggling most people try first.
