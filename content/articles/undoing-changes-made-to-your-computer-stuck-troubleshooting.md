---
title: "Stuck on Undoing Changes Made to Your Computer? A Troubleshooting Walkthrough"
slug: undoing-changes-made-to-your-computer-stuck-troubleshooting
date: 2026-09-04
categories: ["windows-update"]
tags: ["undoing changes", "stuck", "windows 11", "troubleshooting"]
description: "Is 'Undoing changes made to your computer' frozen for hours? Learn how to tell a slow rollback from a stuck one and the safe steps to recover your laptop."
thumbnail: "/images/thumbs/undoing-changes-made-to-your-computer-stuck-troubleshooting.webp"
faqs:
  - q: "How do I know if the undoing changes screen is actually stuck?"
    a: "Watch for signs of life over about two hours. A healthy rollback shows disk activity — the drive light flickers, the fan may spin, and occasionally the progress indicator moves. A truly stuck screen shows zero change for two-plus hours with no disk or fan activity. Laptops with mechanical hard drives legitimately take longer than SSDs, so factor that in."
  - q: "Is it safe to force shut down during undoing changes?"
    a: "It is risky but sometimes unavoidable. Microsoft warns against interrupting a rollback because it can leave the system in an inconsistent state. If you must, hold the power button for a full shutdown, wait thirty seconds, and power on — Windows will usually resume the rollback or fall back to automatic repair. Never pull the battery or cut power mid-write if you can avoid it."
  - q: "What causes the rollback itself to freeze?"
    a: "The most common causes are a failing storage drive that stalls on bad sectors, a corrupted rollback checkpoint, a driver that refuses to unload during the revert, or a power dip on a laptop with a dying battery. The rollback is doing real disk work, so anything that stalls disk I/O stalls the rollback with it."
  - q: "Will automatic repair fix a stuck undoing changes loop?"
    a: "Sometimes. Automatic repair can rebuild the boot configuration and clear a stuck update state, which is enough when the problem is a damaged boot entry rather than deep corruption. If automatic repair also stalls or loops, the next step is a repair install from Windows installation media, which preserves your files."
---

"Undoing changes made to your computer" is supposed to be a temporary screen — a rollback that runs its course and hands you back a working laptop. When it sits there for hours with no movement, the protective mechanism itself has stalled, and you need a different approach than just waiting longer.

The first decision matters most: is the rollback genuinely stuck, or just slow? Interrupting a slow rollback is the one thing that can convert a recoverable situation into real damage. The walkthrough below starts with that assessment, then moves through forced-recovery options in escalating order. Once you are back at the desktop, the loop itself needs fixing — see our guide to [Windows update rollback loops](/articles/how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2/) for the follow-up.

## Why this happens

- **Failing storage drive:** Bad sectors encountered during the rollback's heavy disk writes stall the entire process.
- **Corrupted rollback checkpoint:** The snapshot Windows is reverting to was damaged, so the revert cannot complete cleanly.
- **Driver refusing to unload:** A misbehaving driver blocks the revert sequence, freezing the rollback mid-step.
- **Low battery power dip:** On laptops, a dying battery causing voltage sag during hours of disk activity can freeze the process.
- **Stuck update service state:** The update engine's internal state is inconsistent, and the rollback waits on a signal that never arrives.
- **Antivirus filter conflict:** A security driver filtering disk writes collides with the rollback's file operations.
- **Interrupted earlier rollback:** A previous forced shutdown left a half-completed revert that the current one cannot reconcile.
- **Insufficient disk space for the revert:** The rollback needs working space too, and a nearly full drive stalls it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is actually stuck

Do not act on a rollback that is merely slow.

1. Note the exact time and watch the screen for at least one full hour more.
2. Look for the disk activity light — flickering means real work is happening.
3. Listen for fan noise and disk sounds indicating ongoing activity.
4. If there is any activity at all, give it another hour; large rollbacks on hard drives can take three to four hours.
5. Only proceed to forced recovery if there has been zero activity for two hours or more.

### Fix 2: Perform a controlled forced shutdown

When the rollback is confirmed dead, a careful power cycle is the way out. (If your screen is stuck on a restarting loop rather than the rollback message, the [restart-stuck guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) covers that variant.)

1. Hold the power button for ten seconds until the laptop fully powers off.
2. Unplug the charger and, if the battery is removable, remove it for thirty seconds.
3. Reconnect power and turn the laptop on.
4. Windows will usually resume the rollback — let it try, giving it another full hour.
5. If it resumes and finishes, you are done; if it freezes again at the same point, continue.

### Fix 3: Boot into Windows Recovery Environment

WinRE gives you repair tools outside the stuck rollback.

1. Force the laptop off twice during the Windows logo (hold power button) — the third boot should enter automatic repair.
2. If that fails, boot from Windows installation media and choose **Repair your computer**.
3. In the recovery menu, choose **Troubleshoot**.
4. First try **Startup Repair** — it can fix boot issues masquerading as a stuck rollback.
5. If Startup Repair completes, restart normally and observe.

### Fix 4: Use System Restore from WinRE

Roll back to a restore point from before the update, sidestepping the stuck revert.

1. In WinRE, go to **Troubleshoot > Advanced options > System Restore**.
2. Pick a restore point dated before the problematic update.
3. Let the restore run — this can take thirty minutes or more.
4. When it finishes, the laptop should boot to the desktop.
5. Immediately pause Windows updates for a week while you investigate the cause.

### Fix 5: Clear the update state from the command line

If System Restore is unavailable, clear the stuck update state manually via the recovery command prompt.

1. In WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Identify your Windows drive letter — in WinRE it may be D: or E:, not C:. Check with `dir D:\Windows`.
3. Rename the update cache: `ren D:\Windows\SoftwareDistribution SoftwareDistribution.old` (use the correct letter).
4. Run `chkdsk D: /f` (correct letter) to fix file system errors that may be stalling disk I/O.
5. Exit, choose **Continue** to boot Windows, and give it time.

### Fix 6: Run a repair install from installation media

This reinstalls Windows over itself while keeping your files and most apps — the definitive fix for deep corruption.

1. Create Windows installation media on another computer using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Boot the stuck laptop from the USB drive.
3. Choose your language, then click **Install now** — not Repair.
4. When prompted, choose **Keep personal files and apps**.
5. Let the install complete; the stuck rollback state is replaced by a clean system.

### Fix 7: Check the drive health

If rollbacks keep stalling, the drive itself may be failing. Forcing repeated rollbacks on a dying drive risks data loss.

1. Once booted (by any means above), back up your important files immediately.
2. Open Command Prompt as administrator and run `wmic diskdrive get status`.
3. Check the drive's SMART data with the manufacturer's tool (available via [Windows support guidance](https://support.microsoft.com/en-us/windows)) if you suspect failure.
4. If the drive reports anything other than OK, replace it before attempting further updates.
5. A fresh drive with a clean Windows install ends the rollback problem permanently.

## Closing

A stuck "undoing changes" screen demands patience first and decisive action second. Confirm the stall, power-cycle carefully, and work the recovery environment tools in order — most users recover through System Restore or the command-line cache clear without losing a single file. The one thing to avoid is repeated forced shutdowns on a hunch; each one risks making the half-rolled-back state worse. If you needed Fix 6 or 7, check your drive health before the next update cycle, because recurring stalls are the classic early symptom of a failing drive.
