---
title: "Slow Laptop Charging: Step-by-Step Fixes That Work"
slug: how-to-fix-slow-charging-on-laptop-youtube
date: 2026-09-26
categories: ["battery"]
tags: ["slow charging", "charger", "usb-c", "troubleshooting"]
description: "Laptop taking forever to charge? Diagnose whether it's the charger, cable, port, or settings — and fix slow charging step by step."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-youtube.webp"
faqs:
  - q: "Why is my laptop charging so slowly?"
    a: "The usual suspects are an underpowered charger, a worn or low-quality cable, charging through a hub or dock instead of directly, a dirty USB-C port, heavy power draw while charging, or battery-health features that deliberately slow the charge near full. Checking the charger's wattage against your laptop's requirement is the fastest first step."
  - q: "Does using my laptop while charging make it slower?"
    a: "Yes, noticeably. Gaming, video editing, or even a heavy browser session can consume most of the charger's output, leaving little for the battery. For the fastest charge, close heavy apps, dim the screen, or shut the laptop down while it charges."
  - q: "Can a phone charger charge a laptop?"
    a: "Sometimes, but slowly — or not at all. A 65W laptop needs a charger that can deliver 65W over USB-C Power Delivery. A 20W phone charger may show 'plugged in' without meaningfully charging, and Windows may warn that the charger is underpowered."
  - q: "Is slow charging bad for the battery?"
    a: "No — slower charging is actually gentler on lithium batteries and generates less heat. Slow charging is only a problem when it's caused by a faulty charger or port, or when it's so slow you can't get through your day."
---
You plug in, see the charging icon, and come back an hour later to find the battery has crawled from 40% to 48%. Or worse — the percentage barely moves at all while you're working. Slow charging is one of those problems with a dozen possible causes, but the diagnosis is straightforward once you check things in the right order.

Most slow-charging cases come down to power delivery: the charger, cable, or port isn't delivering what the laptop expects. Settings and software are the next most common culprits. Work through the steps below and you'll find the bottleneck.

## Why this happens

- **The charger is underpowered.** A 45W adapter on a laptop that wants 65W (or a 65W adapter on a 100W gaming machine) charges slowly — or just barely holds the charge steady.
- **The cable can't carry enough power.** Cheap or damaged USB-C cables may only support low wattages even with a good charger; some are data-only or charge-only at 15W.
- **You're charging through a hub or dock.** Hubs, docks, and monitor USB-C ports often pass through less power than a direct wall connection.
- **The USB-C port is dirty or loose.** Lint and debris in the port prevent full contact, throttling power delivery.
- **Heavy usage while charging.** If the laptop is consuming nearly as much as the charger provides, the battery charges at a trickle.
- **Battery-health features are slowing it down.** Charge limiters (80% caps), adaptive charging, and battery saver modes intentionally slow charging near the top.
- **The battery is old and degraded.** Worn cells accept charge less efficiently, and the system may throttle current to protect them.

## How to fix it

Work through these in order — start with the hardware, then move to software.

### Fix 1: Verify your charger's wattage

An underpowered charger is the single most common cause.

1. Check the fine print on your charger brick for its output wattage (e.g., **65W**), and check your laptop's manual or the original charger for the required wattage.
2. If you're using a replacement or third-party charger, make sure it meets or exceeds the laptop's requirement — see our guide on [underpowered chargers for gaming laptops](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/) for what happens when the wattage falls short.
3. Replace an undersized charger with a properly rated one from a reputable brand.

### Fix 2: Plug directly into the wall

Remove every middleman between the outlet and your laptop.

1. Unplug from any **hub, dock, power strip, or monitor** and connect the charger directly to a **wall outlet**.
2. If your laptop has multiple USB-C ports, use the one marked with a **charging or power-delivery icon** — on many laptops only one port supports full-wattage charging.
3. Time the charge for 15 minutes and compare the percentage gain.

### Fix 3: Inspect and swap the cable

Cables fail more often than chargers do.

1. Try a different **USB-C cable** rated for your charger's wattage (look for **100W / 5A** markings for 65W+ setups).
2. Check both ends for bent pins, fraying, or discoloration.
3. For barrel-plug chargers, wiggle the connector gently at the laptop — if charging cuts in and out, the cable or jack is damaged and needs replacement.

If Windows doesn't acknowledge the charger at all, work through our [charger not detected](/articles/what-to-do-if-laptop-charger-not-detected/) checklist instead.

### Fix 4: Clean the charging port

A surprising amount of slow charging is just pocket lint.

1. Power the laptop **off** and unplug everything.
2. Shine a light into the USB-C port and look for lint or debris.
3. Gently remove debris with a **wooden or plastic toothpick** — never metal — and blow out dust with short bursts of compressed air.
4. Reconnect and check whether the charge rate improves.

### Fix 5: Reduce load while charging

Your laptop charges fastest when it's not also working hard.

1. Close games, video editors, and heavy browser sessions while charging.
2. Go to **Settings > System > Power & battery** and set **Power mode** to **Best power efficiency**.
3. Lower brightness to **50%** or below.
4. For the absolute fastest charge, **shut the laptop down** and let it charge undisturbed for 30–60 minutes.

### Fix 6: Check battery-health and charge-limit settings

Features designed to protect your battery can look like a charging problem.

1. Open your manufacturer's utility (**Lenovo Vantage**, **Dell Power Manager**, **HP BIOS**, **MyASUS**) and check for charge caps like **80% limit** or **adaptive charging** — these slow charging deliberately near the cap.
2. If you need a fast full charge today, temporarily disable the cap, then re-enable it afterward.
3. Note that charging naturally slows above **80%** on all lithium batteries — that's chemistry, not a fault.

### Fix 7: Update BIOS, chipset, and battery drivers

Firmware controls the charging handshake, especially over USB-C Power Delivery.

1. Install the latest **BIOS** and **chipset drivers** from your maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. In **Device Manager > Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery**, restart, and let Windows reinstall it.
3. Retest the charge rate with the original charger and cable.

## Closing

Slow charging is a process of elimination: right wattage, right cable, direct wall connection, clean port, light workload — in that order. Nine times out of ten, the fix is one of those five, and it's usually the charger or cable rather than the laptop itself. Remember that the last 20% of any charge is deliberately slow on every modern laptop, so judge your charge speed by the 20–80% range. If charging has become slow across the board and the battery is several years old, check the [battery wear level](/articles/how-to-check-battery-wear-level-on-laptop/) — worn cells simply can't accept current like they used to. And if you regularly charge in a hot room or while the laptop is working hard, remember that heat throttles charging speed by design; moving to a cooler spot or letting the machine idle while it charges can make a bigger difference than any setting. Measure your charge rate in the 20–80% window over a week of normal use, and you'll know whether you've actually fixed it or just had a good day.
