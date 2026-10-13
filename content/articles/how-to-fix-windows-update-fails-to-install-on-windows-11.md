---
title: "Windows Update Fails to Install on Windows 11? Here's the Fix"
slug: how-to-fix-windows-update-fails-to-install-on-windows-11
date: 2026-09-10
categories: ["windows-update"]
tags: ["update fails", "windows 11", "install error", "cumulative update"]
description: "Updates download but won't install on Windows 11? Follow this diagnostic-first guide to find the blocker and get them installed."
thumbnail: "/images/thumbs/how-to-fix-windows-update-fails-to-install-on-windows-11.webp"
faqs:
  - q: "Why do my updates download but fail to install?"
    a: "Downloading and installing are separate phases handled by different parts of Windows. A successful download only means the package arrived intact; installation can still fail because of corrupted system files, a damaged component store, conflicting drivers, insufficient disk space, or a pending restart from an earlier update that was never completed."
  - q: "Should I keep retrying a failed update?"
    a: "Two or three retries are reasonable, since transient glitches happen. Beyond that, stop retrying and diagnose instead — repeated failures usually mean a structural problem like a corrupted cache or a conflicting driver, and hammering the retry button will not fix it. Work through the steps below once rather than retrying blindly."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, as long as you stop the update services first. That folder only holds downloaded update files and installation history. Windows rebuilds it automatically the next time you check for updates. It never contains personal files, settings, or installed programs."
  - q: "What if every update fails, not just one?"
    a: "When all updates fail, the problem is the update engine itself rather than any single package — usually corrupted update components, a damaged servicing stack, or a system-level blocker like a broken driver. Focus on Fix 4 and Fix 6 below, which repair the engine and the servicing stack directly."
---

The pattern is familiar: Windows 11 downloads the update, the progress bar completes, the install starts — and then it fails, rolls back, or throws an error code. Sometimes it fails at 97%. Sometimes it reboots, says "Undoing changes," and hands you back an unpatched system. Downloading works, so your network is fine. The failure is in the installation phase, which means the problem lives inside Windows itself: its files, its drivers, its servicing stack, or its disk.

It helps to understand what "installation" actually involves, because it is several distinct phases and each fails differently. First the package is staged and verified, then files are replaced while Windows is running, then the machine reboots into the offline phase where the servicing stack applies changes that cannot happen on a live system, and finally the changes are committed. A failure before the reboot points at files, space, or the cache; a failure during the offline phase points at drivers or servicing corruption; a rollback after the reboot means the new state failed its consistency checks. Knowing which phase failed narrows the suspect list dramatically.

This guide treats "fails to install" as a diagnostic problem first. Instead of throwing random fixes at it, you will identify the actual blocker — the error code, the phase, the conflicting piece — and then apply the fix that matches.

## Why this happens

- **Corrupted system files.** Damaged Windows files that the update needs to modify or verify cause the installer to abort and roll back.
- **A damaged component store.** The WinSxS servicing store the update builds on is inconsistent, so the install cannot assemble its changes.
- **Conflicting or outdated drivers.** A driver the update tries to replace or work around crashes the install, especially display and storage drivers.
- **Insufficient disk space.** The install phase needs staging room beyond the download size; near-full drives fail late in the process.
- **A pending restart from a previous update.** An earlier update waiting for a reboot holds locks that block the new install.
- **Third-party software interference.** Antivirus, disk encryption tools, and system "optimizers" can block the file operations the installer performs.
- **A corrupted update cache.** Damaged files in SoftwareDistribution poison the install even though the download "completed."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the error code and check Update history

Diagnosis starts with the exact failure.

1. Open **Settings** > **Windows Update** > **Update history** and find the failed update. Note the error code next to it.
2. Search that code — common ones like 0x80070002, 0x80070005, and 0x800f081f each point to a specific cause (missing files, access denied, missing source).
3. Check whether the failure happens at the same percentage every time. Consistent failure points suggest a specific file or driver; random points suggest disk or memory issues.

### Fix 2: Free up disk space

Late-stage install failures are often just a space problem.

1. Open **Settings** > **System** > **Storage** and check free space on C:. You want at least 20 GB for a feature or large cumulative update.
2. Run **Disk Cleanup** (search for it in Start), click **Clean up system files**, and remove Windows Update Cleanup, Temporary files, and Delivery Optimization Files.
3. Empty the Recycle Bin and move large personal files off C: temporarily. Retry the install.

### Fix 3: Complete any pending restart first

A half-finished earlier update blocks everything behind it.

1. Check **Settings** > **Windows Update** for a "Restart required" notice. If present, restart immediately.
2. After rebooting, check **Update history** to confirm the earlier update shows as installed successfully.
3. Only then click **Check for updates** for the new package. Stacked pending restarts are a quiet cause of repeated install failures.

### Fix 4: Reset the update components

Clear the cache so the install starts from clean files.

1. Open an elevated Command Prompt and stop the services:
   ```
   net stop wuauserv
   net stop cryptSvc
   net stop bits
   net stop msiserver
   ```
2. Rename the cache folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
3. Restart all four services and retry the install. For a deeper explanation of this reset, see [how to reset stuck Windows Update components](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).

### Fix 5: Repair system files and the component store

Fix the foundation the installer builds on.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish — this repairs the servicing store.
2. Then run `sfc /scannow` to repair protected system files.
3. Restart and retry the update. If DISM itself fails, point it at a Windows 11 ISO as the repair source, downloadable from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 6: Update or roll back conflicting drivers

Driver conflicts are the most common cause of installs that fail near the end.

1. Open **Device Manager** and look for warning icons, particularly on display and storage controllers.
2. Update the display driver from the manufacturer: NVIDIA, AMD, or [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. If a driver was updated right before the failures started, roll it back via **Properties** > **Driver** > **Roll Back Driver**.
4. Temporarily disable third-party antivirus during the install attempt, then re-enable it.

### Fix 7: Install the update manually from the Catalog

Bypass the automatic engine when it will not cooperate.

1. Note the KB number of the failing update from Update history.
2. Download it from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the `.msu` file.
3. If the manual install also fails, note where — a manual-install failure with the same code confirms the problem is in the servicing stack, not the download pipeline. See [how to install a KB manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/) for the full procedure and architecture-matching details.

## Closing

"Fails to install" is Windows Update's way of saying the download was fine but the system was not ready. Read the error code, clear the space, finish pending restarts, reset the cache, repair the files, and sort out the drivers — in that order, and you will find the actual blocker instead of guessing. The manual Catalog install is always there as the final route for a package the automatic engine simply refuses to handle.
