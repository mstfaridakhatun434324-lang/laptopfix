---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on a Lenovo Laptop"
slug: how-to-fix-attempted-execute-of-noexecute-memory-on-lenovo-laptop
date: 2026-10-07
categories: ["windows-errors"]
tags: ["bsod", "stop code 0xfc", "lenovo", "memory"]
description: "Fix the ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen on your Lenovo laptop with driver, memory, and system repairs that actually work."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-on-lenovo-laptop.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "It means a driver or program tried to run code from a memory region marked non-executable (stop code 0x000000FC). Windows kills the system with a blue screen to protect itself. On Lenovo laptops the usual suspects are a corrupted graphics or chipset driver, faulty RAM, or a bad Windows update that replaced a working driver."
  - q: "Is this blue screen caused by bad RAM?"
    a: "Sometimes, but bad drivers are more common. Run Windows Memory Diagnostic first because it is quick and rules hardware in or out. If the memory test passes clean twice, focus on drivers: roll back the most recently updated driver, then update chipset and graphics drivers from Lenovo."
  - q: "Can a Windows update cause this stop code?"
    a: "Yes. Feature and cumulative updates sometimes replace a stable Lenovo driver with a generic one that misbehaves. If the crashes started right after an update, uninstalling that update or rolling back the driver it touched is often the fastest fix."
  - q: "Will I lose my files fixing this?"
    a: "No. Every fix in this guide — memory tests, driver rollbacks, SFC, DISM, and update uninstalls — leaves your personal files alone. Only a full Windows reset with the 'remove everything' option would delete files, and that is a last resort you probably will not need."
---
Seeing ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on your Lenovo's blue screen is unsettling, mostly because the name sounds like a hardware death sentence. It usually isn't. That stop code (0x000000FC) means something tried to execute code from a chunk of memory Windows had marked as off-limits for execution. Windows panics, throws the blue screen, and reboots to protect itself. Nine times out of ten on a Lenovo, the culprit is a driver doing something it shouldn't, not dying hardware.

The good news is this is very fixable with a methodical approach. This guide walks you through the exact order a technician would use: rule out RAM quickly, then hunt down the bad driver, then repair whatever Windows damage is left behind. You don't need any special tools — just your Lenovo and a bit of patience.

## Why this happens

- **A corrupted or outdated device driver.** Graphics, chipset, Wi-Fi, and storage drivers are the classic offenders. One bad driver writing to the wrong memory address triggers this stop code reliably.
- **Faulty or mismatched RAM.** A failing memory module can corrupt the data structures Windows uses to track which memory is executable. This is less common than driver trouble but worth ruling out early.
- **A Windows update that replaced a working driver.** Lenovo machines are particularly prone to this: Windows Update swaps a stable Lenovo-tuned driver for a generic one, and the crashes start the next reboot.
- **Malware or a rootkit.** Malicious code that injects itself into memory regions can trip the no-execute protection. Rare, but it happens.
- **Overclocking or aggressive BIOS settings.** If you've tweaked memory timings or enabled performance modes in the BIOS, unstable settings can corrupt memory bookkeeping.
- **Corrupted system files.** Damaged Windows kernel files can mislabel memory regions, causing legitimate code to land in no-execute pages.

## How to fix it

Work through these in order. Each fix rules something out, so don't skip ahead — the order is the diagnosis.

### Fix 1: Boot into Safe Mode and note what changed

If the blue screen loops, you need a stable environment first. Safe Mode loads only essential drivers, which usually stops the crashing long enough to work.

1. Force WinRE: power the laptop on, and the moment the Lenovo logo appears, hold the power button to force it off. Repeat three times. On the fourth boot, Windows opens **Automatic Repair**.
2. Click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need to download drivers).
4. Once in, ask yourself: did this start after a Windows update, a driver update via Lenovo Vantage, or new software? Write down the answer — it tells you which fix to prioritize.
5. If you can't even reach WinRE, the general [safe mode boot guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers alternate entry methods.

### Fix 2: Test your RAM with Windows Memory Diagnostic

Rule out hardware before chasing drivers. This takes 15–30 minutes and runs outside Windows.

1. In Safe Mode (or normal Windows if it's stable), press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The laptop reboots into the memory test.
3. Press **F1**, select **Extended**, and let it complete at least two full passes.
4. If it reports hardware problems, you've found it: reseat the RAM modules (power off, unplug, remove the bottom panel, pop the sticks out and back in firmly) and retest. If errors persist, that stick needs replacing.
5. Clean result? RAM is fine — move on. Memory faults are a common companion of this stop code, and the related [IRQL_NOT_LESS_OR_EQUAL guide](/articles/irql-not-less-or-equal-windows-11-fix/) covers the driver side of the same family of crashes.

### Fix 3: Roll back or update the suspect driver via Lenovo tools

Lenovo's own driver stack is tuned for your exact model, and it's the safest source for replacements.

1. Open **Lenovo Vantage** (install it from the Microsoft Store if missing) or **Lenovo System Update**, and run a full driver scan.
2. Install every recommended **chipset**, **graphics**, **BIOS/UEFI**, and **storage** update it offers. Reboot after each batch.
3. If the crashes began right after a driver update, roll back instead: open **Device Manager** (`devmgmt.msc`), right-click the device (start with Display adapters and Network adapters), choose **Properties** > **Driver** tab > **Roll Back Driver**.
4. Grab the exact drivers for your serial number from [Lenovo Support](https://support.lenovo.com/us/en/) if Vantage misses anything — never install chipset or BIOS drivers from random third-party sites.
5. For Intel-based Lenovos, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can catch chipset and Wi-Fi updates Lenovo hasn't packaged yet.

### Fix 4: Repair system files with SFC and DISM

Corrupted Windows files can mislabel memory regions. These two built-in tools repair them without touching your data.

1. Open **Terminal (Admin)** — right-click Start, choose it, accept the UAC prompt.
2. Run `sfc /scannow` and wait for it to finish (10–20 minutes). Don't close the window.
3. If SFC reports it couldn't fix everything, run the DISM repair: `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Run `sfc /scannow` once more after DISM completes, then reboot normally.
5. Microsoft's own [Windows support hub](https://support.microsoft.com/en-us/windows) documents both tools if you want the official reference.

### Fix 5: Check the disk for corruption

A damaged pagefile or system area on the SSD can produce memory-looking crashes that aren't memory at all.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`.
2. Type **Y** when asked to schedule the check, then reboot. The scan runs before Windows loads and can take a while on large drives — let it finish.
3. If chkdsk finds and repairs bad sectors on an SSD, treat it as a warning: back up your important files soon, because SSDs don't heal.

### Fix 6: Uninstall the Windows update that started it

When the timeline points at Patch Tuesday, remove the suspect update.

1. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Find the most recent **cumulative** or **feature** update matching when the crashes began, select it, and click **Uninstall**.
3. Reboot and use the laptop for a day. If the crashes stop, pause updates for a week: **Settings** > **Windows Update** > **Pause updates**.
4. Report the bad update to Lenovo support with your model and serial number so they can flag the driver conflict.

### Fix 7: Run a full malware scan

Since this stop code can be triggered by code injected into protected memory, rule out infection.

1. Open **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan** > **Scan now**.
2. The laptop reboots into a clean environment and scans before Windows loads — this catches rootkits that hide from normal scans.
3. Remove anything it finds, reboot, and confirm the crashes are gone.

### Fix 8: Reset Windows as a last resort

If everything above passes and it still crashes, the installation itself is damaged beyond targeted repair.

1. Back up your files to an external drive or OneDrive first.
2. Go to **Settings** > **System** > **Recovery** > **Reset this PC** > **Keep my files**.
3. Choose **Cloud download** for the freshest Windows image, and let it complete.
4. After the reset, install drivers from Lenovo Vantage before letting Windows Update touch drivers — this avoids reintroducing the original conflict.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY looks scary but follows a predictable pattern on Lenovo laptops: test the RAM, fix the drivers with Lenovo's own tools, repair Windows files, and only then consider bigger steps. Most people are fixed by Fix 3 or Fix 4. If you worked through the whole list and the blue screen persists on a clean Windows install with Lenovo's drivers, that's the point where the motherboard or RAM itself is suspect — and a Lenovo service center visit with your diagnostic notes in hand will save everyone time.
