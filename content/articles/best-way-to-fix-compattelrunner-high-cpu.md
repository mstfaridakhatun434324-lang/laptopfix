---
title: "Best Way to Fix CompatTelRunner.exe High CPU Usage in Windows 11"
slug: best-way-to-fix-compattelrunner-high-cpu
date: 2026-09-10
categories: ["performance"]
tags: ["compattelrunner", "telemetry", "high cpu", "windows 11", "compatibility"]
description: "CompatTelRunner.exe (Microsoft Compatibility Telemetry) spiking your CPU to 30%+? Here's the most reliable way to stop it — disabling the scheduled task that launches it."
thumbnail: "/images/thumbs/best-way-to-fix-compattelrunner-high-cpu.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe is the Microsoft Compatibility Telemetry Runner, a Windows component that collects compatibility and diagnostic data to help Microsoft prepare updates. It's legitimate software, not malware. It normally runs briefly after updates, but a bug or corrupted task can make it run constantly at high CPU, which is when it becomes a problem."
  - q: "Is it safe to disable CompatTelRunner.exe?"
    a: "Yes. Disabling the scheduled task that launches it only stops Microsoft's compatibility data collection on your PC. It doesn't affect Windows updates, security, or any feature you use. Your laptop will still receive and install updates normally — Microsoft just won't get telemetry data from your machine."
  - q: "Why does CompatTelRunner.exe keep coming back after I end it?"
    a: "Because it's launched by a scheduled task called Microsoft Compatibility Appraiser, not by a normal startup entry. Ending the process in Task Manager kills that instance, but the Task Scheduler will launch it again on its next trigger. You have to disable the scheduled task itself to stop it permanently."
  - q: "Will disabling telemetry slow down Windows updates?"
    a: "No. Windows Update works entirely independently of compatibility telemetry. Updates download and install on their normal schedule regardless of whether telemetry is enabled or disabled. The only thing that changes is that Microsoft collects less diagnostic data from your device — update functionality, timing, and reliability are completely unaffected."
---

Few Windows processes inspire as much frustration as CompatTelRunner.exe. It's Microsoft's Compatibility Telemetry Runner — a legitimate component that collects diagnostic data to help prepare Windows updates — but when it malfunctions, it sits at 20 to 40 percent CPU usage for hours, making your laptop hot, loud, and sluggish. Ending it in Task Manager feels satisfying for about ten minutes, until the Task Scheduler dutifully launches it again.

The reason most "fixes" fail is that people treat CompatTelRunner like a normal program. It isn't one. It's launched by a scheduled task buried in the Task Scheduler library, and that task has triggers designed to be persistent. Deleting the executable gets undone by Windows File Protection, renaming it breaks system integrity checks, and killing the process is purely temporary. The reliable fix — the one that actually sticks — is disabling the scheduled task at its source, then cleaning up the conditions that make it run wild.

This guide gives you that fix plus the supporting steps that keep telemetry from coming back after updates. Nothing here affects Windows Update, security, or stability. You're simply telling Windows to stop collecting compatibility data on your machine.

## Why this happens

- **Scheduled task triggers fire repeatedly**: The Microsoft Compatibility Appraiser task is scheduled to run regularly, and on some systems its triggers fire far more often than intended.
- **Corrupted telemetry database**: Damaged data in the telemetry store can cause the runner to loop, retrying the same failed collection endlessly.
- **Post-update appraisal runs long**: After feature updates, the appraiser does a full compatibility scan that can legitimately take a while — but sometimes it never finishes.
- **Conflicting privacy settings**: Partially-disabled telemetry settings can leave the runner in a state where it keeps attempting collection that the settings block.
- **Disk or permission issues**: If the runner can't write its collected data due to disk errors or permission problems, it retries aggressively instead of giving up.
- **Windows 11 24H2 task changes**: Recent Windows builds modified how these tasks trigger, and some systems ended up with duplicate or overlapping triggers.
- **Third-party "debloating" gone wrong**: Aggressive debloat scripts that half-disable telemetry components can leave the runner in a broken loop state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm CompatTelRunner is the actual culprit

Before changing system tasks, verify the process name and its behavior so you're fixing the right thing.

1. Open Task Manager (**Ctrl + Shift + Esc**) and sort the **Processes** tab by CPU.
2. Confirm **Microsoft Compatibility Telemetry** (CompatTelRunner.exe) is the high consumer.
3. Right-click it, choose **Open file location**, and verify it lives in `C:\Windows\System32`. If it's anywhere else, treat it as malware and scan immediately.
4. Note whether the high usage is constant or comes in waves — constant usage points to a stuck task.

If your CPU problem is more general, our [technician's checklist for high CPU](/articles/how-to-fix-high-cpu-usage-on-acer-laptop/) helps identify other common culprits.

### Fix 2: Disable the Microsoft Compatibility Appraiser task

This is the core fix. Disabling the scheduled task stops Windows from launching CompatTelRunner in the first place.

1. Press **Win + R**, type `taskschd.msc`, and press Enter to open Task Scheduler.
2. In the left pane, navigate to **Task Scheduler Library > Microsoft > Windows > Application Experience**.
3. In the center pane, right-click **Microsoft Compatibility Appraiser** and choose **Disable**.
4. Also disable **ProgramDataUpdater** in the same folder — it's a related telemetry task.
5. Navigate to **Task Scheduler Library > Microsoft > Windows > Customer Experience Improvement Program** and disable the **Consolidator** and **UsbCeip** tasks.
6. Restart your laptop.

This stops the scheduled launches. The change survives reboots, though major Windows updates occasionally re-enable these tasks — if the problem returns months later, check here first.

### Fix 3: Set telemetry to the minimum via Group Policy

Reducing the telemetry level at the policy level tells Windows to collect the minimum data, which further reduces the runner's workload on the occasions it does launch.

1. Press **Win + R**, type `gpedit.msc`, and press Enter (Windows 11 Pro).
2. Navigate to **Computer Configuration > Administrative Templates > Windows Components > Data Collection and Preview Builds**.
3. Double-click **Allow Telemetry** (or **Allow Diagnostic Data** on newer builds).
4. Set it to **Enabled** with the option **0 – Security** or the lowest available level.
5. Click OK and restart.

On Windows 11 Home, the same setting lives in **Settings > Privacy & security > Diagnostics & feedback** — turn off optional diagnostic data and delete the collected data.

### Fix 4: Clear the telemetry database

If corrupted telemetry data is causing the retry loop, clearing the store gives the runner a clean slate.

1. Open an **elevated Command Prompt** (search "cmd", right-click, Run as administrator).
2. Run: `net stop DiagTrack` to stop the Diagnostics Tracking Service.
3. Delete the contents of `C:\ProgramData\Microsoft\Diagnosis` (you may need to take ownership of the folder).
4. Run: `net start DiagTrack` to restart the service — or leave it disabled via `services.msc` if you prefer.
5. Restart your laptop and monitor CPU usage.

### Fix 5: Check disk health

Disk errors can cause the telemetry writer to retry endlessly. A quick disk check rules this out.

1. Open an **elevated Command Prompt**.
2. Run `chkdsk C: /f` and agree to run it at next restart.
3. Restart and let the check complete.
4. If chkdsk finds and repairs errors, monitor CompatTelRunner behavior afterward.

### Fix 6: Install pending Windows updates

Ironically, the telemetry runner sometimes misbehaves because the system is waiting on an update it needs. A fully updated system is less likely to trigger appraisal loops.

1. Open **Settings > Windows Update** and install all pending updates.
2. Restart and let the post-update processes complete (give it 30 minutes on AC power).
3. Check Task Manager — the appraiser often settles down once the system is current.
4. If a specific update fails repeatedly, grab it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

### Fix 7: Verify the fix stuck

After all changes, confirm the problem is actually resolved rather than just quieter.

1. Restart your laptop and leave it idle for 15 minutes.
2. Open Task Manager and check that CompatTelRunner.exe isn't consuming CPU.
3. Open Task Scheduler and confirm the Appraiser task still shows **Disabled**.
4. Check again after the next Windows update, since updates can re-enable telemetry tasks.

Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) documents the diagnostic data settings if you want to review what each telemetry level collects. For related background-process cleanup, see our guide on [how to disable background apps on a laptop](/articles/how-to-disable-background-apps-on-laptop/).

## Closing

CompatTelRunner high CPU looks scary but has a simple, permanent fix: disable the scheduled task that launches it, reduce telemetry to minimum, and clear any corrupted data feeding the loop. Unlike killing the process — which never lasts — this approach addresses the actual mechanism, and your laptop goes back to idling quietly.
