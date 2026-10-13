---
title: "Battery Saver Not Working on Your Laptop? Fix It Step by Step"
slug: how-to-fix-battery-saver-not-working-on-laptop-step-by-step
date: 2026-10-12
categories: ["battery"]
tags: ["battery saver", "energy saver", "not working", "windows 11"]
description: "Battery saver turns on but changes nothing? 7 step-by-step fixes covering settings, policies, drivers, and background apps that defeat it."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "What does Battery saver actually do when it works?"
    a: "It dims the screen by about 30 percent, throttles background app activity, pauses OneDrive syncing and mail fetching, and reduces visual effects. Together these typically extend remaining runtime by 20 to 40 percent depending on what you were doing."
  - q: "Why does Battery saver turn on but my battery still drains fast?"
    a: "Because Battery saver reduces background drain — it can't fix a foreground hog. If Chrome with 40 tabs or a game is eating the battery, Battery saver trims the edges but the main drain continues. Check Task Manager's battery usage per app to find the real culprit."
  - q: "Should Battery saver be on all the time?"
    a: "It's designed for low-battery situations, not permanent use — the dimming and throttling get annoying. For everyday plugged-in efficiency, the 'Best power efficiency' power mode is the better always-on choice. Let Battery saver trigger automatically at 20 percent."
  - q: "Does Battery saver work while plugged in?"
    a: "On Windows 11, Energy Saver (the renamed Battery saver) can optionally run on AC power too, but its battery-extending purpose only matters unplugged. If it seems to do nothing while plugged in, that's expected — there's no battery drain to reduce."
---
You flip on Battery saver at 25 percent, expecting the screen to dim and the drain to slow — but nothing visibly changes. The percentage keeps falling at the same rate, the screen stays bright, and background apps keep chattering away. The feature is "on" in name only.

"Not working" actually covers three different failures: the toggle won't stay on, it turns on but changes nothing, or it never triggers automatically. This guide addresses all three, step by step.

## Why this happens

- **The automatic threshold is misconfigured.** Battery saver is set to trigger at 20 percent by default; if the threshold got set to 0 or "Never," it simply never kicks in on its own.
- **A policy is neutering it.** Group Policy or MDM settings can allow the toggle while disabling its actual effects — the switch moves, but nothing happens underneath.
- **Power plans are corrupted.** Battery saver hooks into the active power scheme; a damaged scheme means the feature fires blanks.
- **Background apps are exempted or too aggressive.** Apps with background permissions set to "Always" can largely ignore Battery saver's throttling.
- **The display driver isn't cooperating.** The automatic screen dimming is executed through the graphics driver; a broken driver means brightness never drops.
- **Windows thinks you're on AC power.** A misreporting battery driver makes Windows believe the charger is connected, so battery-only behaviors never engage.
- **High-performance mode overrides it.** If the power mode is set to Best performance, it fights Battery saver's throttling and wins.

## How to fix it

Work through these in order. Each fix targets one of the three failure modes.

### Fix 1: Set the automatic trigger correctly

Start with the basics — most "never triggers" cases are just a bad threshold.

1. Go to **Settings** > **System** > **Power & battery** > **Battery saver** (or **Energy saver**).
2. Set **Turn battery saver on automatically at** to **20%** (or your preference — never "Never").
3. Toggle **Lower screen brightness when using battery saver** to **On** — this is the single most visible effect, and it's sometimes switched off.
4. Unplug the charger and drain to the threshold to verify it engages. If the toggle itself is greyed out rather than ineffective, see our guide to [fixing the greyed-out Battery saver](/articles/how-to-fix-battery-saver-greyed-out-after-windows-11-update/).

### Fix 2: Switch the power mode to Balanced

Best performance mode actively counteracts everything Battery saver tries to do.

1. Go to **Settings** > **System** > **Power & battery** and find **Power mode**.
2. Set it to **Balanced** (or **Best power efficiency** if you want maximum savings).
3. Turn Battery saver on manually and watch for the screen dim and background activity to drop.
4. Avoid Best performance except when genuinely needed — on battery, it's the enemy of everything you're trying to achieve here.

### Fix 3: Reset the power plans

A corrupt power scheme silently disables Battery saver's hooks.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `powercfg -restoredefaultschemes` to rebuild all plans from scratch.
3. Restart the laptop.
4. Reconfigure your Battery saver threshold (Fix 1), since the reset wipes custom settings, then test again.

### Fix 4: Tame background apps

Battery saver throttles background activity — unless apps are configured to ignore it.

1. Go to **Settings** > **Apps** > **Installed apps**, click the three dots on heavy apps (browsers, chat apps, cloud storage), choose **Advanced options**, and set **Background apps permissions** to **Power optimized** instead of **Always**.
2. Open **Task Manager** > **Startup apps** and disable anything you don't need at boot — every startup app is a background drain candidate.
3. Check **Settings** > **System** > **Power & battery** > **Battery usage** to see per-app consumption and target the worst offenders.
4. Turn Battery saver on and compare drain over 30 minutes. For a deeper cleanup, our guide to [turning off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-on-laptop/) goes further.

### Fix 5: Fix the display driver dimming

If everything dims except the screen, the graphics driver is the break in the chain.

1. Open **Device Manager**, expand **Display adapters**, right-click your GPU, and choose **Update driver** > **Search automatically**.
2. If already current, try **Uninstall device** (checking **Attempt to remove the driver**), then restart — Windows installs a fresh copy.
3. For Intel/NVIDIA/AMD graphics, grab the latest driver from the manufacturer's site — [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) — since display brightness control is often fixed in GPU driver updates.
4. Toggle Battery saver and confirm the screen visibly dims within a few seconds.

### Fix 6: Confirm Windows knows you're on battery

Battery saver's triggers depend on Windows correctly detecting battery vs. AC power.

1. Unplug the charger and check the taskbar icon — it should show a battery percentage, not a plug.
2. If Windows still shows charging while unplugged, the battery driver is misreporting: reinstall **Microsoft ACPI-Compliant Control Method Battery** in Device Manager with a full shutdown.
3. In **Settings** > **System** > **Power & battery**, verify the status line says "On battery" and shows a discharging percentage.
4. Retest Battery saver now that Windows knows the truth about your power source.

### Fix 7: Check for policies disabling its effects

The toggle moves but nothing happens — the classic policy-neutered symptom.

1. Run `gpedit.msc` (Pro editions) and check **Computer Configuration** > **Administrative Templates** > **System** > **Power Management** > **Energy Saver Settings** for anything configured.
2. Set any enabled energy-saver policies to **Not Configured**, then run `gpupdate /force` in an elevated Terminal.
3. Check **Settings** > **Accounts** > **Access work or school** for unexpected management enrollment.
4. Restart and test. If a management profile is enforcing it, only your administrator can change it — but at least you'll know the toggle isn't broken, it's locked.

## Closing

Battery saver "not working" is usually a configuration problem, not a broken feature: wrong threshold, wrong power mode, unruly background apps, or a policy quietly disabling it. Set the trigger, tame the apps, confirm Windows knows you're on battery — and the percentage will start falling noticeably slower.
