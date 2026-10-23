---
title: "How to Fix Visual Studio ARM64 Installer Issues on Windows"
slug: visual-studio-arm64-installer-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["visual studio", "arm64", "installer", "visual studio 2022", "snapdragon", "troubleshooting"]
description: "Fix Visual Studio installer issues on ARM64 Windows: stuck downloads, workload errors, and component detection bugs — step-by-step fixes for Snapdragon PCs."
thumbnail: "/images/thumbs/visual-studio-arm64-installer-issues.webp"
faqs:
  - q: "Is there a native ARM64 version of Visual Studio?"
    a: >
      Yes — Visual Studio 2022 version 17.4 and later ships a native ARM64 build for Windows 11 on ARM. Make sure you download the ARM64 bootstrapper rather than the x64 one; the x64 build runs under emulation and misses the point of having the native toolchain.
  - q: "Why does the installer hang on 'Downloading' forever?"
    a: >
      Usually a corrupt package cache, a stalled network connection, or security software intercepting the download. Clear the Packages cache under ProgramData, pause third-party antivirus during the install, and retry with the installer running as administrator — that combination unblocks the vast majority of hangs.
  - q: "The installer finished but my workload is missing. What happened?"
    a: >
      The installer likely picked up a different architecture's components than you expected, or a package failed silently. Check the Individual components tab for the ARM64 variants, read the installer log in the Temp folder for the exact failing package ID, and use Repair before attempting a full reinstall.
  - q: "Can I install both ARM64 and x64 Visual Studio side by side?"
    a: >
      You can, but avoid it unless a specific workload has no ARM64 equivalent. Mixed side-by-side installs confuse component detection and double the update surface — keep native ARM64 as the daily driver and emulate only the workloads that truly lack a native option.
---

You launch the Visual Studio Installer on your Snapdragon laptop to add the .NET workload, and it hangs on "downloading," throws a cryptic package error, or finishes but Visual Studio can't find the ARM64 components it just installed. The installer worked fine on Intel, so this feels like an ARM problem — but the failure is almost always in the installer's machinery, not in Visual Studio itself.

Visual Studio 2022 has a native ARM64 build, yet the installer juggles three architectures at once — ARM64, x64 under emulation, and the shared installer service — plus per-machine caches, strict Windows build requirements, and security software that loves to quarantine installer payloads mid-download. Most failures live in that machinery.

These six fixes run in order: Windows prerequisites first, then running the installer correctly, then cache surgery, then repair, then architecture mix-ups, and finally disk health. Don't skip the early steps — a missing Windows update is the cause more often than a corrupt installation.

## Why this happens

- **Out-of-date Windows build:** The ARM64 installer validates the OS build before touching anything, and it fails cryptically on older Windows 11 builds.
- **Corrupt installer cache:** Interrupted downloads leave partial packages in the cache that the installer keeps retrying instead of re-downloading.
- **Security software interference:** Defender, SmartScreen, or third-party antivirus quarantining payloads mid-install produces errors that blame the package, not the scanner.
- **Architecture confusion:** x64 components selected alongside ARM64 ones, or the wrong bootstrapper downloaded in the first place.
- **Broken update channel:** The installer stuck between update channels, or a half-applied installer update that never completed.
- **Disk space or drive issues:** Large workloads need tens of gigabytes free plus a healthy SSD — a full or failing drive produces "random" package failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Bring Windows up to date first

The ARM64 installer validates the OS build before it touches anything, and it fails cryptically on old builds. Update first, install second — this ordering matters.

1. Open **Settings > Windows Update**, install everything pending, then restart — twice if a second wave of updates appears after the first reboot.
2. Confirm you're on a current Windows 11 build in **Settings > System > About**; very old builds are simply too aged for the current installer.
3. If Windows Update itself errors, run the troubleshooter under **Settings > System > Troubleshoot**, or fetch the specific update from the Microsoft Update Catalog (https://www.catalog.update.microsoft.com/).
4. If an update repeatedly fails, [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) document the supported fixes — they beat guessing.
5. Only after Windows is fully current should you launch the installer again.

### Fix 2: Run the installer the right way

A surprising share of installer failures are permissions and stale state. A clean, elevated launch with a fresh bootstrapper clears them.

1. Download the latest bootstrapper fresh — old bootstrappers pull old installer versions. Double-check it's the **ARM64** bootstrapper, not x64.
2. Right-click it and choose **"Run as administrator"** — the installer needs elevation for per-machine components.
3. Temporarily pause third-party antivirus during the install and re-enable it immediately after; Windows Security usually cooperates, third-party suites are the troublemakers.
4. If SmartScreen flags a payload, verify the file's digital signature first, then allow it once — don't train yourself to click through blindly.
5. Install one workload at a time for the first run; piling on five workloads at once multiplies the failure surface for no benefit.

### Fix 3: Clear the installer cache

Interrupted or failed installs leave partial packages in the cache that poison every retry. Clearing it forces genuinely fresh downloads instead of reusing broken ones.

1. Close the installer and Visual Studio completely — a running instance will hold locks on the cache.
2. Delete `%ProgramData%\Microsoft\VisualStudio\Packages` (the download cache); it rebuilds itself on next launch.
3. Clear `%Temp%` as well — stale temp payloads are a quiet source of signature-mismatch errors.
4. Relaunch the installer as administrator and retry the workload before doing anything more drastic.
5. Only if the installer itself is broken should you reach for `InstallCleanup.exe -f` — it removes everything Visual Studio-related, so treat it as the last resort of this fix, not the first step.

### Fix 4: Repair instead of reinstalling

When the installer runs but a workload misbehaves afterward, Repair fixes component registration without the hours a full reinstall costs. It's the most underused button in the installer.

1. Open **Visual Studio Installer > More > Repair** on the installed instance.
2. Let it complete on AC power with the machine set not to sleep — sleep mid-repair corrupts installer state.
3. If Repair fails, use **More > Uninstall** for the broken workload only, then reinstall just that workload rather than everything.
4. Check the installer logs in `%Temp%` for the specific failing package ID before escalating — the log names the culprit precisely instead of the generic error dialog.
5. For recurring per-user quirks — settings not sticking, extensions misbehaving — remember installer state can be per-user, the same class of issue as [Recall app exclusions not saving](/articles/recall-app-exclusions-not-saving/), where per-user state turned out to be the whole story.

### Fix 5: Fix ARM64/x64 component mix-ups

The installer can silently install x64 components where you expected ARM64, or vice versa. Don't assume — verify what's actually on disk and what Task Manager reports.

1. In the installer, open the **Individual components** tab and confirm the ARM64 variants are selected for the toolchains you need.
2. After install, check Task Manager while Visual Studio runs: the main `devenv.exe` process should report **ARM64** architecture, not x64 emulated.
3. If the wrong architecture landed, use **Modify** to swap the component set rather than layering both architectures on top of each other.
4. For .NET work, install the ARM64 .NET SDK separately and confirm `dotnet --info` reports an ARM64 runtime.
5. Keep x64 emulation only for workloads with no ARM64 equivalent — don't mix architectures "just in case," since it doubles the update surface.

### Fix 6: Check disk space and drive health

A full or failing SSD produces the strangest installer errors — package failures that change on every retry and blame a different component each time. Rule the drive out before blaming the installer further.

1. Free at least **30–40 GB** on the system drive before a big workload install; the installer needs scratch space well beyond the final footprint.
2. Run a drive health check (CrystalDiskInfo or your maker's own tool) and apply any pending SSD firmware from the support page — the [SSD firmware update guide](/articles/ssd-firmware-update-arm-laptop/) walks through that exact check.
3. If the drive uses BitLocker, confirm it's in a healthy state — a suspended or error-state BitLocker can block writes in ways that surface as package failures.
4. Retry the install once the drive is healthy and spacious; "random" failures that vanish at this point were never random.

## Closing

Visual Studio installer issues on ARM64 are almost always environment, not product — current Windows, an elevated clean installer, a fresh cache, and the right architecture. Work the list once and the installer becomes as boring on Snapdragon as it is on Intel. And for those marathon install-and-configure sessions with the IDE glowing for hours, the [OLED burn-in prevention tips](/articles/oled-burn-in-prevention-windows-11/) are worth a skim.
