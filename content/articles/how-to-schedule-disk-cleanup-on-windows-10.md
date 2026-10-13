---
title: "How to Schedule Disk Cleanup on Windows 10 Automatically"
slug: how-to-schedule-disk-cleanup-on-windows-10
date: 2026-09-23
categories: ["performance"]
tags: ["disk cleanup", "schedule", "windows 10", "storage", "automation"]
description: "Set up automatic Disk Cleanup on Windows 10 with Task Scheduler: configure cleanup profiles once and let Windows reclaim space on a schedule."
thumbnail: "/images/thumbs/how-to-schedule-disk-cleanup-on-windows-10.webp"
faqs:
  - q: "Is Disk Cleanup still available on Windows 10, or is it replaced by Storage Sense?"
    a: "Both exist side by side. Disk Cleanup (cleanmgr.exe) is the classic tool and still fully functional on Windows 10. Storage Sense is the newer automatic feature that handles temp files and Recycle Bin on its own schedule. They complement each other: Storage Sense for continuous light cleaning, scheduled Disk Cleanup for the deep categories like Windows Update cleanup and old system files that Storage Sense handles less aggressively."
  - q: "How often should scheduled Disk Cleanup run?"
    a: "Monthly is the sweet spot for most users — frequent enough to prevent buildup, infrequent enough that each run has something meaningful to clean. Weekly makes sense on machines with heavy temp-file churn (video editing, large downloads). Anything more frequent than weekly wastes time; the categories Disk Cleanup targets accumulate over weeks, not hours."
  - q: "Can scheduled Disk Cleanup delete something important?"
    a: "Not if you configure the profile carefully. The standard safe categories are Temporary files, Recycle Bin, Thumbnails, DirectX Shader Cache, and Delivery Optimization Files. Be cautious with Downloads (never auto-clean it), and only include Windows Update Cleanup and Previous Windows installations after you're certain you won't roll back. The sageset profile you save controls exactly what gets deleted — review it once, then trust it."
  - q: "Why does Task Scheduler say my Disk Cleanup task ran but nothing was cleaned?"
    a: "The usual cause is a misconfigured action: the task runs cleanmgr.exe without the /sagerun argument, so it just opens the GUI (or nothing visible) and exits. The action must be cleanmgr.exe with arguments /sagerun:N matching your /sageset:N profile number. Also check the task runs with highest privileges and whether the user is logged on, or it may lack permission to touch system categories."
---

Disk Cleanup is one of those tools everyone knows and nobody runs. Temporary files pile up, the Recycle Bin quietly holds gigabytes, Windows Update leaves behind superseded packages — and the machine slowly fills until something complains. The manual fix takes two minutes, but remembering to do it is the hard part. The permanent fix is making Windows do it on a schedule, unattended, while you sleep.

Windows 10 gives you everything needed: Disk Cleanup's saved-profile mode (`/sageset` and `/sagerun`) plus Task Scheduler. Configure the cleanup profile once, create the scheduled task once, and the maintenance happens forever. Here's exactly how.

## Why this happens

- **Nobody remembers manual maintenance:** The tool works fine; the human schedule doesn't exist.
- **Temp files accumulate silently:** Applications and installers leave gigabytes in temp directories that nothing ever reclaims.
- **Windows Update residue grows:** Each cumulative update leaves superseded components until cleanup runs.
- **Delivery Optimization cache:** Update files shared with other PCs on the network linger after they're needed.
- **The Recycle Bin is invisible storage:** Deleted files still occupy disk space until the bin is emptied.
- **Thumbnail and shader caches bloat:** Rebuilt automatically, so safe to purge — but they regrow between manual cleanups.
- **Storage Sense gaps:** The built-in automatic cleaner is conservative about system file categories.
- **Low disk space degrades performance:** Windows needs free space for paging, updates, and temp operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check how much space you're actually wasting

Before automating, run Disk Cleanup manually once to see the payoff. Search Start for **Disk Cleanup**, select your system drive, click **Clean up system files**, and review the categories and sizes. If it offers you several gigabytes, the schedule is worth setting up. Note which categories are large — those are the ones your scheduled profile must include. This baseline also tells you whether space is even your problem; if Cleanup finds 200 MB, look elsewhere (the [disk active time guide](/articles/what-to-do-if-disk-active-time-100-percent/) covers performance issues that aren't about free space).

1. Search Start for **Disk Cleanup** and run it.
2. Select the system drive (usually C:).
3. Click **Clean up system files** and wait for the rescan.
4. Note the total reclaimable space and the biggest categories.

### Fix 2: Create a saved cleanup profile with sageset

Open an elevated Command Prompt and run `cleanmgr /sageset:1`. A Disk Cleanup dialog appears with checkboxes — this is your saved profile. Check the safe categories: Temporary files, Recycle Bin, Thumbnails, DirectX Shader Cache, Delivery Optimization Files, Temporary Internet Files, and (if you're confident you won't roll back) Windows Update Cleanup. Leave **Downloads** unchecked — never auto-delete that. Click OK to save. The number (1) is your profile ID; you can create multiple profiles with different numbers.

1. Open an elevated Command Prompt (right-click Start → Command Prompt Admin / Terminal Admin).
2. Run `cleanmgr /sageset:1`.
3. Check the safe categories; leave Downloads unchecked.
4. Click OK — the profile is saved under number 1.

### Fix 3: Test the profile with sagerun

Still in the elevated prompt, run `cleanmgr /sagerun:1`. Disk Cleanup runs silently using your saved profile — no dialogs, no prompts. Wait for the process to finish (watch cleanmgr.exe in Task Manager), then check free space before and after. This confirms the profile works and shows you the real reclaim per run. If it errors or cleans nothing, revisit Fix 2 — the profile number in `/sagerun:1` must match the `/sageset:1` number exactly.

1. In the elevated Command Prompt, run `cleanmgr /sagerun:1`.
2. Wait for cleanmgr.exe to finish in Task Manager.
3. Compare free space before and after.
4. If nothing was cleaned, verify the profile number matches.

### Fix 4: Create the scheduled task

Open Task Scheduler (search Start for it). In the right pane click **Create Basic Task**, name it "Monthly Disk Cleanup," and set the trigger — Monthly on a convenient date, or Weekly if the machine churns temp files heavily. For the action, choose **Start a program**: program `cleanmgr.exe`, arguments `/sagerun:1`. On the final screen, check **Open the Properties dialog**, then in Properties tick **Run with highest privileges** (needed for system file categories) and set it to run whether the user is logged on or not. Microsoft documents Task Scheduler in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Task Scheduler → **Create Basic Task**.
2. Name it "Monthly Disk Cleanup"; set a Monthly (or Weekly) trigger.
3. Action: **Start a program** → `cleanmgr.exe` with arguments `/sagerun:1`.
4. In Properties, tick **Run with highest privileges** and configure for your Windows version.

### Fix 5: Handle the idle and power conditions

In the task's Properties → **Conditions** tab, decide: check **Start the task only if the computer is idle** if you don't want cleanup competing with your work, and check **Wake the computer to run this task** if the machine sleeps overnight — otherwise the task silently never runs on a laptop that closes at night. On the Settings tab, enable **Run task as soon as possible after a scheduled start is missed** so a powered-off laptop still gets cleaned at the next opportunity.

1. Open the task's Properties → **Conditions** tab.
2. Optionally require idle; decide on **Wake the computer to run this task**.
3. On the Settings tab, enable **Run task as soon as possible after a scheduled start is missed**.
4. Click OK and enter credentials if prompted.

### Fix 6: Verify the first scheduled run

Don't trust it blindly — check the first run. After the scheduled time passes, open Task Scheduler, select the task, and check the **History** tab and **Last Run Result** (0x0 means success). Compare free space before and after. If the result shows an error code, the usual suspects are: wrong `/sagerun` number, missing highest privileges, or the laptop being asleep without wake enabled. Fix, then use **Run** on the task manually to confirm it works on demand.

1. After the first scheduled time, check the task's **Last Run Result** (want 0x0).
2. Review the History tab for errors.
3. Compare disk free space before and after.
4. Right-click the task → **Run** to test on demand after any fix.

### Fix 7: Layer Storage Sense for continuous light cleaning

As a complement, enable **Settings → System → Storage → Storage Sense** and configure it: run when disk space is low, delete temp files apps aren't using, and auto-empty the Recycle Bin after 30 days. Storage Sense handles the continuous drip; your scheduled Disk Cleanup handles the deep monthly categories. Together they cover everything with zero ongoing effort. If you're on Windows 11 rather than 10, the [SSD boot performance guide](/articles/how-do-i-fix-windows-11-boot-time-slow-ssd/) covers the equivalent maintenance mindset for the newer OS.

1. Open **Settings → System → Storage**.
2. Turn on **Storage Sense** and click it for options.
3. Set cleanup schedules for temp files and Recycle Bin.
4. Leave the scheduled Disk Cleanup task in place for deep cleaning.

## Closing

Scheduled Disk Cleanup is a twenty-minute setup that pays off forever: one saved profile, one scheduled task, and the gigabytes that used to accumulate silently get reclaimed on autopilot. Verify the first run, layer Storage Sense on top for the daily drip, and cross "mysteriously full drive" off your list of recurring problems. The best maintenance is the kind you never have to remember.
