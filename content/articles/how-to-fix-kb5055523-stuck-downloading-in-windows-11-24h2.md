---
title: "KB5055523 Stuck Downloading? Here's How to Fix It on Windows 11 24H2"
slug: how-to-fix-kb5055523-stuck-downloading-in-windows-11-24h2
date: 2026-09-06
categories: ["windows-update"]
tags: ["kb5055523", "stuck downloading", "windows 11 24h2", "cumulative update"]
description: "KB5055523 is stuck downloading on your Windows 11 24H2 laptop? Diagnose the stall and fix it, or install the update manually."
thumbnail: "/images/thumbs/how-to-fix-kb5055523-stuck-downloading-in-windows-11-24h2.webp"
faqs:
  - q: "Why does KB5055523 keep failing to download?"
    a: "The most common reasons are a corrupted partial download in the SoftwareDistribution cache, a metered connection that throttles the download, VPN or proxy interference, and not enough free disk space for staging. Any of these can freeze the progress bar at the same percentage repeatedly, even across restarts."
  - q: "Can I skip KB5055523 and wait for the next update?"
    a: "You can, but it is not recommended. Cumulative updates include security patches for actively exploited vulnerabilities, and skipping one just makes the next package larger since each cumulative update contains everything before it. Fixing the download pipeline now is better than letting updates pile up for months while your system stays exposed to known flaws."
  - q: "Will resetting the update cache delete my personal files?"
    a: "No. Resetting the SoftwareDistribution cache only deletes downloaded update files and pending installation data. Your documents, photos, applications, and settings are completely untouched, and no installed program is affected. Windows simply re-downloads whatever update files it still needs afterward, so the only cost is a little download time."
  - q: "How do I know which KB5055523 package to download manually?"
    a: "Search the Microsoft Update Catalog for KB5055523 and pick the entry matching your architecture and Windows 11 version. Almost all modern laptops are x64. Installing the wrong architecture package will simply refuse to install, so it cannot damage the system."
---

You clicked "Check for updates," KB5055523 appeared, the download started — and then it just stopped moving. The percentage sits there mocking you while the rest of your internet works perfectly. You restart, it tries again, and lands on exactly the same number. This is the classic signature of a stuck cumulative update download on Windows 11 24H2: the update itself is fine, but the delivery mechanism has wedged itself.

Under the hood, the download is handled by the Background Intelligent Transfer Service, which fetches the package in chunks and is supposed to resume gracefully after interruptions. The trouble starts when one of those chunks is corrupt: BITS keeps trying to resume from the damaged data instead of discarding it, so every attempt stalls at the same percentage. Laptops are especially prone to this because lid closes, sleep transitions, and network changes interrupt transfers far more often than on desktops, multiplying the chances of a poisoned partial download.

KB5055523 is a sizable package, and 24H2's update engine can get tripped up by a corrupted cache, a throttled connection, or a half-finished resume. The fixes below go from quick checks to the nuclear option of a manual install, in the order a technician would actually try them.

## Why this happens

- **A damaged partial download keeps resuming.** Windows tries to pick up where the last attempt stopped, but the cached chunks are corrupt, so every attempt stalls at the same point.
- **The SoftwareDistribution cache is inconsistent.** Corruption in the update datastore makes the engine unable to assemble or verify the incoming package.
- **Metered connection throttling.** If Windows thinks your connection is metered, it slows or pauses large downloads without telling you clearly.
- **VPN, proxy, or network filtering.** Anything between you and Microsoft's CDN that inspects or reshapes traffic can break the download stream.
- **Low disk space on the system drive.** The update needs room to download, verify, and stage. Below a few gigabytes free, the download silently stops.
- **The Background Intelligent Transfer Service (BITS) is failing.** BITS handles the actual download; if it is stuck or misconfigured, nothing moves.
- **A missing servicing stack prerequisite.** Without the matching servicing stack update, the engine can reject or mishandle the cumulative package.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall and check the basics

Rule out "just slow" before doing surgery.

1. Note the exact percentage in **Settings** > **Windows Update**, then check again after 45 minutes. No movement confirms a real stall.
2. Confirm your connection works normally with a speed test or streaming video.
3. Check free space: **Settings** > **System** > **Storage** should show at least 10 GB free on C:. Run Disk Cleanup if you are short.

### Fix 2: Restart BITS and the update services

A wedged transfer service is one of the most common causes.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Background Intelligent Transfer Service**, right-click, and choose **Restart**.
3. Do the same for **Windows Update** and **Cryptographic Services**.
4. Click **Check for updates** again and watch for movement over the next 20 minutes.

### Fix 3: Pause, restart, resume

Forcing a clean download state fixes transient resume corruption.

1. In **Settings** > **Windows Update**, click **Pause updates** for one week.
2. Restart the laptop — a real restart, not a shutdown, to clear Fast Startup state.
3. Resume updates and run **Check for updates**. The download restarts from zero with a clean slate.

### Fix 4: Clear the update download cache

When partial downloads are poisoned, deleting them is the fix.

1. Open **Command Prompt as administrator** and run:
   ```
   net stop wuauserv
   net stop bits
   ```
2. Delete the cached downloads:
   ```
   rd /s /q C:\Windows\SoftwareDistribution\Download
   ```
3. Restart the services:
   ```
   net start wuauserv
   net start bits
   ```
4. Check for updates. The same reset procedure is covered step by step in our guide to [resetting stuck Windows Update components](/articles/how-to-fix-kb5041585-stuck-at-downloading-on-dell-laptop/) if you want a refresher on what each folder does.

### Fix 5: Check Delivery Optimization and metered settings

Windows may be deliberately limiting the download.

1. Go to **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** and make sure downloads from other PCs or the internet are allowed.
2. In **Settings** > **Network & internet**, select your connection and turn off **Metered connection**.
3. Disconnect any VPN and retry. If the download jumps forward, the VPN was the bottleneck.

### Fix 6: Install KB5055523 manually

When the automatic engine will not cooperate, go around it.

1. Open [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for **KB5055523**.
2. Download the x64 package for Windows 11 24H2.
3. Run the `.msu` file. It installs the identical signed update without using the broken download pipeline.
4. Restart when prompted, then verify in **Update history**. The full procedure is documented in [how to install a KB update manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/).

### Fix 7: Repair the servicing stack, then retry

A damaged servicing stack poisons every update that passes through it.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt, then `sfc /scannow`.
2. Restart and retry Windows Update.
3. If the download still stalls, an in-place upgrade using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) refreshes the whole servicing stack while keeping your files and apps.

## Closing

KB5055523 stuck downloading is a delivery problem, not an update problem: clear the corrupted cache, make sure the connection is not metered or filtered, and restart the transfer services. For stubborn cases, the manual Catalog install is the same update delivered by a different route. Do not just leave it stuck indefinitely — every week the update sits undownloaded is a week your laptop misses security fixes that matter, and a clean download today prevents the backlog from compounding next month. Treat each stuck download as a signal to run the cache-clearing maintenance in Fix 4 proactively, and the problem rarely recurs.
