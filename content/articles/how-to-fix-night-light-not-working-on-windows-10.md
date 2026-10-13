---
title: "Night Light Not Working on Windows 10? Fix It Now"
slug: how-to-fix-night-light-not-working-on-windows-10
date: 2026-10-08
categories: ["drivers"]
tags: ["night light", "blue light", "display", "windows 10", "troubleshooting"]
description: "Night Light greyed out or not turning on in Windows 10? Fix the blue-light filter with driver, registry, and settings repairs — step by step."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working-on-windows-10.webp"
faqs:
  - q: "Why is Night Light greyed out in Windows 10 settings?"
    a: "A greyed-out Night Light toggle usually means the graphics driver isn't exposing color-temperature control to Windows, or the Night Light registry/cloud-store state is corrupted. Updating the graphics driver fixes the first cause; resetting the Night Light settings state fixes the second. Both are common after Windows updates."
  - q: "Does Night Light work on external monitors?"
    a: "Yes — Night Light is applied by the GPU driver, so it works on any display the driver manages, including external monitors. If Night Light works on the laptop screen but not the external monitor, the monitor's driver or the GPU's per-display color settings are the issue, not Night Light itself."
  - q: "Why does Night Light turn off by itself?"
    a: "Usually a schedule misconfiguration — check the sunset-to-sunrise vs. custom hours setting. It can also be disabled by fullscreen apps, HDR mode engaging, or the graphics driver resetting color settings. Location services being off breaks the sunset schedule specifically, since Windows can't compute local sunset."
  - q: "Is Night Light the same as the monitor's blue light filter?"
    a: "No. Night Light is software color-temperature shifting done by Windows and the GPU driver. Monitor blue-light filters (low blue light modes) are hardware/firmware features in the panel. They can stack — using both is fine — but troubleshoot them separately since they fail independently."
---

Night Light is one of Windows 10's quietest features — until it stops working. The toggle greys out, the schedule silently stops engaging, or the screen just never warms up at night. Because Night Light depends on the graphics driver, the Windows settings cloud store, and location services all cooperating, failures are common and the cause is rarely obvious.

The good news: Night Light failures cluster into a few known patterns with known fixes. A greyed toggle is almost always driver or settings-state; a schedule that never fires is almost always location or cloud-store corruption. Identify your symptom, apply the matching fix.

## Why this happens

- **Graphics driver not exposing color control:** the driver doesn't support Night Light's API.
- **Corrupt settings state:** the cloud-store registry data for Night Light is damaged.
- **Location services off:** sunset-to-sunrise schedule can't compute without location.
- **HDR mode conflict:** HDR engagement overrides Night Light's color temperature.
- **Group policy disabled it:** enterprise or "debloat" scripts turned Night Light off.
- **Driver update reset:** a GPU update cleared the color calibration Night Light needs.
- **Fast Startup state corruption:** hibernated driver state breaks color pipeline.
- **Monitor driver issue:** the PnP monitor driver misreports capabilities.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update the graphics driver

1. A greyed Night Light toggle most often means the GPU driver. Download the latest from Intel ([Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)) or [NVIDIA](https://www.nvidia.com/Download/index.aspx).
2. Install with the clean-install option to clear stale color-calibration state.
3. Reboot and check **Settings > System > Display > Night light settings** — the toggle should be active.
4. If Night Light broke right after a driver update, roll back instead.
5. Also install the monitor's .inf driver from the manufacturer's site — it helps Windows identify the display properly.

### Fix 2: Reset the Night Light settings state

1. This fixes the corrupted cloud-store data behind many Night Light failures.
2. Open Registry Editor and navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current`.
3. Find the `$$windows.data.bluelightreduction.bluelightreductionstate` key, right-click, and **Delete** it. (Also delete `$$windows.data.bluelightreduction.settings` if present.)
4. Sign out and back in (or reboot). Windows rebuilds the Night Light state fresh.
5. Reconfigure your Night Light schedule — the toggle and scheduling should now work.
6. This is the definitive fix for "toggle does nothing" and "schedule never fires" when the driver is fine.

### Fix 3: Fix the schedule and location

1. Go to **Settings > System > Display > Night light settings**.
2. If using **Sunset to sunrise**, ensure **Location** is on: **Settings > Privacy > Location** — Windows needs it to compute sunset.
3. Switch to **Set hours** with explicit times as a test — if the manual schedule works but sunset doesn't, location is the problem.
4. Check that your time zone and clock are correct — a wrong clock breaks scheduling silently.
5. Toggle the schedule off and on once after changes to force re-evaluation.

### Fix 4: Check for HDR and app conflicts

1. If **HDR** is enabled on the display, Night Light may be overridden — HDR takes over the color pipeline.
2. Disable HDR temporarily to test whether Night Light returns.
3. Fullscreen games and video players can suspend Night Light; test on the desktop with no apps open.
4. Third-party "f.lux"-style apps conflict with Night Light — use one or the other, not both.
5. Related color-pipeline issues: [HDR not working on laptops](/articles/how-to-fix-hdr-not-working-on-laptop-step-by-step/) covers the HDR side of this conflict.

### Fix 5: Disable Fast Startup

1. Go to **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart) and power back on.
4. Fast Startup hibernates driver state; corrupted hibernated color-pipeline state breaks Night Light across boots.
5. If Night Light starts working, leave Fast Startup off — the boot-time cost is small on SSDs.

### Fix 6: Check group policy and registry locks

1. Press **Win + R**, type `gpedit.msc` (Pro editions), and check **Computer Configuration > Administrative Templates > Windows Components** for Night Light policies.
2. "Debloat" scripts and some enterprise setups disable Night Light via policy or registry.
3. Check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows` for blue-light-related values and remove them if you didn't set them.
4. After clearing policies, run `gpupdate /force` and reboot.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents policy behavior if you're on a managed device — some locks are intentional.

### Fix 7: Recalibrate display color

1. Search **Calibrate display color** and run the wizard — Night Light builds on the display's color calibration.
2. A corrupted color profile can suppress Night Light's effect even when the toggle works.
3. In **Color Management**, check that the correct display profile is assigned to your monitor.
4. Delete custom color profiles as a test — a bad profile overrides Night Light's temperature shift.
5. After recalibration, toggle Night Light off and on to reapply it onto the fresh profile.
6. Test Night Light at several strength levels — a profile that works at 50% but not 100% indicates a gamut limitation rather than a bug.

## Closing

Night Light failures look mysterious but follow two tracks: greyed toggle means driver or settings-state (Fix 1 and 2), dead schedule means location or cloud-store (Fix 2 and 3). The registry-state reset in Fix 2 is the unsung hero — it fixes a huge share of cases in under two minutes. Get the driver current, clear the corrupt state, verify the schedule, and the warm evening screen comes back. Your eyes will notice the difference the first night it's working again. The same color-pipeline logic applies to [HDR on Windows 11](/articles/how-to-fix-hdr-not-working-on-laptop-on-windows-11/) if brightness features misbehave together.
