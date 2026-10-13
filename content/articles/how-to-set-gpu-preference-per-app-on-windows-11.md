---
title: "How to Set GPU Preference Per App on Windows 11"
slug: how-to-set-gpu-preference-per-app-on-windows-11
date: 2026-10-01
categories: ["performance"]
tags: ["gpu preference", "discrete gpu", "integrated graphics", "windows 11"]
description: "Force games onto your discrete GPU and keep light apps on integrated graphics in Windows 11. Set per-app GPU preferences for better performance and battery life."
thumbnail: "/images/thumbs/how-to-set-gpu-preference-per-app-on-windows-11.webp"
faqs:
  - q: "What does the GPU preference setting actually do?"
    a: "It tells Windows which GPU to assign to a specific app on systems with two GPUs (integrated + discrete). 'High performance' forces the powerful discrete GPU — best for games and creative apps. 'Power saving' forces the integrated GPU — best for browsers and office apps to save battery. 'Let Windows decide' uses Microsoft's heuristics, which are usually right but occasionally pick wrong."
  - q: "Why is my game running on integrated graphics instead of my NVIDIA/AMD GPU?"
    a: "The most common reasons: the app launched on the wrong GPU because Windows guessed wrong, the laptop is in a power-saving mode that favors integrated graphics, or the discrete GPU driver has an issue and Windows fell back. Setting the app's preference to 'High performance' explicitly overrides the guessing. If it still won't use the discrete GPU, check the GPU vendor control panel and update drivers."
  - q: "Does forcing an app to the discrete GPU hurt battery life?"
    a: "Yes, noticeably. The discrete GPU draws far more power than integrated graphics — forcing everyday apps (browser, video player, chat) onto it can cut battery life significantly. That's exactly why per-app preference exists: put only demanding apps (games, video editors, 3D software) on High performance and leave everything else on Power saving or Let Windows decide."
  - q: "The app I want isn't in the list. How do I add it?"
    a: "In Settings > System > Display > Graphics, click 'Add an app' and choose by type: 'Microsoft Store app' for Store apps, or 'Desktop app' then Browse to the program's .exe file. For games, browse to the game's actual executable (not the launcher) — e.g., the .exe in the game's install folder. Classic Win32 apps need the Desktop app path; the Browse dialog starts in Program Files."
---

Most gaming and creator laptops have two GPUs: power-sipping **integrated graphics** (Intel/AMD iGPU) for everyday work and a hungry **discrete GPU** (NVIDIA/AMD dGPU) for heavy lifting. Windows 11 decides which GPU each app gets — and it usually guesses right, but "usually" isn't "always." Games mysteriously running on integrated graphics, the dGPU spinning up (and draining battery) for a chat app, creative software picking the wrong chip — the per-app GPU preference setting fixes all of it in about a minute per app. (On Windows 10, the same setting lives in a slightly different spot — see [our Windows 10 guide](/articles/how-to-set-gpu-preference-per-app-on-windows-10/).) If DWM itself is the GPU hog rather than an app, see [fixing DWM high GPU usage](/articles/how-to-fix-high-gpu-usage-dwm-exe-on-windows-11/).

## Why this happens

- **Windows' automatic GPU selection guesses wrong**: Heuristics misclassify some games and creative apps.
- **Power plans override app choice**: Battery-saver modes force integrated graphics regardless of preference.
- **Apps launched via launchers**: The launcher gets the preference, not the game executable underneath.
- **Driver issues causing fallback**: If the dGPU driver glitches, Windows silently falls back to integrated.
- **External monitor wiring**: On some laptops, external ports are hardwired to one GPU, overriding software preference.
- **Fullscreen vs. windowed behavior**: Some engines pick GPUs differently based on display mode.
- **OEM utilities fighting Windows**: Vendor GPU-switching tools conflicting with Windows' own setting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check which GPU your apps are actually using

Confirm the problem before changing settings.

1. Open **Task Manager** > **Performance** tab and note **GPU 0** vs **GPU 1** — the names tell you which is integrated and which is discrete.
2. Launch the app in question, then check the **Processes** tab > **GPU Engine** column — it shows which GPU each process is using (e.g., "GPU 1 – 3D").
3. If your game shows GPU 0 (integrated) while the dGPU sits idle, you've confirmed the misassignment.
4. Also check **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — note whether **Hardware-accelerated GPU scheduling** is on, as it interacts with assignment.
5. Check your power mode: **Settings** > **System** > **Power & battery** > **Power mode** — **Best power efficiency** aggressively prefers integrated graphics.

### Fix 2: Set per-app GPU preference in Settings

The core fix — takes a minute per app.

1. Go to **Settings** > **System** > **Display** > **Graphics**.
2. Find your app in the list. If it's missing, click **Add an app**: choose **Microsoft Store app** for Store apps, or **Desktop app** > **Browse** and navigate to the program's `.exe`.
3. Important for games: browse to the **game's actual executable**, not the launcher (Steam.exe, EpicGamesLauncher.exe) — the launcher's preference doesn't transfer to the game it spawns.
4. Click the app > **Options** > select **High performance** (discrete GPU) for games/creative apps, or **Power saving** (integrated) for light apps draining battery on the dGPU.
5. Click **Save**, then fully **restart the app** — GPU assignment happens at launch; changing it mid-session does nothing until relaunch.

### Fix 3: Handle launcher-spawned games correctly

Launchers are the classic gotcha.

1. Identify the real game executable: in Steam, right-click the game > **Manage** > **Browse local files** — look for the game's `.exe` (often in a subfolder, not the root).
2. Add that specific `.exe` via **Add an app** > **Desktop app** > **Browse**, and set it to **High performance**.
3. Some games use anti-cheat launchers that spawn the real exe from odd paths — if the setting doesn't stick, check Task Manager's GPU Engine column to see the actual process name and path (right-click > Open file location).
4. For Xbox Game Pass / Microsoft Store games, add them via the **Microsoft Store app** option — their executables live in protected WindowsApps folders you can't browse to directly.
5. Verify in-game: most games show the active GPU in their graphics/video settings screen — confirm it names your discrete GPU.

### Fix 4: Stop power settings from overriding your choice

Your preference loses to aggressive power saving.

1. Set **Settings** > **System** > **Power & battery** > **Power mode** to **Best performance** (or **Balanced**) when plugged in — **Best power efficiency** can override per-app High performance choices.
2. Plug in the charger for gaming/creative work: many laptops disable or throttle the dGPU on battery regardless of software settings — that's firmware, not Windows.
3. Check your OEM utility (Armoury Crate, Legion Zone, OMEN Hub, Dell Power Manager): their GPU modes (**Hybrid**, **Discrete**, **iGPU only**) override Windows' per-app setting — set it to **Hybrid/Optimus** for per-app control, or **Discrete** to force the dGPU globally.
4. In **advanced power plan settings**, check **PCI Express** > **Link State Power Management** — set to **Off** when plugged in if the dGPU keeps sleeping.
5. Re-test: with charger connected and sensible power modes, the per-app preference should now hold.

### Fix 5: Use the GPU vendor control panel as backup

When Windows' setting isn't respected.

1. **NVIDIA**: open **NVIDIA Control Panel** > **Manage 3D settings** > **Program Settings** tab > add the app > set **preferred graphics processor** to **High-performance NVIDIA processor**.
2. **AMD**: open **AMD Software** > **Gaming** > **Graphics** > add the app profile and set **Graphics Profile** appropriately.
3. These vendor settings and Windows' setting can conflict — if both are set differently, results are unpredictable. Pick one system (Windows Settings is the modern path) and leave the other on default.
4. Update the GPU driver if the control panel options are missing — ancient drivers predate proper Windows GPU-preference cooperation. Get current drivers from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
5. After driver updates, re-check your per-app preferences — major driver installs occasionally reset them.

### Fix 6: Verify and troubleshoot stubborn cases

For apps that still won't use the right GPU.

1. Confirm with Task Manager's **GPU Engine** column after a full app restart — and check the in-app GPU indicator if it has one.
2. If a game still uses integrated graphics: check whether your **external monitor** is plugged into a port hardwired to the iGPU (common on thin laptops) — the rendering GPU follows the display wiring on some designs.
3. Try **exclusive fullscreen** vs. **borderless windowed** in the game's settings — some engines only honor GPU preference in true fullscreen.
4. Check for **Windows updates** with graphics stack fixes, and your laptop's **BIOS updates** from the maker — MUX/hybrid graphics behavior is partly firmware.
5. As a last resort for one critical app, use the OEM utility's **discrete-GPU-only mode** (requires reboot) — it forces everything onto the dGPU, sacrificing battery but guaranteeing the assignment.

## Closing

Per-app GPU preference is a two-minute fix with outsized impact: games finally use the GPU you paid for, and light apps stop waking the power-hungry chip. Set it per executable (not per launcher), keep power modes and OEM utilities from overriding it, and verify with Task Manager. Your battery — and your framerates — will thank you.
