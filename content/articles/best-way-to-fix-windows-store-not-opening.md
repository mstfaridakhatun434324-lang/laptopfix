---
title: "Best Way to Fix Microsoft Store Not Opening on Windows"
slug: best-way-to-fix-windows-store-not-opening
date: 2026-09-23
categories: ["windows-errors"]
tags: ["Microsoft Store", "Store won't open", "app repair"]
description: "Microsoft Store won't open or crashes instantly? Reset the cache, repair the app, and get the Store working again with these proven fixes."
thumbnail: "/images/thumbs/best-way-to-fix-windows-store-not-opening.webp"
faqs:
  - q: "Why won't the Microsoft Store open?"
    a: "The usual causes are a corrupted Store cache, damaged app package files, incorrect date and time breaking the Store's secure connection, a disabled required service, or corrupted system files. The Store is a system app with many dependencies, so any one of them failing can prevent it from launching — but the cache reset fixes the large majority of cases in under a minute."
  - q: "Will resetting the Microsoft Store delete my apps?"
    a: "No. Resetting or repairing the Store app only clears its cache and restores its own files — your installed apps, games, and purchases tied to your Microsoft account are untouched. You may need to sign back into the Store afterward, but nothing you installed goes away."
  - q: "What does wsreset.exe do?"
    a: "It clears the Microsoft Store's cache without changing your settings or installed apps. When the cache holds corrupted data, the Store can fail to launch or show blank pages; wsreset wipes that cached data so the Store rebuilds it fresh on next launch. It is safe, fast, and the correct first step for almost any Store misbehavior."
  - q: "The Store opens but shows a blank page. Is that the same problem?"
    a: "Usually, yes — same family of causes. A blank Store typically means the cache is corrupted or the Store cannot reach Microsoft's servers, so check your date and time settings, internet connection, and proxy settings in addition to running wsreset. If the machine is on a work or school network, content filtering may also block the Store's endpoints."
---

The Microsoft Store not opening is one of those small miseries: you click the icon, it bounces or flashes, and nothing happens — or it opens to a blank void. You do not need the Store every day, which is exactly why it is annoying when you do need it and it refuses. App updates, new installs, and even some system components route through it.

The fix is almost always quick. The Store keeps a local cache that corrupts easily, and clearing it resolves most cases in under a minute. The steps below start there and work through the deeper causes — services, date/time, app package repair, and system file fixes — for the stubborn remainder. If you have been ignoring a dead Store for months, expect a backlog of app updates waiting once it revives; let them install before judging whether everything works.

## Why this happens

- **Corrupted Store cache.** Damaged cached data prevents launch or renders blank pages.
- **Damaged Store app package.** The app's own files corrupted by updates or disk errors.
- **Wrong date, time, or region.** Breaks the TLS certificates the Store needs to talk to Microsoft.
- **Disabled background services.** Required services like Install Service set to disabled.
- **Proxy or VPN interference.** Rerouted traffic blocking Store endpoints.
- **Corrupted system files.** Damaged shared components the Store depends on.
- **Broken Microsoft account sign-in state.** A stale or half-signed-in account token confusing the Store's authentication.

## How to fix it

Work through these in order, testing the Store after each step.

### Fix 1: Reset the Store cache with wsreset

The one-minute fix that works most often.

1. Press `Win + R`, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears — wait; do not close it.
3. After 30-60 seconds the Store should open on its own with a cleared cache.
4. If the Store still will not open, restart the laptop once — the cache clear sometimes needs a fresh boot to take full effect.
5. Try browsing and installing an app to confirm.

### Fix 2: Check date, time, and region

A wrong clock silently breaks the Store's secure connections.

1. Right-click the taskbar clock, choose **Adjust date and time**.
2. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Go to **Settings > Time & language > Language & region** and confirm the region matches your actual location.
4. Retry the Store.

### Fix 3: Repair and reset the Store app

When the cache clear is not enough, repair the app package itself.

1. Go to **Settings > Apps > Installed apps**.
2. Find **Microsoft Store**, click the **...** menu, and choose **Advanced options**.
3. Click **Repair** first and test the Store.
4. If it still fails, return and click **Reset** — this reinstalls the app's data (your installed apps are unaffected).

### Fix 4: Run the Store Apps troubleshooter

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** (Windows 11) or **Settings > Update & Security > Troubleshoot > Additional troubleshooters** (Windows 10).
2. Run the **Windows Store Apps** troubleshooter and apply its fixes.
3. Restart and test.

### Fix 5: Check required services and disable proxy/VPN

1. Press `Win + R`, type `services.msc`, and press Enter.
2. Ensure **Microsoft Store Install Service** is not disabled — set it to **Manual** if needed.
3. Verify **Windows Update** service is running, since the Store shares update infrastructure.
4. Fully exit any VPN app and check **Settings > Network & Internet > Proxy** — disable **Use a proxy server** unless required.
5. Retry the Store.

### Fix 6: Re-register the Store with PowerShell

Reinstalls the Store package registration without touching your data.

1. Open **Terminal (Admin)** from `Win + X`.
2. Run:
   `Get-AppXPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete — red errors about already-installed packages are normal and safe to ignore.
4. Restart and test the Store.

### Fix 7: Repair system files

If the Store's shared dependencies are damaged:

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and test.

For update-related Store failures, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) can supply specific fixes manually, and Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the official Store troubleshooting path.

More targeted walkthroughs: [Store not opening step by step](/articles/how-to-fix-windows-store-not-opening-step-by-step/) and [Store not opening on Windows 11](/articles/how-to-fix-windows-store-not-opening-on-windows-11/).

### Fix 8: Refresh the Microsoft account sign-in and check license sync

A stale account token can silently break the Store.

1. Open the Store (or attempt to), click the profile icon, and sign out of your Microsoft account.
2. Go to **Settings > Accounts > Your info** and verify your account shows correctly; use **Verify** if prompted.
3. Sign back into the Store with the same account.
4. In the Store, click the profile icon and check for pending app updates — install them all, since outdated Store components themselves cause launch failures.
5. If apps show licensing errors, open **Settings > Apps > Installed apps**, pick a failing app, and use **Advanced options > Repair**.

## Closing

A dead Microsoft Store is usually a thirty-second problem wearing a scary disguise — wsreset.exe clears the corrupted cache and life goes on. When it does not, the repair/reset in app settings and the PowerShell re-registration cover the deeper app-package damage, and the date/time check catches the silent certificate failures. Run through the list once, and the Store will be back to updating your apps in the background like nothing ever happened. If you have been ignoring a dead Store for months, expect a backlog of app updates waiting once it revives; let them install before judging whether everything works. And if the Store breaks again soon after, look at what changed on the system around that time — a new VPN, a "debloater" script, or a feature update are the usual repeat offenders. Fix the trigger, not just the symptom.
