---
title: "Low Disk Space on C Drive? Full Troubleshooting Walkthrough"
slug: low-disk-space-on-c-drive-troubleshooting
date: 2026-10-06
categories: ["performance"]
tags: ["low disk space", "c drive full", "troubleshooting", "storage", "windows 11"]
description: "C: drive keeps filling up even after cleanup? Troubleshoot the root cause — runaway logs, sync caches, or update leftovers — and reclaim space permanently."
thumbnail: "/images/thumbs/low-disk-space-on-c-drive-troubleshooting.webp"
faqs:
  - q: "Why does my C: drive keep filling up after I clean it?"
    a: "Because something is actively writing to it: runaway application logs, a stuck Windows Update download loop, cloud sync downloading files you didn't ask for, or a misbehaving app cache. One-time cleanup treats the symptom. To fix it permanently, you need to find the process or folder that's growing — a disk analyzer run twice, days apart, reveals the grower."
  - q: "How do I find what's secretly eating my disk space?"
    a: "Run WizTree or WinDirStat as administrator and sort by size — this shows the exact folders consuming space. For the sneakier case of space that keeps disappearing, run the analyzer twice several days apart and compare: the folder that grew is your culprit. Also check Settings, System, Storage for the category breakdown Windows provides."
  - q: "Is it safe to delete files in the Windows Temp folder?"
    a: "Yes, files in C:\\Windows\\Temp and your user Temp folder (%temp%) that aren't currently in use are safe to delete — they're transient by design. Use Disk Cleanup rather than manual deletion for system temp locations. If a file is locked by a running program, Windows will refuse to delete it; skip those. Never delete temp files as a substitute for finding a runaway log writer."
  - q: "Can low disk space actually damage my SSD?"
    a: "Not damage exactly, but it degrades performance and increases wear. SSDs need free blocks for wear-leveling and garbage collection; a nearly-full SSD slows down significantly and wears its remaining cells harder. Keeping 15 to 20 percent free isn't just about having room for files — it's about the drive's long-term health."
---

There's a special frustration to cleaning 10GB off your C: drive and watching it fill up again within a week. That pattern means cleanup isn't your problem — something is actively consuming space, and until you identify it, you're bailing water with a hole in the hull. This guide is the troubleshooting walkthrough for exactly that situation: find the grower, stop it, then clean up properly.

If you just need the one-time cleanup order, the [best-way guide](/articles/best-way-to-fix-low-disk-space-on-c-drive/) covers it. This article is for when space keeps disappearing.

## Why this happens

- **Runaway application logs:** A crashing service or verbose debug logging can write gigabytes per day to log folders.
- **Stuck Windows Update loop:** Failed updates re-downloading endlessly consume space in SoftwareDistribution.
- **Cloud sync downloading unexpectedly:** OneDrive/Dropbox set to "always keep on this device" for huge libraries, or sync errors duplicating files.
- **Hibernation and pagefile on small drives:** Fixed multi-GB system files that never shrink on their own.
- **Windows.old accumulation:** Multiple feature updates each leaving a Windows.old if cleanup never runs.
- **App caches without limits:** Browser, Teams, Adobe, and game launchers caching with no cap.
- **System Restore over-allocation:** Generous restore-point storage silently eating tens of GB.
- **Shadow copies and backup staging:** Forgotten backup tools staging full images on C:.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map the disk and find the grower

Run WizTree as administrator, sort by size, and screenshot or note the top folders. Wait 2–3 days of normal use, run it again, and compare — the folder that grew significantly is your culprit. Common growers: `C:\Windows\Logs`, `SoftwareDistribution\Download`, OneDrive cache folders, `%localappdata%` app caches, and `System Volume Information`. Naming the grower turns a mystery into a targeted fix. For the post-update variant of this problem, see [low disk space after Windows 11 update](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/).

1. Run WizTree (admin); record the largest folders.
2. Wait 2–3 days; run again and compare.
3. Identify the folder that grew — that's your culprit.
4. Target all further fixes at that specific grower.

### Fix 2: Stop runaway logs

If `C:\Windows\Logs` (especially CBS.log) is the grower, the Component-Based Servicing log is ballooning — often due to a corrupted servicing state generating endless log entries. Run DISM RestoreHealth and SFC to fix the underlying servicing corruption, then safely delete or truncate the runaway log. For third-party app logs, check the app's settings for a verbosity/debug-logging toggle and turn it off, or cap the log folder. Deleting the log without fixing the writer just restarts the cycle.

1. Confirm which log file is growing (check file sizes by date).
2. For CBS.log: run DISM RestoreHealth + SFC to fix servicing.
3. For app logs: disable debug/verbose logging in the app's settings.
4. Delete/truncate the bloated log only after fixing the writer.

### Fix 3: Break the stuck update download loop

If `SoftwareDistribution\Download` keeps growing: admin Terminal → `net stop wuauserv` + `net stop bits`, rename `C:\Windows\SoftwareDistribution` to `.old`, restart the services, then check for updates once and let it complete cleanly. A corrupted update cache makes Windows re-download the same payloads repeatedly. After the reset, verify the folder stays stable in size. This also resolves the "updates fail at the same percentage forever" companion symptom. Broader disk guidance: [free up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/).

1. Stop wuauserv and bits services.
2. Rename SoftwareDistribution → SoftwareDistribution.old.
3. Restart services; run one clean update check.
4. Verify the Download folder stops growing.

### Fix 4: Tame cloud sync storage

If your OneDrive folder is the grower: enable Files On-Demand and right-click bulky folders → "Free up space" to return them to cloud-only. Check sync errors — conflicted copies and failed uploads duplicate data. Review selective sync settings: unsync libraries you don't need locally. On work machines, IT-pushed SharePoint libraries are a classic silent grower — ask before unsyncing those, but do ask. The goal is a local footprint you chose deliberately, not one that accumulated by default.

1. Enable Files On-Demand in OneDrive settings.
2. Right-click bulky folders → Free up space (cloud-only).
3. Resolve sync errors and conflicted copies.
4. Use selective sync to drop unneeded libraries.

### Fix 5: Cap the fixed system files

Check the big fixed consumers: hiberfil.sys (`powercfg /hibernate off` if you never hibernate — reclaims GBs instantly), pagefile (cap via Advanced system settings if RAM is ample; never fully disable), and System Restore allocation (System Protection → Configure → limit to ~5%). These don't "grow," but on a small SSD they're a large fixed tax. Measure before and after — on a 256GB drive, hibernation off plus restore capped can free 15–25GB combined.

1. `powercfg /hibernate off` if hibernation is unused.
2. Cap (don't disable) the pagefile if RAM ≥ 16GB.
3. System Protection → Configure → limit to ~5%.
4. Measure reclaimed space after each change.

### Fix 6: Clear update leftovers and Windows.old properly

Disk Cleanup as admin → Clean up system files → check Windows Update Cleanup, Delivery Optimization Files, and Previous Windows installation(s) (only if you won't roll back). These are safe, Microsoft-sanctioned deletions — Microsoft documents the tool on the [Windows support site](https://support.microsoft.com/en-us/windows). Never manually delete WinSxS or SoftwareDistribution contents outside the sanctioned flows; the servicing stack depends on their structure. After cleanup, re-run WizTree to confirm the space is actually free and staying free.

1. Disk Cleanup (admin) → Clean up system files.
2. Check update-related categories + Windows.old if applicable.
3. Never manually delete WinSxS contents.
4. Re-run the disk analyzer to verify lasting results.

### Fix 7: Set up Storage Sense and monitoring

Settings → System → Storage → Storage Sense → On, configured to auto-clean temp files, Recycle Bin (30 days), and optionally Downloads. Then set a calendar reminder to glance at the Storage page monthly — two minutes to catch the next grower early. If space starts disappearing again, you now know the drill: WizTree twice, compare, target the grower. Permanent fixes beat permanent vigilance, but a monthly glance is cheap insurance.

1. Enable and configure Storage Sense.
2. Set a monthly 2-minute Storage page check.
3. If space drops again: re-run the two-scan comparison.
4. Address new growers with the same targeted approach.

## Closing

Recurring low disk space is a detective problem, not a cleaning problem. The two-scan comparison finds the grower in days, and each grower — runaway logs, stuck updates, sync bloat — has a specific, permanent fix. Do the detective work once, fix the writer, automate with Storage Sense, and the red C: bar becomes a story you tell about the old days.
