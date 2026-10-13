---
title: "Black Screen After the Windows 11 24H2 Update? Here's the Recovery"
slug: how-to-fix-windows-11-24h2-black-screen-after-update
date: 2026-09-19
categories: ["windows-update"]
tags: ["black screen", "24h2", "after update", "windows 11", "recovery"]
description: "Updated to 24H2 and now staring at a black screen? Don't panic — from simple wake-ups to driver rollbacks, here's the recovery sequence."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-black-screen-after-update.webp"
faqs:
  - q: "My laptop shows a black screen after the 24H2 update — is my data gone?"
    a: "Almost certainly not. A post-update black screen is a display/output problem, not a data problem — your files are intact on the drive. The causes are usually a graphics driver failing to load, the display output routing to a phantom monitor, or Explorer failing to start. Every fix below preserves your data."
  - q: "How do I know if it's a black screen or the laptop is just off?"
    a: "Check for signs of life: power LED on, fan noise, drive activity, or the screen backlight glowing faintly black (vs. fully off). Try Caps Lock — if the Caps Lock light toggles, Windows is running behind the black screen and it's a display issue. No lights at all means a power/boot problem instead."
  - q: "Why does 24H2 specifically cause black screens?"
    a: "Major build updates replace the graphics driver stack and display subsystem components. If the new inbox driver conflicts with your GPU, or the migration corrupted the driver state, the display never initializes — while everything else boots fine. It's the most common post-feature-update failure mode across all Windows versions."
  - q: "Should I reinstall Windows if the black screen won't clear?"
    a: "Only as a last resort after trying the recovery sequence here. Most 24H2 black screens resolve via the graphics driver reset shortcut, Safe Mode driver rollback, or uninstalling the update from WinRE. Reinstallation is for when WinRE itself is unreachable — which is rare."
---

You installed the 24H2 update, the laptop rebooted, and now... nothing. Black screen. Maybe a cursor. Maybe not even that. Your stomach drops, because a dead display after an update feels like a dead laptop. It isn't. In the overwhelming majority of cases, Windows 11 24H2 is running perfectly fine behind that black screen — it just can't show you, because the graphics driver or display routing broke during the upgrade.

The recovery sequence below is ordered by invasiveness: key combos that wake the display in seconds, then Safe Mode driver surgery, then rolling back the update itself from the recovery environment. Work top to bottom and stop when the picture returns. If your upgrade never completed and is stuck mid-progress instead, see [feature update stuck at 61%](/articles/how-to-fix-feature-update-stuck-at-61-percent-reddit/).

First, the 10-second triage: press Caps Lock. If the light toggles, Windows is alive — it's purely a display problem, and Fix 1 may solve it in seconds.

## Why this happens

- **Graphics driver failed to migrate**: The 24H2 driver stack replaced your GPU driver with an incompatible one, or corrupted its state. The Win+Ctrl+Shift+B shortcut restarts the driver without rebooting — try it first.
- **Display routed to phantom monitor**: The upgrade misdetected displays and is rendering to a non-existent external monitor. Win+P followed by arrow-down and Enter cycles blindly to PC screen only.
- **Explorer.exe failing to start**: Black screen with cursor often means Windows booted but the shell crashed. If Caps Lock toggles, Windows is alive behind the black screen — it is purely a display issue.
- **Fast Startup hibernation conflict**: A stale hibernation state from pre-update can prevent clean display init. A full power drain — unplug, hold power 15 seconds — clears the stale hibernation file.
- **External dock/monitor handshake failure**: Docks and USB-C monitors renegotiating with the new driver stack can leave all outputs dark. Disconnect the dock and test the built-in display alone before anything else.
- **Corrupted driver store migration**: Partial driver migration leaves the GPU in a neither-old-nor-new state. Safe Mode's basic display driver bypasses the broken one so you can roll back.
- **Third-party display utilities**: Screen managers and color profiles hooking the display pipeline break under the new stack. Uninstalling these before retrying 24H2 prevents the recurrence.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wake the display: Win + Ctrl + Shift + B

This key combo restarts the graphics driver without rebooting. It's the fastest fix when it works. This key combo restarts the graphics driver without rebooting. It is the fastest fix when it works.

1. Press **Windows key + Ctrl + Shift + B** simultaneously.
2. You should hear a beep and the screen may flicker — that's the driver resetting.
3. Wait 30 seconds for the display to reinitialize.
4. If the desktop appears, immediately update your graphics driver (Fix 5) so it doesn't recur. If nothing happens, continue.
5. If the beep sounds but nothing appears, the driver reset worked and the issue is output routing — move to Fix 2.

### Fix 2: Force the correct display output

The image may be rendering to a phantom display. The image may be rendering to a phantom display.

1. Press **Windows key + P**, then press the **Down arrow** once and **Enter** (this cycles to 'PC screen only' blind).
2. Wait 15 seconds between each attempt; try 2–3 cycles.
3. If you use a dock or external monitor, disconnect them and retry on the built-in display.
4. If the laptop screen wakes, reconnect externals one at a time afterward.
5. Try the key combo blind a few times with pauses — each press cycles one step through the projection modes.

### Fix 3: Hard reboot to clear Fast Startup state

A stale hibernation file can block display init. A full power cycle clears it. A stale hibernation file can block display init. A full power cycle clears it.

1. Hold the power button for 10 seconds until fully off.
2. Unplug the charger and all peripherals; if the battery is removable, remove it for 30 seconds.
3. Hold the power button for 15 seconds with everything disconnected (drains residual power).
4. Reconnect only the charger and power on. If the screen works, disable Fast Startup later (Control Panel → Power Options → Choose what the power buttons do).
5. On laptops with sealed batteries, hold the power button a full 30 seconds — residual charge lingers longer.

### Fix 4: Boot into Safe Mode and roll back the graphics driver

Safe Mode uses the basic display driver, bypassing the broken one. Safe Mode uses the basic display driver, bypassing the broken one.

1. Force WinRE: power off mid-boot twice (hold power during the Windows logo); on the third boot, Recovery appears.
2. Troubleshoot → Advanced options → Startup Settings → Restart → press 4 for Safe Mode.
3. In Safe Mode: Device Manager → Display adapters → right-click your GPU → **Roll Back Driver** (or Uninstall device, then reboot to let Windows reinstall).
4. Restart normally — the display should return on the basic/rolled-back driver.
5. If Roll Back Driver is greyed out, choose Uninstall device — Windows reinstalls a working driver on reboot.

### Fix 5: Update the graphics driver cleanly

Once you can see the screen, prevent recurrence with a proper driver install. Once you can see the screen, prevent recurrence with a proper driver install.

1. Identify your GPU (Intel/AMD/NVIDIA) in Device Manager.
2. Download the latest driver: [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or AMD's driver download page.
3. Choose 'clean install' if the installer offers it.
4. Reboot and verify stability; reconnect external displays afterward.
5. After the clean install, test sleep-wake cycles specifically — some 24H2 display bugs only appear on resume.

### Fix 6: Uninstall the 24H2 update from WinRE

If no driver maneuver restores the display, roll back the update itself. If no driver maneuver restores the display, roll back the update itself.

1. Boot into WinRE (two interrupted boots, as in Fix 4).
2. Troubleshoot → Advanced options → **Uninstall Updates** → Uninstall latest feature update.
3. Let the rollback complete (it can take 30+ minutes); the laptop returns to the previous build.
4. Once back, update drivers first (Fix 5), then retry 24H2 — or use the [enablement package path](/articles/how-to-enablement-package-install-in-windows-11-24h2/) if eligible.
5. The rollback preserves your files but removes 24H2 — treat it as a pause, not a defeat.

### Fix 7: Check for the 24H2 known display issues

Some black screens are documented 24H2 bugs with specific patches. Some black screens are documented 24H2 bugs with specific patches.

1. On another device, check the Windows release health dashboard for 24H2 display-related known issues.
2. If your GPU/model is listed, wait for the documented fix rather than fighting it.
3. Install the specific KB the dashboard names via the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) once available.
4. Our broader rundown: [24H2 known issues step by step](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/).
5. Bookmark the dashboard entry for your issue — its status changes are your signal to retry 24H2.

## Closing

A black screen after 24H2 is terrifying but rarely fatal: the driver-reset shortcut, blind display switching, Safe Mode rollback, and WinRE uninstall form a ladder from seconds-long fixes to full recovery. Your data was never in danger — and once the right graphics driver is in place, 24H2 behaves itself. Related guides: [feature update stuck at 61%](/articles/how-to-fix-feature-update-stuck-at-61-percent-reddit/) and [enablement package path](/articles/how-to-enablement-package-install-in-windows-11-24h2/) and [24H2 known issues step by step](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/).
