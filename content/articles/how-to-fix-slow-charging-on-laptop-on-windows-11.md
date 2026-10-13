---
title: "How to Fix Slow Charging on a Laptop in Windows 11"
slug: how-to-fix-slow-charging-on-laptop-on-windows-11
date: 2026-10-05
categories: ["battery"]
tags: ["slow charging", "windows 11", "usb-c", "charger"]
description: "Laptop charging painfully slowly on Windows 11? Diagnose charger, cable, USB-C port and power settings to restore full speed."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why is my laptop charging so slowly on Windows 11?"
    a: "The usual suspects are an underpowered charger, a low-quality USB-C cable that can't carry full wattage, charging through a hub or dock, a dirty charging port, or Windows power settings throttling charge current. High system load while charging also slows the net charge rate."
  - q: "Does charging through a USB hub slow things down?"
    a: "Yes, very often. Most hubs and docks pass through less power than a direct charger connection, and some don't pass charging power at all. For maximum charge speed, plug the charger directly into the laptop's designated charging port."
  - q: "Can Windows 11 settings make charging slower?"
    a: "Indirectly. Battery saver, thermal throttling from high temperatures, and manufacturer charge-limit features (like 80% caps) all affect charging behavior. Windows itself doesn't have a 'charge speed' slider, but power plans and background load matter."
  - q: "How fast should my laptop charge?"
    a: "It varies by model, but most modern laptops add 40–60% in the first 30–40 minutes with the correct charger, then slow down as they approach full — that taper near 100% is normal lithium battery behavior, not a fault."
---

You plug in your laptop, come back an hour later, and it's crawled from 30% to 41%. That's not normal — with the right charger, most laptops charge dramatically faster than that, and Windows 11 will even tell you "plugged in" the whole time while the percentage barely moves. Slow charging is almost always a power delivery problem rather than a Windows problem, but Windows 11 has a few settings that contribute. Let's find your bottleneck.

The key insight: your laptop charges at the speed of the *weakest link* — charger wattage, cable rating, port capability, and system load all multiply together. Fix the weakest link and speed usually jumps immediately.

## Why this happens

- **Underpowered charger:** A 45W brick on a laptop designed for 65W or 90W charges slowly or barely holds the charge level under load.
- **Weak USB-C cable:** Many USB-C cables only handle 60W or less, and cheap ones far less. The cable silently caps your charge speed.
- **Charging through a hub or dock:** Docks and hubs commonly deliver reduced wattage to the laptop, sometimes as little as 15–30W.
- **Wrong port:** Some laptops have multiple USB-C ports but only one supports full-speed charging; the others charge slowly or not at all.
- **Heavy load while charging:** Gaming or rendering while plugged in can consume nearly all incoming power, leaving little for the battery.
- **Heat throttling:** Hot batteries charge slower by design — the charging circuit reduces current to protect the cells.
- **Worn battery:** Old batteries with high internal resistance accept charge more slowly, especially in the final stretch.

## How to fix it

Work through these in order — start with the hardware chain, then check software.

### Fix 1: Use the original charger at full wattage

Check the wattage printed on your original charger brick and make sure you're actually using it — not a phone charger or an older, weaker brick from another device. Phone chargers (18–30W) will "charge" a laptop at a crawl. If you've lost the original, buy a replacement matching the laptop's required wattage exactly, from the manufacturer or a reputable brand. While you're at it, confirm the charger is plugged into a wall outlet, not a power strip shared with heavy appliances, which can cause voltage sag.

### Fix 2: Upgrade the USB-C cable

If you charge over USB-C, the cable matters as much as the brick. Look for a cable explicitly rated for the wattage you need — "100W USB-C PD" cables are widely available and inexpensive. Avoid unmarked or ultra-thin cables; they often top out at 15–60W regardless of what the brick can deliver. A cable with an e-marker chip (any decent 100W-rated cable has one) lets the laptop and charger negotiate full speed. Swap the cable and watch the charge rate for 10 minutes — this alone fixes a huge share of slow-charging complaints.

### Fix 3: Plug directly into the laptop's charging port

Bypass any hub, dock, or monitor USB-C connection and plug the charger straight into the laptop. If your laptop has several USB-C ports, check the manual for which one is the designated charging port — it's often marked with a plug or lightning icon. Some ports are data-only or limited to 15W input. After switching ports, give it 5–10 minutes and compare the percentage gain. For broader charging issues, our guide on [laptop plugged in but not charging](/articles/how-to-fix-laptop-plugged-in-not-charging-reddit/) covers the no-charge case.

### Fix 4: Reduce load and heat while charging

Close demanding apps while you need a fast charge — games, video renders, and heavy browser tab counts all eat into charging current. Check **Task Manager (Ctrl + Shift + Esc) → Processes** sorted by CPU and end anything unnecessary. Make sure the vents aren't blocked and the laptop isn't sitting on a bed or couch; if the chassis is hot to the touch, the battery management system is deliberately slowing the charge. Let it cool on a hard surface and charging will speed back up.

### Fix 5: Check manufacturer charge settings

Open your manufacturer's battery app — Lenovo Vantage/Commercial Vantage, Dell Power Manager, HP BIOS settings, MyASUS, or similar — and look for charge thresholds or "battery lifespan" modes. Some modes intentionally slow charging or cap it at 80%. Switch to a **Standard** or **Full charge** mode while you test. Also turn off **Battery saver** in **Settings → System → Power & battery** during the test, since it can alter power behavior on some systems.

### Fix 6: Update BIOS and charging drivers

Visit your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and install the latest BIOS and any power management driver updates for your model. BIOS updates frequently include charging algorithm improvements. In **Device Manager → Batteries**, you can also uninstall the **Microsoft ACPI-Compliant Control Method Battery** driver and restart to force a clean reinstall, which clears corrupted charge negotiation states.

### Fix 7: Test the battery's health

If hardware and settings are all correct and charging is still slow, the battery itself may be worn. Open an admin Command Prompt and run:

```cmd
powercfg /batteryreport /output "C:\battery-report.html"
```

Compare **Design Capacity** with **Full Charge Capacity**. If the battery holds less than 70% of its original capacity, its increased internal resistance slows charging noticeably — replacement is the real fix. Our guide on [checking battery health in Windows 11](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains how to interpret the report in detail.

## Closing

Slow charging is a weakest-link problem, and the link is usually the cable or the charger — not Windows. Get the right wattage brick, a properly rated USB-C cable, and a direct connection to the correct port, and most laptops snap back to full charging speed immediately. If they don't, the battery report will tell you honestly whether the battery itself has aged out. Either way, you now know exactly where the bottleneck is instead of guessing.
