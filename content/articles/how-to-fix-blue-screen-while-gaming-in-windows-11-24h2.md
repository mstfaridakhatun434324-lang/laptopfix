---
title: "Blue Screen While Gaming in Windows 11 24H2? Here's the Fix"
slug: how-to-fix-blue-screen-while-gaming-in-windows-11-24h2
date: 2026-10-01
categories: ["windows-errors"]
tags: ["bsod", "gaming", "24h2", "gpu"]
description: "Blue screen only when gaming on Windows 11 24H2? That's a GPU, driver, heat, or power issue. Here's how to pin it down and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-blue-screen-while-gaming-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my laptop only blue screen while gaming?"
    a: "Gaming is the heaviest sustained load your laptop handles — max GPU, max CPU, max heat, max power draw. Faults that stay hidden during browsing (a flaky GPU driver, marginal VRAM, overheating, an underpowered charger) only surface when everything is stressed at once."
  - q: "Is it my graphics card dying?"
    a: "Possibly, but don't assume it. Outdated or corrupt GPU drivers cause more gaming BSODs than dying hardware. Test drivers, temperatures, and RAM before concluding the GPU is failing — especially on laptops where the GPU can't be replaced separately."
  - q: "Can overheating cause blue screens while gaming?"
    a: "Yes — it's one of the top causes on laptops. Sustained 95°C+ on the CPU or GPU package causes instability crashes. If crashes happen 20–40 minutes into a session rather than immediately, heat is the prime suspect."
  - q: "Should I use the charger that came with my laptop?"
    a: "Absolutely. Gaming laptops need their full wattage — a 65W USB-C charger on a laptop that shipped with a 200W brick will cause power starvation crashes under load. Always game on the original charger, plugged into the wall (not a power strip full of devices)."
---

A blue screen that only appears mid-game is actually a helpful symptom: it tells you the trigger is load. Web browsing barely wakes your GPU; gaming pins the CPU, GPU, memory, thermals, and power delivery at maximum simultaneously. Whatever is marginal in your system — driver, cooling, RAM, or power — gaming finds it.

The diagnostic approach is to stress each subsystem separately until you find the one that breaks. Here's the order that works.

## Why this happens

- **Corrupt or outdated GPU drivers**: The most common cause. Gaming exercises driver paths that nothing else touches, so a damaged graphics driver crashes only under 3D load.
- **Overheating under sustained load**: Laptop cooling is marginal by design. Dust, dried thermal paste, or blocked vents push temps past stability limits 20–40 minutes into a session.
- **Unstable GPU/CPU overclock or undervolt**: Factory or user overclocks that are fine on the desktop become unstable when the silicon is hot and fully loaded.
- **Failing VRAM or system RAM**: Memory errors that never surface in light use appear when games fill VRAM and system RAM to capacity.
- **Insufficient power delivery**: Wrong charger, failing charger, or degraded battery (on laptops that supplement from battery under peak load) causes power starvation crashes.
- **A specific game triggering a driver bug**: Sometimes it's not your hardware at all — one game with a particular engine hits a driver bug that others don't.

## How to fix it

Work through these in order — software and thermals before hardware conclusions.

### Fix 1: Clean-install the latest GPU driver

Don't just update — wipe the old driver completely. Corrupt remnants survive normal updates.

1. Download **DDU (Display Driver Uninstaller)** and the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Boot into Safe Mode (**Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now** > **Troubleshoot** > **Startup Settings**).
3. Run DDU, select your GPU brand, and choose **Clean and restart**.
4. After reboot, install the fresh driver you downloaded. Choose the **Studio/Stable** branch over bleeding-edge Game Ready if crashes persist — newer isn't always more stable.
5. Test with the game that crashed. If it's stable for several sessions, you're done.

### Fix 2: Monitor temperatures and fix cooling

If crashes take 20+ minutes to appear, this is probably your fix.

1. Install HWMonitor or HWiNFO and log CPU/GPU temps during a gaming session.
2. Sustained temps above 95°C on either package indicate a cooling problem.
3. Blow out vents and fans with compressed air (hold fan blades still).
4. Elevate the rear of the laptop for airflow — even bottle caps work — or get a cooling pad.
5. On laptops older than 2–3 years running hot, repasting the CPU/GPU with quality thermal paste often drops temps 10–15°C.
6. In the game's settings, cap the frame rate and drop from Ultra to High — massively less heat for barely visible difference.

For update-related gaming crashes specifically, see the [blue screen while gaming after update guide](/articles/how-to-fix-blue-screen-while-gaming-after-windows-11-update/).

### Fix 3: Reset overclocks and undervolts

Stability first, performance second — at least for diagnosis.

1. Reset MSI Afterburner (or your OC tool) to defaults — zero out core/memory offsets.
2. If you undervolt with ThrottleStop or Intel XTU, reset all offsets to 0.
3. In BIOS, disable XMP memory profiles (set to **Auto**).
4. Game for a few days at stock. If crashes stop, re-apply tuning gradually — your previous settings weren't as stable as they seemed.

### Fix 4: Test with the original charger on wall power

Power starvation masquerades as every other kind of crash.

1. Use only the charger that shipped with the laptop — check the wattage printed on the brick matches what the laptop expects.
2. Plug directly into a wall outlet, not a crowded power strip.
3. If your laptop supplements from the battery under peak load (many gaming models do), check battery health: **Terminal (Admin)** > `powercfg /batteryreport` and open the generated HTML file.
4. A swollen or heavily degraded battery can cause power-delivery instability — if the bottom panel doesn't sit flat, stop using it and replace the battery before anything else.

### Fix 5: Stress-test components individually

Isolate which subsystem breaks under load.

1. **GPU**: Run FurMark or 3DMark's stress test for 20 minutes. Artifacts or crashes point at the GPU/driver.
2. **CPU**: Run Cinebench multi-core a few times. Crashes here with a cool GPU point at CPU/RAM/power.
3. **RAM**: `mdsched.exe` (**Win + R**) > **Restart now and check for problems**. Gaming fills RAM; bad cells crash games first.
4. If only one test crashes, you've found your subsystem. If all pass for 30+ minutes but games still crash, suspect a specific game/driver interaction (Fix 6).

Driver-level memory crashes under load overlap with [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/) — check that guide if your dumps name driver files.

### Fix 6: Test with different games and settings

Determine whether it's your system or one game's engine.

1. Try 2–3 different games, ideally on different engines (e.g., one Unreal, one Unity, one proprietary).
2. If only one game crashes, verify its files (Steam: **Library** > right-click game > **Properties** > **Installed Files** > **Verify integrity**), update it, and check its forums for known crash issues on 24H2.
3. Disable overlays one by one — Discord, GeForce Experience, Steam, Xbox Game Bar overlays all hook the rendering pipeline and cause game-specific crashes.
4. Try the game in borderless windowed vs. exclusive fullscreen; some driver bugs only trigger in one mode.

### Fix 7: Repair Windows' gaming and system components

When hardware tests pass and drivers are clean, the OS itself may be damaged.

1. Open **Terminal (Admin)** (**Win + X**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Reinstall DirectX runtimes and Visual C++ redistributables (the all-in-one packages from Microsoft) — games depend on these and they do get corrupted.
4. Check [Microsoft's Windows support page](https://support.microsoft.com/en-us/windows) for known 24H2 gaming issues and their patches.
5. As a final step, use **Settings** > **System** > **Recovery** > **Reset this PC** > **Keep my files** for a clean OS with your data intact.

If your crashes happen on a Lenovo specifically, the [Lenovo blue screen after update guide](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/) covers OEM-specific driver issues.

## Closing

Gaming BSODs feel random, but they're the most diagnosable crashes you can get — the trigger is load, so you test under load until something breaks. For most people the answer is a clean GPU driver install or a cooling fix, both free and both under an hour. Work the list, stress-test honestly, and don't declare the GPU dead until drivers, heat, RAM, and power have all been cleared — on a laptop, that diagnosis is expensive to get wrong.
