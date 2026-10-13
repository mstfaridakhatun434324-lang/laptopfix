---
title: "Blue Screen While Gaming on Windows 10? How to Fix It"
slug: how-to-fix-blue-screen-while-gaming-on-windows-10
date: 2026-09-13
categories: ["windows-errors"]
tags: ["blue screen", "gaming", "windows 10"]
description: "Blue screens only when gaming on Windows 10? Find out whether it's the GPU driver, overheating, RAM, or power — and fix it."
thumbnail: "/images/thumbs/how-to-fix-blue-screen-while-gaming-on-windows-10.webp"
faqs:
  - q: "Why does my laptop only blue-screen while gaming?"
    a: "Gaming uniquely stresses the GPU driver, thermals, RAM, and power delivery all at once. A weakness in any of them — an unstable GPU driver, clogged cooling, marginal RAM, or a weak charger — stays hidden during light use and only fails under gaming load."
  - q: "Is DDU safe to use?"
    a: "Yes, when used correctly: download it from the official source, run it in Safe Mode, and have your new GPU driver already downloaded before you start. It removes driver remnants that normal uninstalls leave behind, which is exactly what fixes stubborn driver-caused crashes."
  - q: "Can a game itself cause a blue screen?"
    a: "Rarely directly — user-mode game bugs crash the game, not Windows. But a game can trigger the crash by exercising a buggy GPU driver path, corrupted DirectX component, or overheating that nothing else reaches. The fault is still in the driver, hardware, or system components, not the game's code."
  - q: "Should I update my GPU driver to fix gaming crashes?"
    a: "A clean reinstall of a known-stable driver version — yes. But don't blindly grab the newest release; if crashes started right after a driver update, roll back instead. For NVIDIA and AMD, the stable driver from two or three releases ago is often the safest choice."
---

Your laptop runs fine for browsing and office work, then blue-screens twenty minutes into a game. That pattern is a diagnostic gift: gaming stresses the GPU, CPU, RAM, thermals, and power delivery simultaneously, which narrows the suspects dramatically.

Game-only crashes are almost always the graphics driver, overheating, unstable RAM, or the power supply sagging under load. Our [gaming crash reference](/articles/best-way-to-fix-blue-screen-while-gaming/) has the background; the steps below isolate which one is yours. Start at Fix 1.

## Why this happens

- An unstable or corrupted GPU driver crashing under 3D load.

- GPU or CPU overheating — gaming heat that desktop use never produces.

- RAM instability that only shows when games fill memory and stress the controller.

- An underpowered or aging power supply/charger sagging under gaming load.

- Overclocked GPU, CPU, or RAM (including factory overclocks) failing under sustained load.

- Corrupted DirectX or Visual C++ redistributables the game depends on.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Note the stop code and suspect file

Game crashes still leave the usual evidence. Capture it before changing anything.

1. Photograph the blue screen, noting the stop code and any **.sys** file named.

2. After rebooting, check **Event Viewer > Windows Logs > System** for the **BugCheck** entry.

3. Common gaming culprits: **nvlddmkm.sys** / **amdkmdag.sys** (GPU driver), **0x00000116** (VIDEO_TDR_FAILURE).

4. If it's VIDEO_TDR_FAILURE, the GPU driver is suspect number one — continue below.

### Fix 2: Clean-reinstall the GPU driver

Standard driver updates leave remnants behind. A true clean install with DDU is the real fix for driver-caused gaming crashes.

1. Download **Display Driver Uninstaller (DDU)** and the latest GPU driver (NVIDIA: [official download page](https://www.nvidia.com/Download/index.aspx); AMD: [AMD driver page](https://www.amd.com/en/support/download/drivers.html)).

2. Boot into **Safe Mode** and run DDU to remove the GPU driver completely.

3. Restart normally and install the fresh driver, choosing **Custom > Clean installation** if offered.

4. Test with the game that crashed — give it a full session, not five minutes.

### Fix 3: Monitor temperatures while gaming

Heat is the second-biggest gaming crash cause. Measure it instead of guessing.

1. Install **HWiNFO** and enable logging, or watch **GPU-Z** / **Core Temp** on a second monitor.

2. Play until just before the usual crash point and note peak **GPU** and **CPU** temps.

3. Sustained **90°C+** on the GPU or **95°C+** on the CPU means thermal trouble.

4. Clean vents with compressed air, use a cooling pad, and cap framerates to reduce load. Repasting helps chronic cases.

### Fix 4: Test the RAM

Games fill RAM and hammer the memory controller — marginal sticks crash here while passing desktop use.

1. Press **Win + R**, type `mdsched.exe`, and run the Windows Memory Diagnostic.

2. For certainty, run **MemTest86** from USB for 2+ passes.

3. If your RAM runs **XMP/EXPO**, disable it in BIOS and retest — gaming is where unstable memory overclocks die.

4. Replace faulty sticks; no driver tweak fixes bad RAM.

### Fix 5: Check power delivery

Gaming can double a laptop's power draw. A weak charger or battery causes crashes that look like GPU failures.

1. Game with the **original manufacturer charger** plugged in — not a third-party or underpowered one.

2. In **Control Panel > Power Options**, use **High performance** (not Power saver).

3. If the laptop only crashes on battery, the battery can't sustain gaming load — that's normal; game plugged in.

4. Try a known-good charger of the correct wattage if crashes persist.

### Fix 6: Repair DirectX and Visual C++ runtimes

Corrupted shared gaming components crash games and sometimes the display driver with them.

1. Download the **DirectX End-User Runtime** from Microsoft and install it.

2. In **Settings > Apps**, repair or reinstall the **Microsoft Visual C++ Redistributables** (both x86 and x64, all years).

3. Verify game files through **Steam > Properties > Installed Files > Verify integrity** (or the equivalent in your launcher).

4. Retest. Full DirectX guidance is on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Undo overclocks and test at stock

GPU/CPU/RAM overclocks — including manufacturer 'OC mode' utilities — are a top cause of load-only crashes.

1. Reset any GPU overclock in **MSI Afterburner** or similar to defaults.

2. Disable **XMP/EXPO** in BIOS and set any performance utility to **Balanced**.

3. Test the game at completely stock settings.

4. If crashes stop, your overclock was unstable — re-tune conservatively or leave it stock. Our [WHEA guide](/articles/how-to-fix-whea-uncorrectable-error-on-windows-10/) covers hardware-error crashes that often accompany this.

### Fix 8: Isolate the subsystem with separate stress tests

Instead of guessing between GPU and CPU, stress them independently. Whichever test crashes tells you which half of the machine to focus on — fifteen minutes each, definitive answer.

1. Download **FurMark** and run its GPU stress test for 15 minutes, watching temperatures.

2. If FurMark crashes or artifacts, the GPU side (driver, thermals, or card) is the problem.

3. Next, download **Prime95** and run **Small FFTs** for 15 minutes to hammer the CPU and RAM.

4. If Prime95 crashes it, suspect CPU thermals, RAM, or power delivery — not the graphics driver.

5. If both pass but the game still crashes, it's driver- or game-specific: clean-reinstall the GPU driver and verify game files.

6. Note peak temperatures from both tests — a crash at 97C and a crash at 70C are completely different diagnoses.

## Closing

Blue screens that only happen while gaming are the most diagnosable kind: the trigger is load, so the suspects are the GPU driver, heat, RAM, and power. Clean-reinstall the GPU driver with DDU, watch your temperatures, and test the RAM — that trio resolves the overwhelming majority of gaming crashes on Windows 10. And once it's stable, keep the GPU driver current but skip day-one 'game ready' releases unless the game you play needs them; a driver that's been out for two stable weeks beats a shiny new one that blue-screens. Stress-testing the GPU and CPU separately is the fastest way to split 'graphics problem' from 'system problem.' Note your peak temperatures during the tests too — the numbers make the difference between a heat issue and a driver issue obvious, and they tell a repair shop exactly where to look if it comes to that.
