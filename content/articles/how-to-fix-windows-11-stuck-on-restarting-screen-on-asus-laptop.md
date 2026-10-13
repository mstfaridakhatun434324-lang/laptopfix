---
title: "Fix Windows 11 Stuck on the Restarting Screen (ASUS Laptop)"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-on-asus-laptop
date: 2026-09-15
categories: ["windows-errors"]
tags: ["restarting screen", "windows 11", "asus", "stuck"]
description: "ASUS laptop hanging on the Windows 11 Restarting screen? Force it safely, then fix Armoury Crate, drivers, or Fast Startup."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-on-asus-laptop.webp"
faqs:
  - q: "Is holding the power button safe when it's stuck?"
    a: "Yes, after waiting 15 minutes. A hung 'Restarting' screen means the system is idle-waiting on a component that will never respond — no data is being written. Hold the power button 5–10 seconds, unplug for 30 seconds, and boot fresh."
  - q: "Why does my ASUS hang on restart but shut down fine?"
    a: "Restart performs a full kernel reload while shutdown (with Fast Startup) hibernates the kernel — different code paths. A driver or service that hangs during the full unload/reload cycle may shut down cleanly. Armoury Crate services and outdated chipset drivers are the usual ASUS-specific suspects."
  - q: "Could Armoury Crate be causing this?"
    a: "Yes — it's a known contributor. Armoury Crate runs several background services (lighting, performance monitoring, device control) that can stall the shutdown handshake on some versions. Updating Armoury Crate or disabling its autostart services is a legitimate early fix."
  - q: "How do I prevent it from happening again?"
    a: "Keep Armoury Crate and MyASUS updated, disable Fast Startup if hangs recur, and don't stack restarts during Windows Updates. The permanent fix is identifying the hanging component via clean-boot bisection and updating or removing it."
---
Your ASUS has been "Restarting" for far too long, and that spinner isn't going to resolve itself. What's happening: Windows asked every driver and service to shut down, one of them hung — often an Armoury Crate background service, a chipset driver that won't unload, or a Windows Update mid-install — and the reboot is waiting indefinitely for a response that's never coming.

ASUS laptops have a recognizable pattern here: Armoury Crate's constellation of background services is the most common hang source, followed by Fast Startup weirdness and stale chipset drivers. MyASUS background tasks — LiveUpdate checks and scheduled diagnostics — occasionally pile on at exactly the wrong moment. This guide gets you unstuck immediately, then walks the permanent fixes in order.

One more thing worth knowing up front: restarts and shutdowns take different code paths in Windows 11, so "shuts down fine but hangs on restart" is a real and common pattern, not a contradiction. It usually means a driver that handles the hybrid-shutdown path okay but chokes on the full unload/reload cycle that restart demands.

## Why this happens

- **Armoury Crate services stalling shutdown.** LightingService, Armoury Crate Service, and related background tasks hanging during the shutdown handshake.
- **Chipset or storage drivers that won't unload.** Outdated drivers failing the shutdown sequence.
- **Fast Startup corruption.** The hybrid boot state wedging the restart cycle.
- **Windows Update mid-install.** Legitimately slow updates versus genuinely wedged ones — the 15-minute rule distinguishes them.
- **MyASUS background tasks.** LiveUpdate checks and system diagnostics running at shutdown time.
- **Hung applications.** Deadlocked processes Windows waits on forever.

## How to fix it

Work through these in order. Fix 1 is the rescue; the rest are the cure.

### Fix 1: Force shutdown and clear the wedged state

End the waiting game properly.

1. Wait 15 minutes if the spinner moves or the drive light blinks — an update may be working.
2. Frozen or unchanged for 15+ minutes? Hold the **power button 5–10 seconds** until it powers off.
3. Unplug the charger and all USB devices. Hold the power button for 15 seconds with everything unplugged to drain residual power.
4. Reconnect the charger only and power on. Let any disk check finish.
5. If it immediately hangs on Restarting again, interrupt boot three times for WinRE and continue from Fix 5.

### Fix 2: Update or quiet Armoury Crate

ASUS's own software is suspect number one.

1. Open **Armoury Crate** and update it fully — several releases fixed shutdown-hang bugs specifically.
2. In **Settings** (the gear icon), review what's set to run at startup; disable lighting effects and monitoring features you don't use.
3. As a test, open **Task Manager** > **Startup apps** and disable all ASUS/Armoury Crate entries, then restart. Clean restart? One of those services was the hang — re-enable one at a time to find it.
4. Keep Armoury Crate updated going forward; the shutdown fixes tend to arrive quietly in routine updates.

### Fix 3: Disable Fast Startup

The universal fix for recurring restart hangs.

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup**, save, restart to test.
3. Also run `powercfg /h off` then `powercfg /h on` in **Terminal (Admin)** to rebuild the hibernation file cleanly if you use hibernation.
4. Two seconds slower booting, infinitely more reliable restarting — a trade worth making.

### Fix 4: Update chipset, BIOS, and drivers via MyASUS

Stale low-level drivers hang the shutdown handshake.

1. **MyASUS** > **Customer Support** > **LiveUpdate** — install **BIOS** (charger plugged in, don't interrupt), **chipset**, **IRST/storage**, and **network** updates.
2. Reboot between major updates.
3. Test with three consecutive restarts. One clean restart might be luck; three is evidence.
4. For Intel wireless/storage gaps, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is a safe supplement.

### Fix 5: Clean-boot bisection

Find the hanging component scientifically.

1. **Win + R** > `msconfig` > **Services** > **Hide all Microsoft services** > **Disable all**.
2. **Task Manager** > **Startup apps** > disable everything. Restart.
3. Hangs gone? Re-enable services in halves, restarting each round, until the hang returns.
4. Typical ASUS-land culprits beyond Armoury Crate: third-party antivirus, backup utilities, peripheral software (mouse/keyboard RGB), VPN clients. Update or remove the offender.

### Fix 6: Repair the update stack

For hangs entangled with Windows Update:

1. In **Terminal (Admin)**:
   `net stop wuauserv`, `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`, `net start bits`
2. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > run **Windows Update**.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` for good measure.
4. Let pending updates complete fully before testing restarts. Microsoft documents the manual reset on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: System Restore safety net

Undo whatever started the hangs, then protect yourself.

1. Search **Create a restore point** > **System Restore** > pick a date before the hangs began.
2. After restore, update Armoury Crate, MyASUS, and drivers manually before Windows Update runs.
3. Create a fresh restore point once stable — the [System Restore guide](/articles/how-to-use-system-restore-on-windows-11/) shows how to keep protection on so the next bad update is a five-minute undo.

### Fix 8: Audit shutdown with Event Viewer

For hangs that strike intermittently, the logs catch what live testing misses.

1. After recovering from a hang, open **Event Viewer** (`eventvwr.msc`) > **Windows Logs** > **System**.
2. Filter for **User32**, event ID **1074**: the shutdown records reveal which process was still holding on when the hang began.
3. Check **Applications and Services Logs** > **Microsoft** > **Windows** > **Diagnostics-Performance** > **Operational** for events **200–300** — shutdown degradation warnings that name the slow component and its wasted milliseconds.
4. Update, disable, or uninstall the named component. The log records every shutdown, so intermittent hangs that dodge clean-boot bisection get caught here.

## Closing

An ASUS stuck on "Restarting" is a shutdown handshake that never completes, and the ASUS-specific playbook is short: quiet Armoury Crate's services, disable Fast Startup, and refresh the chipset stack via MyASUS. The fifteen-minute rule keeps you from forcing shutdowns during legitimate updates, and the clean-boot bisection catches whatever's left. Restarts should take seconds — after this, they will again. Dell machines hang for the same reasons with Dell's services in the frame — the [Dell walkthrough](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop/) mirrors these steps for that brand.
