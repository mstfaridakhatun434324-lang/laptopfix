---
title: "Windows Update Taking Too Long on Windows 10? Speed It Up"
slug: how-to-fix-windows-update-taking-too-long-on-windows-10
date: 2026-10-04
categories: ["windows-update"]
tags: ["windows 10", "windows update", "slow", "performance"]
description: "Windows 10 updates crawling for hours? Find out what's slowing them down and speed up the download and install process."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-on-windows-10.webp"
faqs:
  - q: "Why are Windows 10 updates so much slower than Windows 11?"
    a: "Windows 10 uses an older update engine that scans, stages, and installs less efficiently, and its cumulative updates have grown very large after years of accumulated fixes. The same hardware updates noticeably faster under Windows 11. On Windows 10 itself, the practical speedups are raising Delivery Optimization bandwidth caps, clearing the cache, minimizing background competition, and installing big backlogs manually."
  - q: "How long is too long for a Windows 10 update?"
    a: "A monthly cumulative update on Windows 10 typically needs 30 to 90 minutes on an SSD-equipped laptop; feature updates can take two to four hours. Beyond those ranges with no Task Manager activity, the process is stuck rather than slow. Overnight runs are reasonable for feature updates on old hardware — but a frozen progress bar with idle resources always warrants the stuck-update repairs."
  - q: "Will clearing the cache delete installed updates?"
    a: "No. The SoftwareDistribution download folder holds only pending downloads and temporary staging files. Installed updates live in the component store, which cache clearing does not touch. Your update history, installed patches, and personal files are all unaffected — Windows simply re-downloads whatever is still pending."
  - q: "Should I just upgrade to Windows 11 instead?"
    a: "If your laptop meets the requirements, it is worth serious consideration: the faster update engine alone transforms the experience, alongside the longer support horizon. Check eligibility with Microsoft's PC Health Check tool first. For hardware that does not qualify, the speedups in this guide are the best available path to tolerable Windows 10 updating."
---

Windows 10 is in its twilight years, and its update machinery shows it: the old update engine is less efficient than Windows 11's, cumulative updates have grown enormous, and aging hardware makes every phase slower. The result is updates that genuinely take hours — long enough that users reasonably wonder whether something is broken.

Sometimes something is broken, and sometimes it is just Windows 10 being Windows 10 on old hardware. This guide helps you distinguish the two, then attacks the real slowdowns: the inefficient old engine, throttled delivery, cluttered caches, and the resource starvation that plagues aging laptops. You cannot make Windows 10 updates fast, but you can stop them from taking all day.

Windows 10's remaining user base skews toward older hardware, which means the slowness compounds: an old update engine on an old CPU with an old disk. Each factor alone is tolerable; together they produce the multi-hour updates this guide addresses. The fixes below attack the factors you can change and help you live with the ones you cannot.

## Why this happens

- **Aging update engine:** Windows 10's update agent is less efficient at scanning and staging than newer versions, so the same update takes longer on 10 than on 11.
- **Enormous cumulative updates:** Years of accumulated fixes make each Windows 10 cumulative update large, and the old engine installs them less efficiently.
- **Slow or failing storage:** Many remaining Windows 10 laptops run on old SATA SSDs or spinning disks, where the install phase's random writes crawl.
- **Background throttling:** Delivery Optimization defaults and metered flags throttle downloads silently, stretching the download phase for hours.
- **Antivirus scanning overhead:** Real-time scanning of every staged update file multiplies install time on already-slow CPUs.
- **Corrupted partial downloads:** The old engine is prone to resuming damaged partial files instead of replacing them, producing progress bars that never move.
- **Update backlog:** A Windows 10 machine that has missed months of updates must process a deep queue serially — each item slow on its own, endless in sequence.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether it is stuck or just slow

Windows 10 updates are slow by nature, so verify before intervening. Task Manager reveals the truth: active disk and CPU usage from update processes means progress, however sluggish; flatlined resources mean a stuck process needing repair.

1. Open Task Manager and observe TiWorker.exe and related processes.
2. Sustained activity means the update is working — let it run, preferably overnight.
3. No activity for over an hour means stuck — continue with the fixes.
4. Never force-shutdown a working update; only intervene in confirmed stuck states.

### Fix 2: Lift Delivery Optimization limits

The old engine plus default bandwidth caps is a brutal combination. Raising the caps on an unmetered connection often produces the single biggest speedup available on Windows 10. The [Windows Modules Installer worker](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-on-dell-laptop/) often accounts for the background disk churn compounding the slowness.

1. Open Settings, Update and Security, Delivery Optimization, Advanced options.
2. Raise or uncheck the download bandwidth limits.
3. Confirm the connection is not flagged as metered.
4. Restart the pending download and measure the difference.

### Fix 3: Clean the update cache

Years of accumulated partial downloads slow the old engine's verification pass. A clean cache lets the current update download and verify without wading through debris.

1. Launch an elevated Command Prompt from the Start menu.
2. Stop the update and transfer services with net stop wuauserv and net stop bits.
3. Clear out everything inside C:\Windows\SoftwareDistribution\Download.
4. Bring both services back with net start, then open Windows Update to rescan.

### Fix 4: Reduce competition for resources

On aging hardware, every background task steals from the update. Pausing sync tools, scans, and heavy apps gives the installer the scarce CPU and disk it needs. Silent throttling from a metered flag is detailed in [metered connection blocking Windows Update](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/).

1. Pause cloud sync services during the update.
2. Disable scheduled antivirus scans until the update finishes.
3. Close browsers and heavy applications.
4. Run the update with the laptop plugged in and otherwise idle.

### Fix 5: Install the latest cumulative update manually

A deep backlog on the old engine is the worst case for speed. Collapsing it with a single manual install of the latest cumulative update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) skips the serial queue entirely.

1. Identify your Windows 10 build with winver.
2. Download the latest cumulative update for that build from the catalog.
3. Install the .msu as administrator and restart.
4. Subsequent updates will be small and comparatively quick.

### Fix 6: Consider the Windows 11 upgrade path

If the hardware qualifies, the honest long-term fix for slow Windows 10 updating is leaving Windows 10 behind. Windows 11's update engine is substantially faster, and [Microsoft's upgrade guidance](https://support.microsoft.com/en-us/windows) covers eligibility and the upgrade process.

1. Check eligibility with the PC Health Check app.
2. Back up important files before upgrading.
3. Upgrade through Windows Update or the Installation Assistant.
4. Post-upgrade updates will be noticeably faster on the same hardware.

### Fix 7: Schedule updates for idle hours

When updates cannot be made fast, they can at least be made invisible. Windows 10's active hours and scheduled install options let the slow phases run overnight, so the slowness stops mattering. This is acceptance rather than repair — but on hardware that will never be fast, it is the pragmatic answer.

1. Open Settings, Update and Security, and set your active hours to cover the waking day.
2. Allow automatic restarts outside active hours.
3. Leave the laptop plugged in and connected overnight.
4. Check in the morning — the slow work happened while you slept.

## Closing

Windows 10 updates are slow for structural reasons — old engine, huge packages, aging hardware — but stuck is different from slow, and the bottlenecks are fixable. Lift the bandwidth caps, clear the cache, starve the competition, and collapse backlogs manually. And when the hardware allows, the Windows 11 upgrade is the permanent escape from the slow lane.
