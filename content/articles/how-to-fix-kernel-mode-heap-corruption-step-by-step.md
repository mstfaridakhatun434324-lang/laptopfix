---
title: "How to Fix KERNEL_MODE_HEAP_CORRUPTION, Step by Step"
slug: how-to-fix-kernel-mode-heap-corruption-step-by-step
date: 2026-09-07
categories: ["windows-errors"]
tags: ["bsod", "drivers", "memory"]
description: "KERNEL_MODE_HEAP_CORRUPTION blue screen? A driver corrupted kernel memory. Here's the step-by-step process to find and fix it."
thumbnail: "/images/thumbs/how-to-fix-kernel-mode-heap-corruption-step-by-step.webp"
faqs:
  - q: "What does KERNEL_MODE_HEAP_CORRUPTION mean?"
    a: "A kernel-mode driver wrote outside its allocated memory in the kernel heap, corrupting neighboring data structures. Windows detects the corruption and bugchecks (stop code 0x13A). It's a driver bug in the overwhelming majority of cases — usually graphics, network, or storage drivers."
  - q: "Is this a hardware problem?"
    a: "Usually not. Genuine heap corruption is a software bug — a driver writing where it shouldn't. Bad RAM can produce similar crashes, but driver causes outnumber hardware causes heavily for this specific stop code. Test drivers first, memory second."
  - q: "Why does it happen mostly when gaming or under load?"
    a: "GPU and network drivers allocate and free kernel heap constantly during heavy use. A driver with a use-after-free or buffer-overflow bug only corrupts the heap when it's churning through allocations — which is exactly what gaming and heavy workloads do."
  - q: "Can Driver Verifier make this worse?"
    a: "Driver Verifier intentionally stresses drivers and will crash the system sooner when a buggy driver is present — that's its job. The crashes it produces name the driver clearly. Just remember to turn Verifier off afterward from Safe Mode."
---

`KERNEL_MODE_HEAP_CORRUPTION` (stop code 0x13A) means a driver wrote to kernel memory it didn't own, scrambling data structures other parts of Windows depend on. When the memory manager later trips over the damage, it halts the system rather than continue on corrupted foundations.

This is a driver's bug, almost by definition — the heap doesn't corrupt itself. Your job is identifying which driver, and the most reliable tool for that is Driver Verifier combined with crash dump analysis. Here's the full process.

## Why this happens

- **Buggy graphics driver**: The leading cause. GPU drivers do heavy kernel heap allocation, and a use-after-free or overflow bug corrupts the heap under load.
- **Faulty network driver**: Wi-Fi/Ethernet drivers allocate packet buffers in the kernel heap constantly; buggy ones corrupt it.
- **Bad storage controller driver**: Less common, but AHCI/NVMe driver bugs produce the same crash, often during large file operations.
- **Corrupted driver binaries**: Damaged .sys files behave like buggy ones — they write to wrong addresses.
- **Incompatible driver after Windows update**: A driver validated against an older kernel's heap layout breaks under the new one.
- **Failing RAM (minority of cases)**: Bad memory can corrupt heap contents, mimicking a driver bug. Worth testing after drivers check out.

## How to fix it

Work through these in order — dump analysis first, then targeted driver work.

### Fix 1: Read the crash dump for the suspect

Start with evidence, not guesses.

1. Install **BlueScreenView** (NirSoft, free) and open `C:\Windows\Minidump`.
2. Check the latest dump's **Caused By Driver** field. For heap corruption, the named driver is often the allocator that detected the damage — close to, if not exactly, the culprit.
3. Note the pattern: does it crash during gaming (GPU suspect), large downloads (network suspect), or file copies (storage suspect)?
4. If dumps consistently name `ntoskrnl.exe`, the kernel found someone else's corruption — proceed to Driver Verifier in Fix 4.
5. Background reading: our [DRIVER_IRQL_NOT_LESS_OR_EQUAL guide](/articles/driver-irql-not-less-or-equal-blue-screen-error-fix/) covers similar dump-reading technique for another driver crash.

### Fix 2: Update the graphics driver with a clean install

The GPU driver is suspect number one — update it thoroughly.

1. Download the latest driver: [NVIDIA](https://www.nvidia.com/Download/index.aspx) for GeForce, [AMD](https://www.amd.com/en/support/download/drivers.html) for Radeon, [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics.
2. During installation, select **Custom** > check **Perform a clean installation** (NVIDIA) or use the **Factory Reset** option (AMD).
3. For a truly clean slate, use **Display Driver Uninstaller (DDU)** in Safe Mode first — it removes every trace of the old driver, including registry leftovers and profiles.
4. Restart and stress-test with the workload that triggered crashes.
5. If the newest driver still crashes, try one version older — occasionally the latest release introduces the heap bug.

### Fix 3: Update network and chipset drivers

If the GPU driver isn't the cause, network and chipset drivers are next.

1. Open **Device Manager** (**Win + X** > **Device Manager**) and update everything under **Network adapters**.
2. Install the full chipset driver package from your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Update storage controller drivers under **IDE ATA/ATAPI controllers** and **Storage controllers**.
4. Restart and retest. Our [24H2 heap corruption variant guide](/articles/how-to-fix-kernel-mode-heap-corruption-in-windows-11-24h2/) covers update-specific wrinkles if this began after a feature update.

### Fix 4: Run Driver Verifier with special pool

Driver Verifier catches heap corruptors red-handed by placing driver allocations in guarded memory.

1. Press **Win + R**, type `verifier`, press Enter.
2. Choose **Create custom settings**, enable **Special pool**, **Pool tracking**, and **Force IRQL checking**, then **Select driver names from a list**.
3. Select third-party drivers — especially graphics, network, and any driver your dumps hinted at. (Don't select all Microsoft drivers; that slows the system to a crawl.)
4. Click **Finish** and restart. Use the laptop normally — Verifier will crash it with a specific stop code (often SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION) naming the driver.
5. After identifying the culprit, boot into Safe Mode, run `verifier`, choose **Delete existing settings**, and update or remove that driver.
6. Warning: Verifier makes the system slower and crash-prone by design. Don't leave it on.

### Fix 5: Roll back recent driver updates

If crashes started after a driver update, revert it.

1. In **Device Manager**, right-click the suspect device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If unavailable, uninstall the device (check **Delete the driver software**), restart, and install the previous known-good version from the manufacturer's archive.
3. Use Microsoft's **Show or hide updates** troubleshooter to block the bad version from reinstalling via Windows Update.

### Fix 6: Test RAM to rule out hardware

If Verifier and dumps keep pointing at the kernel itself, test memory.

1. Run `mdsched.exe` (**Win + R**) > **Restart now and check for problems**.
2. For conclusive results, run MemTest86 overnight from USB.
3. Also run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt — corrupted system files can mimic heap corruption.
4. Reseat RAM modules if accessible; reseat the SSD too, since storage corruption of driver files produces identical symptoms.

### Fix 7: Check for conflicting software

Some software installs kernel drivers that corrupt the heap.

1. Uninstall third-party antivirus temporarily (its filter drivers are a known heap-corruption source) and test with Defender.
2. Remove or update: VPN clients, disk encryption tools, RGB/fan utilities, and game anti-cheat systems — all install kernel drivers.
3. Perform a clean boot (**Win + R** > `msconfig` > hide Microsoft services > **Disable all**, plus disable startup items in Task Manager) and re-enable in halves to isolate the offender.
4. As a last resort, an in-place upgrade from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) refreshes every system driver while keeping files and apps.

## Closing

KERNEL_MODE_HEAP_CORRUPTION is Windows catching a driver misbehaving with kernel memory — and the fix is almost always finding that driver. Read the dumps, clean-install the GPU driver, update network and chipset drivers, and let Driver Verifier name the culprit if the obvious suspects check out. It's detective work, but it ends with a stable system, not a reinstall.
