---
title: "KB5036893 Stuck Downloading on Windows 11? Unstick It Now"
slug: how-to-fix-kb5036893-stuck-downloading-on-windows-11
date: 2026-10-11
categories: ["windows-update"]
tags: ["kb5036893", "stuck downloading", "windows 11", "windows update"]
description: "Fix KB5036893 stuck downloading on Windows 11: clear the stalled queue, fix Delivery Optimization, and get the update downloaded and installed."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-on-windows-11.webp"
faqs:
  - q: "How long should a Windows 11 update take to download?"
    a: "On a decent broadband connection, a cumulative update of a few hundred megabytes should download in minutes, not hours. If the percentage has not moved in over an hour on a working connection, the download is stuck, not slow — treat it as a failure and reset the queue."
  - q: "Does Delivery Optimization cause stuck downloads?"
    a: "It can, and on some networks it is the primary suspect. Delivery Optimization's peer-to-peer sharing sometimes stalls on restrictive networks, misconfigured caches, or bad peers. Turning peer-to-peer downloading off and pulling the update straight from Microsoft's servers often unsticks a frozen percentage immediately."
  - q: "Will resetting the update cache delete my installed updates?"
    a: "No, and this is a common worry. Renaming the SoftwareDistribution folder only clears pending downloads, the download queue, and the update history view — your installed updates stay installed and your system stays patched. Windows rebuilds the folder fresh on the next update check, which is exactly the clean slate a stuck download needs."
  - q: "Why does the download restart from 0% after I fix it?"
    a: "Because the partial download was corrupt or incomplete, Windows discards it and starts clean. That is the correct behavior — a fresh, verified download is what you want. The percentage will move steadily this time if the underlying problem is fixed."
---

Watching KB5036893 sit at 7% — or 42%, or 99% — for hours is a special kind of torment. The download is not slow; it is stuck. Something in the download pipeline has wedged: a corrupted cache entry, a stalled background service, or a network path that silently drops the connection.

Unsticking it is mechanical work. You clear the wedged state, give Windows a clean download path, and verify the network is not the culprit. Work the steps in order and the percentage will start moving again.

Before you begin, plug in the charger and make sure you have at least 10 GB free on C:. Update downloads stall silently on nearly full drives, and you do not want to chase a network ghost when the real problem is storage. Note the exact percentage where it sticks — that detail helps if you need support later.

## Why this happens

- **Corrupted partial download:** An interrupted chunk sits in the cache and the downloader keeps retrying the same bad chunk forever.
- **Stalled BITS queue:** The Background Intelligent Transfer Service job behind the download can wedge and never report progress.
- **Delivery Optimization peer issues:** Peer-to-peer sources on your LAN or the internet can stall or feed corrupt data.
- **DNS or proxy problems:** Misconfigured DNS or a corporate proxy silently breaks the CDN connections Windows Update uses.
- **Metered connection limits:** A connection flagged as metered pauses or throttles the download without a clear message.
- **Antivirus download scanning:** Real-time scanning of the incoming package can serialize the download to a crawl or block it outright.
- **Disk space pressure:** With little free space, the downloader cannot stage the file and stalls instead of erroring clearly.
- **Corrupted update database:** The local DataStore database that tracks download state can corrupt, freezing progress reporting. The same database issue underlies many [generic stuck-download cases](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is stuck, not slow

1. Note the exact percentage and the time, then wait **30 minutes** without using the network heavily.
2. Open **Task Manager → Performance → Wi-Fi/Ethernet** and watch for actual download traffic.
3. If the percentage has not moved and there is no meaningful traffic, it is stuck — proceed.
4. If traffic is flowing steadily, it is just slow: leave it alone and check back in an hour.

### Fix 2: Pause, wait, and resume the update

1. In **Settings → Windows Update**, click **Pause updates** for one week.
2. Wait two full minutes, then click **Resume updates** and **Check for updates**.
3. This tears down the stalled BITS job and starts a fresh one — the simplest unstick there is.
4. If the percentage freezes at the same spot again, the cache itself is corrupt; continue.

### Fix 3: Turn off Delivery Optimization peer-to-peer

1. Go to **Settings → Windows Update → Advanced options → Delivery Optimization**.
2. Turn off **Allow downloads from other PCs**, or set it to **Devices on my local network** only.
3. Clear the Delivery Optimization cache from **Settings → System → Storage → Temporary files** if the option appears.
4. Retry the download — pulling straight from Microsoft's servers eliminates an entire class of stalls.

### Fix 4: Reset the Windows Update download cache

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`.
2. Delete everything in `C:\Windows\SoftwareDistribution\Download` (leave the folder itself).
3. Restart both services and check for updates.
4. The download restarts from 0% with clean state — this resolves the majority of stuck downloads.

### Fix 5: Check the connection: metered, DNS, and proxy

1. In **Settings → Network & internet → Wi-Fi**, open your network and turn **Metered connection** off.
2. Set DNS to a reliable public resolver (your router's admin page or Windows adapter settings) if pages load oddly.
3. In **Settings → Network & internet → Proxy**, make sure no unwanted proxy is configured.
4. Run a speed test — if the whole connection is broken, fix the network first; no update setting overcomes that.

### Fix 6: Reset the network stack

1. In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`.
2. Run `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns`.
3. Reboot the laptop and reconnect to the network.
4. A clean network stack clears the subtle socket-level stalls that pause/resume cannot. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these commands for connectivity troubleshooting.

### Fix 7: Temporarily disable download-scanning security software

1. Temporarily disable any third-party antivirus real-time protection.
2. Retry the download with only Windows Security active.
3. If the percentage moves now, add an exclusion for `C:\Windows\SoftwareDistribution` in your antivirus before re-enabling it.
4. Do not leave protection off longer than the test requires.

### Fix 8: Download KB5036893 manually from the catalog

1. Find KB5036893 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the x64 .msu.
2. Your browser's downloader replaces the stuck Windows Update pipeline entirely.
3. Install the package by double-clicking it, then reboot.
4. Verify in Update history. If even the manual download stalls, the problem is your network or ISP — try a different network to confirm. Windows 10 users with the same symptom should follow the [Windows 10 stuck-download guide](/articles/how-to-fix-kb5036893-stuck-downloading-on-windows-10/) for OS-specific steps.

## Closing

A stuck KB5036893 download on Windows 11 is a wedged pipeline, not a broken update: a corrupt cache chunk, a stalled BITS job, or a network quirk. Pause and resume, disable peer-to-peer, clear the download cache, and reset the network stack. If Windows Update still will not move, the manual catalog install finishes the job in minutes.

To keep downloads healthy going forward, leave Delivery Optimization's peer sharing off on unreliable networks, keep 15 GB or more free on the system drive, and avoid pausing updates for months at a time — long pauses create the giant catch-up downloads most likely to stall.
