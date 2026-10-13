---
title: "CompatTelRunner High CPU After a Windows 11 Update? Fix It"
slug: how-to-fix-compattelrunner-high-cpu-after-windows-11-update
date: 2026-09-22
categories: ["performance"]
tags: ["compattelrunner", "high cpu", "telemetry", "windows 11 update", "compatibility"]
description: "CompatTelRunner.exe eating CPU after a Windows 11 update? Understand the telemetry runner and stop it from hogging resources."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe (Microsoft Compatibility Telemetry Runner) collects compatibility telemetry — data about your apps, drivers, and devices that Microsoft uses to assess whether your machine is ready for the next feature update and to fix compatibility blockers. It runs on a schedule via Task Scheduler, typically intensifying after updates when the system re-evaluates compatibility. It is legitimate Microsoft software, not malware, though its resource appetite surprises everyone the first time they meet it."
  - q: "Is CompatTelRunner.exe a virus?"
    a: "No. It is a genuine Microsoft-signed component living in System32, part of the Windows compatibility telemetry pipeline. Malware occasionally impersonates system process names, so verify the file location: right-click it in Task Manager > Open file location — the real one lives in C:\\Windows\\System32. Anything running the same name from a user folder or Temp directory is an impostor and should be scanned immediately. Location is the whole verification."
  - q: "Why does CompatTelRunner run so aggressively after updates?"
    a: "After a feature or cumulative update, Windows re-runs compatibility appraisal to re-baseline your system against the new build — new drivers, changed APIs, and altered system files all need re-evaluation. This post-update appraisal is far heavier than the routine scheduled runs, and on slower machines it can dominate CPU for hours. It is one-time work per update; the problem cases are when it never finishes and repeats daily."
  - q: "Will disabling CompatTelRunner break Windows Update?"
    a: "Disabling its scheduled tasks does not break update installation — updates download and install through the separate Windows Update servicing pipeline. What you lose is the compatibility telemetry that helps Microsoft target feature updates to your machine and pre-resolve driver blockers. In practice, disabled-telemetry machines update fine; they just contribute no compatibility data. The tradeoff is privacy/performance versus Microsoft's rollout intelligence about your specific hardware."
---

Of all the mysterious processes in Task Manager, CompatTelRunner.exe has the most suspicious name and the most innocent explanation: it is Microsoft's compatibility telemetry runner, scanning your apps and drivers to assess update readiness. After a Windows 11 update it runs an intensive re-appraisal — and on many machines that means hours of high CPU, spinning fans, and a process name that looks like malware doing something unmentionable.

It is not malware. But 'legitimate' and 'acceptable' are different things, and a telemetry process consuming 30 percent CPU for days is not acceptable. This guide covers the full arc: letting the legitimate post-update appraisal finish, then disabling its scheduled runs properly when it will not stop — without breaking updates. For general CPU issues, see [fixing high CPU usage in Windows 11 24H2](/articles/how-to-fix-high-cpu-usage-in-windows-11-24h2/); to audit boot-time residents, read [disabling startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Post-update compatibility re-appraisal**: Updates trigger an intensive one-time re-scan of apps, drivers, and devices against the new build.
- **Scheduled telemetry tasks firing**: The Application Experience scheduled tasks run CompatTelRunner on timers, sometimes daily.
- **Slow disk amplifying the scan**: The appraisal walks thousands of files; HDDs and eMMC make it take several times longer.
- **Stuck appraisal looping**: A corrupted telemetry database or a file it cannot assess makes the runner repeat instead of finishing.
- **Diagnostic Tracking service feeding it**: The connected telemetry services keep the pipeline active and scheduled.
- **Update re-arming disabled tasks**: Feature updates re-enable the telemetry scheduled tasks users had turned off.
- **Impostor malware using the same name**: Rare but real — verify the executable lives in System32 before assuming legitimacy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is the real CompatTelRunner

Thirty seconds that rules out the scary scenario.

1. In **Task Manager** > **Details**, right-click CompatTelRunner.exe > **Open file location** — it must be `C:\Windows\System32`.
2. Right-click the file > **Properties** > **Digital Signatures** — it must show **Microsoft Windows** as the signer.
3. If it lives anywhere else (user folders, Temp, AppData), treat it as malware: run a **Microsoft Defender Offline scan** immediately.
4. Check the command line in Task Manager's Details view (add the column) — the real runner launches from Task Scheduler with telemetry parameters.
5. Only proceed with the tuning below once legitimacy is confirmed.

### Fix 2: Let the post-update appraisal finish once

The intensive run is one-time per update — interrupting it just reschedules it.

1. Confirm the timing: did high CPU start within a day of a Windows update? If yes, this is the appraisal.
2. Give it one plugged-in idle window of 2–3 hours (overnight is ideal) with sleep disabled.
3. Do not kill the process mid-run — Task Scheduler will simply launch it again, often from scratch.
4. After the window, check Task Manager: a completed appraisal goes quiet until the next scheduled run.
5. If it is still raging after a full idle night, it is stuck — continue to the disabling fixes.

### Fix 3: Disable the scheduled telemetry tasks

The direct fix: stop the runner from being launched on schedule.

1. Open **Task Scheduler** (`taskschd.msc`) > **Task Scheduler Library** > **Microsoft** > **Windows** > **Application Experience**.
2. Right-click **Microsoft Compatibility Appraiser** > **Disable**.
3. In the same folder, disable **ProgramDataUpdater** as well — it feeds the same pipeline.
4. Check **Microsoft** > **Windows** > **Customer Experience Improvement Program** and disable its **Consolidator** and **UsbCeip** tasks.
5. Monitor for 48 hours — CompatTelRunner should not appear again outside of update aftermaths.

### Fix 4: Reduce the telemetry level feeding it

Less telemetry configured means less telemetry work scheduled.

1. **Settings** > **Privacy & security** > **Diagnostics & feedback** > **Diagnostic data** — set to **Required** only (not Optional).
2. Turn off **Tailored experiences** and **View diagnostic data** extras on the same page.
3. In Group Policy (Pro) or Registry (Home), the telemetry level **0/Security** (Enterprise) or **1/Basic** minimizes the pipeline — Home users get Required as the floor.
4. Note: this reduces but does not eliminate the scheduled runs — combine with Fix 3 for full effect.
5. Re-check after the next feature update, which may reset these to defaults — Microsoft documents the options at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Clear the corrupted telemetry state

When the runner loops instead of finishing, its state data is usually damaged.

1. With the tasks disabled (Fix 3), open an elevated Command Prompt.
2. Run `schtasks /Change /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /DISABLE` to be certain it is off.
3. Delete the telemetry database: remove files under `C:\Windows\System32\CompatTel` cache locations only if you know the exact safe targets — safer: run **Disk Cleanup** > **Clean up system files** and check all telemetry/diagnostic categories.
4. Re-enable the task once, let it run a single clean appraisal overnight, then disable it again if you prefer it off.
5. A clean single run after state-clearing usually behaves; chronic looping means deeper corruption — continue.

### Fix 6: Check for the update that re-armed it

Feature updates resurrect disabled telemetry tasks. Build the habit of re-checking.

1. After every feature update, revisit **Task Scheduler** > **Application Experience** and confirm your disables held.
2. Re-apply Fix 3 and Fix 4 as needed — it takes two minutes once you know the paths.
3. Consider a small reminder: a calendar note for the week after each Patch Tuesday to glance at Task Manager.
4. If CompatTelRunner spikes appear on a strict monthly schedule with no update correlation, something else is triggering it — check **Event Viewer** > **Applications and Services Logs** > **Microsoft** > **Windows** > **Application-Experience** for the trigger.
5. Persistence pays: the task stays dead as long as you re-kill it after the updates that revive it.

### Fix 7: Scan for impostors and rule out malware

The final verification, because a suspicious name deserves one thorough check.

1. Run **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** — the deepest built-in scan.
2. Check **Autoruns** (Microsoft Sysinternals) for anything referencing CompatTelRunner outside System32.
3. Review **Task Scheduler** for unfamiliar tasks launching similarly-named executables from odd paths.
4. If the offline scan is clean, the file is signed, and the location is System32, close the malware question permanently.
5. Genuine CompatTelRunner managed via Fixes 2–4 is a solved problem — no third-party 'telemetry killer' tools needed, and most of those are worse than the disease.

## Closing

CompatTelRunner is Windows taking its own compatibility census — legitimate, occasionally useful to Microsoft, and absolutely not entitled to 30 percent of your CPU for days. Let the post-update appraisal finish its one-time work, then disable its scheduled encore performances. The census-taker goes home, the fans spin down, and Task Manager loses its most suspicious-looking entry. Your CPU was never its to spend.
