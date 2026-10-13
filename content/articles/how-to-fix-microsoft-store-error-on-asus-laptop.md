---
title: "Fixing Microsoft Store Errors on an ASUS Laptop"
slug: how-to-fix-microsoft-store-error-on-asus-laptop
date: 2026-09-27
categories: ["windows-errors"]
tags: ["microsoft store", "asus", "error 0x80070005"]
description: "Microsoft Store won't open or download apps on your ASUS laptop? Work through these proven fixes for Store error codes and broken app installs."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-asus-laptop.webp"
faqs:
  - q: "Why won't the Microsoft Store open on my ASUS laptop?"
    a: "The usual causes are a corrupted Store cache, broken app-licensing data, wrong date and time settings, or a damaged Windows app platform. ASUS laptops with aggressive power-saving or third-party antivirus can also block the Store's background services from starting correctly."
  - q: "How do I reset the Microsoft Store cache?"
    a: "Press Win + R, type `wsreset.exe`, and press Enter. A blank Command Prompt window appears for a few seconds, then the Store reopens automatically with a cleared cache. This fixes download stalls and error 0x80070005 in many cases without touching your installed apps."
  - q: "What does error 0x80070005 in the Microsoft Store mean?"
    a: "It is an access-denied error: the Store cannot read or write files or registry keys it needs. Common triggers include corrupted app permissions, a damaged user profile, or antivirus blocking Store operations. Resetting the Store app and repairing system files usually resolves it."
  - q: "Will resetting the Store delete my installed apps?"
    a: "No. Resetting or repairing the Microsoft Store app only clears its own data and cache — your installed apps, games, and purchases stay put. Re-registering the Store package with PowerShell is equally safe for your installed software."
---
The Microsoft Store on an ASUS laptop usually fails in one of two ways: it won't open at all, or it opens but every download stalls with a cryptic error code. Either way the root cause is rarely the laptop itself — it's the Store's cache, its licensing data, or the Windows app platform underneath it getting into a bad state.

These fixes are ordered from quickest to deepest. Most Store problems die at the cache-reset step, so don't jump ahead to the heavy repairs until the easy ones have had their chance.

## Why this happens

- **Corrupted Store cache.** The cache that speeds up browsing can itself become damaged, blocking launches and downloads.
- **Broken app licenses.** The Store's licensing database gets out of sync, so it refuses to install or update apps you own.
- **Wrong date, time, or region settings.** The Store validates security certificates against your clock — a wrong date breaks the handshake.
- **Damaged Windows app platform.** Corrupted system components that UWP apps depend on take the Store down with them.
- **Antivirus or firewall interference.** Third-party security software on ASUS laptops sometimes blocks the Store's background services.
- **A corrupted user profile.** Profile-level app data damage makes the Store fail for one user while working fine for others.

## How to fix it

Work through these in order — start with the 30-second cache reset before touching anything deeper.

### Fix 1: Reset the Store cache with wsreset

This is the fastest fix and resolves a surprising share of Store errors.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter**.
2. A blank Command Prompt window opens — leave it alone for 10 to 30 seconds.
3. The Microsoft Store launches automatically when the reset finishes.
4. Try your download or launch again. If error codes like 0x80070005 persist, move to the next fix.

### Fix 2: Check date, time, and region settings

A wrong clock silently breaks the Store's secure connections.

1. Open **Settings > Time & language > Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Go to **Settings > Time & language > Language & region** and confirm your country or region is correct.
4. Restart the Store and retry. This single fix resolves mysterious "something happened on our end" errors more often than people expect.

### Fix 3: Repair or reset the Store app itself

Windows can repair the Store app without affecting your installed apps.

1. Open **Settings > Apps > Installed apps** and find **Microsoft Store**.
2. Click the three dots, choose **Advanced options**.
3. Click **Repair** first and test the Store.
4. If it still fails, return and click **Reset** — this clears the app's data but keeps your installed apps and purchases safe.

### Fix 4: Re-register the Store with PowerShell

If the Store package registration is damaged, re-registering it rebuilds the broken links.

1. Search for **PowerShell**, right-click it, and choose **Run as administrator**.
2. Paste this command and press Enter: `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete — errors in red about packages already existing are normal and harmless.
4. Restart the laptop and open the Store. This also repairs the underlying app platform that other built-in apps depend on.

### Fix 5: Run the Store troubleshooter and repair system files

Let Windows diagnose itself, then fix any damaged components the troubleshooter can't.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
2. Apply any fixes it suggests and retest.
3. Then open an elevated **Command Prompt** and run `sfc /scannow`, followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart after both complete. System file damage is a common reason Store fixes seem to "not stick" — the same corruption also causes [error 0x80070057](/articles/error-code-0x80070057-fix/) in Windows Update.

### Fix 6: Check antivirus and ASUS utilities

Third-party software on ASUS laptops sometimes strangles the Store's background services.

1. Temporarily disable any third-party antivirus and test the Store — if it works, add the Store to the antivirus exceptions or switch products.
2. Open **Services** (search for it in the Start menu) and confirm **Microsoft Store Install Service** is set to **Manual** and can start on demand.
3. Check ASUS utilities like Armoury Crate aren't blocking background app activity in their power or performance profiles.
4. Also verify Windows isn't in S mode unexpectedly: **Settings > System > About** — S mode restricts installs to Store apps only, which confuses troubleshooting.

### Fix 7: Create a fresh user profile as a test

If the Store works for a new user, your profile's app data is the problem — not Windows itself.

1. Go to **Settings > Accounts > Other users** and add a new local user.
2. Sign in as that user and open the Microsoft Store.
3. If the Store works there, migrate your files to the new profile — repairing a deeply corrupted profile takes longer than moving.
4. Copy documents, desktop files, and browser data over, then remove the old profile once everything important is moved.

### Fix 8: Fully reinstall the Store package

When re-registering isn't enough, remove the Store completely and let Windows bring it back.

1. Open **PowerShell as administrator** and run `Get-AppxPackage *WindowsStore* | Remove-AppxPackage` to uninstall the Store.
2. Restart the laptop.
3. Reinstall it by running `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` in elevated PowerShell.
4. If the package is gone from all users, install it fresh from the built-in app installer or via `wsreset.exe -i` on newer builds, then sign in and test downloads.

## Closing

Microsoft Store errors on ASUS laptops are almost never hardware problems — they're cache corruption, clock issues, or damaged app registrations, all fixable without reinstalling Windows. Work the list from the `wsreset.exe` cache clear upward, and the Store will be downloading again. If you hit the same class of permission errors elsewhere in Windows, the [0x80070057 fix guide](/articles/error-code-0x80070057-fix/) covers the deeper system-level repairs. For download help straight from the source, the [Microsoft Store support pages](https://support.microsoft.com/en-us/windows) document every current error code. And if the Store only broke after moving to the 24H2 build, the [Microsoft Store errors in 24H2](/articles/how-to-fix-microsoft-store-error-in-windows-11-24h2/) guide covers the version-specific breakage.
