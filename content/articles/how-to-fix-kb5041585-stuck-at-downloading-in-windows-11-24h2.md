---
title: "KB5041585 Stuck at Downloading in Windows 11 24H2? Fix It"
slug: how-to-fix-kb5041585-stuck-at-downloading-in-windows-11-24h2
date: 2026-09-27
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "windows 11 24h2", "cumulative update", "update cache"]
description: "KB5041585 frozen at 0% or a fixed percentage in Windows 11 24H2? Fix the stuck download with cache resets, manual catalog install, and delivery optimization tweaks."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-in-windows-11-24h2.webp"
faqs:
  - q: "Why does KB5041585 get stuck at downloading?"
    a: "The usual cause is a corrupted partial download in the SoftwareDistribution cache — the update engine keeps retrying the same broken segments. Network interruptions, aggressive antivirus scanning of the download, metered-connection throttling, and corrupted BITS queue entries also freeze progress. Clearing the cache and letting the download start fresh resolves the large majority of these stalls."
  - q: "Can I install KB5041585 manually instead of through Windows Update?"
    a: "Yes. The Microsoft Update Catalog hosts the standalone installer package for the KB, which you can download and run directly. This bypasses the Windows Update download engine entirely and is the standard technician workaround for a stubbornly stuck download. Just make sure you download the package matching your system architecture, which is x64 for nearly all modern laptops."
  - q: "How long should I wait before deciding the download is stuck?"
    a: "Give it at least an hour on a normal broadband connection, longer on slow connections. Cumulative updates are large — often several hundred megabytes — and the progress bar is not perfectly linear, so it can sit at one percentage for a long time legitimately. If it has not moved a single percent in over an hour with an active connection, treat it as stuck."
  - q: "Will clearing the update cache delete anything important?"
    a: "No. The SoftwareDistribution folder holds only downloaded update files and the update history database — no personal data, no installed programs, no settings. Renaming it forces Windows to rebuild it fresh on the next update check. Your update history display will reset, but that is cosmetic and harmless."
---

Cumulative update KB5041585 sits in Windows Update at 0%, or 7%, or 100% — and does not move. Hours pass, the percentage is frozen, and restarting the download just lands you back at the same stuck number. This is one of the most reported Windows 11 24H2 update behaviors, and it is almost never a problem with the update itself.
The download engine is the culprit. Windows Update downloads in segments through the Background Intelligent Transfer Service, and when a segment corrupts — through a network hiccup, an antivirus scan locking the file, or a damaged cache — the engine retries the broken segment forever instead of starting over. The progress bar freezes because the engine is stuck in that retry loop, not because your connection is slow.
The fixes below break the loop: verify the stall, reset the download machinery, rule out network and antivirus interference, and — the reliable fallback — install the KB manually from the catalog. You can grab the standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) by searching the KB number. If the update installs but the machine then misbehaves, the [black-screen-after-update fix](/articles/windows-11-black-screen-after-update-fix/) is the next stop, and the [troubleshooter guide](/articles/how-to-fix-windows-update-with-troubleshooter-on-windows-11/) covers the automated repair path.

## Why this happens

- **A corrupted partial download.** Broken segments in the cache make the engine retry the same data endlessly.
- **BITS queue corruption.** The Background Intelligent Transfer Service holds a stuck job that blocks the queue.
- **Antivirus scanning the download.** Real-time protection locks partial files and interrupts the segment writes.
- **Metered connection throttling.** Windows pauses or crawls downloads on connections marked as metered.
- **Delivery Optimization conflicts.** Peer-to-peer download sources can feed corrupted segments.
- **DNS or network instability.** Flaky connections corrupt segments faster than the engine can verify them.
- **Insufficient disk space.** The download cannot complete staging when the drive is nearly full.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall and rule out slow progress

Cumulative updates are large and the progress bar is non-linear. Confirm a genuine stall before resetting anything.

1. Note the exact percentage and the time, then wait a full hour on broadband.
2. Open Task Manager > Performance > Wi-Fi or Ethernet and confirm whether data is actually flowing.
3. If data is flowing steadily, the download is working — keep waiting.
4. If zero data flows for an hour with an unchanged percentage, proceed.

### Fix 2: Restart the update services

A simple service restart clears transient BITS and update-engine hangs without touching any files.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`.
3. Wait 30 seconds, then run `net start wuauserv` and `net start bits`.
4. Go to Settings > Windows Update and click Retry on the stuck update.

### Fix 3: Reset the download cache completely

This is the core fix: it deletes the corrupted partial download and forces the engine to fetch every segment fresh.

1. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Reboot, then check for updates and watch the download start from zero — that is expected.

### Fix 4: Disable metered connection and Delivery Optimization

Two Windows features can silently throttle or corrupt the download. Rule both out.

1. Go to Settings > Network & internet > Wi-Fi, open your network, and turn off the metered connection toggle.
2. Go to Settings > Windows Update > Advanced options > Delivery Optimization and turn it off temporarily.
3. Restart the download and observe whether progress resumes normally.
4. Re-enable Delivery Optimization afterward if you prefer it on.

### Fix 5: Temporarily disable antivirus during the download

Real-time scanning of multi-hundred-megabyte update files is a documented stall source. A brief disable isolates it.

1. Temporarily disable third-party antivirus real-time protection, keeping Windows Defender active.
2. Retry the KB5041585 download with protection paused.
3. If it completes, add the SoftwareDistribution folder to your antivirus exclusions for future updates.
4. Re-enable full protection immediately after the download finishes.

### Fix 6: Install the KB manually from the Update Catalog

When the download engine will not cooperate, bypass it. The standalone installer does not use the segment-download machinery at all.

1. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for KB5041585.
2. Download the package matching your architecture — x64 for virtually all modern laptops.
3. Run the .msu file as administrator and let it install; reboot when prompted.
4. Verify in Settings > Windows Update > Update history that the KB shows as installed.

### Fix 7: Free disk space and check the drive

A nearly full drive stalls staging, and a failing drive corrupts segments. Check both before the final retry.

1. Confirm at least 20 GB free on C: via Settings > System > Storage.
2. Run Disk Cleanup with system files selected to clear update leftovers.
3. If stalls recur across many updates, check drive health with the manufacturer's diagnostic.
4. Consult the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) for persistent download failures.

### Fix 8: Stabilize the network for large downloads

Cumulative updates are hundreds of megabytes delivered in segments, and an unstable connection corrupts segments faster than the engine can verify them. If KB5041585 repeatedly stalls at the same point, the network path — not Windows — may be the problem. A short stabilization pass before the next download attempt pays off.

1. Switch to a wired Ethernet connection for the download if possible; it eliminates Wi-Fi dropouts entirely.
2. Restart your router and modem, then wait two minutes before reconnecting.
3. Temporarily disconnect VPNs and proxy tools during the download — they interfere with segment verification.
4. In an elevated Command Prompt, run `ipconfig /flushdns` to clear stale DNS entries, then retry the download.

## Closing

A KB stuck at downloading is a download-engine problem, not a bad update. Verify the stall, reset the cache, rule out metering and antivirus interference, and use the manual catalog install when the engine will not cooperate. The standalone package exists precisely for this situation — there is no prize for making the automatic download work when the manual one takes five minutes.
