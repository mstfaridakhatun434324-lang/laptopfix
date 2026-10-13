---
title: "How to Fix a Black Screen After the Windows 11 24H2 Update on an Asus Laptop"
slug: how-to-fix-windows-11-24h2-black-screen-after-update-on-asus-laptop
date: 2026-09-29
categories: ["windows-update"]
tags: ["black screen", "windows 11 24h2", "asus", "display driver", "windows update"]
description: "Asus laptop black-screened after the 24H2 update? Run the Caps Lock test, wake the display, and fix the driver with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-black-screen-after-update-on-asus-laptop.webp"
faqs:
  - q: "How can I tell if my Asus is actually running behind the black screen?"
    a: "Press Caps Lock and watch the indicator light. A toggling light means Windows is running and responsive — the problem is display output only, which is fixable with the driver steps below. Also listen for fans and drive activity. No lights, no sounds, and no response after 30 minutes points to a system that is not booting at all, which needs the recovery environment instead."
  - q: "Why are Asus laptops prone to black screens after 24H2?"
    a: "Many Asus models — especially ROG, TUF, VivoBook, and Zenbook machines — use hybrid graphics with Intel or AMD integrated plus NVIDIA discrete GPUs. The 24H2 upgrade replaces the graphics driver, and the handoff between the two GPUs sometimes breaks. Asus utilities like Armoury Crate that manage display profiles can also conflict with the new driver, compounding the problem."
  - q: "Will these fixes delete anything on my laptop?"
    a: "No. Waking the display, booting Safe Mode, rolling back drivers, and even uninstalling the 24H2 update all target system components only. Your personal files, installed programs, and settings are preserved through every step. There is no need to reinstall Windows from scratch for a post-update black screen."
  - q: "What if the screen works in Safe Mode but not normally?"
    a: "That confirms the diagnosis precisely: the basic Safe Mode display driver works, so the normal graphics driver is the problem. Roll back or reinstall the driver as described in the fixes below, and avoid letting Windows Update reinstall the same bad driver — hide it or install the manufacturer's version first."
---

The 24H2 update restarted your Asus laptop and the screen never came back. Before anything else, run the test that decides the whole repair: press **Caps Lock** and watch the indicator light. Toggling means Windows is running fine behind the black screen — 24H2 broke the display output, not the system. That is a driver problem, and driver problems have a clear fix path.

Asus laptops are well represented in 24H2 black screen reports, and the pattern is consistent: hybrid-graphics machines (ROG, TUF, VivoBook, Zenbook) where the upgrade's new graphics driver fumbles the handoff between integrated and discrete GPUs. Asus's own Armoury Crate display profiles can make it worse by fighting the replacement driver. The system boots; the picture just never arrives.

Work through the fixes below in order, starting with the instant checks. Stop when your desktop returns.

## Why this happens

- **The GPU handoff broke on hybrid graphics.** 24H2's driver fails the switch between integrated and discrete GPUs common on Asus gaming and ultrabook lines.
- **The new driver misreads the panel.** Incorrect refresh rate or resolution handling leaves the display unable to show anything.
- **Output routed to a phantom external display.** The upgrade sometimes sends the picture to a non-existent monitor.
- **Armoury Crate display profiles conflict.** Asus's display management fights the new driver over color profiles and refresh rates.
- **Fast Startup saved a stale state.** The pre-update hybrid shutdown does not match the upgraded system.
- **The update is still finalizing.** 24H2 completes background work after the visible install, occasionally with the display dark.
- **Corrupted system files.** Upgrade damage breaks display pipeline components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Caps Lock test and wake the display

One keypress of diagnosis, then the fastest remedies.

1. Press **Caps Lock**. A toggling indicator means Windows is alive — continue below. Dead silence after 30 minutes means a non-booting system; skip to Fix 6.
2. Press **Windows key + Ctrl + Shift + B** and listen for the driver-restart beep.
3. Press **Windows key + P**, **Down arrow**, **Enter** to cycle projection output away from any phantom display.
4. Disconnect external monitors and docks, then tap power once to sleep and wake.

### Fix 2: Force a restart into Safe Mode

Reach the minimal environment where the basic driver works.

1. Hold the **power button** 10 seconds to force off, wait 30 seconds.
2. Power on; if still black, force off twice more during the Asus logo to trigger recovery.
3. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4** for Safe Mode.
4. A visible desktop in Safe Mode confirms the normal graphics driver as the culprit.

### Fix 3: Roll back the graphics driver

Reverse exactly what the 24H2 upgrade changed.

1. In Safe Mode, open **Device Manager > Display adapters**. On hybrid models, start with the integrated GPU (Intel or AMD), which 24H2 most likely updated.
2. Right-click, **Properties > Driver**, and click **Roll Back Driver** if available.
3. If unavailable, **Uninstall device** with **Attempt to remove the driver for this device** checked, then restart for the basic driver fallback.
4. With the screen back, install the proper driver: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) for discrete GPUs, AMD drivers for AMD, or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel.

### Fix 4: Disable Fast Startup and quiet Armoury Crate

Remove the stale-state and software-conflict causes.

1. In **Control Panel > Power Options > Choose what the power buttons do**, uncheck **Turn on fast startup**.
2. In **Armoury Crate**, reset display profiles to default or temporarily uninstall its display components; also check **Settings > Apps** for other Asus screen tools.
3. Restart twice, confirming the desktop appears reliably each time.
4. Reintroduce Asus utilities gradually after stability is proven.

### Fix 5: Clean-install the correct GPU driver

When rollback leaves you on an ancient driver, install the right current one properly.

1. Download the driver for your exact GPU from the manufacturer links in Fix 3.
2. For NVIDIA, run the installer, choose **Custom**, and check **Perform a clean installation** to wipe the broken 24H2 driver completely.
3. Restart and verify the display initializes on every boot.
4. In **Windows Update > Advanced options**, consider pausing driver updates temporarily so the bad version is not re-offered immediately.

### Fix 6: Uninstall the 24H2 update

If no driver combination stabilizes the display, remove the update.

1. In the recovery environment: **Troubleshoot > Advanced options > Uninstall Updates > Uninstall latest feature update**.
2. Let the rollback finish — you return to the previous working build with files intact.
3. Pause feature updates for several weeks.
4. Before retrying, check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for resolved 24H2 display issues on Asus hardware.

### Fix 7: Verify it is not a hardware failure

Confirm the update is truly to blame.

1. Connect an external monitor — picture there but not on the laptop panel suggests panel or cable hardware.
2. Flashlight test: shine light at the dark screen at an angle; a faint image means backlight failure.
3. Fully dead machine (no Caps Lock, no sounds): hard reset by unplugging, holding power 30 seconds, reconnecting, and booting.
4. Confirmed hardware faults go to Asus support under warranty — not a DIY repair.

## Closing

On Asus laptops the post-24H2 black screen is a hybrid-graphics driver story in the large majority of cases, and the Caps Lock test proves it in seconds. Wake the display, roll back the driver, and finish on manufacturer drivers rather than the upgrade's generic ones. For the same black screen elsewhere, see the [Dell 24H2 black screen guide](/articles/how-to-fix-windows-11-24h2-black-screen-after-update-on-dell-laptop/), the [Acer 24H2 black screen guide](/articles/how-to-fix-windows-11-24h2-black-screen-after-update-on-acer-laptop/), and the [Lenovo 24H2 black screen walkthrough](/articles/how-to-fix-windows-11-24h2-black-screen-after-update-on-lenovo-laptop/).
