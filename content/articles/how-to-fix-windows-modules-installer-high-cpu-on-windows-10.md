---
title: "Windows Modules Installer High CPU on Windows 10? Fix It"
slug: how-to-fix-windows-modules-installer-high-cpu-on-windows-10
date: 2026-09-20
categories: ["performance"]
tags: ["windows modules installer", "high cpu", "windows 10", "tiworker", "windows update"]
description: "TiWorker.exe maxing out CPU on Windows 10? Get the servicing engine unstuck with cache clears and store repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-on-windows-10.webp"
faqs:
  - q: "Why is TiWorker.exe always running on my Windows 10 PC?"
    a: "It is not always running — it feels that way because Windows 10's update cadence keeps the servicing queue busy: monthly cumulative updates, periodic .NET and driver payloads, and feature-update staging all flow through TiWorker. On machines that are behind on updates, the queue is longer and TiWorker runs longer catching up. Once fully updated and settled, TiWorker should be quiet for weeks at a time between Patch Tuesdays."
  - q: "Does Windows 10 handle servicing differently from Windows 11?"
    a: "The core engine (TiWorker, TrustedInstaller, WinSxS) is fundamentally the same, and the same repairs apply: cache clears, DISM store repair, manual KB installs. The differences are cosmetic and cadence-related — Windows 10's Settings paths differ slightly (Update & Security instead of Windows Update), and its longer support tail means older machines with weaker hardware feel servicing more. Every fix in this guide is written for Windows 10's exact menus."
  - q: "Can I stop TiWorker by disabling the Windows Update service?"
    a: "Temporarily stopping wuauserv halts new update work, but TiWorker often continues finishing in-flight servicing, and Windows re-enables the service on its own schedule. As a permanent strategy it is self-sabotage: no security patches, growing vulnerability, and eventual forced catch-up servicing that is worse than the steady cadence. Disable the service only as a brief diagnostic to confirm TiWorker is update-driven, then re-enable and fix the underlying stall."
  - q: "How do I know which update is keeping TiWorker busy?"
    a: "Open Settings > Update & Security > Windows Update > View update history and look for failed or pending entries with KB numbers and error codes. Then check Event Viewer > Windows Logs > System for Servicing errors referencing those KBs. The update with the repeated failures is your anchor — search its KB number plus error code, or install it manually from the Microsoft Update Catalog to bypass whatever is wedging the automated path."
---

Windows 10 may be heading for retirement, but its servicing engine works as hard as ever — and TiWorker.exe remains the process most likely to pin your CPU for hours after Patch Tuesday. The mechanics are familiar: updates install, the component store churns, servicing finalizes. When it all flows, TiWorker is loud for a while and then gone. When it wedges — corrupted cache, damaged store, one KB that cannot install — it becomes a permanent resident, and the machine never quite feels right.

This is the Windows 10-specific unwedging guide, with the exact Settings paths and service names for this OS. The diagnostic logic is universal: prove whether the work is progressing or looping, then clear, repair, or bypass the blockage in order. For updates that fail rather than stall, see [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/); for the automated repair route, read [fixing the Windows Update troubleshooter](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/).

## Why this happens

- **Cumulative update installation in progress**: Monthly cumulative updates are large; TiWorker legitimately runs hot installing them.
- **Catch-up servicing on behind machines**: Systems months behind on updates face a long servicing queue that runs for days.
- **Corrupted SoftwareDistribution cache**: Windows 10's download cache corrupts the same way — and loops the same way — as any version's.
- **Damaged component store**: Years of servicing accumulate store damage; old Windows 10 installs are prime candidates.
- **One failing KB in a retry loop**: A single update failing every Patch Tuesday keeps TiWorker spinning monthly.
- **Feature update staging (while supported)**: In-place upgrades stage gigabytes and run extended servicing passes.
- **Low disk space on aging installs**: Years of accumulated updates, logs, and temp files leave little staging room on old C: drives.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the servicing state in Windows 10 terms

Windows 10's UI differs slightly — use its exact paths.

1. **Settings** > **Update & Security** > **Windows Update** — read the status line and check **View update history** for failed KBs.
2. **Task Manager** > **Processes**: note TiWorker.exe CPU and whether disk activity accompanies it.
3. **Event Viewer** > **Windows Logs** > **System** — filter for **Servicing** and **Windows Update** errors with repeating codes.
4. Elevated `dism /Online /Get-Packages | findstr Pending` — quick check for packages stuck mid-install.
5. Moving progress means patience; frozen repetition means intervention — decide before acting.

### Fix 2: Clear the update cache the Windows 10 way

Same cure, Windows 10's service names.

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
3. `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. **Settings** > **Update & Security** > **Windows Update** > **Check for updates** — clean re-scan.
5. Give TiWorker an hour on the fresh cache before judging — first progress is the signal.

### Fix 3: Repair the store with DISM and SFC

Old installs carry old damage. Heal it.

1. Elevated: `DISM /Online /Cleanup-Image /ScanHealth`, then `/RestoreHealth` — allow extra time on older disks.
2. `sfc /scannow` to repair system files against the healed store.
3. Reboot and re-check Windows Update — long-failing updates often clear on the first attempt post-repair.
4. If RestoreHealth stalls sourcing files, mount a Windows 10 ISO and use `/Source` pointing at it.
5. Very old installs with repeated servicing failures are candidates for the in-place upgrade repair — see Fix 7.

### Fix 4: Reclaim C: space on aging installs

Years of Windows 10 accumulate cruft that starves servicing.

1. **Disk Cleanup** > **Clean up system files**: check **Windows Update Cleanup**, **Previous Windows installations**, **Temporary files** — often 10–20 GB on old installs.
2. **Settings** > **System** > **Storage** > **Temporary files** for the modern equivalent pass.
3. Move user data off C: and uninstall long-dead programs (**Settings** > **Apps**, sort by install date for archaeology).
4. Target 15 GB+ free — servicing on Windows 10 wants the same staging room as 11.
5. Re-run Windows Update after the cleanup; space-starved queues frequently drain immediately.

### Fix 5: Install the failing KB manually from the Catalog

Bypass the wedged orchestration for the one stubborn update.

1. Copy the failing KB number from **View update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — match Windows 10 version (22H2 etc.) and architecture.
3. Run the `.msu` standalone with other apps closed.
4. On success, Windows Update picks up the installed KB and TiWorker settles.
5. On identical failure, the error code is now your precise search term — include the KB number in the query.

### Fix 6: Use the Windows 10 troubleshooter and active hours

Containment plus the automated repair, in this OS's locations.

1. **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Windows Update** > **Run the troubleshooter**.
2. Set **Active Hours** (**Windows Update** > **Change active hours**) to protect your workday from servicing restarts.
3. **Advanced options** > **Pause updates** for up to 35 days during critical periods — use deliberately, not permanently.
4. After Patch Tuesday, one plugged-in overnight window with sleep off lets the queue drain uncontested.
5. Unpause and verify 'You're up to date' with a quiet TiWorker as the done state.

### Fix 7: In-place upgrade repair as the final fix

For Windows 10 installs with years of servicing damage, the repair install is the definitive reset.

1. Download the **Windows 10 Media Creation Tool** from Microsoft and create installation media (or mount the ISO).
2. Run `setup.exe` from within Windows and choose **Upgrade this PC now** > **Keep personal files and apps**.
3. The process reinstalls Windows over itself, rebuilding the component store and servicing stack cleanly — allow 1–3 hours.
4. Reinstall any drivers Windows replaced with generics afterward, then run Windows Update to catch up.
5. If even the repair install fails, the hardware (usually storage) is suspect — back up data and test the drive before anything else.

## Closing

TiWorker on Windows 10 is the same honest engine as on 11 — loud while working, silent when done — running on machines that often carry years of servicing history. Clear the cache it chokes on, repair the store it works in, give it staging room, and bypass the one KB it cannot swallow. The monthly servicing storm becomes what it should be: a few loud hours, then quiet.
