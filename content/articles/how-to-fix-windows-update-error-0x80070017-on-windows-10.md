---
title: "Fix Windows Update Error 0x80070017 on Windows 10: Redownload Cleanly"
slug: how-to-fix-windows-update-error-0x80070017-on-windows-10
date: 2026-09-11
categories: ["windows-update"]
tags: ["windows update", "0x80070017", "windows 10", "crc error", "data error"]
description: "Windows 10 error 0x80070017 signals failed data integrity checks. Clear corrupt sources, verify hardware, and get a clean install of the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070017 mean on Windows 10?"
    a: "A cyclic redundancy check failed — data read back did not match its checksum. The corruption can come from the download, the local update cache, bad disk sectors, or faulty RAM. The update installer correctly refuses to use the damaged data."
  - q: "Why does the same update fail CRC every time I retry?"
    a: "Retries reuse the same corrupt cache or hit the same bad disk sectors, so the result repeats identically. You must clear the cache and verify the storage before retrying — otherwise you are testing the same broken inputs. New inputs are the whole point: fresh cache, verified storage, then retry."
  - q: "How do I test whether my RAM is causing 0x80070017?"
    a: "Run the built-in Windows Memory Diagnostic (mdsched.exe) and let the full test complete. Memory faults corrupt data silently during downloads and installs, producing CRC failures with no network or disk problem. Let every pass finish; interrupted tests miss intermittent faults."
  - q: "Is 0x80070017 on Windows 10 fixed the same as Windows 11?"
    a: "The diagnosis is identical; only the menus differ. Our [Windows 11 0x80070017 guide](/articles/how-to-fix-windows-update-error-0x80070017-on-windows-11/) covers the same repair sequence with Windows 11 navigation for mixed environments. The hardware tests are the same on both, so either guide's results transfer."
---

Windows 10 reports error 0x80070017 when a cyclic redundancy check fails — the data's checksum does not match its contents, so the update installer rejects it. It is the digital equivalent of a tamper-evident seal: the seal is broken, and the installer will not proceed. What the code does not tell you is where the seal broke, and that is the entire troubleshooting task.

The candidates are few but consequential. A damaged download or poisoned cache is the common, harmless case — fixed in minutes. Bad disk sectors are the serious case — back up promptly. Faulty RAM is the sneaky case — invisible until tested. The procedure below works through them from easiest to most significant, with a definitive test at each step so you act on findings, not guesses.

If the CRC failures keep returning across unrelated updates, skip ahead mentally to the hardware tests — recurring corruption is hardware until proven otherwise.

## Why this happens

- **Transfer damage**: Corrupt download failing integrity verification.
- **Cache poisoning**: Damaged fragments reused across retries.
- **Bad sectors**: Disk damage corrupting stored files.
- **RAM bit flips**: Memory faults damaging data in flight.
- **Controller faults**: Storage controller corrupting reads or writes.
- **Thermal storage errors**: Overheated drives making write errors.
- **Interrupted writes**: Earlier crashed updates leaving half-written files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Empty the update download cache

Start with the cheapest definitive test: if the corruption lives in the cache, a purge plus a fresh download resolves it completely, and you will know within one update cycle.

1. Open an elevated Command Prompt.
2. Run net stop wuauserv and net stop bits.
3. Delete the contents of C:\Windows\SoftwareDistribution\Download.
4. Run net start wuauserv and net start bits, then check for updates.

### Fix 2: Run Disk Cleanup for space and debris

Cramped disks corrupt more: the filesystem strains to place large update files, and old damaged debris lingers. Cleaning up addresses both at once.

1. Run Disk Cleanup as administrator on C:.
2. Remove Temporary files, Windows Update Cleanup, and Delivery Optimization Files.
3. Confirm at least 20 GB free afterward.
4. Restart, then retry the update.

### Fix 3: Reset the full update components

When a simple cache clear is not enough, reset the whole component set. This also rebuilds the update metadata database, which can itself carry the corruption.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
2. Rename SoftwareDistribution to SoftwareDistribution.old and catroot2 to catroot2.old.
3. Restart all four services.
4. Reboot and run Check for updates.

### Fix 4: Run chkdsk on the system drive

The direct test for the bad-sector hypothesis. Chkdsk's /r pass reads every sector, recovers what it can, and quarantines the dead ones — and its summary tells you whether the drive is healthy or dying.

1. Run chkdsk C: /f /r in an elevated prompt and confirm the reboot scan.
2. Let it complete fully, however long it takes.
3. A few fixed errors is normal wear; growing bad-sector counts mean replace the drive.
4. Back up first if the counts look bad — before any further updates.

### Fix 5: Test memory with Windows Memory Diagnostic

RAM is the invisible corruptor: it damages data during the exact operations updates rely on, leaving no trace in logs. The built-in tester is the way to see it.

1. Press Windows + R, type mdsched.exe, press Enter.
2. Choose Restart now and check for problems.
3. Do not interrupt the test; let all passes complete.
4. Errors mean reseat or replace the memory — then retest before updating.

### Fix 6: Try the manual catalog install

Installing the package by hand from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) takes a completely different download and staging path, which distinguishes path corruption from systemic hardware corruption.

1. Find the KB number in Update history.
2. Download the x64 .msu from the Update Catalog.
3. Install directly and reboot when prompted.
4. Matching CRC failure here confirms the hardware diagnosis — prioritize the disk and RAM findings.

### Fix 7: Consider a repair install for systemic corruption

If SFC finds unfixable damage, chkdsk keeps finding new errors, or corruption appears outside updates too, the Windows installation itself is compromised and needs rebuilding.

1. Back up personal files to external storage first.
2. Mount the Windows 10 ISO and run setup.exe, choosing Keep personal files and apps.
3. After the repair, run sfc /scannow once more to confirm a clean baseline.
4. Resume normal updating; if problems persist on fresh storage, the RAM or drive needs replacement — see [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for clean-install steps.

### Fix 8: Disable overclocking and scan for malware

CRC failures with no disk or network fault point at invisible corruptors: marginal memory timings that fail under sustained hashing, or malware patching downloads in transit. Test both hypotheses directly instead of guessing.

1. In BIOS or UEFI setup, disable XMP/EXPO profiles and any CPU overclocking, returning everything to stock speeds.
2. Boot into Windows and retry the update at stock speeds to test the overclock hypothesis.
3. Run a Microsoft Defender Offline scan from Windows Security > Virus & threat protection > Scan options.
4. If threats are found and removed, clear the update cache once more and retry on the clean system.

## Closing

Windows 10's 0x80070017 is the checksum doing its protective job, and your job is to find what keeps breaking the seal. The cache purge resolves the everyday cases; chkdsk and the memory test resolve the serious ones. Never let recurring CRC errors become background noise — each one is either a trivial cache problem or an early hardware warning, and the tests above tell you which within the hour. Related: the [Windows 11 0x80070017 guide](/articles/how-to-fix-windows-update-error-0x80070017-on-windows-11/) and our [undoing changes stuck guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) for the related stuck-rollback case.
