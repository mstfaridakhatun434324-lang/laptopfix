---
title: "How to Fix the Microsoft Store Not Opening on Windows 11"
slug: how-to-fix-windows-store-not-opening-on-windows-11
date: 2026-09-07
categories: ["windows-errors"]
tags: ["microsoft store", "windows 11", "app errors"]
description: "Microsoft Store won't launch on Windows 11? These proven fixes reset, repair, and reinstall the Store so you can download apps again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-on-windows-11.webp"
faqs:
  - q: "Why won't the Microsoft Store open on my Windows 11 laptop?"
    a: "The usual causes are a corrupted app cache, broken Microsoft Store files after an update, wrong date and time settings, or a Microsoft account sign-in problem. Running the built-in Store troubleshooter and clearing the Store cache with wsreset.exe fixes the majority of cases in under five minutes."
  - q: "Does wsreset.exe delete my installed apps?"
    a: "No. The wsreset.exe command only clears the Microsoft Store's temporary cache and resets the app. Your installed apps, downloads, and account stay untouched. It is the safest first step when the Store refuses to open."
  - q: "Should I reinstall the Microsoft Store with PowerShell?"
    a: "Only if repair and reset through Settings fail. Re-registering the Store package with PowerShell is a stronger fix that rebuilds its installation, but it takes longer and briefly removes the Store before restoring it."
  - q: "Can a Windows update fix a broken Microsoft Store?"
    a: "Yes. Microsoft regularly ships Store-related fixes through cumulative updates. Open Settings, go to Windows Update, and install any pending updates. If updates themselves fail, use the troubleshooter before trying deeper repairs."
---

You click the Microsoft Store icon, the window flashes or hangs on a blank splash screen, and nothing ever loads. No apps, no updates, no downloads. When the Store refuses to open, it blocks everything that depends on it, from app updates to reinstalling software you already own.

The good news is that a dead Store is almost never permanent damage. It is usually a corrupted cache, a botched update, or a small settings glitch, and Windows 11 has built-in repair tools for exactly this. Work through the fixes below in order and you will almost always get it back.

## Why this happens

- **Corrupted Store cache.** Temporary files the Store relies on get damaged, usually after an interrupted update or a crash, and the app can no longer initialize.
- **Botched Windows update.** A cumulative or feature update can leave Store components in a half-updated state, especially if the laptop shut down during installation.
- **Wrong date, time, or region.** The Store validates certificates against your system clock. If the clock is off by even a few hours, secure connections to Microsoft servers fail silently.
- **Microsoft account sign-in problem.** A stale token or a partial sign-out can leave the Store in a state where it cannot authenticate and simply refuses to render.
- **Corrupted system files.** Damaged Windows components that the Store depends on, such as the AppX deployment framework, prevent the app from launching at all.
- **Disabled services.** Background services the Store needs, like the Windows Update service, can be stopped or disabled by aggressive system cleaners or manual tweaks.
- **Conflicting software.** Third-party antivirus, firewalls, or proxy/VPN tools sometimes block the Store's connection to Microsoft's servers without showing an error.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Clear the Store cache with wsreset

This is the fastest fix and resolves the problem most of the time.

1. Press **Windows key + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window will appear for a few seconds. Do not close it manually.
3. Wait for the Store to launch automatically. If it opens, the cache is cleared and you are done.
4. If nothing happens after a minute, restart the laptop and try opening the Store again.

### Fix 2: Repair or reset the Store app in Settings

Windows 11 includes a built-in repair that preserves your data.

1. Open **Settings** and go to **Apps** > **Installed apps**.
2. Find **Microsoft Store** in the list and click the three dots, then choose **Advanced options**.
3. Click **Repair** and wait for the checkmark to appear. Try launching the Store.
4. If repair did not help, return to the same screen and click **Reset**, then **Reset** again to confirm.
5. Open the Store. A reset returns it to factory state without touching your other apps.

### Fix 3: Run the Windows Store troubleshooter

Windows 11 still ships a troubleshooter that detects Store permission and cache issues automatically.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Windows Store Apps** in the list and click **Run**.
3. Follow the prompts and apply any fixes it recommends.
4. Restart the laptop once the troubleshooter finishes, even if it reports no problems.

### Fix 4: Check date, time, and region settings

A wrong clock is a surprisingly common cause of Store failures.

1. Open **Settings** > **Time & language** > **Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** to force a time update.
4. Go to **Settings** > **Time & language** > **Language & region** and confirm your country or region is correct.
5. Try opening the Store again.

### Fix 5: Sign out and back into your Microsoft account

A stale authentication token can silently block the Store.

1. Open **Settings** > **Accounts** > **Your info**.
2. If you see a warning about verifying your identity, complete the verification steps.
3. Open the Store app if possible, click your profile picture, and choose **Sign out**.
4. Sign back in with your Microsoft account credentials.
5. If the Store will not open at all, switch to a local account and back: **Settings** > **Accounts** > **Your info** > **Sign in with a local account instead**, then reverse the process.

### Fix 6: Re-register the Store with PowerShell

If repair failed, this rebuilds the Store package from scratch.

1. Press **Windows key + X** and choose **Terminal (Admin)** or **Windows PowerShell (Admin)**.
2. Run the following command exactly: `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
3. Wait for the command to finish. It may show red text that you can safely ignore.
4. Restart the laptop and launch the Store.

### Fix 7: Check system files and Windows Update

Deep system damage needs the standard repair tools.

1. Open an elevated Terminal and run `sfc /scannow`. Wait for it to reach 100 percent.
2. If it finds unrepairable damage, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Go to **Settings** > **Windows Update** and install every pending update.
4. For related startup troubles after updates, our guide to [fixing the Store after a Windows 11 update](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/) covers additional recovery steps, and if nothing else works you can [boot into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) to isolate the problem.

If the Store still will not open after all of these, consider that third-party security software may be blocking it. Temporarily disable any VPN or proxy, whitelist the Store in your firewall, or create a new local user account to see if the Store works there. Official guidance for Store and account problems is available on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

A Microsoft Store that will not open is frustrating, but it is almost always a software problem you can fix in under half an hour. Start with `wsreset.exe`, move through repair and reset, and use PowerShell re-registration as your heavy hitter. Once the Store is back, keep Windows updated and avoid force-shutting down during updates so the problem does not come back.
