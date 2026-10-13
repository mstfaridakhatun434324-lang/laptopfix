---
title: "Cumulative Update Won't Install? A Step-by-Step Fix That Works"
slug: how-to-fix-cumulative-update-fails-to-install-step-by-step
date: 2026-10-08
categories: ["windows-update"]
tags: ["cumulative update", "install failed", "patch tuesday", "windows 11", "troubleshooting"]
description: "Cumulative update downloads but won't install? Follow this proven step-by-step sequence — from quick checks to manual installation — and get it done."
thumbnail: "/images/thumbs/how-to-fix-cumulative-update-fails-to-install-step-by-step.webp"
faqs:
  - q: "Why do cumulative updates fail while other updates install fine?"
    a: "Cumulative updates are large, complex packages that touch thousands of system files, so they trip over conditions smaller updates sail past: low disk space, a damaged component store, driver conflicts, or a corrupted download. They're also serviced differently — a single failure rolls back the entire package rather than skipping one piece."
  - q: "Should I keep retrying the failed update?"
    a: "One retry after a reboot is reasonable — transient glitches happen. But if it fails twice with the same behavior, stop retrying and diagnose: repeated identical failures mean a persistent blocker, and each attempt just wastes time and risks compounding the problem."
  - q: "Is it safe to install cumulative updates manually?"
    a: "Yes — the standalone .msu packages from the Microsoft Update Catalog are the exact same files Windows Update downloads, just installed directly. Manual installation is a fully supported path and often succeeds where the automatic pipeline fails, since it skips the download and scan stages entirely."
  - q: "How do I know which KB failed?"
    a: "Go to Settings > Windows Update > Update history and look for the entry marked Failed — the KB number is in the title (e.g., '2026-10 Cumulative Update for Windows 11 ... (KB50XXXXX)'). You'll need that number for the manual download step."
---

The monthly cumulative update is the backbone of Windows security — and when it refuses to install, your laptop sits unpatched while the same update fails, rolls back, and fails again. The pattern is familiar: download completes, install reaches 20% or 90%, then "Something didn't go as planned" and everything undoes itself. Smaller updates install fine, which makes it more confusing.

Here is the thing a technician learns fast: cumulative updates fail for a short list of repeatable reasons, and there is a fixed order for eliminating them. This guide is that order — a checklist refined over hundreds of real repairs. Follow it top to bottom without skipping steps. If your cumulative update fails on every single attempt with no progress at all, our [every-time failure guide](/articles/how-to-fix-cumulative-update-fails-every-time-step-by-step/) digs into the persistent-blocker scenario.

It also helps to know where in the process your update dies, because each phase points at different causes. Fails during download (stuck at a percentage for hours): network, BITS, or cache — Fixes 3 and 4. Fails during install (progress bar moves, then rolls back): space, drivers, AV, or component store — Fixes 2, 5, and 6. Fails instantly with an error code: service or policy problems — check our [update-service guide](/articles/how-to-fix-windows-update-service-not-running-step-by-step/). Match your symptom to the phase before you start, and you'll know which fixes deserve your attention first.

## Why this happens

- **Insufficient disk space**: The update stages gigabytes of files; under ~10 GB free, late-stage failures are common.
- **Corrupt download**: A damaged package fails verification partway through installation.
- **Damaged component store**: WinSxS corruption makes the servicing stack reject the update.
- **Driver conflicts**: Storage, chipset, or third-party filter drivers clash with the files being serviced.
- **Antivirus interference**: Real-time protection quarantining or locking files mid-install.
- **Pending reboot state**: A previous operation left reboot flags that deadlock the installer.
- **Metered connection throttling**: The download never truly completes, leaving a truncated package.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reboot once and retry — the legitimate one-time retry

Transient glitches are real; give it one clean shot.

1. Restart the laptop normally (not shut down — restart, so Fast Startup doesn't preserve state).
2. After boot, wait 5 minutes for startup tasks to settle.
3. Go to **Settings > Windows Update** and click **Check for updates**, then **Retry** on the failed update.
4. If it fails identically a second time, stop retrying — move to Fix 2.

### Fix 2: Free disk space properly

The most common cause and the fastest fix.

1. Open **Settings > System > Storage** and confirm at least **10 GB** free on C:. Aim for 20 GB for feature-adjacent cumulatives.
2. Run **Disk Cleanup** (search Start), click **Clean up system files**, and remove Windows Update Cleanup, temporary files, and delivery optimization files. The Windows Update Cleanup category alone often frees several gigabytes of superseded update files.
3. Empty the Recycle Bin and move large personal files to external storage if needed. Check Downloads and the desktop for forgotten installers and videos — they're the usual space hogs.
4. Retry the update with real headroom. If space immediately fills back up, Storage Sense may be misconfigured — set it to run automatically under **Settings > System > Storage**.

### Fix 3: Run the Windows Update troubleshooter

Microsoft's automated repair catches the easy stuff.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run **Windows Update** and apply every fix it offers.
3. Restart when it finishes, then retry the update.

### Fix 4: Reset the update cache for a clean download

Eliminates the corrupt-payload possibility entirely.

1. In elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` → `catroot2.old`.
3. Restart the three services, then check for updates to pull a completely fresh package.
4. Microsoft documents this cache-reset procedure at the [Windows update support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair the component store with DISM and SFC

When servicing itself is damaged, no package will install.

1. In elevated Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
2. Run `sfc /scannow`, then restart.
3. Retry the cumulative update — a healthy component store accepts packages the damaged one rejected.

### Fix 6: Temporarily remove antivirus interference

Third-party AV is a top-three cause of install-phase failures.

1. Temporarily **uninstall** (not just disable) third-party antivirus — disabled products often leave filter drivers active.
2. Confirm Microsoft Defender is running.
3. Retry the update, then reinstall your AV afterward.

### Fix 7: Install the KB manually from the Update Catalog

The definitive bypass when the automatic pipeline is the problem.

1. Copy the KB number from **Update history**.
2. Download the x64 package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Close all apps, disconnect USB peripherals, and run the `.msu` file.
4. If the manual install works, the package was fine and the automatic path was broken — Fix 4's cache reset usually prevents recurrence.

## Closing

Cumulative update failures feel random but they are not — space, cache, component store, drivers, AV, in that order of likelihood. Work the checklist once and the update installs; work it methodically and you will also know *why* it failed, which means next month's update goes through without drama. Keep 15–20 GB free on C: as a standing habit and half of these failures never happen.

And make the successful install count: after the update completes, restart once more (not shut down — restart), then check Update history to confirm the KB shows as successfully installed rather than merely attempted. A surprising number of "fixed" updates turn out to be pending a final restart. Confirm the success, note which fix worked in case the pattern recurs, and get back to using your laptop — that's the entire point of all this maintenance.
