---
title: "MEMORY_MANAGEMENT Stop Code on ASUS Laptops: A Complete Fix Guide"
slug: how-to-fix-stop-code-memory-management-on-asus-laptop
date: 2026-10-12
categories: ["windows-errors"]
tags: ["blue screen", "memory management", "asus", "windows 11", "ram test"]
description: "MEMORY_MANAGEMENT blue screen on your ASUS laptop? This complete guide covers RAM testing, driver fixes, and BIOS tweaks for stop code 0x1A."
thumbnail: "/images/thumbs/how-to-fix-stop-code-memory-management-on-asus-laptop.webp"
faqs:
  - q: "What causes MEMORY_MANAGEMENT on ASUS laptops specifically?"
    a: "The same causes as other brands — faulty RAM, bad drivers, disk errors — plus ASUS-specific ones: Armoury Crate kernel drivers, aggressive memory profiles on ROG models, and outdated ASUS chipset drivers. Gaming workloads make marginal RAM fail faster, which is why ROG owners see it more."
  - q: "Should I run MemTest86 or is Windows Memory Diagnostic enough?"
    a: "Start with Windows Memory Diagnostic — it's quick. But it misses subtle faults, so if crashes continue after it passes, run MemTest86 overnight. Many 0x1A cases only show errors after hours of testing."
  - q: "Can Armoury Crate cause MEMORY_MANAGEMENT crashes?"
    a: "Yes. Its kernel drivers manage power and memory-adjacent hardware, and buggy versions have triggered 0x1A. Uninstall it temporarily as a test — if crashes stop, reinstall the latest version."
  - q: "Is the RAM soldered on my ASUS laptop?"
    a: "Many thin ASUS models (Zenbook, some VivoBooks) have soldered RAM that can't be replaced — a failure means motherboard service. Gaming models (ROG, TUF) usually have accessible SODIMM slots you can upgrade or replace yourself."
---

MEMORY_MANAGEMENT — stop code 0x1A — means Windows found its own memory records corrupted and stopped before the damage could spread. On ASUS laptops this crash has a particular personality: it loves to appear under gaming load on ROG machines, after Armoury Crate updates, or on machines whose memory has been quietly degrading for a year. The name tells you where to look, and this guide looks there first.

Don't let the technical name intimidate you. The investigation is methodical, the tools are built into Windows, and most cases resolve without spending money.

## Why this happens

- **Degrading RAM modules.** Memory doesn't always fail suddenly — marginal cells cause intermittent 0x1A crashes that worsen over months, especially under gaming or video-editing loads.
- **Armoury Crate driver bugs.** ASUS's utility hooks power and hardware management at kernel level; bad releases corrupt memory management state.
- **Aggressive memory timings on ROG/TUF models.** Factory or user-applied performance memory profiles push RAM past what the silicon reliably handles.
- **Outdated chipset and storage drivers.** Drivers that mismanage DMA or paged memory corrupt the structures 0x1A checks.
- **Failing SSDs.** Corruption in paged-out memory data reads back as memory corruption — a drive problem wearing a RAM costume.
- **Corrupted Windows system files.** Damage to the memory manager's own code triggers the check without any hardware involvement.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Uninstall Armoury Crate temporarily

The ASUS-specific suspect goes first because it's free and fast to test.

1. Open **Settings > Apps > Installed apps**.
2. Uninstall **Armoury Crate** and **Armoury Crate Service**.
3. Restart and use the laptop normally — including the workload that used to crash — for a day or two.
4. If crashes stop, reinstall the latest Armoury Crate from the Microsoft Store; the bug was likely fixed in a newer release.
5. If crashes continue without it, move on — you've eliminated one variable.

### Fix 2: Run Windows Memory Diagnostic

The quick RAM check.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. At the test screen, press **F1**, select **Extended**, and let it run (30–60 minutes).
4. After reboot, check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
5. Any errors mean bad RAM — skip to Fix 4. If it passes, still do Fix 3 before clearing the memory, since this test misses subtle faults.

If you're also seeing page faults, our [PAGE_FAULT_IN_NONPAGED_AREA on ASUS guide](/articles/how-to-fix-page-fault-in-nonpaged-area-on-asus-laptop/) pairs naturally with this one — the two stop codes share causes.

### Fix 3: Run MemTest86 overnight

The conclusive test the built-in diagnostic can't match.

1. Download MemTest86 and write it to a USB drive.
2. Boot from the USB (press **Esc** or **F8** at the ASUS logo for the boot menu, depending on model).
3. Run at least **4 complete passes** — plan for 6–8 hours, so overnight is ideal.
4. One single error is a failure. Note which stick and slot the report identifies.
5. If errors appear, test each stick individually in the same slot to separate stick faults from slot faults.

### Fix 4: Replace or reseat the RAM

Act on what the tests found.

1. Power off, unplug, and (on models with a removable battery) disconnect power fully.
2. Open the service panel and **reseat** each SODIMM — remove it, blow out dust, and firmly reinsert until both clips click.
3. Test again. Loose or oxidized contacts cause exactly these intermittent crashes, and reseating alone sometimes fixes them.
4. If a specific stick failed testing, replace it with matching spec RAM (speed, voltage, and timings matter — check the working stick's label).
5. On soldered-RAM models (most Zenbooks), a failure means contacting ASUS support for board service — don't attempt it yourself.

### Fix 5: Reset memory profiles and update the BIOS

Undo aggressive timings and pick up firmware fixes.

1. Enter the BIOS (**F2** or **Del** at the ASUS logo).
2. Disable any **XMP/DOCP** memory profile — set memory to **Auto** or standard speeds.
3. Choose **Load Optimized Defaults** for anything else you may have tweaked.
4. Check your BIOS version in `msinfo32` against the latest on ASUS support; update if the changelog mentions memory compatibility or stability.
5. Flash only with the charger connected and never interrupt the process.

### Fix 6: Update chipset, storage, and GPU drivers

Drivers are the main non-RAM cause.

1. Install the latest **chipset driver** for your exact ASUS model from ASUS support.
2. Update storage controllers in **Device Manager > IDE ATA/ATAPI controllers**.
3. Clean-install the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. On Intel-based models, [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) catches anything ASUS's page missed.
5. Restart and stress-test with the workload that used to crash.

For the update-triggered variant, see [MEMORY_MANAGEMENT after a Windows 11 update](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/).

### Fix 7: Check the drive and repair system files

The last two suspects: disk and Windows itself.

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r` (schedule at reboot if asked).
2. After booting, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an admin terminal.
3. Check the CHKDSK results in **Event Viewer > Windows Logs > Application** under **Wininit**.
4. Recurring bad sectors mean a dying SSD — back up and replace it.
5. If everything passes and crashes persist, an in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) is the final software step before suspecting the motherboard.

## Closing

MEMORY_MANAGEMENT on ASUS laptops rewards the methodical: test Armoury Crate first (it's the brand-specific wildcard), then test the RAM properly — not just the quick diagnostic — then work drivers and disk. The overwhelming majority of 0x1A crashes surrender to one of these seven steps. And remember the deeper lesson: intermittent crashes that get slowly worse over months are almost always degrading memory, so don't dismiss RAM just because the quick test passed.
