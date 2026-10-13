---
title: "\"Undoing Changes Made to Your Computer\" Stuck? Here's How to Fix It"
slug: how-do-i-fix-undoing-changes-made-to-your-computer-stuck
date: 2026-10-04
categories: ["windows-update"]
tags: ["undoing changes", "update rollback", "stuck loop", "winre", "system restore"]
description: "Asked and answered: what to do when 'Undoing changes made to your computer' never finishes — safe recovery steps that get your laptop booting again."
thumbnail: "/images/thumbs/how-do-i-fix-undoing-changes-made-to-your-computer-stuck.webp"
faqs:
  - q: "My laptop has said 'Undoing changes' for 3 hours. What do I do first?"
    a: "Force a shutdown by holding the power button for 10 seconds, then boot into the Windows Recovery Environment by interrupting the boot twice at the logo screen. From there you can run Startup Repair, boot into Safe Mode, or use System Restore — all without touching your personal files."
  - q: "Does a stuck rollback mean Windows is broken permanently?"
    a: "No. A stuck rollback means the automatic restore process hit a snag, usually a driver conflict or corrupted pending update data. The underlying Windows installation is typically intact, and the recovery environment tools resolve this in the large majority of cases."
  - q: "How do I stop the same update from failing again after I recover?"
    a: "After you are booted, pause updates for one to two weeks, then fix the likely root cause: update drivers from your laptop manufacturer's site, free up disk space, and temporarily disable third-party antivirus during the retry. Retrying the identical update with nothing changed usually reproduces the identical failure."
  - q: "Should I choose 'Reset this PC' if nothing else works?"
    a: "Only as a last resort. Reset with 'Keep my files' preserves your data but removes installed programs, so it costs real time. Try Startup Repair, Safe Mode cleanup, System Restore, and offline DISM/SFC first — resets are rarely necessary for rollback loops."
---

So your laptop tried to install a Windows update, the update failed, and now the screen says "Undoing changes made to your computer" — and it has said that for a very long time. You are asking the right question, because doing nothing is not a strategy here: a rollback that is genuinely stuck needs intervention, and the good news is that the intervention is straightforward and your files are almost certainly safe.

Here is the mental model that makes everything else make sense. Windows keeps a snapshot of the pre-update system. When the update fails, Windows walks that snapshot backward, restoring each changed file. If one step in that walk gets jammed — a driver that will not release, a corrupted instruction file, a disk that cannot be written — the whole process stalls. Your job is to get into the recovery environment, unjam that step, and let Windows finish booting. The fixes below go from least to most invasive.

## Why this happens

- **A driver refuses to roll back:** Storage controller and display drivers are the usual suspects; if the old driver cannot cleanly replace the new one, the restore stalls mid-step.
- **Pending update instructions are corrupted:** The pending.xml file that tells Windows what to undo can itself be damaged, so the rollback engine retries a broken instruction forever.
- **The system drive is full:** Rolling back requires writing restored files. If the failed update consumed the last free space, the rollback has nowhere to write.
- **Third-party antivirus locks system files:** Security filter drivers can hold locks on files the rollback needs to replace, freezing the process.
- **The failed update was interrupted:** A power cut or forced shutdown during the original install leaves the system half-updated in a way the rollback logic cannot reconcile.
- **Pre-existing component store damage:** If system files were already corrupted before the update, the rollback's verification checks fail and it loops.
- **Disk-level errors:** Bad sectors under system files cause silent restore failures that the rollback keeps retrying.
- **Multiple stacked updates:** When several updates install in one session and one fails, the rollback has to unwind all of them in order, multiplying the chances of a jam.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Interrupt the stuck rollback and enter WinRE

The recovery environment is your workshop for everything that follows. Getting there requires interrupting the normal boot three times.

1. Hold the power button for a full 10 seconds until the laptop powers off completely.
2. Power on, and the moment the manufacturer's logo appears, hold the power button for 10 seconds again.
3. Repeat step 2 one more time. On the next boot, Windows enters Automatic Repair and shows the **Choose an option** screen.
4. Select **Troubleshoot > Advanced options** — you now have Startup Repair, System Restore, Command Prompt, and Startup Settings at your disposal.

### Fix 2: Try Startup Repair first

Startup Repair is automated, safe, and fixes boot-record and system-file problems that trap rollback loops. Always try it before anything manual.

1. In WinRE, choose **Troubleshoot > Advanced options > Startup Repair**.
2. If asked, select your Windows installation and enter your account password.
3. Let it run to completion, then select **Continue** to attempt a normal boot.
4. If Windows boots, immediately pause updates for a week before doing anything else.

### Fix 3: Use System Restore from WinRE

System Restore rolls the system back to a snapshot taken before the update — a cleaner operation than the stuck automatic rollback, because it does not depend on the jammed update machinery.

1. In WinRE, go to **Troubleshoot > Advanced options > System Restore**.
2. Select your Windows installation.
3. Choose the restore point with the date just before the failed update (Windows usually creates one automatically).
4. Confirm and let the restore finish, then boot normally and verify everything works.

### Fix 4: Boot to Safe Mode and remove the failed update's traces

Safe Mode skips the problematic drivers, which often lets you boot far enough to clean up the mess the failed update left behind.

1. In WinRE: **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. In Safe Mode, open **Settings > Windows Update > Update history > Uninstall updates** and remove the update that triggered the loop.
3. Open **Terminal (Admin)**, run `net stop wuauserv`, then delete all files in `C:\Windows\SoftwareDistribution\Download`.
4. Restart normally. If the machine boots cleanly, the jammed update data was the problem — the same cleanup that fixes [frozen update downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/) applies here.

### Fix 5: Run offline DISM and SFC from the Command Prompt

If the rollback engine or system files are damaged, repair them while Windows is offline, where nothing is locked or in use.

1. In WinRE, open **Troubleshoot > Advanced options > Command Prompt**.
2. Confirm your Windows drive letter with `dir C:` (in WinRE it is sometimes D: — adjust accordingly).
3. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
5. Type `exit` and choose **Continue** to boot.

### Fix 6: Check the drive for physical errors

Repeated rollback failures at the same stage strongly suggest the disk, not the software. Rule it out before going further.

1. In WinRE Command Prompt, run `chkdsk C: /f /r`.
2. Let the scan finish completely — it can take an hour or more on large drives.
3. If it reports bad sectors, clusters, or unreadable segments, prioritize backing up your data (via another PC or a bootable USB) over further repair attempts.
4. A drive with growing bad sectors should be replaced; software cannot fix failing hardware.

### Fix 7: Reset with file preservation as the final option

If every repair fails, **Troubleshoot > Reset this PC > Keep my files** reinstalls Windows while preserving your personal data. Installed applications will need reinstalling, so treat this as the last resort it is. After the reset, install drivers from your laptop maker's support site first, then let Windows Update run — a clean driver baseline prevents the loop from recurring.

For the technician-oriented version of this same recovery, with offline DISM commands and boot-record repair, see [troubleshooting the stuck undoing-changes screen](/articles/troubleshoot-undoing-changes-made-to-your-computer-stuck/) — plus Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) for recovery environment reference.

## Closing

A stuck "undoing changes" screen is Windows mid-rescue, not Windows dead — it just needs help finishing the job. Interrupt the loop, enter the recovery environment, and work the ladder: Startup Repair, System Restore, Safe Mode cleanup, offline DISM/SFC, disk check, and only then a reset. Once you are back in Windows, fix the root cause before the next update attempt, because the same driver, disk-space, or antivirus problem that caused this loop will cause the next one too.
