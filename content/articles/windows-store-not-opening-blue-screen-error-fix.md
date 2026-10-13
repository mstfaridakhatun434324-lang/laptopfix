---
title: "Windows Store Not Opening? How to Fix It (Plus the BSOD Connection)"
slug: windows-store-not-opening-blue-screen-error-fix
date: 2026-09-20
categories: ["windows-errors"]
tags: ["microsoft store", "store not opening", "app crash", "windows 11"]
description: "Fix the Microsoft Store when it won't open — cache resets, app re-registration, service checks — plus what to do if Store activity ends in a blue screen."
thumbnail: "/images/thumbs/windows-store-not-opening-blue-screen-error-fix.webp"
faqs:
  - q: "Why won't the Microsoft Store open at all?"
    a: "Usually a corrupted app package or cache. The Store is a packaged UWP app, and if its registration breaks — common after failed updates — clicking it does nothing or it flashes and closes. Re-registering the package with PowerShell fixes it in most cases."
  - q: "Can the Microsoft Store cause a blue screen?"
    a: "The Store app itself cannot blue-screen Windows, but the things people do around it can: installing a bad driver that was delivered through the Store, or a corrupted system file that breaks both the Store and kernel components. If you get a BSOD after Store activity, troubleshoot the underlying driver or file corruption."
  - q: "Will resetting the Store delete my installed apps?"
    a: "No. Resetting or re-registering the Store only affects the Store app itself. Your installed apps, games, and purchases are tied to your Microsoft account and remain untouched."
  - q: "The Store opens but immediately closes. Is that the same problem?"
    a: "Yes — same family. An instant-close is the classic sign of a corrupted app package or license cache. Work through the cache reset and re-registration steps below; they cover both the won't-open and opens-then-closes variants."
---

Clicking the Microsoft Store and getting absolutely nothing — no window, no error, just silence — is a weirdly common Windows problem. Sometimes it flashes open and instantly closes. And occasionally, the story has a darker twist: Store activity (or an app installed from it) is followed by an actual blue screen. This guide covers both: the Store that will not open, and what to do when Store-related activity ends in a BSOD.

For Store errors that show an actual error *code*, our guide to [fixing Microsoft Store errors](/articles/how-to-fix-microsoft-store-error-on-acer-laptop/) is the better fit. This one is for the Store that will not launch at all.

Let us clear up the blue screen connection first, because it confuses people: the Microsoft Store app itself cannot cause a blue screen. It is a user-mode app with no more power to crash Windows than Notepad has. When a BSOD follows Store activity, one of two things actually happened — either the Store installed a driver update (some hardware drivers are delivered through the Store) and *that driver* crashed the system, or the system files were already corrupted and the corruption broke both the Store and something kernel-level. In both cases the Store is the messenger, and Fixes 6–7 below go after the real culprit. Do not waste time "fixing" the Store when the dump file is pointing at a driver.

## Why this happens

- **Corrupted Store app package.** The number one cause. A failed update damages the Store's registration and Windows cannot launch it.
- **Corrupted license cache.** The Store checks app licenses at launch; a damaged cache makes it bail out immediately.
- **Broken user profile app data.** The Store's per-user data can corrupt independently of the app itself.
- **Disabled or broken background services.** The Store depends on several services to even start.
- **System file corruption.** The deeper cause when the Store *and* other things (including BSODs) are misbehaving — shared system components are damaged.
- **A bad driver delivered via the Store.** Driver updates for some devices come through the Store; a bad one can destabilize the system to the point of blue screens.

## How to fix it

Work through these in order. Fixes 1–5 target the Store-not-opening problem; Fixes 6–7 address the blue screen connection.

### Fix 1: Reset the Store cache

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. Wait for the blank Command Prompt window to close and the Store to launch on its own (10–30 seconds).
3. If the Store opens now, you are done. If nothing happens, continue — the cache is clean, which later steps need.

### Fix 2: Repair the Store app in Settings

1. Go to **Settings > Apps > Installed apps**.
2. Find **Microsoft Store**, click **... > Advanced options**.
3. Click **Repair** and test. Then, if needed, click **Reset** — you will sign in again, but nothing is lost.
4. Restart the laptop after a reset before testing.

### Fix 3: Re-register the Store with PowerShell

This is the heavy hitter for the won't-open-at-all case.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Run:
   `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Ignore red errors for un-registerable system packages — normal.
4. Restart and try launching the Store. If it still refuses to open after re-registration, the corruption runs deeper than the app package — continue to Fix 6, because at that point you are likely dealing with damaged shared system components rather than a Store-specific problem.

### Fix 4: Verify the background services

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Ensure these are running (start them if not, set to Automatic):
   - **Microsoft Store Install Service**
   - **Background Intelligent Transfer Service**
   - **Windows Update**
   - **Cryptographic Services**
3. Also check **Settings > Time & language > Date & time** — enable **Set time automatically** and click **Sync now**. A wrong clock breaks the Store's license checks silently.

### Fix 5: Test in a new user account

A fresh profile tells you whether the Store's per-user data is the problem.

1. Create a new local admin account (**Settings > Accounts > Other users > Add account**).
2. Sign in as the new user and try the Store.
3. If it opens there, your original profile's Store data is corrupted — migrate to the new profile rather than fighting it.
4. If it fails there too, the problem is system-wide: continue.

### Fix 6: Repair system files (the BSOD connection)

If Store activity is followed by blue screens, or the Store *and* other apps are broken, suspect shared system corruption:

1. In an admin terminal, run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Restart and test both the Store and general stability.
4. Check the minidump from any BSOD — our guide to [checking minidump files in Windows 11 24H2](/articles/how-to-check-minidump-files-in-windows-11-24h2/) shows how. If the dump names a driver that came from a Store-delivered update, roll that driver back in **Device Manager**.

### Fix 7: Uninstall the suspect driver or update

1. If blue screens started after the Store installed a driver update, open **Device Manager**, find the device, and use **Properties > Driver > Roll Back Driver**.
2. If they started after a Windows update, go to **Settings > Windows Update > Update history > Uninstall updates** and remove it.
3. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents known problematic updates — check the KB number there before reinstalling.

## Closing

A Microsoft Store that will not open is almost always a corrupted package or cache, and the PowerShell re-registration in Fix 3 is the definitive cure. The blue screen twist is rarer and points one level deeper — to a driver or system file that the Store merely exposed. Fix the Store with the early steps, fix the underlying system with the later ones, and do not confuse the messenger (the Store) with the actual culprit (the driver or corrupted file behind it).
