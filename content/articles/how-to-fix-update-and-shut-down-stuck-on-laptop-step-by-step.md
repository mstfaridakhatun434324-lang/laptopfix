---
title: "\"Update and Shut Down\" Stuck on Your Laptop? Step-by-Step Fix"
slug: how-to-fix-update-and-shut-down-stuck-on-laptop-step-by-step
date: 2026-09-21
categories: ["windows-update"]
tags: ["update and shut down", "stuck shutting down", "windows 11", "power button", "step by step"]
description: "Laptop stuck on 'Update and shut down' for hours? Follow this step-by-step guide to diagnose the stall, shut down safely, and prevent it next time."
thumbnail: "/images/thumbs/how-to-fix-update-and-shut-down-stuck-on-laptop-step-by-step.webp"
faqs:
  - q: "How long is too long on the 'Update and shut down' screen?"
    a: "Allow up to two hours on a hard drive and one hour on an SSD before calling it stuck. Large cumulative updates write thousands of files during shutdown, and the screen offers almost no progress feedback. If the disk activity light is blinking or you hear drive noise, it is still working. Silence and a frozen screen for the full window means a genuine stall."
  - q: "Is it safe to hold the power button when an update is shutting down?"
    a: "Yes, but only after the full wait window with zero activity. During the early shutdown phase Windows is still writing files, and cutting power then can corrupt the update. After hours of verified inactivity, hold the power button for ten seconds. Windows keeps the update pending and will usually complete it on the next boot, or roll it back safely."
  - q: "Why does the update run again after I forced the shutdown?"
    a: "Windows marks the update as pending rather than finished, so the next boot or shutdown resumes the installation attempt. This is normal and usually fine. If the update then fails and rolls back, the cause is the original failure — corrupted cache, driver conflict, or low disk space — not the forced shutdown, so address that before trying again."
  - q: "Can I shut down without installing updates to avoid this?"
    a: "Yes. In Settings > Windows Update you can pause updates for up to five weeks, which removes the update options from the power menu. Alternatively, use the classic shutdown via Alt+F4 on the desktop, which offers the plain Shut down option. Keep in mind that deferring security updates indefinitely is not advisable; use the pause to schedule a convenient update time instead."
---

You clicked "Update and shut down," closed the lid expectations behind you, and went to bed. Hours later the laptop is still warm, the screen still shows the spinning dots, and nothing has changed. The update-shutdown sequence is supposed to take minutes; when it stretches into hours, something in the shutdown pipeline has stalled.
This scenario is distinct from the better-known "undoing changes" rollback. Here the update is usually still trying to install, not reversing. Windows applies part of the update while the system is still running, then finishes the rest during shutdown — and it is that second phase that freezes. The usual suspects are corrupted update files, a driver that refuses to release, or a service that will not stop, all while the screen tells you nothing useful.
Work through this guide in order: verify the stall, shut down safely, diagnose the cause, fix it, and retry the update properly. If the machine instead hangs while booting back up, the [stuck-on-restarting fix](/articles/windows-11-stuck-on-restarting-screen-fix/) covers that side of the story, and Dell owners can check the [Dell restarting-screen guide](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop/) for brand-specific steps.

## Why this happens

- **The update is genuinely still installing.** Cumulative updates apply thousands of file operations during shutdown; on slower drives this legitimately takes over an hour.
- **A service refuses to stop.** Windows cannot complete the shutdown phase until every service releases, and one hung service stalls the whole pipeline.
- **The update files are corrupted.** Damaged downloads in the SoftwareDistribution cache make the installer retry operations that never succeed.
- **A driver blocks the shutdown.** Storage or network drivers that mishandle power transitions hold the shutdown phase open.
- **Fast Startup interferes.** The hybrid shutdown state can conflict with the update's shutdown phase, leaving the machine in limbo.
- **Disk space is too low.** The installer needs working room for staging files during shutdown.
- **A background app holds a lock.** An application with unsaved state or a locked file can prevent the update phase from completing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall before touching anything

Patience first. The shutdown-phase install gives almost no progress feedback, so most "stuck" cases here are actually just slow — cutting power early is the main way this turns into a real problem.

1. Note the time, then wait one full hour on an SSD or two hours on a mechanical drive.
2. Watch the disk activity light: blinking means installation is progressing, so keep waiting.
3. Check for fan noise or warmth from the vents — sustained activity is a good sign.
4. Proceed only after the full window with zero light activity, zero noise, and an unchanged screen.

### Fix 2: Force the shutdown safely

After a verified stall, the machine will not finish on its own. A forced shutdown at this point is safe because Windows marks the update as pending and resumes it on the next boot.

1. Hold the power button for 10 seconds until the laptop powers off fully.
2. Unplug all USB devices, docks, and external monitors to eliminate peripheral hangs on the next boot.
3. Wait 30 seconds for capacitors to discharge, then press the power button to start the laptop.
4. Let it boot normally — Windows will either complete the update or roll it back and reach the desktop.

### Fix 3: Check what actually happened after booting

The boot after a forced shutdown tells you a lot. Read the signs before doing anything else.

1. If Windows boots to the desktop, open Settings > Windows Update > Update history and see whether the update shows as installed, failed, or pending.
2. If the machine shows "Undoing changes," let it finish — then you are dealing with a failed update, not a stuck shutdown.
3. If it boots into Automatic Repair, let it run; it repairs boot files damaged by the interruption.
4. Note any error code shown in the update history for the next steps.

### Fix 4: Disable Fast Startup

Fast Startup's hybrid shutdown is a documented source of update-shutdown hangs. Disabling it gives updates a clean, full shutdown to work with.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click "Change settings that are currently unavailable" to unlock the options.
3. Uncheck "Turn on fast startup (recommended)" and click Save changes.
4. Restart the laptop once so the change takes effect before the next update attempt.

### Fix 5: Reset the update cache

Corrupted downloads stall the shutdown-phase installer in a retry loop. Clearing the cache forces a fresh download.

1. Open an elevated Command Prompt and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Reboot normally, then check for updates to pull a fresh copy.

### Fix 6: Identify the hanging driver or service

If the shutdown phase keeps stalling, a driver or service is likely holding it open. Find the culprit with the event logs.

1. After a successful boot, open Event Viewer and check Windows Logs > System for errors around the time of the failed shutdown.
2. Look for entries from Service Control Manager naming a service that failed to stop within the timeout.
3. Update that service's driver from the manufacturer's site — [Dell owners should check](https://www.dell.com/support) for the latest storage and chipset drivers.
4. Also review the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) on shutdown hangs for the current known issues.

### Fix 7: Retry the update on your terms

Do not let the next attempt happen accidentally at midnight. Run it deliberately, on AC power, with conditions you control.

1. Connect to AC power and a stable network; pause any metered-connection limits.
2. Temporarily disable third-party antivirus real-time protection during the attempt.
3. Install the update via Settings > Windows Update while you can watch it, rather than through "Update and shut down."
4. If it fails again with a specific code, look it up before retrying blindly.

## Closing

The "Update and shut down" hang is almost always a stalled install phase rather than a broken machine. Verify the stall, shut down safely, disable Fast Startup, clean the cache, and retry deliberately. Once you stop the machine from entering that limbo state, the update either installs cleanly or fails with an honest error code you can actually fix.
