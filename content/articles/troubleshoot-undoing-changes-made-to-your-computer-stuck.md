---
title: "Stuck on 'Undoing Changes Made to Your Computer'? How to Break the Loop"
slug: troubleshoot-undoing-changes-made-to-your-computer-stuck
date: 2026-10-02
categories: ["windows-update"]
tags: ["undoing changes", "stuck update", "rollback loop", "windows 11", "windows 10"]
description: "Your laptop is stuck on 'Undoing changes made to your computer' after a failed update. Here's how to break the rollback loop safely and get Windows booting again."
thumbnail: "/images/thumbs/troubleshoot-undoing-changes-made-to-your-computer-stuck.webp"
faqs:
  - q: "How long should 'Undoing changes' take before I worry?"
    a: "On a healthy machine, the rollback typically finishes in 15 to 45 minutes. If the spinner has been going for over two hours with no progress, or the machine has rebooted into the same screen three or more times, the rollback is stuck and you should intervene using the steps in this guide."
  - q: "Will I lose my files if the update rollback is stuck?"
    a: "Usually not. The 'undoing changes' screen is Windows restoring the pre-update state, and your personal files are not part of what gets rolled back. Your files are at risk only if the disk itself is failing or if you choose a reset option that removes data — so avoid reset options unless nothing else works."
  - q: "Is it safe to force-shutdown during 'Undoing changes'?"
    a: "It is not risk-free, but after two hours of no progress it is often the only way forward, and Windows is designed to recover from an interrupted rollback via the recovery environment. Do not force-shutdown in the first hour; give the rollback a genuine chance to finish first."
  - q: "Why does this happen after every major update?"
    a: "Repeat rollback loops point to a persistent blocker: a driver that fails migration, a corrupted component store, critically low disk space, or an antivirus filter that breaks the install. Fix that root cause after you recover, or the next update will roll back the same way."
---

Few screens inspire as much dread as "Undoing changes made to your computer" spinning endlessly after a failed update. Your laptop tried to install something, the install failed, and now Windows is supposed to be rolling back to the working state — except it never finishes. The machine reboots, returns to the same screen, and the loop continues.

Stay calm. This screen means Windows is actively trying to protect your installation by restoring the last known good state. When it gets stuck, the rollback process itself has hit a snag — usually a corrupted pending operation, a driver that will not unload, or a disk problem. The fixes below are ordered by safety: patience first, then the recovery environment, then the heavier repairs. Do not jump to a reset; almost nobody needs one for this.

## Why this happens

- **Driver migration failure:** A storage or display driver fails to migrate during the update, so the rollback cannot cleanly restore the old driver state and stalls.
- **Corrupted pending operations:** Half-written pending.xml entries from the failed install confuse the rollback engine, which retries the same broken step indefinitely.
- **Critically low disk space:** The rollback needs room to restore replaced files. If the drive filled up during the update, there is nowhere to roll back to.
- **Antivirus filter drivers:** Third-party security filters can lock files the rollback needs to replace, freezing the restore process mid-stream.
- **Disk errors:** Bad sectors in the middle of system files make the rollback's file-restore operations fail silently and repeatedly.
- **Interrupted first attempt:** A power loss or forced shutdown during the original update leaves the system in a neither-here-nor-there state that the rollback cannot reconcile.
- **Corrupted component store:** If WinSxS was already damaged before the update, the rollback has no clean baseline to restore and loops on verification failures.
- **Failing Windows Update cache:** A damaged SoftwareDistribution folder can feed the installer bad data on every retry, producing an endless fail-and-rollback cycle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it a real chance, then force a clean boot into recovery

First, rule out a merely slow rollback. If it has genuinely been over two hours, interrupt it and boot into the Windows Recovery Environment (WinRE), where all the real repair tools live.

1. If the spinner has run for more than two hours with no change, hold the power button for 10 seconds to force a shutdown.
2. Power on. As soon as the manufacturer's logo appears, hold power for 10 seconds again to interrupt boot. Repeat this interrupt twice more.
3. On the third boot, Windows should enter **Automatic Repair** and then the **Choose an option** screen — this is WinRE.
4. Select **Troubleshoot** to access Startup Repair, Safe Mode, Command Prompt, and System Restore.

### Fix 2: Run Startup Repair from the recovery environment

Startup Repair fixes boot configuration problems that can trap the rollback loop. It is automated and safe.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation if prompted and let the tool run.
3. When it finishes, choose **Continue** to boot Windows normally and see whether the loop is broken.

### Fix 3: Boot into Safe Mode and clear the update state

Safe Mode loads a minimal driver set, which bypasses the driver conflict that is often jamming the rollback. From there you can clear the failed update's footprint.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. Once in Safe Mode, open **Settings > Windows Update > Update history** and uninstall the most recent update that triggered the loop.
3. Open **Terminal (Admin)** and stop the update services: `net stop wuauserv` and `net stop bits`.
4. Delete the contents of `C:\Windows\SoftwareDistribution\Download` (leave the folder itself), then restart normally.

### Fix 4: Use System Restore to a pre-update point

If Windows created a restore point before the update — which it usually does — rolling back to it from WinRE bypasses the stuck automatic rollback entirely.

1. In WinRE, go to **Troubleshoot > Advanced options > System Restore**.
2. Choose your Windows installation, then pick the restore point dated just before the failed update.
3. Let the restore complete and boot normally.
4. After booting, pause updates for a week (**Settings > Windows Update > Pause updates**) while you fix the root cause, or the same update will retry and loop again — the same cycle described in [stuck update downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/) often precedes this.

### Fix 5: Repair the component store and boot files from WinRE Command Prompt

When the rollback engine itself is damaged, repair it offline. These commands run against the offline Windows installation.

1. In WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` (if C: is your Windows drive; check with `dir C:` first).
3. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Rebuild boot files: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd`.
5. Type `exit`, choose **Continue**, and boot normally.

### Fix 6: Check the disk for errors

If rollbacks and restores keep failing at the same point, suspect the drive. A disk with bad sectors will corrupt every rollback attempt.

1. Boot into WinRE Command Prompt as in Fix 5.
2. Run `chkdsk C: /f /r` and let the full scan complete — this can take over an hour on large drives.
3. If chkdsk reports bad sectors or the drive makes clicking noises, back up your data immediately using another computer or a live USB before doing anything else.
4. A failing drive needs replacement, not more software repairs.

### Fix 7: Perform an in-place upgrade or reset as a last resort

If nothing breaks the loop, reinstall Windows while preserving your data. Boot from Windows installation media, choose your language, and select **Upgrade** to keep files and apps — or, from WinRE, **Troubleshoot > Reset this PC > Keep my files**. Both give you a fresh update pipeline. After recovery, update drivers from your manufacturer's site before letting Windows Update run wild again.

Once you are booted again, work through our [monthly cumulative update failure guide](/articles/how-to-fix-monthly-cumulative-update-failed-step-by-step/) to remove the root cause — and Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) documents the recovery tools used above.

## Closing

The "undoing changes" loop feels catastrophic but is almost always recoverable without data loss: interrupt the stuck rollback, enter the recovery environment, and work through Startup Repair, Safe Mode cleanup, System Restore, and offline DISM/SFC in that order. Once you are booted again, resist the urge to immediately retry the same update — find the blocker (disk space, drivers, antivirus) first. Break the cycle once, properly, and it stays broken.
