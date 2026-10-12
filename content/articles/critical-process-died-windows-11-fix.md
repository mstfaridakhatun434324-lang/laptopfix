---
title: "How to Fix the CRITICAL_PROCESS_DIED Blue Screen on Windows 11"
slug: critical-process-died-windows-11-fix
date: 2026-10-08
categories: ["windows-errors"]
tags: ["bsod", "blue screen", "windows 11", "critical process died"]
description: "CRITICAL_PROCESS_DIED blue screen on Windows 11? Follow these 7 tested fixes — from SFC and DISM to driver rollbacks — to stop the crashes."
thumbnail: "/images/thumbs/critical-process-died-windows-11-fix.webp"
faqs:
  - q: "What does the CRITICAL_PROCESS_DIED blue screen mean?"
    a: "It means a process Windows needs to keep running — such as csrss.exe or wininit.exe — terminated unexpectedly. Windows halts immediately with this stop code to protect your data, and it's almost always caused by corrupted system files, bad drivers, or failing storage."
  - q: "Can a virus cause CRITICAL_PROCESS_DIED?"
    a: "Yes. Malware can corrupt or inject into critical system processes, and removing an infection badly can leave system files damaged. Run a full scan with Microsoft Defender in Safe Mode first — a clean scan with ongoing crashes points back to drivers or disk corruption."
  - q: "Will the fixes in this guide delete my files?"
    a: "Fixes 1 through 7 do not touch your personal files. SFC, DISM, CHKDSK, and driver changes only repair system files and settings. Fix 8 uses Reset with the 'Keep my files' option, which preserves your user folders but removes installed programs, so back up anything important first."
  - q: "What if CRITICAL_PROCESS_DIED happens right after a Windows update?"
    a: "Then the update itself is the most likely cause — a mismatched driver or a corrupted update component. Skip ahead to Fix 7 and uninstall the most recent update from Safe Mode or the recovery environment. If the crashes stop, pause updates for a few weeks and reinstall after Microsoft ships a revised patch."
---

You power on your Windows 11 laptop, and instead of the login screen you get a blue screen with the stop code CRITICAL_PROCESS_DIED. Sometimes it happens once and never returns. Sometimes it loops every few minutes, making the PC almost unusable. The message is frustratingly vague — it tells you a critical process died, but not which one or why.

The good news: most cases are software-related — corrupted system files, bad drivers, or a broken update — and fixable without a repair shop. Work through the fixes below in order, starting with the least invasive.

## What causes this error

- **Corrupted system files** — A crashed update, power loss during an install, or malware can damage the protected files Windows depends on, killing a critical process at boot.
- **Faulty or incompatible drivers** — A buggy display, storage, or chipset driver can terminate a process it interacts with, especially right after a driver or Windows update.
- **Bad Windows update** — A partially installed or buggy cumulative update can leave system components in an inconsistent state.
- **Disk errors or failing storage** — Bad sectors on the system drive can corrupt executables and pagefile data that critical processes need.
- **Malware** — Infections that inject into or replace system processes, or that damage them when removed, trigger this stop code.
- **Overheating or failing hardware** — Less common, but a dying RAM module or SSD can randomly kill processes; suspect this if crashes are random and all software fixes fail.

## How to fix it

Start with the least destructive fix and move down the list. If Windows won't stay up long enough to try anything, use Safe Mode first.

### Fix 1: Boot into Safe Mode

Safe Mode loads Windows with only essential drivers and services, giving you a stable environment to work in when normal mode keeps crashing.

1. At the login screen, hold **Shift**, click the power icon, and choose **Restart**. If it blue-screens during boot instead, force the machine off twice during the Windows logo — the third boot opens **Automatic Repair**.
2. Choose **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode (or **5** if you need networking).
3. If the system is stable in Safe Mode, run the fixes below from here.

### Fix 2: Run the System File Checker (SFC)

SFC scans protected Windows files and replaces corrupted ones with cached copies — the most useful first repair for this stop code.

1. Open **Start**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Type `sfc /scannow` and press Enter (takes 10–20 minutes).
3. If it reports repaired files, restart and test. If it reports files it could not repair, run Fix 3 first — DISM can repair the store SFC depends on.

### Fix 3: Run DISM to repair the component store

When SFC can't fix files because its repair source is also damaged, DISM downloads clean copies from Windows Update.

1. In an elevated Command Prompt, run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. This needs an internet connection and takes 10–30 minutes. If it sits at one percentage for a while, that's normal — give it 30 minutes before assuming it's stuck.
3. When it completes, run `sfc /scannow` again, then restart.

### Fix 4: Update or roll back drivers

Bad drivers are the most common cause of this error after a system update. Focus on storage (SATA/NVMe), chipset, and display drivers.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Display adapters**, **IDE ATA/ATAPI controllers**, and **Storage controllers**; right-click each device and choose **Update driver > Search automatically for drivers**.
3. If crashes started right after a driver update, instead open **Properties > Driver > Roll Back Driver** on that device.
4. Also check your laptop manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — for chipset and storage drivers for your exact model; they're often newer than what Windows Update offers.
5. A similar driver-focused approach applies to other blue screens like [KMODE_EXCEPTION_NOT_HANDLED](/articles/kmode-exception-not-handled-windows-11-fix/), where the faulty driver usually names itself in the minidump.

### Fix 5: Run CHKDSK on the system drive

If the drive itself has bad sectors, system files can corrupt again even after SFC repairs them.

1. In an elevated Command Prompt, type `chkdsk C: /f /r` and press Enter.
2. Type **Y** when asked to schedule the check at the next restart, then reboot.
3. The scan takes 20 minutes to several hours on large drives — do not interrupt it.
4. If repeated runs report a growing number of bad sectors, your drive is failing: back up your data immediately and replace it.

### Fix 6: Perform a clean boot

A clean boot starts Windows with only Microsoft services, ruling out third-party software conflicts without uninstalling anything.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, click **Open Task Manager** and disable every startup item, then close Task Manager.
4. Click **OK** and restart. If crashes stop, re-enable services in halves until the culprit returns — usually a third-party antivirus, VPN client, or disk utility.
5. Undo the clean boot afterward by reopening `msconfig` and re-enabling services and startup apps.

### Fix 7: Uninstall the most recent Windows update

If crashes began within days of a Patch Tuesday or feature update, the update itself is the prime suspect. This is especially relevant when the same update breaks other things — compare symptoms with guides for problems like [Windows Update error 0x800f081f](/articles/fix-windows-update-error-0x800f081f/) to see if the update is broadly faulty.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**, select the most recent update, and click **Uninstall**.
2. If Windows won't boot, do this from recovery: **Troubleshoot > Advanced options > Uninstall Updates > Uninstall latest quality update**.
3. Afterward, pause updates for 2–3 weeks at **Settings > Windows Update > Pause updates** while you monitor stability.

### Fix 8: Reset Windows (keep your files)

**Safety note:** This is the last resort. Back up your documents, photos, and license keys first — "Keep my files" preserves your user folders but removes all installed programs.

1. Open **Settings > System > Recovery** and click **Reset PC**.
2. Choose **Keep my files**, then **Cloud download** (cleanest copy, needs internet) or **Local reinstall**.
3. It takes 30 minutes to a few hours. Afterward, install drivers from the manufacturer's site before restoring programs — don't let Windows Update install drivers first if a bad driver caused the original problem.

If none of these fixes stop the crashes, especially after a clean reset, you're likely looking at failing hardware — run your manufacturer's built-in diagnostics (usually via F12 or Esc at boot) to test RAM and the SSD.
