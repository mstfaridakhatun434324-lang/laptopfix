---
title: "How to Fix Windows Update Error 0x80070017 on a Laptop"
slug: how-to-fix-windows-update-error-0x80070017-on-laptop
date: 2026-09-26
categories: ["windows-update"]
tags: ["windows update error 0x80070017", "error_crc", "crc error windows update", "data error cyclic redundancy"]
description: "Error 0x80070017 is a CRC data-integrity failure. Test your RAM and disk, get clean media, and install without corruption."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-on-laptop.webp"
faqs:
  - q: "What does error 0x80070017 mean?"
    a: "It means ERROR_CRC, a cyclic redundancy check failure: data read from a disk, download, or memory did not match its checksum. The bytes are not what they are supposed to be, so the installer refuses to use them and reports the mismatch."
  - q: "Is 0x80070017 always a hardware problem?"
    a: "Not always, but often. Corrupt downloads and bad media cause it too. The pattern matters: a single failure on one download suggests the file itself, while repeated CRC errors across different files strongly suggest RAM or disk problems instead. Let the pattern guide your testing order."
  - q: "How is 0x80070017 different from 0x80070570?"
    a: "Both signal corrupt data. 0x80070017 specifically reports a CRC checksum mismatch, usually tied to storage or memory reads, while 0x80070570 is the broader file-corrupt code. The diagnostic approach is similar: verify the file first, then test the hardware. Skipping the hardware tests is how this error becomes a data-loss story."
  - q: "Can I still use my laptop with this error appearing?"
    a: "Yes, for now, but treat recurring CRC errors as a warning. Back up your important files promptly, because the same corruption hitting update files today can hit your documents tomorrow if the disk or RAM is genuinely failing. Back up today, not someday."
---

Error 0x80070017 is the cyclic redundancy check failure — the computer's way of saying the data it read does not match the checksum that proves it is intact. Somewhere between the source and the installer, bytes got mangled, and the integrity check caught it.

CRC errors are the canary in the hardware coal mine. A single occurrence on a downloaded file is usually just a bad download. But when CRC failures repeat across different updates, different files, or different days, the odds tilt hard toward failing RAM or a dying drive, because those are the components every byte passes through.

The diagnostic order matters enormously here. Verify the easy, replaceable things first — the download, the USB stick — and then test the components you cannot re-download: memory and storage.

A checksum is a promise: these bytes are exactly what the sender sent. Error 0x80070017 means the promise was broken, and the break happened somewhere between Microsoft's servers and your installer. The steps below walk the byte's journey backward — from the file on your disk, through memory, to the download — testing each leg until the liar is found.

## Why this happens

- **Corrupted download.** A damaged transfer delivers files whose checksums do not match.

- **Failing RAM.** Bad memory corrupts data as it passes through, failing CRC checks on otherwise good files.

- **Dying hard drive or SSD.** Bad blocks and failing flash corrupt stored data, tripping CRC on read.

- **Bad installation media.** A failing USB drive or scratched disc feeds corrupt setup files.

- **Overclocked or unstable memory.** Aggressive RAM timings, including enabled XMP profiles, can cause intermittent corruption.

- **Overheating components.** Heat-induced instability in RAM or the storage controller corrupts data under load.

- **Corrupt existing system files.** Damaged files already on the system fail checks when updates try to build on them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Re-download on a stable connection

Rule out the file first. A fresh download over a stable wired or strong Wi-Fi connection, with the cache cleared, eliminates transit corruption. If possible, download the same update on a different machine and compare hashes; matching checksums prove the server copy is fine and the corruption is local.

1. Launch an admin Terminal and execute `net stop wuauserv` followed by `net stop bits`.
2. Delete everything in C:\Windows\SoftwareDistribution\Download.
3. Restart the services and retry the download on the most stable connection available.

If the re-downloaded package arrives intact but still refuses to install, the problem has moved past the download stage — our guide to [updates that fail to install](/articles/how-to-fix-windows-update-fails-to-install-on-windows-11/) picks up from there.

### Fix 2: Fix 2: Test the RAM thoroughly

Memory is the prime hardware suspect for recurring CRC errors. Run the extended test, not just the quick pass. MemTest86's default four passes catch the vast majority of faults; let it complete rather than stopping after the first pass looks clean.

1. Press Win + R, type `mdsched.exe`, and choose Restart now and check for problems.
2. Press F1 during the test and select Extended for a deeper scan.
3. Any reported errors mean the RAM must be replaced. Also try disabling XMP in BIOS as a test, since unstable overclocks cause identical symptoms.

### Fix 3: Fix 3: Scan the disk surface

A full surface scan finds the bad blocks behind storage-side CRC failures. This takes time but gives a definitive answer about the drive. A drive that passes chkdsk but shows CRC errors in SMART is still suspect; the controller can mangle data that the platters or flash themselves store correctly.

1. Open Terminal as administrator and run `chkdsk C: /f /r`.
2. Schedule it for the next restart and let the full scan complete.
3. Back up immediately if bad sectors are found; the drive is living on borrowed time.

### Fix 4: Fix 4: Check drive health with SMART data

SMART attributes reveal a drive's self-reported health: reallocated sectors, pending sectors, and CRC error counts. Rising numbers confirm hardware failure. Keep the old ISO file until the new media proves itself; if the new download also fails checks, you will want the original for comparison.

1. Open an admin Terminal and run `wmic diskdrive get status` for a quick pass or fail.
2. For detail, use your SSD manufacturer's toolbox or a SMART reader to check reallocated and pending sector counts.
3. Replace any drive with failing SMART attributes before trusting it with updates.

### Fix 5: Fix 5: Use fresh installation media

For setup-time CRC errors, the USB stick is a frequent villain. Flash drives fail in ways that corrupt large sequential reads exactly like this. DISM with an explicit /Source from a mounted ISO is the escalation when online repair reports it cannot find source files.

1. Download a new ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Write it to a different, known-good USB drive, using a direct laptop port.
3. Retry the installation.

### Fix 6: Fix 6: Repair system files

If the corruption is in the existing installation, DISM and SFC restore the damaged files from known-good sources. After the clean download succeeds, re-enable the antivirus before doing anything else; the test window should be minutes, not hours.

1. In an admin Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`, restart, and retry the update.

### Fix 7: Fix 7: Reduce system instability factors

Heat and aggressive memory settings cause the intermittent corruption that is hardest to pin down. Cooling the system and calming the RAM often stops the errors. If disabling XMP stops the errors, the RAM is not necessarily bad; it may simply need slightly relaxed timings or a BIOS update for stability at its rated speed.

1. Clean dust from vents and confirm fans spin up under load.
2. Disable XMP or memory overclocking in BIOS as a diagnostic step.
3. Retry the update with the system cool and stock. For the broader file-corruption cousin of this error, our [0x80070570 guide](/articles/how-to-fix-windows-update-error-0x80070570-on-laptop/) covers the full diagnostic funnel, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official checks.

## Closing

Error 0x80070017 is a checksum failure, and checksums do not lie: either the file was bad or the hardware mangled it. Re-download once, then test RAM and disk without delay, because recurring CRC errors are hardware's early warning. Back up first, diagnose second, replace third. For the related file-corruption error, see our [0x80070570 walkthrough](/articles/how-to-fix-windows-update-error-0x80070570-on-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official diagnostic guidance.
