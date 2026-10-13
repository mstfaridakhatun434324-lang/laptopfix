---
title: "How to Fix TiWorker.exe High CPU During Windows Update on a Laptop"
slug: how-to-fix-tiworker-exe-high-cpu-windows-update-on-laptop
date: 2026-09-04
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows update", "windows modules installer worker"]
description: "TiWorker.exe is pinning your CPU at 100% during Windows Update? Here's why it happens and how to calm it down without breaking updates."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-on-laptop.webp"
faqs:
  - q: "Is TiWorker.exe a virus?"
    a: "No. TiWorker.exe is the legitimate Windows Modules Installer Worker, part of Windows Update and component servicing. It legitimately uses heavy CPU while installing or scanning updates. Malware can occasionally use the same name, so check that the file lives in C:\\Windows\\WinSxS, which is the genuine location."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "Thirty minutes to two hours is normal on a laptop during or right after an update, especially on older dual-core machines. If it has been pegging the CPU for more than four hours with no progress in Settings > Windows Update, something is stuck and you should work through the fixes below."
  - q: "Can I just end the TiWorker.exe task?"
    a: "Ending the task is safe but usually only a temporary fix, because Windows restarts it. Worse, killing it mid-install can leave component corruption. It is better to let the first phase finish or use the controlled methods below, such as running the troubleshooter or resetting update components."
  - q: "Will high CPU from TiWorker.exe damage my laptop?"
    a: "Short bursts of high CPU are safe. Modern laptops throttle themselves before heat causes damage. Sustained 100% CPU for many hours can still cause uncomfortable heat and battery drain, so fix a stuck worker rather than letting it grind indefinitely."
---

If you open Task Manager while Windows Update is doing its thing, there is a good chance you will see **TiWorker.exe** — the Windows Modules Installer Worker — sitting at the top of the CPU column, sometimes eating 80% or 100% of your processor. Fans spin up, the battery drains, and the laptop feels like it is working overtime. The instinct is to kill it, but TiWorker is doing real work: it installs update payloads, processes component store changes, and runs the servicing stack that keeps Windows coherent.

The problem is when it does not stop. On laptops, especially older or dual-core machines, TiWorker can grind away for hours, turning a routine Patch Tuesday into a day-long performance problem. This guide explains why it spikes, how to tell normal heavy work from a stuck process, and how to fix the stuck case without breaking Windows Update.

## Why this happens

- **Windows is actively installing an update.** TiWorker does the heavy lifting of installing update payloads, compressing files, and updating the component store. High CPU during an active install is expected behavior.
- **Post-update cleanup is running.** After updates install, Windows compresses superseded components and cleans the WinSxS folder. This cleanup phase can run at high CPU for an hour or more on laptops with spinning hard drives.
- **A corrupted update payload is being reprocessed.** If a downloaded package is damaged, TiWorker can loop through the same operations repeatedly without ever completing them.
- **The component store (WinSxS) is bloated or damaged.** A large or corrupted component store multiplies the work TiWorker has to do, and servicing operations may never converge.
- **Windows Update is stuck scanning.** TiWorker works with the update engine; if update detection is broken, the worker can sit in a high-CPU scan loop while Settings shows nothing happening.
- **Third-party antivirus is fighting the installer.** Real-time scanning of every file TiWorker touches creates a feedback loop of CPU usage, particularly during large cumulative updates.
- **A pending restart backlog exists.** Multiple stacked updates waiting for a restart force TiWorker to process everything in one painful session.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether an update is actually progressing

Do not assume it is stuck just because it is loud. High CPU is normal while work is being done.

1. Open **Settings** > **Windows Update** and check the status. If an update is downloading, installing, or pending restart, TiWorker is doing its job.
2. If an update is mid-install, plug in the charger, leave the laptop alone for 60–90 minutes, and check back.
3. To confirm progress, open Task Manager, right-click **TiWorker.exe**, and watch its CPU and disk activity over five minutes. Real work fluctuates; a stuck process looks frozen at a constant value.

### Fix 2: Restart to clear a backlog

The fastest fix when TiWorker has been grinding for hours is often just letting Windows finish what it started.

1. Save your work and select **Start** > **Power** > **Restart**. Do not choose Shut down, since Fast Startup can preserve the stuck state.
2. Let the laptop sit through the full "Working on updates" screen without forcing it off.
3. After restart, check Task Manager for TiWorker.exe. In many cases the backlog clears and CPU returns to normal within minutes.

### Fix 3: Run the Windows Update troubleshooter

When updates are broken, the troubleshooter resets the common failure points that keep TiWorker looping.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Windows Update** and click **Run**. Let it detect problems and apply fixes.
3. Restart and observe TiWorker for 30 minutes. This alone resolves many stuck-worker cases; see our guide on [running the Windows Update troubleshooter](/articles/how-to-fix-windows-update-with-troubleshooter-in-windows-11-24h2/) for deeper detail on what it resets.

### Fix 4: Reset the Windows Update components

A corrupted SoftwareDistribution or Catroot2 folder is the classic cause of endless servicing loops.

1. Open **Command Prompt as administrator**.
2. Stop the update services with these commands, one at a time:
   ```
   net stop wuauserv
   net stop cryptSvc
   net stop bits
   net stop msiserver
   ```
3. Rename the cache folders so Windows rebuilds them:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
4. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, and `net start msiserver`.
5. Check for updates again. If they install cleanly, TiWorker will finish and stand down.

### Fix 5: Repair the component store with DISM and SFC

If TiWorker is choking on a damaged component store, repairing it removes the underlying cause.

1. Open **Command Prompt as administrator** and run `DISM /Online /Cleanup-Image /RestoreHealth`. This can take 15–30 minutes on a laptop.
2. When DISM completes, run `sfc /scannow` and let it finish.
3. Restart the laptop. The servicing stack now has clean data to work with, and TiWorker should complete its work quickly.
4. On metered connections, download the repair source in advance or run DISM with a local source to avoid data charges.

### Fix 6: Exclude update folders from antivirus or update manually

Real-time scanning can turn every TiWorker file operation into a CPU battle.

1. Temporarily pause third-party real-time protection while an update installs, then re-enable it immediately after.
2. For a permanent fix, add exclusions for `C:\Windows\SoftwareDistribution` and `C:\Windows\WinSxS` in your antivirus settings — these are Microsoft-signed system areas, not user files.
3. Alternatively, bypass the automatic engine entirely: [install the KB manually from the Microsoft Update Catalog](/articles/how-to-manually-install-windows-update-on-windows-10/) using the file from [the Update Catalog](https://www.catalog.update.microsoft.com/), which sidesteps the stuck scan-and-install loop.

### Fix 7: Check your drive health and free space

TiWorker's file operations are brutally slow on failing or nearly full drives.

1. Ensure at least 20 GB of free space on C:. Windows servicing needs room to stage files.
2. Run `chkdsk C: /f` from an elevated prompt and restart when prompted.
3. On laptops with old hard drives, the same servicing work that takes 20 minutes on an SSD can take hours on an HDD — consider this when deciding whether TiWorker is genuinely stuck.

## Closing

TiWorker.exe high CPU is usually a sign that Windows is doing heavy but legitimate work — the fix is patience first, then methodical repair of the update pipeline if the work never ends. Reset the update components, repair the component store, and clear any antivirus interference, and the worker will settle down. If TiWorker is still pegged after a full reset and a clean component store, the install media may be the issue; Microsoft's [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the remaining recovery options for a servicing stack that refuses to behave.
