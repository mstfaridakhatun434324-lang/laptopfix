---
title: "How to Fix Slow File Transfer Speeds in Windows 11"
slug: how-to-fix-windows-11-slow-file-transfer
date: 2026-09-14
categories: ["performance"]
tags: ["file transfer", "slow copy", "windows 11", "usb", "ssd"]
description: "File copies crawling at a few MB/s in Windows 11? From USB settings to the infamous Remote Differential Compression, here are the fixes that restore full transfer speed."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-file-transfer.webp"
faqs:
  - q: "Why is file transfer so slow in Windows 11?"
    a: "Common causes include the drive being nearly full, USB ports running at slower speeds than expected, antivirus scanning every file during the copy, Remote Differential Compression adding overhead, outdated storage drivers, or the destination drive being an old HDD. Large numbers of small files also transfer much slower than a single large file of the same total size."
  - q: "What transfer speed should I expect from USB?"
    a: "USB 2.0 tops out around 35 MB/s in practice, USB 3.0/3.1 Gen 1 around 300-400 MB/s, and USB 3.2 Gen 2 up to about 1 GB/s — but the actual speed is limited by the slowest component, usually the drive itself. A spinning external HDD rarely exceeds 120 MB/s regardless of the USB version."
  - q: "Does antivirus slow down file transfers?"
    a: "Yes, noticeably. Real-time protection scans files as they're written, which adds overhead to every file copied. This is most visible when copying thousands of small files. Temporarily disabling real-time protection for a large trusted transfer can double speeds, but remember to turn it back on afterward."
  - q: "Why do small files transfer slower than large files?"
    a: "Each file carries overhead: Windows has to create the file entry, set permissions, update the directory, and flush metadata — for every single file. With thousands of tiny files, this per-file overhead dominates. Zipping them into one archive before transferring is often dramatically faster."
---

Watching a file copy crawl along at 5 MB/s when your hardware should manage a hundred times that is a special kind of frustration. Slow file transfers in Windows 11 are extremely common, and the causes range from simple (wrong USB port) to obscure (a Windows feature called Remote Differential Compression quietly adding overhead to every copy). The tricky part is that the bottleneck is rarely where you'd guess — the copy dialog shows you a speed, but not what's limiting it.

The approach that works is eliminating bottlenecks one at a time: verify the hardware link speed, remove software overhead, fix driver and filesystem issues, and optimize how you do the transfer itself. Most people find their speed jumps dramatically after just one or two of these fixes. A quick baseline helps: copy a single large file (1GB+) and note the speed, then compare after each change.

Before diving in, set expectations honestly. Your transfer can never exceed the slowest component — a USB 2.0 flash drive won't go faster than ~35 MB/s no matter what you tweak. These fixes remove artificial slowdowns; they can't make slow hardware fast.

## Why this happens

- **Wrong USB port or cable**: Plugging a USB 3.x drive into a USB 2.0 port (or using a USB 2.0 cable) silently caps speed at ~35 MB/s.
- **Antivirus real-time scanning**: Every file copied gets scanned on write, adding major overhead especially with many small files.
- **Remote Differential Compression**: This legacy Windows feature adds overhead to file operations and rarely helps on modern systems.
- **Nearly-full destination drive**: Drives slow down significantly when over 85-90% full, especially SSDs without free space for wear leveling.
- **Outdated storage drivers**: Old USB, chipset, or storage controller drivers can prevent the system from using full link speeds.
- **Fragmented or failing HDD**: Mechanical drives with fragmentation or developing bad sectors transfer slowly and erratically.
- **Thousands of small files**: Per-file overhead (creating entries, setting permissions) dominates when copying many tiny files.
- **Write caching disabled**: Without write caching, every write waits for the drive to confirm, which tanks throughput on some hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify you're using the right USB port and cable

This is the number one cause of mysteriously slow USB transfers. USB ports look identical but perform very differently.

1. Check your laptop's manual or port markings — USB 3.x ports are often blue inside or marked "SS" (SuperSpeed).
2. Move the drive to a USB 3.x port and retest with the same large file.
3. Try a different cable — many cheap cables are USB 2.0 internally despite USB-C connectors.
4. In Device Manager, expand **Universal Serial Bus controllers** and confirm you see "USB 3.0/3.1 eXtensible Host Controller" entries.

If speeds jump after switching ports, you've found it. If you're troubleshooting broader USB issues, also check whether the drive itself is the limit by testing it on another computer.

### Fix 2: Test with a single large file

This diagnostic tells you whether the problem is per-file overhead or a genuine throughput bottleneck.

1. Create a 1GB+ test file (or use a large video file you already have).
2. Copy it and note the sustained speed in the copy dialog.
3. Now copy a folder with thousands of small files totaling a similar size and compare.
4. If the large file is fast but the folder is slow, per-file overhead is your issue — zip folders before transferring (see Fix 7).

### Fix 3: Disable Remote Differential Compression

RDC is a legacy feature designed for slow networks that adds overhead to local file operations. Disabling it is safe and often helps.

1. Open **Control Panel > Programs > Turn Windows features on or off**.
2. Uncheck **Remote Differential Compression API Support**.
3. Click OK and restart your laptop.
4. Retest your transfer speeds.

### Fix 4: Update storage and chipset drivers

Outdated drivers can silently limit your storage to slower transfer modes.

1. Open **Device Manager** and expand **Disk drives**, **IDE ATA/ATAPI controllers**, and **Universal Serial Bus controllers**.
2. Right-click each storage-related entry and choose **Update driver > Search automatically**.
3. For the full fix, get chipset drivers from your laptop manufacturer's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo.
4. Use the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel-based systems.
5. Restart and retest.

### Fix 5: Free up space on the destination drive

SSDs slow down dramatically when nearly full because they lack free blocks for wear leveling and write combining.

1. Check free space on the destination drive — aim for at least 15-20% free.
2. Run **Disk Cleanup** (search for it in Start) to remove temporary files and old update data.
3. Move large unused files to another drive or external storage.
4. Our guide on [how to free up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/) covers this thoroughly.

### Fix 6: Enable write caching on the drive

Write caching lets Windows batch writes instead of waiting for each one to complete, which significantly improves throughput on many drives.

1. Open **Device Manager**, expand **Disk drives**, and right-click your drive (or the external drive).
2. Choose **Properties > Policies** tab.
3. Check **Enable write caching on the device** (and "Turn off Windows write-cache buffer flushing" only for drives with their own power backup — generally leave the second box unchecked for external drives).
4. Click OK and retest.

Note: don't enable aggressive write caching on external drives you unplug without ejecting — use "Safely Remove Hardware" to avoid data loss.

### Fix 7: Zip before transferring and pause the antivirus

For the actual transfer technique: archives and fewer antivirus interruptions make a huge difference.

1. For folders with many small files, right-click the folder and choose **Compress to ZIP file** before copying — one large file transfers far faster than thousands of small ones.
2. For large trusted transfers, temporarily turn off real-time protection: **Windows Security > Virus & threat protection > Manage settings > Real-time protection** (turn it back on immediately after).
3. Avoid running other disk-heavy tasks (backups, indexing, game downloads) during the transfer.
4. If copying over the network, check that you're on a wired connection or strong Wi-Fi — wireless transfers are often the real bottleneck.

If your system is generally sluggish beyond file transfers, our guide on [how to speed up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/) addresses the bigger picture.

## Closing

Slow file transfers in Windows 11 almost always come down to a handful of fixable bottlenecks: the wrong USB port, antivirus overhead, RDC, driver issues, or a nearly-full drive. Work through them with a large test file as your benchmark, and you'll usually find one change that restores the speeds your hardware is actually capable of.
