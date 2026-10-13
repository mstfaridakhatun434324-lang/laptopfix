---
title: "What to Do If Your Laptop Only Works When Plugged In"
slug: what-to-do-if-laptop-only-works-when-plugged-in
date: 2026-09-15
categories: ["battery"]
tags: ["laptop only works plugged in", "dead battery", "battery not detected"]
description: "Laptop dies the second you unplug it? That means the battery is dead, disconnected, or undetected. Here is how to diagnose each case."
thumbnail: "/images/thumbs/what-to-do-if-laptop-only-works-when-plugged-in.webp"
faqs:
  - q: "Why does my laptop turn off when I unplug the charger?"
    a: "The battery is not delivering power. Either it is completely worn out, it has become disconnected internally, Windows no longer detects it, or its protection circuit has tripped. The charger powers the laptop directly, which is why everything works until you unplug."
  - q: "Can a laptop run without a battery?"
    a: "Yes, most laptops run fine on AC power with a dead or removed battery. Performance may be slightly reduced on some models that use the battery to supplement peak power draw. It is a workable temporary state, not a long-term solution."
  - q: "How do I know if the battery is dead or just disconnected?"
    a: "Check Device Manager under Batteries. If the battery appears there and Windows shows a percentage, it is detected but worn out. If no battery appears at all, or Windows says no battery detected, it is a detection or connection problem rather than simple wear."
  - q: "Is it worth replacing the battery or buying a new laptop?"
    a: "If the laptop is otherwise fast enough and less than 5 years old, a genuine replacement battery is far cheaper than a new machine. If the laptop is very old, slow, or the battery is only one of several problems, put the money toward a replacement laptop instead."
---

Unplug the charger and the laptop dies instantly. Not a graceful shutdown, not a low-battery warning. Just off, as if you pulled the plug on a desktop. Meanwhile, on AC power, everything works perfectly.

This symptom is wonderfully diagnostic: it tells you the charging and power circuitry work, and the battery specifically does not. The remaining question is why, and the answer falls into three buckets: dead, disconnected, or undetected.

## Why this happens

- **Completely worn battery:** The cells have degraded past the point of holding any useful charge.
- **Tripped protection circuit:** The battery's safety circuit locked out after a deep discharge, overheat, or fault.
- **Loose internal connector:** The battery cable worked loose from the motherboard.
- **Undetected battery:** Windows lost communication with the battery, so it cannot use it.
- **Swollen or damaged battery:** Physical damage can sever internal connections.
- **Wrong or weak adapter masking:** Rare, but an underpowered adapter can create confusing symptoms around battery behavior.
- **BIOS battery setting:** Some BIOS setups have a battery disconnect or ship-mode setting for storage.

## How to fix it

Work through these in order, from detection to physical checks.

### Fix 1: Check whether Windows sees the battery

1. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
2. If **Microsoft ACPI-Compliant Control Method Battery** is present, Windows detects a battery. If the category is empty or missing, you have a detection problem.
3. Hover over the battery icon in the taskbar and note what it says: a percentage, "no battery detected," or nothing.
4. For detection failures, see [no battery detected after Windows update](/articles/how-to-fix-no-battery-detected-after-windows-update-in-windows-11-24h2/) and [battery not detected on Windows 11](/articles/laptop-battery-not-detected-windows-11/).

### Fix 2: Read the battery report for the wear verdict

1. Open an elevated Terminal and run `powercfg /batteryreport`.
2. Compare **Design Capacity** to **Full Charge Capacity**.
3. If full charge capacity is near zero or a tiny fraction of design, the battery is spent. No setting revives it.
4. Check the recent usage section for a sudden cliff, which suggests a protection trip rather than gradual wear.

### Fix 3: Reset the battery protection circuit

1. Shut down, unplug the adapter, and disconnect all peripherals.
2. If the battery is removable, take it out for 5 minutes, then reseat it firmly.
3. For internal batteries, hold the power button for 60 seconds with the adapter unplugged.
4. Plug in, charge for at least an hour undisturbed, then test on battery. A tripped protection circuit sometimes resets with a long, calm charge.

### Fix 4: Reinstall the battery driver

1. In **Device Manager** > **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
2. Restart. Windows reinstalls the driver.
3. Also expand **System devices** and update any ACPI or chipset entries.
4. Test on battery power after the reboot.

### Fix 5: Check the BIOS for battery settings

1. Reboot into BIOS setup and look for battery, power, or advanced sections.
2. Some laptops have a **Battery Disconnect**, **Ship Mode**, or **Battery Health** setting that disables the battery.
3. Make sure the battery is enabled and any ship mode is off.
4. While there, check whether the BIOS itself reports the battery present and its charge level.

### Fix 6: Inspect for physical problems

1. With the laptop off and unplugged, check whether the bottom panel bulges or the laptop rocks on a flat table.
2. Swelling can break internal connections. If you see it, read our [swollen battery safety guide](/articles/how-to-fix-laptop-battery-swelling-step-by-step/) before doing anything else.
3. If you are comfortable opening the laptop and it is out of warranty, reseat the battery cable on the motherboard. If it is in warranty, do not open it. Call support instead.
4. Never force a swollen battery connector.

### Fix 7: Replace the battery

1. If wear is total or the battery is physically damaged, order a genuine replacement matched to your exact model number.
2. Use the manufacturer's parts store or authorized sellers. Avoid unbranded packs.
3. Have a technician install internal batteries.
4. After replacement, run one full charge-discharge-charge cycle to calibrate the new pack.

### Fix 8: Check the battery status in BIOS setup

The BIOS sees the battery without any Windows involvement, which makes its verdict trustworthy.

1. Restart and enter BIOS setup.
2. Find the battery information page, often under **Main**, **Advanced**, or a dedicated **Battery** section.
3. Note what it reports: battery present or not present, charge percentage, and any health or status line.
4. If the BIOS says no battery is installed while one physically is, you have a connection or recognition failure at the hardware level. Reseat or service.
5. If the BIOS sees the battery but reports 0 percent or a failure status after hours of charging, the pack cannot take a charge.
6. If the BIOS reports the battery healthy but Windows cannot use it, the problem is Windows-side: drivers or power configuration.
7. Take a photo of the BIOS battery page with your phone. Support will ask for exactly this information.

## Closing

A laptop that only works plugged in has performed most of the diagnosis for you: the power circuitry works, the charger works, and the battery path specifically does not. The remaining work is sorting dead from disconnected from undetected. Device Manager and the taskbar icon tell you whether Windows sees a battery at all. The battery report tells you whether the cells have any life left, with a near-zero full charge capacity being the clearest possible verdict. The protection-circuit reset revives packs that tripped their safety lockout after a deep discharge. The BIOS battery page gives you the hardware's own testimony, free of any Windows interference. And when the verdict is a spent or damaged pack, a genuine replacement matched to your exact model restores the laptop's portability for a fraction of the cost of a new machine. It is one of the most straightforward laptop diagnoses there is, and now you know exactly how to read it.
