---
title: "Laptop Only Works on AC Power? Bring the Battery Back"
slug: what-to-do-if-laptop-only-works-on-ac-power
date: 2026-09-05
categories: ["battery"]
tags: ["ac power only", "battery not working", "windows 11"]
description: "Laptop dies the second you unplug it? Diagnose whether the battery is dead, disconnected, or just deeply discharged."
thumbnail: "/images/thumbs/what-to-do-if-laptop-only-works-on-ac-power.webp"
faqs:
  - q: "Why does my laptop only work when plugged in?"
    a: "The battery is either dead, disconnected, deeply discharged into protection mode, or not being recognized by Windows. The laptop itself is fine — it's running purely off the adapter. Work through connection and driver checks before assuming the battery needs replacing."
  - q: "Can a dead battery damage my laptop if I keep using AC power?"
    a: "A truly dead battery is inert and harmless, but a swollen or damaged one is not. If the battery area is warm, bulging, or smells odd while on AC power, stop using the laptop and have the battery removed professionally."
  - q: "Will the battery come back if I leave it charging overnight?"
    a: "Sometimes. A deeply discharged battery in protection mode can need several hours of trickle charging before the controller wakes up. Leave it plugged in (powered off) for 6-8 hours once — if there's still no sign of life, the battery is done."
  - q: "Should I remove a dead battery and just use AC?"
    a: "If the battery is removable, yes — running without a dead pack is fine and removes any risk. For internal batteries, leave it in place unless it's swollen; an inert internal battery does no harm sitting disconnected electrically."
---

Your laptop works perfectly — as long as the charger stays plugged in. The moment you unplug, it dies instantly, like someone pulled the plug on a desktop. The machine is telling you plainly: the battery is contributing nothing.

This is actually one of the easier battery problems to diagnose, because the suspects are few: the battery is dead, disconnected, deeply discharged, or invisible to Windows. Microsoft's own [Windows battery guidance](https://support.microsoft.com/en-us/windows) starts from the same place — verify what the system sees before changing anything. Here is how to determine which of the four you are dealing with.

## Why this happens

- **Battery at end of life:** After hundreds of cycles, cells degrade to the point where they hold effectively zero usable charge.
- **Deep discharge protection trip:** A battery left at zero for weeks can trip its protection circuit, which then refuses to wake without an extended trickle charge.
- **Loose or corroded connector:** The battery may be fine but electrically disconnected from the motherboard.
- **Battery not detected by Windows:** Driver or BIOS issues can leave a healthy battery invisible — see the [battery not detected guide](/articles/troubleshoot-battery-not-detected-on-laptop/).
- **Swollen battery disconnected by its own safety circuit:** A swelling pack's controller may permanently disconnect the cells as a safety measure.
- **Wrong or failing charger:** An underpowered adapter can run the laptop but never deliver the extra current needed to charge the battery.

## How to fix it

Work through these in order, from quickest to most involved. Stop at the step that solves it.

### Fix 1: Check what Windows thinks the battery is doing

Get the current status before touching anything.

1. Hover over the battery icon in the taskbar and read the exact message — "plugged in, not charging," a percentage that never moves, or no battery at all.
2. Open **Settings > System > Power & battery** and check whether a battery is listed.
3. Press **Win + X**, open **Terminal (Admin)**, and run `powercfg /batteryreport /output "C:\battery-report.html"`.
4. If the report shows a battery with near-zero full charge capacity, the pack is worn out. If it shows no battery, jump to Fix 4.

### Fix 2: Try the overnight trickle charge

A deeply discharged battery sometimes just needs patience.

1. Shut the laptop down completely — not sleep, full shutdown.
2. Leave the charger plugged in for **6 to 8 hours** or overnight.
3. Power on and check the battery status. If the percentage has moved off zero, the protection circuit woke up — let it charge fully.
4. If nothing changed, the battery is not in protection mode; it is dead or disconnected.
5. One more patience test worth trying: some controllers need the laptop powered on and idle (not off) during the long charge to wake up. If the powered-off attempt failed, try 4 hours plugged in while the laptop sits at the lock screen.

### Fix 3: Test the charger

Make sure the adapter can both run the laptop and charge the battery.

1. Check the wattage on the adapter label against your laptop's requirement.
2. Borrow a known-good adapter of equal or higher wattage and test for an hour.
3. If the borrowed charger starts charging the battery, replace your adapter. Gaming laptops are especially picky — see [whether your charger wattage is enough](/articles/best-way-to-fix-65w-charger-not-enough-for-gaming-laptop/).
4. Inspect the DC jack for looseness or damage; a wobbly jack can deliver enough power to run the system but not enough stable current to charge.

### Fix 4: Reseat the battery

A battery that is not making proper contact behaves exactly like a dead one.

1. Power off and unplug everything.
2. If the battery is removable: take it out, wipe the metal contacts with a dry cloth, and reseat it firmly.
3. If it is internal: remove the bottom panel, disconnect the internal battery cable first for safety, then unplug and firmly replug the battery connector.
4. Reassemble, plug in, and check whether the battery is now recognized and charging.

### Fix 5: Reset the battery drivers

Windows may simply have lost track of a working battery.

1. Open **Device Manager** via **Win + X**.
2. Expand **Batteries**, right-click each **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Restart the laptop and let Windows reinstall the drivers.
4. Check **Settings > System > Power & battery** for the battery's return.

The detailed version of this reset is in the [ACPI battery driver guide](/articles/how-to-reset-acpi-battery-driver-on-laptop/).

### Fix 6: Check the BIOS for battery status

The BIOS sees hardware before Windows gets involved.

1. Restart and press **F2** (Dell, ASUS), **F1** (Lenovo), or **F10** (HP) to enter the BIOS.
2. Find the battery information page and read the status.
3. If the BIOS reports a battery with 0 percent health or a failure code, the pack is done — no software will revive it.
4. If the BIOS sees no battery at all after reseating, the pack's controller is dead.

### Fix 7: Replace the battery

When every check points to a dead pack, replacement is the answer.

1. Confirm the diagnosis: battery report shows near-zero capacity, BIOS reports failure, and reseating changed nothing.
2. Order a genuine or manufacturer-approved battery for your exact model number.
3. For internal batteries, follow a video guide for your specific model or have a shop do it — the connectors are fragile.
4. After installation, charge to 100 percent and run one [calibration cycle](/articles/how-to-calibrate-laptop-battery-windows-11/) so the gauge learns the new pack.
5. Recycle the old battery properly — electronics stores and municipal collection points accept lithium batteries.
6. After the new battery is in and calibrated, keep an eye on it for the first week: it should charge smoothly to 100 percent and discharge evenly. Any early weirdness with a new pack usually means a seating issue, not a bad battery.

## Closing

A laptop that only works on AC power is giving you a clear message: the battery is out of the picture. The overnight charge and reseat cost nothing and revive a surprising number of "dead" batteries. When they do not, the battery report and BIOS give you the evidence to replace the pack with confidence instead of guesswork.
