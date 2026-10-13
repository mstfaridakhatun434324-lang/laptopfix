---
title: "How to Fix Slow Charging on a Laptop After a Windows 11 Update"
slug: how-to-fix-slow-charging-on-laptop-after-windows-11-update
date: 2026-09-22
categories: ["battery"]
tags: ["slow charging", "windows 11 update", "power delivery"]
description: "Laptop charging at a crawl since a Windows 11 update? Fix driver, power plan, and USB-C issues slowing down your charge."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-after-windows-11-update.webp"
faqs:
  - q: "Why is my laptop charging so slowly after updating Windows 11?"
    a: "Updates can install a generic battery or USB-C driver that negotiates lower wattage, reset power plans to power-saving modes that throttle charging current, or enable battery lifespan limiters. The hardware is fine — the software handshake between Windows and the charger changed."
  - q: "How can I tell if my laptop is slow charging?"
    a: "Hover over the battery icon: Windows 11 sometimes shows 'plugged in, charging' with a very slow percentage climb. Time it — a healthy laptop gains roughly 1% every 1-2 minutes. If you gain 5% in an hour, charging is throttled. A USB power meter on the cable gives exact wattage."
  - q: "Does using the laptop while charging make it slower?"
    a: "Yes, significantly. The charger splits its wattage between running the laptop and charging the battery. Gaming or rendering while charging can leave almost nothing for the battery. For the fastest charge, put the laptop to sleep or turn it off."
  - q: "Can a Windows update damage my charger?"
    a: "No. Software cannot damage the charger hardware. But an update can change which charging profile Windows negotiates over USB-C, making a good charger behave like a weak one until the driver is fixed."
---

Before the update, your laptop went from 20% to 80% over lunch. Now it crawls — 5% in an hour, maybe. The charger is the same, the outlet is the same, so what changed? The Windows 11 update changed how your laptop talks to the charger, throttles power, or manages the battery.

Slow charging after an update is almost never a hardware failure. It is a driver, a power plan, or a charging negotiation that the update disturbed. These fixes restore full-speed charging step by step.

## Why this happens

- **The update replaced the battery or USB-C driver.** Generic drivers can negotiate the wrong Power Delivery profile, cutting wattage.
- **A battery lifespan limiter got enabled.** Updates sometimes flip on conservation modes that slow charging near the cap.
- **The power plan changed.** A reset to a power-saving plan can reduce charging current.
- **Background processes consume the charger's output.** Post-update indexing, OneDrive resyncs, and update cleanups eat wattage meant for the battery.
- **USB-C PD renegotiation fails.** The update can break the handshake so the laptop charges at 15W instead of 65W.
- **Thermal throttling kicked in.** Updates can change fan curves, and a hotter laptop charges slower to protect the battery.

## How to fix it

Work through these in order — start with the quick checks.

### Fix 1: Confirm the charger and cable are still adequate

Rule out the physical layer before blaming software.

1. Check the wattage printed on the charger brick and confirm it matches your laptop's requirement.
2. If you charge over USB-C, inspect the cable — a damaged or low-rated cable silently drops the negotiated wattage. Try a known-good cable rated for your charger's wattage.
3. Plug directly into a wall outlet, not a power strip or dock, for the test.
4. With the laptop asleep, time the charge for 30 minutes. Note the percentage gain — this is your baseline.
5. If a different charger/cable charges at normal speed, the issue is hardware, not the update.

### Fix 2: Reinstall the battery and USB-C drivers

The update's generic drivers are the prime suspect.

1. Open **Device Manager** (**Win + X**).
2. Expand **Batteries** > right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device** > **Action** > **Scan for hardware changes**.
3. Expand **Universal Serial Bus controllers**. Right-click **USB Root Hub (USB 3.0)** entries and any **UCSI USB Connector Manager** > **Uninstall device**, then **Action** > **Scan for hardware changes**.
4. Restart the laptop with the charger plugged in.
5. Windows reinstalls fresh drivers and renegotiates the USB-C PD contract from scratch.

### Fix 3: Check for an enabled charge limiter

Updates love to turn these on silently.

1. Open your manufacturer's app — Lenovo Vantage, MyASUS, Dell Power Manager, MSI Center.
2. Look for Conservation Mode, Battery Health Charging, or similar. If active, it may also slow charging as it approaches the cap.
3. Temporarily set it to full capacity mode and time the charge rate.
4. Check the BIOS too — HP Battery Health Manager and Dell charge configuration can throttle charging independently.
5. Our [80% charge limit guide](/articles/how-to-limit-battery-charge-to-80/) details every brand's setting location.

### Fix 4: Reset the power plan

The update may have left you on a neutered power plan.

1. Open **Terminal (Admin)** and run `powercfg /restoredefaultschemes` to rebuild the plans.
2. Activate Balanced: `powercfg /SETACTIVE 381b4222-f694-41f0-9685-ff5bb260df2e`.
3. Go to **Settings** > **System** > **Power & battery** > **Power mode** and set it to **Balanced** (not Best power efficiency) while plugged in.
4. In **Control Panel** > **Power Options** > **Change advanced power settings**, check that nothing under **Battery** or **Processor power management** looks wrong.
5. Retest the charge rate.

### Fix 5: Kill the background load stealing your wattage

After a feature update, Windows does days of background housekeeping.

1. Open **Task Manager** (**Ctrl + Shift + Esc**) and sort by **CPU** and **Disk**.
2. Look for **Windows Module Installer**, **Search Indexer**, **Antimalware Service Executable**, or cloud sync apps running hot.
3. Let the indexer finish if it just started — it settles down. Forcing it off mid-index just prolongs the pain.
4. Pause OneDrive/Dropbox sync while charging: click the tray icon > **Pause syncing**.
5. Go to **Settings** > **Windows Update** and make sure no update is actively downloading or installing during your charge test.
6. Close unnecessary apps — every watt running the laptop is a watt not charging the battery.

### Fix 6: Cool the laptop down

Heat throttles charging speed as a safety measure.

1. Feel the laptop while charging — if it is hot, charging will be slow by design.
2. Use it on a hard flat surface with clear vents. Blow dust out with compressed air (powered off).
3. In **Settings** > **System** > **Power & battery** > **Power mode**, use **Best power efficiency** while charging to reduce heat generation.
4. Charge with the laptop asleep or powered off for the fastest, coolest charge.
5. If heat is a constant problem, see our [overheating while charging guide](/articles/how-to-fix-laptop-overheating-while-charging-on-windows-10/) for deeper fixes.

### Fix 7: Update the BIOS and chipset drivers

Firmware updates frequently fix post-update charging behavior.

1. Get the latest BIOS and chipset drivers from your manufacturer's official support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Install with the charger plugged in; do not interrupt the flash.
3. After the update, unplug the charger for 30 seconds, then plug it back in to force a fresh PD negotiation.
4. Time the charge rate again and compare with your Fix 1 baseline.
5. If charging is still slow after all of this, run `powercfg /batteryreport` and check the battery's health — a severely worn battery accepts charge slowly, and our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) shows how to read the numbers.

## Closing

Slow charging after a Windows 11 update is a software handshake problem far more often than a hardware one. Reinstall the battery and USB-C drivers, check for silently-enabled limiters, and clear the background load — and time your charge rate before and after so you can see the improvement instead of guessing.
