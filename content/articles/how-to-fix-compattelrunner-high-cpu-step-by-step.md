---
title: "How to Fix CompatTelRunner High CPU, Step by Step"
slug: how-to-fix-compattelrunner-high-cpu-step-by-step
date: 2026-09-07
categories: ["performance"]
tags: ["compattelrunner.exe", "high cpu", "telemetry", "compatibility", "windows 11"]
description: "CompatTelRunner.exe hogging CPU and disk? Step-by-step guide to calming Windows compatibility telemetry without breaking updates."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-step-by-step.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe (Microsoft Compatibility Telemetry) collects compatibility data about your system — installed apps, drivers, and devices — to help Microsoft assess whether your PC is ready for Windows feature updates. It runs via scheduled tasks, typically around update periods. Sustained high CPU/disk from it means it's stuck scanning, usually due to a problematic app inventory or corrupt telemetry state."
  - q: "Is CompatTelRunner.exe a virus?"
    a: "The legitimate file is C:\\Windows\\System32\\CompatTelRunner.exe, signed by Microsoft. It's a genuine Windows component, not malware — though its disk-heavy scanning behavior makes people suspicious. Verify via Task Manager > Details > Open file location. Anything running from a different path under this name should be scanned immediately."
  - q: "Will disabling CompatTelRunner break Windows Update?"
    a: "Disabling the telemetry scheduled task doesn't break update delivery — Windows Update works independently. What you lose is Microsoft's compatibility assessment for feature updates on your specific machine, which is advisory data. Monthly security updates are unaffected. Many users disable it with no update issues whatsoever."
  - q: "Why does it use 100% disk instead of CPU on some PCs?"
    a: "CompatTelRunner inventories installed software by scanning the disk heavily — on systems with hard drives (or nearly-full SSDs), the disk becomes the bottleneck before the CPU does. The 100%-disk symptom and the high-CPU symptom are the same process hitting different hardware limits. The fixes below address both, since they target the scanning behavior itself."
---

`CompatTelRunner.exe` — Microsoft Compatibility Telemetry — has one of the worst reputations in Windows: it wakes up uninvited, hammers your disk and CPU for an hour, and its name sounds like spyware. In reality it's the component that inventories your apps and drivers so Microsoft can tell whether a feature update will break your machine. Useful in theory; in practice, when it gets stuck, it's a resource hog with no visible progress bar.

The stuck pattern is recognizable: CompatTelRunner runs at high CPU/disk for hours, far beyond a normal telemetry pass, often triggered by its scheduled task firing daily instead of occasionally. This guide walks through calming it down step by step — from the gentle (let it finish) to the decisive (disable the task). For related telemetry-adjacent CPU issues, see [fixing Runtime Broker](/articles/best-way-to-fix-runtime-broker-high-cpu/); for the broader high-CPU triage, [our CompatTelRunner overview](/articles/best-way-to-fix-compattelrunner-high-cpu/).

## Why this happens

- **Scheduled task firing too often**: The telemetry task misconfigured or re-triggered to run daily instead of occasionally.
- **Huge software inventory**: Hundreds of installed apps (or portable app collections) make each scan pass very expensive.
- **Corrupt telemetry state**: Damaged telemetry database causes the scan to restart from scratch repeatedly.
- **Scanning network/removable drives**: Inventory passes wandering onto slow network shares or USB drives.
- **Conflict with disk-intensive work**: Telemetry scanning while you're gaming or editing multiplies the perceived impact.
- **Pre-feature-update assessment bursts**: Microsoft triggers deeper scans ahead of feature updates — legitimate but heavy.
- **Failing disk amplifying scan cost**: A disk with bad sectors turns a routine inventory into a retry storm.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's legitimate and check the trigger

Confirm what you're dealing with.

1. In **Task Manager** > **Details**, right-click **CompatTelRunner.exe** > **Open file location** — must be `C:\Windows\System32`, signed by Microsoft.
2. Note the resource profile: high **Disk** (HDD systems), high **CPU** (SSD systems), or both. Also note duration — under an hour occasionally is normal-ish; daily multi-hour runs are not.
3. Open **Task Scheduler** > **Task Scheduler Library** > **Microsoft** > **Windows** > **Application Experience** — find **Microsoft Compatibility Appraiser**. Check the **History** tab: how often has it actually run?
4. Check the **Triggers** tab — a healthy setup triggers occasionally; a task set to daily (or with a corrupted trigger firing constantly) explains the symptom.
5. If the task history shows it starting, "running" for hours, then starting again without completing — it's stuck mid-scan (Fixes 2–3).

### Fix 2: Let one full pass complete cleanly

Sometimes it's just never been allowed to finish.

1. The appraiser is designed to run during idle — if you always shut down or sleep the laptop quickly, it restarts its scan every session and never completes.
2. Plug in the laptop, set **Settings** > **System** > **Power & battery** > **Screen and sleep** to generous timeouts, and leave the machine idle for 2 hours.
3. Watch Task Manager — CompatTelRunner should eventually finish and vanish. One completed pass often quiets it for weeks.
4. If it runs the full 2 hours without finishing, it's genuinely stuck — proceed to Fix 3.
5. Don't "help" by ending the task mid-scan repeatedly — each kill restarts the inventory from scratch, which is how occasional scans become perpetual ones.

### Fix 3: Clear the telemetry state and reduce scan scope

Unstick the corrupted scan.

1. In **Task Scheduler** (same Application Experience path), right-click **Microsoft Compatibility Appraiser** > **Disable** temporarily.
2. End any running **CompatTelRunner.exe** in Task Manager.
3. Clear the telemetry cache: navigate to `C:\Windows\System32\CompatTelRunner` state data via `C:\ProgramData\Microsoft\Diagnosis` — you can safely delete the contents of the **DownloadedSettings** and event-transient folders; Windows regenerates them. (Don't delete the folders themselves.)
4. Re-enable the task, then right-click > **Run** to trigger one clean pass while you watch — it should now progress and complete.
5. If you have portable-app collections or huge folders of executables, consider whether the appraiser needs to inventory them — excluding such folders from **Windows Search indexing** also reduces some inventory overlap.

### Fix 4: Disable the Compatibility Appraiser task

The decisive fix for recurring episodes.

1. In **Task Scheduler** > **Microsoft** > **Windows** > **Application Experience**, right-click **Microsoft Compatibility Appraiser** > **Disable**.
2. Also review **ProgramDataUpdater** in the same folder — it's the related telemetry task; disable it too if CompatTelRunner episodes persist.
3. Verify over the next week: no CompatTelRunner in Task Manager, Windows Update still delivering monthly updates normally (**Settings** > **Windows Update** > **Check for updates**).
4. Understand what you gave up: Microsoft's pre-flight compatibility check for *feature* updates on your machine. Monthly security updates are unaffected. Most users notice zero difference.
5. If a future feature update fails with a compatibility error, re-enable the task temporarily, let it run once, then disable again.

### Fix 5: Reduce diagnostic data at the source

Less telemetry overall means less telemetry processing.

1. **Settings** > **Privacy & security** > **Diagnostics & feedback** > set **Diagnostic data** to **Required** only (not Optional) — this reduces what the telemetry pipeline collects and processes.
2. Turn off **Tailored experiences** and **Improve inking and typing** on the same page.
3. Click **Delete** next to **Delete diagnostic data** to clear the backlog the system is chewing through.
4. In **Feedback Hub** settings (or the same Diagnostics page), set feedback frequency to **Never** — fewer prompts, less background activity.
5. These settings are also the privacy-respecting choice — performance and privacy aligned for once.

### Fix 6: Check disk health — the hidden amplifier

A struggling disk turns telemetry into torture.

1. If CompatTelRunner shows 100% disk with modest CPU, open **Task Manager** > **Performance** > disk and check **Average response time** — consistently over 100ms means the disk is the bottleneck, not the telemetry.
2. Run `chkdsk C: /scan` in an elevated terminal to check for file-system errors the scanner might be tripping over.
3. Check drive health with **CrystalDiskInfo** (free) — reallocated sectors or warnings mean the disk is amplifying every scan into a retry storm.
4. For HDDs: ensure the drive isn't nearly full (keep 15%+ free) and run **Optimize** (defrag) — a fragmented HDD makes inventory scans brutally slow.
5. If the disk is failing, no telemetry tweak fixes the root cause — back up and replace. Our [SSD troubleshooting guide](/articles/best-way-to-fix-ssd-slow-on-windows-11/) covers the replacement decision.

### Fix 7: Registry-level control (if the task keeps re-enabling)

For systems where the task mysteriously returns.

1. Some Windows updates re-enable the Appraiser task — if yours keeps coming back, set the registry guard: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection`, create DWORD **AllowTelemetry** = `0` (Security/Enterprise) or `1` (Basic). Back up first.
2. Alternatively, take ownership discipline: in Task Scheduler, right-click the task > **Properties** > change the configured user or remove triggers rather than just disabling — disabled tasks survive updates better when their triggers are also cleared.
3. Verify after the next Patch Tuesday that the task stayed disabled — that's the real test.
4. Keep a note of what you changed (a text file in Documents works) so future-you isn't mystified.
5. Microsoft documents telemetry controls on the [Windows support hub](https://support.microsoft.com/en-us/windows) — the official knobs are preferable to forum registry hacks.

## Closing

CompatTelRunner high CPU is Windows' compatibility inventory getting stuck or over-scheduled — not malware, not a conspiracy. Let one clean pass finish; if it can't, clear its state; if it won't stay quiet, disable the scheduled task and reduce diagnostic data. Monthly updates keep flowing, your disk stops getting flogged by inventory scans, and the process with the suspicious name goes back to the obscurity it deserves.
