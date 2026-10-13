---
title: "How to Fix TiWorker.exe High CPU Usage During Windows Update on Windows 11"
slug: "how-to-fix-tiworker-exe-high-cpu-windows-update-on-windows-11"
date: 2026-09-26
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows modules installer", "windows 11", "windows update"]
description: "TiWorker.exe pinning your CPU at 100% on Windows 11? It is the Windows Modules Installer Worker finishing update tasks. Learn when to wait and how to fix it when it never stops."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-on-windows-11.webp"
faqs:
  - q: "What is TiWorker.exe and is it a virus?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft system process responsible for installing, modifying, and removing Windows updates and optional components. It is not a virus — though malware occasionally disguises itself with similar names, the real TiWorker.exe lives in C:\\Windows\\WinSxS and is digitally signed by Microsoft. High CPU from the genuine process means update work is happening, not an infection."
  - q: "How long should TiWorker.exe use high CPU normally?"
    a: "After a cumulative or feature update, 15 to 45 minutes of elevated CPU is normal while it finalizes component installation and cleanup. On slower laptops or after major updates, it can run for 1 to 2 hours. It becomes a problem only when high CPU persists for many hours, survives restarts, or returns daily without any update activity — those patterns indicate stuck update work, covered in the fixes below."
  - q: "Can I disable TiWorker.exe to stop the high CPU?"
    a: "You should not disable it outright — it is part of the trusted installer machinery Windows needs to update itself, and killing it mid-task can corrupt the component store. The correct approach is to let it finish legitimate work, then fix whatever is keeping it stuck (usually a corrupted update cache). The service can be set to manual as a temporary diagnostic, but permanent disabling breaks Windows Update."
  - q: "Why does TiWorker.exe spike CPU even when I'm not updating?"
    a: "Because Windows Update works in the background: it may be downloading, staging, or cleaning up after updates you never manually started, including automatic maintenance tasks. Check Settings, then Windows Update, then Update history — there is usually recent activity explaining the spike. If the history is empty and TiWorker still hammers the CPU daily, the background work is stuck, not merely background."
---
You open Task Manager to find out why the fan is screaming, and there it is: TiWorker.exe, consuming 40, 70, sometimes 100% of your CPU. The name means nothing to most people, but TiWorker.exe — the Windows Modules Installer Worker — is the engine room of Windows Update on Windows 11, doing the heavy file work of installing and cleaning up updates. High CPU from it is often legitimate. The skill is knowing when it is working and when it is stuck.

The distinction matters because the fixes are opposites. A working TiWorker needs time and should be left alone; killing it mid-task is how component stores get corrupted. A stuck TiWorker — spinning for hours on a corrupted cache or a failed update it cannot complete — needs intervention: the troubleshooter, a cache reset, and the servicing-stack repairs below. This guide teaches you to tell the difference in two minutes, then act correctly.

Quick triage before you start: check **Settings > Windows Update > Update history**. Recent update activity plus high TiWorker CPU equals normal work — give it an hour. No recent activity plus endless high CPU equals stuck — start at Fix 2. If disk (not CPU) is the bottleneck, our [Windows Modules Installer Worker high-disk guide](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-in-windows-11-24h2/) covers that side.

## Why this happens

- **Post-update finalization in progress** — After installing updates, TiWorker performs component cleanup and manifest reconciliation — legitimately CPU-heavy for up to an hour.

- **Corrupted update cache** — Damaged files in SoftwareDistribution make the worker retry the same failed operations in an endless, CPU-burning loop.

- **Stuck Windows Update service state** — A wedged wuauserv or BITS leaves the worker waiting on operations that never complete, spinning on retries.

- **Damaged component store** — CBS corruption forces the worker into repeated failed repair attempts, each consuming a full CPU core.

- **Pending operations backlog** — Months of skipped updates create a huge queue of component work that runs for hours on the next update cycle.

- **Conflicting third-party software** — Antivirus or system utilities fighting the worker over the same files cause repeated access-denied retries.

- **Failing disk slowing file operations** — When every file operation takes ten times longer, the worker's CPU time stretches proportionally as it waits and retries.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually stuck (the 60-minute rule)

Do not 'fix' legitimate work. Confirm the pattern first with Task Manager and update history.

1. Open Task Manager (**Ctrl + Shift + Esc**), find **Windows Modules Installer Worker** under Processes.
2. Check **Settings > Windows Update > Update history** for recent activity.
3. If updates installed in the last day and CPU has been high under an hour, wait — it is working.
4. Only proceed if high CPU persists beyond 60-90 minutes with no recent update, or survives a restart.

### Fix 2: Restart the Windows Update services

A wedged service state is the most common reason a working TiWorker becomes a stuck one. Restarting the stack often unstick it within minutes.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Wait 30 seconds, then `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Watch Task Manager for 10 minutes — TiWorker CPU should settle as the fresh service state clears the jam.

### Fix 3: Run the Windows Update troubleshooter

The troubleshooter specifically detects the stuck-service and corrupted-cache conditions that keep the worker spinning.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart the laptop afterward.
4. Monitor TiWorker for 15 minutes post-reboot. If the troubleshooter itself fails, see our [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 4: Clear the corrupted update cache

When the worker is chewing on damaged files, remove the files. This breaks the retry loop at its source.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete the contents of **C:\Windows\SoftwareDistribution\Download** and the **DataStore** folder.
4. Restart the services and check for updates — the worker gets a clean queue to process.

### Fix 5: Repair the component store with DISM

If the worker is stuck on CBS-level corruption, repair the store it is struggling with.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` (15-30 minutes).
3. Follow with `sfc /scannow`.
4. Restart and observe — a repaired store ends the failed-repair retry loop. Microsoft documents both in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Check for disk problems

A struggling disk makes the worker look guilty when it is actually a victim. Verify the hardware.

1. Open an elevated Command Prompt and run `chkdsk C: /f`.
2. Schedule with **Y**, restart, and let the scan complete.
3. In **Settings > System > Storage > Disks & volumes**, check the drive health status.
4. If the drive is failing, replace it — preferably with an SSD, which also ends TiWorker slowness permanently on old HDDs.

### Fix 7: Install pending updates manually, then clean up

Sometimes the worker is stuck because the queue itself is the problem. Drain the queue manually, then let the worker finish cleanly.

1. Note pending KB numbers in **Update history**, download them from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), and install.
2. After installing, run **Disk Cleanup > Clean up system files** and check **Windows Update Cleanup** to remove superseded components.
3. Restart and confirm TiWorker idles near 0% CPU.
4. The worker should now only spike briefly during genuine future updates.

## Closing

TiWorker.exe high CPU is usually Windows doing its job — loudly. Give legitimate post-update work an hour, then intervene only for the genuinely stuck cases: restart the services, clear the cache, repair the store. Never just kill the process; fix what is keeping it busy.
