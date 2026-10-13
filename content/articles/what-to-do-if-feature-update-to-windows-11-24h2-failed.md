---
title: "Feature Update to Windows 11 24H2 Failed? How to Get It Installed"
slug: what-to-do-if-feature-update-to-windows-11-24h2-failed
date: 2026-09-01
categories: ["windows-update"]
tags: ["24h2 feature update", "upgrade failed", "windows 11", "installation assistant", "troubleshooting"]
description: "Fix a failed feature update to Windows 11 24H2: decode the failure, clear compatibility blocks, and complete the upgrade with the right method."
thumbnail: "/images/thumbs/what-to-do-if-feature-update-to-windows-11-24h2-failed.webp"
faqs:
  - q: "Why does the 24H2 feature update fail at the same percentage every time?"
    a: "A failure at a consistent percentage means the installer hits the same blocking condition on every run — usually a specific driver, a compatibility hold, or a corrupted file it needs at that phase. The setup log pinpoints which one, so check it instead of retrying blindly. The setupact.log file records the exact failing phase, which maps directly to the blocker you need to remove."
  - q: "Will a failed feature update delete my files?"
    a: "No. When a feature update fails, Windows automatically rolls back to your previous build with files, apps, and settings intact. The rollback itself can take 30 minutes or more, so let it finish rather than forcing the machine off. Rollbacks are extensively tested by Microsoft, and interrupted upgrades return to the previous build with user data intact."
  - q: "How much free space does the 24H2 update need?"
    a: "Microsoft recommends at least 20 gigabytes of free space on the system drive, and more is better. The installer stages the new build, keeps a rollback copy, and needs working room. Updates on nearly-full drives fail far more often."
  - q: "Should I use Windows Update or the Installation Assistant for 24H2?"
    a: "If Windows Update fails repeatedly, the Installation Assistant or a mounted ISO often succeeds because they use a fresher installer engine and bypass cached delivery problems. The end result is identical — a full in-place upgrade to 24H2. Both produce an identical in-place upgrade, so choose whichever path is currently working on your machine rather than retrying the broken one."
---

A failed feature update to Windows 11 24H2 is a special kind of frustration: it downloads for an hour, installs to 70 percent, then announces "Something went wrong" and rolls everything back. The rollback works — your files survive — but you are left exactly where you started, with no clear reason why. The good news is that feature-update failures are highly diagnosable. Setup writes detailed logs, fails at consistent phases for consistent reasons, and almost always yields to a methodical approach.

This guide treats the failed 24H2 upgrade like a technician would: read the failure signature, remove the blocker, choose the right install method, and verify the result. No blind retrying.

## Why this happens

- **Incompatible driver in the migration path:** Setup migrates drivers to the new build; one incompatible driver — commonly storage controllers, old VPN virtual adapters, or display drivers — aborts the install at the same phase every time.
- **Compatibility hold:** Microsoft blocks 24H2 on machines with known-bad driver or firmware combinations. The update may download, then fail when the hold is enforced.
- **Corrupted servicing stack:** Damage from earlier cumulative-update failures carries into the feature update, which needs a healthy servicing engine to stage the new build.
- **Insufficient disk space:** The installer needs room for the new Windows image plus a full rollback copy; cramped drives fail late in the process when space runs out.
- **Third-party antivirus interference:** Deep kernel hooks from security products conflict with the build-to-build migration and trigger rollbacks.
- **Failing hardware:** Bad RAM or disk sectors surface during the heavy file operations of an upgrade, producing failures that look like software bugs.
- **Stale update cache:** A corrupted download of the multi-gigabyte feature update fails integrity checks mid-install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the setup logs to find the failure phase

1. After a rollback, open `C:\$Windows.~BT\Sources\Panther\setupact.log` and search for "failed" near the end of the file.
2. Note the phase: failures in **Downlevel** happen before the first reboot (drivers, compatibility), while **OOBE** or **Second boot** failures happen after (driver migration, services).
3. Also check **Settings > Windows Update > Update history** for the error code — 0xC1900101 means driver trouble, 0x80070070 means disk space.
4. Knowing the phase turns a mystery into a targeted repair; everything below maps to a specific phase.

### Fix 2: Remove the incompatible drivers setup chokes on

1. For 0xC1900101 failures, open **Device Manager** and look for devices with yellow warnings — update or uninstall them.
2. Temporarily uninstall third-party VPN clients, virtual network adapters, and disk-encryption filter drivers; reinstall them after the upgrade.
3. Update the storage controller and chipset drivers from your laptop maker's site before retrying.
4. If a [driver update from Windows Update](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) is itself failing, resolve that first — a broken driver pipeline poisons feature updates too.

### Fix 3: Free space and clear the stale download

1. Ensure at least 25–30 GB free on C: using **Settings > System > Storage** and Disk Cleanup (include **Previous Windows installations** and **Temporary Windows installation files**).
2. Stop the update services and rename the SoftwareDistribution folder to force a fresh download of the feature update.
3. Disconnect unnecessary USB devices — external drives and docks sometimes get scanned into the migration and cause failures.
4. Retry via Windows Update once with a clean cache and roomy drive.

### Fix 4: Temporarily remove third-party antivirus

1. Uninstall (not just disable) third-party antivirus — disabled products still leave kernel drivers loaded that conflict with build migration.
2. Windows Defender activates automatically and is fully compatible with the upgrade process.
3. Retry the feature update with only Defender running.
4. Reinstall your preferred security product after 24H2 is stable, and confirm it supports the new build.

### Fix 5: Use the Installation Assistant instead of Windows Update

1. Download the **Windows 11 Installation Assistant** from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and let it download a fresh copy of 24H2 — this bypasses whatever is corrupted in the Windows Update delivery path.
3. Keep the laptop on AC power and do not use it heavily during the install; the assistant needs several uninterrupted hours on slower machines.
4. The assistant performs the same in-place upgrade, preserving files, apps, and settings.

### Fix 6: Do an ISO-based in-place upgrade for stubborn cases

1. Download the Windows 11 24H2 ISO from the [download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it by double-clicking.
2. Run `setup.exe` from the mounted drive and choose **Keep personal files and apps**.
3. The ISO method uses the newest installer engine and skips the Windows Update client entirely — it succeeds where both Update and the Assistant fail.
4. If setup reports a compatibility hold, check the referenced driver or app and update or remove it, then rerun setup.

### Fix 7: Test hardware when software fixes keep failing

1. Run **Windows Memory Diagnostic** (search it in Start) to rule out bad RAM — memory errors corrupt the massive file copies an upgrade performs.
2. Run `chkdsk C: /f` to check the system drive, and review SMART status.
3. If hardware tests fail, no software fix will make the upgrade succeed; replace the faulty component first.
4. After a successful upgrade, watch for post-update issues like [slowness after the 24H2 update](/articles/best-way-to-fix-windows-11-slow-after-24h2-update/) and address them while the rollback window is still open.

## Closing

Feature updates fail for reasons, not for spite — a driver, a hold, a full disk, a damaged cache, or tired hardware. Read the log, clear the blocker, pick the install method that bypasses the damage, and 24H2 goes on cleanly. And once it does, give the new build a week of normal use before declaring victory; the fixes that matter most are the ones you verify.
