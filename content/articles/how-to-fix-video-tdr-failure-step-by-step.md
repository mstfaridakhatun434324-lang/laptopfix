---
title: "How to Fix VIDEO_TDR_FAILURE Blue Screen Step by Step"
slug: how-to-fix-video-tdr-failure-step-by-step
date: 2026-09-26
categories: ["windows-errors"]
tags: ["bsod", "video-tdr-failure", "gpu-driver"]
description: "Fix the VIDEO_TDR_FAILURE blue screen step by step — clean GPU driver reinstall, TDR tweaks, and hardware checks that work."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-step-by-step.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout Detection and Recovery. Windows noticed your graphics driver stopped responding for about two seconds, tried to reset it, and the reset failed — so the system crashed. The filename in brackets, like nvlddmkm.sys or amdkmdag.sys, tells you which GPU driver was involved."
  - q: "Is VIDEO_TDR_FAILURE a sign my GPU is dying?"
    a: "Not necessarily. Most cases are driver bugs, unstable overclocks, or overheating. A dying GPU is possible but it's the least common cause — rule out drivers, heat, and power issues first before assuming hardware failure."
  - q: "Why does it happen when I play games or watch videos?"
    a: "Because that's when the GPU is under load. A marginal driver, an unstable overclock, or heat buildup only shows up when the graphics card is actually working hard, which is exactly what games and video playback demand."
  - q: "Should I update or roll back my graphics driver?"
    a: "If the crashes started after a driver update, roll back. If they started out of nowhere on an old driver, update to the latest stable release. Either way, do a clean install with Display Driver Uninstaller so no remnants of the old driver remain."
---
# How to Fix VIDEO_TDR_FAILURE Blue Screen Step by Step

**VIDEO_TDR_FAILURE** (often with `nvlddmkm.sys`, `amdkmdag.sys`, or `igdkmd64.sys` in brackets) means Windows tried to reset a hung graphics driver and failed. The screen freezes for a couple of seconds, maybe flickers, then the blue screen hits. It's jarring, but the fix path is well mapped.

The strategy: remove every trace of the bad graphics driver and install a clean, stable one, then address heat, overclocks, and power. Follow the steps in order — each one eliminates a category of causes. If your crashes involve other driver stop codes too, our [driver power state failure guide](/articles/driver-power-state-failure-windows-11-fix/) covers the related family of errors.

## Why this happens

- **Corrupted or buggy GPU driver:** The number one cause — a bad install, a regression in a new release, or remnants of an old driver conflicting with the new one.
- **Unstable overclock:** Factory or manual GPU/memory overclocks that aren't fully stable under sustained load.
- **Overheating:** Dust-clogged fans or dried thermal paste pushing the GPU past its thermal limit during games or video.
- **Insufficient or unstable power:** A failing charger or degraded battery on a laptop starving the GPU under load.
- **Failing GPU hardware:** Least common, but possible — usually shows artifacts (glitches, colored blocks) before crashing.
- **Conflicting software:** Screen recorders, overlays, and "game booster" utilities hooking into the graphics pipeline.

## How to fix it

Work through these in order. The clean driver reinstall in Fix 2 resolves most cases on its own.

### Fix 1: Note which driver file is named

The stop code usually names the failing driver — that tells you which GPU to focus on.

1. When the blue screen appears, look for the filename in parentheses after VIDEO_TDR_FAILURE.
2. `nvlddmkm.sys` means NVIDIA, `amdkmdag.sys` means AMD, `igdkmd64.sys` or `igdkmdnd64.sys` means Intel graphics.
3. If you can't catch it in time, [disable automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) so the screen stays put.
4. Write the filename down — you'll need it in Fix 2.

### Fix 2: Clean-reinstall the graphics driver with DDU

A standard driver update often leaves the corrupted files in place. Display Driver Uninstaller removes everything, so the fresh install starts clean.

1. Download **Display Driver Uninstaller (DDU)** from its official site and the latest stable graphics driver from the manufacturer — [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) — but don't install the driver yet.
2. Disconnect from the internet (unplug Ethernet or turn off Wi-Fi) so Windows Update can't sneak in its own driver mid-process.
3. Boot into **Safe Mode** (**Settings > System > Recovery > Advanced startup > Restart**, then **Troubleshoot > Advanced options > Startup Settings**).
4. Run DDU, select your GPU brand, and click **Clean and restart**.
5. After reboot, install the driver you downloaded — choose **Custom install** and tick **Clean installation** if the installer offers it.
6. Reconnect to the internet and test with the game or video that used to crash.

### Fix 3: Roll back if a recent update started it

If the crashes began right after a driver update, the new driver itself is the problem.

1. Open **Device Manager** (**Win + X**), expand **Display adapters**, and double-click your GPU.
2. Go to the **Driver** tab and click **Roll Back Driver**; pick the reason and confirm.
3. If the button is greyed out, use DDU (Fix 2) and manually install the previous driver version from the manufacturer's archive.
4. Consider pausing driver updates: in **Settings > Windows Update > Advanced options**, toggle off **Receive updates for other Microsoft products**, or use the manufacturer's control panel to block auto-updates.

### Fix 4: Remove overclocks and reset GPU settings

An overclock that's stable in benchmarks can still TDR-crash in specific games.

1. If you use MSI Afterburner or similar, reset everything to stock clocks and close the tool.
2. In the NVIDIA Control Panel or AMD Software, restore default 3D settings.
3. For laptops with manufacturer overclocking utilities (often preinstalled on gaming models), set them to **Balanced** or stock.
4. Test stability for a few days before reapplying any overclock — and stress-test properly if you do.

### Fix 5: Fix overheating

Heat-induced TDR failures creep in gradually as dust builds up or thermal paste ages.

1. Install **HWiNFO** or your GPU maker's monitoring tool and watch temperatures during the crashing workload.
2. Sustained temperatures above 85–90°C on a laptop GPU are a red flag.
3. Blast dust from vents and fans with compressed air (short bursts, fans held still).
4. On older laptops, consider a repaste — dried thermal paste is a classic cause of load-only crashes. This means opening the laptop, so only attempt it if you're comfortable; otherwise a repair shop charges modestly for it.
5. Use a cooling pad and keep rear vents unobstructed during heavy use.

### Fix 6: Rule out power problems

A GPU that can't draw stable power will hang exactly the way TDR describes.

1. Always game and render on the **original charger**, plugged directly into the wall — not a dock or underpowered USB-C adapter.
2. Check the charger brick for excessive heat or damage, and try a known-good charger if you have one.
3. In **Settings > System > Power & battery**, set the power mode to **Best performance** while testing.
4. If crashes only happen on battery, the battery may be too degraded to sustain GPU boost clocks — check its health report with `powercfg /batteryreport`.

### Fix 7: Adjust the TDR delay as a diagnostic step

Lengthening the timeout Windows allows before resetting the GPU can distinguish a slow driver from a truly hung one.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a new **DWORD (32-bit)** named `TdrDelay` and set it to `8` (seconds, up from the default 2).
3. Optionally add `TdrDdiDelay` set to `10`.
4. Restart and test. If crashes stop, the driver was just slow (common with heavy scenes); still update the driver, because the underlying slowness remains.
5. If crashes continue unchanged, the GPU is genuinely hanging — revert the values (delete the keys) and continue to Fix 8.

### Fix 8: Test the GPU hardware

If everything software-side is clean, test the hardware itself.

1. Run a GPU stress test like **FurMark** or **3DMark** and watch for artifacts — colored blocks, flickering textures, or geometry glitches point to dying VRAM or a dying core.
2. If your laptop has switchable graphics, force the crashing app to the integrated GPU (**Settings > System > Display > Graphics**) — if crashes stop, the discrete GPU is the problem.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an admin Terminal to rule out system-file involvement.
4. Persistent artifacts under load after a clean driver install mean the GPU is failing — back up your data and talk to the manufacturer about repair options while the laptop is still usable.

## Closing

VIDEO_TDR_FAILURE is a driver problem until proven otherwise: clean-reinstall with DDU, undo bad updates and overclocks, then check heat and power. The TDR delay tweak and stress tests are your tiebreakers when the obvious fixes don't stick. Take it step by step and you'll either fix the crash or know with confidence that the hardware needs professional attention.
