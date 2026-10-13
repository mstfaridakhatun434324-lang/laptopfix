---
title: "Windows Update Stuck on the Restarting Screen? How to Fix It"
slug: "how-to-fix-windows-update-stuck-on-restarting-reddit"
date: "2026-09-30"
categories: ["windows-update"]
tags: ["windows-update", "stuck-restarting", "windows-11", "boot-loop"]
description: "Windows Update frozen on the Restarting screen for hours? Here's how to tell a slow update from a stuck one, and the exact recovery steps that work."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-reddit.webp"
faqs:
  - q: "How long is too long to wait on the Restarting screen?"
    a: "A large feature update can legitimately spend 30 to 60 minutes on the Restarting screen, especially on a machine with a spinning hard drive. Beyond about two hours with no change in the spinning dots or percentage, it is reasonable to treat the update as stuck. If the drive activity light is completely dark for an extended period, that is another strong sign nothing is progressing."
  - q: "Will force-shutting-down during an update break my laptop?"
    a: "It carries some risk, but Windows 11 is designed to roll back incomplete updates on the next boot. The danger is higher during the offline phase when files are actively being replaced, which is why you should wait a couple of hours first. If the screen has been frozen that long, a forced shutdown followed by automatic rollback is usually the only way forward."
  - q: "Why does my laptop get stuck on Restarting after every update?"
    a: "Recurring stalls usually point to a driver that hangs during the restart handshake, a fast startup setting that conflicts with the update sequence, or a failing storage drive that slows the offline phase to a crawl. Updating chipset and storage drivers, disabling fast startup, and checking drive health with the manufacturer's tool typically break the pattern."
  - q: "What does 'Undoing changes made to your computer' mean?"
    a: "That message means Windows detected the update could not complete safely and is rolling back to the previous state. Let it finish — interrupting a rollback is riskier than interrupting the update itself. Once you are back on the desktop, check the update history for the error code and troubleshoot that specific failure before retrying."
---

Few things test your patience like a laptop that has shown the same spinning dots on the Restarting screen for two hours. The instinct is to hold the power button immediately, but a little diagnosis first can save you from turning a recoverable stall into a genuine boot problem. The goal is simple: figure out whether the update is merely slow, then either wait it out or intervene safely.

This situation comes up constantly in community troubleshooting threads because the line between "slow" and "stuck" is genuinely blurry. The steps below follow the order a repair technician would use: observe, wait smartly, force a restart only when justified, then repair whatever caused the stall so it does not happen again next month.

## Why this happens

- **Slow offline phase:** Feature updates do heavy file work during restart; on older hard drives or nearly full SSDs, this can take well over an hour.
- **Driver hanging on shutdown:** A misbehaving storage, chipset, or display driver can refuse to release during the restart handshake, freezing the sequence.
- **Fast startup conflict:** The hybrid shutdown feature can clash with the update's restart cycle, leaving the machine in limbo between states.
- **Corrupt update payload:** If the downloaded files were damaged, the offline installer can choke partway through applying them.
- **Peripheral interference:** USB drives, docks, and even some mice have been known to stall the restart sequence on certain firmware.
- **Failing storage:** A drive with bad sectors or degraded health turns the update's file operations from minutes into hours.
- **BIOS or firmware mismatch:** Outdated firmware can mishandle the power transitions the update performs during restart.
- **Interrupted earlier update:** A previous update that was force-stopped can leave the servicing state half-applied, and the next restart trips over it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Observe and wait the smart way

Before touching anything, gather evidence about whether the update is working or frozen.

1. Note the exact screen text and any percentage shown, then check back in 20 minutes for movement.
2. Watch the drive activity light: steady or blinking activity means work is happening; total darkness for an hour suggests a stall.
3. Listen for fan or drive noise, which indicates the system is still processing.
4. Give it a full two hours before concluding it is stuck, unless the screen is completely frozen with no spinning animation.

### Fix 2: Disconnect peripherals

External devices are a surprisingly common cause of restart stalls and take seconds to rule out.

1. Unplug all USB devices except the power adapter: drives, docks, printers, dongles, and hubs.
2. If you use an external monitor, disconnect it and rely on the laptop screen.
3. Remove any SD cards or discs from the laptop.
4. Wait another 20 to 30 minutes to see if the sequence resumes on its own.

### Fix 3: Perform a forced shutdown and let rollback run

When the wait is clearly over, a forced shutdown lets Windows detect the failure and roll back.

1. Press and hold the power button for 10 full seconds until the laptop powers off.
2. Wait 30 seconds, then power it back on.
3. If you see "Undoing changes made to your computer," let it complete without interruption — this can take a while.
4. Once on the desktop, open Settings, Windows Update, Update history, and note the error code for the failed update.

### Fix 4: Boot into Safe Mode and clear the update cache

Safe Mode gives you a stable environment to remove the damaged files that caused the stall.

1. If the machine boots normally, open Settings, System, Recovery, and click Restart now under Advanced startup.
2. Choose Troubleshoot, Advanced options, Startup Settings, then Restart, and press 4 for Safe Mode.
3. In Safe Mode, open an admin Command Prompt and stop the update services with `net stop wuauserv` and `net stop bits`.
4. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
5. Restart the services with `net start wuauserv` and `net start bits`, then reboot normally.
6. If the service itself refuses to cooperate during these repairs, see [fixing the Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-reddit/).

### Fix 5: Disable fast startup

Fast startup is a frequent repeat offender for restart-related update problems.

1. Open Control Panel and go to Power Options, then choose "Choose what the power buttons do."
2. Click "Change settings that are currently unavailable."
3. Uncheck "Turn on fast startup" and save changes.
4. Retry the update and observe whether the restart phase completes cleanly this time.

### Fix 6: Update chipset and storage drivers

Drivers that hang during shutdown are a top cause of recurring stalls, so bring them current.

1. Visit your laptop manufacturer's support page and download the latest chipset and storage drivers for your exact model.
2. Install them and restart the laptop normally before attempting the update again.
3. Alternatively, use the Intel Driver & Support Assistant to detect and install current Intel drivers.
4. After updating, retry Windows Update and watch the restart phase closely.
5. If drivers keep failing through Windows Update itself, our guide on [updates that fail with error 0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-on-laptop/) covers the underlying file-corruption angle.

### Fix 7: Check drive health before the next attempt

A struggling drive turns every update into a gamble, so verify it is healthy.

1. Open an admin Command Prompt and run `chkdsk C: /f /r`, then restart to let the scan run.
2. Check your SSD manufacturer's toolbox, such as Samsung Magician or the equivalent, for drive health and firmware updates.
3. Ensure at least 20 GB of free space on the system drive.
4. If the drive shows warnings or bad sectors, back up your data before retrying any major update.

### Fix 8: Pause updates, then retry cleanly

Sometimes the smartest move is a controlled pause followed by a fresh attempt with everything repaired.

1. In Windows Update settings, pause updates for one week to stop the automatic retry loop.
2. Use that time to complete the driver, firmware, and disk checks above.
3. Unpause, then click Check for updates and let the update download fresh.
4. During the restart phase, leave the laptop plugged in and untouched until it returns to the desktop.

## Closing

A stuck Restarting screen feels alarming, but in most cases the machine is either finishing slow work or waiting for a nudge that a forced shutdown and cache clear will provide. Work through the sequence calmly, fix the underlying cause — usually a driver, fast startup, or a tired drive — and the next update should sail through the restart phase without drama.
