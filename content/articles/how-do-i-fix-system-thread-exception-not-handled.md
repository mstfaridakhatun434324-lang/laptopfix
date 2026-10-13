---
title: "Fixing the System Thread Exception Not Handled Error"
slug: how-do-i-fix-system-thread-exception-not-handled
date: 2026-09-23
categories: ["windows-errors"]
tags: ["bsod", "system thread exception", "driver fix"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen on your laptop? Identify the failing driver from the dump and fix it with this ordered repair guide."
thumbnail: "/images/thumbs/how-do-i-fix-system-thread-exception-not-handled.webp"
faqs:
  - q: "What causes SYSTEM_THREAD_EXCEPTION_NOT_HANDLED?"
    a: "A system thread — usually a driver — threw an exception that Windows could not catch. The most common triggers are faulty graphics or Wi-Fi drivers, corrupted system files, and occasionally failing RAM. The minidump almost always names the responsible driver file directly."
  - q: "How do I find which driver caused it?"
    a: "Open the latest minidump in C:\\Windows\\Minidump using WinDbg Preview (free from the Microsoft Store) and run `!analyze -v`. The IMAGE_NAME line tells you the driver file. Alternatively, the free BlueScreenView tool lists the crash and highlights the suspect driver in its lower pane."
  - q: "Can bad RAM cause this error?"
    a: "Yes. When a driver is not at fault, defective RAM is the next suspect, since memory corruption makes normal drivers throw exceptions. Run Windows Memory Diagnostic or MemTest86 for at least a full pass; any red error means the RAM stick needs replacing."
  - q: "Should I update or roll back the driver?"
    a: "If the crash started after a driver update, roll back first — the new version is suspect. Otherwise, do a clean update from the manufacturer's site. Graphics drivers from NVIDIA or AMD should come from the vendor directly rather than through Windows Update for the freshest stable build."
---
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is Windows telling you that one of its own worker threads — almost always a driver — hit an error it couldn't recover from. The blue screen usually names a driver file right on the screen (something like `nvlddmkm.sys` or `rtwlanu.sys`), which is your biggest clue. That name is the thread that failed.

The fix path is straightforward: identify the driver, replace it with a correct version, and check the supporting cast (system files, RAM) if the driver alone doesn't explain it. Most of these crashes resolve at the driver step, so start there.

## Why this happens

- **A buggy or corrupted driver threw an unhandled exception.** Graphics, Wi-Fi, audio, and storage drivers are the usual suspects; the minidump normally names the file.
- **A recent driver update introduced the bug.** The crash timeline often lines up exactly with a driver or Windows update.
- **Corrupted system files.** Damaged kernel components can make legitimate drivers behave as though they are broken.
- **Faulty RAM.** Bad memory cells corrupt the data drivers work with, producing exceptions in code that is actually fine.
- **Overheating or unstable overclocks.** Thermal throttling and marginal overclocks cause timing errors that surface as thread exceptions, especially in GPU drivers.
- **Conflicting third-party software.** Antivirus and driver-updater utilities that inject into the kernel can destabilize threads belonging to other drivers.

## How to fix it

Work through these in order — identify the driver first, fix it, then verify the hardware underneath.

### Fix 1: Read the minidump to name the driver

Everything downstream depends on knowing which driver file crashed, so do this first.

1. If the laptop boots, go to `C:\Windows\Minidump\` and copy the newest `.dmp` file somewhere readable.
2. Install **WinDbg Preview** from the Microsoft Store, open the dump, and run `!analyze -v` in the command box.
3. Read the **IMAGE_NAME** line — for example, `nvlddmkm.sys` means the NVIDIA driver, `NETIO.SYS` points at networking.
4. If WinDbg feels heavy, use BlueScreenView: it lists every crash and highlights the suspect driver automatically.
5. Write down the driver name and the device it belongs to before continuing.

### Fix 2: Clean-install the correct driver

The most reliable fix is removing the broken driver completely and installing a fresh, correct version.

1. Boot into **Safe Mode** if crashes block normal use: **Shift + Restart > Troubleshoot > Advanced options > Startup Settings**, press **4**.
2. Open **Device Manager** (**Win + X**), find the device matching the faulty driver, right-click it, and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
3. Restart — Windows will load a basic fallback driver.
4. Download the proper driver: graphics from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html), everything else from your laptop maker's page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
5. Install it, restart again, and use the laptop normally for a while to confirm the crashes stop. This same clean-driver approach also fixes [VIDEO_TDR_FAILURE](/articles/how-to-fix-video-tdr-failure-in-windows-11-24h2/) crashes, which share the same root causes.

### Fix 3: Roll back a recent driver update

If the blue screens started within a day or two of a driver update, the new driver is guilty until proven innocent.

1. Open **Device Manager**, double-click the suspect device, and open the **Driver** tab.
2. Click **Roll Back Driver**, choose a reason, and confirm.
3. Restart and test for a day or two before allowing any driver updates again.
4. If the roll-back button is greyed out, restore via **System Restore** to a point before the update.

### Fix 4: Repair system files with SFC and DISM

When the driver looks fine but crashes persist, corrupted Windows components may be the real problem.

1. Open an elevated **Command Prompt** (search **cmd**, right-click, **Run as administrator**).
2. Run `sfc /scannow` and let it complete — it repairs protected system files.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store SFC relies on.
4. Restart and monitor. If SFC reports it found and fixed corruption, that was likely your culprit.

### Fix 5: Test the RAM

Memory faults make good drivers throw bad exceptions, so rule RAM out before blaming software further.

1. Search for **Windows Memory Diagnostic** in the Start menu, open it, and choose **Restart now and check for problems**.
2. Let the standard test complete; any reported errors mean a stick needs replacing.
3. For a deeper check, create a bootable MemTest86 USB and run at least one full pass (several hours).
4. If errors appear, reseat the RAM modules first — a loose stick causes the same symptoms — then replace the faulty one. Memory problems are also the classic cause of [MEMORY_MANAGEMENT](/articles/memory-management-bsod-windows-11-fix/) blue screens.

### Fix 6: Check temperatures and undo overclocks

Heat and unstable clocks produce exactly this kind of intermittent thread failure.

1. Install a hardware monitor like HWMonitor and check CPU/GPU temperatures under load — sustained readings above 95°C on a laptop are a red flag.
2. Clean dust from vents with compressed air and make sure the laptop sits on a hard, flat surface.
3. If you overclocked the CPU, GPU, or RAM (including XMP profiles), revert everything to stock speeds in the BIOS and retest.
4. On gaming laptops, try the manufacturer's balanced power profile instead of maximum performance for a few days.

### Fix 7: Remove interfering third-party software

Kernel-level utilities can destabilize threads that belong to other drivers.

1. Uninstall third-party antivirus, driver updaters, and system "optimizers" from **Settings > Apps > Installed apps**.
2. Restart and rely on Microsoft Defender temporarily to see whether crashes stop.
3. If the crashes vanish, the removed software was the trigger — find an alternative or check with its vendor for an updated, compatible version.

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED almost always comes down to one bad driver, and the minidump tells you which one. Clean-install the correct driver from the manufacturer, roll back recent updates, then verify system files and RAM if needed. Work the list in order and you'll find the culprit without guessing. If the named driver is a storage driver, also check the guide on [UNEXPECTED_STORE_EXCEPTION](/articles/unexpected-store-exception-windows-11-fix/) — storage faults can masquerade as thread exceptions.
