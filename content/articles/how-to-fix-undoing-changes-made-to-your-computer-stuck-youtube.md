---
title: "\"Undoing Changes Made to Your Computer\" Stuck Forever? Fix It"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-youtube
date: 2026-09-04
categories: ["windows-update"]
tags: ["undoing changes stuck", "rollback frozen", "recovery", "boot loop", "windows update"]
description: "The 'Undoing changes made to your computer' screen has been stuck for hours. Here's how to tell if it's frozen and how to recover your laptop."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-youtube.webp"
faqs:
  - q: "How long can 'undoing changes' legitimately take?"
    a: "A cumulative-update rollback usually takes 15 to 45 minutes; a feature-update rollback can take one to two hours, longer on slow drives. Animated dots and periodic disk activity mean it's working. The screen is only 'stuck' when there's zero animation change and zero disk activity for over two hours — everything short of that is normal rollback slowness."
  - q: "Is it safe to force shutdown during a stuck rollback?"
    a: "It's the last resort, not the first move — but yes, when the rollback is genuinely frozen (two hours, no activity), a single force shutdown is the correct next step. Windows is designed to resume or restart the rollback on the next boot. The danger is in interrupting a working rollback, which is why the two-hour verification rule in this guide matters."
  - q: "Will I lose personal files if the rollback is interrupted?"
    a: "Your personal files are not part of what the rollback modifies — it restores system files only. Even an interrupted rollback doesn't target your documents. In the worst case, you may need the Recovery Environment to finish the rollback or uninstall the update, but your files remain intact on the drive through all of it."
  - q: "Why did the rollback get stuck in the first place?"
    a: "Usually the same reason the update failed: a driver hanging during restore, disk errors slowing file operations to a crawl, or corrupted servicing data the rollback can't process. That's why this guide pairs recovery with root-cause fixes — recovering without fixing the cause just sets up the next failed update and the next stuck rollback."
---

"Undoing changes made to your computer" is supposed to be a temporary screen — Windows reversing a failed update, usually done within the hour. But sometimes the temporary screen becomes permanent: hours pass, the dots spin (or don't), and your laptop is held hostage by its own safety net.

A stuck rollback is unnerving because the usual advice — "don't turn off your computer" — is still on screen, now feeling like a taunt. Here is the framework: verify the freeze with a strict rule, recover with the safest method available, then fix whatever made both the update and its rollback fail.

Work through these in order — diagnose first, then act.

## Why this happens

- **Driver hanging during restore.** The same bad driver that failed the update hangs the rollback.
- **Disk errors.** Bad sectors or filesystem corruption stalling the rollback's file operations.
- **Corrupted servicing data.** Damaged component store the rollback cannot reconcile.
- **Interrupted original update.** A power loss mid-update leaving inconsistent state the rollback struggles with.
- **Insufficient disk space.** The rollback needing working room that the failed update consumed.
- **Failing storage hardware.** A dying drive turning file restoration into endless retries.
- **Corrupted rollback checkpoint.** The pre-update snapshot itself being damaged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Apply the two-hour rule

Do nothing for two full hours from when you first noticed the freeze. Watch for any sign of life: dot animation movement, disk activity light, fan changes, screen flicker. Rollbacks on large feature updates with slow drives genuinely take 90+ minutes, and the progress display is minimal by design.

Only when you have two hours of zero activity — frozen dots, dark disk light, no change whatsoever — is it stuck. Note the exact time. This rule exists because interrupting a working rollback is the one mistake that converts a recoverable situation into a difficult one. The companion guide on [what to do during undoing changes](/articles/what-to-do-if-we-couldn-t-complete-the-updates-undoing-changes/) covers the normal-rollback side of this experience.

### Fix 2: Single force shutdown, then observe

After confirming the freeze, hold the power button 5-10 seconds until the laptop powers off. Wait 30 seconds, then power on — exactly once.

Windows typically does one of three things: resumes and completes the rollback, restarts the rollback from scratch, or boots to the desktop as if nothing happened. Give whichever occurs up to an hour to finish. Do not force-shutdown repeatedly — one clean interruption gives the rollback machinery its best chance to recover; repeated interruptions compound the damage.

### Fix 3: Enter the Recovery Environment

If the laptop boots back into the stuck rollback screen, or loops, interrupt the boot three times (hold power when the Windows logo appears) to reach the Recovery Environment. This is your safe workspace outside the broken rollback.

From here, go to Troubleshoot, Advanced options. You have two strong options: "Uninstall Updates" (removes the failed quality or feature update directly, which often instantly resolves the stuck rollback) or "System Restore" (returns to a pre-update restore point). Try Uninstall Updates first — it is the most targeted fix. Your personal files are untouched by either option.

### Fix 4: Uninstall the failed update manually

In the Recovery Environment: Troubleshoot, Advanced options, "Uninstall Updates." Choose "Uninstall latest quality update" first. If the stuck rollback followed a feature update, use "Uninstall latest feature update" instead.

Let the uninstall complete — it can take 15-30 minutes. Then choose "Continue" to restart normally. In most stuck-rollback cases, removing the update that triggered the whole saga clears the logjam immediately and the laptop boots to the desktop. Once you are back, pause Windows Update for 7 days before doing anything else, so the same update does not immediately retry.

### Fix 5: Check disk health from recovery

A rollback stalled on disk errors will stall again. In the Recovery Environment's Command Prompt, run `chkdsk C: /f /r` (confirm the drive letter with `diskpart`, `list volume` first — in recovery, Windows is often not C:). Let it complete fully; the /r pass on a large drive takes a while.

If chkdsk finds and repairs bad sectors or file-system errors, that was likely the stall cause — the rollback was retrying unreadable sectors forever. After chkdsk completes, restart and see if the rollback now finishes on its own. Recurring disk errors mean the drive is failing and needs replacement regardless of the update situation. Microsoft documents recovery tools in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 6: System Restore to a pre-update point

If uninstalling the update does not clear it, use System Restore: in the Recovery Environment, Troubleshoot, Advanced options, System Restore, and pick the most recent restore point from before the update attempt.

System Restore reverts system files, drivers, and registry to that point without touching personal files. It is a broader hammer than update-uninstall, and it resolves stuck rollbacks caused by corrupted servicing state rather than the update package itself. After restoring and booting normally, run `sfc /scannow` from an elevated Command Prompt to verify system file integrity.

### Fix 7: Fix the root cause before the next update attempt

A recovered laptop that immediately retries the same update will reproduce the same stuck rollback. With the system booted: update drivers and BIOS through your manufacturer's utility, free 15+ GB on C:, uninstall third-party antivirus with its removal tool, and clear the update cache (`net stop wuauserv` / `net stop bits`, empty `C:\Windows\SoftwareDistribution\Download`, restart services).

Then unpause updates and let the update try once — just once — with the fixed foundation. If it fails again, install manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) using the KB number, or hide that specific update and wait for the next month's cumulative package. The [stuck-on-restarting recovery guide](/articles/how-to-fix-windows-update-stuck-on-restarting-on-lenovo-laptop/) covers the closely-related frozen-restart scenario.

## Closing

A stuck "undoing changes" screen is the safety net itself needing rescue — frustrating, but recoverable in nearly every case. Verify the freeze with the two-hour rule, interrupt once, and clear the jam through the Recovery Environment's uninstall-updates or System Restore. Then do the part most people skip: fix the driver, disk, or servicing problem that failed the update in the first place, so the next rollback never has to happen.
