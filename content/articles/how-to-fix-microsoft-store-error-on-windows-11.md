---
title: "How to Fix Microsoft Store Errors on Windows 11"
slug: how-to-fix-microsoft-store-error-on-windows-11
date: 2026-09-08
categories: ["windows-errors"]
tags: ["microsoft store", "windows 11", "app errors"]
description: "Microsoft Store not working on Windows 11? Error codes, blank pages, stuck downloads — here's the complete fix sequence from wsreset to reinstallation."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-windows-11.webp"
faqs:
  - q: "Why is the Microsoft Store not working on Windows 11?"
    a: "The most common causes are a corrupted Store cache, incorrect date/time settings (which break the Store's secure connections), a damaged app package after a Windows update, or sign-in/account issues. The Store depends on several background services, so a failure in any of them surfaces as a Store error."
  - q: "What does wsreset.exe do?"
    a: "It clears the Microsoft Store's cache without changing your account settings or installed apps. It's the safest first fix for most Store problems — blank pages, error codes on launch, and stuck downloads. Run it by typing wsreset.exe in the Run dialog; the Store opens automatically when it finishes."
  - q: "Will resetting the Microsoft Store delete my installed apps?"
    a: "No. Using Settings > Apps > Microsoft Store > Reset clears the Store app's own data and signs you out, but your installed apps and games stay put. You'll just need to sign back into the Store afterward."
  - q: "What if the Microsoft Store is completely missing?"
    a: "If the Store app itself vanished (usually after a debloat script or failed update), you can reinstall it with a PowerShell command that re-registers the built-in package. As a last resort, an in-place Windows upgrade reinstalls all inbox apps including the Store."
---
The Microsoft Store on Windows 11 fails in creative ways: cryptic error codes (0x80072EE7, 0x80131500), endless loading spinners, downloads stuck at 0%, or the app refusing to open at all. Beneath the variety, the causes are a short list — corrupted cache, bad system time, damaged app packages, or account glitches — and the fixes below handle all of them.

Work through these in order, from the 30-second cache clear to full reinstallation. If the Store won't open on a specific brand, our [Store not opening on ASUS guide](/articles/how-to-fix-windows-store-not-opening-on-asus-laptop/) has model-specific notes. Store failures that come with access-denied style error codes may also relate to [error 0x80070005](/articles/how-to-fix-error-0x80070005-in-windows-11-24h2/), which covers permission-related update and Store failures.

## Why this happens

- **Corrupted Store cache:** Stale or damaged cached data breaking page loads and downloads.
- **Wrong date/time:** The Store's HTTPS connections fail certificate checks when your clock is off.
- **Damaged app package:** A Windows update corrupting the Store's own files.
- **Microsoft account sign-in issues:** Token or profile glitches blocking the Store backend.
- **Disabled background services:** The Store needs Background Intelligent Transfer and related services running.
- **Corrupted system files:** Broader Windows damage manifesting in Store failures.
- **VPN/proxy interference:** Network middleboxes breaking the Store's connections.
- **Corrupted user profile Store data:** Per-user Store caches that survive app resets and only clear with a profile-level fix.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the Store works.

### Fix 1: Clear the Store cache with wsreset.exe

The fastest fix — resolves a huge share of Store errors in under a minute.

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window appears for 10–30 seconds — don't close it.
3. The Microsoft Store opens automatically when the reset finishes.
4. Try your download or page again. If it works, you're done.

### Fix 2: Check date, time, and region

Wrong clocks silently break the Store's secure connections.

1. Right-click the taskbar clock > **Adjust date and time**.
2. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Open **Settings** > **Time & language** > **Language & region** and confirm your **Country or region** is correct — mismatched regions cause licensing and availability errors.
4. Restart the Store and retry.

### Fix 3: Repair and reset the Store app

Deeper than wsreset — repairs the app package itself.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Find **Microsoft Store**, click the **...** menu > **Advanced options**.
3. Click **Repair** first and test the Store.
4. If it still fails, click **Reset** (you'll be signed out; your installed apps are unaffected).
5. After resetting, restart the laptop before opening the Store — this ensures the reset fully applies.
6. Open the Store, sign back in, and retry.

### Fix 4: Run the Store Apps troubleshooter

Automated diagnosis for app-platform issues.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Windows Store Apps**.
3. Apply its recommendations and restart the Store.
4. If the troubleshooter is missing on your build, skip to Fix 5 — Microsoft has folded some troubleshooters into the Get Help app.

### Fix 5: Check required background services

The Store depends on services that "optimizers" love to disable.

1. Press **Win + R**, type `services.msc`, press Enter.
2. Find **Background Intelligent Transfer Service** — set **Startup type** to **Automatic** (or **Manual**) and **Start** it.
3. Do the same for **Windows Update** and **Microsoft Store Install Service** (if present).
4. Restart the laptop and test the Store.

### Fix 6: Re-register the Store with PowerShell

Reinstalls the Store's registration without touching your data.

1. Open **PowerShell as administrator**: **Win + S**, type `powershell`, right-click > **Run as administrator**.
2. Run:
   `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete (ignore red errors for other packages if you ran the broader version).
4. If the Store package itself is missing from the list (deleted by a debloat script), the targeted command can't find it — in that case run the broader re-registration for all inbox apps, or use the in-place upgrade in Fix 7.
5. Restart and open the Store.

### Fix 7: Repair system files and check your account

Covers the remaining systemic causes.

1. Open an **administrator Command Prompt**: run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Sign out of the Store (**profile icon** > **Sign out**), restart, and sign back in — this refreshes stale auth tokens.
3. Temporarily disable any VPN or proxy, then retry — if the Store works, add an exception or adjust the VPN's settings.
4. As a test, try the Store in a new local user account; if it works there, your main profile's Store data is corrupt (Fix 3's Reset usually resolves it). To create one quickly: **Settings** > **Accounts** > **Other users** > **Add account** > **I don't have this person's sign-in information** > **Add a user without a Microsoft account**.
5. For persistent corruption, an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (keep files and apps) reinstalls all inbox apps cleanly.

## Closing

Microsoft Store errors look varied but yield to a short, ordered routine: clear the cache with wsreset, fix the clock, repair or reset the app, and re-register it if needed. Most people never get past Fix 3. The two preventive habits that matter: keep your date/time on automatic sync, and don't run "debloat" scripts that rip out Store components — they're the top cause of Stores that vanish entirely. And if downloads specifically stall while browsing works, check your VPN and the Background Intelligent Transfer Service before anything else. Store problems are rarely urgent, but they're worth fixing promptly: an unhealthy Store often signals broader app-platform issues that affect other inbox apps too. Work the list top to bottom and stop at the first fix that holds — most Store issues surrender to the cache clear or the clock check. For general Windows guidance, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the current Store error codes.
