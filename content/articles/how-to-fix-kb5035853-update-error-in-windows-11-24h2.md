---
title: "KB5035853 Update Error on Windows 11 24H2? Fix It for Good"
slug: how-to-fix-kb5035853-update-error-in-windows-11-24h2
date: 2026-10-10
categories: ["windows-update"]
tags: ["kb5035853", "windows 11 24h2", "update error", "cumulative update"]
description: "Fix the KB5035853 update error on Windows 11 24H2: decode the error, repair the update pipeline, and install the cumulative update successfully."
thumbnail: "/images/thumbs/how-to-fix-kb5035853-update-error-in-windows-11-24h2.webp"
faqs:
  - q: "What causes the KB5035853 update error on 24H2?"
    a: "The most common causes are a corrupted Windows Update download cache, damaged system files that fail the update's pre-install checks, outdated servicing stack components, third-party antivirus blocking the install phase, or simply too little free disk space for the update to stage itself."
  - q: "How much free space does a 24H2 cumulative update need?"
    a: "Plan on at least 10 GB of free space on the system drive, and 20 GB is more comfortable. Cumulative updates stage the full package, keep a rollback copy, and need working room. Updates on nearly full drives fail in confusing ways that look like other errors."
  - q: "Can I skip KB5035853 and wait for the next cumulative update?"
    a: "Cumulative updates are, as the name says, cumulative — the next one includes everything in this one. Skipping is safe in the short term, but you stay unpatched until the next release. Fixing the pipeline now is better than postponing the same failure by a month."
  - q: "Why does the update reach 100% and then roll back?"
    a: "A rollback at the end means the install phase hit something it could not migrate — usually a driver, a corrupted system file, or a third-party filter. The error code in Update history plus the Setup event log will name the failing piece."
---

KB5035853 is a routine cumulative update for Windows 11 24H2, but on some laptops it refuses to install and rolls back with an unhelpful error. The update itself is fine — what is broken is the environment it is trying to install into. Your job is to find which part of that environment is broken and fix it.

This guide follows the order a repair technician uses: read the actual error, clear the usual blockers, repair the OS image, and install the update through the path of least resistance. Expect to spend 45 to 90 minutes, most of it waiting on scans.

One more thing before you start: do not "try" fixes at random. Each step below eliminates a suspect, so even the steps that do not fix it give you information. Keep notes on what you tried and what changed — if you end up needing the in-place upgrade at the end, that history tells you the deeper repairs are justified.

## Why this happens

- **Corrupted download cache:** Partial or mismatched package data in the SoftwareDistribution folder fails verification on every attempt.
- **Damaged system files:** The update's pre-install checks abort when protected OS files do not match their expected state.
- **Outdated servicing stack:** The component that installs updates can itself need an update first; without it, newer packages fail.
- **Third-party antivirus interference:** Filter drivers from security suites can block file operations during the install phase.
- **Low disk space:** Staging, rollback copies, and working files need gigabytes the system may not have.
- **Driver conflicts:** A misbehaving driver — often storage or display — can stall the install phase until it times out and rolls back.
- **Interrupted previous update:** A half-applied earlier update leaves component states the new package cannot reconcile, a close cousin of the [0x800f0922 failure pattern](/articles/how-to-fix-windows-update-error-0x800f0922-in-windows-11-24h2/).
- **Metered or proxy connections:** Restricted networks corrupt or truncate the download, producing a package that fails its hash check.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the real error code and the Setup log

1. Open **Settings → Windows Update → Update history** and click the failed KB5035853 entry to reveal the full error code.
2. Press **Win + R**, type `eventvwr.msc`, and check **Windows Logs → Setup** for errors at the failure time.
3. Note both the code and any driver or file named in the log — they direct everything that follows.
4. A generic "failed to install" with no code usually means the download itself is bad; a specific code points at the install phase.

### Fix 2: Free disk space and clear temporary files

1. Open **Settings → System → Storage** and check free space on C: — you want at least **10 GB**, ideally 20 GB.
2. Run **Disk Cleanup** as administrator, selecting temporary files, delivery optimization files, and previous Windows installations if present.
3. Empty the Recycle Bin and move large personal files (videos, installers) to an external drive temporarily.
4. Reboot, then check space again — cleanup sometimes needs a restart to release locked files.

### Fix 3: Run the Windows Update troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters** and run **Windows Update**.
2. Apply every fix it offers and reboot when prompted.
3. The troubleshooter repairs service registrations and permissions that are tedious to fix by hand.
4. Try the update once afterward; if it fails with the identical code, the problem is deeper than service state.

### Fix 4: Reset the Windows Update components

1. In an elevated Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the four services with `net start` and check for updates.
4. This gives the update a clean download and a clean job queue — the fix for most repeat failures.

### Fix 5: Repair the OS image with DISM and SFC

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and let it complete fully.
2. Follow with `sfc /scannow` to repair protected system files.
3. Reboot the laptop, then retry KB5035853.
4. Microsoft documents both repair tools on the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official reference.

### Fix 6: Temporarily remove third-party antivirus

1. Uninstall (not just disable) any third-party antivirus trial — disabled suites still load filter drivers.
2. Reboot so Windows Security becomes the active protection.
3. Retry the update with only Microsoft's protection running.
4. Reinstall your preferred antivirus afterward if you wish; the goal is only to test whether its filter was the blocker.

### Fix 7: Install KB5035853 manually from the catalog

1. Find KB5035853 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the x64 package.
2. Close all apps, disconnect any VPN, and run the .msu file.
3. The standalone installer bypasses the Windows Update pipeline and its corrupted state entirely.
4. Reboot and verify the KB in Update history. Manual installation succeeds surprisingly often after the earlier repairs.

### Fix 8: Clean boot, then in-place upgrade repair

1. Run `msconfig`, hide Microsoft services, disable the rest, disable all startup apps, and reboot into a clean boot.
2. Retry the update there to rule out any remaining third-party interference.
3. If it still fails, mount a 24H2 ISO and run setup, choosing **Keep personal files and apps**.
4. The in-place upgrade reinstalls Windows around your data and resolves damage that DISM cannot reach — the same last-resort path used for the [KB5040442 24H2 error](/articles/how-to-fix-kb5040442-update-error-in-windows-11-24h2/).

## Closing

KB5035853 failing on 24H2 is a pipeline problem wearing an update's name: a bad cache, damaged system files, or a third-party filter standing in the way. Read the error code, clear space, reset the components, repair the image, and install manually if the automatic route will not cooperate. The update goes in, and the pipeline you repaired will serve every future update too.

Keep the habits that prevent repeats: maintain 20 GB of free space on C:, let the troubleshooter run before you start hand-editing services, and update your drivers from the manufacturer twice a year. Updates fail far less often on a system whose fundamentals are healthy.
