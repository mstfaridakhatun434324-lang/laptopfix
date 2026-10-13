---
title: "KB5041585 Stuck at Downloading on Windows 11? Fix It Fast"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-windows-11
date: 2026-09-06
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "windows 11", "cumulative update", "windows update"]
description: "KB5041585 frozen at downloading on Windows 11? Diagnose the stalled transfer, clear the corrupt partial file, and get this cumulative update installed."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-windows-11.webp"
faqs:
  - q: "What is KB5041585?"
    a: "KB5041585 is a Windows cumulative update — a single large package bundling that month's security patches and reliability fixes. Cumulative updates are several hundred megabytes, which makes their downloads more vulnerable to network interruptions and transfer stalls than smaller updates. The size is the reason this particular update gets stuck more often than tiny patches do."
  - q: "How can I tell if the download is stuck versus just slow?"
    a: "Watch the percentage for 30–45 minutes on a working internet connection. A slow download still moves, even in small increments. A stuck download shows zero progress over that window, sometimes with the status text flickering between 'Downloading' and 'Pending download'."
  - q: "Does pausing and resuming the update help?"
    a: "Sometimes. Pausing for a few minutes and resuming can jolt a stalled BITS transfer back to life. But if the underlying partial file is corrupt, pause/resume just resumes the corruption — the cache clear in this guide is the definitive fix."
  - q: "Is it safe to install this update manually?"
    a: "Yes. Downloading the KB package from the official Microsoft Update Catalog and installing it is a fully supported method. The package is byte-identical to what Windows Update would deliver — you are only changing the delivery mechanism, which is exactly why it works when the automatic pipeline is jammed."
---

KB5041585 stuck at "Downloading" on Windows 11 is one of those problems that feels like it should fix itself if you wait long enough. Sometimes it does — slow connections and large cumulative updates need patience. But when the percentage has not budged in an hour, waiting becomes the problem: a stalled transfer holding a corrupt partial file will never complete on its own. This guide helps you make the stuck-vs-slow call correctly, then clears the jam and gets the update installed.

If you are seeing this on Windows 10 instead, the [Windows 10 version of this fix](/articles/how-to-fix-kb5041585-stuck-at-downloading-on-windows-10/) covers the same update with that OS's specifics.

The psychology of a stuck download deserves a mention, because it causes most of the damage in these situations. A frozen percentage bar invites two bad reactions: force-restarting in frustration (which can corrupt the partial download further) or waiting indefinitely (which wastes hours on a transfer that will never complete). The disciplined middle path — verify the stall with evidence, then reset the pipeline decisively — resolves the problem in minutes. The steps below are that middle path: no rage-reboots, no endless waiting, just diagnosis followed by action.

One more Windows 11-specific note: the Settings app sometimes shows a stale "Downloading" status even after the transfer has stalled underneath. If the percentage never moves but Task Manager shows no network activity for the update process, trust Task Manager over Settings. The status text is a lagging indicator; the network graph is ground truth.

## Why this happens

- **Wedged BITS transfer:** The Background Intelligent Transfer Service stalls on a network hiccup and never resumes, leaving the download frozen without an error.
- **Corrupt partial file:** An interrupted attempt left a damaged partial download that Windows keeps trying to resume.
- **Bandwidth contention:** Other downloads, streaming, or cloud sync saturating the connection starves the update transfer.
- **Metered connection restrictions:** Windows throttles update downloads on metered connections, which can look exactly like a stuck download.
- **VPN/proxy interference:** Long-lived update connections are fragile through some VPNs and corporate proxies.
- **Antivirus scanning the partial file:** Real-time scanners locking the partial download file can block the transfer service from appending to it.
- **Low disk space:** The package cannot stage fully, so the download stalls instead of erroring out.
- **Pending restart deadlock:** An earlier update awaiting restart holds the pipeline, and the new download never properly starts — a queue problem also seen when [cumulative updates fail repeatedly](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is stuck, then try pause and resume

1. Note the exact percentage and wait 30 minutes without touching anything. If it moves at all, it is slow — let it finish.
2. If frozen, click "Pause updates" for 7 days, wait 2 minutes, then resume updates.
3. Check whether the download restarts fresh or resumes. If it immediately re-freezes at the same percentage, the partial file is corrupt — continue to Fix 3.

### Fix 2: Eliminate contention and restrictions

1. Pause cloud sync (OneDrive), streaming, and large downloads.
2. Disconnect any VPN temporarily.
3. Check Settings, Network & internet — ensure the connection is not set as metered.
4. Plug in the AC adapter and disable any battery-saver mode that throttles background activity.

### Fix 3: Clear the update cache for a fresh download

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete the contents of C:\Windows\SoftwareDistribution.
4. Restart the services, reboot, and check for updates. The download restarts from zero with clean files.

### Fix 4: Restart and reset BITS

1. In services.msc, restart Background Intelligent Transfer Service and Windows Update.
2. In an elevated Command Prompt, run `bitsadmin /reset /allusers` to clear wedged jobs.
3. Retry the update.

### Fix 5: Run the Windows Update troubleshooter

1. Go to Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart and check for updates.

### Fix 6: Free space and verify the drive

1. Run Disk Cleanup as administrator and clear Windows Update Cleanup, Temporary files, and Delivery Optimization Files — target 20+ GB free.
2. Run `chkdsk C: /f` (schedule at restart if prompted) to rule out disk corruption of the partial file.
3. Retry the download after the space is freed.

### Fix 7: Manual install from the Microsoft Update Catalog

1. Search for KB5041585 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Download the Windows 11 x64 package.
3. Run the installer (temporarily pause third-party antivirus if it interferes), restart when prompted.
4. Confirm installation in Update history. For broader update health guidance, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents these recovery steps officially.

### Fix 8: Reset Delivery Optimization

Windows 11's peer-to-peer update sharing can itself stall downloads.

1. Go to Settings, Windows Update, Advanced options, Delivery Optimization.
2. Turn off "Allow downloads from other PCs" temporarily.
3. Click "Advanced options" within Delivery Optimization and note your bandwidth limits \u2014 overly aggressive limits can throttle the download to a crawl that looks like a stall.
4. Clear the update cache once more (Fix 3), then retry with Delivery Optimization simplified. Re-enable peer sharing afterward if you normally use it.
5. If downloads stall again after re-enabling peer sharing, leave it off permanently — on some networks the peer protocol itself is the problem, and direct downloads from Microsoft are more reliable.

## Closing

The stuck-vs-slow judgment call is the whole battle with KB5041585: give a slow download its time, but do not donate hours to a frozen one \u2014 and do not rage-reboot a transfer that might still be working. Once you have confirmed the stall with real evidence, the cache clear, BITS reset, and manual install are all decisive. Cumulative updates are too important to leave in limbo; they carry the month's security fixes, and a fresh manual install beats a stuck automatic one every single time. If the manual install was what finally worked, consider making it your default approach for future cumulative updates on this machine — a five-minute catalog download beats an hour of watching a frozen progress bar.
