---
title: "CompatTelRunner High CPU? Stop the Telemetry Hog"
slug: how-to-fix-compattelrunner-high-cpu-youtube
date: 2026-10-01
categories: ["performance"]
tags: ["compattelrunner", "high cpu", "telemetry", "windows 11", "compatibility telemetry"]
description: "CompatTelRunner.exe pinning your CPU at 100%? Understand Microsoft's compatibility telemetry and safely rein it in without breaking Windows."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-youtube.webp"
faqs:
  - q: "What is CompatTelRunner.exe and is it a virus?"
    a: "CompatTelRunner.exe is a legitimate Microsoft process — the Windows Compatibility Telemetry runner. It collects usage and compatibility data to help Microsoft decide whether your PC is ready for feature updates. It is not malware, though malware can disguise itself with a similar name, so always verify the file lives in System32 and is digitally signed by Microsoft."
  - q: "Why does CompatTelRunner use so much CPU?"
    a: "It scans your system — installed programs, drivers, and device data — to build a compatibility report, which is CPU and disk intensive. It usually runs after updates, on a schedule, or when Microsoft is evaluating your machine for the next feature update. On older laptops the scan can saturate the CPU for 20 to 60 minutes."
  - q: "Is it safe to disable CompatTelRunner?"
    a: "Disabling its scheduled task is safe and widely done: it stops the telemetry collection scans but does not affect Windows Update's ability to install security patches. The only consequence is that Microsoft gets less compatibility data from your PC, which may delay automatic offers of feature updates — cumulative security updates continue normally."
  - q: "Will CompatTelRunner come back after a Windows update?"
    a: "Sometimes, yes. Major feature updates can re-enable the telemetry scheduled tasks and reset related policies. If high CPU from CompatTelRunner returns after an update, revisit the Task Scheduler and Group Policy steps — they take two minutes to reapply and the process will settle down again."
---

You open Task Manager because the laptop sounds like a jet, and there it is: **CompatTelRunner.exe** chewing through 30, 50, sometimes 100% of your CPU. It sounds sinister, but it's actually Microsoft's own compatibility telemetry — a process that scans your system to report what's installed so Microsoft can judge update readiness.

Legitimate doesn't mean welcome. On older or lower-powered laptops, a CompatTelRunner scan can make the machine unusable for the better part of an hour, and it has a habit of running at the worst possible moments. The good news: this is one of the most cleanly fixable high-CPU problems in Windows, because the process is launched by a scheduled task you can control.

Before you touch anything, verify it's the real thing — malware occasionally wears the same name. Then we'll throttle its schedule, reduce what triggers it, and confirm the CPU stays quiet.

## Why this happens

- **Post-update compatibility scan**: After updates, Windows runs a full telemetry scan to reassess what your PC can handle.
- **Scheduled task trigger**: The **Microsoft Compatibility Appraiser** task fires on schedule or on idle, launching CompatTelRunner.
- **Feature-update evaluation**: When Microsoft is deciding whether to offer your PC the next feature update, appraisal activity spikes.
- **Slow disk amplifies it**: On HDDs, the scan's heavy disk I/O plus CPU work saturates the whole system far longer than on SSDs.
- **Corrupt telemetry database**: A damaged telemetry store can make the scan loop or restart repeatedly instead of finishing.
- **Malware masquerading**: Rare, but fake CompatTelRunner processes exist — they typically live outside System32 and lack Microsoft's signature.
- **Outdated Windows build**: Older builds run the appraiser more aggressively; newer builds have toned its scheduling down.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's the genuine Microsoft process

Rule out malware before changing anything.

1. In **Task Manager**, right-click **CompatTelRunner** (it may show as **Microsoft Compatibility Telemetry**) and choose **Open file location**.
2. The genuine file lives at `C:\Windows\System32\CompatTelRunner.exe` — anywhere else is suspicious.
3. Right-click the file > **Properties** > **Digital Signatures** — it should be signed by **Microsoft Windows**.
4. Run a full scan with **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** to be thorough.
5. If it's genuine (it almost always is), proceed — you're dealing with a configuration problem, not an infection. If it's fake, let Defender remove it and skip the rest.

### Fix 2: Let the current scan finish — once

Sometimes the fastest fix is patience, applied deliberately.

1. Check how long it's been running: Task Manager > **Details** tab > right-click columns > add **CPU time**. If CPU time is under 30 minutes, the scan may simply be mid-run.
2. Plug in the laptop, close heavy apps, and let it run to completion — interrupting scans repeatedly can make the scheduler retry sooner.
3. Watch CPU time: if it keeps resetting to zero every few minutes, the process is crashing and relaunching (a corrupt telemetry store — see Fix 5), not just scanning slowly.
4. If it finishes and CPU drops to normal, you've confirmed it was a one-off scan — still apply Fix 3 so it doesn't ambush you again next month.
5. If it's been grinding for over an hour on an SSD system, don't wait longer — move to the scheduled-task fix.

### Fix 3: Disable the Compatibility Appraiser scheduled task

This is the core fix — stop the launcher, stop the scans.

1. Press `Win + R`, type `taskschd.msc`, and press Enter to open **Task Scheduler**.
2. Navigate to **Task Scheduler Library** > **Microsoft** > **Windows** > **Application Experience**.
3. Right-click **Microsoft Compatibility Appraiser** and choose **Disable**.
4. In the same folder, also disable **ProgramDataUpdater** — it's a related telemetry task that can trigger similar scans.
5. Check the **Customer Experience Improvement Program** folder too and disable its tasks — these feed the same telemetry pipeline. Verify in Task Manager over the next day that CompatTelRunner no longer launches.

### Fix 4: Reduce telemetry via Group Policy or Registry

Lower the data-collection level so there's less reason to scan.

1. Press `Win + R`, type `gpedit.msc` (Pro/Enterprise/Education) and go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Data Collection and Preview Builds**.
2. Enable **Allow Telemetry** and set it to **0 – Security** (or **1 – Basic** on newer builds where 0 is restricted).
3. On Windows Home (no gpedit), use the Registry: navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection`, create DWORD **AllowTelemetry** = **0**.
4. Also set **Settings** > **Privacy & security** > **Diagnostics & feedback** > **Diagnostic data** to the minimum and turn off **Tailored experiences**.
5. Reboot. Lower telemetry levels measurably reduce how often and how long the appraiser runs — many users report it effectively stops.

### Fix 5: Clear a corrupt telemetry store

If CompatTelRunner launches, dies, and relaunches in a loop, its data store is likely corrupt.

1. First apply Fix 3 (disable the task) so the process isn't fighting you while you clean.
2. Open **Command Prompt as administrator** and run: `net stop diagtrack` to stop the Diagnostics Tracking Service.
3. Navigate to `C:\ProgramData\Microsoft\Diagnosis` — back it up if you're cautious, then delete its contents (this is telemetry staging data, safe to clear).
4. Restart the service: `net start diagtrack`, then re-enable or leave disabled per your preference from Fix 3.
5. Check **Settings** > **Windows Update** for pending updates afterward — a healthy telemetry pipeline and an up-to-date build keep the appraiser calm. Microsoft documents update troubleshooting at their [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Rule out disk bottlenecks amplifying the scan

On HDD systems, the scan isn't just CPU-heavy — it's I/O-heavy.

1. During a scan, check **Task Manager** > **Performance** > **Disk** — if active time is 100% with modest throughput, the disk is the amplifier.
2. The real fix is an SSD upgrade, but short-term: make sure at least 15–20% free space exists on C: so the telemetry staging has room.
3. Run **Disk Cleanup** (`cleanmgr`) to clear temp files that the scan would otherwise churn through.
4. If you're still on an HDD, consider our [high disk usage guide](/articles/best-way-to-fix-windows-11-high-disk-usage-on-startup/) — the same I/O contention makes every background task worse.
5. After moving to an SSD, most users find CompatTelRunner scans finish in minutes and are barely noticeable — the "high CPU" complaint largely disappears.

### Fix 7: Monitor and re-apply after feature updates

Feature updates can undo your work — have a re-check routine.

1. After every feature update, reopen **Task Scheduler** and confirm the Appraiser task is still disabled — re-disable if Microsoft re-enabled it.
2. Verify the **AllowTelemetry** policy survived the update.
3. Give the system 48 hours post-update: some appraisal activity immediately after a feature update is normal and settles on its own.
4. If CompatTelRunner returns despite disabled tasks, check for a new task name — Microsoft occasionally renames telemetry tasks. Sort the Application Experience folder by **Last Run Time** to spot the launcher.
5. For persistent cases, [Windows Search indexing](/articles/how-to-fix-search-indexing-high-cpu-windows-11-on-lenovo-laptop/) or [Windows Modules Installer](/articles/best-way-to-fix-windows-modules-installer-high-cpu/) may be the actual CPU hog wearing a similar pattern — verify in Task Manager before assuming telemetry.

## Closing

CompatTelRunner high CPU looks alarming but it's one of Windows' most straightforward fixes: verify the process is genuine, let any in-progress scan finish, then disable the Compatibility Appraiser scheduled task and dial telemetry down. That combination silences the problem for nearly everyone — just remember to re-check after major feature updates, since Microsoft occasionally re-enables the task.
