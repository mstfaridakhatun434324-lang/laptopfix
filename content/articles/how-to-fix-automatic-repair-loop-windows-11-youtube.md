---
title: "How to Fix the Automatic Repair Loop on Windows 11"
slug: how-to-fix-automatic-repair-loop-windows-11-youtube
date: 2026-09-06
categories: ["windows-errors"]
tags: ["repair loop", "boot failure", "windows 11"]
description: "Stuck in the Windows 11 Automatic Repair loop? \"Preparing Automatic Repair\" forever? Here's how to break the loop and boot again."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11-youtube.webp"
faqs:
  - q: "What causes the Automatic Repair loop on Windows 11?"
    a: "Windows fails to boot three times, triggers Automatic Repair, the repair fails, and the cycle repeats. Common triggers: corrupt boot files (BCD), a bad Windows update, the srttrail.txt error, failing storage, or a recent driver change that breaks startup."
  - q: "Will I lose my files fixing the repair loop?"
    a: "The repair steps themselves — rebuilding the BCD, running SFC, uninstalling updates — don't delete personal files. Only a clean install or reset would. Back up from the recovery command prompt first if you're worried, before trying anything drastic."
  - q: "What is the srttrail.txt error in the repair loop?"
    a: "It's the log file Automatic Repair writes when it fails: C:\\Windows\\System32\\Logfiles\\Srt\\SrtTrail.txt. The loop screen sometimes references it. It confirms the repair failed but rarely names the cause — the fixes below address the actual underlying problems."
  - q: "How long should Automatic Repair take before I assume it's looping?"
    a: "A genuine repair usually finishes within 15-30 minutes. If it's been over an hour, or it returns to the same blue 'Automatic Repair' screen after rebooting, you're in the loop and should intervene with the steps below."
---

The Automatic Repair loop is one of the most stressful Windows failures: your laptop shows "Preparing Automatic Repair," then "Diagnosing your PC," then fails — and after rebooting, does it all again. You're locked out of Windows entirely, staring at a blue screen with options that don't seem to help.

The way out is the **Advanced options** menu hiding behind that blue screen. Every fix below runs from there — no Windows installation required to start. Work through them in order.

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: The BCD store tells Windows how to boot. If it's damaged, every boot attempt fails identically.
- **Failed Windows update**: A half-applied cumulative or feature update leaves boot files in an inconsistent state.
- **Corrupt system files in the boot path**: Damage to winload.efi, ntoskrnl.exe, or early-boot drivers stops startup cold.
- **Failing storage drive**: Bad sectors in the boot partition cause intermittent boot failures that trigger the repair cycle.
- **Recent driver or software change**: A bad storage controller or filter driver installed just before the loop began.
- **Disk partition or boot mode mismatch**: BIOS/UEFI boot mode changed (Legacy vs UEFI), or the EFI partition damaged, so the bootloader can't find Windows.

## How to fix it

Work through these in order — each step runs from the recovery environment.

### Fix 1: Break the loop and reach Advanced options

First, stop the cycle and get to the tools.

1. On the blue **Automatic Repair** screen, click **Advanced options** (not Restart — Restart just loops again).
2. If you only see "Preparing Automatic Repair" forever, force it: hold the power button to shut down during the spinner, twice. On the third boot, Windows should offer the recovery screen.
3. From **Advanced options**, you have **Troubleshoot** > **Advanced options** with **Command Prompt**, **Startup Repair**, **System Restore**, and more — the fixes below live here.
4. If the laptop can't even reach this screen, create Windows 11 installation media on another PC ([Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11)), boot from the USB, choose your language, and click **Repair your computer**.

### Fix 2: Run Startup Repair properly

The automatic attempt failed, but a manual run sometimes succeeds — especially after you've tried nothing else yet.

1. Go to **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Select your Windows installation and let it run to completion (give it up to 30 minutes).
3. If it reports it couldn't repair, check the log it mentions: from **Command Prompt**, type `notepad C:\Windows\System32\Logfiles\Srt\SrtTrail.txt` to read what failed.
4. Move on — Startup Repair fixing it here is a bonus, not the plan. Our [srttrail.txt error guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-after-windows-11-update/) goes deeper on this specific log.

### Fix 3: Rebuild the Boot Configuration Data

Corrupt BCD is the top fixable cause. Rebuild it from the command prompt.

1. Open **Command Prompt** from **Troubleshoot** > **Advanced options**.
2. Run these commands one at a time:
   `bootrec /fixmbr`
   `bootrec /fixboot` (if "Access denied," see step 4)
   `bootrec /rebuildbcd`
3. If `rebuildbcd` finds your Windows installation, type `Y` to add it, then restart with `wpeutil reboot`.
4. If `fixboot` gives "Access denied," run:
   `diskpart`, then `list vol`, find the FAT32 EFI partition, `sel vol <number>`, `assign letter=Z:`, `exit`, then `bcdboot C:\Windows /s Z: /f UEFI`.
5. Restart and see if Windows boots. This resolves a large share of repair loops.

### Fix 4: Uninstall the latest Windows update

If the loop started right after an update, remove it from the recovery environment.

1. Go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Try **Uninstall latest quality update** first, then restart and test.
3. If that doesn't help, go back and try **Uninstall latest feature update**.
4. Once booted, pause updates (**Settings** > **Windows Update** > **Pause updates**) for a week and check our [blue screen after Windows 11 update guide](/articles/blue-screen-after-windows-11-update-troubleshooting/) before reinstalling the update.

### Fix 5: Run offline SFC and DISM

Repair corrupted system files without booting Windows.

1. Open **Command Prompt** from Advanced options.
2. Find your Windows drive letter — in recovery it may not be C:. Run `diskpart`, `list vol`, `exit`, then check with `dir D:\` etc. until you find the Windows folder.
3. Run offline SFC: `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows` (replace X: with the correct letter).
4. Then run DISM offline: `DISM /Image:X:\ /Cleanup-Image /RestoreHealth`.
5. Restart with `wpeutil reboot` and test.

### Fix 6: Check the drive for failure

If boot files keep corrupting, the drive itself may be dying.

1. In the recovery **Command Prompt**, run `chkdsk C: /f /r` (use the correct drive letter from Fix 5).
2. Let it complete — on large drives this takes an hour or more. Look for "bad sectors" in the summary.
3. If chkdsk finds many bad sectors, or the manufacturer's diagnostics report failure, back up immediately: from the command prompt, use `xcopy` or `robocopy` to copy your user folder to an external drive, e.g. `robocopy C:\Users\YourName E:\Backup /E`.
4. A failing drive means replacement — no software fix will hold. Laptop maker diagnostics: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).

### Fix 7: System Restore or reset as final options

If the BCD rebuild and file repairs didn't work, roll the system back.

1. Go to **Troubleshoot** > **Advanced options** > **System Restore** and pick a restore point from before the loop began.
2. If no restore points exist, use **Troubleshoot** > **Reset this PC** > **Keep my files** — this reinstalls Windows while preserving personal files (you'll reinstall apps).
3. Only as an absolute last resort: **Remove everything** for a clean install.
4. After recovering, disable the conditions that caused it: keep BIOS and storage drivers current, and don't interrupt Windows updates mid-install.

Related loop scenarios: [automatic repair loop on Lenovo laptops](/articles/how-to-fix-automatic-repair-loop-windows-11-on-lenovo-laptop/) and our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) if you need to reach Safe Mode once booting works.

## Closing

The Automatic Repair loop feels like a dead end, but it's almost always a boot configuration or update problem — both fixable from the recovery command prompt without losing files. Rebuild the BCD, uninstall the offending update, repair system files offline, and check the drive. Work the list patiently; the loop breaks as soon as the underlying boot fault is repaired.
