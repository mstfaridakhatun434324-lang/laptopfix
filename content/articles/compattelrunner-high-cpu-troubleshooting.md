---
title: "CompatTelRunner.exe High CPU? Fix the Compatibility Telemetry Runner"
slug: compattelrunner-high-cpu-troubleshooting
date: 2026-09-01
categories: ["performance"]
tags: ["compattelrunner.exe", "compatibility telemetry", "high cpu", "high disk", "troubleshooting"]
description: "CompatTelRunner.exe hammering your CPU and disk? Learn what the Microsoft Compatibility Telemetry runner does and how to tame it safely."
thumbnail: "/images/thumbs/compattelrunner-high-cpu-troubleshooting.webp"
faqs:
  - q: "What is CompatTelRunner.exe and is it safe?"
    a: "CompatTelRunner.exe is Microsoft's Compatibility Telemetry runner — a legitimate Windows process that collects compatibility data to assess whether your machine is ready for Windows updates. It lives in System32 and is safe. High CPU/disk from it means it's actively scanning your system; the problem is only when it runs excessively long or too often, which the fixes below address."
  - q: "Can I disable CompatTelRunner.exe completely?"
    a: "You can't delete it (Windows protects and restores it), but you can disable the scheduled task that launches it and turn off the telemetry that triggers it. That's the supported approach: Task Scheduler, Microsoft, Windows, Application Experience — disable the Microsoft Compatibility Appraiser task. Windows Update keeps working; you just stop the periodic compatibility scans."
  - q: "Does disabling telemetry break Windows Update?"
    a: "No. Disabling the Compatibility Appraiser task and setting telemetry to the minimum (Required diagnostic data) does not block security or feature updates. The appraiser only assesses upgrade readiness; updates themselves download and install normally. Microsoft documents diagnostic data settings on the Windows support site for confirmation."
  - q: "Why does CompatTelRunner use 100% disk on older laptops?"
    a: "Because compatibility scanning reads enormous numbers of files to inventory software and drivers — on HDDs or nearly-full SSDs, that scan saturates the disk for a long time. The scan is legitimate work, just heavy. Scheduling it for idle hours, or disabling the task if you don't need upgrade assessments, removes the disk storm."
---

**CompatTelRunner.exe** — the Microsoft Compatibility Telemetry runner — has a talent for picking the worst moments: it fires up unannounced, pins the disk to 100%, drags the CPU along, and turns a working laptop into a slideshow for an hour. It's legitimate — Windows uses it to assess whether your machine can take the next feature update — but "legitimate" doesn't help when you're trying to work. The good news: this is one of the most fixable background hogs in Windows, because its trigger is a single scheduled task you control.

This guide shows you how to confirm it's the appraiser task, tame its schedule, reduce its workload, and disable it cleanly if you choose.

## Why this happens

- **Scheduled compatibility scans:** The Microsoft Compatibility Appraiser task runs periodically, scanning installed software and drivers for upgrade readiness.
- **Post-update assessment waves:** After Patch Tuesday or before feature updates, Microsoft triggers assessment scans across fleets.
- **Full inventory on huge software sets:** Machines with lots of installed programs take far longer to inventory.
- **Slow disk amplifies the scan:** HDDs and full SSDs turn a 20-minute scan into a 2-hour disk storm.
- **Corrupted telemetry state:** A damaged telemetry database makes the runner rescan repeatedly without completing.
- **Conflicting "debloating":** Half-disabled telemetry components can leave the runner in a retry loop.
- **Multiple user profiles:** The scan inventories per-user software too — many profiles multiply the work.
- **Stuck scan never completing:** A scan that can't finish (permissions, corrupted files) reruns on its trigger schedule indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the scheduled task is the trigger

Task Manager → Details: verify CompatTelRunner.exe's path is System32 and note when it runs — does it start at consistent times (task-triggered) or randomly? Then Task Scheduler → Task Scheduler Library → Microsoft → Windows → Application Experience → check the "Microsoft Compatibility Appraiser" task's triggers and last-run time. If the process starts match the task's triggers, you've confirmed the mechanism. Everything after this is about managing that task. The [post-update variant](/articles/how-to-fix-compattelrunner-high-cpu-after-windows-11-update/) covers update-triggered waves specifically.

1. Verify CompatTelRunner.exe runs from System32.
2. Note its start times — consistent times suggest task triggers.
3. Task Scheduler → Application Experience → check the Appraiser task.
4. Correlate process starts with task triggers.

### Fix 2: Let one full scan complete

If the appraiser is mid-scan, the pragmatic move is letting it finish: plug in, leave the laptop idle for 2–3 hours, and don't interrupt. An interrupted scan restarts from scratch next trigger — interrupting is how a 30-minute scan becomes a daily 2-hour ordeal. Check Task Scheduler afterward: "Last Run Result" should show success (0x0). One clean completion often quiets the runner for weeks, since the assessment data stays fresh. Only proceed to disabling if scans recur excessively after successful completion.

1. Plug in; leave the laptop idle 2–3 hours.
2. Don't interrupt the scan — interruption restarts it.
3. Verify Task Scheduler shows Last Run Result 0x0 (success).
4. Monitor: weeks of quiet means the scan cycle is healthy.

### Fix 3: Reschedule the task to idle hours

Task Scheduler → Microsoft Compatibility Appraiser → Properties → Triggers: change the schedule to run at 3 AM (or whenever you're asleep), and on the Conditions tab check "Start the task only if the computer is idle." This keeps the assessments happening — useful for genuine upgrade-readiness data — while moving the disk storm out of your working hours. It's the best compromise for users who don't want to disable system functions: same work, civilized timing.

1. Appraiser task → Properties → Triggers → reschedule to idle hours.
2. Conditions tab → "Start only if computer is idle."
3. Also set "Stop if the computer ceases to be idle."
4. Verify the next run happens overnight, not mid-workday.

### Fix 4: Reduce diagnostic data to minimum

Settings → Privacy & security → Diagnostics & feedback → set "Send optional diagnostic data" to Off (keep Required on). Less telemetry configured means less telemetry work triggered. While there, turn off "Tailored experiences" and delete diagnostic data. This doesn't disable the appraiser task directly, but it reduces the broader telemetry workload that often accompanies CompatTelRunner activity. Microsoft documents these settings on the [Windows support site](https://support.microsoft.com/en-us/windows).

1. Diagnostics & feedback → optional diagnostic data Off.
2. Tailored experiences → Off; delete diagnostic data.
3. Reboot; observe runner frequency over the next week.
4. Reduced activity confirms telemetry volume was a factor.

### Fix 5: Disable the Appraiser task

If you've decided the assessments aren't worth the disruption: Task Scheduler → Microsoft Compatibility Appraiser → right-click → Disable. Also disable related tasks in the same folder ("ProgramDataUpdater" if present and problematic). Windows Update continues normally — the appraiser only feeds upgrade-readiness analytics. Note the change somewhere; after major feature updates, verify it stayed disabled, since updates occasionally re-enable telemetry tasks. This is the supported off switch — no file deletion, no registry hacking.

1. Task Scheduler → Application Experience → Disable the Appraiser task.
2. Disable sibling telemetry tasks if they're also disruptive.
3. Verify Windows Update still works normally.
4. Re-check after feature updates (they can re-enable it).

### Fix 6: Address the disk bottleneck

If you keep the task enabled but the scan cripples the machine, the disk is the amplifier: check free space (target 20%+ free on C:), run Disk Cleanup, and check SMART health — a struggling drive turns every scan into an ordeal. On HDD-based laptops, this is also the strongest argument for an SSD upgrade: the same compatibility scan that takes 2 hours on a spinning disk finishes in 15 minutes on an SSD. The [Windows Modules Installer guide](/articles/how-to-fix-windows-modules-installer-high-cpu-step-by-step/) covers similar disk-amplified background work.

1. Free C: space to 20%+; run Disk Cleanup.
2. Check SMART health — rule out a failing drive.
3. On HDDs: seriously consider the SSD upgrade.
4. Re-time a scan after disk improvements.

### Fix 7: Clean up the software inventory it's scanning

The appraiser inventories installed software — fewer programs, faster scan. Uninstall what you don't use (Settings → Apps), remove ancient toolbars and trial software, and clean dead startup entries. Also run DISM RestoreHealth + SFC: corrupted system state can make telemetry scans loop without completing, and repairing it lets the scan finish cleanly. A lean, healthy system is quick to inventory; a cluttered, damaged one keeps the runner busy indefinitely.

1. Uninstall unused programs via Settings → Apps.
2. Remove ancient toolbars/trialware remnants.
3. DISM RestoreHealth + SFC to fix scan-blocking corruption.
4. Trigger the appraiser manually once; verify it completes.

## Closing

CompatTelRunner.exe is Windows doing legitimate homework at illegitimate hours. Confirm the scheduled task, let one scan finish cleanly, then choose your stance: reschedule it to the night, minimize the telemetry feeding it, or disable the task outright. Any of the three beats the default — a surprise disk storm in the middle of your workday. Pick the one that matches how much you value the upgrade-readiness data, and the runner stops being a problem.
