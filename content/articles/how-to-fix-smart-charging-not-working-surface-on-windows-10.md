---
title: "How to Fix Smart Charging Not Working on Surface (Windows 10)"
slug: how-to-fix-smart-charging-not-working-surface-on-windows-10
date: 2026-10-07
categories: ["battery"]
tags: ["surface", "smart charging", "windows 10", "battery limit"]
description: "Surface Smart charging stuck off or on? 7 fixes for Windows 10 — UEFI settings, driver resets, and firmware updates that restore it."
thumbnail: "/images/thumbs/how-to-fix-smart-charging-not-working-surface-on-windows-10.webp"
faqs:
  - q: "What is Smart charging on a Surface?"
    a: "It's a battery-longevity feature that pauses charging at 80 percent (or a similar limit) when the device detects it's plugged in for long periods. Unlike a manual limit, it's adaptive — it learns your routine and only kicks in when it thinks the Surface will stay docked, which is why its behavior can seem inconsistent."
  - q: "Why is Smart charging always on and I can't turn it off?"
    a: "On some Surface models with Windows 10, the toggle lives in the UEFI firmware settings rather than Windows, and older firmware versions had a bug where the setting wouldn't stick. Updating the Surface firmware and toggling it in UEFI usually resolves it."
  - q: "Can I force my Surface to charge to 100%?"
    a: "Yes. Fully shutting down and charging while powered off bypasses Smart charging on most models. For a permanent change, disable it in UEFI settings (Fix 3) or the Surface app, then charge uninterrupted to 100 percent."
  - q: "Is Smart charging bad for my battery?"
    a: "The opposite — it's protective. Keeping a lithium battery below full charge while docked dramatically slows degradation. Only disable it if you genuinely need maximum runtime away from power regularly."
---
Your Surface is plugged in, but it stops at 80 percent and refuses to go further — or the opposite: Smart charging is supposed to be protecting your battery, but the device charges straight to 100 every time and the toggle does nothing. Either way, the feature isn't behaving, and on Windows 10 Surface devices the controls are scattered across three different places.

Smart charging is genuinely useful — it can add years to a battery's life — but only when it works predictably. Let's get it under your control.

## Why this happens

- **The toggle lives in UEFI, not Windows.** On many Surface models the Smart charging switch is a firmware setting, so flipping things in Windows Settings does nothing and users think it's broken.
- **Outdated Surface firmware.** Early Windows 10-era firmware had Smart charging bugs where the setting wouldn't apply or the 80 percent cap engaged permanently.
- **The Surface System Aggregator driver is corrupt.** This driver manages the battery and charging hardware; when it misbehaves, Smart charging commands never reach the hardware.
- **Windows 10 is missing the Surface app controls.** The modern Surface app exposes Smart charging toggles that older Windows 10 builds lack, leaving users with no visible control.
- **A third-party battery tool is conflicting.** Utilities that manage charge limits can fight the firmware-level Smart charging and produce unpredictable caps.
- **The battery's charge controller is stuck.** The embedded controller can latch the 80 percent limit on even after the feature is disabled, until it's reset.
- **Fast Startup is caching a stale power state.** Windows 10's hybrid shutdown can preserve a stuck charging state across reboots.

## How to fix it

Work through these in order. Fix 3 (the UEFI toggle) is the one most people miss.

### Fix 1: Check the Surface app for the toggle

Start with the visible controls before diving into firmware.

1. Open the **Surface** app from the Start menu (install it from the Microsoft Store if it's missing).
2. Look for **Battery** or **Smart charging** settings — on supported models there's a straightforward on/off toggle.
3. If Smart charging is on but you want full charges, turn it off, then unplug and replug the charger.
4. Charge uninterrupted and watch whether it passes 80 percent. If the Surface app has no such section, your model controls it via UEFI — move to Fix 3.

### Fix 2: Update Surface firmware and drivers

Firmware bugs are the leading cause of stuck Smart charging on Windows 10 Surfaces.

1. Go to **Settings** > **Update & Security** > **Windows Update** and install everything, including **Optional updates** where Surface firmware appears.
2. Then open the **Surface** app and check for firmware updates there too.
3. For manual control, download the driver and firmware pack for your exact Surface model from Microsoft's [Surface support pages](https://support.microsoft.com/en-us/windows) and install it.
4. Restart fully (hold **Shift** while clicking **Shut down**, then power on) and test charging behavior.

### Fix 3: Toggle Smart charging in UEFI settings

This is the master switch that overrides everything in Windows.

1. Shut the Surface down completely.
2. Press and hold **Volume Up**, then press and release the **Power** button. Keep holding Volume Up until the UEFI screen appears.
3. Navigate to **Boot configuration** or **Battery** (location varies by model) and find the **Smart charging** or battery limit setting.
4. Set it to your preference, save, and exit. Charge the device and confirm the behavior changed. If UEFI has no such option, your model manages it purely through drivers — continue below.

### Fix 4: Reinstall the Surface battery drivers

When the System Aggregator driver corrupts, charging commands go nowhere.

1. Open **Device Manager** (**Win + X**), expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft Surface ACPI-Compliant Control Method Battery** if present.
3. Expand **Firmware** and **System devices** — right-click any **Surface System Aggregator** entry and choose **Update driver** > **Search automatically**.
4. Shut down fully, wait ten seconds, power on, and let Windows reinstall everything. Test with a full charge cycle.

### Fix 5: Reset the embedded controller

A latched charge limit needs a hardware-level reset that software toggles can't clear.

1. Shut down the Surface and unplug the charger.
2. Press and hold the power button for a full 30 seconds, then release.
3. Wait a minute, reconnect the charger (leave the Surface off), and let it charge for 30 minutes.
4. Power on and check whether the 80 percent cap still engages. This reset also helps when the battery percentage itself is misbehaving — see our guide to [calibrating laptop batteries](/articles/how-to-calibrate-laptop-battery-windows-11/) for the follow-up procedure.

### Fix 6: Disable Fast Startup

Hybrid shutdown can preserve the stuck charging state across every "restart."

1. Open **Control Panel** > **Hardware and Sound** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup**, save, and shut down fully.
4. Power on and test. You can re-enable Fast Startup later once Smart charging behaves — but many Surface owners leave it off permanently for fewer power quirks.

### Fix 7: Remove conflicting battery utilities

Two captains can't steer the charge limit.

1. Open **Settings** > **Apps** and uninstall any third-party battery managers or charge limiters.
2. Check **Task Manager** > **Startup** for leftover battery helpers and disable them.
3. Restart, set your Smart charging preference in exactly one place (UEFI or the Surface app), and charge to test.
4. If nothing has worked, the battery's internal controller may be faulty — contact Microsoft Surface support with your serial number, especially if the device is under warranty. For general battery health verification, [check the battery health report](/articles/how-to-check-battery-health-on-windows-11-laptop/) to rule out worn cells as a contributing factor.

## Closing

Smart charging on Windows 10 Surfaces is a firmware feature wearing a software disguise — the UEFI toggle is the real control, and firmware updates fix most stuck behavior. Get those two right and the feature goes back to quietly extending your battery's life instead of mysteriously capping it.
