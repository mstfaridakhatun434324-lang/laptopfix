---
title: "Fix Windows Defender (Antimalware Service) High CPU on a Lenovo Laptop"
slug: "how-to-fix-windows-defender-high-cpu-on-lenovo-laptop"
date: "2026-09-20"
categories: ["performance"]
tags: ["windows defender", "antimalware service executable", "high cpu", "lenovo laptop", "msmpeng"]
description: "Antimalware Service Executable eating CPU on your Lenovo laptop? Tame Windows Defender's scans without compromising your protection."
thumbnail: "/images/thumbs/how-to-fix-windows-defender-high-cpu-on-lenovo-laptop.webp"
faqs:
  - q: "What is Antimalware Service Executable (MsMpEng.exe)?"
    a: "It is the core background process of Microsoft Defender Antivirus — the engine behind real-time protection, scheduled scans, and threat remediation. High CPU from MsMpEng.exe means Defender is actively scanning files, which is legitimate work, but sustained high usage usually indicates a scan loop, an oversized scan scope, or a conflict worth fixing."
  - q: "Is it safe to disable Windows Defender to stop the CPU usage?"
    a: "Disabling Defender permanently leaves you unprotected and is not recommended. The fixes in this guide reduce its CPU impact while keeping protection active — scheduling scans for idle time, adding exclusions, and fixing scan loops. Only disable it temporarily as a diagnostic, or if you run a reputable third-party antivirus that takes over protection."
  - q: "Why does Defender scan the same files repeatedly?"
    a: "Usually because something keeps changing them — a development build folder, a constantly-updating database, or a sync client rewriting files triggers re-scans on every write. Excluding trusted high-churn folders from real-time scanning breaks the cycle. Corrupted Defender definitions can also cause re-scan loops until definitions are updated."
  - q: "Can I just end MsMpEng.exe in Task Manager?"
    a: "Windows will not let you easily — it is a protected system process, and even with effort it restarts automatically. Fighting the process is futile; the effective approach is configuring what Defender scans and when, which addresses the cause instead of the symptom."
---

**MsMpEng.exe** — Antimalware Service Executable — is Microsoft Defender's scanning engine, and when it decides to work hard, your Lenovo laptop feels it: sustained 20–60% CPU, fans spinning, everything else sluggish. Some of this is legitimate — a scheduled full scan, or real-time protection doing its job during a big file operation. But when Defender burns CPU for hours on an idle machine, or spikes every time you compile code or sync files, it is a configuration problem, not protection doing its job.

The crucial principle: never "fix" Defender CPU by disabling protection. An unprotected laptop is not a fast laptop — it is a compromised one waiting to happen. Every fix below preserves full protection while removing the waste: smarter scheduling, targeted exclusions, repaired definitions, and eliminated scan loops.

Lenovo-specific context: many Lenovo machines ship with a third-party antivirus trial (McAfee, Norton) that, when expired but not removed, fights Defender for file access — both products scanning the same files doubles the CPU. Check for that first.

## Why this happens

- **Scheduled full scans:** The default weekly quick scan — or a triggered full scan — legitimately uses heavy CPU while running.
- **Real-time scanning of high-churn folders:** Dev build outputs, sync folders, and databases get re-scanned on every write.
- **Expired third-party AV conflicting:** A dead McAfee/Norton trial still hooks file access and fights Defender.
- **Corrupted definitions:** Damaged signature updates can cause the engine to re-scan or misbehave until refreshed.
- **Scanning its own exclusions incorrectly:** Misconfigured or missing exclusions for trusted tools (notably developer toolchains).
- **Post-update re-scan:** After Windows or Defender platform updates, a fresh baseline scan runs.
- **Scanning archives repeatedly:** Large ZIP/ISO collections get deeply scanned on every access without exclusions.
- **Lenovo bloatware triggering scans:** Bundled utilities that constantly write logs or temp files keep real-time protection busy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what Defender is actually doing

Open **Windows Security > Virus & threat protection** and check **Protection history** and the last scan time. If a full scan is currently running or just finished, the CPU was legitimate — let it complete. Also note the timing pattern: CPU spikes during specific activities (coding, syncing, gaming) point to real-time scanning of those workloads, which exclusions fix; constant CPU with no pattern points to a stuck scan or conflict. This observation directs every fix below, so spend five minutes here. The 24H2-specific Defender walkthrough is our [Defender high CPU in 24H2 guide](/articles/how-to-fix-windows-defender-high-cpu-usage-in-windows-11-24h2/).

1. Open **Windows Security > Virus & threat protection**.
2. Review **Protection history** and current scan status.
3. Note whether CPU correlates with specific activities.
4. Let any in-progress legitimate scan finish before changing settings.

### Fix 2: Remove conflicting expired antivirus trials

This is the highest-value check on Lenovo machines. Open **Settings > Apps > Installed apps** and look for McAfee, Norton, or any other security suite — especially expired trials. Two antivirus products (even a dead one) hooking the same file operations multiplies CPU. Uninstall the third-party product completely, using the vendor's removal tool if the standard uninstall leaves remnants, then confirm Defender reports itself as the active provider. Restart after removal — filter drivers unload only at boot.

1. Check **Settings > Apps** for third-party antivirus products.
2. Uninstall them (use the vendor's removal tool for leftovers).
3. Confirm **Windows Security** shows Microsoft Defender as active.
4. Restart and compare MsMpEng.exe CPU.

### Fix 3: Add exclusions for trusted high-churn folders

The single most effective Defender tuning: exclude folders that change constantly and that you trust — code build directories, VM folders, video render scratch, sync-client caches. Real-time protection skips excluded paths, breaking the scan-on-every-write cycle. Be surgical: exclude specific folders, never entire drives or Downloads. Each exclusion is a small, conscious tradeoff, and for developer and creator workloads it typically eliminates the worst Defender CPU spikes entirely.

1. Go to **Windows Security > Virus & threat protection > Manage settings > Exclusions**.
2. Click **Add an exclusion > Folder**.
3. Add trusted high-churn folders (build dirs, VM storage, render scratch).
4. Verify CPU during those workloads drops.

### Fix 4: Reschedule scans for idle time

Defender's scheduled scans default to times that may coincide with your work. Open **Task Scheduler > Task Scheduler Library > Microsoft > Windows > Windows Defender** and adjust the scan schedule to the middle of the night or lunch hour — times the laptop is on but you are not working. Also consider switching the scheduled **full** scan to a **quick** scan for the automated run, reserving full scans for manual monthly runs. The machine stays equally protected; the CPU cost just moves to when you do not feel it.

1. Open `taskschd.msc` and navigate to the Windows Defender folder.
2. Open the scheduled scan task's **Triggers** and set an idle-time schedule.
3. Ensure **Conditions > Start only if idle** is checked where appropriate.
4. Confirm the next scheduled scan no longer interrupts work.

### Fix 5: Update Defender definitions and platform

A corrupted or outdated Defender platform is a known cause of scan loops and excess CPU. Open **Windows Security > Virus & threat protection > Protection updates** and check for updates manually — then open **Settings > Windows Update** and install any Defender platform updates waiting there. If behavior is truly bizarre (CPU at 100% constantly with no scan running), reset the Defender configuration via PowerShell (`Update-MpSignature` followed by a platform update). Microsoft documents Defender troubleshooting on the official [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In Windows Security, check **Protection updates** manually.
2. Install Defender platform updates via Windows Update.
3. In elevated PowerShell, run `Update-MpSignature` if issues persist.
4. Restart and observe MsMpEng.exe at idle.

### Fix 6: Limit Defender's CPU during scans

Defender has a built-in throttle: the **ScanAvgCPULoadFactor** setting caps the CPU percentage scans may use (default 50). Lowering it to 20–30 makes scheduled scans nearly invisible at the cost of slower scans — a good trade when scans run during work hours. Set it via PowerShell: `Set-MpPreference -ScanAvgCPULoadFactor 20`. This does not affect real-time protection's responsiveness to actual threats; it only paces the scheduled scan workload. Verify the setting with `Get-MpPreference`.

1. Open **PowerShell as administrator**.
2. Run `Set-MpPreference -ScanAvgCPULoadFactor 20`.
3. Verify with `Get-MpPreference | Select ScanAvgCPULoadFactor`.
4. Observe the next scheduled scan's CPU footprint.

### Fix 7: Check for malware mimicking Defender

In rare cases, sustained MsMpEng.exe CPU with no scan activity — or a MsMpEng.exe running from anywhere other than `C:\Program Files\Windows Defender` — indicates malware masquerading as the Defender process. Verify the file location in Task Manager (right-click > Open file location) and run both a Defender **Offline scan** (which reboots into a clean environment) and a second-opinion scan with the free Malwarebytes scanner. Genuine Defender CPU always correlates with visible scan activity in Protection history; CPU with no history entries is suspicious. Our broader [antimalware CPU guide](/articles/how-to-fix-antimalware-service-executable-high-cpu-after-windows-11-update/) covers the impersonation checks in detail.

1. Verify MsMpEng.exe location is `C:\Program Files\Windows Defender`.
2. Run a **Microsoft Defender Offline scan** from Windows Security.
3. Run a second-opinion scan (e.g., free Malwarebytes).
4. Investigate any CPU with no corresponding Protection history.

## Closing

Defender high CPU is almost never a reason to disable protection — it is a reason to configure it: remove the conflicting expired trial, exclude trusted churn folders, schedule scans for idle hours, and throttle scan CPU. Do that, and MsMpEng.exe goes back to being the quiet guardian it is supposed to be instead of the loudest process on your Lenovo.
