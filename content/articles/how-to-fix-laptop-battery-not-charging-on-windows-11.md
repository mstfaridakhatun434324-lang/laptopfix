---
title: "How to Fix a Laptop Battery That Won't Charge on Windows 11"
slug: how-to-fix-laptop-battery-not-charging-on-windows-11
date: 2026-09-27
categories: ["battery"]
tags: ["not charging", "windows 11", "plugged in not charging", "troubleshooting"]
description: "Laptop says 'plugged in' but the battery won't charge on Windows 11? Here's the complete fix path — from quick checks to driver resets."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-on-windows-11.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean on Windows 11?"
    a: "It means Windows detects the charger but the battery isn't accepting charge. Common causes: a charge limiter holding the battery at a threshold, a worn battery that can't take more charge, overheating that paused charging, or a driver glitch misreporting the state."
  - q: "How do I fix a laptop battery that won't charge?"
    a: "Start with the easy checks: confirm the charger wattage is correct, check for charge limiters in your manufacturer's app, and let an overheated laptop cool. Then reinstall the battery drivers in Device Manager, reset the embedded controller, and check battery health with powercfg /batteryreport."
  - q: "Can a Windows 11 update stop the battery from charging?"
    a: "Yes — updates sometimes corrupt the ACPI battery driver or break the manufacturer's power app, both of which can halt charging. Reinstalling the battery driver and updating the vendor app are the standard fixes after an update."
  - q: "When should I replace the battery instead of troubleshooting?"
    a: "When powercfg /batteryreport shows full charge capacity below 50-60% of design capacity, or the battery is swollen, gets very hot, or drops charge in minutes. At that point no software fix restores capacity — replacement is the answer."
---

"Plugged in, not charging." Four words that turn a laptop into a desktop. The charger is connected, Windows sees it, but the battery percentage sits frozen — or worse, slowly declines while plugged in. On Windows 11, this has a well-trodden diagnostic path, and most cases resolve without spending money.

The key insight: "not charging" is a symptom with many causes, from a helpful feature (charge limiter) to a dying battery. Work the list in order and you'll identify yours.

## Why this happens

- **Charge limiter active** — the battery is intentionally held at 80% or lower.
- **Wrong or failing charger** — insufficient wattage to both run the laptop and charge.
- **Overheating** — charging paused as a thermal safety measure.
- **Corrupted battery driver** — Windows misreporting or blocking charge state.
- **Worn-out battery** — degraded cells that can't accept charge.
- **Stuck embedded controller** — the charge circuitry needs a reset.
- **Loose connection** — charger partially seated, delivering power but not stable charging.

## How to fix it

Work through these in order — quick checks first.

### Fix 1: Rule out the charge limiter

Before anything else, check whether the battery is *supposed* to stop:

1. Open your manufacturer's app — **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **Surface app** — and look for charge thresholds, Conservation Mode, or Smart Charging.
2. If the battery is sitting at exactly 80%, 60%, or ~55%, that's the limiter doing its job.
3. Temporarily disable it and see if charging resumes.

This single check resolves a huge share of "not charging" reports. If the limiter itself is misbehaving, our [charge limiter troubleshooting guide](/articles/how-to-fix-battery-limiter-not-working-on-windows-11/) covers that.

### Fix 2: Verify the charger and connection

A charger that's merely *adequate* for running the laptop may not have headroom to charge:

1. Confirm the charger's wattage matches your laptop's requirement (printed on the original brick).
2. Reseat the connector firmly — barrel plugs and USB-C both suffer from partial insertion.
3. Plug directly into a wall outlet, bypassing docks and power strips for the test.
4. If possible, test with a known-good charger of the correct wattage.

If charging resumes with a different charger, yours is failing — replace it with the right specs. For USB-C-specific issues, see our [USB-C charging troubleshooting](/articles/usb-c-charging-not-working-on-laptop-troubleshooting/).

### Fix 3: Cool it down

Feel the laptop — if it's hot, charging may be thermally paused:

1. Shut down and let it cool for 30 minutes in a ventilated spot.
2. Clear blocked vents and move off soft surfaces.
3. Power on, plug in, and check whether charging resumes.

Persistent overheating while charging needs addressing on its own — see our guide on [laptops overheating while charging](/articles/how-to-fix-laptop-overheating-while-charging-youtube/).

### Fix 4: Reinstall the battery drivers

The classic Windows-side fix:

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
3. Right-click **Microsoft AC Adapter** > **Uninstall device**.
4. Shut down (not restart), wait 30 seconds, power on with the charger connected.

Windows rebuilds both drivers at boot. Check the battery icon after a minute — the status should update to charging if this was the blocker.

### Fix 5: Reset the embedded controller

The EC orchestrates charging, and it gets stuck:

1. Shut down completely and unplug the charger and all peripherals.
2. Hold the power button for **30–60 seconds** (or use the pinhole reset button).
3. Reconnect the charger and power on.

This is safe, takes a minute, and resolves charge-state glitches that survive driver reinstalls.

### Fix 6: Check battery health with a report

If the above didn't help, look at the battery itself:

1. Open Command Prompt and run `powercfg /batteryreport`.
2. Compare **Full Charge Capacity** to **Design Capacity**.
3. Below 60% of design, the battery is significantly worn; near 40-50%, it may refuse to charge meaningfully at all.

Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through interpreting every section. If wear is severe, skip to Fix 8.

### Fix 7: Update BIOS, chipset, and the vendor app

Firmware-level charging bugs get fixed in updates:

1. Install the latest **BIOS** from your manufacturer's support site if the notes mention power or charging.
2. Update **chipset drivers** and your **vendor's power app** (Vantage, MyASUS, Dell Power Manager).
3. Run **Windows Update** including optional driver updates.

Do the BIOS update with the charger connected and don't interrupt it.

### Fix 8: Replace the battery when it's done

If the report shows severe wear, or the battery is swollen, overheats, or drops from full to empty in minutes:

1. Find the exact battery model number for your laptop.
2. Buy a genuine or reputable replacement — avoid suspiciously cheap no-name cells.
3. After installing, run one full calibration cycle.

A fresh battery is the only fix for chemical wear, and on an otherwise healthy laptop it's far cheaper than a new machine. If the laptop is new and under warranty with a dead battery, contact the manufacturer instead of buying one yourself.

## Closing

"Plugged in, not charging" on Windows 11 is a process-of-elimination problem: limiter, charger, heat, drivers, controller, battery — in that order. Most people find their answer in the first three steps, which take about ten minutes combined. The battery report is your objective referee throughout: it tells you whether you're fighting software or chemistry, and that distinction decides whether the fix is free or a replacement battery.

One last habit: once charging works again, glance at the battery icon's status text occasionally over the next few days. If "not charging" creeps back intermittently, note when it happens — during heavy gaming, when hot, or at random. That pattern is valuable diagnostic information that points straight at the culprit, whether it's heat, a dying charger, or a battery on its way out.

And keep your charger honest: if you had to borrow a good one to diagnose, don't hand it back and keep using the suspect brick "because it mostly works." An intermittent charger causes exactly the kind of confusing on-and-off symptoms that waste hours of troubleshooting — replace it and move on.
