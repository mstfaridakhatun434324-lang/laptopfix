---
title: "Speed Up a Slow USB-C PD Charger"
slug: how-do-i-fix-usb-c-pd-charger-charging-slowly
date: 2026-09-27
categories: ["battery"]
tags: ["usb-c pd", "slow charging", "charger", "troubleshooting"]
description: "USB-C charger trickling instead of charging? Check PD negotiation, cable ratings, port choice, and power settings to restore full-speed charging."
thumbnail: "/images/thumbs/how-do-i-fix-usb-c-pd-charger-charging-slowly.webp"
faqs:
  - q: "Why is my USB-C charger charging so slowly?"
    a: "The usual causes: the charger wattage is below what the laptop wants, the cable isn't rated for the wattage (many USB-C cables cap at 60W), you're using a low-power port on a multi-port charger, or the laptop negotiated a low PD profile. Each link — brick, cable, port — can bottleneck the others."
  - q: "Does the cable matter for USB-C charging speed?"
    a: "Enormously. A cable must carry an e-marker chip to support over 60W (3A). Cheap or old USB-C cables often top out at 60W even with a 100W brick. For 100W charging you need a cable explicitly rated 100W/5A with an e-marker."
  - q: "How do I know what wattage my laptop is actually getting?"
    a: "Windows shows 'slow charger' warnings on some models when the wattage is inadequate. Your manufacturer's app (or BIOS) sometimes shows adapter wattage. USB power meters — small dongles that sit between charger and laptop — show exact volts, amps, and watts for around $15-20."
  - q: "Can I use a phone charger for my laptop?"
    a: "In a pinch, yes — USB-C PD is designed to negotiate down safely. But a 25-45W phone charger will charge a laptop very slowly, may not keep up during use, and some laptops refuse it entirely. It's an emergency top-up, not a daily driver."
---
USB-C PD charging is wonderful when it works — one brick for laptop, phone, and tablet — and baffling when it trickles. The laptop says it's charging, but the percentage crawls. The frustration is that every component looks fine individually: the brick is 100W, the cable is USB-C, the port is USB-C. But charging speed is set by the weakest link in the chain, and finding it takes a method.

The chain is: wall → brick → cable → port → laptop negotiation → Windows settings. Test each link in order.

## Why this happens

- **The brick's wattage is too low:** A 45W or 65W charger on a laptop that wants 90W+ charges slowly by design — and may not keep up at all during use.
- **The cable bottlenecks the power:** Cables without an e-marker chip cap at 60W. Your 100W brick plus a 60W cable equals 60W charging.
- **Wrong port on a multi-port charger:** Multi-port GaN chargers split wattage. The laptop port might deliver only 45W when a second device is plugged in — check the port power table.
- **PD negotiation picked a low profile:** The charger and laptop negotiate voltage/current. Glitches, dirty contacts, or incompatible PD versions can land on a low profile (e.g., 15W) instead of the full one.
- **The laptop's USB-C port has a lower cap:** Many laptops cap USB-C input at 65W or 100W even if the brick offers more. The barrel charger remains the full-speed option.
- **Windows power settings throttle charging:** Aggressive battery saver settings and some manufacturer "battery care" modes slow charging deliberately.
- **Heat throttling:** Charging slows automatically when the battery is hot. A laptop charging in a warm room or under load charges slower than a cool idle one.

## How to fix it

Work through these in order — the chain method.

### Fix 1: Verify what the laptop actually needs

You can't diagnose "slow" without knowing "normal."

1. **Check the original charger's wattage:** It's printed on the brick that came with the laptop. That's your target.
2. **Check your USB-C brick's rating:** Read the fine print — the PD output table (e.g., 20V/5A = 100W). Note the maximum single-port output.
3. **Compare:** If the laptop wants 130W and your brick maxes at 65W, slow charging is expected physics, not a fault. Accept it for overnight use, or get a bigger brick.
4. **Check the laptop's USB-C input cap:** The specs or manual state the max USB-C charging wattage. A laptop capped at 65W won't charge faster with a 140W brick — but it should still hit its 65W cap.

Write down the three numbers: laptop wants X, brick offers Y, port accepts Z. Charging speed = the smallest of the three. For the related diagnosis, see [troubleshoot a 65W charger on a gaming laptop](/articles/65w-charger-not-enough-for-gaming-laptop-troubleshooting/).

### Fix 2: Test the cable — the most common bottleneck

Cables are the weakest link more often than bricks.

1. **Check the cable's rating:** Look for printed "5A" or "100W" on the cable. No marking usually means a basic 60W cable.
2. **Swap in a known-good 100W cable:** One explicitly rated 100W/5A with an e-marker chip. This single swap fixes a huge share of slow-charging complaints.
3. **Try a shorter cable:** Long cables (2m+) have more resistance and negotiate down more often. Test with a 1m cable.
4. **Inspect the connectors:** Lint in the USB-C plug is a real charging killer. Clean with a wooden toothpick and compressed air — never metal.
5. **Rule:** If the cable came free with a phone, assume 60W max until proven otherwise.

Buy one quality 100W-rated cable and keep it as your reference — it eliminates the cable variable from all future troubleshooting.

### Fix 3: Use the right port on charger and laptop

Multi-port chargers and multi-port laptops both have "right" and "wrong" choices.

1. **On the charger:** Read the port power table (printed on the brick). Plug the laptop into the highest-wattage port — usually C1. Unplug other devices for the test; many chargers drop the laptop port's output when a second port is used.
2. **On the laptop:** Try each USB-C port. Not every port is full-speed charging — one may be data-only or lower-wattage. The charging port is often marked with a plug icon.
3. **Unplug everything else from the charger** during testing to give the laptop the full output.
4. **Check the wall side too:** A loose wall plug or flaky power strip can starve even a good brick.

### Fix 4: Force a clean PD renegotiation

Sometimes the charger and laptop just agree badly. Make them renegotiate.

1. **Unplug the cable from the laptop** (not just the wall).
2. **Wait 30 seconds** — this lets both sides fully reset their PD state.
3. **Plug the cable into the laptop first**, then into the charger, then the charger into the wall. Order matters for some PD controllers.
4. **Watch the first 60 seconds:** Charging often starts slow and ramps up as negotiation completes. Judge speed after 2–3 minutes, not 20 seconds.
5. **Try the laptop powered off:** If it charges fast while off but slow while on, the issue is load or settings (Fixes 5–6), not negotiation.

### Fix 5: Reduce the load competing with charging

Charging speed is net power: what the brick delivers minus what the laptop burns.

1. **Check what's running:** Open Task Manager and look for high CPU/disk usage. A laptop burning 45W while the charger delivers 65W nets only 20W to the battery — that's your "slow."
2. **Close heavy apps** during charging, or at least pause renders, compiles, and games.
3. **Dim the display:** The screen is a major constant drain. Lower brightness while charging on a weak brick.
4. **Let it charge while asleep:** **Start > Power > Sleep**, leave it plugged in. With near-zero load, all brick power goes to the battery.
5. **Do the math:** If the battery gains ~15% per hour while idle but ~5% while working, the charger is fine — the workload is the bottleneck.

This is the most overlooked cause: the charger isn't slow, the laptop is just hungry. Our guide on [turning off background apps](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) helps trim the load.

### Fix 6: Check Windows and manufacturer charging settings

Software can deliberately slow charging.

1. **Power mode:** **Settings > System > Power & battery > Power mode** — extreme efficiency modes can reduce charge current on some models.
2. **Manufacturer battery care:** Check Lenovo Vantage, MyASUS, Dell Power Manager, or Acer Care Center for charging-speed or battery-care options that limit current.
3. **BIOS settings:** Some BIOS setups have battery charging behavior options (Standard vs. Express). Express charges faster but generates more heat.
4. **Windows Update:** Install pending updates — PD and power management drivers do get fixes.

Microsoft's power documentation at [support.microsoft.com](https://support.microsoft.com/en-us/windows) covers the OS-side settings.

### Fix 7: Measure with a USB power meter and decide

Stop guessing — measure the actual watts.

1. **Get a USB-C power meter** (a small inline dongle, ~$15–20). Plug it between charger and laptop.
2. **Read volts × amps:** 20V × 3.25A = 65W, for example. Compare to the brick's rating and the laptop's cap.
3. **Interpret:** Meter shows full brick output but slow percentage gain = battery wear or heavy load. Meter shows low output = brick, cable, or negotiation problem (you've already tested each).
4. **Decide:** If the chain maxes below the laptop's needs and you need faster charging, buy a higher-wattage GaN brick from a reputable brand — matching the laptop's original wattage, with a rated 100W cable.

The meter pays for itself the first time it stops you buying a new brick when the cable was the problem.

## Closing

Slow USB-C PD charging is a weakest-link problem, and the link is usually the cable — an unmarked 60W cable silently throttling a 100W brick is the classic. Work the chain methodically: confirm the three wattage numbers, swap in a rated 100W cable, use the right ports, force a clean renegotiation, and account for the laptop's own power hunger. Most slow-charging mysteries end with a $15 cable, not an $80 brick.
