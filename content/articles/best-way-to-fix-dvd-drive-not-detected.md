---
title: "The Best Way to Fix a DVD Drive Not Detected in Windows"
slug: "best-way-to-fix-dvd-drive-not-detected"
date: "2026-09-28"
categories: ["drivers"]
tags: ["dvd drive", "optical drive", "windows 11", "device manager", "troubleshooting"]
description: "DVD drive missing from File Explorer? Fix the corrupted registry filters, driver issues, and BIOS settings that hide optical drives."
thumbnail: "/images/thumbs/best-way-to-fix-dvd-drive-not-detected.webp"
faqs:
  - q: "Why is my DVD drive not showing in File Explorer?"
    a: "The most common cause is corrupted UpperFilters or LowerFilters registry entries left by disc-burning software. Other causes include a disabled drive in the BIOS, a loose SATA connection, or a failed drive. The registry filter fix resolves the majority of cases where the drive vanished after a software change."
  - q: "How do I fix a DVD drive not in Device Manager?"
    a: "If the drive is missing from Device Manager too, check the BIOS first: if the BIOS does not see it, Windows never will. Reseat the SATA and power connections if the drive is accessible. If the BIOS sees it but Windows does not, delete the UpperFilters and LowerFilters registry values and restart."
  - q: "Can a Windows update remove my DVD drive?"
    a: "Updates do not usually remove the drive, but they can corrupt the filter drivers that disc software installs, which has the same visible effect. If the drive disappeared right after an update or after installing burning software, the registry filter cleanup below is the fix to try first."
  - q: "Is it safe to delete UpperFilters and LowerFilters?"
    a: "Yes, when done carefully. These values belong to third-party filter drivers, and Windows rebuilds what it needs on restart. Export the registry key as a backup first, delete only those two values under the CD-ROM class key, and leave everything else untouched. Disc software may need reinstalling afterward."
---

You open File Explorer to play a DVD, and the drive is simply gone. Not malfunctioning, not erroring, just absent, as if the laptop never had an optical drive. Device Manager may show it with a warning, or may not show it at all.

Disappearing DVD drives are a Windows classic with a well-known culprit: the UpperFilters and LowerFilters registry entries that disc-burning software installs. When those filters corrupt, Windows hides the entire drive. Hardware causes exist too, but software is guilty most of the time. USB device detection problems follow similar logic, as our [USB not recognized guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) explains.

Start with the registry filter fix, which resolves the majority of cases, then work through the BIOS and hardware checks.

## Why this happens

- **Corrupted UpperFilters or LowerFilters entries:** Leftover filter drivers from burning software block the drive from loading.
- **The drive is disabled in the BIOS:** A BIOS reset can switch the SATA port or the optical drive itself off.
- **A loose SATA or power connection:** Vibration and heat cycles loosen internal connectors over time.
- **A failed optical drive:** Laser assemblies and drive electronics do wear out, especially on older laptops.
- **Conflicting disc software:** Multiple burning suites can install competing filters that break each other.
- **Corrupted CD-ROM class driver:** The generic cdrom.sys driver can be damaged by updates or malware.
- **A dead SATA port:** Rare, but ports and cables fail, particularly after rough handling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Delete the UpperFilters and LowerFilters registry values

This is the famous fix for vanishing optical drives, and it works because the corrupt filters are what hide the drive from Windows. Back up the key first, then remove the two values.

1. Press Windows + R, type regedit, and press Enter to open the Registry Editor.
2. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}.
3. Right-click the key and choose Export to back it up.
4. In the right pane, delete the UpperFilters and LowerFilters values if they exist.
5. Close the editor and restart the laptop, then check File Explorer.

### Fix 2: Uninstall the drive in Device Manager

If the drive appears in Device Manager with a warning, a clean uninstall forces Windows to redetect it with fresh settings on the next boot.

1. Open Device Manager and expand DVD or CD-ROM drives.
2. If the drive is missing, choose View and then Show hidden devices.
3. Right-click the drive and choose Uninstall device.
4. Restart the laptop and let Windows redetect the hardware.
5. Check File Explorer for the drive letter.

### Fix 3: Check the BIOS for the optical drive

The BIOS sees hardware before Windows does. If the BIOS does not list the drive, no Windows fix can help, and you have a connection or hardware problem.

1. Restart and enter the BIOS setup.
2. Look at the storage or device list for the optical drive entry.
3. If it is absent, check that the SATA port is enabled in the BIOS settings.
4. Save and exit, then boot Windows and recheck.
5. If the BIOS sees it but Windows does not, return to the registry filter fix.

### Fix 4: Reseat the drive connection

On laptops with removable optical drives or accessible bays, a loose connection is a quick physical fix. Power down fully before touching anything internal.

1. Shut down the laptop, unplug it, and remove the battery if possible.
2. Locate the optical drive bay, usually secured by a single screw on the bottom.
3. Slide the drive out, inspect the connector for dust or damage, and reseat it firmly.
4. Reassemble and boot into the BIOS to confirm the drive is detected.
5. If reseating fails, test the drive in another compatible laptop if you can.

### Fix 5: Remove conflicting disc-burning software

Multiple burning suites install competing filter drivers, and their conflicts are a prime source of corrupted UpperFilters entries. Removing the software you do not use prevents recurrence.

1. Open Settings, then Apps, and list your disc-burning and virtual-drive software.
2. Uninstall suites you no longer use, keeping at most one.
3. After uninstalling, repeat the registry filter check to clear leftover entries.
4. Restart and verify the drive appears and reads discs.
5. Reinstall your preferred burning software fresh if you still need it. General driver hygiene, as covered in our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/), helps avoid related issues.

### Fix 6: Test the drive with a bootable disc

Booting from a disc bypasses Windows entirely. If the drive boots a disc, the hardware is fine and Windows is definitely the problem; if it cannot, the drive itself has likely failed.

1. Create a bootable DVD or use a Windows installation disc.
2. Restart and open the boot menu, usually F12 or Esc.
3. Select the optical drive as the boot device.
4. If it boots, focus your efforts on Windows-side fixes above.
5. If it cannot read the disc, the drive's laser or electronics have probably failed and need replacement.

### Fix 7: Reinstall the IDE/ATAPI controller drivers

The optical drive talks to Windows through the SATA controller driver. If that controller driver is corrupt, the drive can vanish even with perfect registry filters and healthy hardware. Reinstalling the controller rebuilds the entire communication path from scratch.

1. Open Device Manager and expand IDE ATA/ATAPI controllers.
2. Right-click each SATA controller entry and choose Uninstall device.
3. Do not tick driver deletion for controllers; just uninstall the device instance.
4. Restart the laptop and let Windows redetect the controllers automatically.
5. Check File Explorer for the DVD drive after the restart completes.

## Closing

A missing DVD drive is usually Windows hiding healthy hardware behind corrupted filter entries, not a dead drive. The registry cleanup brings most of them back within minutes, and the controller reinstall covers the rest of the software side. Only when the BIOS cannot see the drive either should you reach for a screwdriver or a replacement.
