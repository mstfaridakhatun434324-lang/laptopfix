---
title: "How to Fix AutoHotkey Not Working on ARM Windows"
slug: autohotkey-arm-windows-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["autohotkey", "arm windows", "hotkeys", "scripts", "windows on arm"]
description: "AutoHotkey scripts failing on your Snapdragon laptop? Fix AutoHotkey on ARM Windows with these proven native v2 build, elevation, and script-porting steps."
thumbnail: "/images/thumbs/autohotkey-arm-windows-not-working.webp"
faqs:
  - q: "Does AutoHotkey work on Windows on ARM?"
    a: >
      Yes. AutoHotkey v2 ships native ARM64 builds, and most scripts run fine — hotkeys, remaps, and GUI scripts all work. Problems come from running the x64 build under emulation, or scripts that call x86-only DLLs or read x64-specific registry paths.
  - q: "Why does my script work on Intel but fail on my ARM laptop?"
    a: >
      The usual causes are DllCall to an x86-only DLL, hardcoded paths like Program Files (x86), registry redirection differences, or COM objects that only exist in x64. The script logic is fine — its system calls assume an x64 machine.
  - q: "Should I use AutoHotkey v1 or v2 on ARM?"
    a: >
      Use v2. It has the best ARM64 support, active development, and cleaner syntax. v1 is in maintenance mode and its ARM story is weaker — migrating scripts to v2 is worth it on a new ARM laptop.
  - q: "Why do my hotkeys not fire in some apps?"
    a: >
      Hotkeys fail in elevated (admin) windows when AutoHotkey runs unelevated, and some games and secure-input fields block hooks. Running the script as administrator fixes the elevation case; the rest are by-design input protections.
---

AutoHotkey is the duct tape of Windows productivity — your hotkeys, text expansions, and little automation scripts. On your Snapdragon laptop, some scripts do nothing, others throw errors about DLLs, and hotkeys refuse to fire in certain apps. The automation you depend on is unreliable.

AutoHotkey v2 does have native ARM64 builds, so the interpreter itself is fine. The failures are at the boundaries: the x64 build under emulation, scripts calling into x86-only DLLs, registry and filesystem redirection differences between ARM64 and x64 processes, and elevation mismatches with hotkey hooks.

This guide gives you six fixes in order: get the native build, fix elevation, adapt scripts for ARM64 paths, handle DLL and COM calls, debug systematically, and manage the v1/v2 question. If another keyboard utility also fights your hotkeys, the conflict pattern matches [PowerToys hotkey issues](/articles/powertoys-arm64-windows-issues/) — only one app can own a hotkey.

## Why this happens

- **x64 AutoHotkey under emulation:** The old installer runs emulated — mostly fine, but hooks and DLL calls behave differently enough to break scripts.
- **Scripts calling x86-only DLLs:** DllCall into a DLL that exists only as x86 fails in the ARM64 process — no emulation fallback inside a native process.
- **Registry/filesystem redirection:** ARM64 processes see different registry views and Program Files paths than scripts written for x64 expect.
- **Elevation mismatch:** Unelevated scripts cannot hook elevated windows — hotkeys silently fail in admin apps.
- **Antivirus blocking hooks:** Keyboard hooks look suspicious to security software; blocked hooks mean dead hotkeys with no error.
- **v1 scripts on v2 interpreter (or vice versa):** Syntax differences cause silent failures or cryptic errors when versions mismatch.
- **Secure input fields:** Password fields and some games block hooks by design — no script can override that.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install native ARM64 AutoHotkey v2

The foundation. The native build's hooks and system calls behave correctly on ARM64 Windows; the emulated x64 build is where the subtle breakage lives.

1. Uninstall your current AutoHotkey from **Settings > Apps > Installed apps**.
2. Download AutoHotkey **v2** ARM64 from autohotkey.com on the Snapdragon laptop.
3. Install and confirm the version in the script's tray icon or the installer details.
4. Test your simplest script first — a basic hotkey remap — before running complex ones.
5. If the simple script works and complex ones fail, the interpreter is fine and the scripts need ARM64 adaptation (Fix 3). WireGuard's ARM client followed the same native-build-first lesson: [WireGuard on ARM Windows](/articles/wireguard-arm-windows-issues/).

### Fix 2: Run scripts as administrator

The classic silent failure: hotkeys work everywhere except in admin windows (Task Manager, installers, elevated apps). The script is not broken — it is underprivileged.

1. Right-click your script and choose **Run as administrator**, then test the failing hotkeys.
2. If they work elevated, make it permanent: create a scheduled task that runs the script at logon with highest privileges, or set the compiled exe to always run as admin.
3. For scripts you run manually, right-click > Properties > Compatibility > **Run this program as an administrator** on the AutoHotkey executable.
4. Accept that UAC prompts at startup are the cost — scripts needing admin cannot silently elevate.
5. Test hotkeys in both normal and admin windows to confirm full coverage.

### Fix 3: Adapt scripts for ARM64 paths and registry

Scripts written for x64 machines hardcode assumptions that break on ARM64: Program Files paths, registry views, and System32 redirection. These are small edits once you know the pattern.

1. Replace hardcoded `C:\Program Files (x86)\` paths — on ARM64, native apps live in `C:\Program Files\`, and the (x86) folder holds emulated apps.
2. For registry reads, be aware that an ARM64 process sees the native registry view; if your script read x64-specific keys, verify the key exists in the view the script sees.
3. Use `A_ProgramFiles` and built-in variables instead of hardcoded paths — they resolve correctly per architecture.
4. Test file operations with `FileExist()` checks before acting — silent path failures are the hardest to debug.
5. When a script automates another app, confirm that app's install path on this machine rather than assuming the old PC's layout. ThinkPad ARM machines show the same path surprises: [ThinkPad T14s Gen 6 issues](/articles/lenovo-thinkpad-t14s-gen6-problems/).

### Fix 4: Fix DllCall and COM incompatibilities

The hard boundary: a native ARM64 process cannot load x86 DLLs, period. Scripts that DllCall into third-party x86 DLLs will fail, and the fix is at the DLL level, not the script level.

1. Identify the failing call — run the script and read the exact error line; DllCall failures name the DLL.
2. Check whether an ARM64 (or ARM64EC) version of the DLL exists — many vendors now ship them.
3. If the DLL is yours or open-source, rebuild it for ARM64 — often just a recompile.
4. For COM objects, verify the component is registered for ARM64 — x64-only COM servers are invisible to ARM64 AutoHotkey.
5. As a workaround, keep a portable x64 AutoHotkey for the specific script that needs the x86 DLL, and run everything else native. Be honest here: some legacy DLLs will never get ARM64 builds, and the dual-install workaround is the real answer. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the architecture boundaries.

### Fix 5: Debug systematically with logging

When a script "does nothing," guessing wastes hours. AutoHotkey has built-in debugging — use it to find the exact failing line instead of rewriting the whole script.

1. Add `ListLines` and temporary `MsgBox`/`ToolTip` calls to trace execution — find where the script stops.
2. Check `#Warn` directives — enable them to surface common issues like uninitialized variables.
3. Run the script from a console/command line to see stderr output that the tray icon hides.
4. Isolate the failing section into a minimal test script — if the minimal version fails, you have a reproducer to fix or report.
5. Compare behavior with the same script on the x64 portable build — differences pinpoint ARM64-specific issues versus general script bugs.

### Fix 6: Handle antivirus and finalize the setup

The last layer is external interference plus long-term maintenance: security software eating hooks, and keeping the setup sane going forward.

1. If hotkeys die randomly, check your antivirus quarantine and behavior-blocker logs for AutoHotkey entries — add exclusions for your scripts folder.
2. Windows Defender is generally fine with AHK; third-party suites with "anti-keylogger" features are the usual blockers — configure their exceptions.
3. Compile critical scripts to .exe (ARM64) with the built-in compiler for reliability — compiled scripts avoid interpreter-path issues.
4. Keep scripts in a synced folder (OneDrive/Documents) so the setup survives machine changes.
5. Document which scripts need admin and which need the x64 portable build — future-you will thank present-you. Auto Super Resolution gaming tweaks live in the same "tune per machine" world: [Auto SR games not working](/articles/auto-super-resolution-games-not-working/).

## Closing

AutoHotkey on Snapdragon laptops works well as the native ARM64 v2 build — emulation and x86-DLL boundaries cause nearly every failure. Most scripts need no changes at all; the ones that break are calling into architecture-specific DLLs or assuming x64 paths, and the fixes are small, mechanical edits. Get the build right, run elevated where needed, and the duct tape holds.
