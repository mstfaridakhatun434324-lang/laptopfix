---
title: "How to Fix Microsoft Store Errors on an Acer Laptop"
slug: how-to-fix-microsoft-store-error-on-acer-laptop
date: 2026-09-15
categories: ["windows-errors"]
tags: ["microsoft store", "app errors", "acer laptop", "windows 11"]
description: "Fix Microsoft Store errors on your Acer laptop — reset the Store cache, repair the app package, check services, and resolve 0x80070005 and similar codes."
thumbnail: "/images/thumbs/how-to-fix-microsoft-store-error-on-acer-laptop.webp"
faqs:
  - q: "Why does the Microsoft Store keep showing error codes on my Acer?"
    a: "The Store depends on a chain of background services, a local cache, and your Microsoft account sign-in. If any link breaks — corrupted cache after an update, a stopped service, or a region mismatch — you get an error code. Resetting the cache fixes the most common cases in under a minute."
  - q: "What does error 0x80070005 mean in the Microsoft Store?"
    a: "Access denied — the Store cannot read or write something it needs, usually its own cache or a license file. Running wsreset.exe and then repairing the Store app package through Settings resolves it. Our dedicated [0x80070005 guide](/articles/how-to-fix-error-0x80070005-in-windows-11-24h2/) covers the deeper system-level version."
  - q: "Can I reinstall the Microsoft Store if nothing works?"
    a: "Yes. You can re-register it with a PowerShell command (Fix 5 below), which effectively reinstalls it without touching your installed apps or purchases. Your app licenses are tied to your Microsoft account, not the local Store installation."
  - q: "Do Acer's preinstalled apps interfere with the Store?"
    a: "Rarely, but Acer Care Center and some preinstalled utilities can delay Store updates at first boot. The bigger factor is usually just Windows itself — the Store is finicky on every brand."
---

The Microsoft Store failing with a cryptic error code — 0x80070005, 0x80131500, 0x80072EE7, take your pick — is a special kind of annoying because the Store is supposed to just work. On Acer laptops there is nothing particularly Acer-specific about these failures; the Store breaks the same way on every brand. But since you are here with an Acer, this guide is written with your machine in mind, including where Acer's own tools fit in.

The fixes go from instant (clear the cache) to thorough (re-register the whole Store). If the Store will not even open at all, you may also want our guide on [Windows Store not opening](/articles/windows-store-not-opening-blue-screen-error-fix/) — different symptom, overlapping fixes.

A quick note on what the Store actually is, because it explains why these fixes work: the Microsoft Store is a UWP packaged app that depends on a local cache, several background services, and your account's license tokens. When people say "the Store is broken," they almost always mean one of those three supports failed — not the Store's code itself. That is why the repair sequence is cache first, services second, app package third. You are rebuilding the supports in order, and each step eliminates a whole category of causes before you move to the next.

## Why this happens

- **Corrupted Store cache.** The number one cause. The cache in `LocalCache` gets damaged by interrupted updates or disk errors, and every Store operation fails until it is cleared.
- **Wrong date, time, or region.** The Store validates licenses against Microsoft's servers; if your clock is off by even a few minutes, authentication fails with misleading error codes.
- **Stopped background services.** The Store needs Background Intelligent Transfer Service, Windows Update, and the Microsoft Store Install Service running.
- **Microsoft account sign-in glitch.** A stale or half-signed-in account state breaks license checks for your apps.
- **Corrupted Store app package.** A failed Windows update can damage the Store's own installation.
- **Proxy or VPN interference.** Corporate proxies and some VPNs break the Store's connection to Microsoft's servers while the browser works fine.

## How to fix it

Work through these in order — Fix 1 takes 30 seconds and works surprisingly often.

### Fix 1: Reset the Store cache with wsreset

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. A blank Command Prompt window opens for 10–30 seconds, then the Store launches automatically. That is the cache being cleared and rebuilt.
3. Try your download or update again. If the error persists, move on — but do not skip this step, because later fixes build on a clean cache.

### Fix 2: Check date, time, and region

1. Go to **Settings > Time & language > Date & time**.
2. Turn on **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Go to **Settings > Time & language > Language & region** and confirm **Country or region** matches where you actually are.
4. Restart the Store and retry. This fixes a shocking number of 0x80072EE7 and license errors.

### Fix 3: Repair and reset the Store app

1. Go to **Settings > Apps > Installed apps**, find **Microsoft Store**, and click the **...** menu > **Advanced options**.
2. Click **Repair** first — this fixes the app without deleting its data.
3. Test the Store. If it still errors, go back and click **Reset** — this clears the app's data (you will need to sign in again, but your purchased apps are safe on your account).
4. Restart the laptop after a reset, then open the Store. If the Store was failing to update apps specifically, also check that you have enough free disk space — the Store fails downloads silently when the drive is nearly full, and the error codes it shows in that case are thoroughly unhelpful.

### Fix 4: Check the required background services

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find each of these, double-click it, set **Startup type** to **Automatic** (or **Manual** where noted), and click **Start** if it is stopped:
   - **Microsoft Store Install Service** (Automatic)
   - **Background Intelligent Transfer Service** (Manual is fine)
   - **Windows Update** (Manual is fine)
   - **Cryptographic Services** (Automatic)
3. If you use a VPN or proxy, temporarily disconnect it and retry the Store — some VPNs block the Store's endpoints specifically.

### Fix 5: Re-register the Microsoft Store with PowerShell

This effectively reinstalls the Store's package registration.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Run:
   `Get-AppxPackage -AllUsers *WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to finish (ignore red errors about packages that cannot be re-registered), then restart.
4. Open the Store — it should behave like a fresh install.

### Fix 6: Sign out and back into your Microsoft account in the Store

1. Open the Store, click your **profile icon** (top right), and choose **Sign out**.
2. Close the Store completely, reopen it, and sign back in.
3. Also verify your account at **Settings > Accounts > Your info** — if Windows itself shows an account problem, fix that first via the **Verify** link.
4. Stale account tokens are a classic cause of "acquiring license" errors.

### Fix 7: Run SFC/DISM and the Store troubleshooter

1. In an admin terminal, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
3. Apply its recommendations and restart.
4. If the Store broke right after a Windows update, check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that update — and consider uninstalling it via **Settings > Windows Update > Update history > Uninstall updates** as a last resort.

## Closing

Microsoft Store errors on an Acer laptop are almost never about Acer — they are about the Store's cache, its services, or its account state. `wsreset.exe` plus a clock check resolves the quick cases; repairing and re-registering the app handles the stubborn ones. The Store is one of Windows' flakier components, but it is also one of the most fixable — you will very rarely need to go beyond Fix 5. If the Store broke specifically after moving to 24H2, our [Microsoft Store errors in 24H2](/articles/how-to-fix-microsoft-store-error-in-windows-11-24h2/) covers the version-specific breakage.
