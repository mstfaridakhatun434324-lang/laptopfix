---
title: "Windows Modules Installer High CPU on ASUS? Unstick Updates"
slug: how-to-fix-windows-modules-installer-high-cpu-on-asus-laptop
date: 2026-09-13
categories: ["performance"]
tags: ["windows modules installer", "high cpu", "asus laptop", "tiworker", "windows update"]
description: "TiWorker.exe grinding on your ASUS laptop? Fix the stuck Windows Modules Installer Worker and get servicing finished."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "What is TiWorker.exe doing on my ASUS laptop?"
    a: "TiWorker.exe (Windows Modules Installer Worker) installs Windows updates, manages optional features, and services system components — staging files, resolving dependencies in the component store, and committing changes. High CPU means update work is actively running. On ASUS machines the job is identical to other brands, but ASUS's own updaters (MyASUS, Armoury Crate driver updates) can trigger parallel servicing that contends for the same resources and stretches the work out."
  - q: "How long is too long for Windows Modules Installer to run?"
    a: "After a cumulative update, 1–4 hours of elevated TiWorker activity is normal; after a feature update, it can legitimately run for much of a day on slower machines. The line is crossed when high CPU persists beyond 24 hours, survives multiple reboots unchanged, or pairs with Windows Update showing the same error repeatedly. That pattern means the work is looping, not progressing — usually a corrupted download cache or damaged component store."
  - q: "Can Armoury Crate interfere with Windows Update servicing?"
    a: "Indirectly, yes. Armoury Crate periodically checks for and installs driver updates, and those installations trigger the same servicing subsystem (TiWorker) that Windows Update uses. When both run concurrently, they contend for servicing locks and disk I/O, which slows both and occasionally wedges one. Staggering them — Windows Update fully complete before allowing Armoury Crate driver updates — avoids the collision."
  - q: "Is it safe to end TiWorker.exe in Task Manager?"
    a: "Ending it provides minutes of relief at most — the servicing subsystem restarts the work, often from scratch, which can make the total job longer. Worse, killing TiWorker mid-commit can corrupt the component store it was writing to, turning a slow update into a broken one. Never end it as a fix. The correct moves are clearing its corrupted inputs (update cache), repairing its workplace (component store), or giving legitimate work an uncontested window to finish."
---

TiWorker.exe has a talent for picking the worst moments: you open your ASUS laptop to get work done, and Windows Modules Installer Worker is consuming the CPU like it is compiling an operating system — which, in a sense, it is. Servicing updates is genuinely heavy work. But on ASUS machines the job often drags far beyond reason, because ASUS's own driver updaters pile parallel servicing work onto the same engine Windows Update is already driving, and the two end up wrestling instead of working.

Untangling it means sequencing the updaters, verifying the work is actually progressing, and repairing the two things that wedge it most: the download cache and the component store. This guide is tuned for the ASUS software stack but the servicing mechanics are universal. For updates that fail outright rather than stall, see [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/); when driver updates specifically misbehave, read [driver updates keep failing in Windows Update](/articles/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2/).

## Why this happens

- **Legitimate servicing after updates**: Post-update finalization genuinely keeps TiWorker hot for hours — the most common and most benign cause.
- **ASUS updaters colliding with Windows Update**: MyASUS and Armoury Crate driver installs trigger parallel servicing that contends for locks and disk.
- **Corrupted update download cache**: Damaged payloads make TiWorker retry the same failed operation endlessly.
- **Damaged component store**: Corruption in WinSxS makes every servicing operation grind or fail outright.
- **One failing update in a retry loop**: A single bad KB retries every boot, each attempt costing another high-CPU round.
- **Slow storage stretching file operations**: TiWorker's small-file workload is brutal on HDDs and entry-level eMMC still found in budget ASUS models.
- **Cramped C: drive starving staging**: Servicing needs gigabytes of scratch space; near-full drives stall the work mid-flight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify progress versus looping

Do not touch a working engine; do intervene in a looping one. Tell them apart first.

1. Open **Settings** > **Windows Update** — a moving percentage or changing status text means genuine progress.
2. Open **Event Viewer** > **Windows Logs** > **System** and look for repeating **Servicing** errors with identical codes — repetition is the loop signature.
3. In **Task Manager**, pair TiWorker's CPU with disk activity: heavy disk means working, high CPU with idle disk means wedged.
4. Run `dism /Online /Get-Packages` elevated and check for packages stuck in **Install Pending** across reboots.
5. If progress is real, jump to Fix 5 for sequencing and let it finish — interrupting real work only restarts it.

### Fix 2: Sequence ASUS updaters after Windows Update

Stop the servicing pile-up at its source.

1. Open **MyASUS** and **Armoury Crate** and pause any pending driver or firmware updates.
2. Let **Windows Update** run to full completion first — install everything, reboot as prompted, until it reports up to date and TiWorker goes quiet.
3. Only then allow MyASUS/Armoury Crate to install their driver updates, one at a time.
4. In Armoury Crate settings, disable automatic driver updates so they never ambush a Windows Update session again.
5. Going forward: Windows Update first, ASUS updaters second, never together.

### Fix 3: Clear the corrupted update cache

The most common unwedge for a looping TiWorker.

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
3. Restart the services with `net start` for each.
4. **Settings** > **Windows Update** > **Check for updates** and let it re-download from a clean cache.
5. Watch TiWorker for an hour: fresh progress means the cache was the culprit.

### Fix 4: Repair the component store with DISM

When the store TiWorker works in is damaged, every job suffers.

1. Elevated terminal: `DISM /Online /Cleanup-Image /ScanHealth` to assess damage.
2. `DISM /Online /Cleanup-Image /RestoreHealth` to repair — budget 30+ minutes on slower storage.
3. Follow with `sfc /scannow` to fix system files against the repaired store.
4. Reboot and re-run Windows Update — healed stores routinely let queued updates complete on the first try.
5. If RestoreHealth cannot fetch files, point it at a Windows ISO with `/Source`. Microsoft documents the servicing tools at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Install the stubborn KB manually

When one update keeps failing through the orchestrated path, sidestep the orchestration.

1. Find the failing KB number in **Settings** > **Windows Update** > **Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), matching your architecture and Windows build.
3. Run the `.msu` with everything else closed — standalone installs skip the download-cache machinery entirely.
4. On success, Windows Update recognizes the installed KB and the queue drains; TiWorker should settle within the hour.
5. On failure with the same code, that code now identifies the real fault — search it verbatim.

### Fix 6: Free staging space and quiet background contenders

Give servicing the disk room and the uncontested I/O it needs.

1. Ensure 10–15 GB free on C: via **Settings** > **System** > **Storage** > **Temporary files** cleanup.
2. Pause OneDrive syncing, Steam downloads, and Armoury Crate background tasks during servicing windows.
3. On HDD-equipped models, schedule major updates overnight with sleep disabled — uncontested hours beat fragmented daytime minutes.
4. Consider the long-term fix: an SSD upgrade turns TiWorker from an hours-long ordeal into a background blip.
5. After each fix attempt, always re-check Windows Update status before declaring victory — quiet TiWorker plus 'up to date' is the done state.

### Fix 7: Reset the update subsystem as the final repair

When caches, repairs, and manual installs all fail, reset the machinery itself.

1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. If that fails, manual reset: stop wuauserv, bits, cryptsvc, msiserver; rename SoftwareDistribution and catroot2; restart services.
3. Reboot and allow the first post-reset scan to complete fully — it is slower than usual; do not interrupt it.
4. If TiWorker still loops, do an in-place upgrade repair install (keeps files and apps) as the last software-level option.
5. Beyond that, suspect storage hardware — run your SSD/HDD maker's diagnostic before assuming Windows is at fault.

## Closing

TiWorker.exe at full tilt on an ASUS laptop is usually two update systems tripping over each other, plus the occasional corrupted cache or damaged store underneath. Sequence Windows Update before ASUS updaters, clear what is corrupted, repair what is damaged, and the servicing engine finishes its work and clocks out. The fans go quiet, the machine comes back, and updates become background noise again — which is all they were ever supposed to be.
