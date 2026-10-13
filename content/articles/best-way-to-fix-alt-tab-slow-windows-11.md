---
title: "Alt+Tab Slow on Windows 11? The Best Way to Fix It"
slug: best-way-to-fix-alt-tab-slow-windows-11
date: 2026-09-28
categories: ["performance"]
tags: ["alt tab slow", "windows 11", "multitasking", "gaming lag"]
description: "Alt+Tab slow or laggy on Windows 11? Fix slow task switching with GPU, focus-assist, and game-mode tweaks that restore instant switching."
thumbnail: "/images/thumbs/best-way-to-fix-alt-tab-slow-windows-11.webp"
faqs:
  - q: "Why is Alt+Tab so slow on Windows 11?"
    a: "Slow Alt+Tab usually comes from the GPU struggling to switch contexts — especially with fullscreen games, where Windows must tear down and rebuild the entire display pipeline. Contributing factors include outdated GPU drivers, Focus Assist holding the switcher, hardware-accelerated GPU scheduling conflicts, and background apps consuming the GPU. On some systems, a Windows bug in the window manager adds latency that updates fix."
  - q: "Does fullscreen vs borderless windowed affect Alt+Tab speed?"
    a: "Enormously. Exclusive fullscreen games must release and reacquire the display when you Alt+Tab, which takes seconds and sometimes crashes. Borderless windowed (or windowed fullscreen) keeps the game in the normal window pipeline, making Alt+Tab nearly instant. If you Alt+Tab frequently, borderless windowed is the single biggest improvement you can make."
  - q: "Will disabling Focus Assist speed up Alt+Tab?"
    a: "It can help on systems where Focus Assist's notification handling interferes with the task switcher, though it's not the primary cause for most users. The bigger wins are GPU driver updates, borderless windowed mode, and disabling fullscreen optimizations per-game. Treat Focus Assist as a secondary tweak after the graphics fixes."
  - q: "Is slow Alt+Tab a sign my GPU is failing?"
    a: "Almost never — it's a software and configuration issue in the vast majority of cases. Failing GPUs show artifacts, crashes, and driver timeouts, not merely slow task switching. If Alt+Tab is your only symptom and games otherwise run fine, work through the driver and settings fixes before worrying about hardware."
---

You hit Alt+Tab and... wait. One second. Two. The screen flickers, the game minimizes with a stutter, and by the time you're on the desktop you've forgotten what you wanted to check. On Windows 10 this was instant; on Windows 11 it can feel broken — especially with fullscreen games. The slowdown lives at the intersection of the GPU, the window manager, and how your game presents itself to Windows. Fix the right layer and instant switching comes back.

The fastest win first: switch your game to **borderless windowed** mode. For the full fix sequence, keep reading. For general gaming performance, pair this with our [power plan guide](/articles/how-to-change-power-plan-to-best-performance-on-windows-11/); for overall system speed, [speeding up Windows 11](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Exclusive fullscreen games**: Releasing and reacquiring the display pipeline takes seconds by design.
- **Outdated GPU drivers**: Old drivers handle context switches inefficiently, adding latency to every switch.
- **Hardware-accelerated GPU scheduling conflicts**: HAGS helps some systems and hurts others — it's a per-system gamble.
- **Focus Assist interference**: Notification management can stall the Alt+Tab overlay.
- **Fullscreen optimizations**: Windows' compatibility layer for old games adds a switching penalty.
- **GPU maxed out by the game**: A fully saturated GPU has no headroom for the compositor's switch work.
- **Background apps using the GPU**: Browsers and Discord compete for the GPU during the switch.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Switch to borderless windowed mode

The single biggest Alt+Tab improvement.

1. In your game's video/display settings, change **Display Mode** from **Fullscreen** to **Borderless Windowed** (sometimes called Windowed Fullscreen).
2. Set the resolution to your monitor's native resolution — borderless at native res looks identical to fullscreen.
3. Test Alt+Tab immediately — switching should now be near-instant, with no display re-initialization.
4. Performance cost is minimal on modern systems (1–3% typically) — well worth the multitasking gain.
5. Some competitive players insist on exclusive fullscreen for the lowest latency; if that's you, the remaining fixes still help, but accept some switch delay as the price.

### Fix 2: Update your GPU driver cleanly

Stale drivers are the top systemic cause.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for your exact GPU.
2. For the cleanest result, use **DDU (Display Driver Uninstaller)** in Safe Mode to remove the old driver completely before installing the new one.
3. During NVIDIA/AMD install, choose **Custom** > check **Clean installation** if you'd rather skip DDU.
4. Restart and test Alt+Tab in both desktop apps and games — driver updates frequently include window-manager latency fixes.
5. Keep drivers current going forward — GPU vendors specifically optimize the Windows 11 compositor path in recent releases.

### Fix 3: Toggle Hardware-Accelerated GPU Scheduling

Test both states — the right one is system-specific.

1. Go to **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**.
2. Note the current state of **Hardware-accelerated GPU scheduling**, then toggle it to the opposite.
3. Restart (required for the change to take effect).
4. Test Alt+Tab responsiveness over a gaming session — on some laptops HAGS on is faster, on others it's slower.
5. Keep whichever setting switches faster — there's no universally correct answer, only what's correct for your hardware.

### Fix 4: Disable fullscreen optimizations per game

Remove the compatibility layer's switching penalty.

1. Find your game's `.exe` (right-click the shortcut > **Open file location**).
2. Right-click the exe > **Properties** > **Compatibility** tab > check **Disable fullscreen optimizations**.
3. Click **OK** and test — this forces the game through a simpler presentation path that switches faster.
4. If it helps, apply to your other frequent games; if a game behaves worse, uncheck it (per-game setting, no global risk).
5. This is especially effective for older games running on Windows 11's newer compositor.

### Fix 5: Turn off Focus Assist and Game Bar interference

Clear the OS-level obstacles.

1. **Settings** > **System** > **Notifications** > turn **Focus Assist** (Do not disturb) off, or at least disable its automatic rules.
2. **Settings** > **Gaming** > **Xbox Game Bar** — if you don't use it, turn it **Off**; its overlay hooks into the same pipeline as the task switcher.
3. Our [Game Bar guide](/articles/how-to-turn-off-game-bar-on-windows-10/) covers full removal if you want it gone entirely.
4. Also disable **Game Mode** temporarily as a test (**Settings** > **Gaming** > **Game Mode**) — it helps most systems but interferes on some.
5. Test Alt+Tab after each toggle to identify which one mattered on your system.

### Fix 6: Reduce GPU saturation

Give the compositor headroom to work with.

1. Lower in-game settings slightly (especially resolution scale and anti-aliasing) so the GPU isn't pegged at 100% — a saturated GPU can't service the switcher promptly.
2. Close GPU-hungry background apps before gaming: browsers with hardware acceleration, Discord's hardware acceleration (**Settings** > **Advanced**), streaming software.
3. In Task Manager > **Performance** > **GPU**, check utilization during gameplay — if it's pinned at 99–100%, that's your bottleneck for switching too.
4. Cap your frame rate slightly below max (in-game limiter or driver control panel) — this reserves GPU headroom and often *improves* Alt+Tab dramatically.
5. A GPU with 10–15% headroom switches tasks; a GPU at 100% makes you wait.

### Fix 7: Update Windows and reset the window manager

When it's an OS bug, not your settings.

1. **Settings** > **Windows Update** — install everything; Microsoft has shipped multiple Alt+Tab latency fixes in cumulative updates.
2. As a soft reset of the shell, restart **Windows Explorer** in Task Manager (right-click > **Restart**) — this refreshes the task switcher without rebooting.
3. Check **Settings** > **System** > **Multitasking** — ensure **Alt+Tab** is set to show your preferred window set (Open windows only vs. tabs can affect the overlay's workload).
4. If a specific update caused the slowdown, check our [slow-after-update guide](/articles/windows-11-slow-after-update-how-to-fix/) for rollback options.
5. Persistent, unfixable Alt+Tab lag on fully updated systems is rare — if you reach this point, it's worth checking for deeper GPU issues per our [high CPU guide](/articles/how-to-fix-high-cpu-usage-step-by-step/).

## Closing

Slow Alt+Tab on Windows 11 is a graphics-pipeline problem with a graphics-pipeline solution: borderless windowed mode, a clean current GPU driver, and enough GPU headroom for the compositor to do its job. Apply those three and the task switcher goes back to feeling instant — the way it should.
