---
title: "How to Troubleshoot Slow File Transfer in Windows 11"
slug: troubleshoot-windows-11-slow-file-transfer
date: 2026-09-17
categories: ["performance"]
tags: ["slow file transfer", "windows 11", "usb speed", "troubleshooting", "file copy"]
description: "Diagnose and fix slow file transfers in Windows 11, from USB bottlenecks and write-caching settings to antivirus scanning and dying drives."
thumbnail: "/images/thumbs/troubleshoot-windows-11-slow-file-transfer.webp"
faqs:
  - q: "What is a normal file transfer speed for a USB drive on Windows 11?"
    a: "A USB 3.0/3.1 flash drive on a healthy port typically sustains 80-150 MB/s reading and 30-100 MB/s writing, depending on the drive. USB 2.0 ports top out around 30 MB/s in practice. If you're seeing single-digit MB/s on a USB 3.0 drive in a blue port, something is wrong — driver, cable, port, or the drive itself is degrading."
  - q: "Does antivirus software really slow down file copies?"
    a: "Yes, measurably. Real-time antivirus inspects every file as it's written, which adds overhead — especially with thousands of small files like photos or source code. A copy that takes 3 minutes unprotected can take 8-10 minutes under heavy scanning. Large single files see less impact. If disabling protection temporarily restores speed, your scanner was the bottleneck, and exclusions are the permanent answer."
  - q: "Should write caching be on or off for external drives?"
    a: "On for internal drives always; for external drives it's a tradeoff. Enabling write caching boosts sequential write speed noticeably but risks data loss if you unplug without ejecting. Use 'Better performance' for a drive that stays connected at a desk, and 'Quick removal' for drives you yank out constantly. The setting lives in the drive's Policies tab in Device Manager."
  - q: "Why does the copy speed start fast then drop to almost nothing?"
    a: "That burst-then-crawl pattern is Windows filling the file cache and then waiting on the actual storage. It happens with USB drives, drives that are nearly full, drives with bad sectors, and some external hard drives that overheat under sustained load. Consistent speeds near zero for minutes at a time usually point at a failing drive or a bad cable rather than a settings issue."
---

Copying a file should be the most boring thing your laptop does. When a transfer that should take two minutes is still crawling after twenty, something specific is throttling it — and it's almost never "Windows is just slow." File transfers move through a chain: the source drive, the system cache, the CPU's I/O handling, the destination drive, and the cable or network in between. A bottleneck at any point shows up as the same symptom: a progress bar moving like molasses.

The good news is that each link in that chain is testable. By isolating variables — same files, different drive; same drive, different port; same port, different cable — you can usually find the culprit in under an hour. This guide walks through that isolation process, then applies the right fix for what you find.

## Why this happens

- **USB port mismatch:** A USB 3.0 drive plugged into a USB 2.0 port (or a broken SuperSpeed lane) silently falls back to ~30 MB/s with no warning.
- **Bad or low-quality cables:** Long, cheap, or damaged USB cables fail to negotiate high-speed modes and retransmit constantly.
- **Real-time antivirus scanning:** Every written file gets inspected, which punishes copies of many small files disproportionately.
- **Write caching disabled:** External drives default to "Quick removal," which skips the cache and writes at the device's raw speed.
- **Nearly full destination drive:** Drives above 90% full slow dramatically as the controller hunts for free blocks.
- **Failing storage:** Drives with bad sectors retry reads/writes repeatedly, producing bursts followed by long stalls.
- **Fragmented or SMR external drives:** Shingled magnetic recording drives collapse to a few MB/s once their small write cache fills.
- **Network transfers throttled elsewhere:** Wi-Fi congestion, old SMB versions, or a router with QoS rules limiting the link.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish a baseline before changing anything

Copy the same test file (something over 1 GB) to the same destination and record the speed shown in the copy dialog. Repeat it once to confirm consistency. Then change exactly one variable: try a different USB port. If speed jumps, the first port is the problem — possibly a failed USB 3.0 controller lane or a loose motherboard connection. This single test rules out half the causes.

1. Copy a 1+ GB file to the target drive; note the MB/s.
2. Repeat to confirm the number is consistent.
3. Try a different USB port — prefer a rear/blue port over a front/hub port.
4. If speed changes, the port (not Windows) is your problem.

### Fix 2: Rule out the cable and the drive

Swap the cable for the shortest quality cable you have, and test the drive on another computer if possible. USB-C hubs and dock passthrough ports are notorious for capping speeds, so plug directly into the laptop when diagnosing. If the drive is slow everywhere, the drive is the problem — back up its data now, because slow reads plus stalls are a classic early failure signature.

1. Replace the cable with a known-good one; re-test.
2. Bypass hubs and docks — connect directly to the laptop.
3. Test the same drive on a second computer.
4. Slow everywhere means the drive is dying; back it up immediately.

### Fix 3: Verify write caching and drive policies

Open Device Manager, expand Disk drives, right-click the target drive, open Properties, and check the Policies tab. For external drives that stay put, choose **Better performance** to enable write caching; for drives you constantly unplug, **Quick removal** is safer but slower. Internal drives should always run with caching enabled — if it's off, that alone explains poor speeds. This setting applies per device, so check each slow drive individually.

1. Open Device Manager and expand **Disk drives**.
2. Right-click the slow drive → **Properties → Policies**.
3. Select **Better performance** (and enable write caching) for desk-bound drives.
4. Click OK, then safely eject and reconnect the drive to apply the change.

### Fix 4: Tame real-time antivirus scanning

Copy a large folder while watching Defender's CPU in Task Manager. If MsMpEng.exe is burning CPU during the copy, the scanner is your bottleneck. The fix isn't disabling protection permanently — it's adding exclusions for the folders you copy to and from regularly (backup targets, video scratch folders, project directories). If your [Windows Defender high CPU usage](/articles/how-to-fix-windows-defender-high-cpu-usage/) persists beyond copies, that guide covers exclusions and scheduling in depth.

1. Start a copy and watch MsMpEng.exe CPU in Task Manager.
2. If it spikes, open **Windows Security → Virus & threat protection → Manage settings → Exclusions**.
3. Add folder exclusions for your regular copy sources and destinations.
4. Re-test the same copy; speed should recover without turning protection off.

### Fix 5: Check disk health and free space

Keep the destination under 85% full; SSDs in particular lose write speed badly past 90%. Then check drive health: in an elevated Command Prompt run `wmic diskdrive get status` for a quick SMART verdict, and `chkdsk X: /f` on the target volume to repair filesystem errors. If CrystalDiskInfo or SMART shows reallocated sectors climbing, the drive is failing regardless of settings — no software fix survives a dying drive. The [disk active time at 100 percent](/articles/what-to-do-if-disk-active-time-100-percent/) guide helps when the system drive itself is the bottleneck.

1. Free space on the destination so it's below 85% full.
2. In an elevated Command Prompt, run `wmic diskdrive get status` to check SMART health.
3. Run `chkdsk X: /f` (replace X with the drive letter) to repair filesystem errors.
4. If bad sectors are found, replace the drive rather than fighting it.

### Fix 6: Fix USB driver and controller issues

Outdated or corrupted USB controller drivers silently drop ports to slower modes. In Device Manager, expand **Universal Serial Bus controllers**, right-click each USB Root Hub and host controller, and choose **Update driver → Search automatically**. For deeper repair, uninstall the host controller entries and restart — Windows reinstalls them fresh. Chipset drivers from your laptop maker matter too: get them from [Dell](https://www.dell.com/support) — or the HP or Lenovo support site for those brands — rather than relying on Windows Update alone.

1. In Device Manager, expand **Universal Serial Bus controllers**.
2. Update drivers on every USB Root Hub and host controller.
3. If no change, uninstall host controller entries and restart the laptop.
4. Install the latest chipset driver package from your laptop manufacturer's support site.

### Fix 7: Address network-transfer bottlenecks separately

For slow copies over the network, test with a wired connection — Wi-Fi link speeds collapse under interference and distance. Map the share and check whether the bottleneck is bandwidth or latency by comparing one big file against many small files (small files expose protocol overhead). On both ends, make sure SMB signing isn't forced on when it isn't needed, and check your router for QoS rules that cap a device. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents SMB and file sharing settings if you need the exact paths.

1. Test the same copy over a wired Ethernet connection.
2. Compare one large file vs. many small files to separate bandwidth from protocol overhead.
3. Check router QoS rules for device speed limits.
4. Update the network adapter driver from the manufacturer's site.

## Closing

Slow file transfers are a diagnosis problem, not a settings problem: baseline the speed, isolate port, cable, drive, caching, antivirus, and drivers one at a time, and the bottleneck reveals itself. Most cases resolve at Fix 2 or Fix 4 — a bad cable or an overzealous scanner. When none of the fixes move the needle, believe the data: the drive is failing, and your priority shifts from speed to backup.
