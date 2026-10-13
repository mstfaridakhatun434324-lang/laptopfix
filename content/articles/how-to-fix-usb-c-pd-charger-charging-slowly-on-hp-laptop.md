---
title: "USB-C PD Charger Charging Slowly on HP Laptop: How to Fix"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-on-hp-laptop
date: 2026-09-30
categories: ["battery"]
tags: ["usb-c", "pd charger", "hp", "slow charging"]
description: "USB-C PD charger charging slowly on your HP laptop? Learn the wattage, cable, and port issues that throttle charging and how to fix each one."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop charge slowly over USB-C?"
    a: "The most common reasons are an underpowered charger, a cable that cannot carry enough wattage, or charging through a data-only USB-C port instead of the charging port. HP laptops also throttle charging when the adapter wattage is below what the BIOS expects."
  - q: "What wattage USB-C charger does my HP laptop need?"
    a: "Most HP ultrabooks need 45W to 65W, while larger models and workstations need 90W or more. Check the original barrel charger's label for the wattage, then match or exceed it with the USB-C PD charger."
  - q: "Can any USB-C cable handle fast charging?"
    a: "No. Many USB-C cables are rated for only 60W, and cheap ones may carry far less. For 100W charging you need a cable explicitly rated 100W (5A) with an e-marker chip. The cable is the bottleneck more often than people think."
  - q: "Does it matter which USB-C port I use?"
    a: "Yes. On many HP models only one USB-C port supports Power Delivery input, sometimes marked with a plug or battery icon. The other ports are data-only and will charge very slowly or not at all."
---

You plug your shiny USB-C PD charger into your HP laptop expecting fast charging, and instead the battery percentage crawls. Worse, it might even say "plugged in" while the percentage slowly drops during heavy use. The charger works fine on your phone, so what gives?

USB-C charging is a negotiation between the charger, the cable, the port, and the laptop — and HP laptops are strict negotiators. If any link in that chain is weak, the laptop quietly drops to a trickle charge. Here is how to find the weak link, starting with the checks that take under a minute.

## Why this happens

- **Underpowered charger:** A 30W phone charger cannot feed a laptop that wants 65W. The laptop accepts what it can get and charges slowly.
- **Low-rated cable:** A cable rated for 60W (or a cheap unrated cable) caps the negotiation even if the charger can deliver 100W.
- **Wrong USB-C port:** Many HP laptops have one charging-capable USB-C port and one data-only port. Plug into the wrong one and you get a trickle.
- **HP Battery Health Manager throttling:** The "Maximize my battery health" mode can slow charging deliberately, especially past certain percentages.
- **Dirty or worn port:** Lint and oxidation in the USB-C port cause poor contact, and the laptop drops to a safe low current.
- **Outdated BIOS/EC firmware:** Older firmware may not negotiate PD profiles correctly with third-party chargers.
- **Background power draw:** If the laptop is consuming nearly as much as the charger delivers, the net charge rate approaches zero.
- **USB-C charging disabled in BIOS:** Some HP BIOS versions have a USB-C charging toggle under **Advanced → Port Options**. If it got switched off during an update, PD charging falls back to a trickle.

## How to fix it

Work through these in order, testing charge speed after each change.

### Fix 1: Match the charger's wattage to the laptop's needs

1. Find your original HP barrel charger's label and note its wattage (common: 45W, 65W, 90W).
2. Check your USB-C PD charger's label. It must meet or exceed that number.
3. If you are using a 30W or 45W phone charger on a 65W laptop, that is the entire problem. Get a PD charger rated for your laptop's wattage or higher. A 100W PD charger is a safe universal pick for most HP ultrabooks.

### Fix 2: Use a proper 100W-rated USB-C cable

1. Look at your cable's packaging or listing. You need one explicitly rated **100W / 5A** with an **e-marker chip**.
2. Shorter is better: a 1m quality cable beats a 2m cheap one for stable PD negotiation.
3. Swap in the known-good cable and watch the charge rate for 10 minutes. Cables fail gradually, so even a cable that used to work can become the bottleneck. This is also the first thing to check in any [USB-C charging problem](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).

### Fix 3: Plug into the correct USB-C port

1. Check your HP model's manual or the icons beside the ports. The charging port often has a small plug or lightning icon.
2. On many HP EliteBook and ProBook models, only the rear USB-C port supports PD input.
3. Try each USB-C port and note which one charges fastest. Mark it mentally and always use that one.

### Fix 4: Check HP Battery Health Manager

1. Reboot, press **Esc**, then **F10** for BIOS Setup.
2. Go to **Advanced → Power Management Options → Battery Health Manager**.
3. If it is set to **Maximize my battery health**, charging is deliberately gentler and slower. Switch to **Let HP Manage My Charging** to test full-speed charging, then decide which mode you prefer long-term.

### Fix 5: Clean the USB-C port

1. Power off the laptop and unplug everything.
2. Shine a light into the port and look for lint or debris.
3. Use a wooden toothpick or plastic pick to gently remove lint. Never use metal.
4. Blow out dust with short bursts of compressed air held upright. A clean port restores full contact and proper PD negotiation.

### Fix 6: Update the BIOS

1. Open **HP Support Assistant** or visit [HP Support](https://support.hp.com/us-en) and enter your model.
2. Install the latest **BIOS** on AC power. HP regularly improves USB-C PD compatibility with third-party chargers in BIOS updates.
3. Also install the latest **chipset** drivers while you are there.

### Fix 7: Reduce load while charging

If the laptop draws 40W running games or renders while the charger delivers 45W, almost nothing reaches the battery.

1. Close heavy applications while charging, or at least pause games and video exports.
2. Check **Task Manager → Processes** sorted by CPU to find power hogs.
3. For a quick test, put the laptop to sleep while plugged in for 30 minutes and compare the charge gained versus charging while in use. If sleep-charging is dramatically faster, your charger is simply undersized for your workload — see our guide on [batteries that drain while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/).

### Fix 8: Test the charger on another device

Before replacing anything, confirm the charger itself is healthy.

1. Plug the PD charger into a phone or tablet that supports fast charging and check whether it fast-charges there.
2. If it crawls on every device, the charger is failing — replace it with a reputable brand.
3. If it fast-charges the phone but not the laptop, the issue is in the laptop's port, firmware, or settings, and the fixes above are where the answer lies. This isolation test saves you from replacing the wrong part.

## Closing

Slow USB-C charging on an HP laptop is almost always a chain problem: the charger, the cable, or the port is the weak link. Match the wattage, use a 100W-rated cable, pick the right port, and check HP's Battery Health Manager. Get those four right and PD charging is usually back to full speed.
