---
title: "Stuck in an Automatic Repair Loop on an HP Laptop? Fix It Here"
slug: how-to-fix-automatic-repair-loop-windows-11-on-hp-laptop
date: 2026-10-10
categories: ["windows-errors"]
tags: ["windows 11", "automatic repair", "hp", "boot loop"]
description: "Your HP laptop keeps saying Preparing Automatic Repair and never boots? Here's how to break the loop and get Windows 11 starting again."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11-on-hp-laptop.webp"
faqs:
  - q: "What is the Automatic Repair loop?"
    a: "It's when Windows fails to start, launches Automatic Repair, the repair fails, and the laptop reboots — only to fail and launch the repair again, endlessly. The root cause is usually corrupted boot files, a damaged system file, a failing drive, or a bad update. Your files are typically untouched."
  - q: "Will breaking the loop delete my files?"
    a: "No. Every fix in this guide — Startup Repair, boot file rebuilds, update uninstalls, System Restore — targets Windows system files, not your personal data. Only the last-resort Reset options touch user files, and even those offer a keep-my-files choice."
  - q: "How do I get to Advanced Options on an HP laptop?"
    a: "Force two interrupted startups: hold the power button during the HP logo to shut down, twice in a row. On the third boot, Windows enters Recovery. Alternatively, power on and press F11 repeatedly to open HP's System Recovery directly, which also leads to Troubleshoot options."
  - q: "What if Startup Repair says it couldn't repair my PC?"
    a: "That message just means the automated tool gave up — it's common and not a verdict on your data. Move on to manual fixes: rebuilding the BCD boot files with bootrec commands, uninstalling the latest update, or running System Restore from the Advanced options menu."
---

Stuck in an Automatic Repair Loop on an HP Laptop? Fix It Here

Few things are as disheartening as watching your HP laptop say "Preparing Automatic Repair," spin for a while, and then... do it all over again. And again. This is the Automatic Repair loop: Windows can't boot, its self-repair can't fix whatever's wrong, and the machine just cycles forever. Take a breath — your files are almost certainly fine. This is a boot problem, not a data problem.

HP laptops give you good recovery tools for exactly this situation, including the F11 recovery key and solid built-in diagnostics. This guide walks you through breaking the loop step by step, from the easy automated fixes to manually rebuilding the boot files. If you'd rather follow the brand-neutral version, see our [step-by-step Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/).

## Why this happens

- **Boot configuration data (BCD) is corrupted.** The BCD tells Windows where and how to start; if it's damaged, every boot attempt fails identically.
- **A Windows update broke the boot chain.** Updates that touch boot files can leave the system unbootable if interrupted or buggy.
- **System files are corrupted.** Damage to core Windows files means the OS can't finish loading, triggering repair on every attempt.
- **The drive is failing.** Bad sectors in critical boot areas cause identical failures on every boot — and every repair attempt.
- **Fast Startup wrote a bad hibernation state.** A corrupted hibernated kernel can wedge the boot process in a repeatable way.
- **Recent driver or software install.** A bad low-level driver (disk filters, encryption) installed just before the loop began can block startup.

## How to fix it

Work through these in order from the Recovery environment. To get there on an HP: force two interrupted boots, or press **F11** during startup.

### Fix 1: Run Startup Repair properly

Give the automated tool one clean shot before going manual.

1. On the Recovery screen, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation and your account, enter your password, and let it run — give it up to 15 minutes.
3. If it reports it couldn't repair your PC, click **Advanced options** to return to the menu (don't choose Turn off PC yet).
4. One failed Startup Repair is normal — it just means you need the manual fixes below.

### Fix 2: Boot into Safe Mode to break the cycle

If Windows can start in Safe Mode, you can fix the problem from inside.

1. Go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
2. Press **4** for Safe Mode. If Windows loads, the core system is intact and something loading at normal boot is the problem.
3. In Safe Mode, open **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update.
4. Also open **Device Manager** and roll back any driver updated just before the loop began. Our Safe Mode primer at [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) covers getting back out cleanly.

### Fix 3: Rebuild the boot files with bootrec

Corrupted BCD is the most common cause, and these commands rebuild it.

1. Go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands one at a time, pressing Enter after each:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   (If `fixboot` gives "Access is denied," continue anyway — the next commands handle it.)
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If prompted to add installations to the boot list, type `Y` and press Enter.
4. Type `exit`, choose **Continue**, and see if Windows boots.

### Fix 4: Repair the EFI bootloader manually

When bootrec isn't enough, rebuild the EFI partition's boot files directly.

1. In the Recovery **Command Prompt**, run `diskpart`, then `list vol` to find the EFI partition (FAT32, usually around 100MB, labeled EFI or with no label).
2. Select it: `sel vol X` (replace X with its number), then `assign letter=Z:` and `exit` diskpart.
3. Run:
   `bcdboot C:\Windows /s Z: /f UEFI`
   (Use the correct Windows drive letter — in WinRE it's often D:; check with `dir C:` first.)
4. Type `exit` and choose **Continue** to reboot.

### Fix 5: Uninstall the latest Windows update

Updates are a leading cause of sudden boot loops.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first, reboot, and test.
3. If the loop persists, return and choose **Uninstall the latest feature update**.
4. Once booted, pause updates via **Settings > Windows Update > Pause updates** for a few weeks. If you need fresh installation media later, the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) has it.

### Fix 6: Run System Restore from Recovery

If a restore point exists from before the loop, this is the gentlest full fix.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Pick the most recent restore point dated before the loop started.
3. Let it complete — the laptop will reboot when done. Your personal files are not affected by System Restore.
4. If no restore points exist, enable System Protection afterward (**System Properties > System Protection**) so you have this safety net next time.

### Fix 7: Check the drive with HP diagnostics and chkdsk

Rule out a failing drive before considering a reset.

1. Restart and press **F2** (or **Esc** then **F2**) during the HP logo to open **HP PC Hardware Diagnostics**.
2. Run the **Hard Drive** / storage tests. Note any failure codes.
3. Back in Recovery's **Command Prompt**, also run `chkdsk C: /f /r` (correct drive letter as needed) to fix file-system errors.
4. If diagnostics report drive failure, back up via a live USB or remove the drive for data recovery, then replace it — no software fix will save a dying drive. HP's own [support site](https://support.hp.com/us-en) can help with warranty checks using your serial number.

### Fix 8: Reset Windows as a last resort

When nothing else breaks the loop, a reset reinstalls Windows while optionally keeping files.

1. Go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files** first — this reinstalls Windows but preserves your personal data (you'll need to reinstall apps).
3. Only choose **Remove everything** if the keep-files reset also fails.
4. After the reset completes, immediately check **Settings > Windows Update** and install all updates cleanly.

## Closing

The Automatic Repair loop looks hopeless because it repeats, but repetition is actually a clue: the same thing fails the same way every boot, which means one specific thing is broken — usually the boot files or a recent update. Rebuild the boot configuration, evict the bad update, and your HP laptop will break the cycle and boot like nothing happened.
