---
title: "How to Stop Apex Legends Crashing on Your ARM Laptop"
slug: apex-legends-arm-laptop-crashing-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["apex legends", "arm laptop", "snapdragon", "crashing", "easy anti-cheat", "troubleshooting"]
description: "Apex Legends crashes on ARM laptops for different reasons than on x86 PCs. Fix anti-cheat errors, shader issues, and emulation stutters with these steps."
thumbnail: "/images/thumbs/apex-legends-arm-laptop-crashing-fix.webp"
faqs:
  - q: "Why does Apex Legends crash on my ARM laptop but not on other games?"
    a: "Apex combines a demanding engine, Easy Anti-Cheat, and heavy shader compilation. On ARM, emulation adds overhead, anti-cheat checks can fail, and shader cache problems crash the game before or during matches."
  - q: "Is Apex Legends officially supported on Windows on ARM?"
    a: "Respawn and EA do not list Windows on ARM as a fully supported platform for Apex Legends, so even a working setup can break after an update. Treat fixes as best-effort troubleshooting, not a guarantee."
  - q: "Should I delete the shader cache to stop crashes?"
    a: "Clearing a corrupted shader cache often helps, but the game will rebuild shaders on the next launch, which takes longer and may stutter. Delete the cache only when crashes point to it, not after every session."
  - q: "Will lowering graphics settings stop the crashes?"
    a: "Lower settings reduce GPU and memory pressure and can stop crashes caused by overload, but they will not fix anti-cheat failures, corrupted files, or a broken driver. Use settings as one step, not the whole fix."
---

On an ARM laptop, that pattern is frustrating because the usual x86 advice assumes hardware and drivers that behave differently on Snapdragon machines. Reinstalling the whole game for the third time rarely helps when the crash comes from anti-cheat, shader compilation, or emulation overhead instead.

Windows on ARM runs Apex through an emulation layer, which adds translation work on top of an already demanding battle royale. When any one of those steps falters, the game does not stutter politely — it closes.

This guide works through the crash causes in order, from the quickest checks to the deeper repairs. Start at the top, test the game after each fix, and stop as soon as matches run cleanly for a full session.

## Why this happens

- **Easy Anti-Cheat validation failures:** Anti-cheat checks that pass easily on x86 can time out or misread the emulated process on ARM, closing the game before a match starts.
- **Corrupted or stale shader cache:** Apex pre-compiles shaders on first launch, and a cache damaged by a crash or an interrupted update will crash the game again every time it tries to reuse those shaders.
- **Emulation overhead under load:** Prism translation adds CPU work, so a busy firefight can push the emulated game past its frame-time budget and trigger a hard crash rather than a dip.
- **Outdated or generic ARM graphics drivers:** A generic driver or a Windows Update driver swap can break the rendering path Apex expects, especially after a game or driver update.
- **Memory and power pressure:** Running the game on battery saver, with a browser full of tabs open, or with too little free RAM can starve the game at exactly the moment it needs more.
- **Corrupted game files after an update:** A failed or partial update leaves mismatched files that pass the launcher check but crash once the engine loads a broken asset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check power, memory, and background load first
Crashes that happen mid-match are often resource crashes in disguise. Before you touch anti-cheat or drivers, give the game the power and memory it needs and see whether the problem was simply overload.

1. Plug in the charger and set **Settings > System > Power & battery > Power mode** to **Best performance**, since battery saver throttles the CPU and GPU.
2. Close browsers, Discord overlays, recording tools, and other heavy apps before launching Apex, then check Task Manager to confirm free RAM.
3. Launch Apex, play one full match, and note whether crashes still happen at the same moments, such as landing or entering a firefight.
4. If crashes stop, reintroduce one background app at a time to find the one that pushed the system over the edge.
### Fix 2: Repair Easy Anti-Cheat
When Apex closes at the splash screen or shows an anti-cheat error, the game itself may be fine — the security layer is the problem. Repairing Easy Anti-Cheat is safer and faster than reinstalling the entire game, and it fixes the most common launch crashes.

1. Open the Apex Legends install folder and find the **EasyAntiCheat** folder, then run **EasyAntiCheat_Setup.exe** as administrator.
2. Select Apex Legends from the game list and click **Repair Service**, then wait for the repair to finish without launching the game early.
3. Restart the laptop so the repaired service loads cleanly at boot, rather than trying to attach to a running session.
4. If the repair fails, check Microsoft's Windows support guidance for Secure Boot and driver-signing, since anti-cheat depends on both. A similar anti-cheat wall blocks some titles outright, as explained in the [Valorant Vanguard ARM guide](/articles/valorant-vanguard-arm-not-supported-fix/) — Apex is more forgiving, but the security layer still matters.
### Fix 3: Verify game files and clear the shader cache
A corrupted asset or shader cache will crash Apex at the same loading point again and again. Verifying files repairs bad assets, and clearing the shader cache forces a clean rebuild, which together remove the two most common repeat-crash causes.

1. In Steam or the EA App, open Apex Legends properties and choose **Verify integrity of game files** (Steam) or **Repair** (EA App).
2. Let the check finish fully and allow it to download any replacement files, even if the list looks small.
3. After verification, delete the Apex shader cache folder in the game's saved-data location, following the launcher's documented cache path for your install.
4. Launch Apex and expect a longer first load while shaders rebuild; do not force-close the game during this step or you will corrupt the new cache.
### Fix 4: Update the ARM graphics driver from your laptop maker
Generic Windows drivers are a frequent crash source on ARM laptops because they lack the maker's validated Adreno tuning for games. Installing the correct OEM driver restores the rendering path Apex was tested against.

1. Open **Device Manager > Display adapters** and note whether the entry is a generic adapter or a named Adreno GPU.
2. Find your exact model in **Settings > System > About**, then download the latest Windows 11 on ARM graphics driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. Run the installer as administrator, restart when prompted, and confirm the new driver version in Device Manager.
4. Launch Apex, set graphics to a moderate preset for the first test, and play through a busy area to stress the new driver.
### Fix 5: Lower settings that overload emulation
High settings on an emulated game do not just lower frame rate — they increase the chance of a crash when the translation layer cannot keep up. A tuned preset keeps Apex playable on ARM without giving up the whole experience.

1. In Apex settings, set **Texture Streaming Budget** to a low or medium value that matches your laptop's RAM, not the maximum the menu offers.
2. Turn **Volumetric Lighting** and **Dynamic Spot Shadows** off, and set **Model Detail** and **Effects Detail** to low for the test session.
3. Cap the frame rate slightly below your display's maximum to give the emulation layer headroom during firefights.
4. If matches now run cleanly, raise one setting at a time until crashes return, then step back one notch — that is your stable ARM preset. Other demanding titles hit the same emulation ceiling, as the [Overwatch 2 ARM issues guide](/articles/overwatch-2-arm-laptop-issues-fix/) shows, so keep expectations realistic for competitive play.
### Fix 6: Clean reinstall and a fresh Windows check
If every targeted fix fails, a clean reinstall removes the possibility of a deeply corrupted install, and a Windows health check rules out a broken system component. Do this last, because it costs the most time. Account trouble on the same laptop is separate: if Copilot account switching misbehaves, see [Copilot account switching issues](/articles/copilot-account-switching-issues/) — it does not affect Apex anti-cheat.

1. Uninstall Apex Legends, then manually delete any leftover game folders the uninstaller leaves behind, including saved cache data.
2. Run **Settings > Windows Update** and install all pending updates, then restart the laptop.
3. Reinstall Apex from Steam or the EA App only, without third-party launchers or mods, and let the first shader build finish uninterrupted.
4. Launch with default settings, play a full match, and only then restore your preferred graphics preset.
5. If crashes persist after a clean install on a fully updated system, the title may simply be unstable on your ARM configuration for now — check EA's patch notes after each season update, since ARM compatibility can change. Camera and AI features can also misbehave on the same machines, as seen with [Studio Effects auto-framing zoom](/articles/studio-effects-auto-framing-zoom-fix/), so keep game and system troubleshooting separate.
## Closing

Apex Legends crashes on ARM laptops usually come from anti-cheat validation, a broken shader cache, or emulation overload. Work through power, anti-cheat repair, file verification, OEM drivers, and tuned settings in order, saving a clean reinstall for last. If crashes survive all six fixes, your ARM configuration is not yet stable for Apex.
