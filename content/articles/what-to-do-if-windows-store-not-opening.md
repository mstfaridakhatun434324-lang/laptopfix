---
title: "Microsoft Store Won't Open on Windows 11? Here's What to Do"
slug: what-to-do-if-windows-store-not-opening
date: 2026-09-20
categories: ["windows-errors"]
tags: ["microsoft store", "store not opening", "windows 11", "appx", "wsreset"]
description: "Clicking the Microsoft Store does nothing, or it opens and instantly closes? Here's what to do — from the quick cache reset to full app re-registration."
thumbnail: "/images/thumbs/what-to-do-if-windows-store-not-opening.webp"
faqs:
  - q: "Why won't the Microsoft Store open on my laptop?"
    a: "The most common reasons are a corrupted Store cache, damaged AppX app packages from a failed update, incorrect date and time settings (which break the Store's security certificates), or a disabled background service the Store depends on. Third-party debloater tools that rip out 'unnecessary' Windows components are another frequent cause — they often damage the Store beyond what a simple reset can fix."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Running wsreset.exe or using the Settings > Apps > Repair/Reset option only clears the Store app's own cache and settings. Your installed apps, games, and purchases remain untouched and tied to your Microsoft account. The nuclear option — removing and reinstalling the Store package itself — also preserves your library, since that's stored server-side."
  - q: "The Store opens but shows error 0x80072EE7. What does that mean?"
    a: "That error almost always means a network or DNS problem rather than a broken Store. The Store can't reach Microsoft's servers, so check your internet connection, verify your date and time are correct, and try switching DNS to 8.8.8.8 temporarily. VPNs and aggressive firewalls also trigger this error by interfering with the Store's connections."
  - q: "Can I reinstall the Microsoft Store if nothing else works?"
    a: "Yes. You can remove the Store package with PowerShell and reinstall it, which replaces every file with a fresh copy. This fixes damage that cache resets can't touch. The exact commands are in Fix 6 below. After reinstalling, sign back in with your Microsoft account and your app library will still be there."
---

You click the Microsoft Store icon. Nothing happens. Or it flashes open and vanishes. Or it opens to an endless loading spinner. However it fails, the result is the same: you can't install apps, update the ones you have, or grab that utility you need. On Windows 11 the Store also handles updates for built-in apps like Photos, Calculator, and even the WebView components other apps depend on — so a dead Store quietly breaks more than it seems.

The Store is a system app like any other, which means it fails for the same mundane reasons: corrupted cache, damaged package files from a bad update, wrong system clock breaking its certificates, or a "debloater" script that gutted components it needs. The fixes below go from the thirty-second cache reset that solves most cases to full package reinstallation for the stubborn ones. Work in order; most people won't need to go past Fix 3.

## Why this happens

- **Corrupted Store cache**: The Store caches heavily. When that cache corrupts — after a crash, a forced shutdown, or a disk hiccup — the app can fail to launch entirely.
- **Damaged AppX package from an update**: Windows updates sometimes leave the Store's own package half-updated, a state no cache clear can fix.
- **Wrong date, time, or region**: The Store validates security certificates against your system clock. A wrong date breaks the handshake and the Store refuses to load.
- **Disabled background services**: The Store depends on services like Background Intelligent Transfer and Windows Update. "Optimization" guides that disable them break the Store as collateral damage.
- **Debloater scripts**: Third-party scripts that strip "bloat" from Windows frequently damage the Store and its dependencies beyond easy repair.
- **Corrupt Microsoft account sign-in state**: A stale or broken account token can leave the Store hanging at launch.
- **Proxy or VPN interference**: Misconfigured proxies and some VPN clients block the Store's traffic while the browser works fine, producing confusing symptoms.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Store cache with wsreset

The classic first step — fast, safe, and surprisingly effective.

1. Press **Windows + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears for a few seconds — this is normal. Don't close it.
3. When it closes on its own, the Store should launch automatically. If it launches, you're done.
4. If nothing happens, continue to Fix 2 — the problem is deeper than the cache.

### Fix 2: Check date, time, and region settings

A wrong clock silently breaks the Store's certificate validation.

1. Open **Settings** > **Time & language** > **Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Go to **Language & region** and confirm your **Country or region** is correct — a mismatched region can hide the Store entirely in some configurations.
4. Try launching the Store again. This single fix resolves a remarkable number of "Store won't open" cases, especially on laptops whose CMOS battery is dying and losing time between boots.

### Fix 3: Repair or reset the Store app

Windows can repair the app package without touching your data.

1. Open **Settings** > **Apps** > **Installed apps** and search for **Microsoft Store**.
2. Click the **...** menu > **Advanced options**.
3. First click **Repair** and test. If that fails, click **Reset** (this clears the app's data but not your installed apps or purchases).
4. Still broken? Click **Terminate** first, then **Reset** again — a hung Store process can block the reset from working.

### Fix 4: Check the services the Store depends on

"Debloated" systems often have these disabled.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Verify these are running and set to their defaults: **Background Intelligent Transfer Service** (Manual), **Windows Update** (Manual), **Microsoft Store Install Service** (Manual).
3. If any are disabled, double-click, set the correct startup type, and start them.
4. If you previously ran a debloater or "privacy" tool, consider that it may have damaged more than services — continue through the remaining fixes, and avoid such tools in future. Microsoft's [support site](https://support.microsoft.com/en-us/windows) documents the correct service defaults.

### Fix 5: Sign out and clear proxy/VPN interference

Account and network issues masquerade as a broken Store.

1. If the Store opens at all, click your profile icon and **Sign out**, then sign back in with your Microsoft account.
2. Disconnect your VPN temporarily and test — several VPN clients intercept Store traffic badly.
3. Check **Settings** > **Network & internet** > **Proxy** — turn off **Use a proxy server** unless you genuinely need one.
4. As a test, switch your DNS to **8.8.8.8** / **8.8.4.4** in your adapter settings; ISP DNS problems cause Store-specific failures that browsers seem immune to.

### Fix 6: Reinstall the Microsoft Store package

When the package itself is damaged, replace it wholesale.

1. Right-click **Start** and open **Windows Terminal (Admin)**.
2. Remove the Store: `Get-AppxPackage -allusers Microsoft.WindowsStore | Remove-AppxPackage`
3. Reinstall it for all users: `Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
4. If the reinstall command finds no package to register (because removal was total), install it fresh from an admin PowerShell with: `wsreset -i` — on current Windows 11 builds this reinstalls the Store. Then reboot and sign in. For the update-specific variant of this problem, our [companion Store fix guide](/articles/how-to-fix-windows-store-not-opening-in-windows-11-24h2/) covers additional scenarios.

### Fix 7: Repair Windows system files

Damage beyond the Store package calls for system-level repair.

1. In **Windows Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`, then restart.
3. Test the Store. These tools fix the shared components — WebView2 runtime, AppX deployment service — that the Store depends on.
4. If SFC reports unfixable damage, an in-place upgrade (Fix 8) is the next step rather than repeating scans.

### Fix 8: In-place upgrade repair install

The last resort that keeps everything: reinstall Windows over itself.

1. Download the [Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) and create Windows 11 installation media, or download the ISO directly.
2. Run **setup.exe** from within Windows (not by booting from the USB).
3. Choose **Keep personal files and apps** when prompted.
4. The process takes 30–90 minutes and replaces all system files — including a thoroughly broken Store — while preserving your files and programs.

## Closing

A dead Microsoft Store is annoying but almost never fatal: start with the thirty-second `wsreset.exe` cache clear, verify your clock and region, then repair or reinstall the app package if needed. The deeper lesson is about those "debloater" scripts and aggressive privacy tools — the Store is woven into Windows 11 more tightly than it looks, and ripping out components you don't understand is the most common way people break it beyond easy repair. Keep your system files intact, keep the clock right, and the Store generally just works. If other built-in apps are misbehaving too — Start menu search, for instance — our [Windows Search troubleshooting guide](/articles/how-to-fix-windows-search-not-working-in-windows-11-24h2/) covers the shared AppX repair techniques in more depth.
