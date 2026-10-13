---
title: "How to Limit OneDrive Sync Bandwidth on Windows 10"
slug: how-to-limit-onedrive-sync-on-windows-10
date: 2026-09-15
categories: ["performance"]
tags: ["onedrive", "sync", "bandwidth", "windows 10", "upload limit"]
description: "OneDrive hogging your upload bandwidth and slowing everything down? Here's how to cap its sync speed, pause syncing, and choose exactly which folders sync."
thumbnail: "/images/thumbs/how-to-limit-onedrive-sync-on-windows-10.webp"
faqs:
  - q: "Why does OneDrive slow down my internet?"
    a: "OneDrive syncs files in both directions, and uploads are the problem — most home connections have far less upload bandwidth than download. When OneDrive uploads large files or a batch of changes, it can saturate your entire upload pipe, which makes web browsing, video calls, and gaming laggy even though downloads are unaffected."
  - q: "Will limiting OneDrive bandwidth break syncing?"
    a: "No. Bandwidth limits only slow the transfer rate; every file still syncs completely and correctly, just more gradually in the background. It's the recommended approach when OneDrive competes with other internet activity — your files stay fully in sync without choking your connection, and you can adjust the cap anytime."
  - q: "What's the difference between pausing sync and limiting bandwidth?"
    a: "Pausing stops all sync activity for a set time (2, 8, or 24 hours) — nothing uploads or downloads until you resume. Bandwidth limiting keeps syncing active but caps the speed, so files trickle through in the background. Use pausing for video calls and gaming sessions; use bandwidth limits as a permanent everyday setting."
  - q: "Can I stop specific folders from syncing?"
    a: "Yes, with selective sync. In OneDrive settings under the Account tab, click Choose folders to pick exactly which cloud folders download to your PC. Unchecked folders stay in the cloud only. Combined with Files On-Demand, this dramatically reduces both bandwidth use and local disk usage."
---

OneDrive is quietly one of the biggest bandwidth consumers on a Windows 10 laptop. Every photo you save, every document you edit, every screenshot you take gets uploaded to the cloud — and because most home internet connections have limited upload speed, OneDrive can saturate your entire upstream pipe. The result: web pages load slowly, video calls stutter, games lag, and everything feels broken, all while OneDrive happily churns away in the background.

The frustrating part is that OneDrive gives no warning. There's no "I'm using all your bandwidth" notification; you just notice that the internet feels terrible at random times. Once you know to look at the OneDrive cloud icon in the taskbar (spinning arrows mean it's actively syncing), the pattern becomes obvious. Fortunately, OneDrive has built-in controls for exactly this: bandwidth caps, scheduled pauses, and selective folder sync. This guide walks through all of them.

These settings persist across restarts, so a few minutes of configuration gives you permanent relief. And nothing here risks your files — limiting bandwidth only changes transfer speed, never completeness.

## Why this happens

- **Unlimited upload by default**: OneDrive uses as much bandwidth as it can by default, with no cap — on a 10 Mbps upload connection, that's the entire pipe.
- **Large files and photo libraries**: A single video file or a batch of high-resolution photos can mean gigabytes of uploading.
- **Frequent small changes**: Auto-saved documents, synced app data, and screenshots create a constant trickle of uploads.
- **Initial sync after setup**: A new laptop or fresh OneDrive setup may need to upload or download your entire cloud library — tens of gigabytes.
- **Multiple devices syncing**: Changes made on your phone or another PC trigger downloads on the laptop too.
- **Files On-Demand disabled**: Without it, OneDrive downloads full copies of everything, multiplying bandwidth use.
- **Metered connection not set**: Windows doesn't automatically throttle OneDrive on connections it doesn't know are limited.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm OneDrive is the bandwidth hog

Before changing settings, verify OneDrive is actually the culprit and not something else on your network.

1. Click the **OneDrive cloud icon** in the taskbar (click the up arrow if it's hidden).
2. If it shows **syncing** with active file transfers, OneDrive is using bandwidth right now.
3. Open Task Manager (**Ctrl + Shift + Esc**), go to the **App history** or **Processes** tab, and check OneDrive's network usage.
4. Note whether the slowdown correlates with OneDrive's active syncing — if yes, proceed.

### Fix 2: Set upload and download rate limits

This is the core fix — a permanent cap that lets OneDrive sync politely in the background without choking your connection.

1. Click the **OneDrive icon** in the taskbar, then click the **gear icon > Settings**.
2. Go to the **Sync and backup** tab (or **Network** tab on older OneDrive versions).
3. Under **Upload rate** and **Download rate**, select **Limit to** and enter a value in KB/s.
4. A good starting point: cap upload at about **50-70% of your connection's upload speed**. If you have 10 Mbps upload (~1250 KB/s), set the limit to around 600-800 KB/s.
5. Click OK. The limit applies immediately.

Test your internet speed first (search "speed test" in your browser) so you know your actual upload bandwidth. Leave enough headroom for video calls and browsing.

### Fix 3: Pause syncing during important tasks

For video calls, gaming sessions, or big downloads, temporarily pausing OneDrive is faster than fiddling with limits.

1. Click the **OneDrive icon** in the taskbar.
2. Click the **gear icon > Pause syncing**.
3. Choose **2 hours**, **8 hours**, or **24 hours**.
4. OneDrive stops all transfers until the pause expires or you manually resume.
5. Remember to resume afterward — or just let the timer expire.

### Fix 4: Use selective sync to reduce what's synced

Fewer synced folders means less data moving in both directions. Most people sync folders they never actually need locally.

1. Open **OneDrive Settings** (gear icon > Settings).
2. Go to the **Account** tab and click **Choose folders**.
3. Uncheck folders you don't need on this laptop — they stay safe in the cloud.
4. Click OK. OneDrive removes the local copies of unchecked folders (cloud copies are untouched).

### Fix 5: Enable Files On-Demand

Files On-Demand is the single biggest bandwidth saver: files appear in Explorer but only download when you actually open them.

1. Open **OneDrive Settings > Sync and backup**.
2. Under **Files On-Demand**, make sure it's turned **on**.
3. In File Explorer, you'll see cloud icons: **cloud icon** = online-only (no bandwidth used until opened), **green checkmark** = downloaded.
4. Right-click any folder and choose **Free up space** to convert downloaded files back to online-only.

### Fix 6: Set your connection as metered

Windows treats metered connections gently — OneDrive pauses most sync activity on them automatically.

1. Open **Settings > Network & Internet > Wi-Fi** (or Ethernet).
2. Click your connected network.
3. Turn on **Set as metered connection**.
4. OneDrive will pause syncing while on this network (you can override per-session if needed).

This is ideal for mobile hotspots and slow hotel Wi-Fi. For more on managing OneDrive's background impact, see our guide on [how to limit OneDrive sync on Windows 11](/articles/how-to-limit-onedrive-sync-on-windows-11/).

### Fix 7: Manage startup and background behavior

If OneDrive's background presence itself bothers you, control when it runs.

1. In **OneDrive Settings > Settings tab**, uncheck **Start OneDrive automatically when I sign in** if you only want it on demand.
2. Alternatively, keep auto-start but rely on the bandwidth limits from Fix 2 — this is the better balance for most users.
3. To fully unlink (nuclear option): **Settings > Account > Unlink this PC**. Your cloud files stay safe; local files remain but stop syncing.

Our guide on [how to disable background apps on a laptop](/articles/how-to-disable-background-apps-on-laptop/) covers taming other background bandwidth users. Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) documents the current OneDrive settings if your interface looks different.

## Closing

OneDrive doesn't have to fight you for bandwidth. Set a sensible upload cap, enable Files On-Demand, trim your synced folders, and pause during important tasks — four changes that take five minutes and permanently end the "why is the internet slow" mystery whenever OneDrive decides to sync.
