---
title: "DVD Drive Not Detected on HP Laptop? Fix It"
slug: how-to-fix-dvd-drive-not-detected-on-hp-laptop
date: 2026-09-03
categories: ["drivers"]
tags: ["dvd drive not detected", "hp laptop dvd", "optical drive missing", "cd drive disappeared"]
description: "DVD drive missing from your HP laptop? Fix detection with filter driver cleanup, BIOS checks, and HP hardware diagnostics."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected-on-hp-laptop.webp"
faqs:
  - q: "Why did my DVD drive disappear from Windows?"
    a: "The classic cause is corrupted UpperFilters/LowerFilters registry entries left by disc-burning or virtual-drive software — they block Windows from loading the optical drive driver. Deleting those filter values restores detection in most cases. Less often, the drive is disabled in the BIOS or its SATA connection failed."
  - q: "Is the filter driver fix safe for the registry?"
    a: "Yes, when limited to the specific CD/DVD device class key. You are deleting only the UpperFilters and LowerFilters values inside the optical-drive class GUID, which disc software recreates if needed. Back up the key first via File > Export, and do not delete anything outside that key."
  - q: "Can a Windows update remove my DVD drive?"
    a: "It can hide it. Updates sometimes reinstall storage drivers in ways that conflict with the optical drive, or reintroduce broken filter entries. If the drive vanished right after an update, the registry filter fix and a storage driver reinstall are the first things to try before suspecting hardware."
  - q: "How do I know if the DVD drive itself is dead?"
    a: "Check the BIOS: if the optical drive appears in the BIOS device list but not Windows, it is a Windows problem. If it is absent from the BIOS too, and reseating (on models with removable drives) does not help, the drive or its connector has failed. HP's boot-time diagnostics can also test the optical drive directly."
---

Optical drives are legacy hardware now, but plenty of HP laptops still ship with them — and Windows still occasionally loses them. The drive vanishes from File Explorer and Device Manager, discs inserted do nothing, and the machine behaves as if the bay were empty.

The good news: a truly dead optical drive is rare. The overwhelmingly common cause is a Windows filter-driver problem in the registry, a ten-minute fix once you know where to look. The steps below start there, then cover the BIOS, driver, and hardware checks for the stubborn cases.

## Why this happens

- **Corrupted UpperFilters/LowerFilters registry entries** from burning or virtual-drive software — the top cause.
- **Optical drive disabled in the BIOS** or dropped from the boot device list.
- **Storage controller driver issue** after a Windows update.
- **Loose drive connector** — the drive's SATA/power connection worked free.
- **Failed drive hardware** — laser or controller board dead, common on old drives.
- **Drive letter conflict** — Windows assigned no letter or a conflicting one.
- **Group policy or software disabling** optical drives on managed machines.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Delete the filter registry entries

This is the classic fix and it works more often than anything else. Open regedit and navigate to the CD/DVD device class key, then delete the UpperFilters and LowerFilters values. Back up the key first with File > Export. Reboot, and Windows redetects the drive. Microsoft documents this procedure in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open regedit and go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}`.
2. Back up the key via File > Export.
3. Delete the UpperFilters and LowerFilters values if present.
4. Reboot and check File Explorer for the drive.

### Fix 2: Check the BIOS for the drive

Reboot into the BIOS (F10 on most HP laptops) and look at the device list. If the optical drive appears here but not in Windows, the problem is Windows-side — continue with the driver fixes. If it is missing from the BIOS too, skip to the hardware checks, because no Windows fix can detect a drive the firmware cannot see.

1. Reboot and press F10 to enter the BIOS.
2. Check the device/boot list for the CD/DVD drive.
3. Present in BIOS but not Windows = software problem.
4. Absent from BIOS = hardware problem; skip ahead.

### Fix 3: Reinstall the storage drivers

In Device Manager, expand DVD/CD-ROM drives (if the drive appears with a warning) and IDE ATA/ATAPI controllers. Uninstall the ATA channel entries and restart — Windows rebuilds the storage stack and often picks the optical drive back up. The same storage-stack rebuild helps other optical-drive variants — see [DVD drive fixes for Windows 11](/articles/how-to-fix-dvd-drive-not-detected-on-windows-11/). If the drive shows with a yellow warning, uninstall it specifically, deleting its driver.

1. Open Device Manager.
2. Under IDE ATA/ATAPI controllers, uninstall each ATA Channel.
3. If the DVD drive appears with a warning, uninstall it too.
4. Restart and let Windows redetect everything.

### Fix 4: Assign or fix the drive letter

Sometimes the drive is detected but invisible because Windows gave it no drive letter. Open Disk Management (diskmgmt.msc) — if the optical drive appears without a letter, right-click it and assign one. This is a quick check that resolves the 'drive exists but I cannot see it' variant.

1. Press Win + X and open Disk Management.
2. Look for the CD/DVD drive in the volume list.
3. Right-click it > Change Drive Letter and Paths > Add.
4. Assign a free letter and check File Explorer.

### Fix 5: Run HP hardware diagnostics

HP's built-in diagnostics can test the optical drive directly. Reboot and press F2 (or Esc then F2) to open HP PC Hardware Diagnostics, and run the optical drive test. A pass means the drive is electrically alive and the problem is Windows; a fail means hardware. HP's diagnostic tools are on [HP support](https://support.hp.com/us-en) if you need the latest version.

1. Reboot and press F2 to open HP diagnostics.
2. Run the optical drive / storage test.
3. Note pass or fail and any failure code.
4. A fail code goes straight to HP support for service options.

### Fix 6: Reseat or replace the drive

On HP models with a removable optical drive (often secured by a single screw on the bottom), power off, remove the screw, slide the drive out, and reseat it firmly. If reseating fails and diagnostics fail, the drive is dead — replacement DVD drives for these bays are inexpensive and model-specific. While you are at it, consider whether an external USB DVD drive is the simpler answer for occasional use.

1. Power off and remove the battery if removable.
2. Remove the retaining screw and slide the drive out.
3. Reseat it firmly and replace the screw.
4. If still undetected, replace the drive or use an external USB one.

### Fix 7: Check boot detection and test the laser

If the drive is detected but cannot read discs, test with a commercially pressed DVD rather than a burned one — a weakening laser often still reads pressed discs while failing on burned media, which tells you the drive is dying rather than misconfigured. Also check the HP boot menu (press Esc at startup, then F9): a drive visible there but invisible in Windows confirms a Windows-only problem. As a final workaround, an external USB DVD drive bypasses the internal bay entirely for little money.

1. Test the drive with a commercially pressed DVD or CD.
2. Check the HP boot menu (Esc > F9) for the drive's presence.
3. If visible at boot but not in Windows, stay on the software fixes.
4. Consider an external USB DVD drive as the pragmatic permanent answer.

## Closing

A missing DVD drive on an HP laptop is a registry filter problem until proven otherwise — the UpperFilters/LowerFilters cleanup restores detection in the majority of cases. The BIOS check is the great divider: drive visible in firmware means Windows can be fixed, invisible means hardware. And given how rarely optical drives are used today, an external USB drive is a perfectly respectable permanent answer. For the update-triggered variant of this fault, see [DVD drive missing after a Windows update](/articles/how-to-fix-dvd-drive-not-detected-after-windows-11-update/).
