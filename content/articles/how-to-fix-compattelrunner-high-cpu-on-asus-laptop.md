---
title: "CompatTelRunner.exe High CPU on an ASUS Laptop? How to Tame It"
slug: how-to-fix-compattelrunner-high-cpu-on-asus-laptop
date: 2026-09-02
categories: ["performance"]
tags: ["compattelrunner", "telemetry", "high cpu", "asus laptop", "windows compatibility"]
description: "CompatTelRunner.exe spiking CPU on your ASUS laptop? Learn what Microsoft's compatibility telemetry does and how to calm it without breaking updates."
thumbnail: "/images/thumbs/how-to-fix-compattelrunner-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "What is CompatTelRunner.exe?"
    a: "CompatTelRunner.exe is Microsoft's Compatibility Telemetry Runner — part of the Windows Customer Experience Improvement Program. It scans your installed applications, drivers, and devices to assess whether your PC is ready for the next Windows feature update, then reports anonymized compatibility data to Microsoft. It typically runs after Patch Tuesday, before feature updates, and occasionally on a schedule. High CPU during these scans is normal; the problem is when it runs constantly or gets stuck."
  - q: "Is CompatTelRunner.exe a virus?"
    a: "No — it's a legitimate Microsoft-signed component located in C:\\Windows\\System32. However, malware sometimes disguises itself with similar names, so verify the location: right-click the process in Task Manager > Open file location. If it opens anywhere other than System32, treat it as suspicious and run a full antivirus scan immediately. The genuine file is digitally signed by Microsoft."
  - q: "Can I safely disable CompatTelRunner.exe?"
    a: "You can reduce or disable its scheduled runs without breaking Windows Update — telemetry collection is separate from the update mechanism itself. Disabling the scheduled task or limiting diagnostic data doesn't stop security updates. What you shouldn't do is delete the executable from System32; that can cause servicing errors. The task-scheduler and Group Policy approaches below are the safe methods."
  - q: "Why does CompatTelRunner.exe run so often on my ASUS laptop?"
    a: "Frequency spikes before Windows feature updates (Microsoft assesses readiness aggressively in the weeks prior) and after major software changes. ASUS laptops with lots of preinstalled utilities give the scanner more to inventory, which extends each run. If it seems to run daily, the scheduled task may be misconfigured or a previous scan may be failing and retrying — both fixable with the steps below."
---

Spotting `CompatTelRunner.exe` at the top of Task Manager with 30–60% CPU is unsettling — the name sounds like malware, and it's doing *something* intensive with your files. It's actually Microsoft's compatibility telemetry: Windows scanning your apps and drivers to decide if your ASUS laptop is ready for the next feature update. Legitimate, but not something that should be grinding away for hours on end.

The nuance most guides miss: CompatTelRunner.exe high CPU comes in two flavors. The normal flavor runs for 10–30 minutes after updates or on Microsoft's schedule, then stops. The broken flavor runs constantly, restarts immediately after ending, or never completes its scan — usually because a previous scan crashed, the task is misconfigured, or it's choking on a specific application it can't inventory. This guide helps you identify which flavor you have and fixes the broken one.

If your ASUS laptop is slow overall, our [Windows 11 high memory usage fix](/articles/windows-11-high-memory-usage-fix/) and [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) guides cover the companion issues.

## Why this happens

- **Scheduled compatibility scan running**: The normal trigger — Microsoft's scheduled telemetry inventory, especially before feature updates.
- **A crashed scan retrying in a loop**: A scan that fails partway restarts repeatedly, producing endless CPU usage.
- **Large software inventory**: Many installed apps (common on ASUS laptops with preinstalled utilities) make each scan longer and heavier.
- **Corrupt telemetry database**: Damaged diagnostic data stores cause the scanner to redo work constantly.
- **Misconfigured scheduled task**: Task Scheduler settings that re-trigger the scan too aggressively.
- **Disk slowness amplifying the scan**: The inventory is disk-heavy; slow or full drives stretch a 15-minute scan into an hour.
- **Impostor malware**: Rare, but worth ruling out — verify the file location is System32.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's legitimate and check whether it's actually stuck

Rule out malware and confirm the problem before changing anything.

1. In Task Manager, right-click **CompatTelRunner.exe** (it may show as "Microsoft Compatibility Telemetry") > **Open file location** — it must resolve to `C:\Windows\System32`. Anywhere else means malware: run a full Windows Security scan immediately.
2. Right-click > **Properties** > **Digital Signatures** — confirm it's signed by Microsoft Corporation.
3. Note when the high CPU started and whether it stops on its own within 30–60 minutes. Self-limiting runs are normal — only persistent runs need fixing.
4. Check **Settings** > **Windows Update** — if a feature update is pending or recently installed, frequent telemetry runs are expected and will settle down within a week or two.
5. If it's been running at high CPU for hours across multiple days with no update activity, it's stuck — continue.

### Fix 2: Let the current scan finish under good conditions

Sometimes the fastest fix is giving it one clean run.

1. Plug in the laptop, close heavy applications, and leave it alone for 45–60 minutes — a scan competing with your workload takes far longer and uses more CPU.
2. Make sure you have at least 10 GB free on C: — the telemetry database needs working room.
3. Don't end the task repeatedly — each kill can corrupt the in-progress inventory, forcing a full rescan from scratch (which is likely how the loop started).
4. After one uninterrupted run, check Task Manager — completed scans usually don't recur for days or weeks.
5. If it *still* restarts immediately after visibly finishing, the scheduled task configuration is the problem — move to Fix 3.

### Fix 3: Disable the scheduled telemetry tasks

The most effective fix for the endlessly recurring case.

1. Open **Task Scheduler** (`taskschd.msc`) > navigate to **Task Scheduler Library** > **Microsoft** > **Windows** > **Application Experience**.
2. You'll see tasks including **Microsoft Compatibility Appraiser** — right-click it > **Disable**. This is the task that launches CompatTelRunner.exe on schedule.
3. Also check **Task Scheduler Library** > **Microsoft** > **Windows** > **Customer Experience Improvement Program** — disable the **Consolidator** and **UsbCeip** tasks if present.
4. This does not break Windows Update — feature updates will still download and install; Microsoft just won't get your compatibility telemetry ahead of time.
5. Restart and monitor for 24 hours — CompatTelRunner.exe should no longer launch on its own. (It may still run briefly during actual feature-update installs, which is fine.)

### Fix 4: Limit diagnostic data collection

Reduce what Windows collects, which reduces the telemetry workload.

1. Go to **Settings** > **Privacy & security** > **Diagnostics & feedback**.
2. Set **Diagnostic data** to the minimum available option — less data collected means less telemetry processing overall.
3. Turn off **Tailored experiences** and **Improve inking and typing** if you don't use those features — each feeds the telemetry pipeline.
4. Under **Feedback**, set frequency to **Never** if desired — one less background task.
5. Note: on some Windows 11 editions the minimum diagnostic setting still allows basic data; that's fine — the goal is reducing the optional telemetry that drives CompatTelRunner.exe's heaviest scans.

### Fix 5: Use Group Policy to disable telemetry (Pro/Enterprise)

For Windows 11 Pro users who want a system-level switch.

1. Press **Win + R**, type `gpedit.msc`, press Enter.
2. Navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Data Collection and Preview Builds**.
3. Open **Allow Telemetry** (or "Allow Diagnostic Data" on newer builds), set it to **Enabled** with the lowest option (Security/Basic), and click OK.
4. Then navigate to **Computer Configuration** > **Administrative Templates** > **System** > **Internet Communication Management** > **Internet Communication settings** and set **Turn off Windows Customer Experience Improvement Program** to **Enabled**.
5. Run `gpupdate /force` in Terminal, then restart. Verify in Task Scheduler that the Application Experience tasks stay disabled.

### Fix 6: Clean up the software inventory it's choking on

A leaner app list means faster, less frequent scans.

1. Go to **Settings** > **Apps** > **Installed apps** — uninstall ASUS-preinstalled utilities you don't use (duplicate photo apps, trial software, old game launchers). Each installed app is something the scanner must inventory.
2. Remove old, abandoned software generally — the scanner struggles most with ancient apps that have broken uninstall entries.
3. Run Disk Cleanup as administrator and clear temporary files — a cleaner disk speeds the inventory pass.
4. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) if you suspect a specific app is crashing the scanner — searching the app name plus "compatibility telemetry" sometimes reveals known conflicts.
5. After cleanup, manually trigger one scan to confirm it completes: re-enable the Appraiser task temporarily, run it, watch it finish, then disable it again.

### Fix 7: Repair system files if the scanner itself is corrupt

When CompatTelRunner.exe crashes and restarts endlessly, the component may be damaged.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Check the Application event log (**Event Viewer** > **Windows Logs** > **Application**) for errors mentioning CompatTelRunner or telemetry around the times of high CPU — the faulting module name points to the corrupt component.
3. If SFC finds corruption it can't fix, the telemetry subsystem may need a repair install — download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11) and run setup keeping files and apps.
4. After repair, leave the scheduled task disabled (Fix 3) — you want the component healthy but not running on its own schedule.
5. Monitor for a week: a repaired system with disabled scheduled telemetry should show zero spontaneous CompatTelRunner.exe activity.

## Closing

CompatTelRunner.exe is Windows doing homework for the next feature update — useful to Microsoft, but not something that should cost you hours of CPU. Verify it's legitimate, give one clean scan a chance to finish, then disable the scheduled tasks if it won't stop on its own. Your Task Manager — and your fans — will be quieter for it.
