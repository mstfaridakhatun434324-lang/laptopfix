---
title: "Windows 11 Stuck on the Restarting Screen on a Lenovo Laptop? Fix It Here"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-on-lenovo-laptop
date: 2026-10-02
categories: ["windows-errors"]
tags: ["windows-11", "restart-loop", "lenovo"]
description: "Lenovo laptop hanging on the restarting screen? From Novo button recovery to driver fixes — get it booting cleanly again."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-on-lenovo-laptop.webp"
faqs:
  - q: "Why does my Lenovo get stuck on the restarting screen?"
    a: "The usual causes are a stuck Windows Update component, a Lenovo utility or driver that won't terminate, Fast Startup holding a broken state, or an external device (dock, USB drive) that Windows waits on. Lenovo-specific utilities like Vantage services are worth checking since they hook into shutdown."
  - q: "What is the Novo button and how does it help?"
    a: "The Novo button is the small recessed button (or pinhole) on the side of most Lenovo laptops. Pressing it while the laptop is off boots directly into the Novo Button Menu, giving you one-press access to BIOS Setup, Boot Menu, and System Recovery — no need for the three-interrupt trick to reach recovery tools."
  - q: "How long should I wait before forcing it off?"
    a: "Give it 10–15 minutes, especially after updates. If the spinner is still going after 20 minutes with no sign of disk activity, it's genuinely hung — hold the power button for 10 seconds to force it off, then work through the fixes below."
  - q: "Will this keep happening after every update?"
    a: "Recurring hangs point to a stuck update cache or an outdated Lenovo driver conflicting with the new build. Clearing the update cache (Fix 4) and updating everything through Lenovo Vantage System Update (Fix 5) breaks the cycle for most people."
---
A Lenovo laptop spinning forever on the blue "Restarting" screen is frustrating — but Lenovo gives you better recovery tools than most brands, including the Novo button that jumps straight to recovery without the usual key gymnastics. The hang itself has the same usual causes as on any Windows 11 machine: a stuck update, a service that won't quit, Fast Startup preserving a broken state, or a peripheral Windows keeps waiting on.

Here's the fix sequence tuned for Lenovo hardware, using the tools Lenovo built for exactly this situation.

## Why this happens

- **A Windows update stuck mid-restart.** The update service can't finish applying files, so the restart waits forever on a step that never completes.
- **A Lenovo service or utility won't terminate.** Vantage services, hotkey utilities, or the ImController service can occasionally hang the shutdown sequence.
- **Fast Startup preserving a broken state.** The hybrid shutdown reloads the same broken driver state every boot.
- **An external device stalling restart.** USB docks (very common with ThinkPads), external drives, and hubs can make Windows wait on hardware responses.
- **Outdated Lenovo drivers conflicting with the build.** Chipset, power management, or storage drivers that predate your Windows build.
- **Corrupted update cache or system files.** Damage that makes every restart trip over the same broken step.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once restarts complete normally.

### Fix 1: Force a clean shutdown and unplug everything

Rule out the simple causes first.

1. Hold the power button for 10 seconds until the laptop is fully off.
2. Unplug every USB device — docks, hubs, drives, receivers, SD cards. ThinkPad docks are a particularly common restart-hang culprit. Leave only the charger.
3. Wait 30 seconds, power on, sign in, and try **Start > Power > Restart**.
4. If it completes, reconnect devices one at a time to find the offender.

### Fix 2: Use the Novo button to reach recovery

Lenovo's shortcut when Windows won't cooperate.

1. Power the laptop off completely.
2. Find the **Novo button** — a small recessed button on the side (press with a paperclip) or a pinhole on some models. On some ThinkPads, **F11** at boot opens similar options.
3. Press it, and choose **System Recovery** from the Novo Button Menu to boot straight into the Windows Recovery Environment — no triple-interrupt dance needed.
4. From here you can access **Startup Repair**, **System Restore**, **Command Prompt**, and **Reset this PC** directly. If the laptop boots fine after this, continue with the fixes below to stop it recurring.

### Fix 3: Turn off Fast Startup and end hanging processes

Stop the two most common software hang sources.

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, uncheck **Turn on fast startup**, and save.
3. Press **Ctrl + Shift + Esc** to open **Task Manager**. Under **Processes**, end anything **Not responding**, especially third-party updaters.
4. Go to the **Startup apps** tab and disable non-essential items — including Lenovo utilities you don't use — then test a restart.

### Fix 4: Clear the stuck Windows Update cache

The fix for hangs that started after an update.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Stop the services:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptSvc`
3. Rename the cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start bits`
   `net start cryptSvc`
5. Go to **Settings > Windows Update**, install any pending updates cleanly, then restart.

### Fix 5: Update all Lenovo drivers with Vantage

Outdated Lenovo drivers are a prime suspect for recurring hangs.

1. Open **Lenovo Vantage** and go to **Device > System Update**.
2. Click **Check for Updates** and install everything offered — especially BIOS, chipset, power management, and storage drivers.
3. Restart when prompted and complete every pending update.
4. If you don't have Vantage, get drivers from [Lenovo's support site](https://support.lenovo.com/us/en/) using your serial number. Fresh, validated drivers eliminate the shutdown-sequence conflicts that cause these hangs. The same update-everything approach helps related Lenovo issues like [blue screens after updates on Lenovo laptops](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/).

### Fix 6: Repair system files and check the drive

Fix corruption in the restart pipeline itself — a damaged component here makes every restart trip over the same broken step.

1. Open an elevated **Command Prompt**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check the disk: `chkdsk C: /f` — type **Y** to schedule it, then restart so the scan runs before Windows loads.
4. In **PowerShell (Admin)**, verify health: `Get-PhysicalDisk | Select FriendlyName, HealthStatus, OperationalStatus`. Our general [restarting screen fix guide](/articles/windows-11-stuck-on-restarting-screen-fix/) covers these repairs in a brand-neutral context too.

### Fix 7: Run Startup Repair or reset as a last resort

When the hang survives everything else.

1. Boot to recovery with the Novo button (Fix 2), go to **Troubleshoot > Advanced options > Startup Repair**, and let it run.
2. If that doesn't help, try **System Restore** from the same menu — pick a date before the hangs started.
3. Final option: **Troubleshoot > Reset this PC > Keep my files** with **Cloud download**.
4. After recovery, install Lenovo Vantage first and update everything before restoring your workflow. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the recovery options if you need more detail.

## Closing

A Lenovo stuck on the restarting screen is usually a stuck update, a hanging service, or a dock Windows won't let go of — and the Novo button gives you a direct line to recovery when nothing else responds. Force a clean shutdown, disconnect peripherals, clear the update cache, and keep Lenovo's drivers current through Vantage. Do that, and the endless spinner becomes a one-time annoyance instead of a recurring ritual, not a habit.
