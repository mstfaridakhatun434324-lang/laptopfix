---
title: "How to Fix Windows Update Stuck Downloading After a Windows 11 Update"
slug: how-to-fix-windows-update-stuck-downloading-after-windows-11-update
date: 2026-09-28
categories: ["windows-update"]
tags: ["stuck downloading", "windows update", "windows 11", "0 percent", "update stuck"]
description: "Windows Update stuck downloading at 0% or frozen mid-download after a Windows 11 update? Unstick it with these proven fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-after-windows-11-update.webp"
faqs:
  - q: "How long should I wait before deciding a download is stuck?"
    a: "Give it at least two hours on a normal broadband connection, and check whether the percentage moves at all during that time — slow progress is still progress. Large cumulative updates can legitimately take a long time. Only intervene when the percentage has been completely frozen for two hours and Task Manager shows no network activity on the update processes."
  - q: "Why does the download freeze at a specific percentage?"
    a: "Common freeze points correspond to specific phases: 0 percent usually means the download never started due to a service or connection problem, while freezes at high percentages often mean a corrupted chunk the downloader keeps retrying. Mid-range stalls frequently trace to the Background Intelligent Transfer Service hanging or a metered connection pausing the transfer."
  - q: "Will resetting the download lose progress?"
    a: "Clearing the update cache discards the partial download, so it starts over from zero. That sounds wasteful, but a corrupted partial download will never complete no matter how long you wait — the fresh download is the only way forward. The re-download typically completes faster than the time already wasted waiting on the stuck one."
  - q: "Can my antivirus cause downloads to stick?"
    a: "Yes. Real-time antivirus scanning of the growing download files in the SoftwareDistribution folder can stall the transfer, especially with large updates. VPNs cause similar stalls by interfering with the content delivery network. Temporarily disabling real-time protection or disconnecting the VPN during the download resolves a surprising number of stuck downloads."
---
After a Windows 11 update — often right after one cumulative update installed — the next update gets stuck downloading. The progress bar freezes at 0 percent, or climbs to some number like 47 percent and stops dead. Hours pass. Restarting the check does not help; the same update sits in the same place. The download is not slow — it is stuck.

This pattern, where one update succeeds and the next one jams, usually means the first update left the pipeline in a bad state: a hung transfer service, a corrupted cache, or a half-paused download that never resumed. The fixes below are ordered to unstick the download with the least disruption, starting with checks and ending with a full cache reset.

One important note about timing: the days right after Patch Tuesday are the worst for this. Microsoft's content delivery network is under maximum load, and a download that would normally complete in twenty minutes can crawl or stall. If your stuck download coincides with the second Tuesday of the month, some of what looks like a local failure is actually server-side congestion — the fixes below still help, but patience is part of the prescription too. First, confirm the stall is real: watch the percentage for 30 minutes and check Task Manager's Performance tab for network activity. A moving percentage, however slowly, means patience. A frozen one means action.

## Why this happens

- **The Background Intelligent Transfer Service hung.** BITS manages update downloads; when it stalls, the percentage freezes.
- **The previous update left a corrupted cache.** Partial or damaged files from the last update poison the next download.
- **A metered connection flag paused the transfer.** The flag may have been set by a hotspot session and forgotten.
- **Antivirus is scanning the in-progress download.** Real-time protection on the growing download files can stall the transfer.
- **VPN interference.** VPN tunnels can disrupt the content delivery network Windows Update uses.
- **Insufficient disk space.** The download needs room to land; a full drive stalls it silently.
- **Microsoft server congestion.** Patch Tuesday and the days after see heavy load, and downloads crawl or stall.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the metered flag and paused updates

Rule out the settings-level blocks first.

1. Go to **Settings > Network & internet > Wi-Fi**, click your network, and turn off **Metered connection** — or enable **Download updates over metered connections** under Windows Update's advanced options.
2. In **Settings > Windows Update**, check for a paused-updates notice and resume if present.
3. Click **Retry** on the stuck download.
4. Watch for 15 minutes. If the percentage moves, the block was settings-level and you are done.

### Fix 2: Restart the transfer services

Unstick the hung download machinery without losing the partial download.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`. Wait for both to confirm stopped.
3. Run `net start bits` and `net start wuauserv`.
4. Return to Windows Update and click **Retry**. Service stalls usually resume from near where they stopped.

### Fix 3: Remove antivirus and VPN interference

Eliminate the two most common external stall causes.

1. Disconnect from any VPN completely.
2. Temporarily disable third-party antivirus real-time protection, or exclude the C:\Windows\SoftwareDistribution folder from scanning.
3. Click **Retry** on the download.
4. Re-enable protection after the download completes. If this was the cause, consider a permanent exclusion for the update cache folder.

### Fix 4: Free up disk space

A download with nowhere to land stalls without an error message.

1. Check **Settings > System > Storage** for free space on C:.
2. Run **Disk Cleanup** with system files selected, removing **Windows Update Cleanup** and temporary files.
3. Ensure at least 10 GB free for cumulative updates, more for feature updates.
4. Retry the download with confirmed space.

### Fix 5: Clear the update cache

When the partial download is corrupted, only a fresh start works. This is the fix that resolves the most genuinely stuck downloads — the ones where the percentage has not moved in hours and the transfer services are otherwise healthy.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`. The old folders remain as a fallback until you delete them.
3. Restart the services with the matching `net start` commands.
4. Check for updates. The download restarts from zero — and this time from clean files. In practice the fresh download usually finishes faster than the time already lost waiting on the corrupted one.

### Fix 6: Run the Windows Update troubleshooter

Let the automated tool check what you might have missed.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its repairs.
3. Restart the laptop.
4. Retry the download. For the official manual reset procedure, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Download the update manually from the Catalog

Bypass the stuck pipeline for this specific update. The manual installer uses a completely separate download and install path, so whatever is jamming Windows Update does not affect it.

1. Find the update's KB number in **Settings > Windows Update > Update history**.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the package matching your system (x64 for most laptops).
3. Run the downloaded installer — it does not use the stuck download pipeline.
4. After the manual install succeeds, run Windows Update normally; the queue should now be clear, and future updates typically download without issue.

## Closing

A download stuck after a previous Windows 11 update is almost always a hung transfer service, a corrupted partial download, or a forgotten metered flag — all fixable without drama. Work from the quick service restart through the cache clear, and keep the manual catalog install as your bypass for the truly stubborn cases. If your downloads stall with a specific error code instead of just freezing, the [0x80070005 error guide](/articles/how-to-fix-windows-update-error-0x80070005-after-windows-11-update/) covers permission-related failures, and the [restarting-screen stuck guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) handles the case where the stall happens at reboot instead of download.
