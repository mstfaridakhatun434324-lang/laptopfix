---
title: "Best Way to Fix Slow File Transfer on Windows 11"
slug: "best-way-to-fix-windows-11-slow-file-transfer"
date: 2026-09-30
categories: ["performance"]
tags: ["slow file transfer", "copy speed", "usb 3", "windows 11", "file copy"]
description: "The most effective fixes for slow file copies on Windows 11, ranked: from checking the USB link to driver updates that restore full speed."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-slow-file-transfer.webp"
faqs:
  - q: "What is the most common cause of slow file transfer on Windows 11?"
    a: "A mismatched USB link — a USB 3 drive plugged into a USB 2.0 port, or connected with a USB 2.0 cable — caps speeds near 35 MB/s regardless of settings. It is the most common cause because laptop ports are often a mix of generations with unclear labeling. Before changing any Windows setting, test the drive in every port with a known-good cable; this single check resolves more “slow transfer” complaints than all software tweaks combined."
  - q: "Should I use a third-party file copy tool?"
    a: "Tools like TeraCopy or FastCopy can help in specific cases — they handle errors better, verify copies, and manage queues more intelligently than Explorer. But they cannot exceed the hardware limit: if your USB link negotiates at USB 2.0 speeds, no software copies faster than 35 MB/s. Fix the hardware link first; consider a copy manager only for reliability features like verification and pause/resume on huge jobs."
  - q: "Why are small files so much slower to copy than large ones?"
    a: "Every file carries fixed overhead: creating the directory entry, setting permissions, antivirus scanning, and index updating. For a 5 GB video that overhead is negligible; for 10,000 tiny files it dominates, and the drive spends more time seeking than transferring. Archiving small files into a single ZIP before copying — then extracting at the destination — is often dramatically faster than copying them individually."
  - q: "Does the file system (NTFS, exFAT, FAT32) affect speed?"
    a: "Somewhat. NTFS is generally fastest on Windows with features like journaling optimized for the OS, while exFAT is the practical choice for cross-platform drives at a small performance cost. FAT32 should be avoided for large transfers entirely — its 4 GB file limit aside, it is slow with modern workloads. For a Windows-only external SSD, NTFS is the best pick; for a drive shared with Macs, exFAT is the compromise."
---
File transfers should be boring: drag, drop, done. When a 10 GB copy takes half an hour on Windows 11, something is wrong — and the fix is rarely the registry hack a forum swears by. This guide ranks the fixes by effectiveness, so you start with the checks that solve most cases and stop the moment your speeds recover.

The ranking reflects a simple truth: transfer speed is a chain — drive, cable, port, driver, Windows settings, antivirus — and the slowest link decides everything. Software tweaks cannot fix a USB 2.0 link, and a new cable cannot fix a dying drive. Work the chain in order.

If you want the full diagnostic walkthrough with benchmarks instead of the ranked list, our [troubleshooting guide](/articles/windows-11-slow-file-transfer-troubleshooting/) is the companion piece.

## Why this happens

- **USB 2.0 link in the chain:** wrong port or cable caps everything near 35 MB/s — the most common cause by far.

- **Drive's write cache exhausted:** consumer flash drives slow sharply after a few GB of sustained writes.

- **Thousands of small files:** per-file overhead dominates, making folders of tiny files crawl.

- **Antivirus real-time scanning:** every file scanned on write; worst with many small files.

- **Remote Differential Compression overhead:** Windows comparing file chunks adds CPU cost to copies.

- **Write caching disabled:** the safe-removal default policy sacrifices speed on external drives.

- **Outdated USB/chipset drivers:** misnegotiated link speeds after Windows updates.

- **Failing drive:** retrying bad sectors produces erratic, collapsing speeds.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Match the drive, port, and cable generation

Ranked first because it solves the majority of cases in two minutes. USB is backward compatible, which means a USB 3 drive silently works — slowly — on a USB 2.0 port or cable with no warning from Windows.

1. Try every USB port on the laptop with the same drive and note the speed in the copy dialog.
2. Blue or teal port interiors usually indicate USB 3.x; black usually means USB 2.0.
3. Swap to a known USB 3 cable — many bundled cables are USB 2.0 despite identical connectors.
4. A USB 3 drive on a proper USB 3 link should exceed 100 MB/s on sequential writes.
5. If speeds recover, stop here — the chain was broken at the link, not in Windows.

### Fix 2: Fix 2: Switch the drive to Better performance policy

Ranked second: Windows defaults external drives to quick-removal mode, disabling write caching. Flipping the policy enables the cache and lifts sustained writes noticeably — the trade-off is remembering to eject safely.

1. Open Device Manager > Disk drives, right-click the external drive > Properties > Policies.
2. Select Better performance and check Enable write caching on the device.
3. Click OK.
4. Always use Safely Remove Hardware before unplugging from now on.
5. Re-run a large copy to measure the gain — 20–50 percent improvements are typical.

### Fix 3: Fix 3: A/B test with antivirus paused

Ranked third because real-time scanning is the biggest software-side drag, especially on folders of small files. A two-minute test tells you definitively whether the scanner is your bottleneck.

1. Copy a representative folder and note the speed.
2. Temporarily disable real-time protection in Windows Security.
3. Repeat the identical copy immediately and compare.
4. Re-enable protection right away regardless of the result.
5. If the scanner was the drag, add a permanent exclusion for the destination folder rather than leaving protection off.

### Fix 4: Fix 4: Disable Remote Differential Compression

Ranked fourth: RDC adds per-chunk comparison overhead that made sense on slow WAN links and mostly wastes CPU today. Disabling it is safe, reversible, and helps network copies most.

1. Open Control Panel > Programs > Turn Windows features on or off.
2. Uncheck Remote Differential Compression API Support and click OK.
3. Restart if prompted.
4. Re-test your typical copy scenario.
5. No improvement? Re-enable it — it was not your bottleneck, as Microsoft's [Windows support docs](https://support.microsoft.com/en-us/windows) imply it rarely is on modern hardware.

### Fix 5: Fix 5: Update USB and chipset drivers

Ranked fifth: driver bugs that misnegotiate USB speeds are common after feature updates, and vendor drivers fix them. This is the fix for “this port used to be fast.”

1. Get the latest chipset and USB 3.x drivers for your exact model from the laptop vendor's support site.
2. Install chipset first, then USB controller drivers, restarting as prompted.
3. Verify in Device Manager that USB 3.x host controllers report correctly.
4. Re-test with a large single file to confirm full link speed is restored.
5. Skip generic driver updaters — vendor drivers are safer and sufficient.

### Fix 6: Fix 6: Check the drive's health

Ranked sixth because it is the least fun answer: sometimes the drive is simply dying. Erratic speeds that collapse mid-copy and never recover point here. Our [disk usage guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-on-hp-laptop/) covers drive-health checks in detail.

1. Run CrystalDiskInfo and check the SMART status.
2. Caution or Bad — especially reallocated or pending sectors — means replace the drive.
3. Back up anything important immediately; do not run heavy benchmarks on a dying drive.
4. For internal drives, run chkdsk C: /scan from an elevated prompt.
5. No software fix repairs failing hardware — replacement is the only real solution.

### Fix 7: Fix 7: Zip small files before copying

Ranked last because it is a workflow change, not a fix — but for folders of thousands of tiny files it is often the biggest speedup available, since it eliminates per-file overhead entirely.

1. Right-click the folder of small files and compress it to a ZIP (or use 7-Zip for better compression).
2. Copy the single archive — sequential speed, minimal overhead.
3. Extract at the destination.
4. Compare total time against the direct copy; 3–5x faster is common for tiny-file collections.
5. Use this approach for photo libraries, code repos, and document archives.

## Closing

The ranked list works because transfer speed is a chain, and chains are fixed at their weakest link: match the USB generation first, enable write caching, rule out the antivirus, trim Windows overhead, update drivers, check drive health — and zip tiny files when the workload itself is the problem. Start at the top, stop when speeds recover, and you will spend minutes on this instead of an afternoon.
