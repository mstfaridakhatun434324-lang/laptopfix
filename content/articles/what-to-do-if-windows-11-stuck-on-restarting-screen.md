---
title: "What to Do If Windows 11 Is Stuck on the Restarting Screen"
slug: what-to-do-if-windows-11-stuck-on-restarting-screen
date: 2026-09-09
categories: ["windows-errors"]
tags: ["restart", "hang", "windows 11"]
description: "Windows 11 stuck on \"Restarting\" with the spinning dots forever? Here's what's hanging the shutdown and how to get moving again."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the Restarting screen?"
    a: "Give it 10-15 minutes — Windows may be finishing updates or flushing large writes. If the spinner is still going after 20-30 minutes with no disk activity (no drive light, no fan changes), it's genuinely stuck and safe to force-power-off."
  - q: "Is it safe to force-shut-down when stuck on Restarting?"
    a: "After 20+ minutes of no progress, yes — the risk of data loss is low because Windows already closed your apps before showing this screen. Hold the power button 5-10 seconds. Then fix the underlying cause so it doesn't recur."
  - q: "Why does my laptop get stuck on Restarting every time?"
    a: "Recurring hangs point to a driver that won't unload (often network, audio, or USB drivers), a Windows Update stuck mid-install, Fast Startup preserving bad state, or a service that refuses to stop. The fixes below address each."
  - q: "Could this damage my SSD or Windows installation?"
    a: "Occasional forced shutdowns are harmless to modern SSDs. Repeated ones during actual disk writes can corrupt files — which is why you should fix the root cause rather than force-power-off every time."
---

The "Restarting" screen with its endless spinning dots is Windows caught between two states: it's closed your session but can't finish shutting down the system. Ten minutes is patience; thirty minutes is a hang. At that point, waiting longer won't help — something is blocking the shutdown, and you need to deal with it.

The forced shutdown gets you moving now; the fixes below stop it from happening again. There's an important distinction: a one-time hang during an update is normal-ish, but a hang every restart is a driver or service problem worth hunting down.

## Why this happens

- **Driver refusing to unload**: Network, audio, USB, or GPU drivers that hang during the shutdown sequence — the most common recurring cause.
- **Windows Update stuck mid-install**: An update that can't complete its restart phase holds the shutdown hostage.
- **Fast Startup preserving bad state**: Hybrid shutdown saves kernel state; corrupted state replays the hang every time.
- **Service that won't stop**: Third-party services (antivirus, backup tools, updaters) ignoring the shutdown signal.
- **External devices blocking shutdown**: USB drives, docks, or peripherals that Windows waits on indefinitely.
- **Corrupted system files**: Damage to shutdown-related components from a bad update or forced power-offs.

## How to fix it

Work through these in order — recover first, then prevent recurrence.

### Fix 1: Force-shut-down safely and boot cleanly

Get unstuck now without making things worse.

1. Wait at least 15-20 minutes on the first occurrence — it might be a legitimate update finishing.
2. If still stuck, press and hold the power button for 5-10 seconds until the laptop powers off.
3. Unplug all USB devices, docks, and external drives.
4. Power on. If Windows boots normally, the hang was transient or device-related.
5. If it boots into "Preparing Automatic Repair," let it finish — then see our [Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-youtube/) if it loops.

### Fix 2: Disable Fast Startup

Fast Startup is a frequent repeat offender for shutdown/restart hangs.

1. Press **Win + R**, type `control`, press Enter.
2. Go to **Hardware and Sound** > **Power Options** > **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)** > **Save changes**.
5. Restart (from the Start menu, not shutdown) and observe. If restarts are now clean, Fast Startup was preserving the bad state.
6. Note: disabling it makes cold boots slightly slower — a fair trade for reliability.

### Fix 3: Finish or repair Windows Update

A stuck update is the classic one-time cause that becomes recurring if never resolved.

1. Open **Settings** > **Windows Update** and check for a failed or pending update.
2. If one is stuck, run the troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
3. For a deeply stuck update, reset the update components from an elevated Command Prompt:
   `net stop wuauserv`
   `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
   `net start bits`
4. Check for updates again and let them install fully — then restart and confirm the hang is gone.
5. Microsoft documents update troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Identify the hanging driver or service

For hangs that recur, find what's blocking shutdown.

1. Open **Event Viewer** (**Win + X** > **Event Viewer**).
2. Navigate to **Windows Logs** > **System** and filter for the time of the hang. Look for errors from **Service Control Manager** (services timing out) or driver warnings just before the shutdown.
3. Common culprits: network drivers, audio drivers (Realtek), and USB controllers. Update them from your manufacturer's site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — or via [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html).
4. If a third-party service is the blocker, set it to **Manual** in `services.msc` or uninstall the parent program.
5. As a diagnostic, clean-boot (**Win + R** > `msconfig` > hide Microsoft services > **Disable all**) and restart — if the hang disappears, re-enable in halves.

### Fix 5: Disconnect external devices before restart

USB devices are a silent cause of shutdown hangs.

1. Before restarting, unplug USB drives, hubs, docks, printers, and external GPUs.
2. Restart. If it's clean, reconnect devices one at a time across restarts to find the offender.
3. For a device you must keep connected, update its driver, and in **Device Manager** check its **Power Management** tab — try toggling **Allow the computer to turn off this device to save power**.
4. Faulty USB hubs are a particularly common culprit; test with a different hub or direct connection.

### Fix 6: Run system file repairs

Corruption in shutdown components causes hangs that survive driver updates.

1. Open an elevated Command Prompt (**Win + S**, type `cmd`, right-click > **Run as administrator**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. Restart and test. If SFC fixes corruption, the hangs often stop immediately.
4. Also check disk health with `chkdsk C: /f` (schedule and reboot) — file system errors can stall shutdown writes.

### Fix 7: Adjust the hung-service timeout (advanced)

If a specific service always times out, you can shorten how long Windows waits — but only after identifying it in Fix 4.

1. Press **Win + R**, type `regedit`, press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.
3. Find or create the string value `WaitToKillServiceTimeout` and set it to `5000` (5 seconds, in milliseconds).
4. This doesn't fix the underlying problem — it just stops one bad service from holding every restart hostage. Fix or remove the service itself when you can.
5. If hangs persist through everything, an in-place upgrade from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) refreshes the shutdown path while keeping files and apps.

If the stuck restart escalates into blue screens, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) picks up where this leaves off.

## Closing

A stuck "Restarting" screen is Windows waiting on something that will never finish — usually a driver, a stuck update, or Fast Startup replaying a bad state. Force the shutdown once, then work the list: disable Fast Startup, clear the update jam, update the hanging driver, and unplug the troublesome USB device. Restarts should take a minute, not half an hour, and after these fixes they will.
