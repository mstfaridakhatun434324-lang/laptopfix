---
title: "Microsoft Store Not Opening After a Windows 11 Update? 7 Fixes"
slug: how-to-fix-windows-store-not-opening-after-windows-11-update
date: 2026-09-17
categories: ["windows-errors"]
tags: ["windows-11", "microsoft-store", "apps"]
description: "Microsoft Store will not open after a Windows 11 update? From wsreset to re-registering the app, these 7 fixes get the Store working again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-after-windows-11-update.webp"
faqs:
  - q: "Why does the Microsoft Store break after Windows updates?"
    a: "The Store is a built-in app with its own cache, licenses, and background services. A Windows 11 update can corrupt its cache, break its app registration, desync its licenses, or leave its services in a bad state. It is one of the more fragile built-in apps, which is why it breaks after updates far more often than, say, Notepad or Calculator."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting or repairing the Store app only clears the Store's own cache and settings — your installed apps, games, and purchases are tied to your Microsoft account and remain untouched. Re-registering the app package (Fix 4) is equally safe for your installed software. Your library is always recoverable from the Store's Library section once it opens."
  - q: "The Store opens but shows error 0x80072EE7 or similar. Is that the same problem?"
    a: "Related but distinct — those codes usually mean a network or account issue rather than a broken app. Check your internet connection, verify date/time are correct (Settings, then Time & language, then Date & time, then Sync now), and sign out and back into the Store. If the app itself will not launch at all, work through this guide's fixes in order."
  - q: "What does the wsreset command actually do?"
    a: "The wsreset command clears the Microsoft Store's cache without removing your apps or account. It deletes temporary download data and resets the Store's internal state, then reopens the Store automatically. Run it from the Run dialog with Windows + R — a blank Command Prompt window appears for up to a minute while it works. If the Store opens cleanly afterward, the cache was the problem."
---

You click the Microsoft Store icon after a Windows 11 update and nothing happens — or it flashes open and dies, or it hangs on the loading spinner forever. It is a classic post-update annoyance, and fortunately one of the easier ones to fix. The Store is just an app, and like any app it can be reset, repaired, and re-registered.

Work through these seven fixes in order.

## Why this happens

- **Corrupted Store cache.** The update damaged the local cache the Store app relies on at launch — the most common cause.
- **Broken app registration.** The update broke the manifest registration that tells Windows the Store app exists and how to launch it.
- **Desynced licenses.** App licenses tied to your Microsoft account can desync during major updates, blocking launch.
- **Stuck background services.** The services the Store depends on (like the Microsoft Store Install Service) can hang after an update.
- **Corrupted system files.** Damage to shared Windows app-platform files affects the Store along with other built-in apps.
- **Date/time mismatch.** The Store validates security certificates; a wrong system clock breaks that validation silently.
- **A damaged user profile.** Profile-level corruption can break Store launch for one account while others work.

## How to fix it

Work through these in order, testing the Store after each step.

### Fix 1: Reset the Store cache with wsreset

The official first step — clears the cache without touching anything else.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter**.
2. A blank Command Prompt window appears for 10-30 seconds — do not close it. The Store should launch automatically when it finishes.
3. If the Store opens, you are done. If nothing happens or an error appears, continue to Fix 2.
4. Note: `wsreset.exe` needs no admin rights and deletes no personal data — it only empties the Store's cache folders.

### Fix 2: Repair and reset the Store app in Settings

Windows has built-in repair/reset for the Store app itself.

1. Open **Settings** → **Apps** → **Installed apps**.
2. Find **Microsoft Store**, click the **...** menu → **Advanced options**.
3. First click **Repair** and wait, then test the Store.
4. If it still will not open, return and click **Reset** (this clears the app's data — your installed apps and purchases are safe), then test again.
5. Restart the laptop after a reset before judging the result.

### Fix 3: Check date, time, and the Store services

Two quick environmental checks that cause silent Store failures.

1. Right-click the taskbar clock → **Adjust date and time** → enable **Set time automatically** and click **Sync now**.
2. Press **Win + R**, type `services.msc`, press **Enter**.
3. Find **Microsoft Store Install Service** — double-click it, set **Startup type** to **Manual**, and click **Start** if it is stopped.
4. Do the same check for **Windows Update** (set to **Manual** or **Automatic**) and **Background Intelligent Transfer Service**.
5. Try launching the Store again.

### Fix 4: Re-register the Microsoft Store app package

When the app's registration is broken, rebuild it with PowerShell.

1. Press **Win + X** → **Terminal (Admin)** → **Yes**.
2. Run this command (copy-paste it exactly):
   `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete — red text for unrelated packages is normal, ignore it.
4. Restart and test. This fix resolves the stubborn cases where reset alone fails.
5. Microsoft documents the app re-registration approach in their [Windows support guides](https://support.microsoft.com/en-us/windows).

### Fix 5: Sign out and back into the Store (and Windows)

License desync is fixed by re-authenticating.

1. If the Store opens at all, click your profile icon → **Sign out**, close the Store, reopen it, and sign back in.
2. If it will not open, go to **Settings** → **Accounts** → **Your info** and verify you are signed in with your Microsoft account (not a local account).
3. As a stronger step: **Settings** → **Accounts** → **Email & accounts** → remove and re-add your Microsoft account.
4. Restart and test the Store launch.

### Fix 6: Run SFC/DISM and the Store troubleshooter

Repair the underlying platform files the Store depends on.

1. In **Terminal (Admin)**, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
2. Run the app troubleshooter: **Settings** → **System** → **Troubleshoot** → **Other troubleshooters** → **Windows Store Apps** → **Run**.
3. Apply whatever it recommends and restart. The troubleshooter often re-registers app licenses, which fixes launch failures that cache resets do not.
4. If other built-in apps (Photos, Calculator) are also broken, the platform damage is wider — the DISM repair matters more in that case, so let it run to completion without interruption.

### Fix 7: Create a new user profile or do an in-place repair

For profile-level or deep system damage.

1. Test with a new account: **Settings** → **Accounts** → **Other users** → **Add account** → create a local account, sign in, and try the Store. If it works there, migrate to the new profile.
2. If the Store is broken for all users, do an in-place repair: run the Windows 11 setup from Microsoft's installation media, choose **Upgrade this PC now** → **Keep personal files and apps**.
3. After the repair, open the Store first and let it update itself before installing anything else.

## Closing

A dead Microsoft Store after a Windows 11 update is almost always a cache or registration problem, and `wsreset.exe` plus the Settings reset (Fixes 1-2) resolve most cases in under five minutes. Only escalate to the PowerShell re-registration when the simple steps fail — and remember that your purchases and installed apps live in your Microsoft account, not in the broken app, so there is nothing to lose by resetting aggressively. Test the Store after each fix rather than running them all blindly; you will usually find the winner early. If you are troubleshooting a same-named but totally different beast, our [UNEXPECTED_STORE_EXCEPTION guide](/articles/how-to-fix-unexpected-store-exception-after-windows-11-update/) covers that blue screen; for a Store that opens but shows a black window, the [black screen after update](/articles/windows-11-black-screen-after-update-fix/) fixes overlap.
