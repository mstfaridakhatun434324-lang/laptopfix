---
title: "SSD Slow in Windows 11? A Step-by-Step Repair Guide"
slug: how-to-fix-ssd-slow-on-windows-11-step-by-step
date: 2026-10-09
categories: ["performance"]
tags: ["ssd slow", "windows 11", "nvme", "trim", "step by step"]
description: "SSD underperforming in Windows 11? Follow this ordered step-by-step guide to benchmark, diagnose, and restore your SSD's full speed."
thumbnail: "/images/thumbs/how-to-fix-ssd-slow-on-windows-11-step-by-step.webp"
faqs:
  - q: "What SSD speed should I expect in Windows 11?"
    a: "It depends on the interface: SATA SSDs top out around 550 MB/s sequential read, PCIe 3.0 NVMe drives reach about 3,500 MB/s, and PCIe 4.0 NVMe drives can exceed 7,000 MB/s. If CrystalDiskMark shows less than half your drive's rated sequential speed, something is wrong. Random 4K performance matters more for everyday snappiness than peak sequential numbers."
  - q: "Does Windows 11 slow down SSDs?"
    a: "Windows 11 itself doesn't inherently slow SSDs, but its updates can: feature updates sometimes replace optimized storage drivers with generic ones, reset power plans that throttle drives, and leave the system re-indexing for days. The OS also enables features like memory integrity (HVCI) that cost a small, measurable amount of storage performance on some systems."
  - q: "Is it safe to defragment an SSD?"
    a: "Traditional defragmentation is unnecessary and wasteful on SSDs — they have no seek penalty, so file fragmentation doesn't slow them. Windows' Optimize Drives tool knows this: when you 'optimize' an SSD, it sends TRIM commands instead of defragmenting. Never use third-party defrag tools on an SSD; just use the built-in Optimize and keep TRIM enabled."
  - q: "How full is too full for an SSD?"
    a: "Keep at least 15 to 20 percent of an SSD free. NAND flash needs empty blocks to write efficiently; as the drive fills, the controller spends more time shuffling data, and both write speeds and latency degrade — sometimes dramatically past 90 percent full. If your C: drive is nearly full, freeing space is often the single biggest performance fix."
---

A slow SSD feels like a betrayal — you paid for instant, and you're getting spinning-rust. But SSDs rarely slow down on their own. The drive is usually fine; it's the software around it (drivers, power settings, full disks, background services) that's strangling performance. That means the fix is almost always in Windows, not in your wallet.

This guide is strictly ordered: benchmark first so every later step is measurable, then work through the software causes from most to least likely, and finish with the hardware verdict. Stop when your numbers recover. For HP-specific driver and firmware steps, see [fixing a slow SSD on HP laptops](/articles/how-to-fix-ssd-slow-on-windows-11-on-hp-laptop/); for 100% disk usage issues, our [high disk usage guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-step-by-step/).

## Why this happens

- **Wrong storage driver**: Generic Microsoft drivers replace optimized manufacturer drivers after updates.
- **SSD too full**: Below 15–20% free space, write performance collapses.
- **TRIM disabled or not running**: The SSD can't reclaim deleted blocks efficiently.
- **Power-saving throttling**: PCIe link-state management and disk sleep timers slow the drive.
- **Background services saturating the disk**: Indexing, antivirus, SysMain, and update servicing.
- **SATA mode or slot issues**: A drive in the wrong mode (IDE instead of AHCI) or a bandwidth-limited slot.
- **Worn or failing NAND**: Genuine end-of-life degradation after heavy write workloads.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Benchmark and record your baseline

You can't fix what you can't measure.

1. Download **CrystalDiskMark** and run the default profile — record sequential read/write and 4K random read/write.
2. Download **CrystalDiskInfo** and note **Health Status**, temperature, and total host writes — high temperature or warnings change the diagnosis.
3. Open **Task Manager** > **Performance** > select your disk — note whether it's identified as SSD and its current active time at idle.
4. Look up your exact SSD model's rated speeds (Device Manager > Disk drives gives the model name) and compute the gap between rated and measured.
5. Write the numbers down — every fix below gets validated against this baseline, and "feels faster" is not a measurement.

### Fix 2: Check AHCI mode and the physical connection

A surprisingly common foundational issue.

1. Open **Device Manager** > **IDE ATA/ATAPI controllers** — you should see **Standard SATA AHCI Controller** or a manufacturer AHCI driver, never IDE mode.
2. If the controller is in IDE mode, switching to AHCI requires a registry tweak before changing the BIOS setting (set `iaStorV` StartOverride to 0) — do this carefully, as a wrong move causes boot failure.
3. For NVMe drives, confirm in BIOS/UEFI that the M.2 slot is set to NVMe/PCIe mode, not SATA.
4. On desktops, try a different SATA port or cable — marginal cables cause retries that look exactly like a slow drive; on laptops, reseat the drive if you're comfortable opening the machine.
5. Re-benchmark after any connection change — a bad cable or wrong mode can halve throughput, and the fix is instant.

### Fix 3: Install the correct storage driver

The highest-yield software fix.

1. In **Device Manager**, check the driver date on your storage controllers — a 2006-dated Microsoft driver means you're on the generic fallback.
2. Get the proper driver: Intel systems want **Intel RST** or the chipset driver (the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds it), AMD systems want the AMD chipset driver, Samsung SSDs have a dedicated NVMe driver.
3. Prefer your laptop manufacturer's driver page first (Dell: [Dell Support](https://www.dell.com/support); Lenovo: Lenovo's official support site) — OEMs sometimes customize storage drivers.
4. Install, reboot, and re-benchmark — this single step resolves a large share of "SSD slow after Windows update" cases.
5. If the manufacturer's driver is ancient, try the component maker's newer driver as a second attempt — but keep the working one noted in case you need to roll back.

### Fix 4: Free space, enable TRIM, and optimize

The maintenance trio.

1. Get C: above 20% free: **Settings** > **System** > **Storage** > **Temporary files**, plus uninstalling unused programs and moving media off the drive.
2. Confirm TRIM: elevated terminal, `fsutil behavior query DisableDeleteNotify` should return `0`; if not, run `fsutil behavior set DisableDeleteNotify 0`.
3. Open **Defragment and Optimize Drives**, select the SSD, click **Optimize** — this issues TRIM across the drive.
4. Check the scheduled optimization is on (weekly) so TRIM stays current without you thinking about it.
5. Re-benchmark — full-disk plus TRIM issues can account for the majority of a slowdown, and recovery is often dramatic. See our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) for deeper cleanup.

### Fix 5: Disable power-saving drive throttling

For SSDs that are fast on AC but sluggish on battery — or slow everywhere.

1. **Settings** > **System** > **Power & battery** > set **Power mode** to **Best performance** (plugged in).
2. **Control Panel** > **Power Options** > **Change advanced power settings** > **PCI Express** > **Link State Power Management** > **Off**.
3. In the same dialog, **Hard disk** > **Turn off hard disk after** > **Never** (plugged in).
4. Check your SSD manufacturer's toolbox software (Samsung Magician, Crucial Storage Executive, WD Dashboard) for its own power/performance modes and set **Maximum performance**.
5. Benchmark on AC power after these changes — if the numbers recover, power management was the limiter, and you can tune on-battery settings separately.

### Fix 6: Stop background services from saturating the disk

Measure who's actually using the drive.

1. **Task Manager** > **Processes** > sort by **Disk** during a slowdown and note the top consumers.
2. Disable **SysMain** if it's constantly active (`services.msc` > SysMain > Disabled) — it helps HDDs far more than SSDs.
3. If **Search Indexer** is the hog, rebuild or limit the index — our [search indexing guide](/articles/how-to-fix-search-indexing-high-cpu-windows-11-step-by-step/) walks through it.
4. Check **Windows Update** for stuck updates — **TiWorker.exe** at high disk for days means servicing is wedged, not working.
5. Guidance on persistent 100% disk usage is also on [Microsoft Support](https://support.microsoft.com/en-us/windows) — but on a healthy SSD with these services tamed, idle disk should sit near zero.

### Fix 7: Evaluate drive health and firmware

The final verdict: software or hardware.

1. Re-check **CrystalDiskInfo** — any status other than **Good**, or rising reallocated/media-error counts, means the NAND is failing.
2. Check for firmware updates in the manufacturer's toolbox app (Samsung Magician, Crucial Storage Executive, WD Dashboard, Intel MAS) and install with the machine plugged in and idle.
3. Watch temperatures — sustained operation above 70°C throttles many SSDs; improve cooling or add a heatsink on desktops.
4. If health is degrading: back up immediately, then replace the drive — SSDs rarely give much more warning than this.
5. If health is Good, firmware is current, and speeds are still low after Fixes 1–6, the bottleneck is elsewhere (RAM exhaustion causing paging, or CPU throttling) — check Task Manager's memory and CPU during the slowdown.

## Closing

SSD troubleshooting is measurement-driven: benchmark, fix the driver, free space and confirm TRIM, unthrottle power management, quiet the background hogs, and check health and firmware. Follow that order with numbers at each step, and you'll either restore full speed or know with certainty that the drive itself needs replacing.
