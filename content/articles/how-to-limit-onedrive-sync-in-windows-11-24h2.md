---
title: "How to Limit OneDrive Sync on Windows 11 24H2"
slug: "how-to-limit-onedrive-sync-in-windows-11-24h2"
date: 2026-09-24
categories: ["performance"]
tags: ["onedrive", "sync", "windows 11 24h2", "bandwidth", "cloud storage"]
description: "OneDrive hogging bandwidth and CPU on Windows 11 24H2? Limit what it syncs, throttle its speed, and schedule it around your work with these settings."
thumbnail: "/images/thumbs/how-to-limit-onedrive-sync-in-windows-11-24h2.webp"
faqs:
  - q: "How do I stop OneDrive from syncing everything?"
    a: "Open OneDrive Settings > Account > Choose folders and uncheck everything you do not need on the laptop — deselected folders stay in the cloud but stop syncing locally. This is called selective sync, and it is the single most effective way to reduce OneDrive's workload. Your files remain safe online and accessible through a browser; they just stop consuming local disk, bandwidth, and CPU on every sync cycle."
  - q: "Can I limit OneDrive's upload and download speed?"
    a: "Yes. In OneDrive Settings > Sync and backup > Advanced settings, you can cap both upload and download rates to a fixed KB/s value instead of letting OneDrive use the full connection. This is ideal on slow or shared connections where OneDrive would otherwise saturate the link and make video calls or gaming lag. Set the cap during work hours and remove it overnight if you want bulk syncing to finish faster."
  - q: "Does pausing OneDrive sync cause problems?"
    a: "No, pausing is completely safe. The pause options (2, 8, or 24 hours) simply freeze all sync activity; your local files stay as they are and cloud files stay as they are until you resume. Nothing is deleted or lost during a pause. It is the right tool when you need full bandwidth for a call or a download — just remember to resume afterward, or the 24-hour auto-resume will do it for you."
  - q: "What is Files On-Demand and should I use it?"
    a: "Files On-Demand keeps placeholder stubs for cloud files instead of full local copies, downloading content only when you open it. It dramatically reduces local disk usage and initial sync load, which is why it is enabled by default on 24H2. Keep it on unless you need guaranteed offline access to everything — for example before a flight. You can right-click any folder and choose Always keep on this device for the critical subset."
---
OneDrive on Windows 11 24H2 is more aggressive than ever: folder backup is pushed during setup, the sync engine starts with Windows, and on a laptop with a big photo library or a slow uplink it can saturate your connection for hours. Video calls stutter, web pages crawl, and Task Manager shows OneDrive grinding away at disk and CPU.

You do not have to choose between OneDrive and a usable connection. Windows gives you precise controls: which folders sync at all, how much bandwidth sync may use, when sync pauses, and whether files live locally or as cloud placeholders. Most people only need two or three of these to transform the experience.

This guide walks through each limiter in order of impact, so you can stop after the first one that solves your problem. If OneDrive should not be running at all on your machine, our [disable-startup guide](/articles/how-to-disable-onedrive-startup-on-windows-11/) covers the full off switch.

## Why this happens

- **Full folder backup enabled:** Desktop, Documents, and Pictures syncing means tens of thousands of files under constant watch.

- **Large photo and video libraries:** camera uploads and phone backups create multi-gigabyte sync backlogs.

- **Unlimited bandwidth usage:** by default OneDrive takes whatever the connection offers, starving everything else.

- **Frequent file churn:** developer folders, caches, or game saves that change constantly trigger endless re-syncs.

- **Multiple devices syncing:** edits from your phone and desktop multiply the sync traffic hitting the laptop.

- **Files On-Demand disabled:** forcing full local copies of everything maximizes both disk usage and sync workload.

- **Slow uplink connection:** asymmetric connections (fast down, slow up) make uploads the bottleneck that never clears.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use selective sync to shrink what OneDrive watches

Selective sync is the highest-impact limiter: every folder you deselect stops generating sync traffic, disk I/O, and CPU cycles permanently. Be deliberate — most people need only a fraction of their cloud on the laptop.

1. Click the OneDrive tray icon > gear icon > Settings.
2. Go to the Account tab and click Choose folders.
3. Uncheck large or rarely used folders — old photo archives, completed projects, phone backups.
4. Click OK; OneDrive removes the local copies but keeps everything in the cloud.
5. Access deselected files anytime through onedrive.com in a browser when you need them.

### Fix 2: Cap upload and download bandwidth

Bandwidth caps let OneDrive sync politely in the background instead of seizing the whole connection. This is the fix for “my internet dies whenever OneDrive syncs” and Microsoft documents it on its [Windows support pages](https://support.microsoft.com/en-us/windows).

1. In OneDrive Settings, go to Sync and backup > Advanced settings.
2. Under Network, set a download rate limit — try 50–70 percent of your measured download speed.
3. Set an upload rate limit too — on slow uplinks, cap it low enough that calls and gaming stay smooth.
4. Click OK and test with a speed test while OneDrive is actively syncing.
5. Adjust the caps until syncing is invisible during normal use.

### Fix 3: Pause syncing during work hours

Sometimes you do not need limits — you need OneDrive completely quiet for the next two hours. The built-in pause is instant, safe, and auto-resumes so you cannot forget it forever.

1. Click the OneDrive tray icon.
2. Click Pause syncing and choose 2 hours, 8 hours, or 24 hours.
3. Confirm the tray icon shows the paused state.
4. Do your calls, gaming, or big downloads in peace.
5. Resume manually from the same menu when done, or let the timer expire — sync restarts automatically.

### Fix 4: Enable Files On-Demand and free up space

Files On-Demand replaces full local copies with tiny placeholders, slashing both disk usage and the sync engine's workload. On 24H2 it is the default, but upgrades and setting changes sometimes turn it off.

1. In OneDrive Settings > Sync and backup > Advanced settings, confirm Files On-Demand is turned on.
2. In File Explorer, right-click bulky folders you rarely open and choose Free up space to convert them to placeholders.
3. For must-have-offline folders, right-click and choose Always keep on this device instead.
4. Check Settings > System > Storage afterward — reclaimed gigabytes are common.
5. Less local data means shorter, cheaper sync cycles from now on.

### Fix 5: Move churn-heavy folders out of OneDrive

Some folders should never have been in OneDrive: anything that changes hundreds of times a day forces constant re-uploads. Relocating these is a one-time fix with permanent payoff.

1. Identify churn-heavy folders: code build outputs, video render caches, game save folders, temp downloads.
2. Move them outside the OneDrive folder hierarchy (for example to C:\Work).
3. If an app insists on a path inside OneDrive, check whether the app lets you redirect its data folder.
4. For Desktop/Documents/Pictures backup, go to Settings > Sync and backup > Manage backup and turn off backup for folders with heavy churn.
5. Watch OneDrive's tray activity drop to near-zero during normal work afterward.

### Fix 6: Set the connection as metered as a last resort

Marking your Wi-Fi as metered tells Windows — and OneDrive — to treat bandwidth as precious. OneDrive pauses automatic syncing on metered connections, which is a blunt but effective limiter when nothing else fits your situation.

1. Open Settings > Network & internet > Wi-Fi and click your connected network.
2. Turn on Metered connection.
3. OneDrive will pause syncing automatically; confirm via the tray icon.
4. Remember this also pauses Windows Update downloads and Store updates — check them manually weekly.
5. Turn the metered flag off when you are back on an unmetered connection so updates resume.

### Fix 7: Unlink or quit when limits are not enough

If you have capped, paused, and deselected everything and OneDrive still misbehaves, the honest answer may be that it does not belong on this laptop. Quitting or unlinking is reversible and keeps your cloud files intact.

1. Right-click the tray icon and choose Quit OneDrive for a temporary full stop.
2. For a longer break, go to Settings > Account > Unlink this PC.
3. Your files stay in the cloud and local copies remain on disk until you delete them.
4. Free up disk space afterward with our [disk cleanup guide](/articles/how-to-free-up-disk-space-on-windows-11/) if the local OneDrive folder was large.
5. Reinstall or relink any time from the Start menu — nothing is permanent.

## Closing

OneDrive does not have to be all-or-nothing. Selective sync shrinks its world, bandwidth caps civilize its appetite, pausing gives you quiet hours, and Files On-Demand keeps the disk lean. Apply the limiters that match your actual annoyance — most people stop after the first two — and OneDrive fades back into the useful background utility it was meant to be.
