---
title: "SSD Running Slow in Windows 11? Restore Full Speed"
slug: how-to-fix-ssd-slow-on-windows-11-on-laptop
date: 2026-09-12
categories: ["performance"]
tags: ["ssd slow", "windows 11", "nvme slow", "trim", "disk performance"]
description: "SSD feeling slower than it should on Windows 11? Fix slow SSD speeds with TRIM, driver, and configuration checks that restore performance."
thumbnail: "/images/thumbs/how-to-fix-ssd-slow-on-windows-11-on-laptop.webp"
faqs:
  - q: "Why is my SSD slow on Windows 11 when it was fast before?"
    a: "The most common reasons are TRIM not running (so the drive can't efficiently reuse deleted blocks), an outdated storage or chipset driver, the SSD being nearly full, or aggressive power-saving settings throttling the drive. Windows 11 updates can also reset storage settings. The drive itself is rarely failing — configuration issues explain the vast majority of slowdowns."
  - q: "Does a full SSD run slower?"
    a: "Yes. SSDs need free space for wear leveling and garbage collection — their internal housekeeping. Once a drive passes about 75–80% full, write speeds can drop sharply because the controller has to shuffle data around to find writable blocks. Keeping at least 20–25% free is the simplest way to preserve performance."
  - q: "How do I check if TRIM is enabled on my SSD?"
    a: "Open Command Prompt as administrator and run `fsutil behavior query DisableDeleteNotify`. A result of 0 means TRIM is enabled (for both NVMe and SATA); a result of 1 means it is disabled. You can enable it with `fsutil behavior set DisableDeleteNotify 0`. TRIM lets Windows tell the SSD which blocks are free, which is essential for sustained write speed."
  - q: "Can Windows 11 power settings slow down my SSD?"
    a: "Yes. The PCI Express Link State Power Management setting and NVMe power-saving features can throttle SSD throughput to save battery, especially on laptops using the Balanced or Power Saver plan. Switching to the High Performance plan (or Best Performance power mode) and disabling aggressive PCIe power saving usually restores full speed at the cost of some battery life."
---

An SSD that benchmarks at half its rated speed — or a laptop that stutters despite having "fast" storage — is frustrating because you paid for speed you're not getting. On Windows 11 laptops, slow SSD performance is usually a configuration problem: TRIM disabled, outdated drivers, power-saving throttling, or a drive that's simply too full.

Before assuming the drive is dying, work through the software causes. They account for the overwhelming majority of SSD slowdowns, and they're all fixable in an afternoon. You'll need realistic expectations too: a SATA SSD tops out around 550 MB/s, while NVMe drives should hit thousands — know which you have before judging the numbers.

## Why this happens

- **TRIM not running**: Without TRIM, the SSD can't efficiently recycle deleted blocks and write speeds crater over time.
- **Drive nearly full**: Past ~80% capacity, the controller struggles with garbage collection and writes slow dramatically.
- **Outdated storage/chipset drivers**: Old AHCI or NVMe drivers cap throughput or mishandle modern drives.
- **Power-saving throttling**: PCIe link-state power management and NVMe power states trade speed for battery life.
- **Wrong SATA mode or old firmware**: IDE mode instead of AHCI, or ancient SSD firmware, both kneecap performance.
- **Background disk hogs**: Antivirus scans, Windows Search indexing, or a runaway process saturating the disk.
- **Failing drive**: Genuinely worn NAND or a dying controller — the least common cause, but worth ruling out.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Benchmark and establish a baseline

You can't fix what you haven't measured — get real numbers first.

1. Download **CrystalDiskMark** (free) and run the default test on your system drive. Note the sequential read/write and random 4K numbers.
2. Compare against your SSD's rated specs (check the manufacturer's product page). A SATA SSD should read around 500–550 MB/s; a PCIe 3.0 NVMe drive should exceed 2,000 MB/s; PCIe 4.0 drives go far higher.
3. Open **Task Manager** > **Performance** > **Disk** and check the drive model, then watch **Active time** during normal use — if it sits at 100% while speeds are low, something is saturating the disk rather than the drive being slow.
4. Check free space: open **File Explorer** > **This PC** and look at the drive's used percentage. Over 80% full is a red flag on its own.
5. If Task Manager shows a specific process hammering the disk, address that first — our guide to [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) covers tracking down disk hogs.

### Fix 2: Verify TRIM and run Optimize

TRIM is the single most important SSD maintenance task, and Windows sometimes stops doing it.

1. Open **Command Prompt as administrator** and run `fsutil behavior query DisableDeleteNotify`. You want `DisableDeleteNotify = 0` (TRIM enabled). If it shows 1, enable it with `fsutil behavior set DisableDeleteNotify 0`.
2. Open **Defragment and Optimize Drives** (search "defragment" in Start). Your SSD should show **Media type: Solid state drive** — if Windows misdetects it as a hard disk, that's a problem to investigate.
3. Select the SSD and click **Optimize**. For SSDs this issues a TRIM/retrim pass, not a defrag. Run it manually now.
4. Click **Change settings** and confirm **Run on a schedule** is on (weekly is fine) so TRIM keeps happening automatically.
5. Re-run CrystalDiskMark after the optimize pass — TRIM-deprived drives often recover significant write speed immediately.

### Fix 3: Free up space and reduce write pressure

A cramped SSD is a slow SSD — give the controller room to work.

1. Aim to keep at least **20–25% of the drive free**. If you're above 80% used, that's likely a major contributor.
2. Run **Disk Cleanup**: search for it in Start, select your system drive, click **Clean up system files**, and remove Windows Update leftovers, temporary files, and old Device driver packages.
3. Open **Settings** > **System** > **Storage** and enable **Storage Sense** to auto-clean temp files and recycle bin contents.
4. Move large media libraries (videos, game installs you rarely play) to an external drive — big static files are the easiest wins.
5. Check for runaway folders: your browser cache, `C:\Windows\Temp`, and cloud sync conflict copies can silently eat tens of gigabytes.

### Fix 4: Update storage, chipset, and SSD firmware

Drivers are the second most common cause after TRIM and capacity.

1. Open **Device Manager** > **Storage controllers** and **IDE ATA/ATAPI controllers** — right-click each entry and choose **Update driver** > **Search automatically for drivers**.
2. Install your laptop manufacturer's **chipset driver** from their support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Chipset drivers include the storage controller optimizations Windows needs.
3. Check for **SSD firmware updates** using the manufacturer's utility (Samsung Magician, WD Dashboard, Crucial Storage Executive, Intel MAS). Firmware updates regularly fix performance bugs — back up important data first, as firmware flashing carries small risk.
4. Verify your SATA controller is in **AHCI mode**, not IDE: check in Device Manager under IDE ATA/ATAPI controllers, or in BIOS/UEFI settings. (Don't flip this casually on a working install — changing modes without preparation can prevent booting.)
5. Reboot and re-benchmark after driver updates to confirm the improvement.

### Fix 5: Disable aggressive power saving for storage

Laptop power plans love to throttle the SSD to save milliwatts.

1. Open **Control Panel** > **Power Options** > **Change plan settings** (on your active plan) > **Change advanced power settings**.
2. Expand **PCI Express** > **Link State Power Management** and set it to **Off** (at least while plugged in). This is a frequent SSD-speed killer on laptops.
3. Expand **Hard disk** > **Turn off hard disk after** and set it to **Never** for SSDs — an SSD uses negligible idle power anyway.
4. In **Settings** > **System** > **Power & battery**, set **Power mode** to **Best performance** while testing.
5. Re-benchmark. If speeds recover, you've found the tradeoff: keep performance settings while plugged in, and accept slightly lower speeds (and longer battery) on battery power.

### Fix 6: Check drive health and rule out failure

If nothing above helps, verify the drive itself is healthy.

1. Install **CrystalDiskInfo** (free) and check the drive's **Health Status** and SMART attributes — look at **Percentage Used** (NVMe) or **Wear Leveling Count** / **Reallocated Sectors** (SATA).
2. A health status of **Good** with low wear means the drive is fine and the problem is elsewhere. **Caution** or **Bad** means back up immediately.
3. Run a full error check: open **Command Prompt as administrator** and run `chkdsk C: /f /r` (schedule at reboot if prompted). This finds file-system corruption that can masquerade as slowness.
4. If the drive is healthy but slow and old, check whether it's a DRAM-less budget SSD — those slow down dramatically under sustained writes by design, and no setting fully fixes that.
5. For a genuinely failing drive, clone to a replacement SSD promptly — and see [checking disk health basics](/articles/how-to-speed-up-windows-11-laptop/) for related maintenance. Microsoft documents storage troubleshooting at Windows support.

## Closing

Slow SSDs on Windows 11 are usually suffering from neglect, not age: TRIM disabled, the drive packed full, outdated drivers, or power settings strangling throughput. Work through the fixes in order, re-benchmark as you go, and you'll almost always recover the speed you paid for — no replacement drive required.
