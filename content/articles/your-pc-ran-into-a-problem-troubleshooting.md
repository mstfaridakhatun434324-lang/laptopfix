---
title: "Your PC Ran Into a Problem: How to Actually Fix It on Windows 11"
slug: your-pc-ran-into-a-problem-troubleshooting
date: 2026-10-08
categories: ["windows-errors"]
tags: ["blue screen", "startup repair", "windows 11", "troubleshooting"]
description: "Stuck on the 'Your PC ran into a problem' blue screen? Follow this technician-tested order of fixes to get Windows 11 booting again."
thumbnail: "/images/thumbs/your-pc-ran-into-a-problem-troubleshooting.webp"
faqs:
  - q: "Why does Windows keep showing 'Your PC ran into a problem'?"
    a: "That message is the generic blue-screen (BSOD) screen. Underneath it, a stop code explains the real cause — often a faulty driver, corrupted system files, or a recent update. If the screen reboots too fast to read the code, disable automatic restart in Startup and Recovery settings, or check the minidump with BlueScreenView after booting."
  - q: "Will my files be deleted if I use Startup Repair?"
    a: "No. Startup Repair only attempts to fix the boot configuration and critical system files; it does not touch your personal files. It is safe to run even if it fails — you can move on to System Restore or SFC scans afterward. Your documents, photos, and downloads remain on the drive unless you choose a full reset."
  - q: "How do I get into Safe Mode when Windows won't boot?"
    a: "Interrupt the boot process three times in a row: hold the power button to force the laptop off during the Windows logo, then power on again. On the third attempt, Windows loads Automatic Repair. Choose Troubleshoot, then Advanced options, then Startup Settings, then Restart, and press 4 for Safe Mode or 5 for Safe Mode with Networking."
  - q: "What should I do if none of the fixes work?"
    a: "Back up your files from Safe Mode or using a Windows installation USB, then perform a cloud-download reset from Troubleshoot > Reset this PC > Keep my files. If even that fails, the drive itself may be failing — run your laptop maker's hardware diagnostics and consider an SSD replacement."
---
That sinking feeling when your laptop restarts mid-work and lands on a blue screen reading "Your PC ran into a problem and needs to restart." You are not alone — this is the single most common Windows 11 crash screen, and in most cases the underlying cause is fixable without reinstalling Windows.

The message itself is deliberately vague. What matters is what happened just before it: a driver update, a Windows Update, a new program install, or a hardware change. Once you know that, the fixes below follow a clear order — quickest first, most involved last — so you stop wasting time on random forum advice.

## Why this happens

- **A recent driver update misbehaved.** Graphics, Wi-Fi, and chipset drivers are the usual suspects; a bad one can crash the kernel the moment it loads.
- **Corrupted system files.** A hard shutdown, power loss during an update, or disk errors can leave core Windows files unreadable.
- **A Windows Update introduced a conflict.** Feature updates occasionally clash with older BIOS versions or third-party antivirus filters.
- **Failing storage or RAM.** Bad sectors or unstable memory produce crashes that look identical to software bugs — and get worse over time.
- **Overheating or hardware strain.** A laptop thermal-throttling under load can trip hardware error checks and force a blue screen.
- **Boot configuration damage.** The BCD store that tells Windows how to start can be corrupted by disk errors or dual-boot tools.

## How to fix it

Work through these in order, from quickest and safest to most involved. Stop as soon as the problem stays fixed.

### Fix 1: Note the stop code and undo the last change

Before touching anything, identify the trigger. If Windows shows a stop code (like `DRIVER_IRQL_NOT_LESS_OR_EQUAL`), photograph it with your phone.

1. Think back: did you install a driver, update Windows, or add new hardware in the last few days?
2. If a program was installed just before the crashes, boot into Safe Mode (see FAQ above) and uninstall it from **Settings > Apps > Installed apps**.
3. If Windows Update ran recently, go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent one, then test for a day.
4. If you added new RAM or an SSD, reseat or temporarily remove it to rule out a hardware fault.

### Fix 2: Run Startup Repair from Advanced Startup

This is Windows' own boot doctor and it takes about five minutes.

1. Force the Advanced Startup menu by interrupting boot three times (hold power during the Windows logo), or go to **Settings > System > Recovery > Advanced startup > Restart now**.
2. Select **Troubleshoot > Advanced options > Startup Repair**.
3. Pick your account, enter your password if asked, and let it run — it may restart once or twice.
4. If it reports it "couldn't repair your PC," don't panic; continue to Fix 3.

### Fix 3: Repair system files with SFC and DISM

If the crash stems from corrupted Windows files, these two commands fix them in place. Run them from an elevated Command Prompt in Safe Mode with Networking.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to finish — it verifies and replaces damaged files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store that SFC relies on.
4. Restart normally and use the laptop for a while to see if the crash returns. If SFC found and fixed corruption, this often ends it.

### Fix 4: Update or roll back drivers

Driver-caused blue screens are the most common repeat offenders, especially after Windows 11 feature updates.

1. Open **Device Manager** (right-click Start) and look for any device with a yellow warning icon.
2. Right-click your graphics adapter and Wi-Fi adapter, choose **Properties > Driver**, and try **Roll Back Driver** if the option is available.
3. If rollback isn't offered, visit your laptop maker's support site — [Dell's support page](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and download the latest chipset, graphics, and network drivers for your exact model.
4. For a quick check of which drivers are actually out of date, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) scans Intel hardware automatically.

### Fix 5: Use System Restore to a known-good point

If the crashes started recently, rolling Windows back a few days is often the fastest real fix.

1. From Advanced Startup, choose **Troubleshoot > Advanced options > System Restore**.
2. Select a restore point dated before the crashes began and click through the wizard.
3. The process doesn't delete your files, but it will remove programs installed after the restore point — note them down first.
4. After the restore completes, pause Windows updates for a week from **Settings > Windows Update** so a bad update doesn't reinstall itself immediately.

### Fix 6: Test your memory and disk

Software fixes won't help if the hardware is failing, so rule it out directly.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems** to run Windows Memory Diagnostic.
2. Open **Terminal (Admin)** and run `chkdsk C: /f /r`, then press Y and restart — it will scan the drive for bad sectors before Windows loads.
3. Check your SSD's health with your manufacturer's tool (Samsung Magician, Crucial Storage Executive, or your laptop maker's diagnostics), which you can usually launch from the BIOS.
4. If either test reports failures, replace the faulty part before doing anything else — no software fix survives bad hardware.

### Fix 7: Reset Windows with the cloud-download option

When everything else fails, a reset with files kept gives you a clean Windows without losing your documents.

1. Boot to Advanced Startup and pick **Troubleshoot > Reset this PC > Keep my files**.
2. Choose **Cloud download** so Windows fetches a fresh image from [Microsoft's servers](https://www.microsoft.com/en-us/software-download/windows11) rather than reusing possibly-corrupt local files.
3. Follow the prompts; the process takes 30–60 minutes and your PC restarts several times.
4. After the reset, install drivers from your laptop maker's site before anything else, then add programs back one at a time.

## Closing

The "Your PC ran into a problem" screen looks catastrophic, but the fix ladder is methodical: undo what changed, repair the boot, repair the files, fix the drivers, test the hardware, and only then reset. Most laptops are stable again by Fix 4. If you notice the crashes follow a pattern — always during gaming, always on wake — tell a technician the pattern and the stop code, and diagnosis gets dramatically faster. For deeper blue-screen specifics, the guides on [disabling automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) and [fixing the general blue screen of death](/articles/how-to-fix-blue-screen-of-death-windows-11/) walk through reading stop codes in detail.
