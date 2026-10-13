---
title: "Windows Defender High CPU on 24H2? Calm MsMpEng.exe Down"
slug: how-to-fix-windows-defender-high-cpu-usage-in-windows-11-24h2
date: 2026-10-13
categories: ["performance"]
tags: ["windows defender", "high cpu", "windows 11 24h2", "msmpeng", "antimalware service executable"]
description: "MsMpEng.exe eating CPU after the Windows 11 24H2 update? Learn why Defender spikes and how to reduce its load without weakening protection."
thumbnail: "/images/thumbs/how-to-fix-windows-defender-high-cpu-usage-in-windows-11-24h2.webp"
faqs:
  - q: "Why is Windows Defender using so much CPU after the 24H2 update?"
    a: "The 24H2 update triggers a full re-baseline: Defender rescans the system after major OS changes, and the update itself touches tens of thousands of files that each pass through real-time scanning. Additionally, 24H2's tightened security defaults can increase scanning scope. This heavy period normally settles within 24 to 48 hours as the initial scan completes and caches rebuild."
  - q: "Is it safe to turn off Windows Defender to stop high CPU?"
    a: "No — disabling Defender removes real-time malware protection and leaves the system exposed, and Tamper Protection will fight the change anyway. It also rarely helps for long, since Windows re-enables it. The correct approach is reducing Defender's workload: schedule scans for idle hours, exclude trusted high-churn folders, and let post-update scans finish. You keep full protection while reclaiming your CPU."
  - q: "How do I know if Defender high CPU is actually malware?"
    a: "Check Windows Security > Virus & threat protection > Protection history. Genuine malware activity shows detections, quarantined items, or blocked threats alongside the CPU usage. If protection history is clean, definitions are current, and CPU is high with no detections, Defender is almost certainly busy with legitimate scanning work — a stuck scan, a high-churn folder, or post-update re-baselining — not fighting an infection."
  - q: "Will excluding folders from Defender scans put me at risk?"
    a: "Exclusions trade a small amount of protection for performance, so they must be selective. Exclude folders you control and trust — your code projects, Steam library, video scratch disks — and never exclude Downloads, Temp, user profile roots, or system directories. A targeted exclusion for a folder Defender rescans hundreds of times daily is a reasonable tradeoff; broad exclusions are not."
---

After the Windows 11 24H2 update, many users open Task Manager to find Antimalware Service Executable (MsMpEng.exe) camped at 20, 40, or even 70 percent CPU — fans roaring, laptop hot, everything sluggish. It looks like the antivirus has gone rogue. In nearly every case it has not: 24H2 is a major platform update, and Defender responds to major platform updates with heavy re-scanning, re-baselining, and definition churn that hammers the CPU for a day or two.

The mistake is reaching for the off switch. Disabling Defender guts your protection and Windows fights you on it anyway; the real fix is shrinking Defender's workload so it finishes its business and gets out of the way. Below is the technician's sequence: confirm what it is doing, let legitimate scans finish on your schedule, exclude the folders it obsessively rescans, and repair it if it is genuinely stuck. For the wider high-CPU picture, see [fixing high CPU usage in Windows 11 24H2](/articles/how-to-fix-high-cpu-usage-in-windows-11-24h2/); to trim what launches at boot, read [disabling startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Post-24H2 full system re-baseline**: Major updates trigger Defender to rescan broadly so its baselines match the new OS build — the single most common cause of the spike.
- **Real-time scanning of update-touched files**: 24H2 touches tens of thousands of files; each gets scanned as the system settles, compounding CPU load for a day or more.
- **High-churn folders rescanned endlessly**: Developer build outputs, game libraries, and download folders change constantly and get re-scanned on every change.
- **Scheduled scan colliding with active hours**: The default scheduled scan may run while you work if 24H2 reset its triggers or idle conditions.
- **Corrupt definitions or platform update**: A damaged Security Intelligence update or Defender platform can send the engine into inefficient scanning loops.
- **Leftover third-party antivirus drivers**: Remnants of previously installed AV products install filter drivers that fight Defender for every file access.
- **Genuine threat remediation in progress**: Occasionally the CPU spike is Defender working hard against real malware — always check protection history before tuning.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Protection history before changing anything

Never tune blind. Two minutes of evidence separates legitimate scanning from a stuck engine.

1. Open **Windows Security** > **Virus & threat protection** > **Protection history** and look for recent scans, quarantines, or blocked threats.
2. Confirm **Virus & threat protection updates** shows current definitions — stale definitions cause inefficient, repeated scanning.
3. In **Task Manager** > **Details**, right-click MsMpEng.exe and check whether CPU correlates with disk activity (active scan) or sits high while idle (stuck engine).
4. Note timing: constant high CPU versus spikes during specific activities like compiling code or Steam updates point to different causes.
5. If Protection history shows the same files scanned repeatedly, note those paths — they are your exclusion candidates.

### Fix 2: Give the post-24H2 scan a clean window to finish

Interrupting the re-baseline scan just restarts it. Let it complete once, on your terms.

1. Leave the laptop plugged in and idle for 2–3 hours — preferably overnight — so the initial 24H2 scan completes without contention.
2. Keep the lid open and sleep disabled during this window: **Settings** > **System** > **Power & battery** > set sleep to **Never** temporarily.
3. Do not run heavy apps during the window; every new file you create gets scanned and extends the job.
4. Afterward, check Task Manager: MsMpEng.exe should drop to near zero at idle if the baseline completed.
5. If CPU is still high after a full idle night, move on — the scan is not the problem, something is keeping it busy.

### Fix 3: Reschedule scans to idle hours

Move Defender's heavy lifting to when you are not using the machine.

1. Open **Task Scheduler** (`taskschd.msc`) > **Task Scheduler Library** > **Microsoft** > **Windows** > **Windows Defender**.
2. Right-click **Windows Defender Scheduled Scan** > **Properties** > **Triggers**, and set a time you are reliably away, such as 3 AM.
3. On the **Conditions** tab, enable **Start the task only if the computer is idle** and **Stop if the computer ceases to be idle**.
4. Decide on **Wake the computer to run this task**: enable it for reliable overnight scans, disable it if 3 AM wake-ups bother you.
5. Stagger the **Cache Maintenance** and **Cleanup** tasks so they do not pile onto the same window.

### Fix 4: Add targeted exclusions for trusted high-churn folders

The highest-impact fix for developers, gamers, and creators whose folders change hundreds of times daily.

1. Open **Windows Security** > **Virus & threat protection** > **Manage settings** > **Exclusions** > **Add or remove exclusions**.
2. Add specific trusted folders: your code workspace, Steam library (`steamapps\common`), or video-editing scratch disks — never broad paths like `C:\`.
3. Exclude trusted processes too (e.g., your compiler or game launcher executable) if folder exclusions are insufficient.
4. Never exclude **Downloads**, **Temp**, browser profiles, or system folders — that is where real threats live.
5. Re-test during your normal heavy workload: MsMpEng.exe should spike briefly on genuinely new files, not camp at high CPU.

### Fix 5: Repair Defender's definitions and platform

A corrupted Security Intelligence update or platform component can loop the engine. Repair it cleanly.

1. Open an elevated PowerShell and run `Update-MpSignature` to force a fresh definition pull.
2. In **Settings** > **Windows Update**, install everything pending — Defender platform updates ship through Windows Update.
3. If the Microsoft Store version exists on your system, check **Store** > **Downloads** for a **Windows Security** platform update.
4. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — Defender is a Windows component and these repairs cover it.
5. Reboot and observe for 30 minutes at idle; a repaired engine settles to near-zero CPU quickly.

### Fix 6: Remove conflicting third-party antivirus remnants

Leftover filter drivers from old AV products are a classic cause of Defender spinning its wheels on every file operation.

1. Check **Settings** > **Apps** for any third-party antivirus still installed and uninstall it properly.
2. Download that vendor's official **removal tool** (search the vendor name plus removal tool) — uninstallers routinely leave filter drivers behind.
3. Run the removal tool, reboot, and confirm **Windows Security** shows Microsoft Defender as the active provider.
4. In **Device Manager** > **View** > **Show hidden devices**, look under **Non-Plug and Play Drivers** for orphaned AV filter drivers and uninstall them.
5. Monitor MsMpEng.exe for a day — driver conflicts cause the most stubborn, reboot-resistant CPU usage.

### Fix 7: Run an offline scan, then consider your options

Rule out the one scenario where high CPU is Defender doing its job heroically: fighting real malware.

1. Go to **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** > **Scan now**.
2. The machine reboots into a clean environment outside Windows — let the scan complete fully, which can take an hour.
3. If it finds and removes threats, the high CPU was legitimate; monitor for a day to confirm normal behavior returns.
4. If the scan is clean and tuning failed, the legitimate alternative to disabling Defender is a reputable third-party AV that registers with Windows Security Center.
5. Whatever you do, keep **Tamper Protection** on — disabling it to hack Defender quiet is never the answer; see [Microsoft's Windows security guidance](https://support.microsoft.com/en-us/windows) for the supported settings.

## Closing

Defender high CPU after 24H2 is almost always the engine doing real work — re-baselining after a major update or rescanning folders that never sit still. Give the initial scan its window, schedule future scans for idle hours, exclude the trusted folders it chews on, and it fades back into the background. The off switch is the one fix that trades your security for nothing.
