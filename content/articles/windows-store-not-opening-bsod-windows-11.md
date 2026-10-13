---
title: "Windows Store Not Opening and BSOD on Windows 11? Fix Both"
slug: windows-store-not-opening-bsod-windows-11
date: 2026-09-17
categories: ["windows-errors"]
tags: ["microsoft store", "bsod", "store not opening", "windows 11"]
description: "Microsoft Store won't open AND you're getting blue screens on Windows 11? These share a root cause — fix it once with this ordered guide."
thumbnail: "/images/thumbs/windows-store-not-opening-bsod-windows-11.webp"
faqs:
  - q: "Can a broken Microsoft Store cause blue screens?"
    a: "Not directly — the Store is a user-mode app and can't crash the kernel. When both fail together, they share a root cause: corrupted system files, a bad update, a failing drive, or a broken user profile affecting both. Fix the shared cause and both symptoms clear up together."
  - q: "Why does the Microsoft Store just flash and close?"
    a: "The classic 'flash and close' means the Store app's package registration or its cached data is corrupted. The wsreset.exe cache clear fixes this in most cases; if not, re-registering the Store package with PowerShell or resetting the app in Settings usually does it."
  - q: "Will wsreset.exe delete my installed apps or games?"
    a: "No. wsreset.exe only clears the Microsoft Store's cache — it doesn't touch installed apps, games, downloads, or your Microsoft account. It's completely safe and takes about thirty seconds. Your library and installed apps remain exactly as they were."
  - q: "What if the Store works in a new account but not mine?"
    a: "That points to corrupted per-user Store data or profile damage. You can try deleting the Store's local cache folders for your profile, but migrating to the new account is usually faster and more reliable. Copy your files over and reinstall your apps there."
---
A Microsoft Store that won't open, paired with blue screens, looks like two separate breakdowns — but a technician sees one patient with two symptoms. The Store is a user-mode app; it cannot cause a kernel crash. So when both fail together, the smart move is to hunt the shared root cause: corrupted system files, a bad update, a dying drive, or profile damage. Fix that once, and both problems leave together.

Work this list in order — shared-cause repairs first, then Store-specific fixes. The order matters because Store-only fixes (like wsreset) will seem to work temporarily if the real cause is underneath, only for the symptoms to return. Start at the foundation and you'll fix it once, properly.

## Why this happens

- **Corrupted system files.** Damage to shared Windows components breaks both the Store framework and kernel stability.
- **A bad Windows update.** Updates have shipped that broke Store packages while also delivering a crashing driver.
- **Failing storage.** Bad sectors corrupt Store app data and system files simultaneously.
- **Corrupted user profile.** Profile-level damage breaks per-user Store data and can load bad shell components.
- **Broken Store cache or registration.** The Store's own cache or app registration can corrupt independently.
- **Microsoft Store background services.** The Install Service and related background services the Store depends on can fail silently after updates.
- **Third-party antivirus.** Over-aggressive AV can quarantine Store components while its kernel filter causes blue screens.
- **Date and time drift.** If the system clock is significantly wrong, Store authentication fails and app launches misbehave — verify the clock is set to automatic in **Settings > Time & language**.

## How to fix it

Work through these in order.

### Fix 1: Repair system files with SFC and DISM

The highest-value shared-cause fix.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `sfc /scannow` and let it complete.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart, then test the Store and use the laptop normally for a few hours. If both symptoms are gone, corrupted files were the shared cause.
5. If SFC reports it couldn't fix some files, run DISM first and then SFC again — the second pass usually succeeds once the component store is repaired.

### Fix 2: Clear the Store cache with wsreset

The classic Store-specific fix — fast and safe.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears for about 30 seconds — don't close it.
3. The Store should launch automatically when the reset completes.
4. If the Store opens now, the cache was the problem. If it still flashes and closes, continue.

### Fix 3: Reset and re-register the Store app

When the cache clear isn't enough, repair the app package.

1. Go to **Settings > Apps > Installed apps**, find **Microsoft Store**, click the three dots, choose **Advanced options**.
2. Click **Repair** first and test; if that fails, click **Reset**.
3. If reset doesn't help, open **Terminal (Admin)** and run:
   `Get-AppXPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
4. Restart and test the Store again.
5. After re-registering, sign out of the Store app itself (profile icon > Sign out) and sign back in — stale authentication tokens cause "flash and close" behavior that survives app resets.

### Fix 4: Check for a bad Windows update

If both problems started after an update, suspect it.

1. Go to **Settings > Windows Update > Update history** and compare dates with symptom onset.
2. Use **Uninstall updates** to remove the most recent one, then restart.
3. Test the Store and watch for blue screens for a day.
4. If symptoms clear, pause updates for two weeks. Grab verified fixed builds from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) before unpausing.

### Fix 5: Remove conflicting antivirus

AV products can break Store components and crash the kernel — matching your symptom pair.

1. Fully uninstall third-party antivirus from **Settings > Apps > Installed apps**.
2. Restart with **Windows Security** as your protection.
3. Test the Store and monitor for blue screens.
4. If both clear, the AV was the shared cause. For the deeper AV-to-BSOD connection, see the [UNEXPECTED_STORE_EXCEPTION guide](/articles/best-way-to-fix-unexpected-store-exception/).

### Fix 6: Check drive health

A failing drive corrupts unrelated components simultaneously.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`, type Y, and restart for the scan.
2. Check SMART status with your SSD maker's health tool.
3. If warnings appear, back up immediately and plan a replacement.
4. Healthy drive results let you proceed confidently to the profile test.

### Fix 7: Test a new user profile, then reset if needed

The last software layers.

1. Create a new local administrator account in **Settings > Accounts > Other users**.
2. Sign in and test the Store there; use the account for a few hours to check for blue screens.
3. If the new profile is clean, migrate your files to it.
4. If problems persist system-wide, do **Settings > System > Recovery > Reset PC > Keep my files > Cloud download**. For Store-only issues without blue screens, the [dedicated Store fix guide](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/) goes deeper.
5. After the reset, verify the Store opens and updates an app successfully before reinstalling your full software set — confirm the foundation is solid first.

## Closing

Store-plus-BSOD is a textbook shared-cause scenario, and the shared causes have a clear order: system files, bad update, AV, drive, profile. The wsreset trick fixes the Store alone in seconds when it's just a cache problem — but when blue screens ride along, don't stop there.

Fix the foundation, and you'll stop playing whack-a-mole with symptoms that keep coming back. Once both are stable, make a system image backup to an external drive while everything is healthy — it's the fastest recovery path if either symptom ever returns. And going forward, treat simultaneous failures as a signal: when two unrelated things break together, the cause is almost always underneath both of them, not in either one.
