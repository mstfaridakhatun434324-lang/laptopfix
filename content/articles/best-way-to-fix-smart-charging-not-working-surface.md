---
title: "Fixing Smart Charging Not Working on Microsoft Surface"
slug: best-way-to-fix-smart-charging-not-working-surface
date: 2026-09-22
categories: ["battery"]
tags: ["Surface", "smart charging", "battery limit"]
description: "Surface Smart Charging stuck off or not limiting charge? Here's how to get it working again on Surface Laptop and Pro."
thumbnail: "/images/thumbs/best-way-to-fix-smart-charging-not-working-surface.webp"
faqs:
  - q: "What is Smart Charging on a Surface device?"
    a: "Smart Charging is a battery longevity feature that pauses charging at 80% when it detects you keep your Surface plugged in most of the time. Unlike a fixed limit, it adapts: if you start taking the device on the go, it resumes charging to 100%. It is managed through the Surface app and device firmware."
  - q: "Why is Smart Charging not available on my Surface?"
    a: "It requires a supported device (Surface Laptop 5 and newer, Surface Pro 9 and newer, and recent Surface Laptop Studio models), up-to-date firmware, and the Surface app. Older devices like Surface Pro 8 and earlier do not support Smart Charging at all — they only offer the fixed 80% battery limit in UEFI."
  - q: "Smart Charging is on but my Surface still charges to 100%. Is it broken?"
    a: "Usually not. Smart Charging deliberately allows full charges when your usage pattern changes — for example, after several days of mobile use. It needs about a week of consistent plugged-in behavior to engage. If it never engages after two weeks of desk use, then something is genuinely wrong."
  - q: "Can I force Smart Charging to stay at 80%?"
    a: "Yes — disable Smart Charging in the Surface app and enable the fixed Battery limit (80%) instead, either in the Surface app or in UEFI settings. The fixed limit is dumber but absolute: the battery will never charge past 80% until you turn the limit off."
---

Smart Charging is one of the best battery features on modern Surface devices — when it works. It learns that your Surface Laptop lives on a desk and quietly holds the charge at 80%, then lets it fill to 100% when you actually start traveling. But plenty of owners find the toggle greyed out, missing entirely, or switched on yet doing nothing.

The fixes depend on which of those you're seeing. Work through them in order — most Smart Charging problems trace back to firmware, the Surface app, or simply misunderstanding how the adaptive logic behaves.

## Why this happens

- **Outdated Surface firmware.** Smart Charging is implemented in the UEFI/firmware layer. Old firmware may lack the feature entirely or contain the bugs that break it.
- **Missing or outdated Surface app.** The toggle lives in the Surface app; without the current version from the Microsoft Store, the option may not appear.
- **Unsupported device.** Smart Charging needs recent hardware. Older Surface models only support the fixed 80% UEFI battery limit, not the adaptive feature.
- **The adaptive logic hasn't learned yet.** Smart Charging needs days of consistent usage data before it engages. Users who just enabled it often conclude it's broken on day two.
- **A conflicting battery limit.** If the fixed 80% battery limit is enabled in UEFI, it overrides Smart Charging behavior and can make the feature appear non-functional.
- **Corrupt power subsystem state.** Failed updates or interrupted firmware installs can leave the charging controller in a confused state where toggles don't stick.

## How to fix it

Work through these in order, checking the Surface app after each step.

### Fix 1: Confirm your Surface actually supports Smart Charging

Don't troubleshoot a feature your hardware lacks.

1. Open the **Surface** app (search for it in Start; install it from the Microsoft Store if missing).
2. Go to **Battery** or **Power** settings within the app. You should see **Smart Charging** listed on supported devices.
3. Supported: Surface Laptop 5/6/7, Surface Pro 9/10/11, Surface Laptop Studio 2, and newer. Not supported: Surface Pro 8 and earlier, Surface Laptop 4 and earlier, Surface Go models.
4. If your device isn't supported, use the fixed **Battery limit** in UEFI instead: shut down, hold **Volume Up + Power** to enter UEFI, and enable the 80% limit under **Boot configuration** or **Battery**.
5. If your device is supported but the option is missing, continue — the app or firmware needs attention.

### Fix 2: Update the Surface app and all firmware

The most common actual fix.

1. Open the **Microsoft Store → Library** and install all pending updates, especially the **Surface** app itself.
2. Go to **Settings → Windows Update** and install everything, including **optional driver updates** — Surface firmware arrives through Windows Update.
3. After updating, restart the Surface (full restart, not just sleep).
4. Reopen the Surface app and check whether Smart Charging now appears and toggles correctly.
5. If Windows Update shows firmware failing to install, download the **Surface driver and firmware MSI** for your exact model from the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) support section and install it manually. For general Windows-side battery help, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Toggle Smart Charging off and on cleanly

A stuck toggle often just needs a clean reset.

1. In the **Surface** app, turn **Smart Charging** off.
2. Shut down the Surface completely. Unplug the charger.
3. Press and hold the power button for 20 seconds, then release — this resets the embedded controller state on most Surface models.
4. Plug the charger back in, power on, and re-enable **Smart Charging** in the Surface app.
5. Keep the Surface plugged in at your desk for the next several days so the adaptive logic can observe the pattern.

### Fix 4: Resolve conflicts with the fixed battery limit

The two features fight each other.

1. Decide which you want: **Smart Charging** (adaptive, allows 100% when traveling) or the fixed **Battery limit** (always caps at 80%).
2. If you want Smart Charging, make sure the fixed limit is OFF everywhere: check the Surface app's battery settings and the UEFI firmware settings (Volume Up + Power at boot).
3. If you'd rather have the dumb-but-reliable cap, turn Smart Charging off and enable the fixed 80% limit instead — many desk-bound users prefer this. Our general guide on [limiting battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) covers the concept across brands.
4. After changing, give it one full charge cycle to confirm the behavior matches your choice.

### Fix 5: Give the adaptive logic time — then verify it's learning

Impatience is the number one false alarm.

1. Smart Charging typically needs 5–7 days of consistent plugged-in usage before it first engages.
2. During this learning period, keep your routine steady: plugged in at the desk during the day is the pattern it needs to see.
3. After a week, check the battery icon: when Smart Charging is actively limiting, you'll often see the charge hold at 80% with a "plugged in" status.
4. If after two full weeks of desk use it still charges to 100% every time, the feature genuinely isn't engaging — proceed to Fix 6.
5. Note that occasional 100% charges are normal even when working — the algorithm periodically allows a full charge to keep the gauge calibrated, similar to a [manual battery calibration](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 6: Reset the Surface UEFI and reinstall firmware

For genuinely stuck charging controllers.

1. Back up your data first — this step is safe, but firmware work deserves a backup.
2. Enter UEFI (shut down, then hold **Volume Up** while pressing **Power**).
3. Choose **Exit → Restore Defaults** (wording varies by model), then save and exit.
4. Boot into Windows, run **Windows Update** again to re-apply any firmware, and restart.
5. Reconfigure Smart Charging in the Surface app from scratch. If it still fails, the issue may need Microsoft's hands — see Fix 7.

### Fix 7: Contact Microsoft Support with diagnostic data

When software fixes are exhausted:

1. In the Surface app, run any available **diagnostic** or battery health check and screenshot the results.
2. Generate a battery report (`powercfg /batteryreport` in an elevated terminal) to document actual capacity and charging behavior.
3. Contact Microsoft Support through the Surface app's **Help** section or the [Windows support hub](https://support.microsoft.com/en-us/windows) with your model, firmware version, and what you've tried.
4. If the device is under warranty or covered by Microsoft Complete, a persistent Smart Charging failure with healthy battery numbers usually qualifies for service.

## Closing

Smart Charging problems on Surface almost always come down to three things: firmware that's behind, the adaptive logic not having enough data yet, or the fixed battery limit fighting it. Update everything, pick one limiting strategy, give it a week of steady desk use, and the feature usually starts behaving. Your battery will thank you with extra years of healthy capacity.
