---
title: "Why Your Laptop Battery Only Charges When It's Off"
slug: what-to-do-if-battery-only-charges-when-laptop-is-off
date: 2026-09-15
categories: ["battery"]
tags: ["charges only when off", "not charging", "charger wattage"]
description: "Battery charges fine when the laptop is off but not while you're using it? The causes and fixes, from weak chargers to power settings."
thumbnail: "/images/thumbs/what-to-do-if-battery-only-charges-when-laptop-is-off.webp"
faqs:
  - q: "Why does my laptop only charge when turned off?"
    a: "The charger can't supply enough power for both running the laptop and charging the battery simultaneously. When the machine is off, all the charger's output goes to the battery; when on, the system consumes most of it."
  - q: "Is it bad to use my laptop while it's charging slowly?"
    a: "Not harmful, just slow. But if the battery actually drains while plugged in and in use, your charger is seriously undersized or failing — that situation deserves a proper charger."
  - q: "Can Windows settings cause this?"
    a: "Rarely on their own, but aggressive performance modes increase power draw, widening the gap between what the charger provides and what the system needs. Power saver modes reduce the shortfall."
  - q: "Will a bigger charger fix it?"
    a: "Usually yes, if the charger is the bottleneck. Match or exceed the wattage printed on the laptop's bottom sticker or in its manual, and use the correct voltage."
---

It's a strange symptom: shut the laptop down, plug it in, and the battery charges perfectly. Boot up, start working, and the percentage freezes — or even drops — despite the charger being connected. The machine works fine on AC power; it just won't *charge* while awake.

This is almost always a power-budget problem. Your charger produces X watts; your running laptop consumes Y watts; the battery gets whatever's left. When Y eats nearly all of X, charging stalls the moment you power on. The fix is either increasing X (better charger) or decreasing Y (lighter load) — preferably both.

## Why this happens

- **Undersized charger:** the most common cause — a 45W or 65W adapter on a machine that needs 90W+.
- **Failing charger:** an aging adapter whose output has degraded below its rating.
- **High-performance power plan:** max-performance modes push power draw above what the charger can spare.
- **Power-hungry workload:** gaming, rendering, or compiling while plugged in consumes the charging budget.
- **USB-C PD negotiation failure:** the laptop and charger fail to agree on a higher wattage and fall back to a trickle.
- **Damaged cable:** a worn cable increases resistance, reducing delivered power.
- **BIOS power limits:** some firmware caps charging current while the system is under load to manage heat.

## How to fix it

Work through these in order.

### Fix 1: Check your charger's wattage against the laptop's requirement

The core diagnostic.

1. Flip the laptop over and read the power input spec, e.g. **19.5V ⎓ 6.15A (120W)**.
2. Read your charger's output label and compare. If the charger is smaller, you've found it.
3. Common trap: using a phone or tablet USB-C charger (18–45W) on a laptop that wants 65W+.
4. Another trap: docks and hubs that advertise passthrough charging but deliver far less than the brick alone.
5. Plug the original (or correctly sized) charger directly into a wall outlet and retest while the laptop is on.
6. The 24H2-specific variant of this issue is covered in [battery only charges when off on Windows 11 24H2](/articles/how-to-fix-battery-only-charges-when-laptop-is-off-in-windows-11-24h2/).

### Fix 2: Get a properly sized charger

If the math doesn't work, no setting will fix it.

1. Buy a charger matching the laptop's rated voltage and equal-or-higher wattage.
2. For USB-C laptops, ensure both charger and cable support the needed PD wattage (cables matter — many top out at 60W).
3. Stick to reputable brands; out-of-spec PD negotiation causes exactly the "charges only when off" pattern.
4. Keep the receipt and test immediately: with the new charger, the battery should gain percentage during normal use.
5. If a correct charger doesn't help, the problem is elsewhere — continue below.
6. **Pro tip:** borrow a higher-wattage charger from a friend *before* buying — 30 minutes of on-charge testing tells you definitively whether wattage is the bottleneck, and it costs nothing.
7. Watch the charge indicator while switching between light and heavy use (web browsing vs. video rendering); a percentage that climbs at idle but stalls under load confirms the charger is exactly on the edge of sufficiency.

### Fix 3: Reduce power draw while plugged in

Narrow the gap between consumption and charger output.

1. In **Settings > System > Power & battery**, set **Power mode** to **Best power efficiency** or **Balanced** (not Best performance).
2. Close games and heavy apps while charging; check **Task Manager** (Ctrl+Shift+Esc) for CPU hogs.
3. Lower screen brightness to around 50%.
4. Disconnect external monitors, USB hubs, and peripherals that draw power.
5. Retest: if the battery now charges (slowly) while on, the charger is marginal but workable with lighter loads.

### Fix 4: Inspect the cable and connector

Degraded connections silently cut delivered wattage.

1. Examine the full cable for kinks, fraying, or melted spots.
2. Check barrel connectors for bent center pins and USB-C plugs for lint or damage.
3. Wiggle the connector gently while watching the charging indicator — flickering means a bad connection.
4. Try a different cable with the same brick (if detachable) to isolate which part failed.
5. Clean USB-C ports with compressed air and a wooden toothpick — never metal.

### Fix 5: Reinstall battery drivers and reset the EC

A confused charge controller can misallocate power.

1. Open **Device Manager**, expand **Batteries**, and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
2. Shut down fully, unplug everything, and hold the power button for 30–60 seconds.
3. Reconnect the charger and boot — Windows reinstalls the drivers.
4. Test charging while the laptop is on.
5. If the battery also [drains while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/), the driver reset often helps that too.

### Fix 6: Update the BIOS

Firmware controls USB-C PD negotiation and charge-current allocation.

1. Download the latest BIOS from your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)).
2. Install with the charger connected; don't interrupt it.
3. After rebooting, test USB-C charging specifically — BIOS notes often mention PD fixes.
4. Re-check any BIOS battery settings (charge thresholds, adapter warnings) that might limit current.

### Fix 7: Check for overheating throttling charge current

Some firmware reduces charging current when the system is hot.

1. Feel the chassis and listen to fans during use while plugged in.
2. Ensure vents are clear; clean dust with compressed air.
3. Avoid charging-while-gaming on a soft surface — that's maximum heat plus maximum draw.
4. If cooling improves on-charge behavior, heat was part of the bottleneck.
5. Consider a cooling pad for sustained heavy workloads.

### Fix 8: Test the battery's own health

A worn battery accepts charge slowly, exaggerating the symptom.

1. Run `powercfg /batteryreport /output "C:\battery-report.html"` in an admin terminal.
2. If full charge capacity is under 60% of design, the battery's high internal resistance is part of the problem.
3. A failing battery plus a marginal charger combine into exactly this symptom.
4. Replace a worn battery with a genuine part and retest with the correct charger.

## Closing

"Charges only when off" is your charger's way of saying it can't keep up. Size the adapter to the laptop's actual requirement, trim unnecessary power draw, and the battery will charge whether the machine is awake or asleep — no more babysitting the power button just to get a charge reliably every time.

One last thing worth knowing: this symptom often appears gradually, because chargers lose output capacity as they age — a 65W brick that once kept up can quietly degrade into a 45W-class brick over a few years. If the problem crept up on a charger that *used* to work fine, the adapter itself aging out is the most likely story, and a fresh OEM-spec replacement fixes it in one step.
