---
title: "Troubleshoot Slow File Transfer on Windows 11"
slug: "windows-11-slow-file-transfer-troubleshooting"
date: 2026-09-18
categories: ["performance"]
tags: ["slow file transfer", "usb", "windows 11", "copy speed", "troubleshooting"]
description: "File copies crawling at a few MB/s on Windows 11? Diagnose whether the bottleneck is the USB port, the drive, the network, or Windows itself."
thumbnail: "/images/thumbs/windows-11-slow-file-transfer-troubleshooting.webp"
faqs:
  - q: "What is a normal USB file transfer speed on Windows 11?"
    a: "It depends on the USB generation. USB 2.0 tops out near 35 MB/s in practice, USB 3.x Gen 1 reaches roughly 300 to 400 MB/s with a fast drive, and Gen 2 can exceed 800 MB/s. If your USB 3 drive copies at USB 2.0 speeds, you are almost certainly on a USB 2.0 port or cable. Matching drive, port, and cable generation is the first thing to verify."
  - q: "Why does the transfer speed drop halfway through a large copy?"
    a: "Most consumer flash drives and external SSDs have a fast SLC cache that fills up after a few gigabytes of sustained writing, after which speeds fall to the drive's much slower native write rate — sometimes under 50 MB/s. This is hardware behavior, not a Windows bug, and no setting changes it. The speed graph in the copy dialog dipping mid-transfer is the classic signature of cache exhaustion."
  - q: "Does antivirus slow down file transfers?"
    a: "Yes, measurably. Real-time protection scans files as they are written, which adds overhead to every file — the effect is worst with thousands of small files rather than a few large ones. Temporarily pausing real-time protection during a big trusted copy is a legitimate diagnostic step. If speeds jump dramatically, add an exclusion for the destination folder or schedule large copies outside active scanning hours."
  - q: "Can Windows settings actually speed up file copies?"
    a: "A few can. Disabling Remote Differential Compression removes per-file comparison overhead, switching a removable drive's removal policy to Better performance enables write caching, and updating the USB controller driver fixes negotiation bugs that strand ports at USB 2.0 speeds. No setting will make a slow drive fast, though — settings only remove bottlenecks that should not be there in the first place."
---
You plug in a USB 3 drive, drag a 20 GB folder across, and watch the speed graph crawl at 8 MB/s. The math says it should take a minute; Windows says forty. Slow file transfer on Windows 11 is maddening precisely because the bottleneck could be anywhere: the port, the cable, the drive, the network, your antivirus, or a Windows setting quietly throttling everything.

The mistake most people make is changing settings at random. A technician diagnoses first: is the link negotiating at the right speed? Is the drive itself slow, or is something in Windows interfering? Each answer points to a different fix, and the tests take minutes.

This guide follows that diagnostic order — hardware link first, then the drive, then network transfers, then Windows settings — so you fix the actual bottleneck instead of all of them. If the whole system feels sluggish rather than just copies, start with our [Windows 11 speed-up guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) instead.

## Why this happens

- **Wrong USB port or cable:** a USB 3 drive in a USB 2.0 port (or on a USB 2.0 cable) is capped at roughly 35 MB/s no matter what Windows does.

- **Drive cache exhaustion:** flash drives slow dramatically after their fast SLC cache fills, which is normal hardware behavior.

- **Thousands of small files:** per-file overhead — creating entries, scanning, indexing — makes 10,000 small files copy far slower than one big file of the same size.

- **Real-time antivirus scanning:** every written file gets scanned, adding latency that compounds across large copies.

- **Remote Differential Compression:** this Windows feature compares file chunks during copies and adds CPU overhead, especially on network transfers.

- **Outdated USB controller drivers:** buggy drivers can fail to negotiate USB 3 speeds, silently stranding ports at USB 2.0.

- **Failing drive with reallocated sectors:** a dying drive retries reads and writes, producing erratic, collapsing transfer speeds.

- **Network bottleneck for shared folders:** Wi-Fi congestion, 100 Mbps Ethernet, or an overloaded NAS caps network copies regardless of PC speed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the USB link speed first

Most “slow USB” complaints are a link problem, not a Windows problem. USB ports on laptops are often a mix of 2.0 and 3.x, and they are not always labeled clearly. Confirm what speed the connection actually negotiated before touching any setting.

1. Plug the drive into each USB port on the laptop in turn and note which color the port interior is — blue or teal usually means USB 3.x.
2. Open Device Manager, expand Universal Serial Bus controllers, and confirm you see USB 3.x eXtensible Host Controller entries.
3. Copy a single 1 GB test file and watch the speed; a USB 3 drive on a USB 3 port should well exceed 60 MB/s.
4. Try a different cable — many bundled cables are USB 2.0 despite fitting the same connector.
5. If one port is fast and another is slow, you have found your answer: use the fast port and stop troubleshooting.

### Fix 2: Test the drive itself in isolation

If every port is slow, the drive may simply be slow — or failing. A quick benchmark separates a healthy-but-modest drive from one that needs replacing, and Microsoft's guidance on drive maintenance lives on its [Windows support site](https://support.microsoft.com/en-us/windows).

1. Download a free benchmark tool such as CrystalDiskMark and run a 1 GB sequential test on the external drive.
2. Compare the result to the drive's advertised speeds; under half the rating on a USB 3 link suggests a problem.
3. Check the drive's SMART health with CrystalDiskInfo — any Caution or Bad status means replace, not tweak.
4. For internal-drive slowness, run chkdsk C: /scan from an elevated Command Prompt.
5. If the drive is healthy but slow after its cache fills, that is inherent to the hardware — split huge copies into smaller batches.

### Fix 3: Disable Remote Differential Compression

Remote Differential Compression (RDC) is a Windows feature that computes file differences during transfers. It was designed for slow WAN links and mostly adds CPU overhead on modern fast connections. Disabling it is safe and reversible.

1. Open Control Panel and go to Programs > Turn Windows features on or off.
2. Scroll down and uncheck Remote Differential Compression API Support.
3. Click OK and let Windows apply the change, then restart if prompted.
4. Re-run your typical copy and compare speeds — network transfers benefit most.
5. If there is no change, you can re-enable it; it was not your bottleneck.

### Fix 4: Enable write caching on the external drive

Windows defaults removable drives to quick removal, which disables write caching to protect against unplugged-drive corruption. Switching to Better performance enables the cache and can noticeably lift sustained write speeds — at the cost of needing to eject safely.

1. Open Device Manager and expand Disk drives.
2. Right-click your external drive, choose Properties, and open the Policies tab.
3. Select Better performance and ensure Enable write caching on the device is checked.
4. Click OK; from now on, always use Safely Remove Hardware before unplugging this drive.
5. Re-test a large copy to measure the improvement.

### Fix 5: Rule out antivirus and indexing interference

Real-time protection and the search indexer both inspect files as they land, and their overhead multiplies across thousands of files. A quick A/B test tells you in minutes whether they are your bottleneck.

1. Copy a representative folder and note the speed with everything running normally.
2. Temporarily turn off real-time protection in Windows Security > Virus & threat protection > Manage settings.
3. Repeat the same copy immediately — a large jump implicates the scanner.
4. Turn real-time protection back on right away, then add a permanent exclusion for the destination folder instead.
5. If you copy to indexed locations constantly, narrow the index scope as described in our [high disk usage guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-step-by-step/).

### Fix 6: Update USB and chipset drivers

Driver bugs that misnegotiate link speeds are more common than people expect, especially after Windows feature updates. Fresh chipset and USB controller drivers from the laptop vendor fix a surprising number of “my USB 3 port acts like USB 2” cases.

1. Identify your laptop's exact model and download the latest chipset and USB drivers from the vendor's support site.
2. Install the chipset driver first, then any USB 3.x controller driver, restarting between them if asked.
3. In Device Manager, check the USB Root Hub properties > Advanced to confirm negotiated speeds afterward.
4. Avoid generic driver-updater utilities — vendor or Windows Update drivers are safer and sufficient.
5. Re-test with your 1 GB file to confirm the link now runs at full speed.

### Fix 7: Diagnose network transfers separately

Copies to a NAS or shared folder follow different rules: the network itself is usually the limit. Chasing USB settings will not fix a Wi-Fi bottleneck, so test the network path on its own terms.

1. If on Wi-Fi, move the laptop closer to the router and re-test — a big jump means congestion or weak signal.
2. Prefer a wired Ethernet connection for multi-gigabyte transfers; even 100 Mbps Ethernet caps you at about 12 MB/s.
3. Check whether the NAS or target PC is itself busy — its disk or CPU can be the limit, not yours.
4. Try copying with the laptop as the only active device on the network to rule out congestion.
5. For persistently slow LAN copies, test with a large single file: if that is fast but folders are slow, per-file overhead (and antivirus) is the cause.

## Closing

Slow file transfers are a bottleneck problem, and bottlenecks are found by testing, not guessing. Check the USB link speed, benchmark the drive, isolate network copies, then tune Windows settings like RDC and write caching. Worked in that order, you will either find a fixable setting or learn — honestly — that the drive itself is the limit, which is still a useful answer.
