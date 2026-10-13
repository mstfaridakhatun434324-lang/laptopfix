---
title: "Windows Update Stuck Downloading on Windows 11 24H2: Fix It"
slug: how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2
date: 2026-09-01
categories: ["windows-update"]
tags: ["stuck downloading", "windows 11 24h2", "bits", "delivery optimization", "0 percent"]
description: "Windows Update is frozen at 0% or crawling on Windows 11 24H2? Diagnose the download stall and get updates flowing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2.webp"
faqs:
  - q: "How do I know if the download is stuck or just slow?"
    a: "Open Task Manager's Performance tab and watch network usage. Consistent download traffic means it's working, even at 0% — Windows sometimes doesn't update the percentage until chunks complete. If network activity is flat at zero for over an hour while the update claims to be downloading, it's genuinely stuck and this guide applies."
  - q: "Does 24H2 download updates differently from earlier versions?"
    a: "Yes, somewhat. 24H2 uses checkpoint cumulative updates, which changed the payload structure — the system downloads a smaller delta against the last checkpoint rather than the full cumulative package. The download pipeline (BITS, Delivery Optimization) works the same way, so the stall causes and fixes here apply equally, but a corrupted checkpoint baseline can cause unique failures."
  - q: "Can I use my laptop normally while the download is stuck?"
    a: "Yes. A stuck download doesn't harm anything — it's just not progressing. You can keep working; the fixes in this guide (service restarts, cache clears) are safe to run while you use the machine. Only avoid restarting mid-fix: let each step complete, especially the DISM and cache operations, before moving on."
  - q: "Will resetting the download delete updates I already installed?"
    a: "No. Clearing the SoftwareDistribution cache only removes pending downloads and metadata — installed updates stay installed. Your update history is preserved. The worst case is re-downloading the pending update from scratch, which is exactly what you want when the partial download is the corrupted part."
---

The update says "Downloading — 0%." An hour later: "Downloading — 0%." Or it creeps to 7% and dies there. On Windows 11 24H2, download stalls have the usual classic causes plus a few quirks of the new checkpoint update model — but the diagnostic approach is the same: verify the stall, then work the delivery pipeline from the service layer down.

Downloads are the most mechanical part of Windows Update. Bits move or they don't, and when they don't, the cause is almost always in BITS itself, the cache, the network path, or a throttling setting. There is very little mystery here once you check the right things.

Work through these in order — diagnose first, then act.

## Why this happens

- **BITS deadlock.** The transfer service wedges and stops requesting data.
- **Corrupted partial download.** Damaged chunks in the cache that the downloader keeps retrying.
- **Delivery Optimization issues.** Bad peer sources or misconfigured optimization stalling the transfer.
- **Metered connection.** Windows silently pausing the download on a metered network.
- **Bandwidth caps.** Delivery Optimization throttles set aggressively low.
- **Corrupted checkpoint baseline.** 24H2's checkpoint model failing against a damaged baseline.
- **Network interference.** VPNs, proxies, or strict firewalls breaking the download stream.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with Task Manager

Open Task Manager, Performance tab, and watch the Wi-Fi/Ethernet graph for 15 minutes. Steady traffic means downloading is happening — 24H2's checkpoint deltas can sit at 0% for a long time while the manifest downloads, then jump suddenly.

Also check that the laptop is not asleep and the connection is stable — try loading a webpage to confirm real connectivity. Only when network activity is flat zero for a full hour, on a working connection, do you have a genuine stall. Write down the frozen percentage for comparison after each fix.

### Fix 2: Restart BITS and the Windows Update service

The classic unstick for a wedged transfer:

1. Press Win+R, type `services.msc`, press Enter.
2. Right-click "Background Intelligent Transfer Service" and choose Restart.
3. Right-click "Windows Update" and choose Restart.
4. If BITS shows Disabled, set its Startup type to Manual first, then start it.

Back in Settings, Windows Update, click "Check for updates" and watch for 20 minutes. A BITS deadlock is the single most common download-stall cause, and a service restart clears it without losing downloaded progress.

### Fix 3: Clear the partial download cache

When the cached chunks are corrupt, only a clean download works:

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`, then `net stop bits`
3. Delete everything inside `C:\Windows\SoftwareDistribution\Download`.
4. Run: `net start bits`, then `net start wuauserv`
5. In Settings, Windows Update, click "Check for updates."

The percentage resets to 0% — expected. Watch for genuine progress over the next 30 minutes. If it stalls at the exact same point again, the issue is upstream of the cache (network or throttling), not in it.

### Fix 4: Check metered status and Delivery Optimization

Go to Settings, Network & internet, click your connection, and verify "Set as metered connection" is off — metered networks pause downloads silently. Then go to Windows Update, Advanced options, Delivery Optimization: try turning off "Allow downloads from other PCs" to force a direct Microsoft download, and check Advanced settings for bandwidth caps.

A background-download cap near zero percent will make even a healthy connection look stalled. These settings persist across networks and updates, so a cap set months ago could be the entire problem. The metered-connection angle is covered in depth in the [metered connection blocking guide](/articles/how-to-fix-metered-connection-blocking-windows-update-on-laptop/).

### Fix 5: Bypass VPN, proxy, and firewall interference

Disconnect any VPN and retry the download — VPNs are a frequent cause of stalled or corrupted update streams. Check Settings, Network & internet, Proxy: turn off "Use a proxy server" unless your network requires it.

For firewall issues, temporarily disable third-party firewall software (keep Windows Firewall on) and retry. If the download suddenly works, add an exception for the update services or leave the third-party firewall's update-friendly mode enabled. Corporate networks with TLS inspection are a special case — the download may need IT's allowlist. Microsoft documents connectivity requirements in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 6: Reset the full update components

For stalls surviving the targeted fixes, reset everything:

1. Open Command Prompt as administrator.
2. Stop: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`
3. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`
4. Start: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`
5. Check for updates.

On 24H2, follow this with `DISM /Online /Cleanup-Image /RestoreHealth` to repair any checkpoint-baseline damage — a corrupted baseline makes every checkpoint delta fail to assemble, which presents as a download stall. If downloads stall but installs are your real problem, the [monthly cumulative failure guide for 24H2](/articles/how-to-fix-monthly-cumulative-update-failed-in-windows-11-24h2/) picks up where this leaves off.

### Fix 7: Manual download from the Update Catalog

When the automated download pipeline will not cooperate, skip it: find the KB number in Update history, visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), download the x64 .msu, and install it directly.

The Catalog download uses your browser, bypassing BITS and Delivery Optimization entirely. It is the same signed package through Microsoft's official manual channel. This is the definitive workaround for machines where the download pipeline itself is the broken component — and it gets you the update today instead of after days of pipeline debugging.

## Closing

Download stalls on 24H2 are pipeline problems: wedged BITS, corrupt cache, metered or throttled connections, or network interference. Verify the stall is real before acting, restart the transfer services, clear the cache, check the network path — and use the manual Catalog download when the pipeline itself refuses to cooperate. The bits either move or they don't; this sequence finds out why and fixes it.
