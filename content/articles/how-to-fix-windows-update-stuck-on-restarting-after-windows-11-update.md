---
title: "Windows Update Stuck on Restarting After a Windows 11 Update? Here's the Fix"
slug: how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update
date: 2026-10-13
categories: ["windows-update"]
tags: ["stuck on restarting", "windows 11 update", "restart hang", "update recovery", "fast startup"]
description: "Laptop frozen on 'Restarting' after installing a Windows 11 update? How to recover safely, fix the underlying cause, and prevent the next hang."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update.webp"
faqs:
  - q: "My laptop says 'Restarting' after an update and won't move. What do I do?"
    a: "First, wait 90 minutes — post-update restarts do heavy file work and are often just slow. If there's been no disk activity and the spinner is frozen for over an hour, hold the power button 10 seconds to force off, unplug USB devices, and power back on. Windows resumes the update from a checkpoint in most cases."
  - q: "Why does the restart hang happen after every Windows 11 update?"
    a: "The usual repeat offenders are a driver that won't unload (storage, display, or network drivers are classic), Fast Startup interfering with the restart handoff, or a USB peripheral stalling the shutdown sequence. Updating drivers and disabling Fast Startup break the cycle for most people."
  - q: "Should I unplug my laptop while it's stuck on 'Restarting'?"
    a: "No — keep it plugged in. A power loss during the restart phase is far worse than a hang, because Windows is actively writing system files. Only force a shutdown (keeping AC connected) after you've confirmed it's genuinely stuck with no disk activity for over an hour."
  - q: "It finally restarted but now updates fail. Are they related?"
    a: "Often yes. A hang during restart can leave the update half-applied, and the next update attempt then fails against the inconsistent state. Run DISM /Online /Cleanup-Image /RestoreHealth and sfc /scannow after recovering from a hang to repair any servicing damage before the next update round."
---

This is the scenario: the update installed, Windows asked for a restart, and now your laptop has displayed "Restarting" with spinning dots for an unreasonable amount of time. It's the worst kind of stuck because you can't see progress, you can't cancel, and every instinct says to hold the power button — which might be exactly the wrong move if the update is actually mid-write. The difference between a slow restart and a hung one is the most important diagnosis in this guide, because everything else follows from it.

Post-update restarts are Windows' heavy-lifting phase: replacing in-use system files, migrating drivers, updating boot data. Windows 11's cumulative updates have grown larger, and this phase has grown longer with them — 20 to 40 minutes is normal on modern hardware. But "normal" has a limit, and beyond it lies the hang: a driver refusing to unload, Fast Startup colliding with the restart, or a peripheral holding the shutdown sequence hostage. Here's how to tell which you're facing and what to do about each.

## Why this happens

- **A driver won't unload**: Storage, display, or network drivers hanging the shutdown sequence — the top cause of repeat hangs.
- **Fast Startup collision**: The hybrid shutdown state conflicts with the update's restart, freezing the handoff.
- **USB peripherals stall shutdown**: Docks, external drives, and printers holding the sequence waiting for responses.
- **Disk errors**: Bad sectors in the paths being written turn a normal restart into an hours-long crawl.
- **Stacked updates**: Multiple updates queuing file operations into one marathon restart.
- **Antivirus file hooks**: Security software inspecting every file swap during the update.
- **Corrupt hibernation file**: A damaged hiberfil.sys breaking the hybrid shutdown path.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify stuck vs. slow before touching anything

Ninety percent of the damage in this scenario is self-inflicted — force-restarting a working update. Diagnose first.

1. Start a timer from when the Restarting screen appeared. Allow **90 minutes** (SSD) or **2 hours** (HDD).
2. Listen for drive activity and watch for fan speed changes — both mean work is happening.
3. Observe the spinner: smooth animation = responsive system; frozen for 30+ minutes = likely hung.
4. If your laptop has a drive activity LED, blinking = progress.
5. Keep AC power connected throughout — never let the battery die here.
6. Only continue to Fix 2 after an hour of zero activity.

### Fix 2: Force the restart safely

For a confirmed hang, a forced shutdown is correct. Windows checkpoints update progress and resumes.

1. Hold **power** for 10 seconds until the laptop shuts off.
2. Disconnect **all USB devices**, docks, external drives, and printers.
3. Wait 30 seconds, then power on with only AC connected.
4. You'll typically see "Working on updates" complete within 10–30 minutes.
5. If it reaches the desktop, go to **Settings > Windows Update > Update history** to verify the update installed.
6. If it hangs again at the same point, continue to Fix 3.

### Fix 3: Disable Fast Startup permanently

Fast Startup is implicated in a large share of restart hangs. Disabling it costs a few seconds of boot time and buys reliable restarts.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)** and save.
5. Test with a manual **Restart** — it should complete cleanly.
6. As a bonus, also run `powercfg /hibernate off` then `powercfg /hibernate on` in elevated Command Prompt to rebuild a potentially corrupt hibernation file.

### Fix 4: Update the drivers that hang shutdowns

The repeat-hang pattern almost always traces to one driver. Update the usual suspects proactively.

1. Open **Device Manager** and update drivers under **Storage controllers**, **Display adapters**, and **Network adapters** (right-click > Update driver).
2. Get chipset and storage drivers from your maker: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
3. Update graphics from NVIDIA, AMD, or Intel's official driver pages rather than relying on Windows Update's versions.
4. Our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/) covers the systematic approach.
5. After updating, the next Patch Tuesday restart should complete normally — if it doesn't, one specific driver is the culprit (see Fix 6).

### Fix 5: Repair servicing damage from the interrupted update

A hang-interrupted update can leave the component store inconsistent, poisoning future updates.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow` after DISM completes.
4. Run `chkdsk C: /f` to catch filesystem damage from the hard shutdown.
5. Restart cleanly and verify **Settings > Windows Update** shows a healthy state.
6. This post-hang cleanup is what separates "recovered" from "recovered and stable."

### Fix 6: Find the hanging driver with a clean boot

If hangs recur after driver updates, isolate the offender methodically instead of guessing.

1. Run `msconfig`, check **Hide all Microsoft services**, and **Disable all**.
2. Disable all startup items in Task Manager.
3. Restart — if the restart is now fast, a third-party driver or service was hanging it.
4. Re-enable in halves to narrow it down: services first, then startup items.
5. Frequent culprits: VPN clients, third-party disk tools, RGB/peripheral software, old printer drivers.
6. Update or uninstall the identified culprit. If it's a driver Windows Update keeps reinstalling, see our [driver failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) for hiding it.

### Fix 7: Change your update-restart habits

Prevention is a procedure, not just a setting.

1. Before major updates, disconnect docks and USB peripherals — reconnect after.
2. Use **Restart** (not Shut down) when Windows requests it post-update.
3. Don't stack a month of deferred updates into one session if you can avoid it — smaller, frequent rounds restart faster.
4. Keep 20 GB free on C: so staging never becomes the bottleneck.
5. If a specific update hangs repeatedly, uninstall it in Safe Mode and pause updates until Microsoft revises the package — the same approach in our [24H2 Restarting screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).

## Closing

The "Restarting" hang is a patience test with a technical core: verify it's truly stuck before forcing anything, then eliminate the repeat causes — Fast Startup, stale drivers, and connected peripherals. One clean recovery plus the preventive steps above turns a monthly ordeal into a non-event. Your updates will still take their 20–40 minutes; they just won't take your evening.
