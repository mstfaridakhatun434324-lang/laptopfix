---
title: "The Best Way to Fix a BSOD on Startup in Windows 11"
slug: best-way-to-fix-bsod-on-startup-windows-11
date: 2026-10-12
categories: ["windows-errors"]
tags: ["bsod on startup", "blue screen", "windows 11", "boot loop"]
description: "Blue screen every time Windows 11 starts? This ordered fix guide covers Safe Mode, Startup Repair, driver rollbacks, and System Restore."
thumbnail: "/images/thumbs/best-way-to-fix-bsod-on-startup-windows-11.webp"
faqs:
  - q: "Why does my laptop blue screen every time it starts Windows 11?"
    a: "Something that loads during startup is crashing the kernel — almost always a driver, a startup program's kernel component, or corrupted boot files. Because the crash happens before you reach the desktop, normal troubleshooting tools are out of reach, so you work through the Advanced Startup recovery environment instead. The fixes below are ordered to get you booting with minimal risk."
  - q: "How do I reach the recovery screen when Windows won't start?"
    a: "Hold the power button to force the laptop off while the Windows logo or spinning dots show, then power on again. Repeat this three times; on the third boot Windows loads Automatic Repair instead of crashing. If that fails, boot from a Windows 11 installation USB and click Repair your computer for the same menu."
  - q: "Is it safe to use System Restore for startup crashes?"
    a: "Yes — System Restore is one of the safest tools here because it only reverts system files, drivers, and registry settings to a previous point, leaving your personal files alone. Pick the most recent restore point from before the crashes started. It will uninstall programs added after that point, so make a note of anything you installed recently."
  - q: "What if Safe Mode also blue screens?"
    a: "That points to a deeper problem: corrupted core system files, a damaged boot configuration, or failing hardware. Move to Startup Repair, then SFC and DISM from the Command Prompt in the recovery environment, then a System Restore. If those all fail, test your RAM and SSD — hardware faults crash Safe Mode just as easily as normal boot."
---
A blue screen on startup is uniquely frustrating: you can't get into Windows to fix Windows. Every attempt to boot ends in the same crash and reboot loop. The key insight is that you're not actually locked out — Windows 11 ships a full recovery environment that's reachable even when the OS itself can't start, and it contains every tool you need.

This guide follows the order a repair tech uses: get into the recovery environment, try the automated fixes, then repair files, roll back the bad change, and only reset as a last resort. Don't skip steps — each one rules out a layer.

## Why this happens

- **A bad driver loads at boot.** Graphics, storage controller, and antivirus filter drivers load early; one bad update means a crash before the login screen.
- **Corrupted boot configuration data (BCD).** The BCD tells Windows where and how to start; disk errors or failed updates can damage it.
- **Damaged system files.** An interrupted update or hard shutdown can leave critical files half-written.
- **A startup program's kernel component.** Some security and disk utilities install drivers that load at boot and can crash the kernel.
- **Failing storage.** If the drive can't reliably serve the files Windows needs during boot, the startup sequence collapses.
- **Bad RAM.** Corrupted memory contents during the boot process produce crashes that look exactly like driver failures.

## How to fix it

Work through these in order. Each step assumes the previous ones didn't resolve it.

### Fix 1: Get into Advanced Startup and try Safe Mode

First, reach the recovery tools.

1. Force the laptop off during the Windows logo (hold power ~5 seconds), power on, and repeat until **Automatic Repair** appears — usually three interrupted boots.
2. Choose **Advanced options > Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4** for Safe Mode. If the desktop loads, the problem is a driver or startup item — proceed to Fix 2.
4. If Safe Mode also crashes, skip to Fix 3; your issue is deeper than a normal-mode driver.

### Fix 2: Remove the offending driver or program in Safe Mode

In Safe Mode, undo what broke the boot.

1. Open **Device Manager** and check for yellow warning icons, especially on the display adapter and network adapter.
2. Right-click suspects, choose **Properties > Driver**, and use **Roll Back Driver** if available.
3. Open **Settings > Apps > Installed apps**, sort by date, and uninstall anything installed just before the crashes — driver updaters and security suites first.
4. Restart normally. If Windows boots, update the rolled-back drivers from your laptop maker's official support site before doing anything else.

### Fix 3: Run Startup Repair

Let Windows attempt the automated boot fix.

1. From the **Advanced options** screen, choose **Troubleshoot > Advanced options > Startup Repair**.
2. Select your account, enter your password, and let it run — it can take several minutes and may restart the laptop.
3. If it says it couldn't repair your PC, that's useful information, not a dead end — continue below.
4. Don't run it repeatedly; one clean attempt is enough before moving on.

### Fix 4: Rebuild the boot configuration

If Startup Repair failed, repair the BCD manually from the Command Prompt.

1. From **Advanced options**, open **Command Prompt**.
2. Run these commands in order, pressing Enter after each:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `fixboot` reports access denied, run `bcdboot C:\Windows` instead to rebuild the boot files.
4. Type `exit`, choose **Continue**, and test the boot.

### Fix 5: Repair system files offline with SFC and DISM

Corrupted files can be repaired from the recovery environment.

1. Open **Command Prompt** from **Advanced options**.
2. Note: in the recovery environment your Windows drive may be D: instead of C:. Check with `diskpart` then `list volume` if unsure.
3. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter to match).
4. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`, adjusting the drive letter the same way.
5. Restart and test. File-level corruption that survived normal boot is often fixed here.

### Fix 6: Use System Restore

Roll the system back to before the crashes began.

1. From **Advanced options**, choose **System Restore**.
2. Pick the most recent restore point dated before the problem started.
3. Complete the wizard and let the laptop restart — this takes 10–20 minutes.
4. If Windows boots, immediately pause updates for a week under **Settings > Windows Update** so a bad update doesn't reinstall itself.

### Fix 7: Test hardware, then reset as a last resort

If nothing software-side works, suspect the hardware or do a clean reset.

1. Run your laptop maker's built-in diagnostics (usually **F12** or **F2** at the logo) to test RAM and storage.
2. From **Command Prompt** in recovery, run `chkdsk C: /f /r` to scan the drive.
3. If hardware passes, go to **Troubleshoot > Reset this PC > Keep my files > Cloud download** — this pulls a fresh Windows image from Microsoft.
4. After the reset, install drivers from your laptop maker's site first, then test stability before reinstalling old programs. For the classic "your PC ran into a problem" variant of this loop, the [dedicated troubleshooting guide](/articles/your-pc-ran-into-a-problem-troubleshooting/) covers reading the stop code behind the crash.

## Closing

Startup blue screens feel terminal but are almost always a driver, a boot file, or a recent change — all repairable from the recovery environment. The habit that saves the most time: when the laptop is healthy, create a manual restore point before every driver or major update. Two clicks today prevents a whole evening of recovery work later.

It's also worth keeping your BitLocker recovery key somewhere reachable from your phone — many recovery screens ask for it before running repairs, and hunting for it mid-crisis is miserable. Save it to your Microsoft account or print it and keep it with your laptop bag. Once you're booting cleanly again, add programs back gradually over a few days, so if the crash returns you'll know exactly which install brought it back. For blue screens that mention a specific stop code at startup, the [Srttrail.txt error guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-after-windows-11-update/) handles the most common variant.
