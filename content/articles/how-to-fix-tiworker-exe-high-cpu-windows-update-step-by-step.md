---
title: "Step-by-Step: Taming TiWorker.exe High CPU on Windows 11"
slug: how-to-fix-tiworker-exe-high-cpu-windows-update-step-by-step
date: 2026-09-26
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows modules installer", "windows 11", "step by step"]
description: "A step-by-step method to diagnose and fix TiWorker.exe high CPU on Windows 11: verify the stall, stop services cleanly, clear the cache, and repair the store."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-step-by-step.webp"
faqs:
  - q: "Should I disable TiWorker.exe to stop the high CPU?"
    a: "No. TiWorker.exe is the Windows Modules Installer Worker, a core system process that installs updates — disabling it breaks Windows Update entirely. The high CPU is a symptom of a stuck update, not a rogue process. Fix the stuck update underneath it by clearing the cache and repairing the component store, and TiWorker will settle on its own once it has healthy work to do."
  - q: "How do I tell normal TiWorker activity from a stuck update?"
    a: "Check Settings > Windows Update. If an update is downloading or installing and progressing, high TiWorker CPU is normal — give it up to two hours. If the update shows no progress for hours, the percentage never moves, or TiWorker pins the CPU with no update running at all, the process is stuck and the steps in this guide apply."
  - q: "Why does TiWorker.exe come back after I end the task?"
    a: "Because the queued update task that spawned it is still active. Ending TiWorker in Task Manager kills the worker but not the job, so Windows simply starts a new worker for the same stuck package. You must stop the Windows Update service first, then clear the corrupted cache — that removes the broken job the worker keeps getting assigned."
  - q: "Can low disk space cause TiWorker.exe high CPU?"
    a: "Yes. When the system drive is nearly full, TiWorker's compression and staging operations slow to a crawl and retry repeatedly, pinning the CPU far longer than normal. Freeing at least 20 GB on the C: drive often resolves mysteriously long TiWorker sessions. Check Settings > System > Storage before assuming the update itself is broken."
---

TiWorker.exe — the Windows Modules Installer Worker — is the engine room of Windows Update. When updates install, it compresses, verifies, and stages thousands of files, and that work legitimately saturates a CPU core or two. The problem is that it gives you no useful feedback: Task Manager shows a process eating your processor, the update screen shows little progress, and you are left guessing whether to wait or act.
The step-by-step method below removes the guessing. Each step is a gate: verify the stall, stop the pipeline cleanly, remove the corrupted input, repair the underlying store, and retry under control. You test after each fix, so you stop as soon as the problem is solved instead of performing surgery the machine did not need.
This is the generic Windows 11 version of the TiWorker repair; the HP-specific edition with HP driver considerations is the [TiWorker on HP guide](/articles/how-to-fix-tiworker-exe-high-cpu-windows-update-on-hp-laptop/). For machines where updates fail outright, the [update troubleshooter walkthrough](/articles/how-to-fix-windows-update-with-troubleshooter-on-windows-11/) automates parts of this sequence, and Microsoft's own [support guidance](https://support.microsoft.com/en-us/windows) documents the current known update issues.

## Why this happens

- **An update is legitimately installing.** TiWorker's file compression and staging work is CPU-intensive by design during active installs.
- **A corrupted package keeps it retrying.** A damaged download makes TiWorker attempt the same failed operation in a loop.
- **The WinSxS component store is damaged.** Corruption in the store forces long, failing maintenance passes.
- **The update cache holds broken files.** Bad data in SoftwareDistribution gives the worker garbage to process.
- **Disk space is critically low.** Staging operations crawl and retry when the drive is nearly full.
- **A long update backlog.** Months without updating queue an enormous amount of work into one session.
- **A failing driver update loops.** Driver packages that fail verification trigger repeated install attempts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall in Task Manager and Settings

Step one is always diagnosis. TiWorker doing real work looks identical to TiWorker stuck — the difference is whether the update is progressing.

1. Open Settings > Windows Update and note the exact status and progress percentage.
2. Open Task Manager > Processes, find Windows Modules Installer Worker, and note its CPU over five minutes.
3. If the update percentage is moving, wait — give it up to two hours before acting.
4. Proceed only if CPU stays high for hours with zero update progress.

### Fix 2: Stop the update pipeline cleanly

Never kill TiWorker directly while it holds file locks. Stopping the driving services halts the work gracefully.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` to stop the Windows Update service.
3. Run `net stop bits` to stop the background transfer service.
4. Confirm TiWorker.exe drops out of Task Manager within a minute or two.

### Fix 3: Clear the SoftwareDistribution cache

This removes the corrupted package TiWorker was choking on. It is the single highest-yield step in the sequence.

1. With services stopped, run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
2. Also run `ren C:\Windows\System32\catroot2 catroot2.old` for the signature cache.
3. Restart both services with `net start wuauserv` and `net start bits`.
4. Reboot the machine before checking for updates again.

### Fix 4: Free up disk space

A cramped system drive turns TiWorker's staging work into an endless crawl. Give it room before the retry.

1. Open Settings > System > Storage and confirm at least 20 GB free on C:.
2. Run Disk Cleanup with system files selected; clear temporary files, delivery optimization files, and old update cleanup data.
3. Uninstall unused applications and move large personal files off the system drive.
4. Re-verify the free space — do not skip this check.

### Fix 5: Repair the component store

If the cache clear did not calm TiWorker, the WinSxS store itself is likely damaged. DISM repairs it from known-good sources.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Allow 15 to 30 minutes; do not interrupt it even if the progress bar stalls.
3. Follow with `sfc /scannow` to verify system file integrity.
4. Restart the machine when both complete.

### Fix 6: Retry the update and monitor

With clean cache, free space, and a repaired store, the retry should show TiWorker spiking briefly during real work instead of plateauing.

1. Connect to AC power and a stable network connection.
2. Go to Settings > Windows Update and click Check for updates.
3. Watch Task Manager during the install: brief high-CPU bursts are normal and healthy.
4. If a specific update fails, note its KB number and check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a standalone package.

### Fix 7: Check drivers with the manufacturer tool

A failing driver package is the last common cause of TiWorker loops. Current drivers from the silicon vendor install cleanly.

1. Run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to check chipset and integrated graphics drivers.
2. Update display and storage drivers from the laptop manufacturer's support site.
3. In Device Manager, roll back any driver installed on the date the problems began.
4. Retry the update after the driver refresh.

### Fix 8: Keep the update backlog from rebuilding

Once TiWorker is calm, stop the next marathon session before it starts. TiWorker grinds hardest when months of skipped updates arrive all at once, so the long-term fix is keeping the queue short. A machine that installs its updates monthly gives the worker small, quick jobs instead of an all-day backlog.

1. Leave automatic updates enabled so small updates install as they arrive rather than piling up.
2. Set active hours in Settings > Windows Update > Advanced options so installs happen when you are not working.
3. Do not pause updates for months at a time — a long pause guarantees the next session is a heavy one.
4. Once a month, manually check for updates and install what is pending while you are nearby to monitor.

## Closing

The TiWorker sequence is a loop you can break: verify, stop cleanly, clear the cache, free space, repair the store, retry. Most cases resolve at the cache-clear step. The process itself is never the enemy — it is a faithful worker stuck with a broken assignment, and once you fix the assignment, the CPU graph returns to normal.
