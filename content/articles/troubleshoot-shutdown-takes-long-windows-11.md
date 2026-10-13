---
title: "Troubleshooting Slow Shutdowns in Windows 11"
slug: troubleshoot-shutdown-takes-long-windows-11
date: 2026-09-28
categories: ["performance"]
tags: ["shutdown troubleshooting", "slow shutdown", "event viewer", "windows 11", "hang"]
description: "Troubleshoot slow Windows 11 shutdowns systematically: read the shutdown logs, isolate blockers, and verify the fix."
thumbnail: "/images/thumbs/troubleshoot-shutdown-takes-long-windows-11.webp"
faqs:
  - q: "How do I troubleshoot a slow shutdown step by step?"
    a: "First, time several shutdowns to establish a baseline and rule out update-related slowness. Second, read Event Viewer's Diagnostics-Performance log (event ID 203) and the System log — they name the exact apps, services, or drivers that delayed shutdown. Third, test in Safe Mode: fast shutdown there means a third-party component is guilty. Then isolate with clean boot and fix or remove the convicted component."
  - q: "What do shutdown event IDs 203, 204, and 1074 mean?"
    a: "Event ID 203 in the Diagnostics-Performance log flags a shutdown performance degradation and names the slow component with its delay time. Event 204 marks a slow foreground app close. Event 1074 in the System log records the shutdown initiation itself — who started it and why (user, update, power button). Together they reconstruct the full shutdown timeline for diagnosis."
  - q: "Why is shutdown fast in Safe Mode but slow normally?"
    a: "Safe Mode loads only Microsoft drivers and services, so a fast Safe Mode shutdown proves a third-party driver or service is the blocker in normal mode. The next step is clean-boot isolation: disable all non-Microsoft services and startup apps, confirm fast shutdown, then re-enable in halves until slowness returns. The last batch re-enabled contains the culprit."
  - q: "Can a failing hard drive cause slow shutdowns?"
    a: "Yes. During shutdown, Windows flushes caches and writes state to disk — a failing drive with bad sectors retries writes repeatedly, stretching shutdown dramatically. If slow shutdowns coincide with disk errors in Event Viewer (event ID 7, 11, or 51), run chkdsk and check SMART health with CrystalDiskInfo. Back up immediately if the drive shows warnings."
---

Slow shutdown troubleshooting is forensic work: the crime happens in the 60 seconds after you click Shut down, and the witnesses are Windows' own logs. This guide walks the full diagnostic path — from baseline measurements through log analysis, Safe Mode isolation, and clean-boot bisection — so you find the actual blocker instead of applying random registry tweaks.

Keep a simple log as you go: shutdown times, what was running, and what each test changed. Patterns emerge fast when you write them down.

## Why this happens

- **Named app blockers**: Specific applications with close delays, logged by name in the Diagnostics-Performance log.
- **Slow service stops**: Third-party services exceeding their stop timeout, forcing Windows to wait or kill them.
- **Driver power-down hangs**: Drivers failing the shutdown IRP, stalling the kernel's power transition.
- **Update installation**: Legitimate but slow update finalization during shutdown.
- **Disk flush delays**: Failing or busy storage slowing the cache flush and hive writes.
- **Network timeout waits**: Open handles to network resources forcing timeout delays.
- **User-profile unload issues**: Roaming or corrupted profiles delaying the profile service.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Baseline and rule out updates

Establish facts before theorizing.

1. Time **three** shutdowns with a stopwatch (click to power-off), noting what was open each time. Record all three numbers — variance matters.
2. Open **Settings** > **Windows Update** before each test shutdown: if "Update and shut down" is offered or updates are mid-install, that shutdown doesn't count toward your baseline.
3. Check **Reliability Monitor** (search Start): its timeline shows shutdown failures and hangs with dates — correlate slow shutdowns with software installs or updates.
4. Note the shutdown *behavior*: spinner with disk activity (working, possibly updates), spinner with no activity (true hang), or "waiting for app" screen (named app blocker).
5. If shutdowns are slow only sometimes, note the pattern — after long sessions (leaked state), with specific apps open (app blocker), or randomly (driver/service). If boot is also slow, review [slow SSD boot fixes](/articles/what-to-do-if-windows-11-boot-time-slow-ssd/).

### Fix 2: Read the shutdown forensic logs

Let Windows name the blocker.

1. Open **Event Viewer** (`eventvwr.msc`) > **Applications and Services Logs** > **Microsoft** > **Windows** > **Diagnostics-Performance** > **Operational**.
2. Filter for event ID **203** (shutdown degradation). Each entry names the component and its delay in milliseconds — sort by time and read the most recent slow shutdowns.
3. Cross-reference with **Windows Logs** > **System** filtered for IDs **1074** (shutdown reason), **6006** (event log stopped = clean shutdown completed), and **6008** (unexpected shutdown = you held the power button).
4. Look for **Service Control Manager** events (ID 7036/7045) near shutdown time — services that took long to enter the stopped state.
5. Build your suspect list from the logs: apps named in 203s, services slow in 7036s, drivers in any bugcheck-adjacent warnings. This list drives every later step.

### Fix 3: Safe Mode and clean boot isolation

Prove whether it's third-party, then bisect to find it.

1. Boot into **Safe Mode** (Shift + Restart > Troubleshoot > Startup Settings > Safe Mode) and shut down from there. Time it.
2. Fast in Safe Mode = third-party driver/service/app. Slow in Safe Mode too = Microsoft component, core driver, or hardware — skip to Fix 5.
3. Back in normal mode, run `msconfig`: **Services** tab > **Hide all Microsoft services** > **Disable all**. Task Manager > **Startup apps** > disable all. Reboot.
4. Time the shutdown in this clean-boot state. If fast, re-enable services in **halves**: enable half, reboot, time shutdown. Continue halving the guilty half until one service/app remains.
5. Once identified: update it, configure it to close cleanly, disable its service (`services.msc` > Disabled), or uninstall it. Restore your normal configuration for everything innocent.

### Fix 4: Fix the convicted app or service

Targeted fixes for the usual convicted components.

1. **For a named app**: check its settings for "close to tray" or background modes — apps that minimize instead of closing often delay shutdown. Update the app; check its vendor forums for known shutdown hangs.
2. **For a named service**: open `services.msc`, find it, and check its **Recovery** tab — then decide: set **Startup type** to **Manual** (if you launch the parent app yourself) or **Disabled** (if unused).
3. **Tighten timeouts** as a safety net: registry `HKEY_CURRENT_USER\Control Panel\Desktop` > `WaitToKillAppTimeout` = `2000`, `HungAppTimeout` = `2000`, `AutoEndTasks` = `1`; and `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` > `WaitToKillServiceTimeout` = `5000`. (Back up the registry first.)
4. **For sync/cloud apps**: pause syncing before shutdown during testing — if shutdowns speed up, configure the app's own clean-exit behavior or quit it manually pre-shutdown.
5. Re-time three shutdowns after the fix and compare against baseline — the numbers should show clear, repeatable improvement.

### Fix 5: Investigate drivers and hardware

When isolation points below the application layer.

1. Check **Device Manager** for warning icons — resolve those first regardless.
2. Update **chipset drivers** from your vendor ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — the chipset driver handles power transitions for the whole board.
3. If a driver update preceded the problem, roll it back: Device Manager > device > Properties > Driver > **Roll Back Driver**.
4. Test shutdown with all USB devices disconnected — USB power-transition hangs are common and easy to test.
5. Check disk health: run `chkdsk C: /f` and inspect SMART data with CrystalDiskInfo — disk errors during the shutdown flush are a real cause. Also verify system file integrity with `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`.

### Fix 6: Verify and document the fix

Close the loop like a technician.

1. After applying fixes, time **three more** shutdowns under normal conditions (typical apps open, no pending updates). All three should be near your target (under ~30 seconds on SSD).
2. Re-check the Diagnostics-Performance log after a few days — no new event 203s means the blocker is truly gone, not just quieter.
3. Write down what the cause was and what fixed it (a note in your phone is fine). Shutdown issues recur after major updates; your notes make the second fix a 5-minute job.
4. If problems return after a Windows feature update, re-run Fix 2's log analysis first — updates commonly reintroduce old blockers or add new ones.
5. For persistent, unexplained cases, Microsoft's power and shutdown documentation at Windows support covers advanced tracing with Windows Performance Recorder.

## Closing

Shutdown troubleshooting is one of the most satisfying diagnostic exercises in Windows: the logs literally name the culprit, isolation proves it, and the fix is usually a single setting or uninstall. Time it, read the logs, bisect the suspects — slow shutdowns don't survive that process. For trimming what launches at boot, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).
