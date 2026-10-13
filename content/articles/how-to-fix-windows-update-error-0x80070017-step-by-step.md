---
title: "Windows Update Error 0x80070017, Step by Step: Repair the Corrupt Data"
slug: how-to-fix-windows-update-error-0x80070017-step-by-step
date: 2026-10-06
categories: ["windows-update"]
tags: ["0x80070017", "crc error", "windows update error", "data error", "windows 11"]
description: "Error 0x80070017 is a data/CRC error: a file Windows Update needs is corrupt. Follow these steps to clear the cache, verify your drive and memory, and install a clean copy."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070017-step-by-step.webp"
faqs:
  - q: "What is error 0x80070017 in plain language?"
    a: "It means Windows tried to read a file and the file's contents did not match its checksum — a cyclic redundancy check failure. Something damaged the data: a bad download, a corrupt cache, failing RAM, or bad disk sectors. The fix depends on which of those damaged it."
  - q: "Is 0x80070017 dangerous for my files?"
    a: "The error itself does not touch your personal files. But if the underlying cause is a failing drive or bad RAM, those can eventually threaten your data. That is why this guide includes disk and memory checks — not because the update error is dangerous, but because its causes can be."
  - q: "Why does this error appear during Windows installation from USB too?"
    a: "Because the same CRC check runs when setup reads install files. During USB installs, 0x80070017 usually means the USB drive is faulty, the ISO was corrupted during download, or the RAM is bad. Re-creating the USB media with a fresh ISO is the standard fix there."
  - q: "How long do the disk and memory checks take?"
    a: "CHKDSK with the /r flag can take one to several hours on large drives. The Windows Memory Diagnostic standard pass takes roughly 15–30 minutes. Run them when you do not need the laptop, and let each finish uninterrupted for trustworthy results."
---

Error 0x80070017 stops Windows Update with a message about data being corrupt, and unlike vague service errors, this one is telling the truth: a file the update needs failed its integrity check. The question is never whether the data is damaged — it is — but where the damage happened. A download corrupted in transit is a five-minute fix. A drive that corrupts files after they arrive is a hardware replacement. This guide walks the full diagnostic ladder, cheapest and safest first, so you find the real cause instead of guessing.

Read the whole ladder before starting, but work it in order. Each step either fixes the problem or rules out a cause, and the later hardware checks only make sense after the software causes are eliminated. If your laptop is an HP, the [HP-focused 0x80070017 guide](/articles/how-to-fix-windows-update-error-0x80070017-on-hp-laptop/) adds manufacturer-specific driver steps to this same sequence.

A useful mental model for this error: think of the update as a chain of custody. Microsoft's servers hand a file to your network, your network hands it to your RAM, your RAM hands it to your disk, and your disk hands it to the installer \u2014 with a checksum verified at the end. Error 0x80070017 means the checksum failed, but it cannot tell you which handoff damaged the goods. This guide interrogates each handoff in turn, starting with the cheapest to test and ending with the hardware, so the culprit is found by elimination rather than guesswork.

## Why this happens

- **Interrupted or unstable download:** Wi-Fi drops, VPN reconnects, or the laptop sleeping mid-download produce a truncated or scrambled file that fails verification.
- **Poisoned update cache:** Once a corrupt file is cached in SoftwareDistribution, every retry reads the same broken copy and fails identically.
- **Bad disk sectors:** A deteriorating drive corrupts files written to failing sectors — the download arrives fine and reads back damaged.
- **Failing RAM modules:** Memory errors corrupt data as it streams from the network through RAM to disk. Large update payloads are excellent at exposing marginal RAM.
- **Inconsistent component store:** A previously interrupted update leaves the servicing stack in a half-applied state, and the next attempt's files do not line up with what the store expects.
- **Storage driver instability:** Outdated or buggy storage drivers can mishandle large sequential writes, introducing corruption that looks exactly like a bad download.
- **Overzealous disk utilities:** Third-party defragmenters, disk cleaners, or encryption filters that touch files mid-write can alter update payloads.
- **Nearly full system drive:** With almost no free space, large files get written in awkward fragments and truncated pieces, which fail checksums — the same low-space pattern behind [cumulative updates failing repeatedly](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give the download one clean chance

Rule out a transient network glitch before touching the system.

1. Switch to the most stable connection available — Ethernet if possible, otherwise strong Wi-Fi close to the router.
2. Disconnect any VPN and pause large downloads or streaming on the network.
3. Plug in the AC adapter and set the laptop to not sleep for the next hour.
4. In Settings, Windows Update, click Retry. If 0x80070017 returns, the damage is persistent — continue below.

### Fix 2: Purge the update cache completely

This is the highest-yield fix for this error code.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
3. Open C:\Windows\SoftwareDistribution and delete everything inside it.
4. Also delete the contents of C:\Windows\SoftwareDistribution\Download specifically if you want to be thorough — it is inside the folder you just emptied anyway.
5. Restart the three services with `net start` and reboot the laptop.
6. Check for updates to pull a fully fresh copy.

### Fix 3: Repair system files with SFC and DISM

If corruption has spread to protected system files, repair them before retrying.

1. In an elevated Command Prompt, run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart the laptop.
4. Run Windows Update again. If SFC reports corruption it could not fix and DISM also struggles, note that — it is a hint the storage underneath may be unreliable.

### Fix 4: Scan the drive for bad sectors

1. Open an elevated Command Prompt.
2. Run `chkdsk C: /f /r`. Accept the prompt to schedule it at next restart.
3. Restart and let the scan run to completion without interrupting it.
4. Review the summary: a few bad sectors on an old drive can be monitored, but a growing count means replacement time. Back up first, always.

### Fix 5: Test the memory

CRC failures during big downloads are a classic RAM symptom, so test before assuming the drive is at fault.

1. Press Win + R, type `mdsched.exe`, press Enter.
2. Select "Restart now and check for problems".
3. After reboot, open Event Viewer, go to Windows Logs, System, and filter for MemoryDiagnostics-Results.
4. If errors appear, reseat the RAM modules (if accessible) and retest; persistent errors mean replacing the faulty stick.

### Fix 6: Update storage and chipset drivers

1. Identify your storage controller in Device Manager.
2. Get the latest chipset and storage drivers from your laptop manufacturer's support site or via [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel-based systems.
3. Install, restart, and retry the update.

### Fix 7: Manual install from the Microsoft Update Catalog

When the automated pipeline keeps producing corrupt copies, bypass it.

1. Note the failing KB number from Update history.
2. Download the correct package for your Windows version and architecture from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Verify the download completes fully, then run the installer as administrator.
4. Restart when prompted and confirm the update in Update history.

### Fix 8: Retry from a clean boot state

Background software can interfere with downloads in subtle ways.

1. Run `msconfig`, hide all Microsoft services, and disable the rest plus all startup items.
2. Restart into the clean boot state.
3. Clear the update cache once more and retry the update.
4. If it succeeds here but failed normally, re-enable services in halves to isolate the interfering program \u2014 disk utilities and aggressive antivirus are the usual suspects.

## Closing

The 0x80070017 ladder is really a process of elimination across a chain of custody: bad download, bad cache, bad files, bad sectors, bad RAM, bad interference. Most people stop at step two. If you had to go further \u2014 into clean-boot isolation or hardware tests \u2014 you have done something genuinely valuable: you have either repaired real system damage or caught a hardware failure early, and either outcome beats dismissing an update error that keeps coming back.
