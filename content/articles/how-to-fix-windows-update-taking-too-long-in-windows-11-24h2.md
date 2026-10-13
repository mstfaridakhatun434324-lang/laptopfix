---
title: "How to Fix Windows Update Taking Too Long in Windows 11 24H2"
slug: how-to-fix-windows-update-taking-too-long-in-windows-11-24h2
date: 2026-10-08
categories: ["windows-update"]
tags: ["windows 11 24h2 update slow", "windows update taking too long", "24h2 update speed", "speed up windows update"]
description: "Windows 11 24H2 updates taking hours? Learn to tell slow from stuck, then speed things up with cache resets, disk cleanup, and Delivery Optimization tuning."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-in-windows-11-24h2.webp"
faqs:
  - q: "How long should a Windows 11 24H2 update normally take?"
    a: "A monthly cumulative update typically takes 15 to 45 minutes on an SSD. A feature update to 24H2 can take 1 to 3 hours, longer on a hard drive. If a cumulative update exceeds 2 hours with no progress movement and no disk activity, treat it as stuck rather than slow and work through the fixes above."
  - q: "Why was my first 24H2 update so much slower than later ones?"
    a: "The first update under the checkpoint cumulative model does extra one-time work to establish the checkpoint baseline. Later monthly updates are smaller and faster because they build on those checkpoints. This is expected behavior, not a problem with your laptop."
  - q: "Does Delivery Optimization slow down my updates?"
    a: "It can. When it works, peer sharing speeds things up, but when it gets stuck re-requesting chunks from other PCs, downloads crawl. Restricting it to your local network or turning it off entirely is a quick test — if the update suddenly speeds up, you found the culprit."
  - q: "Will a slow update damage my laptop if I force a restart?"
    a: "Interrupting a working update risks corrupting the update cache, which makes the next attempt even slower. Only force a restart when you have confirmed zero disk activity for an extended period. A slow update is annoying; a corrupted one is worse."
---

Windows 11 24H2 updates have a reputation for taking longer than previous versions, and much of that is by design rather than a fault on your laptop. Version 24H2 introduced checkpoint cumulative updates, a new servicing model where each monthly update builds on checkpoints instead of replacing the whole payload. The first 24H2 update on a machine can be unusually large and slow, especially if the laptop skipped several months of updates. [a feature update parked at 61 percent](/articles/how-to-fix-feature-update-stuck-at-61-percent-step-by-step/)

That said, there is a line between slow and stuck. A monthly cumulative update on an SSD should finish within 30 to 60 minutes; a feature update to 24H2 can take 1 to 3 hours. If your laptop has been grinding for far longer than that with no progress movement, the causes below — from delivery optimization loops to a bloated update cache — are the usual suspects.

## Why this happens

- **Checkpoint update transition.** The first 24H2-era updates on a machine can be much larger than usual as the new checkpoint servicing model initializes.
- **Corrupted SoftwareDistribution cache.** The installer silently retries bad payload data, which looks like slowness rather than an error.
- **Nearly full system drive.** Staging needs working room; a drive over 90% full makes every phase dramatically slower.
- **Delivery Optimization peer loops.** The P2P sharing feature can get stuck re-requesting chunks from peers instead of Microsoft's servers.
- **Third-party antivirus scanning staged files.** Real-time scanning of every file the installer touches multiplies install time.
- **Spinning hard drive.** 24H2's larger payloads punish HDDs; what takes 30 minutes on an SSD can take 3+ hours on a hard drive.
- **Metered connection throttling.** Windows slows or pauses downloads on metered connections, stretching updates across hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is slow, not stuck

Check for real activity before intervening. Many 'stuck' 24H2 updates are just slow, and interrupting one causes the corruption people fear.

1. Open Task Manager (Ctrl + Shift + Esc) and look at disk usage by TiWorker.exe, SetupHost.exe, or TrustedInstaller.
2. Check the drive activity LED if your laptop has one.
3. If there is sustained activity, give a cumulative update 60 minutes and a feature update 3 hours.
4. Only proceed with repairs if activity is zero and progress is frozen.
5. Note the elapsed time so you can judge whether later fixes actually helped.

### Fix 2: Free up disk space

24H2 updates stage large payloads. Free space is the single biggest predictor of update speed on laptops with small SSDs.

1. Open Settings > System > Storage and review what is consuming space.
2. Run Disk Cleanup and remove temporary files, delivery optimization files, and previous Windows installations.
3. Uninstall apps you no longer use, starting with the largest.
4. Move photos and videos to cloud storage or an external drive.
5. Target at least 20 to 25 GB free on C: before retrying.

### Fix 3: Reset the Windows Update components

A bloated or corrupt cache is the most common fixable cause of slow updates. This clears it completely.

1. Open Command Prompt as administrator.
2. Stop the services: net stop wuauserv, net stop bits, net stop cryptsvc, net stop msiserver.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Rename C:\Windows\System32\catroot2 to catroot2.old.
5. Restart all four services with net start, then check for updates again.

### Fix 4: Tune Delivery Optimization

Delivery Optimization shares update chunks with PCs on your network and the internet. Limiting it often speeds up slow downloads.

1. Go to Settings > Windows Update > Advanced options > Delivery Optimization.
2. Turn off 'Allow downloads from other PCs' or restrict it to devices on your local network.
3. Under Advanced options, check that bandwidth limits are not set unusually low.
4. If downloads were crawling, retry the update and compare the speed.
5. You can re-enable peer sharing afterward if you prefer it.

### Fix 5: Check for a metered connection

Windows deliberately slows updates on metered connections. A connection wrongly flagged as metered stretches every update.

1. Go to Settings > Network & internet > Wi-Fi (or Ethernet) and open your connection properties.
2. If 'Metered connection' is on and you have unlimited data, turn it off.
3. Then go to Settings > Windows Update and make sure downloads are not paused.
4. Retry the update on the unmetered connection.
5. Leave metering on only for genuinely capped mobile hotspots.

### Fix 6: Temporarily disable third-party antivirus

Real-time scanners inspect every file the installer stages, which can double install times on 24H2's larger payloads.

1. Open your antivirus settings and disable real-time protection temporarily.
2. Do not browse untrusted sites while protection is off.
3. Run the update and observe whether it completes noticeably faster.
4. Re-enable protection immediately after the update finishes.
5. If speed improved dramatically, consider scheduling updates when the scanner can be paused.

### Fix 7: Install the latest servicing stack update

The servicing stack is the engine that installs updates; an outdated one works inefficiently on 24H2 payloads. [an update frozen on the restarting screen](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-lenovo-laptop/)

1. Check Settings > Windows Update > Update history for the servicing stack version.
2. Visit [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for the latest servicing stack update for Windows 11 24H2.
3. Download the .msu matching your architecture (usually x64) and install it.
4. Restart if prompted, then retry the main update.
5. Servicing stack updates are small and install quickly.

## Closing

Slow 24H2 updates are usually fixable rather than something to endure — a clean cache, free disk space, and a current servicing stack resolve the large majority of cases. Time your next update after applying these fixes; if a cumulative update still takes hours with a healthy cache and drive, the drive itself becomes the prime suspect. Related slow-update patterns are covered in [Windows Update stuck on downloading](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).
