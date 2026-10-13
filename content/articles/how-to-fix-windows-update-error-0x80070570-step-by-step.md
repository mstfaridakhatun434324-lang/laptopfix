---
title: "Fix Windows Update Error 0x80070570: Corrupt Files Resolved Step by Step"
slug: how-to-fix-windows-update-error-0x80070570-step-by-step
date: 2026-10-02
categories: ["windows-update"]
tags: ["0x80070570", "windows update error", "corrupt update files", "windows 11", "windows 10"]
description: "Windows Update error 0x80070570 means a file it downloaded is corrupt or unreadable. Follow this step-by-step guide to clear the cache, repair the file system, and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-step-by-step.webp"
faqs:
  - q: "What does error 0x80070570 mean during Windows Update?"
    a: "It means Windows Update tried to read a file that was corrupt, incomplete, or in an unexpected format. The most common cause is a damaged download in the update cache, but it can also signal failing RAM or disk sectors that corrupted the file on the way in."
  - q: "Can 0x80070570 be caused by bad RAM?"
    a: "Yes, and it is more common than most people expect. Error 0x80070570 is famously associated with faulty RAM during Windows installations because bad memory corrupts data as it is written to disk. If the error returns after clearing caches, running the Windows Memory Diagnostic is a sensible next step."
  - q: "Will deleting the SoftwareDistribution folder delete my personal files?"
    a: "No. The SoftwareDistribution folder holds only cached update downloads and update history metadata — nothing you created lives there. Deleting its contents cannot touch your documents, photos, or installed programs. Windows simply rebuilds the cache from scratch the next time it checks for updates, which usually takes just a few minutes."
  - q: "How do I know the fix actually worked?"
    a: "Run a manual update check after applying the fix. If the previously failing update installs to completion and 0x80070570 does not reappear, the repair worked. For extra confidence, restart the laptop and check once more — two consecutive clean update cycles mean the problem is genuinely resolved rather than temporarily quiet."
---

Seeing error 0x80070570 interrupt your Windows Update feels especially unfair because the message tells you almost nothing. The update downloads, the progress bar moves, and then everything halts with a hexadecimal code that could mean a dozen things. In practice, though, this error has a consistent personality: it is almost always about a file that Windows cannot read — either because the download arrived damaged, the storage cache is tangled, or, less often, because the memory or drive that handled the file is itself failing.

The good news is that the first layer of fixes is quick and safe, and it resolves the majority of cases. The approach here is deliberately ordered: start with the cheap, non-destructive steps that clear out corrupt update data, and only move to hardware checks if the error refuses to leave. Follow the sequence as written rather than cherry-picking, because each step builds on a clean slate left by the previous one.

## Why this happens

- **Corrupt download in the update cache:** The most common trigger. A transient network hiccup or interrupted download leaves a damaged file in the SoftwareDistribution cache, and every retry reads the same broken copy.
- **Failing or flaky RAM:** 0x80070570 has a long association with memory errors. Bad RAM corrupts data as it moves between the download, memory, and disk, producing unreadable files from a perfectly good download.
- **Bad disk sectors:** Sectors that are starting to fail can corrupt files written to them. The update file lands on a dying sector, and the installer cannot read it back intact.
- **Tangled update components:** Stopped or misconfigured Windows Update services, stale BITS jobs, and locked cache files can produce a partially written file that reads as corrupt.
- **Third-party antivirus interference:** Real-time scanners that hook deeply into file operations can damage or quarantine fragments of large update payloads mid-download.
- **Out-of-date storage or chipset drivers:** Unstable storage drivers can silently corrupt writes under load, especially on laptops with older firmware and large cumulative updates.
- **Insufficient free disk space:** When the drive is nearly full, large update files get written in fragments or truncated, and the truncated file fails its integrity check — a pattern that also causes [cumulative updates to fail every single time](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the built-in Windows Update troubleshooter

Start with the automated tool before touching anything manually. Open Settings, go to System, then Troubleshoot, then Other troubleshooters, and run the Windows Update troubleshooter. It checks service states, resets stuck components, and clears minor cache corruption on its own.

1. Press Win + I to open Settings.
2. Go to System, then Troubleshoot, then Other troubleshooters.
3. Click Run next to Windows Update and let it complete.
4. Restart the laptop and check for updates again.

### Fix 2: Clear the SoftwareDistribution cache

This is the single most effective fix for 0x80070570 because it forces Windows to download a fresh, uncorrupted copy of the update.

1. Open an elevated Command Prompt (search "cmd", right-click, Run as administrator).
2. Stop the update services with these commands, pressing Enter after each: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Open File Explorer and navigate to C:\Windows\SoftwareDistribution. Delete everything inside the folder (not the folder itself).
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
5. Restart the laptop and run Windows Update again.

### Fix 3: Run SFC and DISM scans

If the corruption extends beyond the cache into system files, these tools repair it.

1. Open an elevated Command Prompt.
2. Run `sfc /scannow` and wait for it to finish (this can take 20–30 minutes).
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store the SFC tool relies on.
4. Restart and try the update once more. If you want background on related corruption codes, the guide on [fixing Windows Update error 0x80070017](/articles/how-to-fix-windows-update-error-0x80070017-step-by-step/) covers similar file-integrity territory.

### Fix 4: Temporarily disable third-party antivirus

Real-time antivirus can interfere with large update payloads.

1. Open your antivirus settings and disable real-time protection temporarily.
2. Run Windows Update and let it complete.
3. Re-enable real-time protection immediately afterward.
4. If the update succeeded only with protection off, add an exclusion for the update process or switch to Windows Defender during update days.

### Fix 5: Test your RAM with Windows Memory Diagnostic

If 0x80070570 survives cache clears and file repairs, suspect hardware — starting with memory.

1. Press Win + R, type `mdsched.exe`, and press Enter.
2. Choose "Restart now and check for problems".
3. Let the test run to completion (standard mode is fine for a first pass).
4. After the laptop restarts, check the results in Event Viewer under Windows Logs, System, filtering for MemoryDiagnostics-Results.
5. If errors are reported, one of your RAM modules is failing and needs replacement — no software fix will permanently clear the error until it is swapped.

### Fix 6: Check the drive for bad sectors

1. Open an elevated Command Prompt.
2. Run `chkdsk C: /f /r` and accept the offer to schedule the check at the next restart.
3. Restart the laptop and let the check complete — it can take a while on large drives.
4. Review the summary for bad sectors. A handful can be tolerated; growing counts mean the drive is dying and should be replaced before it takes your data with it.

### Fix 7: Update storage drivers and retry, or install manually

1. Visit your laptop manufacturer's support page or use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to update chipset and storage drivers.
2. Free up at least 20 GB on the system drive.
3. Retry Windows Update. If it still fails, download the specific KB package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it manually — a fresh standalone package bypasses the damaged cache entirely.

## Closing

Error 0x80070570 looks cryptic, but it follows a predictable script: corrupt update data first, system file damage second, failing hardware third. Work the list from top to bottom, and in most cases the SoftwareDistribution clear alone ends the story. If you reach the memory and disk checks, treat any failures there as a gift — you have found a real hardware problem while it was still just an update error, before it became data loss.
