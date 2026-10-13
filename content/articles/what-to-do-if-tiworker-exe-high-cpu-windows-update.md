---
title: "TiWorker.exe High CPU During Windows Update: What to Do"
slug: what-to-do-if-tiworker-exe-high-cpu-windows-update
date: 2026-10-10
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows modules installer", "performance"]
description: "TiWorker.exe is eating your CPU during Windows Update? Learn what it does, when to leave it alone, and how to calm it down."
thumbnail: "/images/thumbs/what-to-do-if-tiworker-exe-high-cpu-windows-update.webp"
faqs:
  - q: "What is TiWorker.exe and is it safe?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft process that installs, modifies, and removes Windows update components. It is completely safe and essential. High CPU from TiWorker during an update is normal behavior, not malware. Only worry if it runs at high CPU for many hours with no update in progress, which suggests a stuck servicing operation."
  - q: "How long should TiWorker.exe use high CPU?"
    a: "During an active update, 30 minutes to two hours of elevated CPU is normal, depending on the update size and your hardware. After Patch Tuesday cumulative updates, expect the longer end. If TiWorker is still maxing a CPU core six or more hours after updates finished, with no update activity in Settings, something is stuck and the fixes below apply."
  - q: "Can I end TiWorker.exe in Task Manager?"
    a: "You can, but you should not during an active update. Killing it mid-install corrupts the servicing operation and can leave updates half-applied. If no update is running and TiWorker has been stuck for hours, ending the task is relatively safe, but follow up with the servicing repairs below so the underlying stuck operation does not just restart the cycle."
  - q: "Why does TiWorker.exe slow my laptop to a crawl?"
    a: "TiWorker is disk and CPU intensive by design: it decompresses packages, verifies thousands of files, and writes system components. On laptops with hard drives or dual-core processors, this saturates the hardware and everything else stutters. The slowdown is temporary and ends when the servicing work completes, usually within a couple of hours."
---

TiWorker.exe at 80 percent CPU, fans screaming, laptop barely responsive, and Windows Update swears everything is fine. The process name means nothing to most people, which makes it look suspicious. It is not malware. It is Windows doing the heavy lifting of installing updates, and it is notoriously bad at sharing resources while it works.

The key question is always the same: is TiWorker working or stuck? Working means leave it alone. Stuck means intervene. This guide teaches you to tell the difference in two minutes, then gives you the calm-down sequence for genuinely stuck cases and the coping strategies for normal-but-painful ones.

## Why this happens

- **Active update installation:** TiWorker does the actual file work of updates, and large updates keep it busy for a long time.
- **Post-update cleanup:** After installing, it compresses superseded components and cleans the component store, which is CPU-heavy.
- **Stuck servicing operation:** A corrupted update leaves TiWorker retrying the same failed operation in a loop.
- **Corrupted component store:** Damage in WinSxS forces TiWorker into repeated repair attempts that never complete.
- **Conflicting pending updates:** Multiple queued updates fight over the servicing stack, keeping the worker spinning.
- **Slow hard drive:** On HDD laptops, TiWorker's file operations bottleneck on disk, stretching CPU-visible work for hours.
- **Windows Update client bugs:** Occasionally the update client itself mis-schedules servicing work and never signals completion.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is working or stuck

1. Open **Settings > Windows Update** and check whether an update is currently downloading, installing, or pending a restart.
2. In Task Manager, look at TiWorker's CPU and disk usage over five minutes. Declining usage means progress; flatlined maximum usage for hours means stuck.
3. Check the update history for recent activity. TiWorker running hot right after Patch Tuesday is expected.
4. If an update is active, skip to the coping strategies in Fix 7 and Fix 8. Only apply the intervention fixes when no update is running and the process has been stuck for hours.

### Fix 2: Give it a proper window before intervening

1. Plug in the charger. TiWorker throttles on battery power, which paradoxically stretches the work longer.
2. Close heavy applications to give the servicing work uncontested resources. The faster it finishes, the sooner your laptop is usable.
3. Let it run for at least two hours from when you first noticed it, longer after feature updates.
4. Most TiWorker panics end here. The process finishes, CPU drops, and the laptop returns to normal with updates installed. Premature killing is the main way people turn a slow success into a real problem.

### Fix 3: Restart the Windows Update services

1. If TiWorker is stuck with no active update, open an admin Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`, wait for confirmation, then `net start wuauserv` and `net start bits`.
3. This breaks the stuck servicing loop and lets the update client reschedule cleanly.
4. Watch Task Manager for ten minutes. TiWorker should either settle down or start a legitimate new round of work that completes normally.

### Fix 4: Clear the update cache

1. Stop the services as in Fix 3: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and restart the services.
3. A corrupted download cache is a classic cause of TiWorker looping on the same damaged package forever.
4. Check for updates afterward. The fresh download usually processes cleanly, and TiWorker completes its work instead of spinning. For broader pipeline issues, the [cumulative update guide](/articles/cumulative-update-fails-to-install-troubleshooting/) continues the repair.

### Fix 5: Repair the component store

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt with internet connected.
2. Follow with `sfc /scannow` and restart when both finish.
3. Component store corruption forces TiWorker into endless repair attempts. Fixing the store removes the reason for the loop.
4. After restarting, monitor TiWorker for 30 minutes. It may run briefly to finish legitimate pending work, then settle. Persistent high CPU after a clean DISM points at the update client itself.

### Fix 6: Run the Windows Update troubleshooter

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Update**.
2. The troubleshooter resets stuck servicing states and clears pending operations that keep TiWorker engaged.
3. Restart the laptop after it completes, even if it reports no issues found.
4. If TiWorker immediately ramps up again with no update in progress, check Task Scheduler for stuck update tasks and the servicing logs for repeating errors. Microsoft documents servicing behavior on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Schedule updates for idle hours

1. Open **Settings > Windows Update > Advanced options** and set active hours to cover your working day so restarts and heavy servicing happen overnight.
2. Leave the laptop plugged in and powered on overnight after Patch Tuesday. TiWorker does its worst work while you sleep instead of while you work.
3. Enable **Receive updates for other Microsoft products** only if you want them; fewer products means less servicing work.
4. This does not reduce TiWorker's total work, but it moves the pain to hours when you do not feel it. The [update and shut down guide](/articles/what-to-do-if-update-and-shut-down-stuck-on-laptop/) covers the overnight install path.

### Fix 8: Reduce servicing load on older laptops

1. Uninstall unused Windows features in **Settings > Apps > Optional features** to shrink what TiWorker must service.
2. Run Disk Cleanup as administrator monthly and include system files. A leaner component store means less work per update.
3. Consider an SSD upgrade on hard drive laptops. TiWorker's file-heavy work completes dramatically faster on solid state, which is the single best hardware fix for servicing slowness.
4. Keep third-party software updated through its own updaters rather than letting everything pile onto Windows Update at once.

## Closing

TiWorker.exe high CPU is usually Windows working, not Windows broken. Verify an update is active, give it time on AC power, and let it finish. When it is genuinely stuck with no update running, restart the services, clear the cache, and repair the component store. Respect the worker's job and it stops screaming at you.
