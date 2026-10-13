---
title: "Laptop Only Works When Plugged In? Here's How to Fix It"
slug: how-to-fix-laptop-only-works-when-plugged-in-youtube
date: 2026-09-08
categories: ["battery"]
tags: ["only works plugged in", "battery dead", "shuts off unplugged", "troubleshooting"]
description: "Your laptop dies the instant you unplug it? Here's how to figure out whether the battery is dead, disconnected, or just misconfigured — and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-youtube.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug the charger?"
    a: "The battery isn't delivering any power — it's either completely worn out, disconnected from the motherboard, not detected by Windows, or in a deep-discharge protection state. The laptop runs fine on AC because the charger powers it directly."
  - q: "Can a dead battery damage my laptop if I keep using it plugged in?"
    a: "A dead battery won't usually damage anything, but a swollen one can — check for a bulging trackpad, keyboard, or bottom panel. If you see swelling, stop using the laptop and get the battery replaced promptly."
  - q: "Is it worth replacing the battery on an old laptop?"
    a: "If the laptop is otherwise fast enough for your needs, a battery replacement (often $40–$90 for genuine parts) is far cheaper than a new machine. Check the battery's health with powercfg /batteryreport first to confirm it's actually worn out."
  - q: "Could this be a software problem rather than a dead battery?"
    a: "Sometimes. Corrupted battery drivers or a stuck embedded controller can make Windows ignore a healthy battery. The driver reinstall and EC reset steps below take a few minutes and are worth trying before buying a replacement."
---

Unplug the charger and the laptop dies instantly — no graceful shutdown, no low-battery warning, just off. Plug it back in and it boots like nothing happened. If your laptop has effectively become a desktop, the battery has dropped out of the power equation entirely.

This feels like a dead battery, and often it is. But "dead" covers several different situations — a worn-out battery, one Windows can't see, or one stuck in a protection state — and they don't all need a replacement. Let's diagnose properly.

One quick test before you start: with the charger plugged in, check whether the battery icon shows a percentage that never changes, or "plugged in, not charging." A stuck percentage usually means the battery can't take a charge (worn out), while "not detected" points to a communication problem. That distinction will tell you which fixes below are most likely to help.

## Why this happens

- **Battery worn to zero usable capacity** — it reports a charge but can't deliver current under load.
- **Battery not detected by Windows** — driver corruption makes a healthy battery invisible.
- **Deep-discharge protection** — a fully drained battery's safety circuit refuses to wake up without a long charge.
- **Loose internal battery connector** — common after drops or on machines that were opened for upgrades.
- **Charging circuit fault** — the battery is fine but the motherboard can't charge or draw from it.
- **Swollen battery disconnected by its own safety mechanism** — some batteries cut themselves off when they swell.

## How to fix it

Work through these in order — diagnose before you buy.

### Fix 1: Check what Windows thinks about the battery

Press **Win + X**, open **Device Manager**, and expand **Batteries**. If **Microsoft ACPI-Compliant Control Method Battery** is missing or has a warning icon, Windows can't see the battery at all — that's a detection problem, not necessarily a dead battery. Also check the taskbar battery icon: "No battery is detected" versus a percentage that drops to zero instantly tells you which situation you're in. For the no-detection case, our [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/) goes deeper.

### Fix 2: Reinstall the battery drivers

A corrupted driver can make Windows ignore a perfectly good battery:

1. In **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
2. Also uninstall **Microsoft AC Adapter**.
3. Shut down (don't restart), unplug the charger, wait 60 seconds, then plug in and power on.

Windows rebuilds both drivers from scratch during boot. Unplug the charger after startup and see if the laptop stays alive.

### Fix 3: Try the long slow charge

A battery in deep-discharge protection sometimes needs patience, not a replacement:

1. Plug in the charger and leave the laptop **powered off** for at least **4–6 hours** (overnight is better).
2. Don't try to power it on during this time — some protection circuits only reset when the machine is off.
3. After the long charge, power on and check the battery percentage.

If the battery now shows a charge and the laptop survives unplugged for even a few minutes, the protection circuit has reset. Run a [battery calibration](/articles/how-to-calibrate-laptop-battery-windows-11/) next to teach the gauge the true capacity.

### Fix 4: Run powercfg /batteryreport and read the numbers

Open Command Prompt and run `powercfg /batteryreport`, then open the HTML report:

- **Design Capacity vs. Full Charge Capacity:** if full charge is under 40–50% of design, the battery is heavily worn.
- **Cycle count:** several hundred cycles on a 3+ year old battery means normal end-of-life.
- **Recent usage:** if the report shows the battery draining from 100% to 0% in minutes, it can't hold a charge.

This is the single most useful diagnostic step — it tells you whether to keep troubleshooting software or start shopping. Our guide to [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through interpreting every section.

### Fix 5: Check for a swollen battery

Power off, unplug, and inspect the laptop physically: does the trackpad feel raised, does the keyboard bulge, does the bottom panel not sit flat, are there gaps in the seams? A swollen lithium battery is a safety issue — don't puncture it, don't keep charging it, and get it replaced at a repair shop. Swollen batteries sometimes trigger the exact "only works plugged in" symptom because their internal safety circuit disconnects them.

### Fix 6: Reseat the internal battery connector

If you're comfortable opening the laptop (check your warranty first):

1. Power off, unplug, and remove the bottom panel.
2. Locate the battery connector on the motherboard, unplug it, wait 30 seconds, and reconnect it firmly.
3. Reassemble and test.

A connector that worked loose — from a drop, heat cycling, or a previous repair — causes exactly this symptom. If the connector looks corroded or burnt, that's a board-level problem for a technician.

### Fix 7: Replace the battery

If the report shows severe wear, the battery is swollen, or nothing else helped:

1. Find the exact battery model number (printed on the battery or in your laptop's manual).
2. Buy a genuine or high-quality replacement — cheap no-name batteries often have inflated capacity claims and poor safety circuits.
3. After installing, run one full charge-discharge cycle so the system learns the new battery.

## Closing

A laptop that only works plugged in is telling you the battery is out of the circuit — your job is to find out why before spending money. The driver reinstall and long charge are free and fix the software-side cases; the battery report tells you when the battery is genuinely worn out. And if you spot any swelling, skip the rest of the troubleshooting and get that battery replaced safely.

Once you've sorted it, keep an eye on the battery report every few months. Catching wear early — when capacity first dips below 80% of design — lets you plan a replacement on your schedule instead of having the battery die on you mid-trip.

It's also worth keeping your important work saved to cloud storage or an external drive while the battery is unreliable. A laptop with no working battery has no safety net against power cuts, so treat every unplugged moment as borrowed time until the battery is genuinely fixed.
