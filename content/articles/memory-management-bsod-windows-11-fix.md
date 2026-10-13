---
title: "Memory Management BSOD on Windows 11: How to Fix It"
slug: memory-management-bsod-windows-11-fix
date: 2026-09-18
categories: ["windows-errors"]
tags: ["bsod", "memory-management", "windows-11"]
description: "The MEMORY_MANAGEMENT blue screen on Windows 11 usually means bad RAM or a driver corrupting memory. Here's the full fix sequence."
thumbnail: "/images/thumbs/memory-management-bsod-windows-11-fix.webp"
faqs:
  - q: "What causes the MEMORY_MANAGEMENT blue screen on Windows 11?"
    a: "Stop code 0x0000001A fires when Windows' memory manager detects corruption in how memory is allocated or tracked. The usual suspects are faulty RAM sticks, a driver writing to memory it doesn't own, corrupted system files, or a failing storage drive feeding bad data into memory."
  - q: "How do I know if it's my RAM or a driver?"
    a: "Pattern is everything. Crashes that name different drivers each time, or happen randomly with no trigger, point at RAM. Crashes that always involve the same .sys file or happen during one specific activity (gaming, video calls) point at a driver. When in doubt, test the RAM first — it's the definitive check."
  - q: "Can a Windows update cause MEMORY_MANAGEMENT errors?"
    a: "Yes — feature updates replace drivers and change memory manager behavior, which can expose a marginal RAM stick or an incompatible driver that previously got away with bad behavior. If the crashes started right after an update, update your drivers and test the RAM."
  - q: "Will adding more RAM fix this error?"
    a: "No. This error is about memory corruption, not memory shortage. Adding RAM won't help and could even complicate diagnosis. Fix the faulty stick or the misbehaving driver first."
---
The MEMORY_MANAGEMENT blue screen (stop code 0x0000001A) is Windows' memory manager catching something writing where it shouldn't, or finding its own bookkeeping corrupted. On a laptop, that usually means one of two things: a RAM stick going bad, or a driver corrupting memory behind the scenes.

The tricky part is that both causes produce identical-looking crashes. The fixes below are ordered to separate them efficiently — you'll either find the bad hardware or the bad driver without wasting a weekend on the wrong one.

## Why this happens

- **Faulty RAM.** A dying memory stick flips bits randomly, corrupting whatever Windows stored there — the single most common cause.
- **A driver corrupting memory.** Buggy graphics, network, or storage drivers can write outside their allocated memory and trip the memory manager's corruption checks.
- **Corrupted system files.** Damage to Windows' own memory management components produces the same stop code from legitimate operations.
- **Failing storage drive.** A drive returning corrupted data poisons the memory pages Windows caches from it.
- **Overclocked or mismatched RAM.** XMP profiles that aren't quite stable, or mixed RAM sticks with different timings, cause intermittent corruption under load.
- **Disk-level corruption in the page file.** A damaged pagefile.sys means the virtual memory Windows swaps to disk comes back corrupted.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Run the Windows Memory Diagnostic

Start with the definitive RAM check — it's built in and takes under half an hour.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the standard test run to completion. If it reports **hardware problems were detected**, you've found your cause — skip to Fix 4.
4. If it passes, don't celebrate yet: the built-in test is quick but not exhaustive. For the full guide to interpreting memory test results, see our [memory management troubleshooting walkthrough](/articles/memory-management-bsod-troubleshooting/).

### Fix 2: Update your drivers, especially graphics and chipset

A single bad driver is the most common non-RAM cause.

1. Press **Win + X** and open **Device Manager**.
2. Update drivers under **Display adapters**, **Network adapters**, and **System devices** (right-click each > **Update driver > Search automatically for drivers**).
3. Then visit your laptop maker's support site and install the latest chipset and graphics drivers for your exact model — manufacturer drivers are tested against your specific hardware.
4. If crashes began after a recent driver update, roll that driver back instead: **Properties > Driver tab > Roll Back Driver**.
5. Restart and use the laptop normally for a day before declaring victory.

### Fix 3: Repair system files and check the disk

Eliminate software-side corruption in one pass.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and wait for it to finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` (needs internet).
4. Check the drive itself: `chkdsk C: /f` — type **Y** if prompted, then restart so the scan runs at boot.
5. These steps also resolve the closely related [stop code memory management variants](/articles/how-to-fix-stop-code-memory-management/) that share the same root causes.

### Fix 4: Reseat or replace the RAM

If the memory diagnostic found errors, act on it.

1. Power off, unplug, and (if your battery is removable) remove the battery. On sealed laptops, just ensure it's fully off.
2. Open the RAM compartment (check your model's manual — some ultrabooks have soldered RAM that can't be serviced).
3. Remove each stick, blow out the slots with compressed air, and reseat the sticks firmly until the clips click.
4. If you have two sticks, test with one at a time to identify the bad one. A stick that fails consistently needs replacing — match the specs (DDR4/DDR5, speed, voltage) of the working stick.
5. While you're in there, make sure you're not mixing sticks with different timings, which causes exactly this kind of intermittent corruption.

### Fix 5: Run an extended memory test with MemTest86

For crashes that persist despite a passing Windows diagnostic.

1. Download MemTest86 and create a bootable USB drive.
2. Boot from the USB (usually **F12** or **Esc** at the logo screen for a boot menu).
3. Run at least **two full passes** — this takes a few hours but catches intermittent faults the quick test misses.
4. Any red errors mean the RAM is bad, even if Windows' own test passed. Replace the faulty stick.

### Fix 6: Reset the page file and check virtual memory settings

A corrupted page file can masquerade as a RAM problem.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to the **Advanced** tab and click **Settings** under **Performance**.
3. In the new window, go to **Advanced > Virtual memory > Change**.
4. Uncheck **Automatically manage paging file size for all drives**, select **No paging file**, and click **Set**. Restart.
5. Go back to the same dialog, re-enable **Automatically manage paging file size for all drives**, click **Set**, and restart again. This deletes and recreates pagefile.sys from scratch.

### Fix 7: Clean-install Windows as a last resort

If the RAM passes extended testing and drivers are current, the installation itself may be corrupt beyond repair.

1. Back up everything.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Remove everything** with **Cloud download**.
3. After setup, run the memory diagnostic once more on the clean system. If crashes continue on a fresh install with passing RAM tests, you're looking at a motherboard-level fault — time for professional diagnosis. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the reset process step by step.

## Closing

MEMORY_MANAGEMENT crashes come down to a simple fork in the road: bad RAM or a bad driver corrupting RAM. Test the memory first with the built-in diagnostic (and MemTest86 if needed), update your drivers, and repair system files — that sequence identifies the culprit for nearly everyone. And remember: this error is about corruption, not capacity, so don't let anyone sell you more RAM as the fix.
