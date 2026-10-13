---
title: "Laptop Battery Only Charges When It's Off? Here's the Fix"
slug: how-to-fix-battery-only-charges-when-laptop-is-off-after-windows-11-update
date: 2026-09-12
categories: ["battery"]
tags: ["charges only when off", "windows 11", "charger wattage"]
description: "Battery only charges when the laptop is powered off after a Windows 11 update? It's usually charger wattage, heat, or a driver issue — here's how to fix it."
thumbnail: "/images/thumbs/how-to-fix-battery-only-charges-when-laptop-is-off-after-windows-11-update.webp"
faqs:
  - q: "Why does my laptop only charge when turned off?"
    a: "When on, the laptop consumes most of the charger's power, leaving nothing for the battery — this means the charger is underpowered, the battery is hot, or a driver is blocking charging while Windows runs."
  - q: "Can a Windows update cause charging to stop while the laptop is on?"
    a: "Yes. Updates can change power management drivers or thermal policies, making the system divert all charger power to running the laptop. Driver reinstalls and BIOS updates usually restore normal behavior."
  - q: "Is it bad to use the laptop while it only charges when off?"
    a: "It's inconvenient, not dangerous. But running on an underpowered charger long-term can cause performance throttling and sudden shutdowns under load — fix the root cause rather than living with it."
  - q: "How much wattage does my laptop charger need?"
    a: "Check the original brick's label or the manual — ultrabooks typically need 45-65W, performance laptops 90-130W, gaming laptops 180W+. A charger below spec causes exactly this symptom."
---
Here's a strange one: shut the laptop down, plug it in, and the battery charges fine. Boot into Windows, and charging stops — "plugged in, not charging" — even though nothing changed except the power state. If this started after a Windows 11 update, you're dealing with a power budget problem, and the update just exposed it.

When the laptop is off, the charger only feeds the battery. When it's on, the charger must run the whole system *and* charge the battery. If the charger can't do both — or if Windows misjudges the budget — charging loses. Let's fix the budget.

## Why this happens

- **The charger is underpowered.** A 65W brick on a laptop that wants 90W can run the system or charge the battery, but not both. When off, all 65W goes to the battery.
- **Heat blocks charging while running.** Many laptops pause charging when the battery is hot — and the battery is hottest while the system runs. Off = cool = charging allowed.
- **The 24H2 driver misreads the charger.** The update can break charger's wattage identification, so Windows thinks a 90W charger is a 45W one and refuses to charge while running.
- **USB-C PD negotiation fails in Windows.** Power Delivery negotiation is driver-driven; if it fails, the laptop falls back to low-wattage charging that only works when off.
- **A charge limit plus high usage.** With an 80% cap active and heavy load, some controllers prioritize running the system and never allocate power to top up.
- **Battery health protection kicked in.** Worn batteries generate more heat under load; the controller may allow charging only when cool (off) as a safety measure.

## How to fix it

Work through these in order. The charger check comes first because it's the most common cause.

### Fix 1: Verify the charger wattage

1. Read the output wattage printed on your charger brick (e.g., "65W", "90W").
2. Check your laptop's manual or the manufacturer's site for the required wattage.
3. If the charger is below spec — a 65W charger on a 90W laptop, a classic with universal chargers — that's your answer. Get the correct wattage. The [65W-on-gaming-laptop guide](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/) covers underpowered-charger symptoms in detail.
4. Even at the right wattage, try the original manufacturer charger — third-party bricks sometimes misreport their capacity after driver updates.

### Fix 2: Cool the laptop down and retest

1. Shut down all heavy apps, or better, let the laptop sit idle for 20 minutes.
2. Check that vents are clear and the laptop isn't on a bed or blanket.
3. With the system cool and idle, plug in and watch the battery icon for 5 minutes.
4. If charging starts when cool but stops under load, heat is the trigger — improve airflow, clean dust from vents, and consider a cooling pad.

### Fix 3: Reinstall the battery and charger drivers

1. Open **Device Manager** (**Windows key + X**).
2. Under **Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery**.
3. Under **System devices** or **Universal Serial Bus controllers**, look for USB-C/PD controller entries — right-click and **Update driver** > **Search automatically**.
4. Restart. Windows reinstalls the battery driver and renegotiates the charger handshake.

### Fix 4: Test with a different USB-C port (USB-C laptops)

1. Unplug and try every USB-C port on the laptop — manufacturers often wire only specific ports for full Power Delivery.
2. After the 24H2 update, the PD-capable port assignment can effectively change if the driver enumerates ports differently.
3. Mark the working port and use it for charging going forward.

### Fix 5: Reduce the power budget while running

If the charger is marginal, lighten the load so there's power left for charging.

1. Set **Settings** > **System** > **Power & battery** > **Power mode** to **Best power efficiency**.
2. Close heavy apps while charging — especially games, video renders, and anything pinning the CPU.
3. Lower screen brightness. These free up watts that the controller can redirect to the battery. If the battery drains even while plugged in under load, see [drain while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/).

### Fix 6: Update BIOS and chipset drivers

1. Download the latest **chipset driver** and **BIOS** from your manufacturer's support site.
2. Install chipset first, then BIOS, with the charger connected.
3. BIOS updates frequently include embedded-controller fixes for charge arbitration — deciding how power splits between system and battery.
4. After updating, test charging while running a moderate workload.

### Fix 7: Check battery health for heat-related protection

1. Run `powercfg /batteryreport /output "C:\battery-report.html"` in an admin Terminal.
2. If full charge capacity is below 70% of design, the aging battery runs hotter under load, and the controller may be protecting it by charging only when cool.
3. In that case the real fix is a battery replacement — the "only charges when off" is a symptom of a worn, hot battery, not a settings problem.

### Fix 8: Cap processor boost to free watts for charging

When the charger is marginal, trimming peak CPU power leaves more for the battery.

1. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. Expand **Processor power management** > **Maximum processor state** and set **Plugged in** to **90%** (from 100%).
3. This disables the highest CPU boost states — you lose a few percent of peak performance but free up 10-20W that the controller can redirect to charging.
4. Test: with the cap in place, the battery icon should switch to charging under your normal workload. If it does, your charger was right on the edge, and this cheaper-than-a-new-charger tweak solves it. For sustained heavy work, though, a properly sized charger is still the right long-term answer.

## Closing

"Only charges when off" is a power budget story: the charger can't feed the system and the battery at once, the battery is too hot while running, or Windows misjudges the charger after the update. Check wattage, cool it down, reinstall the drivers — and the battery will start charging while you work, not just while you sleep. Cap the processor boost as a stopgap, and size the charger correctly for the permanent fix.
