---
title: "How to Fix a Failed Monthly Cumulative Update After a Windows 11 Update"
slug: how-to-fix-monthly-cumulative-update-failed-after-windows-11-update
date: 2026-10-03
categories: ["windows-update"]
tags: ["cumulative update", "monthly update", "windows update", "update failed", "windows 11"]
description: "The monthly cumulative update keeps failing after your last Windows 11 update? Diagnose the failure and get the patch installed."
thumbnail: "/images/thumbs/how-to-fix-monthly-cumulative-update-failed-after-windows-11-update.webp"
faqs:
  - q: "What is a cumulative update?"
    a: "A cumulative update is Microsoft's monthly rollup of security patches and bug fixes for Windows 11, released on the second Tuesday of each month. Each one contains all previous fixes, so installing the latest brings you fully current. When one fails, your system misses that month's security patches until the failure is resolved or the next month's update supersedes it."
  - q: "Why would a cumulative update fail right after a previous update succeeded?"
    a: "The previous update often leaves the pipeline in a fragile state: a corrupted download cache, a service that did not restart cleanly, or pending operations that never finalized. The next cumulative update then trips over that leftover damage. It is rarely the new update's fault — it is the debris from the last one."
  - q: "How do I find which cumulative update failed?"
    a: "Open Settings, then Windows Update, then Update history. Failed cumulative updates are listed by their KB number, such as KB5034441, along with an error code. The KB number lets you download the exact package manually from the Microsoft Update Catalog, and the error code points to the specific failure cause."
  - q: "Can I skip a failed cumulative update and wait for next month's?"
    a: "You can, since each cumulative update supersedes the last — next month's package includes everything this one had. But skipping leaves that month's security fixes uninstalled for weeks, which is a real exposure. Better to fix the failure now with the steps below; waiting should be the last resort, not the plan."
---

Microsoft ships a cumulative update for Windows 11 every month, and most of the time it installs without drama. Then one month it does not: the update downloads, attempts to install, fails — sometimes with an error code, sometimes by rolling back with the "undoing changes" screen — and the next attempt fails the same way. Notably, this often happens right after a previous Windows 11 update, which is a strong hint about the cause.

The pattern is the tell. When a cumulative update fails in the wake of a successful one, the new update is rarely the problem. The previous update left debris: a corrupted download cache, a service stuck in a bad state, pending operations that never finalized, or a driver the last update touched. The new cumulative update trips over that debris and fails. Fix the debris, and the update installs.

This guide is ordered to clear the most common debris first. Work through the fixes in order.

## Why this happens

- **The previous update corrupted the download cache.** Damaged files left behind poison the next update's download.
- **A service did not restart cleanly.** wuauserv, cryptSvc, or bits stuck in a bad state breaks the next install.
- **Pending operations never finalized.** An earlier update's unfinished restart leaves locks the new update cannot clear.
- **Insufficient disk space.** Cumulative updates need staging room; the last update may have eaten the remaining free space.
- **A driver the last update touched now conflicts.** Driver changes from the previous update can fail the new update's checks.
- **Corrupted system files.** Damage that the last update exposed — or caused — fails the new installer's verification.
- **Antivirus interference.** Security software that tolerated the last update blocks a file operation in this one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failed update and its error code

Start with specifics, not retries.

1. Open **Settings > Windows Update > Update history** and find the failed cumulative update. Note its KB number and error code.
2. Common codes: 0x80070002 (missing/corrupt files), 0x800f0922 (EFI partition space), 0x80070005 (permissions), 0x8024200D (download interrupted).
3. Search the KB number on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that month's release.
4. Keep the KB number handy — you will use it for the manual install in Fix 6.

### Fix 2: Restart properly to clear pending operations

A real restart clears more than you might expect.

1. Save your work and do a full **Restart** — not shutdown, which may use hybrid boot and preserve the stuck state.
2. After booting, wait five minutes for background services to settle.
3. Open **Settings > Windows Update** and click **Check for updates** before launching other programs.
4. If the update now installs, a pending operation was the blocker. If it fails identically, continue.

### Fix 3: Clear the update cache

The highest-probability fix for post-update failures.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Check for updates. The cumulative update re-downloads fresh, free of the previous update's debris.

### Fix 4: Free up disk space

The previous update may have consumed the last of your free space.

1. Check **Settings > System > Storage** for free space on C: — aim for at least 15 GB before a cumulative update.
2. Run **Disk Cleanup** with system files selected and remove **Windows Update Cleanup**, which deletes superseded update files from previous months.
3. Clear temporary files and the Recycle Bin.
4. Retry the update with confirmed free space.

### Fix 5: Run the troubleshooter and repair system files

Repair the pipeline and the system it updates.

1. Run the **Windows Update** troubleshooter under **Settings > System > Troubleshoot > Other troubleshooters**.
2. In an elevated Command Prompt, run `sfc /scannow` to completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15 to 30 minutes.
4. Restart and retry the update. These repairs fix the damage the previous update left behind.

### Fix 6: Install the cumulative update manually

Bypass the damaged pipeline for this specific update.

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for the KB number from Fix 1.
2. Download the package matching your system (x64 for most laptops) and run it.
3. The manual installer does not use the Windows Update download cache, so cache corruption is irrelevant to it.
4. Restart when prompted and verify the KB appears as installed in update history.

### Fix 7: Check for the specific error's known fix

Some error codes have targeted solutions worth trying before giving up.

1. For **0x800f0922**, the EFI system partition may be full — this needs partition management to resolve, and Microsoft documents the workaround.
2. For **0x80070005**, permission problems on update folders are the cause; the cache reset in Fix 3 usually resolves it, but persistent cases need the folder permissions repaired.
3. For repeated **0x8024200D**, network interruptions are corrupting the download — try the manual install over a stable wired connection.
4. If none of the targeted fixes work, pause updates for a week and let the next Patch Tuesday supersede the failed one — but treat this as a last resort, since it leaves security gaps.

## Closing

A cumulative update failing after a previous Windows 11 update is debris cleanup, not mystery: clear the cache, restart the services, free up space, and repair what the last update damaged. The manual catalog install is your reliable bypass when the automatic pipeline will not cooperate for one specific KB. And once the debris is cleared, the following months' updates typically install without any intervention at all. For error-specific guidance, the [0x80070002 walkthrough](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) and the [0xC1900101 driver-rollback guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/) cover the two most common cumulative update failure codes in depth.
