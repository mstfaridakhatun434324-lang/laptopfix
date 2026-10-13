---
title: "How to Fix Microsoft Store Not Opening on Windows 11 24H2"
slug: how-to-fix-windows-store-not-opening-in-windows-11-24h2
date: 2026-09-01
categories: ["windows-errors"]
tags: ["microsoft store", "windows-11", "apps", "troubleshooting"]
description: "Microsoft Store won't open on Windows 11 24H2? Follow these proven fixes, from cache resets to full Store re-registration, to get it working again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-in-windows-11-24h2.webp"
faqs:
  - q: "Why won't the Microsoft Store open on Windows 11 24H2?"
    a: "The usual causes are a corrupted Store cache, damaged app package registration, incorrect date and time settings, or broken Windows Update components that the Store depends on. After the 24H2 update, mismatched app packages left over from the older build are a particularly common trigger."
  - q: "Is wsreset.exe safe to run?"
    a: "Yes. The wsreset.exe tool simply clears the Microsoft Store cache and reopens the Store; it does not delete your installed apps, purchases, or account. It is the official first troubleshooting step and takes under a minute."
  - q: "Will resetting the Store delete my installed apps?"
    a: "No. Repairing or resetting the Microsoft Store through Settings only affects the Store app itself, not the apps you installed through it. Your library and purchase history are tied to your Microsoft account and remain intact."
  - q: "What if the Store opens but shows a blank page?"
    a: "A blank Store usually means a network or region issue rather than a broken app. Check that your date, time, and region are correct, disable any VPN or proxy temporarily, and run the cache reset. If the catalog still won't load, re-register the Store package with PowerShell."
---

You click the Microsoft Store icon, the splash screen flashes for a second, and then... nothing. Or it opens to a gray void. On Windows 11 24H2 this has become a familiar annoyance, usually showing up after a feature update leaves the Store's app package in a half-migrated state.

The Store is a system app, so you cannot just uninstall and reinstall it like normal software. But you can reset its cache, repair its registration, and fix the services it depends on. The steps below go from quick to thorough, and one of them almost always does the trick. Before you start, make sure you are signed in with your Microsoft account and that your internet connection is working, since both are easy to overlook when the Store itself will not open to tell you.

## Why this happens

- **Corrupted Store cache.** Leftover cache from before the 24H2 upgrade can prevent the new Store package from launching.
- **Broken app registration.** The Store's package registration can be damaged by interrupted updates or disk errors.
- **Wrong date, time, or region.** The Store validates security certificates and licensing against your clock; a wrong setting silently blocks it.
- **Disabled or broken Windows Update services.** The Store relies on update components to check licenses and download apps.
- **VPN or proxy interference.** Network tools that reroute traffic can break the Store's connection to Microsoft's servers.
- **Corrupted user profile data.** Sometimes the Store works fine in a new user account but not in yours, pointing to profile-level corruption.
- **Pending system updates.** 24H2 had follow-up cumulative updates that fixed Store launch bugs for many users.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Reset the Store cache with wsreset

The official first step, and it fixes a surprising number of cases.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter**.
2. A blank Command Prompt window appears; wait for it to close on its own.
3. The Microsoft Store should open automatically when the reset finishes.
4. If the Store opens now, you are done. If it flashes and closes again, move on to the next fix without repeating this one.

### Fix 2: Repair and reset the Store app in Settings

A deeper reset that keeps your apps and account intact.

1. Open **Settings** then **Apps** then **Installed apps**.
2. Find **Microsoft Store**, click the three dots, and choose **Advanced options**.
3. Click **Repair** and test the Store.
4. If it still fails, return and click **Reset**, confirm, and test again.
5. Restart the laptop after the reset for good measure.

### Fix 3: Check date, time, and region settings

A wrong clock silently kills Store licensing checks.

1. Open **Settings** then **Time & language** then **Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** under Additional settings.
4. Go to **Language & region** and confirm your **Country or region** is correct.
5. Try launching the Store again.

### Fix 4: Re-register the Store with PowerShell

This rebuilds the Store's package registration from scratch.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Paste this command and press **Enter**:
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete; red errors about packages in use are usually harmless.
4. Restart the laptop and launch the Store.

### Fix 5: Fix Windows Update components

The Store depends on update services, so repair them.

1. Open **Terminal (Admin)** and run these commands one at a time:
   `net stop wuauserv`
   `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
   `net start bits`
2. Open **Settings** then **Windows Update** and install all pending updates.
3. Restart and test the Store.

### Fix 6: Disable VPN and proxy temporarily

Network rerouting is a classic cause of Store connection failures.

1. Disconnect any VPN client completely.
2. Open **Settings** then **Network & internet** then **Proxy**.
3. Turn off **Automatically detect settings** and **Use a proxy server** if enabled.
4. Also check **VPN** and disconnect any configured VPN.
5. Launch the Store; if it works, re-enable your VPN afterward and test again. Some VPN providers also offer split tunneling, which lets you exclude the Store from the tunnel while keeping everything else protected.

### Fix 7: Run SFC and DISM

System file damage can break Store dependencies, especially after a rough 24H2 upgrade.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow` and let it finish.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` if needed.
4. Restart and test the Store.

### Fix 8: Test in a new user account

This tells you whether the problem is system-wide or profile-specific.

1. Open **Settings** then **Accounts** then **Other users**.
2. Click **Add account** and create a new local user.
3. Sign in as the new user and launch the Store.
4. If it works there, your main profile is corrupted; migrate your files to the new account.
5. If it fails there too, consider an in-place upgrade using media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

If the Store launches but downloads stall, Microsoft's own [Windows support](https://support.microsoft.com/en-us/windows) has current service-status notes, and our guide to [Windows 11 install error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-youtube/) covers the update errors that often travel with Store problems. A stuck update can also leave the system hanging on restart, which our [restarting screen guide](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-reddit/) addresses.

## Closing

A dead Microsoft Store on 24H2 is annoying but almost never serious. The cache reset handles the easy cases, PowerShell re-registration handles the stubborn ones, and the new-user test tells you exactly where the damage lives. Once it is working again, keep Windows updated; Microsoft quietly fixed several Store launch bugs in post-24H2 cumulative updates, and staying current is the best prevention. If the Store breaks again after a future feature update, start with wsreset before anything else, since cache corruption after upgrades remains the single most common cause.
