---
title: "High CPU Usage After a Windows 11 Update: Complete Fix Guide"
slug: how-to-fix-high-cpu-usage-after-windows-11-update
date: 2026-09-04
categories: ["performance"]
tags: ["high cpu usage", "windows 11 update", "performance fix", "task manager", "troubleshooting"]
description: "CPU pinned at 90–100% after a Windows 11 update? This complete guide diagnoses post-update CPU hogs — from Windows Modules Installer to telemetry — and fixes them in order."
thumbnail: "/images/thumbs/how-to-fix-high-cpu-usage-after-windows-11-update.webp"
faqs:
  - q: "Why is my CPU at 100% right after installing a Windows 11 update?"
    a: "Immediately after an update, Windows runs one-time housekeeping: compatibility telemetry, search re-indexing, .NET optimization, and Windows Modules Installer finishing the job. This typically settles within a few hours of plugged-in idle time. If CPU is still pinned after a full day of normal use and reboots, a process is stuck and the fixes in this guide will identify and stop it."
  - q: "How do I find which process is causing high CPU after the update?"
    a: "Open Task Manager with Ctrl+Shift+Esc, click the Processes tab, and sort by CPU. If a single named process like TiWorker.exe or CompatTelRunner.exe dominates, note it. For deeper detail, use the Details tab or Performance tab to confirm whether it's one core or all cores loaded. Screenshot the top offenders — that list decides which fix in this guide applies to your case."
  - q: "Is it safe to let Windows Modules Installer run at high CPU?"
    a: "Yes — TiWorker.exe (Windows Modules Installer Worker) is legitimate and essential; it finishes installing update components in the background. Ending it mid-task can corrupt the update and force a rollback loop. Give it up to two hours on a plugged-in machine. Only treat it as a problem if it never finishes across multiple days, which usually means a stuck update component."
  - q: "When should I roll back a Windows 11 update that caused high CPU?"
    a: "Consider rollback only after you've tried the targeted fixes — the Update Troubleshooter, DISM/SFC repair, disabling stuck post-update tasks, and driver updates — and a clean boot still shows the load. If the problem started the exact day of a feature update and no fix helps within a week, use Settings → Windows Update → Update history → Uninstall updates to roll back before the ten-day window closes."
---

A Windows 11 update is supposed to make your laptop better, not turn it into a space heater. Yet one of the most common complaints after a feature or cumulative update is the same: CPU usage pinned at 70, 90, or even 100 percent at idle, fans roaring, battery draining in half the normal time, and everything feeling sluggish. It often appears within a day of the update landing, and it rarely fixes itself by accident.

The good news is that post-update CPU spikes are usually not hardware damage or a bad update you must live with — they are specific Windows processes doing specific post-install work, or occasionally getting stuck while doing it. The fix is diagnosis first: find the process, understand its job, then apply the right fix for that process rather than spraying random "speed up Windows" tweaks. This guide walks you through that in order.

## Why this happens

- **Windows Modules Installer finishing the update:** TiWorker.exe completes installation tasks in the background and can consume heavy CPU for hours after a big update.
- **Post-update re-indexing:** The search indexer rebuilds its database, and Defender rescans changed system files, both of which hammer the CPU.
- **Compatibility telemetry backlog:** CompatTelRunner.exe runs the deferred telemetry collection a new Windows build triggers, which is notoriously heavy on older CPUs.
- **Stuck or corrupted update components:** A partially applied component keeps its installer worker looping forever instead of finishing and exiting.
- **Driver mismatches from the new build:** Old storage, chipset, or GPU drivers can misbehave under the new kernel, showing up as System or ntoskrnl.exe CPU.
- **Startup programs re-enabled:** Major updates sometimes re-enable disabled startup apps or reinstall manufacturer bloatware.
- **Background Microsoft Store updates:** The Store silently updates every inbox app at once right after a feature update lands.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact process eating CPU

Don't guess — open **Task Manager** (Ctrl+Shift+Esc), sort the Processes tab by CPU, and watch for a few minutes. Note the exact process name: TiWorker.exe, CompatTelRunner.exe, MsMpEng.exe, SearchIndexer.exe, or System. If nothing stands out in the simple view, click **Details** and sort there, or check the Performance tab to see whether it's one core or the whole CPU. For a post-update specific walkthrough of the most common culprits, see the guide to [Windows 11 slow after an update](/articles/windows-11-slow-after-update-how-to-fix/) — but stay here for the ordered process-by-process fixes. Your top one or two processes decide everything below.

1. Open Task Manager with Ctrl+Shift+Esc and click **More details**.
2. On the Processes tab, click the CPU column to sort by usage.
3. Leave it open for 3–5 minutes and note the top processes and their percentages.
4. Switch to the Details tab for exact process names if needed.

### Fix 2: Let legitimate post-update work finish (with a deadline)

Much post-update load is legitimate and finite. The trick is giving it a real chance while setting a deadline. Plug the laptop in, leave it idle with the lid open (not asleep) for two to three hours, and let TiWorker.exe, the indexer, and .NET optimization finish. Check Task Manager periodically: healthy post-update work visibly declines. If usage is identical after three hours of idle plugged-in time, it's stuck, not busy — move on to Fix 3. Never end TiWorker.exe mid-task; interrupting it can corrupt update components.

1. Plug the laptop into AC power.
2. Leave it on and idle (not sleeping) for 2–3 hours.
3. Re-check Task Manager — usage should be visibly declining.
4. If unchanged after 3 hours, continue to the next fix.

### Fix 3: Run the Windows Update Troubleshooter and check for pending work

Stuck update components are a top cause of permanent post-update CPU load. Go to **Settings → System → Troubleshoot → Other troubleshooters** and run **Windows Update**. It detects interrupted downloads, corrupted update caches, and failed component registrations, then repairs them — often ending the TiWorker.exe loop that was eating your CPU. After it finishes, go to **Settings → Windows Update** and install anything pending, then reboot. If you want Microsoft's own background on update troubleshooting, the [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official steps for a stuck update.

1. Open **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its repairs.
3. Go to **Settings → Windows Update** and install pending updates.
4. Reboot and re-check Task Manager after 30 minutes.

### Fix 4: Stop the CompatTelRunner.exe loop

If Task Manager shows CompatTelRunner.exe (Microsoft Compatibility Telemetry) holding high CPU for days, it's the telemetry backlog. The practical fix: disable the scheduled task. Open **Task Scheduler → Task Scheduler Library → Microsoft → Windows → Application Experience** and disable **Microsoft Compatibility Appraiser**. This stops the telemetry collection runs without affecting Windows Update itself. Also clear the SoftwareDistribution download cache if Fix 3 found corruption: stop the Windows Update service, delete `C:\Windows\SoftwareDistribution\Download\*`, and restart the service. The [Antimalware high-CPU fix for post-update systems](/articles/how-to-fix-antimalware-service-executable-high-cpu-after-windows-11-update/) covers the Defender side of the same post-update pileup.

1. Open Task Scheduler as administrator.
2. Navigate to Microsoft → Windows → Application Experience.
3. Right-click **Microsoft Compatibility Appraiser** and choose Disable.
4. Optionally clear the SoftwareDistribution download cache if corruption was found.

### Fix 5: Repair system files with SFC and DISM

Update-time file corruption makes system processes work harder and loop. Open an elevated Command Prompt and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`. DISM pulls clean component copies from Windows Update (grab them directly from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if you need a specific package), and SFC replaces damaged protected files. Reboot after both complete. This is especially effective when the top CPU consumer is System, ntoskrnl.exe, or a svchost.exe group — the signature of the OS itself struggling with damaged files.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
3. Run `sfc /scannow` and let it finish.
4. Reboot and observe CPU for 30 minutes.

### Fix 6: Update chipset, storage, and GPU drivers

Feature updates ship with a new kernel build, and old drivers — especially Intel/AMD chipset, NVMe storage, and GPU drivers — can misbehave badly under it, showing as System or ntoskrnl CPU. Don't rely on Windows Update alone for drivers. Visit your laptop manufacturer's support page for the chipset and storage drivers, and get GPU drivers from the vendor. For Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) auto-detects the right chipset drivers. Reboot after each driver install and re-check.

1. Identify your chipset and GPU models in Device Manager.
2. Download current chipset drivers from your manufacturer or Intel.
3. Download current GPU drivers from the GPU vendor.
4. Install each, rebooting between them, then re-check Task Manager.

### Fix 7: Clean boot and re-audit startup programs

Finally, rule out software. Major updates sometimes re-enable startup entries you had disabled. Open Task Manager's **Startup apps** tab, sort by status, and disable anything non-essential (cloud clients, updaters, chat apps). For a deeper check, run **msconfig**, go to Services, check **Hide all Microsoft services**, and disable the rest — then reboot. If CPU normalizes, re-enable services in halves to find the offender. This catches third-party updaters and utilities that broke or went haywire under the new build.

1. Open Task Manager → **Startup apps** and disable non-essentials.
2. Run `msconfig`, hide Microsoft services, disable the rest.
3. Reboot and check CPU at idle.
4. Re-enable in halves to isolate the culprit.

## Closing

Post-update CPU spikes look alarming but follow a predictable script: finish, repair, update, isolate. Work the list once, methodically, and the vast majority of cases resolve without drastic measures. If you've completed every fix and a clean boot still shows sustained high CPU from a system process, the remaining options are an in-place upgrade repair or rolling back the update — but in practice, Fix 1 through Fix 6 catch it long before that point.
