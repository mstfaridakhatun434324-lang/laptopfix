---
title: "Fix 'Feature Experience Pack' Failed to Install"
slug: best-way-to-fix-feature-experience-pack-failed-to-install
date: 2026-09-28
categories: ["windows-update"]
tags: ["feature experience pack", "update failed", "windows 11", "windows update"]
description: "Windows Feature Experience Pack failing to install? It's a small but fussy package. Here are 7 fixes — from Store repair to manual install."
thumbnail: "/images/thumbs/best-way-to-fix-feature-experience-pack-failed-to-install.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It is a small Microsoft package that delivers updates to Windows shell features — things like the Snipping Tool, the touch keyboard, and parts of the Settings app — independently of full OS builds. Because it updates through both Windows Update and the Microsoft Store servicing pipeline, it can fail for Store-related reasons that never affect regular cumulative updates, which is why it needs its own troubleshooting approach."
  - q: "Do I actually need the Feature Experience Pack to install?"
    a: "Not urgently, but yes eventually. It is not a security update, so a failed install leaves you unpatched in no meaningful sense — but it does gate newer versions of built-in apps and shell features. More importantly, a persistently failing package can block or complicate other updates behind it. Fix it at your convenience, but do not ignore it for months."
  - q: "Why does it fail when my other updates install fine?"
    a: "Because it travels a different pipeline. The Feature Experience Pack is serviced partly through the Microsoft Store infrastructure, so Store cache corruption, a broken Store app, or account sync problems can fail it while classic Windows Update packages sail through. That split pipeline is also why the standard update-cache reset sometimes does not help — you have to repair the Store side too."
  - q: "Will reinstalling the Microsoft Store delete my apps?"
    a: "No. Re-registering or resetting the Microsoft Store app only repairs the Store application itself — your installed apps, games, and purchases are tied to your Microsoft account and remain untouched. You may need to sign back into the Store afterward, but nothing you installed will be removed by the repair."
---

The Windows Feature Experience Pack is a small update with an outsized ability to annoy. It appears in Windows Update, fails to install — sometimes with an error code, sometimes silently — and then keeps reappearing. Meanwhile every other update installs fine, which makes the failure feel personal. It is not: the Feature Experience Pack travels a different servicing pipeline than cumulative updates, and that pipeline has its own distinct failure modes.

This package updates shell-level features (Snipping Tool, touch keyboard, parts of Settings) and is serviced through a hybrid of Windows Update and Microsoft Store infrastructure. That hybrid nature is the whole story: Store cache corruption, a damaged Store app, or account sync issues can kill the Experience Pack install while leaving classic updates untouched. The fixes below cover both sides of the pipeline, starting with the most common causes.

## Why this happens

- **Corrupted Microsoft Store cache.** The Store-side cache holds damaged package data that fails validation on install.
- **A broken Microsoft Store app.** If the Store app itself is damaged, Store-serviced packages cannot install.
- **Windows Update cache corruption.** The Windows Update side of the hybrid pipeline has its own damaged staging.
- **Account sync problems.** A Microsoft account in a bad auth state can block Store-pipeline installs.
- **Insufficient disk space.** Even small packages fail staging on a nearly full system drive.
- **Antivirus interference.** Real-time scanners occasionally quarantine the small executables in the package.
- **Pending restart deadlock.** The package queues behind a restart that never happens, failing on every retry.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the error code and restart properly

Start with the basics: a surprising number of Experience Pack failures are just a pending restart away from resolving.

1. Note any error code in **Settings > Windows Update > Update history** next to the failed Feature Experience Pack.
2. Do a full **Restart** (not shutdown) — the package often queues behind a restart, and shutdown with Fast Startup does not clear the same state.
3. After restarting, check for updates and retry the install immediately.
4. If it fails again with the same code, the pipeline itself needs repair — continue to Fix 2.

### Fix 2: Reset the Microsoft Store cache

The Store side of the pipeline is the most common culprit. Clear it first.

1. Press **Win + R**, type `wsreset.exe`, and press Enter. A blank command window opens for a minute or so, then the Microsoft Store launches — that means the cache cleared.
2. Open the Microsoft Store, click your profile icon, and check for Store app updates — install any pending ones, since an outdated Store app mishandles the package.
3. Sign out of the Store and sign back in to refresh the account auth state.
4. Return to **Settings > Windows Update** and retry the Feature Experience Pack install.

### Fix 3: Re-register the Microsoft Store app

If the Store app itself is damaged, resetting its cache is not enough — re-register the whole app package.

1. Open PowerShell as administrator (search PowerShell, right-click, **Run as administrator**).
2. Run: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` — this re-registers all built-in apps including the Store. It takes several minutes and shows red errors for system packages that cannot be re-registered; those are normal and safe to ignore.
3. Restart the laptop.
4. Open the Store to confirm it launches cleanly, then retry the Feature Experience Pack in Windows Update.

### Fix 4: Reset the Windows Update cache

Cover the Windows Update side of the hybrid pipeline too — damage there fails the package just as surely.

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run: `net start wuauserv`, `net start bits`, `net start cryptsvc`. Then check for updates and retry the install.

### Fix 5: Run both troubleshooters

Microsoft ships separate troubleshooters for the two pipelines — run them both.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter first and apply all suggested fixes.
3. Then run the **Windows Store Apps** troubleshooter and apply its fixes.
4. Restart and retry. If a troubleshooter will not run at all, see our guide to the [Windows Update troubleshooter not working](/articles/windows-update-troubleshooter-not-working-troubleshooting/).

### Fix 6: Repair system files and check disk space

Deeper corruption and cramped storage both break small-package installs in ways that look like pipeline failures.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
2. Confirm at least 10 GB free on C: at **Settings > System > Storage** — run Disk Cleanup if needed.
3. Temporarily pause third-party antivirus real-time protection and retry the install.
4. If DISM reports source errors, our guide to [running DISM RestoreHealth](/articles/how-to-run-dism-restore-health-on-windows-11/) covers feeding it repair files from a Windows ISO.

### Fix 7: Install via the Store or hide the update

Two endgame options: get the package through the other pipeline, or stop it from nagging while you wait for Microsoft to fix a bad release.

1. Open the Microsoft Store and check **Library** for pending updates to system components — the Experience Pack content sometimes arrives there instead.
2. If the package keeps failing identically across all fixes, use Microsoft's "Show or hide updates" troubleshooter to hide it temporarily — Microsoft occasionally ships a bad Experience Pack revision and reissues it days later.
3. Unhide it after a week or two and retry; reissued packages usually install cleanly.
4. As the absolute last resort, an in-place upgrade with the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) (keeping files and apps) resets both pipelines completely.

## Closing

The Feature Experience Pack fails because it straddles two servicing pipelines — Windows Update and the Microsoft Store — and either side can break the install while the other works fine. Reset the Store cache, re-register the Store app, clear the update cache, and the package almost always goes through. If regular cumulative updates start failing alongside it, the problem has spread to the core update machinery — our guide to [monthly cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-10/) (the techniques apply to Windows 11 too) covers that; and for keeping the whole system healthy, see our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/).
