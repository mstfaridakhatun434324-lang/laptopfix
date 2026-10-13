---
title: "Update Assistant Stuck at 99%? A Step-by-Step Fix"
slug: how-to-fix-update-assistant-stuck-at-99-percent-step-by-step
date: 2026-09-07
categories: ["windows-update"]
tags: ["update assistant stuck at 99", "windows 11 upgrade stuck", "installation assistant fix", "feature update troubleshooting"]
description: "Update Assistant frozen at 99%? This step-by-step walkthrough shows how to tell a real hang from a slow one, clear the broken download cache, and finish the Windows 11 upgrade."
thumbnail: "/images/thumbs/how-to-fix-update-assistant-stuck-at-99-percent-step-by-step.webp"
faqs:
  - q: "Why does the Assistant get stuck but Windows Update works?"
    a: "The two tools fetch updates through different mechanisms. The Assistant downloads the entire feature-update image and validates it as one large file, which exposes storage slowness and disk problems that Windows Update's smaller incremental chunks sail past. That is why a 99% hang in the Assistant does not doom the whole upgrade — the Media Creation Tool or regular Windows Update often completes the same update without trouble."
  - q: "Should I delete the $Windows.~BT folder?"
    a: "Yes — provided the Assistant is fully closed first. That folder is simply the staging area for the downloaded image, and Windows rebuilds it on the next run, so removing it wipes out the corrupted partial download that keeps causing repeat hangs at 99%. Just never delete it while an installation is actively running, because that would interrupt a live upgrade in progress."
  - q: "Does the Update Assistant work on metered connections?"
    a: "Not reliably. The Assistant pulls down several gigabytes, and on a metered connection Windows can throttle or quietly pause the transfer — meanwhile the progress bar sits at 99%, misleading you into thinking the install is stuck. Always run the Assistant on an unmetered connection. Check Settings > Network & internet first and confirm the metered flag is off before you launch it."
  - q: "Is the Media Creation Tool better than the Update Assistant?"
    a: "When the Assistant keeps hanging, frequently yes. The Media Creation Tool downloads and stages the update through a completely separate code path, so the cache corruption trapping the Assistant does not follow you across. Both are official Microsoft utilities downloaded from the same page — the MCT is simply the more dependable fallback once the Assistant has stalled more than once."
---

Staring at the Update Assistant parked at 99% for an hour is miserable, but your first task is to decide whether it is genuinely hung or merely slow. The Assistant's progress bar is famously coarse: between 99% and the restart prompt, it verifies the cryptographic hashes of a multi-gigabyte image, and on a slow drive that silent verification can take 20 to 40 minutes without the bar twitching. Open Task Manager and watch the disk — steady read activity means it is still laboring away. If the drive has been completely silent for over an hour, you have a real hang. Broader sluggishness is covered in [Windows Update taking too long overall](/articles/how-to-fix-windows-update-taking-too-long-after-windows-11-update/).

Once you have confirmed a genuine stall, the suspects narrow quickly: a corrupted partial download that the Assistant keeps resuming instead of replacing, a disk too cramped to stage the final files, or a driver or firmware snag at the exact moment the Assistant hands control to Windows Setup. Each of these has a clean remedy, and none of them endangers your files — the Assistant leaves your running system untouched until the actual installation phase begins.

## Why this happens

- **A corrupted partial download in the staging folder.** The Assistant resumes a broken $Windows.~BT cache rather than fetching fresh bytes, so the same damaged data stalls it at 99% on every attempt.
- **Antivirus grinding through the downloaded image.** Real-time scanning of a 5+ GB file during hash verification can drag the process to a crawl or block it outright.
- **An outdated Assistant executable.** An old binary can mishandle the current feature update's requirements — always grab a fresh copy from Microsoft before retrying.
- **Too little disk space for the final staging step.** The last percentage points need room to unpack and position files; a nearly full C: drive stalls the process without any error message.
- **The manufacturer updater competing for the servicing stack.** Laptop vendor utilities running their own updates can lock components the Assistant needs, deadlocking the handoff.
- **Firmware problems surfacing at handoff.** The 99% mark is exactly where the Assistant passes control to Windows Setup, which is when outdated BIOS issues reveal themselves.
- **A metered connection quietly pausing the download.** The transfer never actually finished — the bar just displays 99% while Windows waits for an unmetered connection.
- **Marginal sectors on the drive.** Verifying a multi-gigabyte image reads the whole disk surface, exposing failing sectors that stall the process; chkdsk and SMART data confirm this one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pause real-time antivirus while the Assistant runs

Hash-checking a 5 GB image while a scanner inspects every byte can stall verification indefinitely. Laptop vendor updater utilities running at the same time are another classic 99% trap — two updaters wrestling over the servicing stack deadlock the handoff.

1. Open your third-party antivirus and switch off real-time protection for the duration of the run.
2. In Task Manager, end any manufacturer updater processes before launching the Assistant.
3. Start the Update Assistant again.
4. If the bar climbs past 99%, the scanner was the bottleneck.
5. Re-enable protection the moment the upgrade finishes.
6. Consider adding the Assistant's download folder to the scanner's exclusion list for future runs.

### Fix 2: Wipe the Assistant's download cache

Stale or damaged partial downloads poison every retry. [The same Assistant stalling on Lenovo laptops](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-lenovo-laptop/) follows the same cache-clearing logic. An old Assistant binary can also mishandle the current feature update, so always fetch a fresh copy from Microsoft instead of reusing a months-old one.

1. Exit the Update Assistant completely — verify in Task Manager that it is really gone.
2. If it exists, delete the contents of C:\$Windows.~BT, which is the Assistant's staging folder.
3. Clear C:\Windows\SoftwareDistribution\Download as well.
4. Download a brand-new Update Assistant from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
5. Right-click the fresh download and run it as administrator.
6. Once the upgrade lands, run winver to confirm the new build number.

### Fix 3: Launch the Assistant with elevated rights

Permission snags at handoff are uncommon but real. At the 99% mark, the download hands control to Windows Setup, which is precisely why driver and firmware troubles show up at this handoff point.

1. Right-click the Update Assistant executable and choose Run as administrator.
2. Approve the UAC prompt.
3. Keep other heavy applications closed while it works.
4. If it still parks at 99%, permissions were never the issue — keep going.
5. Elevation also smooths over staging folders with unusual access-control lists.

### Fix 4: Bring the BIOS up to date before the handoff

Firmware-related stalls clear with a current BIOS. Scanning the multi-gigabyte image in real time with antivirus remains a common slowdown, so leaving the staging folder out of the scan is a sensible tweak.

1. Check the current BIOS version with msinfo32.
2. Find the latest BIOS for your exact laptop model on the manufacturer's support site or [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
3. Flash it with the charger plugged in, and do not interrupt the process.
4. Retry the Assistant once the BIOS update completes.
5. This clears the 99% stalls that turn out to be handoff failures in disguise.
6. Re-enable your antivirus and the vendor utility automation after the upgrade.

### Fix 5: Inspect the drive for failing sectors

Reading a multi-gigabyte image for verification lays bare any marginal sectors. If the C: drive shows no free-space fluctuation and the disk sits idle, the Assistant has stalled — it is hung, not working.

1. Open an elevated Command Prompt and run: chkdsk C: /f.
2. Accept the prompt to schedule the scan, restart, and let it finish.
3. Review SMART data through your disk diagnostics utility.
4. A drive accumulating reallocated sectors will stall every large verification — no cache clear fixes that.
5. Replace a failing drive before attempting the upgrade again.

### Fix 6: Switch to the Media Creation Tool

A different tool means a different code path, and it frequently gets past the point where the Assistant sticks. The Media Creation Tool downloads and stages through its own implementation, which is exactly why it escapes Assistant-specific corruption.

1. From [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), get the Media Creation Tool for Windows 11.
2. Run it and choose 'Upgrade this PC now'.
3. Choose the 'Keep personal files and apps' option.
4. The MCT fetches its own image and uses its own staging path.
5. This avoids the Assistant's corrupted cache altogether.
6. If the Assistant stalls identically a second time, change tools instead of repeating the failed attempt.

### Fix 7: Fall back to an ISO in-place upgrade

When every assistant and tool stalls, this is the most reliable manual route. When a 99% stall persists after the cache clear, the culprit is the handoff to the installer — the BIOS, the storage driver, or disk health — not the download.

1. Head to Microsoft's Windows 11 download page and grab the Windows 11 ISO.
2. Double-click the ISO to mount it.
3. Launch setup.exe with administrator rights.
4. Pick 'Keep personal files and apps' and unplug unnecessary peripherals.
5. ISO setup uses the same engine as Windows' own upgrades, so it rarely hangs at handoff.
6. Make a note of how long the successful run took — it makes judging future 'stuck' moments much easier.

## Closing

The Assistant's coarse progress bar is the real villain in most of these stories, which is why the disk-activity check always comes first — plenty of 'stuck' upgrades are just slow ones. When the hang is genuine, clearing the cache and running a fresh Assistant binary resolves the majority of cases, while the stubborn remainder yield to a BIOS update, a drive check, or a different Microsoft tool. A related stall — [a feature update frozen at 61 percent](/articles/how-to-fix-feature-update-stuck-at-61-percent-step-by-step/) — follows the same diagnostic rhythm.
