---
title: "How to Fix Windows Update Error 0x80070057 on a Laptop"
slug: "how-to-fix-windows-update-error-0x80070057-on-laptop"
date: "2026-10-11"
categories: ["windows-update"]
tags: ["0x80070057", "invalid-parameter", "windows-update", "windows-11"]
description: "Error 0x80070057 ('the parameter is incorrect') blocks Windows updates. Here's what causes it and the repairs that actually clear it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070057-on-laptop.webp"
faqs:
  - q: "What does 'the parameter is incorrect' mean for Windows Update?"
    a: "It means a component in the update process received data it could not interpret — a malformed registry value, a corrupted update metadata entry, or an unexpected disk layout value. The most famous trigger is the System Reserved partition being too small or full for the update's needs. The error is the system's generic way of saying an input did not make sense."
  - q: "Is 0x80070057 related to the System Reserved partition?"
    a: "Very often, yes. Windows updates stage boot files on the System Reserved partition, and if it is too small or completely full, the operation fails with this parameter error. This is especially common on older machines upgraded through multiple Windows versions, where the reserved partition was created tiny by older installers. Checking its free space is one of the first things to do."
  - q: "Can third-party partition tools cause this error?"
    a: "They can contribute. Resizing or moving partitions with third-party tools sometimes leaves the partition layout in a state Windows Update does not expect, triggering parameter errors during the boot-file staging phase. If the error appeared after partition work, that is a strong lead. Built-in Disk Management is safer for layout changes on the system disk."
  - q: "Will resetting Windows fix 0x80070057?"
    a: "A reset usually fixes it because it rebuilds the partition layout and servicing state from scratch, but it is overkill as a first response. The targeted fixes in this guide — clearing the reserved partition, repairing the component store, resetting update components — resolve the error without touching your files and apps. Keep reset as the final option."
---

Error 0x80070057, "the parameter is incorrect," is one of the more misleading update errors because it sounds like you did something wrong. You did not. It means some part of the update machinery received a value it could not work with — most famously, a System Reserved partition with no room to stage boot files, but also corrupted update metadata or damaged registry entries.

Because the error has a few distinct root causes, the fixes below are ordered to check the most common one first: the reserved partition. From there they move through metadata repair and component resets, ending with the manual install bypass.

‘The parameter is incorrect’ is Windows at its most cryptic — it sounds like a programming error, not something a laptop owner should ever see. But in the update context it has a very concrete usual meaning: the update tried to stage boot files onto the System Reserved partition and found it too small or completely full. That tiny partition, created years ago by an older Windows installer, becomes the bottleneck for a modern cumulative update. It is the single most common root cause of this error, which is why checking it comes first in the sequence below, ahead of the metadata and component repairs.

## Why this happens

- **Full System Reserved partition:** The update cannot stage boot files when the small reserved partition has no free space.
- **Undersized reserved partition:** Very old installations created 100 MB reserved partitions that modern updates cannot use.
- **Corrupt update metadata:** Damaged entries in the update data store feed invalid parameters to the installer.
- **Damaged registry values:** Corrupted Windows Update registry keys pass bad configuration to the engine.
- **Third-party partition changes:** Resizing tools can leave a layout the updater does not expect.
- **Corrupt SoftwareDistribution cache:** Damaged cached files produce parameter errors during verification.
- **Language pack conflicts:** Mismatched or partially installed language packs sometimes trigger this code.
- **Failing drive sectors:** Bad sectors in critical areas corrupt the data the updater reads.

## How to fix it

Work through these in order — diagnose first, then act.

When you open Disk Management in Fix 1, look carefully at all the small partitions on your system disk, not just C:. The System Reserved or EFI partition is typically a few hundred megabytes, has no drive letter, and shows as nearly full — that combination is the fingerprint of this error’s most common cause.

### Fix 1: Check the System Reserved partition

This is the most common root cause — verify it before anything else.

1. Press Win + R, type `diskmgmt.msc`, and press Enter.
2. Locate the System Reserved partition on your system disk and note its size and free space.
3. If it is 100 MB or completely full, you have likely found the problem.
4. Do not delete it — the fixes below address the space issue safely.

### Fix 2: Free space on the System Reserved partition

Clearing font and log debris from the reserved partition often resolves the error.

1. Open Command Prompt as administrator.
2. Assign a drive letter: `mountvol Y: /s` to mount the EFI system partition, or use Disk Management to letter the reserved partition.
3. Navigate to the mounted drive and look for unneeded files such as old logs or duplicate fonts — delete only obvious junk.
4. Remove the drive letter afterward with `mountvol Y: /d` or via Disk Management.
5. Retry Windows Update.

### Fix 3: Run the Windows Update troubleshooter

The automated tool repairs several metadata issues behind this error.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply recommended fixes.
3. Restart the laptop.
4. Check for updates again.

### Fix 4: Clear the update cache and metadata

Damaged metadata is the second most common cause after the reserved partition.

1. In an admin Command Prompt, run `net stop wuauserv` and `net stop bits`.
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download` and the DataStore folder.
3. Run `net start wuauserv` and `net start bits`.
4. Restart and retry the update.

### Fix 5: Reset the Windows Update components fully

Rebuild the entire update infrastructure including the catalog store.

1. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with `net start` for each.
4. Reboot and test Windows Update.
5. For the broader component-reset technique, see our [0x80070002 repair guide](/articles/how-to-fix-windows-update-error-0x80070002-on-laptop/), which covers the same foundation.

### Fix 6: Repair the component store

Deep servicing corruption feeds bad parameters to the installer.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt.
2. Follow with `sfc /scannow`.
3. Restart after both complete.
4. Retry the update.

### Fix 7: Remove problematic language packs

Partially installed language packs are a documented trigger for this code.

1. Open Settings, Time & language, Language & region.
2. Remove any language packs you do not use, especially ones showing install errors.
3. Restart the laptop after removal.
4. Retry Windows Update with only your needed languages installed.

### Fix 8: Install the update manually

Bypass the parameter validation that keeps failing in the automatic path.

1. Identify the failing KB number from update history.
2. Download the matching .msu from the Microsoft Update Catalog.
3. Run the standalone installer and restart when prompted.
4. Verify installation in update history.
5. Our guide to [manually installing Windows updates](/articles/how-to-manually-install-windows-update-on-windows-11/) details each Catalog step.

If your reserved partition is the undersized 100 MB variety from a very old installation, the long-term fix is a clean install of current Windows 11, which creates properly sized system partitions from the start. That is a bigger project than this error usually requires — the space-freeing in Fix 2 resolves most cases — but it is worth knowing for machines that fight every update. Short of that, keep the reserved partition clear of debris and avoid third-party partition resizers on the system disk; the built-in Disk Management is far less likely to leave a layout that confuses the updater. For the reserved-partition-adjacent error 0x800F0922, see our [dedicated guide](/articles/how-to-fix-windows-update-error-0x800f0922-on-laptop/).

## Closing

Error 0x80070057 rewards a targeted approach: check the System Reserved partition first, since that is the culprit more often than not, then work through metadata and component repairs. It is a fixable, well-understood error — not a mystery, despite what the message text suggests.
