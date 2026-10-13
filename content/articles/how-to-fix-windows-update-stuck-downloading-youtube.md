---
title: "Windows Update Stuck Downloading? Step-by-Step Fixes That Actually Work"
slug: how-to-fix-windows-update-stuck-downloading-youtube
date: 2026-09-19
categories: ["windows-update"]
tags: ["windows update", "stuck downloading", "update fix", "troubleshooting"]
description: "Windows Update stuck at 0% or frozen mid-download? Diagnose the stall and fix it with a proven sequence, from simple restarts to a full component reset."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-youtube.webp"
faqs:
  - q: "How long should I wait before deciding Windows Update is stuck?"
    a: "Give it at least 30 to 60 minutes on a stable connection before intervening, especially for large feature updates that download several gigabytes. If the percentage has not moved at all in over an hour, or the download repeatedly resets to 0%, it is genuinely stuck. Check Task Manager first — active network and disk activity means it is still working."
  - q: "Is it safe to restart my laptop while an update is downloading?"
    a: "Yes, restarting during the download phase is safe. The download is just files being copied; nothing is being installed yet. Windows Update resumes or restarts the download after reboot. Never force a shutdown during the installation phase, when the screen says updates are being installed — that is where interruptions cause damage."
  - q: "Why does Windows Update keep getting stuck at the same percentage?"
    a: "A consistent stall point usually means a corrupted file in the local update cache or a specific package that fails integrity checks and gets re-downloaded in a loop. Clearing the SoftwareDistribution download cache breaks the loop. If it stalls at the same point after a cache clear, the package itself may be bad and needs a manual download."
  - q: "Can my antivirus cause Windows Update to get stuck downloading?"
    a: "Yes. Some third-party antivirus and firewall products inspect or block the connections Windows Update uses, causing downloads to crawl or stall. Temporarily disabling real-time protection — or the firewall component specifically — often unblocks the download immediately. Re-enable protection as soon as the download completes."
---

A download bar frozen at 0%, 47%, or 99% for hours is one of the most common Windows complaints, and it is almost never a Microsoft server problem. The stall is usually local: a corrupted cache file, a misbehaving service, a network setting, or a package that keeps failing its integrity check and restarting. The fix is a sequence, not a single trick.

The technician approach is to escalate gently. Start with the harmless checks — network, disk space, a service restart — and only move to cache deletion and component resets if the simple steps fail. Most stuck downloads resolve in the first three fixes; the later ones exist for the stubborn cases.

This guide assumes the update is stuck in the **download** phase, not the install phase. If your screen says "installing" or "working on updates" with a spinning circle, that is a different problem with different risks. For pure download stalls, work through the steps below.

## Why this happens

- **Corrupted download cache:** A partially downloaded file in the SoftwareDistribution folder fails its checksum, so the downloader discards it and starts over — forever.
- **Windows Update service hung:** The wuauserv service can deadlock after a failed attempt, leaving the UI showing progress that is not actually happening.
- **BITS transfer queue jammed:** The Background Intelligent Transfer Service manages the actual download; a jammed job blocks the whole queue behind it.
- **Metered connection throttling:** Windows pauses or severely limits update downloads on connections marked as metered, which sometimes gets set accidentally on home Wi-Fi.
- **Disk space too low for staging:** Downloads need room to land and expand. When C: is nearly full, the download stalls instead of erroring out cleanly.
- **VPN, proxy, or firewall interference:** Corporate VPNs and aggressive firewalls can block the specific endpoints Windows Update uses, producing a silent stall rather than an error.
- **Delivery Optimization peer issues:** The peer-to-peer sharing feature can get stuck waiting on unreachable peers on some networks. For the full deep-dive version of this repair, see the [step-by-step stuck-downloading guide](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is actually stuck

1. Open **Task Manager → Performance** and watch the Wi-Fi/Ethernet graph for two minutes. Steady traffic means it is still downloading.
2. Check **Settings → Windows Update** and note the exact percentage, then check again in 30 minutes.
3. Open **Task Manager → Processes** and look for disk activity from Service Host processes — active disk writes mean staging is happening.
4. If there is zero network and zero disk activity for a full hour, it is stuck. Proceed.
5. Also confirm you have at least 10 GB free on C: — a full drive is the simplest explanation.

### Fix 2: Restart the update services

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Update**, right-click, and choose **Restart**. If it is stopped, choose **Start**.
3. Do the same for **Background Intelligent Transfer Service**.
4. Return to **Settings → Windows Update** and click **Check for updates** or **Retry**.
5. Wait 15 minutes. A hung service is the single most common cause, and this alone fixes a large share of stalls.

### Fix 3: Check metered connection and network settings

1. Go to **Settings → Network & internet → Wi-Fi**, click your network, and check **Metered connection** — turn it **Off** if it is on.
2. Temporarily disconnect any **VPN** and disable third-party firewall features.
3. If you use a proxy, go to **Settings → Network & internet → Proxy** and turn off manual proxy setup temporarily.
4. Restart the laptop so the network stack comes up clean, then retry the download.
5. On corporate or school networks, ask whether update endpoints are filtered — some networks block them by policy.

### Fix 4: Clear the download cache

1. Open **Terminal as administrator** and run `net stop wuauserv` and `net stop bits`.
2. In File Explorer, go to `C:\Windows\SoftwareDistribution\Download` and delete everything inside.
3. Back in Terminal, run `net start wuauserv` and `net start bits`.
4. Go to **Settings → Windows Update** and click **Check for updates** — the download restarts from a clean cache.
5. This is safe: the folder holds only downloaded packages, never installed updates. For persistent stalls tied to one specific package, the [in-depth 24H2 stuck-downloading fix](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/) covers package-specific resets.

### Fix 5: Run the Windows Update troubleshooter

1. Open **Settings → System → Troubleshoot → Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Let it complete — it checks service states, cache integrity, and pending operations automatically.
4. Apply any fixes it recommends and restart if asked.
5. Retry the download. The troubleshooter catches configuration drift that manual steps miss.

### Fix 6: Reset all update components

1. Open **Terminal as administrator**.
2. Run these stop commands: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Restart the laptop and check for updates. This full reset resolves stalls that survive a simple cache clear.

### Fix 7: Disable Delivery Optimization temporarily

1. Go to **Settings → Windows Update → Advanced options → Delivery Optimization**.
2. Turn **off** "Allow downloads from other PCs".
3. Restart the Windows Update service from `services.msc`.
4. Retry the download — with peer sources removed, Windows pulls only from Microsoft servers.
5. You can re-enable Delivery Optimization after the update completes; it saves bandwidth on metered plans.

### Fix 8: Download the update manually as a last resort

1. Note the KB number from **Update history** in Settings.
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), search the KB, and download the matching package.
3. Double-click the `.msu` to install it directly, bypassing the stuck downloader.
4. Restart when prompted and verify in Update history.
5. If even the manual install fails, the package itself may be corrupt — run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` before trying again, following the official guidance on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

A stuck download is a plumbing problem, not a broken computer. Confirm the stall, restart the services, check the network flags, clear the cache, and reset components in that order. One of those steps almost always gets the bytes flowing again — and once you know the sequence, the next stuck update is a ten-minute job instead of an afternoon of staring at a frozen percentage.
