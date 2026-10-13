---
title: "Microsoft Store Won't Open? Here's How to Fix It"
slug: how-to-fix-windows-store-not-opening-reddit
date: 2026-09-25
categories: ["windows-errors"]
tags: ["microsoft store", "store not opening", "wsreset", "appx", "windows 11"]
description: "Microsoft Store won't open or crashes instantly? Fix it in 8 steps — cache resets, re-registration, and the deeper AppX repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-store-not-opening-reddit.webp"
faqs:
  - q: "Why won't the Microsoft Store open?"
    a: "The usual causes are a corrupted Store cache, damaged AppX package registration, broken system files the Store depends on, or account sync issues. The Store is more fragile than regular apps because it depends on several background services all working correctly."
  - q: "Does wsreset.exe delete my apps?"
    a: "No. wsreset.exe only clears the Store's temporary cache — your installed apps, purchases, and account stay untouched. It's the safest first fix and resolves a large share of Store problems."
  - q: "The Store opens then immediately closes — what's wrong?"
    a: "That's typically a corrupted AppX registration or a damaged user profile component. Re-registering the Store package with PowerShell (Fix 4) fixes most instant-crash cases. If it affects all Store apps, not just the Store itself, suspect system-file corruption."
  - q: "Could my antivirus block the Microsoft Store?"
    a: "Yes — overzealous third-party security suites sometimes block Store processes or its network access. If the Store broke right after installing security software, temporarily disable it to test. Windows Defender doesn't cause this problem."
---

The Microsoft Store refusing to open — bouncing, flashing, or crashing instantly — is one of Windows' more irritating failure modes, because you need the Store to update the very apps that might fix things. It's especially confusing because the Store looks like a simple app but behaves like a system component, with background services, licenses, and account tokens all needing to line up before the window even appears.

Fortunately, the repair ladder is well understood: cache, re-registration, services, system files, account state, and finally the nuclear options. Start at the top; most people are fixed by Fix 3.

## Why this happens

- **Corrupted Store cache.** The most common cause — stale or damaged cache files prevent launch.
- **Broken AppX package registration.** The Store's registration with Windows is damaged, so the system can't start it.
- **Disabled background services.** The Store depends on services like AppX Deployment Service; if they're disabled, it can't run.
- **Corrupted system files.** Damage to shared components the Store relies on.
- **Account or licensing sync issues.** Microsoft account problems can block Store initialization.
- **Third-party interference.** Antivirus, debloat scripts, or "privacy" tools that removed Store dependencies.
- **Corrupted Microsoft account token cache.** Stale authentication tokens can prevent the Store from initializing even when the app itself is healthy.

## How to fix it

Work through these in order — start with Fix 1 and stop when the Store opens.

### Fix 1: Run wsreset.exe

The classic first fix — clears the cache safely.

1. Press **Windows + R**, type `wsreset.exe`, and press Enter.
2. A blank command window appears for 10–30 seconds — don't close it.
3. The Store should launch automatically when the reset completes.
4. Try browsing or updating an app to confirm it's healthy.
5. If the window closes but the Store still won't open, continue to Fix 2.

### Fix 2: Check date, time, and network basics

The Store is picky about these.

1. Right-click the clock and open **Adjust date and time** — enable **Set time automatically**; certificate validation fails with wrong time.
2. Confirm your internet works in a browser — the Store needs connectivity to initialize.
3. If you're on VPN or proxy, disconnect temporarily and retry.
4. Flush DNS: run `ipconfig /flushdns` in **Terminal**.
5. Retry the Store. For the post-update variant of Store failures, see [Windows Store not opening after a Windows 11 update](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/). If the Store opens but downloads fail with error codes, our [Microsoft Store error after Windows 11 update guide](/articles/how-to-fix-microsoft-store-error-after-windows-11-update/) covers those.

### Fix 3: Repair and reset the Store app

Use Windows' built-in app repair.

1. Go to **Settings > Apps > Installed apps**, find **Microsoft Store**.
2. Click the three dots > **Advanced options**.
3. Click **Repair** first and test the Store.
4. If repair doesn't help, click **Reset** (this clears app data but keeps the app installed).
5. Test again. Reset is stronger than wsreset and fixes registration-adjacent issues.

### Fix 4: Re-register the Store with PowerShell

Rebuild the Store's registration from scratch.

1. Open **Terminal (Admin)**.
2. Run:
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for completion — red "in use" errors are usually harmless.
4. Restart the laptop.
5. Launch the Store. This fixes most instant-crash cases.

### Fix 5: Check the services the Store depends on

Make sure nothing critical is disabled.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **AppX Deployment Service (AppXSVC)** — set it to **Manual** (not Disabled).
3. Check **Client License Service (ClipSVC)** and **Microsoft Store Install Service** similarly.
4. If you ran a "debloat" script, it may have disabled these — re-enable them.
5. Restart and test the Store.

### Fix 6: Run the Store Apps troubleshooter and SFC

Let Windows diagnose itself.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Store Apps**.
2. Apply any fixes it suggests and test.
3. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
4. Restart after both complete.
5. If the troubleshooter found nothing and SFC was clean, the issue is likely account-related — continue below.

### Fix 7: Sign out and back into your Microsoft account

Fix licensing and sync issues.

1. Open the **Store** (if it opens at all) — or go to **Settings > Accounts**.
2. Sign out of your Microsoft account in the Store's profile menu, then sign back in.
3. Alternatively, switch your Windows account to a local account and back (**Settings > Accounts > Your info**).
4. As a test, create a new local user account (**Settings > Accounts > Other users**) and try the Store there — if it works, your main profile is corrupted.
5. For a corrupted profile, migrate to the new account rather than fighting it.

### Fix 8: Reinstall the Store and refresh Windows

The final options.

1. In **Terminal (Admin)**, fully remove and reinstall:
   `Get-AppxPackage *WindowsStore* -AllUsers | Remove-AppxPackage`
   then reinstall via the re-registration command from Fix 4 (or from the Store's offline package).
2. If that fails, **Settings > System > Recovery > Reset PC** with **Keep my files** refreshes all AppX components.
3. Never run debloat scripts that remove the Store afterward — they cause exactly this problem.
4. After reset, update the Store itself first via its **Library** page.
5. Microsoft's [Store support pages](https://support.microsoft.com/en-us/windows) cover account-specific edge cases.

## Closing

A Store that won't open is almost always cache, registration, or a disabled service — the first five fixes cover it. The key insight is that the Store isn't a normal app; it's a system component with dependencies, so "reinstall the app" thinking doesn't apply until you've worked the dependency chain. When account tokens are the issue, signing out and back in does more than any repair command. And once it's healthy, leave the debloat scripts alone — they're the number-one cause of repeat Store breakage, and no script's promised performance gain is worth breaking app updates. If the Store breaks again right after a specific change — a new antivirus, a debloat script, a major update — that change is your prime suspect, and System Restore is faster than reworking the whole ladder.
