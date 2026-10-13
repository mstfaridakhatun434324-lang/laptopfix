---
title: "CompatTelRunner High CPU on Windows 11: Fix Guide"
slug: how-to-fix-compattelrunner-high-cpu-on-windows-11
date: 2026-09-16
categories: ["performance"]
tags: ["compattelrunner.exe", "telemetry", "high cpu", "windows 11", "compatibility"]
description: "CompatTelRunner.exe eating CPU on Windows 11? Learn what Microsoft Compatibility Telemetry does and how to stop its CPU spikes safely."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-on-windows-11.webp"
faqs:
  - q: "What is CompatTelRunner.exe and is it malware?"
    a: "CompatTelRunner.exe is a legitimate Microsoft process — the Compatibility Telemetry runner that collects system data to check upgrade readiness and app compatibility. It's digitally signed by Microsoft and lives in System32. Malware sometimes uses similar names, but the real one is safe; verify it's in C:\\Windows\\System32 and signed by Microsoft before worrying."
  - q: "Can I delete CompatTelRunner.exe to stop the CPU usage?"
    a: "Don't delete it. Removing system files triggers Windows File Protection to restore them, can break the Windows Update compatibility checks, and may cause update failures. The supported approaches — disabling the scheduled task and limiting diagnostic data — achieve the same CPU relief without damaging system integrity."
  - q: "Will disabling telemetry break Windows Update?"
    a: "No. Disabling the Microsoft Compatibility Appraiser scheduled task stops the telemetry collection runs, but Windows Update itself keeps working normally — it doesn't depend on CompatTelRunner to download or install updates. You may lose some upgrade-readiness pre-checks, but updates continue to function."
  - q: "How long does CompatTelRunner normally run?"
    a: "A healthy telemetry run lasts minutes to maybe an hour, typically after updates or on its weekly schedule, then exits. If it's been running at high CPU for days, or restarts immediately every time you end it, the task is stuck or its data collection is failing — which is exactly what the fixes below address."
---

CompatTelRunner.exe — Microsoft Compatibility Telemetry — has a reputation problem, and it's earned. This background process periodically wakes up, consumes 20–50% CPU scanning your system, and on some Windows 11 machines seems to never finish. Task Manager shows the name, the fan noise confirms the load, and ending the task only helps until the next scheduled run.

The process itself is legitimate: it collects compatibility data Microsoft uses for update readiness. But "legitimate" doesn't mean "must tolerate at 40% CPU." This guide shows how to calm it down through supported settings — scheduled task control, diagnostic data limits, and the group policy options — without deleting system files.

## Why this happens

- **Post-update telemetry backlog:** After feature updates, the appraiser re-scans the entire system — heavy and slow.
- **Stuck scheduled task:** A corrupted task state causes runs that never complete and restart endlessly.
- **Full diagnostic data level:** The "Full" setting collects dramatically more data than "Required."
- **Large app inventories:** Machines with hundreds of installed apps take far longer to inventory.
- **Corrupted telemetry store:** Damaged data files cause the collector to retry indefinitely.
- **Disk slowness amplifying scans:** On HDDs or busy SSDs, the file inventory crawl takes many times longer.
- **Conflicting scheduled triggers:** Multiple triggers firing the task in overlapping runs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's the scheduled task and end the current run

Open Task Manager and verify CompatTelRunner.exe is the sustained high-CPU process. Then open **Task Scheduler → Task Scheduler Library → Microsoft → Windows → Application Experience** and check the **Microsoft Compatibility Appraiser** task — its Last Run Time and status tell you whether you're looking at a scheduled run or a stuck loop. End the current process in Task Manager as a temporary reset, then watch whether it restarts on its own within the hour. A run that restarts immediately signals a stuck task, which Fix 2 addresses. The [condensed CompatTelRunner fix](/articles/best-way-to-fix-compattelrunner-high-cpu/) covers this same check briefly.

1. Confirm CompatTelRunner.exe CPU in Task Manager.
2. Check the Appraiser task's status in Task Scheduler.
3. End the current run as a temporary reset.
4. Watch for an immediate restart (stuck) versus quiet (scheduled).

### Fix 2: Disable the Microsoft Compatibility Appraiser task

The most effective supported fix. In **Task Scheduler → Microsoft → Windows → Application Experience**, right-click **Microsoft Compatibility Appraiser** and choose **Disable**. This stops the telemetry collection runs entirely while leaving Windows Update fully functional. It's reversible — re-enable anytime. For most users this single change ends CompatTelRunner CPU spikes permanently, since the process only runs when this task triggers it. Also disable the related **ProgramDataUpdater** task in the same folder if it's similarly noisy.

1. Open Task Scheduler as administrator.
2. Navigate to Microsoft → Windows → Application Experience.
3. Right-click **Microsoft Compatibility Appraiser** → Disable.
4. Optionally disable ProgramDataUpdater too.

### Fix 3: Reduce diagnostic data to Required

Lower the data level so any remaining telemetry runs are cheap. Go to **Settings → Privacy & security → Diagnostics & feedback** and set **Diagnostic data** to the minimum available (Required only), and turn off **Tailored experiences**. This shrinks what the collector gathers on every run. While there, review **Settings → Privacy & security → Activity history** and clear stored history — a bloated activity database is part of what the appraiser chews through. Less data to collect means shorter, cheaper runs even if the task ever re-enables.

1. Set diagnostic data to Required only.
2. Turn off Tailored experiences.
3. Clear stored activity history.
4. Verify the setting survives a reboot.

### Fix 4: Use Group Policy to manage telemetry (Pro/Enterprise)

On Windows 11 Pro, you get the proper administrative control. Open **gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Data Collection and Preview Builds** and configure **Allow Telemetry** (set to the minimal level) and **Disable the Windows Customer Experience Improvement Program**. Group Policy enforcement survives feature updates better than manual task disables, which major updates sometimes re-enable. Check the policy after each feature update — Microsoft has a habit of resetting telemetry preferences, so re-verification is part of the maintenance. Microsoft documents these policies in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open gpedit.msc as administrator.
2. Navigate to Data Collection and Preview Builds.
3. Set telemetry to the minimal allowed level.
4. Re-verify after each Windows feature update.

### Fix 5: Clear the corrupted telemetry store

If runs start but never finish, the telemetry database itself may be damaged. Stop the **Connected User Experiences and Telemetry** (DiagTrack) service via services.msc, then delete the contents of the telemetry data folder under ProgramData (the collector rebuilds it cleanly on next run). Restart the service. A corrupted store is a classic cause of the "runs for days" pattern — the collector retries the same damaged data forever. After clearing, any future run starts from a clean database and completes normally.

1. Stop the DiagTrack service in services.msc.
2. Clear the telemetry data folder under ProgramData.
3. Restart the DiagTrack service.
4. Monitor the next scheduled run for normal completion.

### Fix 6: Verify the executable is genuine

Rare but worth ruling out: malware mimicking the name. Right-click the CompatTelRunner.exe process in Task Manager → **Open file location** — the genuine file lives in `C:\Windows\System32`. Right-click it → Properties → Digital Signatures and confirm it's signed by Microsoft. If it's anywhere else or unsigned, treat it as malware: run a full Defender scan immediately. Also check the [troubleshooting overview](/articles/compattelrunner-high-cpu-troubleshooting/) for additional diagnostic angles if the genuine process still misbehaves after Fixes 1–5.

1. Open the process's file location from Task Manager.
2. Confirm it resides in C:\Windows\System32.
3. Verify the Microsoft digital signature.
4. Full Defender scan if anything looks wrong.

## Closing

CompatTelRunner.exe is legitimate Microsoft telemetry — but legitimacy doesn't obligate you to donate 40% CPU to it. Disable the scheduled task, drop diagnostic data to Required, and clear any corrupted store, and the process goes quiet while Windows Update keeps working fine. Check the task again after each feature update, since those love to re-enable it.
