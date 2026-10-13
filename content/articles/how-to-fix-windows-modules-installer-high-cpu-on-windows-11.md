---
title: "Windows Modules Installer High CPU on Windows 11? Fix It"
slug: how-to-fix-windows-modules-installer-high-cpu-on-windows-11
date: 2026-09-19
categories: ["performance"]
tags: ["windows modules installer", "high cpu", "windows 11", "tiworker", "servicing"]
description: "TiWorker.exe stuck at high CPU on Windows 11? Diagnose the servicing stall and get updates completing again."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-on-windows-11.webp"
faqs:
  - q: "Is Windows Modules Installer Worker supposed to use 100% CPU?"
    a: "Briefly, yes — TiWorker is a heavyweight by design, and during active update installation it can saturate a CPU core or more. That is normal and temporary. What is not normal is sustained high CPU for days, high CPU when Windows Update reports no activity, or the same update failing repeatedly with TiWorker spinning each time. Intensity is fine; endlessness is the problem. Judge TiWorker by whether its work completes, not by how loud it is while working."
  - q: "What's the difference between TiWorker.exe and TrustedInstaller.exe?"
    a: "They are two faces of the same servicing system: TrustedInstaller.exe is the Windows Modules Installer service (the privileged identity that owns system files), and TiWorker.exe (Windows Modules Installer Worker) is the worker process that does the actual installation labor under that identity. In Task Manager you will usually see TiWorker consuming the CPU during updates. Fixing one means fixing the servicing pipeline both belong to — the cache-clear and DISM repairs in this guide cover both."
  - q: "Why does TiWorker run even when I'm not installing updates?"
    a: "Windows performs background servicing constantly: installing small cumulative payloads, managing optional features, cleaning superseded components, and preparing staged updates. Much of this is invisible — Windows Update may show 'You're up to date' while servicing finalizes work from the last patch. TiWorker also runs when you add/remove Windows features or install certain drivers. Background servicing is normal; background servicing that never ends is the fault condition."
  - q: "Can I schedule TiWorker to only run at night?"
    a: "You cannot schedule TiWorker directly, but you can shape when its work happens: set Active Hours to cover your day so restarts and intensive servicing avoid it, pause updates during critical work weeks, and leave the machine plugged in overnight after Patch Tuesday so queued servicing completes uncontested. These controls do not micromanage TiWorker, but they reliably move its heavy lifting out of your working hours."
---

TiWorker.exe does not do subtle. When Windows Modules Installer Worker gets going, it takes the CPU it needs — sometimes all of it — and your laptop becomes a very expensive space heater for the duration. Usually the duration is reasonable: updates install, servicing finalizes, and within hours the machine is quiet again. But when the hours become days, when reboots change nothing, when Task Manager shows TiWorker grinding with no update in sight — the servicing engine is stuck, and stuck servicing needs intervention.

This is the general Windows 11 guide to unwedging it: telling real work from a loop, clearing the corrupted caches, repairing the component store, and resetting the subsystem when gentler measures fail. Brand-specific wrinkles (Dell, Acer, ASUS) have their own guides; the mechanics here apply to every Windows 11 machine. For updates that fail rather than stall, see [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/); for a broken updater UI, read [fixing the Windows Update troubleshooter](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/).

## Why this happens

- **Active update installation in progress**: TiWorker legitimately saturates CPU while installing updates — heavy, temporary, and self-limiting.
- **Post-update servicing finalization**: After reboots, TiWorker spends hours committing component changes — normal aftermath, not a fault.
- **Corrupted SoftwareDistribution cache**: Damaged downloads trap TiWorker in a retry loop that never progresses.
- **Damaged WinSxS component store**: The store TiWorker operates on can corrupt, making every servicing job grind or fail.
- **Failing update retrying endlessly**: One bad KB retries every boot; each attempt costs another high-CPU servicing round.
- **Optional-features changes triggering servicing**: Adding or removing Windows features launches full servicing passes many users do not connect to TiWorker.
- **Insufficient disk space for staging**: Servicing stages gigabytes of files; a cramped C: drive stalls the work mid-flight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the servicing state before acting

Distinguish the three states: working, finalizing, and looped. Each gets a different response.

1. **Settings** > **Windows Update**: note the exact status — downloading, installing with a percentage, pending restart, or up to date.
2. **Task Manager**: pair TiWorker's CPU with disk I/O — heavy disk means real work; high CPU with idle disk suggests a wedge.
3. **Event Viewer** > **Windows Logs** > **System**: filter for **Servicing** events — repeating identical errors are the loop signature.
4. Elevated `dism /Online /Get-Packages` — packages stuck in **Install Pending** across reboots confirm the stall.
5. If the state is 'installing with moving progress', stop here and let it finish — everything below is for stuck states.

### Fix 2: Clear the update download cache

The highest-probability unwedge for a looping worker.

1. Elevated Command Prompt: `net stop wuauserv` + `net stop bits` + `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old` (keep the old folder until success is confirmed).
3. `net start` each service again.
4. **Settings** > **Windows Update** > **Check for updates** — clean re-scan and re-download.
5. Observe TiWorker for an hour: genuine progress now means the cache was the entire problem.

### Fix 3: Repair the component store

When the workplace is damaged, every job fails. Fix the workplace.

1. Elevated: `DISM /Online /Cleanup-Image /ScanHealth` — assess before treating.
2. `DISM /Online /Cleanup-Image /RestoreHealth` — the actual repair; allow up to an hour on slow disks.
3. `sfc /scannow` afterward to fix system files against the healed store.
4. Reboot, then check Windows Update — a repaired store typically drains the queued work on its own.
5. If RestoreHealth fails to source files, provide a Windows ISO via `/Source` and retry.

### Fix 4: Free staging space on C:

Servicing cannot complete without room to work.

1. Verify at least 10–15 GB free on C: — below that, TiWorker stalls are expected, not mysterious.
2. **Settings** > **System** > **Storage** > **Temporary files**: clear update cleanup, delivery optimization files, thumbnails, recycle bin.
3. Move personal large files off C: — the drive is for system and apps, not your video archive.
4. Uninstall unused large apps (**Settings** > **Apps**, sort by size).
5. Retry the update cycle after freeing space — space-starved servicing often completes immediately.

### Fix 5: Install the failing update from the Catalog

When one KB defeats the orchestrated path, go around it.

1. Identify the failing KB in **Update history** (failed entries with error codes).
2. Fetch it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — match architecture and build.
3. Run the `.msu` standalone with nothing else running — this bypasses the download and orchestration layers.
4. Success: Windows Update detects the KB and moves on; TiWorker quiets within the hour.
5. Failure with the same code: the code now names the true fault — search it exactly, quotes included.

### Fix 6: Contain the blast radius: active hours and pausing

While fixing the stall, keep servicing out of your workday.

1. **Settings** > **Windows Update** > **Advanced options** > **Active Hours** — cover your full working day.
2. **Pause updates** for a week during critical deadlines — a controlled pause beats a surprise servicing storm.
3. After Patch Tuesday, give the machine one plugged-in overnight window with sleep disabled to drain the queue.
4. Do not pause indefinitely — the goal is scheduling control, not update avoidance.
5. Once the stall is fixed, unpause and let the normal cadence resume.

### Fix 7: Reset Windows Update components

The full subsystem reset for stalls that survive everything above.

1. First try the automated route: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Manual reset if needed: stop wuauserv, bits, cryptsvc, msiserver; rename SoftwareDistribution and catroot2; restart all four.
3. Reboot and let the first scan complete without interruption — it is slower than normal.
4. If TiWorker still loops post-reset, run an in-place upgrade repair install (keeps files, apps, and settings).
5. Persistent failure beyond that implicates storage hardware — check drive health with the manufacturer's diagnostic.

## Closing

Windows Modules Installer Worker is the sound of Windows maintaining itself — loud, temporary, and usually honest work. When the work never ends, the cause is corrupted inputs, a damaged workplace, or one update that cannot succeed, and each has a direct repair. Clear the cache, heal the store, free the space, and the engine finishes its shift. Servicing storms pass; the skill is knowing when to wait one out and when to intervene.
