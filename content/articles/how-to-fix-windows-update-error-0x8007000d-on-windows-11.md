---
title: "Fix Windows Update Error 0x8007000d on Windows 11 (Invalid Data)"
slug: how-to-fix-windows-update-error-0x8007000d-on-windows-11
date: 2026-09-13
categories: ["windows-update"]
tags: ["windows update", "0x8007000d", "corrupt files", "troubleshooting", "windows 11"]
description: "Error 0x8007000d means Windows 11 received corrupted update data. Learn how to clear the bad cache, repair system files, and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8007000d-on-windows-11.webp"
faqs:
  - q: "What does 0x8007000d mean in plain English?"
    a: "On Windows 11, error 0x8007000d means ERROR_INVALID_DATA: Windows Update downloaded or staged update files, but they failed integrity checks, so installation was refused. The usual causes are an interrupted download, a corrupted SoftwareDistribution cache, disk errors, or antivirus interference. Clearing the cache and repairing system files resolves it in most cases."
  - q: "Can a failing hard drive cause error 0x8007000d?"
    a: "Yes, and it is the cause to rule out when the error repeats across many different updates. A drive with bad sectors or failing flash can corrupt update files as they are written, so every download fails validation. Run `chkdsk C: /f /r` and check the drive's SMART health; if errors keep appearing, back up your data and replace the drive."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Renaming it — which is what the fix does — is safe. It only holds staged downloads and the update history database, not installed updates or personal files. Windows recreates the folder automatically on the next update check. The .old copy remains as a backup until you are confident everything works, at which point you can delete it."
  - q: "Why does the error come back after I fixed it once?"
    a: "Recurrence points to an ongoing corrupting agent: a failing drive, an antivirus that keeps quarantining payload files, or a scheduled cleanup tool deleting servicing files. Fix the agent, not just the symptom — check disk health, review antivirus quarantine logs, and disable aggressive third-party cleaners before clearing the cache again."
---
Error 0x8007000d is Windows Update rejecting the package it downloaded: the data arrived, but its contents are invalid, so the installer refuses to touch it. Think of it as a parcel that arrived with a torn label — the delivery worked, the contents cannot be trusted. On Windows 11 this usually means the local download cache or the component store has corrupted entries.

The corruption is almost always local rather than coming from Microsoft's servers: an interrupted download, a disk hiccup, or security software quarantining part of the payload. Because the bad data sits in a cache, the standard cure is to throw the cache away and let Windows fetch a fresh copy.

If the same invalid-data error is haunting a different machine, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x8007000d-on-windows-10/) covers Windows 10, and when corruption runs deeper into the component store, the [companion guide for 0x80073712](/articles/how-to-fix-windows-update-error-0x80073712-on-windows-11/) picks up where this guide leaves off. Start with the quick checks below.

## Why this happens

- **The download cache holds corrupted files:** 0x8007000d means invalid data, and the most common source is a partially downloaded or bit-damaged package sitting in the SoftwareDistribution folder. Every retry reuses the same bad files until the cache is cleared.
- **An interrupted download left fragments behind:** Laptops that sleep, lose Wi-Fi, or shut down mid-download are prime candidates. The update engine resumes from fragments that no longer match the expected checksums, and validation fails.
- **Disk errors damaged the cached payload:** Bad sectors or file-system errors on the system drive can corrupt update files after a perfectly good download. If the drive is developing faults, this error recurs until the disk is checked.
- **Antivirus quarantined part of the package:** Overaggressive real-time scanning sometimes flags update payload components as suspicious and removes or locks them, leaving an incomplete package that fails data validation.
- **The component store has corrupted entries:** When the underlying WinSxS store that servicing builds upon is damaged, even fresh downloads fail to assemble, and the error persists across cache clears.
- **A failing drive is corrupting writes:** An SSD or HDD with failing flash cells or weak sectors can corrupt data as it is written. Recurring 0x8007000d across many different updates is a classic early warning of storage trouble.
- **Conflicting third-party system tools interfered:** Registry cleaners, aggressive debloat scripts, and some driver updaters modify servicing-related files or permissions, producing invalid data errors when the update engine touches those components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter first

The built-in troubleshooter checks for the exact conditions behind 0x8007000d — corrupted cache registrations, stopped services, and pending-file mismatches — and repairs them without you memorizing service names. It is the fastest way to rule out the simple causes before you go manual.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Choose Windows Update and click Run the troubleshooter.
3. Apply all recommended fixes and let it finish.
4. Restart the laptop, then open Settings > Windows Update and retry.
5. If the error persists, continue with the cache reset below — the troubleshooter often fixes the services but leaves bad files behind.

### Fix 2: Clear the corrupted download cache

This is the core fix for 0x8007000d: stop the update services, rename the SoftwareDistribution and catroot2 folders so Windows abandons the corrupted data, and restart the services. Windows rebuilds both folders and downloads fresh, checksum-validated copies of everything.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the three services with `net start wuauserv`, `net start bits`, `net start cryptsvc`, then check for updates.

### Fix 3: Repair system files with SFC and DISM

If clearing the cache does not help, the corruption may live in the protected system files or the component store itself. SFC scans protected files against known-good hashes, and DISM repairs the store those files are restored from — run DISM first so SFC has a healthy source to pull from.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to reach 100 percent.
3. When DISM finishes, run `sfc /scannow` and let it complete.
4. Restart the laptop after both scans finish.
5. Retry the update in Settings > Windows Update. If DISM reports it cannot find source files, see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for specifying an install image as the repair source.

### Fix 4: Check the system drive for errors

When 0x8007000d keeps returning for update after update, suspect the storage. CHKDSK scans the file system and marks bad sectors so Windows stops writing update data onto failing storage, which eliminates an entire recurring cause in one pass.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f /r`.
3. Type Y when asked to schedule the check at the next restart.
4. Restart the laptop and let the scan complete without interrupting it.
5. After booting back up, clear the update cache once more (Fix 2) and retry — the fresh download now lands on verified-good sectors.

### Fix 5: Install the update in a clean boot

Third-party services — especially antivirus filters and system utilities — can tamper with update payloads as they are written, recreating the invalid-data condition on every attempt. A clean boot starts Windows with only Microsoft services, removing those suspects from the equation for one update attempt.

1. Press Win + R, type `msconfig`, and press Enter.
2. On the Services tab, check Hide all Microsoft services, then click Disable all.
3. On the Startup tab, open Task Manager and disable all startup items.
4. Restart, then run the update from Settings > Windows Update.
5. Afterward, reopen `msconfig`, re-enable everything, and restart to return to normal.

### Fix 6: Install the update manually from the Microsoft Update Catalog

When the automatic pipeline keeps producing invalid data, bypass it: fetch the standalone installer from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and run it directly. The Catalog download uses your browser rather than the update services, so corrupted service state cannot taint the package.

1. Note the KB number shown next to the failing update in Settings > Windows Update.
2. Search that KB number on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Download the edition matching your architecture (x64 on most laptops).
4. Run the .msu file and follow the prompts, then restart.
5. Run a normal update check afterward to confirm the queue cleared.

## Closing

Error 0x8007000d is Windows protecting you from bad data, so treat it as a hygiene problem: clear the corrupted cache, verify the disk, and repair the file integrity chain with DISM and SFC. In the large majority of Windows 11 cases, the cache reset alone ends it — and if the error ever becomes a repeat visitor across unrelated updates, take the hint and check your drive's health before it becomes a bigger story.
