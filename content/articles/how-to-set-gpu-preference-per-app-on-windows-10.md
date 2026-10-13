---
title: "How to Set GPU Preference Per App on Windows 10"
slug: how-to-set-gpu-preference-per-app-on-windows-10
date: 2026-10-09
categories: ["performance"]
tags: ["gpu preference", "discrete gpu", "windows 10", "graphics settings"]
description: "On Windows 10 with dual GPUs? Assign apps to the right graphics chip — games to the discrete GPU, light apps to integrated — via Graphics settings."
thumbnail: "/images/thumbs/how-to-set-gpu-preference-per-app-on-windows-10.webp"
faqs:
  - q: "Where is the per-app GPU setting on Windows 10?"
    a: "Settings > System > Display, scroll down and click 'Graphics settings' (the link at the bottom). There you choose the app type — 'Classic app' for traditional desktop programs (browse to the .exe) or 'Microsoft Store app' for Store apps — add it, click Options, and pick 'High performance' (discrete GPU) or 'Power saving' (integrated GPU). The app must be restarted for the choice to take effect."
  - q: "What's the difference between 'Classic app' and 'Microsoft Store app'?"
    a: "'Classic app' means traditional Win32 desktop programs — you click Browse and navigate to the program's .exe file yourself. 'Microsoft Store app' shows a dropdown of your installed Store/UWP apps (including Xbox Game Pass games) without needing file paths. Picking the wrong type just means your app won't appear — switch types and try again."
  - q: "Why does Windows 10 keep ignoring my GPU preference?"
    a: "The usual reasons: you set the preference on the launcher instead of the game executable, the laptop is on battery with aggressive power saving, the OEM's GPU utility (GeForce Experience profiles, AMD Switchable Graphics, or vendor tools like Armoury Crate) is overriding Windows, or the discrete GPU driver is outdated. Also, some fullscreen games negotiate the GPU directly with the driver, bypassing Windows' preference."
  - q: "Should I use Windows settings or the NVIDIA/AMD control panel?"
    a: "Pick one and leave the other on default — setting both can conflict unpredictably. On Windows 10 version 1803 and later, the Windows Graphics settings page is the modern, recommended path and works across vendors. The NVIDIA Control Panel ('Manage 3D settings' > 'Program Settings') and AMD Software equivalent remain useful as a fallback when Windows' setting isn't respected by a particular app."
---

Windows 10 laptops with two GPUs — integrated graphics plus a discrete NVIDIA or AMD chip — rely on per-app assignment to balance performance and battery. Left to defaults, Windows 10's heuristics usually pick correctly, but games landing on integrated graphics (slideshow framerates) or the discrete GPU firing up for a PDF reader (battery drain) are both common misfires. The fix is the **Graphics settings** page, where you assign each app its GPU explicitly. (On Windows 11 the page moved slightly — see [our Windows 11 guide](/articles/how-to-set-gpu-preference-per-app-on-windows-11/).) If the compositor itself is the GPU hog, [DWM high GPU usage](/articles/how-to-fix-high-gpu-usage-dwm-exe-on-windows-11/) covers that side.

## Why this happens

- **Windows 10 heuristics misclassify apps**: Older detection logic guesses wrong more often than Windows 11's.
- **Preference set on launcher, not game**: Steam/Epic launchers don't pass their GPU assignment to the game process.
- **Battery saver overriding**: Power saver modes force integrated graphics regardless of per-app choice.
- **Vendor utilities conflicting**: OEM GPU-switching tools fighting Windows' own assignment.
- **Outdated discrete GPU driver**: Old drivers predate proper cooperation with Windows 10's GPU preference.
- **Fullscreen exclusive mode bypass**: Some engines negotiate the GPU directly, ignoring the OS preference.
- **External display wiring**: Ports hardwired to one GPU override software assignment.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify which GPU apps are using now

Confirm the misassignment with Task Manager.

1. Open **Task Manager** > **Performance** tab: identify **GPU 0** and **GPU 1** by name (integrated vs. discrete).
2. Launch the problem app, then check the **Processes** tab > **GPU** column (enable it via right-click > columns if hidden) — it shows per-process GPU utilization.
3. For the engine view: **Details** tab > right-click columns > **Select columns** > check **GPU Engine** — shows exactly which GPU each process renders on.
4. Game on the wrong GPU confirmed? Also note your power state (plugged in vs. battery) and **Settings** > **System** > **Power & sleep** > power mode — **Battery saver** forces integrated.
5. Plug in the charger before judging gaming assignments — most firmware disables the dGPU on battery no matter what Windows says.

### Fix 2: Assign the GPU in Graphics settings

The core Windows 10 procedure.

1. Go to **Settings** > **System** > **Display**, scroll to the bottom, and click **Graphics settings**.
2. Under **"Choose an app to set preference,"** select the app type: **Classic app** for desktop programs, **Microsoft Store app** for Store/Xbox games.
3. For Classic app: click **Browse**, navigate to the program's `.exe` (for games, the actual game exe — in Steam, right-click game > Manage > Browse local files), and click **Add**.
4. Click the added app > **Options** > choose **High performance** (uses the discrete GPU) or **Power saving** (integrated GPU) > **Save**.
5. **Fully restart the app** — GPU assignment happens at process launch; the setting does nothing for an already-running app.

### Fix 3: Handle games behind launchers

The step everyone misses on Windows 10.

1. Never rely on setting the preference for `Steam.exe` or `EpicGamesLauncher.exe` — the game spawns as a separate process that needs its own entry.
2. Find the real executable: Steam library > right-click game > **Manage** > **Browse local files**; look past the launcher stub for the game's main `.exe` (check subfolders like `Binaries` or `x64`).
3. Add that exe as a **Classic app** and set **High performance**.
4. For **Xbox Game Pass / Microsoft Store games**: use the **Microsoft Store app** type and pick the game from the dropdown — their exes hide in protected `WindowsApps` folders.
5. Verify in-game (graphics settings usually name the active GPU) and in Task Manager's GPU Engine column — both should agree on the discrete GPU.

### Fix 4: Stop power modes from overriding

Your preference is advisory when power saving is aggressive.

1. Set the power slider (click the battery icon) to **Best performance** or **Better performance** when plugged in — **Battery saver**/**Best battery life** forces integrated graphics.
2. Go to **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**: expand **PCI Express** > **Link State Power Management** > set to **Off** for **Plugged in**.
3. Check for OEM power utilities (Dell Power Manager, Lenovo Vantage, Armoury Crate): their performance profiles can override Windows — set them to a balanced/performance profile, not battery saver.
4. Game and create **plugged in** whenever possible — on battery, firmware-level dGPU restrictions apply on most laptops regardless of OS settings.
5. Re-test the assignment after each power change — the preference only holds when the power stack isn't vetoing it.

### Fix 5: Use the vendor control panel when Windows won't cooperate

The fallback path for stubborn apps.

1. **NVIDIA Control Panel** > **Manage 3D settings** > **Program Settings** tab > **Add** the app > set **preferred graphics processor** to **High-performance NVIDIA processor** > Apply.
2. **AMD**: **AMD Radeon Software** > **Gaming** tab > add the game > configure its graphics profile for high performance.
3. Intel integrated-only tweaks aren't needed here — the vendor panels matter for forcing the discrete chip.
4. Rule: configure in **one place only**. If you use the NVIDIA panel, leave the Windows Graphics settings entry on **"Let Windows decide"** (or remove it) to avoid conflicts.
5. Update the GPU driver if these options are missing or ignored — download from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html). Old drivers are the top reason vendor assignment fails.

### Fix 6: Troubleshoot the stubborn leftovers

For apps that defy both systems.

1. Try the game's **display mode**: switch between **Fullscreen**, **Borderless**, and **Windowed** — some engines only honor GPU selection in exclusive fullscreen.
2. Disable **fullscreen optimizations**: right-click the game exe > **Properties** > **Compatibility** > check **Disable fullscreen optimizations** — this changes the presentation path and sometimes the GPU negotiation.
3. Check **Windows Update** for graphics-stack updates and your maker's **BIOS updates** — hybrid-graphics behavior is partly firmware, and BIOS changelogs often mention GPU switching fixes.
4. If an external monitor is involved, test which port it's on — on many laptops each port is wired to a specific GPU, and the cable decides, not the software.
5. For one mission-critical app, the blunt instrument: many BIOS setups offer a **discrete graphics only** mode — everything uses the dGPU (battery life suffers), but assignment arguments end for good.

## Closing

Windows 10's per-app GPU setting works fine once you know its quirks: set it on the real executable (not the launcher), keep power modes from vetoing it, use one configuration system (Windows or vendor, not both), and verify with Task Manager. The game gets the GPU it needs; the battery keeps the rest.
