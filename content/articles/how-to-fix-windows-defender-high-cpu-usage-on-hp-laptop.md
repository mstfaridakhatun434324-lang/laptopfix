---
title: "Fix Windows Defender High CPU Usage on Your HP Laptop"
slug: how-to-fix-windows-defender-high-cpu-usage-on-hp-laptop
date: 2026-09-08
categories: ["performance"]
tags: ["windows defender high cpu", "hp laptop", "antimalware service executable", "msmpeng.exe", "cpu fix"]
description: "Defender maxing out your HP laptop's processor? Clear stuck scans, set smart exclusions, and fix Antimalware Service Executable CPU spikes safely."
thumbnail: "/images/thumbs/how-to-fix-windows-defender-high-cpu-usage-on-hp-laptop.webp"
faqs:
  - q: "Why does Antimalware Service Executable use so much CPU on HP laptops?"
    a: "HP laptops ship with large preinstalled software suites and recovery partitions — thousands of files Defender scans. Combined with a bloated scan history or a stuck scheduled scan, MsMpEng.exe can pin the CPU for hours. Clearing history and excluding trusted folders fixes most cases."
  - q: "Should I install a third-party antivirus instead?"
    a: "Not to solve this. A second antivirus adds its own background scanning on top of Defender's, and the two can conflict — fighting over the same files and doubling CPU usage instead of halving it. Defender is a capable antivirus once its stuck state is cleared. Fix the configuration first; only consider alternatives for feature reasons, never for this CPU issue."
  - q: "How do I schedule Defender scans for nighttime?"
    a: "Open Task Scheduler, navigate to Task Scheduler Library, Microsoft, Windows, Windows Defender, and open the Windows Defender Scheduled Scan task. On the Triggers tab, set a daily 2:00 AM run with a two-hour maximum, and on the Conditions tab require the PC to be idle. You may need to briefly toggle Tamper Protection off to save the change."
  - q: "Can HP Wolf Security conflict with Windows Defender?"
    a: "Occasionally, yes. Wolf Security is built to complement Defender, but if both have real-time file scanning enabled, every file gets scanned twice — which looks exactly like Defender misbehaving. Open HP Wolf Security settings and disable any file-scanning feature that duplicates Defender's real-time protection, while keeping Wolf's other protections like threat isolation enabled."
---

Antimalware Service Executable grinding away at 50 or 80 percent CPU turns an HP laptop into a space heater with a keyboard. The fans scream, the battery drains in half the time, and everything you actually want to do stutters. It is Windows Defender — your own antivirus — and it is supposed to be protecting you, not punishing you.

On HP machines this often traces to the same roots as on any Windows laptop: a scan history database that has grown corrupt, a scheduled full scan firing at the worst time, or Defender dutifully scanning HP's mountain of preinstalled software. Sometimes HP Wolf Security's overlapping features join the pile-on.

The fixes below keep your protection fully on while returning your CPU. No disabling Defender, no sketchy registry hacks — just proper configuration.

## Why this happens

- **Corrupt or bloated scan history:** The protection history database grows until the engine struggles on every cycle.

- **Scheduled full scans at bad times:** Default schedules often land mid-workday instead of overnight.

- **Scanning HP's preinstalled software:** Thousands of bundled files get re-scanned repeatedly.

- **Huge user folders under real-time watch:** Game libraries, video projects, and code repos multiply scan cost.

- **Stuck scan task:** A scheduled scan that hangs mid-run restarts in a loop, pinning CPU indefinitely.

- **HP Wolf Security overlap:** Redundant real-time features scanning the same files twice.

- **Definition update problems:** A bad intelligence update leaves the engine in a high-effort state. The 24H2-specific version of this problem is detailed in [Windows Defender high CPU in 24H2](/articles/how-to-fix-windows-defender-high-cpu-in-windows-11-24h2/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Defender is the CPU hog

HP laptops run many background utilities. Make sure MsMpEng.exe is actually the problem before reconfiguring security.

1. Open Task Manager with Ctrl plus Shift plus Esc and sort by CPU.
2. Confirm Antimalware Service Executable is the sustained top consumer.
3. Open Windows Security, Virus and threat protection, and check for an active scan.
4. Review Protection history for repeated failed or blocked scan entries.
5. If no scan is running but CPU is high, the engine is stuck — continue below.

### Fix 2: Clear the Defender scan history

This is the highest-success single fix for stuck Defender CPU usage. A clean history database lets the engine start fresh.

1. In Windows Security, temporarily turn off Real-time protection.
2. Open File Explorer and go to C:\ProgramData\Microsoft\Windows Defender\Scans\History.
3. Delete all contents of the History folder, including the Service subfolder.
4. Turn Real-time protection back on immediately.
5. Restart the laptop.
6. Watch Task Manager for 15 minutes to confirm the spike is gone.

### Fix 3: Exclude HP bloat and your big folders

Defender should not waste cycles re-scanning HP's recovery partitions or your 200 GB game library. Exclusions target the waste precisely.

1. Open Windows Security, Virus and threat protection, Manage settings.
2. Under Exclusions, add HP recovery and tools folders you never modify.
3. Add your trusted large folders: game libraries, video projects, virtual machines.
4. Never exclude Downloads, Temp, AppData, or Windows folders.
5. Check [HP Support](https://support.hp.com/us-en) for guidance on HP Wolf Security settings to avoid overlap.
6. Monitor CPU over the next day — exclusions apply immediately.

### Fix 4: Reschedule scans to the middle of the night

A full scan is legitimate work — it just should not happen while you are working. Moving it to 2 AM removes the conflict entirely.

1. Open Task Scheduler from Start.
2. Go to Task Scheduler Library, Microsoft, Windows, Windows Defender.
3. Open Windows Defender Scheduled Scan and edit its trigger.
4. Set it to 2:00 AM daily with a 2-hour maximum runtime.
5. On the Conditions tab, require 10 minutes of idle time.
6. You may need to briefly toggle Tamper Protection off in Windows Security to save the change — turn it back on after.

### Fix 5: Check HP Wolf Security for overlap

Two real-time scanners on the same files means every file gets scanned twice. One of them has to yield.

1. Open HP Wolf Security from the Start menu or system tray.
2. Review its real-time protection features.
3. Disable any file-scanning feature that duplicates Defender's real-time protection.
4. Keep Wolf Security's other features — like threat isolation — enabled.
5. Restart and compare Defender CPU usage.
6. If you uninstalled Wolf Security, run HP's cleanup to remove leftover drivers.

### Fix 6: Force a clean intelligence update

A partially applied definition update can leave the engine thrashing. Forcing a clean update resets it.

1. Open PowerShell as administrator.
2. Run `Update-MpSignature` to pull fresh intelligence.
3. Run `Get-MpComputerStatus` and verify AMServiceEnabled is True.
4. If issues persist, check the [Windows support hub](https://support.microsoft.com/en-us/windows) for known Defender issues.
5. Restart the laptop and verify idle CPU over 30 minutes.

### Fix 7: Run a Microsoft Defender Offline scan

If Defender stays restless after every configuration fix, rule out actual malware. Some infections actively fight the scanner, which looks exactly like Defender malfunctioning. An offline scan runs before Windows boots, catching threats that hide from normal scans.

1. Open Windows Security, then Virus and threat protection.
2. Click Scan options.
3. Select Microsoft Defender Offline scan.
4. Click Scan now — the laptop will restart into the offline environment.
5. Let the scan complete; it takes about 15 minutes.
6. When Windows restarts, check Protection history for what was found and removed.

## Closing

Windows Defender does not have to be the enemy of your HP laptop's performance. Clear the stuck history, exclude the folders that do not need constant re-scanning, move full scans to the night, and check Wolf Security for overlap — and MsMpEng.exe goes back to guarding quietly in the background. For the variant that strikes right after Patch Tuesday, see [Defender high CPU after the Windows 11 update](/articles/how-to-fix-windows-defender-high-cpu-after-windows-11-update/).
