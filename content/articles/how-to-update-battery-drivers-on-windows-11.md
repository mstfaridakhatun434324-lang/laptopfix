---
title: "How to Update Your Battery Drivers on Windows 11"
slug: how-to-update-battery-drivers-on-windows-11
date: 2026-09-28
categories: ["battery"]
tags: ["drivers", "Windows 11", "Device Manager"]
description: "Fix battery issues on Windows 11 by updating or reinstalling battery drivers. Complete walkthrough from quick refresh to chipset driver updates."
thumbnail: "/images/thumbs/how-to-update-battery-drivers-on-windows-11.webp"
faqs:
  - q: "How do I reinstall the battery driver on Windows 11?"
    a: "Open Device Manager with Win + X, expand Batteries, right-click Microsoft ACPI-Compliant Control Method Battery, choose Uninstall device, then click Action and Scan for hardware changes. Windows reinstalls the driver automatically."
  - q: "Can outdated drivers stop my battery from charging?"
    a: "Yes. A corrupted or mismatched battery driver can block charge commands, freeze the percentage display, or make Windows fail to detect the battery entirely — even though the battery hardware is perfectly fine."
  - q: "Should I update chipset drivers too?"
    a: "Absolutely. The chipset driver manages the hardware interface that the battery driver uses. Many battery problems blamed on the battery driver are actually fixed by updating the chipset and power management drivers from the laptop manufacturer."
  - q: "Where do I download the correct drivers?"
    a: "From your laptop manufacturer's support site — Dell, HP, Lenovo, ASUS, Acer, or MSI — using your exact model number. Manufacturer drivers are tuned for your hardware; generic Windows drivers are only a fallback."
---

Windows 11 handles battery drivers a little differently under the hood than Windows 10, but the troubleshooting playbook is the same: the driver is the messenger between Windows and your battery's firmware, and when the messages get garbled you see frozen percentages, phantom "not charging" states, and disappearing batteries.

The 24H2 update in particular has been rough on battery drivers for some models, so if your battery issues started right after an update, drivers are suspect number one. This guide takes you from the 30-second refresh through the full driver-stack rebuild. The Windows 10 version of these steps lives in our [Windows 10 battery driver guide](/articles/how-to-update-battery-drivers-on-windows-10/).

## Why this happens

- **Feature updates swap drivers.** Windows 11 upgrades (especially 24H2) sometimes replace manufacturer-tuned battery drivers with generic versions that misreport or fail to initialize.
- **Corrupted driver state.** Failed updates, forced shutdowns, and disk errors can corrupt driver files or their registry configuration.
- **Outdated chipset drivers.** The chipset driver owns the embedded-controller interface. If it lags behind the BIOS or Windows build, battery communication breaks even with a perfect battery driver.
- **Duplicate device entries.** Upgrades can leave stale battery device entries that conflict with the live ones.
- **Manufacturer utility conflicts.** Battery utilities from Lenovo, ASUS, or Dell install filter drivers that occasionally clash with Windows' native stack after updates.
- **Firmware/driver mismatch.** A new BIOS that changes the battery interface needs matching drivers — running old drivers against new firmware causes exactly these symptoms.

## How to fix it

Work through these in order, from quickest to most thorough.

### Fix 1: Quick refresh with Scan for hardware changes

Start with the fastest possible reset of the device state.

1. Press **Win + X** and open **Device Manager**.
2. Expand the **Batteries** category.
3. From the menu bar, click **Action**, then **Scan for hardware changes**.
4. Give it a minute and watch the taskbar battery icon — if the status corrects, you are done.

### Fix 2: Uninstall and reinstall the battery driver

The standard fix for a corrupted battery driver.

1. In **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** and select **Uninstall device**.
3. If the laptop lists two battery entries (common on dual-battery ThinkPads), uninstall both.
4. Click **Action > Scan for hardware changes** — Windows redetects the battery and reinstalls the driver.
5. Restart with the charger plugged in and verify the battery status and percentage.

### Fix 3: Pull driver updates from Windows Update

Check Microsoft's catalog for newer drivers, including optional ones.

1. Open **Settings** (**Win + I**), go to **Windows Update**, and click **Check for updates**.
2. Click **Advanced options**, then **Optional updates**, and expand **Driver updates**.
3. Install any updates mentioning battery, chipset, system, or your manufacturer's name.
4. Restart and retest. For manually hunting specific driver versions, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you search by hardware ID.

### Fix 4: Install manufacturer chipset and power drivers

The most impactful step — do not skip it.

1. Find your exact model number (bottom sticker or **Settings > System > About**).
2. Visit the manufacturer's support site and open **Drivers & Downloads** for your model, filtering for **Windows 11**.
3. Download the latest **Chipset** driver plus any **Power Management**, **ACPI**, or **ATK Package** drivers offered.
4. Install the chipset driver first, restart, then install the power management driver.
5. These govern the hardware path the battery driver depends on — this step resolves a large share of post-24H2 battery issues.

### Fix 5: Remove ghost battery devices

Stale entries from before the update can interfere.

1. In **Device Manager**, click **View > Show hidden devices**.
2. Expand **Batteries** and uninstall any grayed-out entries by right-clicking and choosing **Uninstall device**.
3. Check **System devices** for grayed-out ACPI or battery-related entries and remove those too.
4. Restart. Windows rebuilds a clean device list on boot.

### Fix 6: Update the BIOS to match

If the BIOS is newer than the drivers (or vice versa), bring them into alignment.

1. Download the latest **BIOS** for your exact model from the manufacturer's support site.
2. With the AC adapter connected and all apps closed, run the update and do not touch the machine until it restarts itself.
3. After booting, open **Device Manager** and confirm the battery devices show no warning icons.

### Fix 7: Verify with a battery report and rollback option

Confirm the fix and know your fallback.

1. In an administrator **Terminal**, run `powercfg /batteryreport` and open the report.
2. Verify **Design Capacity**, **Full Charge Capacity**, and **Cycle Count** look sensible and the taskbar percentage matches.
3. If a specific driver update made things worse, roll back: in **Device Manager**, right-click the device, choose **Properties**, open the **Driver** tab, and click **Roll Back Driver**.
4. If driver work does not resolve it and the battery itself is suspect, move on to the hardware checks in our [plugged in, not charging guide](/articles/how-do-i-fix-laptop-plugged-in-not-charging/).

### Fix 8: Reset power plans and use System Restore

If the driver trouble began right after a specific update, roll the system back or reset its power configuration.

1. Press **Win + R**, type `rstrui`, and check whether a restore point exists from before the problem started. If so, run System Restore — it reverts drivers and system files without touching your personal files.
2. If no restore point exists, reset the power plans: open an administrator **Terminal** and run `powercfg -restoredefaultschemes`. This rebuilds the Balanced, Power Saver, and High Performance schemes from scratch.
3. Restart, then reinstall the battery driver once more using Fix 2 so it initializes against the clean power configuration.
4. Recheck the battery icon and run `powercfg /batteryreport` to confirm the driver is reading the battery correctly.

## Closing

On Windows 11, battery driver trouble almost always follows an update — and the fix almost always follows the same script: reinstall the ACPI battery driver, update the chipset drivers from the manufacturer, and verify with a battery report. Keep the manufacturer's chipset driver current as a matter of routine and you will avoid most of these headaches entirely. When the BIOS sees the battery fine but Windows 11 does not, drivers are guilty until proven innocent.
