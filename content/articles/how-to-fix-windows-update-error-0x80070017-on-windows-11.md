---
title: "Windows 11 Error 0x80070017: Fix the CRC Check Failure"
slug: how-to-fix-windows-update-error-0x80070017-on-windows-11
date: 2026-09-10
categories: ["windows-update"]
tags: ["windows update", "0x80070017", "windows 11", "crc error", "data error"]
description: "Error 0x80070017 is a cyclic redundancy check failure — the data did not survive intact. Find where it is being damaged and install cleanly."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-on-windows-11.webp"
faqs:
  - q: "What is Windows Update error 0x80070017?"
    a: "It is a CRC (cyclic redundancy check) failure — ERROR_CRC. Data read back did not match what was written, so the update installer rejected it. The damage happens in the download, in the local cache, on the disk, or in memory."
  - q: "How is 0x80070017 different from 0x80070570?"
    a: "They are siblings: 0x80070570 means a file was corrupt or unreadable, while 0x80070017 specifically means a redundancy check failed during a read or transfer. The causes and fixes overlap heavily — cache, disk, memory — which is why both guides test the same hardware."
  - q: "Can a bad download cause 0x80070017 repeatedly?"
    a: "Only if the same corrupt source keeps being reused. If fresh downloads on a stable connection keep failing CRC, suspect the disk or RAM instead — something below the network is damaging the data. Clear the cache first; it is the fastest way to test the download hypothesis."
  - q: "Should I replace my drive over one 0x80070017?"
    a: "No. A single CRC failure after a flaky download is usually innocent. Replace-or-repair urgency applies when CRC errors recur across different updates and chkdsk or SMART data confirms storage damage. For driver packages specifically failing, check our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/)."
---

Error 0x80070017 is the cyclic redundancy check sounding the alarm: data that went in does not match data that came out. Every file carries a checksum, and when Windows 11 reads an update file whose checksum fails, it stops rather than install damaged bits. The code is precise about what happened — data corruption — and silent about where, which is where the troubleshooting begins.

Where is a short list with big implications. Corruption in the download means the network or the cache is at fault — annoying but harmless. Corruption on the disk means bad sectors — back up now. Corruption in memory means faulty RAM — replace soon. The steps below test each in order of likelihood and ease, so a ten-minute cache clear either fixes it or points you at the hardware tests that matter.

Treat recurring CRC failures as a hardware warning until proven otherwise. Data you care about flows through the same disk and RAM.

## Why this happens

- **Damaged download**: Transfer corruption failing the integrity check on arrival.
- **Corrupt cache**: Bad fragments in SoftwareDistribution failing checks on every retry.
- **Bad disk sectors**: Storage damage corrupting files at rest.
- **Faulty memory**: Bit flips during extraction or installation.
- **Failing storage controller**: Controller errors corrupting reads and writes.
- **Overheating drive**: Thermal errors on hot NVMe storage during long operations.
- **Filesystem damage**: Logical corruption breaking reads of intact data.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the download cache

The fastest hypothesis to test is that the corruption lives in the cache. Purging it forces a completely fresh download, and if the CRC passes afterward, the case is closed in minutes.

1. Open an elevated Command Prompt.
2. Run net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Delete everything inside C:\Windows\SoftwareDistribution\Download.
4. Restart the four services, reboot, and retry the update.

### Fix 2: Download on a stable connection

If the corruption enters during transfer, a clean pipe matters. Marginal Wi-Fi corrupts more than people expect — packets get damaged, not just dropped — so prove the download on the most stable link available.

1. Switch to Ethernet or move close to the router for the download.
2. Pause other network activity during the transfer.
3. Retry the update and let the download complete uninterrupted.
4. If the CRC now passes, the old connection was the corruptor.

### Fix 3: Repair system files with DISM and SFC

Corruption in the existing Windows image makes the update's checks fail against a damaged baseline. Repairing the baseline first gives the update clean ground to build on.

1. In an elevated Command Prompt, run DISM /Online /Cleanup-Image /RestoreHealth.
2. Then run sfc /scannow to completion.
3. Reboot the laptop.
4. Retry the update on the repaired system.

### Fix 4: Scan the disk with chkdsk

Bad sectors are the hardware explanation for CRC failures, and chkdsk is the direct test. Its report distinguishes cosmetic filesystem issues from a genuinely failing drive.

1. Run chkdsk C: /f /r in an elevated Command Prompt and approve the reboot scan.
2. Let the full scan finish — it can take an hour or more.
3. Review bad-sector counts in the summary.
4. Many bad sectors means the drive is failing: back up immediately and plan replacement.

### Fix 5: Test the RAM

Memory faults corrupt data invisibly during the operations updates perform most — decompression, hashing, writing. When disk and download both check out, RAM is the remaining suspect.

1. Run mdsched.exe and choose Restart now and check for problems.
2. Allow the complete test cycle to finish.
3. If errors are found, reseat the modules and retest.
4. Persistent errors mean replacing the RAM — on soldered-memory laptops, that means manufacturer service.

### Fix 6: Install the package manually from the catalog

A manual install from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) changes the entire download and staging path, which isolates whether the corruption is path-specific or systemic.

1. Get the KB number from Update history.
2. Download the x64 .msu from the Update Catalog.
3. Install it directly and reboot when asked.
4. If the manual install also fails CRC, the hardware verdict from the tests above stands — act on it.

### Fix 7: Check SMART data and drive health

For recurring CRC errors, get the drive's own testimony. SMART attributes reveal reallocated sectors and error rates that chkdsk summaries only hint at.

1. Use your SSD or HDD manufacturer's health utility to read SMART data.
2. Look specifically at reallocated sector count and uncorrectable errors.
3. If thresholds are exceeded, clone to a new drive immediately — do not keep updating on failing storage.
4. After replacement, clean-install Windows; [Microsoft's support hub](https://support.microsoft.com/en-us/windows) documents the process.

### Fix 8: Rule out overclocking and malware

Two invisible corruptors cause CRC errors with no other symptoms: unstable memory overclocks that flip bits under hashing load, and malware that hooks the network stack and damages downloads. Eliminate both before you blame the disk.

1. Enter UEFI setup during boot, disable XMP or EXPO memory profiles, and confirm the RAM runs at stock speeds.
2. Save, boot into Windows, and retry the update — if CRC errors stop, the overclock was the corruptor.
3. Open Windows Security > Virus & threat protection > Scan options and run a Microsoft Defender Offline scan.
4. On a clean result, clear the update cache and retry; on a detection, clean first, then retry.

## Closing

Error 0x80070017 is data integrity doing its job — the checksum caught damage before it became your system. Honor that warning by finding the damage source rather than retrying blindly. Cache and connection fixes handle the innocent cases; the disk and memory tests protect you in the serious ones. A CRC failure is never just an update problem when it repeats — it is your storage or memory telling you something, and it deserves to be heard. Related: the [Windows 10 0x80070017 guide](/articles/how-to-fix-windows-update-error-0x80070017-on-windows-10/) and our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) if CRC failures hit driver packages.
