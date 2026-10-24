---
title: "How to Fix Notepad++ Issues on ARM64 Windows 11"
slug: notepad-plus-plus-arm64-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["notepad++", "arm64", "text editor", "snapdragon", "windows on arm"]
description: "Notepad++ crashing, plugins broken, or running slow on your Snapdragon laptop? Fix Notepad++ ARM64 issues with these build, plugin, and config repairs."
thumbnail: "/images/thumbs/notepad-plus-plus-arm64-windows-issues.webp"
faqs:
  - q: "Is there a native ARM64 version of Notepad++?"
    a: >
      Yes. Notepad++ ships official ARM64 builds — download the ARM64 installer from notepad-plus-plus.org on the Snapdragon laptop. The native build is noticeably faster to launch and lighter on resources than the emulated x64 version.
  - q: "Why don't my Notepad++ plugins work on ARM64?"
    a: >
      Plugins must match the application's architecture: ARM64 Notepad++ needs ARM64 plugins. Most popular plugins now ship ARM64 builds, but older or unmaintained ones may be x64-only — those simply will not load, and there is no emulation fallback for plugins.
  - q: "Why is Notepad++ slow to open large files on my ARM laptop?"
    a: >
      Large-file slowness is usually the same on every architecture — syntax highlighting, word wrap, and plugins processing megabytes of text. Disabling highlighting for the large file and turning off word wrap are the standard fixes.
  - q: "Will I lose my settings if I reinstall Notepad++?"
    a: >
      Not if you back up first. Notepad++ stores settings in %APPDATA%\Notepad++ (or beside the executable for portable installs). Copy that folder before reinstalling and restore it after — or let the fresh install regenerate defaults if the config was corrupt.
---

Notepad++ is the editor you have used for a decade — instant launch, tabs for everything, plugins for the rest. On your Snapdragon laptop it launches slowly, plugins refuse to load, or it crashes opening files that worked fine on your old machine. Your most trusted tool feels untrustworthy.

Notepad++ does have official ARM64 builds, so the core editor is fine. The pain is almost entirely the plugin architecture boundary: x64 plugins cannot load in ARM64 Notepad++, and many users migrated plugin folders from old PCs. Add in emulated installs and corrupted configs, and you get the full catalog of complaints.

This guide gives you six fixes in order: get the native build, fix the plugin situation, reset the configuration, fix large-file performance, repair shell integration, and handle updates. If the machine also runs Android tooling on ARM, the architecture-matching lesson is the same as [Android Studio emulator issues on ARM](/articles/android-studio-arm-windows-emulator/).

## Why this happens

- **Emulated x64 build installed:** The old installer runs under Prism emulation — slower launch, heavier resource use, and plugin weirdness.
- **x64 plugins in ARM64 Notepad++:** Plugins are DLLs that must match the host architecture — x64 plugins silently fail to load (or crash) the ARM64 build.
- **Migrated plugin folder:** Copying `%APPDATA%\Notepad++\plugins` from an x64 PC imports incompatible DLLs wholesale.
- **Corrupted config.xml:** Damaged settings cause crashes on launch, lost preferences, and the classic "settings revert every restart."
- **Heavy plugins on large files:** Syntax highlighting plus linters plus large files overwhelms any build — architecture is not the bottleneck.
- **Broken Explorer context menu:** The "Edit with Notepad++" shell extension needs correct registration, which breaks on reinstalls.
- **Outdated build:** ARM64-port fixes ship in updates — old builds carry fixed bugs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build

Everything downstream — especially plugins — depends on the host architecture. Confirm and correct the build before touching plugins or configs.

1. In Notepad++, go to **? > About Notepad++** and check the build architecture.
2. If it is x64, uninstall from **Settings > Apps > Installed apps**.
3. Download the **ARM64** installer from notepad-plus-plus.org on the Snapdragon laptop.
4. Install fresh — do not let the installer import old settings yet; test the clean baseline first.
5. Confirm fast launch and stable editing on plain files. If the editor is now snappy, emulation was the drag.

### Fix 2: Fix the plugin architecture mismatch

This is the heart of Notepad++-on-ARM troubleshooting. The rule is absolute: ARM64 host, ARM64 plugins. The Plugins Admin is your friend — it serves architecture-matched plugins automatically.

1. Open **Plugins > Plugins Admin** and check **Installed** — note any plugin showing errors or failing to load.
2. Remove every plugin you do not recognize or did not intentionally install on this machine — migrated x64 DLLs hide here.
3. Reinstall the plugins you actually need **through Plugins Admin** — it fetches the ARM64 build when one exists.
4. For a must-have plugin with no ARM64 build, check the plugin's GitHub for ARM64 releases or community forks — many have them now.
5. Accept that some unmaintained x64-only plugins genuinely cannot run — find an alternative or keep a portable x64 Notepad++ purely for that plugin. ExpressVPN's ARM transition hit the same "some components lag behind" reality: [ExpressVPN on ARM64](/articles/expressvpn-arm64-windows-not-working/).

### Fix 3: Reset the corrupted configuration

Crashes on launch, settings that will not persist, bizarre UI behavior — `config.xml` is damaged. Notepad++ regenerates clean defaults; your files and (compatible) plugins survive.

1. Fully close Notepad++ (check the tray — it can minimize there).
2. Press **Win + R**, type `%APPDATA%\Notepad++`, and rename **config.xml** to **config.xml.bak** (keep a copy of the whole folder first if you have elaborate customizations).
3. Relaunch Notepad++ — it creates a fresh default config.
4. Test stability and basic editing before reinstalling plugins.
5. Rebuild your settings manually rather than restoring the old XML — that reimports the corruption. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the app-data locations pattern.

### Fix 4: Fix large-file performance

Opening a 200MB log file and watching Notepad++ choke is not an ARM problem — it is a "parsing 200MB with highlighting and plugins" problem. These are the standard large-file mitigations, and they work on every architecture.

1. Before opening the huge file, set **Language > N > Normal Text** to disable syntax highlighting for it.
2. Turn off **View > Word Wrap** — wrapping is surprisingly expensive on very long lines.
3. Disable heavy plugins (linters, auto-completion helpers) for the session via **Plugins** menu toggles.
4. For truly massive files, use the 64-bit build's large-file handling and be patient on first open — the initial parse is the slow part.
5. Consider a dedicated log viewer for multi-GB files — Notepad++ is a text editor, not a big-data tool, and honesty about tool limits beats fighting them.

### Fix 5: Repair Explorer context menu integration

"Edit with Notepad++" missing from the right-click menu after reinstalls is a shell-extension registration issue. The fix depends on which installer type you used.

1. If you used the standard installer, the context menu entry registers automatically — if missing, reinstall choosing the context menu option explicitly.
2. On Windows 11, check the **Show more options** submenu — the entry may be there rather than on the top-level menu.
3. For the portable version, context menu integration is not automatic — use **Settings > Preferences > File Association** or a manual registry script from the Notepad++ docs.
4. If the entry exists but does nothing, the target path points at the old install location — reinstall cleanly (Fix 1) to fix the path.
5. Third-party context menu editors can also hide the entry — check those if you use one.

### Fix 6: Stabilize updates and the portable option

The last decisions are about maintenance: how you update, and whether the installed or portable flavor suits you better on this machine.

1. Update through **? > Update Notepad++** — the updater preserves architecture, so ARM64 stays ARM64.
2. If auto-update fails, download the ARM64 installer manually and run it over the top — settings are preserved.
3. Consider the **portable ZIP** (ARM64) if you prefer: extract, run, and your entire config travels in one folder — ideal for keeping x64 and ARM64 installs separate.
4. Keep a portable x64 build only if you depend on an x64-only plugin — run it solely for that task, not as your daily editor.
5. Back up `%APPDATA%\Notepad++` (or the portable folder) periodically — a known-good config backup turns future corruption into a two-minute restore. Surface Pro 11 users juggling ARM quirks will recognize the maintenance pattern: [Surface Pro 11 OLED screen issues](/articles/surface-pro-11-oled-screen-issues/).

## Closing

Notepad++ on Snapdragon laptops is the same fast editor you remember once it is the native ARM64 build with architecture-matched plugins — emulation and migrated x64 plugin DLLs cause nearly every complaint. The Plugins Admin is the safe path for plugins; manual DLL copying from old PCs is how the trouble starts. Keep the build native, the plugins matched, and a config backup handy, and the editor stays boring in the best way.
