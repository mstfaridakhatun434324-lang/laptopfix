---
title: "USB-C PD Charger Charging Slowly? How to Speed It Up"
slug: best-way-to-fix-usb-c-pd-charger-charging-slowly
date: 2026-09-27
categories: ["battery"]
tags: ["usb-c slow charging", "power delivery", "pd charger", "charging speed"]
description: "USB-C charger trickling power into your laptop? These are the highest-impact fixes for slow Power Delivery charging, ranked by what actually helps."
thumbnail: "/images/thumbs/best-way-to-fix-usb-c-pd-charger-charging-slowly.webp"
faqs:
  - q: "Why is my USB-C charger charging my laptop so slowly?"
    a: "Almost always a power mismatch: the charger's wattage is too low for the laptop, the cable can't carry the full wattage, you're in the wrong port, or the laptop is consuming nearly as much as the charger delivers. USB-C charging only works well when charger, cable, and port all agree on high wattage."
  - q: "Does the cable matter for USB-C charging speed?"
    a: "Enormously. Many USB-C cables are rated for only 60W or even 15W despite looking identical to 100W+ cables. A 100W-capable laptop paired with a 60W cable charges at 60W max — the cable is the bottleneck, and it looks exactly like a charger problem."
  - q: "What wattage USB-C charger do I need?"
    a: "Match or exceed your laptop's requirement: ultrabooks typically need 45-65W, performance laptops 90-100W, and gaming laptops usually can't use USB-C charging at all. Check the original barrel charger's wattage as your target."
  - q: "Why does charging speed up when I close the lid?"
    a: "Because the charger was barely covering the laptop's running power draw. With the lid closed and the system idle, nearly all the charger's wattage goes into the battery instead of being split with the CPU, GPU, and screen."
---

Slow USB-C charging is a math problem wearing a disguise. Your laptop needs a certain wattage; your charger offers a certain wattage; the cable permits a certain wattage — and the actual charging speed is the lowest of the three, minus whatever the laptop burns just staying on. Fix the bottleneck and the speed follows. Here are the fixes ranked by impact.

Before you start, grab the three numbers if you can: the wattage your laptop wants (on the original charger's label), the wattage your USB-C charger offers (on its label), and your cable's rating (printed on the connector, if you're lucky). If the charger's number is the smallest, that's your answer before you even begin. Most people never check the cable's number, which is exactly why the cable is the culprit so often — it's the one number nobody knows.

## Why this happens

- **Charger wattage too low.** A 45W phone charger on a 90W laptop delivers a trickle — or barely holds the battery steady under load.
- **The cable is the bottleneck.** Plenty of USB-C cables top out at 60W. The charger can offer 100W all day; the cable won't carry it.
- **Wrong port.** Many laptops have multiple USB-C ports but only one supports Power Delivery input — the others are data-only.
- **High power draw while charging.** Gaming or rendering while plugged into a marginal charger means almost nothing reaches the battery.
- **PD negotiation failure.** Charger and laptop fail to agree on a voltage profile and fall back to a safe low wattage (often 15W).
- **Dirty or worn port/cable** causing the negotiation to drop to lower profiles intermittently.
- **The laptop's own PD input cap.** Some ultrabooks limit USB-C intake to 65W even with a 100W charger connected — upgrading the charger past the laptop's cap buys nothing.
- **Multi-port chargers splitting wattage.** A "100W" GaN charger with your phone also plugged in may only offer the laptop 65W; the label rating is the total, not per-port.
- **Heat throttling.** Charging slows deliberately when the battery gets hot — a protection behavior, not a fault.

## How to fix it

Ranked by impact — start at the top.

### Fix 1: Get the wattage math right

1. Find your laptop's required wattage on the original charger's label or the bottom sticker.
2. Check your USB-C charger's rated output (e.g., 65W, 100W). If it's below the laptop's requirement, that's your bottleneck — upgrade the charger.
3. Buy a charger rated at or above the laptop's needs from a reputable brand. For a 90W laptop, a 100W PD charger is the sweet spot.
4. If it's a multi-port charger, test with only the laptop connected — other devices steal from the shared total. And if you're running a gaming laptop on USB-C, read [why a 65W charger can't feed a gaming laptop](/articles/best-way-to-fix-65w-charger-not-enough-for-gaming-laptop/) before spending anything.

**Prove the charger delivers what its label claims:** Before blaming the laptop, confirm the charger isn't the liar in the chain.

5. Plug the charger into a different PD-capable device (a modern phone or tablet with a USB-C PD trigger) and check that it fast-charges at the expected rate.
6. If it underperforms on every device, the charger is failing or counterfeit — cheap no-name "100W" chargers are a common disappointment. Replace it with a unit from a known brand.
7. Also try a different wall socket directly — not a power strip shared with heavy appliances. Sagging mains voltage can make some chargers drop to a lower output profile.

**Check the laptop's PD input cap:** Sometimes the chain is fine and the laptop is the ceiling.

8. Look up your laptop's spec sheet for its maximum USB-C PD input — many ultrabooks cap at 65W even though they ship with 65W barrel adapters that behave identically.
9. If your laptop caps at 65W, a 100W charger will charge it at 65W. That's not a fault and a bigger charger won't help — spend the money on a better cable instead.
10. This cap is set in firmware and can't be raised. Knowing it stops you chasing a fix that doesn't exist.

### Fix 2: Use a cable rated for the full wattage

1. Check your cable's rating — quality cables print it on the connector housing (look for "100W" or "5A" markings). Unmarked bargain cables are usually 60W or less.
2. Look for "e-marked" on the product listing if buying new — the e-marker chip is what lets the cable advertise 100W+ capability to the charger during negotiation. No chip, no high-wattage handshake.
3. Replace it with an e-marked USB-C cable rated for 100W (240W cables exist now too, and are fine — the laptop only draws what it negotiates).
4. Keep the cable short if possible; very long cables can cause negotiation issues at high wattage.

### Fix 3: Plug into the correct port

1. Check your laptop manual for which USB-C port accepts charging — it's often marked with a small power/plug icon.
2. Move the charger to that port. On some laptops the rear or left-side port is the charging one.
3. Our [USB-C charging not working guide](/articles/how-to-fix-usb-c-charging-not-working-on-laptop/) has more on port quirks if charging doesn't start at all.

### Fix 4: Reduce load while charging

1. If you must charge with a lower-wattage charger, close heavy applications while charging — every watt the CPU/GPU doesn't burn goes to the battery.
2. Lower screen brightness and switch **Power mode** to **Best power efficiency** in **Settings** > **System** > **Power & battery**.
3. For the fastest possible charge, shut the laptop down or close the lid (set lid-close to **Do nothing** or **Sleep** first in **Control Panel** > **Power Options** > **Choose what closing the lid does**).

### Fix 5: Clean the port and reseat the cable

1. Power off, then inspect the USB-C port for lint and debris — clean gently with a wooden toothpick or compressed air.
2. Push the cable in firmly; USB-C connectors should seat fully with no gap.
3. Try flipping the cable — USB-C is reversible, but a worn connector can make better contact one way.

### Fix 6: Watch for the "plugged in, not charging" threshold behavior

Sometimes the charging isn't slow — it's paused, which looks like extreme slowness on the percentage display.

1. Check whether the percentage is truly climbing slowly or completely frozen. Frozen at 80% (or 60%) usually means a manufacturer charge limit is engaged, not a PD problem — check **Lenovo Vantage**, **MyASUS**, or **Dell Power Manager**.
2. Some laptops also pause charging when the battery is very hot or very cold. If the machine just came in from a cold car or a hot room, let it reach room temperature and retest.
3. Distinguishing "slow" from "paused" saves you from replacing a charger that was never the problem.

### Fix 7: Rule out heat throttling

1. If charging starts fast then slows, feel the charger and laptop — excessive heat triggers protective slowdowns.
2. Improve ventilation and move the charger off heat-trapping surfaces.
3. This is normal protection behavior; the fix is cooling, not a new charger.

### Fix 8: Update PD-related firmware

1. Install all Windows updates including optional firmware updates (**Settings** > **Windows Update**).
2. Check your manufacturer's support page for BIOS or Thunderbolt/USB-C firmware updates — PD negotiation bugs do get fixed in firmware. ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/))
3. If a dock or hub sits between charger and laptop, test without it — cheap hubs are notorious PD bottlenecks.

## Closing

Slow USB-C charging is the lowest of three numbers: charger wattage, cable rating, port capability. Match all three to your laptop's needs and the trickle becomes a proper charge. The single most common real-world fix is the cable — people upgrade the charger and keep the 60W cable, then wonder why nothing changed. Check the cable.

If you've matched all three and the speed is still wrong, our [slow USB-C PD troubleshooting guide](/articles/usb-c-pd-charger-charging-slowly-troubleshooting/) walks you through isolating each component. And judge the fix by the 0–80% rate — the last 20% always charges slower.
