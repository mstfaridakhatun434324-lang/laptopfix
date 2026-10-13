---
title: "Windows 11 Taking Forever to Shut Down? Here's the Fix"
slug: how-do-i-fix-shutdown-takes-long-windows-11
date: 2026-09-27
categories: ["performance"]
tags: ["slow shutdown", "windows 11", "shutdown hang", "power", "troubleshooting"]
description: "Windows 11 hanging on shutdown for minutes? Find what's blocking shutdown and fix slow shutdowns for good."
thumbnail: "/images/thumbs/how-do-i-fix-shutdown-takes-long-windows-11.webp"
faqs:
  - q: "Why does Windows 11 take so long to shut down?"
    a: "Shutdown stalls when Windows waits on something: an app refusing to close, a background service taking too long to stop, a driver hanging during power-down, or Windows Update installing in the background. Windows gives each app 20 seconds by default before forcing it closed — a few stubborn apps stack those timeouts into minutes. The Event Viewer shutdown logs name the exact blockers."
  - q: "Is it safe to force shutdown when Windows hangs?"
    a: "Occasionally, yes — holding the power button is a last resort, not a routine. Forced shutdowns risk corrupting files that were being written and can damage the update state if updates were installing. Fix the underlying blockers instead so normal shutdowns complete in seconds. If you must force it, wait at least 5 minutes first to rule out a slow-but-working update."
  - q: "Can Windows Update cause slow shutdowns?"
    a: "Yes — 'Update and shut down' legitimately takes longer as updates install, sometimes 10+ minutes for feature updates. That's normal and shouldn't be 'fixed.' The problem is when *every* shutdown is slow with no update involved. Check Settings > Windows Update to see if updates are pending — if so, let them finish rather than fighting the shutdown time."
  - q: "What is the normal shutdown time for Windows 11?"
    a: "A healthy Windows 11 laptop on an SSD shuts down in roughly 10–25 seconds from clicking Shut down to power off. Anything consistently over a minute indicates a blocker worth investigating. Time a few shutdowns to establish your baseline — occasional slow ones during updates are fine; every-time slow ones are not."
---

Clicking **Shut down** should end your day in seconds. When the "Shutting down" spinner grinds for minutes — or hangs indefinitely until you hold the power button — something is refusing to let go. It's annoying, it wastes your time, and forced power-offs risk your files.

Slow shutdowns have specific, findable causes: an application that won't close, a service that takes forever to stop, a driver hanging during power transition, or updates installing silently. Windows even logs exactly what's blocking shutdown — you just need to know where to look. Here's the fix, in order.

## Why this happens

- **Apps refusing to close**: Programs with unsaved work or hung windows make Windows wait out the timeout per app.
- **Services slow to stop**: Third-party services (updaters, sync tools, security software) with long stop routines.
- **Driver power-transition hangs**: Drivers failing to handle the shutdown power state, stalling the kernel.
- **Windows Update installing**: Legitimate update installation during shutdown — slow but normal.
- **Network resources**: Open files on network shares or mapped drives timing out during disconnect.
- **Corrupt hibernation/Fast Startup state**: Damaged hybrid-shutdown data causing hangs.
- **Background tasks**: Scheduled tasks or maintenance running at the moment you shut down.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the blocker in Event Viewer

Windows logs shutdown delays — read the log first.

1. Press **Win + R**, type `eventvwr.msc`, and press Enter.
2. Navigate to **Windows Logs** > **System**. Click **Filter Current Log** and enter event IDs `203, 204, 205, 1074, 6006` — these cover shutdown performance and blockers.
3. Look for entries like "This application took longer than expected to close" — they name the exact application or service.
4. Also check **Applications and Services Logs** > **Microsoft** > **Windows** > **Diagnostics-Performance** > **Operational**, filtered for event ID `203` (shutdown degradation) — it lists slow components with timings.
5. Write down the named blockers. If it's always the same app or service, you've found your target. If shutdowns are just generally slow with no named blocker, continue through the fixes.

### Fix 2: Close the usual suspects before shutdown

Build a shutdown routine that removes the common blockers.

1. Before shutting down, close all applications manually — especially browsers with many tabs, Office apps, and anything that was syncing or downloading.
2. Check the **system tray** (^ icon) for apps running in the background: cloud sync clients, chat apps, updaters. Right-click > **Quit** the ones you don't need.
3. Disconnect mapped network drives you don't need: **File Explorer** > right-click the mapped drive > **Disconnect**. Open network files force timeout waits during shutdown.
4. Save all work first — apps with unsaved changes trigger the "waiting for app" screen, which pauses shutdown until timeout.
5. Test: with everything closed manually, time the shutdown. If it's fast now, the blocker was an app — reintroduce apps one evening at a time to find which one.

### Fix 3: Reduce the hung-app timeout

When apps hang, don't let Windows wait so long for them.

1. Press **Win + R**, type `regedit`, approve UAC. **Back up first**: File > Export.
2. Navigate to `HKEY_CURRENT_USER\Control Panel\Desktop`.
3. Find or create the string value `HungAppTimeout` and set it to `2000` (milliseconds, down from the default 5000).
4. Find or create `WaitToKillAppTimeout` and set it to `2000` (down from 20000) — this is the big one for slow shutdowns.
5. Also set `AutoEndTasks` to `1` so Windows automatically ends hung apps instead of showing the wait screen. Reboot for changes to take effect, then time your shutdowns.

### Fix 4: Speed up service shutdown

Services get their own timeout — tighten it.

1. In the same registry area, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.
2. Find or create the string value `WaitToKillServiceTimeout` and set it to `5000` (milliseconds, down from the default 20000+ on some systems).
3. Identify slow services: in **Event Viewer** > **System**, look for Service Control Manager entries (event ID 7045/7036 patterns) around shutdown time naming slow-stopping services.
4. For third-party services that are consistently slow (updaters, RGB software, printer utilities), consider disabling them: `services.msc` > service > **Startup type: Disabled** — or uninstall the parent app if unused.
5. Keep Windows' own services and your antivirus service alone — only target third-party services you've identified as slow. See [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) for safe service-trimming principles.

### Fix 5: Address updates, drivers, and Fast Startup

Rule out the system-level causes.

1. Open **Settings** > **Windows Update**: if updates are pending or "Update and shut down" appears, let them install — time that shutdown separately and don't count it as a problem.
2. Update **chipset and storage drivers** from your vendor ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — driver power-transition hangs are a real shutdown killer.
3. Toggle **Fast Startup** off as a test: Control Panel > Power Options > Choose what the power buttons do > uncheck **Turn on fast startup**. Some systems shut down cleaner without hybrid shutdown.
4. Rebuild the hibernation file: elevated Command Prompt > `powercfg /h off`, reboot, then `powercfg /h on`.
5. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt to repair any corrupt shutdown components. Microsoft documents power troubleshooting at Windows support.

### Fix 6: Check for deeper issues

When shutdowns hang hard (not just slow), dig deeper.

1. If shutdown *never* completes (spinner forever), note whether the disk activity light is active — active = something working (wait); dark = true hang.
2. Boot into **Safe Mode** and shut down from there. Fast shutdown in Safe Mode convicts a third-party driver or service — use clean-boot isolation (msconfig) to find it.
3. Check **Reliability Monitor** (search Start): it logs shutdown failures with faulting modules — a driver name here is gold.
4. Test with all USB devices disconnected — faulty USB devices hang the power transition surprisingly often.
5. If a specific driver is named, update it from the chipmaker (Intel, NVIDIA, AMD) or roll it back if the problem started after an update.

## Closing

Slow shutdowns aren't mysterious — Windows logs the blockers, timeouts are tunable, and the usual suspects (hung apps, slow services, updates, drivers) each have a fix. Diagnose with Event Viewer, tighten the timeouts, clear the blockers, and shutdown goes back to taking seconds. If startup is slow too, see [speeding up a slow Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/).
