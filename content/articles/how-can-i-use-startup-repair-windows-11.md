---
title: "How to Use Startup Repair on Windows 11: A Technician's Walkthrough"
slug: how-can-i-use-startup-repair-windows-11
date: 2026-09-16
categories: ["windows-errors"]
tags: ["startup repair", "windows 11", "winre", "boot problems", "recovery"]
description: "Startup Repair is Windows 11's built-in tool for fixing boot failures. Learn how to launch it from Settings or recovery media and what to do when it can't fix the problem."
thumbnail: "/images/thumbs/how-can-i-use-startup-repair-windows-11.webp"
faqs:
  - q: "Where is Startup Repair located in Windows 11?"
    a: "Startup Repair lives inside the Windows Recovery Environment (WinRE). Reach it via Settings > System > Recovery > Advanced startup > Restart now, then Troubleshoot > Advanced options > Startup Repair. If Windows won't boot at all, interrupt the boot process three times in a row to force WinRE, or boot from USB installation media."
  - q: "Will Startup Repair delete my personal files?"
    a: "No. Startup Repair only repairs boot-related data such as the Boot Configuration Data, master boot record, and damaged system files needed to start Windows. It does not touch your documents, photos, or installed programs. It is one of the safest repairs you can run, which is why technicians try it before anything more drastic."
  - q: "What should I do if Startup Repair says it couldn't repair my PC?"
    a: "That message is common and not a dead end. It simply means the automatic tool hit something beyond its abilities, such as a corrupt BCD store, a bad driver, or a failing drive. Move on to manual repairs: rebuild the BCD with bootrec commands, run offline SFC and chkdsk, or uninstall the latest Windows update from the recovery menu."
  - q: "How long does Startup Repair take to run?"
    a: "Most runs finish in five to twenty minutes. If it runs for over an hour with no progress, something is likely wrong — possibly a failing hard drive keeping the tool stuck. Force a shutdown, then boot into the recovery command prompt and run chkdsk to check the drive before trying Startup Repair again."
---

Few moments are more stressful than pressing the power button and watching Windows refuse to start. Before you assume the worst — a dead drive, a reinstall, lost data — reach for Startup Repair, the free recovery tool Microsoft builds into every copy of Windows 11. It exists for exactly this situation: Windows can't boot, and you need an automated first attempt at a fix.

Startup Repair lives inside the Windows Recovery Environment (WinRE), a small repair OS on a hidden partition of your drive. It scans your boot configuration, the master boot record, and core startup files, then attempts to patch whatever it finds broken. It won't fix everything — hardware failures and some update damage are beyond it — but it resolves a surprising share of boot problems in a few minutes, with zero risk to your files.

This guide walks you through launching Startup Repair three ways: from inside Windows (when it still boots), from the recovery environment (when it doesn't), and from USB installation media (when the recovery partition itself is damaged). You'll also learn what to do when Startup Repair reports that it couldn't fix your PC, because that message is a beginning, not an end. If your failed boots also show a blue screen, our [blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps you identify the underlying stop code in parallel.

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: The BCD store tells Windows where and how to start. When it gets damaged — by a failed update, a power cut during shutdown, or disk errors — every boot attempt fails.
- **Damaged master boot record (MBR) or boot sector**: On systems using legacy BIOS booting, a damaged MBR stops the boot chain before Windows even loads.
- **Missing or corrupt boot files**: Files like `winload.efi` can be quarantined by overzealous antivirus software or damaged by bad sectors.
- **A botched Windows update**: Updates rewrite boot components. If the process is interrupted, the system can be left in a half-updated, unbootable state.
- **Changed BIOS/UEFI settings**: A BIOS reset or update that flips the storage mode between RAID and AHCI, or disables UEFI boot, makes the existing installation unbootable.
- **Failing storage drive**: Bad sectors landing on boot-critical files produce consistent boot failures that repeat identically every attempt.
- **Newly installed incompatible driver**: A bad storage controller or chipset driver can break the boot sequence the very next restart.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Launch Startup Repair from Settings (Windows still boots)

If Windows boots but you're preparing for a recurring boot problem — or you're already in Windows after a scare — this is the easiest path.

1. Open **Settings** > **System** > **Recovery**.
2. Under **Recovery options**, click **Restart now** next to **Advanced startup**.
3. Your PC restarts into the blue **Choose an option** screen. Click **Troubleshoot** > **Advanced options** > **Startup Repair**.
4. Select your account, enter your password if asked, and let the tool run. Don't interrupt it.

### Fix 2: Launch Startup Repair when Windows won't boot

When Windows can't start, force the recovery environment yourself.

1. Press the power button to start the laptop, then hold the power button to force it off as soon as you see the manufacturer's logo or the spinning dots.
2. Repeat this **three times**. On the third or fourth boot, Windows should enter **Automatic Repair** mode and show the recovery screen.
3. Click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Repair**.
4. Choose your account and enter your password, then let it run to completion — usually five to twenty minutes.

### Fix 3: Run Startup Repair from USB installation media

If the recovery partition itself is damaged, the forced-boot method won't work. Boot from external media instead.

1. On a working PC, download the [Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) and create a Windows 11 USB installer.
2. Plug the USB into the broken laptop and boot from it (usually **F12**, **F9**, or **Esc** for the boot menu, depending on brand).
3. On the Windows Setup screen, click **Next**, then **Repair your computer** in the bottom-left corner — do not click Install.
4. Go to **Troubleshoot** > **Advanced options** > **Startup Repair** and follow the prompts.

### Fix 4: Read the log when Startup Repair fails

A failed repair still gives you diagnostic information. Don't just click through the failure screen.

1. After Startup Repair reports it couldn't repair your PC, click **Advanced options** instead of shutting down.
2. Open **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Type `notepad` and press Enter, then use **File** > **Open** to browse to `C:\Windows\System32\LogFiles\Srt\SrtTrail.txt` (the Windows drive may be D: in recovery — check with `dir`).
4. Read the log's "Root cause found" section. Common entries include "Boot configuration data store repair failed" (BCD damage — see Fix 5) and "A patch is preventing the system from starting" (a bad update — see Fix 7).

### Fix 5: Rebuild the BCD manually

When the log points at boot configuration damage, rebuild it yourself — this is the fix Startup Repair attempts but sometimes can't complete.

1. From the recovery **Command Prompt**, run these commands one at a time:
   - `bootrec /fixmbr`
   - `bootrec /fixboot` (if you get "Access is denied," do the manual EFI rebuild below instead)
   - `bootrec /scanos`
   - `bootrec /rebuildbcd`
2. If `rebuildbcd` finds zero installations, rebuild manually: run `diskpart`, then `list vol`, identify the FAT32 EFI partition, `select vol N`, `assign letter=Z:`, `exit`, then `bcdboot C:\Windows /s Z: /f UEFI` (verify the Windows drive letter first).
3. Type `exit`, choose **Continue**, and attempt a normal boot.

### Fix 6: Run offline SFC and disk checks

Corrupt system files or a damaged file system can defeat Startup Repair. Fix the underlying damage from the same command prompt.

1. In the recovery **Command Prompt**, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter to match your Windows drive in recovery).
2. When SFC finishes, run `chkdsk C: /f /r` and let the full scan complete — this can take a while on large drives.
3. Type `exit` and select **Continue**. If chkdsk reported many bad sectors, the drive itself may be failing — back up your data promptly even if the boot is fixed.

### Fix 7: Uninstall the latest update from recovery

If the boot failure began within a day of a Windows update, the update is the prime suspect — and Startup Repair rarely fixes update damage on its own.

1. From the recovery menu, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first, then restart and test.
3. If the problem persists, return and choose **Uninstall the latest feature update**.
4. Once Windows boots, open **Settings** > **Windows Update** and use **Pause updates** for a week or two, and check [Microsoft's support pages](https://support.microsoft.com/en-us/windows) for known issues with that update before allowing it again.

### Fix 8: Check BIOS settings and drive health

When every software repair fails, look at the firmware and hardware layer.

1. Enter your BIOS/UEFI setup (usually **F2** or **Del** during boot) and confirm the storage mode (AHCI vs RAID) matches what Windows was installed with, and that UEFI boot is enabled if your installation is UEFI-based.
2. Run your manufacturer's built-in diagnostics — **F12** > **Diagnostics** on Dell, **F2** system diagnostics on HP, Lenovo's bootable diagnostics — and run the full storage test.
3. If the drive fails diagnostics, replace it and reinstall Windows from the USB media you made in Fix 3. Your files can usually be recovered by connecting the old drive to another PC before it deteriorates further.

## Closing

Startup Repair is the right first move for any Windows 11 boot failure: it's free, built in, safe for your files, and fixes the most common boot problems in minutes. When it reports failure, don't read that as a verdict — read the SrtTrail log, rebuild the BCD, check the disk, and roll back the last update, in that order. Most "unrepairable" boots surrender to one of those manual steps. And if your failed boots keep looping back to the recovery screen instead of ever reaching Windows, our [automatic repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) picks up exactly where this one leaves off.
