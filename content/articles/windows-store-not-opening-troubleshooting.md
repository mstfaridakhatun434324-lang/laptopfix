---
title: "Microsoft Store Won't Open? Get It Working Again"
slug: windows-store-not-opening-troubleshooting
date: 2026-10-03
categories: ["windows-errors"]
tags: ["microsoft store", "store not opening", "apps", "troubleshooting"]
description: "Microsoft Store won't open or crashes instantly on Windows 11? Work through these fixes — cache reset, re-registration, and update repairs."
thumbnail: "/images/thumbs/windows-store-not-opening-troubleshooting.webp"
faqs:
  - q: "Why won't the Microsoft Store open at all?"
    a: "The most common reasons are a corrupted Store cache, a broken Store app registration, incorrect date and time settings, or a stuck Windows Update state. Less often, corrupted system files or a disabled background service is responsible. The fixes below address them in order of likelihood."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store app only affects the Store itself — its cache, settings, and registration. Your installed apps, games, and their data are untouched. Re-registering the Store via PowerShell is equally safe for your app library. You will not need to reinstall anything afterward."
  - q: "The Store opens but shows a blank page — is that the same problem?"
    a: "Usually yes — it's the same family of issues. A blank or endlessly loading Store typically means cache corruption, network/proxy interference, or the Store's background services being stuck. The wsreset and service fixes below resolve blank-page cases too. Start with the cache reset before trying anything deeper."
  - q: "Do I need a Microsoft account for the Store to work?"
    a: "The Store app itself should open without signing in, though downloading apps requires a Microsoft account. If the Store won't open even before any sign-in prompt, the problem is technical — cache, registration, or system files — not your account. Sign-in trouble is a separate issue from launch failure."
---


The Microsoft Store failing to open — bouncing, flashing, or closing instantly — is one of those Windows annoyances that feels disproportionate to its cause. The Store is just an app, but it's an app with deep hooks into Windows Update, licensing services, and the app deployment engine, so when any of those misbehave, the Store is the visible casualty. The good news: the fix is almost always in the Store's own cache or registration, not in Windows itself.

Start with the symptom details. If the Store icon does nothing at all, that's usually cache or registration. If it opens and immediately closes, that's often a corrupted app package. If it opens to a blank page or spins forever, suspect network, proxy, or the background services the Store depends on. Each has a matching fix below. And if you're seeing Store *install* failures with an error code rather than a launch failure, our guide to [error 0x80070003 on Windows 11](/articles/how-to-fix-error-0x80070003-on-windows-11/) covers the update-engine side, while [how to analyze BSOD dump files](/articles/how-to-analyze-bsod-dump-files-on-laptop/) is there if system instability is the deeper issue.

## Why this happens

- **Corrupted Store cache**: The Store caches aggressively; a corrupted cache is the single most common reason it won't launch.
- **Broken app registration**: The Store's package registration can break after updates or failed installs, leaving Windows unable to start it.
- **Incorrect date and time**: The Store validates licenses and certificates — a wrong system clock breaks that validation silently.
- **Stuck Windows Update components**: The Store shares infrastructure with Windows Update; a wedged update state takes the Store down with it.
- **Disabled background services**: Services like the Microsoft Store Install Service or Background Intelligent Transfer Service, if disabled, prevent the Store from functioning.
- **Corrupted system files**: Damage to the app deployment components (AppX infrastructure) breaks Store launch.
- **Proxy or VPN interference**: Misconfigured proxy settings or a VPN can block the Store's connections, producing hangs or blank pages rather than clean errors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Store cache with wsreset

The fastest fix and the one that works most often.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears — don't close it. Wait for it to finish on its own; the Store should launch automatically when it completes.
3. If the Store launches, you're done. If nothing happens after a minute, continue to Fix 2.
4. Note: this clears the cache only — your apps, downloads, and account stay exactly as they were.

### Fix 2: Repair and reset the Store app

Use Windows' built-in app repair before anything drastic.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Find **Microsoft Store** in the list, click the **...** menu > **Advanced options**.
3. Click **Repair** first and test the Store. Repair fixes the installation without touching data.
4. If repair doesn't help, click **Reset**. This clears the Store's data and returns it to a fresh state.
5. Restart the laptop and try launching the Store again.

### Fix 3: Check date, time, and region

A wrong clock breaks Store certificate validation.

1. Right-click the taskbar clock > **Adjust date and time**.
2. Turn on **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Go to **Settings** > **Time & language** > **Language & region** and confirm your region is correct — mismatched regions can block Store content.
4. Try the Store again. This sounds trivial, but it resolves a surprising number of "won't open" cases, especially on laptops whose CMOS battery is dying and losing time.

### Fix 4: Re-register the Store with PowerShell

Rebuilds the Store's registration when the package itself is damaged.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run this command to re-register the Store package:

   ```powershell
   Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
   ```

3. Wait for it to complete — errors in red about packages already existing are normal and harmless.
4. Restart the laptop and launch the Store.
5. If PowerShell reports the package is missing entirely, continue to Fix 6 for the full reinstall.

### Fix 5: Check the Store's background services

The Store depends on services that "optimizer" tools love to disable.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Microsoft Store Install Service** — set its Startup type to **Manual** (not Disabled) and start it if it's stopped.
3. Find **Background Intelligent Transfer Service (BITS)** — set to **Manual** or **Automatic**, and start it.
4. Find **Windows Update** service — set to **Manual** at minimum. The Store shares update infrastructure, and a disabled update service breaks it.
5. Try the Store again. If you use a "debloat" or optimizer tool, check that it isn't re-disabling these on every boot.

### Fix 6: Reinstall the Store completely

When re-registration isn't enough, remove and reinstall the package.

1. In **Terminal (Admin)**, remove the Store package:

   ```powershell
   Get-AppxPackage *WindowsStore* -AllUsers | Remove-AppxPackage
   ```

2. Then reinstall it from the system source:

   ```powershell
   Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
   ```

   If the package files are gone entirely, this step fails — in that case, the in-place upgrade in Fix 7 restores them.

3. Restart and test. Your installed Store apps remain; only the Store shell itself was replaced.

### Fix 7: Repair Windows with an in-place upgrade

The final fix for deep AppX infrastructure damage.

1. Download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run `setup.exe`, and choose **Keep personal files and apps**.
3. The repair reinstalls Windows over itself, rebuilding the entire app deployment stack the Store depends on.
4. After completion, run **Windows Update** fully — the Store and its dependencies get their latest versions through updates. Check the [Microsoft support page for Windows](https://support.microsoft.com/en-us/windows) if you need the official troubleshooting reference alongside these steps.

## Closing

A Store that won't open is rarely a Windows-is-broken situation — it's usually a corrupted cache or a broken registration, both fixed in minutes by wsreset or PowerShell re-registration. The pattern to remember: cache first, repair second, re-register third, services fourth. If you find yourself here repeatedly, look at what's breaking it — aggressive cleaner tools and debloat scripts are the usual repeat offenders.
