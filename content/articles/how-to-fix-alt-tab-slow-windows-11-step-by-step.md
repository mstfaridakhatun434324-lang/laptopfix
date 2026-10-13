---
title: "Alt-Tab Slow on Windows 11? A Step-by-Step Fix That Works"
slug: how-to-fix-alt-tab-slow-windows-11-step-by-step
date: 2026-09-29
categories: ["performance"]
tags: ["alt tab slow", "windows 11", "task switching", "step by step"]
description: "Alt-Tab lagging on Windows 11? Follow this ordered, step-by-step guide to diagnose and fix slow task switching for good."
thumbnail: "/images/thumbs/how-to-fix-alt-tab-slow-windows-11-step-by-step.webp"
faqs:
  - q: "Why does Alt-Tab freeze for a few seconds on Windows 11?"
    a: "The freeze is usually the graphics pipeline stalling: the Desktop Window Manager waits on the GPU to finish its current work before compositing the task-switcher UI. Triggers include outdated display drivers, Game Bar hooks intercepting the keypress, exclusive-fullscreen games forcing a display mode change, and mixed refresh rates across monitors. The keyboard input itself registers instantly — the visible delay is all rendering."
  - q: "Is Alt-Tab lag a sign my laptop is dying?"
    a: "Almost never. Alt-Tab lag is a software and driver issue in the vast majority of cases, not failing hardware. Failing GPUs produce artifacts, crashes, and blue screens — not a consistent two-second delay on one specific shortcut. If Alt-Tab is the only slow thing on an otherwise healthy laptop, work through driver and overlay fixes before worrying about hardware."
  - q: "Does the Alt-Tab delay happen on Windows 10 too?"
    a: "It can, but Windows 11 changed the Alt-Tab UI to a more compositor-heavy design with rounded visuals and blur effects, which exposed GPU scheduling weaknesses that Windows 10's simpler switcher hid. The same fixes apply on both — update drivers, disable Game Bar, use borderless windowed mode — but Windows 11 users report it more often because the new switcher demands more from the GPU."
  - q: "Can I make Alt-Tab instant like it used to be?"
    a: "You can get very close. The classic-style instant switch returns when you remove the latency sources: updated GPU drivers, no overlay hooks, hardware-accelerated GPU scheduling set correctly for your system, and borderless windowed games. Some users also prefer the old Alt-Tab UI via registry tweaks, but that's cosmetic — the real speed comes from fixing the pipeline underneath."
---

Alt-Tab should be instant — it's the most-used shortcut in Windows, and when it lags, the whole computer feels broken. The good news: slow Alt-Tab on Windows 11 is one of the most fixable annoyances out there, because the causes are well understood and the fixes are concrete. This guide walks you through them in the order a technician would: quick wins first, deeper driver work second, edge cases last.

Each step tells you how to test whether it worked, so you stop as soon as your switches are snappy again. If task switching is slow because the entire machine is slow, detour first to [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); HP owners should also check the [HP-specific Alt-Tab guide](/articles/how-to-fix-alt-tab-slow-windows-11-on-hp-laptop/).

## Why this happens

- **Game Bar interception**: Xbox Game Bar hooks Alt-Tab system-wide, adding overlay latency to every press.
- **Display driver stalls**: The GPU context switch behind Alt-Tab stalls on outdated or buggy drivers.
- **Exclusive fullscreen games**: Alt-tabbing out of exclusive fullscreen forces a full display mode change.
- **Mixed refresh rates**: Different refresh rates on laptop panel vs. external monitor confuse the compositor.
- **Overlay software hooks**: Discord, NVIDIA, and Steam overlays each inject delay into the switch path.
- **Hardware-accelerated GPU scheduling mismatch**: The wrong HAGS setting for your driver version worsens switch latency.
- **Corrupted DWM state**: The Desktop Window Manager occasionally gets into a degraded state that only a reset clears.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable Xbox Game Bar and background recording

Step one for everyone — it takes 30 seconds and fixes the majority of cases.

1. Open **Settings** > **Gaming** > **Xbox Game Bar** and toggle it **Off**.
2. Open **Settings** > **Gaming** > **Captures** and disable **Record in the background while I'm playing a game**.
3. Press Alt-Tab five times in different apps right now — if the lag is gone, you're done.
4. If you rely on Game Bar recording, first try updating it via the **Microsoft Store**, then retest before disabling.
5. Leave it off for a full day of normal use to confirm the fix holds under real conditions.

### Fix 2: Switch games to borderless windowed mode

Eliminate the exclusive-fullscreen mode-change penalty.

1. Open your game's video/display settings and change **Display Mode** from **Fullscreen** to **Borderless Windowed** (sometimes called Borderless or Windowed Fullscreen).
2. Set the game's resolution to match your desktop resolution so the switch is seamless.
3. Alt-Tab out and back in — borderless switches should now be near-instant since no display mode change occurs.
4. Repeat for each game where you Alt-Tab frequently; keep competitive titles in whatever mode performs best in-game.
5. Note the small trade-off: borderless can add a frame or two of input latency in some titles — test your main games.

### Fix 3: Update your display drivers cleanly

Fix the GPU stalls underneath every switch.

1. Open **Device Manager** > **Display adapters** and note your GPU model(s).
2. Download the latest driver: NVIDIA from [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), AMD from AMD's official driver page, Intel from Intel's driver support site.
3. During NVIDIA installation choose **Custom** > **Perform a clean installation**; AMD and Intel installers have similar clean/factory-reset options.
4. Reboot when prompted — a clean driver install resets the whole graphics stack.
5. Test Alt-Tab in desktop apps and games; driver-caused delays typically disappear entirely after this.

### Fix 4: Audit and disable overlay software

Strip every hook between your keypress and the switch.

1. In **Discord**, go to **User Settings** > **Game Overlay** and turn off **Enable in-game overlay**.
2. In the **NVIDIA App**, open **Settings** and disable the **In-Game Overlay**.
3. In **Steam**, go to **Settings** > **In Game** and uncheck **Enable the Steam Overlay while in-game**.
4. Check **Task Manager** > **Startup apps** for other overlay tools (MSI Afterburner OSD, RivaTuner, recording software) and disable what you don't need.
5. Reboot and retest — then re-enable overlays one at a time if you miss them, testing Alt-Tab after each.

### Fix 5: Align refresh rates and display settings

Stop the compositor from tripping over mismatched displays.

1. Open **Settings** > **System** > **Display** > **Advanced display** and note the refresh rate of each connected display.
2. If your laptop panel is 120/144Hz and an external monitor is 60Hz, try setting both to 60Hz temporarily as a test.
3. On the same page, check **HDR** — disable it under **Settings** > **System** > **Display** if enabled, since HDR transitions add latency on some panels.
4. If you use multiple monitors with very different specs, test Alt-Tab with only the laptop display active (Win + P > PC screen only).
5. Keep the configuration that gives the fastest switches; reintroduce the second monitor afterward to confirm.

### Fix 6: Toggle hardware-accelerated GPU scheduling

Find the right HAGS setting for your driver version.

1. Open **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**.
2. Toggle **Hardware-accelerated GPU scheduling** to the opposite of its current value.
3. Restart the laptop — this change requires a reboot to take effect.
4. Use Alt-Tab heavily for a day (apps, browsers, games) and judge the responsiveness.
5. Keep the faster setting; there's no universally correct value — it depends on your GPU and driver version.

### Fix 7: Repair system files and reset the compositor

Clean up when the software stack itself is degraded.

1. Open **Command Prompt as administrator** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Install all pending updates via **Settings** > **Windows Update** — Microsoft has fixed DWM and Alt-Tab regressions in cumulative updates (see [Microsoft support](https://support.microsoft.com/en-us/windows)).
3. Open **Settings** > **System** > **Display** > **Graphics** and clear any experimental per-app GPU preferences.
4. As a final test, create a new local administrator account and try Alt-Tab there — fast switches in a fresh profile mean your main profile's shell settings are corrupt.
5. If the new profile is fast, migrate your files and settings over rather than fighting the old profile.

## Closing

Slow Alt-Tab is a pipeline problem, not a mystery: keypress → hooks → GPU → compositor, and every fix in this guide shortens one of those stages. Most people are fixed by step two or three — Game Bar off, borderless windowed, fresh drivers. Work the list in order, test after each step, and stop the moment your switches feel instant again.
