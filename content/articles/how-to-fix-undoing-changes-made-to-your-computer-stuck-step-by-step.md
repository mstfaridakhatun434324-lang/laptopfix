---
title: "Undoing Changes Made to Your Computer Stuck? A Complete Step-by-Step Fix"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step
date: 2026-09-21
categories: ["windows-update"]
tags: ["undoing changes", "step by step", "windows update", "stuck", "windows 11"]
description: "A complete step-by-step walkthrough for the stuck 'Undoing changes made to your computer' screen, from safe waiting to full recovery."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step.webp"
faqs:
  - q: "What is the very first thing to do on the stuck undo screen?"
    a: "Nothing — for a while. Note the time, then wait a full hour on an SSD laptop or two hours on a hard-drive laptop, watching for disk activity. Most undo screens that look stuck are actually just slow. Intervening too early risks interrupting a working rollback. Only act after the screen has shown zero change and the drive light has stayed dark for the whole waiting window."
  - q: "What if the laptop won't boot after I force a restart?"
    a: "Let the automatic repair run — it appears on its own after two failed boot attempts and fixes most rollback-interrupted boot configurations. If automatic repair fails, boot into the recovery environment and use Startup Repair, System Restore to a pre-update point, or the command-line bootrec tools. Your files remain intact through all of these."
  - q: "How do I prevent this from happening again?"
    a: "After recovering, identify the failing update in update history, clear the update cache, free up at least 20 GB on the C: drive, update your drivers from the manufacturer, and temporarily disable third-party antivirus before retrying. Retrying the identical update with nothing changed is what creates the repeat loop — change the conditions first."
  - q: "Should I try the update again immediately after recovery?"
    a: "Not immediately. First confirm the system is stable, then work through the prevention steps above. When you do retry, do it deliberately: plugged in, on stable internet, with no other programs running. If the same update fails twice with the same error, stop and install it manually from the Microsoft Update Catalog or hide it."
---

This is the full step-by-step walkthrough for the "Undoing changes made to your computer" screen — the one that appears after a failed Windows update and sometimes refuses to go away. If you are staring at that screen right now, start at Fix 1 and follow the sequence exactly. Each step tells you what to do, how long to wait, and how to tell whether it worked before moving on.

The sequence is designed around a simple principle: do the least invasive thing that could work, verify the result, and only then escalate. Most people resolve the problem in the first three steps. The later steps cover the harder cases — a laptop that will not boot after a forced restart, and preventing the loop from recurring.

Keep the laptop plugged into power for the entire process. Every step below assumes you have already been on the undo screen for a while and are unsure whether it is still working.

## Why this happens

- **The update failed and triggered an automatic rollback.** Driver conflicts, corrupted downloads, or blocked file operations abort the install, and Windows reverses the partial changes.
- **The rollback is slow, not stuck.** Restoring thousands of system files takes 15 to 45 minutes on SSDs and up to two hours on hard drives.
- **The rollback genuinely stalled.** Failing drive sectors, exhausted disk space, or conflicting security software can freeze the undo process.
- **The update cache is corrupted.** Damaged download files make both the install and the rollback chew on bad data.
- **A driver fights the restore.** Queued driver updates can conflict with the files being restored.
- **Disk space ran out mid-rollback.** The undo process needs working room; a full drive stalls it.
- **Memory faults corrupt the restore.** Bad RAM produces corrupt writes that the rollback engine retries endlessly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait the full window and verify activity (0–2 hours)

Do not skip this. Intervening in a working rollback is the one mistake that can make things worse.

1. Note the current time. Commit to waiting one full hour (SSD) or two full hours (hard drive) from when the screen first appeared.
2. Watch the disk activity light. Blinking or solid light means the rollback is working — reset your timer and keep waiting.
3. Listen for drive or fan sounds. Steady activity means progress.
4. If the screen changes at all — a percentage appears, the laptop restarts on its own — the process is alive. Proceed to Fix 2 only after the full window with zero change and zero activity.

### Fix 2: Force a restart (5 minutes)

A truly frozen rollback will not unfreeze. Since Windows was already reverting to a safe state, this is the correct intervention.

1. Hold the **power button** for 10 full seconds until the laptop shuts off.
2. Disconnect all USB drives, docks, external monitors, and SD cards.
3. Wait 30 seconds, then press the power button once.
4. Watch what happens: most laptops boot to the desktop or login screen. If you land in the blue recovery environment, continue to Fix 3.

### Fix 3: Use the recovery environment (15–30 minutes)

If the laptop does not boot normally, the recovery environment is your workshop.

1. On the blue recovery screen, choose **Troubleshoot > Advanced options > Startup Repair** and let it run to completion.
2. If Startup Repair fails, go back and try **System Restore** — pick a restore point dated before the update attempt.
3. If no restore point exists, open **Command Prompt** from Advanced options and run `bootrec /fixmbr`, `bootrec /fixboot`, and `bootrec /rebuildbcd` in sequence.
4. Restart after each attempt and check whether Windows boots. One of these three resolves the large majority of post-intervention boot failures.

### Fix 4: Boot into Safe Mode and clear the update cache (15 minutes)

Once Windows boots, prevent the next attempt from failing the same way.

1. Hold **Shift** while clicking **Restart** from the login screen, then navigate to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.
2. Open an elevated Command Prompt and run: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with the matching `net start` commands, then reboot normally.

### Fix 5: Free disk space and update drivers (20 minutes)

Remove the two most common repeat-failure causes before retrying anything.

1. Open **Settings > System > Storage** and confirm at least 20 GB free on C:. Use **Disk Cleanup** with system files to clear update leftovers.
2. Update your drivers from the laptop manufacturer's support site — Dell, HP, or Lenovo — focusing on chipset, storage, and display.
3. Temporarily disable third-party antivirus; rely on Windows Security for now.
4. Restart to a clean state before the next step.

### Fix 6: Repair system files and run the troubleshooter (30 minutes)

Fix the underlying damage that caused the original failure.

1. In an elevated Command Prompt, run `sfc /scannow` to completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow up to 30 minutes.
3. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
4. Restart. The update pipeline should now be in a healthy state.

### Fix 7: Retry deliberately — or bypass the bad update (30+ minutes)

The final step is a controlled retry, not a blind one.

1. Plug in the power adapter, connect to stable internet, close all programs, and click **Check for updates**.
2. If the same update fails with the same error, download it by KB number from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually.
3. If the manual install also fails, hide the update with the show/hide troubleshooter and check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that KB.
4. Only after two controlled failures should you consider a repair install — most loops break well before this point.

## Closing

The stuck undo screen rewards patience first and method second: verify it is truly frozen, intervene cleanly, recover through the built-in tools, and then change the conditions before retrying. Followed in order, these seven steps resolve the problem for the overwhelming majority of laptops without ever touching personal files. For brand-specific variations of the same screen, see the [Windows 11 undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11/) and the [24H2-era undoing-changes deep dive](/articles/how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2/), which cover the rollback behavior of newer builds in detail.
