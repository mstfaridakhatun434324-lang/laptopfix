---
title: "Laptop Battery Only Charges When Turned Off on Windows 11? Fix It"
slug: how-to-fix-battery-only-charges-when-laptop-is-off-on-windows-11
date: 2026-10-13
categories: ["battery"]
tags: ["battery", "charging", "power", "windows 11"]
description: "Battery charges only when your Windows 11 laptop is off? Diagnose the power shortfall and fix it with these 7 steps."
thumbnail: "/images/thumbs/how-to-fix-battery-only-charges-when-laptop-is-off-on-windows-11.webp"
faqs:
  - q: "Why does my laptop only charge when it's off?"
    a: "The charger can't supply enough power to both run the laptop and charge the battery at the same time. When the machine is off, all the adapter's wattage goes to the battery. When it's on, the system consumes everything and there's nothing left for charging. An underpowered or failing adapter is the usual cause."
  - q: "Is it bad to use a laptop that only charges when off?"
    a: "It's a warning sign, not an emergency. The laptop is telling you the power budget doesn't add up. Continuing to run it this way stresses the adapter (which may overheat) and the battery (which cycles unnecessarily). Fix the underlying power shortfall rather than living with it."
  - q: "Can a Windows setting cause charging-only-when-off?"
    a: "Rarely, but yes — an aggressive custom power plan or a vendor performance profile can push power draw so high that nothing remains for charging. More often it's the adapter. Rule out the charger first; it's the cause in the majority of cases."
  - q: "Should I buy a higher wattage charger to fix this?"
    a: "Only up to the laptop's rated wattage — check the label on the bottom of the machine. Buying the correct rated adapter is the fix. Going far above the rating is safe (the laptop draws only what it needs) but unnecessary and more expensive."
---

Here's the strange pattern: shut the laptop down, plug it in, and the battery charges normally. Boot into Windows 11, and the percentage freezes — or even falls — despite the charger being connected. It feels like Windows is blocking the charge, but the real story is almost always about power arithmetic: your adapter produces X watts, the running laptop consumes all X watts, and zero are left for the battery.

When the machine is off, consumption drops to nearly nothing, so the full adapter output flows into the battery. The seven fixes below identify where the power is going and restore the balance — usually by fixing the supply side, sometimes by trimming the demand side.

## Why this happens

- **An underpowered or failing adapter.** The most common cause. A 65W adapter on a laptop that needs 90W, or an aging adapter that no longer delivers its rated wattage, can't run the system and charge simultaneously.
- **A damaged cable or loose connector.** Resistance from a frayed cable or a wobbly jack reduces the effective power reaching the laptop.
- **High power draw from performance settings.** An aggressive power plan, a discrete GPU running constantly, or a vendor "performance" profile can push consumption past what the adapter supplies.
- **A degraded battery with high internal resistance.** Worn cells accept charge inefficiently, so the limited surplus power can't push energy in while the system runs.
- **Dust-clogged cooling forcing max fan speeds.** Fans at full tilt add meaningful power draw on top of an already hot system.
- **USB devices drawing bus power.** Multiple power-hungry USB peripherals (external drives, hubs) siphon wattage the battery needs.

## How to fix it

Work through these in order — supply first, then demand.

### Fix 1: Verify the adapter matches the laptop's rating

The label on the laptop is the truth; the adapter must match it.

1. Flip the laptop over and read the required input wattage (volts × amps).
2. Read your adapter's output rating. If it's lower — a 65W brick on a 90W laptop, for example — you've found the problem.
3. Borrow or buy an adapter at the correct rated wattage (equal or higher is fine) and test: boot into Windows and watch the battery icon for 10 minutes.
4. If the correct adapter charges while the system runs, replace the undersized one permanently. If the original is lost, look up the correct part number on [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support. This mirrors the classic [65W-charger-too-weak problem on gaming laptops](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-on-windows-11/).

### Fix 2: Test the adapter for degradation

An adapter can be the right wattage on paper and still fail in practice.

1. Feel the brick during use — excessive heat, buzzing, or a burning smell means it's failing.
2. Inspect the full cable length for kinks, fraying, and heat discoloration, especially near the brick and connector.
3. Wiggle the connector gently where it meets the laptop. If the charging indicator flickers, the cable or jack is intermittent.
4. Test with a known-good adapter of the correct wattage. If charging-while-on works with the replacement, retire the old adapter — don't keep it as a spare.

### Fix 3: Reduce power draw with the right power mode

If the adapter is borderline, trimming demand can tip the balance.

1. Open **Settings > System > Power & battery** and set **Power mode** to **Best power efficiency**.
2. Unplug all non-essential USB devices — external hard drives and powered hubs are the biggest sippers.
3. Close GPU-heavy apps. On laptops with dual graphics, force integrated graphics for the desktop: **Settings > System > Display > Graphics**, and set apps to **Power saving**.
4. Retest: with demand lowered, a marginal adapter may now have enough surplus to charge.

### Fix 4: Check for a runaway process consuming power

Something invisible might be eating the wattage.

1. Open **Task Manager** (**Ctrl + Shift + Esc**) and sort the **Processes** tab by **Power usage**.
2. Look for **Very high** entries that shouldn't be there — stuck installers, runaway browser processes, or crypto miners (in the worst case).
3. End the suspicious tasks and watch the battery icon.
4. Check the **Startup apps** tab and disable anything with high startup impact that you don't need.

### Fix 5: Clean the cooling system

Hot components and screaming fans waste power.

1. Shut down, unplug, and blow compressed air through the intake and exhaust vents in short bursts.
2. Check that the fans actually spin down at idle — fans stuck at maximum indicate a thermal or driver problem.
3. Update the BIOS from the manufacturer's support site; fan-curve fixes are common in BIOS changelogs.
4. A cooler laptop draws less power, leaving more headroom for charging.

### Fix 6: Reinstall the battery drivers

Rule out the software side before concluding it's purely a power-budget issue.

1. Open **Device Manager**, expand **Batteries**, and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
2. Shut down fully (**Shift + Shut down**), unplug for 60 seconds, then boot with the charger connected.
3. Windows reinstalls the drivers during boot.
4. If the battery now charges while Windows runs, the driver was misreporting the power state. If nothing changed, the cause is the power budget, not software.

### Fix 7: Assess the battery's health

A worn battery can refuse charge current while the system runs.

1. In **Terminal (Admin)**, run `powercfg /batteryreport` and open the HTML file.
2. Compare **Design Capacity** with **Full Charge Capacity**. Below 70% indicates significant wear.
3. Check the **Battery capacity history** for a steep recent drop.
4. If the battery is heavily worn, replace it — and pair the new pack with the correct-wattage adapter. [Understand what the capacity numbers mean](/articles/how-to-check-battery-design-vs-full-charge-capacity-on-windows-11/) before you decide.

## Closing

"Charges only when off" is your laptop's way of saying the power math doesn't work while it's running. In most cases the adapter is undersized or dying — match it to the laptop's rated wattage and the problem disappears. Only after the supply side checks out should you chase software causes, because no driver fix can create watts that aren't there.
