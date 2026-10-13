---
title: "Windows Update Stuck Downloading? Reddit's Best Fixes, Tested"
slug: how-to-fix-windows-update-stuck-downloading-reddit
date: 2026-09-09
categories: ["windows-update"]
tags: ["stuck downloading", "windows update", "download stuck", "windows 11", "bits"]
description: "Update frozen at 0% or 47% for hours? These are the community-vetted fixes for Windows Update downloads that refuse to finish."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-reddit.webp"
faqs:
  - q: "How long is too long for a Windows Update download?"
    a: "On decent broadband, a cumulative update should download within 30 to 60 minutes. If the percentage has not moved for over two hours and Task Manager shows no network activity on the update process, the download is genuinely stuck. Feature updates are much larger and legitimately take longer, so give those three to four hours before intervening. The key test is always the same: no percentage movement plus no network activity equals stuck."
  - q: "Why does the download get stuck at the same percentage every time?"
    a: "A repeat stall at the same percentage almost always means a corrupted partial file in the download cache. Each retry resumes from the poisoned cache instead of starting fresh. Clearing the SoftwareDistribution download folder forces a clean re-download, which is why it is the most recommended fix in community threads."
  - q: "Can I use my laptop normally while an update downloads?"
    a: "Yes, light use is fine, but avoid heavy network activity like streaming or large downloads, which compete for bandwidth. Also avoid putting the laptop to sleep during the download. Heavy disk activity from gaming can also slow the staging process noticeably."
  - q: "Will restarting break a stuck download?"
    a: "No. Restarting during the download phase is completely safe — the worst case is that Windows discards the partial download and starts over from scratch. Unlike interrupting the installation phase, interrupting the download phase carries essentially no risk to your system or files. If a download is genuinely frozen with zero network activity, a restart is actually one of the reasonable first responses."
---

Few progress bars are as maddening as a Windows Update download frozen at 47% for three hours. Forum threads on this exact problem run to thousands of comments, and over the years the community has converged on a set of fixes that genuinely work. This guide distills those threads into an ordered sequence, skipping the folklore and keeping the fixes with real track records.

A stuck download is a delivery problem, not an installation problem. The package is not arriving intact, so the fixes target the cache, the connection, and the Background Intelligent Transfer Service that manages the transfer.


The single most useful diagnostic is Task Manager's network graph: open it, watch for a minute, and you will know whether the download is stuck or merely slow. Slow downloads with active transfer just need patience — possibly overnight for large feature updates. Only the fixes below apply to genuinely frozen transfers, so confirm the freeze first.
## Why this happens

- **Corrupted partial download:** A damaged chunk in the cache blocks all retries at the same point.
- **BITS wedged:** The Background Intelligent Transfer Service stalls and stops requesting data.
- **Bandwidth contention:** Other apps, cloud sync, or streaming starve the download.
- **Sleep interrupting the transfer:** The laptop dozes mid-download and the resume fails.
- **Metered connection:** Windows throttles or pauses the download on metered networks.
- **Antivirus scanning:** Real-time protection locks the growing download file.
- **Microsoft server issues:** Occasionally the problem is upstream, and patience is the fix.
- **Delivery Optimization peer issues:** Corrupted peer-to-peer chunks stalling the transfer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually stuck

1. Open **Task Manager > Performance > Wi-Fi or Ethernet** and watch for download activity.
2. Check the update percentage, wait 30 minutes, and check again.
3. No network activity plus no percentage movement for over an hour means stuck.
4. If data is flowing, leave it alone — slow is not stuck. Only proceed when you have confirmed the freeze.
5. Compare the network graph against the update percentage over two separate 30-minute windows.
6. Screenshot the frozen percentage as a baseline to measure later fixes against.

### Fix 2: Pause and resume the download

1. In **Settings > Windows Update**, click **Pause for 1 week**, then immediately click **Resume updates**.
2. This forces the update client to re-evaluate and often restarts a stalled transfer.
3. Watch the percentage for 15 minutes to see if it begins moving.
4. This is the lowest-effort fix in the community playbook and works surprisingly often.
5. After resuming, wait a full 15 minutes before judging — restarts can be slow to begin.
6. If pause-resume fails twice, move on; repeating it further rarely helps.

### Fix 3: Clear the download cache

1. Open an elevated Command Prompt and run `net stop wuauserv` and `net stop bits`.
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download` (the folder, not its parent).
3. Restart the services with `net start wuauserv` and `net start bits`.
4. Check for updates to trigger a fresh download. This is the single most upvoted fix across every thread on the topic.
5. Check the folder size before deleting — a zero-byte cache suggests a different problem than a multi-gigabyte one.
6. After restarting services, confirm new files begin appearing in the Download folder.

### Fix 4: Restart the BITS service properly

1. Press **Win + R**, type `services.msc`, and find **Background Intelligent Transfer Service**.
2. Set its Startup type to **Automatic (Delayed Start)** if it is not already.
3. Click **Restart**, then also restart the **Windows Update** service.
4. A wedged BITS is invisible in the UI but obvious in its effects; a clean restart restores the transfer engine. For the broader service repair, see our guide on [update errors after major system changes](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/).
5. In services.msc, verify BITS dependencies are also running correctly.
6. If BITS will not stay running, check the System event log for its error entries.

### Fix 5: Eliminate bandwidth competition

1. Pause cloud sync apps (OneDrive, Dropbox) during the download.
2. Close streaming, gaming, and large browser downloads.
3. Temporarily disable third-party antivirus real-time scanning, keeping Defender on.
4. Set the laptop to **Best performance** power mode and disable sleep in **Settings > System > Power & battery**.
5. Temporarily disconnect other devices from your network to rule out household congestion.
6. Schedule the retry for off-peak hours if your ISP throttles during the evening.

### Fix 6: Check the metered connection and network

1. Go to **Settings > Network & internet**, select your connection, and turn off **Metered connection**.
2. If on Wi-Fi, try wired Ethernet or phone USB tethering to rule out wireless flakiness.
3. Flush the DNS cache with `ipconfig /flushdns` in an elevated Command Prompt.
4. Retry the download and monitor Task Manager for real transfer activity.
5. Try forgetting and rejoining the Wi-Fi network to clear a stale connection profile.
6. If tethering works but Wi-Fi does not, the router or wireless driver is the real issue.

### Fix 7: Download from the Update Catalog instead

1. Find the KB number in **Settings > Windows Update > Update history**.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the x64 .msu.
3. Run the installer directly — your browser handles the download, bypassing BITS entirely.
4. This is the community's nuclear option and it essentially never fails. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) also endorses manual installation for stubborn updates.
5. Download the .msu with a download manager that supports resume for very large packages.
6. Verify the file's digital signature before running it to rule out a corrupted download.

## Closing

Stuck downloads are almost always a poisoned cache or a wedged transfer service, and the community has proven the fix order: verify, pause-resume, clear the cache, restart BITS, remove competition, and go manual as the finale. Once the package arrives intact, installation is usually smooth. If the failure moves to the install phase instead, our guide on [cumulative updates that fail to install](/articles/best-way-to-fix-cumulative-update-fails-to-install/) takes over from here. Once the package arrives, installation is usually uneventful — the download was the hard part. If you find yourself here monthly, consider the manual Catalog route as your default; it is faster than fighting the service.
