---
title: "CompatTelRunner High CPU on Windows 10: Fix Guide"
slug: how-to-fix-compattelrunner-high-cpu-on-windows-10
date: 2026-09-28
categories: ["performance"]
tags: ["compattelrunner.exe", "telemetry", "windows 10", "high cpu", "compatibility"]
description: "CompatTelRunner.exe spiking CPU on Windows 10? Stop Microsoft Compatibility Telemetry's CPU usage with these safe, supported fixes."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-on-windows-10.webp"
faqs:
  - q: "What is CompatTelRunner.exe on Windows 10?"
    a: "It's Microsoft's Compatibility Telemetry runner — a legitimate signed system process that periodically scans your hardware, drivers, and installed software to assess upgrade readiness and app compatibility. It lives in C:\\Windows\\System32. High CPU happens when its scheduled runs get stuck, the telemetry backlog grows after updates, or its data store corrupts — all fixable without deleting anything."
  - q: "Is it safe to disable the Compatibility Appraiser task on Windows 10?"
    a: "Yes. Disabling the Microsoft Compatibility Appraiser scheduled task stops CompatTelRunner's runs, and Windows Update continues working normally — update delivery doesn't depend on telemetry collection. It's reversible in Task Scheduler anytime. This is the standard, supported fix recommended across Microsoft's own documentation and IT communities."
  - q: "Will these fixes work on Windows 10 Home without Group Policy?"
    a: "Yes — the core fixes (disabling the scheduled task, reducing diagnostic data in Settings, clearing the telemetry store) all work on Home. Group Policy is only available on Pro/Enterprise, but it's an enhancement, not a requirement. Windows 10 Home users get full relief from the Task Scheduler and Settings steps alone."
  - q: "Why does CompatTelRunner run at the worst possible times?"
    a: "Its triggers include system idle, scheduled weekly runs, and post-update backlogs — but 'idle' detection is imperfect, so it often fires while you're working. Disabling the scheduled task (Fix 2) removes the scheduling entirely, which is why it's the definitive fix rather than trying to reschedule around your usage."
---

Windows 10 users know CompatTelRunner.exe well — often too well. Microsoft Compatibility Telemetry periodically wakes up, scans the system at 20–50% CPU, and on many machines seems to take forever to finish. It fires at inconvenient times, the fan noise announces it, and ending the task only helps until the next scheduled run.

The process is legitimate, but you don't have to donate your CPU to it. Windows 10 gives you the same supported controls as Windows 11: scheduled task management, diagnostic data settings, and (on Pro) Group Policy. Here's the fix sequence.

## Why this happens

- **Stuck scheduled runs:** The Appraiser task starts but never completes, restarting endlessly.
- **Post-update backlog:** Cumulative and feature updates trigger full re-scans of the system.
- **Full diagnostic data:** The highest data level multiplies what each run collects.
- **Corrupted telemetry store:** Damaged data files trap the collector in retry loops.
- **Large software inventories:** Hundreds of installed programs extend every scan.
- **Slow disks:** HDDs make the file-inventory crawl many times longer.
- **Overlapping triggers:** Multiple task triggers firing concurrent runs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the process and check the task

Open Task Manager, confirm CompatTelRunner.exe is the sustained high-CPU process, and verify it's genuine: right-click → Open file location should show `C:\Windows\System32`, and Properties → Digital Signatures should show Microsoft. Then open **Task Scheduler → Task Scheduler Library → Microsoft → Windows → Application Experience** and inspect the **Microsoft Compatibility Appraiser** task — last run time, next run time, and history reveal whether you're seeing a scheduled run or a stuck loop. End the current process as a temporary reset. The [Windows 11 CompatTelRunner guide](/articles/how-to-fix-compattelrunner-high-cpu-on-windows-11/) covers the same verification on the newer OS.

1. Confirm CompatTelRunner.exe CPU in Task Manager.
2. Verify location (System32) and Microsoft signature.
3. Inspect the Appraiser task's run history in Task Scheduler.
4. End the current run as a temporary reset.

### Fix 2: Disable the Microsoft Compatibility Appraiser task

The definitive fix on Windows 10: in **Task Scheduler → Microsoft → Windows → Application Experience**, right-click **Microsoft Compatibility Appraiser** and choose **Disable**. CompatTelRunner only runs when this task triggers it, so disabling the task ends the CPU spikes permanently — while Windows Update keeps working normally. Also disable **ProgramDataUpdater** in the same folder if it's active. Revisit after feature updates, which sometimes re-enable the task. The [condensed fix guide](/articles/best-way-to-fix-compattelrunner-high-cpu/) lists this as the primary step.

1. Open Task Scheduler as administrator.
2. Navigate to Microsoft → Windows → Application Experience.
3. Disable **Microsoft Compatibility Appraiser**.
4. Also disable ProgramDataUpdater if present and noisy.

### Fix 3: Set diagnostic data to Basic

Reduce what any telemetry run collects: **Settings → Privacy → Diagnostics & feedback** → set **Diagnostic data** to **Basic** (the minimum on Windows 10) and turn off **Tailored experiences**. Basic versus Full is a dramatic difference in collection volume — shorter runs, less CPU, less disk. While in Privacy settings, review **Activity history** and clear it; the appraiser chews through that database on every run. These settings persist well on Windows 10, but verify after feature updates.

1. Set diagnostic data to Basic in Privacy settings.
2. Turn off Tailored experiences.
3. Clear stored activity history.
4. Verify settings after future feature updates.

### Fix 4: Disable the DiagTrack service's heavy lifting

The **Connected User Experiences and Telemetry** (DiagTrack) service feeds the telemetry pipeline. Open services.msc, find it, and set its Startup type to **Disabled** (or Manual if you prefer caution), then stop it. This cuts the background telemetry collection that triggers appraiser runs, without affecting Windows Update or Defender. Combined with the disabled scheduled task, this leaves CompatTelRunner with essentially nothing to do. It's reversible — set back to Automatic if ever needed. Microsoft documents the service in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open services.msc and find Connected User Experiences and Telemetry.
2. Set Startup type to Disabled and stop the service.
3. Confirm CompatTelRunner no longer launches.
4. Re-enable only if a specific need arises.

### Fix 5: Clear the corrupted telemetry data store

If runs start but never finish — the "always running" pattern — the data store is likely corrupt. Stop the DiagTrack service (if running), then delete the telemetry data contents under ProgramData's Microsoft Diagnosis folder — the collector rebuilds it cleanly. Restart the service if you kept it enabled. Corrupted stores are the classic cause of infinite runs: the collector retries the same damaged data forever. After clearing, any future collection starts clean and completes. The [troubleshooting overview](/articles/compattelrunner-high-cpu-troubleshooting/) covers additional store-related diagnostics.

1. Stop the DiagTrack service.
2. Clear the telemetry data folder under ProgramData.
3. Restart the service (if you kept it enabled).
4. Monitor for normal, finite runs.

### Fix 6: Group Policy lockdown (Pro/Enterprise)

On Windows 10 Pro, enforce it properly: **gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Data Collection and Preview Builds** → set **Allow Telemetry** to the minimum (0/Security where available) and enable **Disable Windows Consumer Features** while you're hardening. Policy enforcement survives the feature updates that re-enable manual tweaks — this is the set-and-forget answer for Pro machines. Verify with `gpresult` that the policy applied, and re-check after each feature update since major upgrades can reset policy states.

1. Open gpedit.msc as administrator.
2. Set Allow Telemetry to minimum in Data Collection.
3. Disable consumer features as a bonus hardening step.
4. Verify with gpresult; re-check after feature updates.

## Closing

CompatTelRunner.exe on Windows 10 is tamed the same way as on 11: disable the Appraiser task, drop diagnostic data to Basic, and clear any corrupted store. The process is legitimate, but your CPU is yours — these supported controls return it to you without breaking updates or system integrity. Check the task once more after each feature update, and enjoy the quiet. Save this guide's Task Scheduler path somewhere handy — you'll want it again after the next feature update.
