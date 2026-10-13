---
title: "How to Fix TiWorker.exe High CPU Usage During Windows Update on Windows 10"
slug: "how-to-fix-tiworker-exe-high-cpu-windows-update-on-windows-10"
date: 2026-09-27
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows modules installer", "windows 10", "windows update"]
description: "TiWorker.exe eating your CPU on Windows 10? Learn the 60-minute rule for legitimate update work, then fix stuck installer loops with cache resets and servicing repairs."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-on-windows-10.webp"
faqs:
  - q: "Is TiWorker.exe high CPU worse on Windows 10 than Windows 11?"
    a: "Often, yes, in practice. Windows 10 machines are typically older — slower CPUs, mechanical hard drives, less RAM — so the same installer workload takes longer and is more visible. The process itself is identical (Windows Modules Installer Worker), but on a 7-year-old laptop with an HDD, post-update work that takes 20 minutes on a modern machine can take 2 hours. The fixes are the same; the patience required is greater."
  - q: "Can TiWorker.exe high CPU mean my Windows 10 is infected?"
    a: "Extremely unlikely. The genuine TiWorker.exe is a signed Microsoft process in C:\\Windows\\WinSxS doing update work. Malware mimicking system process names is real but rare, and it would not correlate with Windows Update activity. If Task Manager shows high CPU from TiWorker right after Patch Tuesday or after you checked for updates, it is legitimate work. Verify the file location and digital signature if you want certainty."
  - q: "Why does TiWorker.exe run for hours on my old Windows 10 laptop?"
    a: "Three compounding factors: a backlog of months of updates creating a huge component queue, a mechanical hard drive making every file operation slow, and possibly a corrupted cache causing retries. Old laptops that update infrequently get hit hardest — the worker has to process an enormous backlog on slow hardware. Letting updates install monthly prevents the mega-backlog that causes marathon sessions."
  - q: "Should I end TiWorker.exe in Task Manager?"
    a: "No. Ending it mid-task risks corrupting the component store, which turns a slow update session into a broken servicing stack requiring DISM repair. If it is genuinely stuck (hours of high CPU, no update activity, survives restarts), use the fixes below — restart the update services and clear the cache — which stop the work cleanly instead of killing it mid-write."
---
On Windows 10, TiWorker.exe high CPU is a familiar sight on aging laptops: the fan roars, everything slows to a crawl, and Task Manager blames the Windows Modules Installer Worker. The process is legitimate — it is Windows Update's file-work engine — but on older hardware its normal workload is heavy enough to look like a malfunction. Telling 'old laptop doing updates' apart from 'stuck installer loop' is the entire game here.

Windows 10 adds specific wrinkles. Many of these machines still run on spinning hard drives, where the worker's file operations take an order of magnitude longer. Infrequent updaters accumulate enormous component backlogs. And the Windows 10 servicing stack, while mature, carries years of potential corruption on machines that have been through dozens of update cycles. The triage below accounts for all of it.

Start with the 60-minute rule in Fix 1 — on Windows 10 with an HDD, extend it to two hours before declaring a problem. If you have already confirmed the worker is stuck, skip ahead to Fix 3. For the Windows 11 version of this problem, see our [TiWorker high CPU guide for Windows 11](/articles/how-to-fix-tiworker-exe-high-cpu-windows-update-on-windows-11/).

## Why this happens

- **Post-update work on slow hardware** — The same component finalization that takes 20 minutes on an SSD can take 2 hours on an old HDD — legitimate work, just slow.

- **Mega-backlog from infrequent updating** — Months of skipped updates create a massive component queue that the worker chews through in one marathon session.

- **Corrupted update cache** — Damaged SoftwareDistribution files send the worker into a retry loop, burning CPU on operations that can never succeed.

- **Wedged update services** — Stuck wuauserv or BITS states leave the worker spinning on operations with no completion path.

- **Component store corruption** — Years of update cycles can damage the CBS store; the worker's repair attempts then fail repeatedly at high CPU cost.

- **Antivirus file contention** — Legacy third-party suites on old machines fight the worker over system files, multiplying retries.

- **Failing hard drive** — Bad sectors turn every file operation into a timeout-and-retry cycle that looks like endless CPU usage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Apply the 60-minute rule (2 hours on HDD)

On Windows 10 hardware, patience thresholds must be realistic. Verify the pattern before intervening.

1. Open Task Manager and confirm **Windows Modules Installer Worker** is the CPU consumer.
2. Check **Settings > Update & Security > Windows Update > View update history** for recent activity.
3. If updates are recent and it has been under 60 minutes (SSD) or 2 hours (HDD), wait — this is normal work on old hardware.
4. Proceed only for multi-hour high CPU with no update activity, or CPU surviving restarts.

### Fix 2: Restart the update services cleanly

Unstick the wedged service state that turns working sessions into infinite ones. Restarting the services is safe even mid-task because they coordinate their shutdown — unlike killing TiWorker.exe directly, which can strand file operations half-finished.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Pause 30 seconds, then `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Watch Task Manager for 10-15 minutes for the CPU to settle.

### Fix 3: Clear the update cache

Break the retry loop at its source by removing the damaged files the worker keeps choking on. On Windows 10 this cache clear works best paired with the servicing stack update from the previous fix — do them in the same session.

1. Open an elevated Command Prompt.
2. Stop the services: `net stop wuauserv`, `net stop bits`.
3. Delete the contents of **C:\Windows\SoftwareDistribution\Download** and **DataStore**.
4. Restart the services and let the worker process a clean queue. If the built-in troubleshooter is needed instead, our [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) applies to Windows 10's troubleshooter too.

### Fix 4: Install the servicing stack update first

The Windows 10-specific step: an outdated servicing stack makes every update operation — including the worker's — unreliable.

1. Find the latest Servicing Stack Update KB for your Windows 10 build on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Download and install the SSU .msu, then restart.
3. Now let Windows Update run — the worker operates on a current servicing foundation.
4. This single step resolves a surprising share of chronic Windows 10 update-worker problems.

### Fix 5: Repair with DISM and SFC

For worker loops rooted in store corruption, repair the store the worker depends on.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and allow 15-30 minutes.
3. Follow with `sfc /scannow`.
4. Restart and monitor. Both tools are documented in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Rule out the hard drive

On Windows 10-era laptops, the HDD is guilty until proven innocent for any 'everything is slow' symptom.

1. Run `chkdsk C: /f /r` from an elevated prompt, schedule with **Y**, and reboot for the full scan.
2. Check **This PC > C: > Properties > Tools** or your manufacturer's diagnostics for SMART warnings.
3. If the drive is failing, replace it — an SSD upgrade is the single best investment for these machines.
4. A healthy SSD also permanently ends the multi-hour TiWorker sessions.

### Fix 7: Update monthly to prevent mega-backlogs

The long-term fix is behavioral: small monthly updates never create the marathon sessions that infrequent updating does. Set a monthly reminder if needed — the machines that suffer marathon TiWorker sessions are almost always the ones that skip updates for months.

1. Open **Settings > Update & Security > Windows Update > Advanced options**.
2. Ensure updates are not paused indefinitely and active hours cover your usage.
3. Install Patch Tuesday updates within a week of release, on AC power.
4. Monthly 15-minute sessions replace the dreaded 4-hour catch-up marathons.

## Closing

TiWorker.exe on Windows 10 is usually an old laptop doing legitimate update work slowly — give it realistic time on HDD hardware. For the genuinely stuck cases, restart the services, update the servicing stack, clear the cache, and keep updates monthly so the backlog never becomes a marathon again.
