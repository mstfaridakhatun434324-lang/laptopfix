---
title: "How to Fix a Laptop Plugged In But Not Charging on Windows 11"
slug: how-to-fix-laptop-plugged-in-not-charging-windows-11
date: 2026-10-10
categories: ["battery"]
tags: ["battery", "charging", "windows 11", "power"]
description: "Laptop plugged in but not charging on Windows 11? Here are 7 proven fixes, from driver resets to BIOS settings, to get your battery charging again."
thumbnail: "/images/thumbs/how-to-fix-laptop-plugged-in-not-charging-windows-11.webp"
faqs:
  - q: "Why does my laptop say plugged in but not charging?"
    a: "Most often it's a corrupted battery driver, a worn-out charger or cable, or a vendor battery-health feature like Lenovo's Conservation Mode that caps charging. Less commonly, the battery itself has degraded past the point of accepting a charge, or the BIOS needs an update. Working through the fixes in this guide from simplest to hardest will identify the cause."
  - q: "Can a bad charger cause plugged in not charging?"
    a: "Yes. If the adapter can't deliver the wattage your laptop expects, Windows may run the machine on AC power without charging the battery at all. Try the original charger, check for frayed cables, plug directly into a wall outlet instead of a power strip, and test with a known-good adapter of equal or higher wattage."
  - q: "Will reinstalling battery drivers delete my data?"
    a: "No. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager only removes the software interface between Windows and the battery. Windows reinstalls it automatically on restart, and none of your files, apps, or settings are affected in any way."
  - q: "How do I know if my battery needs replacing?"
    a: "Run powercfg /batteryreport and compare Design Capacity with Full Charge Capacity in the generated report. If the full charge capacity has fallen to roughly 60 to 70 percent of the design capacity or lower, the battery is worn out and replacement is the realistic fix. Most laptop batteries last two to four years of regular use."
---

You plug in your charger, the Windows 11 taskbar shows the battery icon, and the tooltip reads "Plugged in" — yet the percentage never climbs. Sometimes Windows states it bluntly: "plugged in, not charging." Your laptop runs perfectly while connected to the wall, but the moment you unplug it, the battery drains as though the charger was never there.

This problem strikes Windows 11 laptops from every major brand — Dell, HP, Lenovo, Asus, and Acer — and it rarely has a single cause. Sometimes the culprit is physical: a frayed cable or a weak third-party adapter. Other times it is software: a corrupted battery driver, a vendor conservation feature quietly capping your charge, or an outdated BIOS misreporting battery state. The six fixes below are ordered from simplest to most involved, so work through them in order.

## Why this happens

- **A failing or underpowered charger or cable.** The adapter must deliver the wattage your laptop expects. A damaged cable, a worn barrel connector, or a low-wattage USB-C charger can run the laptop on AC power without charging the battery.
- **Corrupted Microsoft ACPI battery drivers.** Windows reads battery state through the Microsoft ACPI-Compliant Control Method Battery driver. When it corrupts — often after a Windows update — the charging status it reports can be completely wrong.
- **A vendor battery-health feature is limiting the charge.** Lenovo Conservation Mode, Asus Battery Health Charging, Dell battery settings, and HP Battery Health Manager deliberately stop charging at 60–80% to extend battery lifespan, which looks exactly like a charging failure.
- **Misconfigured or corrupted power plans.** A damaged power scheme can block normal charging behavior or force the wrong power states after updates and tweaks.
- **An aging or failed battery.** Lithium-ion cells chemically degrade with every charge cycle. After a few years of regular use, a worn battery may refuse to accept a charge at all.
- **Outdated BIOS or firmware.** The embedded controller that manages charging communicates through BIOS-level firmware. A bug there can freeze the reported charge state or confuse the charging circuitry.

## How to fix it

Start with Fix 1 and move down the list — most cases are resolved by the first three.

### Fix 1: Check the charger, cable, and power source

A surprising share of "not charging" cases come down to the adapter itself, so rule out hardware before touching software.

1. Inspect the charger brick and cable for fraying, kinks, or a loose barrel or USB-C connector. Wiggle the plug gently where it meets the laptop — if charging flickers on and off, the cable or port is failing.
2. Plug the adapter directly into a wall outlet, bypassing power strips, extension cords, and USB hubs or docking stations.
3. If your laptop charges over USB-C, use the port marked with a charging icon and the original adapter — phone chargers rarely deliver enough wattage for a laptop.
4. Test with a different compatible charger of equal or higher wattage. If a known-good adapter charges normally, replace your charger.

### Fix 2: Run the Windows battery troubleshooter

Windows 11 ships with a built-in Power troubleshooter that detects misconfigured power settings and resets them automatically.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Find "Power" in the list and click Run.
3. Apply any recommended fixes, then restart the laptop when prompted.
4. If the troubleshooter reports no problems, move on to Fix 3 — driver issues are the next most likely cause.

### Fix 3: Reinstall the Microsoft ACPI battery drivers

This is the most reliable software fix for charging problems, and it takes about two minutes.

1. Right-click the Start button and open Device Manager.
2. Expand the Batteries section.
3. Right-click "Microsoft ACPI-Compliant Control Method Battery" and choose Uninstall device, then confirm.
4. Right-click "Microsoft AC Adapter" and uninstall it the same way.
5. Restart the laptop. Windows detects the battery hardware during boot and reinstalls both drivers automatically.
6. After signing in, plug in the charger and check whether the taskbar battery icon now shows charging.

### Fix 4: Update the BIOS

An outdated BIOS can miscommunicate with the embedded controller that manages charging, freezing the reported battery state.

1. Press Win + R, type `msinfo32`, press Enter, and note the BIOS Version/Date under System Summary.
2. Visit your manufacturer's support site and search for your exact model to see whether a newer BIOS is available.
3. Download the BIOS update. Keep the charger plugged in, close all applications, and run the installer.
4. Allow the laptop to restart and finish the flash process — do not power it off or close the lid while it runs.
5. Once Windows boots again, check whether the battery charges normally.

### Fix 5: Check battery charge thresholds and conservation mode

If your battery stops at a round number — 60% or 80% — and Windows says "plugged in, not charging," a battery-health feature is doing its job, not malfunctioning.

- **Lenovo:** Open Lenovo Vantage > Device > Power and turn off Conservation Mode.
- **Asus:** Open MyASUS > Battery Health Charging and select Full capacity mode.
- **Dell:** Open Dell Power Manager > Battery Settings and choose Standard.
- **HP:** Restart, press F10 to enter BIOS, go to Advanced > Power Management Options > Battery Health Manager, and select the full-charge option.

For step-by-step instructions on every brand, see our guide to removing the [80 percent charge limit on Windows 11](/articles/laptop-battery-stuck-at-80-percent-windows-11-fix/).

### Fix 6: Reset power plans and generate a battery report

A corrupted power scheme can be restored to defaults in seconds, and a battery report reveals whether the battery itself is worn out.

1. Right-click Start and open Terminal (Admin).
2. Run `powercfg /restoredefaultschemes` to reset all power plans to Windows defaults.
3. Run `powercfg /batteryreport /output "C:\battery-report.html"` to generate a detailed report.
4. Open the report in your browser and compare Design Capacity with Full Charge Capacity. If the full charge capacity is far below the design capacity, the battery is worn out and replacement is the realistic fix.
5. For a deeper look, run `powercfg /energy` and let it observe your system for 60 seconds, then review the energy-report.html it produces for errors.

For most people, one of these six fixes restores charging — usually a driver reinstall or a conservation setting they never knew was on. If nothing above helps and the battery report shows severe wear, a replacement battery or a service visit is the next step. And if your laptop feels sluggish while you troubleshoot, heavy background apps keep the processor busy and the fans spinning; our guide to [fixing high RAM usage on Windows 11](/articles/windows-11-high-ram-usage-fix/) can help with that too.
