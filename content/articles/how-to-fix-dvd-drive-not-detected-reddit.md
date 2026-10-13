---
title: "DVD Drive Not Detected? Reddit-Tested Fixes for Windows Laptops"
slug: how-to-fix-dvd-drive-not-detected-reddit
date: 2026-09-06
categories: ["drivers"]
tags: ["dvd drive", "optical drive", "not detected", "device manager", "troubleshooting"]
description: "A DVD drive missing from File Explorer and Device Manager is usually a driver, registry, or connection problem. Here are the fixes Redditors confirm actually work."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected-reddit.webp"
faqs:
  - q: "Why is my DVD drive not showing up in File Explorer or Device Manager?"
    a: "The most common cause is a missing or corrupted CD/DVD driver, often after a Windows update removes the driver stack. Registry filter corruption (UpperFilters/LowerFilters) and a loose SATA connection are the next most likely culprits. If the drive also spins up when you insert a disc, the hardware is fine and the issue is software."
  - q: "Can a Windows update cause the DVD drive to disappear?"
    a: "Yes. Windows 10 and 11 feature updates have repeatedly dropped optical drive support by removing or misconfiguring the cdrom.sys driver stack. Many users report the drive vanishing immediately after an update. In those cases reinstalling the driver or adding the missing registry values usually restores the drive without any hardware work."
  - q: "Is my DVD drive dead if the tray does not open?"
    a: "Not necessarily. The tray eject button often relies on Windows drivers, so a missing driver can disable it. Try the manual eject pinhole: straighten a paperclip, insert it into the tiny hole next to the tray, and push gently. If the tray slides out and the disc spins, the hardware is likely fine."
  - q: "Should I replace the DVD drive or use an external USB drive instead?"
    a: "If the drive shows no power, makes no sound, and is invisible in BIOS, internal replacement is warranted but only if you actually use discs. For most users an external USB DVD drive is cheaper and easier: no disassembly, no firmware concerns, and it works on any machine you own now or later."
---

A DVD drive that vanishes from File Explorer is one of those problems that feels hardware-fatal but usually isn't. The drive was working fine last week, now it is gone — no drive letter, no icon in Device Manager, and sometimes not even a response when you press the eject button. Before you order a replacement, work through the real causes, because the community-tested fixes below bring most "dead" drives back to life.

The classic pattern reported on Reddit is this: a Windows update installs, the laptop reboots, and the optical drive is simply gone. Other times the drive spins but Windows refuses to acknowledge it. In both cases the failure almost always sits in the software layer — driver stack, registry filters, or power management — rather than in the laser assembly itself. That is good news, because software failures are free to fix.

## Why this happens

- **Windows update removed the driver stack:** Feature updates have repeatedly dropped or broken the cdrom.sys driver binding, leaving the drive invisible even though the hardware is healthy.
- **Corrupted registry filter values:** UpperFilters and LowerFilters entries under the CD/DVD drive class key are notoriously corrupted by uninstalls of burning software, and Windows then hides the drive entirely.
- **BIOS no longer sees the drive:** A loose SATA connector or a dead drive will be absent from the BIOS/UEFI device list. No BIOS entry means no operating system can see it, full stop.
- **Drive disabled in Device Manager:** Windows sometimes marks the device as disabled after driver conflicts. It stays hidden under a collapsed category or with a grayed icon rather than throwing an obvious error.
- **AHCI or SATA controller driver issue:** The optical drive hangs off the same storage controller as your SSD. If that controller driver is corrupted, the drive drops off the bus with it.
- **Power management cut the port:** Aggressive USB/SATA power-saving settings can power down the drive bay. On laptops the internal optical drive is particularly vulnerable after resume from sleep.
- **Failed firmware or dead hardware:** Drives do wear out. Laser diodes degrade, and drives that make clicking or grinding noises and appear nowhere are usually finished.
- **Third-party filter drivers from old software:** Old disc-burning or virtual-drive tools install filter drivers that survive uninstalls in broken form, blocking Windows from enumerating the hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the hardware is visible in BIOS

1. Restart the laptop and press the BIOS key (usually **F2**, **Del**, or **F12**) repeatedly during boot.
2. Look for a storage or device list — the DVD drive should appear by model name (for example, "HL-DT-ST DVDRAM" or similar).
3. If it appears here but not in Windows, the problem is 100% software. Skip to Fix 3.
4. If it is missing from BIOS too, power off, remove the drive from its bay if your model allows it, clean the contacts, and reseat it firmly. Recheck BIOS before touching anything else.

### Fix 2: Look for the drive in Device Manager's hidden devices

1. Press **Win + X** and open **Device Manager**.
2. Click **View → Show hidden devices**.
3. Expand **DVD/CD-ROM drives**. A grayed-out drive here means Windows disabled it — right-click and choose **Enable device**.
4. If you see a drive with a yellow warning icon, right-click it, choose **Uninstall device**, then restart. Windows will attempt a fresh install on boot, similar to the approach in this [USB device not recognized guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

### Fix 3: Delete the corrupted UpperFilters and LowerFilters registry entries

1. Press **Win + R**, type `regedit`, and press Enter. Click **Yes** on the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}`.
3. In the right pane, look for **UpperFilters** and **LowerFilters** values.
4. Right-click each one you find and choose **Delete**. Confirm the deletion.
5. Restart the laptop. This is the single most-reported fix for drives that disappeared after a Windows update, and it also applies to the [DVD drive not detected after an update](/articles/how-to-fix-dvd-drive-not-detected-after-windows-11-update/) scenario.

### Fix 4: Reinstall the storage controller driver

1. In Device Manager, expand **IDE ATA/ATAPI controllers**.
2. Right-click the SATA AHCI controller (often named "Intel Chipset SATA/PCIe RST Premium Controller" or similar) and choose **Uninstall device**.
3. Do **not** check "delete the driver software for this device" unless you have the chipset driver installer downloaded.
4. Restart. Windows reinstalls the controller and re-enumerates everything attached to it, including the optical drive.

### Fix 5: Run the hardware troubleshooter and force re-enumeration

1. Press **Win + R**, type `msdt.exe -id DeviceDiagnostic`, and press Enter to launch the hardware troubleshooter.
2. Let it scan and apply any recommended fixes.
3. Open an elevated Command Prompt and run `pnputil /scan-devices` to force Windows to re-enumerate the hardware bus.
4. Open Device Manager again, click **Action → Scan for hardware changes**, and check whether the drive reappears.

### Fix 6: Disable power saving on the drive's controller

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Expand **USB settings** and **PCI Express → Link State Power Management**, and set both to **Off**.
3. In Device Manager, under **IDE ATA/ATAPI controllers**, right-click the SATA controller → **Properties → Power Management** tab, and uncheck "Allow the computer to turn off this device to save power."
4. Restart and test with a disc inserted before the system has a chance to sleep.

### Fix 7: Test with an external USB DVD drive to confirm hardware failure

1. Borrow or buy a cheap external USB DVD drive — most cost less than a tank of gas.
2. Plug it into a rear or direct USB port (not through a hub) and wait for Windows to install it.
3. If the external drive works immediately, your internal drive has failed at the hardware level.
4. Check your warranty status with the manufacturer's support page — Dell, HP, and Lenovo all have warranty lookup tools. For deeper Windows driver guidance, the official [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents current recovery options.

## Closing

A missing DVD drive is almost never a dead drive. Work the list from the BIOS check down through the registry fix, and the drive reappears in the vast majority of cases. Only reach for your wallet — or an external USB drive — after the hardware checks confirm the internal drive is truly gone.
