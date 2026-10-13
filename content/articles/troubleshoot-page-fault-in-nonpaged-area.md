---
title: "PAGE_FAULT_IN_NONPAGED_AREA Blue Screen: How to Fix It"
slug: troubleshoot-page-fault-in-nonpaged-area
date: 2026-10-05
categories: ["windows-errors"]
tags: ["page fault in nonpaged area", "bsod", "stop code 0x50", "windows 11"]
description: "PAGE_FAULT_IN_NONPAGED_AREA (0x50) crashes Windows when memory goes wrong. Follow this technician's guide to fix it for good."
thumbnail: "/images/thumbs/troubleshoot-page-fault-in-nonpaged-area.webp"
faqs:
  - q: "What causes PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Windows tried to read data from a memory region marked nonpageable — memory that must always be in RAM — and found it missing or invalid. Typical causes: faulty RAM, a buggy driver referencing freed memory, a corrupt page file, or antivirus filter drivers. The stop code is 0x00000050."
  - q: "Is PAGE_FAULT_IN_NONPAGED_AREA a RAM problem?"
    a: "It can be, but not always. Faulty RAM is a leading cause, yet drivers and corrupt system files trigger the same code. Run the Windows Memory Diagnostic early: if it reports errors, you have a hardware answer. If RAM passes, the culprit is software, and the fixes below target drivers and system files."
  - q: "Can a Windows update cause this blue screen?"
    a: "Yes, frequently. Feature updates replace drivers and change memory management behavior, and a driver that worked before can start referencing invalid memory afterward. If the crash began within days of an update, roll back the update or the most recently changed driver before trying deeper hardware diagnostics."
  - q: "Should I disable the page file to fix this error?"
    a: "No — disabling the page file often makes things worse, because nonpaged pool memory management depends on the paging subsystem. Instead, verify the page file is system-managed, test RAM, and update drivers. Only tune the page file if you have a specific, diagnosed reason to do so."
---

**PAGE_FAULT_IN_NONPAGED_AREA** (stop code **0x00000050**) is one of the most common blue screens on Windows 11 laptops, and its name actually tells you what's wrong: Windows needed data from a "nonpaged" region of memory — an area the kernel guarantees will always be in physical RAM — and the data wasn't there. The system can't continue without it, so it stops.

In the repair shop, this error falls into two camps. The first is **hardware**: faulty RAM sticks, a dying SSD corrupting data in transit, or (rarely) a failing motherboard memory controller. The second is **software**: a buggy driver referencing memory that was freed, a corrupt page file, or an antivirus filter driver hooking memory operations incorrectly. Both camps produce the identical blue screen, so you have to diagnose before you start replacing parts or reinstalling Windows.

Start by noting when the crash happens. Crashes under heavy load (gaming, video editing) lean toward RAM or heat; crashes at random idle moments lean toward drivers; crashes right after a Windows update point at the update itself. If a driver filename appears on the blue screen, photograph it — that narrows everything down instantly. For the update angle, see our guide on [page faults after Windows 11 updates](/articles/how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update/); for the memory side, the [memory management BSOD guide](/articles/memory-management-bsod-windows-11-fix/) pairs well with this one.

## Why this happens

- **Faulty or failing RAM**: Bad memory cells return garbage when the kernel reads nonpaged pool memory — the single most common hardware cause of 0x50.
- **A buggy device driver**: Drivers that reference memory after freeing it (a "use-after-free" bug) trigger this exact fault. Graphics, network, and storage drivers are frequent offenders.
- **Corrupt page file**: If `pagefile.sys` is damaged, Windows can lose track of what belongs in nonpaged memory.
- **A recent Windows or driver update**: Updates change drivers and memory behavior; a previously fine driver can break overnight.
- **Antivirus and security software**: Kernel-level filter drivers from third-party antivirus products hook memory operations and are a classic source of 0x50 crashes.
- **Failing SSD or hard drive**: A dying drive corrupts data between storage and RAM, which the kernel reads as a page fault.
- **Overclocked or misconfigured memory**: Aggressive XMP profiles and manual RAM overclocks destabilize the memory the kernel depends on.
- **Corrupt system files**: Damage to core Windows files involved in memory management.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Memory Diagnostic

Rule out bad RAM before anything else — it's the fastest hardware check available.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The laptop reboots into the memory test.
3. Let it complete (15–30 minutes for the standard pass). Any errors reported mean defective RAM.
4. If errors appear on a laptop with removable RAM, reseat the modules first (power off, remove battery if possible, reseat firmly) and retest — loose modules cause faults too. Replace the stick if errors persist.

### Fix 2: Boot into Safe Mode and note the pattern

Safe Mode loads only Microsoft drivers, which isolates third-party drivers instantly.

1. Hold **Shift** while clicking **Restart**, then go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** and press **4** for Safe Mode.
2. Use the laptop for a while in Safe Mode. If it never crashes here, a third-party driver or startup program is the cause — continue with Fix 3 and Fix 6.
3. If it crashes in Safe Mode too, the problem is hardware, core Windows files, or a Microsoft driver — skip to Fixes 4 and 5.

### Fix 3: Update or roll back the suspect driver

The blue screen often names the driver file — target it.

1. If the crash screen named a `.sys` file, identify its device: `ntfs.sys` is storage, `nvlddmkm.sys` is NVIDIA, `rtwlanu.sys`/`rtwlane.sys` is Realtek Wi-Fi, `tcpip.sys` is networking.
2. Open **Device Manager** (**Win + X**), find the device, right-click and choose **Update driver** > **Search automatically for drivers**.
3. If the crash started after a driver update, use **Properties** > **Driver** tab > **Roll Back Driver** instead.
4. For graphics and chipset drivers, prefer the manufacturer's version: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).

### Fix 4: Repair system files and the component store

Corrupt Windows files in the memory-management path cause 0x50 even with healthy RAM.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to finish — it repairs protected system files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to fix the store SFC relies on.
4. Restart and test under the conditions that used to crash. If SFC found and fixed corruption, retest before continuing — this alone resolves many cases.

### Fix 5: Check the disk and the page file

Storage corruption feeds bad data into memory.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r` and confirm the scan on next restart. Reboot and let it complete (it can take an hour on large drives).
2. Press **Win + R**, type `sysdm.cpl`, go to the **Advanced** tab > **Performance** > **Settings** > **Advanced** > **Virtual memory** > **Change**.
3. Make sure **Automatically manage paging file size for all drives** is checked. A manually shrunken page file is a known trigger.
4. Check drive health with your SSD manufacturer's tool (e.g. Samsung Magician, Crucial Storage Executive) — reallocated sectors or critical warnings mean the drive is dying.

### Fix 6: Temporarily remove third-party antivirus

Antivirus filter drivers are a classic 0x50 source.

1. Open **Settings** > **Apps** > **Installed apps** and uninstall your third-party antivirus completely (don't just disable it — the filter driver stays loaded when disabled).
2. Restart. Windows Defender activates automatically and is safe to run alone for testing.
3. Use the laptop for a day or two. If crashes stop, the antivirus was the cause — reinstall its latest version, or switch to a different product.
4. Keep Defender's real-time protection on while testing; never run without any antivirus.

### Fix 7: Reset BIOS memory settings to defaults

Unstable memory clocks cause faults the kernel can't distinguish from bad RAM.

1. Restart into **BIOS/UEFI** (**F2**, **Del**, or **Esc** at the logo).
2. **Load Optimized Defaults**, which disables XMP/DOCP profiles and manual overclocks.
3. Save and exit, then retest under load. If stability returns, your memory overclock was the problem.
4. You can re-enable XMP afterward only if the laptop passes a full memory test with it on.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA is a symptom with two families of causes — bad memory and bad drivers — and the diagnostic order above separates them quickly: memory test first, Safe Mode to isolate drivers, then file and disk repair. If the memory diagnostic passes, crashes don't happen in Safe Mode, and a fresh manufacturer driver doesn't help, back up your data and have the SSD and motherboard checked, because you've eliminated everything software can explain.
