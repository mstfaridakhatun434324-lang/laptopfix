---
title: "How to Fix CompatTelRunner High CPU Usage in Windows 11"
slug: how-to-fix-compattelrunner-high-cpu-reddit
date: 2026-09-04
categories: ["performance"]
tags: ["compattelrunner", "high cpu", "telemetry", "windows 11", "compatibility"]
description: "CompatTelRunner.exe hammering your CPU and disk? Understand what the compatibility telemetry runner does and how to tame its scheduled scans."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-reddit.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe — the Microsoft Compatibility Telemetry Runner — collects compatibility data about your system and apps to help Microsoft assess upgrade readiness for Windows updates. It runs on a schedule via Task Scheduler, scanning installed software and drivers. It's legitimate Microsoft software in C:\\Windows\\System32, but its scans are notoriously heavy, pinning CPU and disk for extended periods on many systems."
  - q: "Is it safe to disable CompatTelRunner?"
    a: "Yes. Disabling its scheduled task stops the telemetry scans but doesn't affect Windows updates, security patches, or system stability — those run through separate mechanisms. The only thing you lose is sending Microsoft compatibility telemetry, which has no benefit to you as a user. The Task Scheduler method in Fix 3 is the safe, reversible way to do it."
  - q: "Why does CompatTelRunner run for hours?"
    a: "Its scan inventories every installed application, driver, and device, and on systems with lots of software — or slow disks — that inventory takes a very long time. It also re-runs aggressively around Windows feature updates. If it seems to never finish, it's usually re-triggering: each reboot or update check can restart the scan, creating the impression of one endless run."
  - q: "Will disabling telemetry affect Windows Update?"
    a: "No. Windows Update, Defender definitions, and driver updates all operate independently of compatibility telemetry. Disabling CompatTelRunner's scheduled task only stops the data-collection scans. Your system keeps receiving every update exactly as before — you'll just stop donating CPU cycles to Microsoft's upgrade-planning statistics."
---

CompatTelRunner.exe is one of Windows' most resented background processes: a telemetry collector that scans your entire software inventory and, while doing so, pins CPU and disk like it's rendering video. You didn't ask it to run, you get nothing from its work, and on some systems it seems to run forever. The frustration is understandable — and the fix is straightforward.

CompatTelRunner runs on a Task Scheduler schedule, which means you can control it precisely: see when it runs, limit its impact, or disable it cleanly. This guide starts with confirming the diagnosis, then gives you the full range from gentle throttling to full disable.

## Why this happens

- **Scheduled telemetry scans:** The Microsoft Compatibility Appraiser task triggers heavy inventory scans on a schedule.
- **Pre-update assessment bursts:** Before feature updates, it scans aggressively to assess upgrade readiness.
- **Slow disk amplification:** On HDDs, its file inventory takes far longer and hammers the disk at 100%.
- **Re-triggering loops:** Reboots and update checks restart the scan, making it look endless.
- **Large software inventory:** Many installed apps and drivers mean a longer, heavier scan.
- **Corrupted task state:** A damaged scheduled task can run far more often than intended.
- **Coinciding with other scans:** Running alongside Defender or indexing multiplies the perceived slowdown.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm CompatTelRunner is the actual hog

Open Task Manager during the slowdown, sort by CPU (and check the Disk column too — CompatTelRunner is often a disk hog first, CPU hog second), and confirm CompatTelRunner.exe is the top consumer. Right-click → Open file location to verify it's in `C:\Windows\System32` (legitimate) and not elsewhere (malware impersonation — scan immediately if so). Note the timing: does it start at boot, at a consistent time of day, or around update checks? The schedule pattern tells you which trigger to address in Task Scheduler.

1. Confirm CompatTelRunner.exe tops CPU or Disk in Task Manager.
2. Verify its location is C:\Windows\System32.
3. Note when it starts: boot, scheduled time, or around updates.
4. Check what else is scanning simultaneously.

### Fix 2: Let the current scan finish before judging

If CompatTelRunner just started (after an update or a long off-period), the honest move is letting it complete one full pass — killing it mid-scan just means it restarts later and you've wasted the work. Plug in the laptop, leave it idle for an hour or two, and check whether it finishes and CPU normalizes. If it completes and stays quiet for days, it was a legitimate one-time assessment. If it returns within a day or never seems to finish, continue to the control fixes — that's abnormal behavior worth disabling.

1. Note the scan's start time and let it run undisturbed.
2. Keep the laptop plugged in and idle.
3. Check after 1–2 hours whether it completed.
4. Continue only if it recurs quickly or never finishes.

### Fix 3: Disable the scheduled telemetry task

Open Task Scheduler → **Task Scheduler Library → Microsoft → Windows → Application Experience** and find "Microsoft Compatibility Appraiser." Right-click → Disable. This stops the scheduled scans cleanly without deleting anything — the task can be re-enabled the same way. Also check **Customer Experience Improvement Program** in the same library and disable its tasks if you want the full telemetry quiet. This is the standard, reversible fix that most guides recommend, and it has zero impact on updates or security. Microsoft documents Task Scheduler management in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Task Scheduler → Microsoft → Windows → Application Experience.
2. Right-click Microsoft Compatibility Appraiser → Disable.
3. Optionally disable Customer Experience Improvement Program tasks.
4. Monitor for a week to confirm the scans stopped.

### Fix 4: Reduce diagnostic data sent to Microsoft

Go to **Settings → Privacy & security → Diagnostics & feedback** and set diagnostic data to Required only (not Optional), turn off "Improve inking and typing," and disable tailored experiences. Less telemetry configured means less telemetry work scheduled — it doesn't directly kill CompatTelRunner's task, but it reduces the overall telemetry subsystem activity that often accompanies it. This is also just good privacy hygiene. Combined with Fix 3's task disable, the telemetry pipeline goes fully quiet.

1. Set diagnostic data to Required only.
2. Disable inking/typing improvement and tailored experiences.
3. Confirm no telemetry tasks remain enabled in Task Scheduler.
4. Verify idle CPU and disk stay calm.

### Fix 5: Address it via Group Policy (Pro) or Registry (Home)

For an administrative-level block: on Pro, `gpedit.msc` → **Computer Configuration → Administrative Templates → Windows Components → Data Collection and Preview Builds** → set "Allow Telemetry" to Enabled with option 0 (Security) or 1 (Basic). On Home, set `HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection\AllowTelemetry` (DWORD) = 0. This policy-level setting constrains the whole telemetry subsystem, preventing CompatTelRunner from being re-enabled by updates — which occasionally happens with the Task Scheduler method alone. It's the most durable option for users who want telemetry permanently quiet.

1. Apply the Allow Telemetry policy (0/Security) via gpedit or registry.
2. Restart the laptop.
3. Verify the Compatibility Appraiser task stays disabled.
4. Re-check after the next Windows update.

### Fix 6: Rule out impersonation and companion hogs

If CPU is still high with telemetry disabled, something else is wearing the load. Double-check the process location again (malware sometimes names itself CompatTelRunner.exe in user-writable folders), run a full Defender scan, and look at what runs alongside: Defender full scans and search indexing often coincide with telemetry scans, and fixing those separately may be the real win. The [antimalware high-CPU guide](/articles/antimalware-service-executable-high-cpu-windows-11/) and the [search indexer guide](/articles/how-to-fix-windows-search-indexer-high-cpu/) cover the two most common companions.

1. Re-verify the executable's System32 location.
2. Run a full Microsoft Defender scan.
3. Identify companion processes scanning simultaneously.
4. Fix companions with their dedicated guides.

## Closing

CompatTelRunner is legitimate but gluttonous — a telemetry scanner that treats your CPU like it's Microsoft's. Let one legitimate scan finish, then disable its scheduled task and tighten diagnostic data settings. Updates keep flowing, security is unaffected, and the periodic multi-hour CPU siege simply stops happening.
