---
title: "How to Fix Microsoft Store Errors After a Windows 11 Update"
slug: how-to-fix-microsoft-store-error-after-windows-11-update
date: 2026-09-19
categories: ["windows-errors"]
tags: ["microsoft store", "windows 11 update", "wsreset", "app error", "0x80073cf9"]
description: "Microsoft Store broken after a Windows 11 update? Fix error codes, stuck downloads, and a Store that won't open with these proven repairs."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-after-windows-11-update.webp"
faqs:
  - q: "Why does the Microsoft Store break after Windows updates?"
    a: "Feature updates rewrite shared system components the Store depends on — the AppX deployment service, licensing service, and update components. If any of those registrations break during the update, the Store shows error codes, refuses to open, or gets stuck downloading. The app itself is rarely the problem; the plumbing underneath it is."
  - q: "What does wsreset.exe do?"
    a: "wsreset.exe clears the Microsoft Store's cache and re-registers the app without deleting your installed apps or purchases. It is the official first-line fix and takes about 30 seconds. Run it by pressing Win + R, typing wsreset.exe, and pressing Enter. A blank Command Prompt window appears, then the Store opens fresh when the reset completes."
  - q: "Will resetting the Store delete my installed apps?"
    a: "No. Resetting or re-registering the Microsoft Store only affects the Store app itself. Your installed apps, games, and purchase history are tied to your Microsoft account and remain untouched. You will stay signed in in most cases, though occasionally you may need to sign back into the Store."
  - q: "What if the Store still shows an error after all repairs?"
    a: "If cache resets, re-registration, and the troubleshooter all fail, the corruption is likely in Windows itself rather than the Store. Run SFC and DISM to repair system files, or use the 'Fix problems using Windows Update' cloud repair in Settings, Recovery. As a last resort, reinstalling the Store package via PowerShell or resetting Windows will resolve it."
---
You install a Windows 11 update, everything looks fine, and then you open the Microsoft Store to grab an app — and it either refuses to open, throws an error code like 0x80073CF9 or 0x803FB005, or sits forever on a spinning download. This is one of the most common post-update annoyances, and it is almost never the Store's fault.

The update breaks one of the background services the Store relies on. The fixes below repair those services in order of least to most invasive, and one of them resolves this for the vast majority of people.

## Why this happens

- **Corrupted Store cache:** Update migrations can leave the Store's local cache in an inconsistent state, causing hangs and cryptic error codes on launch.
- **Broken AppX package registration:** The Store is a UWP app registered with the system; updates sometimes damage that registration so Windows cannot start it.
- **Damaged Windows Update components:** The Store downloads through the same delivery pipeline as Windows Update — if those components break, Store downloads stall or fail.
- **Licensing service glitches:** The ClipSVC (Client License Service) validates your app licenses; post-update it can get stuck and block Store operations.
- **Corrupted system files:** Updates that partially fail leave damaged shared libraries that the Store depends on at startup.
- **Date, time, or region mismatch:** The Store validates security certificates against your clock — a wrong system time after an update causes immediate connection errors.
- **Third-party antivirus or firewall interference:** Overzealous security software can block the Store's background services after system files change.

## How to fix it

Work through these in order, starting at Fix 1. Test the Store after each fix — most people stop at Fix 2.

### Fix 1: Reset the Store cache with wsreset

The official first step, and it fixes a surprising number of cases in under a minute.

1. Close the Microsoft Store completely.
2. Press **Win + R**, type `wsreset.exe`, and press Enter.
3. A blank Command Prompt window opens — do not close it. Wait 30-60 seconds.
4. The Store launches automatically when the reset finishes. Try downloading an app to test.
5. If the blank window closes but the Store does not open, move to Fix 2.

### Fix 2: Repair and reset the Store app in Settings

Windows can repair the Store's installation without touching your data.

1. Open **Settings > Apps > Installed apps**.
2. Find **Microsoft Store** in the list, click the three dots, and choose **Advanced options**.
3. First click **Repair** and wait for the checkmark, then test the Store.
4. If it still fails, return and click **Reset**, confirm, and test again. Reset clears the app's data but keeps your installed apps and purchases.
5. Restart the laptop after the reset for good measure.

For broader post-update breakage beyond the Store, the walkthrough for [Windows Update install error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/) covers the shared update components involved here.

### Fix 3: Re-register the Store with PowerShell

When the Store's system registration is damaged, re-registering the package fixes it.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Paste this command and press Enter:
   `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to complete — red text warnings during the process are usually harmless.
4. Restart the laptop and open the Store.

### Fix 4: Restart the Store and licensing services

Two background services commonly get stuck after updates.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Microsoft Store Install Service** — double-click it, set **Startup type** to **Manual**, click **Start** if it is stopped, then **OK**.
3. Find **Client License Service (ClipSVC)** — right-click it and choose **Restart**.
4. Also restart **Windows Update** and **Background Intelligent Transfer Service (BITS)** the same way.
5. Open the Store and test a download.

### Fix 5: Run the Store troubleshooter and check date/time

Two quick checks that resolve the "silly but real" causes.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Store Apps**. Apply any fix it suggests.
2. Then go to **Settings > Time & language > Date & time** — turn on **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. If your region changed during the update, check **Settings > Time & language > Language & region** and set the correct country.
4. Open the Store again — certificate errors caused by clock drift disappear immediately once time syncs.

### Fix 6: Repair Windows system files and update components

If the Store still misbehaves, the damage is deeper in Windows itself.

1. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Run `sfc /scannow` and let it finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart, then go to **Settings > System > Recovery** and use **Fix problems using Windows Update** (the cloud repair option) — it reinstalls core Windows components without touching your files.
5. Detailed steps for stubborn update-component damage are in Microsoft's own [Windows support documentation](https://support.microsoft.com/en-us/windows).

### Fix 7: Clear the SoftwareDistribution folder

A corrupted update download cache poisons both Windows Update and Store downloads.

1. Open **Terminal (Admin)** and stop the update services:
   `net stop wuauserv`
   `net stop bits`
2. Press **Win + R**, type `C:\Windows\SoftwareDistribution`, press Enter, and delete everything inside the **Download** folder (leave the folder itself).
3. Back in the terminal, restart the services:
   `net start wuauserv`
   `net start bits`
4. Open the Store and retry your download. For general blue-screen-style system instability after updates, our [blue screen fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) is a useful companion read.

## Closing

Microsoft Store failures after a Windows 11 update feel like the Store is broken, but nine times out of ten it is the update that left the Store's cache, registration, or background services in a bad state. The wsreset cache clear plus a Settings-level reset resolves most cases in minutes; the PowerShell re-registration and service restarts handle the stubborn ones. Work the list in order, and you will have downloads flowing again without ever needing to reinstall Windows.
