---
title: "How to Troubleshoot the Automatic Repair Loop on Windows 11"
slug: troubleshoot-automatic-repair-loop-windows-11
date: 2026-10-07
categories: ["windows-errors"]
tags: ["automatic-repair", "boot-loop", "recovery"]
description: "Stuck in the Windows 11 Automatic Repair loop? Break out of it: disable auto-repair, fix boot files with bootrec, check the drive, and restore booting."
thumbnail: "/images/thumbs/troubleshoot-automatic-repair-loop-windows-11.webp"
faqs:
  - q: "What is the Automatic Repair loop?"
    a: "It's when Windows fails to boot, launches Automatic Repair to fix itself, fails to fix the problem, and reboots — only to fail again, forever. You'll see 'Preparing Automatic Repair' then 'Diagnosing your PC' on every boot, sometimes with a SrtTrail.txt log reference. The repair tool can't fix the underlying cause on its own."
  - q: "Will I lose my files in the Automatic Repair loop?"
    a: "Your files are almost certainly still on the drive — the loop is a boot problem, not a data problem. Every fix here preserves your data. Only a clean reinstall would touch personal files, and that's the last resort. If you're worried, back up from the recovery Command Prompt before repairing."
  - q: "What is SrtTrail.txt?"
    a: "It's the log file Automatic Repair writes when it fails, stored at C:\\Windows\\System32\\LogFiles\\Srt\\SrtTrail.txt. It sometimes names the failing component — a corrupt boot file, a bad driver, or a disk error — which tells you which fix to prioritize. You can read it from the recovery Command Prompt with Notepad."
  - q: "How long should I let Automatic Repair run?"
    a: "One full attempt — if it returns to the same 'Automatic Repair couldn't repair your PC' screen, don't keep retrying it. Repeated attempts don't fix new things; they just waste time. Move on to the manual fixes below, starting with disabling the loop itself."
---
The Automatic Repair loop is Windows trying to help and failing in a circle: boot fails, repair runs, repair can't fix it, reboot, boot fails again. You'll see "Preparing Automatic Repair," then "Diagnosing your PC," then the blue recovery screen — every single time. The way out isn't running the repair again; it's taking manual control.

The loop has a handful of usual causes: corrupted boot files, a bad driver or update, a damaged registry, or a failing drive. The fixes below go from breaking the loop open to repairing each cause. Your files are safe throughout — this is a boot problem, not a data problem.

## Why this happens

- **Corrupted Boot Configuration Data (BCD)** — the bootloader's instructions are damaged.
- **Damaged system files** critical to startup, often from an interrupted update.
- **A bad driver or Windows update** that breaks the boot process.
- **Corrupted registry hives** preventing Windows from loading its configuration.
- **Failing SSD/HDD** with bad sectors in the boot or system areas.
- **Incorrect BIOS settings** (SATA mode changed from AHCI to RAID, or vice versa) after a BIOS update or reset.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Break the loop — boot to Advanced options

First, stop the cycle so you can work.

1. On the **Automatic Repair** screen, click **Advanced options** instead of Restart.
2. Go to **Troubleshoot** → **Advanced options** — this is your workshop for everything below.
3. If the laptop reboots into the loop before you can click, force it: hold the power button during "Preparing Automatic Repair" to interrupt, and on the next boot you should land on the recovery screen directly.
4. From here, don't choose "Continue" or "Turn off your PC" yet — head to **Command Prompt** first.

### Fix 2: Disable Automatic Repair temporarily

This stops the loop from hijacking every boot while you repair.

1. In **Troubleshoot** → **Advanced options** → **Command Prompt**, run:
   `bcdedit /set {default} recoveryenabled No`
2. Type `exit` and choose **Continue**. Windows will now show the actual error (blue screen or boot error) instead of looping.
3. Note the error — a stop code or "INACCESSIBLE_BOOT_DEVICE" tells you where to focus.
4. You can re-enable it later with `bcdedit /set {default} recoveryenabled Yes` once booting is fixed.

### Fix 3: Rebuild the boot files with bootrec

Corrupted boot files are the most common cause, and these commands rebuild them.

1. Back in the recovery **Command Prompt**, run these in order:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   (If fixboot gives "Access is denied," use the bcdboot method in step 3.)
   `bootrec /scanos`
   `bootrec /rebuildbcd`
2. If prompted to add installations to the boot list, type **Y** for each.
3. For the "Access is denied" case, run instead:
   `bcdboot C:\Windows /s C: /f UEFI`
   (Adjust drive letters to match your Windows partition as seen from recovery.)
4. Type `exit`, choose **Continue**, and test the boot.

For the SrtTrail-specific variant of this loop, our [SrtTrail.txt error guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-after-windows-11-update/) covers reading the log to target the exact failing file.

### Fix 4: Run Startup Repair manually (once, properly)

The automatic version failed, but a manual run after bootrec sometimes succeeds.

1. Go to **Troubleshoot** → **Advanced options** → **Startup Repair**.
2. Let it run exactly once. If it fails, don't repeat it — move on.
3. If it reports it can't fix the PC, click **Advanced options** and continue with Fix 5.
4. Check the log afterward at `C:\Windows\System32\LogFiles\Srt\SrtTrail.txt` via Command Prompt + Notepad for the named cause.

### Fix 5: Uninstall the breaking update or driver

If the loop started after Patch Tuesday or a driver update, remove the trigger.

1. Go to **Troubleshoot** → **Advanced options** → **Uninstall Updates**.
2. Try **Uninstall latest quality update** first, then test booting.
3. If that doesn't work, try **Uninstall latest feature update**.
4. For driver-caused loops, boot into **Safe Mode** (via **Startup Settings**) and roll back the suspect driver in **Device Manager**.

### Fix 6: Check the drive and system files

Boot-area disk damage causes loops that bootrec can't fix alone.

1. In the recovery **Command Prompt**, run `chkdsk C: /f /r` (use the correct drive letter for Windows in recovery).
2. Then run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
3. Follow with `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. If chkdsk reports bad sectors in the boot area, the drive may be failing — check SMART data and plan a replacement.

### Fix 7: Restore the registry from backup

Windows keeps automatic registry backups that can undo corruption.

1. In the recovery **Command Prompt**, navigate to `C:\Windows\System32\config`.
2. Check for the **RegBack** folder: `dir C:\Windows\System32\config\RegBack`.
3. If it contains files with nonzero sizes, back up the current hives and copy the RegBack versions over them:
   `copy C:\Windows\System32\config\RegBack\* C:\Windows\System32\config\`
4. Confirm each overwrite, type `exit`, and boot. (On newer Windows 11 builds RegBack may be empty — if so, skip this fix.)

### Fix 8: System Restore, reset, or clean install

The escalation ladder when repairs fail.

1. Try **System Restore** (**Troubleshoot** → **Advanced options** → **System Restore**) and pick a restore point from before the loop started.
2. If no restore points exist, use **Reset this PC** → **Keep my files**.
3. If the reset fails, back up your data from the recovery Command Prompt (`notepad.exe` → File → Open gives you a file browser for copying to USB), then clean-install from [official Windows 11 media](https://www.microsoft.com/en-us/software-download/windows11).
4. After any successful boot, immediately check the drive's SMART health — loops caused by dying drives will return.

Our step-by-step [automatic repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) covers additional command-line repairs if the bootrec sequence above didn't resolve it.

## Closing

The Automatic Repair loop feels like a dead end because Windows keeps "fixing" the same unfixable thing. The way out is to stop letting it: break into Advanced options, rebuild the boot files manually, remove the triggering update, and check the drive. Most loops surrender to bootrec or an update uninstall. And if the drive turns out to be the cause, you've just caught a failing SSD before it took your data — which makes the loop almost worth it. Almost.
