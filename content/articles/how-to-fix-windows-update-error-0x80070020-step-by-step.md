---
title: "How to Fix Windows Update Error 0x80070020 Step by Step"
slug: how-to-fix-windows-update-error-0x80070020-step-by-step
date: 2026-10-11
categories: ["windows-update"]
tags: ["windows update", "0x80070020", "file lock", "windows 11"]
description: "Error 0x80070020 means a program is locking files Windows Update needs. Follow this step-by-step guide — pause antivirus, clean boot, and finish the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-step-by-step.webp"
faqs:
  - q: "What causes Windows Update error 0x80070020?"
    a: "The code is ERROR_SHARING_VIOLATION: another process had a file open that the updater needed to replace, so Windows blocked the install to prevent corruption. The most common locker is antivirus real-time protection, followed by stuck installer processes, cloud sync tools, backup agents, and occasionally the search indexer. It is purely a contention problem, and the fix is removing the contention rather than repairing the system."
  - q: "How do I find which program is locking the file?"
    a: "The clean-boot procedure is the reliable method: disable all non-Microsoft services and startup apps, retry the update, and re-enable programs in halves until the error returns. For a quicker first hint, check Task Manager for stuck msiexec.exe or setup.exe processes. Antivirus is the culprit often enough that pausing real-time protection is always worth trying before committing to the full clean boot."
  - q: "Will this error damage my Windows installation?"
    a: "No. The sharing violation is a protective refusal — Windows stops the install rather than writing over a file another process is actively using. Nothing is half-installed and nothing is corrupted by the failure itself. The only genuine risk is remaining unpatched while the error persists, which is why isolating the locker promptly matters more than worrying about damage."
  - q: "Why does the error happen at the same percentage every time?"
    a: "Because the updater reaches the same locked file at the same point in every attempt. The consistency is diagnostic gold: it confirms a specific file is blocked rather than random corruption striking. A clean boot removes the locker, and the update then sails past the exact percentage where it always stalled, which also confirms your diagnosis was correct."
---

Error 0x80070020 means ERROR_SHARING_VIOLATION — the updater tried to update a file that another program was using, and Windows said no. It's a traffic jam, not a breakdown: two processes want the same file, and the update loses. Nothing installed, nothing broke, but the update can't finish until the road is clear.

The consistent signature of this error is where it stalls — usually the same percentage every time, because the updater hits the same locked file at the same point in the sequence. That consistency is your diagnostic clue, and it's a reassuring one: random corruption strikes unpredictably, but a lock strikes repeatably. You're not dealing with a damaged system; you're dealing with a scheduling conflict between two programs.

It's also worth appreciating what Windows is doing here. Overwriting a file that another process is actively using could corrupt that process or leave the file in a torn state, so the updater declines the operation rather than risk it. The frustration is that Windows reports the collision without naming the other party. Every fix below is designed to answer that one unanswered question — who is holding the file? — starting with the most likely suspects and ending with a procedure that identifies any locker with certainty.

## Why this happens

- **Antivirus real-time scanning.** The scanner locks files to inspect them at exactly the moment the updater needs to replace them — the single most common cause of this code.
- **Stuck installer processes.** A previous `msiexec.exe` or `setup.exe` that never exited keeps its file handles claimed indefinitely.
- **Cloud sync clients.** OneDrive, Dropbox, and similar tools lock files mid-sync, and their timing is unpredictable.
- **Backup software.** Scheduled backup jobs claim large sets of files during the update window.
- **Windows Search indexer.** The indexer occasionally locks a file the updater wants to replace, especially right after boot.
- **A pending reboot from an earlier update.** Files already flagged for replacement at restart can't be touched again until that restart happens.
- **Corrupted updater state.** A confused update service can end up contending with its own stale locks from a previous failed attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry immediately

A genuine reboot clears every transient lock in one move, so always start here.

1. Save all your work, then do a full **Restart** from the Start menu — not a shutdown, because fast startup can preserve file locks across a shutdown.
2. As soon as you're back at the desktop, open **Settings > Windows Update** and click **Check for updates** or **Retry** before launching anything else.
3. If the update now proceeds past its old stall point, the locker was a transient background task that has since finished.
4. If 0x80070020 returns at the same percentage, the locker is persistent and you continue to Fix 2.

### Fix 2: Temporarily disable third-party antivirus

Real-time protection is the most common persistent locker, so test it before anything elaborate.

1. Open your third-party antivirus and pause or disable its real-time protection; Windows Security automatically covers you during the test.
2. Immediately retry the failing update while protection is paused — don't browse or delay, just run the update check.
3. Re-enable your antivirus right after the test, regardless of whether the update succeeded.
4. If the update went through, add `C:\Windows\SoftwareDistribution` to the antivirus exclusions, or make pausing protection part of your update routine.

### Fix 3: End stuck installer processes

A previous installation that never cleaned up after itself squats on the files your update needs.

1. Press **Ctrl + Shift + Esc** to open Task Manager and switch to the **Details** tab.
2. Scan for `msiexec.exe`, `setup.exe`, or `TrustedInstaller.exe` entries that show no CPU activity and aren't tied to anything you're doing.
3. Right-click one stuck process and choose **End task** — a single clean termination, not a killing spree.
4. Restart the laptop to release any remaining handles, then retry the update.

### Fix 4: Quiet sync and backup tools

Cloud sync clients are stealthy lockers because they touch files on their own schedule.

1. Click the OneDrive icon in the taskbar and choose **Pause syncing**; quit Dropbox or any other sync client entirely for the test.
2. Check whether a scheduled backup is running — backup tools claim huge file sets and are frequent collision partners.
3. With the sync tools quiet, retry the update check.
4. Resume syncing afterward, and consider keeping backups scheduled well away from your usual update window to prevent future collisions.

### Fix 5: Perform a clean boot to isolate the locker

This is the definitive diagnostic: strip the system to Microsoft-only software and see if the error survives.

1. Press **Windows key + R**, type `msconfig`, and press Enter. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
2. Open Task Manager's **Startup apps** tab and disable every entry, then restart the laptop.
3. In this minimal state, retry the update — it almost always succeeds here, which proves a third-party program is the locker.
4. Re-enable services in halves, rebooting and retesting after each half, until 0x80070020 returns. The last group you enabled contains the culprit; update, reconfigure, or replace that program.

### Fix 6: Reset the Windows Update components

Sometimes the updater contends with its own stale state from a previous failed attempt.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, and `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, and `net start msiserver`.
4. Retry the update; the fresh component state carries no stale locks or confused pending operations.

### Fix 7: Install the update manually in a quiet environment

For the last stubborn package, combine the standalone installer with minimal contention.

1. Note the failing KB number from **Settings > Windows Update > Update history**.
2. Download that KB as an x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Pause your antivirus and sync tools as in Fixes 2 and 4, then run the standalone installer — its simpler flow holds fewer files open simultaneously.
4. Confirm the KB shows as installed in Update history, then run a normal check. For background on sharing-violation scenarios, Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) is the authoritative reference.

## Closing

Error 0x80070020 is contention, not corruption — something else is holding the file, and the clean-boot sequence in Fix 5 identifies the holder on any laptop with certainty. For HP-specific angles like bundled utilities acting as lockers, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80070020-on-hp-laptop/), and if your failure is invalid data rather than a locked file, the [0x8007000D step-by-step guide](/articles/how-to-fix-windows-update-error-0x8007000d-step-by-step/) is the correct companion.
