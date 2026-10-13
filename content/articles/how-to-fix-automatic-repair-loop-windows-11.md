---
title: "Windows 11 Stuck in an Automatic Repair Loop? Here's the Fix"
slug: how-to-fix-automatic-repair-loop-windows-11
date: 2026-09-12
categories: ["windows-errors"]
tags: ["automatic repair", "repair loop", "boot failure", "srttrail", "windows 11"]
description: "Windows 11 keeps saying 'Preparing Automatic Repair' and never boots? Break the loop in 8 steps, from quick fixes to full recovery."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11.webp"
faqs:
  - q: "What is the Automatic Repair loop?"
    a: "It's when Windows fails to boot, launches Automatic Repair to fix itself, fails at that too, and reboots — repeating forever. The trigger is usually corrupted boot files, a bad update, or disk errors. Your files are typically still intact on the drive."
  - q: "Will I lose my files fixing this?"
    a: "The repair steps themselves don't delete files. Only a clean reinstall or reset without the 'keep my files' option removes data. Back up first anyway using the Command Prompt in the recovery environment if your files matter."
  - q: "What is the SrtTrail.txt error?"
    a: "SrtTrail.txt is the log file Automatic Repair writes when it fails. Seeing a message about it just means the automated repair couldn't fix the boot problem — it doesn't tell you the cause. Our [SrtTrail.txt blue screen guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-in-windows-11-24h2/) digs into that specific log."
  - q: "How do I stop Automatic Repair from running?"
    a: "From the recovery Command Prompt, run bcdedit /set {default} recoveryenabled No. This stops the loop so you can boot (or see the real error). Only do this after attempting repairs — disabling recovery without fixing the cause just changes how the failure looks."
---

The Automatic Repair loop is Windows trying to be helpful and failing at it: something prevents booting, the repair tool runs, it can't fix the problem, the laptop reboots, and the whole cycle repeats. It's alarming, but your files are usually untouched — this is a boot plumbing problem, not a dead drive.

Every fix below runs from the blue **Advanced options** screen that the loop eventually shows you (or that you reach by interrupting startup three times).

## Why this happens

- **Corrupted Boot Configuration Data (BCD).** The bootloader's instructions are damaged, so Windows can't find itself.
- **Failed or interrupted Windows update.** A half-applied update leaves boot files in an inconsistent state.
- **Disk errors on the system partition.** Bad sectors in critical boot areas defeat both booting and repair.
- **Corrupted system files.** Damage to core Windows files that the automated repair can't replace on its own.
- **New hardware or BIOS changes.** Storage mode switches or new drives confuse the boot sequence.
- **Malware damage to the boot sector.** Less common now, but boot-sector infections still cause this on unprotected systems.

## How to fix it

Work through these in order — start with Fix 1 and stop when Windows boots.

### Fix 1: Break the loop and boot into Safe Mode

First, get control back.

1. On the **Automatic Repair** screen, click **Advanced options > Troubleshoot > Advanced options > Startup Settings > Restart**.
2. Press **4** for Safe Mode (or **5** for Safe Mode with Networking).
3. If Windows boots in Safe Mode, the core system is intact — a driver or startup program is likely the trigger.
4. In Safe Mode, open **Device Manager** and roll back any recently updated driver, then restart normally.
5. If Safe Mode also fails, continue with the repair steps below.

### Fix 2: Run Startup Repair properly once

Give the automated tool one clean shot before going manual.

1. Go to **Troubleshoot > Advanced options > Startup Repair**.
2. Let it run to completion without interrupting — it can take 15+ minutes.
3. If it reports it couldn't repair, click **Advanced options** (not Shut down) to stay in the recovery environment.
4. Note any log file mentioned (often `SrtTrail.txt`) — it confirms the automated path is exhausted.
5. Move on to manual boot repair.

### Fix 3: Rebuild the BCD and boot records

This fixes the majority of repair loops.

1. Open **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands in order:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `fixboot` returns "Access denied," run these instead:
   `diskpart`, then `list volume`, note the EFI partition, `select volume N`, `assign letter=Z:`, `exit`, then `bcdboot C:\Windows /s Z: /f UEFI`.
4. Type `exit` and choose **Continue** to restart.
5. If Windows boots, immediately run Windows Update and a full `sfc /scannow` to stabilize things.

### Fix 4: Run CHKDSK on the system drive

Disk errors defeat both booting and repair — fix the disk first.

1. In the recovery **Command Prompt**, identify your Windows drive letter with `diskpart` > `list volume` > `exit` (it's often D: or E: in WinRE).
2. Run `chkdsk D: /f /r` (using the correct letter) and let it finish — this can take over an hour on large drives.
3. If it finds and repairs many bad sectors, the drive may be failing — plan a replacement even if Windows boots.
4. After CHKDSK, run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows`.
5. Restart and test. Brand-specific variants of this loop are covered for [Lenovo](/articles/how-to-fix-automatic-repair-loop-windows-11-on-lenovo-laptop/), [ASUS](/articles/how-to-fix-automatic-repair-loop-windows-11-on-asus-laptop/), and [Dell](/articles/how-to-fix-automatic-repair-loop-windows-11-on-dell-laptop/) laptops.

### Fix 5: Uninstall the latest update

If the loop started after an update, remove it.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Try **Uninstall latest quality update** first, then restart.
3. If the loop persists, return and **Uninstall latest feature update**.
4. Once booted, pause updates for a couple of weeks via **Settings > Windows Update**.
5. Update your storage and chipset drivers from the manufacturer's support page before unpausing.

### Fix 6: Disable Automatic Repair and early-launch anti-malware

Stop the loop mechanism to see the real error underneath.

1. In the recovery **Command Prompt**, run `bcdedit /set {default} recoveryenabled No`.
2. Also try disabling early-launch protection: `bcdedit /set {default} disableelamdrivers yes`.
3. Restart — Windows will now either boot or show the actual blue screen error instead of looping.
4. If a specific stop code appears, troubleshoot that directly (for example, [INACCESSIBLE_BOOT_DEVICE](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/) has its own fix path).
5. Re-enable recovery later with `bcdedit /set {default} recoveryenabled Yes` once stable.

### Fix 7: System Restore from the recovery environment

Roll back to before the problem started.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Pick a restore point dated before the loop began.
3. Let it complete — this affects system files and settings, not your personal files.
4. Restart and test the boot.
5. If no restore points exist, enable System Protection afterward (**System Properties > System Protection**) so you have this safety net next time.

### Fix 8: Reset or clean-install Windows

The last resort when boot damage is beyond repair.

1. First, back up files: in the recovery **Command Prompt**, use `robocopy D:\Users\YourName E:\Backup /E` (adjust letters) to copy data to a USB drive.
2. Go to **Troubleshoot > Reset this PC** and try **Keep my files** first.
3. If the reset fails, do a clean install from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) created on another PC.
4. During setup, delete the old system partitions only if you're sure backups are complete.
5. After installing, get drivers from the manufacturer before letting Windows Update run wild — guidance is on Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

The Automatic Repair loop looks like a dead laptop, but it's usually a fixable boot-record or disk problem — Fixes 3 and 4 resolve most cases with files intact. The key discipline is working in order and backing up before the destructive steps. Once you're booting again, turn on System Protection and keep a recovery USB handy; the next loop (if there ever is one) will be a ten-minute fix instead of a panic.
