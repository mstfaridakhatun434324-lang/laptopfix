---
title: "How to Fix KERNEL_MODE_HEAP_CORRUPTION the Smart Way"
slug: best-way-to-fix-kernel-mode-heap-corruption
date: 2026-10-08
categories: ["windows-errors"]
tags: ["kernel-mode-heap-corruption", "bsod", "driver"]
description: "KERNEL_MODE_HEAP_CORRUPTION means a driver corrupted kernel memory. Here is the smart fix order: identify the driver, then fix or remove it."
thumbnail: "/images/thumbs/best-way-to-fix-kernel-mode-heap-corruption.webp"
faqs:
  - q: "What is the kernel heap and why does corrupting it crash Windows?"
    a: "The kernel heap is memory the Windows kernel hands out to drivers for their internal data. If a driver writes past its allocation or frees the same block twice, the heap's bookkeeping is destroyed. Windows detects this on the next allocation and crashes deliberately (stop code 0x13A) rather than continue with corrupted kernel memory."
  - q: "Which drivers most often cause heap corruption?"
    a: "Graphics drivers lead the list, followed by network (Wi-Fi/Ethernet) drivers, storage controller drivers, and antivirus filter drivers. These all allocate heavily from the kernel heap, so their bugs surface here first. USB device drivers for docks and peripherals are another frequent source on laptops."
  - q: "Can I just ignore it if it only happens rarely?"
    a: "You should not. Heap corruption is progressive — the corrupting driver keeps corrupting, and crashes get more frequent over time. Rare crashes also risk silent data corruption before the crash. Treat the first occurrence as the warning it is and fix it now."
  - q: "Does Driver Verifier help with heap corruption?"
    a: "It is the single best tool for it. Verifier's special pool option makes the corrupting driver crash immediately at the moment of corruption, with the driver's name in the dump — instead of crashing later in an innocent driver. That turns a mystery into a named suspect."
---
KERNEL_MODE_HEAP_CORRUPTION (stop code 0x13A) is one of the more honest blue screens: it tells you exactly what happened — a driver trashed memory belonging to the kernel. The dishonest part is that the crash usually happens later, in a completely innocent driver, long after the real culprit did its damage. KERNEL_MODE_HEAP_CORRUPTION (stop code 0x13A) is one of the more honest blue screens: it tells you exactly what happened — a driver trashed memory belonging to the kernel. The dishonest part is that the crash usually happens later, in a completely innocent driver, long after the real culprit did its damage.

The smart way to fix it is not to reinstall drivers blindly. It is to make the guilty driver crash at the scene of the crime, using Driver Verifier — then fix that specific driver. The smart way to fix it is not to reinstall drivers blindly. It is to make the guilty driver crash at the scene of the crime, using Driver Verifier — then fix that specific driver.

## Why this happens

- **A buggy graphics driver.** The heaviest kernel-heap user on most laptops, and the most common corrupter.
- **Faulty network drivers.** Wi-Fi drivers allocate constantly; a buffer bug corrupts the heap quickly.
- **Antivirus filter drivers.** They intercept nearly every I/O operation, giving their bugs maximum opportunity.
- **USB dock and peripheral drivers.** Laptop docks with display, network, and audio drivers are a dense source of heap bugs.
- **Corrupted driver binaries on disk.** A damaged .sys file misbehaves in ways its developers never intended.
- **Bad RAM.** Memory errors corrupt heap structures directly, mimicking a driver bug — always worth ruling out.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Enable Driver Verifier with Special Pool

This is the key move: Verifier makes the corrupting driver crash instantly instead of corrupting silently. Special Pool places each driver's allocations on isolated pages with guard pages around them, so an overrun crashes instantly at the offending driver instead of corrupting silently.

1. Press **Win + R**, type `verifier`, and press **Enter**.
2. Choose **Create custom settings (for code developers)**, click **Next**, and tick **Special pool** (plus **Pool tracking** and **Force IRQL checking** for good measure).
3. Choose **Select driver names from a list** and tick every non-Microsoft driver.
4. Click **Finish** and restart. Use the laptop normally — the next crash will name the actual corrupting driver.

### Fix 2: Read the Verifier-induced crash dump

The dump now contains the answer instead of a mystery. The dump now contains the answer instead of a mystery — note that without Verifier, this same crash would likely have named an innocent driver.

1. After the crash, open the newest file in `C:\Windows\Minidump` with WinDbg Preview from the Microsoft Store.
2. Run `!analyze -v` and read the IMAGE_NAME line — that driver corrupted the heap.
3. Search the filename to identify its product. Write it down; this is your target for the remaining fixes.

### Fix 3: Update or replace the guilty driver

Precision strike instead of carpet bombing. Precision strike instead of carpet bombing: you are fixing the one driver proven guilty rather than updating everything and hoping.

1. If it is a hardware driver, get the newest version from the device maker's site — for graphics, [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), [AMD's driver page](https://www.amd.com/en/support/download/drivers.html), or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. If it is already the newest, try the previous version — new drivers introduce heap bugs too.
3. For antivirus or dock drivers, do a clean reinstall of the product, or uninstall it temporarily to confirm the crashes stop.
4. Then disable Verifier: run `verifier /reset` in an elevated prompt and restart. Never leave Verifier running permanently.

### Fix 4: Test the RAM to rule out hardware

If Verifier crashes keep naming different drivers, the heap is being corrupted by bad memory, not a driver. If Verifier crashes keep naming different drivers, the heap is being corrupted by bad memory, not a driver — that inconsistency is the whole diagnostic signal.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. If errors appear, reseat or replace the RAM. Our [memory management guide](/articles/memory-management-bsod-windows-11-fix/) walks through full RAM diagnosis.
4. If the quick test passes but suspicion remains, run MemTest86 overnight for certainty.

### Fix 5: Repair system files

A corrupted kernel binary can corrupt its own heap. A corrupted kernel binary can corrupt its own heap, which is why this step comes before you conclude the hardware is at fault.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. This is quick and rules out Windows' own files as the corrupter.

### Fix 6: Disconnect docks and USB peripherals

Laptop docks are a concentrated source of third-party kernel drivers. Unplug every USB device, dock, and external monitor — laptop docks pack display, network, and audio drivers into one very suspicious package.

1. Unplug every USB device, dock, and external monitor.
2. Use the laptop standalone for a day or two.
3. If crashes stop, reconnect devices one at a time, waiting a day between each, to find the one whose driver corrupts the heap.
4. Update that device's driver from its maker before reconnecting permanently. For general crash-screen reading, see our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 7: Check for a BIOS or chipset update

An outdated BIOS or chipset driver can mishandle the memory mappings that heap allocations depend on, producing corruption no driver update will fix.

1. Visit your laptop maker's support site and compare your BIOS version (`msinfo32` > **BIOS Version/Date**) against the latest.
2. Install the newest chipset driver package for your exact model — not the generic one from Windows Update.
3. Flash the BIOS only on AC power, and leave the machine untouched until it reboots itself.
4. Retest for several days: BIOS-level memory handling fixes resolve a small but real slice of persistent 0x13A crashes.

## Closing

KERNEL_MODE_HEAP_CORRUPTION rewards the methodical: Driver Verifier with Special Pool turns a who-did-it mystery into a named driver, and from there it is a straightforward driver fix. Skip the Verifier step and you will chase ghosts — use it, and you will know the culprit by name within a day. Work the list in order and resist the urge to skip the Verifier step — it feels like extra work, but it is the difference between a one-day fix and a two-week driver lottery.
