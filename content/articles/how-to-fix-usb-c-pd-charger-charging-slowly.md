---
title: "USB-C Charger Charging Slowly? Speed It Back Up"
slug: how-to-fix-usb-c-pd-charger-charging-slowly
date: 2026-09-09
categories: ["battery"]
tags: ["usb-c charging", "slow charging", "power delivery"]
description: "USB-C charger crawling instead of fast-charging? Fix the wattage, cable, and port issues that throttle Power Delivery charging."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly.webp"
faqs:
  - q: "Why is my USB-C charger charging my laptop so slowly?"
    a: "USB-C Power Delivery negotiates wattage between the charger, cable, and laptop. Slow charging means the negotiation settled low — usually because the charger is underpowered, the cable can't carry the wattage, or you're plugged into a data-only USB-C port instead of a charging port."
  - q: "Does the USB-C cable affect charging speed?"
    a: "Hugely. Many USB-C cables only support 60W even if the charger can deliver 100W, and cheap cables may not support Power Delivery at all. The cable must be rated for the wattage your laptop needs — look for 100W or 240W ratings on quality cables."
  - q: "Can I use a phone charger for my laptop?"
    a: "It will usually charge, but very slowly — a 25W phone charger on a 65W laptop means hours for a meaningful charge, and the laptop may discharge while in use. It won't damage anything, but it's a stopgap, not a solution."
  - q: "How do I know what wattage my laptop is actually getting?"
    a: "Check Settings > System > Power & battery in Windows 11, which sometimes reports slow charger warnings. A USB-C power meter dongle (about $15-20) plugged inline shows exact volts, amps, and watts — the definitive answer."
---

USB-C was supposed to simplify charging: one cable for everything. In practice, "one cable" hides a negotiation between your charger, your cable, and your laptop — and when any of the three undersells itself, you get a trickle instead of a charge. Your laptop might even lose battery while plugged in.

Slow USB-C charging is almost never a Windows problem. It is a hardware negotiation problem, which means the fixes are physical: the right charger, the right cable, the right port. The USB-C Power Delivery spec allows chargers and devices to negotiate anything from 5W to 240W, and when that handshake goes wrong you get a trickle. Windows 11 will even warn you about [slow chargers](https://support.microsoft.com/en-us/windows) in the Settings app.

## Why this happens

- **Underpowered charger:** A 45W adapter on a laptop that wants 90W+ will charge slowly or not at all under load. This is the number one cause.
- **Low-rated cable:** The cable is the forgotten link. A cable rated for 60W caps a 100W charger at 60W, silently.
- **Wrong USB-C port:** Many laptops have multiple USB-C ports but only one or two support Power Delivery charging. The others are data-only.
- **Power strip or dock in the middle:** Hubs and docks consume power and some renegotiate PD downward, especially unpowered ones.
- **Laptop drawing more than the charger gives:** Gaming or rendering while plugged into a weak adapter means the battery drains despite being "charging."
- **Dirty or damaged port:** Lint and corrosion in the USB-C port cause poor contact, and PD may fall back to a safe low wattage.

## How to fix it

Work through these in order, from quickest to most involved. Stop at the step that solves it.

### Fix 1: Match the charger wattage to the laptop

Check the math first — it takes thirty seconds.

1. Find your laptop's required wattage: check the original adapter's label or the manufacturer's specs page.
2. Check your USB-C charger's output on its label — look for the PD wattage, not just "fast charge."
3. If the charger delivers less than the laptop wants, that is your answer. Buy a PD charger rated at or above the laptop's requirement.
4. For gaming laptops, note that even a correct-wattage charger can struggle — see [whether your charger wattage is enough](/articles/best-way-to-fix-65w-charger-not-enough-for-gaming-laptop/).

### Fix 2: Upgrade the cable

The cable is guilty more often than people think.

1. Check your cable for a wattage rating — quality cables print "100W" or "240W" on the connector housing.
2. If there is no rating, assume it is a basic 60W-or-less cable and replace it.
3. Buy a USB-IF certified cable rated for at least your charger's wattage, from a reputable brand.
4. Retest charging speed with the new cable before changing anything else.

### Fix 3: Use the correct USB-C port

Not all ports are equal.

1. Check your laptop's manual or the manufacturer's site for which USB-C ports support charging — they are often marked with a small plug or lightning icon.
2. Move the charger to a charging-capable port.
3. If your laptop has Thunderbolt ports, those always support PD charging — prefer them.
4. Avoid charging through a hub or dock for this test; plug the charger directly into the laptop.

### Fix 4: Clean the port and check the connection

Poor contact forces PD to negotiate down to safe levels.

1. Power off the laptop and unplug everything.
2. Shine a light into the USB-C port and look for lint, dust, or bent pins.
3. Gently clean with a wooden toothpick or compressed air — never metal tools.
4. Plug the cable in firmly; it should seat with a solid click and no wobble.

### Fix 5: Remove middlemen — docks, hubs, and extensions

Simplify the chain to isolate the bottleneck.

1. Unplug from any dock, hub, or USB-C extension and connect the charger directly to the laptop with a good cable.
2. If charging speeds up, the dock or hub was throttling PD — check whether it has its own power supply and whether it is rated for your wattage.
3. Some docks reserve power for themselves; a 90W dock may only pass 65W to the laptop.
4. If you must use a dock, get one whose passthrough wattage meets your laptop's needs.

### Fix 6: Check Windows power settings

Windows can slow charging indirectly through power plans.

1. Open **Settings > System > Power & battery** and look for any "slow charger" warning — Windows 11 flags underpowered adapters here.
2. Set **Power mode** to **Best power efficiency** while charging on a weak adapter, so more of the incoming power goes to the battery instead of the CPU.
3. Close heavy apps during charging if the adapter is marginal.
4. Disable **USB selective suspend**: open **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **USB settings**, and set **USB selective suspend** to **Disabled**.

### Fix 7: Verify with a power meter and replace the weak link

Stop guessing and measure.

1. Get an inexpensive USB-C power meter dongle and plug it inline between charger and laptop.
2. Read the actual negotiated voltage and wattage.
3. If the meter shows far less than the charger's rating, the cable or port is the bottleneck. If it shows the full rating but charging is still slow, the laptop's charging circuit may need service.
4. Replace whichever link underperforms, then re-measure to confirm the fix.
5. Keep the meter — it is useful for spot-checking any USB-C charger or cable in the future, and it pays for itself the first time it stops you buying a replacement you did not need.

For broader charging diagnostics, a [battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) shows whether the battery itself is healthy while you sort the power delivery.

## Closing

Slow USB-C charging is a negotiation failure, and negotiations fail at the weakest link. Match the charger wattage, use a properly rated cable, pick the right port, and measure with a meter instead of guessing. That sequence resolves nearly every slow-charging case without touching Windows at all — and the meter means you will never have to guess again.
