---
title: "How to Fix Windows Update Stuck on Downloading on a Lenovo Laptop"
slug: how-to-fix-windows-update-stuck-downloading-on-lenovo-laptop
date: 2026-09-08
categories: ["windows-update"]
tags: ["windows update stuck downloading", "lenovo windows update download", "bits stuck fix", "delivery optimization slow"]
description: "Windows Update download frozen on your Lenovo laptop? Restart BITS, reset the download cache, check for metered connections, and get the bytes flowing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-lenovo-laptop.webp"
faqs:
  - q: "How can I tell if the download is stuck or just slow?"
    a: "Watch Task Manager's network graph and the exact percentage. If data is flowing or the percentage creeps up over 20 minutes, it is slow — leave it. If zero bytes move for 30+ minutes and the percentage is frozen, it is stuck. Large 24H2-era updates on slow connections can legitimately take hours."
  - q: "Why does the download restart from 0% after I clear the cache?"
    a: "Because you deleted the partial download along with the corruption. Starting clean is the point — the old partial data contained the damaged chunks that were breaking resume. A fresh download of intact chunks finishes faster than a corrupted one retrying forever."
  - q: "Can Lenovo Vantage really interfere with Windows Update?"
    a: "Yes, through bandwidth contention and occasional servicing locks. Both use BITS for transfers, and on slow connections Vantage's driver downloads can starve Windows Update. Pausing Vantage while Windows Update runs is a harmless test that resolves a real category of stalls."
  - q: "Should I disable Delivery Optimization permanently?"
    a: "Not necessarily. Peer sharing helps on fast networks, but when it malfunctions it causes exactly this symptom. Turning it off is a diagnostic step — if downloads suddenly work, you found the cause. You can re-enable it later or leave it off; direct Microsoft downloads are perfectly fine."
---

Windows Update stuck on 'Downloading' with a frozen percentage on your Lenovo laptop is usually a delivery problem, not an install problem — the bits are not arriving, so there is nothing to install yet. The download pipeline involves BITS, Delivery Optimization, your network, and Microsoft's servers, and a stall in any one of them freezes the counter. [Windows Update stuck downloading after an update](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/)

Lenovo-specific note: Lenovo Vantage sometimes runs its own downloads concurrently, and on metered or slow connections the two can starve each other. Also check the obvious: 24H2-era updates are large, and on a slow connection 'stuck at 12%' for an hour may just be slow. The first fix separates slow from stuck so you do not repair what is not broken.

## Why this happens

- **Hung BITS jobs.** Stalled Background Intelligent Transfer jobs clog the queue and nothing new downloads. bitsadmin /list /allusers shows the hung jobs directly.
- **Corrupted download cache.** Damaged chunks in SoftwareDistribution break resume logic. Rename the folder rather than deleting it, so you can revert.
- **Delivery Optimization peer loop.** Re-requesting chunks from peers instead of progressing. The setting is under Windows Update > Advanced options > Delivery Optimization.
- **Metered connection throttling.** Windows deliberately trickling the download. Settings > Network & internet reveals the metered flag.
- **VPN or proxy interference.** Update endpoints blocked while browsing works fine. Disconnect the VPN fully, not just pause it, when testing.
- **DNS resolution failure.** The update CDN hostnames not resolving on your network. ipconfig /flushdns after changing servers.
- **Lenovo Vantage bandwidth contention.** Concurrent Vantage downloads starving Windows Update. Vantage > settings > driver updates can be set to manual.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine slow versus stuck

Check whether bytes are actually moving before repairing anything. BITS (Background Intelligent Transfer Service) is the engine behind update downloads; hung BITS jobs are the most common reason the percentage freezes.

1. Open Task Manager > Performance > Wi-Fi/Ethernet and watch for download activity.
2. In Settings > Windows Update, note the exact percentage, wait 20 minutes, and compare.
3. If data is flowing, it is slow — leave it alone, possibly overnight.
4. If zero data flows for 30+ minutes, it is stuck — continue.
5. Also test browsing to confirm the network itself works.
6. Watch Task Manager > Performance > network for 10 minutes to confirm bytes are actually flowing now.

### Fix 2: Restart the BITS and update services

Hung transfer jobs clear with a service restart. The SoftwareDistribution\Download folder holds partial downloads — when its resume metadata corrupts, the counter freezes because the resume logic loops.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits.
3. Wait 10 seconds, then run: net start bits, net start wuauserv.
4. Check whether the download resumes within a few minutes.
5. If it stalls again at the same percentage, the cache is likely corrupt — next fix.
6. Note the percentage, wait 20 minutes, and compare — movement means working, frozen means still stuck.

### Fix 3: Reset the download cache

Clear the corrupted chunks so the download starts clean. [updates taking too long in general](/articles/how-to-fix-windows-update-taking-too-long-in-windows-11-24h2/) Delivery Optimization's peer sharing can re-request the same chunks endlessly; restricting it to Microsoft servers is a valid diagnostic step.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv & net stop bits & net stop cryptsvc.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Restart the services with net start.
5. The download restarts from zero — this is expected and healthy.
6. Confirm the BITS service shows as Running in services.msc after the restart.

### Fix 4: Pause Lenovo Vantage downloads

Eliminate bandwidth contention from Lenovo's own updater. On Lenovo laptops, pause Lenovo Vantage's own downloads while testing — both use BITS and they contend for bandwidth on slow connections.

1. Open Lenovo Vantage and pause any in-progress downloads.
2. Set Vantage driver updates to manual temporarily.
3. Close Vantage completely.
4. Retry the Windows Update download alone.
5. Re-enable Vantage automation after the update completes.
6. Check that SoftwareDistribution\Download is repopulating with fresh timestamps.

### Fix 5: Check for metered connection

A wrongly flagged metered connection trickles the download. A metered connection makes Windows deliberately trickle downloads; a wrongly flagged metered connection looks exactly like a stuck download.

1. Go to Settings > Network & internet and open your connection.
2. Turn off 'Metered connection' if you have unlimited data.
3. In Windows Update, ensure downloads are not paused.
4. Retry and watch the speed.
5. Only use metering on genuinely capped connections.
6. Test browsing to confirm the network path itself is healthy.

### Fix 6: Disable VPN and proxy temporarily

Update CDN traffic is sensitive to VPNs and proxies. VPNs and proxies can block the CDN endpoints Windows Update uses even while web browsing works fine, because update traffic uses different hosts.

1. Disconnect any VPN client completely (not just pause it).
2. Go to Settings > Network & internet > Proxy and turn off manual proxy.
3. Flush DNS: ipconfig /flushdns in Command Prompt.
4. Retry the download on the direct connection.
5. If it works, the VPN/proxy was interfering — update its config or exclusions.
6. If you changed DNS, verify with nslookup that update hostnames resolve.

### Fix 7: Switch DNS servers

CDN resolution failures stall downloads while browsing seems fine. DNS failures against the update CDN produce stalls that look like client problems; switching to 8.8.8.8 is a thirty-second test.

1. Open network adapter properties > IPv4 properties.
2. Set DNS to 8.8.8.8 and 8.8.4.4 (or 1.1.1.1 / 1.0.0.1).
3. Run ipconfig /flushdns.
4. Retry the download.
5. If it resumes, your ISP's DNS was failing the update CDN hostnames.
6. Reconnect the VPN afterward and confirm whether the stall returns — that identifies the culprit.

## Closing

Download stalls are delivery problems with a short suspect list, which makes them satisfying to fix — restart BITS, clear the cache, check the network path, and the bytes flow again. The Catalog bypass exists for the stubborn cases where the pipeline itself will not cooperate. For installs that fail after downloading, [a metered connection blocking updates](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) picks up the story. For Microsoft's own documentation on these repairs, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
