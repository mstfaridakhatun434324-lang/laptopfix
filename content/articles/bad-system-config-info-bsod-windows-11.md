---
title: "BAD_SYSTEM_CONFIG_INFO BSOD in Windows 11: Boot Repair Walkthrough"
slug: bad-system-config-info-bsod-windows-11
date: 2026-09-12
categories: ["windows-errors"]
tags: ["bad system config info", "bsod windows 11", "boot repair", "bcd", "winre"]
description: "BAD_SYSTEM_CONFIG_INFO BSOD in Windows 11? Walk through boot repair from WinRE: Startup Repair, BCD rebuild, registry restore, and disk fixes."
thumbnail: "/images/thumbs/bad-system-config-info-bsod-windows-11.webp"
faqs:
  - q: "Can I fix BAD_SYSTEM_CONFIG_INFO without installation media?"
    a: "Usually yes. Windows 11 includes the Recovery Environment on the hard drive — trigger it by interrupting the boot three times in a row, and you get Startup Repair, Command Prompt, and System Restore without any USB stick. You only need installation media if WinRE itself is damaged or missing."
  - q: "How long does a BCD rebuild take?"
    a: "The commands themselves take under five minutes. What takes time is getting into the Recovery Environment and identifying the correct drive letter, since WinRE often assigns different letters than normal Windows. Budget 20–30 minutes total for a careful first attempt."
  - q: "What if my drive letter is different in Recovery Environment?"
    a: "That is normal — WinRE enumerates drives differently. Always run diskpart, then list volume, to identify which letter holds your Windows folder before running bootrec, chkdsk, or offline SFC. Running repairs against the wrong volume is the most common self-inflicted complication."
  - q: "Should I try Safe Mode for BAD_SYSTEM_CONFIG_INFO?"
    a: "Safe Mode rarely helps here because the failure happens before Windows loads far enough for Safe Mode to matter — the BCD or registry damage blocks even minimal boot. Go straight to the Recovery Environment tools instead; they operate outside the broken boot path."
---

When Windows 11 greets you with BAD_SYSTEM_CONFIG_INFO (stop code 0x74) instead of a login screen, the operating system is failing at its earliest job: assembling the configuration it needs to start. The Boot Configuration Data store and the system registry hives are the two structures involved, and damage to either produces the same symptom — a blue screen during boot, then usually the Recovery Environment. Your files are almost certainly fine; it's the boot metadata that's broken.

This walkthrough is the Windows 11 edition of the repair: every step runs from the Recovery Environment (WinRE), ordered from automatic to manual, with the drive-letter gotcha that trips up first-timers called out explicitly. For the general troubleshooting reference, see [BAD_SYSTEM_CONFIG_INFO troubleshooting](/articles/bad-system-config-info-troubleshooting/).

## Why this happens

- **Corrupted BCD store.** The loader's configuration is damaged — the leading cause of 0x74 on Windows 11.
- **Damaged SYSTEM registry hive.** Boot-time registry reads fail, halting configuration assembly.
- **Interrupted Windows 11 updates.** Feature updates rewriting boot files when power or patience runs out mid-process.
- **Disk errors in the EFI/boot partitions.** Bad sectors corrupting the small partitions Windows 11 boots from.
- **Partition layout changes.** Cloning, resizing, or third-party partition tools desyncing the BCD.
- **Failed storage or encryption drivers.** Boot-start drivers installed badly, breaking the early boot chain.
- **Registry "cleaner" damage.** Aggressive utilities deleting or corrupting hive data.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enter WinRE and run Startup Repair

Start where Windows 11 wants you to start.

1. If the laptop boots to WinRE automatically, choose **Troubleshoot > Advanced options > Startup Repair**.
2. If not, force it: power on, and the moment the Windows logo appears, hold the power button to force off. Repeat three times.
3. Alternatively, boot from Windows 11 installation media and click **Repair your computer**.
4. Select your Windows 11 installation and let Startup Repair run (10–20 minutes).
5. If it reports failure, note the log path — then continue; manual repair succeeds where this often doesn't.

### Fix 2: Identify your drive letter, then rebuild the BCD

The step everyone rushes — don't.

1. In WinRE: **Troubleshoot > Advanced options > Command Prompt**.
2. Run `diskpart`, then `list volume`, then `exit`. Note which letter holds your Windows folder — commonly D: or E: in WinRE, not C:.
3. Run `bootrec /scanos` to confirm your installation is detected.
4. Run `bootrec /fixmbr` and `bootrec /fixboot` (continue past any "Access is denied" on UEFI).
5. Run `bootrec /rebuildbcd`, answer **Y**, then `exit` and restart.
6. If rebuildbcd finds no installations: `bcdedit /export C:\BCD_Backup`, `attrib c:\boot\bcd -h -r -s`, `ren c:\boot\bcd bcd.old`, `bootrec /rebuildbcd`.

The post-update edition of this repair is detailed in [how to fix BAD_SYSTEM_CONFIG_INFO after a Windows 11 update](/articles/how-to-fix-bad-system-config-info-after-windows-11-update/).

### Fix 3: Restore the registry from a restore point

System Restore carries full registry snapshots.

1. In WinRE: **Troubleshoot > Advanced options > System Restore**.
2. Choose a point dated before the boot failures.
3. Complete the restore and restart — files preserved, system state rolled back.
4. After booting, verify **System Protection** is enabled for future incidents.
5. If no restore points exist, the manual hive restore (RegBack) is the fallback — though on Windows 11 it's usually empty by default.

### Fix 4: Run offline CHKDSK and SFC with the right letters

Repair the filesystem using the WinRE drive mapping.

1. From the WinRE Command Prompt, run `chkdsk D: /f /r` — substituting your actual Windows letter from Fix 2.
2. Let the full scan complete; bad sectors in boot partitions explain recurring 0x74.
3. Run offline SFC: `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` (again, your letter).
4. Re-run the BCD rebuild (Fix 2) after repairs — clean filesystem first, then clean boot data.
5. Repeated new bad sectors mean a failing drive: clone it before it gets worse.

Safe Mode is a useful diagnostic for many boot-adjacent problems — see [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) for every method.

### Fix 5: Check the EFI partition

Windows 11's UEFI boot depends on a healthy EFI system partition.

1. From the WinRE Command Prompt: `diskpart` > `list disk` > `select disk 0` > `list partition` — identify the EFI partition (usually ~100–260 MB, FAT32).
2. Assign it a letter: `select partition N` > `assign letter=Z:` > `exit`.
3. Run `bcdboot D:\Windows /s Z: /f UEFI` (your Windows letter) to rebuild the EFI boot files.
4. Remove the temporary letter: `diskpart` > `select partition N` > `remove letter=Z:` > `exit`.
5. Restart — this fixes 0x74 cases where the EFI boot files (not just the BCD) were damaged.

### Fix 6: Uninstall the last update

If the timeline points at an update, remove it.

1. In WinRE: **Troubleshoot > Advanced options > Uninstall Updates**.
2. Remove the **latest quality update** first; test booting.
3. Then the **latest feature update** if needed (slower, but thorough).
4. Once booted, pause updates for a week in **Settings > Windows Update**.
5. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) later for a fixed revision of the KB.

### Fix 7: Reset with file preservation

When boot metadata resists all repair.

1. In WinRE: **Troubleshoot > Reset this PC > Keep my files**.
2. Prefer **Cloud download** for clean source files.
3. Back up anything critical via Command Prompt first if you have doubts.
4. After the reset, install drivers only from the manufacturer's support page.
5. Enable System Protection and make a restore point before reinstalling applications.

## Closing

The Windows 11 BAD_SYSTEM_CONFIG_INFO repair is a WinRE workflow, and the discipline that makes it work is small: identify the real drive letter before running anything, rebuild the BCD before touching the registry, and repair the filesystem before rebuilding the BCD a second time. Most cases resolve by Fix 2 — a careful BCD rebuild with the right volume letters. The failures that need more are usually telling you about disk damage underneath, so don't skip the CHKDSK step even when the BCD rebuild seems to work. Fix the metadata, verify the disk, set up System Protection, and stop code 0x74 becomes a solved problem instead of a recurring nightmare.
