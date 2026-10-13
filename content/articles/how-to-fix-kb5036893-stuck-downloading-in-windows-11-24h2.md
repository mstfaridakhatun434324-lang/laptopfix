---
title: "How to Fix KB5036893 Stuck Downloading on Windows 11 24H2"
slug: how-to-fix-kb5036893-stuck-downloading-in-windows-11-24h2
date: 2026-09-05
categories: ["windows-update"]
tags: ["kb5036893", "stuck downloading", "windows 11 24h2", "cumulative update"]
description: "KB5036893 won't finish downloading on Windows 11 24H2? Here is how to unstick it, from quick network fixes to a manual install."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-in-windows-11-24h2.webp"
faqs:
  - q: "What is KB5036893?"
    a: "KB5036893 is a cumulative update package for Windows 11 that bundles security fixes, quality improvements, and reliability patches. Like all cumulative updates, it includes everything since the last baseline, which is why the download is large and why a failed attempt can leave the update stuck in the download phase."
  - q: "How long should the download take?"
    a: "On a normal broadband connection, a cumulative update download should finish within 30 minutes to an hour. If the progress percentage has not moved for over two hours while your internet works fine for everything else, the download is genuinely stuck and needs intervention rather than more patience."
  - q: "Is it safe to stop a stuck download?"
    a: "Yes, stopping a download is safe. Windows only installs the package after the full file is downloaded and verified. Interrupting the download does not harm the system; at worst you delete a partial file and start over, which is exactly what the fixes below do in a controlled way."
  - q: "Should I install this update manually from the Catalog?"
    a: "Yes, if the automatic download keeps stalling. The Microsoft Update Catalog hosts the same signed package, and installing it locally bypasses whatever is failing in the download pipeline. Match the package to your architecture and Windows build before running it."
---

KB5036893 is one of those cumulative updates that should download quietly in the background and then ask for a restart. On some Windows 11 24H2 laptops, though, it parks itself at a fixed percentage — 0%, 37%, 100% — and never moves. The progress bar becomes decoration, and every "Retry" click just puts you back in the same spot. It is frustrating because the update contains real security fixes you should not skip, but the download pipeline is the thing that is broken, not the update itself.

Part of the problem is the sheer size of what is being downloaded. Cumulative updates for 24H2 are large packages — often approaching a gigabyte — because each one carries the full set of fixes since the last baseline, not just the newest changes. On laptops, where connections drop when the lid closes and power plans throttle background activity, a download of that size has many chances to corrupt a chunk or lose its place. Windows is supposed to resume cleanly from partial downloads, but when the cached chunks themselves are damaged, every retry stalls at exactly the same point, which is the signature symptom you are seeing.

This guide walks through the full recovery path for a stuck KB5036893 download, ordered from fastest to most decisive. Work down the list until the update either downloads normally or you install it by hand.

## Why this happens

- **Corrupted partial download.** An interrupted or errored download leaves a partial file in the cache that Windows keeps trying to resume from instead of restarting cleanly.
- **SoftwareDistribution folder corruption.** The update cache that holds pending downloads can become inconsistent, freezing every download that touches it.
- **Metered connection or Delivery Optimization throttle.** Windows deliberately limits download speed or pauses entirely on connections it considers metered or constrained.
- **VPN or proxy interference.** Corporate VPNs, ad-blocking proxies, and misconfigured system proxies can break the connection to Microsoft's update servers mid-download.
- **Insufficient disk space for staging.** Cumulative updates need several gigabytes of staging room. If C: is nearly full, the download stalls silently.
- **Conflicting third-party antivirus or firewall.** Overzealous security software can quarantine or block chunks of the update payload as it arrives.
- **Pending servicing stack update.** Some cumulative updates depend on a servicing stack update being installed first; without it, the package cannot even be accepted.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is stuck, not just slow

Cumulative update downloads are large and can legitimately look stalled, especially on 24H2 where the package includes months of accumulated fixes. Do not start deleting caches until you have proof the download is genuinely frozen rather than merely slow.

1. Open **Settings** > **Windows Update** and note the exact percentage. Wait 30 minutes and check again — zero movement means stuck.
2. Test your internet separately: load a video or run a speed test. If the connection is fine, the problem is the update pipeline.
3. Check disk space: open **Settings** > **System** > **Storage** and confirm at least 10 GB free on the system drive.

### Fix 2: Pause and resume the update

A simple pause flushes the download state and often clears transient stalls.

1. In **Settings** > **Windows Update**, click **Pause updates** and set it to pause for 1 week.
2. Restart the laptop.
3. Return to Windows Update, click **Resume updates**, and click **Check for updates**. The download restarts from scratch instead of resuming a broken partial file.

### Fix 3: Disable metered connection and VPN

Windows will not download aggressively on connections it thinks are limited.

1. Open **Settings** > **Network & internet** > **Wi-Fi** (or Ethernet), select your connection, and turn off **Metered connection**.
2. Disconnect any VPN completely — do not just minimize it — and retry the download.
3. If you use a system-wide proxy or ad-blocker at the network level, temporarily disable it for the update.

### Fix 4: Reset the update cache

This is the classic fix and resolves the majority of stuck downloads.

1. Open **Command Prompt as administrator**.
2. Stop the services:
   ```
   net stop wuauserv
   net stop bits
   ```
3. Delete the contents of the download cache:
   ```
   rd /s /q C:\Windows\SoftwareDistribution\Download
   ```
4. Restart the services with `net start wuauserv` and `net start bits`.
5. Click **Check for updates**. KB5036893 now downloads fresh. Our walkthrough on [resetting stuck update components](/articles/how-to-fix-kb5041585-stuck-at-downloading-on-dell-laptop/) shows the same procedure in more detail if you want a second reference.

### Fix 5: Run the Windows Update troubleshooter

Let Microsoft's own diagnostic check for broken update components.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Windows Update** and apply any fixes it suggests.
3. Restart and retry the download. The troubleshooter handles common issues like missing services and broken registrations automatically.

### Fix 6: Install KB5036893 manually from the Update Catalog

If the automatic pipeline will not cooperate, sidestep it entirely.

1. Visit [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for **KB5036893**.
2. Choose the package matching your system (most laptops are x64) and click **Download**.
3. Run the `.msu` file and follow the installer. This installs the exact same signed update without touching the broken download cache.
4. Restart when prompted. For the full manual-install procedure, see [how to install a KB update manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/).

### Fix 7: Install the servicing stack update first

Sometimes the cumulative update cannot download properly because its prerequisite is missing.

1. In the [Update Catalog](https://www.catalog.update.microsoft.com/), search for the latest **servicing stack update** for Windows 11 24H2.
2. Install it manually, restart, then retry KB5036893 through Windows Update.
3. If the download still stalls after this, consider an in-place repair install using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), which refreshes the entire servicing stack.

## Closing

A stuck KB5036893 download is almost always a broken download pipeline rather than a bad update: a corrupted cache, a metered connection, or a confused resume state. Clearing the cache and retrying fixes most cases, and the Update Catalog manual install is the reliable escape hatch for the rest. Either way, get the update installed — skipping cumulative updates leaves known security issues unpatched, and a clean install through one of these paths gets you back on track.
