---
title: "Microsoft Store Won't Open? A Step-by-Step Repair Guide"
slug: how-to-fix-windows-store-not-opening-step-by-step
date: 2026-09-17
categories: ["windows-errors"]
tags: ["microsoft store", "windows 11", "app repair"]
description: "Clicking the Microsoft Store and nothing happens? Follow this step-by-step guide to reset, repair, and reinstall the Store until it opens again."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-step-by-step.webp"
faqs:
  - q: "Why won't the Microsoft Store open when I click it?"
    a: "Usually its app package registration is broken, the cache is corrupt, or a background update left it in a bad state. Failed Windows updates and interrupted app updates are the most common triggers. The fixes below repair the registration without touching your installed apps."
  - q: "Is it safe to reinstall the Microsoft Store with PowerShell?"
    a: "Yes. Removing and re-registering the Store package only affects the Store app itself. Your installed apps, purchase history, and Microsoft account stay intact. It's one of the safest deep repairs you can do on Windows."
  - q: "The Store opens but closes instantly. Which fix helps?"
    a: "Start with wsreset.exe, then use Settings > Apps > Installed apps > Microsoft Store > Advanced options > Repair. An instant-close usually means the package's activation data is corrupt, and the Repair button rebuilds exactly that."
  - q: "How do I prevent the Store from breaking again?"
    a: "Let Windows Update run to completion, don't force-shutdown during app updates, and keep the Store's own updates enabled in Library > Get updates. Running wsreset occasionally after major Windows updates also keeps the cache healthy."
---
You click the Microsoft Store icon and... nothing. Or a window flashes for a split second and vanishes. Everything else on the laptop works fine, which makes it extra annoying. This is a launch problem, distinct from the [Store opening but showing error codes](/articles/how-to-fix-microsoft-store-error-on-lenovo-laptop/) — here the app itself can't even start.

The causes are almost always the same handful of issues: a corrupt cache, a broken app registration, or damaged system files. Work through the steps in order, testing the Store after each one.

## Why this happens

- **Corrupted Store cache.** Stale temporary files can prevent the app from initializing.
- **Broken app package registration.** Windows "forgets" how to launch the Store after a bad update.
- **Corrupted system files.** Damage to shared UWP framework files stops all Store apps from launching.
- **Interrupted app update.** A Store self-update that got cut off leaves the package half-installed.
- **User profile corruption.** The Store's per-user activation data can break while other apps still work.
- **Conflicting third-party software.** Aggressive "debloater" tools and some antivirus products disable Store components.
- **Disabled background services.** The Store needs services like **Background Intelligent Transfer** and **Windows Update** running.

## How to fix it

Work through these in order — each step is a little deeper than the last.

### Fix 1: Reset the Store cache

The fastest fix and worth trying first, even for launch failures.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter**.
2. A blank command window appears. Wait — don't close it.
3. When it closes on its own, the Store should attempt to launch.
4. If the Store opens now, you're done. If not, restart the laptop and try `wsreset.exe` once more.
5. After a restart, also try launching the Store from **Start > All apps** instead of the taskbar pin — the pin itself can occasionally be the broken part.
6. If it still won't launch, move on to Fix 2.

### Fix 2: Repair the Store through Settings

Windows can repair the Store's package without data loss.

1. Open **Settings > Apps > Installed apps**.
2. Find **Microsoft Store** in the list (use the search box at the top).
3. Click the three dots next to it and choose **Advanced options**.
4. Under the Reset section, click **Repair** and wait for the checkmark.
5. Try launching the Store.
6. If it still fails, return to the same page and click **Terminate** first, then **Repair** again — terminating kills any hung Store processes holding files open.

### Fix 3: Run the Windows Store Apps troubleshooter

The built-in troubleshooter checks the common breakages automatically.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Store Apps**.
3. Apply every fix it offers, even if the description sounds unrelated.
4. Restart your laptop when it completes.
5. Microsoft keeps the troubleshooter definitions updated through [support.microsoft.com](https://support.microsoft.com/en-us/windows), so make sure Windows Update has run recently for the latest version.
6. Test the Store launch after the reboot.

### Fix 4: Reset the Store app completely

One level deeper than Repair — this clears all the Store's local data.

1. Return to **Settings > Apps > Installed apps > Microsoft Store > Advanced options**.
2. Click **Reset** and confirm the prompt.
3. Wait for the checkmark, then launch the Store from the **Start menu**.
4. Sign in again when prompted — Reset clears the saved session.
5. Go to **Library** and click **Get updates** to refresh the Store's own components.
6. Try opening a few app pages to confirm browsing and installing both work.

### Fix 5: Re-register the Store with PowerShell

This rebuilds the launch registration that Windows uses to start the app.

1. Right-click the **Start** button and select **Terminal (Admin)**.
2. Paste this command and press **Enter**:
   `Get-AppxPackage -AllUsers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to finish — ignore any red text that appears; it's normal.
4. Close the terminal and launch the Store from **Start > All apps**.
5. If the package files themselves are damaged, the command will fail. In that case, run `wsreset -i` from an elevated terminal to reinstall the Store from scratch.
6. Restart and verify the Store opens reliably, not just once.

### Fix 6: Check the services the Store depends on

If background services are disabled, the Store may refuse to start.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Background Intelligent Transfer Service** — set its Startup type to **Automatic** and start it.
3. Find **Windows Update** and do the same.
4. Find **Microsoft Store Install Service** — set it to **Manual** and start it.
5. Also verify **AppX Deployment Service (AppXSVC)** is running.
6. Restart the laptop and try the Store again. If a "tweaking" utility keeps disabling these, uninstall it.

### Fix 7: Create a new user profile to test

This isolates profile corruption from system-wide damage.

1. Open **Settings > Accounts > Other users** and click **Add account**.
2. Choose **I don't have this person's sign-in information**, then **Add a user without a Microsoft account**.
3. Make it an administrator via **Change account type**.
4. Sign out and sign into the new account.
5. Try launching the Store there. If it opens, your old profile's app data is corrupt — migrate your files to the new profile.
6. If the Store won't open on a fresh profile either, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal, then try the [full blue-screen-class repair path](/articles/how-to-fix-blue-screen-of-death-windows-11/) only if other system apps are broken too.

## Closing

A Store that won't open is nearly always a registration or cache problem, and the ladder above fixes it without reinstalling Windows. The PowerShell re-registration at Fix 5 is the heavy hitter — it resolves the stubborn cases that cache resets can't touch. Once it's working, keep the Store updated from its own Library page and avoid "debloating" scripts that strip Store components, and it should stay healthy.
