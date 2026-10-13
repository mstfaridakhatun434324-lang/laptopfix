---
title: "Slow File Transfer on Windows 11? Here's What to Do"
slug: what-to-do-if-windows-11-slow-file-transfer
date: 2026-09-28
categories: ["performance"]
tags: ["slow file transfer", "windows 11", "copy speed", "usb transfer", "file explorer"]
description: "Windows 11 copying files at a crawl? Learn why transfers slow down and how to get full speed back from USB drives, network shares, and internal disks."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-slow-file-transfer.webp"
faqs:
  - q: "Why is file transfer so slow on Windows 11?"
    a: "The most common reasons are USB ports running at 2.0 speeds, antivirus scanning every file during the copy, remote differential compression overhead on network transfers, outdated storage drivers, and a drive that is nearly full or failing. Large numbers of small files also copy far slower than one big file because each file needs its own setup and teardown."
  - q: "Is slow file transfer a sign my hard drive is failing?"
    a: "It can be. A drive developing bad sectors retries reads repeatedly, which tanks copy speed and causes freezes during transfers. If speeds dropped suddenly, you hear clicking, or Event Viewer shows disk errors under Windows Logs > System, back up your data immediately and run a SMART check before doing anything else."
  - q: "Does Remote Differential Compression really slow down copies?"
    a: "On local network copies it can add measurable overhead, because Windows computes checksums to avoid copying unchanged data — pointless work when you are copying fresh files to a new destination. Disabling it is a safe, reversible tweak that many people report speeds up network transfers, especially for large media files."
  - q: "Should I use a third-party tool for faster file copying?"
    a: "Third-party copiers can help with specific jobs like batch small-file transfers or unreliable network links, because they queue better and resume after interruptions. For most people, though, fixing the underlying bottleneck — the USB port speed, the driver, or the antivirus setting — delivers a bigger and more permanent improvement than any copy tool."
---

You plug in a USB drive, drag over a folder, and the progress bar barely moves — stuck at a few megabytes per second on hardware that should do ten times that. Slow file transfer on Windows 11 is one of those problems that wastes hours quietly, because most people just wait instead of fixing it.

Here's the good news: in the vast majority of cases the hardware is fine. The slowdown comes from a setting, a driver, or a background service getting in the way. A Windows 11 laptop with a decent SSD should sustain several hundred megabytes per second between internal partitions and 100+ MB/s to a USB 3 drive. If you're seeing a fraction of that, something is throttling you — and it's usually fixable in minutes.

We'll walk through diagnosis first so you fix the real bottleneck, not a random setting. If folders themselves open slowly as well as copy slowly, our [File Explorer repair guide](/articles/how-to-fix-file-explorer-slow-after-windows-11-update/) covers that side of the problem.

## Why this happens

- **Wrong USB port speed**: The flash drive is in a USB 2.0 port (black or white insert) instead of a USB 3.x port (blue or red insert), capping speed at ~35 MB/s.
- **Antivirus real-time scanning**: Microsoft Defender scans every file as it's written, which turns small-file copies into a crawl.
- **Remote Differential Compression**: A legacy Windows feature that adds checksum overhead to network copies with zero benefit for fresh files.
- **Outdated storage drivers**: The chipset, NVMe, or USB controller driver is generic or years old, leaving performance modes disabled.
- **Nearly full or fragmented drive**: HDDs slow dramatically above ~85% capacity; even SSDs throttle when nearly full.
- **Failing drive sectors**: Bad sectors force repeated read retries — transfers stutter, hang, and occasionally error out.
- **Background disk hogs**: Search indexing, OneDrive sync, or Windows Update consuming the same disk during your copy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify you're actually on a fast USB port

Half of all "slow transfer" complaints end here.

1. Look at the port: USB 3.x ports usually have a **blue** or **red** plastic insert; USB 2.0 ports are black or white. Move the drive to a blue/red port.
2. In **Device Manager** > **Universal Serial Bus controllers**, confirm you see entries like **USB 3.x** or **xHCI** — not just "USB 2.0 Hub".
3. Check the drive itself: cheap flash drives often write at 10–20 MB/s no matter what. Test with a second drive to separate drive limits from system limits.
4. For USB-C ports, make sure you're using a data-capable cable — charge-only cables negotiate at USB 2.0 speeds or don't transfer data at all.
5. Retest the copy and note the speed: if it jumped from ~5 MB/s to 80+ MB/s, you were simply in the wrong port.

### Fix 2: Rule out a failing drive before anything else

If speed collapsed suddenly, check drive health first — no tweak helps a dying disk.

1. Open **Command Prompt as administrator** and run `wmic diskdrive get status` — every drive should say **OK**.
2. Check **Event Viewer** > **Windows Logs** > **System** for recent **disk** errors or warnings — a growing list means bad sectors.
3. Copy a single large file (1 GB+) and watch: a healthy drive holds a steady speed; a failing one surges, stalls, surges, stalls.
4. If anything looks wrong, back up your important files **now** before running any repair — disk checks can push a marginal drive over the edge.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in error-checking tool (`chkdsk`) if you need guided steps for a scan.

### Fix 3: Update storage and chipset drivers

Generic Windows drivers leave performance on the table.

1. Open **Device Manager**, expand **Disk drives**, right-click your SSD/HDD, and check the driver date under **Properties** > **Driver** — if it's from the Windows install era, update it.
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers** and do the same.
3. Get chipset and storage drivers from your laptop maker — Dell, HP, and Lenovo all offer driver-detection tools on their support sites — rather than relying on Windows Update alone.
4. Also update USB controller drivers the same way; an old xHCI driver can cap USB 3 drives at USB 2 speeds.
5. Reboot and retest — driver updates commonly restore 2–3x copy speed on systems running generic drivers.

### Fix 4: Disable Remote Differential Compression for network copies

If the slow copy is to a NAS or shared folder, this legacy feature is a prime suspect.

1. Press `Win + R`, type `optionalfeatures`, and press Enter.
2. Scroll to **Remote Differential Compression API Support** and **uncheck** it.
3. Click OK and let Windows apply the change — a reboot may be required.
4. Retest your network copy. For large fresh files, many users see a clear speed jump because Windows stops computing checksums it doesn't need.
5. This is fully reversible — recheck the box if you ever notice delta-based sync tools behaving differently (rare).

### Fix 5: Tame antivirus scanning during big copies

Real-time protection scans each file on write — brutal for thousands of small files.

1. For a one-off big copy, temporarily exclude the destination folder: **Windows Security** > **Virus & threat protection** > **Manage settings** > **Exclusions** > **Add an exclusion** > **Folder**.
2. Run the copy, then **remove the exclusion** afterward — don't leave permanent exclusions on folders you download into.
3. Alternatively, schedule large copies for idle time: Defender's impact is much lower when you're not also browsing and working.
4. If a third-party antivirus is installed, its on-access scanner is usually even heavier — check its settings for a "gaming/silent mode" or scheduled-scan option.
5. Note: if your copies involve many tiny files, a faster fix is archiving them into a single ZIP first — one big file copies far faster than 10,000 small ones regardless of antivirus.

### Fix 6: Free space and check the drive's condition

Full drives are slow drives — especially HDDs and nearly-full SSDs.

1. Open **Settings** > **System** > **Storage** and check free space on both source and destination — aim for at least **15–20% free**.
2. Run **Disk Cleanup** (`cleanmgr`) or Storage Sense to clear temp files, old Windows Update leftovers, and the Recycle Bin.
3. For HDDs (not SSDs), run **Defragment and Optimize Drives** (`dfrgui`) — never defrag an SSD; Windows handles SSD optimization automatically.
4. Check the destination drive's health too — copying **to** a failing drive is just as slow as copying from one.
5. If the drive is an external HDD, make sure it's not sleeping mid-copy: in **Power Options** > **Advanced**, set **USB selective suspend** to Disabled as a test.

### Fix 7: Stop background processes competing for the disk

A copy fighting the indexer and the cloud for I/O will always lose.

1. Open **Task Manager** > **Performance** > **Disk** during a slow copy — if active time is pinned at 100% while your copy crawls, something else is eating I/O.
2. Sort **Processes** by the Disk column to find the hog: common culprits are **Search Indexer**, **OneDrive**, **Antimalware Service Executable**, and **TiWorker**.
3. Pause OneDrive sync during the copy (tray icon > **Pause syncing**), and let the search indexer finish or [reduce its indexed scope](/articles/best-way-to-fix-search-indexing-high-cpu-windows-11/) if it never settles.
4. Pause Windows Update downloads during big transfers: **Settings** > **Windows Update** > **Pause updates**.
5. Retest with the hogs quiet — if speed recovers, you've found your bottleneck, and managing those background tasks is the permanent fix.

## Closing

Slow file transfer on Windows 11 is almost never a hardware limitation — it's a USB 2 port, an outdated storage driver, antivirus scanning every file, or a background process hogging the disk. Check the port, check the drive's health, update drivers, and quiet the background competition, and your copies will usually return to full speed without spending a cent.
