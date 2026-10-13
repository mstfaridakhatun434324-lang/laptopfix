---
title: "Windows 11 Slow After an Update? Fix the Sluggishness"
slug: how-to-fix-windows-11-slow-after-update-reddit
date: 2026-09-17
categories: ["performance"]
tags: ["windows 11 slow", "slow after update", "windows update", "performance", "reddit"]
description: "Windows 11 feeling sluggish after the latest update? Learn why updates slow laptops down and the community-tested fixes that restore speed."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-update-reddit.webp"
faqs:
  - q: "How long should I wait after an update before troubleshooting?"
    a: "Give it 24 to 48 hours of normal, plugged-in use, including idle time when background tasks run. Cumulative monthly updates usually settle within a day; annual feature updates can take two days on slower drives. If the laptop is still sluggish after two days with the same symptoms — not improving at all — move from waiting to the active fixes in this guide."
  - q: "Can I uninstall a Windows update that made things slow?"
    a: "Yes, for most updates. Go to Settings > Windows Update > Update history > Uninstall updates, select the recent update, and uninstall it, then pause updates for a week. Note that uninstalling removes its security fixes too, so treat it as a diagnostic step: if speed returns, the update was the cause, and you can reinstall it later after Microsoft issues fixes."
  - q: "Why do updates re-enable apps I disabled?"
    a: "Feature updates essentially reinstall Windows while keeping your files, and that process rebuilds parts of the configuration — including some startup entries, default apps, and privacy settings — from the new image's defaults. Your personal files survive, but per-app toggles sometimes do not. It is annoying but expected, which is why re-checking startup apps after every feature update is good hygiene."
  - q: "Should I pause updates to avoid the slowdown?"
    a: "Pausing for a week or two after a problematic update is reasonable; pausing indefinitely is not. Unpatched systems accumulate real security risk quickly. A better long-term strategy is setting Active Hours so updates install overnight, keeping good backups, and applying the post-update checklist in this article — wait, verify settings, clean up — rather than avoiding updates entirely."
---

You installed the update, rebooted, and now everything is slower: boot takes twice as long, apps hesitate, the disk churns for an hour, and the laptop you liked last week feels like a different machine. This is the single most reported Windows performance complaint online, and it spikes reliably in the days after every Patch Tuesday and each annual feature update.

Most post-update slowness is temporary and explicable. After an update, Windows runs a backlog of deferred work all at once: Defender re-scans replaced system files, the search indexer rebuilds, the Store updates inbox apps, and the update components themselves clean up. On top of that, updates sometimes reset your settings — power plans, startup apps, visual effects — or install a driver version that performs worse than the one you had.

The right response is a short waiting period plus targeted checks, not panic. The steps below separate the normal (settles in a day or two) from the broken (needs intervention), in the order the community has found most effective. For the structured variant of this guide, see [slow boot after update](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/).

## Why this happens

- **Post-update background task storm**: Defender rescans, index rebuilds, and Store updates all run at once after reboot.
- **Reset power plan**: updates sometimes revert a High performance or Best performance plan to Balanced.
- **Re-enabled startup apps**: updates can re-enable startup entries you previously disabled.
- **New driver regressions**: an update-bundled graphics or storage driver may perform worse than your old one.
- **Corrupted update components**: a partially failed update leaves services retrying work forever.
- **Old update files consuming disk**: Windows.old and staged update files can leave the system drive nearly full.
- **Re-enabled visual effects**: feature updates occasionally reset personalization and effects settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it 48 hours of normal use

Most post-update slowness is the background backlog, which genuinely finishes on its own. Resist the urge to fix things during this window; you may break what was about to heal itself.

1. Use the laptop normally for two days, keeping it plugged in with some idle time.
2. Avoid running heavy benchmarks during this window — they compete with the backlog.
3. If speed returns on its own, the update was fine; if not, continue below.

### Fix 2: Check what is actually busy

Do not guess at the cause — Task Manager names it in seconds. Screenshot the sorted list; it is your evidence for which fix worked.

1. Open Task Manager and sort Processes by CPU, Memory, and Disk in turn.
2. Note the top consumers: MsMpEng (Defender), SearchIndexer, TiWorker (update), or Wsappx (Store).
3. Match each to its dedicated fix — Defender rescans settle; a stuck TiWorker needs the update cache cleared.

### Fix 3: Verify your power plan survived

This two-minute check fixes a surprising number of post-update slowdowns. Check both plugged-in and on-battery plans, since updates can reset each independently.

1. Open Settings > System > Power & battery and check the Power mode setting.
2. Set it to Best performance while troubleshooting.
3. For the full walkthrough see [change power plan to best performance](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/).

### Fix 4: Re-disable startup apps

Updates love to resurrect disabled startup entries. Put them back down. Updates are notorious for resurrecting Teams and other chat clients.

1. Open Task Manager > Startup apps and sort by Status.
2. Disable everything you do not need at boot — updaters, chat apps, game launchers.
3. Reboot and time the startup; the difference is often dramatic. Details: [disable startup programs](/articles/how-to-disable-startup-programs-windows-11/).

### Fix 5: Clear the update cache and retry

If Windows Update itself is stuck, its cache is the standard fix. Do not delete the SoftwareDistribution folder itself, only its Download contents.

1. Stop the Windows Update and BITS services in services.msc.
2. Delete the contents of C:\Windows\SoftwareDistribution\Download.
3. Restart the services and check for updates again.

### Fix 6: Roll back a bad driver

When slowness started with the update and centers on graphics or storage, the bundled driver is suspect. Driver rollback is only offered if Windows actually replaced the driver during the update.

1. Open Device Manager, find your display adapter or storage controller, and open Properties.
2. On the Driver tab, choose Roll Back Driver if available.
3. If unavailable, download the previous driver from your laptop maker's support site and install it manually.

### Fix 7: Clean up post-update disk bloat

A full system drive after an update cripples everything. Reclaim the space. Never delete Windows.old in the first ten days unless disk space is critical.

1. Run Disk Cleanup as administrator and tick Previous Windows installations and Temporary Windows installation files.
2. Remove Windows.old only if you are sure you will not roll back within 10 days.
3. Aim for at least 15–20% free space on the system drive. [Microsoft's Windows help](https://support.microsoft.com/en-us/windows) documents the cleanup tools.

### Fix 8: Uninstall the problematic update

When every other fix fails and the timeline clearly starts at a specific update, removing that update is a legitimate diagnostic step. Windows lets you uninstall most cumulative updates from the update history page, and if performance returns immediately, you have proven the update was the cause rather than a coincidence.

1. Open Settings > Windows Update > Update history > Uninstall updates.
2. Select the update installed just before the slowdown began and uninstall it.
3. Pause updates for two weeks so it does not reinstall overnight.
4. If speed returns, report the issue via Feedback Hub before reinstalling later.

## Closing

Post-update slowness is usually Windows doing legitimate catch-up work, plus a few settings the update reset behind your back. Wait out the backlog, verify your power plan and startup apps, clear the update cache if something is stuck, and clean up the disk bloat. In the large majority of cases the laptop is back to its old self within two days — no reinstall required.
