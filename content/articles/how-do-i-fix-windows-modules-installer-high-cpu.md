---
title: "How Do I Fix Windows Modules Installer High CPU?"
slug: how-do-i-fix-windows-modules-installer-high-cpu
date: 2026-10-04
categories: ["performance"]
tags: ["windows modules installer", "tiworker", "high cpu", "windows update"]
description: "Windows Modules Installer Worker (TiWorker.exe) maxing your CPU? Learn when to let it finish, how to unstick failed updates, and how to calm it down."
thumbnail: "/images/thumbs/how-do-i-fix-windows-modules-installer-high-cpu.webp"
faqs:
  - q: "What is Windows Modules Installer Worker?"
    a: "Windows Modules Installer Worker (TiWorker.exe) is the process that installs, modifies, and removes Windows updates and optional components. When Windows Update downloads patches, TiWorker does the actual installation work — expanding packages, replacing system files, and cleaning up. High CPU from TiWorker almost always means updates are actively installing, which is legitimate, if inconvenient, work."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "For a normal monthly cumulative update, 15-45 minutes of elevated CPU is typical; for a feature update, one to several hours. It should drop back to zero when done. If TiWorker has been at high CPU for many hours across multiple days — or returns to high CPU immediately after every reboot — an update is stuck or corrupted, and the fixes below (troubleshooter, SoftwareDistribution reset) will unstick it."
  - q: "Can I end TiWorker.exe in Task Manager?"
    a: "You can, but it's counterproductive — Windows will restart it and the update resumes from scratch, so you lose progress and extend the total time. The only scenario where ending it helps is a genuinely wedged update that never progresses; even then, the proper fix is resetting the update cache (Fix 3), not killing the process. Let legitimate installs finish."
  - q: "Why does TiWorker run at high CPU right after I turn on my laptop?"
    a: "Windows schedules update installation and post-update cleanup (including the WinSxS component-store cleanup) around boot and idle time. If updates downloaded overnight or a previous install didn't complete, TiWorker picks up at startup. This is by design — the system is finishing maintenance. Frequent occurrences mean updates keep failing to complete, which points to the stuck-update fixes below."
---

`Windows Modules Installer Worker` — `TiWorker.exe` — at 40%, 60%, even 80% CPU is one of the most-googled Windows complaints, and the answer is usually boring: it's installing updates. TiWorker is the engine that applies Windows updates and manages optional features, and update installation is genuinely CPU-intensive work. The real question isn't "what is it" but "is it making progress or stuck?" — because a TiWorker that's working will finish and vanish, while a stuck one will torment you for days. Here's how to tell the difference and fix the stuck kind. For the related Service Host update container, see [Service Host high CPU](/articles/how-to-fix-service-host-high-cpu-on-asus-laptop/); for the 24H2-specific TiWorker variant, see [TiWorker high CPU in 24H2](/articles/how-to-fix-tiworker-high-cpu-in-windows-11-24h2/).

## Why this happens

- **Legitimate update installation**: Monthly cumulative or feature updates being applied — heavy but temporary.
- **Post-update component cleanup**: WinSxS cleanup and update finalization after a reboot.
- **A stuck or corrupted update**: A failed download or broken package retried endlessly.
- **Corrupt SoftwareDistribution cache**: Damaged update metadata causing re-scan loops.
- **Optional features installing**: Language packs, .NET features, or RSAT tools installing in the background.
- **Interrupted updates**: Shutdowns mid-install leaving the worker in a resume loop.
- **Failing disk slowing installs**: Update I/O on a dying drive stretches a 30-minute job into hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it's working or stuck

This distinction decides everything else.

1. Open **Settings** > **Windows Update** and read the status: "Downloading," "Installing," or a percentage = working; no status but high TiWorker = possibly stuck.
2. Open **Task Manager** > **Details**, find **TiWorker.exe**, and watch CPU over 30 minutes: gradually declining = progressing; flat at high CPU for hours = stuck.
3. Check disk activity alongside: working TiWorker shows heavy disk writes (it's replacing system files); stuck TiWorker often shows high CPU with little disk activity (spinning, not progressing).
4. Look at **C:\Windows\Logs\CBS\CBS.log** (the component servicing log) — recent timestamps with progress entries = working; repeating identical errors = stuck.
5. If it's working, the correct fix is patience: let it finish, preferably plugged in and undisturbed. Only proceed if it's genuinely stuck.

### Fix 2: Run the Windows Update troubleshooter

The automated first pass for stuck updates.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Let it complete — it resets update service registrations, clears pending states, and restarts the update components.
3. Reboot when prompted, then check **Settings** > **Windows Update** > **Check for updates**.
4. Monitor TiWorker for an hour: the troubleshooter resolves simple stuck states, and you'll see it either complete the update or idle at zero.
5. If the troubleshooter reports problems it couldn't fix, note the details — they usually point at the cache corruption Fix 3 addresses.

### Fix 3: Reset the SoftwareDistribution cache

Clears the corrupted metadata behind most stuck TiWorkers.

1. Open an **elevated Command Prompt** and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Go to **Settings** > **Windows Update** > **Check for updates** — Windows rebuilds fresh metadata and re-downloads what's needed.
5. This is safe: the `.old` folders are just caches; Windows recreates them. Delete the `.old` folders after a week of stable updates.

### Fix 4: Repair the component store with DISM

When the corruption is deeper than the download cache.

1. Open an **elevated Command Prompt** and run: `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store TiWorker installs from.
2. This takes 15–30 minutes and legitimately uses CPU itself — let it finish uninterrupted.
3. Follow with `sfc /scannow` to repair protected system files from the now-healthy store.
4. Reboot, then check Windows Update again — with a healthy store, previously failing updates usually install cleanly.
5. If DISM fails with source errors, provide an install source: mount the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) and run DISM with `/Source:` pointing at its `install.wim`.

### Fix 5: Manage active hours and update scheduling

Keep TiWorker from ambushing your workday.

1. Go to **Settings** > **Windows Update** > **Advanced options** > **Active hours** — set them to cover your actual workday so restarts and heavy install phases avoid those hours.
2. On Windows 11 Pro, use Group Policy (`gpedit.msc` > Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage end user experience) to configure **deadline and notification** behavior.
3. Pause updates strategically: **Settings** > **Windows Update** > **Pause updates** for 1–5 weeks when you have a critical deadline — but don't leave them paused indefinitely.
4. For metered connections, enable **"Download updates over metered connections"** = off so big updates wait for unmetered Wi-Fi.
5. Schedule a weekly maintenance window: let the laptop sit plugged in and idle for an hour so TiWorker completes its work without competing with you. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents active-hours configuration.

### Fix 6: Check the disk and consider a manual update

When the hardware or a specific KB is the blocker.

1. Run `chkdsk C: /scan` from an elevated prompt — update installs on a failing drive stall and stretch; S.M.A.R.T. warnings mean the drive, not the updater, is the problem.
2. Ensure 20GB+ free on C: — feature updates need substantial scratch space; cramped drives cause install loops.
3. If one specific KB keeps failing, hide it or install it manually: download it from the [Update Catalog](https://www.catalog.update.microsoft.com/) and run the standalone installer, which often succeeds where Windows Update fails.
4. Check **Update history** (Settings > Windows Update > Update history) for the failing KB's error code (e.g., 0x800f0922, 0x80073701) — searching the code focuses the fix.
5. As a final measure, an **in-place upgrade** with the Windows 11 ISO refreshes the entire servicing stack — the definitive cure for a TiWorker that survives everything else.

## Closing

TiWorker high CPU is usually just Windows doing maintenance — the fix is letting it finish. When it doesn't finish, it's a stuck update: troubleshooter first, SoftwareDistribution reset second, DISM third. Work that sequence and the Modules Installer goes back to being a background process you never notice.
