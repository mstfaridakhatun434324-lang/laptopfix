---
title: "Windows Update Taking Too Long After a Windows 11 Update (Fix)"
slug: how-to-fix-windows-update-taking-too-long-after-windows-11-update
date: 2026-09-28
categories: ["windows-update"]
tags:
  - windows update
  - slow update
  - windows 11
  - performance
  - troubleshooting
description: "Windows Update taking hours after a Windows 11 update? Learn what is normal, what is stuck, and how to speed up or repair painfully slow updates."
thumbnail: "/images/thumbs/how-to-fix-windows-update-taking-too-long-after-windows-11-update.webp"
faqs:
  - q: "How long should a Windows 11 update normally take?"
    a: >
      On a modern SSD laptop with decent broadband, monthly cumulative updates take 10 to 30 minutes including the reboot. Feature updates take 30 to 90 minutes. HDD or eMMC laptops can take two to three times longer. Anything beyond 4 hours for a cumulative update, or a percentage frozen with zero disk activity for over an hour, is abnormal.
  - q: "Does low disk space really slow down Windows Update?"
    a: >
      Enormously. The installer stages files, creates backups, and shuffles data on C:, and all of that degrades sharply under about 15 GB free — stalling entirely under 10 GB. Freeing space to 20 GB or more is the single most effective speedup for slow updates, ahead of network or CPU fixes.
  - q: "Why is my update stuck at the same percentage every time?"
    a: >
      A repeat stall at the same percentage almost always means a corrupted download chunk or a servicing-stack problem rather than genuine slowness. Reset the SoftwareDistribution cache for a fresh download; if it still stalls at the same point, repair the image with DISM and SFC, then try the manual catalog install for that KB.
  - q: "Will an SSD really make Windows Update faster?"
    a: >
      Yes — dramatically. Disk I/O dominates the install phase, and the jump from a spinning hard drive to even a budget SATA SSD typically cuts cumulative update times by half or more. If your laptop still has an HDD and updates regularly take hours, an SSD upgrade pays for itself in saved time within months.
---

There is slow, and then there is Windows Update slow. A monthly update that takes twenty minutes is normal; one that sits at 37 percent for three hours is not. After a Windows 11 update, the next update cycle sometimes drags terribly — downloads crawl, installation stalls, and the whole machine feels hostage to a progress bar.

Slow updates have a physics to them: download speed, disk speed, free space, and CPU contention each contribute, and on laptops the usual suspects are a nearly full drive, a spinning hard disk, and background apps fighting the installer for resources. Genuine stuck updates are a separate, smaller category with different fixes.

This guide helps you tell slow from stuck, speed up the legitimate cases, and repair the ones that are truly wedged.

## Why this happens

- **Large cumulative update on a slow disk:** multi-gigabyte updates on HDD or eMMC laptops install dramatically slower than on SSDs — this is physics, not a bug.
- **Nearly full system drive:** staging and file shuffling slow to a crawl under ~15 GB free, and can stall entirely under ~10 GB.
- **Slow or congested network:** update downloads share bandwidth with everything else; a saturated connection makes the download phase look frozen.
- **Background apps consuming CPU and disk:** browsers, game launchers, and antivirus scans compete with the installer for the same resources.
- **Corrupted download forcing silent retries:** a damaged payload makes the engine re-download chunks repeatedly without telling you.
- **Outdated servicing stack:** an old servicing stack processes new updates inefficiently or stalls on them.
- **Driver updates bundled with the cumulative:** large driver packages in the same cycle extend the install phase significantly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decide whether it is slow or stuck

Do not intervene in a merely slow update — interrupting a healthy install causes the corruption you are trying to avoid. Check for progress signals first.

1. Note the percentage and time; check again in 30 minutes for any movement at all.
2. Open Task Manager and look for disk and network activity from Service Host or TiWorker — activity means progress.
3. On HDD laptops, allow up to 3 hours for a big cumulative update before calling it stuck.
4. If the percentage has not moved and there is zero disk/network activity for a full hour, treat it as stuck and continue.

### Fix 2: Free up disk space

The single highest-impact speedup. Updates need working room, and a cramped C: drive is the most common reason updates drag.

1. Open Settings > System > Storage and use Cleanup recommendations to remove large unused items.
2. Run Disk Cleanup (cleanmgr.exe) including system files: tick Windows Update Cleanup and Delivery Optimization Files.
3. Move personal files off C: to another drive or external storage until at least 20 GB is free.
4. Retry the update with the space cleared and compare the speed.

### Fix 3: Switch to a faster, stable network

Downloads are half the battle. A weak Wi-Fi signal or congested network turns a 20-minute download into a 3-hour one.

1. Move closer to the router or switch to a wired Ethernet connection.
2. Pause streaming, cloud backups, and large downloads on the network during the update.
3. Restart the router if speeds are inexplicably low.
4. If downloads still crawl only for Microsoft servers, try the [manual catalog install](https://www.catalog.update.microsoft.com/) for the specific KB instead.

### Fix 4: Quiet the machine during the install

Give the installer the machine. Background contention is invisible but brutal on dual-core and older quad-core laptops.

1. Close browsers, launchers, and heavy apps before starting the update.
2. Pause your antivirus's scheduled full scan until the update completes.
3. Plug in the charger and set the laptop to not sleep: Settings > System > Power & battery.
4. Let the install run untouched — checking Task Manager every two minutes does not help.

### Fix 5: Run the Windows Update troubleshooter

When slowness comes with errors or repeated stalls at the same percentage, the troubleshooter can detect the stuck state underneath.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Reboot and start the update cycle fresh.
4. If it reports nothing but the stall persists at the same point, continue.

### Fix 6: Reset the update cache to clear poisoned downloads

Silent retry loops on corrupted chunks look exactly like extreme slowness. A cache reset forces genuinely fresh downloads.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services and run Windows Update — the fresh download is often dramatically faster.

### Fix 7: Install the update manually and repair the image

For updates that will not finish by any automatic means, take manual control — and repair the servicing stack underneath if needed.

1. Note the KB number from update history and install it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. If manual install also stalls, run DISM /Online /Cleanup-Image /RestoreHealth then sfc /scannow in an elevated prompt.
3. Reboot and run Windows Update once more to confirm normal speed is restored.
4. Chronic slowness on an old HDD laptop may simply mean it is time for an SSD — the single best upgrade for update times.

## Closing

Slow updates are usually a resource problem — disk space, disk speed, or network — not a Windows problem, and the fixes above address each in order of impact. Reserve the stuck-update repairs for genuinely frozen progress. And schedule big updates for when you can leave the machine alone — an update you are not watching always feels faster than one you are. If your updates fail outright instead of dragging, the [0x80070002 download fix](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/) and our [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-step-by-step/) are the next stops.
