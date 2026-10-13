---
title: "Windows Modules Installer High CPU on Acer? Let It Finish Right"
slug: how-to-fix-windows-modules-installer-high-cpu-on-acer-laptop
date: 2026-09-06
categories: ["performance"]
tags: ["windows modules installer", "high cpu", "acer laptop", "tiworker", "windows update"]
description: "TiWorker.exe maxing CPU on your Acer laptop? Understand Windows Modules Installer and get it to finish instead of spinning forever."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-on-acer-laptop.webp"
faqs:
  - q: "What is Windows Modules Installer Worker (TiWorker.exe)?"
    a: "Windows Modules Installer Worker (TiWorker.exe) is the background engine behind Windows Update installations, optional-feature changes, and system component servicing. When updates download or install, TiWorker does the heavy lifting: staging files, resolving dependencies, and committing changes. High CPU from it means update work is actively happening. It is supposed to be temporary — persistent high CPU over days means the work is stuck, not progressing."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "After a cumulative or feature update, several hours of elevated TiWorker activity is normal — it can legitimately run hot for 2–6 hours on slower machines while it processes the update. It should then go quiet until the next update cycle. If TiWorker has held high CPU for more than 24 hours, through reboots, the servicing stack is wedged: a download is corrupted, a component store is damaged, or an update keeps failing and retrying."
  - q: "Can I disable Windows Modules Installer Worker?"
    a: "You can stop the Windows Update and TrustedInstaller services, but this breaks all updating — including security patches — and Windows will eventually restart the work anyway. Disabling servicing is never a real fix; it trades a temporary CPU problem for a permanently unpatched, increasingly unstable system. The correct approach is helping the stuck work complete: clear the update cache, repair the component store, and let the queue drain."
  - q: "Why does TiWorker hit Acer laptops particularly hard?"
    a: "Acer's value-oriented lineup includes many machines with slower eMMC storage, modest dual-core processors, or hard drives — hardware where TiWorker's file operations take far longer than on premium SSD machines. Acer also ships Acer Care Center and quick-access utilities that compete for the same disk I/O. The process is identical on all brands; it simply takes longer and feels worse on entry-level hardware."
---

TiWorker.exe — Windows Modules Installer Worker — is the process that does Windows Update's heavy lifting, and on Acer laptops it has a reputation for doing it loudly: 50, 80, 100 percent CPU for hours, fans screaming, the machine barely usable. Some of that is legitimate — updates are genuinely expensive to install, especially on Acer's entry-level hardware with slower storage. But when TiWorker never finishes, never goes quiet, and survives reboots, the update machinery is stuck, not working.

The fix is helping the stuck work complete, not killing the worker. This guide diagnoses whether TiWorker is progressing or wedged, clears the corrupted caches that wedge it, repairs the component store it depends on, and accounts for Acer's hardware and bundled software. For update failures specifically, see [fixing a broken Windows Update troubleshooter](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/); when updates fail outright, read [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/).

## Why this happens

- **Legitimate post-update servicing in progress**: After updates install, TiWorker spends hours finalizing component changes — normal, temporary, and self-limiting.
- **Corrupted Windows Update download cache**: A damaged download makes TiWorker retry the same failed operation endlessly instead of progressing.
- **Damaged component store (WinSxS)**: The component store TiWorker works against can corrupt, causing every servicing operation to grind or fail.
- **Update stuck in a fail-retry loop**: A failing update retries on every boot, and each attempt costs another round of high TiWorker CPU.
- **Slow eMMC/HDD storage amplifying the work**: Acer's entry-level storage makes TiWorker's thousands of file operations take several times longer.
- **Acer background utilities competing for disk**: Acer Care Center scans and quick-access tools contend for the same disk I/O TiWorker needs.
- **Insufficient free disk space stalling staging**: TiWorker needs gigabytes of scratch space; a nearly-full drive makes servicing crawl or fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether TiWorker is working or wedged

Do not intervene in legitimate work — but do not wait forever on a stuck loop either. Measure first.

1. Open **Task Manager** > **Processes** and note TiWorker.exe's CPU; then check **Settings** > **Windows Update** for the current status message.
2. If Windows Update shows downloading or installing with a moving percentage, TiWorker is working — give it time, plugged in, overnight if needed.
3. If the percentage is frozen for hours or Update shows the same error repeatedly, the work is wedged.
4. Check **Event Viewer** > **Windows Logs** > **System** for repeated **Windows Update** or **Servicing** errors with the same code.
5. Also run `dism /Online /Get-Packages` in an elevated terminal to see if a package is stuck in **Install Pending** state.

### Fix 2: Clear the Windows Update cache

The most common unwedging: delete the corrupted download cache so the update re-downloads cleanly.

1. Open an elevated Command Prompt and run `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old` (do not delete it yet).
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Go to **Settings** > **Windows Update** > **Check for updates** and let it re-scan and re-download from scratch.
5. Monitor TiWorker: a healthy re-download shows progress; if it wedges identically again, the problem is deeper — continue below.

### Fix 3: Repair the component store with DISM

TiWorker works against the WinSxS component store; when the store is damaged, every operation suffers.

1. Open an elevated terminal and run `DISM /Online /Cleanup-Image /ScanHealth` to assess the damage first.
2. If issues are found, run `DISM /Online /Cleanup-Image /RestoreHealth` — this can take 30+ minutes on slower Acer storage; let it finish.
3. Follow with `sfc /scannow` to repair protected system files against the now-healthy store.
4. Reboot, then check Windows Update again — repaired stores often let previously-failing updates sail through.
5. If DISM itself fails, run it with an explicit source or from a Windows install ISO; persistent DISM failure suggests deeper corruption.

### Fix 4: Free disk space for the servicing scratch area

TiWorker stages gigabytes of files; a nearly-full C: drive turns servicing into a crawl or a failure loop.

1. Check free space on C: — servicing wants at least 10–15 GB free, more for feature updates.
2. Run **Settings** > **System** > **Storage** > **Temporary files** and remove update cleanup, delivery optimization files, and the recycle bin contents.
3. Move personal files (videos, downloads) off C: to another drive or external storage.
4. Uninstall large unused apps and games from **Settings** > **Apps** — Acer's bundled trials are prime candidates.
5. Retry Windows Update after freeing space; watch TiWorker complete work that previously stalled. Microsoft's guidance on update disk requirements is at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Pause Acer's background utilities during servicing

Acer Care Center scans and update agents fighting TiWorker for disk I/O stretch a 2-hour job into an 8-hour one.

1. Open **Acer Care Center** > **Settings** and disable or reschedule automatic tune-ups and checkups away from update windows.
2. Check **Acer Quick Access** and similar utilities for background polling features you do not use, and turn them off.
3. In **Task Manager** > **Startup apps**, disable Acer utilities you never open manually.
4. Let one full update cycle complete with the utilities quiet — measure whether TiWorker finishes faster.
5. Re-enable sensible schedules afterward; the goal is sequencing, not permanent removal.

### Fix 6: Install the specific failing update manually

When one KB keeps failing through Windows Update, the standalone installer often succeeds where the orchestrated path fails.

1. Identify the failing KB number from **Settings** > **Windows Update** > **Update history** (failed entries).
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the build matching your system (x64, Windows 11).
3. Run the `.msu` installer manually with nothing else running — standalone installs bypass the download-cache machinery entirely.
4. If it succeeds, Windows Update will detect the installed KB and move on; TiWorker should quiet down within the hour.
5. If the manual install also fails with the same code, search that exact error code — it now names the real problem.

### Fix 7: Reset Windows Update components as the final repair

When caches, store repairs, and manual installs all fail, reset the entire update subsystem to a known-good state.

1. Run the official **Windows Update Troubleshooter**: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. If that fails, use the manual reset: stop wuauserv, bits, cryptsvc, and msiserver, then rename SoftwareDistribution and catroot2 folders.
3. Re-register the update DLLs only if you are comfortable with the command-line procedure from Microsoft's documentation.
4. Reboot and check for updates fresh — the first scan after a reset takes longer; let it complete.
5. If TiWorker still spins after a full reset, consider an in-place upgrade repair install (keeps files and apps) as the final software-level fix.

## Closing

TiWorker.exe at high CPU is Windows Update doing its job — until it is not, and the difference is whether the work ever finishes. On Acer hardware, where slower storage stretches every servicing job, patience plus the cache-clear and DISM repairs above resolve the vast majority of stuck cases. Help the worker finish its shift instead of firing it, and the fans finally get to rest.
