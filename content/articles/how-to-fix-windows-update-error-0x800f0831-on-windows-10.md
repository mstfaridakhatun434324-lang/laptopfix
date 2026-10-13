---
title: "Fix Windows Update Error 0x800F0831 on Windows 10: Missing Update Fixed"
slug: how-to-fix-windows-update-error-0x800f0831-on-windows-10
date: 2026-09-06
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x800f0831", "servicing stack", "prerequisite"]
description: "Error 0x800F0831 on Windows 10 means a prerequisite update is missing. Install the missing SSU and repair the chain with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0831-on-windows-10.webp"
faqs:
  - q: "What does 0x800F0831 mean on Windows 10?"
    a: "It means a required prerequisite update is missing — usually the servicing stack update for your Windows 10 version. The update you want cannot install until its dependency is in place. Long update pauses and silently failed servicing stack updates are the typical causes."
  - q: "Which update is usually the missing one?"
    a: "The servicing stack update (SSU) for your specific Windows 10 version (such as 22H2). Cumulative updates declare a minimum SSU version as a prerequisite, and if yours is older or missing, the install fails with 0x800F0831. Check your version in Settings > System > About first."
  - q: "Can Windows 10 install the missing update automatically once I fix things?"
    a: "The servicing stack update (SSU) for your specific Windows 10 version is the usual missing piece — cumulative updates declare a minimum SSU version as a prerequisite. If yours is older or missing, the install fails. Check your version in Settings > System > About, then install the matching SSU manually from the Update Catalog."
  - q: "What if the SSU itself fails to install?"
    a: "Then the servicing layer is likely corrupted. Reset the update cache, run DISM and SFC, and retry the SSU. If it still fails, an in-place upgrade repair install rebuilds the entire servicing stack and resolves it — the nuclear option that preserves your files and applications while replacing every servicing component."
---

On Windows 10, error 0x800F0831 has the same meaning as elsewhere: a prerequisite update is missing from the chain. Windows 10's long servicing history makes this especially common — machines that sat with updates paused, or that had a servicing stack update fail quietly months ago, develop gaps that newer cumulative updates refuse to jump over. The installer is protecting you from an untested configuration; your job is to fill the gap.

Windows 10 versions matter here more than on Windows 11, because SSUs are version-specific (21H2, 22H2, and so on). Always confirm your exact version before downloading anything manually. Work the steps below in order, installing missing pieces oldest-first.

## Why this happens

- **Missing version-specific SSU:** The servicing stack update for your Windows 10 build was never installed.
- **Silently failed SSU:** A previous SSU reported success but did not complete, leaving the chain broken.
- **Extended update pauses:** Long pauses create prerequisite gaps no single update can bridge.
- **Hidden updates:** Manually or tool-hidden updates removed required chain links.
- **Corrupted servicing records:** Installed prerequisites whose records are damaged appear missing to the installer.
- **Out-of-sequence manual installs:** Installing cumulative updates manually without their SSUs.
- **Cache metadata corruption:** Damaged SoftwareDistribution metadata miscalculates prerequisites.
- **Component store damage:** WinSxS corruption hiding legitimately installed updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your Windows 10 version, then install the SSU manually

Version accuracy is everything for SSUs on Windows 10.

1. Go to **Settings > System > About** and note the **Version** (e.g., 22H2) and **System type** (x64).
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for the latest servicing stack update for that exact version.
3. Download and install the `.msu`, then restart.
4. Check for updates — the blocked update typically proceeds now.

### Fix 2: Audit update history for the gap

Read the history like a ledger and find the missing entry.

1. Open **Settings > Update & Security > Windows Update > View update history**.
2. Scan for failed updates, particularly servicing stack or older cumulative updates.
3. Write down the KB numbers of anything failed or conspicuously absent.
4. Install them manually from the Update Catalog in chronological order, restarting after each.

### Fix 3: Reveal hidden updates

Check whether a required update is hiding.

1. Run the **Show or hide updates** troubleshooter and choose **Show hidden updates**.
2. Unhide any Windows updates in the list.
3. Run **Check for updates** and install everything in the presented order.

### Fix 4: Reset the update cache

Clear metadata that may be miscalculating prerequisites.

1. Open **Command Prompt (Admin)**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and check for updates.

### Fix 5: Repair servicing with DISM and SFC

Make installed prerequisites visible again by repairing servicing data.

1. In **Command Prompt (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Restart and retry. The same servicing repair resolves [0x800F0922 errors](/articles/how-to-fix-windows-update-error-0x800f0922-on-windows-10/) on Windows 10.

### Fix 6: Manually install the blocked update after the SSU

Once the servicing stack is current, install the target update directly to skip queue issues.

1. Get the failing update's KB number from update history.
2. Download the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the `.msu` and restart when prompted.
4. Confirm success in update history.

### Fix 7: In-place upgrade for an unrecoverable chain

When the chain has too many gaps — years of pauses, multiple failed SSUs — reinstall Windows 10 over itself with an official ISO, choosing **Keep personal files and apps**. This establishes a clean, current update baseline in one operation. Afterward, avoid long update pauses; steady monthly updates keep the prerequisite chain intact, as described on the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows).

Windows 10's servicing stack updates are version-specific in a way that trips people up. An SSU for 21H2 will not satisfy a 22H2 cumulative update's prerequisite check, and the Update Catalog lists SSUs for every supported version side by side — downloading the wrong one is easy. Always start from Settings > System > About, confirm the exact version, and match it precisely. If your machine is on an older build, consider that the deeper fix may be updating to the latest build itself, since older builds accumulate stranger prerequisite tangles. Second, make the update-history audit a habit, not a one-time event: after every Patch Tuesday, glance at the history for anything failed or missing, and fill gaps while they are small. A one-month gap is a five-minute manual install; a six-month gap is the afternoon-long archaeology project this guide describes. Third, resist tools that promise to take control of Windows 10 updates by hiding or blocking them — they create exactly the prerequisite holes that surface as 0x800F0831 months later. The [Windows 11 version of this guide](/articles/how-to-fix-windows-update-error-0x800f0831-on-windows-11/) follows the same logic for the newer OS. Steady, automatic, unhidden updates are the whole prevention program.

If you are managing updates across several family or office laptops, standardize the approach: leave Windows Update on automatic, check the history monthly, and install any failed SSU the same week it fails. The machines that generate 0x800F0831 are almost always the ones where updates were paused temporarily six months ago and never resumed. A calendar reminder on Patch Tuesday — the second Tuesday of each month — takes thirty seconds per machine and prevents the entire category of missing-prerequisite errors.

## Closing

Windows 10's 0x800F0831 is a bookkeeping error with a bookkeeping fix: identify your version, install the missing servicing stack update, fill any other gaps oldest-first, and repair servicing data if installed updates are not being recognized. Keep the chain continuous afterward — regular monthly updates are the simplest prevention — and the missing-prerequisite error will not return.
