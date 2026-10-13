---
title: "Windows Modules Installer Worker High Disk Usage in Windows 11 24H2 — How to Calm It Down"
slug: how-to-fix-windows-modules-installer-worker-high-disk-usage-in-windows-11-24h2
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows modules installer worker", "tiworker.exe", "high disk usage", "windows 11 24h2", "100% disk"]
description: "TiWorker.exe pinning your disk at 100% on Windows 11 24H2? Learn what Windows Modules Installer Worker is doing and how to stop the disk thrashing safely."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-worker-high-disk-usage-in-windows-11-24h2.webp"
faqs:
  - q: "What is Windows Modules Installer Worker (TiWorker.exe)?"
    a: "It is the background process that installs, modifies, and removes Windows update components. Whenever Windows Update stages or applies packages, TiWorker does the heavy file work against the component store. High disk usage from it usually means updates are actively installing — it is legitimate system activity, not malware, though a stuck update can keep it looping far longer than normal."
  - q: "Is it safe to end the Windows Modules Installer Worker task?"
    a: "Ending it in Task Manager is safe in the sense that Windows will simply restart it, but it is rarely useful — the process resumes and continues its work, and killing it mid-install can corrupt the update transaction. The better approach is to let pending updates finish, or fix the stuck update that is keeping the worker busy, using the steps in this guide."
  - q: "How long should TiWorker high disk usage normally last?"
    a: "On an SSD, a normal update session keeps TiWorker busy for 15 to 45 minutes. On a mechanical hard drive, several hours is possible during a feature update. If disk usage stays pegged at 90 to 100 percent for more than a few hours with no update progress in Settings, the worker is stuck on a failed package and you should clear the update cache."
  - q: "Can I disable Windows Modules Installer Worker permanently?"
    a: "No, and you should not try. It is a core part of the servicing stack, and disabling it breaks Windows Update entirely, leaving security patches uninstalled. The correct fix is to resolve whatever is making it loop — a corrupted cache, a stuck download, or a failing drive — not to kill the messenger. Pausing updates temporarily is the safe way to buy quiet time."
---

Open Task Manager on a Windows 11 24H2 laptop, sort by disk, and find Windows Modules Installer Worker (TiWorker.exe) sitting at 90 to 100 percent while everything else crawls. Your first instinct is that something is broken. Usually, it is not — TiWorker is the process that does the actual file work of installing updates: staging packages, writing to the component store, and cleaning up superseded components. When updates are flowing, high disk usage is the job getting done.

The problem starts when the job never finishes. A stuck download, a corrupted cache, or a failing drive can keep TiWorker retrying the same work in a loop for hours or days, and on a mechanical hard drive that loop makes the whole laptop feel broken. The diagnostic question is therefore simple: is TiWorker making progress, or is it spinning its wheels? Check Settings, then Windows Update — if updates are actively downloading or installing, let it work. If nothing is progressing, work through the fixes below.

One quick identity check first, because it matters: the legitimate TiWorker.exe lives in C:\Windows\WinSxS and C:\Windows\System32. Right-click it in Task Manager, choose Open file location, and confirm. Malware occasionally borrows the name, and that is a very different problem with a very different fix.

## Why this happens

- **Updates are genuinely installing:** TiWorker's normal job is disk-heavy, and 24H2's larger cumulative updates keep it busy longer than older builds did.
- **A stuck update keeps the worker retrying:** a failed download that never clears makes TiWorker loop on the same package indefinitely.
- **A corrupted SoftwareDistribution cache:** bad staged files force repeated verification and re-download attempts.
- **Post-update component cleanup:** after installing, TiWorker compresses and removes superseded components — heavy disk work that is entirely normal.
- **A mechanical hard drive bottleneck:** on HDDs, TiWorker's random read/write pattern saturates the disk far more visibly than on SSDs.
- **Corrupted component store:** damage in WinSxS makes staging fail and retry in a loop.
- **Malware using a similar name:** rare, but a fake TiWorker from another location will also show high disk usage.
- **Automatic maintenance tasks stacking up:** update work combined with indexing and defragmentation can peg a slow drive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is legitimate and check update progress

Before changing anything, confirm the process is real and whether it is doing productive work.

1. In Task Manager, right-click Windows Modules Installer Worker and choose Open file location — it should resolve inside C:\Windows\WinSxS or System32.
2. Open Settings, then Windows Update, and check whether updates are downloading, installing, or pending restart.
3. If updates are progressing, give TiWorker up to an hour on SSD (longer on HDD) to finish.
4. Run a full scan with Windows Security to rule out a namesake malware process. If the troubleshooter angle interests you, our guide on the [update troubleshooter not working](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) covers related repair paths.

### Fix 2: Restart the Windows Update services

A clean restart of the servicing stack often breaks TiWorker out of a retry loop without touching any data.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv` and `net stop bits`.
3. In Task Manager, end the TiWorker.exe process — it will restart cleanly with the services.
4. Run `net start wuauserv` and `net start bits`.
5. Watch Task Manager for 10 minutes to see whether disk usage settles.

### Fix 3: Clear the SoftwareDistribution cache

When the staged files are corrupt, TiWorker burns disk re-verifying them forever. A cache reset gives it a clean set to work with.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. Rename `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the four services and reboot.
5. Let Windows Update re-scan; TiWorker should now process a fresh, valid download queue. Microsoft documents this procedure on its [Windows update support pages](https://support.microsoft.com/en-us/windows).

### Fix 4: Run DISM and SFC to repair the component store

TiWorker works directly against the WinSxS store. If the store is damaged, every staging operation fails and retries.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
3. Run `sfc /scannow` afterward.
4. Reboot and monitor TiWorker for 20 minutes.
5. Persistent looping after a clean store points at the drive itself — see Fix 7.

### Fix 5: Run Disk Cleanup and free space

A nearly full drive forces TiWorker into a painful cycle of staging, failing for space, and cleaning up. Giving it room often ends the loop.

1. Run Disk Cleanup as administrator and select Windows Update Cleanup, Temporary files, and Delivery Optimization Files.
2. Confirm at least 15 to 20 GB free on C:.
3. Open Settings, then System, then Storage, and turn on Storage Sense for ongoing cleanup.
4. Reboot and check whether disk usage normalizes after the next update cycle.

### Fix 6: Pause updates to buy quiet time, then install manually

If you need the laptop usable right now, pausing updates stops TiWorker immediately and safely — then you control when the work happens.

1. Go to Settings, then Windows Update, and pause updates for one to two weeks.
2. Confirm TiWorker settles in Task Manager.
3. When you have time, unpause and let updates install while the laptop is plugged in and idle.
4. For a stubborn package, download it directly from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually.
5. Reboot after manual installation and verify TiWorker goes quiet. For a shorter routine aimed specifically at portable machines, see our [TiWorker high disk usage on laptop walkthrough](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-on-laptop/).

### Fix 7: Check the health of the drive

On older laptops, TiWorker at 100 percent disk for days with no update progress is a classic early symptom of a failing drive — the worker keeps hitting read errors and retrying.

1. In an elevated Command Prompt, run `wmic diskdrive get status` and look for OK.
2. Run `chkdsk C: /f` and reboot to let it scan.
3. Check your SSD/HDD manufacturer's utility for detailed SMART data.
4. If errors or warnings appear, back up immediately — no software fix outlasts failing hardware.
5. After replacing the drive, reinstall cleanly rather than cloning a damaged system.

## Closing

Windows Modules Installer Worker at high disk usage is usually Windows Update doing its job loudly, not a malfunction — the fix is to help it finish, not to silence it. Let legitimate update work complete, clear the cache when it loops, and repair the component store when staging keeps failing. The one case that deserves urgency is a looping TiWorker paired with SMART warnings: that is a drive telling you its time is short, and backups come before any further troubleshooting.
