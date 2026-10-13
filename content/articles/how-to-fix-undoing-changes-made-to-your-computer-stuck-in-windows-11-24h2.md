---
title: "'Undoing Changes Made to Your Computer' Stuck in Windows 11 24H2 — Recovery Guide"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2
date: 2026-09-15
categories: ["windows-update"]
tags: ["undoing changes stuck", "windows 11 24h2", "update rollback", "recovery", "windows update"]
description: "The 'Undoing changes made to your computer' screen is frozen on Windows 11 24H2. Learn how to tell stuck from slow and recover safely."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2.webp"
faqs:
  - q: "What makes the undoing changes screen freeze on 24H2?"
    a: "Version 24H2's rollback reverses more components than earlier builds — including virtualization-based security configurations and updated driver frameworks — so the transaction is longer and has more points where a misbehaving driver can deadlock it. A storage driver that will not unload cleanly is the most common deadlock source. The screen looks frozen because the servicing engine gives almost no progress feedback during the reversal."
  - q: "How do I know if the rollback is stuck or just slow on 24H2?"
    a: "Watch the disk activity light and listen to the machine. Blinking disk activity or audible drive work means the rollback is progressing — 24H2 rollbacks legitimately take 30 to 60 minutes on SSDs and longer on hard drives. A completely dark, silent machine at an unchanging screen for over an hour is stuck. Only the second case calls for intervention."
  - q: "Can I boot into recovery while the undoing changes screen is showing?"
    a: "Yes, by interrupting the boot. Hold the power button for 10 seconds to shut down, then power on and interrupt twice more at the Windows logo to reach Automatic Repair. From there you can access Safe Mode, System Restore, Startup Repair, and the command prompt. Use this path only after confirming the rollback is truly frozen, not merely slow."
  - q: "Will System Restore help if the rollback is stuck?"
    a: "Sometimes. If Windows created a restore point before the update — which it normally does — restoring to it from the recovery environment can bypass a deadlocked rollback. Choose the most recent pre-update restore point. If no restore points exist, the remaining options are the cache reset from the recovery command prompt or an in-place upgrade repair."
---

Windows 11 24H2 made the "Undoing changes made to your computer" screen both more common and more intimidating. The rollback transaction in 24H2 reverses more than earlier builds did — virtualization-based security settings, new driver frameworks, additional servicing stack components — which means it takes longer and offers more places for a misbehaving driver to deadlock it. The screen gives you no progress bar, so a healthy 45-minute rollback and a genuinely frozen one look identical at first glance.

That ambiguity is what this guide resolves first. You will learn to read the machine's physical signals — disk light, fan, drive sounds — to distinguish slow from stuck, because the correct action differs completely between the two. Interrupting a working rollback risks component-store corruption; patiently waiting on a deadlocked one wastes hours. Everything below is ordered so the diagnosis comes before the intervention.

Keep the charger connected from this moment on. Power loss during a 24H2 rollback is one of the few things that can convert a recoverable stall into an unbootable system, and it is entirely preventable.

## Why this happens

- **A storage or chipset driver deadlocking the reversal:** the most common 24H2-specific freeze — a driver that will not unload while the engine tries to restore its previous version.
- **Virtualization-based security components:** 24H2's deeper VBS integration adds reversal steps that can stall on older firmware.
- **A corrupted update cache:** the failed package's staged files interfering with the rollback's own bookkeeping.
- **Critically low disk space:** the rollback needs room for both copies of changed files; without it, the transaction cannot complete.
- **A failing drive stalling on bad sectors:** read errors during file restoration that the engine retries indefinitely.
- **Interrupted power during the original install:** a half-applied update whose transaction log the rollback struggles to unwind.
- **Third-party disk encryption or security drivers:** filter drivers that block the file operations the reversal requires.
- **Pending servicing operations:** leftover transaction state from an earlier update complicating the current reversal.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the machine — stuck or slow?

This diagnosis determines everything that follows. Get it right before touching the power button.

1. Confirm the charger is connected and the charging light is on.
2. Watch the disk activity light for 15 minutes: steady blinking means the rollback is working.
3. Listen for drive activity and check whether the fan is running — both indicate real work.
4. On 24H2, allow 60 minutes on SSD and up to 90 on HDD before judging. Only a dark, silent, unchanging screen past those windows counts as stuck.
5. If it is working, walk away — this is also the right call for machines [stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/), where the same patience applies.

### Fix 2: One controlled hard reset, then observe

For a confirmed-frozen rollback, a single clean power cycle lets Windows re-attempt the reversal or fall into recovery.

1. Verify zero disk activity for at least 30 consecutive minutes.
2. Hold the power button for 10 seconds until fully off.
3. Disconnect all USB devices, docks, and external drives.
4. Wait 30 seconds, power on, and watch: the rollback may resume and complete, or Automatic Repair may appear.
5. If the desktop loads, back up your files immediately before any further repairs.

### Fix 3: Reach the recovery environment and try Safe Mode

If the rollback screen returns frozen, boot around it into the recovery tools.

1. Interrupt the boot twice at the Windows logo to reach Automatic Repair.
2. Choose Troubleshoot, then Advanced options, then Startup Settings, then Restart, and press 4 for Safe Mode.
3. If Safe Mode loads, run the Windows Update troubleshooter from Settings, then System, then Troubleshoot.
4. If Safe Mode also hangs, return to Advanced options — the command-prompt and restore tools there are your next options.
5. For a troubleshooter that will not cooperate, see the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 4: Use System Restore from the recovery environment

Windows normally snapshots before updating. Restoring that snapshot can bypass a deadlocked rollback entirely.

1. In the recovery environment, go to Troubleshoot, then Advanced options, then System Restore.
2. Choose the most recent restore point dated before the update.
3. Let the restore complete — it typically takes 15 to 30 minutes.
4. If it succeeds, boot normally and immediately address the cause: clear the update cache and update drivers before retrying.
5. If no restore points exist, continue to Fix 5.

### Fix 5: Reset the update cache from the recovery command prompt

Clearing the poisoned cache from outside Windows removes the failed package's grip on the servicing stack.

1. In the recovery environment, open Command Prompt from Advanced options.
2. Identify your Windows drive letter (it may not be C: here — use `diskpart` then `list volume` to check).
3. Rename the cache: `ren D:\Windows\SoftwareDistribution SoftwareDistribution.old` (adjust the letter).
4. Restart and let Windows boot normally.
5. Once on the desktop, run Windows Update — Microsoft documents the cache reset on its [update support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Repair the store with DISM and SFC, then free space

A damaged component store or a full drive can freeze the rollback itself — fix both from the working desktop.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. Run Disk Cleanup as administrator and ensure at least 20 GB free on C:.
4. Update storage and chipset drivers from your manufacturer's support site.
5. Retry the update only after all three are clean.

### Fix 7: In-place upgrade as the final repair

When the servicing stack cannot unwind or complete transactions, reinstalling Windows over itself rebuilds it.

1. On a working machine, download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) and create a USB installer.
2. Boot the troubled laptop from the USB, or mount the ISO if the desktop loads.
3. Run setup, choose "Keep personal files and apps," and allow 30 to 90 minutes.
4. After the repair, install manufacturer drivers first, then Windows updates.
5. Verify Update history shows clean installs with no red entries.

## Closing

A frozen undoing-changes screen on 24H2 demands one skill above all: telling slow from stuck. The disk light is the instrument, patience is the method, and the recovery environment is the safety net. Most of these cases resolve at Fix 1 (it was just slow) or Fix 2 (one clean reset unjammed it). The deeper repairs exist for the stubborn remainder — work them in order, and the rollback screen loses its power to frighten.
