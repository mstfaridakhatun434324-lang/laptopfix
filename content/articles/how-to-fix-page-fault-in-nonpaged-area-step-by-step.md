---
title: "How to Fix PAGE_FAULT_IN_NONPAGED_AREA, Step by Step"
slug: how-to-fix-page-fault-in-nonpaged-area-step-by-step
date: 2026-09-05
categories: ["windows-errors"]
tags: ["bsod", "memory", "stop code"]
description: "PAGE_FAULT_IN_NONPAGED_AREA blue screen? Windows needed data in locked memory and it wasn't there. Step-by-step fix inside."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-step-by-step.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA mean?"
    a: "Windows tried to read data from the nonpaged pool — memory that's locked in RAM and never swapped to disk — but the data wasn't there. Stop code 0x50. Causes range from bad RAM and failing drives to buggy drivers and antivirus filters."
  - q: "Is this error always bad RAM?"
    a: "Not always, though RAM is a leading suspect. Drivers that corrupt memory, failing SSDs, and even antivirus filter drivers cause the identical crash. Test memory, but don't buy new RAM until you've ruled out drivers and storage."
  - q: "Why does it happen when I launch a specific program?"
    a: "That program (or its driver, like an anti-cheat or antivirus filter) is likely corrupting the nonpaged pool. If one app triggers it consistently, update or reinstall that app and check for its driver updates first."
  - q: "Can a Windows update cause PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Yes. Updates can install incompatible storage or filter drivers, or leave the pagefile configuration broken. If crashes started right after an update, rolling back the update or its drivers is a sensible first move."
---

`PAGE_FAULT_IN_NONPAGED_AREA` (stop code 0x50) is Windows discovering that data it locked into physical RAM — data that by definition can never be paged out to disk — is missing or corrupted when something tries to read it. That's a serious inconsistency, so Windows stops everything.

The tricky part is the range of causes: bad RAM, a dying SSD, a buggy driver, or an overzealous antivirus filter can all produce this exact crash. The steps below are ordered to eliminate suspects efficiently, cheapest and most likely first.

## Why this happens

- **Failing RAM**: The most common hardware cause. Bad memory cells corrupt data sitting in the nonpaged pool.
- **Buggy storage or filter drivers**: Disk filter drivers (antivirus, encryption, backup tools) operate on the nonpaged pool; a bug corrupts it.
- **Failing SSD or hard drive**: A dying drive returns corrupt data that gets locked into the nonpaged pool and then fails verification.
- **Corrupted pagefile or virtual memory misconfiguration**: A damaged pagefile.sys or wrong virtual memory settings destabilize memory management.
- **Outdated BIOS/chipset firmware**: Memory controller bugs in old firmware corrupt RAM contents under load.
- **Antivirus real-time filters**: Kernel-level AV filters are a classic cause — they intercept every disk and memory operation.

## How to fix it

Work through these in order — memory test and driver checks first.

### Fix 1: Test your RAM thoroughly

RAM is suspect number one for this stop code. Test it properly.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let both passes complete. Any error — even a single one — means bad RAM, full stop.
3. For a conclusive test, run MemTest86 from a USB drive overnight (4+ passes).
4. If errors appear and RAM is removable, test sticks one at a time to find the bad module. If soldered, the board needs professional repair.
5. While you're in there: reseat the RAM modules. Poor contact causes intermittent faults that mimic failing RAM.

### Fix 2: Check your drive health

A dying drive corrupts data as it's read into locked memory.

1. Open an elevated Command Prompt (**Win + S**, type `cmd`, right-click > **Run as administrator**).
2. Run `chkdsk C: /f /r` — schedule it for next restart if prompted, then reboot and let it complete (it takes a while on large drives).
3. Check SMART data: install CrystalDiskInfo (free) and look at **Health Status**. Anything but "Good" means replace the drive.
4. Your manufacturer also provides diagnostics: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
5. If the drive is failing, back up immediately — this is the one fix where delay risks data loss.

### Fix 3: Temporarily disable third-party antivirus

AV filter drivers are a notorious cause of nonpaged pool corruption.

1. If you run third-party antivirus, uninstall it completely (disabling leaves the filter driver loaded).
2. Restart — Windows Defender activates automatically and is far less likely to cause this crash.
3. Use the laptop normally for a day or two. If crashes stop, the AV was the cause.
4. Before reinstalling, check the vendor's site for a version explicitly supporting your Windows build, or consider staying with Defender.

### Fix 4: Update storage and chipset drivers

The drivers managing your disk and memory controller must be current and correct.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers** — update every entry (**Update driver** > **Search automatically**).
3. Install the full chipset driver package from your laptop manufacturer's support site.
4. For Intel systems, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
5. Also update your SSD firmware if the manufacturer offers a tool (Samsung Magician, Crucial Storage Executive, WD Dashboard).

### Fix 5: Reset virtual memory settings

A corrupted pagefile or bad manual virtual memory settings destabilize the memory manager.

1. Press **Win + R**, type `sysdm.cpl`, press Enter. Go to the **Advanced** tab > **Performance** > **Settings** > **Advanced** tab > **Virtual memory** > **Change**.
2. Check **Automatically manage paging file size for all drives** and click **OK** through all dialogs.
3. Alternatively, to rebuild a corrupt pagefile: uncheck automatic management, set **No paging file**, restart, then re-enable automatic management and restart again.
4. Retest. Manual pagefile tweaks from "optimization" guides are a common hidden cause of this crash.

### Fix 6: Identify a bad driver with Driver Verifier

If hardware tests pass, a driver is corrupting the pool — Verifier will catch it.

1. Press **Win + R**, type `verifier`, press Enter.
2. Choose **Create standard settings** > **Automatically select unsigned drivers** > **Finish**, then restart.
3. Use the laptop normally. Verifier will blue-screen naming the corrupting driver — often with a more specific stop code like SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION.
4. Boot into Safe Mode, run `verifier` again, choose **Delete existing settings**, then update or remove the identified driver.
5. Our guide on [special pool memory corruption](/articles/special-pool-detected-memory-corruption-blue-screen-error-fix/) covers what to do when Verifier points at pool corruption specifically.

### Fix 7: Update BIOS and repair system files

Finish with firmware and system integrity.

1. Check your BIOS version with `msinfo32` and update from the manufacturer's support site if newer firmware exists — memory controller fixes are common in BIOS changelogs.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` from an elevated prompt.
3. If crashes persist after all of this, the remaining suspects are the motherboard's memory controller or a subtle RAM fault that only MemTest86's extended passes catch — consider professional diagnostics.

For related memory-type crashes, see our guides on [MEMORY_MANAGEMENT stop codes](/articles/how-to-fix-stop-code-memory-management-step-by-step/) and the [general blue screen walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

PAGE_FAULT_IN_NONPAGED_AREA looks scary because it involves "locked" memory, but the diagnostic path is clear: test the RAM, check the drive, remove the antivirus filter, update storage drivers, and reset virtual memory. One of those steps almost always reveals the culprit — and unlike some blue screens, this one rarely requires a Windows reinstall to resolve.
