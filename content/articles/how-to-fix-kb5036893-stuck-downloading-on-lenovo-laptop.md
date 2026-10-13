---
title: "KB5036893 Stuck Downloading on Lenovo Laptop? Unstick It"
slug: how-to-fix-kb5036893-stuck-downloading-on-lenovo-laptop
date: 2026-09-05
categories: ["windows-update"]
tags: ["kb5036893", "lenovo laptop", "stuck downloading", "windows update", "cumulative update"]
description: "KB5036893 stuck at downloading on your Lenovo laptop? Clear the stalled download, fix the Lenovo-specific snags, and install this update cleanly."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-on-lenovo-laptop.webp"
faqs:
  - q: "What is KB5036893?"
    a: "KB5036893 is a Windows cumulative update package. Like all cumulative updates, it bundles security fixes and quality improvements into a single large download. When it gets stuck downloading, the problem is almost always the download pipeline or a corrupt partial file, not the update's contents."
  - q: "Why do cumulative updates get stuck downloading on Lenovo laptops specifically?"
    a: "Lenovo's Vantage utility, aggressive battery-saver power plans, and network driver quirks can each stall the Background Intelligent Transfer Service that downloads updates. None of these are defects — but together they make stuck downloads more likely on Lenovo machines than on a clean Windows install."
  - q: "How long should a cumulative update take to download?"
    a: "On a decent broadband connection, the download phase typically takes 10–30 minutes for a cumulative update of this size. If the percentage has not moved for over an hour on a working connection — and especially if it sits at the same number after a pause-and-resume — the download is genuinely stuck rather than slow, and the fixes in this guide apply."
  - q: "Will I lose anything by clearing the update cache?"
    a: "No. Clearing the SoftwareDistribution cache only deletes downloaded update files and update metadata — the raw materials of updating, not anything of yours. Your personal files, applications, settings, and even your installed drivers are completely unaffected. Windows re-downloads whatever it needs on the next update check, usually within minutes."
---

KB5036893 is a cumulative update — a big, important package — and watching it sit at 0% or freeze mid-download on your Lenovo laptop is maddening. The update itself is almost certainly fine; what is stuck is the delivery mechanism. Lenovo laptops add a few specific wrinkles: Lenovo Vantage running its own update checks, power plans that throttle background downloads on battery, and network drivers that occasionally stall the transfer service. This guide unsticks the download with Lenovo's quirks accounted for.

Work on AC power with Vantage's automatic updates paused. The steps are ordered from quickest to most thorough, and most stuck downloads resolve in the first three.

Cumulative updates like KB5036893 deserve a little context, because their size explains their fragility. Unlike small security patches, a cumulative package bundles an entire month's fixes into one large download \u2014 hundreds of megabytes that must arrive intact and install as a unit. That size gives every weak link in the chain more time to fail: the network has more bytes to corrupt, BITS has a longer transfer to stall, and the disk has more data to stage. When a cumulative download sticks, it is rarely a comment on the update's quality \u2014 it is the logistics of moving big files on imperfect infrastructure.

## Why this happens

- **Stalled BITS transfer:** The Background Intelligent Transfer Service, which downloads updates, wedges on a bad network state and stops making progress without reporting an error.
- **Corrupt partial download:** An interrupted earlier attempt left a damaged partial file that the downloader keeps trying to resume instead of restarting.
- **Lenovo Vantage contention:** Vantage's own update and driver scans competing for bandwidth and file locks can stall Windows Update's download.
- **Battery-saver throttling:** Lenovo power plans on battery aggressively throttle background network activity, freezing downloads that would complete fine on AC power.
- **Metered connection limits:** If the connection is flagged metered, Windows restricts the download — the [metered connection guide](/articles/how-do-i-fix-metered-connection-blocking-windows-update/) covers this fully.
- **Network driver stall:** Outdated Lenovo network drivers can drop sustained large transfers while handling browsing fine, producing a download that starts and then dies.
- **VPN or proxy interference:** Corporate VPNs and proxies sometimes mangle or throttle the long-lived connections Windows Update uses.
- **Disk space shortage:** With insufficient free space, the download cannot stage the full package and stalls instead of failing cleanly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the stage — AC power, Vantage paused, connection stable

1. Plug in the AC adapter. Do not attempt this on battery.
2. Open Lenovo Vantage and pause automatic updates and Wi-Fi security scans temporarily.
3. Disconnect any VPN.
4. In Settings, Windows Update, click "Retry" next to the stuck KB5036893 and watch for 10 minutes. Many stalls clear once the throttling conditions are removed.

### Fix 2: Restart the download services

1. Press Win + R, type `services.msc`, press Enter.
2. Restart the Windows Update service and the Background Intelligent Transfer Service.
3. Return to Windows Update and check for updates. A service restart alone unblocks a surprising number of stuck downloads.

### Fix 3: Clear the SoftwareDistribution cache

This discards the corrupt partial download forcing the stall.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete everything inside C:\Windows\SoftwareDistribution.
4. Restart the services with `net start`, reboot, and check for updates to begin a completely fresh download.

### Fix 4: Update Lenovo network drivers

1. Open [Lenovo Support](https://support.lenovo.com/us/en/), enter your model, and download the latest Wi-Fi and Ethernet drivers.
2. Install them and restart.
3. Retry the download. Fresh network drivers fix the stall pattern where downloads start strong and die partway.

### Fix 5: Reset BITS and the network stack

1. In an elevated Command Prompt, run `bitsadmin /reset /allusers` to clear wedged transfer jobs.
2. Reset the network stack: `netsh winsock reset` and `netsh int ip reset`.
3. Restart the laptop and retry the update.

### Fix 6: Free disk space and check the drive

1. Ensure at least 20 GB free on the system drive — use Disk Cleanup (cleanmgr) targeting Windows Update Cleanup and Temporary files.
2. If the drive is healthy but full, the download stalls silently; space is the fix.
3. Run `chkdsk C: /f` if you suspect disk issues are corrupting the partial download.

### Fix 7: Install KB5036893 manually from the Update Catalog

When the automated download will not cooperate, bypass it.

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for KB5036893.
2. Download the package matching your system (x64 for most Lenovo laptops).
3. Close Vantage temporarily, run the installer, and restart when prompted.
4. Verify in Update history that KB5036893 shows as installed. The sibling guide for [KB5055523 stuck on Lenovo](/articles/how-to-fix-kb5055523-stuck-downloading-on-lenovo-laptop/) uses the same manual-install fallback.

### Fix 8: Try a fundamentally different network path

If the stall follows you across retries, the network path itself may be the problem.

1. Switch from Wi-Fi to Ethernet, or from your home connection to a phone hotspot \u2014 change the entire route, not just the signal strength.
2. If you use custom DNS, temporarily revert to your ISP's defaults (or vice versa) \u2014 DNS issues can break the content-delivery endpoints Windows Update uses.
3. Restart your router; stale NAT sessions are a classic cause of stalled long-lived transfers.
4. Retry the download on the new path. If it completes, the laptop was never the problem \u2014 your network route was.

## Closing

A stuck KB5036893 download on a Lenovo laptop is a delivery problem, not an update problem \u2014 and delivery problems yield to service restarts, cache clears, fresh network drivers, and when needed, a completely different network path. The manual catalog install remains your guaranteed exit: it sidesteps the entire download pipeline in one move. Once the update is in, re-enable Vantage's automatic checks, let the two updaters take turns instead of fighting, and remember that cumulative updates are worth the trouble \u2014 they carry the month's security fixes.
