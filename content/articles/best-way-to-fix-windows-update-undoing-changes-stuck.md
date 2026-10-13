---
title: "Best Way to Fix Windows Update Stuck on Undoing Changes"
slug: best-way-to-fix-windows-update-undoing-changes-stuck
date: 2026-09-30
categories: ["windows-update"]
tags: ["undoing changes stuck", "we couldn t complete the updates", "update rollback stuck", "windows update failed reverting"]
description: "Stuck on Undoing changes made to your computer? The rollback is wedged. Here's the safest way to unstick it and update successfully."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-undoing-changes-stuck.webp"
faqs:
  - q: "What does Undoing changes made to your computer mean?"
    a: "It means an update failed to install and Windows is rolling back to the previous state. The message itself is normal and healthy; it only becomes a problem when the rollback itself gets stuck and the screen never progresses to the desktop."
  - q: "How long can Undoing changes legitimately take?"
    a: "On a healthy system, minutes to about an hour. Large feature-update rollbacks on slow drives can take longer. If the spinner is animating and the drive is active, let it work for up to two hours before intervening. Interrupting real progress is the one mistake that makes everything worse."
  - q: "Will I lose files during the undoing changes rollback?"
    a: "No. The rollback reverses the update's system changes only. Your personal files are not touched by the rollback process, though having a backup is always wise before major updates are installed. A backup turns every recovery step below into a stress-free operation."
  - q: "Why did the update fail in the first place?"
    a: "The usual causes are driver conflicts, insufficient disk space, corrupt download payloads, and third-party software interfering with the install. Fixing the underlying cause matters as much as escaping the stuck screen, or the next attempt fails the same way."
---

The message We couldn't complete the updates, undoing changes is Windows doing the responsible thing: an update failed, and the system is rolling itself back to the last known good state. It is one of the better-designed safety nets in Windows — until the safety net itself gets stuck.

A stuck rollback usually means the reversal hit something it cannot undo cleanly: a driver that will not revert, a servicing transaction that will not close, or a disk so full the rollback cannot stage its work. The screen sits, the spinner turns, and the machine never reaches the desktop.

Getting out requires respecting the rollback's intent while giving it an escape hatch. The steps below move from patient waiting through the recovery environment to the underlying fix that stops the failure from repeating.

The undoing-changes screen is Windows keeping a promise: if an update fails, you get your old system back. A stuck promise is still better than a broken system, but it needs help. The sequence below respects the rollback's work — never interrupting real progress — while giving you the tools to escape when the work has genuinely stopped.

## Why this happens

- **Driver that will not roll back.** A driver the update replaced cannot be restored, stalling the reversal.

- **Stuck servicing transaction.** The servicing stack cannot close the failed transaction cleanly.

- **Insufficient disk space.** The rollback needs working room to restore previous files; a full drive starves it.

- **Corrupt rollback data.** Damaged backup copies of the pre-update state cannot be restored.

- **Third-party software interference.** Antivirus or utilities blocking the rollback's file operations.

- **Disk errors.** Bad sectors in the areas holding rollback data halt the restore.

- **Interrupted original install.** A violently interrupted update leaves state the rollback logic cannot parse.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Wait, genuinely wait

Rollbacks do real work: restoring thousands of files takes time, and interrupting it is the one thing that can turn a recoverable situation into an unbootable one. Patience is the fix more often than people believe. Large rollbacks write gigabytes back to the disk; on an older hard drive the throughput alone accounts for most of the wait, not any malfunction.

1. Allow up to two hours if the spinner is animating or the drive light is active.
2. Do not force-shutdown while there is any sign of activity.
3. Only move to the next fix when the screen is fully frozen with no activity for over an hour.

### Fix 2: Fix 2: Force shutdown into the Recovery Environment

When the rollback is truly dead, break the loop by forcing WinRE. Two interrupted boots trigger Automatic Repair, giving you tools the stuck screen does not. The two-interrupted-boots method works because Windows counts failed starts; after two, it assumes you need help and offers the recovery environment.

1. Hold the power button 10 seconds to force off.
2. Power on, and force off again as soon as the manufacturer's logo appears. Repeat once more.
3. On the third boot, Windows enters the Recovery Environment automatically.

### Fix 3: Fix 3: Uninstall the latest quality update

WinRE lets you surgically remove the update that triggered the whole mess. Without the failed update present, the system boots normally. Quality updates versus feature updates matter here; removing the quality update is quick, while a stuck feature-update rollback may need the feature update removed instead.

1. In WinRE, choose Troubleshoot, then Advanced options, then Uninstall Updates.
2. Choose Uninstall latest quality update and let it complete.
3. Select Continue to boot Windows normally.

### Fix 4: Fix 4: Run Startup Repair

If the boot is damaged beyond the bad update, Startup Repair fixes boot files and the boot configuration. Startup Repair is safe to run even when you are unsure it is needed; at worst it finds nothing and you move on.

1. In WinRE, go to Troubleshoot, then Advanced options, then Startup Repair.
2. Let the repair run to completion.
3. Reboot and check that Windows loads.

### Fix 5: Fix 5: Boot Safe Mode and clear the cache

Safe Mode's minimal drivers sidestep whatever hung the rollback. From there, clearing the update cache removes the failed payload so it cannot trigger another rollback. Safe Mode with Networking is unnecessary for cache clearing; plain Safe Mode loads fewer drivers and is the safer choice for this operation.

1. In WinRE, go to Troubleshoot, Advanced options, Startup Settings, and boot into Safe Mode.
2. In an admin Terminal, run `net stop wuauserv` and `net stop bits`, then delete everything in C:\Windows\SoftwareDistribution\Download.
3. Restart the services, reboot normally, and pause updates for a week.

### Fix 6: Fix 6: Free up disk space from WinRE

A rollback starved of disk space cannot finish. WinRE's command prompt lets you delete the obvious space hogs without booting Windows. From the WinRE command prompt, the C: drive may appear as D:; verify with dir before deleting anything so you target the right volume.

1. In WinRE, open Troubleshoot, then Advanced options, then Command Prompt.
2. Delete temp files and clear the Recycle Bin contents from the command line, and remove any giant files you recognize as disposable.
3. Exit, continue to Windows, and confirm at least 15 to 20 GB free on C:.

### Fix 7: Fix 7: Fix the underlying cause before retrying

Escaping the stuck screen is only half the job. Before allowing the update again, address why it failed: update drivers, run DISM and SFC, and ensure free space. Driver updates should come from the manufacturer rather than Windows Update for this validation pass; you want known-good drivers, not the ones that just failed.

1. Update chipset, storage, and graphics drivers from the manufacturer.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` in an admin Terminal.
3. Then retry the update. For the diagnostic deep-dive version of this problem, see our [undoing-changes troubleshooting guide](/articles/windows-update-undoing-changes-stuck-troubleshooting/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the recovery environment.

## Closing

A stuck Undoing changes screen is a wedged safety net: the rollback is the right idea executed badly. Wait it out if there is activity, escape through WinRE if there is not, and always fix the underlying driver, space, or corruption cause before the update tries again. For the full diagnostic approach, read our [undoing-changes troubleshooting guide](/articles/windows-update-undoing-changes-stuck-troubleshooting/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the official recovery tools. If the screen specifically says "Undoing changes made to your computer," the [undoing-changes message fix](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-in-windows/) walks through that exact failure.
