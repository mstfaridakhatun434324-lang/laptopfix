---
title: "USB-C PD Charger Charging Slowly? Here’s What to Do"
slug: what-to-do-if-usb-c-pd-charger-charging-slowly
date: 2026-09-24
categories: ["battery"]
tags: ["usb-c pd slow charging", "usb-c charger slow", "power delivery charging"]
description: "USB-C charger trickling instead of charging? Fix slow USB-C PD charging with wattage checks, cable swaps, and port settings."
thumbnail: "/images/thumbs/what-to-do-if-usb-c-pd-charger-charging-slowly.webp"
faqs:
  - q: "Why is my USB-C charger charging so slowly?"
    a: "Almost always a wattage mismatch: the charger, cable, or port negotiates a lower Power Delivery profile than the laptop wants. A 45W charger on a 90W laptop, a charge-only-limited cable, or the wrong USB-C port are the usual culprits."
  - q: "Do USB-C cables affect charging speed?"
    a: "Hugely. Basic USB-C cables are limited to 60W; 100W+ charging needs an e-marked cable with a chip identifying its capability. A cheap cable silently caps your 100W charger at 60W, and there's no visible difference between the cables."
  - q: "Can I use a phone charger on my laptop?"
    a: "In a pinch, yes — if the laptop supports USB-C PD charging, a phone charger will usually trickle-charge it while idle or off. But 18–25W won't keep up with active use; the battery may still drain, just slower. It's a survival tool, not a solution."
  - q: "Why does my laptop charge slowly even with the original charger?"
    a: "Check the cable for damage, try a different USB-C port (only some support PD input), and look for a BIOS 'USB-C charging' throttle setting. Also, heavy use while charging consumes most of the input — the net charge rate is input minus usage."
---
USB-C was supposed to end charger confusion — one port, one cable, everything just works. Instead, your laptop trickle-charges at a crawl while the same charger fast-charges your phone. The frustration is real, but so is the explanation: USB-C Power Delivery is a negotiation between charger, cable, and laptop, and any weak link throttles the whole chain to the lowest common denominator.

Here's how to find the weak link.

## Why this happens

- **Under-wattage charger:** A 45–65W charger on a laptop that expects 90W+ negotiates a low PD profile and charges slowly — or not at all under load.
- **Non-e-marked cable:** Standard cables cap at 60W; without the e-marker chip, the charger and laptop won't agree to higher profiles.
- **Wrong USB-C port:** Many laptops have multiple USB-C ports but only one wired for PD charging input.
- **Heavy use while charging:** If the laptop draws 50W running and the charger delivers 65W, only 15W reaches the battery.
- **BIOS charging throttles:** Some laptops limit USB-C charging current in firmware, especially on battery-conservation settings.

## How to fix it

Work through these in order — the chain is only as fast as its slowest link.

### Fix 1: Check the actual negotiated wattage

Stop guessing and measure what the laptop is receiving.

1. In Windows, check **Settings** > **System** > **Power & battery** — some laptops show "slow charger" warnings here.
2. Better: use your manufacturer's utility or the BIOS, which often shows input wattage.
3. Compare against your laptop's expected wattage (manual or support page).
4. A big gap between charger rating and negotiated input means the cable or port is the limiter — continue below.

Some USB-C power meters (inline dongles) show live wattage directly — a $15 tool that ends all speculation if you troubleshoot chargers often.

### Fix 2: Match the charger wattage to the laptop

The single most common cause, stated plainly.

1. Find your laptop's required wattage: check the original barrel charger's label or the manual.
2. Read your USB-C charger's output — the fine print lists PD profiles like 20V/4.5A (90W).
3. If the charger is smaller than the requirement, that's the throttle. Buy a PD charger meeting or exceeding the laptop's wattage.
4. For docks and hubs: many reserve wattage for themselves — a "90W" dock may deliver only 65W to the laptop. Gaming laptops are especially sensitive here — see our guide to [fixing a 65W charger not being enough for a gaming laptop](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/).

Bigger is safe: the laptop only draws what it negotiates. Smaller is the problem. When buying, look for GaN chargers from reputable brands — they're compact and run cooler. For the adapter-detection side of this, see our [charger not detected guide](/articles/how-to-fix-laptop-charger-not-detected-youtube/).

### Fix 3: Upgrade to an e-marked 100W cable

The invisible throttle most people never suspect.

1. Check your cable: e-marked cables are often labeled 100W or 5A; unmarked cheap cables are usually 60W/3A max.
2. Replace any suspect cable with a certified USB-C cable rated 100W (or 240W for the newest PD 3.1 setups).
3. Keep the cable short — long cables add resistance and can reduce negotiated rates.
4. Retest: the same charger with a proper cable often jumps a full PD tier.

This is the cheapest fix on this list and resolves a large fraction of "slow USB-C charging" complaints. The cable is the component everyone overlooks because it looks identical either way.

### Fix 4: Use the correct USB-C port

Not all ports are created equal.

1. Check your manual for which USB-C port supports charging input — it's often marked with a plug or battery icon.
2. Move the charger to that port.
3. On some laptops, the charging port changes based on BIOS settings — check for USB-C/Thunderbolt power options in BIOS.
4. Avoid charging through a hub's pass-through unless you've verified its delivered wattage (Fix 1).

Thunderbolt ports usually support PD input, but plain data-only USB-C ports on some models don't. The manual's port diagram is authoritative here.

### Fix 5: Reduce load while charging

Net charge rate is input minus consumption.

1. While charging, check **Task Manager** for CPU hogs — heavy compilation, gaming, or video rendering can consume most of a modest charger's output.
2. Lower screen brightness and close unnecessary apps during charging sessions.
3. For the fastest charge, put the laptop to sleep while plugged in — nearly all input goes to the battery.
4. If the battery percentage drops while "charging" under load, the charger is simply too small (back to Fix 2).

This isn't a fix for the charger — it's physics. But recognizing it stops you from blaming hardware for what's actually a workload mismatch.

### Fix 6: Check BIOS USB-C charging settings

Firmware can throttle PD input deliberately.

1. Enter BIOS and look under **Power** or **Advanced** for USB-C charging options.
2. Some laptops offer **USB-C charging current** limits or tie PD input to battery conservation modes.
3. Disable any throttling, or set conservation features to allow full-rate charging.
4. Save and retest with your wattmeter or the OS battery screen.

Lenovo and Dell business laptops are the most likely to have these settings. Business-focused firmware sometimes defaults to conservative charging on unknown adapters.

### Fix 7: Update firmware and drivers

PD negotiation involves firmware on both ends.

1. Update the laptop BIOS — PD controller firmware ships inside BIOS updates.
2. Update the chipset and Thunderbolt drivers from your manufacturer's support page ([Intel's assistant](https://www.intel.com/content/www/us/en/support/detect.html) helps identify the hardware).
3. If your charger or dock has updatable firmware (many Thunderbolt docks do), update that too.
4. Retest negotiation after each update.

PD is a protocol, and protocol bugs get fixed in firmware. If slow charging appeared after an update, this fix works in reverse too — check for newer firmware that addresses the regression.

## Closing

Slow USB-C charging is a weakest-link problem: charger wattage, cable e-marking, correct port, and reasonable load all have to line up. Check them in order and the throttle reveals itself — usually an under-wattage charger or a 60W cable silently capping a 100W setup. Get the chain right and USB-C genuinely delivers on its one-cable promise; get one link wrong and you're trickle-charging for hours wondering why.
