---
title: "How to Fix Windows Update Error Code 0x80070057"
slug: error-code-0x80070057-fix
date: 2026-09-21
categories: ["windows-errors"]
tags: ["windows-11", "windows-update", "error-code"]
description: "Error 0x80070057 blocking your Windows 11 updates? These fixes clear the corrupted cache and get updates installing again."
thumbnail: "/images/thumbs/error-code-0x80070057-fix.webp"
faqs:
  - q: "What does error code 0x80070057 mean?"
    a: "It translates to 'The parameter is incorrect' — Windows Update received data it can't process. The usual cause is a corrupted update cache (the SoftwareDistribution folder), though wrong system date/time, disk errors, and corrupted system files can produce the same code."
  - q: "Why does 0x80070057 keep coming back after I fix it?"
    a: "If the underlying cause is disk corruption or a failing drive, the update cache keeps getting damaged each time Windows rebuilds it. Run chkdsk and check your drive health — recurring 0x80070057 is often an early warning of storage problems."
  - q: "Can I just skip the update that's failing?"
    a: "You can pause updates temporarily, but the failed update will keep retrying and eventually block others. Better to fix the root cause now — the cache-clearing steps below take about ten minutes and resolve it permanently in most cases."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, with the update services stopped first (as shown in Fix 3). Windows rebuilds the folder automatically on the next update check. Renaming it instead of deleting is even safer — you keep a backup you can restore if something goes wrong."
---
Error code 0x80070057 is Windows Update's way of saying "the parameter is incorrect" — which is spectacularly unhelpful. In plain terms, the update engine downloaded or prepared files it can't make sense of, so the whole update fails. It shows up on Windows 11 when installing cumulative updates, feature updates, or even driver updates.

The fix is straightforward in most cases: the local update cache is corrupted, and clearing it lets Windows start fresh. Here's the full sequence, from the two-minute checks to the deeper repairs.

## Why this happens

- **Corrupted update cache.** The SoftwareDistribution folder holds downloaded update files; if they get damaged (bad shutdown, disk hiccup), every install attempt fails with 0x80070057.
- **Wrong system date and time.** Update servers reject requests from machines whose clock is significantly off, and the cryptographic checks fail with this exact error.
- **Corrupted system files.** Damage to the Windows Update components themselves produces the same code.
- **Disk errors.** Bad sectors in the areas where updates are staged corrupt the files as they're written.
- **Third-party antivirus interference.** Overzealous security software can quarantine or block update files mid-download.
- **Corrupted catroot2 folder.** This folder holds update signatures; if its database is damaged, signature verification fails.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Check for updates after each step — stop when they install cleanly.

### Fix 1: Check your date, time, and region settings

A wrong clock is the fastest fix when it applies.

1. Right-click the clock in the taskbar and choose **Adjust date and time**.
2. Turn on **Set time automatically** and **Set time zone automatically**.
3. Click **Sync now** under **Additional settings**.
4. Go to **Settings > Time & language > Language & region** and confirm your region is correct.
5. Try the update again. This alone fixes 0x80070057 more often than people expect.

### Fix 2: Run the Windows Update troubleshooter

Let Windows attempt its own automated repair first.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Windows Update** and click **Run**.
3. Let it diagnose and apply fixes — it commonly resets stuck services and repairs the update database.
4. Restart when it finishes and check for updates again.

### Fix 3: Clear the corrupted update cache

This is the core fix for 0x80070057 — it resolves the error for the majority of people.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Stop the update services:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptSvc`
   `net stop msiserver`
3. Rename (don't delete) the cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start bits`
   `net start cryptSvc`
   `net start msiserver`
5. Go to **Settings > Windows Update** and click **Check for updates**. Windows rebuilds both folders from scratch.

### Fix 4: Repair system files with SFC and DISM

If the update components themselves are damaged, the cache will just corrupt again.

1. In the same elevated **Command Prompt**, run `sfc /scannow` and wait for it to finish.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — this needs an internet connection.
3. Restart and retry the update. These repairs also help with the broader family of post-update failures, like the [driver IRQL errors after updates](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/) that share the same corrupted-component roots.

### Fix 5: Check the disk for errors

Rule out storage corruption as the recurring cause.

1. Open an elevated **Command Prompt**.
2. Run `chkdsk C: /f` — type **Y** when asked to schedule the scan, then restart so it runs before Windows loads.
3. After booting, open **PowerShell (Admin)** and check drive health: `Get-PhysicalDisk | Select FriendlyName, HealthStatus, OperationalStatus`.
4. If the health status isn't **Healthy**, back up your files — a failing drive will keep corrupting updates no matter how many times you clear the cache.

### Fix 6: Temporarily remove third-party antivirus and clean-boot

Eliminate software that's intercepting the update process.

1. Go to **Settings > Apps > Installed apps** and uninstall your third-party antivirus completely (disabling often leaves its filter drivers active). Windows Defender covers you in the meantime.
2. For a deeper isolation, perform a clean boot: press **Win + R**, type `msconfig`, go to the **Services** tab, check **Hide all Microsoft services**, click **Disable all**, then restart.
3. Try the update in this minimal state. If it succeeds, re-enable services in groups to find the conflicting program. Similar interference patterns cause other update-failure crashes like [page faults after updates](/articles/how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update/).

### Fix 7: Install the update manually or reset Windows Update

When the automatic path keeps failing, go around it.

1. Note the KB number of the failing update from **Settings > Windows Update > Update history** — you'll see entries like "Failed to install on ‎…" with the KB number beside them.
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search for that KB number, download the package matching your system (x64 for most modern laptops, ARM64 for Snapdragon machines — check **Settings > System > About** if unsure), and install it manually by double-clicking the `.msu` file.
3. If the manual install also fails with 0x80070057, reset the Windows Update components following Microsoft's documented reset procedure on the [Windows support hub](https://support.microsoft.com/en-us/windows) — this re-registers every update DLL and rebuilds the component store.
4. As a final option, use **Settings > System > Recovery > Fix problems using Windows Update** (reinstalls Windows while keeping files and apps) — this rebuilds the entire update stack cleanly without a full wipe.

## Closing

Error 0x80070057 is almost always a corrupted update cache wearing a cryptic disguise. Verify your clock, run the troubleshooter, and clear the SoftwareDistribution and catroot2 folders — that three-step combination fixes it for most people in under fifteen minutes. If it keeps coming back, look at the disk: recurring cache corruption is your early warning that the storage drive needs attention before it becomes a bigger problem.
