---
title: "Windows Update Undoing Changes Stuck? What to Do Now"
slug: what-to-do-if-windows-update-undoing-changes-stuck
date: 2026-10-05
categories: ["windows-update"]
tags: ["undoing changes", "update rollback stuck", "windows update", "stuck loop"]
description: "Your laptop is stuck on Undoing changes made to your computer? Learn how long to wait and how to break the loop safely."
thumbnail: "/images/thumbs/what-to-do-if-windows-update-undoing-changes-stuck.webp"
faqs:
  - q: "How long should Undoing changes take on a laptop?"
    a: "A normal rollback takes 15 to 45 minutes on an SSD laptop and up to 90 minutes on a hard drive machine. The screen shows no progress details, which makes even a healthy rollback feel stuck. Only treat it as a genuine stall if nothing has changed for over two hours on an SSD or three hours on a hard drive, with zero disk activity."
  - q: "Can I turn off my laptop while it says Undoing changes?"
    a: "Avoid it if at all possible. Interrupting a rollback is riskier than interrupting the original update because the system is mid-restoration. Only force a shutdown after confirming zero disk activity for several hours, and be prepared to use recovery tools afterward. In most cases, patience is the correct and complete fix."
  - q: "Why did my update fail and start undoing changes?"
    a: "Windows rolls back automatically when an update cannot complete safely, usually due to a driver conflict, corrupted update files, insufficient disk space, or a failing hard drive. The rollback itself is working as designed. The real task is diagnosing why the update failed, using the error code in update history, so the next attempt succeeds instead of rolling back again."
  - q: "What if Undoing changes loops forever and never finishes?"
    a: "A true infinite loop usually means the rollback itself hit corrupted files or a failing disk. Boot into the Windows Recovery Environment, try Startup Repair, and if that fails, use System Restore to a point before the update. As a last resort, the Reset this PC option with file preservation gets you a working system."
---

Undoing changes made to your computer is Windows telling you the update failed and it is putting everything back. That message is actually good news: the safety net caught the fall. The bad news is that the safety net itself can appear to hang, leaving you staring at a spinner with no progress bar and no estimate.

Here is the critical distinction: a rollback in progress versus a rollback that is genuinely stuck. The first needs only patience and power. The second needs the recovery environment and a careful hand. This guide helps you tell them apart and act correctly for each case.

## Why this happens

- **Rollback is file-heavy and silent:** Restoring thousands of files shows no progress, looking frozen while working normally.
- **Failing hard drive:** Bad sectors stall the restore with endless retries, turning a 30-minute rollback into hours.
- **Corrupted restore data:** The snapshot Windows needs to roll back to is damaged, so the process cannot complete.
- **Interrupted original update:** A forced shutdown during the install left the system in a state the rollback struggles to unwind.
- **Driver conflicts during restore:** The same driver that broke the update can interfere with restoring the old state.
- **Low disk space:** The rollback needs working room, and a nearly full drive throttles it badly.
- **Pending operations deadlock:** Queued servicing operations from the failed update block the restore sequence.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the rollback is actually running

1. Check the disk activity LED. Flickering means the restore is progressing, even with no on-screen change.
2. On hard drive laptops, listen for seeking sounds. Rhythmic activity is a healthy sign.
3. Confirm the laptop is plugged into AC power. A rollback that loses power mid-restore creates far worse problems.
4. If there is any activity, wait. Give SSD machines up to two hours and hard drive machines up to three before declaring a stall. Most undoing-changes scares end here.

### Fix 2: Wait with the right setup

1. Plug in the charger and make sure it is actually charging, not just connected.
2. Disable any sleep timers you can reach, though the rollback screen usually suppresses sleep on its own.
3. Do not press keys or move the mouse repeatedly hoping to wake something up. The screen is supposed to look like that.
4. Set a timer for one hour and walk away. Constant watching makes normal rollbacks feel broken. If the screen is identical with zero disk activity after the full waiting period, move to recovery steps.

### Fix 3: Force a restart only when truly stalled

1. After confirming hours of zero activity, hold the power button for 10 seconds to force shutdown.
2. Wait 30 seconds, then power on. Windows will usually resume or restart the rollback automatically.
3. If it boots normally to the desktop, the rollback eventually completed. Check **Settings > Windows Update > Update history** for the failure details.
4. If it returns to the stuck screen, let it try once more for 30 minutes before moving to the recovery environment. For background on failed updates generally, the [cumulative update guide](/articles/cumulative-update-fails-to-install-troubleshooting/) explains the failure side.

### Fix 4: Boot into the Recovery Environment

1. Force shutdown during boot three times in a row: power on, hold power when the logo appears, repeat. On the third boot, Windows enters the Recovery Environment.
2. Choose **Troubleshoot > Advanced options > Startup Repair** and let it run. It fixes boot issues that can trap a rollback, and it is fully automatic.
3. If Startup Repair does not help, return to Advanced options and try **System Restore**, picking a restore point from before the update. Choose the most recent pre-update point for the smallest change.
4. System Restore rolls the system back cleanly without touching your personal files, which often succeeds where the automatic undo stalled. Your documents, photos, and downloads are preserved through the process.

### Fix 5: Repair the disk underneath the rollback

1. From the Recovery Environment, open **Troubleshoot > Advanced options > Command Prompt**.
2. Run `chkdsk C: /f /r` to find and repair disk errors. On large drives this takes a while; let it finish.
3. If chkdsk reports bad sectors or unrecoverable errors, the disk itself is why the rollback stalled. Back up data via the Command Prompt before doing anything else.
4. A healthy disk lets the rollback complete on the next boot. A failing disk means replacement before any further updates, since every future update will hit the same wall.

### Fix 6: Find why the update failed in the first place

1. Once you are back in Windows, open **Settings > Windows Update > Update history** and note the failed update's KB number and error code.
2. Common rollback triggers include driver conflicts, which the [0xC1900101 troubleshooting](/articles/update-fails-with-error-0xc1900101-troubleshooting/) guide decodes, and corrupted update caches.
3. Address the root cause before retrying: update drivers, clear the SoftwareDistribution cache, and free disk space. Each of these is a ten-minute job that prevents another hour-long rollback.
4. Retrying the same update without fixing the cause just produces another rollback. Microsoft documents common failure codes on the [Windows support hub](https://support.microsoft.com/en-us/windows), which helps you match your code to the right repair.

### Fix 7: Reset the PC if the loop will not break

1. If the undoing-changes screen truly never completes and recovery tools fail, return to the Recovery Environment.
2. Choose **Troubleshoot > Reset this PC > Keep my files**. This reinstalls Windows while preserving your personal data.
3. You will need to reinstall applications afterward, so treat this as the last resort it is.
4. After the reset, install updates one at a time and watch for the one that triggers trouble. A clean system with current drivers rarely rolls back.

## Closing

Undoing changes is Windows protecting you, and the vast majority of stuck appearances are just slow, silent rollbacks doing their job. Verify activity, stay on AC power, and wait the full period before intervening. When intervention is truly needed, the recovery environment gives you Startup Repair, System Restore, and Reset in escalating order.
