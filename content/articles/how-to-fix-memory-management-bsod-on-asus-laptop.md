---
title: "MEMORY_MANAGEMENT Blue Screen on an Asus Laptop? Fix It"
slug: how-to-fix-memory-management-bsod-on-asus-laptop
date: 2026-09-25
categories: ["windows-errors"]
tags: ["blue screen", "memory", "asus"]
description: "MEMORY_MANAGEMENT blue screens on your Asus laptop point at RAM or driver trouble. Test your memory and apply these fixes to stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-memory-management-bsod-on-asus-laptop.webp"
faqs:
  - q: "What causes the MEMORY_MANAGEMENT blue screen?"
    a: "Stop code 0x0000001A means Windows' memory manager detected corruption — usually faulty RAM, a bad driver corrupting memory, or disk errors in the paging area. On Asus laptops, unstable Armoury Crate or Aura drivers occasionally contribute."
  - q: "How do I know if it's the RAM or a driver?"
    a: "Run Windows Memory Diagnostic first. If RAM passes but crashes continue, suspect drivers — especially after a recent update. Crashes in Safe Mode point at hardware; crashes only in normal mode point at drivers."
  - q: "Can I fix this without opening the laptop?"
    a: "Often yes. Driver updates, SFC/DISM repairs, and disabling the page file rebuild solve many cases. You only need to open the laptop if testing proves a RAM stick is faulty and it's user-replaceable."
  - q: "Will this error damage my files?"
    a: "The crash itself doesn't target files, but memory corruption can garble data being written when the crash hits. Save work frequently while diagnosing, and back up before running overnight memory tests."
---
MEMORY_MANAGEMENT (stop code 0x0000001A) is Windows catching its memory manager in a corrupted state and stopping before things get worse. On Asus laptops, the usual culprits are faulty RAM, a driver scribbling where it shouldn't, or disk problems in the paging area. The name points at memory, but don't order new RAM until you've tested — drivers cause this just as often.

Work through these fixes in order, from testing to repair. If your blue screen names a specific driver file instead, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) shows how to decode it.

## Why this happens

- **Faulty RAM modules.** Bad cells corrupt data the memory manager trusts.
- **Buggy device drivers.** Drivers that corrupt pool memory trigger this stop code.
- **Corrupted page file.** Damage to `pagefile.sys` breaks virtual memory.
- **Disk errors.** Bad sectors in paging areas look like memory corruption.
- **Overclocked RAM.** XMP profiles that aren't stable cause intermittent corruption.
- **Asus utility conflicts.** Armoury Crate, Aura Sync, and MyAsus drivers occasionally cause memory issues after updates.
- **Corrupted system files.** Damage to the memory manager's own files.

## How to fix it

Work through these in order — test stability after each.

### Fix 1: Run Windows Memory Diagnostic

Start with the free built-in RAM test.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the standard test complete (10-20 minutes).
4. After rebooting, open **Event Viewer > Windows Logs > System** and filter for **MemoryDiagnostics-Results**.
5. If errors are found, reseat the RAM modules if accessible, then retest.
6. If errors persist, replace the faulty stick. Check your Asus model's manual for the correct DDR generation and speed — mixing specs causes its own problems.

### Fix 2: Run MemTest86 for a definitive answer

The Windows tool can miss intermittent faults; MemTest86 rarely does.

1. On another PC, download MemTest86 from its official site and create a bootable USB.
2. Boot the Asus laptop from the USB (press **Esc** during boot for the boot menu).
3. Let it run at least 4 full passes — this takes several hours, so run it overnight.
4. Any red errors mean bad RAM, full stop.
5. If your Asus has two slots, test each stick alone to identify the culprit.
6. Replace faulty modules with matched pairs when possible — matched RAM is more stable than mixed sticks.

### Fix 3: Update drivers from Asus, not Windows Update

Asus-tuned drivers fix conflicts the generic ones miss.

1. Go to the official Asus support website and look up your exact model.
2. Download the latest chipset, storage, and graphics drivers for your Windows version.
3. Install the chipset driver first, then storage, then graphics — rebooting between each.
4. In **Device Manager**, check for any yellow warning icons and resolve those.
5. If crashes started right after a driver update, use **Properties > Driver > Roll Back Driver** on the suspect device instead.
6. Update **Armoury Crate** and **MyAsus** from the Microsoft Store too — outdated Asus utilities are a known trigger.

### Fix 4: Rebuild the page file

A corrupted page file mimics RAM failure.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to **Advanced > Settings** (under Performance) **> Advanced > Change** (under Virtual memory).
3. Uncheck **Automatically manage paging file size for all drives**.
4. Select **No paging file**, click **Set**, **OK**, and restart.
5. Return to the same dialog, re-check **Automatically manage paging file size for all drives**, click **Set**, and restart again.
6. Windows builds a fresh `pagefile.sys`. If crashes stop, the old page file was corrupt — also run `chkdsk C: /f` to check why it corrupted.

### Fix 5: Check the disk

Paging-area disk errors cause this exact stop code.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Run:
   `chkdsk C: /f /r`
3. Type **Y** to schedule at restart if prompted, then reboot and let it finish.
4. Afterward, check drive health: `wmic diskdrive get status` should report **OK**.
5. For NVMe drives, check the manufacturer's toolbox for health percentage and temperature history.
6. If the drive is failing, replace it — continuing on a dying drive risks both crashes and data loss. Our [NTFS.SYS guide](/articles/how-to-fix-ntfs-sys-blue-screen-on-lenovo-laptop/) covers storage-focused crashes in more depth.

### Fix 6: Repair system files

Rule out corruption in Windows' own memory management files.

1. Open an elevated terminal.
2. Run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Then:
   `sfc /scannow`
4. Restart when SFC completes.
5. If SFC reports unfixable corruption, run it again in Safe Mode — fewer locked files means better repair odds.
6. Microsoft documents these tools on [support.microsoft.com](https://support.microsoft.com/en-us/windows) if you want the official walkthrough.

### Fix 7: Disable XMP and test at stock RAM speeds

Unstable memory overclocks are a classic intermittent cause.

1. Restart and enter BIOS/UEFI (press **F2** or **Del** during Asus boot).
2. Find the memory settings — often under **Advanced > Memory** or in **Ai Tweaker**.
3. Disable **XMP** (Intel) or **DOCP** (AMD) profiles.
4. Set memory to **Auto** / JEDEC standard speeds.
5. Save (**F10**) and boot into Windows.
6. Use the laptop for a few days. If crashes stop, the XMP profile was unstable on your modules — either keep stock speeds or manually loosen timings. If crashes continue at stock speeds with tested-good RAM, suspect the motherboard's memory controller and contact Asus support.

## Closing

MEMORY_MANAGEMENT rewards methodical testing: prove the RAM good or bad with MemTest86, then chase drivers and the page file. On Asus laptops specifically, keep Armoury Crate and the Asus-provided chipset drivers current — they're involved in more of these crashes than people expect. And remember that "memory management" in the stop code describes where Windows noticed the corruption, not necessarily where it started; drivers are guilty just as often as RAM. Work the ladder patiently and retest after every change — intermittent memory faults need a few days of normal use before you can declare victory.
