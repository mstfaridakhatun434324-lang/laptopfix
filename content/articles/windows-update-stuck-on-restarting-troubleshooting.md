---
title: "Windows Update Stuck on Restarting? Here's the Fix"
slug: windows-update-stuck-on-restarting-troubleshooting
date: 2026-09-29
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update", "restart loop", "troubleshooting"]
description: "Your laptop hangs on Restarting during a Windows update? Learn how to tell slow from stuck and recover safely without losing data."
thumbnail: "/images/thumbs/windows-update-stuck-on-restarting-troubleshooting.webp"
faqs:
  - q: "How long can a Windows update legitimately stay on the Restarting screen?"
    a: "On a modern laptop with an SSD, the Restarting phase during an update usually takes 5 to 20 minutes. On machines with hard drives or large feature updates, 30 to 60 minutes is still normal. Only consider it stuck if the screen is unchanged, with no disk activity, for over an hour on an SSD machine or two hours on a hard drive machine."
  - q: "Is it safe to force shutdown during the Restarting screen?"
    a: "It is a last resort, not a first move. Interrupting the offline install phase triggers an automatic rollback, which is designed to be safe but can occasionally corrupt the update state. Only force a shutdown after confirming genuine zero activity for over an hour, and always attempt it with the laptop plugged into AC power."
  - q: "Why does my laptop get stuck on Restarting every update?"
    a: "Recurring stalls point to a systematic problem: a driver that deadlocks during the boot handoff, a failing hard drive that cannot complete file operations, or fast startup interfering with the restart sequence. Fix the underlying cause with the driver and disk checks below instead of force-shutting down every month."
  - q: "Will a stuck restart damage my Windows installation?"
    a: "Usually not. Windows is designed to roll back an interrupted update to the previous working state, and your files are not touched during this process. Damage happens only in rare cases where the disk itself is failing. If rollbacks complete cleanly each time, your installation is intact and the stall has an external cause worth diagnosing."
---

The Restarting screen during a Windows update is a special kind of limbo. The spinner spins, the dots circle, and minutes turn into an hour with no percentage, no message, and no clue whether anything is happening. On a laptop you need for work tomorrow, every extra minute feels like a gamble.

Most of the time, the machine is actually working through the offline phase of the update: replacing locked system files, migrating drivers, and updating the boot environment. That work is disk-heavy and progress-poor, which is exactly why the screen looks frozen. But genuine stalls happen too, usually from the same culprits every time.

This guide gives you the technician's playbook: how to read the signs, how long to wait, how to recover safely when waiting fails, and how to stop it from happening every update.

## Why this happens

- **Offline file replacement is slow:** The restart phase replaces files that were locked while Windows ran, and on hard drives this takes a long time with no progress display.
- **Driver migration deadlock:** A driver fails to hand off during the boot transition, freezing the sequence silently.
- **Fast Startup interference:** The hybrid shutdown feature can conflict with the update's expected full restart cycle.
- **Failing hard drive:** Bad sectors stall file operations with endless retries that look identical to a freeze.
- **Windows Update service hang:** The service orchestrating the restart stops responding mid-sequence.
- **Peripheral driver waits:** Connected USB devices hold up the boot handoff while their drivers wait on hardware.
- **Corrupted pending update state:** A previous interrupted update leaves operations queued that the current restart cannot complete.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the activity signs before doing anything

1. Look for the disk activity LED on your laptop. Flickering or solid activity means the update is progressing.
2. Listen for hard drive sounds on HDD machines. Rhythmic seeking means work is happening; total silence for an hour means a stall.
3. Feel for heat and fan activity. A working update keeps the CPU busy enough to warm the chassis.
4. If any sign shows life, plug in the charger and wait. Only proceed to forced recovery after a full hour of zero activity on SSD machines.

### Fix 2: Force a shutdown only as a last resort

1. After confirming a genuine stall, press and hold the power button for 10 seconds until the laptop powers off completely.
2. Wait 30 seconds, then power on. Windows should detect the interrupted update and begin an automatic rollback.
3. Let the rollback finish without interrupting it, even if it takes 30 minutes. Interrupting a rollback is far riskier than interrupting the original update.
4. Once back in Windows, do not immediately retry the update. Work through the fixes below first so the stall does not repeat.

### Fix 3: Disable Fast Startup to clean up the boot cycle

1. Open Control Panel, go to **Power Options > Choose what the power buttons do**, and click **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup** and save the changes.
3. Fast Startup's hybrid shutdown can confuse the update restart sequence, especially after a rollback.
4. Restart normally once to establish a clean boot cycle, then attempt the update again. If updates broadly misbehave, the [update service guide](/articles/windows-update-service-not-running-troubleshooting/) covers the service-level repairs.

### Fix 4: Check the hard drive health

1. Recurring restart stalls on older laptops often mean a dying drive. Open an admin Command Prompt and run `wmic diskdrive get status`.
2. If the status is not OK, back up your data immediately before attempting any further updates.
3. Run `chkdsk C: /scan` in admin PowerShell to check for file system problems that stall the offline phase.
4. A healthy drive eliminates the most dangerous cause. If the drive is failing, replace it before updating, since a major update on a dying disk risks everything.

### Fix 5: Update drivers that deadlock the boot handoff

1. In Device Manager, update the chipset, storage controller, and graphics drivers from your laptop maker's support page, not just Windows Update.
2. Pay special attention to storage drivers. The restart phase hands the disk between the old and new kernels, and outdated AHCI or NVMe drivers stall exactly there.
3. Uninstall any grayed-out hidden devices in Device Manager that represent long-removed hardware with lingering drivers.
4. Disconnect all USB peripherals before retrying the update. A single misbehaving USB driver can hold the entire boot sequence hostage.

### Fix 6: Reset the update pipeline after a rollback

1. After a rollback, the update state is often messy. Open an admin Command Prompt and run `net stop wuauserv`, then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then `net start wuauserv`.
2. Run the Windows Update troubleshooter from **Settings > System > Troubleshoot > Other troubleshooters**.
3. Repair system files with `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to clear corruption the interrupted update may have left.
4. Check the [Windows support hub](https://support.microsoft.com/en-us/windows) for any known issues with the specific update before retrying.

### Fix 7: Install the update manually to bypass the stall

1. Note the KB number from **Settings > Windows Update > Update history**.
2. Download the standalone installer from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), choosing the version that matches your system architecture.
3. Install it with all USB devices disconnected and Fast Startup still disabled.
4. Manual installs run the offline phase with fewer competing processes and often complete where the automatic restart stalled. If the failure instead produces a driver error code, see the [0xC1900101 troubleshooting guide](/articles/update-fails-with-error-0xc1900101-troubleshooting/).

## Closing

A stuck Restarting screen is usually a slow offline phase, not a dead update. Verify activity, wait appropriately, and only force recovery when the signs confirm a true stall. Fix the drivers, the disk, and Fast Startup afterward, and the next update restarts cleanly. Keep a habit of checking drive health yearly on older laptops, since the restart phase is always the first place a failing disk shows its weakness.
