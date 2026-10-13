---
title: "SSD Slow on Windows 11? The Best Way to Restore Full Speed"
slug: best-way-to-fix-ssd-slow-on-windows-11
date: 2026-09-25
categories: ["performance"]
tags: ["ssd slow windows 11", "slow ssd", "nvme slow", "ssd performance", "troubleshooting"]
description: "Your SSD feels slower than it should on Windows 11? Here is the most effective fix order to restore full SSD speed."
thumbnail: "/images/thumbs/best-way-to-fix-ssd-slow-on-windows-11.webp"
faqs:
  - q: "What SSD speeds should I expect on Windows 11?"
    a: "A modern NVMe Gen3 drive should read around 3,000 MB/s and Gen4 around 5,000 to 7,000 MB/s; SATA SSDs top out near 550 MB/s. Test with CrystalDiskMark and compare against your drive published specs. If you are getting less than half the rated sequential speed, something is wrong — the fixes in this guide address the common causes."
  - q: "Does a full SSD really run slower?"
    a: "Yes, significantly. SSD controllers need free blocks to write efficiently; above roughly 80 percent full, write speeds can collapse as the drive shuffles data to make room. Keep at least 15 to 20 percent free for consistent performance. This single factor explains a large share of 'my SSD got slow over time' complaints."
  - q: "Should I defragment my SSD to speed it up?"
    a: "No — never run a traditional defrag on an SSD; it wastes write cycles for zero benefit since flash has no seek time. Windows runs TRIM automatically on a schedule, which is the correct maintenance. If TRIM is disabled or the optimization schedule is broken, re-enabling it is the right fix, not defragmentation."
  - q: "Can Windows 11 updates make an SSD slower?"
    a: "They can, temporarily and occasionally permanently. Major updates sometimes reset storage drivers to generic versions or change power settings. If slowness started right after an update, check the storage controller driver and power plan first — both are quick checks that resolve most post-update slowdowns."
---

An **SSD** that benchmarks at half its rated speed turns a fast laptop into a frustrating one: boots drag, apps bounce in the dock, and file copies crawl. The cruel irony is that the drive itself is usually fine — Windows 11 configuration issues like wrong drivers, disabled TRIM, or aggressive power saving are slowing it down, and every one of them is fixable in software.

The best fix order starts with the checks that take seconds — free space, TRIM status, power plan — then moves to drivers and firmware, saving hardware diagnostics for last. Work top to bottom and you will find the bottleneck quickly, because SSD slowdowns on Windows 11 cluster around a handful of well-known causes.

Grab CrystalDiskMark first and run one benchmark so you have a before number; every fix below gets judged against it. If slow boots are your main symptom rather than general slowness, the [SSD boot-time guide](/articles/how-to-fix-windows-11-boot-time-slow-ssd-step-by-step/) targets that phase specifically.

## Why this happens

- **Drive over 80% full:** With few free blocks, the SSD controller must erase-before-write constantly, and write speeds can collapse to a fraction of rated.
- **TRIM disabled or not running:** Without TRIM the OS never tells the drive which blocks are free, so garbage collection falls behind and writes slow down.
- **Wrong storage controller driver:** The generic Microsoft NVMe driver works but vendor drivers (Samsung, Intel) often unlock full queue-depth performance.
- **Aggressive PCIe power saving:** PCI Express link-state power management can throttle the SSD link to save battery, cutting throughput noticeably.
- **Outdated SSD firmware:** Firmware bugs affecting performance are common; vendors ship fixes that Windows Update never delivers.
- **BitLocker or encryption overhead:** Software encryption adds CPU cost to every I/O; on machines without hardware acceleration it is measurable.
- **Failing drive with remapped sectors:** A drive burning through its spare blocks slows as the controller works around bad flash — a hardware problem no setting fixes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free space and confirm TRIM is active

Start with the two fastest checks. Confirm at least 15–20% free space — delete or move the obvious bulk first. Then verify TRIM: open Terminal as administrator and run `fsutil behavior query DisableDeleteNotify`; a result of 0 means TRIM is on. Also open "Optimize Drives" and confirm your SSD shows "OK" with a recent optimization date and a weekly schedule. These two checks resolve the most common gradual-slowdown cases outright.

1. Check free space in File Explorer; clear to at least 15–20% free.
2. Run `fsutil behavior query DisableDeleteNotify` — want 0 (NTFS).
3. Open Optimize Drives; ensure the SSD is scheduled for weekly optimization.
4. Re-run CrystalDiskMark and compare to your baseline.

### Fix 2: Switch to the High performance power plan and tame PCIe saving

Windows power saver plans throttle the PCIe link your NVMe drive uses, and on some laptops the difference is hundreds of MB/s. Switch to Best performance (or High performance) while testing. Then in the advanced power settings, find "PCI Express → Link State Power Management" and set it to Off or Moderate — not Maximum power savings — for both battery and plugged-in states.

1. Open Power Options and select the High performance / Best performance plan.
2. In advanced settings, set PCI Express Link State Power Management to Off (plugged in).
3. Set it to Moderate power savings on battery as a compromise.
4. Benchmark again on the high-performance plan.

### Fix 3: Install the correct NVMe/storage driver

Device Manager often shows the generic "Standard NVM Express Controller" — functional, but vendor drivers frequently benchmark faster and fix quirks. Check your SSD maker site (Samsung Magician, Intel, WD Dashboard) for a dedicated NVMe driver, and your laptop maker page for the chipset/storage driver package. Install, reboot, and benchmark: this is the fix behind most "slow after a clean Windows install" cases. Guidance on sourcing drivers is at [Windows support](https://support.microsoft.com/en-us/windows).

1. Identify your SSD model in Task Manager → Performance → Disk.
2. Download the vendor NVMe driver or the laptop maker chipset package.
3. Install and restart, then verify the new driver in Device Manager.
4. Re-benchmark and compare sequential and 4K random scores.

### Fix 4: Update the SSD firmware

Firmware updates fix performance bugs, improve garbage collection, and occasionally unlock speed on newer NAND — and they never come through Windows Update. Use the vendor toolbox (Samsung Magician, Crucial Storage Executive, WD Dashboard, Intel MAS) to check for firmware newer than what is installed. Back up first: firmware flashes are safe but interrupt power at your peril — laptop plugged in, battery charged.

1. Install your SSD vendor management tool.
2. Check the firmware version against the latest available.
3. Back up critical data, plug in, and apply the update.
4. Benchmark after the required reboot.

### Fix 5: Check for encryption overhead and write-cache settings

If BitLocker device encryption is on, test with it suspended briefly to measure the overhead — on CPUs without AES acceleration it can cost real throughput. More commonly, verify that write caching is enabled on the drive: Device Manager → Disk drives → your SSD → Policies → "Enable write caching on the device" should be checked. For the related boot-phase angle, the [boot-time SSD troubleshooting guide](/articles/windows-11-boot-time-slow-ssd-troubleshooting/) digs into startup-specific I/O.

1. In Device Manager, open the SSD Properties → Policies tab.
2. Ensure write caching is enabled (and the flush-buffer option per your risk tolerance).
3. Check BitLocker status; measure with it suspended if you suspect overhead.
4. Record benchmark deltas for each change.

### Fix 6: Rule out a dying drive with SMART data

If software fixes change nothing, read the drive SMART data: percentage used (wear), media errors, and available spare capacity. Vendor tools show this clearly; anything above 90% used, or growing error counts, means the drive is the problem and no setting will save it. Back up immediately — a slow drive with SMART warnings is a drive on a deadline — then replace it.

1. Open the vendor tool and read SMART: percentage used, error counts, spare blocks.
2. Also check Windows Event Viewer → System for disk errors (event 153, 154).
3. Warnings present: back up everything now, before further testing.
4. Plan replacement; SSDs are consumables with finite write endurance.

### Fix 7: Clean-install storage drivers as a last resort

When the driver stack itself is tangled — leftover filters from old tools, a half-installed vendor driver — the clean move is to remove storage filter drivers and let Windows rebuild the stack. Uninstall third-party disk tools, remove their filter drivers in Device Manager (View → Show hidden devices → Storage controllers), and reinstall the chipset package fresh. If even this fails and SMART is clean, an in-place Windows repair is the final software step before suspecting the motherboard or slot.

1. Uninstall third-party disk utilities and their drivers.
2. In Device Manager, remove phantom storage controllers (show hidden devices).
3. Reinstall the laptop maker chipset/storage package cleanly.
4. If still slow with clean SMART, run an in-place Windows upgrade repair.

## Closing

SSD slowness on Windows 11 is a configuration problem far more often than a hardware one: free space, TRIM, power plans, the right NVMe driver, and current firmware cover nearly every case. Benchmark before and after each change, work the list in order, and check SMART the moment software stops helping — a dying drive announces itself if you look.
