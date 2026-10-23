---
title: "How to Fix PowerShell 7 Problems on ARM Windows"
slug: powershell-7-arm-windows-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["powershell 7", "arm64", "windows on arm", "pwsh", "modules", "troubleshooting"]
description: "Fix PowerShell 7 issues on ARM Windows: install the true ARM64 build, repair execution policy and profiles, handle incompatible modules, and reinstall cleanly."
thumbnail: "/images/thumbs/powershell-7-arm-windows-issues.webp"
faqs:
  - q: "How do I know if my PowerShell 7 is running under emulation?"
    a: "Open PowerShell 7 and run $env:PROCESSOR_ARCHITECTURE. If it prints AMD64 on your ARM laptop, you installed the x64 build and it is running through Prism emulation. A true ARM64 install prints ARM64. Reinstall using the ARM64 package to fix it."
  - q: "Why do some PowerShell modules fail to load on ARM?"
    a: "Modules that ship native x64 binaries — certain SQL, VMware, or hardware-vendor modules — cannot load into an ARM64 PowerShell process. Use the module's pure-managed alternative where one exists, or run those specific commands from Windows PowerShell 5.1, which has broader legacy compatibility on ARM."
  - q: "Can I install PowerShell 7 with winget on a Snapdragon laptop?"
    a: "Yes. Running winget install --id Microsoft.PowerShell --source winget on an ARM64 machine pulls the ARM64 build automatically. If you previously installed the x64 MSI by hand, uninstall it first so you do not end up with two architectures fighting over file associations."
  - q: "Why does my PowerShell profile break after an update?"
    a: "Updates can change module paths or reset PSReadLine versions, and a profile that assumed the old layout throws errors at every launch. Temporarily renaming the profile to test a clean start isolates the problem in seconds."
---

You installed PowerShell 7 on your Snapdragon laptop expecting the fast, modern shell from your old machine — but scripts throw odd errors, favorite modules refuse to import, tab completion stutters, or the whole thing feels oddly sluggish. Worse, sometimes there are *two* PowerShell 7s and you are never sure which one a script actually launched.

On Windows 11 on ARM, PowerShell 7 problems trace back to a small set of causes: the wrong architecture build running under emulation, a profile or module written for x64 assumptions, execution-policy confusion between the many installed shells, or a botched update that left two builds fighting. Each has a clean fix.

This guide gives you six fixes in diagnostic order: verify the architecture, repair policy and profiles, handle incompatible modules, fix the Windows Terminal integration, and finish with a clean reinstall if the install itself is the problem.

## Why this happens

- **x64 build installed instead of ARM64:** The GitHub release page lists several assets, and the x64 MSI is easy to grab by mistake. It runs, but through emulation — slower, and a trap for native modules.
- **Two architectures side by side:** An x64 install plus an ARM64 install means scripts, shortcuts, and file associations may launch either one unpredictably.
- **Execution policy set on the wrong shell:** Windows PowerShell 5.1 and PowerShell 7 keep separate policies. Setting it in one does nothing for the other, which confuses everyone at least once.
- **Modules with native x64 binaries:** Some modules bundle compiled x64 DLLs that simply cannot load into an ARM64 process — no setting fixes that, only a different module or a different host.
- **Stale or machine-specific profiles:** Profiles that hard-code x64 paths (`Program Files` instead of `Program Files (Arm)`) or assume modules that moved will error on every launch.
- **PSReadLine version mismatches:** The prompt-rendering module ships with Windows PowerShell 5.1 in an old version; mixing versions across hosts causes garbled input or crashes.
- **Broken Windows Terminal default profile:** Terminal may still point at the old x64 `pwsh.exe` path after you switch architectures, so the "fixed" install never actually launches.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm and install the true ARM64 build

Everything downstream — modules, speed, Terminal integration — depends on running the native build. Verify first; it takes ten seconds.

1. Open PowerShell 7 and run `$env:PROCESSOR_ARCHITECTURE` — you want **ARM64**. If it prints **AMD64**, you have the emulated x64 build.
2. Also run `[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture` to double-confirm the process architecture.
3. If it is wrong, uninstall the x64 build via **Settings > Apps > Installed apps** (look for "PowerShell 7-x64").
4. Install the ARM64 build with `winget install --id Microsoft.PowerShell --source winget` from an elevated prompt — winget selects the ARM64 asset automatically on ARM machines.
5. Re-run the architecture check, and confirm the Start Menu shortcut now launches the ARM64 build. If odd audio-adjacent symptoms made you doubt the platform generally, remember ARM quirks are usually per-app — [Dolby Atmos issues on ARM laptops](/articles/dolby-atmos-arm-laptop-not-working/) are a driver matter, not a sign your shell is broken.

### Fix 2: Set the execution policy on the right shell

"Script cannot be loaded because running scripts is disabled" in PowerShell 7 is not fixed by changing policy in Windows PowerShell 5.1. Each shell owns its policy.

1. In **PowerShell 7** (the ARM64 one), run `Get-ExecutionPolicy -List` and note the `CurrentUser` and `LocalMachine` scopes.
2. Set it where you need it: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` is the usual safe choice for a dev machine.
3. If a script still refuses, check whether it is blocked at the file level: right-click the .ps1, open Properties, and clear **"This file came from another computer"** with Unblock-File.
4. For scheduled or automated runs, prefer signing scripts or scoping policy to the task's user rather than setting `Unrestricted` machine-wide.
5. Document the policy you chose — six months from now, "it worked on my old laptop" will mean "the policy was different," and [missing system info like an unlisted NPU](/articles/msinfo32-npu-not-listed/) teaches the same lesson: check what the machine actually reports, not what you remember.

### Fix 3: Handle modules that will not load on ARM64

When `Import-Module` fails with a bad-image or architecture error, the module ships native x64 code. No compatibility flag loads an x64 DLL into an ARM64 process — you need a different strategy per module.

1. Read the actual error: "could not load file or assembly" with a BadImageFormatException means native-architecture mismatch, not a corrupt download.
2. Check the module's documentation or gallery page for an ARM64 or pure-managed build — many popular modules have quietly added one.
3. If none exists, run just those commands from **Windows PowerShell 5.1** (the inbox x86/ARM-compatible host), which keeps broader legacy module support on ARM Windows.
4. As a bridge, use PowerShell 7's Windows compatibility feature: `Import-WinModule` proxies 5.1 modules into your 7 session for cmdlets that do not need native speed.
5. Pin module versions that work: after finding a working combination, note the versions — gallery updates occasionally regress ARM support, and [offline speech-model downloads for Live Captions](/articles/live-captions-offline-speech-models/) show the same pattern of version-sensitive components.

### Fix 4: Repair a broken profile and PSReadLine

If every launch prints red errors before you type anything, or tab completion and syntax coloring behave strangely, the profile or PSReadLine is the culprit — not PowerShell itself.

1. Test a clean start: launch `pwsh -NoProfile`. If the errors vanish, your profile is the problem.
2. Open the profile path with `pwsh -NoProfile -Command $PROFILE` and rename that file temporarily (append `.bak`).
3. Rebuild the profile minimally: re-add lines in small groups, restarting each time, until the offender shows itself — usually a hard-coded x64 path or an `Import-Module` for a module that moved.
4. For PSReadLine weirdness, run `Get-Module PSReadLine` and update it: `Install-Module PSReadLine -Force -AllowPrerelease` (current versions fixed several rendering bugs).
5. Keep the profile under version control or at least backed up — a profile is code, and treating it like code saves the next rebuild.

### Fix 5: Fix the Windows Terminal default profile

After switching architectures, Windows Terminal often keeps launching the old x64 `pwsh.exe` — so your "fixed" install never runs and nothing seems to change.

1. In Windows Terminal, open **Settings > Startup** and check which profile is the default.
2. Open **Settings > Profiles** and inspect the PowerShell profile's **Command line** — it should point at the ARM64 install path, typically under `Program Files\PowerShell\7\pwsh.exe` (not `Program Files (x86)`).
3. If it points to the old x64 path, update the command line or delete the stale profile and let Terminal re-detect PowerShell on next launch.
4. Test with the architecture one-liner from Fix 1 inside the Terminal-launched session — trust the output, not the profile name.
5. If Terminal itself misbehaves after the change, [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) document the supported reset and repair paths for inbox apps.

### Fix 6: Clean-reinstall when the install itself is corrupt

When updates half-applied, uninstalls left files behind, or two builds still fight over associations, stop repairing and start over. A clean reinstall takes five minutes.

1. Uninstall **every** PowerShell 7 entry in **Settings > Apps > Installed apps** — x64 and ARM64 alike.
2. Delete leftover folders: `%ProgramFiles%\PowerShell\7` and `%ProgramFiles(x86)%\PowerShell\7` if they remain, plus check the PATH for stale entries.
3. Install servicing updates first — grab the latest cumulative update via [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is being stubborn — since servicing-stack issues can break MSIX/MSI installs.
4. Reinstall cleanly with `winget install --id Microsoft.PowerShell --source winget` and verify architecture with Fix 1's check.
5. Reinstall needed modules fresh from the gallery rather than copying old module folders — stale native binaries are how this mess starts.

## Closing

PowerShell 7 on ARM Windows fails for boring, fixable reasons: the wrong architecture build, a policy set on the wrong shell, a module with x64-only binaries, or a profile written for another machine. Verify ARM64 first, then work the list — policy, modules, profile, Terminal, and finally a clean reinstall — and the shell becomes as dependable as it was on x64.
