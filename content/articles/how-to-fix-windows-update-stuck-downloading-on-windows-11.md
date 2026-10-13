---
title: "Fix Windows Update Stuck Downloading on Windows 11"
slug: how-to-fix-windows-update-stuck-downloading-on-windows-11
date: 2026-10-05
categories: ["windows-update"]
tags: ["stuck downloading", "windows update", "windows 11", "bits"]
description: "Windows 11 update stuck at 0% or frozen mid-download? It's a download-pipeline problem. Here are 7 fixes — BITS reset, cache clear, and more."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-windows-11.webp"
faqs:
  - q: "How long should I wait before calling a download stuck?"
    a: "Give it at least an hour on a normal broadband connection, longer for feature updates which are several gigabytes. Check Task Manager's Performance tab for actual network activity — if the Wi-Fi or Ethernet graph shows sustained download traffic, the update is progressing even if the percentage barely moves. A true stall shows zero network activity and zero disk writes for over an hour."
  - q: "Why does the download stick at 0% specifically?"
    a: "Zero percent almost always means the download never started: the Background Intelligent Transfer Service (BITS) has a stuck job queue, the update service cannot reach Microsoft's servers, or a metered-connection setting is blocking the transfer. It is a pipeline problem, not a file problem — which is why the BITS reset and service checks in the steps below target 0% stalls specifically."
  - q: "Will restarting my laptop during a stuck download cause problems?"
    a: "No — interrupting the download phase is the safest possible interruption. Partial downloads are simply discarded or resumed; nothing has been installed or modified yet. Restart freely if the download is stuck. The danger zone is the install phase after the first restart, where interruption can trigger the undoing-changes rollback. Downloads are disposable by design."
  - q: "Does a VPN or metered connection cause downloads to stall?"
    a: "Both can. Metered connections pause most update downloads by design — Windows is obeying your setting, not malfunctioning. VPNs can stall downloads when the VPN endpoint throttles large transfers or when split-tunneling misroutes the update traffic. Temporarily disabling the metered flag and disconnecting the VPN are quick diagnostic steps that resolve a surprising number of download stalls."
---

A Windows 11 update stuck downloading is its own special purgatory: the percentage sits at 0% — or climbs to 37% and parks there — for hours, while the rest of the system works fine. Unlike install-phase failures, nothing is broken yet; the update simply is not arriving. That distinction matters because it narrows the suspects to the download pipeline: the transfer services, the network path, and the cache that receives the files.

The download pipeline has three main actors. BITS (Background Intelligent Transfer Service) manages the actual transfer jobs. The Windows Update service orchestrates what gets downloaded. And the SoftwareDistribution folder receives and assembles the pieces. A stall means one of these three is wedged — a stuck BITS job queue is the classic — or the network path itself is blocked. The fixes below unstick each layer in order.

## Why this happens

- **Stuck BITS job queue.** Dead transfer jobs clog the queue so new downloads never start — the classic 0% cause.
- **Corrupted download cache.** Damaged partial files in SoftwareDistribution that the updater keeps retrying.
- **Metered connection blocking.** Windows deliberately pausing downloads on connections marked as metered.
- **VPN or proxy interference.** Tunnels throttling or misrouting the large update transfers.
- **Antivirus network filtering.** Security software inspecting and stalling the download stream.
- **DNS or connectivity issues.** The update service unable to reliably reach Microsoft's servers.
- **Insufficient disk space.** Downloads that cannot be written stalling instead of erroring clearly.
- **Delivery Optimization cache corruption.** Windows 11's peer-to-peer download cache can hold damaged chunks that fail validation on every retry, stalling the download at the same percentage indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall and check the network path

Verify it is genuinely stuck and rule out the deliberate blocks before repairing anything.

1. Open Task Manager's **Performance** tab and watch the network graph for 5 minutes — sustained traffic means it is downloading, however slowly.
2. Check **Settings > Network & internet > Wi-Fi**, click your network, and see if **Metered connection** is on — turn it off if so.
3. Disconnect any VPN temporarily and retry the download.
4. If there is zero network activity for a full hour and no metered/VPN block, the pipeline is wedged — continue to Fix 2.

### Fix 2: Reset the BITS queue

The single most effective fix for downloads stuck at 0%. Clear the dead jobs so new transfers can start.

1. Open Command Prompt as administrator.
2. Run `bitsadmin /reset /allusers` to clear every stuck transfer job on the system.
3. Restart the **Background Intelligent Transfer Service** in `services.msc` (set it to Automatic if it is not).
4. Go to **Settings > Windows Update** and click **Check for updates** — the download should start fresh within minutes. If it still sits at 0%, also clear the Delivery Optimization cache at **Settings > System > Storage > Temporary files** (check **Delivery Optimization Files**) before checking for updates again.

### Fix 3: Restart the update services

If BITS was fine, the orchestration layer may be the wedged part. Restart it cleanly.

1. In an administrator Command Prompt, run: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Wait 30 seconds, then run: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
3. Check for updates again.
4. If the download starts but stalls at the same percentage repeatedly, the cache is corrupted — continue to Fix 4.

### Fix 4: Clear the download cache

Damaged partial downloads poison every retry. Wipe them and force a clean fetch.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates — the entire download restarts from zero with clean files.

### Fix 5: Check disk space and network filtering

Downloads need somewhere to land and a clear path to travel.

1. Confirm at least 10 GB free on C: at **Settings > System > Storage** (20 GB for feature updates).
2. Temporarily disable third-party antivirus web/network filtering and retry the download.
3. Try a different network if possible — mobile hotspot versus Wi-Fi — to rule out router or ISP-level throttling of Microsoft's servers.
4. Flush the DNS cache as a precaution: `ipconfig /flushdns` in an administrator Command Prompt.

### Fix 6: Run the Windows Update troubleshooter

The automated tool checks service states and re-registers components — worth running once the manual resets are done.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Update**.
2. Apply all suggested fixes and restart.
3. Check for updates again.
4. If the troubleshooter will not run, see our guide to the [troubleshooter not working](/articles/windows-update-troubleshooter-not-working-troubleshooting/).

### Fix 7: Download manually from the Update Catalog

When the download pipeline will not cooperate, sidestep it entirely.

1. Find the stuck update's KB number in **Settings > Windows Update > Update history** (or note which update is pending).
2. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the KB and download the x64 `.msu` package — this uses your browser's download, not BITS.
3. Double-click the `.msu` to install directly.
4. If even the manual download is slow or fails, the problem is your network path, not Windows — try the download from a different network. For persistent pipeline damage, our [0x80070002 guide](/articles/how-to-fix-windows-update-error-0x80070002-on-dell-laptop/) covers the deeper cache and store repairs.

## Closing

A Windows 11 update stuck downloading is a pipeline problem — BITS queue, services, cache, or network path — and it is one of the safest failures to fix because nothing has been installed yet. Reset BITS, restart the services, clear the cache, and check the metered and VPN settings; downloads almost always resume. If the download completes but the install then fails, that is a different phase with different fixes — see our guide to updates that [fail to install](/articles/how-to-fix-windows-update-fails-to-install-on-dell-laptop/) (the techniques apply beyond Dell); and once updates flow, keeping drivers current via our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) prevents the next cycle's stalls.
