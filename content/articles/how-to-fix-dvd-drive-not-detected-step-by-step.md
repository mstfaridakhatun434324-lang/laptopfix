---
title: "How to Fix a DVD Drive Not Detected: Step-by-Step Guide"
slug: how-to-fix-dvd-drive-not-detected-step-by-step
date: 2026-09-30
categories: ["drivers"]
tags: ["dvd drive", "optical drive", "cd drive not detected", "atapi driver", "upperfilters"]
description: "DVD drive not detected in Windows? Fix the missing optical drive with registry filter repairs, driver reinstalls, and BIOS checks, step by step."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected-step-by-step.webp"
faqs:
  - q: "Why did my DVD drive disappear from Windows?"
    a: "The classic cause is corrupted UpperFilters and LowerFilters registry values for the CD/DVD device class, often left behind by uninstalled burning software. Windows then fails to load the optical drive driver and the drive vanishes from File Explorer and Device Manager. Deleting those two registry values is the definitive fix and has worked since Windows 7."
  - q: "Is it safe to delete UpperFilters and LowerFilters?"
    a: "Yes, for the CD/DVD device class key, this is a Microsoft-documented fix. These values belong to third-party filter drivers, and Windows rebuilds what it needs. Back up the registry key first by exporting it. Do not delete filter values from other device class keys unless a specific guide directs you to."
  - q: "My DVD drive shows in BIOS but not Windows — what does that mean?"
    a: "That confirms the drive hardware and its connection are fine, and the problem is purely in Windows' driver stack — almost always the filter driver corruption described above. If the drive is missing from the BIOS too, check the SATA connection or consider hardware failure, since Windows can't see what the BIOS doesn't."
  - q: "Do I need a driver for my DVD drive?"
    a: "No separate driver download is needed. Windows includes the generic cdrom.sys driver for all ATAPI optical drives. When the drive is missing, the fix is repairing Windows' driver stack (filters, device enumeration) rather than finding a driver. Manufacturer sites don't publish optical drive drivers because none are required."
---

A DVD drive that vanishes from Windows — gone from File Explorer, gone from Device Manager — is a Windows driver-stack problem with one of the most famous fixes in PC troubleshooting: the UpperFilters/LowerFilters registry repair. This issue has persisted across Windows versions for over a decade because the underlying mechanism (third-party filter drivers corrupting the optical device class) never changed.

Before the registry work, do the quick BIOS check: if the drive appears in BIOS setup, the hardware is fine and Windows is the problem. If it's missing from BIOS too, you're looking at a connection or hardware issue instead.

## Why this happens

- **Corrupted UpperFilters/LowerFilters:** Uninstalled burning software (Nero, Roxio, Alcohol 120%, Daemon Tools) leaves filter values that block the cdrom driver from loading.
- **Windows update driver stack changes:** Updates can disturb the delicate filter chain for the optical device class.
- **Drive disabled in Device Manager:** The drive entry gets disabled and forgotten, invisible in the normal view.
- **SATA/AHCI driver issues:** The optical drive hangs off the SATA controller; a broken storage controller driver hides it along with everything else on that channel.
- **BIOS SATA mode changes:** Switching between AHCI/IDE/RAID modes can orphan the optical drive's enumeration.
- **Loose SATA/power connection:** On desktops and some laptops, the drive's cable works loose — the drive then vanishes everywhere including BIOS.
- **Failed drive electronics:** Optical drives do die; a dead drive disappears from BIOS and Windows alike.
- **Filter drivers from virtual drive software:** Virtual CD tools install filters that conflict with the physical drive's driver chain.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the drive is visible in BIOS

1. Restart and enter BIOS/UEFI setup.
2. Look at the storage or boot device list for your DVD/CD drive model.
3. **Visible in BIOS** = hardware and connection are fine; the problem is Windows' driver stack. Continue with the fixes below.
4. **Missing from BIOS** = check physical connections (Fix 7) or suspect hardware failure — no Windows fix applies.
5. This thirty-second check determines the entire direction of troubleshooting, so don't skip it.

### Fix 2: Check Device Manager with hidden devices shown

1. Press **Win + X** → **Device Manager** → **View → Show hidden devices**.
2. Expand **DVD/CD-ROM drives** — look for your drive greyed out (disabled) or with a warning.
3. If disabled (down arrow), right-click → **Enable device**.
4. If it shows a warning, note the error code: **Code 19** (registry config damaged) and **Code 39** (driver corrupt/missing) both point to the filter fix in Fix 3.
5. If the category is entirely absent, the driver stack isn't enumerating optical drives at all — the registry repair is your next step. The [hidden devices walkthrough](/articles/best-way-to-enable-hidden-devices-in-device-manager/) details the ghost-cleanup technique.

### Fix 3: Delete the UpperFilters and LowerFilters values

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}` — this is the CD/DVD device class key.
2. **Back up first:** right-click the key → **Export** and save the .reg file somewhere safe.
3. In the right pane, if **UpperFilters** exists, right-click → **Delete**. Do the same for **LowerFilters** if present.
4. Close the registry editor and **restart** the computer.
5. Check File Explorer and Device Manager for the drive. This is the legendary fix for vanishing optical drives — corrupted filter values from old burning software are the cause in the majority of cases. Microsoft documents this exact procedure in their [support articles](https://support.microsoft.com/en-us/windows).

### Fix 4: Uninstall the IDE/ATAPI controller entries

1. In Device Manager, expand **IDE ATA/ATAPI controllers**.
2. Right-click each **ATA Channel** entry and choose **Uninstall device** (leave the controller itself unless the channels don't help).
3. Restart — Windows redetects the channels and re-enumerates attached optical drives.
4. Check for the DVD drive in File Explorer after reboot.
5. This rebuilds the storage channel enumeration that the optical drive depends on, catching cases where the filter fix alone wasn't enough.

### Fix 5: Run the Hardware and Devices troubleshooter

1. Press **Win + R** and run `msdt.exe -id DeviceDiagnostic` to launch the Hardware and Devices troubleshooter.
2. Let it scan and apply any fixes it recommends for the optical drive class.
3. Alternatively, open **Settings → System → Troubleshoot → Other troubleshooters** and run relevant troubleshooters.
4. While automated troubleshooters rarely fix this specific issue outright, they sometimes repair the device metadata and enumeration that accompany filter corruption.
5. If the troubleshooter reports it couldn't identify the problem, continue — the manual fixes here are more targeted.

### Fix 6: Check SATA operation mode in BIOS

1. Enter BIOS setup and find **SATA Operation** or **SATA Mode** (under Advanced or Storage).
2. Note the current mode (AHCI, RAID, or IDE). If it was recently changed — by you, an update, or a reset — that change can orphan the optical drive.
3. **AHCI** is correct for virtually all modern systems. Changing this mode can prevent Windows from booting, so only change it if you know it was altered, and be prepared to change it back.
4. Save and exit, then check for the drive in Windows.
5. If a BIOS reset caused the issue, also verify the boot order still points to your Windows drive before worrying about the DVD drive.

### Fix 7: Reseat the drive's physical connection

1. For desktops: power off, open the case, and reseat both the **SATA data cable** and the **SATA power cable** on the drive. Try a different SATA port on the motherboard.
2. For laptops with removable optical drives (increasingly rare): eject the drive via the release latch, then firmly reinsert it.
3. For external USB DVD drives: try a different USB port (directly on the machine, not a hub) and a different cable — underpowered USB ports cause exactly this vanishing behavior.
4. Power on and check BIOS for the drive before booting Windows.
5. If reseating brings it back in BIOS but Windows still hides it, return to the filter fix — you may have both a connection and a software issue.

### Fix 8: Test the drive's hardware health

1. With the drive visible in BIOS, test it with a known-good disc at the BIOS/boot level if your firmware offers diagnostics.
2. In Windows (once detected), test reading, and if it's a burner, a test burn to a rewritable disc.
3. A drive that appears but can't read any disc — with the lens cleaned — has a failed laser assembly.
4. Try the drive in another computer if possible; failure there confirms hardware death.
5. Replacement internal DVD drives are inexpensive for desktops; for laptops, a USB external DVD drive is the practical replacement. When the drive is one of several [undetected devices](/articles/best-way-to-fix-dvd-drive-not-detected/), suspect the broader storage controller rather than the drive.

## Closing

The vanishing DVD drive is one of Windows' most solved problems: corrupted filter values in the optical device class key, fixed by deleting two registry values and rebooting. The BIOS visibility check at the start tells you whether you're doing registry surgery or checking cables. Either way, the drive doesn't need a driver download — Windows already has the driver; it just needs the broken filters out of its way.
