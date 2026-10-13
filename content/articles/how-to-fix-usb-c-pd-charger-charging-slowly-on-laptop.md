---
title: "Why Your USB-C PD Charger Charges Slowly (and How to Fix It)"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-on-laptop
date: 2026-09-28
categories: ["battery"]
tags: ["usb-c", "pd charger", "slow charging"]
description: "USB-C charger crawling at a snail's pace? Check PD wattage negotiation, cable limits, and port choice — most slow USB-C charging is fixable in minutes."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-on-laptop.webp"
faqs:
  - q: "Why is my USB-C charger so slow on my laptop?"
    a: "Usually the charger and laptop negotiated a lower wattage than you expected — a 65W brick on a laptop that wants 90W, a cable limited to 60W, or the wrong USB-C port. USB-C charging only runs at full speed when charger, cable, and port all support the same PD profile."
  - q: "Does the USB-C cable affect charging speed?"
    a: "Absolutely. Many USB-C cables only carry 60W (3A); you need a 100W-rated (5A) cable with an e-marker chip for higher wattages. A cheap cable silently caps a 100W charger at 60W, and a charge-only cable may not negotiate PD at all."
  - q: "Can I use any USB-C port for charging?"
    a: "No. On many laptops only one specific USB-C port supports Power Delivery input — the others are data-only. Check the port icons: a battery or plug symbol marks the charging-capable port. Plugging into the wrong one gives you trickle charging or nothing."
  - q: "Is slow USB-C charging bad for the battery?"
    a: "No — slower charging is actually gentler on battery chemistry. The problem is practical: if the charger can't keep up with the laptop's power draw, the battery drains even while plugged in, or never reaches full."
---
You plugged in a USB-C charger expecting fast top-ups, but the battery percentage barely moves — or worse, it keeps dropping while you work. USB-C was supposed to simplify charging, but the mix of wattages, cables, and ports makes "it fits, so it charges" dangerously optimistic.

Slow USB-C charging is almost always a negotiation problem: somewhere between the wall and the battery, the chain agreed on less power than the laptop needs. Here's how to find the weak link and fix it.

## Why this happens

- **The charger wattage is too low.** A 45W or 65W PD brick on a laptop designed for 90W+ charges slowly and may not keep up under load.
- **The cable caps the power.** Standard USB-C cables top out at 60W; without a 5A e-marked cable, a 100W charger is throttled to 60W.
- **You used the wrong port.** Many laptops have one PD-capable port and several data-only ones — the wrong port gives trickle charge.
- **The laptop negotiated a low PD profile.** PD chargers offer stepped voltages (5V, 9V, 15V, 20V); if the handshake fails, the laptop may fall back to a slow 5V mode.
- **A dock or hub sits in the middle.** Hubs consume 10–15W themselves and some only pass through reduced wattage.
- **Battery protection limits the rate.** A hot battery, a nearly-full battery, or a worn battery all charge slower by design.

## How to fix it

Work through these in order — check the chain from wall to laptop, weakest link first.

### Fix 1: Match the charger to the laptop's requirement

1. Find the wattage your laptop actually needs — it's printed on the original barrel charger, near the charging port, or in the manual.
2. Read the fine print on your USB-C brick: it must support USB **PD** (Power Delivery), not just QC or proprietary fast charge, and its 20V output wattage should meet or exceed the laptop's requirement.
3. Phone chargers (18–30W) will technically charge most USB-C laptops but at a crawl — fine for overnight, useless for working.
4. If your laptop needs more than your brick offers, the [65W charger gaming laptop problem](/articles/how-do-i-fix-65w-charger-not-enough-for-gaming-laptop/) explains exactly what happens with underpowered adapters.

### Fix 2: Upgrade to a proper 100W PD cable

1. Check your cable for a wattage rating — quality cables print "100W" or "5A" on the connector housing.
2. If there's no marking, assume it's a 60W cable and replace it with a certified USB-IF 100W (or 240W for newer EPR laptops) cable.
3. Keep the cable short: 1m negotiates more reliably than 2m+ bargain cables.
4. Retest: a cable swap alone fixes a huge share of "slow USB-C charging" complaints.

### Fix 3: Use the correct USB-C port

1. Look closely at the ports — the charging-capable one usually has a small battery, plug, or lightning-bolt icon beside it (on Thunderbolt laptops, any Thunderbolt port typically accepts charge).
2. Move the charger to that port and watch the battery icon for a few minutes.
3. Check your manual: some laptops only charge from the left-side port, or disable charging on a port when a dock is connected elsewhere.
4. Blow out the port with compressed air — lint in the connector causes partial connections that negotiate low power.

### Fix 4: Remove hubs and docks from the chain

1. Plug the charger directly into the laptop, bypassing any hub or dock.
2. If speed returns, the hub was eating wattage — check its specs for pass-through charging limits (many cap at 60W even with a 100W brick).
3. For dock users, use the dock's own supplied power adapter rather than daisy-chaining your PD brick through it.

### Fix 5: Check what Windows thinks is happening

1. Go to **Settings** > **System** > **Power & battery** and read the charging status text — Windows 11 sometimes reports "plugged in, charging slowly" explicitly.
2. Open **Terminal (Admin)** and run `powercfg /batteryreport`, then check the recent history for the charge rate in mW — compare direct-plug vs. hub numbers.
3. If the rate is low even with the right brick, cable, and port, continue to Fix 6.

### Fix 6: Update BIOS and PD controller firmware

1. USB-C PD negotiation is handled partly in firmware — check your manufacturer's support page for BIOS updates mentioning USB-C, PD, or Thunderbolt: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Some manufacturers ship separate Thunderbolt/USB-C firmware updaters — install those too.
3. Flash with the charger connected and don't interrupt the process.

### Fix 7: Rule out battery-side throttling

1. Slow charging above 80% is normal — lithium charging tapers near full by design.
2. If the laptop is very hot, charging slows to protect the cells; let it cool and retest.
3. Check real battery health with `powercfg /batteryreport` — a badly worn battery charges slowly because the controller limits current to failing cells. The [battery wear guide for Windows 11](/articles/how-to-fix-battery-wear-level-too-high-on-windows-11/) covers reading those numbers.

### Fix 8: Test with a wattage meter to see the real number

1. If you have (or can borrow) a USB-C power meter dongle, put it between charger and laptop — it shows the actual negotiated wattage.
2. Compare against the brick's rating: if the meter shows 60W on a 100W brick, the cable is the limiter; if it shows 20W on a 65W brick, the PD handshake failed.
3. No meter? Use the battery report's charge rate in mW as a rough proxy — direct-plug vs. hub vs. different cable, and the numbers tell the story.
4. Once you know the real negotiated wattage, the fix is obvious: replace whichever link negotiated it down.

## Closing

USB-C charging is a chain — brick, cable, port — and it only runs as fast as the weakest link. Match the wattage, use a rated cable in the right port, and most "slow charging" mysteries resolve in one swap.
