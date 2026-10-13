---
title: "Fix Windows Defender High CPU Usage in Windows 11 24H2"
slug: how-to-fix-windows-defender-high-cpu-in-windows-11-24h2
date: 2026-10-08
categories: ["performance"]
tags: ["windows defender high cpu", "antimalware service executable", "windows 11 24h2", "msmpeng.exe", "cpu 100%"]
description: "Antimalware Service Executable eating your CPU after the 24H2 update? Reschedule scans, trim exclusions safely, and fix the Defender CPU spike without disabling protection."
thumbnail: "/images/thumbs/how-to-fix-windows-defender-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Why is Antimalware Service Executable using so much CPU in 24H2?"
    a: "The 24H2 update can reset scan schedules, re-enable full scans on large folders, or leave Defender scanning its own history. Corrupt scan history and scheduled tasks firing during work hours are the most common triggers. Clearing the scan history and rescheduling scans usually drops usage within a day."
  - q: "Is it safe to disable Windows Defender to stop high CPU?"
    a: "No — and it rarely helps anyway, since Windows re-enables it automatically. Disabling leaves every file you open unprotected. The effective fixes keep protection fully on: clear the corrupted scan history, exclude trusted heavy folders, and move full scans to overnight hours. You get the same CPU relief with zero security tradeoff."
  - q: "How long should a Defender full scan take?"
    a: "A healthy full scan takes 30 minutes to a few hours depending on drive size and file count. If MsMpEng.exe pins the CPU for days or spikes every few minutes without a scan running, something is stuck — clear the scan history and check scheduled tasks."
  - q: "Does adding exclusions make my PC less safe?"
    a: "Barely, if you exclude wisely. An exclusion just tells Defender to skip re-scanning files you know are safe, like your Steam library or a video project folder. The risk only becomes real if you exclude risky locations — never exclude Downloads, Temp, or system folders. Everything else on the PC stays fully protected."
---

After the Windows 11 24H2 update, a lot of laptops developed the same annoying symptom: Antimalware Service Executable (MsMpEng.exe) sitting at 30, 60, even 100 percent CPU for hours. Your fans roar, everything lags, and Task Manager points the finger squarely at Windows Defender. It feels like your own antivirus turned against you.

The 24H2 update is notorious for this because it can reset Defender's scan schedule, balloon the scan history database, or leave the engine re-scanning folders it already cleared. The process is not malfunctioning in the classic sense — it is usually stuck in a loop or pointed at an unreasonable workload. That distinction matters, because the fix is to unstick it, not to kill your protection.

Below is the technician's order of operations: confirm what Defender is actually doing, clear the stuck state, then reshape its schedule so it never bothers you during work hours again.

## Why this happens

- **24H2 reset the scan schedule:** Feature updates can restore default scheduled scans, including full scans that fire while you are working.

- **Bloated scan history database:** A corrupt or oversized protection history makes the engine work harder on every scan cycle.

- **Scanning its own folders:** Defender sometimes scans its own definition and history folders in a loop after an update.

- **Huge folders under real-time watch:** Developer folders, game libraries, and video projects with hundreds of thousands of small files multiply scan cost.

- **Stuck scheduled task:** The Windows Defender scheduled scan task can hang mid-run and restart repeatedly, pinning CPU indefinitely.

- **Definition update glitch:** A partially applied intelligence update can leave the engine in a high-effort fallback mode. If Defender is not your only hog, check our guide to [fixing Antimalware Service Executable high CPU on Windows 11](/articles/antimalware-service-executable-high-cpu-windows-11/) for the general case.

- **Conflicting third-party antivirus remnants:** Leftover drivers from an uninstalled antivirus fight Defender for file access, doubling the work.

- **Tamper Protection blocking your fixes:** Some repairs need Tamper Protection toggled off briefly, which 24H2 guards more aggressively.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Defender is the real culprit

High CPU blamed on Defender is sometimes a different process hiding behind it. Two minutes of checking saves you from fixing the wrong thing.

1. Open Task Manager with Ctrl plus Shift plus Esc and sort by CPU.
2. Confirm Antimalware Service Executable (MsMpEng.exe) is the top consumer and note the percentage.
3. Open Windows Security, then Virus and threat protection, and check whether a scan is currently running.
4. If no scan is running but CPU is high, the engine is stuck — proceed to the next fixes.
5. Check the Protection history page for repeated blocked or failed scan entries, which hint at a loop.

### Fix 2: Clear Defender's scan history and cache

A bloated or corrupt history database is the single most common cause of post-24H2 Defender CPU spikes. Clearing it forces a clean rebuild.

1. Open Windows Security and temporarily turn off Real-time protection (you will turn it back on shortly).
2. Open File Explorer and navigate to C:\ProgramData\Microsoft\Windows Defender\Scans\History.
3. Delete everything inside the History folder — the Service subfolder contents too.
4. Also clear C:\ProgramData\Microsoft\Windows Defender\Scans\MpCache if it exists.
5. Turn Real-time protection back on immediately.
6. Restart the laptop and watch Task Manager for 15 minutes to confirm the spike is gone.

### Fix 3: Reschedule scans to idle hours

Default scheduled scans often land mid-workday. Moving them to 2 AM means Defender does its heavy lifting while you sleep.

1. Open Task Scheduler from Start search.
2. Navigate to Task Scheduler Library, Microsoft, Windows, Windows Defender.
3. Double-click Windows Defender Scheduled Scan, go to the Triggers tab, and edit the trigger.
4. Set it to run at 2:00 AM daily and tick 'Stop task if it runs longer than' with a 2-hour limit.
5. On the Conditions tab, check 'Start the task only if the computer is idle for' 10 minutes.
6. Click OK — you may need to briefly disable Tamper Protection in Windows Security for the change to stick.

### Fix 4: Add smart exclusions for heavy folders

Exclusions tell Defender to stop re-scanning folders you know are safe. Target the big ones — game libraries, video projects, developer repos — and CPU drops fast.

1. Open Windows Security, Virus and threat protection, Manage settings.
2. Under Exclusions, choose Add or remove exclusions, then Add an exclusion, Folder.
3. Add your largest trusted folders one at a time — for example your Steam library or video project drive.
4. Never exclude Downloads, Temp, AppData, or Windows system folders.
5. Monitor Task Manager over the next day; exclusions take effect immediately.
6. For the full exclusion strategy, see [disabling Windows Defender temporarily in 24H2](/articles/how-to-disable-windows-defender-temporarily-in-windows-11-24h2/) — and why exclusions beat disabling.

### Fix 5: Repair Defender with PowerShell commands

When the engine itself is in a bad state after 24H2, a repair reinstall of its platform update resets behavior without touching your settings or files.

1. Open PowerShell as administrator.
2. Run `Get-MpComputerStatus` and check AMServiceEnabled and AntivirusEnabled are True.
3. Run `Update-MpSignature` to force a clean intelligence update.
4. If problems persist, run `Add-MpPreference -ExclusionPath` only for paths you trust — or undo bad ones with `Remove-MpPreference`.
5. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for the latest Defender platform update guidance.
6. Restart and verify CPU stays normal during idle.

### Fix 6: Remove conflicting antivirus leftovers

Old antivirus drivers that survived an uninstall intercept the same files Defender scans, so every file gets scanned twice — sometimes in a fight that never ends.

1. Open Settings, Apps, Installed apps, and look for any third-party antivirus you thought you removed.
2. Uninstall it, then download that vendor's official removal tool and run it to clear leftover drivers.
3. Open Device Manager, enable Show hidden devices, and check for orphaned antivirus filter drivers.
4. Run `sfc /scannow` in an admin Command Prompt to repair system file damage the conflict may have caused.
5. Restart, then confirm only Windows Defender is active under Windows Security, Protection areas.

## Closing

Defender high CPU after 24H2 is almost never a reason to ditch your antivirus — it is a stuck scan history, a bad schedule, or a folder that should have been excluded long ago. Work the list in order and you keep full protection with your CPU back where it belongs: under your control.
