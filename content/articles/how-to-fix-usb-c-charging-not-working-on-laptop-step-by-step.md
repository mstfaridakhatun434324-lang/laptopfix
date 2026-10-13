---
title: "USB-C Charging Not Working on Your Laptop? Step-by-Step Fix"
slug: how-to-fix-usb-c-charging-not-working-on-laptop-step-by-step
date: 2026-09-22
categories: ["battery"]
tags: ["usb-c charging", "power delivery", "charger", "troubleshooting"]
description: "Laptop won't charge over USB-C? Work through this step-by-step checklist covering cables, wattage, ports, drivers, and BIOS settings."
thumbnail: "/images/thumbs/how-to-fix-usb-c-charging-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "Why won't my laptop charge with a USB-C charger?"
    a: "The usual reasons: the charger or cable doesn't support USB Power Delivery at your laptop's required wattage, you're using a data-only cable, the USB-C port doesn't support charging, or the port's power controller needs a reset. Work through cable, charger, port, and driver checks in that order."
  - q: "Do all USB-C ports on a laptop support charging?"
    a: "No. Many laptops have multiple USB-C ports but only one supports charging — check for a small power or lightning icon next to the port, or look in the manual. Plugging into a data-only port does nothing."
  - q: "Can any USB-C cable charge a laptop?"
    a: "No. Many cheap USB-C cables are data-only or rated for just 15W phone charging. Laptop charging needs a cable rated for USB Power Delivery at 60W or more (100W+ for gaming laptops). The cable's rating is usually printed on the connector housing."
  - q: "Is USB-C charging slower than the barrel charger?"
    a: "It can be, if the USB-C charger delivers fewer watts than the original adapter. A 65W USB-C charger on a laptop that wants 90W will charge slowly or only maintain the battery during light use. Match the wattage for full-speed charging."
---
USB-C charging promised one cable for everything, and when it works it's wonderful. But the standard hides a minefield: not every USB-C port charges, not every cable carries power, and not every "65W" charger actually delivers it. The result is a laptop that charges fine on its barrel adapter but completely ignores a USB-C charger — or charges so slowly the percentage barely moves.

The fix is a process of elimination across four layers: the cable, the charger, the port, and the software. Go in order and you'll find the broken layer quickly. Don't skip the boring steps — in USB-C troubleshooting, the boring steps are where the answer lives, because every failure mode looks identical from the outside.

## Why this happens

- **Wrong cable:** data-only or low-wattage cables can't carry laptop charging current.
- **Underpowered charger:** a 30W phone charger can't feed a 65W laptop; the laptop may refuse it outright.
- **Wrong port:** only specific USB-C ports on many laptops support power input.
- **No Power Delivery negotiation:** charger and laptop fail to agree on a voltage, often due to cheap non-compliant hardware.
- **Dirty or damaged port:** lint and bent pins break the connection.
- **USB power controller glitch:** the port's controller chip can lock up and need a reset.
- **BIOS/firmware limitation:** some laptops need a BIOS update for proper USB-C PD behavior, or have charging disabled in BIOS.
- **Driver issues:** the USB and battery drivers mediate charging; corruption breaks the chain.

## How to fix it

Work through these in order — each step eliminates one layer.

### Fix 1: Use the right port

1. Look for a power plug or lightning icon next to the USB-C ports — that's the charging-capable one.
2. Check the manual if there's no marking; on many models only the left-side port charges.
3. Plug the charger into that specific port and wait 30 seconds — PD negotiation isn't instant.

### Fix 2: Verify the cable is PD-rated

1. Check the cable for printed wattage ratings (60W, 100W) on the connector housings.
2. Swap in a known-good cable rated for your laptop's wattage. Thick, short cables from reputable brands are the safest bet.
3. Avoid cables longer than 2 meters for high-wattage charging — voltage drop over long cables causes negotiation failures.
4. If the laptop charges with the new cable, the old one was data-only or underrated. Label it so you don't reuse it.

### Fix 3: Confirm the charger's wattage and PD support

1. Read the charger's label: it must list USB Power Delivery (PD) and a wattage at or above your laptop's requirement.
2. Phone chargers (18–30W) won't cut it for most laptops — you need 45W minimum for ultrabooks, 65–100W for most others.
3. Test with a known-good PD charger of the correct wattage. Multi-port chargers: use the port labeled for laptop/high-power output, since power is shared across ports.

### Fix 4: Clean the USB-C port

1. Power off the laptop and unplug everything.
2. Shine a light into the port and look for lint, dust, or bent pins.
3. Remove debris gently with a wooden toothpick or compressed air — never metal.
4. Reconnect and check whether charging starts. A surprising number of "dead" ports are just dirty.

### Fix 5: Reset the USB power controller

1. Shut down fully (Shift + Shut down), unplug all USB-C devices and the charger.
2. Hold the power button for 30 seconds to reset the embedded controller.
3. Boot up, then plug in the USB-C charger before any other USB devices.
4. This clears the controller lockups that silently block PD negotiation.

### Fix 6: Update drivers and BIOS

1. In **Device Manager**, expand **Universal Serial Bus controllers** and check for warning icons. Update or reinstall any flagged USB drivers.
2. Reinstall the battery drivers too (**Batteries > Microsoft ACPI-Compliant Control Method Battery > Uninstall**, then reboot).
3. Check the manufacturer's support site for a BIOS update — USB-C PD fixes appear regularly in changelogs. Flash with the barrel charger connected if you have one. General Windows power troubleshooting is documented at [Microsoft support](https://support.microsoft.com/en-us/windows).

### Fix 7: Check BIOS USB-C settings

1. Enter the BIOS/UEFI setup and look for USB-C, Power Delivery, or Thunderbolt power settings.
2. Make sure USB-C charging isn't disabled — some business laptops ship with it off.
3. On Thunderbolt ports, ensure any "Thunderbolt pre-boot" or security settings aren't blocking the power contract.

### Fix 8: Test methodically to isolate the fault

1. Try your charger + cable on a different USB-C laptop, and a known-good charger + cable on yours.
2. If yours charges with the known-good set, your charger or cable is at fault — replace the failing piece.
3. If nothing charges it via USB-C but the barrel adapter works, the port's power circuitry may be damaged — that's a service-center repair. Document your tests; they'll speed up the warranty claim.

## Closing

USB-C charging failures are almost never mysterious once you check the layers: the right port, a PD-rated cable, a charger with enough watts, and a clean port cover the vast majority. The frustrating part is that any weak link looks identical — "not charging" — so resist the urge to buy a new charger until you've tested the cable and port first. Methodical elimination beats random replacement every time. And once USB-C charging works, label your good cable — future you, digging through a drawer of identical-looking cables, will appreciate it. One working setup beats three mystery cables.

Related: [laptop battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) and [Surface not charging](/articles/how-to-fix-surface-laptop-battery-not-charging-on-windows-10/). If USB-C works but the battery drains unusually fast afterward, check [which app is draining your battery](/articles/how-to-find-which-app-is-draining-battery-in-windows-11-24h2/) — slow charging plus fast drain is a miserable combination worth fixing from both ends.
