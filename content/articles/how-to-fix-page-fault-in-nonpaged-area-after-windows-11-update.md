---
title: "Fix PAGE_FAULT_IN_NONPAGED_AREA After a Windows 11 Update"
slug: how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update
date: 2026-09-27
categories: ["windows-errors"]
tags: ["page fault in nonpaged area", "blue screen", "windows 11 update"]
description: "Fix the PAGE_FAULT_IN_NONPAGED_AREA blue screen after a Windows 11 update: test RAM, update storage drivers, and repair the pagefile."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA mean?"
    a: "Stop code 0x00000050 means Windows tried to read memory from the nonpaged area — memory that must always be present — and found it missing or invalid. The usual causes are faulty RAM, a bad storage or antivirus driver, or disk corruption affecting the pagefile."
  - q: "The blue screen names a .sys file — what do I do?"
    a: "That file is almost certainly your culprit. Search the filename to identify its driver (often ntfs.sys, storport.sys, or an antivirus filter), then update or reinstall that specific driver. A named file turns a guessing game into a targeted fix."
  - q: "Can a Windows update really cause this?"
    a: "Yes — updates replace storage drivers and kernel components, and a bad or incompatible storage driver is one of the top triggers of 0x50. If the crash started within days of an update, treat drivers as suspect number one."
  - q: "Is my hard drive dying?"
    a: "Possibly, but not necessarily. Run chkdsk C: /f /r first — if it reports many bad sectors, back up immediately. If the disk is clean, the cause is far more likely a driver or RAM issue."
---

PAGE_FAULT_IN_NONPAGED_AREA (0x00000050) is Windows discovering that memory it was promised would always be there… was not. The nonpaged area holds critical kernel data that can never be swapped to disk, so a fault there means something is deeply wrong: bad RAM, a corrupt driver, or disk damage in the wrong place.

After a Windows 11 update, storage drivers are the prime suspect — the update swaps them out, and a bad one starts faulting immediately. Here is how to pin it down.

## Why this happens

- **Bad storage driver from the update:** New AHCI/NVMe or Intel RST drivers with bugs fault when accessing nonpaged pool memory.
- **Failing RAM:** A bad cell in the nonpaged region produces this exact stop code, often intermittently.
- **Antivirus filter drivers:** Outdated security software hooks file access at the kernel level; after an update these hooks can fault.
- **Disk corruption:** Bad sectors or a corrupted NTFS structure in critical areas trigger 0x50 during file operations.
- **Corrupted pagefile:** A damaged pagefile confuses the memory manager even though the fault is technically in the nonpaged area.
- **Faulty hardware recently added:** New RAM sticks or SSDs that are marginal can start faulting under the new driver stack.

- **Borderline RAM overclocking:** XMP profiles that are almost-but-not-quite stable tend to fault specifically in nonpaged pool under load — exactly where this stop code lives.
## How to fix it

Work through these in order — check the named driver first if the blue screen gave you one.

### Fix 1: Identify the named driver on the blue screen

1. The next time it crashes, note any **.sys filename** on the blue screen (photograph it — it disappears fast). Consider disabling [automatic restart](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) so the screen stays up.
2. Common names: `ntfs.sys` (file system), `storport.sys` / `stornvme.sys` (storage), `ndis.sys` (network), or an antivirus filter like `fltMgr`-adjacent third-party files.
3. Search the filename online to identify the exact driver and its vendor.
4. Update that specific driver first — a named culprit makes this the highest-probability fix on the list.

### Fix 2: Update storage drivers from the manufacturer

1. Open **Device Manager → Storage controllers** and **IDE ATA/ATAPI controllers**.
2. Note the current driver versions, then visit your laptop maker's support page for the latest chipset and storage drivers for your exact model.
3. Install them — especially **Intel Rapid Storage Technology (RST)** or AMD chipset drivers if your laptop uses them.
4. Restart and test. Storage drivers are the most common 0x50 trigger after a Windows update, so do this even if no file was named.

### Fix 3: Run chkdsk on the system drive

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r`.
2. Type **Y** to schedule it, restart, and let the scan run (30+ minutes on large drives).
3. The `/r` flag finds bad sectors and recovers readable data; `/f` fixes file system errors.
4. If chkdsk reports bad sectors, back up your important files now — then retest. A clean chkdsk rules out the disk and points you back at drivers and RAM.

### Fix 4: Test the RAM

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Let the complete test run — do not interrupt it.
3. If errors appear and your laptop has accessible RAM slots, power off, reseat the modules, and retest.
4. Persistent errors mean replacement time. RAM faults in the nonpaged area are intermittent by nature, so one clean pass after reseating is not enough — run it twice to be sure.

### Fix 5: Update or temporarily remove your antivirus

1. Update your third-party antivirus to the latest version — vendors patch kernel filter drivers for each Windows build.
2. If crashes continue, uninstall it temporarily and let **Microsoft Defender** take over (**Settings → Privacy & security → Windows Security**).
3. Test for a day or two. Antivirus filter drivers sit directly in the file-access path where 0x50 faults occur.
4. If stability returns, reinstall the latest version of your antivirus or switch to Defender permanently.

### Fix 6: Reset the pagefile and disable Fast Startup

1. Press **Win + R**, type `sysdm.cpl` → **Advanced → Performance Settings → Advanced → Virtual memory → Change**.
2. Tick **Automatically manage paging file size for all drives** → **Set** → **OK**.
3. Then go to **Control Panel → Power Options → Choose what the power buttons do → Change settings currently unavailable** and uncheck **Turn on fast startup**.
4. Restart (a real restart, not a fast-startup hybrid). Fast Startup can preserve corrupted kernel state across "shutdowns," and disabling it forces a clean boot every time.

### Fix 7: Run SFC/DISM and consider a repair install

1. In **Terminal (Admin)**, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
2. If crashes persist, download Windows 11 from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) and run an in-place repair install keeping files and apps.
3. As a last resort before hardware replacement, check for related [memory management crashes](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) — the two stop codes share causes and the combined checklist catches edge cases.
4. If nothing software-side helps and RAM tests clean, have the SSD health checked — a dying drive can pass chkdsk while still faulting intermittently.

### Fix 8: Isolate a bad RAM module by testing sticks individually

Windows Memory Diagnostic tests all RAM together. Testing modules one at a time identifies the specific failing stick when the full test reports errors.

1. Power off the laptop completely, unplug it, and remove the battery if it is removable.
2. If your laptop has accessible RAM slots, remove all but one module (ground yourself first to avoid static damage).
3. Boot and run `mdsched.exe` → **Restart now and check for problems** with just that stick installed.
4. Repeat for each module. The stick that produces errors is the faulty one — replace it and retest with the full set.
5. If no single stick errors alone but they error together, the slots, the motherboard, or a mismatched pair is the issue — try matched modules next.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA after an update is a storage-driver problem more often than a hardware problem — update those drivers first, check the disk second, test the RAM third, and isolate individual modules fourth if the memory test flags anything. If the blue screen named a `.sys` file, you have a head start most troubleshooters would envy: go straight at that driver. Worked methodically, this stop code resolves without new hardware in the large majority of cases.
