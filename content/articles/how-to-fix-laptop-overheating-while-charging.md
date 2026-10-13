---
title: "How to Stop Your Laptop Overheating While Charging"
slug: how-to-fix-laptop-overheating-while-charging
date: 2026-10-10
categories: ["battery"]
tags: ["overheating", "charging", "cooling"]
description: "Laptop gets hot every time you plug in? Fix charging-related overheating with airflow, charge limits, and workload changes."
thumbnail: "/images/thumbs/how-to-fix-laptop-overheating-while-charging.webp"
faqs:
  - q: "Is it normal for a laptop to get hot while charging?"
    a: "Some warmth is normal — charging is an exothermic process and the power circuitry adds heat. What's not normal is the machine becoming uncomfortable to touch, fans screaming constantly, or the battery area getting distinctly hotter than the rest of the chassis. That pattern means heat sources are stacking up and need addressing."
  - q: "Should I use my laptop while it's charging?"
    a: "Light use is fine. Heavy workloads (gaming, rendering) during fast charging pile CPU/GPU heat on top of charging heat, which is the worst thermal combination for the battery. If you must do heavy work plugged in, it's better once the battery is already full, when charge current — and charge heat — drops to nearly zero."
  - q: "Does fast charging damage the battery through heat?"
    a: "Fast charging generates more heat than slow charging, and sustained heat accelerates wear — that's the tradeoff. Most modern laptops manage this with thermal throttling of charge current. You can help by keeping the machine ventilated during charging and using charge limits so the hottest part of the curve (the top 20%) is avoided."
  - q: "Why does my charger itself get so hot?"
    a: "Power bricks convert AC to DC at 85-95% efficiency, and the lost 5-15% becomes heat — a 90W charger can dissipate over 10W as heat, which feels very warm. That's normal. What's not normal is a burning smell, discoloration, or a charger too hot to hold, which means it's failing and should be replaced."
---

Charging adds a whole second heat source to your laptop. The CPU and GPU make their heat, and then the battery cells, the charging circuitry, and the power brick all add theirs on top. When everything stacks — heavy workload plus fast charging plus blocked vents — temperatures climb into the range that actively shortens battery life. The fix isn't one trick; it's unstacking those heat sources so they stop arriving all at once.

This guide is specifically about the charging side of overheating: what's normal, how to measure it, and how to change when and how you charge so the heat stays in the safe zone. For the general overheating playbook (dust, paste, airflow), see [fixing an overheating laptop battery](/articles/how-to-fix-laptop-battery-overheating-reddit/).

## Why this happens

- **Charging is exothermic:** The chemistry of pushing energy into lithium cells releases heat, most intensely during the fast-charge phase.
- **Heat stacking:** CPU/GPU heat plus charging heat arrive simultaneously when you work hard while plugged in at low battery.
- **Voltage regulator heat:** The motherboard's power circuitry works hardest during charging and sits physically near the battery in many designs.
- **Blocked airflow during charging:** People charge laptops on beds and couches, sealing vents exactly when the machine needs cooling most.
- **Underpowered or failing charger:** A struggling charger runs hot and charges inefficiently, converting more energy to waste heat.
- **Aging cells:** Worn batteries have higher internal resistance, so the same charge current produces more heat than it did when new.

## How to fix it

Work through these in order — charging habits first, hardware second.

### Fix 1: Measure charging temperatures properly

Establish what's actually happening before changing habits.

1. Install HWMonitor or HWiNFO64 and note battery-area and CPU temperatures with the machine idling on battery.
2. Plug in at around 20-30% battery and record temperatures every 10 minutes through the charge cycle — you'll see the peak during fast charging and the cooldown as it approaches full.
3. Repeat the same test while doing your normal workload plugged in, and compare the two curves.
4. If the battery area exceeds ~50°C sustained during charging, or the machine thermal-throttles (sudden slowdowns), you have a real problem to fix.
5. Re-run this same test after the fixes below to verify improvement.

### Fix 2: Separate heavy work from fast charging

Break up the worst heat combination.

1. When the battery is low (under ~80%), keep workloads light while it charges — browsing and documents, not gaming or video encoding.
2. Do your heavy plugged-in work after the battery is full, when charge current drops to a trickle and charging heat nearly disappears.
3. If you must work hard on a low battery, consider charging to 60-70% first with the machine idle or asleep, then unplugging for the heavy session on battery.
4. In **Settings > System > Power & battery > Power mode**, use **Best power efficiency** during charging sessions to cap the heat the CPU adds.
5. Close unnecessary heavy apps during charging — check **Task Manager > Processes** sorted by CPU for anything burning cycles you don't need.

### Fix 3: Set a charge limit to skip the hottest part of the curve

The top of the charge is where heat and wear concentrate.

1. **Lenovo:** enable Conservation Mode in Vantage (caps at ~60%). **ASUS:** MyASUS > Battery Health Charging > Balanced (80%) or Maximum Lifespan (60%).
2. **Dell:** BIOS or Dell Power Manager > Battery Settings > Standard/Adaptive or a custom 50-80% range. **HP:** BIOS > Power Management > Battery Health Manager.
3. **Microsoft Surface:** the built-in Smart Charging caps at 80% automatically on newer devices.
4. A lower cap means the battery spends less time in the high-voltage, high-heat region — this single setting does more for long-term battery health than almost anything else.
5. Only charge to 100% when you genuinely need maximum runtime for travel.

### Fix 4: Fix the charging environment

Where and how you charge matters as much as what you run.

1. Always charge on a hard, flat surface with vents clear — never charge a laptop inside a bag, under bedding, or on a couch cushion.
2. Elevate the rear of the laptop an inch or two during charging to open the intake airflow path.
3. Keep the power brick itself ventilated and off insulating surfaces — don't bury it under blankets or wedge it behind furniture.
4. Charge in the coolest reasonable room; a 5°C cooler room is roughly 5°C cooler components.
5. If you use a dock, make sure it isn't blocking the laptop's vents — some vertical docks partially cover intake grilles.

### Fix 5: Check the charger and cable

Bad power delivery creates waste heat everywhere.

1. Use the original charger or a reputable replacement with matching wattage, voltage, and (for USB-C) proper PD rating — check the fine print on the brick.
2. Inspect the cable for kinks, fraying, or heat damage; a damaged cable increases resistance and heat at every connection.
3. Feel the brick during charging: warm is normal, too-hot-to-hold or smelling of hot plastic is not — replace it.
4. For USB-C charging, confirm the laptop is actually negotiating the right PD profile (some machines show this in BIOS or the OEM app) — a fallback to 5V slow charging is inefficient and warm.
5. If charging is slow as well as hot, see [troubleshooting slow charging](/articles/troubleshoot-usb-c-pd-charger-charging-slowly/) — the causes overlap.

### Fix 6: Clean the cooling system

Charging heat is manageable when the cooling system works; it's the dust that makes it unmanageable.

1. With the machine off, blow compressed air through the exhaust vents in short bursts to clear surface dust.
2. For a thorough job, remove the bottom panel and clean fan blades and heatsink fins directly, holding fans still while you blow.
3. Check the battery visually while inside — swelling, warping, or a chemical smell means stop and replace the pack.
4. On machines 2+ years old with gradually rising temperatures, consider fresh thermal paste on the CPU/GPU — dried paste is a classic cause of heat creep.
5. After cleaning, rerun the temperature test from Fix 1 under identical conditions to confirm the drop.

### Fix 7: Update firmware and drivers

Manufacturers do tune charging thermals in updates.

1. Check your OEM app (Vantage, MyASUS, SupportAssist, HP Support Assistant) for **BIOS/UEFI** updates — charging algorithms and thermal tables are frequently refined.
2. Update chipset and battery drivers via **Device Manager > Batteries** and **System devices**.
3. Some updates specifically address "battery gets hot while charging" complaints — check the BIOS changelog for thermal or battery entries.
4. After updating, monitor one full charge cycle to confirm behavior improved.
5. Intel's driver update utility at [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can catch chipset driver updates the OEM app misses.

## Closing

Charging heat is physics — you can't eliminate it, but you can stop it from stacking with everything else. Charge on a hard surface, keep heavy work away from the fast-charge window, cap the charge at 80% or below, and keep the vents clean. Do those four things and the "hot while charging" problem usually fades into mild, harmless warmth.
