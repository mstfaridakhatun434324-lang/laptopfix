---
title: "How to Fix the Microsoft Store Not Opening on Windows 10"
slug: how-to-fix-windows-store-not-opening-on-windows-10
date: 2026-10-12
categories: ["windows-errors"]
tags: ["microsoft-store", "apps", "windows-10"]
description: "Microsoft Store won't open on Windows 10? Splash screen then nothing, or instant close — here's how to get it working again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-on-windows-10.webp"
faqs:
  - q: "Why won't the Microsoft Store open on Windows 10?"
    a: "The Store is a UWP app that depends on several background services and an intact app package. Common causes: corrupted Store cache, broken app registration after an update, stopped background services, incorrect date/time breaking Microsoft's certificate checks, or corrupted system files."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store (wsreset.exe or Settings > Apps > Advanced options > Reset) only clears the Store app's own cache and data. Your installed apps, games, and purchases tied to your Microsoft account are unaffected."
  - q: "What does wsreset.exe do?"
    a: "It's Microsoft's official Store cache reset tool. Running it clears the Store's cache and re-registers the app without touching your data. The Store opens automatically when it finishes — if it opens, the fix worked. It takes under a minute and is always worth trying first."
  - q: "Can antivirus block the Microsoft Store from opening?"
    a: "Yes. Overzealous third-party antivirus or firewall software can block the Store's network access or its background processes, causing instant closes or endless loading. Temporarily disabling it (or testing in a clean boot) quickly reveals whether it's the cause."
---
You click the Microsoft Store icon, the splash screen flashes — and then nothing. Or it opens and immediately closes. Or it just sits there loading forever. On Windows 10, where the Store is also the update mechanism for built-in apps, a dead Store quietly breaks more than just shopping.

The causes are well-mapped and the fixes are quick. Here's the order to try them, from the 30-second cache reset to the deeper repairs.

## Why this happens

- **Corrupted Store cache** — the most common cause; stale or damaged cache data prevents launch.
- **Broken app registration** — a Windows update damaged the Store's package registration.
- **Stopped background services** — the Store depends on services like Background Intelligent Transfer and Windows Update.
- **Wrong date, time, or region** — Microsoft's servers reject connections when your clock is off, breaking Store authentication.
- **Corrupted system files** — damaged Windows components the Store relies on.
- **Antivirus/firewall interference** — third-party security blocking the Store's processes or traffic.
- **Microsoft account sign-in issues** — token or account problems preventing the Store from initializing.
- **Proxy or VPN interference** — network configurations that break the Store's connection to Microsoft's servers.

## How to fix it

Work through these in order — the first two resolve the majority of cases.

### Fix 1: Reset the Store cache with wsreset.exe

The official first step, straight from Microsoft.

1. Press **Windows + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears — don't close it. Wait; it closes itself when done (usually under a minute).
3. The Microsoft Store should open automatically afterward. If it opens and works, you're done.
4. If nothing happens or it still won't open, continue to Fix 2.

### Fix 2: Repair and reset the Store app

The Settings-based deeper reset.

1. Go to **Settings** > **Apps** > **Apps & features**.
2. Find **Microsoft Store** in the list, click it, and choose **Advanced options**.
3. First click **Repair** — this fixes the app without deleting its data. Test the Store.
4. If Repair doesn't help, return and click **Reset** — this clears the Store's data and cache. Test again.
5. Neither deletes your installed apps or purchases.

### Fix 3: Check date, time, and region settings

An incorrect clock silently breaks Store authentication.

1. Right-click the clock in the taskbar > **Adjust date/time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** under Synchronize your clock.
4. Go to **Settings** > **Time & Language** > **Region** and confirm your country/region is correct.
5. Try the Store again — certificate validation fails when the clock is wrong, and this fixes more cases than people expect.

### Fix 4: Re-register the Store package with PowerShell

Fix broken app registration after updates.

1. Press **Windows + X** > **Windows PowerShell (Admin)**.
2. Paste this command and press Enter:
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete — ignore red error text about already-registered packages; that's normal.
4. Restart the laptop and test the Store.

### Fix 5: Verify the required background services

The Store needs its supporting services running.

1. Press **Windows + R**, type `services.msc`, press Enter.
2. Check each of these — set **Startup type** to **Automatic** (or **Manual** where noted) and **Start** them if stopped:
   - **Background Intelligent Transfer Service** (Automatic)
   - **Windows Update** (Manual is fine, but it must be able to start)
   - **Microsoft Store Install Service** (Manual)
   - **Cryptographic Services** (Automatic)
3. Restart and test the Store.

### Fix 6: Run the Store Apps troubleshooter

Windows 10's built-in diagnostic for app problems.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters**.
2. Select **Windows Store Apps** and click **Run the troubleshooter**.
3. Apply whatever fixes it suggests and restart.
4. This tool commonly catches permission and registration issues the manual steps miss.

### Fix 7: Check antivirus, proxy, and account issues

External factors that block the Store.

1. Temporarily disable third-party antivirus/firewall and test the Store — if it works, add the Store as an exception or switch to Microsoft Defender.
2. Disconnect any VPN and test. Also check **Settings** > **Network & Internet** > **Proxy** — turn off **Use a proxy server** unless you genuinely need one.
3. Open the Store (if it opens at all) > click your profile icon > **Sign out**, then sign back in with your Microsoft account. Or go to **Settings** > **Accounts** > **Your info** and verify your account is properly signed in.
4. As a last resort, run in an admin PowerShell:
   `DISM /Online /Cleanup-Image /RestoreHealth`
   then `sfc /scannow`, restart, and retest — this repairs underlying system corruption.

### Fix 8: Reinstall the Store via PowerShell and check Windows Update

When the Store package itself is damaged beyond repair.

1. Open **Windows PowerShell (Admin)** (**Windows + X**) and run:
   `Get-AppxPackage -allusers *WindowsStore* | Remove-AppxPackage`
   This removes the Store package completely. Restart the laptop.
2. Then reinstall it by running:
   `Get-AppxPackage -allusers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
   If the package files are intact in the Windows image, this restores the Store fresh.
3. Go to **Settings** > **Update & Security** > **Windows Update** and install all pending updates — Microsoft periodically ships Store fixes in cumulative updates, and an outdated build can have Store bugs fixed months ago.
4. If the Store still won't open after a full reinstall, the underlying Windows installation has deeper damage — an in-place upgrade (run Windows 10 setup from Microsoft's media creation tool, choosing **Keep personal files and apps**) repairs it while preserving everything.

## Closing

A dead Microsoft Store on Windows 10 is almost always the cache, the registration, or a background service — `wsreset.exe` plus the Settings reset covers the vast majority of cases in under five minutes. The clock check and service verification catch the sneaky remainder, and the PowerShell reinstall handles the truly stubborn ones. If you're on Windows 11 instead, the same principles apply — see [Microsoft Store not opening step by step](/articles/how-to-fix-windows-store-not-opening-step-by-step/) and [Store not opening on Windows 11](/articles/how-to-fix-windows-store-not-opening-on-windows-11/) for the version-agnostic checklist, and Microsoft's [Store support pages](https://support.microsoft.com/en-us/windows) document the official fixes.
