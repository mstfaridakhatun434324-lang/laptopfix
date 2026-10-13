---
title: "Fix KERNEL_SECURITY_CHECK_FAILURE on Windows 11 (Step-by-Step Guide)"
slug: how-to-fix-kernel-security-check-failure-on-windows-11
date: 2026-09-04
categories: ["windows-errors"]
tags: ["bsod", "kernel-security-check-failure", "windows-11"]
description: "KERNEL_SECURITY_CHECK_FAILURE on Windows 11 is usually a bad driver or corrupt files. Follow these proven steps to diagnose and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-kernel-security-check-failure-on-windows-11.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "It is a Windows blue screen stop code (0x00000139) triggered when the kernel detects that a data structure it relies on has been corrupted. In practice this almost always points to a faulty device driver, corrupt system files, or bad memory feeding invalid data to the kernel."
  - q: "Can a single bad driver cause KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Yes, and it is the most common cause. Network, Wi-Fi, graphics, and storage drivers that pass malformed structures to the kernel trigger this check regularly. Updating or rolling back the suspect driver resolves most cases without touching your files."
  - q: "Is KERNEL_SECURITY_CHECK_FAILURE a virus?"
    a: "No. It is a defensive crash by Windows itself, not malware. However, rootkits that hook into the kernel can trip it. If the crash started after installing shady software, scan with Windows Security and remove the suspicious program before troubleshooting drivers."
  - q: "Will I lose my files fixing this error?"
    a: "Not with the standard repairs. SFC, DISM, driver updates, memory tests, and CHKDSK do not touch personal files. Only the last-resort option, a full Windows reset with the remove-everything choice, deletes data — back up first if you reach that point."
---

Seeing `KERNEL_SECURITY_CHECK_FAILURE` flash across your screen is never fun. This blue screen, stop code `0x00000139`, means Windows caught the kernel working with a corrupted data structure and pulled the plug before real damage could happen. It sounds dramatic, but in most cases the fix is a driver update or a quick system file repair.

I have walked people through this exact error dozens of times, and the culprit is almost always the same trio: a misbehaving driver, damaged system files, or flaky RAM. Work through the fixes below in order and you will very likely have a stable machine again without a reinstall.

## Why this happens

- **A driver hands the kernel bad data.** The most common trigger: a network, Wi-Fi, graphics, or storage driver passes a corrupted or mismatched structure to the kernel, tripping the security check.
- **Corrupted system files.** A botched update, hard shutdown, or failing drive can damage the core files Windows relies on, and the kernel notices the inconsistency.
- **Faulty RAM.** Bad memory cells feed the kernel garbage values. If the crashes seem random and frequent, memory is a prime suspect.
- **Outdated BIOS or firmware.** Old UEFI firmware can misreport hardware tables to Windows 11, especially after a major feature update.
- **Overclocking or unstable undervolting.** Pushing CPU, RAM, or GPU past stable limits corrupts kernel data structures in flight.
- **Failing storage drive.** Bad sectors on the system drive corrupt files silently until the kernel trips over them.
- **Conflicting low-level software.** Some antivirus tools, disk utilities, and virtualization drivers hook deep into the kernel and clash with Windows 11.

## How to fix it

Work through these in order, from least to most invasive. Stop as soon as the crashes stop — there is no need to complete the whole list.

### Fix 1: Boot into Safe Mode if the crash loops

If your laptop blue-screens before you can do anything, get into Safe Mode first so the remaining fixes are possible.

1. Force the recovery environment: hold the **power button** to shut down mid-boot three times in a row.
2. On the fourth boot, select **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need the internet).
4. Once inside, continue with the fixes below — most of them work fine in Safe Mode.

If Safe Mode itself refuses to load, see our guide on [Windows 11 Safe Mode not working on Lenovo laptops](/articles/fix-windows-11-safe-mode-not-working-on-lenovo-laptop/) for recovery-environment alternatives.

### Fix 2: Repair system files with SFC and DISM

Corrupted system files are the quickest win here, and the repair tools are built into Windows.

1. Open **Start**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run the System File Checker: `sfc /scannow` — let it finish (it can take 15–30 minutes).
3. If it reports unfixable errors, run the DISM repairs in this exact order:
   - `DISM /Online /Cleanup-Image /ScanHealth`
   - `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart normally and use the laptop for a day. Many `KERNEL_SECURITY_CHECK_FAILURE` cases end right here.

### Fix 3: Update the drivers most likely to blame

A stale or buggy driver is the single most common cause, so update the usual suspects before anything drastic.

1. Open **Device Manager** (`Win + X` > **Device Manager**).
2. Expand **Display adapters**, **Network adapters**, and **Storage controllers**.
3. Right-click each device and choose **Update driver** > **Search automatically for drivers**.
4. For graphics especially, grab the latest package directly from the source — use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics, or your GPU vendor's official tool for NVIDIA and AMD cards.
5. Check your laptop maker's support page too — [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) covers the general driver-update flow if you need a walkthrough.
6. Restart after updates and monitor for another 24 hours.

### Fix 4: Roll back a recent driver update

If the blue screens started right after a driver update, the new driver is the suspect until proven otherwise.

1. Open **Device Manager** and find the device you updated (often Wi-Fi or graphics).
2. Right-click it and choose **Properties**, then open the **Driver** tab.
3. Click **Roll Back Driver** if it is available, pick a reason, and confirm.
4. Restart and test. If rolling back fixes it, stay on the older driver until the vendor releases a fixed version.

### Fix 5: Test your RAM

Random, frequent `KERNEL_SECURITY_CHECK_FAILURE` crashes are a classic sign of failing memory.

1. Press `Win + R`, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the Windows Memory Diagnostic run its full pass — do not interrupt it.
4. After reboot, check the results in **Event Viewer** > **Windows Logs** > **System**, filtering for `MemoryDiagnostics-Results`.
5. If errors are found and your laptop has two RAM sticks, test one at a time to isolate the bad one; replace it. This error on Dell machines often pairs with the memory angle we cover in [fixing the MEMORY_MANAGEMENT stop code on Dell laptops](/articles/how-to-fix-stop-code-memory-management-on-dell-laptop/).

### Fix 6: Remove conflicting low-level software

Kernel hooks from third-party tools can trip the security check even when drivers are fine.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall any third-party antivirus, disk cleaners, VPN clients, or overclocking utilities you added recently.
3. Run `msconfig`, open the **Services** tab, check **Hide all Microsoft services**, and disable the rest temporarily for testing.
4. Restart and see if the crashes stop. If they do, re-enable services one group at a time to find the culprit.

### Fix 7: Check the drive and update the BIOS

Two deeper hardware-adjacent checks that are worth doing before you consider reinstalling.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r` — type **Y** when prompted and restart so the scan runs.
2. Visit your laptop manufacturer's support site and check for a BIOS/UEFI update for your exact model.
3. Follow their flashing instructions exactly, with the charger plugged in — a power loss mid-flash can brick the board.
4. Reset any CPU/RAM overclock or undervolt in the BIOS back to defaults while you are there.

### Fix 8: Reset Windows as a last resort

If every fix above fails, a corrupted installation may be beyond targeted repair.

1. Open **Settings** > **System** > **Recovery**.
2. Click **Reset PC** and choose **Keep my files** first — this reinstalls Windows while preserving your data.
3. If crashes persist even after that, repeat with **Remove everything** (back up to an external drive first).
4. A clean reinstall that still crashes points squarely at hardware — usually RAM or the SSD — and it is time for a repair shop.

## Closing

`KERNEL_SECURITY_CHECK_FAILURE` looks scary, but it is almost always software: a driver, a corrupted file, or a conflicting program. Start with SFC and driver updates, test your RAM if the crashes feel random, and keep the reinstall as your last card. Your laptop is not dying — it just needs the kernel to stop being fed bad data.
