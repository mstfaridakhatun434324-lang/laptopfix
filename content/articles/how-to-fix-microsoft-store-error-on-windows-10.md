---
title: "How to Fix Microsoft Store Errors on Windows 10"
slug: how-to-fix-microsoft-store-error-on-windows-10
date: 2026-10-02
categories: ["windows-errors"]
tags: ["Microsoft Store", "Windows 10", "app errors"]
description: "Microsoft Store not working on Windows 10? Fix error codes, stuck downloads, and sign-in problems with these steps."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-windows-10.webp"
faqs:
  - q: "Why is the Microsoft Store not opening on Windows 10?"
    a: "The usual causes are a corrupted Store cache, incorrect date and time (which breaks the Store's security certificates), a disabled Windows Update service (the Store depends on it), or corrupted Store app files. The WSReset cache clear in this guide fixes the most common case in under a minute."
  - q: "What does Microsoft Store error 0x80070422 mean?"
    a: "It means a required service is disabled — almost always the Windows Update service, which the Store needs for downloads. Re-enable it via services.msc (Startup type: Automatic) and the Store starts working again."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store app only affects the Store itself — its cache and settings. Your installed apps, games, and purchases tied to your Microsoft account are untouched and remain available for reinstall."
  - q: "Do I need to be signed in to use the Microsoft Store?"
    a: "You can browse without signing in, but downloading and updating apps requires a Microsoft account sign-in. If downloads fail with account errors, sign out and back in via the Store's profile menu — stale credentials cause a surprising share of Store errors."
---
The Microsoft Store on Windows 10 has a talent for failing in creative ways: error codes when you try to download, apps stuck at "Pending" forever, the Store itself refusing to open, or sign-in loops that go nowhere. Behind the variety, though, the causes are a short list — cache corruption, service problems, account glitches, and date/time issues — and the fixes are well-established.

This guide covers the full range: the one-minute cache reset that fixes most cases, the service and account repairs for the stubborn ones, and the deeper app-repair steps for when the Store itself is broken. Work top-down; most people stop at Fix 2.

## Why this happens

- **Corrupted Store cache.** The Store keeps a local cache of listings, images, and download state. When it corrupts — after a crashed download or a bad update — the Store misbehaves in every direction at once. The famous `WSReset.exe` exists specifically for this.
- **Wrong date, time, or time zone.** The Store validates security certificates on everything it downloads. A wrong system clock breaks validation, producing cryptic errors for what is really a clock problem.
- **Disabled Windows Update service.** The Store's download engine depends on the Windows Update service and BITS. "Debloating" tools that disable these break the Store as collateral damage — error 0x80070422 is the telltale sign.
- **Corrupted Store app files.** The Store is itself an app, and its own files can corrupt — especially after Windows updates. When the Store won't even open, its own installation is usually the problem.
- **Stale Microsoft account credentials.** Token expiry, password changes, or account security holds leave the Store signed in with credentials that no longer work, causing download and purchase errors.
- **Proxy or VPN interference.** The Store is pickier about network paths than the browser is. Misconfigured proxies and some VPNs break its connections while everything else works fine.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Reset the Store cache with WSReset

The one-minute fix that resolves the majority of Store problems.

1. Close the Microsoft Store completely — check **Task Manager** and end any **Microsoft Store** processes still running.
2. Press **Win + R**, type `WSReset.exe`, and press Enter.
3. A blank Command Prompt window appears for 10–30 seconds while the cache clears. Don't close it — wait.
4. The Store launches automatically when the reset finishes. Try your download again immediately. If the original error is gone, you're done — this was cache corruption, the most common cause.

### Fix 2: Check date, time, and time zone

The two-minute check that fixes the second-most-common cause.

1. Right-click the **taskbar clock** and choose **Adjust date and time**.
2. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Restart the Store and retry. Certificate validation is time-sensitive, and a clock that's off by even a day breaks Store downloads with misleading error codes.
4. If your clock keeps resetting to the wrong time after reboots, the CMOS battery is dying — a cheap replacement at any repair shop, and it also prevents this error from recurring.

### Fix 3: Run the Store Apps troubleshooter

Let Windows diagnose its own app platform.

1. Open **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Store Apps** and click **Run the troubleshooter**.
3. Apply whatever fixes it suggests — it commonly resets Store permissions and re-registers app packages.
4. Restart the laptop (not just the Store) and test. The troubleshooter also verifies the services the Store depends on.

### Fix 4: Verify the required services are running

The Store can't download without its engine room.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Set these to **Automatic** and **Started**: **Windows Update**, **Background Intelligent Transfer Service**, and **Microsoft Store Install Service** (if present).
3. If any were Disabled, something turned them off — check for "debloat" or "privacy" tools in **Settings > Apps** and remove them, or they'll break the Store again.
4. Retry the Store. Service-disabled errors (including the service-focused [error 0x80070422](/articles/how-to-fix-error-0x80070422-in-windows-11-24h2/)) vanish the moment the services are back. Microsoft's [support site](https://support.microsoft.com/en-us/windows) documents these service dependencies if you want the full list.

### Fix 5: Sign out and back into the Store

Clear stale account credentials.

1. Open the **Microsoft Store**, click your **profile icon** (top-right), and choose **Sign out**.
2. Close the Store completely, reopen it, click the profile icon, and **Sign in** with your Microsoft account — entering the password fresh, not relying on saved credentials.
3. If you recently changed your Microsoft account password, this step is nearly mandatory — the Store often keeps trying the old token silently.
4. After signing in, check **Library** (bottom-left) — your owned apps should list correctly, confirming the account is healthy.

### Fix 6: Repair or reset the Store app

When the Store itself is corrupted, repair its installation.

1. Open **Settings > Apps > Apps & features**, find **Microsoft Store** in the list, and click **Advanced options**.
2. First click **Repair** — this fixes the app without touching its data. Test the Store.
3. If Repair doesn't help, click **Reset** — this clears the Store's data and returns it to a fresh state. Your installed apps and purchases are unaffected (they're tied to your account, not the Store app).
4. After resetting, open the Store and let it sit for a minute — it re-syncs your library on first launch, which can look like hanging on a slow connection.

### Fix 7: Re-register the Store via PowerShell

The deep repair for a Store that won't open at all.

1. Press **Win + X** and open **Windows PowerShell (Admin)**.
2. Run this command to re-register the Store package (copy-paste it exactly):
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete — errors in red about packages "already installed" are normal and safe to ignore.
4. Restart the laptop and open the Store. Re-registration rebuilds the app's Windows integration from scratch, fixing the "won't launch" cases that Reset doesn't reach.

## Closing

Microsoft Store errors look varied but they're shallow — cache, clock, services, account, app files, in that order of likelihood. And if the Store works but Windows Update itself is failing underneath it, our [0x80004005 update guide](/articles/how-to-fix-error-0x80004005-in-windows-11-24h2/) covers the shared machinery. The WSReset trick (Fix 1) deserves to be muscle memory: any time the Store acts up, that's your first move, before you even start reading error codes. And if you used a debloating tool in the past, remember it's the prime suspect whenever Store services show up disabled — the tool "optimized" your Store into brokenness, and removing the tool is part of the permanent fix.
