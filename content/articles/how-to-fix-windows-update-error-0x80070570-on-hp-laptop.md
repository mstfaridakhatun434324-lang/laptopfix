---
title: "How to Fix Windows Update Error 0x80070570 on an HP Laptop (7 Tested Fixes)"
slug: how-to-fix-windows-update-error-0x80070570-on-hp-laptop
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows update", "error 0x80070570", "hp laptop", "windows 11", "troubleshooting"]
description: "Error 0x80070570 means corrupted files are blocking updates on your HP laptop. These 7 fixes find the corruption — bad download, disk errors, or faulty RAM — and repair it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070570 mean?"
    a: "It means Windows detected corrupted data — a file that failed its integrity check — during an update and stopped rather than install the corruption. The damage can be in the downloaded package, on the disk, or in RAM. The repair sequence re-downloads, checks the disk, tests memory, and repairs system files in that order."
  - q: "How do I know if my RAM is the problem?"
    a: "Run Windows Memory Diagnostic (mdsched.exe). RAM-caused corruption is intermittent and affects large operations like updates disproportionately. If the diagnostic reports errors, replace the faulty module — no software repair can fix hardware that corrupts data in transit. Intermittent faults are the hardest to catch, so never skip the full test pass."
  - q: "Can a dying SSD cause this error?"
    a: "Yes. A failing SSD returns corrupted data on reads, which surfaces as checksum failures during updates. HP's storage diagnostic and chkdsk with the /r flag detect this. If bad sectors or read errors appear, back up immediately and replace the drive — it will only get worse."
  - q: "Why re-download when the troubleshooter exists?"
    a: "Because the troubleshooter fixes configuration, not damaged package bytes. If the downloaded .msu or staged payload is corrupt, only a fresh download replaces those bytes. The cache rename forces Windows to fetch everything anew instead of resuming from damaged partial files."
---

Error 0x80070570 on an HP laptop is Windows' file-corruption alarm: during an update, the system tried to read a file — from the download, the disk, or memory — and the data did not match what was expected. The update halted rather than install garbage. It is the operating system refusing to build on a rotten foundation.

The corruption can live in three places, and the fix depends on which: a bad download (re-fetch it), a damaged disk (repair or replace it), or faulty RAM (test and replace it). HP laptops see the RAM variant more than most because a marginal memory module corrupts exactly the large sequential reads that updates perform.

This guide is structured as an elimination: rule out the download first, then the disk, then memory, with repairs at each stage. Do not skip the diagnostics — guessing wrong here wastes hours.

## Why this happens

- **Corrupted update download:** The package arrived damaged — bad mirror, interrupted transfer, or proxy mangling.
- **Failing system drive:** Bad sectors or a dying SSD corrupting files the update needs to read.
- **Faulty RAM:** Marginal memory corrupting data during the large reads updates perform.
- **File-system damage:** Logical corruption from improper shutdowns or crashes.
- **Damaged component store:** Servicing files corrupted by earlier interrupted updates.
- **Antivirus quarantine damage:** Security software removing or altering files mid-operation.
- **Overheating during reads:** Thermal throttling causing read errors on marginal hardware.
- **Aging installation media:** Corrupted ISO or USB when the update path involves installation media.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-download the update cleanly

Rule out the simplest cause first: a damaged package. Force a completely fresh download. If the troubleshooter itself misbehaves, see [How to fix driver updates failing in windows update step by step](/articles/how-to-fix-driver-updates-failing-in-windows-update-step-by-step/) for a dedicated walkthrough.

1. In Terminal (Admin), run: net stop wuauserv, then net stop bits.
2. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
3. Run: net start wuauserv, then net start bits.
4. Check for updates and let the full download complete without interruption.

### Fix 2: Run the Windows Update troubleshooter

Catches configuration issues riding alongside the corruption and repairs what it can automatically.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the laptop.
4. Retry the update.

### Fix 3: Check the disk with chkdsk and HP diagnostics

Determine whether the drive itself is corrupting files. HP's built-in diagnostics plus chkdsk cover hardware and file system; drive guidance is on [HP's official support site](https://support.hp.com/us-en).

1. Restart, press F2, and run HP's storage diagnostic.
2. Back in Windows, open Terminal (Admin) and run: chkdsk C: /f /r
3. Allow the full scan — the /r pass takes a while but finds bad sectors.
4. If either test fails, back up immediately; the drive is the root cause.

### Fix 4: Test the RAM with Windows Memory Diagnostic

Faulty RAM is the sneaky cause of 0x80070570. The built-in diagnostic catches most failures.

1. Press Windows key + R, type mdsched.exe, and press Enter.
2. Choose Restart now and check for problems.
3. Let the test complete — it takes 15 to 30 minutes.
4. If errors are reported, the RAM module needs replacement before updates can succeed.

### Fix 5: Repair the component store with DISM and SFC

Fixes corruption in the servicing files themselves. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents these repair tools.

1. In Terminal (Admin), run: DISM /Online /Cleanup-Image /RestoreHealth
2. Follow with: sfc /scannow.
3. Restart the laptop.
4. Retry the update and watch for 0x80070570.

### Fix 6: Install from freshly downloaded media

When the corruption involves installation media or a stubborn package, a fresh [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com) download plus manual install bypasses the damaged path.

1. Download a fresh Windows 11 ISO from Microsoft.
2. Note the failing KB number from Update history.
3. Install the KB manually from the Microsoft Update Catalog.
4. Verify success in Update history.

### Fix 7: In-place upgrade for deep corruption

Replaces all system files from pristine sources when corruption runs too deep for targeted repair, keeping your files and apps.

1. Back up irreplaceable data first.
2. Run Windows 11 setup from fresh installation media, keeping files and apps.
3. Complete the upgrade.
4. Confirm updates install cleanly afterward.

### Fix 8: Set up early-warning health monitoring

Corruption has causes, and causes give warnings — if you watch for them. A dying drive whispers before it screams: SMART warnings, occasional chkdsk repairs, updates failing with corruption codes. Faulty RAM hints too: random application crashes, occasional blue screens with different stop codes each time. The monitoring routine below turns those whispers into actionable alerts, so the next corruption source gets caught at the warning stage instead of the 0x80070570 stage. HP's built-in diagnostics make this easy: they are already on the machine, they test storage and memory, and running them twice a year is fifteen minutes that can save your data.

1. Twice a year, boot HP PC Hardware Diagnostics (F2 at startup) and run the storage and memory tests.
2. Once a year, run chkdsk C: /f and review its summary for repaired errors or bad sectors.
3. Take SMART warnings seriously: one warning means back up that day, not next month.
4. Keep the laptop cool and ventilated — heat accelerates both drive and memory degradation.
5. Maintain a real backup of irreplaceable files, separate from the laptop, updated monthly at minimum.
6. At the first repeated corruption symptom, run the full diagnostic battery before attempting software repairs.

## Closing

Once 0x80070570 is resolved, protect against recurrence on your HP laptop: keep the machine cool and ventilated during updates, shut down properly instead of forcing power off, and run the memory diagnostic promptly if you ever see random corruption symptoms again. If related errors appear, see [How to fix windows update troubleshooter not working on laptop](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-laptop/) and [How to fix metered connection blocking windows update](/articles/how-to-fix-metered-connection-blocking-windows-update/) — corruption rarely travels alone, and systematic elimination finds every instance.
