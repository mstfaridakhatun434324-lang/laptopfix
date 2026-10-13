---
title: "How to Fix Windows Update Error 0x80070570 on Your Laptop"
slug: how-to-fix-windows-update-error-0x80070570-on-laptop
date: 2026-09-24
categories: ["windows-update"]
tags: ["windows update error 0x80070570", "error_file_corrupt", "corrupt update files", "bad ram update error"]
description: "Error 0x80070570 means update files are corrupt. Find whether the cause is bad downloads, failing RAM, or disk errors, and fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-laptop.webp"
faqs:
  - q: "What does error 0x80070570 mean?"
    a: "It means ERROR_FILE_CORRUPT: a file the installer needs is damaged. The corruption can come from a bad download, failing RAM corrupting data in memory, disk errors, or damaged installation media, and the fix depends on which source is responsible."
  - q: "Can bad RAM really cause update errors?"
    a: "Yes. Faulty memory corrupts data as it is read and written, so downloaded files that were fine on the server arrive corrupted in memory. If corruption errors recur across different downloads, testing the RAM is essential before anything else. Do not skip this when corruption keeps recurring."
  - q: "How do I test my laptop's RAM?"
    a: "Use Windows Memory Diagnostic: press Win + R, type mdsched.exe, and choose to restart and test. For a deeper test, MemTest86 run from a USB drive checks every cell over multiple passes and catches intermittent faults. Run it overnight for the most thorough result."
  - q: "Should I worry about my hard drive with 0x80070570?"
    a: "It is worth checking. Run chkdsk to scan for bad sectors and check the drive's SMART health data. Recurring corruption errors with a healthy disk point at RAM instead; with a failing disk, replace the drive before it gets worse."
---

Error 0x80070570 is Windows telling you that a file it needs is corrupt — damaged, unreadable, not what it should be. Unlike the download-specific codes, this one is broader: the corruption could have happened in transit, in memory, on the disk, or on the installation media itself.

That breadth makes diagnosis the heart of this fix. Re-downloading helps if the network mangled the file. It does nothing if your RAM is flipping bits or your SSD is developing bad blocks, because the next copy will corrupt exactly the same way. The steps below are ordered as a diagnostic funnel: rule out the cheap causes first, then test the hardware.

Take this code seriously when it recurs. One corrupt download is bad luck; repeated corruption across different files is hardware telling you it needs attention.

Corruption is a symptom with many authors, and 0x80070570 does not name its author — that is your job. The diagnostic funnel below is ordered by cost: free and fast checks first, hardware tests second, replacements last. Resist the temptation to skip straight to reinstalling Windows; a fresh install on failing RAM just produces fresh corruption.

## Why this happens

- **Corrupted download.** A bad network transfer delivers damaged payload files that fail integrity checks.

- **Failing RAM.** Bad memory corrupts data in transit, so even perfect downloads arrive damaged.

- **Disk errors or bad sectors.** Failing storage corrupts files as they are written or read back.

- **Damaged installation media.** A scratched DVD or flaky USB drive feeds corrupt setup files to the installer.

- **Corrupt component store.** Existing WinSxS damage makes staged files fail validation.

- **Antivirus quarantining payload files.** Security software occasionally damages or removes update files mid-write.

- **Interrupted previous installation.** A killed install leaves half-written files that later attempts trip over.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Re-download the update with a clean cache

If the corruption happened in transit, a fresh download fixes it. Clearing the cache first guarantees the damaged copy is not reused. Download over the most reliable connection you have for this test; re-downloading over the same flaky hotel Wi-Fi that corrupted the first copy just repeats the experiment.

1. In an elevated Terminal, run `net stop wuauserv` and `net stop bits`.
2. Delete everything in C:\Windows\SoftwareDistribution\Download.
3. Run `net start wuauserv` and `net start bits`, then check for updates on a stable connection.

### Fix 2: Fix 2: Test the RAM

Recurring corruption is the classic symptom of bad memory. Windows Memory Diagnostic is built in and takes the laptop offline for a thorough test. If the laptop has two RAM sticks, testing with one removed at a time isolates the bad module physically when diagnostics are inconclusive.

1. Press Win + R, type `mdsched.exe`, and press Enter.
2. Choose Restart now and check for problems.
3. If it reports errors, the RAM needs replacing; on most laptops this means a service visit or a SO-DIMM swap.

### Fix 3: Fix 3: Check the disk for errors

Bad sectors corrupt whatever lands on them. A disk scan tells you whether storage is the corruption source. The /r flag implies /f and adds the surface scan; on large modern drives the full pass can take several hours, so start it before bed.

1. Open Terminal as administrator and run `chkdsk C: /f /r`.
2. Type Y when asked to schedule it, restart, and let the full scan run, which takes a while on large drives.
3. If chkdsk finds bad sectors, back up immediately and plan a drive replacement.

### Fix 4: Fix 4: Recreate the installation media

When the error appears during feature updates or clean installs from USB, the media itself is suspect. Flash drives do go bad, and ISO downloads do corrupt. Recreate the USB even if the old one looks fine; flash memory fails gradually, and a stick that reads small files perfectly can still corrupt multi-gigabyte sequential writes.

1. Download a fresh ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Verify the download completed fully, then create the USB with the Media Creation Tool on a different, known-good flash drive.
3. Retry the installation from the new media.

### Fix 5: Fix 5: Run SFC and DISM

If the corruption lives in the existing Windows installation rather than the new payload, the system file repairs address it. DISM fixes the store, SFC fixes the files. Run DISM first even though SFC is the more famous tool; SFC cannot fix files when the store it draws from is itself damaged.

1. In an admin Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`, restart, and retry the update.

For a deeper look at the SFC pass — reading its log, interpreting the results, and what to do when it reports files it could not fix — see our [SFC scan walkthrough](/articles/how-to-run-sfc-scannow-in-windows-11-24h2/).

### Fix 6: Fix 6: Temporarily disable third-party antivirus

Real-time scanners have been known to damage large payload files during writes. Disabling the AV for one download attempt rules it out. Add the SoftwareDistribution folder to the antivirus exclusions only as a last resort; the temporary disable is safer than a permanent exclusion.

1. Disable third-party antivirus real-time protection temporarily.
2. Clear the download cache once more and retry the update.
3. Re-enable protection immediately afterward.

### Fix 7: Fix 7: Try a different USB port and drive

For media-based installs, the port and the stick both matter. A failing USB controller or a dying flash drive produces exactly this corruption signature. Front-panel and hub ports can be flaky on some laptops; the ports soldered directly to the motherboard are always the most reliable choice for installer media.

1. Copy the installer to a different, preferably new, USB drive.
2. Use a USB port directly on the laptop rather than a hub or dock.
3. Retry. For CRC-specific corruption during setup, our [0x80070017 guide](/articles/how-to-fix-windows-update-error-0x80070017-on-laptop/) covers the deeper hardware checks, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official diagnostics.

## Closing

Error 0x80070570 demands diagnosis before treatment: re-download for the one-off corruption, but test RAM and disk when it recurs, because hardware is the usual author of repeated corruption. Work the funnel in order and you will find the real source. For the closely related CRC failure, see our [0x80070017 walkthrough](/articles/how-to-fix-windows-update-error-0x80070017-on-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official hardware diagnostics.
