---
title: "Update Orchestrator Eating CPU in Windows 11 24H2? Calm It Down"
slug: how-to-fix-update-orchestrator-high-cpu-in-windows-11-24h2
date: 2026-10-03
categories: ["windows-update"]
tags: ["update orchestrator", "high cpu", "windows 11 24h2", "wuauserv", "task scheduler"]
description: "Update Orchestrator (UsoClient/MusNotification) pushing CPU to 100% on Windows 11 24H2? Here's how to find the real trigger and bring usage back to normal."
thumbnail: "/images/thumbs/how-to-fix-update-orchestrator-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Is Update Orchestrator high CPU a virus?"
    a: "No — Update Orchestrator is a legitimate Windows component (UsoClient.exe and related tasks) that manages Windows Update sessions. High CPU from it almost always means update scans, metadata downloads, or a stuck session, not malware. That said, always verify the process location: the real one lives in C:\\Windows\\System32. Anything running Update Orchestrator from another folder should be scanned with Microsoft Defender immediately."
  - q: "How long should Update Orchestrator run at high CPU?"
    a: "Bursts of elevated CPU during active update scans are normal and should settle within 10 to 30 minutes. If UsoClient.exe or the UpdateOrchestrator scheduled tasks hold CPU above 50 percent for hours, repeat at every boot, or survive a completed update, the orchestrator session is likely stuck — run through the fixes below to reset it."
  - q: "Can I disable Update Orchestrator safely?"
    a: "Disabling it outright will break Windows Update, so don't delete or permanently disable the UpdateOrchestrator scheduled tasks. The fixes below pause, reset, or reconfigure the service instead, so updates keep working while the runaway CPU stops. If you need a temporary reprieve, pausing updates for 7 days from Settings is the supported way to silence it."
  - q: "Why does it only spike on battery or when I wake the laptop?"
    a: "Wake timers and the 'run on AC power' conditions on orchestrator tasks make it resume scans the moment the laptop wakes. On Windows 11 24H2, several orchestrator tasks lost their idle conditions, so they run at full priority. Fix 3 re-applies sane task conditions and idle waits to stop the wake-up spikes."
---

You open Task Manager because the fan is screaming, and there it is: Update Orchestrator — or UsoClient.exe, MusNotification.exe, or one of the UpdateOrchestrator scheduled tasks — sitting at 60, 80, even 100% CPU while you are doing nothing. The laptop gets hot, battery drains, and nothing you click makes it stop. On Windows 11 24H2 this has become one of the most reported update complaints, and it is usually not a sign of failing hardware or malware. It is the update machinery spinning its wheels: scanning, retrying, and re-scanning because a session got stuck or the update metadata never finished downloading.

The good news is that Update Orchestrator is just a scheduled-task wrapper around Windows Update logic, so it responds well to diagnosis. The key is to find out *which* task is spinning and *why* it cannot finish. Work through the fixes in order — most people find the culprit by Fix 3 and never need the rest. Related update-engine problems, like a Windows Update that hangs at the restart screen, are covered in our [guide to updates stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-step-by-step/).

## Why this happens

- **Stuck update session**: The orchestrator started an update session that never completed. It keeps retrying the scan in a tight loop, burning CPU on every attempt.
- **Corrupt update metadata**: Damaged files in the SoftwareDistribution folder make each scan fail partway, so the orchestrator re-runs it endlessly.
- **Reboot-required state mismatch**: The system thinks a reboot is pending, but the flag never clears, causing orchestrator tasks to wake repeatedly trying to finish.
- **Broken task conditions in 24H2**: Several UpdateOrchestrator tasks run without idle conditions on 24H2, so they execute at full priority instead of waiting for idle time.
- **Conflicting third-party services**: Some OEM update tools and antivirus updaters hook the same APIs, forcing orchestrator scans to restart.
- **Large cumulative updates pending**: Feature and cumulative packages are big; the orchestrator decompresses and hashes them, which is legitimately CPU-heavy for a while.
- **Background Intelligent Transfer conflicts**: BITS jobs stuck in a transient error state keep the orchestrator's download phase looping.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which orchestrator process is actually spinning

Do not treat the symptom blindly — find the real process first.

1. Open **Task Manager** (Ctrl + Shift + Esc) and go to the **Details** tab.
2. Sort by CPU and note the exact name: `UsoClient.exe`, `MusNotification.exe`, `wuauclt.exe`, or `TiWorker.exe`.
3. Right-click it, choose **Open file location**, and confirm it points to `C:\Windows\System32`. If it does not, run a full Defender scan before anything else.
4. Note whether it spikes at boot, on wake, or constantly — you will use this in Fix 3.

### Fix 2: Let the pending scan finish on AC power

Sometimes the orchestrator is doing legitimate work — it just needs quiet time to finish.

1. Plug in the charger and connect to a stable, non-metered network.
2. Go to **Settings > Windows Update** and click **Check for updates**.
3. Leave the laptop on for 30–45 minutes without heavy use. If CPU drops to normal after an update installs or completes its scan, the issue was a backlog, not a bug.
4. If usage is still pinned after the scan completes and the system is idle, move to Fix 3.

### Fix 3: Recondition the UpdateOrchestrator scheduled tasks

This is the fix that solves most 24H2 cases — restoring idle conditions so tasks stop running at full priority.

1. Open **Task Scheduler** (search for it in Start) and navigate to **Task Scheduler Library > Microsoft > Windows > UpdateOrchestrator**.
2. Open each task (**Schedule Scan**, **Schedule Wake To Work**, **USO_UxBroker**, **Backup Scan**) and go to the **Conditions** tab.
3. Check **Start the task only if the computer is idle for**, set it to **30 minutes**, and check **Wait for idle for** (1 hour).
4. On the **Settings** tab, check **Run task as soon as possible after a scheduled start is missed** but leave **Allow task to be run on demand** as-is.
5. Repeat for **Task Scheduler Library > Microsoft > Windows > WindowsUpdate > Scheduled Start** if present.
6. Restart the laptop and watch Task Manager for one hour — the orchestrator should now stay quiet until idle.

### Fix 4: Reset the Windows Update components

Corrupt metadata in SoftwareDistribution is the classic cause of scan loops.

1. Open an **elevated Command Prompt** (right-click Start > Terminal (Admin)).
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
5. Run **Settings > Windows Update > Check for updates** to rebuild the metadata cleanly.

### Fix 5: Clear the reboot-pending state

A phantom "reboot required" flag keeps orchestrator tasks waking forever.

1. Open **Registry Editor** and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired` — if the key exists and no reboot is genuinely pending, delete it.
2. Also check `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager` for a stale `PendingFileRenameOperations` value left by a failed install, and remove it.
3. Restart once. If the orchestrator goes quiet after boot, the stuck flag was the problem. Microsoft documents update troubleshooting steps at the [Windows update support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Run DISM and SFC to repair the update stack

If the component store itself is damaged, every orchestrator scan will thrash.

1. In elevated Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish (this can take 15–30 minutes).
2. Then run `sfc /scannow` and restart when it completes.
3. Check Task Manager after boot — a repaired component store lets scans complete instead of looping.

### Fix 7: Disable conflicting OEM update schedulers

Third-party updaters can force the orchestrator to re-scan constantly.

1. In **Task Scheduler**, look under **Task Scheduler Library** for vendor folders (Dell, HP, Lenovo, ASUS, Acer) and disable tasks named like "SupportAssist", "Update", or "Optimization" that run at logon.
2. In **Services** (`services.msc`), set any vendor update service to **Manual** instead of Automatic.
3. Use the vendor's own tool (for example, the [Dell support updater](https://www.dell.com/support)) on demand rather than on a schedule, then reboot and re-check CPU.

## Closing

Update Orchestrator high CPU is annoying but almost always fixable without reinstalling anything — it is the update engine asking for help finishing a job, not a failing laptop. Once the stuck session is cleared and the task conditions are sane, the orchestrator goes back to doing short, quiet scans in the background. If the spikes return every Patch Tuesday, that is normal scan behavior; if they return daily with no updates pending, run through Fixes 3 through 5 again. And if the orchestrator's thrashing ever leaves an update half-applied, our [undoing-changes recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) walks you through the rollback side.
