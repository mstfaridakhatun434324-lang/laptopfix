---
title: "How to Fix PowerToys Issues on ARM64 Windows 11"
slug: powertoys-arm64-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["powertoys", "arm64", "windows utilities", "snapdragon", "windows on arm"]
description: "PowerToys modules not working on your Snapdragon laptop? Fix PowerToys ARM64 issues on Windows 11 with these step-by-step installer, elevation, and reset steps."
thumbnail: "/images/thumbs/powertoys-arm64-windows-issues.webp"
faqs:
  - q: "Is PowerToys available natively for ARM64?"
    a: >
      Yes. Microsoft ships native ARM64 builds of PowerToys — the GitHub releases page and the Microsoft Store both offer ARM64 installers. Running the native build is important because several PowerToys modules hook deeply into the OS, where emulation causes the most trouble.
  - q: "Why do some PowerToys modules not work on my ARM laptop?"
    a: >
      Individual modules can fail while the main app runs fine — usually because the module needs administrator elevation, conflicts with another utility, or its settings are corrupt. Toggling the module off and on in PowerToys Settings re-initializes it.
  - q: "Why does PowerToys ask for administrator rights so often?"
    a: >
      Modules like Keyboard Manager, FancyZones (in some configurations), and Always on Top hook system-level input and windows, which requires elevation. Running PowerToys as administrator once and enabling "run at startup" with elevation avoids repeated prompts.
  - q: "Can PowerToys slow down my laptop?"
    a: >
      Individual modules are lightweight, but enabling many at once — especially PowerToys Run with many plugins, or Find My Mouse effects — adds background load. Disable modules you do not use; each has its own toggle in PowerToys Settings.
---

PowerToys is the power user's toolbox — FancyZones, PowerToys Run, Keyboard Manager, the color picker — and on your Snapdragon laptop some of it just does not work. A module toggles on but does nothing, PowerToys Run never appears, settings will not save, or the whole thing crashes on launch. The toolbox has holes in it.

Microsoft does ship native ARM64 PowerToys, so the foundation is fine. The failures are the usual suspects: the wrong installer build, per-module corruption, elevation problems, conflicts with other utilities hooking the same keys, and settings files damaged by migration from an old PC.

This guide gives you six fixes in order: install the right build, fix elevation, repair individual modules, reset the settings, resolve hotkey conflicts, and handle startup. If the laptop's Wi-Fi also misbehaves on ARM, the driver-layer parallel is [Surface Laptop 7 Wi-Fi issues](/articles/surface-laptop-7-wifi-issues-fix/).

## Why this happens

- **Wrong installer architecture:** The x64 installer runs under emulation — mostly working, but the deep OS hooks (keyboard, window management) are where emulation breaks first.
- **Missing administrator elevation:** Several modules need elevation to hook input; without it they silently do nothing.
- **Corrupted per-module settings:** PowerToys stores JSON settings per module — damaged files make individual modules fail while others work.
- **Hotkey conflicts:** Another app (or Windows itself) already owns the hotkey — PowerToys loses silently.
- **Conflicting utilities:** Other keyboard/window tools hooking the same APIs fight PowerToys for control.
- **Damaged installation:** Interrupted updates leave mixed binaries that crash on launch or break random modules.
- **Startup entry broken:** PowerToys not launching at login, or launching without elevation, makes everything feel intermittently broken.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build

The GitHub releases page lists separate x64 and ARM64 installers, and grabbing the wrong one is easy. The native build's OS hooks are the reliable ones — verify this before debugging any module.

1. Check your installed version: **PowerToys Settings > General** shows the version; the installer filename you used indicates the architecture.
2. Uninstall PowerToys from **Settings > Apps > Installed apps**.
3. Download the **ARM64** installer from the PowerToys GitHub releases page (or install from the Microsoft Store, which serves the right build).
4. During install, check **Run PowerToys as administrator** if offered — it prevents a whole class of module failures.
5. Launch, open Settings, and test your failing module before restoring old settings. NordVPN's ARM client had the same "get the right installer" lesson: [NordVPN on ARM Windows](/articles/nordvpn-arm-windows-issues/).

### Fix 2: Run as administrator and fix elevation

Half of all "module does nothing" reports are elevation. Keyboard Manager cannot remap keys in elevated windows, Always on Top cannot pin admin windows, and FancyZones misbehaves — all without any error message.

1. Right-click the PowerToys shortcut and choose **Run as administrator**, then test the failing module.
2. If it works elevated, make it permanent: **PowerToys Settings > General** and enable **Run as administrator** (or **Always run as administrator**).
3. In the same page, enable **Run at startup** so elevation applies from login — a manual elevated launch that you forget is the classic intermittent failure.
4. Accept the UAC prompt at startup; if UAC prompts annoy you, that is the price of system-level hooks — there is no safe bypass.
5. Retest each failing module. Modules that work elevated but not otherwise were never broken — they were underprivileged.

### Fix 3: Repair individual failing modules

When the app runs but one module misbehaves — PowerToys Run will not open, Text Extractor does nothing, the color picker will not activate — the module's own state is corrupt. PowerToys lets you reset modules surgically.

1. Open **PowerToys Settings** and go to the failing module's page.
2. Toggle the module **Off**, wait 10 seconds, toggle it **On** — this re-initializes its hooks.
3. Check the module's hotkey/shortcut setting — re-record the activation shortcut in case the binding is damaged.
4. For PowerToys Run specifically: check its plugin list and disable third-party plugins one by one — a bad plugin breaks the whole launcher.
5. For FancyZones: re-run the **Layout editor** and reapply your layout — zone definitions corrupt more often than the module itself. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the settings-storage locations.

### Fix 4: Reset PowerToys settings completely

When multiple modules fail or settings will not save, the JSON settings store is damaged — often from migrating settings from an x64 PC. A full reset is fast and you can rebuild in minutes.

1. Fully exit PowerToys (tray icon > Exit).
2. Press **Win + R**, type `%LOCALAPPDATA%\Microsoft\PowerToys`, and rename the folder to `PowerToys.bak`.
3. Launch PowerToys — it recreates default settings.
4. Re-enable only the modules you actually use, configuring each fresh.
5. Test for a few days before deleting the `.bak` folder — and do not copy old JSON files back, since they carry the corruption.

### Fix 5: Resolve hotkey and utility conflicts

PowerToys losing a hotkey fight looks exactly like a broken module: you press the shortcut, nothing happens, no error. The winner is usually Windows itself or another utility.

1. List your failing module's shortcut in PowerToys Settings and try changing it to something unusual (e.g., **Win+Ctrl+Alt+T**) — if the new binding works, the old one was stolen.
2. Common thieves: **Win+Shift+S** (Snipping Tool), **Win+V** (clipboard history), Xbox Game Bar shortcuts, and other keyboard utilities.
3. If you run AutoHotkey, ShareX, or similar tools, check their hotkeys against PowerToys' — only one can own each combination.
4. Disable the conflicting feature in the other app (or in Windows Settings) rather than fighting over the binding.
5. After resolving, restart PowerToys so it re-registers its hooks cleanly.

### Fix 6: Repair the installation and startup behavior

The remaining cases are installation damage: crashes on launch, modules missing from Settings, updates that never apply. A clean reinstall with the right build closes these out.

1. Uninstall PowerToys, then check `%LOCALAPPDATA%\Microsoft` and `%PROGRAMFILES%` for leftovers and remove them.
2. Restart the PC — this clears any hung PowerToys processes holding files.
3. Install the ARM64 build fresh (Fix 1), running the installer as administrator.
4. In **Settings > General**, enable **Run at startup** and **Run as administrator** together — this combination is the stable long-term configuration.
5. Reconfigure modules fresh (do not import old settings). If a specific module still fails on a clean native install, report it on the PowerToys GitHub with your ARM64 build noted — the team actively fixes ARM issues. Warranty-class hardware faults are a different road: [AI laptop warranty and NPU repair](/articles/ai-laptop-warranty-npu-repair/).

## Closing

PowerToys on Snapdragon laptops works well as the native ARM64 build run with administrator rights — wrong-architecture installs and missing elevation explain the large majority of "it does nothing" reports. The per-module toggles make diagnosis easy: when one module fails and the rest work, the problem is that module's state, not PowerToys. Reset surgically, resolve hotkey fights, and the toolbox is whole again.
