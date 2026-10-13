---
title: "VIDEO_TDR_FAILURE on an Acer Laptop: How to Fix It"
slug: how-to-fix-video-tdr-failure-on-acer-laptop
date: 2026-10-12
categories: ["windows-errors"]
tags: ["video-tdr-failure", "acer", "gpu-driver"]
description: "VIDEO_TDR_FAILURE on an Acer laptop usually means the graphics driver timed out. Here is the complete Acer-specific fix sequence, step by step."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-acer-laptop.webp"
faqs:
  - q: "What causes VIDEO_TDR_FAILURE specifically on Acer laptops?"
    a: "The same things as anywhere — graphics driver timeouts — but Acer's mix of Intel, NVIDIA, and AMD configurations plus Acer Care Center's driver management adds wrinkles. The most common Acer-specific trigger is Windows Update replacing Acer's validated graphics driver with a generic one."
  - q: "Where do I get the right graphics driver for my Acer?"
    a: "From Acer's support site for your exact model first — those drivers are validated against your BIOS. Only if the problem persists should you try the GPU maker's reference driver (NVIDIA, AMD, or Intel's detection tool). Never rely solely on Windows Update for graphics drivers on Acer hardware."
  - q: "Can Acer Care Center fix driver problems automatically?"
    a: "Acer Care Center can check for and install Acer-released driver updates, which is a decent first pass. But it does not do clean installs, and it will not fix a corrupted driver — for VIDEO_TDR_FAILURE you usually need the manual clean-install process below."
  - q: "My Acer crashes only when gaming. Is the GPU dying?"
    a: "Probably not — load-only crashes are far more often heat or driver timeouts than dead hardware. Clean the vents, update the driver properly, and monitor temperatures before worrying about the GPU itself. A dying GPU crashes increasingly at idle too."
---
VIDEO_TDR_FAILURE (stop code 0x116) means your graphics driver stopped responding, Windows tried to reset it, and the reset failed. On Acer laptops — with their wide range of Intel, NVIDIA, and AMD graphics configurations — the fix is usually a proper driver reinstall done the Acer way. VIDEO_TDR_FAILURE (stop code 0x116) means your graphics driver stopped responding, Windows tried to reset it, and the reset failed. On Acer laptops — with their wide range of Intel, NVIDIA, and AMD graphics configurations — the fix is usually a proper driver reinstall done the Acer way.

This guide is tuned for Acer hardware: where to get validated drivers, how Acer's tools fit in, and the heat and BIOS checks that matter on Acer models. This guide is tuned for Acer hardware: where to get validated drivers, how Acer's tools fit in, and the heat and BIOS checks that matter on Acer models.

## Why this happens

- **Windows Update replaced Acer's graphics driver.** A generic driver that does not understand Acer's power management causes timeouts.
- **Corrupted graphics driver files.** Partial updates or disk errors leave the driver half-broken.
- **Overheating.** Acer's thin models throttle hard; a dust-choked GPU stops responding inside the two-second TDR window.
- **Outdated BIOS.** Acer fixes GPU power-state handling in BIOS updates on several model lines.
- **Conflicting overlay or recording software.** Screen recorders and game overlays hook the graphics pipeline and destabilize recovery.
- **Failing GPU hardware.** The least common cause, but real — usually shows as crashes spreading from load-only to idle over weeks.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Get the Acer-validated graphics driver

Acer tests these against your exact model's BIOS and power delivery — start here, not with generic drivers. Acer tests these against your exact model's BIOS and power delivery — start here, not with generic drivers, because TDR is often a power-management mismatch.

1. Find your exact model number (sticker on the bottom or **Acer Care Center > My System**).
2. Download the latest VGA/graphics driver for that model from Acer's support site.
3. Keep the installer handy — you will use it after the clean uninstall in the next fix.

### Fix 2: Clean-uninstall the current graphics driver

A regular update leaves corrupted files behind; this wipes them completely. A regular update leaves corrupted files behind; this wipes them completely, including the registry entries a standard uninstall misses.

1. Open **Device Manager** (**Win + X > Device Manager**) and expand **Display adapters**.
2. Right-click your GPU, choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.
3. Restart the laptop. Windows will load a basic display driver — the screen may look low-resolution, which is normal.
4. Run the Acer driver installer you downloaded, choose a clean/custom install if offered, and restart again.

### Fix 3: Update the BIOS from Acer

Several Acer model lines have BIOS fixes specifically for GPU timeout behavior. Several Acer model lines have BIOS fixes specifically for GPU timeout behavior — check the BIOS changelog for graphics or power-management mentions.

1. On Acer's support page for your model, check the BIOS section for a newer version than yours (check yours with `msinfo32` > **BIOS Version/Date**).
2. Connect AC power — never flash on battery.
3. Run the BIOS update and leave the machine completely alone until it reboots itself.
4. Retest with whatever workload triggered the crashes.

### Fix 4: Rule out heat

Load-only TDR crashes are the signature of a thermal problem. Load-only TDR crashes are the signature of a thermal problem — a GPU that is fine at idle but times out under load is almost always heat, not a dead chip.

1. Install HWMonitor and watch GPU temperature during the crashing workload.
2. Sustained readings above 90C mean cooling trouble: with the laptop off, blow compressed air through the intake and exhaust vents.
3. Use a cooling pad and make sure the laptop sits on a hard surface, not bedding.
4. On models over two years old, dried thermal paste is a likely culprit — a shop repaste is quick and cheap. If you need to read crash details, first [disable automatic restart](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) so the screen stays visible.

### Fix 5: Remove overlays and recording software temporarily

These inject into the graphics pipeline and are notorious TDR triggers. These inject into the graphics pipeline and are notorious TDR triggers — overlays are the first thing to suspect when crashes happen in games but never on the desktop.

1. Uninstall or disable Discord overlay, GeForce Experience overlay, Xbox Game Bar, OBS, and similar tools.
2. Test for a day or two with everything off.
3. If crashes stop, re-enable them one at a time to find the offender, then check that product for updates.

### Fix 6: Try the GPU maker's reference driver

If Acer's validated driver still times out, the reference driver is the next experiment. If Acer's validated driver still times out, the reference driver is the next experiment — but be ready to come straight back if timeouts worsen.

1. For NVIDIA, download from [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx); for AMD, [AMD's driver page](https://www.amd.com/en/support/download/drivers.html); for Intel, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Do a clean uninstall (Fix 2) before installing the reference driver.
3. If timeouts get worse, roll straight back to the Acer driver — that tells you the Acer-validated version was correct and something else (heat, hardware) is wrong.

### Fix 7: Check for hardware failure

The last resort, after drivers and heat are exhausted. Disable the discrete GPU in Device Manager and run on integrated graphics for a day — if crashes vanish, the discrete GPU or its driver is implicated.

1. Disable the discrete GPU in **Device Manager** and run on integrated graphics for a day — if crashes vanish, the discrete GPU or its driver is implicated.
2. Run Acer's built-in hardware diagnostics (usually **F2** at boot > **Diagnostics**) for a GPU check.
3. If the GPU fails diagnostics or crashes spread to idle use, contact Acer support while under warranty, or a repair shop after. Related reading: our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

On Acer laptops, VIDEO_TDR_FAILURE is a driver-and-heat story far more often than a dead-GPU story. Get Acer's validated graphics driver installed cleanly, bring the BIOS current, and make sure the cooling is actually working — that trio resolves the overwhelming majority of cases. Keep a note of the exact driver version that finally worked — Acer's driver pages get updated, and knowing your known-good version saves you if a future update regresses.
