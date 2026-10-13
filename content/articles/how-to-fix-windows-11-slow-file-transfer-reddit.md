---
title: "Slow File Transfers on Windows 11? Top Community Fixes"
slug: how-to-fix-windows-11-slow-file-transfer-reddit
date: 2026-10-10
categories: ["performance"]
tags: ["slow file transfer", "usb", "file copy", "windows 11"]
description: "File copies crawling on Windows 11? Fix slow USB transfers, network copy bottlenecks, and the settings that throttle your transfer speeds."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-file-transfer-reddit.webp"
faqs:
  - q: "What is a normal USB file transfer speed on Windows 11?"
    a: "Rough real-world expectations: USB 2.0 tops out around 30-40 MB/s, USB 3.0/3.1 Gen 1 around 300-400 MB/s, USB 3.1 Gen 2 around 800-1000 MB/s, and USB4/Thunderbolt higher still — but the drive itself is usually the limit, not the port. A spinning external HDD rarely exceeds 120 MB/s; a SATA SSD about 500 MB/s. If you're far below the slowest component's capability, something is throttling."
  - q: "Why do transfers start fast then slow to a crawl?"
    a: "That's the write cache filling up. Windows (and the drive) buffer the first chunk of data at high speed, then the sustained speed drops to what the drive can actually write continuously — especially dramatic on cheap flash drives and QLC SSDs whose SLC cache exhausts after a few GB. It's normal physics, not a bug. Truly abnormal is starting slow and staying slow, or speeds in the KB/s range."
  - q: "Does antivirus slow down file transfers?"
    a: "Yes, measurably — real-time antivirus scans files as they're written, and on large transfers (thousands of files) the per-file scan overhead dominates. Copying 50GB of small files with aggressive real-time scanning can take several times longer. For trusted bulk copies, temporarily pausing real-time protection (re-enable immediately after) or excluding the destination folder during the copy are legitimate speedups."
  - q: "Why are network file transfers so much slower than the Wi-Fi speed?"
    a: "Wi-Fi link speed is a theoretical ceiling you'll never reach — protocol overhead, SMB version negotiation, the NAS/destination drive's write speed, and Windows' network throttling all take their cut. A '1200 Mbps' Wi-Fi connection realistically moves files at 40-70 MB/s to a good NAS. If you're getting single-digit MB/s, suspect SMB1 fallback, a 100 Mbps wired bottleneck, or antivirus scanning network writes."
---

Copying files should be limited by your hardware — the drive, the port, the network — not by Windows getting in the way. But slow transfers on Windows 11 are a perennial complaint: USB copies crawling at USB 2.0 speeds on USB 3 ports, network copies a fraction of the Wi-Fi rate, transfers that start fast and die. The causes split neatly into port/drive issues, Windows settings (caching policies, throttling), and software interference (antivirus, filters). Here's how to work through them. For disk-health fundamentals that underlie transfer speed, see [checking disks for errors](/articles/how-to-check-disk-for-errors-in-windows-11-24h2/); for general system slowness, the [speed-up checklist](/articles/laptop-running-slow-windows-11-how-to-speed-up/) applies.

## Why this happens

- **Wrong USB port or cable**: USB 3 drive in a USB 2 port (or with a charge-only cable) caps speed silently.
- **Write-caching policy**: "Quick removal" default disables write caching, hurting large transfers.
- **Antivirus real-time scanning**: Per-file scan overhead dominating multi-thousand-file copies.
- **Drive itself is the bottleneck**: Cheap flash drives and QLC SSDs collapse after cache exhaustion.
- **SMB/network misconfiguration**: Old SMB versions, 100Mbps links, or Wi-Fi issues on network copies.
- **Failing drive retrying**: Bad sectors turning reads/writes into retry storms.
- **Background disk competition**: Indexer, antivirus scans, or updates saturating the same disk mid-copy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure properly and identify the bottleneck

Numbers first — "slow" is relative.

1. Note the actual speed: Windows' copy dialog shows MB/s — record the **sustained** speed (after the first 10 seconds), not the initial burst.
2. Identify every component's ceiling: the **port** (USB 2/3/3.1 — check for blue inserts/SS markings), the **drive's rated speed**, and for network, the **link speed** (Settings > Network > adapter properties).
3. Your real-world speed should be near the **slowest** component's rating. USB 3 flash drive rated 400 MB/s copying at 35 MB/s = something's wrong; copying at 250 MB/s = normal overhead.
4. Test with a single large file vs. many small files: huge gaps (fast large file, crawling small files) point to per-file overhead (antivirus, filesystem) rather than raw throughput.
5. Try a different port, cable, and (if possible) a different drive — isolating whether the bottleneck follows the port, the cable, or the drive.

### Fix 2: Fix USB port, cable, and driver issues

The most common "mystery slowdown" — silently running at USB 2.0.

1. Plug into a **USB 3 port** (blue insert, "SS" marking, or USB-C) — Windows won't warn you when a USB 3 drive negotiates USB 2.0 speeds in a USB 2 port.
2. Use a **data-rated cable** — cheap charge-only or damaged USB-C cables silently fall back to USB 2.0 speeds; swap cables as a test.
3. In **Device Manager** > **Universal Serial Bus controllers**, check for warning icons; update the **USB 3.0/3.1 eXtensible Host Controller** driver from your laptop maker or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Avoid USB hubs for speed tests — plug directly into the laptop; hubs (especially unpowered ones) bottleneck and cause renegotiation.
5. For USB-C/Thunderbolt docks, confirm the dock's firmware is current — dock firmware bugs are a real cause of capped transfer speeds.

### Fix 3: Enable write caching (Better performance policy)

The classic Windows transfer-speed toggle.

1. Open **Device Manager** > **Disk drives** > right-click your external drive > **Properties** > **Policies** tab.
2. Switch from **Quick removal** (default; write caching off) to **Better performance** (write caching on) > OK.
3. Consequence: with Better performance, you **must** use **Safely Remove Hardware** before unplugging — pulling the drive mid-write risks corruption. That's the tradeoff for the speed.
4. For internal drives this policy is already optimal; this fix matters for **external** drives, where Quick removal is the default.
5. Re-test the same copy: large sequential transfers typically gain 20–50% from caching; small-file copies gain less (they're overhead-bound, not cache-bound).

### Fix 4: Reduce antivirus and software interference

Per-file overhead is the silent killer of big copies.

1. For a trusted bulk copy, temporarily **pause real-time protection** (Windows Security > Virus & threat protection > Manage settings), run the copy, then **re-enable immediately**. Time both to quantify the AV tax.
2. Alternatively, add the **destination folder** as an exclusion during the copy, then remove the exclusion afterward — safer than a global pause.
3. Close background disk hogs during the copy: pause cloud sync (OneDrive/Dropbox), pause the search indexer heavy lifting, and don't run Windows Update mid-transfer.
4. Disable **Remote Differential Compression** for network copies (Control Panel > Programs > Turn Windows features on/off > uncheck it) — on fast LANs its CPU cost exceeds its bandwidth savings.
5. If you use third-party copy tools (TeraCopy, FastCopy), test against plain Explorer — occasionally the tool, not Windows, is the bottleneck.

### Fix 5: Fix network transfer bottlenecks

For slow copies to/from NAS and network shares.

1. Check the actual link speed: **Settings** > **Network & internet** > adapter > **Link speed** — a 100 Mbps (not 1000) reading means a bad cable, port, or switch negotiation; fix the physical layer first.
2. On Wi-Fi, move closer to the router and prefer **5/6 GHz** bands — then compare against a wired test to separate Wi-Fi issues from protocol issues.
3. Ensure **SMB2/3** is in use, not SMB1: in elevated PowerShell, `Get-SmbConnection` shows the dialect per connection — SMB1 is slow and insecure; disable it (Windows Features) and let SMB3 negotiate.
4. On the NAS/server side, check its drive health and network mode — a NAS with a failing drive or half-duplex link caps everything regardless of your laptop.
5. For large single files, try mapping the share vs. UNC path, and disable **"Large Send Offload"** quirks only as a diagnostic — NIC driver updates from the maker usually fix offload bugs properly. The [Update Catalog](https://www.catalog.update.microsoft.com/) carries NIC driver updates when Windows Update doesn't offer them.

### Fix 6: Check drive health and filesystem

When the drive itself is dying or misformatted.

1. Run `chkdsk X: /scan` (replace X:) on the external drive — file-system errors cause retry storms that look like slowness.
2. Check S.M.A.R.T. data for reallocated/pending sectors — a drive with growing bad sectors gets progressively slower as it remaps; back it up and replace it.
3. Check the filesystem: **exFAT** is the cross-platform default but slower than **NTFS** on Windows for many small files; if the drive is Windows-only, NTFS usually transfers faster (back up data before reformatting).
4. For SSDs (internal or external), confirm **TRIM** is active (`fsutil behavior query DisableDeleteNotify` should return 0) and the SSD firmware is current — degraded SSDs without TRIM slow dramatically.
5. Monitor **Task Manager** > **Performance** > disk **Active time** vs. **Response time** during the copy: 100% active with high response times = the disk is saturated (hardware limit); low active time with slow copy = something upstream throttling. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the removal-policy tradeoffs officially.

## Closing

Slow file transfers are a weakest-link problem: the port, the cable, the drive, the antivirus, or the network — one of them is the bottleneck, and the copy dialog's MB/s tells you which performance tier you're actually in. Fix the physical layer first, enable write caching on externals, quiet the antivirus for trusted copies, and get SMB modern on network copies.
