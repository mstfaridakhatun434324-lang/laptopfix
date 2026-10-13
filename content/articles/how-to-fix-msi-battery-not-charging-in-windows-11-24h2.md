---
title: "How to Fix an MSI Laptop Battery Not Charging in Windows 11"
slug: how-to-fix-msi-battery-not-charging-in-windows-11-24h2
date: 2026-09-13
categories: ["battery"]
tags: ["msi laptop", "msi center", "battery not charging", "windows 11"]
description: "MSI laptop plugged in but not charging in Windows 11? Check MSI Center's battery modes, reset the EC, update firmware, and fix charging step by step."
thumbnail: "/images/thumbs/how-to-fix-msi-battery-not-charging-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my MSI laptop plugged in but not charging?"
    a: "The most common MSI-specific cause is the Battery Health Option in MSI Center — if it's set to Balanced (80%) or Best for Battery (60%), charging stops at that limit by design. Other causes include an EC firmware glitch (fixed by a power-drain reset), outdated BIOS/EC firmware, corrupted ACPI battery drivers after a Windows update, or an underpowered charger on gaming models that need 180W+."
  - q: "What is MSI Center Battery Health Option and where is it?"
    a: "It's MSI's charge-limit feature inside the MSI Center app, under Features > Battery Health Option (sometimes under System Diagnosis depending on version). It offers three modes: Best for Mobility (charges to 100%), Balanced (stops at 80%), and Best for Battery (stops at 60%). If your battery won't go past 60 or 80 percent, this setting is almost certainly the reason."
  - q: "How do I reset the EC on an MSI laptop?"
    a: "Shut the laptop down, unplug the charger and all USB devices. Press and hold the power button for 30-45 seconds to drain residual power and reset the embedded controller. On some MSI models there's a dedicated EC reset pinhole on the bottom — check your manual. Reconnect the charger and power on. This clears charging glitches that survive normal restarts."
  - q: "Can I use a lower-wattage charger on my MSI gaming laptop?"
    a: "It may power the laptop but not charge the battery — MSI gaming laptops often ship with 180W, 200W, or 240W chargers, and the system prioritizes running the machine over charging when power is limited. For reliable charging, always use the original MSI charger or an exact-wattage replacement. USB-C charging on most MSI gaming models is data-only and won't charge at all."
---

MSI laptops — especially the gaming lines — have their own charging personality. Between MSI Center's battery health modes, EC firmware quirks, and the massive wattage their chargers deliver, an MSI that says "plugged in, not charging" is usually following an instruction rather than suffering a failure. The trick is knowing which MSI-specific setting or reset applies.

This guide walks through the MSI-specific checks first (because they solve most cases), then the general Windows fixes that apply to any laptop.

## Why this happens

- **MSI Center Battery Health Option set to 60% or 80%.** The Balanced and Best for Battery modes cap charging by design — the number one cause on MSI machines.
- **EC firmware glitch.** The embedded controller that manages charging locks up, especially after sleep/wake cycles or updates.
- **Outdated BIOS or EC firmware.** MSI fixes charging bugs in BIOS/EC updates distributed through MSI Center's Live Update.
- **Corrupted ACPI battery drivers.** Windows updates can break the driver Windows uses to talk to the battery.
- **Underpowered or third-party charger.** Gaming MSI laptops need their full-wattage brick; a weaker charger runs the laptop but can't charge the battery simultaneously.
- **Battery calibration drift.** The fuel gauge misreports the charge level, making a healthy battery look stuck.
- **Worn battery pack.** After heavy gaming use and heat cycles, the pack itself may no longer accept a charge.

## How to fix it

Work through these in order, starting with the easiest. Stop when your issue is resolved.

### Fix 1: Check MSI Center's Battery Health Option

Before anything else, rule out the intentional limit — this takes thirty seconds.

1. Open **MSI Center** (install it from the Microsoft Store or MSI's site if missing).
2. Go to **Features > Battery Health Option** (on some versions it's under **System Diagnosis**).
3. Check which mode is active: **Best for Mobility** (100%), **Balanced** (80%), or **Best for Battery** (60%).
4. If it's on Balanced or Best for Battery, switch to **Best for Mobility**.
5. Keep the charger plugged in and watch whether the percentage starts climbing past the old limit.

### Fix 2: Reset the embedded controller (EC reset)

The EC manages charging at the hardware level, and a reset clears glitches that survive reboots.

1. Shut the laptop down completely.
2. Unplug the charger and disconnect all USB devices and docks.
3. Press and hold the **power button for 30-45 seconds**.
4. Some MSI models have a small **EC reset pinhole** on the bottom panel — if yours does, press it gently with a paperclip for 10 seconds instead.
5. Reconnect the charger and power on, then check the battery icon.

### Fix 3: Use the original MSI charger

MSI gaming laptops are picky about wattage — and for good reason.

1. Check the wattage printed on your original MSI charger (often 180W, 200W, or 240W on gaming models).
2. If you're using a third-party, travel, or USB-C charger, switch back to the original brick.
3. Make sure both ends of the charger cable are firmly seated — MSI's larger bricks have a detachable AC cord that works loose.
4. Try a different wall outlet to rule out a bad socket.
5. Note: on most MSI gaming laptops the USB-C port does not support charging input at all, so don't rely on it.

### Fix 4: Update BIOS and EC firmware via MSI Center

MSI bundles charging fixes into firmware updates regularly.

1. Open **MSI Center** and go to **Support > Live Update**.
2. Click **Scan** and install any **BIOS** or **EC firmware** updates offered.
3. Keep the original charger connected during the entire update — do not interrupt it.
4. After the update and restart, re-check the Battery Health Option from Fix 1 (updates can reset it).

### Fix 5: Reinstall the battery drivers

A clean driver reinstall fixes Windows-side communication with the battery.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click each **Microsoft ACPI-Compliant Control Method Battery** entry and choose **Uninstall device**.
4. Also uninstall **Microsoft AC Adapter**.
5. Shut down fully (not restart), unplug for 30 seconds, then boot up — Windows reinstalls the drivers automatically.

### Fix 6: Run MSI Center's battery calibration

If the percentage is stuck or jumps around, the fuel gauge needs recalibrating.

1. Open **MSI Center** and look for **Battery Calibration** (under Features or System Diagnosis).
2. Connect the original charger and start the calibration — it will fully charge, then fully discharge, then recharge the battery.
3. This takes several hours; let it run uninterrupted, ideally overnight.
4. After calibration, the reported percentage should track the real charge. Our general [battery calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/) explains what's happening under the hood.

### Fix 7: Check Windows power and driver updates

Don't overlook the generic Windows side — it bites MSI laptops too.

1. Open **Settings > Windows Update** and install everything, including **optional driver updates** under Advanced options.
2. Open **Device Manager > Batteries** and confirm no yellow warning icons remain after the reinstall.
3. In **Settings > System > Power & battery**, confirm the power mode isn't causing odd behavior — test with **Balanced**.
4. Restart once more and test charging.

### Fix 8: Verify battery health with a report

If nothing has worked, get objective data before concluding the battery is dead.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`.
2. Compare **Design Capacity** vs **Full Charge Capacity** in the generated report.
3. Healthy capacity + no charging = firmware/driver issue: repeat Fixes 2, 4, and 5 together in sequence.
4. Collapsed capacity (well under 70% of design) + no charging = worn-out pack. Contact MSI support for a genuine replacement battery — gaming laptop batteries are model-specific, so match the exact part number. See our [battery health check guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) for reading the full report.

If the battery charges but never reaches 100%, our walkthrough for [batteries that won't charge to 100%](/articles/how-to-fix-laptop-battery-not-charging-to-100-percent-step-by-step/) covers the remaining causes. For the general case without MSI specifics, see [laptop battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/).

Official resources: Microsoft's [Windows battery support page](https://support.microsoft.com/en-us/windows) for the built-in troubleshooters, and MSI's own support channels for model-specific BIOS and EC firmware.

## Closing

On MSI laptops, "not charging" is a Battery Health Option limit or an EC glitch far more often than a dead battery. Check MSI Center first, reset the EC second, and update the firmware third — that sequence resolves the large majority of MSI charging complaints without ever opening the machine.
