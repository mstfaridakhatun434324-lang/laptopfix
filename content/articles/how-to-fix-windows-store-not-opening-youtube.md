---
title: "How to Fix the Microsoft Store When It Won't Open"
slug: how-to-fix-windows-store-not-opening-youtube
date: 2026-09-18
categories: ["windows-errors"]
tags: ["microsoft store", "apps", "windows 11"]
description: "Microsoft Store won't launch, crashes instantly, or hangs on the logo? These repairs get it opening and downloading again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-youtube.webp"
faqs:
  - q: "Why won't the Microsoft Store open at all?"
    a: "Usually a corrupt Store app cache, a broken app package registration, incorrect date/time settings (which break Store authentication), or a stalled update service. The wsreset.exe cache clear fixes the most common case in under a minute."
  - q: "Will resetting the Store delete my installed apps?"
    a: "No. Resetting or repairing the Microsoft Store app only affects the Store itself — your installed apps, games, and purchases tied to your Microsoft account are untouched. You may need to sign back into the Store afterward."
  - q: "What does wsreset.exe do?"
    a: "It clears the Microsoft Store's cache and re-registers the app without changing your account or installed apps. A blank Command Prompt window opens for 10-30 seconds, then the Store launches fresh. It is the fastest first-line fix."
  - q: "Can antivirus block the Microsoft Store?"
    a: "Yes — overzealous third-party firewalls and antivirus suites sometimes block the Store's network access or its background services. If the Store opens but cannot download, temporarily disabling third-party security software is a worthwhile test."
---
You click the Microsoft Store icon and... nothing. Or it flashes open and vanishes. Or it sits on its logo forever. The Store breaking is annoying because it also breaks app updates for everything installed through it — so a dead Store slowly rots your whole app library.

The causes are almost always local: a corrupt cache, a broken registration, wrong system time, or a stalled service. The fixes below are ordered from the 30-second cache clear to deeper repairs.

## Why this happens

- **Corrupt Store cache:** Damaged temporary data preventing launch — the most common cause.
- **Broken app package registration:** The Store's registration with Windows damaged by updates or "debloating" tools.
- **Wrong date, time, or region:** The Store authenticates with Microsoft servers; clock skew breaks the handshake.
- **Stalled Windows Update / BITS services:** The Store depends on the same download infrastructure as Windows Update.
- **Corrupt user profile Store data:** Per-user Store state damaged for one account.
- **Third-party firewall/antivirus blocking:** Security software cutting off the Store's network access.
- **Proxy or VPN interference:** Network configurations that break Microsoft's content delivery endpoints.
- **Metered connection restrictions:** A connection marked as metered can pause Store downloads indefinitely without an obvious error.

## How to fix it

Work through these in order, testing the Store after each.

### Fix 1: Clear the Store cache with wsreset

The fastest fix and the right first step.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter**.
2. A blank Command Prompt window opens for 10-30 seconds — do not close it. When it finishes, the Microsoft Store launches automatically.
3. If the Store now opens, sign in and check for app updates. If wsreset errors out or changes nothing, continue.

### Fix 2: Check date, time, and region

Wrong clock settings silently break Store authentication. This sounds too simple to matter, but the Store's sign-in tokens are time-sensitive — even a few minutes of skew against Microsoft's servers causes authentication to fail with no useful error message. It commonly happens after a CMOS battery dies, after traveling across time zones with manual time set, or after a botched update resets the clock.

1. Go to **Settings > Time & language > Date & time** and turn on **Set time automatically** and **Set time zone automatically**. Click **Sync now**.
2. Go to **Settings > Time & language > Language & region** and confirm your region is correct.
3. Retry the Store. This fixes a surprising number of "Store won't connect" cases.

### Fix 3: Repair and reset the Store app

Windows can repair the Store's installation in place.

1. Go to **Settings > Apps > Installed apps**, find **Microsoft Store**, click the **...** menu, and choose **Advanced options**.
2. Click **Repair** first and test. If it still fails, click **Reset** — this clears the Store's data without affecting your installed apps or purchases.
3. Reopen the Store and sign back in if prompted.

### Fix 4: Re-register the Store package with PowerShell

If the app package itself is broken, re-register it. You will know this is the right fix when wsreset and the Settings repair both fail silently — the app launches and dies, or never appears at all. Re-registration rebuilds the manifest binding without touching your installed apps, purchases, or sign-in state.

1. Open **Windows PowerShell as administrator** (right-click Start > **Terminal (Admin)**).
2. Run: `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Reboot and test. This reinstalls the Store's registration for all users without touching your data.

### Fix 5: Restart the required services

The Store depends on the same download infrastructure as Windows Update. If BITS or the update service is broken, the Store cannot fetch anything — and fixing those services often repairs both at once. This is also why a Store that opens but never finishes downloads almost always traces back here rather than to the Store app itself.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Restart these services, setting each **Startup type** to **Automatic** (or **Manual** where Automatic is not offered): **Windows Update**, **Background Intelligent Transfer Service**, and **Microsoft Store Install Service**.
3. Retry the Store. If you use a third-party firewall, temporarily disable it and test — then add an exception for the Store rather than leaving protection off.

### Fix 6: Run the Store troubleshooter and check for Windows updates

Let Windows diagnose itself, and make sure the OS is current.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
2. Then go to **Settings > Windows Update** and install all pending updates — Microsoft regularly ships Store fixes in cumulative updates. Check [Microsoft Support](https://support.microsoft.com/en-us/windows) for any documented Store outages before assuming the problem is local.

### Fix 7: Repair system files

Deep corruption affecting the Store's dependencies.

1. Open an elevated Command Prompt: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
2. Reboot and test. If the Store broke right after a feature update, this step repairs the components the update damaged.

### Fix 8: Test a new user profile

If the Store works in a fresh account, your profile's Store data is corrupt.

1. Go to **Settings > Accounts > Other users > Add account** and create a local account.
2. Sign in and open the Store. If it works, the corruption is per-user — migrate to the new profile or, less drastically, sign out of the Store in the old profile, clear `%LocalAppData%\Packages\Microsoft.WindowsStore_*`, and sign back in.
3. For related app-platform issues, our [Windows Search repair guide](/articles/how-to-fix-windows-search-not-working-reddit/) covers similar package-repair techniques for other built-in apps.

## Closing

A dead Microsoft Store is almost always a cache, registration, clock, or service problem — all fixable without reinstalling Windows. Run wsreset, verify your time settings, repair the app, re-register the package, and the Store comes back to life along with your app updates. For Store error codes rather than launch failures, our [Microsoft Store error guide](/articles/how-to-fix-microsoft-store-error-in-windows-11-24h2/) covers the coded-error side of Store troubleshooting.
