---
title: "Fix the Windows 11 Automatic Repair Loop on an ASUS Laptop"
slug: how-to-fix-automatic-repair-loop-windows-11-on-asus-laptop
date: 2026-10-13
categories: ["windows-errors"]
tags: ["automatic repair", "boot loop", "windows 11", "asus laptop"]
description: "ASUS laptop stuck in the Windows 11 Automatic Repair loop? Here's the exact recovery sequence — from Startup Repair to boot file rebuilds."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11-on-asus-laptop.webp"
faqs:
  - q: "What is the Automatic Repair loop?"
    a: "It's when Windows fails to boot, launches Automatic Repair, the repair fails, and the laptop reboots — only to fail and repair again, forever. The loop means the boot process is broken (corrupt boot files, bad update, disk errors) but the recovery environment itself still works, which is your way in."
  - q: "Will fixing the loop delete my files?"
    a: "The standard fixes — Startup Repair, boot file rebuilds, update uninstalls, System Restore — all preserve your files. Only the 'Reset this PC' option with 'Remove everything' deletes data, and that's clearly labeled as a last resort."
  - q: "Why did my ASUS get stuck in the loop?"
    a: "Common triggers: a Windows update that broke boot files, corrupted BCD (boot configuration data), disk errors, a failing drive, or an interrupted update. On ASUS gaming laptops, aggressive overclocking or Armoury Crate power tweaks can also corrupt the boot state."
  - q: "How do I get to Advanced Options if Windows won't boot?"
    a: "You're probably already there — the loop itself lands on the 'Automatic Repair couldn't repair your PC' screen, which has an Advanced options button. Click it to reach Troubleshoot, where all the real fixes live."
---

The Automatic Repair loop is Windows trying its best and failing: it can't boot, so it launches repair; repair can't fix it, so it reboots; boot fails again. On ASUS laptops the loop usually starts after a bad update, corrupted boot files, or disk trouble — and the good news is that the recovery environment (the blue **Choose an option** screen) gives you every tool you need to break out. Your files are safe through all of this.

Work through the fixes in order. Each one targets a deeper layer of the boot process.

## Why this happens

- **Corrupted BCD (Boot Configuration Data)**: The BCD tells Windows where and how to boot. If it's damaged — by a failed update, a forced shutdown, or disk errors — Windows can't start and Automatic Repair can't rebuild it on its own.
- **Failed Windows update**: An update that broke boot-critical files or drivers leaves the system unbootable. Automatic Repair detects the failure but can't undo the update by itself.
- **Disk errors or a failing drive**: Bad sectors in the boot partition or system files cause boot failures that repeat identically every attempt — the definition of a loop.
- **Corrupted system files**: Damage to the kernel or boot drivers means Windows starts loading and then crashes, triggering repair again.
- **Fast Startup conflicts**: A corrupted hibernation file from Fast Startup can poison every boot attempt with the same broken state.
- **ASUS-specific firmware or overclock instability**: On ASUS gaming laptops, unstable overclocks, XMP profiles, or Armoury Crate power modifications can corrupt the boot process, especially after firmware updates.

## How to fix it

You're working from the **Automatic Repair couldn't repair your PC** screen. Click **Advanced options** > **Troubleshoot** to begin.

### Fix 1: Try Startup Repair once more, properly

It failed before, but give it one clean shot — sometimes it needs two passes.

1. Go to **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Select your account, enter your password, and let it run fully (10-15 minutes).
3. If it fails, don't loop on it — move to Fix 2. Repeating a failed repair changes nothing.

### Fix 2: Boot into Safe Mode

If Safe Mode works, the core OS is intact and a driver or update is the problem.

1. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **4** for Safe Mode.
3. If Safe Mode boots: uninstall the most recent update (**Settings** > **Windows Update** > **Update history** > **Uninstall updates**), update or roll back drivers in **Device Manager**, then restart normally.
4. If Safe Mode also fails, continue to Fix 3 — the boot files themselves need rebuilding.

### Fix 3: Rebuild the BCD and boot files

This is the fix that breaks most repair loops.

1. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run these commands one at a time, pressing Enter after each:

   ```cmd
   bootrec /fixmbr
   bootrec /fixboot
   ```

   If `fixboot` returns "Access is denied," run these instead:

   ```cmd
   diskpart
   list vol
   ```

   Find the EFI partition (FAT32, ~100MB), note its letter, then:

   ```cmd
   sel vol <number>
   assign letter=Z:
   exit
   bcdboot C:\Windows /s Z: /f UEFI
   ```

3. Then rebuild the boot configuration:

   ```cmd
   bootrec /rebuildbcd
   ```

4. Type `exit`, choose **Continue** to restart, and test.

### Fix 4: Run system file repair from the recovery prompt

Corrupted system files can keep the loop going even with a healthy BCD.

1. Open **Command Prompt** from **Advanced options** again.
2. Run:

   ```cmd
   sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
   ```

3. Let it complete — this takes a while from the recovery environment.
4. Restart and test.

### Fix 5: Uninstall the recent update

If the loop started after an update, remove it from recovery.

1. Go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Remove the latest **quality update** first, restart, and test.
3. If the loop persists, go back and uninstall the latest **feature update**.
4. Once booted, pause updates for a few weeks.

### Fix 6: Use System Restore

If you have a restore point from before the loop, this is the cleanest undo.

1. Go to **Troubleshoot** > **Advanced options** > **System Restore**.
2. Pick the most recent restore point from before the problem started.
3. Let it complete and restart. Your files are preserved; only system changes are rolled back.

### Fix 7: Check the disk for errors

A failing drive explains loops that resist every software fix.

1. Open **Command Prompt** from **Advanced options**.
2. Run:

   ```cmd
   chkdsk C: /f /r
   ```

3. Let it finish — on large drives this can take an hour or more.
4. If chkdsk finds bad sectors in critical areas, back up your data at the first successful boot and plan a drive replacement. See [what to do about faulty hardware corrupted page](/articles/what-to-do-if-faulty-hardware-corrupted-page/) for hardware triage.

### Fix 8: Reset BIOS to defaults

On ASUS machines, unstable firmware settings can poison the boot.

1. Restart and press **F2** (or **Del**) to enter BIOS.
2. Press **F9** to **Load Optimized Defaults**, then **F10** to save and exit.
3. If you had XMP, overclocks, or Armoury Crate-linked BIOS tweaks, leave them off until the system is stable for a week.

### Fix 9: Reset Windows keeping your files (last resort)

When nothing else breaks the loop, reinstall Windows without losing personal data.

1. Go to **Troubleshoot** > **Reset this PC**.
2. Choose **Keep my files**.
3. Follow the prompts. This reinstalls Windows, removes apps and settings, but preserves your personal files.
4. Afterward, install drivers from ASUS's support site before running Windows Update.

## Closing

The Automatic Repair loop feels hopeless because it repeats, but it's actually Windows handing you the recovery tools on a platter — rebuild the BCD, remove the bad update, check the disk, and the loop breaks. Most ASUS laptops are back up by Fix 3 or Fix 5. For the Dell version of this problem, see [how to break the automatic repair loop on Dell](/articles/how-to-fix-automatic-repair-loop-windows-11-on-dell-laptop/), or learn [how to use System Restore on Windows 11](/articles/how-can-i-use-system-restore-on-windows-11/) for the restore-point strategy in depth.
