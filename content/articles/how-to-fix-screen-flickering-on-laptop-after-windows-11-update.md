---
title: "How to Fix Screen Flickering on a Laptop After a Windows 11 Update"
slug: how-to-fix-screen-flickering-on-laptop-after-windows-11-update
date: 2026-09-13
categories: ["drivers"]
tags: ["screen flickering", "display flicker", "windows 11 update", "graphics driver"]
description: "Laptop screen flickering after a Windows 11 update? Diagnose whether it's the driver or an app, then apply six targeted fixes from refresh rate to clean reinstall."
thumbnail: "/images/thumbs/how-to-fix-screen-flickering-on-laptop-after-windows-11-update.webp"
faqs:
  - q: "How do I tell if the flickering is caused by a driver or an app?"
    a: "Open Task Manager with Ctrl+Shift+Esc: if Task Manager flickers along with everything else, the display driver is the cause. If Task Manager stays steady while the rest of the screen flickers, an incompatible app is doing it. This thirty-second test decides your entire troubleshooting path, so do it before changing anything — driver fixes won't help an app problem and vice versa."
  - q: "Can a Windows update really cause screen flickering by itself?"
    a: "Yes, and it's one of the most common post-update complaints. Updates replace the graphics driver, change the default refresh rate, or install an app compatibility shim that misbehaves. The flicker starting immediately after an update is strong evidence of a software cause — hardware flicker from a failing panel or cable doesn't synchronize with Microsoft's patch schedule."
  - q: "Is screen flickering dangerous for my eyes or the laptop?"
    a: "Prolonged flicker causes eye strain and headaches in sensitive people, so don't just live with it — but it won't physically damage the panel. The exception is flicker accompanied by graphical corruption or crashes, which can indicate GPU instability worth fixing promptly. Either way, treat flicker as a problem to solve this week, not a quirk to tolerate."
  - q: "Why does the flickering stop when I plug in the charger?"
    a: "On battery, Windows may drop the refresh rate or enable panel self-refresh and aggressive GPU power saving to extend battery life, and those power-saving display features can flicker on certain panels. Plugging in disables them. If this matches your symptom, the fix is in the display and power settings — raise the refresh rate back up and disable panel self-refresh — rather than in the driver."
---

Your screen flickers — brightness pulsing, horizontal tearing, or the whole display blinking — and it started right after the Windows 11 update. Before you do anything else, run the thirty-second test that decides everything: press **Ctrl + Shift + Esc** to open Task Manager. If Task Manager flickers too, your display driver is the problem. If Task Manager is rock-steady while everything behind it flickers, an incompatible application is the problem. That single observation splits this guide's path cleanly, so don't skip it.

Post-update flicker is overwhelmingly a software issue. The update touched your graphics driver, possibly changed your refresh rate default, and may have dragged along an app that no longer agrees with the new build. Hardware flicker — failing backlights, loose display cables — doesn't start the morning after Patch Tuesday. We'll cover the driver path first (the common one), then the app path, and finish with the settings that cause flicker on specific panels. If the flicker is on an external monitor rather than the laptop screen, the [second monitor flickering guide](/articles/how-to-fix-second-monitor-flickering-after-windows-11-update/) addresses that separately.

## Why this happens

- **The graphics driver was replaced with a buggy build.** The update installed a display driver whose vsync or refresh-rate handling glitches on your specific panel.
- **The refresh rate default changed.** The update reset your panel from 120/144 Hz to 60 Hz, or enabled a dynamic refresh rate your panel handles poorly.
- **An incompatible app is redrawing badly.** Apps with overlay, hook, or outdated rendering code (older antivirus UIs, some screen tools) flicker against the new build while the driver itself is fine.
- **Panel self-refresh or power saving glitches.** PSR (Panel Self-Refresh) and Intel/AMD power-saving display features can flicker when the driver update changes their behavior.
- **Hardware GPU scheduling conflicts.** 24H2's scheduling changes can destabilize specific driver builds, producing flicker under light GPU load.
- **A corrupted color profile or HDR setting.** The update may have applied a broken ICC profile or toggled HDR on a panel that doesn't handle it cleanly.
- **The DWM (desktop compositor) is crashing and restarting.** Repeated compositor restarts look like full-screen flicker and point to driver or shell-extension instability.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm driver vs. app with Task Manager

Do the diagnostic properly before changing anything.

1. Press **Ctrl + Shift + Esc** and watch Task Manager for 30 seconds.
2. **Task Manager flickers too** → display driver problem → continue with Fix 2.
3. **Task Manager is steady** → incompatible app → skip to Fix 5.
4. Note the flicker pattern too: rhythmic pulsing suggests refresh-rate/power issues; random tearing suggests driver instability.

### Fix 2: Roll back or clean-reinstall the graphics driver

The driver path starts here.

1. Device Manager > **Display adapters** > right-click your GPU > **Properties** > **Driver** tab.
2. If the driver date is recent (matches the update), click **Roll Back Driver** and restart.
3. If rollback isn't available, do a clean reinstall: download the driver from Intel ([Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html), choosing clean/factory install options.
4. Test for an hour of normal use — driver flicker often needs sustained use to confirm it's gone.

### Fix 3: Set the correct refresh rate

A wrong refresh rate is a classic post-update flicker source.

1. **Settings** > **System** > **Display** > **Advanced display**.
2. Set **Choose a refresh rate** to your panel's native rate (the highest option is usually correct — 120 Hz, 144 Hz, etc.).
3. If **Dynamic** refresh rate is selected, switch to a fixed rate — dynamic switching flickers on some panels.
4. Apply and observe. This single setting resolves a large share of post-update flicker reports.

### Fix 4: Disable panel self-refresh and display power saving

Stop the power features from modulating your panel.

1. Open **Intel Graphics Command Center** (or AMD Software / NVIDIA Control Panel) and find **Panel Self-Refresh** — turn it **Off**.
2. In the same app, disable **Display Power Saving Technology** or equivalent.
3. In Windows **Settings** > **System** > **Power & battery**, set the power mode to **Best performance** temporarily for testing.
4. If flicker stops, you've found it — keep PSR off; the battery cost is minor.

### Fix 5: Find and remove the incompatible app

For the Task-Manager-steady case.

1. Think about what updated recently alongside Windows — antivirus suites, screen recording tools, and older utilities are the usual suspects.
2. Uninstall candidates one at a time (**Settings** > **Apps** > **Installed apps**), testing after each.
3. Check the app's vendor site for a Windows 11 24H2-compatible version before reinstalling.
4. As a quick screen, boot into **Safe Mode** — if the flicker is gone there, an app or third-party driver is confirmed as the cause.

### Fix 6: Reset the color profile and check HDR

Clear display-pipeline corruption.

1. **Settings** > **System** > **Display** — turn **HDR** off temporarily if it's on.
2. Search **Color Management**, select your display, and remove any custom ICC profiles, restoring the system default.
3. In the graphics control panel, reset all color/video settings to defaults.
4. Restart. If the flicker was profile-related, it's gone — re-enable HDR afterward only if your panel genuinely supports it. Persistent full-screen flicker with crashes points back to the driver: revisit the [display driver TDR fixes](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) for the deeper GPU-stability steps.

## Closing

Screen flicker after an update is a solved problem with a diagnostic at its heart: Task Manager tells you whether to fix the driver or hunt an app, and from there it's refresh rates, power-saving features, and clean driver installs. Work the test first and the fixes in order, and the flicker that arrived with the update will leave the same way it came — through software, not through a repair shop.
