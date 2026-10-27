---
title: "How to Fix Baldur's Gate 3 Issues on Your ARM Laptop"
slug: balders-gate-3-arm-laptop-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["baldurs gate 3", "arm laptop", "snapdragon", "game crashes", "windows 11", "troubleshooting"]
description: "Fix Baldur's Gate 3 crashes, stuttering, and launch failures on your ARM laptop with step-by-step repairs for graphics, DirectX, and power settings today."
thumbnail: "/images/thumbs/balders-gate-3-arm-laptop-issues-fix.webp"
faqs:
  - q: "Why does Baldur's Gate 3 crash on my ARM laptop?"
    a: "Most crashes come from the game's x64 code running through Windows on ARM emulation, an outdated Adreno graphics driver, or a corrupted Vulkan or DirectX shader cache. Updating the driver and clearing the cache fixes the majority of cases."
  - q: "Can an ARM laptop run Baldur's Gate 3 well?"
    a: "Yes, for a story-driven RPG it can run acceptably at modest settings once the driver and power settings are right. Expect lower frame rates than a comparable x86 gaming laptop, and keep shadows and volumetrics low for the smoothest experience."
  - q: "Should I use Vulkan or DirectX 11 in Baldur's Gate 3 on ARM?"
    a: "Try DirectX 11 first. Vulkan can be faster on some systems, but on ARM laptops it is more likely to hit driver bugs that cause black screens or crashes on launch. Switch only after DirectX 11 is stable."
  - q: "Will verifying game files delete my saves?"
    a: "No. Verifying files checks the game installation only and leaves your save folder untouched. Still, back up your saves before major repairs, just in case a reinstall or profile reset is needed later."
---

Baldur's Gate 3 is a huge, demanding role-playing game, and on an ARM laptop it has one extra hurdle: the game was built for x64 processors, so Windows 11 on ARM must translate its code on the fly. That translation works well for a turn-based RPG, but a driver bug, a bad shader cache, or an aggressive power setting can still turn an evening in the Forgotten Realms into a crash to the desktop.

Most Baldur's Gate 3 problems on Snapdragon laptops share a small set of causes. You are not dealing with a broken game or a laptop that cannot run it. You are dealing with driver versions, graphics API choices, power modes, and files that go stale after an update.

This guide walks through those causes in order, from quick settings checks to a clean driver and game repair. Work through the fixes one at a time, test the game after each step, and stop as soon as it runs stably.

## Why this happens

- **x64 emulation overhead:** Baldur's Gate 3 runs through Prism emulation on ARM, so any CPU-heavy scene — a crowded camp, a big battle with many effects — puts extra strain on the system and exposes weaknesses elsewhere.
- **Outdated or generic Adreno driver:** A generic Windows display driver, or an older OEM driver, may lack the Vulkan and DirectX fixes the game needs, causing crashes, black screens, or missing textures.
- **Wrong graphics API choice:** Vulkan is the default for many players, but on ARM it can trigger driver crashes that DirectX 11 avoids entirely.
- **Corrupted shader or game cache:** After a game patch or a driver update, old cached shaders can conflict with the new code and crash the game during loading screens.
- **Power mode throttling the GPU:** Battery saver and best-efficiency power modes cap the GPU just when the game needs it most, producing stutter, long loads, and sudden exits.
- **Overlay and background software conflicts:** Screen recorders, Discord overlays, and third-party tuning tools can hook into the emulated game process and destabilise it.
- **Corrupted or mismatched game files:** A failed update or an interrupted download can leave a damaged data file that only fails when the game reaches a particular area or cutscene.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set power mode to Best performance and plug in

The most common reason a game stutters or closes on an ARM laptop is power management, not hardware weakness. Snapdragon laptops are tuned for battery life, and that tuning works against a long gaming session unless you override it.

1. Plug in the charger before launching, so battery saver cannot engage mid-session.
2. Open **Settings > System > Power & battery** and set **Power mode** to **Best performance**.
3. Turn off **Battery saver** completely, including its automatic threshold.
4. Close heavy background apps, especially browsers with many tabs, before starting the game.
5. Play through a busy scene; if stutter drops sharply, power mode was a major part of the problem.

### Fix 2: Switch the game to DirectX 11

If the game crashes on launch, shows a black screen with sound, or freezes on the Larian logo, the graphics API is the first suspect. Vulkan is excellent on native x86 hardware, but its ARM driver path is newer and less tested, while DirectX 11 uses a more mature translation route. A similar API-first approach also helps when [Cyberpunk 2077 refuses to launch on ARM laptops](/articles/cyberpunk-2077-arm-laptop-not-launching-fix/).

1. Open the Larian Launcher and click the gear icon next to Play, if your version shows graphics options there.
2. Otherwise, open **Options > Video** from the main menu and change the graphics API to **DirectX 11**.
3. If the game will not reach the menu, use the launcher options or configuration file to force DirectX 11.
4. Restart the game completely after changing the API — do not just reload a save from the same session.
5. Test a save in a demanding area, such as the goblin camp, before declaring the fix successful.

### Fix 3: Update the OEM Adreno graphics driver

A game patch can outpace an old graphics driver, and Windows Update sometimes replaces a validated OEM driver with a generic one. Reinstalling the driver from your laptop maker restores the ARM-specific fixes the game depends on.

1. Open **Device Manager > Display adapters** and note the current driver name and date.
2. Check your exact laptop model in **Settings > System > About** before downloading anything.
3. Download the latest Windows 11 on ARM graphics driver from [Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en) support for your model.
4. Run the installer as administrator, let it finish without sleep, and restart when prompted.
5. Launch the game again and check stability and texture quality.

### Fix 4: Clear the shader cache and verify game files

When crashes happen only on loading screens, or only after a patch, stale cached data is a likely culprit. Clearing caches is safe — the game rebuilds them on the next launch, and the rebuilt cache matches your current driver and game version.

1. Close Baldur's Gate 3 and its launcher completely, checking Task Manager for any lingering process.
2. In your game platform, open the game's properties and choose **Verify integrity of game files**, then wait for the scan.
3. If files are repaired, restart the game before changing any other setting, so you test one change at a time.
4. Delete the game's shader cache folder if your platform describes one for your install, then relaunch.
5. Allow the first load to finish fully, even if it is slow — interrupting shader rebuilding recreates the corruption.

### Fix 5: Lower the demanding graphics settings

Baldur's Gate 3 looks beautiful at high settings, but shadows, volumetric fog, and draw distance are expensive under emulation. Lowering just those settings often buys a large stability gain with a small visual cost.

1. In **Options > Video**, set the overall preset to **Medium** as a baseline.
2. Lower **Shadow quality** and **Volumetric fog** first, since these cost the most performance for the least benefit.
3. Reduce **Model and texture quality** one step if textures load slowly or pop in late.
4. Cap the frame rate at 30 or 60 frames per second to stop the GPU overheating and throttling.
5. Save the settings, restart the game, and compare a busy combat encounter with how it ran before.

### Fix 6: Disable overlays and clean up background software

Overlays inject themselves into the game process, and under emulation that injection is more fragile than on native hardware. If crashes correlate with voice chat or recording, an overlay is a strong suspect, and removing it is a quick, free test.

1. Turn off the in-game overlay in Discord, your game platform, and any recording app you use.
2. Close third-party GPU tuning, fan control, and screen-recording tools before launching the game.
3. Open Task Manager and end any non-essential app using significant CPU or GPU.
4. Launch the game alone, with no overlay active, and play through the scene that previously crashed.
5. If it runs cleanly, re-enable overlays one at a time to identify the offender. For a related case where a missing control had a simple settings cause, see the [Click to Do image-action fix](/articles/click-to-do-create-image-missing-fix/).

## Closing

Baldur's Gate 3 on an ARM laptop is very playable once the power mode, graphics API, and driver are aligned, and most crashes trace back to one of those three rather than to the laptop itself. Keep the charger connected, stay on DirectX 11 unless Vulkan proves stable, and revisit the driver after every major update. If a future patch breaks the game again, follow the [Click to Do tools in Snipping Tool](/articles/click-to-do-snipping-tool-not-working/) pattern: verify one setting at a time until the new culprit appears.
