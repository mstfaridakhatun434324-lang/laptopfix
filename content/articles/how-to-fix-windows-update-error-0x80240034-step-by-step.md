---
title: "How to Fix Windows Update Error 0x80240034 Step by Step"
slug: how-to-fix-windows-update-error-0x80240034-step-by-step
date: 2026-10-03
categories: ["windows-update"]
tags: ["windows update", "0x80240034", "download failed", "windows 11"]
description: "Error 0x80240034 means Windows Update couldn't download the package. Follow this step-by-step guide: check metered settings, clear the cache, and download manually."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80240034-step-by-step.webp"
faqs:
  - q: "What causes Windows Update error 0x80240034?"
    a: "The code is WU_E_DOWNLOAD_FAILED: the update package did not finish downloading. Common causes are a metered connection limiting the transfer, Wi-Fi drops or VPN interruptions, a corrupted SoftwareDistribution cache holding partial fragments, proxy interference, or too little free disk space. Because nothing installs from a failed download, your system is unchanged — the repair focuses on the network and the cache."
  - q: "How do I know if my connection is metered?"
    a: "Open Settings, Network and internet, then Wi-Fi or Ethernet, and click your connected network. The metered connection toggle is shown there. Windows sometimes enables it automatically on mobile hotspots. On a normal home broadband connection it should be off; when it is on, Windows restricts large update downloads, which is a leading cause of this exact error."
  - q: "Why does the same update keep failing to download?"
    a: "Because each retry reuses the corrupted download cache. Partial fragments from the first failed attempt sit in the SoftwareDistribution folder, and subsequent retries trip over them instead of starting fresh. Renaming that folder forces Windows to download a completely clean copy, which is why the cache reset in Fix 4 breaks the retry loop."
  - q: "Can I download the update on another PC and transfer it?"
    a: "Yes. The Microsoft Update Catalog lets you download the .msu package on any computer; copy it to a USB drive, run it on the affected laptop, and the standalone installer handles the rest. This is genuinely useful when the laptop's own connection is the problem — a phone hotspot or a friend's Wi-Fi for one download beats endless failed retries."
---

Error 0x80240034 is Windows Update admitting the download didn't make it: WU_E_DOWNLOAD_FAILED. The package started transferring and never finished — cut off by a metered connection, a Wi-Fi drop, a poisoned cache, or simply nowhere to land on a full disk. Your system is untouched, because Windows never installs a package it can't fully verify.

The trap with this error is the retry loop: clicking "Retry" just re-downloads into the same broken cache over the same constrained connection. The sequence below breaks the loop by fixing the conditions first — connection, space, cache — and only then fetching the package again.

Note that a failed download is never dangerous. Windows cryptographically verifies packages before installing anything, so partial or corrupted data is discarded, never applied. The frustration of 0x80240034 is purely logistical — time and bandwidth spent on downloads that go nowhere. Fix the underlying condition once, and the same update that failed five times will typically sail through on the next attempt. There's one more habit worth building: whenever an update fails repeatedly, check Update history for the KB number before retrying. Knowing exactly which package is failing lets you jump straight to the manual Catalog download instead of burning through your data allowance on attempts that were never going to work. Technicians always identify the package first and retry second — it's faster, cheaper on metered connections, and it turns a mysterious failure into a concrete task with a concrete package. That single habit will save you more time across future update problems than any other trick in this guide.

## Why this happens

- **A metered connection limiting transfers.** Windows throttles or pauses large downloads on metered networks.
- **Unstable Wi-Fi or VPN drops.** Interruptions mid-transfer leave partial, unverifiable fragments.
- **A corrupted download cache.** Failed fragments poison every subsequent retry.
- **Proxy server interference.** Misconfigured proxies break the download stream.
- **Antivirus scanning timeouts.** Real-time scanning of huge packages can stall the transfer.
- **Low disk space.** The package needs room to download and unpack.
- **Sleep mode during download.** The laptop sleeping mid-transfer kills it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the metered connection setting

The single most common cause, and a thirty-second check.

1. Go to **Settings > Network & internet > Wi-Fi**, click your network, and look at the **Metered connection** toggle.
2. On home broadband, turn it **off**; Windows restricts update downloads while it's on.
3. On genuinely limited data, keep it on but move to unmetered Wi-Fi before updating.
4. For persistent metered-connection weirdness, see our dedicated guide on [fixing metered connections blocking Windows Update](/articles/best-way-to-fix-metered-connection-blocking-windows-update/).

### Fix 2: Give the download a stable path

Eliminate the transient network causes.

1. Disconnect any VPN and retry — a flaky tunnel is a classic download killer.
2. If you're on Wi-Fi, move closer to the router or plug in Ethernet for the download.
3. Set the laptop to stay awake: **Settings > System > Power & battery**, and set screen and sleep to generous timeouts while plugged in.
4. Click **Retry** in Windows Update; many one-off 0x80240034 errors clear on a clean attempt.

### Fix 3: Clear disk space for the download

Check the landing zone before blaming the network.

1. Open **Settings > System > Storage**; cumulative updates want several gigabytes of free space on C:.
2. Run Disk Cleanup with **Clean up system files** and clear Windows Update Cleanup, temporary files, and delivery optimization files.
3. Uninstall large unused apps and empty the Recycle Bin.
4. Retry the download with comfortable headroom.

### Fix 4: Reset the SoftwareDistribution cache

Break the retry loop by deleting the poisoned fragments.

1. In an administrator Command Prompt: `net stop wuauserv` and `net stop bits`.
2. Rename the folder: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
3. Restart the services: `net start wuauserv` and `net start bits`.
4. Run **Check for updates**; the download starts completely fresh with nothing stale to trip over.

### Fix 5: Check proxy and Delivery Optimization settings

Misrouted traffic fails the same way a dead connection does.

1. Open **Settings > Network & internet > Proxy** and make sure **Use a proxy server** is off unless you genuinely need one.
2. Go to **Settings > Windows Update > Advanced options > Delivery Optimization** and try toggling **Allow downloads from other PCs** off temporarily.
3. Run the **Windows Update** troubleshooter at **Settings > System > Troubleshoot > Other troubleshooters** to repair the transfer services.
4. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) has more on these network-related failures.

### Fix 6: Fetch the package manually

When the automatic downloader keeps failing, sidestep it.

1. Note the failing KB number from **Settings > Windows Update > Update history**.
2. Download the x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) — on another PC and a USB drive if your connection is the problem.
3. Run the installer on the affected laptop; it verifies the package before installing.
4. Confirm the KB shows as installed in Update history, then run a normal update check.

### Fix 7: Tune Delivery Optimization for unreliable connections

Windows' peer-to-peer update sharing can hurt more than it helps on flaky networks.

1. Open **Settings > Windows Update > Advanced options > Delivery Optimization**.
2. Turn **Allow downloads from other PCs** off temporarily — on unstable connections, peer chunks add failure points.
3. Retry the update with Microsoft's servers as the sole source.
4. If the download now completes, leave peer downloads off; you lose nothing except a little download speed in ideal conditions.

## Closing

Error 0x80240034 is a logistics problem — the package never arrived intact — so connection checks and a cache reset fix it far more often than system repairs do. For HP-specific angles like Support Assistant bandwidth contention, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80240034-on-hp-laptop/), and if Windows can't even reach the update servers, the [0x8024402C step-by-step guide](/articles/how-to-fix-windows-update-error-0x8024402c-step-by-step/) addresses that distinct failure.
