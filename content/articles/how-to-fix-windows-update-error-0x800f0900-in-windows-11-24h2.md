---
title: "How to Fix Windows Update Error 0x800F0900 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x800f0900-in-windows-11-24h2
date: 2026-09-04
categories: ["windows-update"]
tags: ["windows update", "0x800f0900", "error code", "windows 11", "manifest"]
description: "Error 0x800F0900 means corrupted manifests the XML parser cannot read. Repair the servicing metadata with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0900-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x800F0900 mean?"
    a: "CBS_E_XML_PARSER_FAILURE: Windows' servicing engine tried to read a component manifest and the XML was malformed. Manifests describe every system component, so a corrupted one stops the update before any files change. Disk faults, truncated metadata downloads, or overzealous cleaners are the usual wreckers."
  - q: "How do I confirm the failure is in the metadata stage?"
    a: "Open C:\\Windows\\Logs\\CBS\\CBS.log and search for recent 0x800F0900 entries mentioning XML or manifest parse errors. If the failure lands before any file-copy activity begins, the metadata is the problem — not your network, disk space, or the update package itself."
  - q: "What does DISM RestoreHealth do for this error?"
    a: "It re-downloads clean manifests along with their payload files, directly replacing the XML the parser chokes on. The tool compares your servicing metadata against healthy copies from Windows Update and repairs every damaged record it finds. Allow 15 to 30 minutes on a laptop."
  - q: "The error keeps returning after repairs. Why?"
    a: "Recurring manifest corruption points below the software: a failing drive keeps damaging the metadata area, or bad RAM corrupts files as they are written. Run chkdsk and the Windows Memory Diagnostic. If hardware checks out, a damaged pending-operations file may be re-poisoning the store — the RevertPendingActions repair in this guide clears it."
---

Every Windows update begins with paperwork. Before a single file is copied, the servicing engine reads manifests — XML documents describing each component, its version, and its dependencies. Error 0x800F0900 is what happens when that paperwork is illegible: the XML parser hits a malformed manifest and the whole installation is refused before it starts. Think of it as a building inspector rejecting blueprints with smudged lines — nothing gets built until the plans are readable again.

Laptops running 24H2 meet this in a few familiar ways. A metadata download truncated mid-flight, a disk fault in the metadata region, a cleanup utility that "helpfully" deleted servicing records, or a damaged pending-operations file that poisons every servicing attempt with parse errors.

The reassuring part: the fix targets the metadata, not your data. Your files and programs are never at risk from these repairs — only the servicing records get touched. Below, the repairs move from confirming the diagnosis to rebuilding the damaged records, in order of invasiveness, and you can stop at the first fix that works.

## Why this happens

- **A manifest file is malformed.** Damaged XML in the component store stops the parser cold.
- **Metadata downloaded incomplete.** A truncated transfer left half a manifest where a whole one should be.
- **Disk faults hit the metadata area.** Bad sectors where servicing records live corrupt them silently.
- **A damaged pending-operations file poisons servicing.** A broken pending.xml throws parse errors into every operation.
- **Cleaners deleted servicing records.** Naive tools remove metadata the engine still references.
- **Registry data backing manifests is corrupt.** The registry mirrors some manifest information; damage there has the same effect.
- **Failing RAM corrupted files in memory.** Rare, but bad memory can mangle files as they are being written.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Nail down the failure as a metadata problem

Knowing the stage matters: metadata-stage failures need servicing repairs, not network or disk-space tweaks.

1. Open `C:\Windows\Logs\CBS\CBS.log` in a text editor and search for 0x800F0900 entries from the last day that mention XML or manifest parsing failures.
2. If the failure occurs before any file copying begins, continue below — the metadata is the patient.
3. If failures appear at later stages too, the [24H2 update-failure reference](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) handles the remaining members of the family.

### Fix 2: Have DISM rebuild the servicing metadata

RestoreHealth fetches clean manifests alongside payload files, directly replacing the XML the parser cannot read. This is the single most effective repair for 0x800F0900, and it needs no preparation beyond an administrator prompt and a working internet connection.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` to 100 percent.
2. Follow with `sfc /scannow` for the guarded system files.
3. Restart, then retry the update.

### Fix 3: Clear a poisoned pending-operations file

A broken pending.xml throws parse errors into everything, like a single misfiled form jamming an entire office. Reverting it discards the unfinished operations that keep re-corrupting the metadata, giving the parser a clean set of documents to work with.

1. From the elevated prompt, run `DISM /Image:C:\ /Cleanup-Image /RevertPendingActions`.
2. If it reports that pending actions were reverted, reboot immediately.
3. Retry the update from a clean servicing state.

### Fix 4: Let the troubleshooter have a turn

The Windows Update troubleshooter recognizes metadata-stage symptoms and applies its own safe corrections to the pipeline. Run it before the heavier manual repairs — it is quick, and it sometimes clears exactly this code.

1. Enter Settings > System > Troubleshoot > Other troubleshooters.
2. Start the Windows Update diagnostic and heed its questions.
3. Reboot and validate the update again.

### Fix 5: Reset the update engine's cache

Corrupt cache metadata can masquerade as store damage, sending you chasing the wrong repair. Relocating the cache folders aside compels a fresh download state — if the error vanishes afterward, the store was innocent all along.

1. Cease the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rebadge the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Reboot the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Inspect for updates and observe the result.

### Fix 6: Install the KB package manually

When automatic delivery keeps stumbling on metadata, walk around it: fetch the exact package and install it yourself from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

1. Jot down the KB number from Update history.
2. Hunt that KB on the Catalog and fetch the x64 Windows 11 build.
3. Drive the `.msu` file through its installer, then reboot if asked.

### Fix 7: Lay a fresh Windows over the existing copy

For metadata damage that survives every targeted repair, a fresh servicing layer comes from reinstalling 24H2 over itself with files and apps kept. Use only the ISO from [Microsoft's Windows 11 download portal](https://www.microsoft.com/en-us/software-download/windows11).

1. Load the ISO and execute `setup.exe`.
2. Endorse the license terms, then elect **Keep personal files and apps**.
3. Allot 30 to 90 minutes with several restarts; never sever power mid-run.
4. Corroborate that updates install cleanly afterward.

## Closing

Manifests are paperwork, and paperwork can be reissued: a restored store parses cleanly and updates flow again. If the same corruption keeps reappearing after every repair, treat it as a hardware warning — back up your data and check the drive before the next cumulative update arrives. For updates that then fail at later stages, the [24H2 update-failure reference](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) handles the remaining codes, and [the official Windows support hub](https://support.microsoft.com/en-us/windows) documents the servicing internals in depth. Keep this guide bookmarked too — manifest damage has a habit of recurring on laptops with aging drives, and the same repairs will serve you again. On non-24H2 builds, the laptop edition of this repair covers the same manifest fix with extra focus on updating the servicing stack first. Hitting 0x800F0900 on Windows 10 instead? The [Windows 10 variant](/articles/how-to-fix-windows-update-error-0x800f0900-on-windows-10/) walks the same repairs through the older menus.
