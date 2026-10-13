---
title: "Fix CompatTelRunner.exe High CPU in Windows 11 24H2"
slug: how-to-fix-compattelrunner-high-cpu-in-windows-11-24h2
date: 2026-09-18
categories: ["performance"]
tags: ["compattelrunner.exe high cpu", "telemetry", "windows 11 24h2", "compatibility telemetry", "cpu fix"]
description: "CompatTelRunner.exe spiking CPU after 24H2? Understand what the telemetry runner does, then tame it safely without breaking Windows Update."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "It is Microsoft's Compatibility Telemetry Runner: a legitimate Windows component that scans your installed apps and drivers to verify they will survive the next Windows update. It is supposed to run briefly on a schedule. After the 24H2 update it can get stuck re-scanning endlessly, holding 30 to 60 percent CPU for hours — a corrupted telemetry cache is the usual reason."
  - q: "Is it safe to disable CompatTelRunner.exe?"
    a: "Yes. Disabling its scheduled task in Task Scheduler stops the background scans without affecting Windows Update, activation, or any feature — updates run their own compatibility checks at install time. The only thing you lose is sending Microsoft pre-update telemetry about your machine, which affects Microsoft's data, not your PC's stability."
  - q: "Why does it run so long after the 24H2 update?"
    a: "The feature update resets telemetry schedules to aggressive defaults and can corrupt the existing telemetry cache. With a damaged cache, the runner never recognizes its work as done and rescans the whole system repeatedly. Clearing the diagnostic data cache and rescheduling — or disabling — the task breaks the loop."
  - q: "Will disabling telemetry break anything?"
    a: "No. Disabling the Microsoft Compatibility Appraiser task only stops background compatibility scans. Windows Update, security patches, activation, and all features continue working normally. Microsoft simply receives less diagnostic data from your machine. It is a supported configuration change, not a hack."
---

CompatTelRunner.exe — the Microsoft Compatibility Telemetry Runner — has one of the most suspicious names in Task Manager, and after the Windows 11 24H2 update it started living up to it: pinning CPUs at 30 to 60 percent for hours, sometimes days, with no visible progress and no off switch in sight. It looks like spyware. It is actually just Microsoft's compatibility checker stuck in a loop.

The runner's job is legitimate: scan your apps and drivers to make sure the next Windows update will not break them. The problem is that 24H2 can leave it re-scanning endlessly — a corrupted telemetry cache or a reset schedule turns a periodic task into a permanent one.

You have two paths: fix it so it runs properly, or disable the scheduled task so it never runs at all. This guide covers both, in that order.

## Why this happens

- **Reset telemetry schedule after 24H2:** The feature update restores aggressive default schedules.

- **Corrupted telemetry cache:** Damaged cache data makes the runner rescan forever instead of completing.

- **Huge app/driver inventory:** Systems with many installed programs take far longer per scan.

- **Stuck scheduled task:** The Microsoft Compatibility Appraiser task hangs mid-run and restarts repeatedly.

- **Feedback diagnostics set to full:** Higher diagnostic levels trigger more frequent and deeper telemetry runs.

- **Conflicting privacy tools:** Third-party tools blocking telemetry endpoints can cause retry loops. Similar stuck-task behavior: [CompatTelRunner high CPU after the Windows 11 update](/articles/how-to-fix-compattelrunner-high-cpu-after-windows-11-update/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm CompatTelRunner is the hog

Telemetry runs under a specific executable. Verify it before changing system task schedules.

1. Open Task Manager with Ctrl plus Shift plus Esc and sort by CPU.
2. Find CompatTelRunner.exe and note sustained usage over five minutes.
3. Open Task Scheduler and navigate to Microsoft, Windows, Application Experience.
4. Check whether 'Microsoft Compatibility Appraiser' shows as currently running.
5. If it is running with high CPU and never finishes, it is stuck — continue.

### Fix 2: Reduce diagnostic data to Required

Lowering the diagnostic level reduces how often and how deeply telemetry runs. A legitimate, supported setting.

1. Open Settings, Privacy and security, Diagnostics and feedback.
2. Set Diagnostic data to 'Required diagnostic data'.
3. Turn off 'Improve inking and typing' and 'Tailored experiences'.
4. Click 'Delete diagnostic data' to clear the existing cache.
5. Restart the laptop.
6. Monitor CompatTelRunner.exe over the next few hours.

### Fix 3: Reschedule the Appraiser to rare off-hours

If you prefer keeping telemetry working, confine it to a monthly 3 AM run instead of letting it fire at will.

1. Open Task Scheduler, Microsoft, Windows, Application Experience.
2. Right-click Microsoft Compatibility Appraiser and choose Properties.
3. On the Triggers tab, replace triggers with a single monthly trigger at 3:00 AM.
4. On Conditions, require idle and AC power.
5. On Settings, set 'Stop the task if it runs longer than' to 1 hour.
6. Click OK and verify the next run time looks sane.

### Fix 4: Disable the Appraiser task entirely

The clean, supported off switch. Windows Update performs its own compatibility checks, so updates keep working.

1. In Task Scheduler, Microsoft, Windows, Application Experience.
2. Right-click Microsoft Compatibility Appraiser and choose Disable.
3. Also disable 'ProgramDataUpdater' in the same folder if it shows high activity.
4. Restart the laptop.
5. Confirm CompatTelRunner.exe no longer appears in Task Manager.
6. Check the [Windows support hub](https://support.microsoft.com/en-us/windows) if a future update re-enables it — re-disable after major updates.

### Fix 5: Clear the telemetry cache via Disk Cleanup

If you disabled the task but remnants still run, a corrupted cache may be the trigger. Clearing it removes the loop fuel.

1. Run Disk Cleanup as administrator on C:.
2. Check all temporary and diagnostic data categories.
3. Also clear C:\Windows\Temp and the SoftwareDistribution download cache carefully.
4. Run `sfc /scannow` in an admin Command Prompt to rule out system file damage.
5. Restart and verify the process stays gone.

### Fix 6: Block re-enablement after updates

Feature updates sometimes re-enable the Appraiser task. A quick post-update check keeps it off permanently.

1. After each Windows feature update, revisit Task Scheduler's Application Experience folder.
2. Re-disable Microsoft Compatibility Appraiser if the update re-enabled it.
3. Consider a small scheduled task of your own that disables it monthly — or just check manually.
4. Keep diagnostic data at Required so even re-enabled runs are minimal.
5. Verify in Task Manager that no telemetry CPU spikes return.

### Fix 7: Use Group Policy to tame telemetry (Pro editions)

On Windows 11 Pro, Group Policy gives you a supported, persistent way to limit telemetry that survives feature updates better than Task Scheduler tweaks alone. Set it once and the runner stays quiet through updates.

1. Press Win plus R, type `gpedit.msc`, and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Data Collection and Preview Builds.
3. Open 'Allow Diagnostic Data' and set it to Enabled with the options value at the lowest setting.
4. Also enable 'Disable Microsoft consumer experiences' while you are there.
5. Run `gpupdate /force` in an admin Command Prompt.
6. Restart and confirm CompatTelRunner.exe stays quiet in Task Manager.

## Closing

CompatTelRunner.exe is legitimate software behaving badly — a compatibility checker that forgot how to finish. Reduce the diagnostic level, reschedule or disable its task, and the CPU spikes stop without affecting Windows Update one bit. Check back after each feature update, since those love to turn it back on. Telemetry is not the only background chatter worth quieting — [turning off Windows tips and suggestions](/articles/how-to-turn-off-windows-tips-and-suggestions-in-windows-11-24h2/) cuts another stream of it. A quick Task Scheduler check after each Patch Tuesday takes thirty seconds and keeps the runner from quietly returning. Quiet machines tend to stay quiet.
