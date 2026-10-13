---
title: "Windows Update Taking Too Long on an ASUS Laptop? How to Speed It Up"
slug: how-to-fix-windows-update-taking-too-long-on-asus-laptop
date: 2026-09-23
categories: ["windows-update"]
tags: ["slow update", "asus laptop", "windows update", "taking too long"]
description: "Windows Update drags on your ASUS laptop? Find what's slowing it down and make updates finish in a reasonable time."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-on-asus-laptop.webp"
faqs:
  - q: "How long should Windows updates take on an ASUS laptop?"
    a: "A monthly cumulative update should take 15 to 45 minutes on an ASUS laptop with an SSD, including the restart. A feature update takes 45 to 90 minutes. If a routine cumulative update exceeds three hours with no visible progress, treat it as stuck rather than slow and work through the fixes below."
  - q: "Do MyASUS and Armoury Crate slow down Windows Update?"
    a: "They can. When ASUS's utilities scan for or install drivers at the same time Windows Update runs, the two systems contend over the same driver packages, duplicating evaluation work and occasionally conflicting over which version wins. Pausing MyASUS and Armoury Crate automatic updates while Windows Update runs removes the contention and usually produces a noticeable speedup."
  - q: "Why is the download phase so slow on my ASUS?"
    a: "Slow downloads are usually network-related rather than ASUS-related: metered connection throttling, Delivery Optimization misconfiguration, or a congested connection. The install phase is where ASUS-specific factors like driver contention and slow storage matter most, so diagnose by phase — fix the network for slow downloads, and quiet ASUS's utilities and clean the cache for slow installs."
  - q: "Is it safe to leave a slow update running overnight?"
    a: "Yes, and it is often the smartest move. Plug in the charger, set active hours to cover your sleep, and let the update grind through the night. Forcing a shutdown on a working update risks corruption; patience with AC power connected is always the safer choice."
---

ASUS laptops span everything from featherweight ultrabooks to desktop-replacement gaming rigs, but they share a common complaint: Windows Update sometimes takes far longer than it should. The causes split into two groups — the generic ones that slow updates on any laptop, and the ASUS-specific ones: MyASUS and Armoury Crate contending with Windows Update, and the eMMC or budget SSD storage in entry-level ASUS models that turns update file operations into an endurance event.

The storage factor deserves emphasis because it is the hardest limit in the system. An update performs tens of thousands of small random reads and writes as it verifies, stages, and replaces files — precisely the workload where eMMC and budget flash perform worst, sometimes an order of magnitude slower than a decent SSD. No amount of cache cleaning changes the physics of the storage; it only removes the avoidable overhead sitting on top of it. That is why this guide separates the two: fix everything fixable first, then make an honest assessment of whether the remaining slowness is the hardware telling you its limits.

This guide separates "slow but working" from "actually stuck," then speeds things up in priority order.

## Why this happens

- **ASUS utility contention.** MyASUS and Armoury Crate driver checks running alongside Windows Update duplicate driver evaluation work.
- **Slow storage.** eMMC or budget SSDs in entry-level ASUS models make the thousands of small file operations in an update painfully slow.
- **Bloated update cache.** Accumulated cache data forces the engine to verify more than necessary.
- **Nearly full drive.** Low free space cramps the staging areas updates need.
- **Metered or throttled network.** The download phase stretches when Windows limits transfer speed.
- **Update backlog.** Multiple pending updates install sequentially, multiplying total time.
- **Antivirus overhead.** Real-time scanning of every update file operation adds significant time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is slow, not stuck

Do not interrupt working updates.

1. Open Task Manager and check disk activity. Sustained disk I/O means the update is working.
2. Identify the phase: slow downloading is a network issue; slow installing is disk, CPU, or contention; slow on the blue "working on updates" screen is the servicing engine.
3. Allow at least two hours for a cumulative update on budget ASUS hardware before calling it stuck.

### Fix 2: Quiet MyASUS and Armoury Crate

Remove the ASUS-specific contention. MyASUS and Armoury Crate both run background services that periodically scan for driver updates, and when those scans coincide with Windows Update's own driver evaluation, the two systems duplicate each other's work and can lock the same files. Quieting them is not about disabling useful tools permanently — it is about giving Windows Update an uncontested window to finish, after which you can re-enable everything.

1. Open **MyASUS** and pause automatic driver and system updates.
2. In **Armoury Crate**, disable automatic update checks temporarily.
3. Run Windows Update with ASUS's tools silent. This alone noticeably speeds updates on machines where both systems were fighting over drivers.

### Fix 3: Clean the cache and temporary files

Reduce the work the engine must do.

1. Run **Disk Cleanup** as administrator with **Clean up system files**, selecting **Windows Update Cleanup**, **Temporary files**, and **Delivery Optimization Files**.
2. Reset the update cache from an elevated Command Prompt:
   ```
   net stop wuauserv
   net stop bits
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   net start wuauserv
   net start bits
   ```
3. The full component reset is documented in [our update engine repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).

### Fix 4: Free up disk space

Give the installer elbow room.

1. Target at least 20 GB free on C: — check in **Settings** > **System** > **Storage**.
2. On ASUS laptops with small eMMC storage, this is often the entire problem: move personal files to external storage or the cloud.
3. Run `powercfg /h off` in an elevated prompt to reclaim hibernation file space if you are critically short.

### Fix 5: Speed up the download phase

Fix the network side.

1. In **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization**, enable downloads from other PCs on your local network.
2. Disable **Metered connection** for your network in **Settings** > **Network & internet**.
3. For very slow downloads, [install the update manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/) — one browser download is often faster than the engine's throttled transfer.

### Fix 6: Update ASUS drivers from ASUS first

Pre-empt the driver evaluation slowdown.

1. Get the latest chipset, storage, and wireless drivers for your exact model from ASUS support and install them.
2. Restart, then run Windows Update. With ASUS's drivers current, the engine stops its lengthy driver re-evaluation.
3. Keep ASUS's utilities updated too — old versions of MyASUS are themselves a source of contention.

### Fix 7: Schedule around the slowness

When the hardware is simply slow, manage the timing.

1. Set **Active hours** in Windows Update to cover your waking hours so restarts and heavy phases happen overnight.
2. Plug in the charger and let long updates run while you sleep — safe and stress-free.
3. For persistent slowness issues, [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents expected durations and the official diagnostic path.

## Closing

Slow updates on ASUS laptops come down to contention and storage: quiet MyASUS and Armoury Crate while Windows Update works, clean the cache, free the space, and get ASUS's drivers current beforehand. On entry-level models with eMMC storage, accept that updates are an overnight activity and schedule them that way. The goal is not to make a slow drive fast — it is to remove every avoidable slowdown so the hardware only does the work it must. Revisit this checklist twice a year: caches re-bloat, drives re-fill, and utilities re-enable their automatic checks after their own updates. Ten minutes of maintenance every few months keeps update times from creeping back up. Small, regular maintenance beats heroic rescue efforts every time.
