---
title: "How to Fix the Memory Management Stop Code on Windows 10"
slug: how-to-fix-stop-code-memory-management-on-windows-10
date: 2026-09-22
categories: ["windows-errors"]
tags: ["memory-management", "windows-10", "blue-screen"]
description: "Memory Management blue screen on Windows 10? Test your RAM, update drivers, and repair system files with this step-by-step fix guide."
thumbnail: "/images/thumbs/how-to-fix-stop-code-memory-management-on-windows-10.webp"
faqs:
  - q: "Does the Memory Management stop code always mean bad RAM?"
    a: "No — despite the name, it's frequently a driver bug rather than faulty memory. Drivers that corrupt memory pools trigger this stop code just as easily as bad RAM does. Always update drivers and repair system files before buying replacement memory; test the RAM, but don't assume it's guilty."
  - q: "Can a Windows 10 update cause Memory Management blue screens?"
    a: "Yes. Updates that replace storage, graphics, or chipset drivers are the most common trigger for new-onset crashes. If the blue screens started within a day of Patch Tuesday or a feature update, roll back the most recently updated driver first — that's the highest-probability fix."
  - q: "How long should I run a memory test?"
    a: "The built-in Windows Memory Diagnostic standard test takes 10–15 minutes and catches most failures. For intermittent crashes, run the extended test overnight or use MemTest86 for at least 4 full passes (several hours). One clean quick pass doesn't fully clear RAM that only fails when hot."
  - q: "Will increasing virtual memory fix this error?"
    a: "Sometimes it helps when the crashes happen with many apps open and RAM nearly full, but it's a workaround, not a fix for driver-caused corruption. If you have 8GB or less of RAM and constantly run at 90%+ usage, increasing the page file or adding RAM is sensible — but still update drivers first."
---
The Memory Management stop code (0x0000001A) is Windows catching something corrupting its memory handling and pulling the emergency brake. Despite the name, this is as often a driver problem as a RAM problem — buggy drivers corrupt the same memory structures that bad RAM does, and Windows can't tell the difference from the crash alone.

That means the smart approach is to check the cheap, fixable causes first: drivers, system files, and disk errors — then test the RAM properly. The steps below follow that order, and each one is designed to either fix the problem or rule out a suspect so you don't waste time. Keep track of which fixes you've tried and whether the crashes changed at all — that pattern is useful if you end up needing the dump analysis.

For the Windows 11 version see [Stop Code Memory Management on Windows 11](/articles/how-to-fix-stop-code-memory-management-on-windows-11/), and if you suspect the RAM specifically, jump to our [Memory Diagnostic tool guide](/articles/how-to-run-memory-diagnostic-tool-in-windows-11-24h2/).

## Why this happens

- **Buggy device drivers.** Graphics, storage, and network drivers that corrupt memory pools are the most common cause.
- **Faulty RAM.** A bad stick flips bits in memory structures, producing exactly this stop code.
- **Corrupted system files.** Damaged Windows memory-management components after a bad update.
- **Disk errors.** Bad sectors in the page file area cause memory-management faults that look like RAM issues.
- **Overclocked or mismatched RAM.** XMP profiles, mixed RAM sticks, or aggressive timings create instability.
- **Software conflicts.** Two antivirus products or buggy virtualization software fighting over memory.

## How to fix it

Work through these in order — drivers first, hardware last.

### Fix 1: Update graphics, chipset, and storage drivers

Drivers are the most likely cause, so start here.

1. Open **Device Manager** (press **Win + X** and choose it).
2. Update **Display adapters**, then **IDE ATA/ATAPI controllers** and **Storage controllers**, then **Network adapters** — right-click each, choose **Update driver > Search automatically for drivers**.
3. For the freshest versions, download from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart and use the laptop normally to see if crashes stop.

### Fix 2: Roll back the driver from the last update

If crashes started right after an update, reverse it.

1. In **Device Manager**, right-click the most recently updated device and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver**, pick a reason, and confirm.
3. If the button is greyed out, uninstall the device (tick **Attempt to remove the driver for this device**) and restart so Windows reinstalls its previous driver.
4. Then pause Windows updates briefly: **Settings > Update & Security > Windows Update > Pause updates for 7 days**, to stop the bad driver reinstalling immediately.

### Fix 3: Run SFC and DISM

Repair the Windows components that manage memory.

1. Right-click **Start** and choose **Windows PowerShell (Admin)**.
2. Run: `sfc /scannow`
3. When done, run: `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart. If SFC found and fixed corruption, retest for a day or two before declaring victory.

### Fix 4: Check the disk and page file

Disk errors in the page file area mimic RAM faults.

1. Open an admin **PowerShell** and run: `chkdsk C: /f`
2. Type **Y** to schedule the check and restart.
3. After the check, verify the page file: press **Win + R**, type `sysdm.cpl`, go to **Advanced > Performance Settings > Advanced > Virtual memory**, and confirm it's **System managed**.
4. If you manually set a tiny page file, switch it back to system-managed — an undersized page file causes exactly these crashes under load.

### Fix 5: Run Windows Memory Diagnostic properly

Now test the RAM — properly, not just the quick pass.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Press **F1** during the test to open options, choose **Extended**, and set at least 2 passes.
4. If you have two sticks and errors appear, test each stick alone in the same slot to identify the bad one.
5. Replace faulty RAM — and if the laptop has mismatched sticks (different brands/speeds), consider a matched pair, since mismatches cause this stop code on their own.

### Fix 6: Disable overclocking and XMP

Unstable memory settings are a classic trigger.

1. Restart into BIOS/UEFI (**F2** or **Del** at boot).
2. Disable **XMP / DOCP** memory profiles and any CPU overclocking.
3. Save with **F10** and exit.
4. Test for several days at stock speeds. If crashes vanish, the RAM simply can't handle the overclocked timings.

### Fix 7: Remove conflicting security software

Two memory-hooking security products cause corruption-style crashes.

1. Open **Settings > Apps** and check for multiple antivirus products, or an antivirus plus a "system optimizer" with real-time protection.
2. Keep one reputable product and uninstall the rest.
3. If you use virtualization software (VirtualBox, VMware) that you installed recently, update it — old versions hook memory in ways Windows 10 doesn't like.

### Fix 8: Clean-install the most suspicious driver

When one driver keeps coming back as the suspect, wipe it completely.

1. Download **Display Driver Uninstaller (DDU)** on another PC and copy it over, plus the fresh driver installer.
2. Boot into Safe Mode (**Settings > Update & Security > Recovery > Advanced startup > Restart**, then **Troubleshoot > Advanced options > Startup Settings**).
3. Run DDU to completely remove the graphics driver, then install the fresh driver you downloaded.
4. Microsoft documents the official blue screen process in its Windows support hub.

## Closing

Memory Management is a "something corrupted memory" alarm, not a "your RAM is dead" diagnosis — and drivers are guilty more often than memory is. Update and roll back drivers first, repair system files, then test the RAM thoroughly before spending money on replacements. Work the list in order and the crashes will stop; skip straight to buying RAM and you may fix nothing at all while the real culprit — usually a driver — keeps crashing your laptop.
