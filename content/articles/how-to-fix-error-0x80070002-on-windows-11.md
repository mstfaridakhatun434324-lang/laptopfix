---
title: "How to Fix Windows 11 Error 0x80070002"
slug: how-to-fix-error-0x80070002-on-windows-11
date: 2026-09-21
categories: ["windows-errors"]
tags: ["0x80070002", "update error", "file not found"]
description: "Error 0x80070002 means Windows 11 can't find files it needs for updates or installs. Repair the missing pieces with these steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070002-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070002 mean?"
    a: "It is Windows' file-not-found error surfacing through updates, installs, or backups: the system expected a file to exist and it was not there. In Windows Update it usually means corrupted or missing update cache files; in backups it means a missing profile path; in Store installs it means damaged app packages. The context where you see it determines the right fix."
  - q: "Why does 0x80070002 happen during Windows Update?"
    a: "The update engine downloads files into the SoftwareDistribution folder and later expects to find them there. If the download was corrupted, interrupted, or partially cleaned by a disk utility, the expected files are missing and the update fails with this code. Resetting the update cache so everything downloads fresh is the standard fix."
  - q: "Can disk cleanup tools cause 0x80070002?"
    a: "Yes. Aggressive third-party cleaners sometimes delete files from the update cache or WinSxS component store that Windows still references. Stick to the built-in Disk Cleanup tool and avoid cleaners that promise to remove Windows update files or system caches beyond what Microsoft's own tool offers."
  - q: "How do I fix 0x80070002 for Microsoft Store apps?"
    a: "Run wsreset.exe to clear the Store cache, then run the Windows Store Apps troubleshooter from Settings > System > Troubleshoot > Other troubleshooters. If a specific app fails, uninstall it completely and reinstall from the Store. Persistent Store-wide failures usually yield to resetting the Store app itself in Settings > Apps."
---

Error 0x80070002 is Windows reporting that a file it went looking for was not there. It is the "file not found" of the Windows error world, and it shows up in Windows Update, Microsoft Store installs, system backups, and driver installations alike. The code is the same everywhere; the fix depends on which operation threw it.

For most people, this error appears in Windows Update: the updater expects cached files that are missing or corrupted, and the whole update aborts. The fixes below cover the update scenario first (the most common), then the Store and general cases. One reassuring fact: because this error is about missing files rather than broken ones, the repairs are additive — you are giving Windows fresh copies of what it lost, which is safer than most troubleshooting. Nothing below risks your personal data. One more thing worth knowing: because this error is about files Windows expected but could not find, it sometimes appears in misleading places — a backup failing with 0x80070002, for instance, usually means the target path changed, not that Windows itself is broken. Match the fix to the context where you saw the error and you will resolve it faster.

## Why this happens

- **Corrupted or incomplete update cache.** Missing files in SoftwareDistribution that the updater expects to find.
- **Overzealous cleanup tools.** Third-party cleaners deleting referenced system files.
- **Corrupted system files.** Damage to components that resolve file paths.
- **Wrong system date and time.** Breaks the secure connections and file validation updates rely on.
- **Corrupted Store cache.** Damaged app packages producing file-not-found during installs.
- **Damaged user profile paths.** Backup and sync operations referencing folders that no longer exist.
- **Broken Windows Update Medic Service recovery.** The service meant to self-heal update components failing and leaving gaps behind.

## How to fix it

Work through these in order, retrying the failed operation after each step.

### Fix 1: Check date, time, and run the troubleshooter

Quick wins first.

1. Right-click the taskbar clock, choose **Adjust date and time**, enable **Set time automatically**, and click **Sync now**.
2. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
3. Run **Windows Update** (or **Windows Store Apps** if the error is Store-related) and apply its fixes.
4. Restart and retry.

### Fix 2: Reset the Windows Update cache

The core fix for update-related 0x80070002.

1. Open **Terminal (Admin)** from `Win + X`.
2. Stop the services:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptSvc`
3. Rename the cache:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start bits`
   `net start cryptSvc`
5. Go to **Settings > Windows Update** and check for updates.
6. Let the check complete fully before judging the result — the first check after a cache reset rebuilds the update metadata, which takes several minutes on slower machines.

### Fix 3: Clear the Microsoft Store cache

For Store-related 0x80070002:

1. Press `Win + R`, type `wsreset.exe`, and press Enter — a blank Command Prompt window appears while the cache clears, then the Store opens.
2. If a specific app fails, uninstall it from **Settings > Apps > Installed apps** and reinstall from the Store.
3. For persistent Store-wide errors, go to **Settings > Apps > Installed apps > Microsoft Store > Advanced options** and click **Repair**, then **Reset** if needed.

### Fix 4: Repair system files with SFC and DISM

Fix the underlying file-resolution damage.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow`.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and retry the failed operation.

### Fix 5: Check the disk for errors

Missing files sometimes mean a struggling drive.

1. Open **Terminal (Admin)** and run `chkdsk C: /f`, scheduling on restart if prompted.
2. After the check completes, retry the update or install.
3. If CHKDSK finds many bad sectors, back up your data — the drive may be failing.

### Fix 6: Install the update manually from the Update Catalog

Bypass the damaged automatic pipeline.

1. Note the KB number from **Settings > Windows Update > Update history**.
2. Search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download the matching .msu and install it directly.

### Fix 7: Perform an in-place upgrade as the last resort

When system file damage resists repair:

1. Download the **Media Creation Tool** from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it, choose **Upgrade this PC now**, and keep personal files and apps.
3. The upgrade reinstalls Windows cleanly over the existing install, replacing all damaged system files.

The closely related [error 0x80070057](/articles/error-code-0x80070057-fix/) shares several fixes, and brand-specific install failures are covered in our [0x80070002 on Lenovo](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/) guide.

### Fix 8: Re-register all system app packages and reset the update medic service

When corruption spans multiple system components, re-register them in bulk.

1. Open **Terminal (Admin)**.
2. Re-register built-in app packages:
   `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
   (Ignore red errors for packages that cannot re-register — they are normal.)
3. Restart the **Windows Update Medic Service**: open `services.msc`, find it, and click **Restart**.
4. Restart the laptop, then retry the failed operation.
5. If the error appeared during backup, also verify the backup target path exists and is writable — a renamed or disconnected target produces this exact code.

## Closing

Error 0x80070002 is Windows losing track of its own files, and the remedy is to give it fresh copies: reset the update cache, clear the Store cache, repair system files, and the missing pieces get rebuilt. Avoid aggressive third-party cleaners going forward — the built-in Disk Cleanup knows which files are safe to remove, and random "system boosters" do not. When the automatic routes keep failing, the manual Catalog install or an in-place upgrade finishes the job. And if the error ever returns after a cleaner ran, you will know exactly which program to blame — uninstall it and stick with the built-in tools.
