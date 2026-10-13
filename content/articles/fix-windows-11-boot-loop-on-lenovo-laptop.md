---
title: "How to Fix a Windows 11 Boot Loop on a Lenovo Laptop"
slug: fix-windows-11-boot-loop-on-lenovo-laptop
date: 2026-09-04
categories: ["windows-errors"]
tags: ["boot loop", "Lenovo", "startup repair"]
description: "Lenovo laptop stuck restarting over and over on Windows 11? These Lenovo-specific and general fixes break the boot loop without losing your files."
thumbnail: "/images/thumbs/fix-windows-11-boot-loop-on-lenovo-laptop.webp"
faqs:
  - q: "Why is my Lenovo laptop stuck in a boot loop?"
    a: "The most common causes are a failed Windows update, corrupted boot files, a driver that crashes during startup, or Fast Startup preserving a broken system state. On Lenovo machines specifically, outdated BIOS firmware or Lenovo Vantage driver updates that conflict with a new Windows build can also trigger the loop. The fix depends on which of these is responsible, so work through the steps in order."
  - q: "Will fixing a boot loop delete my files?"
    a: "Not if you use the right tools. Startup Repair, Safe Mode, SFC scans, and uninstalling updates all preserve your personal files. Only a Reset with the remove-everything option or a clean install deletes data. As a precaution, if you can reach the recovery Command Prompt, back up critical files to a USB drive before attempting aggressive repairs."
  - q: "How do I get into recovery mode on a Lenovo laptop?"
    a: "Force-shut down the laptop three times in a row while the Lenovo logo is showing, and on the fourth boot Windows Recovery Environment should appear. Alternatively, Lenovo's Novo button — the small recessed button beside the power button on many models — boots directly into the Novo Button Menu, where you can choose System Recovery to reach the same recovery tools."
  - q: "Can a BIOS update fix a Windows 11 boot loop on Lenovo?"
    a: "Sometimes, yes — particularly on newer Lenovo models where the factory BIOS predates the installed Windows 11 build. Lenovo regularly ships BIOS updates that fix boot compatibility issues. You can update from within the BIOS using a USB drive, or via Lenovo Vantage once you can boot. Only update the BIOS after ruling out software causes, and never interrupt a BIOS flash."
---

A boot loop is maddening: the Lenovo logo appears, the spinner turns, the screen goes black, and the whole thing starts over — endlessly. You never reach the login screen, and every restart feels like the laptop is taunting you. On Lenovo laptops this usually traces back to a Windows update gone wrong, a corrupted boot file, or a driver that crashes the moment it loads.

The trick is getting into the Windows Recovery Environment (WinRE), because every real fix happens from there. Lenovo actually gives you two ways in: the standard triple-force-shutdown method, and the Novo button that most Lenovo laptops have. Once you are in, work the fixes below in order — most loops break by Fix 3.

## Why this happens

- **A failed or partial Windows update.** The update writes new boot files, the process gets interrupted, and the system can neither finish nor roll back.
- **Corrupted Boot Configuration Data (BCD).** The boot store tells Windows how to start; damage here means every boot attempt dies the same way.
- **A crashing startup driver.** Graphics or storage drivers that fail on load take the whole boot down with them.
- **Fast Startup preserving a broken state.** The hibernation-based fast boot can reload the same corrupted kernel state on every start.
- **Outdated Lenovo BIOS.** Older firmware on newer Windows 11 builds can cause boot incompatibilities Lenovo later patches.
- **Disk errors or a failing drive.** Corrupted boot files from bad sectors produce a loop that repairs cannot permanently fix.

## How to fix it

Work through these in order, testing a normal boot after each one.

### Fix 1: Break the loop and reach the recovery environment

You cannot fix anything until you can get into WinRE.

1. Power on the laptop and, the moment the **Lenovo logo** appears, hold the power button until it shuts off.
2. Repeat this **three times**. On the fourth power-on, you should see **Preparing Automatic Repair**, then **Choose an option**.
3. Alternative: with the laptop fully off, press the **Novo button** (small pinhole button next to the power button — use a paperclip) and select **System Recovery** from the Novo Button Menu.
4. If neither works, create Windows 11 installation media on another PC from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), boot from the USB, and click **Repair your computer**.

### Fix 2: Try Startup Repair first

The automatic repair handles common boot-file damage quickly.

1. In WinRE, click **Troubleshoot**, then **Advanced options**, then **Startup Repair**.
2. Select your user account and enter the password.
3. Let the repair run — it can take 5 to 15 minutes.
4. Click **Continue** to restart and see if the loop is broken.

### Fix 3: Boot into Safe Mode and remove the trigger

Safe Mode loads only essential drivers, which bypasses most driver-caused loops.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
2. Press **4** (or **F4**) for **Safe Mode**.
3. If Windows loads, open **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update.
4. Open **Device Manager** (`Win + X`), and roll back any driver updated just before the loop started — right-click the device, **Properties > Driver > Roll Back Driver**.
5. Uninstall any program installed right before the problem began via **Settings > Apps > Installed apps**.
6. Restart normally.

If you cannot reach Safe Mode at all, skip to Fix 4.

### Fix 4: Disable Fast Startup and automatic restart

Fast Startup can reload the same broken state every boot, and disabling automatic restart lets you actually see the error.

1. If you can reach Safe Mode, open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, uncheck **Turn on fast startup (recommended)**, and click **Save changes**.
3. From WinRE, go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **9** (or **F9**) to **Disable automatic restart after failure**.
4. Boot normally — if a blue screen appears instead of a loop, note the stop code and treat that error directly.

For persistent blue screens behind the loop, our guide to [disabling automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) explains how to capture the real error.

### Fix 5: Repair system files and rebuild the BCD

Corrupted boot files are a leading cause of unbreakable loops.

1. In WinRE, open **Command Prompt** from **Advanced options**.
2. Confirm your Windows drive letter with `diskpart`, then `list vol`, then `exit` (it is often D: or E: in WinRE, not C:).
3. Run `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` using the correct letter.
4. Then run `DISM /Image:D:\ /Cleanup-Image /RestoreHealth`.
5. Rebuild the boot data: `bootrec /fixmbr`, `bootrec /fixboot`, then `bootrec /rebuildbcd`.
6. Type `exit`, choose **Continue**, and test.

### Fix 6: Run Lenovo diagnostics and update the BIOS

Rule out hardware, then fix firmware-level boot issues.

1. Boot into the **Lenovo Diagnostics** (press **F10** during startup on most models, or use the Novo button menu).
2. Run the quick storage and memory tests. If the drive fails, replace it before doing anything else.
3. If hardware passes, check your BIOS version against the latest on [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model.
4. Update the BIOS using Lenovo's bootable update utility on a USB drive — keep the charger plugged in and do not touch the laptop during the flash.
5. After the update, load BIOS defaults (**F9** in most Lenovo BIOS setups), save, and boot.

### Fix 7: Reset Windows while keeping files

When repairs cannot break the loop, a reset reinstalls Windows cleanly.

1. In WinRE, choose **Troubleshoot > Reset this PC**.
2. Select **Keep my files**.
3. Choose **Cloud download** for the freshest files (needs internet) or **Local reinstall**.
4. Follow the prompts — the process takes 30 to 60 minutes.
5. Afterward, install drivers from [Lenovo Support](https://support.lenovo.com/us/en/) rather than relying solely on Windows Update.

A similar loop on a different brand follows the same principles — see our walkthrough for [Windows 11 boot loops on Acer laptops](/articles/how-to-fix-windows-11-boot-loop-on-acer-laptop/) for comparison.

## Closing

Boot loops on Lenovo laptops feel hopeless because you never get anywhere near your desktop, but the Novo button and the force-shutdown trick both get you into the recovery environment where the real tools live. Startup Repair, Safe Mode cleanup, and a BCD rebuild break the loop in the large majority of cases; Lenovo diagnostics and a BIOS update cover the rest. Keep your BIOS and drivers current through Lenovo Vantage going forward, and the odds of seeing this loop again drop sharply.
