---
title: "Microsoft Store Error Codes: Fix Them All in Minutes"
slug: how-to-fix-microsoft-store-error-youtube
date: 2026-10-07
categories: ["windows-errors"]
tags: ["microsoft store error", "store not working", "windows 11", "error codes"]
description: "Microsoft Store showing 0x80070005, 0x80131500, or stuck downloads? Clear the cache, reset the Store, and fix every common error code."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-youtube.webp"
faqs:
  - q: "Why does the Microsoft Store show error 0x80070005?"
    a: "Error 0x80070005 is an access-denied error, usually caused by corrupt Store cache, wrong permissions on Store folders, or a broken app package registration. Clearing the cache with wsreset.exe and re-registering the Store package fixes it in most cases. If it persists after a reset, create a new local user account to test whether your user profile is damaged."
  - q: "What does error code 0x80131500 in the Microsoft Store mean?"
    a: "Code 0x80131500 typically signals a network or region problem: the Store can't reach Microsoft's servers because of proxy settings, VPN interference, incorrect date and time, or a region mismatch on your account. Check your internet connection, disable VPNs and proxies, sync your clock, and verify your Microsoft account region matches your location."
  - q: "Why are my Microsoft Store downloads stuck at pending?"
    a: "Stuck or pending downloads usually come from a corrupt Store cache, the Background Intelligent Transfer Service not running, or too many queued items. Clear the cache, restart the BITS and Windows Update services, and pause then resume the download. Signing out and back into the Store also clears stuck queues."
  - q: "Should I reinstall the Microsoft Store app itself?"
    a: "Reinstalling is a last resort, not a first step. Try wsreset.exe, the Store troubleshooter, and Settings-based repair and reset first — these resolve the overwhelming majority of errors without touching the app package. Re-register the Store with PowerShell only if reset options fail or the Store won't open at all."
---

The Microsoft Store fails in frustratingly vague ways: error codes like **0x80070005**, **0x80131500**, or **0x80072EE7**, downloads stuck on "Pending" forever, or the app opening to a blank screen. Behind those cryptic codes are a handful of repeat causes — corrupt Store cache, broken app registrations, network and proxy interference, wrong system time, and damaged user profiles. Fix the cause family and the specific code usually resolves with it.

Work the list from least destructive to most. Nearly every Store error surrenders to a cache clear or a reset; almost none require reinstalling Windows, despite what some forums suggest. If the Store won't open at all rather than showing an error, also check our guide on [Store not opening after updates](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/); for a Store that opens but misbehaves on one brand of laptop, see [Store not opening on ASUS laptops](/articles/how-to-fix-windows-store-not-opening-on-asus-laptop/).

## Why this happens

- **Corrupt Store cache**: The Store keeps a local cache of licenses, downloads, and page data. When it corrupts, you get error codes, blank pages, and stuck downloads.
- **Broken app package registration**: Windows tracks the Store as an app package; if that registration breaks (often after a feature update), the Store errors or won't launch.
- **Network, proxy, or VPN interference**: The Store is picky about TLS and endpoints — proxies, VPNs, and aggressive firewalls break its server communication with cryptic codes.
- **Incorrect date, time, or region**: Store licensing and server authentication depend on correct time and matching region settings.
- **Stopped background services**: The Store depends on BITS, Windows Update, and the Microsoft Store Install Service. If they're disabled, downloads stall.
- **Corrupt user profile**: Sometimes the Store works fine in a new user account but errors in yours — the profile's app data is damaged.
- **Pending Windows updates**: The Store and Windows Update share infrastructure; a broken update state breaks both.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the Store cache with wsreset

The fastest fix and the right first move for almost every Store error.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window opens for 10–60 seconds while the cache clears. Don't close it.
3. The Microsoft Store launches automatically when done. Try your download or page again.
4. If the error persists, move on — but note that this fixes roughly half of all Store error codes by itself.

### Fix 2: Check date, time, region, and network basics

Authentication failures masquerade as Store errors.

1. Open **Settings** > **Time & language** > **Date & time**. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
2. In **Time & language** > **Language & region**, confirm your **Country or region** matches your actual location and your Microsoft account region.
3. Temporarily disconnect any **VPN** and disable proxy: **Settings** > **Network & internet** > **Proxy** > turn off **Use a proxy server** and **Automatically detect settings** if misconfigured.
4. Retry the Store. If it works with the VPN off, add an exception for Microsoft Store traffic in your VPN app rather than leaving it off.

### Fix 3: Run the Store troubleshooter and repair the app

Windows has built-in tools for exactly this.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run the **Microsoft Store Apps** troubleshooter. Apply any fixes it suggests.
2. Go to **Settings** > **Apps** > **Installed apps**, find **Microsoft Store**, click the **…** menu > **Advanced options**.
3. Click **Repair** first (keeps your data) and test. If the error remains, click **Reset** (clears Store data and sign-in — you'll sign in again).
4. For error 0x80070005 specifically, Reset resolves it more often than Repair.

### Fix 4: Restart the Store's background services

Stuck downloads are usually a service problem.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Background Intelligent Transfer Service (BITS)** — set **Startup type** to **Automatic** and click **Start** if it's stopped.
3. Do the same for **Windows Update** and **Microsoft Store Install Service**.
4. Open the Store, go to **Library**, and click **Get updates** to flush the stuck queue. Pause and resume any download still showing "Pending."

### Fix 5: Re-register the Store with PowerShell

When the app package registration itself is broken.

1. Open **Terminal (Admin)** or **PowerShell (Admin)**.
2. Run this command to re-register the Store for all users:
   `Get-AppXPackage -AllUsers -Name Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete (errors in red about already-registered packages are normal and safe to ignore).
4. Restart the laptop and open the Store. If it now launches and works, the registration was the problem.

### Fix 6: Test in a new user account

Isolates profile corruption in minutes.

1. Open **Settings** > **Accounts** > **Other users** > **Add account**. Create a local account without a Microsoft account for the test.
2. Sign out and sign into the new account. Open the Microsoft Store and try the failing action.
3. If the Store works in the new account, your main profile's app data is corrupt. Migrate your files to the new account rather than fighting the old one.
4. If it fails in the new account too, the problem is system-wide — continue to Fix 7.

### Fix 7: Install pending Windows updates and repair system files

Shared infrastructure means shared fixes.

1. Open **Settings** > **Windows Update** and install everything pending, then restart. Check [Microsoft's support site](https://support.microsoft.com/en-us/windows) if an update itself fails.
2. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart once more and test the Store. At this point you've repaired the cache, the registration, the services, the profile question, and the system files — remaining failures are rare and usually tied to a specific broken update, which Microsoft documents on its support pages.

## Closing

Microsoft Store errors look cryptic but they're almost never mysterious: cache, registration, network, services, profile — in that order. Work the list patiently and resist the urge to reinstall Windows over a Store code; the Store is a replaceable app package, and the fixes above resolve the overwhelming majority of cases without touching your files or the rest of the system.
