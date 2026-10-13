---
title: "KB5041585 Stuck at Downloading? A Step-by-Step Unstick Guide"
slug: how-to-fix-kb5041585-stuck-at-downloading-step-by-step
date: 2026-09-08
categories: ["windows-update"]
tags: ["kb5041585", "download stuck", "step by step", "windows update", "windows 11"]
description: "Step-by-step recovery for KB5041585 stuck at downloading: verify, unblock the network, repair BITS, reset the cache, and install."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-step-by-step.webp"
faqs:
  - q: "How do I know the download is truly stuck and not just slow?"
    a: "Watch the percentage for 15 minutes. Genuine progress moves, however slowly; a stuck download does not move a single percent. Also check Task Manager's network graph — a healthy download shows sustained traffic, while a stuck one shows near-zero activity. Note the exact percentage before each fix attempt so you can measure whether the next step actually moved it."
  - q: "Will restarting my laptop lose the partial download?"
    a: "No. BITS resumes partial downloads from where they stopped, so a restart is safe. In fact, restarting is one of the simplest ways to unstick a wedged download queue, since it restarts the BITS service cleanly. BITS is designed for interrupted transfers and resumes from the last verified chunk, so restarts are always safe during downloads."
  - q: "What is BITS and why does it matter here?"
    a: "BITS, the Background Intelligent Transfer Service, is the component that downloads updates in the background using idle bandwidth. When its job queue wedges or its state corrupts, update downloads freeze — and repairing BITS is the core of most download-stuck fixes."
  - q: "Can I just download the update myself instead?"
    a: "Yes. The Microsoft Update Catalog offers the standalone KB5041585 package, which installs without using the Windows Update download pipeline at all. It is the fastest escape hatch when the automated download will not cooperate. It is the fastest escape hatch in this entire guide when the automated download refuses to cooperate after the pipeline repairs."
---

This is the slow, careful, miss-nothing version of the KB5041585 download-stuck fix. Each step has a checkpoint: you verify the result before moving on, so you always know whether you are progressing or need to try the next approach. No step assumes the previous one worked — that is the whole point of a step-by-step guide.

Set aside about thirty minutes. Keep the laptop plugged in and connected to a stable network throughout.

A quick orientation on how to use this guide: every fix ends with a checkpoint — a concrete thing to observe that tells you whether that fix worked. Do not skip checkpoints. The most common mistake with stuck downloads is applying five fixes at once and never learning which one mattered, which means the next stuck download starts the guessing all over again. Work one fix, check the percentage, then move on.

## Why this happens

- **BITS job queue wedged:** The background transfer service's queue can wedge on a bad job, freezing all update downloads behind it.
- **Corrupted cache chunks:** Partially downloaded data that fails integrity checks gets re-requested forever.
- **Network interference:** VPNs, proxies, and filtering tools break the specific HTTP range requests BITS depends on.
- **Metered connection flags:** A metered flag tells Windows to hold or trickle the download.
- **Service dependency failures:** BITS depends on other services; if one fails, downloads silently stop.
- **Antivirus stream interception:** Web shields that proxy traffic can stall the long-lived BITS connections.
- **Regional delivery issues:** Occasionally the content delivery network itself is slow or inconsistent for your region.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall with Task Manager

1. Open **Settings > Windows Update** and note the exact download percentage of KB5041585.
2. Open **Task Manager > Performance > Wi-Fi/Ethernet** and watch the throughput graph for two minutes.
3. Checkpoint: sustained traffic means it is slow, not stuck — give it time. Near-zero traffic with an unmoving percentage means a genuine stall — continue.
4. Write down the percentage; you will compare against it after each fix to measure progress.

### Fix 2: Simple restart and pause-resume cycle

1. In **Settings > Windows Update**, click **Pause for 1 week**, wait one full minute, then click **Resume updates**.
2. Checkpoint: if the percentage moves within five minutes, the stall is cleared — let it finish.
3. If nothing changes, restart the laptop normally (Start > Power > Restart).
4. After the reboot, check the percentage again before proceeding — restarts alone unstick a surprising number of BITS queues.

### Fix 3: Remove network interference

1. Disconnect any VPN completely and close its client.
2. Go to **Settings > Network & internet**, open your connection properties, and set **Metered connection** to **Off**.
3. Temporarily disable third-party firewall network filtering and "game booster" tools.
4. Checkpoint: retry the download for ten minutes. If it moves, re-enable your tools one at a time afterward to identify the culprit — the [metered-connection guide](/articles/best-way-to-fix-metered-connection-blocking-windows-update/) covers persistent cases.

### Fix 4: Restart the transfer services cleanly

1. Open an elevated Command Prompt.
2. Run, in order: `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`, `net stop msiserver`.
3. Wait fifteen seconds, then run: `net start cryptSvc`, `net start bits`, `net start wuauserv`, `net start msiserver`.
4. Checkpoint: open `services.msc` and confirm all four show **Running**. Then check for updates and watch the percentage for ten minutes.

### Fix 5: Reset the download cache

1. With services stopped (repeat Fix 4's stop commands), rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
2. Rename `C:\Windows\System32\catroot2` to `catroot2.old`.
3. Restart the four services and click **Check for updates** — KB5041585 starts downloading from zero.
4. Checkpoint: the percentage should begin moving within ten minutes on a healthy connection. A fresh cache eliminates corrupted-chunk loops permanently.

### Fix 6: Reset the network stack

1. In an elevated Command Prompt, run `netsh winsock reset`, then `netsh int ip reset`, then `ipconfig /flushdns`.
2. Restart the laptop — these commands require a reboot to take effect.
3. After rebooting, retry the download before reconnecting the VPN or re-enabling filters.
4. Checkpoint: if downloads now work but were broken before, the network stack was the root cause — leave the interfering tool disabled until you have configured a proper exclusion.

### Fix 7: Bypass the pipeline with a manual install

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), search **KB5041585**, and download the x64 package.
2. Run the installer and let it complete — it does not use BITS or the download cache at all.
3. Checkpoint: **Settings > Windows Update > Update history** should show KB5034441 replaced by KB5041585 as successfully installed (check the KB number matches).
4. Run **Check for updates** afterward to confirm the pipeline considers the system current. If future updates also stall, treat the delivery pipeline as systemically ill and work the network-side fixes again — and make sure [driver updates](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) are not queuing behind the same blockage.

### Fix 8: Tune Delivery Optimization for stuck downloads

1. Open **Settings > Windows Update > Advanced options > Delivery Optimization** and check whether **Allow downloads from other PCs** is enabled.
2. If it is, try toggling it **Off** temporarily — peer-to-peer chunks from other machines on your network occasionally deliver corrupt data that fails verification and restarts the download.
3. Also click **Advanced options** inside Delivery Optimization and confirm no bandwidth limit is set absurdly low (a 5% background cap on a slow link looks exactly like a stuck download).
4. Checkpoint: retry the download after these changes. Delivery Optimization misconfiguration is a quiet cause of stalls that survives every BITS and cache reset because it sits in a different subsystem.

## Closing

Step by step, checkpoint by checkpoint: verify the stall, restart, clear interference, restart services, reset the cache, reset the network, install manually. One of these steps moves the percentage — and the checkpoint tells you which one, so you also learn what was wrong. That is the difference between fixing it and merely working around it.
