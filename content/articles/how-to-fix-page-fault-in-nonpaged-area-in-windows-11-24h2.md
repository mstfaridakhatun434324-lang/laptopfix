---
title: "Page Fault in Nonpaged Area in Windows 11 24H2: How to Fix It"
slug: how-to-fix-page-fault-in-nonpaged-area-in-windows-11-24h2
date: 2026-09-18
categories: ["windows-errors"]
tags: ["windows 11 24h2", "page fault", "bsod"]
description: "PAGE_FAULT_IN_NONPAGED_AREA crashing Windows 11 24H2? Here is what the stop code really means, plus the driver, RAM, and disk fixes that resolve it."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-in-windows-11-24h2.webp"
faqs:
  - q: "Does this stop code always mean my RAM is dying?"
    a: "No — despite the memory-sounding name, drivers cause it more often than hardware. The name describes where the fault was detected (the nonpaged pool), not what caused it. Always investigate the driver angle first; reach for MemTest86 only when dumps implicate the kernel itself or no third-party driver appears."
  - q: "Why did this start right after updating to 24H2?"
    a: "Windows 11 24H2 reworked parts of memory management and driver enforcement. Drivers that worked on 23H2 by bending the rules can now trip faults. The fix is the same as any driver-caused crash: update the implicated driver to a 24H2-certified version from the manufacturer."
  - q: "Can a virus cause PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Rarely directly, but malware can corrupt drivers or install malicious filter drivers that cause it. More commonly, it is the antivirus itself — specifically its file-system filter driver — rather than malware. Run a Defender offline scan to rule malware out, then look at drivers."
  - q: "How is this different from MEMORY_MANAGEMENT?"
    a: "Both are memory-related stop codes, but PAGE_FAULT_IN_NONPAGED_AREA specifically means something touched invalid memory in the nonpaged pool — it names a precise event. MEMORY_MANAGEMENT is a broader corruption-of-memory-structures code. The former points at drivers first; the latter points at RAM first."
---

PAGE_FAULT_IN_NONPAGED_AREA is Windows telling you that something tried to read memory that was guaranteed to be there — and it was not. The nonpaged area is memory the system promises never to swap to disk, so a fault there means a driver asked for data at a wrong address, the RAM returned garbage, or the page tables themselves are corrupt. On Windows 11 24H2, this stop code shows up most often after driver updates or on machines with aging memory.

The name sounds like a RAM death sentence, but drivers cause this crash more often than hardware does. The strategy: identify the faulting driver from the dump if you can, update or remove the usual suspects, test the memory, and check the disk. In that order.

## Why this happens

- **A faulty device driver:** the most common cause — a driver referencing freed or invalid memory, often the storage, network, or graphics driver after an update.
- **Failing or mismatched RAM:** bad memory cells in the nonpaged pool region produce exactly this fault, especially on laptops that run hot.
- **Corrupted page file or disk errors:** a damaged pagefile.sys or bad sectors where the system expects valid data can trigger the fault.
- **Antivirus filter drivers:** third-party antivirus installs file-system filter drivers that operate in the nonpaged area; a buggy filter crashes the system.
- **Windows 11 24H2 driver incompatibilities:** the 24H2 update tightened memory management, and older drivers that bent the rules on 23H2 now break them.
- **Overclocked or undervolted hardware:** unstable memory timings or aggressive undervolts corrupt kernel memory under load.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Read the dump to name the driver

The crash dump usually fingers the culprit. Ten minutes with WinDbg saves hours of guessing.

1. After the next crash and reboot, open `C:\Windows\Minidump` and note the newest `.dmp` file.
2. Install **WinDbg Preview** from the Microsoft Store, open the dump, and run `!analyze -v`.
3. Find the **IMAGE_NAME** line — e.g. `ntfs.sys` (disk/file system), `nvlddmkm.sys` (NVIDIA), `Netwtw10.sys` (Intel Wi-Fi), or a third-party `.sys`.
4. If it names `ntoskrnl.exe` or `ntfs.sys` with no third-party driver, suspect RAM or disk instead and jump to Fix 5.
5. Write down the driver name — every fix below is more effective when aimed at the right target.

### Fix 2: Update or roll back the suspect driver

Drivers cause most of these crashes, so the driver is the first thing to change. Direction depends on timing.

1. Open **Device Manager** (right-click **Start**), locate the device matching the dump's driver name.
2. If crashes began after a driver or Windows update: **Properties > Driver tab > Roll Back Driver**.
3. Otherwise: **Update driver > Search automatically**, then check **Settings > Windows Update > Advanced options > Optional updates**.
4. For the authoritative version, go to the source: [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html), the [NVIDIA download page](https://www.nvidia.com/Download/index.aspx), or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
5. Restart and stress the scenario that crashed before (the game, the file copy, the wake-from-sleep). One clean day is a good sign; one clean week is confirmation.

### Fix 3: Remove or update third-party antivirus

Antivirus filter drivers live in the nonpaged area by design, which makes them prime suspects for this exact stop code.

1. If you run third-party antivirus, update it to the latest version first — vendors patch filter-driver bugs regularly.
2. If crashes persist, uninstall it temporarily and rely on **Microsoft Defender** (which is automatically re-enabled).
3. Use the vendor's dedicated removal tool, not just Settings uninstall — leftover filter drivers are the ones that crash.
4. Test for several days on Defender alone. If the crashes stop, the antivirus was the cause; try a fresh install of its latest version or switch products.
5. Never run two real-time antivirus products at once — their filter drivers fight each other in exactly the memory region this stop code is about.

### Fix 4: Disable automatic paging tweaks and check virtual memory

A manually misconfigured page file can contribute. Let Windows manage it.

1. Press **Win + R**, type `sysdm.cpl`, go to the **Advanced** tab, and under Performance click **Settings**.
2. On the **Advanced** tab of Performance Options, click **Change** under Virtual memory.
3. Tick **Automatically manage paging file size for all drives** and click OK. Restart.
4. If you previously disabled the page file for SSD longevity reasons, re-enable it — some drivers assume it exists, and its absence causes precisely this class of fault.
5. This is a supporting fix, not a primary one — pair it with the driver work above.

### Fix 5: Test the RAM thoroughly

When dumps blame the kernel or ntfs.sys with no third-party driver in sight, test the memory. Do this properly — quick tests miss intermittent faults.

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Let the standard test complete. If it reports errors, you have found it — but a pass does not fully clear the RAM.
3. For a definitive test, create a **MemTest86** USB on another PC (free edition), boot from it, and run at least 2 full passes (several hours).
4. If errors appear: power off, reseat the RAM modules, and retest. On laptops with soldered RAM, errors mean a board-level repair.
5. Also revert any RAM overclocking or XMP profiles in BIOS while testing — unstable timings are a classic cause of nonpaged faults.

### Fix 6: Check the disk and system files

Disk corruption feeding bad data to the memory manager produces the same symptom as bad RAM. Check the storage.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r`. Reboot if it schedules the scan.
2. Then run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check the drive's SMART health: open an elevated prompt and run `wmic diskdrive get status` — anything other than OK warrants a backup and replacement plan.
4. If chkdsk keeps finding new errors on every run, the drive is deteriorating — clone it to a new SSD rather than continuing to repair it.
5. The broader [blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers dump analysis in more depth if your dumps keep pointing at ntfs.sys.

### Fix 7: Clean-install the implicated driver stack

When one driver resists update and rollback both, strip the whole related stack and reinstall clean.

1. Download Display Driver Uninstaller (DDU) on another PC if the suspect is the GPU driver; for network or storage, get the fresh driver installer first.
2. Boot into Safe Mode ([guide](/articles/how-to-boot-windows-11-in-safe-mode/)), run DDU with **Clean and restart** for GPU cases.
3. For other drivers: in Safe Mode's Device Manager, **Uninstall device** with **Delete the driver software** ticked for each related device.
4. Reboot normally and install the fresh drivers from the manufacturer sources in Fix 2 — one at a time, testing between each.
5. Check Microsoft's Windows support hub for any 24H2-specific known issues with your hardware before declaring victory.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA rewards methodical work: read the dump, fix the named driver, and only then suspect the hardware. Most 24H2 cases resolve at the driver layer — an update, a rollback, or removing a misbehaving antivirus filter. Save the multi-hour memory tests for when the dumps genuinely point nowhere, and you will fix this faster than the scary name suggests.
