---
title: "Blue Screen While Gaming on Windows 11? Here's How to Fix It"
slug: blue-screen-while-gaming-bsod-windows-11
date: 2026-09-17
categories: ["windows-errors"]
tags: ["blue screen gaming", "bsod gaming", "gpu crash", "windows 11"]
description: "Crashing to a blue screen mid-game on Windows 11? It's usually GPU drivers, thermals, or unstable clocks — here's how to diagnose and fix each one."
thumbnail: "/images/thumbs/blue-screen-while-gaming-bsod-windows-11.webp"
faqs:
  - q: "Why does my PC only blue-screen while gaming?"
    a: "Games stress components that idle use never touches: the GPU at full load, high-wattage power delivery, maximum thermals, and aggressive driver code paths. A marginal GPU driver, overheating graphics card, unstable overclock, or weak power supply only fails under that load — which is why the desktop is fine and games crash."
  - q: "Is it my graphics card dying?"
    a: "Possibly, but don't assume it. Far more common are buggy GPU drivers, overheating from dust-clogged cooling, and unstable overclocks. Test in order: clean-install the GPU driver, monitor temperatures, reset clocks to stock. Only suspect the card itself when crashes persist at stock settings with clean drivers and healthy thermals."
  - q: "Which stop codes are common while gaming?"
    a: "VIDEO_TDR_FAILURE and VIDEO_SCHEDULER_INTERNAL_ERROR point at the GPU driver timing out. IRQL_NOT_LESS_OR_EQUAL and SYSTEM_SERVICE_EXCEPTION during games usually implicate the graphics driver too. WHEA_UNCORRECTABLE_ERROR during gaming suggests CPU or power-delivery hardware. The code narrows the suspect list dramatically — always note it."
  - q: "Can a weak power supply cause gaming blue screens?"
    a: "Yes, especially on desktops — but gaming laptops have their own version: an underpowered or failing AC adapter. If crashes happen only at peak load and the battery drains even while plugged in, the adapter can't feed the GPU. Test with the original manufacturer adapter at the correct wattage before suspecting anything else."
---

A blue screen that only strikes mid-game is telling you something specific: the failure lives in the parts of your system that gaming alone stresses. The GPU running at full tilt, power delivery at maximum draw, thermals at their peak, driver code paths that only execute under 3D load — desktop use never touches any of this, which is why everything seems fine until you launch a game. The stop code still matters (photograph it), but the "only while gaming" pattern already narrows the field to four suspects: GPU drivers, thermals, clocks, and power.

This guide is ordered by likelihood and cost: driver work first (free, most common), then thermals and clocks (free, very common), then power and hardware (where replacement enters the picture). If your crashes happen outside games too, start with our general [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) instead; for power-state crashes adjacent to gaming loads, see our [driver power state failure guide](/articles/driver-power-state-failure-windows-11-fix/), and for hardware-error stop codes see our [WHEA guide](/articles/whea-uncorrectable-error-windows-11-fix/).

## Why this happens

- **Buggy GPU drivers**: New game-ready drivers sometimes ship with regressions that crash specific titles or engines.
- **Overheating GPU/CPU**: Dust-clogged cooling can't shed gaming heat loads, and thermal protection triggers crashes.
- **Unstable overclocks**: GPU, CPU, or VRAM overclocks (including factory "OC" modes) that fail only under sustained load.
- **Insufficient power**: An underpowered or degrading AC adapter/charger can't feed peak gaming draw on laptops.
- **Failing GPU hardware**: Degrading VRAM or GPU silicon that errors only when hot and fully utilized.
- **Corrupt game/driver interaction**: Specific game engines triggering driver bugs (common after either updates).
- **Bad RAM**: Memory errors that only surface when games fill RAM and stress the memory controller.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the stop code and the trigger

Pattern recognition before anything else.

1. Photograph every blue screen — the stop code (VIDEO_TDR_FAILURE, IRQL, WHEA, etc.) and any named `.sys` file.
2. Note the trigger precisely: which game, how many minutes in, and whether it happens in menus or only in heavy scenes. Menu-only crashes suggest driver/UI issues; heavy-scene crashes suggest thermals, power, or clocks.
3. Check whether lowering the game's graphics settings delays or prevents the crash — if it does, you're looking at load-dependent causes (thermals, power, clocks) rather than a pure driver bug.
4. Open **Event Viewer** > **Windows Logs** > **System** and confirm the BugCheck entries match what you photographed.

### Fix 2: Clean-install the GPU driver

The single most effective gaming-crash fix.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) for your exact GPU — or Intel's driver assistant for Intel graphics.
2. Choose **Custom install** and tick **Clean installation** (NVIDIA) / **Factory reset** (AMD) to fully remove the old driver first.
3. If crashes started right after a driver update, do the reverse: install the previous known-good version instead.
4. Disable automatic driver updates via Windows Update for the GPU afterward if a specific version proves stable — Windows "helpfully" upgrading your GPU driver mid-diagnosis wastes days.

### Fix 3: Monitor temperatures under load

Heat is the silent gaming killer.

1. Install HWMonitor or HWiNFO and log CPU/GPU temperatures during 15 minutes of the crashing game.
2. Sustained GPU temps above 88–90°C or CPU above 95°C on a laptop indicate inadequate cooling — repaste territory or at minimum a deep clean.
3. Blast vents and fans with compressed air (short bursts, fans held still). On laptops, elevate the rear for airflow and test again — a 5°C drop that stops crashes confirms thermals.
4. Check that fans actually spin up under load; a dead fan produces exactly this symptom set, and replacement fans are cheap compared to the crashes they cause.

### Fix 4: Reset all overclocks to stock

Unstable clocks fail only under load — the textbook gaming-only crash.

1. Reset GPU clocks in MSI Afterburner or the vendor utility — including disabling factory "OC mode" profiles.
2. Enter the BIOS and disable XMP/DOCP memory profiles, returning RAM to stock speeds.
3. Disable CPU auto-overclock features (PBO, MCE, "performance enhancement") in the BIOS.
4. Retest the crashing game for at least an hour. If stock clocks fix it, any overclock you reintroduce must be validated with a full gaming session, not a five-minute benchmark.

### Fix 5: Verify power delivery

Peak gaming draw exposes weak power.

1. On a laptop: confirm you're using the original manufacturer adapter at the correct wattage — a 65W adapter on a gaming laptop that shipped with 200W+ guarantees load crashes.
2. Test with the battery removed if your model allows, and test with a known-good adapter of the right wattage if available.
3. Check for a swollen battery or a loose DC jack — both cause power interruptions under load that present as crashes.
4. On a desktop: verify the PSU wattage covers GPU + CPU peak draw with headroom, and that PCIe power cables are fully seated (a partially seated 8-pin is a classic).

### Fix 6: Test RAM and storage under load

Rule out the components games stress hardest.

1. Run Windows Memory Diagnostic (`mdsched.exe` > restart and check) — games fill RAM in ways desktop use doesn't.
2. Run `chkdsk C: /f /r` to rule out storage corruption of game and driver files.
3. If you have two RAM sticks, test gaming with one at a time — a marginal stick often fails only under gaming memory pressure.
4. Move the crashing game to a different drive temporarily; if crashes stop, the original drive has issues under sustained reads.

### Fix 7: Isolate game-specific vs. system-wide

Determine whether it's one game or your system.

1. Test with a different demanding game or a GPU stress test (FurMark, 3DMark demo). Crashes across everything = system issue (driver/thermal/power/hardware). Crashes in one game only = game or game-driver interaction.
2. For single-game crashes: verify game files (Steam > Properties > Installed Files > Verify), update the game, and check the game's forums for known crash threads with your GPU.
3. Try the game in windowed/borderless mode and with V-Sync on — both reduce peak load spikes that trigger marginal hardware.
4. As a last resort for single-game issues, use Display Driver Uninstaller (DDU) in Safe Mode for the most thorough driver purge possible, then install only the GPU vendor's driver.

## Closing

Gaming-only blue screens are load-dependent failures, and the fix order reflects that: drivers first, thermals and clocks second, power and hardware third. The diagnostic question that matters most is whether lowering load (settings, clocks, temperatures) changes the crash — if it does, you're chasing physics (heat, power, silicon limits), not software. Get the system stable at stock settings with clean drivers first; that's your baseline. Only then reintroduce overclocks, driver updates, and maxed settings one at a time, so the next crash tells you exactly which change caused it. For crashes that follow you out of games and onto the desktop, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) picks up the trail.
