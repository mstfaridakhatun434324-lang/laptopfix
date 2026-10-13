---
title: "KB5055523 Stuck Downloading on Windows 10? Unstick It Fast"
slug: how-to-fix-kb5055523-stuck-downloading-on-windows-10
date: 2026-09-08
categories: ["windows-update"]
tags: ["kb5055523", "stuck downloading", "windows 10", "bits"]
description: "Fix KB5055523 stuck downloading on Windows 10: restart the update agent, clear the queue, disable P2P sharing, and install the update."
thumbnail: "/images/thumbs/how-to-fix-kb5055523-stuck-downloading-on-windows-10.webp"
faqs:
  - q: "Does Windows 10 handle update downloads differently from Windows 11?"
    a: "The core engine — BITS plus the SoftwareDistribution cache — is the same, but Windows 10's update agent is older and its progress reporting is coarser. Windows 10 also defaults Delivery Optimization peer sharing to on more aggressively. The fixes overlap heavily, but the menus and the troubleshooter paths differ."
  - q: "Why does my Windows 10 PC download updates so much slower than my phone?"
    a: "BITS deliberately downloads in the background using idle bandwidth so it never hogs your connection — that politeness reads as slowness. Peer-to-peer misconfiguration and antivirus download scanning slow it further. A healthy Windows 10 download should still finish a cumulative update within the hour on broadband."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, with the update services stopped first. The folder holds only pending downloads and history; Windows rebuilds it automatically. Deleting its contents is the standard, Microsoft-supported way to clear a corrupted download queue — it touches nothing installed and nothing personal."
  - q: "My download is stuck at 0% — is that different from stuck at 80%?"
    a: "Stuck at 0% usually means the job never started: a service problem, a metered block, or a network issue. Stuck mid-download usually means a corrupt cache chunk or a stalled peer. Both yield to the same sequence below, but the 0% case leans toward Fixes 2 and 6 while the mid-download case leans toward Fixes 4 and 5."
---

On Windows 10, KB5055523 stuck downloading has its own personality. The older update agent reports progress coarsely, peer-to-peer sharing defaults to aggressive, and the BITS queue wedges in ways the newer Windows 11 agent mostly avoids. The symptom is identical — a frozen percentage — but the most effective fix order is tuned for Windows 10's menus and behaviors.

Follow this sequence top to bottom. It starts with the classic service restart, moves through the cache and P2P settings, and ends with the manual install that bypasses the whole pipeline.

Windows 10's updater deserves a little patience at the start and none after that: its progress bar is coarse and its initial negotiation is slow, so verify a genuine stall with Task Manager before resetting anything. But once you have confirmed thirty minutes of zero network activity, stop waiting — every further hour of hoping is an hour you could have spent fixing. Keep the charger plugged in throughout; Windows 10 is more likely than 11 to pause update work on battery, which can mimic a stuck download.

## Why this happens

- **Wedged wuauserv/BITS:** Windows 10's update services stall and need a proper restart, not just a retry click.
- **Corrupt download cache:** Interrupted chunks poison the SoftwareDistribution folder the downloader resumes from.
- **Aggressive P2P defaults:** Windows 10 shares updates with internet peers out of the box, inviting bad-peer stalls.
- **Metered connection flags:** Silently pauses cumulative downloads with no clear notification.
- **Proxy/VPN interference:** Breaks the CDN endpoints the downloader prefers.
- **Antivirus stream scanning:** Chokes the large package download mid-stream.
- **Aging HDDs:** Older Windows 10 laptops on spinning disks hit bad sectors in the staging area.
- **Corrupt update database:** The DataStore loses track of job state. Compare the [KB5036893 Win10 stall](/articles/how-to-fix-kb5036893-stuck-downloading-on-windows-10/) — same engine, same failure family.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with real measurements

1. Note the percentage in **Settings → Update & Security → Windows Update** and the time.
2. Open **Task Manager → Performance** and watch network activity for 30 minutes.
3. Zero traffic plus a frozen percentage means stuck; steady traffic means slow — wait it out.
4. Check free space on C: — under 15 GB can stall staging silently.
5. Stuck at 0% points at services or network; stuck mid-download points at cache or peers.

### Fix 2: Restart the update services correctly

1. Press **Win + R**, type `services.msc`, and locate **Windows Update** and **Background Intelligent Transfer Service**.
2. Restart both, even if they claim to be running — a zombie "running" state is the classic Windows 10 failure.
3. Return to Windows Update and click **Check for updates**.
4. Watch for 15 minutes; a genuine service stall clears here.
5. If the service will not stay running, continue — the cache reset in Fix 4 addresses the deeper cause.

### Fix 3: Run the Windows 10 troubleshooter

1. **Settings → Update & Security → Troubleshoot → Additional troubleshooters → Windows Update**.
2. Run it, apply every fix, reboot when asked.
3. The troubleshooter re-registers the update DLLs that Windows 10's agent sometimes loses.
4. Retry the download once afterward.
5. Unchanged behavior means the problem is data (cache) or network, not service registration.

### Fix 4: Clear the SoftwareDistribution cache

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`.
2. Delete all contents of `C:\Windows\SoftwareDistribution\Download`.
3. Restart: `net start wuauserv`, `net start bits`.
4. Check for updates — the download restarts cleanly from zero.
5. If it freezes at the same percentage again, suspect the network path and try a hotspot.

### Fix 5: Disable peer-to-peer sharing

1. **Settings → Update & Security → Delivery Optimization**.
2. Turn off **Allow downloads from other PCs** completely.
3. Retry the download as a direct pull from Microsoft.
4. Windows 10's aggressive P2P defaults cause more stalls than on Windows 11 — this toggle matters more here.
5. Leave it off unless you run several Windows 10 PCs on a fast LAN.

### Fix 6: Check metered, proxy, and VPN settings

1. **Settings → Network & Internet → Wi-Fi**: turn off **Set as metered connection**.
2. Check **Proxy** for unexpected manual entries; disconnect VPNs during the download.
3. School and corporate networks with filtering proxies are frequent culprits — test a home network if possible.
4. Retry after each change to identify the blocker.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the network settings that affect updating.

### Fix 7: Reset the network stack

1. Elevated prompt: `netsh winsock reset`, `netsh int ip reset` — then reboot.
2. After reboot: `ipconfig /flushdns`.
3. Reconnect and retry the download.
4. This clears socket-level stalls that survive service restarts.
5. If the whole connection is slow, fix the network first — no update setting overcomes a broken link.

### Fix 8: Manual install from the Update Catalog

1. Download the Windows 10 x64 .msu for KB5055523 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Close all apps, disconnect VPN, run the package.
3. Reboot; verify in **View update history**.
4. The standalone installer bypasses BITS, P2P, and the cache entirely.
5. For the general stuck-download reference beyond this KB, the [post-clean-install update guide](/articles/how-to-fix-windows-update-error-after-clean-install-on-windows-10/) covers related Windows 10 pipeline repairs.

## Closing

Windows 10's KB5055523 download stalls are the update agent's own state in almost every case: zombie services, a poisoned cache, or peer-to-peer sharing gone wrong. Restart the services properly, run the classic troubleshooter, clear the cache, disable P2P, and check metered and proxy settings. When the pipeline will not cooperate, the catalog installer finishes it in minutes. Keep P2P off on simple networks and 15 GB free on C:, and Windows 10's updater — old as it is — will do its job quietly. And make update checks a monthly habit rather than waiting for the automatic cycle: small, frequent updates download reliably, while the giant catch-up batches that pile up over months are the ones that stall.
