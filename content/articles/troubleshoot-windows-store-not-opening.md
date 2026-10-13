---
title: "Troubleshooting the Microsoft Store Not Opening on Windows 11"
slug: troubleshoot-windows-store-not-opening
date: 2026-09-07
categories: ["windows-errors"]
tags: ["microsoft store", "store not opening", "app troubleshooter", "wsreset", "windows 11"]
description: "Microsoft Store won't open on Windows 11? Troubleshoot the splash-screen-and-crash with cache resets, re-registration, and update fixes."
thumbnail: "/images/thumbs/troubleshoot-windows-store-not-opening.webp"
faqs:
  - q: "Why does the Microsoft Store open and immediately close?"
    a: "The classic cause is a corrupted Store cache or a broken app registration — the app launches, fails its integrity check, and Windows kills it. Running WSReset.exe clears the cache, and re-registering the app package with PowerShell rebuilds the registration. One of those two fixes resolves the vast majority of open-then-crash cases."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store app only affects the Store itself — your installed apps, games, and purchases stay untouched. Even reinstalling the Store package leaves your library intact, since purchases are tied to your Microsoft account, not the local app installation."
  - q: "Can a Windows update break the Microsoft Store?"
    a: "Yes, updates occasionally leave the Store in a half-migrated state, especially feature updates. If the Store broke right after an update, check for a follow-up Store update in the app itself (if it opens) or install the latest cumulative update — Microsoft frequently ships Store fixes bundled with them."
  - q: "What if WSReset.exe doesn't fix it?"
    a: "Move to re-registering the Store package via PowerShell, then run the Windows Store Apps troubleshooter, then check for corrupted system files with SFC. If all of that fails, a new local user profile test tells you whether the problem is system-wide or confined to your user account."
---

The Microsoft Store failing to open is one of those quietly infuriating Windows 11 problems: you click the icon, the splash screen flashes, and then... nothing. Or it opens to a blank window. Or it crashes the moment you search. The Store is a UWP app with its own cache, registration, and update pipeline, and any of those layers can break independently — which is why the fix sequence matters. Randomly reinstalling things wastes time; working the layers in order doesn't.

Most Store failures come down to four things: a corrupted cache, a broken app registration, a stalled Store update, or system-file damage underneath it all. This guide walks each layer, from the 30-second cache reset to the deeper repairs, with a profile test at the end to settle whether the problem is your user account or the whole system.

## Why this happens

- **Corrupted Store cache.** Stale or damaged cache data crashes the app during launch — the most common cause.
- **Broken app registration.** The Store's package registration with Windows is damaged, so the app can't initialize.
- **Stalled or half-installed Store update.** An interrupted self-update leaves the app in an inconsistent state.
- **Corrupted system files.** Damage to the app-platform components the Store depends on.
- **Date, time, or region mismatch.** The Store validates licenses against Microsoft's servers; a wrong clock breaks authentication.
- **Disabled background services.** Required services (like the Microsoft Store Install Service) disabled by "optimizer" tools.
- **Corrupted user profile.** Store data tied to a damaged user profile fails while other accounts work fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Store cache with WSReset

The 30-second fix that resolves most cases.

1. Press **Windows + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears — wait; don't close it.
3. After 30–60 seconds the Store should launch automatically with a cleared cache.
4. If the Store opens, check for its own updates: **Library > Get updates**.
5. If nothing happens after two minutes, move on — the cache wasn't the (only) problem.

### Fix 2: Repair and reset the Store app

Use the built-in app repair pipeline.

1. Open **Settings > Apps > Installed apps**, find **Microsoft Store**.
2. Click the three dots > **Advanced options**.
3. Click **Repair** first — this fixes the installation without deleting data. Test the Store.
4. If it still fails, click **Reset** — this clears the app's data and returns it to a fresh state.
5. Launch the Store again and sign back in if prompted.

Your installed apps and purchases are unaffected by both operations. The update-triggered variant of this problem is covered in [how to fix Windows Store not opening after a Windows 11 update](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/).

### Fix 3: Re-register the Store with PowerShell

Rebuild the app's registration when repair doesn't stick.

1. Open **Terminal (Admin)** or **PowerShell (Admin)**.
2. Run: `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to complete — red text warnings during the process are usually harmless.
4. Restart the laptop (not just sign out — a full restart).
5. Launch the Store and test browsing, searching, and downloading.

This re-registers the package for all users, which also fixes cases where the Store broke for every account on the machine.

### Fix 4: Run the Store Apps troubleshooter and check services

Let Windows diagnose its own app platform.

1. Open **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Store Apps**.
2. Apply any fixes it recommends and test.
3. Press **Windows + R**, type `services.msc`, and verify these are running: **Microsoft Store Install Service** (Manual is fine) and **Windows Update** (the Store uses its pipeline).
4. If a "debloat" or "optimizer" tool disabled services, re-enable the defaults — those tools break the Store routinely.
5. Also confirm **Background apps** permissions: **Settings > Apps > Installed apps > Microsoft Store > Advanced options** — background access should be allowed.

The 24H2-specific edition lives at [how to fix Windows Store not opening in Windows 11 24H2](/articles/how-to-fix-windows-store-not-opening-in-windows-11-24h2/).

### Fix 5: Fix date, time, region, and account issues

Authentication failures masquerade as launch failures.

1. Open **Settings > Time & language > Date & time** — enable **Set time automatically** and **Set time zone automatically**, then **Sync now**.
2. Check **Settings > Time & language > Language & region** — the region should match your actual location; mismatches break Store licensing.
3. Open **Settings > Accounts** and confirm you're signed in with your Microsoft account; sign out and back in if the Store shows account errors.
4. If you use a VPN, disconnect it temporarily — region mismatches between VPN and account can block the Store.
5. Test the Store after each change so you know which one mattered.

### Fix 6: Repair system files

Fix damage in the app platform underneath the Store.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow` and restart.
3. Install all pending updates in **Settings > Windows Update** — Store platform fixes ship in cumulative updates.
4. If SFC found and repaired corruption, re-run Fix 3 (re-registration) afterward — repaired files sometimes need re-registering.
5. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a newer cumulative update if Windows Update insists you're current but the Store still fails.

### Fix 7: Test a new user profile

Determine whether the problem is your profile or the system.

1. Open **Settings > Accounts > Other users > Add account** and create a local account.
2. Sign into the new account and launch the Microsoft Store.
3. If the Store works there, your original profile's app data is corrupted — migrate to the new profile.
4. To migrate: copy your user folders (Documents, Pictures, etc.) to the new account, reinstall apps as needed, then remove the old profile.
5. If the Store fails on the new profile too, the problem is system-wide — consider an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.

## Closing

A Microsoft Store that won't open is almost always a cache, registration, or update problem — the kind of thing WSReset and PowerShell re-registration were made for. Work the layers in order instead of jumping to reinstalls, and check the unglamorous suspects (clock, region, disabled services) before assuming deep corruption. And once it's working, let the Store update itself normally and keep the "debloat" tools away from its services — most Store breakages are self-inflicted by utilities that promise to slim down Windows and deliver a broken app platform instead.
