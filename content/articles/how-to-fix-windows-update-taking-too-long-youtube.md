---
title: "Windows Update Taking Too Long? Speed It Up With These Fixes"
slug: "how-to-fix-windows-update-taking-too-long-youtube"
date: "2026-09-24"
categories: ["windows-update"]
tags: ["windows update", "slow update", "taking too long", "speed up"]
description: "Windows Update taking hours on your laptop? Learn what's normal, what's stuck, and seven ways to speed up slow downloads and installations."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-youtube.webp"
faqs:
  - q: "How long should a Windows update normally take?"
    a: "A monthly cumulative update typically takes fifteen to forty-five minutes total, including download and installation, on a modern laptop with a decent connection. Feature updates take longer, often one to three hours, because they migrate much more of the system. If a cumulative update has been running for over two hours with no progress, or a feature update exceeds five hours, something is likely stuck rather than slow."
  - q: "Is it safe to restart a laptop stuck on an update?"
    a: "If the progress indicator has not moved for over two hours and disk activity has stopped, a forced restart is reasonably safe on modern Windows, which is designed to roll back incomplete updates. Hold the power button to shut down, wait thirty seconds, and power on. Windows will usually resume or roll back cleanly. Avoid interrupting an update that is actively progressing, even slowly."
  - q: "Why do updates take longer on older laptops?"
    a: "Older laptops have slower storage, less RAM, and weaker CPUs, all of which stretch out the installation phase where thousands of files are processed. A mechanical hard drive in particular can make updates take several times longer than an SSD. Keeping the drive defragmented, or better yet upgrading to an SSD, is the single biggest speedup for aging machines."
  - q: "Does a slow internet connection affect installation time?"
    a: "A slow connection only affects the download phase, not the installation phase. Once the package is fully downloaded, installation speed depends on your CPU, RAM, and storage. If the download crawls, the fixes for network and Delivery Optimization in this guide help. If the install phase crawls after a quick download, focus on disk space, drive speed, and background processes."
---
Watching Windows Update crawl for hours tests anyone's patience. The percentage ticks upward at a glacial pace, or worse, sits frozen while the fan spins and you wonder whether anything is happening at all. Slow updates are not always broken updates, some phases are genuinely time-consuming, but knowing the difference between slow and stuck saves you from both unnecessary waiting and premature panic.

Update time splits into two phases with different bottlenecks. The download phase depends on your connection speed, Microsoft's servers, and settings like metered connections and Delivery Optimization. The installation phase depends on your CPU, RAM, and especially your storage speed, plus how much background activity competes for resources. Diagnosing which phase is slow tells you which fixes apply.

This guide helps you tell slow from stuck, then gives you seven ways to speed things up, from network tweaks to storage upgrades. Work through them in order. If your update is not just slow but failing outright, our [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) is the right next read.

## Why this happens

- **Slow or metered connection:** Throttled or low-bandwidth networks stretch the download phase dramatically.
- **Mechanical hard drive:** HDDs process the thousands of install-phase file operations far slower than SSDs.
- **Low disk space:** Near-full drives force the installer into slow, fragmented staging.
- **Background competition:** Heavy apps, antivirus scans, and indexing steal CPU and disk from the installer.
- **Delivery Optimization misconfiguration:** Poor peer settings can slow rather than speed downloads.
- **Stuck download state:** A wedged transfer service looks like slowness but is actually a stall.
- **Large feature payload:** Annual feature updates are gigabytes in size and legitimately take hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is slow or stuck

Do not act blindly. Check for real activity before intervening.

1. Note the exact percentage and the time, then check again in thirty minutes.
2. Open Task Manager and look at disk and network activity for the update processes.
3. Steady disk or network activity means it is working, however slowly.
4. Zero activity for over an hour with no progress change means it is stuck.
5. If stuck, hold the power button to force a restart and let Windows roll back.

### Fix 2: Optimize the network for the download phase

Remove throttles and instability slowing the transfer.

1. Turn off the metered connection toggle in your Wi-Fi network properties.
2. Switch to wired Ethernet or move closer to the router.
3. Disconnect the VPN during the download.
4. Pause bandwidth-heavy activities like streaming on the network.
5. Retry the update and compare download speed.

### Fix 3: Tune Delivery Optimization

Fix peer-sharing settings that may be hindering rather than helping.

1. Go to Settings, Windows Update, Advanced options, Delivery Optimization.
2. Try toggling Allow downloads from other PCs off to use Microsoft servers directly.
3. Check Advanced options for bandwidth limits and raise or remove them.
4. Restart and observe whether download speed improves.
5. Keep the setting that performs better for your network.

### Fix 4: Free disk space and reduce background load

Give the installer room and resources to work at full speed.

1. Ensure at least 15 to 20 GB free on C: using Storage settings.
2. Run Disk Cleanup as administrator to clear temporary files.
3. Close heavy applications and pause antivirus scans during the install.
4. Disable unnecessary startup programs in Task Manager.
5. Retry the update with the system otherwise idle.

### Fix 5: Reset a genuinely stalled download

If diagnosis shows a stall rather than slowness, clear it and start fresh.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services and reboot, then retry the update.

### Fix 6: Schedule updates for idle hours

Stop fighting the update for resources by letting it run when you are not.

1. Go to Settings, Windows Update, Advanced options.
2. Set active hours to cover your working day.
3. Allow the update to run overnight on AC power with the lid open or set to do nothing when closed.
4. Check progress in the morning instead of watching it.
5. Many seemingly slow updates complete fine given uninterrupted time.

### Fix 7: Consider an SSD upgrade for chronic slowness

If every update takes hours on an old hard drive, the hardware is the bottleneck.

1. Confirm the drive type in Task Manager, Performance tab.
2. If it shows HDD, research a compatible SSD for your laptop model.
3. Clone the drive or clean-install Windows on the new SSD.
4. Expect update times to drop dramatically, often by two-thirds.
5. Keep the old drive as an external backup afterward.

For download-specific errors rather than slowness, see our [download error fixes](/articles/how-to-fix-kb5062553-download-error-on-windows-11/) and Microsoft's guidance at https://support.microsoft.com/en-us/windows.

### Fix 8: Prevent sleep and drive spin-down during updates

Laptops that sleep mid-update create some of the worst slowdowns and stalls. When the machine dozes during the install phase, the servicing stack pauses and resumes awkwardly, stretching a forty-minute update into hours. Configuring the power plan to stay fully awake during updates, including preventing the hard drive from spinning down, gives the installer the uninterrupted run it needs to finish at full speed.

1. Open Control Panel, Power Options, and edit your active plan's advanced settings.
2. Set Sleep after to Never for the plugged-in state temporarily.
3. Expand Hard disk and set Turn off hard disk after to Never while plugged in.
4. Disable USB selective suspend so external devices do not reset mid-install.
5. Keep the lid open or set closing the lid to Do nothing during the update.
6. Restore your normal power settings after the update completes.

## Closing

Slow Windows updates usually have an identifiable bottleneck: the network for downloads, the drive for installs, or a stalled service masquerading as slowness. Diagnose the phase first, then apply the matching fix, and most updates finish in a reasonable window. For chronically slow older laptops, an SSD upgrade pays for itself in time saved across every future update.
