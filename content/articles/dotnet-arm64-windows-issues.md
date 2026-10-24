---
title: "How to Fix .NET (dotnet) Issues on ARM64 Windows Laptops"
slug: dotnet-arm64-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["dotnet", "arm64", "developer", "windows 11", "sdk", "troubleshooting"]
description: "The .NET SDK or runtime failing on your ARM64 Windows laptop? Follow these step-by-step fixes for the right installer, PATH issues, and x64 conflicts."
thumbnail: "/images/thumbs/dotnet-arm64-windows-issues.webp"
faqs:
  - q: "Does .NET support Windows on ARM natively?"
    a: >
      Yes — Microsoft publishes native ARM64 builds of the .NET SDK and runtime for Windows. Download the installer labeled ARM64 from Microsoft's .NET download page; the x64 installer will run under emulation and cause architecture conflicts.
  - q: "Why does dotnet say the SDK is not found after installing?"
    a: >
      This is almost always a PATH problem or an architecture mismatch: the x64 dotnet may be shadowing the ARM64 one, or the installer added the wrong directory to PATH. Run where dotnet to see which binary resolves, and check that the ARM64 install folder comes first.
  - q: "Can ARM64 .NET run x64 NuGet packages?"
    a: >
      Managed (pure .NET) packages run fine on any architecture. Packages with native x64 binaries will fail on ARM64 — look for ARM64-native versions of the package, or replace the native dependency with a managed alternative.
  - q: "Should I install both x64 and ARM64 .NET on my Snapdragon laptop?"
    a: >
      Only if you need to run x64 .NET apps under emulation. For native ARM64 development, install just the ARM64 SDK to avoid PATH shadowing. If both are needed, manage the order in PATH carefully — the same discipline applies to [Java JDK installs on ARM Windows](/articles/java-jdk-arm-windows-install/).
---

You installed the .NET SDK on your Snapdragon laptop, opened a terminal, typed `dotnet --info` — and got "command not found," a crash, or an SDK list that shows the wrong architecture. Your projects built fine on your old machine, but here even `dotnet new console` misbehaves.

.NET on Windows ARM is genuinely native — Microsoft ships full ARM64 SDKs and runtimes — but the installer ecosystem is full of traps: the download page defaults to x64, old scripts install the x64 SDK under emulation, and having both architectures installed creates PATH shadowing where the wrong `dotnet.exe` wins. The result looks like a broken SDK when it is really a wrong-architecture SDK. The same ARM64-first rule applies across the dev stack — [Copilot in Teams not working on laptops](/articles/copilot-in-teams-not-working-laptop/) and [Paint generative fill issues](/articles/paint-generative-fill-not-working/) are different features, but they share the "install the ARM build, not the x64 build" root cause pattern.

This guide gives you six fixes in order: install the correct ARM64 SDK, fix PATH and shadowing, resolve runtime-vs-SDK mismatches, handle native dependencies, fix Visual Studio integration, and clean up mixed-architecture installs. All commands run in PowerShell or Terminal.

## Why this happens

- **x64 SDK installed instead of ARM64:** The .NET download page defaults to x64. On ARM Windows the x64 SDK runs under emulation, producing crashes, wrong-architecture builds, and confusing `dotnet --info` output.
- **PATH shadowing between architectures:** With both x64 and ARM64 SDKs installed, whichever `dotnet.exe` appears first in PATH wins. A stale x64 entry silently shadows the ARM64 SDK.
- **Runtime/SDK version mismatch:** A project targeting .NET 8 with only the .NET 9 SDK (or vice versa) fails to run — the "you must install a runtime" error that looks like a broken install.
- **Native NuGet dependencies without ARM64 binaries:** Packages wrapping x64 native DLLs fail at runtime on ARM64 even though the managed code compiles fine.
- **Visual Studio installing the wrong workloads:** The VS installer can pull x64-targeted components or miss the ARM64 build tools, breaking builds launched from the IDE while command-line builds work.
- **Corrupted install from mixed script runs:** Install scripts that detect the OS as "Windows" without checking architecture download x64 binaries, leaving a half-native, half-emulated mess.
- **Emulated terminal resolving the wrong dotnet:** Running `dotnet` from an x64-emulated terminal (or an x64 VS Developer Prompt) can resolve the emulated SDK even when the ARM64 SDK is correctly installed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 .NET SDK

Start by ensuring the SDK itself is the right architecture — everything downstream depends on this.

1. Uninstall any existing .NET SDK entries from **Settings > Apps > Installed apps** (note the architecture column — remove x64 SDKs you do not need).
2. Go to Microsoft's .NET download page and explicitly choose the **ARM64** installer for Windows — do not accept the default x64 download.
3. Run the installer and let it complete; restart your terminal afterwards so PATH changes take effect.
4. In a new PowerShell window, run `dotnet --info` and check the **RID** line — it must read **win-arm64**, not win-x64.
5. Run `dotnet new console -o armtest` then `dotnet run` inside it — a clean "Hello, World!" proves the SDK is functional.

### Fix 2: Fix PATH order and architecture shadowing

When `dotnet` resolves to the wrong binary, the fix is PATH surgery, not reinstallation.

1. In PowerShell, run `where.exe dotnet` (or `Get-Command dotnet | Select-Object Source`) to see every dotnet on your PATH in resolution order.
2. The ARM64 SDK installs to `C:\Program Files\dotnet` while the x64 SDK uses `C:\Program Files (x86)\dotnet` — note which appears first.
3. Open **Settings > System > About > Advanced system settings > Environment Variables** and edit the system **Path**.
4. Move `C:\Program Files\dotnet` above any x86 dotnet entries — or remove the x64 entries entirely if you do not need emulated .NET.
5. Open a fresh terminal and re-run `where.exe dotnet` and `dotnet --info` to confirm the ARM64 SDK now wins.

### Fix 3: Match runtimes to your projects' target frameworks

"SDK works but my app won't run" is a runtime mismatch, not an SDK problem. Align the installed runtimes with what your projects target.

1. Run `dotnet --list-runtimes` and note which versions and architectures are installed (look for **Microsoft.NETCore.App** entries with **arm64**).
2. Open your project's `.csproj` and check `<TargetFramework>` — e.g. `net8.0` needs the .NET 8 runtime.
3. If the matching runtime is missing, download the **ARM64** runtime installer (or the full SDK, which includes runtimes) for that major version.
4. For self-contained deployments, publish with `dotnet publish -r win-arm64 --self-contained` so the app carries its own runtime.
5. Re-run the app and confirm the "must install .NET runtime" error is gone.

### Fix 4: Handle native dependencies and NuGet packages

Builds succeed but the app crashes loading a native library — the package has no ARM64 binaries.

1. Read the crash output for `BadImageFormatException` — that exception name is the signature of an architecture mismatch in a native dependency.
2. Check the NuGet package page for an ARM64 or `win-arm64` native asset; upgrade to a version that ships one.
3. If no ARM64 build exists, look for a managed-code alternative to the package that avoids native binaries entirely.
4. As a temporary workaround, you can run the app under x64 emulation with the x64 runtime — expect noticeably slower performance.
5. For your own native interop, compile the native component for ARM64 and place the DLL where the `win-arm64` RID resolution expects it.

### Fix 5: Fix Visual Studio's ARM64 targeting

Command-line builds work but Visual Studio builds fail — the IDE is targeting the wrong architecture.

1. In Visual Studio Installer, confirm you installed the **.NET desktop development** workload with ARM64 support, not just x64 components.
2. In your solution, open **Build > Configuration Manager** and set the platform to **ARM64** (create it via **New** if it is missing).
3. Check the project's debug settings — the **Start** action should launch the ARM64 dotnet host, not an emulated one.
4. Clean the solution (**Build > Clean Solution**), delete `bin` and `obj` folders, and rebuild to clear stale x64 artifacts.
5. Run from Visual Studio and confirm the process architecture in Task Manager shows **ARM64**, not x86 or x64 emulation.

### Fix 6: Clean up mixed-architecture installs completely

When several partial fixes have stacked up, the reliable path is a full purge and a single clean ARM64 install.

1. Uninstall every .NET SDK and runtime from **Settings > Apps**, both x64 and ARM64.
2. Delete leftover folders: `C:\Program Files\dotnet` (ARM64) and `C:\Program Files (x86)\dotnet` (x64) if they remain.
3. Remove all dotnet entries from the system PATH, then restart the laptop.
4. Install only the **ARM64** SDK for the .NET version you need, from Microsoft's official download page.
5. Verify with `dotnet --info` (RID: win-arm64), then reinstall only the additional runtimes your projects need — ARM64 builds only.

## Closing

.NET on ARM64 Windows is a first-class, native experience — the failures are almost never the framework itself but the wrong installer, PATH shadowing, or x64 native dependencies sneaking in. Keep one rule: ARM64 SDK, ARM64 runtimes, ARM64 NuGet natives, and verify with `dotnet --info` whenever something looks off. The one honest limitation is the native-dependency gap — if a package you need ships x64 binaries only, you either find an alternative or accept emulation. For installer and version questions, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) points to the current .NET download and ARM64 documentation.
