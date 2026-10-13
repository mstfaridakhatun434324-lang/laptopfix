---
title: "How to Fix Windows Update Error 0x80070017 on Windows 11 24H2"
slug: "how-to-fix-windows-update-error-0x80070017-in-windows-11-24h2"
date: 2026-09-14
categories: ["windows-update"]
tags: ["0x80070017", "crc error", "windows update error", "windows 11 24h2", "windows update"]
description: "Error 0x80070017 is a CRC data error: the update files failed their checksum. Fix it by purging the bad download, checking disk health, and forcing a clean re-download on Windows 11 24H2."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-in-windows-11-24h2.webp"
faqs:
  - q: "What does Windows Update error 0x80070017 mean?"
    a: "Error 0x80070017 is a CRC (cyclic redundancy check) failure — the data read from the update package does not match its checksum, meaning the file is corrupted. Practically, the update downloaded to your PC is damaged: the bits on disk differ from what Microsoft published. Windows detects this during verification and refuses to install, reporting the CRC error instead of risking a broken installation."
  - q: "Is 0x80070017 a hard drive problem?"
    a: "It can be, but usually is not — the most common cause is simply a bad download, especially over unstable Wi-Fi. However, if the error repeats across different updates after you clear the cache, the disk becomes the prime suspect: bad sectors corrupt large files reliably. Run CHKDSK and check the drive's SMART health; if the drive is healthy, look at RAM and the network connection next."
  - q: "How is 0x80070017 different from 0x80070570?"
    a: "Both indicate corrupted update files, but they fail at different checks: 0x80070017 is a CRC checksum mismatch detected when reading the data, while 0x80070570 (ERROR_FILE_CORRUPT) is the filesystem reporting a file or directory as corrupted and unreadable. In practice the fixes overlap heavily — clear the cache, check the disk, re-download — but 0x80070017 leans more toward download and memory issues, 0x80070570 more toward filesystem damage."
  - q: "Will I lose data fixing error 0x80070017?"
    a: "No. Every fix for this error targets the update cache, system files, or hardware diagnostics — none of them touch your documents, photos, or installed programs. The most destructive step in the sequence is the in-place repair install, and even that is designed to keep your files and apps. Still, keeping a current backup before any major system repair is always sensible."
---
Error 0x80070017 is Windows Update's way of saying the numbers do not add up. Every update package carries checksums, and when Windows reads the downloaded files and the math fails — a CRC error — it stops cold rather than install corrupted code. On Windows 11 24H2 you will usually see this on cumulative updates and feature updates, the big multi-gigabyte packages where a single flipped bit breaks the whole checksum.

Nine times out of ten the story is mundane: a Wi-Fi hiccup truncated the download, or a previous partial download got stitched together badly. But when the error survives a fresh download, the investigation has to go deeper — to the disk sectors the file landed on, the RAM it passed through, and the storage drivers doing the writing. That is the order this guide follows: cheap software fixes first, hardware verification for the stubborn cases.

Before you start, note the exact KB number that failed in **Settings > Windows Update > Update history** — you will need it for the manual-install fallback in Fix 7. And if the update seems to download forever without ever erroring, our guide to [updates stuck downloading in 24H2](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) covers that sibling problem.

## Why this happens

- **Truncated or interrupted download** — Wi-Fi drops, VPN reconnects, or the laptop sleeping mid-download produce a partial package whose checksum cannot possibly match. Resuming a broken partial file repeats the failure.

- **Corrupted files in SoftwareDistribution** — The download cache accumulates damaged fragments across retries. Windows keeps trying to use them instead of starting clean, so the CRC error persists.

- **Bad sectors on the disk** — Large update packages span many sectors; one bad sector in the wrong place corrupts the file every time it is written there, producing repeat CRC failures on otherwise good downloads.

- **Unstable RAM** — Memory errors flip bits as data streams through, so the file written to disk differs from what arrived over the network. This mimics a download problem perfectly.

- **Outdated storage drivers** — Buggy AHCI, NVMe, or Intel RST drivers can corrupt large sequential writes — exactly the pattern of a multi-gigabyte update package landing on disk.

- **Antivirus mangling the download** — Real-time scanners that modify or quarantine parts of the package mid-download break the checksum just as surely as a network glitch.

- **Failing download due to proxy or VPN** — Corporate proxies and some VPNs interfere with the range requests Windows Update uses, delivering subtly corrupted or incomplete byte ranges.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the update cache and force a fresh download

This is the fix that resolves most 0x80070017 cases: delete every trace of the damaged download so Windows cannot reuse it, then pull a clean copy.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete everything inside **C:\Windows\SoftwareDistribution\Download**.
4. Run `net start wuauserv` and `net start bits`, then **Check for updates**. Prefer a wired connection for the re-download if possible.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter detects stuck download states and corrupted cache metadata that manual deletion can miss, and it resets the BITS queue for good measure. When the update downloads but then will not install at all, our [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-after-windows-11-update/) covers that next phase.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Apply any fixes it recommends and restart the laptop.
4. Check for updates again and watch whether the download completes cleanly this time.

### Fix 3: Check the disk with CHKDSK

If a fresh download fails CRC again, the disk is suspect. CHKDSK's surface scan finds bad sectors and maps them out so files stop landing on damaged media.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r`.
2. Type **Y** to schedule the scan and restart the laptop.
3. Allow the scan to complete fully — the percentage may sit still for long stretches on large drives.
4. After rebooting, clear the update cache once more (Fix 1) and retry, so no file written to a bad sector survives.

### Fix 4: Test system memory for errors

Recurring CRC failures with a healthy disk point at RAM. Bit flips in memory corrupt downloads invisibly, and the symptom is always 'the file is bad' no matter how many times you re-download.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Select **Restart now and check for problems**.
3. At the blue test screen, press **F1** and choose the **Extended** test for a thorough pass.
4. If any errors appear, test RAM sticks individually to find the faulty module and replace it.

### Fix 5: Update storage and chipset drivers

Storage driver bugs that corrupt large writes are rare but real, and they cluster around major Windows builds like 24H2. Fresh chipset and NVMe drivers eliminate this variable.

1. Identify your laptop's exact model, then visit the manufacturer's support site (Dell, HP, or Lenovo) for the latest chipset and storage drivers.
2. Alternatively, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect outdated Intel storage and chipset drivers automatically.
3. Install the updates and restart.
4. Clear the update cache and attempt the Windows update again on the fresh driver stack.

### Fix 6: Repair system files with SFC and DISM

A damaged servicing stack can corrupt packages during the staging phase, after a perfect download. Repairing the component store removes this failure point.

1. Open an elevated Command Prompt.
2. Run `sfc /scannow` and wait for completion.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart, then retry the update. Details on both tools are in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Install the KB manually from the Microsoft Update Catalog

When Windows Update's own download machinery is the problem, sidestep it: fetch the package as a normal file download and install it directly.

1. Note the failing KB number from **Update history**.
2. Search for it at the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the x64 .msu.
3. Disconnect from any VPN, temporarily pause third-party antivirus, and run the .msu.
4. Restart when prompted and verify the KB is listed as installed.

## Closing

A CRC error is Windows refusing to install something it cannot verify — which is exactly what you want it to do. Give it a genuinely fresh download on verified-healthy disk and memory, and 0x80070017 stops appearing.
