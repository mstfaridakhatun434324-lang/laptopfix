---
title: "Windows 11 Slow File Transfer? Speed Up Copy Speeds"
slug: how-to-fix-windows-11-slow-file-transfer-youtube
date: 2026-09-01
categories: ["performance"]
tags: ["slow file transfer", "windows 11", "copy speed", "usb", "ssd"]
description: "File copies crawling on Windows 11? Diagnose slow transfer speeds on USB drives, SSDs, and network shares — and fix them."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-file-transfer-youtube.webp"
faqs:
  - q: "Why is file transfer so slow on Windows 11 compared to Windows 10?"
    a: "The most reported cause is Windows 11's mandatory SMB signing and tightened security defaults slowing network transfers, plus early 22H2 builds having a genuine large-file copy regression (fixed in later cumulative updates). For USB, the cause is usually the drive itself — a flash drive's advertised speed versus its real sustained write speed — or the USB port negotiating a slower standard than expected."
  - q: "What is a normal USB transfer speed I should expect?"
    a: "USB 3.x flash drives realistically sustain 100–400 MB/s depending on quality; cheap drives often manage only 20–60 MB/s on large writes despite USB 3 branding. External SSDs over USB 3.2 Gen 2 should hit 400–1000 MB/s. If you're seeing under 30 MB/s on a USB 3 port with a decent drive, something is wrong — usually the port, cable, or drive's cache being exhausted."
  - q: "Does antivirus slow down file transfers?"
    a: "Yes, measurably. Real-time protection scans files as they're written, which can halve transfer speeds on large copies — especially with many small files. As a diagnostic, pause real-time protection briefly during a test copy. If speed doubles, the AV is the bottleneck; the practical fix is scheduling big copies when protection can stay on, or excluding trusted destinations."
  - q: "Why do many small files copy slower than one big file?"
    a: "Every file carries overhead: creating the directory entry, updating the journal, security descriptors, and thumbnail/indexer attention. Ten thousand small files can take ten times longer than a single file of the same total size. Zipping small files before transfer, or using a tool like Robocopy with multithreading, dramatically cuts this overhead."
---

Watching a file copy dialog crawl at 8 MB/s when you know your hardware can do ten times that is a special kind of frustration. Slow file transfer on Windows 11 has distinct flavors — USB copies, internal drive-to-drive copies, and network transfers — and each has its own usual suspects. This guide covers all three, because the "slow transfer" complaint rarely specifies which until you dig in.

The pattern: first identify which kind of transfer is slow and measure it properly, then work the cause list for that type. A USB stick that writes at 25 MB/s is probably just a cheap stick; a network share that dropped from 110 MB/s to 30 MB/s after upgrading to Windows 11 is a configuration problem with a real fix. If your whole drive feels slow (not just copies), see [fixing slow SSDs](/articles/best-way-to-fix-ssd-slow-on-windows-11/); for general system sluggishness, [speeding up a slow laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **USB port/cable negotiating a slower standard**: A USB 3 drive in a USB 2 port (or with a charge-only cable) caps at ~35 MB/s.
- **Cheap flash drive with exhausted cache**: Budget drives burst fast for seconds, then collapse to native NAND speed.
- **Windows 11 SMB signing overhead**: Mandatory signing on network shares costs significant throughput on some setups.
- **Antivirus real-time scanning**: Every file scanned on write — brutal for many-small-file copies.
- **Nearly-full destination SSD**: SSDs lose write speed dramatically above ~85% capacity.
- **Outdated USB/chipset drivers**: Old drivers can prevent USB 3.x link training entirely.
- **Indexing and thumbnails competing**: The search indexer and thumbnail generator fighting the copy for disk I/O.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure properly and identify the transfer type

Numbers first — "slow" needs a baseline.

1. Run a proper benchmark: copy a single 2–4 GB file (a movie or ISO) and note the sustained speed after the first 10 seconds (ignore the initial burst).
2. Identify the type: **USB external**, **internal drive-to-drive**, or **network share** — the fixes diverge completely from here.
3. For USB: check which port you're using — blue/teal inserts or SS markings indicate USB 3.x; try a different port, preferably one directly on the laptop (not a hub).
4. For network: test with a large single file and note whether speed is consistent or saw-toothing — consistent-but-slow suggests signing/encryption overhead; saw-toothing suggests Wi-Fi or disk contention.
5. Record your numbers — you'll compare after each fix to know what actually helped.

### Fix 2: Fix USB transfer speeds

The most common "slow transfer" complaint.

1. Verify the port speed: **Device Manager** > **Universal Serial Bus controllers** — look for "USB 3.x" host controllers, and check the drive appears under the right hub. A USB 3 drive showing under a USB 2 hub means the port or cable is the limiter.
2. Try every USB port on the laptop — ports on opposite sides often use different controllers, and one may train at full speed while another doesn't.
3. Ditch hubs and adapters for the test — connect directly. Cheap hubs silently downgrade to USB 2 speeds.
4. For external SSDs/HDDs: open **Device Manager** > **Disk drives** > your external drive > **Policies** tab > select **Better performance** (enables write caching) — then always use **Safely Remove Hardware**.
5. Update USB/chipset drivers: [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop vendor's support site. If the drive is just cheap (sustained 20–40 MB/s regardless of port), no software fix will save it — that's the hardware.

### Fix 3: Fix many-small-file copies

Where "slow" is really "overhead."

1. For thousands of small files, zip them first — one large archive copies an order of magnitude faster than the loose files, then extract at the destination.
2. Use **Robocopy** with multithreading: open Terminal and run `robocopy "source" "dest" /E /MT:16` — 16 threads dramatically cut per-file overhead versus Explorer's single-threaded copy.
3. Temporarily pause real-time antivirus during the copy as a test (**Windows Security** > **Virus & threat protection** > **Manage settings**) — if speed multiplies, the AV is your bottleneck; re-enable it after and schedule big copies accordingly.
4. Disable **Remote Differential Compression** for network copies of small files (Windows Features > uncheck it) — its per-file hashing overhead exceeds its benefit on fast LANs.
5. Close the destination folder in File Explorer during the copy — Explorer generating thumbnails and previews for incoming files slows the write stream.

### Fix 4: Fix slow network transfers (SMB)

Windows 11's security defaults cost throughput.

1. First, rule out Wi-Fi: test with an Ethernet cable if possible. A "slow network transfer" that's actually a weak Wi-Fi link is the most common misdiagnosis.
2. Check SMB signing requirements: in an elevated PowerShell, run `Get-SmbClientConfiguration` — if **RequireSecuritySignature** is True, signing is mandatory and costs 20–40% throughput on some hardware.
3. On trusted home networks, you can relax this: `Set-SmbClientConfiguration -RequireSecuritySignature $false -Confirm:$false` — understand this reduces security against network attacks; never do it on untrusted networks.
4. Ensure both PCs use the **Private** network profile (**Settings** > **Network & internet** > connection > **Private**) — Public profile throttles discovery and sharing features.
5. Update the **network adapter driver** from your laptop vendor or Intel/Realtek directly — driver-level SMB performance fixes are common. Microsoft documents sharing performance on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Free the destination drive and stop I/O competition

A choked destination can't receive fast no matter the source.

1. Check destination free space: if the SSD is over 85% full, free space until it's under 80% — SSD write speeds collapse when the drive can't find fresh blocks.
2. Pause **OneDrive/Dropbox** sync during large copies — sync engines competing for the same disk cut copy speeds substantially.
3. Pause the **search indexer** temporarily: `services.msc` > **Windows Search** > **Stop** during the copy, restart after.
4. Check Task Manager > **Performance** > disk — if **Active time** is pinned at 100% with low transfer rates, something else is hammering the disk; sort Processes by Disk to find it.
5. For HDD destinations: run **Defragment and Optimize Drives** (`dfrgui`) — heavily fragmented spinning disks copy slowly; never defrag SSDs (use TRIM/Optimize instead, which Windows handles automatically).

### Fix 6: Update Windows — the 22H2 copy regression

A genuine Windows bug bit many users.

1. Early Windows 11 22H2 builds had a confirmed bug slowing large file copies by up to 40% — fixed in cumulative update **KB5022913** and later.
2. Open **Settings** > **Windows Update** and install everything pending — if you've been deferring updates, this alone may restore full speed.
3. Check your build: **Win+R** > `winver` — anything before the fixed cumulative updates is suspect for copy slowness.
4. After updating, re-run your Fix 1 benchmark with the same file — compare numbers to confirm the improvement.
5. Keep **Delivery Optimization** from eating bandwidth during copies: **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** > limit background bandwidth.

### Fix 7: Hardware reality check

When it's not Windows' fault.

1. Test the same USB drive on another computer — same slow speed means the drive is the limiter, not your laptop.
2. Check drive health: **CrystalDiskInfo** (free) shows SSD health percentage and HDD reallocated sectors — a dying drive gets slow before it gets dead.
3. For external HDDs: listen for clicking or rhythmic seeking during copies — audible distress plus slowness means back up immediately and replace.
4. Try a different cable for external drives — USB-C cables especially vary wildly; a charge-only or USB 2.0 cable in a USB-C shell silently caps speed.
5. If the internal SSD benchmarks slow (CrystalDiskMark well below spec), see our [SSD troubleshooting guide](/articles/best-way-to-fix-ssd-slow-on-windows-11/) — the copy problem may be a drive problem.

## Closing

Slow file transfer is three problems wearing one name — USB, internal, or network — and each has a short, specific fix list. Measure first, identify your transfer type, then work the matching fixes: ports and drivers for USB, Robocopy and AV pauses for small files, SMB tuning for network. The copy dialog should be a brief progress bar, not a meditation exercise.
