---
title: "How to Fix a Laptop That Only Works When Plugged In on Windows 11"
slug: how-to-fix-laptop-only-works-when-plugged-in-on-windows-11
date: 2026-09-26
categories: ["battery"]
tags: ["plugged in", "battery dead", "windows 11"]
description: "Laptop dies instantly when unplugged on Windows 11? Diagnose dead batteries, detection failures, and charging faults step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-on-windows-11.webp"
faqs:
  - q: "Why does my laptop shut off the moment I unplug it?"
    a: "The battery is delivering zero power — either it is completely worn out, Windows has stopped detecting it, or the charging circuit never charges it. The laptop runs fine on AC because the charger powers it directly, bypassing the battery entirely."
  - q: "How do I check if my battery is dead on Windows 11?"
    a: "Run powercfg /batteryreport in an admin Terminal. If Full Charge Capacity is a small fraction of Design Capacity, the battery is worn out. If the report shows no battery information at all, Windows cannot detect the battery — a driver or hardware connection issue."
  - q: "Can I still use my laptop with a dead battery?"
    a: "Yes. A laptop with a dead battery works normally on AC power — it is effectively a small desktop. Just save your work often, since any power interruption shuts it down instantly with no battery backup."
  - q: "Is a swollen battery dangerous?"
    a: "Yes. If the trackpad is lifting, the bottom case is bulging, or the laptop rocks on a flat table, stop using it and stop charging it. Swollen lithium batteries are a fire risk. Do not puncture it — take it to a repair shop or recycler for safe handling."
---

Unplug the charger, and the laptop dies mid-keystroke. No "low battery" warning, no graceful shutdown — it just cuts out like a desktop during a blackout. Plug it back in, and everything is fine. Your laptop has become a very compact desktop, and the battery is contributing exactly nothing.

This guide separates the three possible realities: a battery that is truly dead, a battery Windows cannot see, and a battery that never gets charged. Each has a different fix, and the battery report tells you which one you are dealing with.

## Why this happens

- **The battery reached end of life.** Cells degraded to the point of delivering no usable current.
- **Windows stopped detecting the battery.** Driver corruption or a failed enumeration after an update.
- **The battery is not being charged.** A faulty charger, DC jack, or charging circuit means the battery slowly emptied and never refilled.
- **The battery is disconnected internally.** Loose connector from a drop or failed clip.
- **The battery is swollen and the protection circuit cut it off.** Safety circuits disconnect dangerous packs.
- **BIOS disabled the battery.** Servicing modes or reset defaults can isolate the battery.

## How to fix it

Work through these in order — diagnose first, then fix the actual cause.

### Fix 1: Run a battery report and read the verdict

Five minutes here saves hours of guessing.

1. Right-click **Start** > **Terminal (Admin)**.
2. Run `powercfg /batteryreport` and open the HTML file.
3. **No battery section at all?** Windows cannot see the battery — skip to Fix 3.
4. **Full Charge Capacity near zero or under 15% of design?** The battery is dead — skip to Fix 7.
5. **Capacity looks reasonable?** The battery exists and holds charge, so the problem is detection or the switchover — continue to Fix 2.
6. Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains every section of this report. Microsoft also documents the battery report command at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 2: Check the obvious: charge state and charger

Make sure the battery is actually being fed.

1. Hover over the battery icon. It should say "plugged in, charging" with a rising percentage.
2. If it says "plugged in" without "charging," the battery is not receiving power — check the charger wattage against the laptop's requirement.
3. Leave it plugged in for 2 hours. If the percentage never moves, the charging path is broken.
4. Try a different outlet and, if possible, a known-good charger of the correct wattage.
5. Watch for a flickering charging indicator — that points to a loose DC jack or failing charger cable.

### Fix 3: Force Windows to redetect the battery

If the report showed no battery, make Windows look again.

1. Open **Device Manager** (**Win + X**).
2. Expand **Batteries**. If **Microsoft ACPI-Compliant Control Method Battery** is there, right-click > **Uninstall device**.
3. Click **Action** > **Scan for hardware changes**.
4. Restart the laptop.
5. If the Batteries section is empty or the device will not reinstall, see our full [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/).
6. After redetection, unplug the charger briefly to test — even 10 seconds of runtime proves the battery is engaging.

### Fix 4: Reset the embedded controller

The EC manages the battery switchover. When it locks up, unplugging kills power instantly.

1. Shut down fully — hold **Shift** while clicking **Shut down** to bypass fast startup.
2. Unplug the charger and all peripherals.
3. If the battery is removable, take it out. Hold the power button for 30 seconds.
4. Reinsert, plug in, and power on.
5. For sealed models, use the pinhole reset button on the bottom (10 seconds with a paperclip) if your model has one.
6. Unplug and test. If the laptop now survives even a minute on battery, the EC was stuck.

### Fix 5: Check BIOS for battery status and settings

The firmware knows things Windows does not.

1. Enter BIOS (**F2**, **F10**, **Del**, or **Fn+F2** — varies by brand).
2. Look for a battery information or health page. Note what it says: not detected, failed, or healthy.
3. Check for **Battery Disconnect**, **Ship Mode**, or similar options and make sure they are off.
4. Load optimized defaults if anything looks odd, then save and exit.
5. If BIOS says the battery is not detected either, the problem is hardware — connection or the pack itself.

### Fix 6: Inspect the physical battery

Time to look inside — but only if you are comfortable.

1. Shut down, unplug everything.
2. Remove the back panel with the right screwdriver (check a teardown for your model).
3. Find the battery connector — wide plug, cable to the battery pack. Reseat it firmly.
4. **Check for swelling now.** A puffy battery, lifting trackpad, or bulging case = stop. Do not charge it, do not puncture it. Take it for safe disposal and get a replacement.
5. Look for corrosion or burnt marks on the connector. Clean light corrosion with isopropyl alcohol and let it dry fully.
6. Reassemble and test on battery.

### Fix 7: Replace the battery if it is dead

When the report says the capacity is gone, believe it.

1. Confirm: full charge capacity under ~20% of design, or the laptop dies the instant AC disconnects even after all software fixes.
2. Find the exact battery part number — printed on the old pack or in the manufacturer's parts lookup.
3. Buy genuine or reputable OEM-equivalent. Match voltage, watt-hour rating, and connector exactly.
4. After installing, charge to 100%, then run one full calibration cycle so the controller learns the new pack.
5. If a new battery still does not engage, the charging circuit on the motherboard is faulty — that is a board-level repair for a shop, not a DIY job.

## Closing

A laptop that only works plugged in is telling you the battery is out of the circuit — dead, undetected, or uncharged. The battery report tells you which within minutes. Software fixes (driver reinstall, EC reset) rescue the "undetected" cases; nothing rescues a truly dead battery except a replacement. Either way, you will know exactly where you stand after Fix 1.
