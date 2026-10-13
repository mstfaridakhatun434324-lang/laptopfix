---
title: "How to Fix Microsoft Store Errors on an HP Laptop"
slug: how-to-fix-microsoft-store-error-on-hp-laptop
date: 2026-09-19
categories: ["windows-errors"]
tags: ["microsoft-store", "hp", "windows-11"]
description: "Microsoft Store not opening or showing errors on your HP laptop? Follow these proven fixes for 0x80070005, 0x803F8001, and other Store error codes."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-hp-laptop.webp"
faqs:
  - q: "Why won't the Microsoft Store open on my HP laptop?"
    a: "The most common causes are a corrupted Store cache, incorrect date and time settings, a broken Windows Update component, or sign-in problems with your Microsoft account. On HP laptops specifically, outdated network drivers from a fresh Windows install can also prevent the Store from reaching Microsoft's servers."
  - q: "What does Microsoft Store error 0x80070005 mean?"
    a: "Error 0x80070005 is an access-denied error. It usually means the Store's app packages or cache folders have wrong permissions, often after a failed update. Resetting the Store app and running the WSReset cache-clearing tool fixes it in most cases without touching your installed apps."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store through Settings only clears the Store app's own data and cache. Your installed apps, games, and purchases stay untouched because they are tied to your Microsoft account, not to the Store app's local cache."
  - q: "Do I need a Microsoft account to use the Microsoft Store?"
    a: "You can browse the Store with a local account, but downloading and updating apps requires signing in with a Microsoft account. If sign-in itself fails with an error, that is a separate account or network issue — try signing in at account.microsoft.com in a browser first to confirm your credentials work."
---
Few things are more annoying than clicking the Microsoft Store icon and getting a spinning loader, a blank page, or an error code instead of your apps. On HP laptops this tends to surface after a Windows update, a fresh install from HP's recovery media, or when the Store's cache quietly corrupts itself over time. The good news: Store errors are almost always repairable in a few minutes, and your apps and purchases are safe throughout.

The Store depends on more moving parts than most people realize — your Microsoft account sign-in, the date and time, Windows Update components, and several background services all have to agree. So instead of randomly trying things, work through the fixes below in order. Each one targets the next most likely cause, and one of them fixes the problem nearly every time.

## Why this happens

- **A corrupted Store cache** — temporary files the Store keeps for faster loading get damaged, and the app hangs or throws an error on launch.
- **Wrong date, time, or region settings**: the Store validates security certificates against your clock, so even a few minutes' drift can block connections.
- **Broken Windows Update components**: the Store shares update machinery with Windows Update, so a stuck update service breaks Store downloads too.
- **Microsoft account sign-in problems** — expired credentials, two-factor hiccups, or a corrupted account token in Windows.
- **Outdated HP network drivers** after a clean install, leaving the Wi-Fi driver too old to hold a stable TLS connection to Microsoft's servers.
- **Third-party antivirus or firewall rules** that block the Store's background traffic while letting the browser through, which makes the problem confusing to diagnose.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Run WSReset to clear the Store cache

This is the classic first step for a reason: it fixes the majority of Store launch failures in under a minute, and it touches nothing else.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window will open — don't close it. Wait while it clears the cache.
3. The Microsoft Store will launch automatically when the reset finishes. Try browsing or updating an app.
4. If the Store still misbehaves, move on to Fix 2 — the cache wasn't the (only) problem.

### Fix 2: Check date, time, and region

A wrong clock is the sneakiest cause of Store errors because everything else on the laptop can look perfectly fine.

1. Open **Settings** → **Time & language** → **Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** under Additional settings to force an immediate sync with Microsoft's time servers.
4. Go to **Time & language** → **Language & region** and confirm your country is correct, then relaunch the Store.

If your clock keeps drifting after every reboot, the CMOS battery may be dying — a cheap fix, but one worth knowing about before you chase software causes.

### Fix 3: Repair and reset the Store app

Windows lets you repair the Store without reinstalling anything, which fixes damaged app packages.

1. Open **Settings** → **Apps** → **Installed apps**.
2. Find **Microsoft Store** in the list, click the three dots, and choose **Advanced options**.
3. Click **Repair** first and wait for the checkmark, then test the Store.
4. If repair doesn't help, click **Reset** on the same page and confirm. This wipes the Store's local data but keeps your apps and purchases.

For related app problems beyond the Store itself, our guide to fixing the [Start menu not working on Windows 11](/articles/how-to-fix-start-menu-not-working-on-windows-11-on-hp-laptop/) covers similar repair tools for other broken built-in apps.

### Fix 4: Run the Windows Store Apps troubleshooter

Microsoft's built-in troubleshooter checks the services and permissions the Store depends on.

1. Open **Settings** → **System** → **Troubleshoot** → **Other troubleshooters**.
2. Find **Windows Store Apps** and click **Run**.
3. Apply whatever fix it recommends — it commonly resets hung services or repairs the Store's registration.
4. Restart the laptop after the troubleshooter finishes, even if it says no problems were found, then test again.

### Fix 5: Re-register the Store with PowerShell

If the Store's registration with Windows is damaged — common after failed updates — this command rebuilds it cleanly.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Paste this command and press Enter:
   `Get-AppXPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to finish; ignore red text unless it ends with an actual error message.
4. Restart and open the Store. This also repairs the Store's background update tasks.

### Fix 6: Fix Windows Update components

Because the Store rides on update infrastructure, a broken update service produces Store errors like 0x80070005 or endless "pending" downloads.

1. In **Terminal (Admin)**, run these commands one at a time, pressing Enter after each:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
2. Then run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair any damaged system files.
3. Open **Settings** → **Windows Update** and install any pending updates — Store fixes often ship inside cumulative updates.

Our step-by-step Store repair guide goes deeper into [update-related Store failures](/articles/how-to-fix-microsoft-store-error-step-by-step/) if this fix turns out to be the one that matters for you.

### Fix 7: Update HP network drivers and check your account

If everything above failed, the problem is usually the network path or the account itself.

1. Download the latest Wi-Fi and chipset drivers for your exact HP model from the [HP support site](https://support.hp.com/us-en) — search by serial number for the right ones.
2. In the Store, click your profile picture and sign out, then sign back in with your Microsoft account to refresh the account token.
3. Temporarily disable any third-party antivirus or firewall and test the Store — if it works, add an exception for the Store rather than leaving protection off.
4. As a last resort, create a new local user account (**Settings** → **Accounts** → **Other users**), sign into the Store there, and confirm it works — a working Store on a fresh profile means your main user profile is corrupted.

## Closing

Microsoft Store errors on HP laptops look cryptic, but they follow a pattern: cache first, clock second, app registration third, and update machinery fourth. Walk the fixes in that order and you'll land on the cause without reinstalling Windows or losing a single app. And once the Store is healthy again, let it update your apps — an up-to-date Store is far less likely to corrupt its cache the next time around.
