---
title: "Fix Windows Update Stuck Downloading on Windows 10"
slug: how-to-fix-windows-update-stuck-downloading-on-windows-10
date: 2026-10-07
categories: ["windows-update"]
tags: ["stuck downloading", "windows update", "windows 10", "bits"]
description: "Windows 10 update frozen at 0% or stuck mid-download? 7 fixes — BITS reset, cache rebuild, metered-connection check — to get downloads moving."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-windows-10.webp"
faqs:
  - q: "How long should a Windows 10 update download normally take?"
    a: "A monthly cumulative update is a few hundred megabytes and should download in minutes on broadband; feature updates are several gigabytes and can take 30 to 60 minutes. Only call it stuck after an hour of zero progress. Check Task Manager's Performance tab for real network activity first — the Settings percentage is a poor progress indicator and often sits still while data flows."
  - q: "Why is my Windows 10 download stuck at 0%?"
    a: "Zero percent means the transfer never started. The usual causes on Windows 10 are a wedged BITS job queue, the Windows Update service failing to reach Microsoft's servers, or a metered-connection setting pausing the download. Windows 10 is also more aggressive than 11 about deferring downloads on metered connections, so the metered flag is worth checking first — it is the fastest fix when it applies."
  - q: "Is it safe to restart while a Windows 10 update is stuck downloading?"
    a: "Completely safe. The download phase has installed nothing and modified nothing — partial downloads are discarded or resumed automatically. Restart as freely as you like during a download stall. The phase where interruption matters is after the install begins and the first restart happens; downloads themselves are disposable by design."
  - q: "Do I need to keep Windows 10 updated if I plan to upgrade to Windows 11?"
    a: "Yes, at least stay reasonably current. The Windows 11 upgrade checks system health and servicing state, and a machine with a deeply broken update pipeline often fails the upgrade too. Fixing the download stall now — with the steps below — gives you a healthy servicing stack, which makes the eventual Windows 11 upgrade dramatically more likely to succeed."
---

A Windows 10 update stuck downloading follows the same script every time: the progress bar sits at 0% — or freezes partway — for hours while everything else on the laptop works perfectly. No error message, no crash, just a download that refuses to download. On Windows 10 this is especially common around Patch Tuesday, when Microsoft's servers are hammered and the local download pipeline is at its most fragile.

The reassuring fact is that a download stall is the safest update failure there is: nothing has been installed, nothing has been modified, and interrupting it carries zero risk. The suspects are the download pipeline itself — BITS (Background Intelligent Transfer Service) and its job queue, the Windows Update orchestration service, the network path, and the cache receiving the files. The fixes below unstick each layer, starting with the most common.

## Why this happens

- **Wedged BITS job queue.** Dead transfer jobs block new downloads — the number one cause of 0% stalls.
- **Metered connection pausing.** Windows 10 aggressively defers downloads on metered connections by design.
- **Corrupted partial downloads.** Damaged cache files that the updater retries instead of replacing.
- **Windows Update service hung.** The orchestration service itself stuck and not dispatching work to BITS.
- **VPN, proxy, or firewall interference.** Network intermediaries throttling or breaking the large transfers.
- **Antivirus network filtering.** Security software inspecting the download stream and stalling it.
- **Disk space exhaustion.** Downloads with nowhere to be written stalling instead of failing clearly.
- **Corrupted Delivery Optimization cache.** Windows 10's peer-to-peer download sharing can cache damaged update chunks that fail validation repeatedly, freezing the download at the same percentage on every attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall and check the deliberate blocks

Rule out the settings that pause downloads on purpose before repairing anything.

1. Open Task Manager's **Performance** tab and watch network activity for 5 minutes — real traffic means it is downloading despite the frozen percentage.
2. Go to **Settings > Network & Internet > Wi-Fi** (or Ethernet), click your connection, and check **Set as metered connection** — turn it off; Windows 10 defers downloads on metered links.
3. Disconnect any VPN and retry. VPN endpoints frequently throttle Microsoft's update servers.
4. With zero network activity for a full hour and no metered/VPN block, the pipeline is genuinely wedged — continue to Fix 2.

### Fix 2: Reset the BITS queue

The classic 0% fix: clear the dead transfer jobs so fresh downloads can start.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Run `bitsadmin /reset /allusers` to clear all stuck transfer jobs.
3. Open `services.msc`, find **Background Intelligent Transfer Service**, set it to **Automatic**, and start it.
4. Go to **Settings > Update & Security > Windows Update** and click **Check for updates** — the download should begin within minutes. If the percentage still does not move, open Disk Cleanup, check **Delivery Optimization Files**, and clean them — stale peer-cached chunks are a common hidden cause of repeat stalls at the same percentage.

### Fix 3: Restart the Windows Update services

If BITS is healthy, restart the orchestration layer around it.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Wait 30 seconds, then: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
3. Check for updates again.
4. If downloads start but repeatedly stall at the same percentage, the cache is corrupted — move to Fix 4.

### Fix 4: Rebuild the download cache

Wipe the damaged partial downloads and force Windows to fetch clean copies.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates — the download restarts from zero with a clean cache.

### Fix 5: Free disk space and clear network interference

Downloads need landing room and a clear path.

1. Ensure at least 10 GB free on C: (**Settings > System > Storage**); feature updates need closer to 20 GB.
2. Run Disk Cleanup with **Clean up system files** to remove old update backups.
3. Temporarily disable third-party antivirus web shields and retry.
4. Try an alternate network (phone hotspot) to rule out router or ISP throttling, and run `ipconfig /flushdns` in an elevated prompt as a precaution.

### Fix 6: Run the Windows Update troubleshooter

Windows 10's troubleshooter automates the service and component checks — run it after the manual resets.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Windows Update** and run it.
2. Apply every suggested fix, then restart.
3. Check for updates again.
4. If the troubleshooter will not run, our guide to the [troubleshooter not working](/articles/windows-update-troubleshooter-not-working-troubleshooting/) covers that separately (written for Windows 11, but the mechanics match).

### Fix 7: Install the update manually from the Update Catalog

Bypass the broken pipeline with a browser download and direct install.

1. Identify the stuck update's KB number in **View update history**.
2. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for that KB and download the x64 `.msu`.
3. Double-click the `.msu` to install directly, then restart when prompted.
4. Verify in Update history. If the manual route also stalls, the issue is the network path — try a different connection. For the monthly-failure pattern on Windows 10, our guide to [cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-10/) covers the deeper repairs.

## Closing

A Windows 10 download stall is a pipeline problem with pipeline fixes: reset BITS, restart the services, rebuild the cache, and check the metered-connection and VPN settings that pause downloads deliberately. Because nothing is installed yet, every step here is safe to try. Once downloads flow, keep the pipeline healthy — and if the download finishes but the install then fails, our guide to updates that [fail to install](/articles/how-to-fix-windows-update-fails-to-install-on-dell-laptop/) picks up at the next phase (the techniques apply to Windows 10 as well as 11).
