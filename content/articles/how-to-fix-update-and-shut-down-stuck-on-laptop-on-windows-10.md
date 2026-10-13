---
title: "How to Fix 'Update and Shut Down' Stuck on a Windows 10 Laptop"
slug: "how-to-fix-update-and-shut-down-stuck-on-laptop-on-windows-10"
date: 2026-09-23
categories: ["windows-update"]
tags: ["update and shut down", "windows update stuck", "windows 10", "fast startup", "shutdown stuck"]
description: "Windows 10 laptop stuck on 'Update and shut down'? Disable Fast Startup, clear the pending update state, and use the restart path that actually finalizes updates."
thumbnail: "/images/thumbs/how-to-fix-update-and-shut-down-stuck-on-laptop-on-windows-10.webp"
faqs:
  - q: "Does Windows 10 have the same Fast Startup problem as Windows 11?"
    a: "Yes — Fast Startup debuted in Windows 8 and is enabled by default in Windows 10 too, so the identical hybrid-shutdown conflict affects 'Update and shut down' on Windows 10. The setting lives in the same place (Power Options > Choose what the power buttons do), and disabling it is the same permanent fix. Windows 10 machines are also more likely to have older, slower drives that stretch the hang from minutes into hours."
  - q: "How long should I wait before forcing a shutdown on Windows 10?"
    a: "Wait 30-45 minutes. Windows 10's update finalization on a mechanical hard drive can legitimately take that long, and the shutdown screen gives no progress details. If the spinner is still moving and the drive light flickers, it is working — slowly. Only force the shutdown when the screen is frozen with no drive activity for an extended period."
  - q: "Will forcing a shutdown corrupt my Windows 10 installation?"
    a: "Almost certainly not at this stage. By the time you see the 'shutting down' screen during 'Update and shut down,' the update's file operations are complete — what is hanging is the power-off step itself. Windows 10 verifies system integrity on the next boot and resumes or rolls back cleanly. The dangerous moment to force-shutdown is during the blue 'Working on updates' phase, not the shutdown phase."
  - q: "Why does 'Update and restart' work when 'Update and shut down' hangs?"
    a: "A restart is a full kernel cycle: everything unloads, the machine reboots, and pending update operations finalize during startup. A Fast Startup shutdown saves the kernel state to disk instead of truly shutting down, so operations that require a genuine boot-from-off never trigger. 'Update and restart' gives the update the full cycle it was designed around."
---
Windows 10's 'Update and shut down' hangs for the same reason it does on Windows 11 — Fast Startup's hybrid shutdown — but Windows 10 adds its own wrinkles: older hardware, more mechanical hard drives, and an update engine that shows even less information on the shutdown screen. The result is the familiar scene: a laptop that was supposed to power off an hour ago, still glowing, still spinning.

The mechanics are worth understanding because they dictate the fix. 'Update and shut down' installs the update, then attempts a shutdown. With Fast Startup on, that shutdown hibernates the kernel instead of fully powering off. Updates that need a true boot cycle to finalize their last steps never get it, and the machine waits on a condition that will never arrive. The screen spins; nothing progresses.

This guide follows the Windows 10 menus and includes the Windows 10-specific recovery paths. Fix 1 rescues the machine tonight; Fix 2 prevents recurrence. If you are on Windows 11, the equivalent steps are in our [Windows 11 'Update and shut down' guide](/articles/how-to-fix-update-and-shut-down-stuck-on-laptop-on-windows-11/).

## Why this happens

- **Fast Startup hybrid shutdown** — Enabled by default since Windows 8, it hibernates the kernel on 'shutdown.' Updates requiring a genuine cold boot never get one.

- **Update designed for the restart path** — Many updates finalize only across a restart; the shutdown path cannot satisfy them and stalls.

- **Slow mechanical hard drive** — Common in Windows 10-era laptops, HDDs stretch finalization from minutes to hours, mimicking a hang.

- **Driver blocking the shutdown sequence** — Aging audio, network, or chipset drivers that will not unload hold the entire shutdown hostage.

- **Corrupted pending.xml** — A damaged pending-operations file makes finalization fail silently behind the spinning screen.

- **Lid closed mid-process** — Sleep triggering instead of shutdown freezes the update in a half-powered limbo.

- **Insufficient disk space** — Finalization needs scratch space; a full drive stalls the file shuffling indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait, then force the shutdown safely

Rescue the machine first. The update work is done by the time the shutdown screen hangs — you are only interrupting the power-off step.

1. Wait 30-45 minutes (longer on HDDs) to rule out slow-but-working finalization.
2. Hold the power button for 10 seconds until fully off.
3. Wait 30 seconds, then boot normally without interrupting.
4. Verify in **Settings > Update & Security > Windows Update > View update history** whether the update completed.

### Fix 2: Disable Fast Startup permanently

The root-cause fix on Windows 10, identical in effect to Windows 11: real shutdowns every time. Note that shutdowns take a few seconds longer without Fast Startup — a small price for reliability, and restarts are unaffected.

1. Open Control Panel > **Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.
4. Perform one full shutdown (not restart) to flush the hibernation state.

### Fix 3: Prefer 'Update and restart' going forward

Build the habit that avoids the problem class entirely. If you must power the machine off after updating, do it from the desktop once the restart completes — the system is then clean, updated, and shuts down quickly.

1. Choose **Update and restart** whenever updates are pending.
2. Let the machine reboot fully to the login screen.
3. Confirm the update in **View update history**.
4. Shut down normally afterward if you want the laptop off — from a clean, updated state.

### Fix 4: Clear the pending update state

A corrupted pending state causes repeat hangs. Purge it so the next shutdown starts clean. A damaged pending.xml is also behind machines that show 'working on updates' for hours — clearing it fixes both symptoms at once.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`.
3. Empty **C:\Windows\SoftwareDistribution\Download**.
4. Run `net start wuauserv` and `net start bits`, then use **Update and restart** for pending updates. For retry loops after this, see [cumulative updates failing to install](/articles/how-to-fix-cumulative-update-fails-to-install-after-windows-11-update/).

### Fix 5: Identify the driver holding up shutdown

Enable verbose status messages to see exactly what the shutdown sticks on. If no single driver stands out, update the chipset and storage drivers first — they are the most common shutdown-hangers on aging Windows 10 laptops.

1. Press **Win + R**, type `regedit`, go to `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`.
2. Create DWORD **VerboseStatus** set to 1.
3. Shut down and note which service or driver the screen names when it sticks.
4. Update that driver from the manufacturer's support site. Microsoft's driver guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Free disk space before updating

Windows 10 laptops with small drives hit space-related finalization stalls often. Give the update room.

1. Open **Settings > System > Storage** and run **Storage Sense** plus **Free up space now**.
2. Target at least 20 GB free on C: before installing updates.
3. Move personal files off the system drive permanently if space is chronically tight.
4. Retry the update via the restart path with space available.

### Fix 7: Check drive health with CHKDSK

On aging Windows 10 hardware, the drive itself is a legitimate suspect for multi-hour finalizations. This check is worth running annually on old machines — drives usually decline gradually, and CHKDSK catches the decline early.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r`.
2. Schedule with **Y** and restart to run the full surface scan.
3. Let it complete — on large HDDs this takes a while.
4. If bad sectors are found, back up and plan a drive replacement; an SSD upgrade transforms these old machines.

## Closing

Windows 10's stuck 'Update and shut down' is the Fast Startup trap wearing an older operating system's clothes. Disable Fast Startup, use the restart path for updates, and keep the drive healthy — the hang stops happening.
