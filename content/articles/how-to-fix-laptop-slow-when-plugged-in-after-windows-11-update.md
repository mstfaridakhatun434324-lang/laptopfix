---
title: "Laptop Slow When Plugged In After a Windows 11 Update? Fix It"
slug: how-to-fix-laptop-slow-when-plugged-in-after-windows-11-update
date: 2026-09-27
categories: ["performance"]
tags: ["slow when plugged in", "windows 11 update", "charger issue", "power throttling"]
description: "Laptop slower on AC power than on battery after a Windows 11 update? Diagnose charger, power plan, and driver causes step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-when-plugged-in-after-windows-11-update.webp"
faqs:
  - q: "Why would my laptop be slower when plugged in than on battery?"
    a: "It's counterintuitive but common: the usual causes are a failing or underpowered charger that triggers the laptop's protective throttling, a power plan that applies the wrong settings on AC, or a driver (often the battery/ACPI driver) misreporting power state after an update. Some laptops also throttle when they detect a non-OEM charger. The update connection: new power-management drivers or firmware can change how the laptop interprets the charger's signal."
  - q: "Can a Windows update really cause slowdowns only when plugged in?"
    a: "Yes. Updates replace power-management drivers (Intel DPTF, ACPI battery drivers), chipset drivers, and BIOS-adjacent firmware interfaces. If the new driver misreads the charger's wattage or the battery's state, the laptop may engage protective throttling exclusively on AC power. Rolling back the battery/chipset driver or updating the BIOS frequently resolves exactly this pattern."
  - q: "How do I know if my charger is the problem?"
    a: "Check the charger's wattage label against your laptop's requirement — a 45W charger on a laptop that needs 90W causes throttling. Try a known-good OEM charger of the correct wattage; if speed returns on AC, the old charger is faulty or underrated. Also inspect the connector for damage and try a different wall outlet. Many laptops show a BIOS warning ('AC adapter wattage unknown') when the charger isn't communicating properly."
  - q: "Is it safe to keep using the laptop while it throttles on AC?"
    a: "Generally yes — throttling is a protective mechanism, not damage in progress. But don't ignore it long-term: if the cause is a failing charger delivering unstable power, that can stress components. And if the cause is overheating masked as power throttling, sustained heat shortens component life. Diagnose it within a few days rather than living with it indefinitely."
---

It's a strange one: unplug the laptop and it perks up; plug it in and everything drags — fans loud, apps stuttering, benchmarks tanking. You'd expect AC power to mean maximum performance, and when a Windows 11 update is the dividing line between "worked fine" and "slow on charger," the update changed something in the power path: a driver, a power plan default, or firmware behavior.

This is a diagnosis-first problem because the causes split into three very different buckets: the charger itself (wattage, failure, communication), Windows power settings (plans applying wrong on AC), and drivers/firmware (ACPI, chipset, BIOS). Work through them in that order — physical first, then settings, then drivers. For general post-update slowness, see [Windows 11 slow after update](/articles/windows-11-slow-after-update-how-to-fix/); for power-plan basics, [changing to Best Performance](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/) is a related read.

## Why this happens

- **Underpowered or failing charger**: The laptop detects insufficient wattage and throttles to protect itself — the #1 cause.
- **Charger communication failure**: The center pin/wire that identifies the adapter breaks; the laptop throttles assuming an unknown adapter.
- **Power plan misconfigured for AC**: An update can reset plans so "Plugged in" uses power-saver settings.
- **ACPI/battery driver corruption**: The update replaced the driver that reports power state; misreporting triggers throttling.
- **Intel DPTF / chipset driver issues**: Dynamic Platform and Thermal Framework misconfiguration throttles on AC specifically.
- **BIOS power settings changed**: Some updates reset BIOS-adjacent settings like adapter warnings or performance modes.
- **Overheating on AC**: Higher clocks on AC generate more heat; if cooling is marginal, thermal throttling hits only when plugged in.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the charger and power source

Rule out the physical layer first — it's the most common cause.

1. Read your charger's label: note the wattage (e.g., 65W, 90W, 130W) and compare with your laptop's requirement (check the manufacturer's specs or the original charger's rating).
2. Borrow or buy a known-good **OEM** charger of the correct wattage and test — if speed returns, your charger is faulty or underrated. Universal/third-party chargers often lack the identification chip and trigger throttling.
3. Inspect the charger's connector and cable for damage, and try a different wall outlet (avoid overloaded power strips).
4. Boot into BIOS (F2/Del at startup) — many laptops display adapter wattage there; "Unknown" means the charger isn't communicating.
5. If the charger is correct and healthy, the problem is software — continue.

### Fix 2: Verify power plans for the plugged-in state

Updates love to reset these.

1. Open **Settings** > **System** > **Power & battery** and check the **Power mode** for plugged-in — set it to **Best performance** (or at least Balanced).
2. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** for your active plan.
3. Check **Processor power management** > **Maximum processor state** — the **Plugged in** value should be 100%. If it's set low (some updates set it to 50–80%), that's your slowdown.
4. Also verify **Minimum processor state** (plugged in) isn't 0% with aggressive parking, and **System cooling policy** (plugged in) is **Active**.
5. If you use a vendor utility (Vantage, Armoury Crate, Dell Power Manager), confirm its AC profile is Performance, not Quiet/Battery-saver.

### Fix 3: Reinstall the ACPI battery and charger drivers

The update may have corrupted the power-state reporting chain.

1. Open **Device Manager** > **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device** (check "attempt to remove driver" if offered).
2. Also uninstall **Microsoft AC Adapter** under Batteries.
3. Shut down (don't restart), unplug the charger, remove the battery if it's removable, hold the power button 15 seconds, reinsert/reconnect, and boot — Windows reinstalls fresh drivers.
4. For sealed batteries: shut down, unplug for 30 seconds, then boot on AC — same effect.
5. Test performance on AC after Windows reinstalls the drivers.

### Fix 4: Update chipset and Intel DPTF drivers

The thermal/power framework drivers that govern throttling.

1. Open **Device Manager** > **System devices** and look for **Intel Dynamic Platform and Thermal Framework** entries — note driver dates.
2. Update chipset and DPTF drivers from your laptop manufacturer's support page (Dell, HP, Lenovo, ASUS) — use your exact model — or run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel-based systems.
3. Alternatively, run Windows Update's **optional driver updates**.
4. If the problem *started* with a recent DPTF/chipset update, roll it back: **Device Manager** > device > **Properties** > **Driver** > **Roll Back Driver**.
5. As a diagnostic (not a permanent fix), you can temporarily disable DPTF devices in Device Manager to confirm they're the throttling source — re-enable after testing.

### Fix 5: Check BIOS settings and update BIOS

Firmware governs adapter detection and throttling policy.

1. Enter BIOS (F2/Del/F12 at boot, varies by brand) and look for adapter/thermal settings: **Adapter Warnings**, **Thermal Management**, **Performance Mode**.
2. Ensure performance/thermal mode is set to **Performance** (not Quiet) for AC operation.
3. Check for a BIOS update on the manufacturer's support site — release notes mentioning "power," "thermal," or "adapter" are directly relevant.
4. Update BIOS following the manufacturer's instructions exactly (plugged in, don't interrupt).
5. After the update, re-check the adapter wattage readout in BIOS — a fixed identification issue confirms the firmware was at fault.

### Fix 6: Rule out thermal throttling on AC

AC power means higher clocks means more heat.

1. Install HWiNFO and log CPU temperatures and clock speeds during a heavy task on AC vs. on battery.
2. If temps hit 95–100°C on AC with clocks collapsing, you're thermal-throttling — clean vents with compressed air, ensure the laptop sits on a hard surface, and consider a cooling pad.
3. Check fans spin up properly on AC; a fan stuck at low speed (firmware bug) causes exactly this AC-only slowdown.
4. On older laptops, dried thermal paste is the classic cause — a professional repaste restores thermal headroom.
5. Only after thermals are verified healthy should you conclude the issue is purely power-policy.

### Fix 7: Reset power plans to defaults

When settings are tangled beyond manual repair.

1. Open an admin Terminal and run `powercfg -restoredefaultschemes` — this resets all power plans to Windows defaults.
2. Reboot, then set your preferred plan again via **Settings** > **System** > **Power & battery**.
3. Re-verify the advanced settings from Fix 2 after the reset.
4. If a vendor utility re-applies its own broken profile afterward, update or reinstall that utility — it's the real culprit.
5. As a final step, run Windows Update fully — Microsoft occasionally ships fixes for power-regression bugs in cumulative updates.

## Closing

"Slow only when plugged in" after an update almost always traces to one of three things: a charger the laptop no longer trusts, power-plan settings the update scrambled, or ACPI/chipset drivers misreporting power state. Test the charger first (it's the winner statistically), verify the plugged-in power settings, then work through the driver and firmware layers. The pattern is distinctive enough that the fix, once found, tends to be permanent.
