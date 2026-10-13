---
title: "How to Fix 'Undoing Changes Made to Your Computer' Stuck on an HP Laptop"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-hp-laptop
date: 2026-10-02
categories: ["windows-update"]
tags: ["undoing changes", "hp", "windows update", "stuck", "rollback"]
description: "HP laptop stuck on 'Undoing changes made to your computer'? Learn the safe waiting window, HP-specific checks, and how to break the loop."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-hp-laptop.webp"
faqs:
  - q: "How long should I wait on the undo screen on an HP laptop?"
    a: "Wait a full hour on an SSD-equipped HP laptop, or two hours on one with a mechanical hard drive, before concluding the rollback is stuck. HP's business and consumer lines both restore thousands of system files during a rollback, which takes time on slower storage. Only intervene after the screen shows zero change and the drive activity light stays dark for the entire window."
  - q: "Is it safe to force restart an HP laptop during the rollback?"
    a: "Yes, after a genuine multi-hour stall. The rollback was already returning the system to its previous working state, so interrupting a frozen one is far safer than interrupting an active update. Hold the power button for 10 seconds, disconnect peripherals, and boot — most HP laptops come up normally or enter automatic repair, which fixes the boot configuration itself."
  - q: "Do HP's own tools cause the update to fail in the first place?"
    a: "Sometimes. HP Support Assistant and HP Wolf Security components have been known to conflict with update installations, particularly when outdated. Updating HP's own software before retrying the Windows update removes one common failure source. The rollback screen itself, though, is a Windows mechanism — HP tools are suspects for the original failure, not the stuck screen."
  - q: "Will the rollback delete my files?"
    a: "No. Undoing changes reverses only the system modifications the failed update made. Your documents, photos, installed applications, and personal settings are untouched. The rollback exists precisely to return you to the working system you had before the update attempt, files and all."
---

The "Undoing changes made to your computer" screen means a Windows update failed on your HP laptop and Windows is rolling back to the previous working state. It is the safety net doing its job. The problem begins when the screen sits there for hours — no percentage, no change, just a spinning circle — and you cannot tell whether the rollback is working or frozen.

On HP laptops there are a couple of brand-specific wrinkles worth knowing. HP Support Assistant, HP Wolf Security, and HP's BIOS-level utilities sometimes contribute to the original update failure, and HP's Sure Start BIOS protection can interact with the boot process after a forced restart. None of that changes the core repair sequence, but it adds HP-specific checks to the later steps.

This guide covers the full sequence: how long to wait, how to verify the rollback is actually working, how to intervene safely if it is frozen, and how to stop the next update attempt from ending the same way. Work through the fixes in order.

## Why this happens

- **The update failed and triggered the rollback.** Driver conflicts, corrupted downloads, or blocked file operations abort the install; Windows reverses the partial changes automatically.
- **The rollback is slow, not stuck.** Restoring system files takes 15 to 45 minutes on SSDs, up to two hours on hard drives.
- **The rollback stalled.** Failing drive sectors, exhausted disk space, or conflicting security software can freeze the undo process mid-way.
- **HP security software interfered.** Outdated HP Wolf Security or third-party antivirus components can block the rollback's file operations.
- **The update cache is corrupted.** Damaged download files make the rollback engine work on bad data.
- **Disk space ran out.** The undo process needs working room on C:; a full drive stalls it.
- **A queued HP driver update conflicts.** HP driver packages staged by Windows Update can fight the files being restored.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait the full window and verify real activity

Most "stuck" rollbacks are slow rollbacks. Verify before acting.

1. Note the time. Wait one full hour (SSD) or two full hours (hard drive) from when the screen first appeared.
2. Watch the disk activity light on the laptop. Blinking means the rollback is working — keep waiting.
3. Listen for drive chatter or fan noise. Steady activity means progress; total silence for 30 minutes means a stall.
4. Proceed only after the full window with zero screen change and zero drive activity.

### Fix 2: Force a restart and let HP's boot process recover

A frozen rollback will not unfreeze itself.

1. Hold the **power button** for 10 seconds until the laptop powers off completely.
2. Disconnect all USB devices, docks, external monitors, and SD cards.
3. Wait 30 seconds, then power on. Most HP laptops boot to the desktop or login screen.
4. If the laptop enters the blue recovery screen, let **Automatic Repair** run — it fixes interrupted boot configurations on its own. HP's Sure Start may also verify the BIOS during this boot; let it finish.

### Fix 3: Boot into Safe Mode and clear the update cache

Once Windows is up, stop the next attempt from failing identically.

1. Hold **Shift** while clicking **Restart** from the login screen, then go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.
2. In an elevated Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with the matching `net start` commands, then reboot normally.

### Fix 4: Update HP's own software before retrying

Remove the HP-specific failure sources.

1. Open **HP Support Assistant** and install all its pending updates — outdated HP utilities are a known update-failure contributor.
2. Check **HP Wolf Security** or your third-party antivirus: temporarily disable real-time protection during the next update attempt.
3. Visit [HP support](https://support.hp.com/us-en), enter your model, and check for a BIOS update — an outdated BIOS causes failures on major updates.
4. Restart to a clean state with HP's software current.

### Fix 5: Free up disk space

Space-starved rollbacks and retries fail in exactly this pattern.

1. Open **Settings > System > Storage** and confirm at least 20 GB free on C:.
2. Run **Disk Cleanup** with system files selected; remove **Windows Update Cleanup** and temporary files.
3. Move large personal files to external storage and uninstall unused programs.
4. Only retry the update after confirming the free space.

### Fix 6: Repair system files and run the troubleshooter

Fix the underlying damage behind the original failure.

1. In an elevated Command Prompt, run `sfc /scannow` to completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15 to 30 minutes.
3. Run the **Windows Update** troubleshooter under **Settings > System > Troubleshoot > Other troubleshooters**.
4. Restart. For documented manual repair steps, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Retry deliberately or bypass the bad update

A controlled retry, not a blind one.

1. With power connected and stable internet, close all programs and click **Check for updates**.
2. If the same update fails with the same error, note its KB number from update history and install it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. If the manual install also fails, hide the update or pause updates for a few weeks while a fixed version ships.
4. For a feature update your HP hardware struggles with, a repair install from the Windows 11 download page rebuilds the system while keeping files and apps.

## Closing

The stuck undo screen on an HP laptop follows the same rules as anywhere else — verify the stall with real disk-activity checks, intervene cleanly, then change the conditions before retrying — with HP Support Assistant updates and Wolf Security added to the suspect list. Work the sequence once, properly, and the loop ends. For the same screen on other brands, see the [Windows 11 undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11/) and the [24H2-era undoing-changes deep dive](/articles/how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2/), or the [step-by-step undoing-changes walkthrough](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step/) for the full recovery sequence.
