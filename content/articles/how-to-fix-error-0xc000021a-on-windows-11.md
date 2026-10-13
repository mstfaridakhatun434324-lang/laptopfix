---
title: "How to Fix Error 0xc000021a on Windows 11"
slug: how-to-fix-error-0xc000021a-on-windows-11
date: 2026-09-02
categories: ["windows-errors"]
tags: ["0xc000021a", "blue screen", "startup repair"]
description: "Error 0xc000021a stops Windows 11 from booting when a critical system process fails. Here are the proven fixes, from Startup Repair to a clean install."
thumbnail: "/images/thumbs/how-to-fix-error-0xc000021a-on-windows-11.webp"
faqs:
  - q: "What does error 0xc000021a mean on Windows 11?"
    a: "It means a critical Windows process — Winlogon.exe or Csrss.exe — terminated unexpectedly during startup, so the kernel halts the boot to protect the system. You will see a blue screen with the stop code 0xc000021a. The most common triggers are corrupted system files, a botched Windows update, mismatched drivers, or a third-party program that hooks into the login process."
  - q: "Can I fix 0xc000021a without reinstalling Windows?"
    a: "Often, yes. Start with Startup Repair from the recovery environment, then run SFC and DISM from a Command Prompt, uninstall the most recent quality update, and disable driver signature enforcement once to see if a bad driver is the cause. Most boot-blocking cases resolve with these steps, so a reinstall is only needed when system files are damaged beyond what DISM can repair."
  - q: "Why does 0xc000021a appear after a Windows update?"
    a: "Updates replace core system files, and if that process is interrupted by a power cut, disk error, or conflicting driver, the replaced files can be left in a broken state. On the next boot, Winlogon or Csrss crashes because it loads the damaged files. Uninstalling the latest update from the recovery environment usually restores the previous working files."
  - q: "Does 0xc000021a mean my hard drive is failing?"
    a: "Not necessarily, but it is worth checking. Corrupted files can come from bad sectors or a dying SSD, so run chkdsk and check the drive's SMART health. If errors keep coming back after every repair, or CHKDSK reports unreadable sectors, back up your data immediately and consider replacing the drive before reinstalling Windows."
---

The 0xc000021a blue screen is one of the nastiest errors on Windows 11 because it hits before you ever reach the desktop. Your laptop starts, the logo spins for a bit, and then everything dies with the message "Your PC ran into a problem and needs to restart" and the stop code 0xc000021a. Automatic repair kicks in, fails, and you end up in a loop with no way into Windows.

The good news: this error almost never means your hardware is dead. It means a critical Windows process — usually Winlogon.exe or Csrss.exe — crashed during startup, and Windows halted on purpose. The fixes below go from easiest to most aggressive, and the vast majority of cases are fixed by Fix 3 or Fix 4. You will do everything from the Windows Recovery Environment (WinRE), which you can reach by holding the power button to force-shut down the laptop three times in a row during boot.

## Why this happens

- **Corrupted system files.** Interrupted updates, sudden power loss, or disk errors can damage the core files that Winlogon and Csrss depend on at boot.
- **A bad Windows update.** Quality and feature updates replace boot-critical components; if one lands wrong, the next restart crashes immediately.
- **Incompatible or unsigned drivers.** Graphics, storage controller, or security drivers that do not match your Windows build can take down system processes.
- **Third-party software hooking into startup.** Some antivirus tools, disk utilities, and "optimizer" programs inject themselves into the login process and crash it.
- **Damaged Boot Configuration Data (BCD).** If the boot store points at the wrong or missing loader files, critical processes never initialize correctly.
- **Failing storage.** Bad sectors on an HDD or a degrading SSD silently corrupt the exact files Windows reads during startup.

## How to fix it

Work through these in order, testing a normal boot after each one.

### Fix 1: Run Startup Repair from the recovery environment

Start with the built-in automatic repair — it fixes common BCD and boot-loader problems without touching your files.

1. Force WinRE open: power on the laptop, then hold the power button to force it off as soon as the Windows logo appears. Repeat this **three times**.
2. On the fourth boot you should land on **Choose an option**. Click **Troubleshoot**.
3. Select **Advanced options**, then **Startup Repair**.
4. Choose your account, enter your password, and let the repair run to completion.
5. When it finishes, click **Continue** to restart normally and check whether the error is gone.

### Fix 2: Boot into Safe Mode and remove the suspect update or program

If Startup Repair did not help, get into Safe Mode where only essential drivers load.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
2. Press **4** (or **F4**) for Safe Mode.
3. Once in, open **Settings > Windows Update > Update history > Uninstall updates**.
4. Remove the most recent update installed before the error started, then restart.
5. If you recently installed new antivirus software or a driver utility, uninstall it from **Settings > Apps > Installed apps** while still in Safe Mode.
6. Restart normally and test.

### Fix 3: Repair system files with SFC and DISM from WinRE

This is the fix that resolves most 0xc000021a cases. Corrupted Winlogon or Csrss dependencies get rebuilt from the component store.

1. In WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Type `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` and press Enter. Note: your Windows drive may show up as D: or E: in WinRE — check with `dir C:` first.
3. Wait for the scan to finish, then run the DISM repair: `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` (use the correct drive letter for your Windows partition).
4. When DISM completes, run the SFC command once more to verify.
5. Type `exit`, choose **Continue**, and boot normally.

If DISM fails because it cannot reach Windows Update, mount your Windows 11 ISO as a source, or use the steps in our guide on [running SFC in Windows 11 24H2](/articles/how-to-run-sfc-scannow-in-windows-11-24h2/) for the offline-source method.

### Fix 4: Uninstall the latest update from the recovery environment

When a quality update is the culprit and you cannot even reach Safe Mode, remove it directly from WinRE.

1. Open **Command Prompt** from **Troubleshoot > Advanced options**.
2. List installed updates with `wmic qfe list brief /format:table` and note the most recent KB number.
3. Remove it with `wusa /uninstall /kb:XXXXXXX` using that KB number.
4. If wusa cannot run in WinRE, go back and use **Troubleshoot > Advanced options > Uninstall Updates** instead, choosing **Uninstall latest quality update**.
5. Restart and test a normal boot.

### Fix 5: Rebuild the Boot Configuration Data

A damaged BCD can crash boot-critical processes before they finish initializing.

1. From WinRE, open **Command Prompt** under **Advanced options**.
2. Run `bootrec /fixmbr` and then `bootrec /fixboot`. If fixboot gives "Access denied", skip to step 4.
3. Run `bootrec /rebuildbcd` and confirm adding the found Windows installation.
4. If rebuildbcd finds nothing, recreate the store manually: `bcdboot C:\Windows /s S: /f UEFI` where S: is your EFI partition letter (find it with `diskpart`, then `list vol`).
5. Type `exit` and restart.

### Fix 6: Disable driver signature enforcement and roll back drivers

A mismatched driver — often graphics or storage — can crash Csrss at boot.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
2. Press **7** (or **F7**) to **Disable driver signature enforcement**, then try booting.
3. If Windows starts, open **Device Manager** with `Win + X`.
4. Expand **Display adapters** and **IDE ATA/ATAPI controllers**, right-click each device, and choose **Properties > Driver > Roll Back Driver** if the option is available.
5. Alternatively, update them properly: grab the latest driver from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
6. Restart normally with signature enforcement back on.

### Fix 7: Check the drive for errors and failing health

If the error keeps returning after repairs, the storage itself may be damaging files.

1. From WinRE's **Command Prompt**, run `chkdsk C: /f /r` (use your Windows drive letter) and let it complete — it can take a while on large drives.
2. If you can boot into Safe Mode, check SMART health with a tool like CrystalDiskInfo, or run `wmic diskdrive get status` in an elevated Command Prompt.
3. Back up your important files immediately if CHKDSK reports bad sectors or SMART shows warnings.
4. A drive that keeps corrupting files needs replacing before any reinstall will stick.

For a broader walkthrough of blue-screen recovery techniques, see our guide on [fixing blue screens on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 8: Reset Windows while keeping your files

When every repair fails, a reset rebuilds the system cleanly.

1. In WinRE, choose **Troubleshoot > Reset this PC**.
2. Select **Keep my files**.
3. Choose **Cloud download** if you have a stable internet connection, otherwise **Local reinstall**.
4. Follow the prompts and let the reset finish — this takes 30 to 60 minutes.

If even the reset fails, do a full clean install using the media from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11). The official walkthrough at [Microsoft Support](https://support.microsoft.com/en-us/windows) covers creating bootable media step by step.

## Closing

Error 0xc000021a looks terrifying because it locks you out of Windows entirely, but it is a software problem far more often than a hardware one. Start with Startup Repair and SFC/DISM from the recovery environment, remove the most recent update, and rebuild the BCD if needed — that sequence clears the error for the overwhelming majority of laptops. Only reach for a reset or clean install when the repairs genuinely cannot fix the damage, and check your drive health before you reinstall so you are not putting fresh Windows on failing storage.
