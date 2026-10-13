---
title: "How to Fix Error 0x80070057 on Windows 10 (Parameter Is Incorrect)"
slug: how-to-fix-error-0x80070057-on-windows-10
date: 2026-09-14
categories: ["windows-errors"]
tags: ["0x80070057", "parameter incorrect", "windows update", "windows 10"]
description: "Error 0x80070057 'the parameter is incorrect' on Windows 10? Fix broken updates, backup failures, and disk issues with this ordered guide."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070057-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070057 mean?"
    a: "It means 'the parameter is incorrect' — Windows received an invalid value during an operation. In Windows Update, it usually indicates corrupted update metadata or a damaged SoftwareDistribution cache. In backup, it often means a decimal-symbol locale mismatch or a corrupt backup target. In disk formatting, it can mean partition table problems."
  - q: "Why does this error appear during Windows Backup?"
    a: "The classic backup trigger is a locale issue: if your decimal symbol is set to something other than a period (common in some European locales), the backup tool fails with 0x80070057. Go to Control Panel > Region > Additional settings and set the decimal symbol to a period (.). This single setting fixes a huge share of backup-context cases."
  - q: "Can disk problems cause 0x80070057?"
    a: "Yes. Corrupted file system structures or a damaged partition table can make disk operations fail with 'parameter incorrect.' Running chkdsk and verifying the partition layout in Disk Management are worthwhile steps when the error appears during formatting, partitioning, or backup to a specific drive."
  - q: "Is it safe to rename the SoftwareDistribution folder?"
    a: "Yes, when done with the update services stopped. Windows treats the renamed folder as a backup and creates a fresh one automatically. If anything goes wrong, you can delete the new folder and rename the old one back. It's the standard, Microsoft-documented approach to clearing update cache corruption."
---
Error 0x80070057 — "the parameter is incorrect" — is one of those codes that appears in completely different situations: Windows Update, Windows Backup, disk formatting, even Microsoft Store. The meaning shifts with the context, but the repair approach is consistent: identify the context, fix the corrupted data or wrong setting behind it, and verify.

This guide covers the three main contexts in order of frequency: updates, backup, and disk operations. The first thing to do is classify your situation — were you updating, backing up, or working with disks? That single question picks your starting fix and saves you from working through irrelevant steps. Everything here is safe for your files; the most invasive step is the in-place upgrade at the end, and even that keeps your data.

## Why this happens

- **Corrupted Windows Update cache.** Damaged metadata or cache files make the update engine choke on invalid parameters.
- **Wrong decimal symbol in Region settings.** The famous backup trigger — a comma decimal symbol breaks the backup tool's parsing.
- **Corrupted system files.** Damaged update or backup components produce invalid internal parameters.
- **Disk/file system errors.** Corruption in the file system makes disk operations fail.
- **Damaged update metadata.** Partially downloaded update definitions contain invalid values.
- **Third-party disk tools.** Partition managers that leave the partition table in a non-standard state trigger "parameter incorrect" during format operations.
- **Third-party interference.** AV or "tweaking" tools corrupting the update pipeline.
- **Stuck update metadata.** Partially downloaded update definitions contain invalid values that persist across retries until the cache is cleared.

## How to fix it

Work through these in order, matching your context.

### Fix 1: Reset the Windows Update components

For update-context errors, this is the primary fix.

1. Open **Command Prompt as administrator**.
2. Stop the services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the caches:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services, reboot, and check for updates.
5. If any service fails to stop, restart the PC and retry the sequence — don't rename folders while a service still holds them.
6. After the reboot, give Windows a few minutes before checking for updates so the services fully reinitialize.

### Fix 2: Fix the decimal symbol for backup errors

If 0x80070057 appears during Windows Backup, check this first — it's the classic cause.

1. Open **Control Panel > Clock and Region > Region**.
2. Click **Additional settings** at the bottom.
3. Set the **Decimal symbol** to **.** (a period).
4. Apply, then retry the backup. This fixes the locale-parsing bug that triggers the error in many regions.
5. While in Region settings, also confirm the list separator matches your locale's standard — mismatched separators cause the same class of parsing failures in older backup tools.

### Fix 3: Run the appropriate troubleshooter

Let Windows diagnose its own component.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Run the **Windows Update** troubleshooter for update errors.
3. Apply all recommended fixes and restart.
4. Retest. The troubleshooter also resets service configurations that manual steps might miss.

### Fix 4: Repair system files

Fix corruption in the update and backup components.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Restart and retry the failing operation.
4. Run DISM before SFC — DISM repairs the store SFC draws from. If you need the package manually, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) hosts individual updates.
5. When SFC finds corruption it can't repair, the correct order is DISM first, then SFC again — DISM fixes the store SFC draws from, so the second pass usually succeeds where the first failed.

### Fix 5: Check the disk and partitions

For disk, format, or backup-to-drive contexts.

1. Run `chkdsk C: /f` (and on the target drive letter for backup errors) from an elevated Command Prompt.
2. Open **Disk Management** (`diskmgmt.msc`) and verify the target partition is healthy with a proper file system — RAW or unallocated partitions trigger this error during backup.
3. For external backup drives, try a different USB port and cable — flaky connections corrupt transfers.
4. If the partition table itself is damaged, back up what you can and recreate the partition.

### Fix 6: Remove third-party interference

AV and system utilities can corrupt the pipeline.

1. Fully uninstall third-party antivirus from **Settings > Apps**.
2. Undo any recent "tweaks" from system utility programs, especially ones touching update or region settings.
3. Restart and retest with a clean configuration.
4. Reinstall security software only after confirming the fix. For the sibling error code, see [fixing 0x80070003](/articles/how-to-fix-error-0x80070003-on-windows-10/).

### Fix 7: Manual update install or in-place upgrade

Final options when the pipeline won't heal.

1. Note the failing KB number from update history and download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Run the `.msu` and restart.
3. If manual install also fails with 0x80070057, do an in-place upgrade: run the Media Creation Tool, choose **Upgrade this PC now**, keep files and apps.
4. The in-place upgrade rebuilds the entire update and backup stack cleanly.

## Closing

Error 0x80070057 is a chameleon, but each of its contexts has a signature fix: update cache reset for updates, decimal symbol for backup, chkdsk for disk operations. The mistake is treating it as one problem — match the fix to where you saw it, and what looked like a cryptic system failure turns out to be a five-minute setting or a standard cache clear.

Going forward, the decimal symbol check is worth remembering any time a backup or old control-panel tool throws a parameter error — it's one of those legacy quirks that still bites in specific regions. For the quick-reference version of this error code, see the [dedicated 0x80070057 fix guide](/articles/error-code-0x80070057-fix/). And for update-context errors, the same preventive habits apply as always: don't interrupt updates, keep free space on the system drive, and fix a failing update promptly instead of letting retries pile up. Small habits, far fewer cryptic errors.
