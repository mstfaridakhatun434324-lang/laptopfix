---
title: "Memory Management Stop Code in Windows 11 24H2: How to Fix It"
slug: how-to-fix-stop-code-memory-management-in-windows-11-24h2
date: 2026-09-28
categories: ["windows-errors"]
tags: ["windows 11 24h2", "memory management", "bsod"]
description: "MEMORY_MANAGEMENT blue screen on Windows 11 24H2? From targeted driver updates to full MemTest86 RAM testing, here is the complete fix sequence."
thumbnail: "/images/thumbs/how-to-fix-stop-code-memory-management-in-windows-11-24h2.webp"
faqs:
  - q: "How can I tell if it's the RAM or a driver?"
    a: "Timeline and dumps. Sudden onset right after a driver/Windows update screams driver; gradual worsening over weeks screams RAM. Dumps naming a specific third-party driver point at software; dumps blaming ntoskrnl with varying details, or a different culprit every crash, point at hardware. MemTest86 errors settle it definitively."
  - q: "Will adding more RAM fix this?"
    a: "No — adding RAM to a system with a faulty stick just gives you more memory alongside the faulty stick. The bad module keeps corrupting structures. The fix is identifying and replacing the bad module (Fix 5), not adding capacity around it."
  - q: "Can antivirus cause MEMORY_MANAGEMENT?"
    a: "Yes — antivirus filter drivers operate in the memory paths this stop code polices, and a buggy filter can corrupt pool structures. If crashes started after an antivirus update, temporarily switching to Defender is a valid diagnostic step. It is less common than RAM or graphics drivers, but real."
  - q: "Why does MemTest86 take so long? Can I skip it?"
    a: "Because it writes and verifies patterns across every byte of RAM multiple times — thoroughness is the point. The built-in Windows test (Fix 1) is the quick screen; MemTest86 is the definitive one. For this specific stop code, where RAM is the leading cause, skipping the definitive test means possibly replacing the wrong part."
---

MEMORY_MANAGEMENT is Windows catching corruption in the structures it uses to manage memory itself — page tables, pool headers, PFN lists. When the memory manager's own bookkeeping does not add up, the system bug-checks rather than continue with an unreliable view of RAM. The name points at memory, and memory (the hardware) is indeed the most common cause — but drivers corrupt these structures too, so both need investigation.

On Windows 11 24H2 this stop code appears in two flavors: the sudden-onset kind after a driver or Windows update (usually software), and the gradual kind that gets more frequent over weeks (usually dying RAM). The timeline tells you where to start; the steps below cover both.

## Why this happens

- **Failing RAM:** the most common cause — bad cells corrupting the memory manager's data structures, often worsening gradually over time.
- **A buggy driver corrupting pool memory:** drivers that overwrite pool headers or mishandle allocations trip the memory manager's integrity checks.
- **Corrupted page file:** a damaged pagefile.sys feeds bad data back into memory management on page-in.
- **Disk errors:** bad sectors in the paging area or system files corrupt what the memory manager reads.
- **Windows 11 24H2 incompatibilities:** older drivers that corrupt memory in ways 24H2's stricter checks now catch.
- **Overclocked or mismatched RAM:** unstable timings corrupt structures under load; mixed RAM kits are a classic trigger.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Run Windows Memory Diagnostic

Start with the built-in test — it is quick and catches gross RAM failures immediately.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Let the standard test run to completion and note the result shown after reboot.
3. Errors here are conclusive: the RAM is bad. Skip to Fix 5 for the isolation procedure.
4. A pass here is not conclusive — Windows Memory Diagnostic misses subtle faults. Continue with the driver steps, and keep MemTest86 in reserve.
5. If crashes are frequent enough to interrupt the test itself, that is also diagnostic information — severe RAM faults crash the tester too.

### Fix 2: Update drivers, prioritizing the usual suspects

Before the multi-hour memory test, rule out the software causes — they are faster to check.

1. Read the dump first if you can: WinDbg Preview, `!analyze -v`, check **IMAGE_NAME** for a named driver.
2. Update graphics, chipset, storage, and network drivers from manufacturer sources: [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html).
3. Check **Settings > Windows Update > Advanced options > Optional updates** for driver updates.
4. If crashes began after a specific driver update, roll that one back instead (**Device Manager > Properties > Driver > Roll Back Driver**).
5. Test for a day. Driver-caused MEMORY_MANAGEMENT usually resolves here; hardware-caused does not.

### Fix 3: Reset virtual memory to automatic

A corrupted or misconfigured page file is a real (if uncommon) cause. Eliminate it.

1. Press **Win + R**, type `sysdm.cpl`, **Advanced** tab, **Settings** under Performance, **Advanced** tab, **Change** under Virtual memory.
2. Select each drive, choose **System managed size**, click **Set**. Ensure **Automatically manage paging file size for all drives** is ticked at the top.
3. Click OK through the dialogs and restart.
4. To force a fresh pagefile: temporarily set **No paging file**, reboot, then set **System managed size** again and reboot — this deletes and recreates pagefile.sys.
5. If crashes stop after the pagefile rebuild, disk errors likely corrupted the old one — run `chkdsk C: /f /r` to check the underlying cause.

### Fix 4: Repair system files and check the disk

Corruption in the storage layer feeds the memory manager bad data. Verify both.

1. Elevated Command Prompt: `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Then `chkdsk C: /f /r` (reboot to let it run).
4. Check SMART: `wmic diskdrive get status` — non-OK means replace the drive, not more repairs.
5. Re-run `sfc /scannow` after chkdsk, since disk repairs can reveal file damage. The [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) has more on dump analysis if your dumps keep naming ntoskrnl.

### Fix 5: Run MemTest86 and isolate the bad module

The definitive memory test. If software fixes failed, this is where the answer lives.

1. Create a MemTest86 USB on another PC and boot from it.
2. Run at least 4 full passes — overnight is ideal. Note which pass and test number produce errors.
3. Errors: power off, open the RAM compartment (or bottom panel), reseat the modules, retest.
4. Still errors: test one module at a time in the primary slot to identify the bad stick. Replace it — RAM is cheap, crashes are expensive.
5. While testing, reset BIOS memory settings to stock (disable XMP, manual timings, overclocks). Mixed-capacity or mixed-brand kits: test with only the matched pair.

### Fix 6: Check thermals and power

Heat and unstable power cause memory errors that look exactly like bad RAM — rule them out before buying parts.

1. Monitor with HWiNFO64: memory-controller-adjacent temperatures and any thermal throttling flags during the crash workload.
2. Blow out dust from vents and fans; ensure the laptop sits on a hard flat surface.
3. Test on AC power with the battery at a healthy charge — a failing battery causing voltage droop under load can corrupt memory operations.
4. Try the OEM charger, not a third-party one — underpowered chargers cause brownouts under combined CPU+GPU load.
5. If crashes only happen on battery or only under combined load, power delivery is suspect, not the RAM sticks.

### Fix 7: Clean-install Windows 11 24H2

When hardware tests pass but crashes persist, eliminate the software stack completely.

1. Back up everything.
2. Clean-install from Microsoft's Windows 11 download page.
3. Install chipset and storage drivers first, test stability before adding anything else.
4. Add software gradually. If crashes return after a specific install, its driver is the corrupter.
5. Crashes on a clean 24H2 install with stock drivers, good thermals, and MemTest86-clean RAM point to the motherboard or CPU memory controller — professional diagnosis. For recovery-environment techniques during all this, the [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers every entry method.

## Closing

MEMORY_MANAGEMENT rewards the honest diagnostic sequence: quick memory screen, driver updates, pagefile reset, disk checks, then the definitive MemTest86 run. Most cases resolve in the first half — a driver update or a pagefile rebuild. But when it is the RAM, no software fix will ever hold, and the hours MemTest86 takes are cheaper than weeks of mystery crashes. Test, do not guess.
