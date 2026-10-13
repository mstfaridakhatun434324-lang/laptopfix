---
title: "DVD Drive Not Detected in Windows? Bring It Back"
slug: how-to-fix-dvd-drive-not-detected
date: 2026-09-18
categories: ["drivers"]
tags: ["dvd drive", "optical drive", "not detected", "device manager"]
description: "DVD drive vanished from File Explorer on your Windows laptop? Fix the missing optical drive with registry, driver, and BIOS checks."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected.webp"
faqs:
  - q: "Why did my DVD drive disappear from Windows?"
    a: "The classic cause is corrupted UpperFilters/LowerFilters registry values in the CD-ROM class key — usually left behind by disc-burning software that was uninstalled. Windows then fails to load the drive's driver stack and hides the device entirely. Deleting those two registry values and restarting restores the drive in the majority of cases."
  - q: "My laptop doesn't have a DVD drive — is something wrong?"
    a: "No — most laptops built after roughly 2016 simply don't include optical drives; manufacturers removed them to make machines thinner. If your laptop never had a visible disc tray, nothing is missing. This guide is for machines that physically have a drive (or had one detected before) that Windows no longer shows."
  - q: "Can a Windows update remove my DVD drive?"
    a: "It can hide it. Updates sometimes replace the storage controller driver or reset filter drivers in a way that breaks the optical drive's driver chain. If the drive vanished right after an update, check Device Manager for the drive with a warning icon, roll back the storage/IDE controller driver, and check the UpperFilters/LowerFilters registry values."
  - q: "The drive is detected but won't read discs. Is it the laser?"
    a: "Often it's just a dirty lens — optical drives are dust magnets. Try a lens-cleaning disc first (a few dollars). If cleaning doesn't help and the drive spins but never reads, the laser assembly is likely worn out — optical drives are consumable parts with finite laser life. Replacement internal drives are cheap; external USB DVD drives are even cheaper and work on any laptop."
---

The disappearing DVD drive is a classic Windows ailment: the drive is physically in the laptop, the tray opens, but File Explorer shows nothing and Device Manager may not list it either. Nine times out of ten this is the famous UpperFilters/LowerFilters registry corruption — leftover filter drivers from burning software that break the whole CD-ROM driver chain when the software is removed.

The sequence: check Device Manager visibility, clear the filter registry values, fix the controller driver, then verify in BIOS. If your drive appears but misbehaves after updates, see [DVD drive not detected after Windows Update](/articles/how-to-fix-dvd-drive-not-detected-after-windows-11-update/) for the update-specific variant.

## Why this happens

- **Corrupt UpperFilters/LowerFilters registry values**: Uninstalled burning software (Nero, Roxio, Alcohol 120%) leaves filter entries that break the driver chain.
- **Storage controller driver updated**: The IDE/ATAPI or SATA controller driver changed, and the optical drive didn't survive the transition.
- **Drive disabled in Device Manager**: Accidentally disabled, or disabled by a "debloat" script.
- **BIOS/UEFI doesn't see the drive**: Loose SATA connection (on laptops with removable drives) or the drive disabled in BIOS.
- **Windows Update driver mismatch**: New controller driver incompatible with the old optical drive's expectations.
- **Dead drive hardware**: Failed laser or controller board — the drive draws power (tray opens) but never enumerates.
- **Third-party filter drivers**: Virtual drive software (Daemon Tools, Virtual CloneDrive) installing filters that conflict.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Device Manager visibility

Find out how Windows currently sees (or doesn't see) the drive.

1. Press **Win + X** > **Device Manager** and expand **DVD/CD-ROM drives**. If your drive is listed with no warning, the issue may be File Explorer display, not detection — skip to Fix 5.
2. If it's listed with a yellow warning, right-click > **Properties** and read the error code — Code 19, 31, 32, 39, and 41 all point at the filter-driver problem (Fix 2).
3. Click **View** > **Show hidden devices** — a greyed-out drive means it's disabled; right-click > **Enable device**.
4. If the DVD/CD-ROM category is missing entirely, expand **IDE ATA/ATAPI controllers** and check for warnings there — the controller driver is the next suspect (Fix 3).
5. Note the exact state before changing anything — it determines which fix applies.

### Fix 2: Delete the UpperFilters and LowerFilters values

The famous fix — resolves the majority of vanished-drive cases.

1. Press **Win + R**, type `regedit`, approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}` — this is the CD-ROM device class key. (Back up first: **File** > **Export** the key.)
3. In the right pane, look for **UpperFilters** and **LowerFilters** values. Right-click each and **Delete** them. If only one exists, delete just that one; if neither exists, this isn't your problem — move on.
4. Close Registry Editor and **restart** the laptop (not shut down — restart, so Fast Startup doesn't skip driver reinitialization).
5. After reboot, check **Device Manager** > **DVD/CD-ROM drives** and File Explorer — the drive should be back. You'll need to reinstall any disc-burning software whose filters you deleted if you still use it.

### Fix 3: Fix the IDE/ATAPI controller driver

When the controller underneath the drive is the problem.

1. In **Device Manager**, expand **IDE ATA/ATAPI controllers**.
2. Right-click each **Standard SATA AHCI Controller** (or Intel Chipset SATA entry) > **Properties** > **Driver** tab.
3. If the problem started after an update, click **Roll Back Driver**.
4. Otherwise, right-click > **Uninstall device** (do not check delete driver), then **Action** > **Scan for hardware changes** to reinstall the controller fresh.
5. Restart and check whether the DVD drive reappears. Controller reinstallation re-enumerates all attached SATA devices, including the optical drive. The controller driver is part of the chipset package — see [installing chipset drivers](/articles/how-can-i-install-chipset-drivers/) if controller problems persist.

### Fix 4: Check BIOS/UEFI for the drive

Confirm the firmware sees the hardware.

1. Restart into BIOS/UEFI (**F2**/**Del**/**F10**).
2. Look at the storage/device inventory — most BIOS screens list connected SATA devices. Your DVD drive should appear by model name.
3. If it's absent from BIOS, the drive isn't communicating at hardware level: on laptops with removable optical bays, power off, remove and reseat the drive module.
4. Check for any **SATA port** or **optical drive** enable/disable options and ensure they're enabled.
5. If BIOS sees it but Windows doesn't after Fixes 1–3, the problem is purely Windows-side — consider the system-file repair in Fix 7.

### Fix 5: Assign a drive letter and check File Explorer

For drives detected by Windows but invisible in Explorer.

1. Press **Win + X** > **Disk Management** and look for the CD-ROM entry (usually Disk with "CD-ROM" label, often without a drive letter).
2. Right-click it > **Change Drive Letter and Paths** > **Add** > assign a letter like E: or F:.
3. In File Explorer, check **This PC** — the drive should now appear. Insert a disc to confirm it reads.
4. If Disk Management doesn't show the drive at all, you're back to detection-level troubleshooting (Fixes 2–4).
5. Also check File Explorer > **View** > **Show** > **Hidden items** isn't the issue — optical drives aren't hidden by that setting, but empty drives can be hidden by the "Hide empty drives" folder option: **File Explorer** > **...** > **Options** > **View** tab > uncheck **Hide empty drives in the Computer folder**.

### Fix 6: Remove virtual drive and burning software conflicts

Third-party filter drivers are repeat offenders.

1. Uninstall virtual drive software (Daemon Tools, PowerISO virtual drives, Virtual CloneDrive) temporarily — their filter drivers sit in the same chain.
2. Uninstall old disc-burning suites you no longer use, then recheck the UpperFilters/LowerFilters values from Fix 2 — uninstallers often leave them behind, so verify manually.
3. Restart after each uninstall and check Device Manager.
4. If you need virtual-drive functionality, reinstall *one* current tool after the physical drive is working — modern versions are better behaved.
5. Keep a note of which software you removed in case the drive vanishes again after reinstalling it.

### Fix 7: Repair system files and test the hardware

The final software pass, then a hardware verdict.

1. Open an elevated terminal and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. After repair, re-verify the registry values from Fix 2 haven't been recreated by something.
3. Hardware test: boot from a Linux live USB (Ubuntu works) and check whether the drive appears there. Visible in Linux but not Windows = Windows problem, keep digging. Invisible in both = dead drive.
4. Also test with the drive's tray: if the tray won't even open with the eject button (no power), check the drive's power/SATA connection or the bay seating.
5. Replacement reality: internal laptop DVD drives are $20–40 and usually one screw + slide-out; external USB DVD drives are $25–35 and work on any machine with zero disassembly. For most people the external drive is the pragmatic answer. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional optical-drive troubleshooting if needed.

## Closing

The vanished DVD drive is one of Windows' most solved problems — the UpperFilters/LowerFilters registry fix has been rescuing optical drives for twenty years, and it still works because the underlying driver architecture hasn't changed. Clear the filters, fix the controller, and the drive almost always comes home.
