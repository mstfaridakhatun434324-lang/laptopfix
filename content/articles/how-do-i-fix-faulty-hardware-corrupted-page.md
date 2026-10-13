---
title: "FAULTY_HARDWARE_CORRUPTED_PAGE: What It Means and How to Fix It"
slug: how-do-i-fix-faulty-hardware-corrupted-page
date: 2026-09-08
categories: ["windows-errors"]
tags: ["blue screen", "faulty hardware", "corrupted page", "stop code 0x12b", "ram failure"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE (0x12B) keeps crashing your laptop? Find out whether it's RAM, drivers, or the SSD — and fix it in 8 steps."
thumbnail: "/images/thumbs/how-do-i-fix-faulty-hardware-corrupted-page.webp"
faqs:
  - q: "What does FAULTY_HARDWARE_CORRUPTED_PAGE mean?"
    a: "It's stop code 0x0000012B. Windows detected that a page of physical memory contains corrupted data that can't be trusted — single-bit errors in RAM are the classic trigger. Despite the scary name, software causes (drivers, overclocking) are common too, so test before buying new RAM."
  - q: "Is this error always a RAM problem?"
    a: "Not always. Windows names it 'faulty hardware' because memory corruption was detected, but buggy drivers writing to the wrong addresses, unstable overclocks, and even a failing SSD's page file can produce it. Run the memory diagnostic and driver checks first to narrow it down."
  - q: "Can I keep using my laptop with this error?"
    a: "You can, but you shouldn't trust it with important work. Memory corruption can silently damage files you're saving. Back up your data first, then troubleshoot — if the corruption spreads, you risk losing documents, not just getting blue screens."
  - q: "Will MemTest86 find errors that Windows Memory Diagnostic misses?"
    a: "Sometimes. MemTest86 runs outside Windows with more thorough test patterns and often catches intermittent faults the built-in tool misses. If Windows Memory Diagnostic is clean but crashes continue, run MemTest86 from a USB stick for at least 4 full passes."
---

FAULTY_HARDWARE_CORRUPTED_PAGE (stop code 0x12B) is Windows telling you it caught memory corruption red-handed. A "page" is a 4KB chunk of RAM, and Windows checksums critical pages — when one fails the check, the system crashes on purpose rather than let corrupted data reach your files. The name points at hardware, and RAM really is the most common cause, but drivers and overclocking fake this error convincingly.

The smart approach is to rule out the free fixes first, test the memory properly, and only then spend money on hardware.

## Why this happens

- **Failing or marginal RAM modules.** Single-bit errors from dying memory cells are the textbook cause — they corrupt pages randomly.
- **Unstable RAM overclock or XMP/EXPO profile.** Aggressive memory timings cause exactly the intermittent corruption this stop code reports.
- **Buggy drivers writing out of bounds.** A driver scribbling past its allocated memory corrupts neighboring pages, and Windows blames "hardware."
- **Failing SSD corrupting the page file.** If the drive holding `pagefile.sys` develops bad blocks, pages swapped to disk come back corrupted.
- **Overheating memory or motherboard.** Heat-induced instability produces transient errors that look like permanent RAM faults.
- **Corrupted system files.** Damage to the memory manager's own code can make healthy pages fail integrity checks.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Back up your data right now

Memory corruption can silently damage files, so protect yourself before troubleshooting.

1. Copy important documents, photos, and projects to an external drive or cloud storage immediately.
2. Don't run disk-intensive operations (large copies, video renders) until you've tested the memory — stress increases corruption risk.
3. If the laptop crashes during backup, boot into Safe Mode (hold **Shift** while clicking **Restart**, then **Troubleshoot > Advanced options > Startup Settings**) where less memory pressure exists.
4. Verify the backup opened correctly on another device before continuing.
5. With data safe, you can troubleshoot aggressively without fear.

### Fix 2: Reset memory and CPU settings to stock

Overclocks are the cheapest cause to eliminate.

1. Restart and enter BIOS/UEFI (**Del**, **F2**, or **F10** during boot).
2. Disable XMP/EXPO memory profiles and any CPU overclock or undervolt.
3. Choose **Load Optimized Defaults**, save, and exit.
4. Use the laptop for a day at stock settings and watch for crashes.
5. If the crashes stop, your "stable" overclock wasn't — keep stock settings or retune conservatively.

### Fix 3: Run Windows Memory Diagnostic

The built-in test catches obvious RAM faults quickly.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Select **Restart now and check for problems**.
3. Press **F1** at the test screen and choose **Extended** test with more passes for a thorough check.
4. Let it complete fully — this can take 30+ minutes.
5. After reboot, open **Event Viewer > Windows Logs > System**, filter for **MemoryDiagnostics-Results**, and read the outcome. Errors mean at least one stick is bad.

If the built-in test is clean but crashes persist, our [step-by-step FAULTY_HARDWARE_CORRUPTED_PAGE guide](/articles/how-to-fix-special-pool-detected-memory-corruption-step-by-step/) covers the deeper memory-forensics approach.

### Fix 4: Test with MemTest86 from a USB stick

For intermittent faults the Windows tool misses.

1. On another computer, download MemTest86 and create a bootable USB with its included tool.
2. Boot your laptop from the USB (use the boot menu key — often **F12** or **Esc**).
3. Let it run at least **4 full passes** — this takes several hours; overnight is ideal.
4. Any red errors mean faulty RAM. Note which stick/slot if your laptop has removable memory.
5. Test sticks individually in different slots to separate a bad stick from a bad motherboard slot.

### Fix 5: Reseat or replace the RAM

Physical fixes for confirmed memory problems.

1. Power off, unplug, and (on laptops with removable panels) open the memory compartment.
2. Remove each stick, blow out dust, and reseat firmly until the clips click.
3. If you have two sticks, test with one at a time to isolate the faulty one.
4. Replace confirmed-bad sticks with the exact specification your laptop manual lists (DDR generation, speed, and voltage all matter).
5. On ultrabooks with soldered RAM, a confirmed fault means a motherboard repair — get a quote before deciding; sometimes a USB-booted Linux environment can limp along, but don't trust it with important data.

### Fix 6: Update drivers and BIOS/UEFI firmware

Rule out driver-caused page corruption.

1. Open **Device Manager** and update storage controller, chipset, and GPU drivers.
2. Visit your manufacturer's support page — [Dell](https://www.dell.com/support), HP, or Lenovo — and install the latest BIOS/UEFI update, which often includes memory-compatibility fixes.
3. Keep the charger plugged in during any firmware update and don't interrupt it.
4. Also update the SSD firmware if the manufacturer offers a tool for it.
5. Restart and test under the workload that used to crash.

### Fix 7: Check the drive holding the page file

A failing SSD can corrupt swapped pages.

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r`, typing **Y** to schedule it for the next restart.
2. Check SMART health with your SSD maker's utility or run `wmic diskdrive get status` in Command Prompt.
3. If the drive shows warnings or `chkdsk` finds many bad clusters, clone to a new SSD promptly.
4. As a diagnostic step, you can move the page file: **Settings > System > About > Advanced system settings > Performance Settings > Advanced > Virtual memory**, and set it to a different healthy drive.
5. For the Windows 11 24H2-specific variant of this crash, see [FAULTY_HARDWARE_CORRUPTED_PAGE in Windows 11 24H2](/articles/how-to-fix-faulty-hardware-corrupted-page-in-windows-11-24h2/).

### Fix 8: Repair Windows system files

Eliminate OS-level corruption as the last software step.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow` and restart.
3. If crashes continue after clean memory tests and repaired files, the fault is almost certainly hardware — RAM, motherboard, or SSD.
4. At that point, professional diagnosis with known-good parts is the fastest path.
5. Microsoft's [blue screen troubleshooting hub](https://support.microsoft.com/en-us/windows) lists additional recovery options.

## Closing

FAULTY_HARDWARE_CORRUPTED_PAGE earns its dramatic name, but don't order new RAM on day one — overclocks, drivers, and dying SSDs all wear the same disguise. Work the list in order: back up, de-clock, test memory properly with MemTest86, and only spend money when a test actually convicts the hardware. Your files will thank you for the backup-first approach either way.
