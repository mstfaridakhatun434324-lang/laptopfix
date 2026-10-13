---
title: "Set the Right GPU for Each App: A Per-App Preference Guide"
slug: best-way-to-set-gpu-preference-per-app
date: "2026-09-16"
categories: ["performance"]
tags: ["gpu preference", "dual gpu", "integrated graphics", "nvidia", "windows 11"]
description: "Laptop with two GPUs? Set a per-app GPU preference on Windows 11 so games use the fast GPU and light apps sip battery on integrated graphics."
thumbnail: "/images/thumbs/best-way-to-set-gpu-preference-per-app.webp"
faqs:
  - q: "How do I know if my laptop has two GPUs?"
    a: "Open Task Manager, then Performance, and count the GPU entries — dual-GPU laptops show GPU 0 and GPU 1 (typically Intel or AMD integrated plus an NVIDIA or AMD discrete chip). You can also check Device Manager under Display adapters. If there is only one entry, per-app GPU preferences do not apply to your machine."
  - q: "Which apps should use the high-performance GPU?"
    a: "Games, video editors, 3D software, CAD tools, and anything that renders heavily — these benefit enormously from the discrete GPU. Everything else (browsers, office apps, media players, chat) should stay on integrated graphics to save battery. The exception: if a specific light app stutters on integrated graphics, promote it individually rather than switching everything."
  - q: "Why is my game still slow after setting high performance?"
    a: "Three usual reasons: the game is CPU-bound rather than GPU-bound (check Task Manager during play), the laptop is not plugged in and the discrete GPU is power-limited, or the setting did not apply because the game launches through a launcher — set the preference on the launcher's executable too, or on the actual game binary in its install folder."
  - q: "Does the GPU preference affect battery life?"
    a: "Significantly. The discrete GPU draws far more power than integrated graphics. Forcing everything to high performance can cut battery life by 30 percent or more. The power-saving preference exists precisely for this: keep light apps on integrated graphics and reserve the discrete GPU for the handful of apps that genuinely need it."
---

Most gaming and creator laptops carry two graphics processors: a frugal integrated GPU sipping power for everyday tasks, and a hungry discrete GPU waiting for heavy lifting. Windows is supposed to pick the right one per app automatically — and it gets it wrong often enough that manual control matters. A game stuck on integrated graphics stutters; a browser forced onto the discrete GPU drains your battery for no benefit.

Per-app GPU preferences are Windows' built-in fix: you tell each application which GPU to use, and Windows obeys. It takes a few minutes to set up and pays off every day in both performance and battery life.

## Why this happens

- **Automatic switching guesses wrong** — Windows' auto-select misjudges some apps' needs.
- **Launchers mask the real app** — the GPU setting applies to the launcher, not the game it spawns.
- **Driver updates reset preferences** — GPU driver reinstalls sometimes wipe custom assignments.
- **Power modes override** — battery saver can force integrated graphics regardless of preference.
- **External monitors change the equation** — displays wired to the discrete GPU bypass preferences.
- **UWP vs. desktop app paths** — Store apps and classic apps are managed in slightly different UI flows.
- **Outdated graphics drivers** — old drivers expose fewer apps correctly to the preference system.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your dual-GPU setup

Do not configure what you do not have.

1. Open **Task Manager → Performance** and count GPU entries — two means dual-GPU.
2. Note which is which: **GPU 0** is usually integrated (Intel/AMD), **GPU 1** discrete (NVIDIA/AMD).
3. Check **Device Manager → Display adapters** to confirm the exact models.
4. If only one GPU exists, per-app preferences will not appear — your tuning options are power plans instead.
5. While here, note driver dates — stale drivers cause most preference weirdness.

### Fix 2: Set preferences in Windows Settings

The built-in, vendor-neutral method that works for every app.

1. Go to **Settings → System → Display → Graphics**.
2. Under **Custom options for apps**, click **Add app** → choose **Desktop app** or **Microsoft Store app**.
3. Browse to the app's `.exe` (for games, find the actual game binary, not just the launcher).
4. Click the added app → **Options** → choose **Power saving** (integrated), **High performance** (discrete), or **Let Windows decide**.
5. Set games and creative apps to **High performance**; leave browsers and office apps on **Power saving** or auto.

Changes apply the next time the app launches — no restart needed. Microsoft documents this in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Handle launcher-spawned games correctly

This is the number one reason "I set it but nothing changed."

1. Identify the launcher (Steam, Epic, EA App) and the actual game executable in its install folder.
2. Add **both** the launcher and the game `.exe` to the graphics preferences list.
3. Set the game binary itself to **High performance** — the launcher's setting does not inherit downward.
4. Verify in-game: many games show the active GPU in their graphics settings or via an overlay.
5. Alternatively, use Task Manager's **GPU Engine** column while the game runs to confirm which GPU is busy.

One setting on the wrong executable explains most "preference ignored" complaints.

### Fix 4: Use the GPU vendor control panel for finer control

NVIDIA and AMD panels offer options Windows Settings does not.

1. **NVIDIA**: right-click desktop → **NVIDIA Control Panel → Manage 3D settings → Program Settings** tab.
2. Select the program (or add it), then choose the preferred graphics processor explicitly.
3. Set **Power management mode** to **Prefer maximum performance** for demanding games.
4. **AMD**: use **AMD Software → Gaming → Graphics** for per-game profiles.
5. Vendor settings and Windows settings can conflict — when in doubt, set it in one place and leave the other on auto.

Get current drivers first: [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).

### Fix 5: Fix preferences that will not stick

Sometimes assignments reset or refuse to apply.

1. Update both GPU drivers — mismatched driver versions confuse the preference system.
2. Remove the app from the graphics list and re-add it fresh.
3. Check that **Hardware-accelerated GPU scheduling** is on: **Settings → System → Display → Graphics → Change default graphics settings**.
4. Learn more in the [GPU scheduling guide](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-11/).
5. If a specific app ignores preferences entirely, check its own settings — some apps (especially older games) hardcode GPU selection.

Driver reinstalls are the most common cause of wiped preferences — recheck after every GPU driver update.

### Fix 6: Balance performance with battery life

The discrete GPU is fast and thirsty — use it deliberately.

1. Keep the global default on **Let Windows decide** or **Power saving**.
2. Promote only the 3–5 apps that genuinely need the discrete GPU.
3. On battery, consider demoting even games to integrated for light titles — many indie games run fine.
4. Use your maker's battery/thermal modes alongside GPU preferences for the full picture.
5. Monitor with Task Manager's per-GPU graphs to confirm the split matches your intent.

A thoughtful assignment list can add an hour or more of real battery life. Pair it with the [best performance power plan](/articles/how-to-change-power-plan-to-best-performance-on-windows-11/) tuned for plugged-in use.

### Fix 7: Troubleshoot external monitor complications

External displays can bypass your careful preferences.

1. Check which GPU your laptop's HDMI/DisplayPort is wired to — many laptops wire external outputs directly to the discrete GPU.
2. If so, anything on the external monitor uses the discrete GPU regardless of per-app settings.
3. This is actually convenient for gaming (guaranteed discrete GPU) but wasteful for office work on a dock.
4. Some laptops offer a **MUX switch** or **Advanced Optimus** in BIOS or the maker app to change this wiring.
5. With Advanced Optimus, per-app preferences work across both internal and external displays.

## Closing

Per-app GPU preferences are the control panel dual-GPU laptops should have shipped with: set demanding apps to high performance, keep everything else on power saving, and remember to target the actual game binary rather than its launcher. Five minutes of configuration buys you full frame rates where they matter and real battery life everywhere else — the entire point of having two GPUs in the first place.
