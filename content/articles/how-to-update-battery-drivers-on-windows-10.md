---
title: "How to Update Your Battery Drivers on Windows 10"
slug: how-to-update-battery-drivers-on-windows-10
date: 2026-09-26
categories: ["battery"]
tags: ["drivers", "Windows 10", "Device Manager"]
description: "Update or reinstall your battery drivers on Windows 10 to fix charging issues, wrong percentages, and unrecognized batteries. Step-by-step guide."
thumbnail: "/images/thumbs/how-to-update-battery-drivers-on-windows-10.webp"
faqs:
  - q: "Where are the battery drivers in Windows 10 Device Manager?"
    a: "Open Device Manager (Win + X), expand the Batteries category. You will typically see Microsoft AC Adapter and Microsoft ACPI-Compliant Control Method Battery. The ACPI entry is the one that manages battery communication."
  - q: "Will updating battery drivers fix charging problems?"
    a: "It fixes problems caused by corrupted or outdated drivers — wrong percentages, 'plugged in not charging,' and unrecognized batteries. It will not fix worn-out cells, faulty chargers, or hardware failures."
  - q: "Is it safe to uninstall the battery driver?"
    a: "Yes. Uninstalling the Microsoft ACPI-Compliant Control Method Battery device is safe — Windows reinstalls it automatically on the next hardware scan or restart. Your battery keeps working on firmware-level control meanwhile."
  - q: "How do I update chipset drivers that affect the battery?"
    a: "Download them from your laptop manufacturer's support site (Dell, HP, Lenovo, ASUS, or Acer) for your exact model. Chipset and power-management drivers control how Windows talks to the charging hardware, so they matter as much as the battery driver itself."
---

Battery drivers are the translators between Windows 10 and your battery's firmware chip. When the translation breaks — usually after a Windows update — you get the classic symptoms: percentages that freeze, "plugged in, not charging," or a battery Windows pretends does not exist. The hardware is fine; the conversation has broken down.

Updating or reinstalling these drivers is a five-minute job and fixes a surprising share of battery weirdness. This guide covers the full sequence: the quick Device Manager refresh, the clean reinstall, and the deeper chipset-driver update that actually matters most. For Windows 11, the steps are nearly identical — see our [Windows 11 battery driver guide](/articles/how-to-update-battery-drivers-on-windows-11/).

## Why this happens

- **Windows updates replace working drivers.** Feature updates sometimes install a generic driver over the manufacturer's tuned version, breaking battery communication.
- **Driver corruption.** Unexpected shutdowns or failed updates can corrupt the driver files, leaving the battery device in an error state.
- **Stale chipset drivers.** The chipset driver manages the low-level power interface. An outdated chipset driver can break battery reporting even when the battery driver itself is fine.
- **Multiple conflicting battery devices.** Some laptops show duplicate or ghost battery entries in Device Manager that confuse Windows about which device to talk to.
- **BIOS/firmware mismatch.** A BIOS update can change the battery interface in ways old drivers do not understand, requiring a driver refresh to match.
- **Power management software conflicts.** Manufacturer utilities sometimes install their own battery filter drivers that clash with Windows' native ones.

## How to fix it

Work through these in order, from the quick refresh to the full driver stack update.

### Fix 1: Scan for hardware changes (the 30-second refresh)

The simplest step sometimes re-establishes communication.

1. Press **Win + X** and select **Device Manager**.
2. Expand **Batteries**.
3. Click **Action** in the menu bar, then **Scan for hardware changes**.
4. Watch the battery icon for a minute — if the percentage or charging status corrects itself, you are done.

### Fix 2: Uninstall and reinstall the ACPI battery driver

The classic fix for corrupted battery drivers. Safe and reversible.

1. In **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. If a checkbox offers to delete driver software, leave it unchecked for now.
3. If you see multiple battery entries (some laptops list two), uninstall each one.
4. Click **Action > Scan for hardware changes**. Windows detects the battery and reinstalls the driver automatically.
5. Restart the laptop with the charger connected, then check the battery status.

### Fix 3: Update the driver through Windows Update

Check whether Microsoft has a newer driver waiting.

1. In **Device Manager**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Update driver**.
2. Select **Search automatically for drivers** and let Windows check.
3. Then open **Settings > Update & Security > Windows Update** and click **Check for updates**.
4. Click **View optional updates**, expand **Driver updates**, and install anything battery, chipset, or system-related.
5. Restart and verify the battery behavior.

### Fix 4: Install the manufacturer's chipset and power drivers

This is the step most guides skip, and it matters more than the battery driver itself.

1. Find your exact laptop model on the bottom sticker.
2. Go to the manufacturer's support site — [Dell](https://www.dell.com/support), HP, Lenovo, ASUS, or Acer — and open **Drivers & Downloads** for your model.
3. Download the latest **Chipset** driver and any **Power Management** or **ATK/ACPI** driver listed for Windows 10.
4. Install the chipset driver first, restart, then install the power management driver.
5. Alternatively, run Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), which automatically detects outdated Intel chipset and power-management drivers and installs the correct versions — handy when you are unsure which chipset package matches your machine.
6. Restart once more after everything is installed, then verify in **Device Manager** that no warning icons remain on the Batteries or System devices entries.
7. These drivers control the hardware interface the battery driver talks through — updating them resolves issues the battery driver reinstall alone cannot.

### Fix 5: Clean up duplicate or ghost battery devices

Ghost entries can hijack battery communication.

1. In **Device Manager**, click **View** and enable **Show hidden devices**.
2. Expand **Batteries** and look for grayed-out entries — these are ghosts from old configurations.
3. Right-click each grayed-out entry and choose **Uninstall device**.
4. Also check **System devices** for duplicate ACPI entries with warning icons.
5. Restart and confirm only the live battery devices remain.

### Fix 6: Update the BIOS

When drivers are current but the battery still misbehaves, the firmware side may need updating.

1. On the manufacturer's support site for your exact model, download the latest **BIOS** update.
2. Close all programs, connect the AC adapter, and run the updater.
3. Do not interrupt the process — a failed BIOS flash can brick the laptop.
4. After the automatic restart, check **Device Manager** to confirm the battery devices initialized cleanly.

### Fix 7: Verify the fix with a battery report

Confirm the driver stack is now reading the battery correctly.

1. Open an administrator **Command Prompt** (**Win + X**, then **Command Prompt (Admin)**) and run `powercfg /batteryreport`.
2. Open the report and check that **Design Capacity**, **Full Charge Capacity**, and **Cycle Count** show sensible values.
3. Compare the reported percentage with the taskbar icon — they should agree.
4. If the numbers look sane and match the icon, the drivers are healthy. If problems persist despite clean drivers, the issue is likely hardware — see our [battery not charging troubleshooting](/articles/laptop-battery-not-charging-troubleshooting/) guide for the hardware checks.

## Closing

Battery driver problems are among the most satisfying to fix because the solution is quick, free, and definitive: refresh, reinstall, update the chipset drivers, and verify with a battery report. Make the manufacturer's chipset driver part of your routine — it is the foundation everything else stands on. And remember the golden rule of battery troubleshooting: if the BIOS sees the battery correctly but Windows does not, it is always worth fixing the drivers before spending money on hardware.
