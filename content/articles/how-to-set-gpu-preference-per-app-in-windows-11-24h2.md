---
title: "How to Set Per-App GPU Preferences in Windows 11 24H2"
slug: how-to-set-gpu-preference-per-app-in-windows-11-24h2
date: 2026-10-09
categories: ["performance"]
tags: ["gpu preference per app", "windows 11 24h2", "graphics settings", "integrated vs discrete gpu"]
description: "Force demanding apps onto your discrete GPU and keep light apps on integrated graphics. A complete guide to per-app GPU preferences in Windows 11 24H2."
thumbnail: "/images/thumbs/how-to-set-gpu-preference-per-app-in-windows-11-24h2.webp"
faqs:
  - q: "What does setting a GPU preference per app actually do?"
    a: "On laptops with two GPUs — power-efficient integrated graphics and a powerful discrete GPU — Windows decides which GPU each app uses. The per-app preference overrides that decision for specific programs: set a game to High performance to force the discrete GPU, or set a browser to Power saving to keep it on integrated graphics. This gives you manual control over the performance-versus-battery-life tradeoff instead of trusting Windows' automatic assignment."
  - q: "Why is my game still using the wrong GPU after I set the preference?"
    a: "Usually you set the preference on the wrong executable — many games launch via helper .exe files, but the preference must target the actual rendering process. Other causes: the app overriding the choice with its own GPU selector, outdated drivers ignoring the OS hint, or the laptop's MUX switch / manufacturer utility forcing its own assignment. Check Task Manager's GPU Engine column to confirm which GPU the app actually landed on."
  - q: "Should I set everything to High performance GPU?"
    a: "No — that defeats the purpose of having two GPUs. Forcing light apps (browsers, chat, music players) onto the discrete GPU wastes battery, generates heat, and can actually hurt performance through unnecessary GPU switching. Reserve High performance for games, 3D renderers, video editors, and GPU-accelerated creative tools. Everything else belongs on Power saving (integrated), which is faster for 2D work and sips power."
  - q: "Do per-app GPU settings survive driver updates?"
    a: "Usually yes — the preferences are stored in the Windows graphics settings database, not in the driver, so routine driver updates preserve them. However, major Windows feature updates (like moving to 24H2) occasionally reset graphics preferences, and reinstalling an app to a new path orphans its old entry. After any feature update or driver clean-install with DDU, it is worth spending two minutes verifying your key apps still show the correct preference."
---

Your gaming laptop has two graphics chips: efficient integrated graphics for everyday work and a power-hungry discrete GPU for heavy lifting. Windows 11 is supposed to assign each app to the right one automatically — and frequently gets it wrong, running your game on integrated graphics (slideshow framerates) or your web browser on the discrete GPU (battery draining for no reason).

Per-app GPU preferences put you in charge: you tell Windows exactly which GPU each program may use. In Windows 11 24H2 the settings moved slightly and gained a few new behaviors, so this guide walks through the current interface step by step. Pair this with [hardware-accelerated GPU scheduling](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2/) for the full graphics-tuning picture, and check [fixing DWM high GPU usage](/articles/how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2/) if the desktop compositor itself is misbehaving.

## Why this happens

- **Windows auto-assignment is conservative**: The OS often defaults unknown apps to integrated graphics to save battery, which starves games and creative apps of the GPU they need.

- **Launchers vs. actual executables**: You set the preference on the launcher, but the game renders through a different .exe that never got the assignment.

- **Outdated GPU drivers**: Old drivers may ignore the OS preference hint entirely, especially NVIDIA/AMD drivers from before the feature matured.

- **Manufacturer utilities overriding Windows**: OMEN Hub, Armoury Crate, and similar tools can force their own GPU modes that beat Windows settings.

- **MUX switch in the wrong position**: Laptops with a multiplexer switch in iGPU-only mode physically cannot use the discrete GPU no matter what Windows says.

- **Preferences reset by updates**: Feature updates and clean driver installs can wipe or orphan per-app entries without telling you.

- **Apps with internal GPU selectors**: Some professional apps choose their own GPU in their preferences, overriding whatever Windows requests.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open the graphics settings the 24H2 way

The path moved slightly in recent Windows 11 builds; here is the current one.

1. Open **Settings > System > Display > Graphics** (scroll down in the Display page).
2. At the top, confirm **Default graphics settings** shows both GPUs if you have two — if only one appears, the discrete GPU may be disabled in BIOS or Device Manager.
3. Note the **Hardware-accelerated GPU scheduling** toggle here too; it interacts with per-app assignment.
4. This page lists apps you have customized under **Custom settings for applications** — empty on a fresh system.
5. Keep this page open; every fix below happens here.

### Fix 2: Add your app and set its GPU

The core procedure: register the exact executable, then assign it.

1. On the **Graphics** page, click **Add app** (or **Browse** for classic desktop apps) and navigate to the app's real .exe — for games, find the actual game binary in its install folder, not the launcher shortcut.
2. For Microsoft Store apps, choose **Microsoft Store app** from the dropdown instead of browsing.
3. Click the newly added app, click **Options**, and choose **High performance** (discrete GPU) or **Power saving** (integrated GPU).
4. Click **Save**, then fully close and relaunch the app — the preference applies at launch, not to running processes.
5. Verify in **Task Manager > Processes**: right-click columns, enable **GPU** and **GPU engine** to confirm the app landed on the intended GPU.

### Fix 3: Assign the right profile to each app type

A sensible policy beats random tweaking.

1. Set **High performance**: games, Blender, Premiere/DaVinci, OBS, CAD tools, and any app that stutters on integrated graphics.
2. Set **Power saving**: browsers, Discord/Slack, Spotify, Office apps, and launchers (Steam, Epic) — the launcher does not need the discrete GPU even if the game does.
3. Leave **Let Windows decide** for utilities and small tools where it genuinely does not matter.
4. After assigning, run each important app and confirm placement with Task Manager's GPU engine column.
5. Revisit after major app updates — some updaters replace the .exe path and orphan the preference entry.

### Fix 4: Fix apps that ignore the preference

When the setting seems to do nothing, one of these is usually overriding it.

1. Double-check you targeted the rendering .exe: in Task Manager, find the app's process while it runs, right-click > **Open file location**, and compare with your Graphics settings entry.
2. Check the app's own settings for a GPU/renderer selector (common in Adobe apps, Blender, and many games) and align it with your Windows choice.
3. Open your manufacturer's utility (OMEN Gaming Hub, Armoury Crate, Lenovo Vantage, Nitro Sense) and look for GPU mode settings — set to **Hybrid/Optimus** or **MSHybrid** so Windows retains control.
4. If your laptop has a **MUX switch** (check BIOS or the maker utility), ensure it is not locked to iGPU-only mode.
5. Update both GPU drivers — integrated from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or [AMD](https://www.amd.com/en/support/download/drivers.html), discrete from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or AMD — since stale drivers are a top cause of ignored preferences.

### Fix 5: Handle browsers and multi-window apps specially

Browsers and launchers need care because they spawn many processes.

1. For Chrome/Edge: set the main browser .exe to **Power saving** unless you do heavy WebGL work — this alone can add noticeable battery life.
2. If a specific web app needs GPU power, use a separate browser profile or a different browser assigned to High performance rather than flipping the main one.
3. For game launchers: assign the launcher to Power saving and the game binary to High performance — two entries, correct behavior.
4. For Discord/OBS streaming setups: keep Discord on Power saving but set OBS to High performance so encoding gets the strong GPU.
5. Test battery impact: run on battery for an hour of typical use and compare drain against your old settings.

### Fix 6: Use Task Manager to audit the whole system

A periodic audit catches apps that slipped onto the wrong GPU.

1. Open **Task Manager > Processes**, enable the **GPU engine** column, and sort by it.
2. Look for surprises: any light app on GPU 1 (discrete) that should be on GPU 0 (integrated), or any game stuck on GPU 0.
3. For each surprise, add or correct its entry in **Settings > System > Display > Graphics**.
4. Check **Task Manager > Performance > GPU** to see per-GPU utilization and confirm the discrete GPU actually idles during light work.
5. Repeat this audit after every Windows feature update, since 24H2-class upgrades are the most common preference wipers.

### Fix 7: Reset graphics preferences when everything is tangled

For systems where years of entries conflict, a clean slate is faster than archaeology.

1. In **Settings > System > Display > Graphics**, remove custom entries for apps you no longer use or recognize.
2. If behavior is truly bizarre, reset via registry is not recommended — instead, reinstall GPU drivers cleanly (DDU in Safe Mode), which often clears stale associations.
3. Re-add only your important apps (games, creative tools, browser) with deliberate choices from Fix 3's policy.
4. Verify each with Task Manager before moving on — five minutes of verification beats weeks of mysterious stuttering.
5. Document your final assignments somewhere (a note or screenshot) so the next feature update's reset costs you minutes, not detective work. Microsoft's official Windows support documentation covers this graphics settings feature if you need the reference.

## Closing

Per-app GPU preferences are one of the highest-leverage settings on a dual-GPU laptop: five minutes of assigning games to High performance and everyday apps to Power saving buys you both smoother framerates and longer battery life. Set them deliberately, verify with Task Manager, and re-check after major updates — Windows will not remind you when it forgets.
