---
title: "How to Fix an MSI Laptop Battery Not Charging on Windows 10"
slug: how-to-fix-msi-battery-not-charging-on-windows-10
date: 2026-09-13
categories: ["battery"]
tags: ["MSI", "not charging", "Windows 10"]
description: "MSI laptop plugged in but not charging on Windows 10? Check MSI Center's battery options, the EC firmware, and the usual driver suspects."
thumbnail: "/images/thumbs/how-to-fix-msi-battery-not-charging-on-windows-10.webp"
faqs:
  - q: "Why is my MSI laptop plugged in but not charging?"
    a: "The most common MSI-specific cause is the Battery Health Option in MSI Center or Dragon Center, which intentionally caps charging at 60 or 80 percent to protect the battery. Other causes include a stuck embedded controller, a dead charger, a corrupted battery driver, or an EC firmware bug fixed by a BIOS update."
  - q: "What is MSI Battery Health Option?"
    a: "It is a feature in MSI Center and Dragon Center that limits maximum charge to extend battery lifespan: Best for Battery caps at 60 percent, Balanced at 80 percent, and Best for Mobility allows 100 percent. If your battery stops at 60 or 80 percent, this feature is working as intended — switch it to Best for Mobility for a full charge."
  - q: "How do I reset the EC on an MSI laptop?"
    a: "Shut down the laptop, unplug the charger and all peripherals, then press and hold the power button for 30 to 45 seconds. Some MSI models have a small EC reset pinhole on the bottom — press it with a paperclip for 30 seconds. Reconnect the charger and power on."
  - q: "Can a Windows 10 update stop an MSI battery from charging?"
    a: "Yes. Updates can corrupt the battery driver stack or conflict with MSI's own power utilities. Reinstalling the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager and updating MSI Center plus the chipset driver usually restores charging after an update."
---

An MSI laptop that says "plugged in, not charging" has a short list of usual suspects, and the first one is a feature, not a fault. MSI's Battery Health Option deliberately stops charging at 60 or 80 percent to prolong battery life, and plenty of owners mistake it for a broken charger. Before you buy anything, check that setting — it takes thirty seconds and resolves a large share of these reports.

If the Battery Health Option is not the cause, the next suspects are the embedded controller, the charger, and Windows 10's battery drivers. Work through the list in order; each step rules out one layer.

## Why this happens

- **Battery Health Option cap:** MSI Center or Dragon Center is set to Best for Battery (60 percent) or Balanced (80 percent), which looks exactly like "not charging."
- **Stuck embedded controller:** The EC chip that manages charging can lock up and needs a hard reset.
- **Failing charger or cable:** MSI gaming laptops need high-wattage bricks; a weak or dying adapter cannot sustain charging.
- **Corrupted battery driver:** Windows 10 updates can break the ACPI battery driver stack.
- **EC firmware bug:** Older BIOS/EC firmware on some MSI models mishandles charge negotiation until updated.
- **Worn battery:** A battery with collapsed capacity may refuse charge or report "not charging" permanently.

## How to fix it

Work through these in order — start with the MSI-specific setting before touching drivers.

### Fix 1: Check MSI Center's Battery Health Option

This is the cause more often than not.

1. Open **MSI Center** (or **Dragon Center** on older models).
2. Go to **General Settings** and find **Battery Health Option**.
3. If it is set to **Best for Battery** (caps at 60 percent) or **Balanced** (caps at 80 percent), that is your "problem" — it is intentional.
4. Switch it to **Best for Mobility** to allow charging to 100 percent.
5. Wait a few minutes and confirm the percentage starts climbing again.

### Fix 2: Perform an EC reset

A stuck embedded controller blocks charging until reset.

1. Shut down the laptop completely and unplug the charger and every peripheral.
2. Press and hold the power button for **30 to 45 seconds** — this drains residual power and resets the EC.
3. If your MSI model has a small **EC reset pinhole** on the bottom panel, press it with a straightened paperclip for 30 seconds instead.
4. Reconnect only the original MSI charger and power on.
5. Check the battery icon within a few minutes for charging status.

### Fix 3: Test the charger and power path

Rule out the hardware that feeds the laptop.

1. Confirm you are using the original MSI power brick with its full rated wattage — gaming models often need 180W or more, and a weaker adapter will not charge under load.
2. Inspect the brick, cable, and DC jack for damage, overheating smells, or a loose fit.
3. Try a different wall outlet, bypassing any power strip.
4. If you have access to a compatible MSI charger, test with it — chargers fail far more often than motherboards.
5. Watch the charger's LED if it has one; no light means the brick itself is likely dead.

### Fix 4: Reinstall the battery drivers

Windows 10 can lose track of the battery after updates.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Also uninstall **Microsoft AC Adapter** if present.
4. Shut down (do not restart), unplug the charger, hold the power button 30 seconds, then reconnect and power on.
5. Windows rebuilds the drivers on boot — check charging status after the desktop loads. Our general guide covers [laptops not charging when plugged in](/articles/best-way-to-fix-laptop-battery-not-charging-when-plugged-in/).

### Fix 5: Update MSI Center, Dragon Center, and chipset drivers

Outdated MSI software fights Windows 10 power management.

1. Update **MSI Center** or **Dragon Center** from the Microsoft Store or MSI's website.
2. Download the latest **chipset** and **Intel Management Engine** drivers for your exact model from MSI's support page.
3. Install them, restart, and re-check the Battery Health Option setting — updates sometimes reset it.
4. If Dragon Center is old and buggy, consider migrating to the newer MSI Center if your model supports it.
5. Retest charging on AC power with no heavy apps running.

### Fix 6: Update the BIOS/EC firmware

MSI fixes charging bugs in firmware updates.

1. Find your exact model on MSI's support site and check the latest **BIOS** version against yours (shown in **System Information**, run `msinfo32`).
2. Follow MSI's BIOS update instructions precisely — keep the charger connected and do not interrupt the process.
3. After the update, enter the BIOS setup and choose **Load Optimized Defaults**, then save and exit.
4. Reconfigure the Battery Health Option in MSI Center afterward, since firmware updates can reset it.
5. Observe one full charge cycle to confirm the fix held.

### Fix 7: Check battery health and replace if worn

If everything software-side checks out, the battery itself is suspect.

1. In an admin Command Prompt, run `powercfg /batteryreport /output "C:\battery-report.html"` and open the report.
2. Compare **Full Charge Capacity** with **Design Capacity** — far below 60 percent means the pack is worn out.
3. On MSI laptops with removable batteries, try running on a known-good battery if available.
4. Order a replacement matched to your exact MSI model number from a reputable seller.
5. After installing, run a full calibration: charge to 100 percent, drain to shutdown, then recharge uninterrupted. For update-related variants, see [battery not charging after a Windows 11 update](/articles/best-way-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update/). For the OS-side power stack, Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents the built-in battery troubleshooter.

## Closing

MSI charging problems usually end at one of three places: the Battery Health Option doing its job, a stuck EC needing a reset, or a tired charger. Check the software cap first, reset the controller second, and verify the brick third — that sequence resolves the overwhelming majority of cases without spending a cent. If the battery report shows a worn-out pack, replacement is the honest fix.
