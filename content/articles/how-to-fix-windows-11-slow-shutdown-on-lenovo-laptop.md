---
title: "Windows 11 Slow Shutdown on a Lenovo Laptop? Fix It"
slug: how-to-fix-windows-11-slow-shutdown-on-lenovo-laptop
date: 2026-09-07
categories: ["performance"]
tags: ["slow shutdown", "lenovo laptop", "windows 11", "shutdown fix", "hang"]
description: "Windows 11 taking forever to shut down on your Lenovo laptop? Fix hanging apps, slow services, and driver delays for fast power-offs."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-shutdown-on-lenovo-laptop.webp"
faqs:
  - q: "How long should Windows 11 take to shut down?"
    a: "On a healthy SSD system, 10–20 seconds from clicking Shut down to full power-off is normal. Up to 30 seconds is acceptable if several apps were open. Consistently over a minute — or hanging indefinitely on the 'Shutting down' screen — indicates a stuck app, service, or driver refusing to terminate, and it's worth diagnosing rather than tolerating."
  - q: "Is it safe to force shutdown with the power button?"
    a: "Occasionally, yes — holding the power button is the escape hatch for a truly hung shutdown. But doing it regularly risks file-system corruption and data loss in open apps. If you're force-shutting down often, that's a symptom to fix, not a routine to adopt. Fix the hanging component so normal shutdowns complete on their own."
  - q: "Why does my Lenovo hang on 'Shutting down' with the spinner?"
    a: "Windows is waiting for something to terminate: usually an app with unsaved state, a Lenovo background service (Vantage components, telemetry, update services), a network driver holding connections, or a hung system service. Windows waits through timeouts (20 seconds per service by default) before force-closing, so one stubborn service adds its full timeout to every shutdown."
  - q: "Does fast startup affect shutdown speed?"
    a: "Fast startup changes what shutdown does — it hibernates the kernel instead of fully closing it, which is usually quicker than a full shutdown. But it can mask problems: driver issues that would surface on a clean shutdown get carried over. If shutdowns are slow, test with fast startup off to see the true full-shutdown behavior, then decide which mode to keep."
---

You click **Shut down**, the screen says "Shutting down" with the spinner... and a minute later it's still there. Maybe it eventually powers off; maybe you give up and hold the power button. Either way, something is refusing to let go, and Windows waits politely through timeout after timeout before forcing the issue.

On Lenovo laptops, the usual shutdown blockers are Lenovo background services, apps with unsaved state, network drivers holding connections, and Windows' own generous timeouts. This guide finds what's hanging and fixes it — for fast, clean shutdowns. If boots are the slow part instead, see our [SSD boot guide](/articles/how-to-fix-windows-11-boot-time-slow-ssd-step-by-step/).

## Why this happens

- **Apps refusing to close**: Programs with unsaved work or hung windows block shutdown until timeout.
- **Lenovo background services**: Vantage components, telemetry, and update services slow to terminate.
- **Network drivers holding connections**: Wi-Fi/Ethernet drivers waiting on network timeouts during shutdown.
- **Windows Update finalizing**: Legitimate "don't turn off" work that looks like a hang.
- **Hung system services**: A stuck service forcing Windows through its full 20-second kill timeout.
- **Pagefile clearing enabled**: The "clear pagefile at shutdown" policy adds significant time on every power-off.
- **USB devices delaying**: External drives or peripherals that don't suspend promptly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify what's hanging

Watch the shutdown and check the logs after.

1. During the next slow shutdown, watch the screen: does it show "Shutting down" plainly, or does it name an app ("Closing 1 app and shutting down")? A named app is your culprit — close it manually before shutdown as a test.
2. After booting back up, open **Event Viewer** > **Windows Logs** > **System** — filter for events around the shutdown time. Look for **6006/6008** (event log service stop/start, marking the shutdown window) and any service timeout errors (event 7045/7034 or application hangs).
3. **Event Viewer** > **Windows Logs** > **Application** — check for application hang events timestamped at shutdown.
4. The Reliability Monitor (search "Reliability" in Start) shows a timeline — shutdown failures and critical events appear as red X marks on the shutdown date.
5. Time three shutdowns with a stopwatch and note consistency: consistent slowness = systematic cause; occasional hangs = a specific app or update.

### Fix 2: Close apps cleanly before shutdown

The simplest fix for the most common cause.

1. Before shutting down, close all apps manually (`Alt + F4` through them or right-click taskbar icons > Close).
2. Pay attention to which app resists: browsers with "restore session" prompts, Office apps with unsaved documents, IDEs, and games are frequent blockers.
3. In **Settings** > **Accounts** > **Sign-in options**, check **Automatically save my restartable apps** — turning this off can speed shutdowns (Windows won't try to gracefully persist app state), at the cost of apps not reopening after restart.
4. For apps that hang on close: update them — shutdown hangs are often fixed app bugs. Check the vendor's site for newer versions.
5. Make it a habit for a week: manual close-all before shutdown. If shutdowns are suddenly fast, you've confirmed the cause category — then decide which specific app to update, replace, or always close first.

### Fix 3: Tame Lenovo's shutdown-blocking services

Lenovo utilities are frequent shutdown delayers.

1. Open **Lenovo Vantage** > **Settings** — disable options like automatic updates checks and telemetry that spawn background work at shutdown time.
2. **Services** (`services.msc`): find Lenovo services (telemetry, "ImController," update-related) — set non-essential ones to **Manual**. Keep driver/update-critical ones on Automatic.
3. **Task Scheduler**: look for Lenovo tasks scheduled "at logoff" or shutdown-adjacent triggers — these run during shutdown and delay it. Disable the non-essential ones.
4. Task Manager > **Startup apps**: disable Lenovo entries you don't need — fewer running services means fewer to terminate at shutdown.
5. Test: time three shutdowns after the changes. Lenovo service cleanup commonly cuts 20–40 seconds off pathological shutdowns. Get driver updates from [Lenovo Support](https://support.lenovo.com/us/en/) rather than removing Vantage entirely — it's genuinely useful when tamed.

### Fix 4: Fix network-driver shutdown delays

Drivers waiting on network timeouts are silent shutdown killers.

1. Before shutdown, disconnect from VPNs manually — VPN clients are notorious for hanging shutdown while tearing down tunnels.
2. Update Wi-Fi and Ethernet drivers from [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model — or Intel's latest via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel adapters.
3. In Device Manager > network adapter > **Properties** > **Power Management**: uncheck **Allow the computer to turn off this device to save power** as a test — sometimes the power-down handshake itself hangs.
4. If you use a USB network adapter or dock Ethernet, test shutdowns with it unplugged — dock drivers are frequent offenders.
5. Disable **Wake on LAN** features you don't use (Device Manager > adapter > Advanced) — WoL drivers sometimes linger during shutdown negotiating with the network.

### Fix 5: Adjust shutdown timeouts (carefully)

Reduce how long Windows politely waits for stuck processes.

1. Open Registry Editor (`regedit`) and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.
2. Find **WaitToKillServiceTimeout** — the default is 20000 (20 seconds per service). You can lower it to 5000 (5 seconds). This is safe: it only shortens the wait before Windows force-terminates an already-hung service.
3. In `HKEY_CURRENT_USER\Control Panel\Desktop`, check **WaitToKillAppTimeout** (default 20000) — lower to 5000, and ensure **AutoEndTasks** is set to 1 (auto-ends hung apps instead of waiting forever).
4. Back up the keys first (right-click > Export) — standard registry caution.
5. Reboot, then time shutdowns. This doesn't fix the underlying hang, but it converts a 2-minute shutdown into a 20-second one while you hunt the root cause with the other fixes.
6. Never set these to 0 — that risks data corruption by killing apps mid-write. 5000ms is the sensible floor.

### Fix 6: Check pagefile clearing and fast startup

Two settings that directly change shutdown behavior.

1. Check whether pagefile clearing is enabled: `regedit` > `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management` > **ClearPageFileAtShutdown**. If it's 1, set it to 0 — clearing the pagefile on every shutdown adds many seconds (it's a security feature most home users don't need).
2. Test fast startup both ways: `powercfg.cpl` > **Choose what the power buttons do** > toggle **Turn on fast startup**. Time shutdowns in each state.
3. With fast startup on, "shutdown" hibernates the kernel — usually faster, but carries driver state over. With it off, you get a true clean shutdown — slower but more honest.
4. If full shutdowns (fast startup off) hang but hybrid ones don't, a driver is misbehaving during full teardown — update chipset and storage drivers from Lenovo Support.
5. Unplug USB drives/peripherals before shutdown as a test — a drive that won't spin down promptly stalls the whole sequence.

### Fix 7: Repair system files and update everything

The systemic fixes for unidentified hangers.

1. Elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth` → `sfc /scannow` → reboot.
2. **Settings** > **Windows Update** — install everything. Shutdown slowness during "update finalization" periods is legitimate; judge only after fully updated.
3. Update the **BIOS** from Lenovo Support — firmware-level power management affects shutdown sequencing, and Lenovo has fixed shutdown hangs in BIOS updates.
4. [Perform a clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) and shut down from it — fast shutdown in clean boot proves a third-party program; re-enable in halves to find it.
5. If Event Viewer consistently names one service, search its name plus "slow shutdown" — there's often a known fix or a newer version. Microsoft documents shutdown troubleshooting at [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

Slow shutdowns are Windows waiting on something — an app, a Lenovo service, a network driver — through generous timeouts. Find the waiter with Event Viewer, close apps cleanly, tame Lenovo's background services, update network drivers, and trim the timeouts. Shutdown should be a 15-second affair, not a staring contest with a spinner.
