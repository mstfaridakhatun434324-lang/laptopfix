---
title: "Speed Up the Painfully Slow Epic Games Launcher on ARM Windows"
slug: epic-games-launcher-arm-windows-slow
date: 2026-10-23
categories: ["ai-pc"]
tags: ["epic games", "launcher slow", "arm windows", "epic launcher", "performance", "troubleshooting"]
description: "Fix the sluggish Epic Games Launcher on ARM Windows: disable hardware acceleration, clear the web cache, trim background work, and reinstall it cleanly."
thumbnail: "/images/thumbs/epic-games-launcher-arm-windows-slow.webp"
faqs:
  - q: "Why is the Epic Games Launcher so slow on my ARM laptop?"
    a: "The launcher is a Chromium-based desktop app with no native ARM64 build, so every part of it — the store pages, the library, the download manager — runs through x64 emulation. Emulated Chromium is dramatically slower than native, which is why the same launcher feels fine on an x64 machine and sluggish on yours."
  - q: "Will Epic release a native ARM64 launcher?"
    a: "Only Epic knows, and they have not announced one. The practical approach is to reduce the work the emulated launcher has to do: turn off hardware acceleration, clear its cache regularly, and keep it closed when you are not actively downloading or launching a game."
  - q: "Does the slow launcher affect game performance?"
    a: "No. The launcher's slowness is separate from the game itself — once a game is running, the launcher mostly sits idle. Close the launcher completely after starting your game to free the CPU and memory its emulated processes were consuming."
  - q: "Is reinstalling the Epic Games Launcher safe for my games?"
    a: "Yes, as long as you do not delete the game folders. The launcher rediscovers existing game installations when you point it at the same library folder after reinstalling. Your saves are stored separately — in the cloud or in your Documents folder — and are untouched by a launcher reinstall."
---

The Epic Games Launcher on your ARM laptop takes ten seconds to open, stutters when you scroll the store, and makes the whole machine feel tired while it downloads. On your old x64 laptop the same launcher was merely unremarkable — here it feels broken.

It is not broken; it is emulated. The launcher is a Chromium-based app with no native ARM64 build, so Windows runs the entire thing — UI rendering, JavaScript, the download manager — through the x64 emulation layer. Emulated Chromium is one of the heaviest workloads you can put through that layer, and the launcher does it constantly in the background.

You cannot make Epic ship an ARM64 build, but you can dramatically cut the work the emulated launcher performs. These six fixes trim its heaviest behaviors one by one: rendering, caching, background polling, and disk I/O.

## Why this happens

- **No native ARM64 build:** Every launcher process runs through x64 emulation, which costs significant CPU overhead versus native code — the single root cause of the sluggishness.
- **Hardware acceleration fighting emulation:** The launcher's GPU acceleration path assumes an x64 graphics stack; through emulation it often renders slower than plain software rendering.
- **Bloated web cache:** The Chromium cache accumulates store images, page data, and stale entries. On an emulated browser engine, parsing that cache on startup is painfully slow.
- **Constant background polling:** The launcher polls for friend activity, news, and updates on timers. Each wake-up spins up emulated code paths that a native app would handle cheaply.
- **Slow drive or fragmented install:** The launcher hammers its own data folder with small reads and writes. On a nearly-full or slow drive, that I/O pattern stalls the already-slow emulated UI thread.
- **Startup bloat:** The launcher defaults to starting with Windows and running in the system tray, so its emulated processes tax the machine from the moment you log in.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable hardware acceleration in the launcher

This is the highest-impact single toggle. The launcher's hardware-accelerated rendering goes through the emulated graphics path and frequently performs worse than software rendering on ARM — turning it off makes scrolling and page loads visibly snappier.

1. Open the Epic Games Launcher and click your profile icon, then **Settings**.
2. Scroll to the bottom and check **Disable Hardware Acceleration** (or uncheck "Enable Hardware Acceleration" depending on the version).
3. Fully quit the launcher — right-click its system tray icon and choose **Exit**, not just closing the window.
4. Reopen it and browse the store for a minute; page rendering should feel noticeably lighter.
5. If anything looks graphically wrong afterward, the toggle is trivially reversible — but on most ARM laptops it stays off permanently.

### Fix 2: Clear the launcher's web cache

Months of store browsing leave gigabytes of cached web data that the emulated Chromium engine re-parses on every start. Clearing it is the classic fix for a launcher that gets slower over time, and it costs you nothing but a re-login.

1. Fully exit the launcher from the system tray icon.
2. Press **Win + R**, type `%localappdata%\EpicGamesLauncher\Saved`, and press Enter.
3. Delete the **webcache** folder (and **webcache_4430** / **webcache_4147** if present — version numbers vary).
4. Restart the launcher and sign back in; the first launch rebuilds a clean, small cache.
5. Repeat this every few months, or whenever the launcher starts feeling heavy again. The same "stale cache, fresh start" logic resolves plenty of [cloud download recovery headaches](/articles/cloud-download-recovery-arm-laptop/) on these machines too.

### Fix 3: Stop it running at startup and in the background

The launcher does not need to be alive when you are not gaming. Keeping it out of startup and fully exiting it after use removes a permanent emulated workload from your machine — the easiest performance win on this list.

1. In the launcher's **Settings**, uncheck **Run When My Computer Starts**.
2. In Windows, open **Settings > Apps > Startup** and set **EpicGamesLauncher** to **Off** as a belt-and-suspenders measure.
3. After launching a game, right-click the tray icon and **Exit** the launcher entirely — the game keeps running fine without it.
4. Check Task Manager's Startup apps tab to confirm nothing Epic-related re-enabled itself after an update.
5. When you next want to play, open the launcher fresh; a cold start with a clean cache (Fix 2) is faster than resuming a week-old background session.

### Fix 4: Throttle downloads and limit background work

The download manager is another heavy emulated component, and at full speed it saturates both the CPU (decompression) and the disk. Throttling it slightly paradoxically makes the machine feel faster while barely slowing the download.

1. In launcher **Settings**, check **Throttle Downloads** and set a limit around 70–80% of your connection speed.
2. Uncheck any "allow downloads while playing" style options if present, so the launcher never competes with your game.
3. Pause the launcher's auto-update checks during gaming sessions: **Settings** > uncheck automatic updates if the option exists in your version.
4. Avoid browsing the store in a second tab while a large download runs — each store page is more emulated Chromium work on top of the download thread.
5. Schedule big downloads for when you are away from the machine; the launcher is allowed to be slow when nobody is watching.

### Fix 5: Reinstall the launcher cleanly on your fastest drive

A launcher installed years ago — or carried over through Windows upgrades — accumulates corrupted state no cache-clear fixes. A clean reinstall on the internal NVMe SSD gives the emulated code the fastest possible I/O.

1. Fully exit the launcher, then uninstall it via **Settings > Apps > Installed apps** — do NOT delete your game folders when prompted.
2. After uninstalling, delete `%localappdata%\EpicGamesLauncher` and `%programdata%\Epic` leftovers manually.
3. Download the latest installer from Epic's site and install it to the default location on your internal SSD — never a USB drive or SD card.
4. On first launch, sign in and verify your library: use **Locate** on each installed game and point it at the existing folder instead of redownloading.
5. Reapply Fixes 1–3 on the fresh install, since a reinstall resets all settings to defaults.

### Fix 6: Reduce what the launcher shows and syncs

Every carousel, news card, and friend-activity feed is JavaScript the emulated engine must execute. A minimal launcher is a fast launcher — strip the UI down to the library and nothing else.

1. In **Settings**, disable news, notifications, and any "show on startup" store content you do not use.
2. Set the launcher to open directly to your **Library** instead of the Store home page.
3. Sign out of the friends/social features if you do not use them — the presence polling is pure background cost.
4. Keep your installed-games list tidy; each entry's metadata gets refreshed on launch.
5. If you run local AI tools on this machine, note the same principle applies there — trimming background work is also how you keep [Ollama from fighting the NPU](/articles/ollama-npu-not-working-windows/) for resources.

## Closing

The Epic Games Launcher will never be fast on ARM until Epic ships a native build — but "never fast" and "painfully slow" are different things. Disable hardware acceleration, clear the web cache, keep it out of startup, and close it when you are done: those four habits remove most of the emulation tax you actually feel. The games themselves are unaffected, so once the download finishes, quit the launcher and enjoy the part that matters. And if you use parental controls on a shared family machine, the [Recall parental controls guide](/articles/recall-parental-controls-family-safety/) covers the Family Safety side of these PCs.
