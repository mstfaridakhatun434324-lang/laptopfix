---
title: "How to Fix Windows Defender High CPU Usage on Windows 11"
slug: "how-do-i-fix-windows-defender-high-cpu-usage"
date: "2026-09-11"
categories: ["performance"]
tags: ["windows defender", "antimalware service executable", "high cpu", "windows 11"]
description: "Antimalware Service Executable using 30%+ CPU constantly? Fix Windows Defender high CPU usage without disabling your protection."
thumbnail: "/images/thumbs/how-do-i-fix-windows-defender-high-cpu-usage.webp"
faqs:
  - q: "What is Antimalware Service Executable?"
    a: "It is the background process, MsMpEng.exe, that powers Windows Defender's real-time protection. It scans files as they are opened, created, or downloaded, and runs scheduled full scans. Normal behavior is brief CPU spikes during file activity and near-zero usage at idle. Sustained high CPU means it is stuck scanning something repeatedly or fighting with another security product."
  - q: "Is it safe to disable Windows Defender to fix high CPU?"
    a: "Disabling real-time protection entirely leaves you exposed and Windows will nag you to turn it back on. The fixes in this guide reduce Defender's CPU usage while keeping protection active: adding scan exclusions for trusted folders, scheduling scans for idle hours, and resolving conflicts with other antivirus software. Never run with no antivirus at all."
  - q: "Why does Defender scan the same files repeatedly?"
    a: "The usual reason is a corrupted scan history or a folder containing files Defender cannot complete, such as a huge developer build directory or a constantly-changing database file. Each scan attempt restarts instead of finishing. Clearing the scan history and excluding the problematic folder breaks the loop and returns CPU to normal."
  - q: "How long should a Defender full scan take?"
    a: "On an SSD with a typical 200 to 400 GB of data, a full scan takes 20 to 60 minutes. On a mechanical hard drive it can take several hours. If a scheduled scan never seems to finish across multiple days, or quick scans also hang, the scan engine or its history is likely damaged and needs the repair steps below."
---

Antimalware Service Executable, or MsMpEng.exe, is supposed to be invisible. It is the engine behind Windows Defender's real-time protection, scanning files as they open and running scheduled sweeps in the background. Most of the time it sips CPU at 0 to 2 percent. But when it goes wrong, it can pin a CPU core at 30 percent or more for hours, turning a fast laptop into a space heater.

The pattern is distinctive: Task Manager shows Antimalware Service Executable near the top of the CPU list even when you are doing nothing. Fans spin up, the laptop gets warm at idle, and battery life collapses. Common triggers include a stuck scan loop, Defender fighting a second antivirus, or a folder full of files that Defender chokes on, like a developer's build directory with tens of thousands of small files.

This guide fixes high Defender CPU without disabling your protection. You will identify what it is stuck scanning, add targeted exclusions, schedule scans for when you are away, and repair the scan engine if it is damaged.

## Why this happens

- **A stuck scheduled scan:** A full scan that never completes keeps the engine at high CPU indefinitely instead of finishing and standing down.
- **Conflict with another antivirus:** Two real-time scanners inspecting the same files multiply CPU usage and can deadlock each other.
- **Scanning a huge developer or build folder:** Tens of thousands of small files in node_modules or build output take enormous scan time on every change.
- **Corrupted scan history:** Damaged history data makes Defender re-scan files it already cleared, looping forever.
- **Real-time protection scanning archives repeatedly:** Large constantly-changing files like virtual machine disks or databases trigger endless re-scans.
- **Outdated Defender engine:** Old antimalware platform versions contain bugs that newer updates fixed.
- **Full scan scheduled during work hours:** The default schedule may run heavy scans while you are actively using the laptop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Defender is the problem and update it

Verify MsMpEng.exe is genuinely the top consumer, then make sure the Defender engine itself is current before deeper surgery.

1. Open Task Manager with Ctrl+Shift+Esc and sort by CPU.
2. Confirm Antimalware Service Executable is consistently near the top.
3. Open Windows Security from the Start menu.
4. Go to Virus and threat protection, then Protection updates, and click Check for updates.
5. Install any Security Intelligence updates and restart.

### Fix 2: Add exclusions for trusted heavy folders

Exclusions tell Defender to skip folders you trust. This is the single most effective fix for developers and anyone with huge file collections.

1. Open Windows Security, then Virus and threat protection.
2. Under Virus and threat protection settings, click Manage settings.
3. Scroll to Exclusions and click Add or remove exclusions.
4. Click Add an exclusion, choose Folder, and add paths like build directories or virtual machine folders.
5. Only exclude folders you trust completely; never exclude Downloads or Temp.

### Fix 3: Schedule scans for idle hours

Moving the heavy scheduled scan to the middle of the night keeps it from competing with your work.

1. Press Win+R, type taskschd.msc, and press Enter.
2. Navigate to Task Scheduler Library, Microsoft, Windows, Windows Defender.
3. Double-click Windows Defender Scheduled Scan and open the Triggers tab.
4. Edit the trigger to run at a time you are asleep, such as 3 AM.
5. On the Conditions tab, check Start the task only if the computer is idle.

### Fix 4: Remove conflicting second antivirus software

Two real-time antivirus products will fight. Windows is designed to have exactly one active real-time scanner.

1. Open Settings, Apps, Installed apps.
2. Look for any third-party antivirus beyond Windows Security.
3. If you find one, uninstall it properly through its own uninstaller.
4. Confirm Windows Security shows Virus and threat protection as active afterward.
5. Never run two real-time scanners simultaneously again.

### Fix 5: Clear Defender's scan history

Corrupted history can trap Defender in a re-scan loop. Clearing it forces a fresh start.

1. Open File Explorer and navigate to C:\ProgramData\Microsoft\Windows Defender\Scans\History.
2. You may need to take ownership or use an administrator File Explorer.
3. Delete the contents of the History folder, not the folder itself.
4. Alternatively, open Windows Security, Protection history, and clear it there.
5. Restart and watch MsMpEng.exe CPU over the next hour.

### Fix 6: Repair the Defender platform

If nothing else helps, the antimalware platform itself may be damaged. These commands repair it using built-in tools.

1. Open Terminal as administrator with Win+X.
2. Run DISM /Online /Cleanup-Image /RestoreHealth and wait for completion.
3. Run sfc /scannow afterward and restart.
4. Check Windows Update for any pending Security Intelligence updates.
5. Microsoft documents Defender troubleshooting further in its [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Cap Defender's CPU usage during scans

Windows lets you limit the average CPU load Defender uses while scanning. Lowering the cap keeps scans from overwhelming weaker laptop CPUs, at the cost of slower scans.

1. Open Terminal as administrator with Win+X.
2. Type Set-MpPreference -ScanAvgCPULoadFactor 30 and press Enter.
3. This caps scan CPU around 30 percent instead of the default 50.
4. Trigger a quick scan and confirm the system stays responsive.
5. Raise it back to 50 later if scans take unreasonably long.

### Fix 8: Cap Defender's CPU usage during scans

Windows lets you limit the average CPU load Defender uses while scanning. Lowering the cap keeps scans from overwhelming weaker laptop CPUs, at the cost of slower scans.

1. Open Terminal as administrator with Win+X.
2. Type Set-MpPreference -ScanAvgCPULoadFactor 30 and press Enter.
3. This caps scan CPU around 30 percent instead of the default 50.
4. Trigger a quick scan and confirm the system stays responsive.
5. Raise it back to 50 later if scans take unreasonably long.

## Closing

High Defender CPU is fixable without sacrificing protection. In the large majority of cases, the answer is exclusions for trusted heavy folders, a saner scan schedule, or removing a conflicting second antivirus. Keep real-time protection on, keep the engine updated, and point Defender away from the folders it chokes on. If MsMpEng.exe is calm but the system is still slow, the next place to look is usually [search indexing activity](/articles/best-way-to-fix-search-indexing-high-cpu-windows-11/). For the full diagnostic toolkit, see our guide to [Antimalware Service Executable high CPU](/articles/antimalware-service-executable-high-cpu-windows-11/). For the full diagnostic toolkit, see our guide to [Antimalware Service Executable high CPU](/articles/antimalware-service-executable-high-cpu-windows-11/).
