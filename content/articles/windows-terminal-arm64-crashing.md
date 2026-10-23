---
title: "How to Stop Windows Terminal Crashing on ARM64"
slug: windows-terminal-arm64-crashing
date: 2026-10-23
categories: ["ai-pc"]
tags: ["windows terminal", "arm64", "crashing", "settings.json", "troubleshooting"]
description: "Stop Windows Terminal crashing on ARM64: reset a corrupt settings.json, fix GPU rendering, repair broken shell profiles, and reinstall cleanly when needed."
thumbnail: "/images/thumbs/windows-terminal-arm64-crashing.webp"
faqs:
  - q: "Why does Windows Terminal close immediately on launch?"
    a: "The most common cause is a corrupt or invalid settings.json — a bad edit, a bad theme, or a profile pointing at a shell path that no longer exists. Renaming settings.json so Terminal regenerates a clean default fixes the instant-close in most cases."
  - q: "Does GPU acceleration cause Terminal crashes on ARM?"
    a: "It can. The Atlas text-rendering engine leans on the GPU, and on some Snapdragon graphics drivers a specific glyph, font, or resize sequence crashes the renderer. Switching the profile's rendering to software mode is the quickest way to test whether the GPU is involved."
  - q: "Can a custom font crash Windows Terminal?"
    a: "Yes — a corrupt or unusual font file can crash the text renderer the moment Terminal tries to shape text with it. If crashes started right after changing the font face, switch back to Cascadia Mono or Consolas to confirm."
  - q: "Will reinstalling Windows Terminal delete my settings?"
    a: "A Store repair or reinstall keeps your settings.json in place, since settings live in your user profile, not the app package. But if settings.json itself is the problem, reinstalling alone will not help — reset the settings file too."
---

You press the Terminal shortcut and the window flashes and dies — or it opens, you start typing, and it vanishes mid-command. On an ARM64 Copilot+ laptop, where Terminal is the front door to PowerShell, WSL, and every dev workflow, an unstable terminal poisons the whole machine.

Windows Terminal crashes on ARM64 for a short list of reasons: a hand-edited settings.json with a syntax error or a dead shell path, the GPU text renderer tripping over a driver or font, a profile launching a shell that instantly exits, or a Store update that left the package in a half-upgraded state. All of them are diagnosable without reinstalling Windows.

This guide gives you six fixes in the order that finds the fault fastest: reset the settings file, tame the renderer, repair shell profiles, neutralize fonts and themes, then repair or reinstall the app itself.

## Why this happens

- **Corrupt or invalid settings.json:** One bad comma, an unclosed brace, or a schema change after an update, and Terminal dies parsing its own config at startup.
- **Dead default-profile command line:** If the default profile points to a `pwsh.exe`, `wsl.exe` distro, or SSH target that no longer exists, the tab's process exits instantly — which can take the whole window with it.
- **GPU renderer hitting a driver bug:** The Atlas engine exercises the Adreno GPU in ways few apps do; a driver edge case around specific glyphs or window sizes can crash the renderer.
- **Problematic font:** Corrupt or exotic font files crash text shaping. The crash often correlates with installing a new Nerd Font or switching the profile font.
- **Experimental or legacy settings carried over:** Settings synced from an x64 machine — like `experimental.rendering.forceFullRepaint` combos or old `"compatibility"` blocks — can misbehave on ARM64 builds.
- **Half-applied Store update:** A Terminal update interrupted by sleep or shutdown can leave mismatched binaries that crash on features the new version expects.
- **Conflicting overlay or injection software:** Screen-capture hooks, some antivirus "safe banking" overlays, and old GPU utilities inject into the Terminal process and destabilize it — the same class of interference behind [spatial audio glitches on ARM](/articles/spatial-audio-not-working-windows-11-arm/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset settings.json to a clean default

This is the highest-yield step: most instant-on-launch crashes are config crashes. Do not edit the broken file first — sideline it and let Terminal prove it can run clean.

1. Open File Explorer and go to `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\` — this is where the live `settings.json` lives.
2. Rename `settings.json` to `settings.json.bak` (do not delete it yet; your customizations are in there).
3. Launch Windows Terminal — it will generate a fresh default settings file. If it opens and stays open, the old config was the problem.
4. Reintroduce your customizations in small chunks: copy a few profiles or color schemes at a time from the `.bak`, restarting Terminal after each chunk, until the crash returns — the last chunk holds the culprit.
5. Validate the JSON as you go: paste each chunk into any JSON validator before saving. A single trailing comma has ended more Terminal sessions than any driver bug.

### Fix 2: Switch the renderer off the GPU

If Terminal opens but crashes when you resize, scroll fast, or hit certain characters, suspect the Atlas GPU renderer — especially after a graphics driver update.

1. With Terminal open (safe mode via Fix 1 if needed), go to **Settings > Rendering** and set **Text renderer** to the software option, or per-profile under the profile's **Advanced** section.
2. Alternatively, add `"experimental.rendering.software": true` to the profile in settings.json for a targeted test.
3. Stress-test: resize the window repeatedly, `cat` a large file, and scroll aggressively — the exact actions that crashed before.
4. If software rendering is stable, update the Adreno graphics driver from your maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and retest with GPU rendering re-enabled.
5. Keep software rendering as a fallback profile rather than a global setting if only one profile misbehaves — no need to punish every tab for one bad interaction.

### Fix 3: Repair the default shell profile

A profile whose command line points nowhere launches a process that exits in milliseconds. Terminal may interpret that as a fatal error, particularly when it is the default profile.

1. In **Settings > Startup**, note the **Default profile**, then open that profile's settings and inspect its **Command line**.
2. Verify the target exists: for PowerShell 7 it should be the ARM64 `pwsh.exe` under `Program Files\PowerShell\7`, not a leftover x64 path — the same architecture mix-up that breaks [standalone PowerShell 7 installs](/articles/powershell-7-arm-windows-issues/) also breaks Terminal profiles.
3. For WSL profiles, run `wsl -l -v` in a working shell and confirm the distro named in the profile is actually installed and not in a broken state.
4. Temporarily set the default profile to **Command Prompt** (`cmd.exe`) — if Terminal becomes stable, the previous default's shell was the problem, not Terminal.
5. Fix or recreate the broken profile with a verified command line, then restore it as default and confirm stability over a full work session.

### Fix 4: Neutralize fonts, themes, and acrylic effects

Font and theme crashes are sneaky because they strike mid-session — everything works until the renderer shapes one particular glyph. If crashes began after cosmetic changes, this is your fix.

1. In each profile's **Appearance** settings, set **Font face** back to **Cascadia Mono** (or Consolas) temporarily.
2. Disable **Acrylic** background effects and background images for a test run — composition effects interact with the GPU path from Fix 2.
3. If you installed a new font recently, uninstall it via **Settings > Personalization > Fonts** and retest before reinstalling a fresh copy of the font file.
4. Switch the color scheme to a built-in one (Campbell, One Half Dark) to rule out a malformed custom scheme.
5. Reintroduce cosmetics one at a time. Font problems on ARM are usually the font file itself, not the platform — much like [per-app quirks in Studio Effects on Google Meet](/articles/studio-effects-google-meet-not-working/) trace to the app layer, not the NPU.

### Fix 5: Repair or reinstall the Terminal package

When Terminal crashes even with a clean settings file, software rendering, and cmd.exe as the shell, the app package itself is suspect — usually a half-applied Store update.

1. Go to **Settings > Apps > Installed apps**, find **Windows Terminal**, open its advanced options, and run **Repair** first — this fixes package registration without touching your data.
2. If Repair does not help, use **Reset** — note this clears app data but your settings.json in LocalState survives; back it up anyway.
3. Still crashing? Uninstall Terminal from the same screen, restart the laptop, then reinstall **Windows Terminal** fresh from the Microsoft Store.
4. After reinstall, launch before restoring any old settings — confirm the clean app is stable, then reintroduce your settings.json from the Fix 1 backup in chunks.
5. Check Microsoft's release notes for any known-issue notices about the Terminal version you are on; occasionally a specific release has an ARM64 regression with a documented workaround.

### Fix 6: Rule out injected software with a clean boot

If a pristine Terminal on a pristine config still dies, something else is injecting into the process — overlays, hooks, and "security" tools are the usual suspects.

1. Run `msconfig`, go to **Services**, check **Hide all Microsoft services**, then **Disable all**.
2. In Task Manager's **Startup apps**, disable everything non-Microsoft, then restart.
3. Launch Terminal and use it normally for a while — stability here proves third-party interference.
4. Re-enable services and startup items in halves to bisect the culprit; screen recorders, GPU overlays, and banking-protection tools are prime suspects.
5. Once identified, check that tool's settings for an exclusion list and add `WindowsTerminal.exe` — or use the native [Process Explorer ARM64 build](/articles/process-explorer-arm64-download/) to watch exactly which DLLs load into the Terminal process.

## Closing

Windows Terminal crashes on ARM64 are config crashes far more often than platform crashes: a broken settings.json, a dead shell path, a font the renderer chokes on, or a GPU driver edge case. Reset the config, verify the shell path, tame the renderer — and only then blame the app package. Work the list in order and the terminal stops being the thing you think about.
