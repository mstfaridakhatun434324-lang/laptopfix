---
title: "How to Fix Error 0x80070003 on Windows 10 (Update & Backup Errors)"
slug: how-to-fix-error-0x80070003-on-windows-10
date: 2026-09-08
categories: ["windows-errors"]
tags: ["0x80070003", "windows update error", "windows 10", "update failed"]
description: "Error 0x80070003 blocking Windows 10 updates or backups? Fix missing update files, corrupt caches, and broken services with this guide."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070003-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070003 mean?"
    a: "It's Windows' way of saying 'the system cannot find the path specified.' In the update context, it means Windows Update is looking for update files or folders that are missing or corrupted — usually because the SoftwareDistribution cache got damaged, an update partially downloaded, or a required system folder was moved or deleted."
  - q: "Will resetting Windows Update delete my files?"
    a: "No. Resetting the Windows Update components only clears the update cache (the SoftwareDistribution and catroot2 folders) and restarts the update services. Your documents, programs, and settings are completely untouched. The worst that happens is Windows re-downloads pending updates, which is exactly what you want when the cached copies are corrupt."
  - q: "Why does this error appear during backup too?"
    a: "The same error code appears in backup when the backup tool can't find a source path — for example, a library pointing to a folder that was moved, renamed, or lives on a disconnected drive. Check your backup settings for stale folder references and remove or fix them."
  - q: "How do I stop 0x80070003 from coming back?"
    a: "Keep the update cache healthy: don't delete system folders manually, let updates finish without forced shutdowns, and run the update troubleshooter at the first sign of trouble rather than after multiple failed attempts. If the error recurs frequently, check your drive health — recurring cache corruption can signal a failing drive."
---
Error 0x80070003 translates to "the system cannot find the path specified" — Windows Update went looking for files it expected to be there, and they weren't. This usually means the update cache got corrupted: a download was interrupted, files were partially written, or something cleaned out folders Windows Update depends on. The fix is straightforward: clear the bad cache, restart the services, and let Windows download fresh copies.

This guide walks the standard repair order, from the built-in troubleshooter to a full manual reset of the update components. Every step is non-destructive — your files, programs, and settings are never at risk. The whole process takes about twenty minutes, and the manual reset in Fix 2 is the step that actually resolves most cases, so don't be tempted to skip ahead to the heavier options.

## Why this happens

- **Corrupted SoftwareDistribution cache.** Interrupted downloads or disk errors leave the update cache in an inconsistent state.
- **Missing system folders.** Overzealous cleaning tools sometimes delete folders Windows Update expects to find.
- **Stuck update services.** The Windows Update, BITS, or Cryptographic services can hang in a bad state.
- **Corrupted system files.** Damaged core files break the update engine's ability to stage files.
- **Antivirus interference.** Some AV products quarantine update cache files mid-download.
- **Disk errors.** Bad sectors in the cache area cause repeated corruption of freshly downloaded files.
- **Metered connection interruptions.** On metered connections, Windows may pause downloads mid-file, leaving the cache in the exact half-written state that triggers this error.

## How to fix it

Work through these in order.

### Fix 1: Run the Windows Update troubleshooter

The automated first step — quick and safe.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Update** and click **Run the troubleshooter**.
3. Let it detect and apply fixes, then restart when prompted.
4. Try checking for updates again. If 0x80070003 persists, continue — the troubleshooter fixes service states but not deep cache corruption.

### Fix 2: Manually reset the Windows Update components

This is the definitive fix for cache corruption.

1. Open **Command Prompt as administrator** (right-click Start).
2. Stop the services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
5. Restart the laptop and check for updates — Windows rebuilds fresh cache folders automatically.
6. If a service refuses to stop, restart the laptop and try the sequence again — a stuck service usually releases after a reboot.
7. After restarting, open **Settings > Update & Security > Windows Update** and click **Check for updates** — expect a longer-than-usual download as Windows refetches everything cleanly.

### Fix 3: Repair system files

If the update engine itself is damaged, fix the files.

1. In an elevated Command Prompt, run `sfc /scannow`.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and retry the update.
4. If DISM fails, download the Windows 10 ISO and use it as a repair source — the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) can also provide specific update packages manually.

### Fix 4: Install the update manually

Bypass the broken automatic pipeline entirely.

1. Note the KB number of the failing update from **Settings > Update & Security > Windows Update > View update history**.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the package for your system type (x64 for most laptops).
3. Run the downloaded `.msu` file and follow the prompts.
4. Restart when asked. Manual installation often succeeds where the automatic downloader keeps tripping over its corrupt cache.

### Fix 5: Check disk health and free space

Rule out the physical layer.

1. In an elevated Command Prompt, run `chkdsk C: /f` and restart if prompted.
2. Ensure at least 20GB free on C: — updates fail in strange ways when disk space is critically low.
3. Run Disk Cleanup (**cleanmgr**) as administrator and clear **Windows Update Cleanup** and temporary files.
4. Retry the update with a healthy disk and ample free space.

### Fix 6: Temporarily disable third-party antivirus

AV products sometimes quarantine update files mid-download.

1. Fully uninstall (not just disable) your third-party antivirus from **Settings > Apps**.
2. Restart and rely on Windows Security temporarily.
3. Run the update check again.
4. If it succeeds, reinstall your AV afterward — or consider whether Windows Security alone meets your needs. Related update-code fixes: [0x80070057](/articles/error-code-0x80070057-fix/) and the [0x80073712 guide](/articles/how-to-fix-error-0x80073712-on-windows-10/).

### Fix 7: Perform an in-place upgrade repair

When the update engine is damaged beyond component resets.

1. Download the Windows 10 Media Creation Tool from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) (use the Windows 10 version).
2. Run it and choose **Upgrade this PC now**, keeping files and apps.
3. The in-place upgrade reinstalls Windows over itself, rebuilding the entire update stack.
4. After completion, updates should flow normally. This takes 30–60 minutes but preserves everything.
5. Once the in-place upgrade finishes, run Windows Update immediately and let it complete fully before reinstalling third-party software — you want to verify the repaired update pipeline works before adding variables back.

## Closing

Error 0x80070003 is almost always a cache problem, and the manual component reset in Fix 2 resolves the overwhelming majority of cases. The key discipline: when an update fails, fix the cache before retrying repeatedly — each failed retry can deepen the corruption, and Windows will happily keep failing the same way for weeks if you let it.

Once updates are flowing again, protect the pipeline going forward. Let updates finish without forced shutdowns, keep at least 20GB free on your system drive so staging never chokes, and leave the SoftwareDistribution folder alone — "cleaner" tools that touch it are a leading cause of this exact error. If the error ever returns, you'll now recognize it instantly and know that the component reset is a ten-minute fix, not a crisis.
