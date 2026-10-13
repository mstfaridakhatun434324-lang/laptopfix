---
title: "Microsoft Store Errors on a Lenovo Laptop? Fix It Fast"
slug: how-to-fix-microsoft-store-error-on-lenovo-laptop
date: 2026-09-15
categories: ["windows-errors"]
tags: ["microsoft store", "lenovo", "windows 11"]
description: "Microsoft Store throwing error codes on your Lenovo laptop? These step-by-step fixes reset the cache, repair the app, and get downloads working again."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-lenovo-laptop.webp"
faqs:
  - q: "Why does Microsoft Store show an error code on my Lenovo laptop?"
    a: "The most common causes are a corrupted Store cache, wrong date/time settings, pending Windows updates, or a broken Microsoft account sign-in. Lenovo preloads like Lenovo Vantage rarely cause it directly, but outdated Lenovo drivers can contribute when downloads stall."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Resetting (wsreset.exe) only clears the Store's temporary cache files. Your installed apps and purchase history stay intact because they're tied to your Microsoft account, not the local cache."
  - q: "Store says I'm offline but my Wi-Fi works. What should I check?"
    a: "First verify your date and time are set automatically in Settings > Time & language. Then run the Network troubleshooter. If specific error codes like 0x80072EFD appear, resetting the Store cache and re-signing into your Microsoft account usually resolves it."
  - q: "Can I reinstall the Microsoft Store completely?"
    a: "Yes — uninstalling and reinstalling via PowerShell (covered in Fix 6) gives you a completely fresh Store package. This is safe and doesn't affect other apps. It's the deepest repair short of reinstalling Windows itself."
---
You open the Microsoft Store on your Lenovo laptop to grab an app or an update, and instead of a download you get a cryptic error code — 0x80072EFD, 0x803F8001, or just a blank page that never loads. Frustrating, but almost always fixable. The Store is a sandboxed UWP app, and when its cache or licensing gets tangled, it fails loudly.

These fixes are ordered from quickest to deepest. If the [Store won't open at all on your machine](/articles/how-to-fix-windows-store-not-opening-step-by-step/), you'll want that companion guide too — it covers the no-launch scenario specifically.

## Why this happens

- **Corrupted Store cache.** Temporary download data gets stuck and blocks every new request.
- **Incorrect date and time.** Store licensing is time-sensitive; a clock that's off by even a few minutes breaks certificate checks.
- **Broken Microsoft account sign-in.** A stale token or password change can silently invalidate Store sessions.
- **Pending Windows updates.** The Store depends on shared system components that may be waiting on an update.
- **Corrupted app package.** The Store's own files can get damaged by a bad update or disk errors.
- **VPN, proxy, or DNS interference.** Network filters can block Store endpoints while regular browsing still works.
- **Third-party antivirus blocking Store traffic.** Some security suites flag the Store's background downloads.

## How to fix it

Work through these in order — stop when the Store works.

### Fix 1: Reset the Store cache with wsreset

This is the classic one-minute fix and it resolves a surprising number of Store errors.

1. Press **Win + R** to open the Run dialog.
2. Type `wsreset.exe` and press **Enter**.
3. A blank Command Prompt window appears for a few seconds — don't close it; let it finish.
4. The Store should launch on its own when the reset completes.
5. Try your download again.
6. If nothing happens, restart the laptop and run `wsreset.exe` once more.

### Fix 2: Check date, time, and region

A wrong clock is one of the sneakiest Store killers.

1. Open **Settings > Time & language > Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** under Additional settings.
4. Go back to **Time & language > Language & region** and confirm your **Country or region** is correct.
5. Restart the Microsoft Store and try downloading again.
6. If errors persist, compare your clock with an online time source — a CMOS battery issue on older laptops can keep resetting the clock.

### Fix 3: Run the Windows Store Apps troubleshooter

Windows has a built-in troubleshooter just for this.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Windows Store Apps** and click **Run**.
3. Follow the on-screen prompts and apply any fixes it suggests.
4. Restart your laptop when it finishes.
5. While you're in Troubleshoot, also run the **Network and Internet** troubleshooter if downloads stall rather than error out.
6. Open the Store and test a small free app download to confirm it's fixed.

### Fix 4: Repair or reset the Store app

A deeper repair than the cache reset — this fixes the app package itself.

1. Open **Settings > Apps > Installed apps**.
2. Scroll to **Microsoft Store** and click the three dots, then **Advanced options**.
3. Click **Repair** and wait for the checkmark. Try the Store now.
4. If the error remains, go back and click **Reset**. Confirm when prompted.
5. Note that Reset clears the app's data but keeps your installed apps and purchases.
6. Launch the Store from the **Start menu** and sign in again if asked.

### Fix 5: Re-sign into your Microsoft account and check for updates

Stale credentials cause a whole family of Store errors.

1. Open the Store, click your **profile icon** in the top bar, and choose **Sign out**.
2. Open **Settings > Windows Update** and install every pending update, including optional ones. Microsoft documents the current release health on [support.microsoft.com](https://support.microsoft.com/en-us/windows), which helps if you suspect a known bad patch.
3. Restart the laptop — Lenovo's [support site](https://support.lenovo.com/us/en/) also lists driver updates for your exact model, worth grabbing while you're at it.
4. Sign back into the Store with your Microsoft account.
5. Go to **Library** in the Store and click **Get updates** to refresh all apps.
6. Test the original download that was failing.

### Fix 6: Reinstall the Microsoft Store with PowerShell

The nuclear option for the Store itself — a completely fresh package.

1. Right-click the **Start** button and choose **Terminal (Admin)**.
2. Uninstall the Store package:
   `Get-AppxPackage -allusers *WindowsStore* | Remove-AppxPackage`
3. Reinstall it for all users:
   `Get-AppxPackage -allusers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
4. If the reinstall command can't find the package files, run this instead to pull a fresh copy:
   `wsreset -i`
5. Restart the laptop.
6. Open the Store — it should behave like a brand-new install. Sign in and retry your download.

### Fix 7: Disable VPN/proxy and flush DNS

If the Store errors mention connectivity (0x80072EFD, 0x80131500), the network path is the problem.

1. Open **Settings > Network & internet > VPN** and disconnect any active VPN.
2. Go to **Settings > Network & internet > Proxy** and turn off **Use a proxy server**.
3. Open Command Prompt as administrator: right-click **Start**, choose **Terminal (Admin)**.
4. Flush the DNS cache:
   `ipconfig /flushdns`
5. Reset the network stack:
   `netsh winsock reset`
6. Restart the laptop and try the Store again with no VPN active.

## Closing

Microsoft Store errors on a Lenovo laptop look alarming but follow a predictable pattern: cache, clock, credentials, updates, network. Work through the fixes in order and you'll almost always land the solution at Fix 1 or Fix 4. Keep Windows and your Lenovo drivers current, and the Store tends to stay out of trouble. If errors return repeatedly with the same code, note the exact code and screenshot the message — it makes diagnosing the next occurrence much faster, and it gives any support technician a concrete starting point instead of a vague description. If the error code looks update-related rather than Store-specific, our [0x80070057 repair guide](/articles/error-code-0x80070057-fix/) covers the most common one.
