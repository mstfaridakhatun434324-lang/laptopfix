---
title: "How to Fix NVIDIA App DLSS Not Working on Windows 11 Laptops"
slug: nvidia-app-dlss-not-working-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["nvidia", "dlss", "gaming laptop", "windows 11", "graphics", "troubleshooting"]
description: "DLSS missing or not working through the NVIDIA App on your laptop? Follow these step-by-step fixes for game support, driver settings, and overlay issues."
thumbnail: "/images/thumbs/nvidia-app-dlss-not-working-laptop.webp"
faqs:
  - q: "Why is DLSS missing from my NVIDIA App settings?"
    a: >
      The NVIDIA App shows DLSS options only when it detects a compatible RTX GPU with a current driver and the app itself is up to date. An outdated driver, an old NVIDIA App build, or running on the integrated GPU instead of the RTX card will hide the options entirely.
  - q: "Does DLSS work on every game?"
    a: >
      No — each game must include DLSS support built in by its developer. You can enable overrides for some games through the NVIDIA App, but if a game has no DLSS code at all, the feature cannot engage. Check the game's own graphics settings for a DLSS or upscaling entry.
  - q: "Why does DLSS cause stuttering on my laptop?"
    a: >
      Stuttering usually comes from the frame-generation pipeline conflicting with the game's frame pacing, or from the laptop hitting thermal limits while the GPU boosts. Try a lower DLSS quality preset, turn off frame generation, and make sure the laptop is plugged in with cooling adequate.
  - q: "Can I use DLSS and the iGPU for battery savings?"
    a: >
      No — DLSS is an NVIDIA RTX technology that requires the discrete GPU to be active and driving the game. Battery-saving iGPU modes will disable it. DLSS is a plug-in, high-performance feature, similar in spirit to how [DirectStorage needs specific hardware on ARM laptops](/articles/directstorage-not-working-arm-laptop/).
---

You installed the NVIDIA App, you own an RTX laptop, and DLSS is nowhere to be found — no toggle, no presets, games still rendering at native resolution. Or DLSS appears but enabling it changes nothing, or worse, it tanks your frame rate instead of raising it. On a gaming laptop you paid a premium for, that feels like money left on the table.

DLSS (Deep Learning Super Sampling) is NVIDIA's AI upscaling: the GPU renders the game at a lower internal resolution and the AI model reconstructs a sharp full-resolution image, buying you large frame-rate gains. The NVIDIA App is the modern control panel for it — driver overrides, per-game presets, and the overlay live there. When it breaks, the causes stack: an outdated Game Ready driver, the NVIDIA App running stale, the game itself lacking DLSS code, the laptop quietly running on integrated graphics, or an overlay conflict. Related gaming-stack quirks also show up in overlays like the [Widgets board not working on Windows 11](/articles/widgets-board-not-working-windows-11/) and in [Photos Cocreator not working](/articles/photos-cocreator-not-working/) — both features that misbehave when the GPU stack is unhealthy.

This guide gives you six fixes in order: confirm the game and GPU support DLSS, update the driver and the NVIDIA App, verify the game is actually using the RTX GPU, configure DLSS correctly per game, fix overlay and conflict issues, and do a clean reinstall. Start plugged in — DLSS never engages on battery saver.

## Why this happens

- **Outdated NVIDIA driver:** The NVIDIA App reads DLSS capabilities through the driver. A driver months out of date can hide DLSS options or break newer presets entirely.
- **Old NVIDIA App version:** The app's DLSS controls and override features are delivered through app updates. A stale app misses presets, the DLSS indicator, and per-game controls.
- **Game lacks native DLSS support:** DLSS must be compiled into the game by its developer. No built-in support means no DLSS — the app cannot inject it into every title.
- **Laptop running on integrated graphics:** Hybrid-GPU laptops default many games to the iGPU for battery savings. If the game launches on Intel or AMD integrated graphics, the RTX card — and DLSS — are invisible to it.
- **Wrong DLSS quality preset or frame generation mismatch:** Ultra Performance presets on an already-fast game, or frame generation on a title with unstable pacing, can look or feel worse than DLSS off.
- **Overlay and third-party conflicts:** Discord overlays, recording tools, and aggressive antivirus hooks can fight the NVIDIA overlay and break DLSS indicator and override controls.
- **Corrupted app or driver installation:** A partially updated app or a driver install that broke mid-way leaves the DLSS stack in a half-configured state — controls render but do nothing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the game actually supports DLSS

Chasing a toggle for a game that has no DLSS code is the most common time sink. Confirm support before changing anything.

1. Open the game's own graphics or display settings and look for **DLSS**, **NVIDIA DLSS**, or an **Upscaling** option.
2. If no such option exists anywhere in the settings, the game does not support DLSS — check the developer's patch notes to be sure it was never added.
3. If the option exists, set it to **Quality** mode and restart the game — some titles only apply DLSS after a full restart.
4. Note which games in your library show the option; you will use one of them as your test game for every step below.
5. For games with override support in the NVIDIA App, check the app's per-game section to see if DLSS overrides are offered for your test title.

### Fix 2: Update the GPU driver and the NVIDIA App

DLSS presets ship with the driver, and the app's controls ship with the app — update both before assuming anything is broken.

1. Open the NVIDIA App and check **Drivers** for a new Game Ready or Studio driver — download and install it, choosing **Custom > Clean install** if offered.
2. In the NVIDIA App, go to **Settings** and check for an app update; install it and restart the app.
3. Alternatively, grab the latest driver directly from the [official NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx) if the app fails to detect one.
4. Restart the laptop after both updates — the DLSS stack initializes at driver load time.
5. Reopen the NVIDIA App and check whether DLSS options and presets now appear for your test game.

### Fix 3: Force the game onto the RTX GPU

If Windows hands the game to the integrated GPU, DLSS is physically unavailable. Pin the game to the discrete card.

1. Open **Settings > System > Display > Graphics** in Windows 11.
2. Find your test game in the app list (or add it via **Browse** if missing) and click **Options**.
3. Select **High performance** — this is the RTX GPU — and click **Save**.
4. Also check your laptop maker's utility (NVIDIA Control Panel > Manage 3D settings > preferred GPU, or Armoury/Legion/Vantage) for a MUX switch or **Ultimate/DGPU** mode, and enable it if present.
5. Launch the game, open its settings, and confirm it now reports the RTX GPU — then check DLSS again.

### Fix 4: Configure DLSS correctly per game

With support confirmed and the right GPU active, misconfiguration is the remaining culprit. Set the preset deliberately instead of leaving it on auto.

1. In the NVIDIA App, open the per-game section for your test game.
2. Set the DLSS override to **Quality** (best image) or **Balanced** (best mix) — avoid Ultra Performance unless you need extreme frame rates at low resolution.
3. If the game offers **Frame Generation**, leave it off for your first test — it multiplies frames but can introduce stutter on unstable titles.
4. In-game, set the resolution to your display's native resolution and let DLSS do the upscaling — running a low in-game resolution with DLSS compounds softness.
5. Test for five minutes of actual gameplay, not just the menu — some menus render at fixed settings that ignore DLSS.

### Fix 5: Resolve overlay and software conflicts

The NVIDIA overlay hosts the DLSS indicator and some override controls. When third-party software fights it, DLSS features misbehave.

1. In the NVIDIA App settings, toggle the **In-Game Overlay** off, restart the app, then toggle it back on.
2. Disable competing overlays one at a time: Discord (User Settings > Game Overlay), Xbox Game Bar (**Settings > Gaming**), and any recording tool's overlay.
3. Temporarily pause third-party antivirus or system "optimizers" and retest — aggressive hooks can intercept the DLSS pipeline.
4. Close background apps that capture the screen (OBS, capture tools) before launching the game.
5. If DLSS now works, re-enable your overlays one at a time to find the specific offender.

### Fix 6: Clean reinstall the driver and the NVIDIA App

A corrupted installation can leave DLSS half-functional — options visible but inert. A full clean reinstall is the definitive reset.

1. Uninstall the NVIDIA App from **Settings > Apps > Installed apps**.
2. Use Display Driver Uninstaller (DDU) in Safe Mode to remove the GPU driver completely, or use the clean-install option from a fresh driver package.
3. Restart the laptop, then install the latest driver from [NVIDIA's official download page](https://www.nvidia.com/Download/index.aspx).
4. Reinstall the NVIDIA App from NVIDIA's site, sign in, and let it detect your GPU and games.
5. Configure DLSS per game from Fix 4 and test with your known-good title.

## Closing

DLSS on a laptop is a chain — game support, current driver, current app, RTX GPU active, sane preset — and any broken link reads as "DLSS not working." Work the chain in order and you will find the break quickly; in most cases it is the game running on the iGPU or a driver that is simply too old. Keep the NVIDIA App updated and you will keep picking up new DLSS presets and overrides automatically. And remember the honest limit: no driver trickery can add DLSS to a game that never shipped with it — for those titles, the game's own upscaling options are the best you get.
