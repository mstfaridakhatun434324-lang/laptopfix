---
title: "Windows Update Stuck on Restarting on Windows 10: Unsticking It"
slug: how-to-fix-windows-update-stuck-on-restarting-on-windows-10
date: 2026-09-11
categories: ["windows-update"]
tags: ["stuck on restarting", "windows 10", "update stuck", "reboot loop"]
description: "Windows 10 update stuck on the restarting screen? Learn how to tell a slow install from a frozen one and the safe steps to get your laptop booting again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-on-windows-10.webp"
faqs:
  - q: "How long is too long for the restarting screen?"
    a: "On an SSD, most update restarts finish within thirty minutes. On a mechanical hard drive, allow up to two hours. If the spinner has been going for over two hours with no disk activity — no drive light, no fan changes — the restart is genuinely stuck. Patience first: interrupting a working install is worse than waiting an extra hour."
  - q: "Will forcing a shutdown during the restart damage Windows?"
    a: "It can, but usually does not. Windows is designed to recover from interrupted updates via automatic rollback. The risk is real but small — the bigger risk is repeated forced shutdowns, which compound partial states. One careful power cycle after confirming the stall is the accepted recovery step."
  - q: "Why does this happen on Windows 10 specifically?"
    a: "Windows 10's update engine applies changes across the restart boundary, and driver handoffs during that window are fragile. Old drivers, antivirus filter drivers, and failing disks stall the handoff. Windows 11 reworked parts of this pipeline, which is why the symptom is more common on Windows 10 machines."
  - q: "Should I disable automatic updates after this?"
    a: "No — pausing briefly while you fix the underlying cause is fine, but disabling updates permanently trades a recoverable annoyance for unpatched security vulnerabilities. Fix the driver or disk issue that caused the stall, and updates will restart normally without drama."
---

The "Restarting" screen with its endless spinner is one of Windows 10's most stressful sights. The update was installing, the laptop rebooted as expected, and then... nothing. Minutes become an hour, the dots keep circling, and you start wondering whether the machine will ever come back.

In most cases it will — either by finishing on its own or with a careful nudge. The critical skill is distinguishing a slow install from a frozen one, because the recovery steps differ completely. This guide starts with that assessment, then walks through the recovery ladder from a safe power cycle up to the deeper repairs. If your screen specifically shows the [restarting screen variant with no progress](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-windows-10/), the same principles apply, with screen-specific notes there.

## Why this happens

- **Driver handoff stall:** A driver fails to unload or reload across the restart boundary, freezing the boot sequence.
- **Antivirus filter conflict:** Security drivers intercept the restart's file operations and deadlock.
- **Failing storage drive:** Bad sectors hit during the restart's heavy disk writes stall the process.
- **Corrupted update state:** A half-applied update leaves the boot configuration in limbo.
- **Peripheral interference:** A connected USB device's driver blocks the restart sequence.
- **Low-level disk errors:** File system corruption that the running OS tolerated becomes fatal during the offline phase.
- **Insufficient power:** On laptops, a dying battery causing a brownout mid-restart corrupts the in-flight update.
- **BIOS handoff issues:** Firmware that misbehaves during the warm reboot stalls before Windows even loads.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait and verify it is actually stuck

Most "stuck" restarts are just slow — especially on hard drives.

1. Note the time and give it a full additional hour if you have not already waited two.
2. Watch the disk activity light: flickering means the install is still working.
3. Listen for fan and disk sounds indicating ongoing activity.
4. If there is any sign of life, keep waiting — some Windows 10 updates take three hours on mechanical drives.
5. Only proceed when there has been zero activity for over an hour.

### Fix 2: Perform a controlled power cycle

Once the stall is confirmed, a careful shutdown is the standard recovery. Microsoft covers interrupted-update recovery on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Hold the power button for ten seconds until the laptop powers off completely.
2. Unplug the charger and remove the battery for thirty seconds if it is removable.
3. Reconnect power and turn the laptop on.
4. Windows will typically resume the update, roll it back, or boot to the desktop — give it up to an hour.
5. If it boots normally, immediately check update history to see what happened.

### Fix 3: Boot into Safe Mode and clear the state

If normal boot stalls again, Safe Mode bypasses the problematic drivers. Our [Windows 11 safe-mode update guide](/articles/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update/) describes the same technique on the newer OS.

1. Force the laptop off twice during the Windows logo to trigger automatic repair.
2. Go to **Troubleshoot > Advanced options > Startup Settings** and choose Safe Mode.
3. Once in Safe Mode, open Command Prompt as administrator.
4. Run `net stop wuauserv` and `net stop bits`, then rename the SoftwareDistribution folder as described in Fix 4.
5. Restart normally — the update will re-download cleanly.

### Fix 4: Clear the update cache from recovery

When you cannot reach the desktop at all, clear the cache from the recovery command prompt.

1. Boot into the Windows Recovery Environment (installation media > **Repair your computer** if needed).
2. Open **Troubleshoot > Advanced options > Command Prompt**.
3. Find your Windows drive letter — in WinRE it is often D:, so verify with `dir D:\Windows`.
4. Run `ren D:\Windows\SoftwareDistribution SoftwareDistribution.old` with the correct letter.
5. Exit and choose **Continue** to boot Windows normally.

### Fix 5: Run Startup Repair

Automatic repair fixes boot configuration damage from the interrupted update.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Let it run — it diagnoses and repairs boot issues automatically.
3. If it reports it could not repair, note the log location and continue to Fix 6.
4. If it succeeds, restart and observe whether the update completes.
5. Check update history once booted.

### Fix 6: System Restore to before the update

Roll the system back to a known-good point, sidestepping the stuck state entirely.

1. In WinRE, go to **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point dated before the problematic update.
3. Let the restore complete — allow thirty minutes or more.
4. Boot to the desktop and pause updates for a week.
5. Use the pause to update drivers before retrying.

### Fix 7: Check the drive and update drivers

Recurring restart stalls point at hardware or driver rot — fix the root cause before the next update.

1. Back up your files once you can boot.
2. Run `chkdsk C: /f` from an elevated Command Prompt and let it complete.
3. Update storage, display, and chipset drivers from the manufacturer's site.
4. Uninstall third-party antivirus temporarily before the next update attempt.
5. Retry the update with the charger connected and peripherals disconnected.

### Fix 8: Disable fast startup

Fast startup's hybrid shutdown can trap a half-finished update state across reboots, making the stall recur.

1. Open Control Panel and go to **Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup**.
4. Shut down fully (not restart) and power on fresh.
5. Retry the update with fast startup off — re-enable it later if you prefer it.

## Closing

A Windows 10 update stuck on "Restarting" is frightening but almost always recoverable: wait long enough to be sure, power-cycle once, and use the recovery environment if needed. The pattern behind repeat stalls is consistent — aging drivers, aggressive antivirus, or a tired drive — and addressing it between updates keeps the spinner from ever overstaying its welcome again. The update will finish; the laptop is not bricked; work the ladder calmly.
