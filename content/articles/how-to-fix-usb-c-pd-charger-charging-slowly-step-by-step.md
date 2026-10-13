---
title: "USB-C PD Charging Slow: Step-by-Step Fix for Windows Laptops"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-step-by-step
date: 2026-10-01
categories: ["battery"]
tags: ["usb-c", "pd charger", "slow charging", "power delivery"]
description: "USB-C PD charger charging slowly? Follow this step-by-step guide to diagnose the charger, cable, port, and settings slowing you down."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-step-by-step.webp"
faqs:
  - q: "How can I tell how fast my laptop is actually charging?"
    a: "Hover over the battery icon to see the estimated time to full, or generate a battery report with powercfg /batteryreport and check recent charge rates. The simplest test: note the percentage, wait 30 minutes of light use, and compare the gain before and after each fix."
  - q: "Will a higher-wattage PD charger damage my laptop?"
    a: "No. USB-C Power Delivery is negotiated: the laptop only draws what it needs, up to its own maximum. A 100W charger on a 65W laptop is safe. What matters is that the charger meets the laptop's minimum, not that it matches exactly."
  - q: "Why does my laptop charge slower when it is hot?"
    a: "Lithium batteries charge slower at high temperatures by design — the charging circuit reduces current to protect the cells. If the laptop is hot from gaming, charging will throttle until it cools. This is normal protection behavior, not a fault."
  - q: "Do USB-C hubs slow down charging?"
    a: "Often yes. Many hubs pass through only part of the charger's wattage, and some reserve power for themselves. For the fastest charge, plug the charger directly into the laptop's charging port rather than through a hub or dock."
---

Your USB-C PD charger promises fast charging, but your laptop disagrees. The percentage ticks up at a glacial pace, or worse, it holds steady while plugged in as if the charger were decorative. Before you blame the laptop, understand this: USB-C charging involves four negotiators — charger, cable, port, and laptop — and the slowest one sets the speed.

This guide isolates each link in order, from the most common culprit to the rarest. By the end you will know exactly which piece to replace or adjust. Grab a pen or open a notes app, because you will be comparing charge speeds between tests, and written numbers beat memory every time. Do not skip the measurement steps — they are what turn guessing into diagnosing.

## Why this happens

- **Charger wattage below the laptop's draw:** The charger cannot cover both running the laptop and charging the battery, so charging slows to a trickle or stalls.
- **Cable bottleneck:** A 60W-rated or unrated cable caps negotiation below what the charger and laptop could otherwise agree on.
- **Wrong port:** Many laptops designate only one USB-C port for PD input; the others charge slowly or not at all.
- **Hub or dock in the path:** Docks and hubs consume power and often limit pass-through wattage.
- **Charge limit software:** Manufacturer tools (Lenovo Vantage, MyASUS, Dell Power Manager) can cap charge speed or percentage.
- **Thermal throttling:** A hot battery charges slowly by design to protect the cells.
- **Driver or firmware issue:** Outdated chipset drivers or BIOS can mishandle PD negotiation with third-party chargers.
- **Damaged charger circuitry:** A charger with frayed wiring or heat damage may still output power but fail PD negotiation, silently falling back to basic 5V charging at a crawl.
- **USB selective suspend interference:** Aggressive USB power management in Windows can disrupt steady PD negotiation on some machines, causing the charge rate to fluctuate or settle low.

## How to fix it

Work through these in order, measuring charge speed for 15–30 minutes after each change.

### Fix 1: Check what the laptop actually needs

1. Find the original charger's wattage on its label, or check the laptop's specs on the manufacturer's site.
2. Read your PD charger's label for its maximum output (look for the 20V line: 20V × 3.25A = 65W, 20V × 5A = 100W).
3. If the charger is weaker than the original, you have found the problem. Buy a PD charger rated at or above the original wattage. Overshooting is safe — the laptop negotiates only what it needs.

### Fix 2: Test with a known-good 100W cable

1. Borrow or buy a USB-C cable explicitly rated **100W (5A)** with an e-marker chip.
2. Keep it short — 1 meter is ideal for stable negotiation.
3. Charge for 20 minutes and compare the percentage gain to your old cable. If speed jumps, the old cable was the bottleneck. Retire it from laptop duty.

### Fix 3: Plug directly into the laptop's charging port

1. Remove any hub, dock, or adapter between the charger and the laptop.
2. Identify the PD-capable port: check the manual or look for a plug/battery icon beside the port.
3. Plug the charger straight into that port. Many "slow charging" cases are just a dock silently eating 15–20W. For related port issues, see our guide on [USB-C charging not working at all](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).

### Fix 4: Check manufacturer battery software

1. Open your brand's tool: **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **HP BIOS Battery Health Manager**, or **MSI Center**.
2. Look for charge caps, lifespan modes, or "slow charge" settings and disable them temporarily.
3. Retest. If speed returns, you can re-enable the gentler mode later as a conscious choice rather than a mystery.

### Fix 5: Cool the laptop down

1. Feel the chassis. If it is hot, charging is being throttled to protect the battery.
2. Close heavy apps, lift the rear of the laptop for airflow, and let it cool for 15 minutes.
3. Retest charging on a cool machine. If speed is normal when cool, the "problem" was thermal protection working correctly.

### Fix 6: Update chipset drivers and BIOS

1. Go to your manufacturer's support site and install the latest **chipset drivers** — these handle USB-C PD communication on most boards.
2. Install the latest **BIOS** on AC power without interruption. BIOS updates frequently fix PD negotiation with third-party chargers.
3. After updating, test with your normal charger and cable combo.

### Fix 7: Reset the battery drivers in Windows

1. Open **Device Manager** (**Win + X → Device Manager**).
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Shut down, unplug everything for **30 seconds**, reconnect the charger, and boot. Windows reinstalls the driver and re-establishes battery communication cleanly.

### Fix 8: Measure and decide

Do a controlled test: with the laptop asleep and plugged in, note the percentage, wait exactly 30 minutes, and note it again. A healthy setup should gain roughly 25–40% in that time on most ultrabooks. If yours gains under 10% after all fixes, the charger itself is likely faulty or counterfeit — replace it with a reputable brand. If the battery still [drains while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/) under load even with a proper charger, the laptop's power demands simply exceed what USB-C can deliver, and the original barrel charger is the answer.

## Closing

Slow USB-C PD charging is a process of elimination: wattage, cable, port, hub, software, heat, firmware. Test each link deliberately instead of guessing, and the culprit reveals itself quickly. Most of the time it is the cable or an underpowered charger — the two cheapest things to replace. And once charging is fast again, you will wonder why you tolerated the trickle for so long. Keep your test notes; if the problem ever returns, you will know exactly which link to recheck first.
