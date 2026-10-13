---
title: "Windows 11 Stuck on the Restarting Screen? Quick Fixes"
slug: windows-11-stuck-on-restarting-screen-fix
date: 2026-09-13
categories: ["windows-errors"]
tags: ["windows-11", "restart-loop", "startup-issues"]
description: "Your laptop spinning on the restarting screen forever? These fixes break the hang and get Windows 11 booting normally again."
thumbnail: "/images/thumbs/windows-11-stuck-on-restarting-screen-fix.webp"
faqs:
  - q: "How long should I wait on the restarting screen before doing something?"
    a: "Give it 10–15 minutes the first time, especially if Windows just installed updates — some updates genuinely take a while. If the spinner is still going after 20 minutes with no disk activity (no drive light flicker, no fan changes), it's hung and you should force a shutdown."
  - q: "Will forcing a shutdown while stuck on restart damage Windows?"
    a: "Occasionally it can corrupt an update that was mid-install, which is why you wait first. One forced shutdown is rarely catastrophic, and Windows 11 is good at rolling back a failed update. If it boots into recovery afterward, that's normal — just continue from there."
  - q: "Why does this keep happening after every Windows update?"
    a: "Recurring hangs usually mean a stuck update component, a corrupted SoftwareDistribution folder, or a driver that conflicts with the new build. Clearing the update cache and updating drivers breaks the cycle in most cases."
  - q: "Can a USB device cause the restarting screen to hang?"
    a: "Yes — external drives, docks, and even some USB hubs can stall the restart sequence while Windows waits on them. Unplug everything except the charger before restarting as a quick first test."
---
Few things are as maddening as watching your laptop spin on the blue "Restarting" screen long after it should have finished. You told it to restart ten minutes ago, and it's still showing that little dotted circle, going nowhere. This usually happens after a Windows update, a driver install, or a program that refused to close cleanly.

The hang is almost always caused by something that won't let go: a stuck Windows Update component, a service that won't stop, a misbehaving driver, or an external device Windows keeps waiting on. Here's how to break out of it and stop it from coming back.

## Why this happens

- **A Windows update got stuck mid-restart.** The update service downloaded files but can't finish applying them, so the restart sequence waits indefinitely for a step that will never complete.
- **A background service or app won't terminate.** Some third-party services (antivirus, backup tools, updaters) ignore Windows' shutdown requests, and the restart timer never expires.
- **A driver is hanging the shutdown sequence.** Display, storage, or network drivers that fail to respond to the power-off command keep the whole restart pipeline stuck.
- **Fast Startup is conflicting with a fresh restart.** The hybrid shutdown state can hold onto broken session data that a normal restart was supposed to clear.
- **An external device is stalling the process.** USB drives, docking stations, and SD cards can make Windows wait on hardware responses during the hardware re-enumeration that happens at boot.
- **Corrupted system files or a damaged update cache.** If key files in the update store are corrupt, every restart attempt trips over the same broken step.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop as soon as restarts work normally again.

### Fix 1: Force a clean shutdown and disconnect everything

Before doing anything fancy, rule out the simple causes.

1. Hold the power button for 10 seconds until the laptop powers off completely.
2. Unplug every USB device: drives, docks, hubs, receivers, SD cards. Leave only the charger connected.
3. Wait 30 seconds, then power on and sign in.
4. Try restarting from **Start > Power > Restart** and watch whether it completes this time. If it does, one of those devices was the culprit — plug them back one at a time to find it.

### Fix 2: End the hanging processes before you restart

If restarts hang but shutdowns work, a stubborn program is likely the cause.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. Look under **Processes** for anything marked **Not responding**, especially third-party updaters, backup tools, or antivirus components.
3. Select each one and click **End task**.
4. Go to the **Startup apps** tab and disable anything non-essential — you can re-enable them later.
5. Try the restart again. A clean boot, described in our guide to [performing a clean boot on Windows 11](/articles/how-can-i-perform-clean-boot-windows-11/), is the deeper version of this step if the problem persists.

### Fix 3: Turn off Fast Startup

Fast Startup is a known cause of restart hangs because it turns restarts into glorified log-offs.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully, wait 10 seconds, power on, and test a restart.

### Fix 4: Clear the stuck Windows Update cache

This is the fix for hangs that started right after a Windows update.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Stop the update services:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptSvc`
3. Rename the update folders so Windows rebuilds them fresh:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start bits`
   `net start cryptSvc`
5. Go to **Settings > Windows Update** and click **Check for updates** — let any pending updates install cleanly, then restart. If an update is corrupted, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you download and install it manually as a standalone package.

### Fix 5: Run the system file and image repair tools

Corrupted system files can break the restart pipeline itself.

1. Open an elevated **Command Prompt** (as administrator).
2. Run `sfc /scannow` and wait for it to complete — about 10–15 minutes.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`. This needs internet access.
4. Restart and test. If you can't reach the desktop at all, both tools also run from the **Command Prompt** option inside the recovery environment (see Fix 6).

### Fix 6: Use Startup Repair from the recovery environment

If the laptop won't boot properly after the forced shutdown, let Windows repair itself.

1. Force the laptop off, then power on. Interrupt the boot by holding the power button at the logo screen. Do this **three times** to trigger the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Let it run — it diagnoses boot problems and fixes common ones automatically. Our walkthrough of [using Startup Repair on Windows 11](/articles/how-can-i-use-startup-repair-windows-11/) covers what to do if it says it couldn't repair your PC.

### Fix 7: Check for a failing drive

Repeated restart hangs paired with slowness can signal a dying storage drive.

1. Open an elevated **Command Prompt**.
2. Run `chkdsk C: /f /r` — type **Y** when asked to schedule it, then restart. The scan runs before Windows loads and can take a while on large drives.
3. After booting, check drive health: in **PowerShell (Admin)**, run `Get-PhysicalDisk | Select FriendlyName, HealthStatus, OperationalStatus`.
4. If the health status shows anything other than **Healthy**, back up your files immediately and plan a drive replacement — no software fix will save a failing drive. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the recovery options if Windows itself won't start at this point.

## Closing

A laptop stuck on the restarting screen feels broken, but the cause is usually mundane: a stuck update, a stubborn service, or an external device Windows keeps waiting on. Force a clean shutdown, disconnect your peripherals, and clear the update cache, and most hangs disappear. If the problem keeps returning after every update, keep the update services and drivers healthy — that's what prevents the next hang before it starts.
