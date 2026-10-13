---
title: "How to Fix a Failed Monthly Cumulative Update, Step by Step"
slug: how-to-fix-monthly-cumulative-update-failed-step-by-step
date: 2026-10-01
categories: ["windows-update"]
tags: ["cumulative update", "windows update", "failed update", "patch tuesday", "troubleshooting"]
description: "A monthly cumulative update that keeps failing isn't random. Follow this step-by-step sequence to diagnose and fix it on any Windows 10 or 11 laptop."
thumbnail: "/images/thumbs/how-to-fix-monthly-cumulative-update-failed-step-by-step.webp"
faqs:
  - q: "Why does the same cumulative update fail every month?"
    a: "Recurring failures almost always point to a persistent blocker rather than a bad update package: a corrupted component store, a broken update cache, insufficient disk space, or a conflicting driver or antivirus. Until that blocker is removed, every month's update will hit the same wall at the same point."
  - q: "Is it safe to skip a failed cumulative update?"
    a: "Temporarily, yes — Windows will keep offering it. But cumulative updates bundle security patches, so skipping leaves known vulnerabilities unpatched. Fix the underlying failure rather than hiding the update long-term. A pause of a week or two while you troubleshoot is reasonable."
  - q: "How much free disk space does a cumulative update need?"
    a: "Microsoft recommends at least 10 GB free on the system drive, and in practice 15–20 GB is safer. The update downloads the full package, stages it, keeps a rollback copy, and then cleans up. Tight disk space is one of the most common causes of cumulative update failures on older laptops."
  - q: "What if the update fails at the same percentage every time?"
    a: "A consistent failure point is diagnostic gold. Failing early (0–30%) usually means download or verification problems. Failing late (70–100% or during reboot) usually means driver conflicts, disk errors, or corrupted system files. Match your troubleshooting to where it stops."
---

Every month, Microsoft ships a cumulative update that bundles that month's security fixes and quality improvements into a single package. And every month, some laptops refuse to install it — downloading fine, then failing at install, or installing and then rolling back with a "we couldn't complete the updates" message. If yours fails month after month, stop treating each failure as a new problem. It is almost certainly one persistent blocker, and this guide walks you through finding and removing it, step by step.

The sequence below is ordered deliberately: quick checks first, then cache and file repairs, then the heavier repairs. Check for updates after each major step and stop when it installs. Note exactly where the failure occurs each time — download, install, or reboot phase — because that tells you which fixes matter most.

## Why this happens

- **Corrupted update cache:** The SoftwareDistribution folder holds damaged or partial package files, so the installer fails verification or cannot find expected components.
- **Broken component store:** DISM-level corruption in WinSxS means the update has no clean baseline to apply its changes against, and setup aborts.
- **Insufficient disk space:** Cumulative updates need room to download, stage, and keep a rollback snapshot. Laptops with nearly full system drives fail repeatedly.
- **Conflicting drivers:** Storage, display, or antivirus filter drivers can block the update's driver-migration phase, especially on machines with old OEM drivers.
- **Antivirus interference:** Real-time protection can quarantine update payload files mid-install, leaving the package incomplete and triggering a rollback.
- **Pending operations from a previous failure:** A half-applied update leaves pending.xml entries and registry flags that block every subsequent attempt until cleared.
- **Corrupted system files:** Damaged protected files that SFC would flag can cause the update's file-replacement phase to fail hash verification.
- **Metered or unstable connection:** A connection that drops during the multi-gigabyte download produces a truncated package that fails integrity checks at install time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free up disk space and check the failure point

Rule out the simplest blocker first. Note whether the update fails during download, during the install percentage, or during the reboot — you will use this later.

1. Open **Settings > System > Storage** and confirm at least 15 GB free on C:. If not, run **Disk Cleanup** (search it in Start), tick **Windows Update Cleanup** and **Temporary files**, and clean up.
2. Try the update again and record exactly where it fails and any error code shown.
3. If it fails during download every time, skip ahead to Fix 4 (cache reset) as your priority. If it fails during reboot, prioritize Fix 5 (DISM/SFC).

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter resets update components and clears common blockers automatically. It resolves a surprising share of cumulative update failures on its own.

1. On Windows 11: **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.
2. On Windows 10: **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update > Run the troubleshooter**.
3. Apply every fix it suggests, restart, and retry the update.

### Fix 3: Pause, then unpause updates to clear pending state

Sometimes a stuck pending operation blocks the queue. Pausing updates for a week clears the active download state, and unpausing forces a fresh evaluation.

1. Go to **Settings > Windows Update** (or **Update & Security > Windows Update** on Windows 10).
2. Click **Pause updates** and choose one week.
3. Restart the laptop.
4. Return and click **Resume updates**, then **Check for updates**.

### Fix 4: Reset the update cache (SoftwareDistribution and Catroot2)

This is the highest-yield fix for recurring cumulative update failures. It discards every downloaded and half-installed package and forces a clean download.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)**.
2. Run these three commands to stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart the laptop and check for updates. The download starts over from zero — that is expected and desired.

### Fix 5: Repair the component store with DISM, then SFC

If the update downloads cleanly but fails during installation, the component store is the likely culprit. DISM restores it; SFC then fixes protected files.

1. Open **Terminal (Admin)**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`. Allow 15–30 minutes; it downloads healthy replacements from Windows Update.
3. Run `sfc /scannow` and wait for verification to complete.
4. Restart and retry the cumulative update. This pair resolves most install-phase failures, including the [parameter-incorrect 0x80070057 error](/articles/how-to-fix-windows-update-error-0x80070057-on-windows-11/) that sometimes appears with cumulative packages.

### Fix 6: Install the update manually from the Microsoft Update Catalog

If Windows Update itself is the broken link in the chain, bypass it. The standalone installer applies the same cumulative package without the download pipeline.

1. Note the KB number of the failing update (shown in update history).
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for that KB number.
3. Download the version matching your system (x64 for most laptops; check **Settings > System > About > System type**).
4. Run the downloaded `.msu` file and follow the prompts, then restart.

### Fix 7: Temporarily disable third-party antivirus and retry

If every automated method fails, security software is a prime suspect — it can intercept update files at the exact moment they are written.

1. Disable real-time protection in your antivirus (use its temporary pause option).
2. Retry the update via Windows Update or the manual catalog installer.
3. Re-enable protection immediately after the install completes and the laptop restarts.
4. If this was the fix, add Windows Update exclusions in your antivirus settings so next month's cumulative update does not hit the same wall.

If the update never gets far enough to fail at install because the download itself stalls, see our guide to [unsticking frozen update downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/) first.

## Closing

A cumulative update that fails every month is not bad luck — it is a stuck pipeline, and the steps above clear it in a logical order: space, troubleshooter, pause cycle, cache reset, DISM and SFC, manual install, antivirus check. Most laptops are fixed by Fix 4 or Fix 5. Keep a note of which step worked, because if the same failure returns next month, you will know exactly where to start instead of guessing all over again.
