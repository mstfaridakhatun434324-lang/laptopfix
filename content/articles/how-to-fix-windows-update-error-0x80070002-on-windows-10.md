---
title: "How to Fix Windows Update Error 0x80070002 on Windows 10"
slug: how-to-fix-windows-update-error-0x80070002-on-windows-10
date: 2026-09-20
categories: ["windows-update"]
tags: ["0x80070002", "windows 10", "update error", "missing files"]
description: "Windows Update error 0x80070002 means files are missing on Windows 10. Here's how to restore them and get updates working."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070002-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070002 mean?"
    a: "It is the Windows error code for 'The system cannot find the file specified.' In Windows Update, it means the update engine expected a file — in the download cache, the component store, or the system folders — and it was not there. The usual causes are a corrupted update cache, interrupted downloads, or damaged system files."
  - q: "Is 0x80070002 a serious error?"
    a: "No, it is one of the more benign update errors. It indicates missing or corrupted update files rather than hardware failure or deep system damage. The standard repairs — clearing the update cache and running the system file checker — resolve it in the large majority of cases."
  - q: "Why does 0x80070002 appear even with a good internet connection?"
    a: "Because the missing files are local, not remote. Your connection successfully talks to Microsoft's servers, but the files Windows downloaded are corrupted, incomplete, or were deleted from the cache. The error is about what is on your disk, not what is on the network."
  - q: "Can 0x80070002 be caused by a failing drive?"
    a: "Occasionally, yes. If files keep going missing after you repair them — the error returns with every update — the drive may be corrupting data. Run chkdsk and check the drive's SMART health. But try the software fixes first; drive failure is the exception, not the rule."
---

Error **0x80070002** is Windows Update's way of saying "the file I need is not here." On Windows 10 it typically appears when the update engine reaches for a downloaded package, a cache entry, or a system file and finds nothing — or finds a corrupted fragment where a whole file should be. Your internet connection is irrelevant to this error; the problem is entirely local, in the files on your disk.

The error surfaces at the point where Windows verifies what it downloaded. Every update package carries cryptographic hashes, and the engine checks each file against its hash before installation — a security measure that also catches corruption. When a file is missing or its hash does not match, the engine reports 0x80070002 rather than installing something untrustworthy. So the error is actually the verification system working correctly: it caught a bad file and refused to proceed. The repair job is to remove the bad files and give the engine clean ones to verify, which is exactly what the steps below do.

Because the cause is missing or damaged files, the fix is straightforward in concept: remove the damaged files, repair the system files, and let Windows re-download clean copies. The steps below do exactly that, in the order that resolves the error fastest.

## Why this happens

- **Corrupted download cache.** Interrupted or errored downloads leave partial files that the engine treats as complete, then fails on.
- **Deleted or damaged SoftwareDistribution contents.** Cleanup tools or manual deletion removed files the update engine still references.
- **Corrupted system files.** Protected Windows files the update needs are damaged or missing.
- **A damaged component store.** The servicing store references files that no longer exist on disk.
- **Interrupted previous update.** A power loss or forced shutdown mid-update left the file state inconsistent.
- **Third-party cleanup tools.** Aggressive "optimizer" software deleting files from Windows folders that it should never touch.
- **Disk errors.** Bad sectors silently corrupting or losing update files between download and install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the date, time, and basic state

An incorrect system clock breaks update file verification.

1. Right-click the clock, choose **Adjust date/time**, and enable **Set time automatically** and **Set time zone automatically**.
2. A wrong date invalidates the cryptographic signatures on update files, producing file-not-found-style errors.
3. Restart and retry the update. This sounds trivial, but it genuinely fixes a share of 0x80070002 cases.

### Fix 2: Run the Windows Update troubleshooter

Let the automated repair handle the common file issues.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Windows Update** > **Run the troubleshooter**.
2. Apply every fix it offers and restart.
3. The troubleshooter specifically checks for missing update files and broken registrations — the exact territory of this error.

### Fix 3: Delete the corrupted update cache

Remove the damaged files so clean ones can replace them.

1. Open an elevated Command Prompt and stop the services:
   ```
   net stop wuauserv
   net stop bits
   ```
2. Delete the cache contents:
   ```
   rd /s /q C:\Windows\SoftwareDistribution\Download
   ```
3. Restart the services with `net start wuauserv` and `net start bits`, then check for updates. Windows re-downloads everything it needs from scratch.

### Fix 4: Repair system files with SFC and DISM

Restore the missing or damaged protected files.

1. In an elevated Command Prompt, run `sfc /scannow` and let it complete.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store — the source of truth for system files.
3. Restart and retry. These two commands directly address the "file not found" condition at the system level.

### Fix 5: Check the disk for errors

Rule out the drive as the file-eater.

1. Run `chkdsk C: /f` from an elevated prompt, confirm the restart prompt, and reboot.
2. After the scan, retry the update.
3. If chkdsk finds and repairs errors but 0x80070002 keeps returning, check the drive's SMART status with your manufacturer's diagnostic — recurring file loss is a drive-health warning.

### Fix 6: Reset the full update component set

When the cache alone is not enough, reset everything.

1. Stop all four update services and rename both cache folders:
   ```
   net stop wuauserv
   net stop cryptSvc
   net stop bits
   net stop msiserver
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   net start wuauserv
   net start cryptSvc
   net start bits
   net start msiserver
   ```
2. Retry the update. The complete reset procedure is explained in [our update component reset guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).

### Fix 7: Install the update manually or repair in place

Bypass or rebuild when the engine will not heal.

1. Note the failing KB number and install it directly from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — a manual install sidesteps the damaged automatic pipeline. See [how to install updates manually on Windows 10](/articles/how-to-manually-install-windows-update-on-windows-10/) for the procedure.
2. If manual installs also fail with 0x80070002, the servicing stack needs an in-place repair install, documented at [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows).

## Closing

Error 0x80070002 is refreshingly honest: files are missing, so you replace them. Clear the corrupted cache, repair the system files with SFC and DISM, and check the disk — in that order, the error resolves in the vast majority of cases. It is one of the least scary update errors precisely because its cause is so concrete, and the fix is equally concrete: give Windows back the files it lost. If the error keeps returning after a full repair cycle, treat the recurrence as data rather than bad luck: something is deleting or corrupting the files between repairs, and the usual suspects are an overzealous cleanup utility running on a schedule or a drive whose failing sectors keep eating newly written files. Identify the file-eater and the error stops coming back. Keep a monthly backup routine alongside it, and no update error can ever truly hurt you.
