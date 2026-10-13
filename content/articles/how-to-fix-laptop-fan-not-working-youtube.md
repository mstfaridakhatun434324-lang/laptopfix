---
title: "Fix a Laptop Fan That Refuses to Spin"
slug: how-to-fix-laptop-fan-not-working-youtube
date: 2026-09-28
categories: ["drivers"]
tags: ["laptop fan", "overheating", "cooling", "fan control", "troubleshooting"]
description: "Laptop fan not spinning? Diagnose whether it's a driver, BIOS setting, or dead fan — and fix overheating before it damages your hardware."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-not-working-youtube.webp"
faqs:
  - q: "Is it normal for a laptop fan to stop completely sometimes?"
    a: "Yes, on modern laptops. Many models use zero-RPM fan curves that stop the fan entirely below about 50°C to stay silent. A fan that never spins even under heavy load or when the chassis is hot is the real problem — test with a stress test before assuming the worst."
  - q: "Can a driver stop the laptop fan from working?"
    a: "Yes. The embedded controller firmware and chipset drivers manage the fan curve, and a bad BIOS or chipset driver update can freeze the fan at zero. Reinstalling chipset drivers and updating the BIOS are the standard software fixes before suspecting hardware."
  - q: "How hot is too hot for a laptop?"
    a: "Sustained CPU temperatures above 95°C or a chassis too hot to touch indicate failed cooling. Brief spikes to 90°C during heavy loads are normal on thin laptops, but idle temperatures above 60°C with a silent fan mean the cooling system is not doing its job."
  - q: "Should I replace the fan myself?"
    a: "On many laptops the fan is a separate, inexpensive part and replacement is a moderate-difficulty repair with a service manual. If the laptop is under warranty, use it instead — opening the chassis can void coverage. Always rule out software causes first."
---

A laptop fan that never spins is easy to misread. Modern laptops deliberately stop their fans at low temperatures, so "not spinning" is only a problem when the machine is hot and still silent. The real diagnostic question is simple: does the fan spin when the CPU is under load and temperatures climb? If yes, your cooling is working as designed. If no, you're looking at a driver/firmware issue or a dead fan — and overheating will throttle performance and eventually damage components.

This guide separates normal behavior from real failure, then walks the repair path.

## Why this happens

- **Zero-RPM fan curve by design:** Most modern laptops stop the fan below 45–55°C for silence — this is normal, not a fault.
- **Corrupted chipset or EC driver:** The embedded controller that drives the fan depends on chipset drivers; a bad update can freeze fan control.
- **BIOS fan settings changed:** Some BIOS setups expose fan modes (silent/performance) that can get stuck or reset by an update.
- **Dust-clogged heatsink:** A blocked heatsink makes the fan work harder and louder, but severe clogging plus a failed bearing can stop it.
- **Dead fan motor or bearing:** Fans are mechanical; after years of spinning, bearings seize and motors burn out.
- **Disconnected fan cable:** The small fan connector can work loose after drops or previous servicing.
- **Power plan limiting cooling:** Aggressive power-saving plans can cap fan speed on some models.
- **Failed temperature sensor:** If the EC can't read temperatures, some firmware defaults the fan to off instead of full speed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually broken with a stress test

1. Install a temperature monitor like **HWiNFO64** or **Core Temp**.
2. Run a stress test (Cinebench, Prime95, or a demanding game) for five minutes while watching temperatures and listening.
3. If the fan spins up as temperatures pass 60–70°C, your fan is fine — the "problem" was the zero-RPM idle curve.
4. If temperatures exceed 90°C with no fan noise or airflow from the vents, you have a genuine failure — continue.

### Fix 2: Check the BIOS fan controls

1. Enter **BIOS/UEFI setup** and look for **Fan**, **Cooling**, or **Thermal** settings.
2. Set the fan mode to **Performance** or **Normal** rather than Silent/Quiet.
3. Some BIOS versions show live fan RPM — zero RPM here at high temperature confirms a hardware-level fault.
4. Save and exit, then repeat the stress test from Fix 1. For model-specific fan diagnostics, see our [fan troubleshooting guide](/articles/laptop-fan-not-working-troubleshooting/).

### Fix 3: Update chipset drivers and BIOS

1. Download the latest **chipset driver** and **BIOS** from your laptop manufacturer's support site for your exact model.
2. Install the chipset driver first, restart, then apply the BIOS update on AC power.
3. These updates restore proper communication between Windows, the embedded controller, and the fan.
4. Intel-based laptops can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch chipset updates Windows Update misses.

### Fix 4: Reset the power plan cooling policy

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Expand **Processor power management → System cooling policy** and set it to **Active** for both battery and plugged-in.
3. Active cooling ramps the fan before throttling the CPU; Passive does the opposite.
4. Also set **Maximum processor state** back to 100% if a "battery saver" tweak capped it — capped CPUs generate less heat, which can keep the fan off while the system still feels sluggish.

### Fix 5: Clean the vents and heatsink

1. Power off and unplug the laptop.
2. Blow **short bursts** of compressed air into the exhaust vents (hold the can upright) to dislodge dust.
3. For a thorough clean, remove the bottom cover per the service manual and clear the heatsink fins and fan blades with air and a soft brush.
4. While inside, check that the fan's cable is firmly seated in its motherboard connector — a loose cable is a free fix.

### Fix 6: Test the fan directly in diagnostics

1. Boot into the manufacturer's **hardware diagnostics** (F12 on Dell, F2 on Lenovo, Esc/F2 on HP) and run the **fan test**.
2. Diagnostics drive the fan directly, bypassing Windows entirely — if it spins here, the motor is alive and the fault is software.
3. If it doesn't spin in diagnostics, the fan motor, cable, or motherboard fan header has failed.
4. Note the exact result code; support will ask for it if you file a warranty claim.

### Fix 7: Replace the fan assembly

1. Look up your model's service manual and the fan's part number — fans are usually model-specific.
2. Order a genuine or high-quality compatible fan; they're typically inexpensive.
3. Replace it following the manual: disconnect battery, remove heatsink screws in numbered order, transfer thermal pads, and apply fresh thermal paste while you're in there.
4. If the laptop is under warranty, stop here and file a claim instead — a free professional repair beats a DIY risk.

### Fix 8: Use a cooling pad as a stopgap

1. If you must use the laptop before repair, a powered **cooling pad** adds external airflow through the intake vents.
2. Elevate the rear of the laptop for better natural convection.
3. Limit heavy tasks: cap frame rates, close background apps, and avoid charging while gaming to reduce heat.
4. This is a bridge, not a fix — sustained overheating shortens the life of the CPU, GPU, and battery. Related thermal behavior on the GPU side is covered in our [display driver troubleshooting](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/).

## Closing

A silent fan at idle is good engineering; a silent fan at 95°C is a failure. The stress test tells you which one you have in five minutes. From there it's a short path — BIOS mode, chipset drivers, a cleaning, and only then a replacement. Don't ignore a genuinely dead fan: heat kills laptops slowly and expensively.
