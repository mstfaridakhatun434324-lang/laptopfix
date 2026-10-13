---
title: "Alt+Tab Lagging on Windows 11? Troubleshoot Slow Task Switching"
slug: alt-tab-slow-windows-11-troubleshooting
date: 2026-09-29
categories: ["performance"]
tags: ["alt tab", "task switching lag", "windows 11", "display issues"]
description: "Troubleshoot slow Alt+Tab on Windows 11: diagnose GPU, game-mode, and compositor causes of laggy task switching."
thumbnail: "/images/thumbs/alt-tab-slow-windows-11-troubleshooting.webp"
faqs:
  - q: "Why does Alt+Tab freeze my game for several seconds?"
    a: "Exclusive fullscreen games must surrender the display to Windows and take it back when you return — that teardown and rebuild takes seconds and occasionally hangs. The freeze is the GPU re-initializing the display pipeline. Switching the game to borderless windowed mode eliminates the freeze entirely because the game never leaves the normal window compositor."
  - q: "Can Alt+Tab slowness be caused by too little RAM?"
    a: "Indirectly, yes. When RAM is full, Alt+Tabbing to another app can trigger paging — Windows swapping memory to disk — which makes the switch feel extremely slow. If Task Manager shows memory above 90% during the lag, closing apps or adding RAM helps. But pure GPU-context-switch slowness happens even with free RAM, so check memory first to know which problem you have."
  - q: "Does refresh rate affect Alt+Tab speed?"
    a: "It can. Switching between a game running at one refresh rate and a desktop at another forces the display to re-sync, adding delay — especially on high-refresh monitors. Running both the game and desktop at the same refresh rate (in borderless windowed, the desktop rate governs) minimizes this. Mismatched rates are a subtle but real contributor."
  - q: "Why is Alt+Tab slow only in one specific game?"
    a: "Per-game differences come down to how each game handles focus loss and display mode: its fullscreen implementation, whether it pauses rendering when unfocused, and its anti-cheat's interference with the switch. Check that game's display settings (borderless windowed), disable its fullscreen optimizations via the exe properties, and look for game-specific patches — it's a game configuration issue, not a Windows one."
---

Alt+Tab used to be instant. Now there's a beat — sometimes a long one — between the keypress and the switch, and in games it can feel like the whole system locks up. Slow task switching on Windows 11 has several distinct causes, and troubleshooting it well means figuring out which layer is slow: the game's display mode, the GPU driver, the compositor, or system resources. Each has a different fix, and applying the wrong one wastes your time.

This guide is the diagnostic path: identify the slow layer, then fix it. For the quick-fix sequence, see [best way to fix slow Alt+Tab](/articles/best-way-to-fix-alt-tab-slow-windows-11/); for gaming performance broadly, our [power plan guide](/articles/how-to-change-power-plan-to-best-performance-on-windows-11/).

## Why this happens

- **Exclusive fullscreen context switches**: The display pipeline teardown/rebuild is inherently slow.
- **GPU driver inefficiency**: Old or buggy drivers add latency to every compositor operation.
- **Refresh-rate mismatches**: Game and desktop at different rates force display re-syncs on switch.
- **Memory pressure and paging**: Full RAM turns task switches into disk-swapping delays.
- **Fullscreen optimizations layer**: The compatibility shim adds overhead to the switch path.
- **Overlay software hooks**: Discord, GeForce Experience, and Game Bar overlays intercept the switch.
- **Windows compositor bugs**: Occasionally the DWM itself is the slow layer, fixed by updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Characterize the slowness

Different symptoms, different causes.

1. Time it: is the delay under a second (annoying), 2–5 seconds (broken-feeling), or a full freeze (something wrong)?
2. Note when it happens: only with games open, only with one specific game, or even switching between two browser windows?
3. Browser-to-browser slowness points to system resources or compositor issues; game-only slowness points to display mode and GPU.
4. Check Task Manager > **Performance** during a slow switch: GPU at 100%? Memory above 90%? Disk active? Each implicates a different layer.
5. Write down your pattern — it determines which of the fixes below matter for you.

### Fix 2: Fix the display mode (game-related slowness)

For slowness that only happens with games.

1. Switch the game to **Borderless Windowed** at native resolution — retest Alt+Tab immediately.
2. If the game lacks borderless mode, try **Windowed** maximized as a test — if that's fast, display mode is confirmed as the cause.
3. Match refresh rates: set the game's refresh to your desktop's rate in its video settings.
4. Disable **fullscreen optimizations** on the game exe (**Properties** > **Compatibility**) as an additional test.
5. If borderless fixes it, you're done with this layer — the remaining fixes are for non-game slowness.

### Fix 3: Investigate memory pressure

For slowness switching between regular apps.

1. Open Task Manager > **Performance** > **Memory** during normal use — sustained usage above 85–90% is the danger zone.
2. Sort **Processes** by Memory — browsers are the usual hogs; consider Memory Saver mode or fewer tabs.
3. Check the **Disk** tab during a slow Alt+Tab — heavy disk activity during the switch means paging, confirming RAM starvation.
4. Reduce startup apps via our [startup guide](/articles/how-to-disable-startup-programs-windows-11/) to free RAM at the source.
5. If RAM is constantly full and your laptop allows it, a memory upgrade is the real fix — 16GB is the comfortable minimum for heavy multitasking in 2026.

### Fix 4: Update and clean-install the GPU driver

For compositor-level slowness across everything.

1. Identify your GPU (Task Manager > **Performance** > **GPU**) and download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Use **DDU in Safe Mode** for a truly clean install if you've never done one — old driver remnants cause exactly this kind of latency.
3. After installing, test Alt+Tab between desktop apps first (no game running) — improvement here confirms a driver/compositor cause.
4. Toggle **Hardware-accelerated GPU scheduling** (**Settings** > **System** > **Display** > **Graphics**) and test both states after a restart each time.
5. Keep a note of which driver version worked — if a future update regresses, you'll know to roll back.

### Fix 5: Disable overlay and hook software

Overlays intercept the switch path.

1. Disable the **Xbox Game Bar** (**Settings** > **Gaming** > **Xbox Game Bar** > Off) and test.
2. Disable **Discord's overlay** (**User Settings** > **Game Overlay** > off) and its hardware acceleration.
3. Turn off **GeForce Experience/NVIDIA overlay** (Alt+Z > settings > in-game overlay off) or the AMD equivalent.
4. Test Alt+Tab after each disable — overlays stack, and sometimes it's the combination, not any single one.
5. Re-enable the ones you actually use once you've identified the offender — the goal is diagnosis, not permanent deprivation.

### Fix 6: Reset the desktop window manager

When the compositor itself is the slow layer.

1. Open Task Manager, find **Windows Explorer**, right-click > **Restart** — this refreshes the shell and task switcher.
2. For a deeper reset, sign out and back in (closes all apps — save work first).
3. Check **Settings** > **Windows Update** and install everything — DWM latency fixes ship in cumulative updates.
4. In **Settings** > **System** > **Multitasking**, try changing the Alt+Tab display option (windows only vs. windows+tabs) — fewer items in the switcher overlay can help.
5. If slowness appeared after a specific update, our [slow-after-update guide](/articles/windows-11-slow-after-update-how-to-fix/) covers rollback.

### Fix 7: Check for deeper system issues

When nothing above explains it.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated terminal — corrupt shell components cause bizarre UI latency.
2. Test in a **new local user account** — if Alt+Tab is fast there, your profile's shell configuration is corrupt.
3. Check Event Viewer (**Windows Logs** > **System**) for **nvlddmkm** or **amdkmdap** errors around the slow switches — driver crashes masquerading as lag.
4. Monitor CPU during switches — a background process spiking (see our [high CPU guide](/articles/how-to-fix-high-cpu-usage-step-by-step/)) can make everything feel slow.
5. Persistent, unexplained compositor lag on healthy hardware is rare — document your findings for a support case if you reach this point.

## Closing

Slow Alt+Tab is a layer cake: game display mode, GPU driver, overlays, memory, compositor. Diagnose which layer is slow by characterizing when it happens, fix that layer, and verify. Most cases resolve at Fix 2 or Fix 4 — borderless windowed and a clean GPU driver are the two moves that fix the overwhelming majority of laggy task switching.
