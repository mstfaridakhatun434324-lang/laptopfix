---
title: "dwm.exe High GPU Usage on an ASUS Laptop? Fixes That Work"
slug: how-to-fix-high-gpu-usage-dwm-exe-on-asus-laptop
date: 2026-09-30
categories: ["performance"]
tags: ["dwm.exe", "high gpu usage", "asus laptop", "desktop window manager", "gpu"]
description: "Desktop Window Manager spiking GPU on your ASUS laptop? Fix Armoury Crate interference, update graphics drivers, and calm dwm.exe."
thumbnail: "/images/thumbs/how-to-fix-high-gpu-usage-dwm-exe-on-asus-laptop.webp"
faqs:
  - q: "Why does dwm.exe use so much GPU on ASUS laptops?"
    a: "ASUS gaming and creator laptops combine powerful discrete GPUs with integrated graphics, MUX switches, and Armoury Crate's display controls — a complex pipeline the compositor must drive. Common triggers: Armoury Crate's GPU mode switching confusing DWM, outdated graphics drivers mishandling Windows 11's effects, Aura lighting overlays hooking the display path, and mismatched refresh rates on external monitors. The compositor works overtime whenever the display pipeline changes state unexpectedly."
  - q: "Does Armoury Crate cause dwm.exe GPU spikes?"
    a: "It can. Armoury Crate manages GPU modes (Eco/Standard/Ultimate), display refresh rates, and Aura lighting — all of which interact with the compositor. Bugs in mode switching have left DWM re-compositing continuously, and the lighting service's screen-sampling features (like Aura Sync with screen-reactive effects) directly increase compositor workload. If spikes correlate with Armoury Crate running, try exiting it completely as a diagnostic step."
  - q: "Should I use ASUS's GPU drivers or the chipmaker's?"
    a: "For ASUS laptops with MUX switches and Armoury Crate GPU modes, start with ASUS's drivers from your model's support page — they're validated against the MUX firmware and Armoury Crate's switching logic. Chipmaker-direct drivers sometimes break GPU mode switching or cause DWM instability on MUX systems. Only try NVIDIA/AMD/Intel direct drivers if ASUS's are very outdated and DWM issues persist, and be ready to roll back."
  - q: "Will disabling the MUX switch / Ultimate mode help?"
    a: "As a diagnostic, yes — Ultimate mode (dGPU direct to display) bypasses the iGPU entirely, which can stabilize a flaky hybrid handoff that keeps DWM resyncing. But Ultimate mode costs battery life and isn't always the real fix. Better: update both GPU drivers to ASUS's matched pair and let Standard/hybrid mode work normally. Use Ultimate mode as a test to confirm the hybrid path is the problem, then fix the drivers."
---

ASUS laptops — ROG Strix, Zephyrus, TUF, Vivobook Pro — pack some of the most complex display pipelines in the laptop world: integrated plus discrete GPUs, MUX switches, Armoury Crate GPU modes, Aura lighting, high-refresh panels. All of that is great for gaming, but it gives `dwm.exe` (Desktop Window Manager) a lot of ways to get confused — and a confused compositor burns GPU: 20–60% in Task Manager while the desktop sits still, fans ramping, battery draining.

The ASUS-specific suspects, in order: Armoury Crate's GPU/display management, mismatched or outdated graphics drivers (ASUS validates specific pairs for MUX systems), Aura lighting hooks, and external monitor refresh-rate mismatches. Work through them in that order.

First, verify dwm.exe is really the consumer: Task Manager > **Performance** > **GPU**, check which engine spikes. If Armoury Crate is running, exit it fully and watch for 10 minutes — that's your fastest diagnostic. For the Dell-flavored DWM guide, see [dwm.exe on Dell](/articles/how-to-fix-high-gpu-usage-dwm-exe-on-dell-laptop/); for the general 24H2 deep-dive, the [DWM on 24H2 guide](/articles/how-to-fix-dwm-high-gpu-usage-in-windows-11-24h2/) covers the compositor fundamentals.

## Why this happens

- **Armoury Crate GPU mode churn**: Eco/Standard/Ultimate switching leaving DWM re-compositing continuously.
- **Mismatched MUX driver pair**: iGPU and dGPU drivers from different generations confusing the switch.
- **Aura lighting screen sampling**: Reactive lighting effects forcing extra compositor passes.
- **Outdated ASUS-validated drivers**: Factory drivers predating Windows 11 24H2 compositor changes.
- **External monitor refresh mismatch**: High-refresh external + internal panel at different rates.
- **GameVisual / display profiles**: ASUS color profiles intercepting the display pipeline.
- **Overlay software**: Discord, GeForce Experience, and recorder overlays fighting the compositor.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with Armoury Crate fully exited

The fastest ASUS-specific diagnostic.

1. Right-click the Armoury Crate tray icon and choose **Exit** — then open Task Manager and end any remaining **ArmouryCrate** service processes.
2. Watch dwm.exe's GPU usage for 10–15 minutes of normal desktop use.
3. If it settles, Armoury Crate's display/GPU management was the trigger — proceed to Fix 2 to fix it properly rather than living without the app.
4. If nothing changes, Armoury Crate is innocent; continue to driver fixes.
5. Note your current GPU mode (Eco/Standard/Ultimate) before exiting — you'll want to test each mode later.

### Fix 2: Update Armoury Crate and set a stable GPU mode

Fix the management layer instead of removing it.

1. Open **Armoury Crate** > **Settings** > **About** > **Check for updates** — install all Armoury Crate, ASUS System Control Interface, and firmware updates.
2. Go to the **GPU mode** (or System Configuration) section and set it explicitly — **Standard** for daily use — rather than leaving it on auto-switching, which is the churn source.
3. Test each mode deliberately: run **Standard** for a day, note dwm.exe behavior; only use **Ultimate** when gaming (it bypasses the iGPU, stabilizing the compositor at the cost of battery).
4. In Armoury Crate's **Aura Sync**, set lighting to **Static** or turn off screen-reactive effects — reactive modes sample the display and load the compositor.
5. Disable Armoury Crate's **GameVisual** auto-switching if enabled — per-app color profiles intercepting the pipeline cause DWM overhead.

### Fix 3: Install ASUS's matched graphics driver pair

MUX systems need driver pairs that were validated together.

1. Go to ASUS support for your exact model and download the latest **Intel/AMD integrated** and **NVIDIA/AMD discrete** graphics drivers.
2. Install the integrated driver first, reboot, then the discrete driver with **Clean installation** checked.
3. Resist the urge to install chipmaker-direct drivers on MUX systems unless ASUS's are ancient — direct drivers have broken Armoury Crate GPU switching and caused DWM instability.
4. After installing, verify in Armoury Crate that GPU mode switching still works — broken switching after a driver update means the pair is incompatible; roll back.
5. Monitor dwm.exe for a full day; driver-pair issues sometimes take a sleep/wake cycle to manifest.

### Fix 4: Fix the MUX switch state

A confused MUX keeps the compositor re-negotiating the display path.

1. In Armoury Crate, switch GPU mode to **Ultimate**, let it apply (requires restart), and test dwm.exe for 20 minutes — this is the dGPU-direct diagnostic.
2. Switch back to **Standard**, restart, and test again — sometimes the switch cycle itself clears a stuck MUX state.
3. Check the BIOS (F2/Del at boot) for **MUX** / **dGPU mode** options on models that expose them — ensure the setting matches what Armoury Crate expects.
4. If your model has a manual MUX and Armoury Crate fights it, pick one control method and stick with it — conflicting controllers cause the churn.
5. Update the BIOS from ASUS support — MUX firmware fixes ship in BIOS updates.

### Fix 5: Align external monitor refresh rates

High-refresh externals are a classic DWM stressor on ASUS machines.

1. **Settings** > **System** > **Display** > **Advanced display**: check every connected display's refresh rate.
2. Zephyrus/Strix panels often run 165/240Hz while external monitors run 60/144Hz — try setting the external to match the internal, or vice versa, as a test.
3. Disconnect the external display entirely for 15 minutes — if dwm.exe normalizes, the multi-monitor config is the trigger.
4. Try different ports/cables (HDMI vs USB-C/DisplayPort) — bandwidth-limited connections force the compositor into odd paths.
5. In **NVIDIA Control Panel** > **Change resolution**, verify the external isn't running a scaled resolution — GPU scaling adds compositor work.

### Fix 6: Tone down effects and overlays

Reduce compositor load while the pipeline is fragile.

1. **Settings** > **Personalization** > **Colors** > **Transparency effects** off; **Settings** > **Accessibility** > **Visual effects** > **Animation effects** off (diagnostic).
2. Disable hardware acceleration in **Discord** (Settings > Advanced) and your browser (Settings > System) one at a time, testing dwm.exe after each.
3. Turn off the **GeForce Experience** in-game overlay and **Xbox Game Bar** (Settings > Gaming) during testing.
4. Close RGB control software beyond Armoury Crate (OpenRGB, SignalRGB) — multiple lighting controllers sampling the screen multiply compositor load.
5. Re-enable effects once the underlying issue is fixed — a healthy ASUS system handles all of them smoothly.

### Fix 7: Clean-reinstall drivers with DDU and verify

The thorough reset for stubborn cases.

1. Download **DDU** plus ASUS's current driver pair; boot into **Safe Mode**.
2. Clean the integrated driver, then the discrete driver, then reinstall integrated first, discrete second (clean install option).
3. Reinstall Armoury Crate from ASUS support only if you need it — otherwise run without it for a day to establish a clean baseline.
4. Check **Settings** > **Windows Update** for cumulative updates with compositor fixes; individual KBs are on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
5. For driver downloads beyond ASUS's page: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — use only if ASUS's drivers are the problem, and verify MUX switching survives.

## Closing

On ASUS laptops, dwm.exe GPU spikes trace back to the display pipeline's complexity — Armoury Crate's GPU management, MUX driver pairs, and Aura lighting all touch the compositor's path. Exit Armoury Crate to diagnose, update it and set a stable GPU mode, install ASUS's matched driver pair, and align your monitor refresh rates. The compositor goes back to sipping single-digit GPU, and your battery life returns with it.
