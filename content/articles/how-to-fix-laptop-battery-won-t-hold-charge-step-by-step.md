---
title: "Laptop Battery Won't Hold a Charge? Step-by-Step Diagnosis"
slug: how-to-fix-laptop-battery-won-t-hold-charge-step-by-step
date: 2026-09-14
categories: ["battery"]
tags: ["battery won't hold charge", "short battery life", "wear level", "diagnosis"]
description: "Your laptop dies minutes after unplugging even though it 'charges to 100%'. Here's how to tell whether it's wear, calibration, or something else — step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-won-t-hold-charge-step-by-step.webp"
faqs:
  - q: "Why does my laptop die at 30% or 40% battery?"
    a: "The battery gauge is miscalibrated or the cells are worn. The controller thinks there's 30% left based on voltage, but the worn cells' voltage collapses suddenly under load. A full calibration cycle (100% → drain to shutdown → rest → 100%) often fixes the gauge; if it doesn't, check the wear level — high wear means the cells genuinely can't deliver."
  - q: "My battery charges to 100% but only lasts 20 minutes. Is it dead?"
    a: "Almost certainly, yes — if the wear level is high. '100%' just means the battery reached whatever its current full charge capacity is, which might be a fraction of the original design capacity. Run powercfg /batteryreport: if full charge capacity is under 50% of design, the battery is at end of life and needs replacing."
  - q: "Can a Windows update cause the battery to not hold charge?"
    a: "An update can't damage cells, but it can make a worn battery's problems visible: new power management behavior, a reset gauge, or background tasks consuming more power. If the timing coincides with an update, check for runaway processes and recalibrate before concluding the battery died."
  - q: "Is it worth replacing the battery on an old laptop?"
    a: "If the laptop otherwise meets your needs, usually yes — a genuine replacement battery is far cheaper than a new laptop and restores original runtime. Check that the rest of the machine is healthy first (it boots reliably, the charger works, no swelling damage), and buy a genuine battery, not the cheapest marketplace option."
---

It charges to 100%. You unplug, feeling optimistic. Twenty minutes later it's at 12%, and by minute thirty it's dead. Or it skips from 40% straight to 7% and shuts off without warning. A battery that won't hold a charge is different from one that won't charge at all — the charging circuitry works fine; the battery just can't store (or report) usable energy anymore.

The critical question is whether the battery is truly worn out or just misreporting. Those look identical from the outside but have opposite fixes: one needs a $60 battery, the other needs a free calibration. This guide tells them apart.

## Why this happens

- **Genuine cell wear:** Lithium cells lose capacity with every cycle and with age. At 40-60% wear, "100%" represents less than half the original runtime.
- **Miscalibrated gauge:** The controller's percentage table drifted. It reports 40% when the cells are nearly empty, causing sudden shutdowns that look like the battery can't hold charge.
- **High self-discharge:** Worn or damaged cells lose charge internally even with no load — the battery drains itself sitting on a shelf.
- **Voltage sag under load:** Worn cells maintain voltage at idle but collapse the moment the CPU/GPU demands current, triggering the low-battery shutdown prematurely.
- **Unbalanced cell groups:** In multi-cell packs, one weak group hits empty while others still have charge. The controller shuts down to protect the weak group, wasting the remaining capacity.
- **Heat-accelerated degradation:** A battery that lived hot (gaming laptop, blocked vents) wears far faster than its cycle count suggests.
- **Parasitic drain:** A motherboard fault or misbehaving device drawing current even when "off" can mimic a battery that won't hold charge — the battery is fine, something is drinking from it.

## How to fix it

Work through these in order — diagnose before spending money.

### Fix 1: Get the real numbers with a battery report

Everything starts with data. Guessing wastes money.

1. Plug in, charge to 100%, and leave it for 30 minutes.
2. Open an admin terminal (right-click **Start > Terminal (Admin)**) and run `powercfg /batteryreport`.
3. Open the HTML file from your user folder. Note **Design Capacity** and **Full Charge Capacity**.
4. Compute wear: (Design − Full Charge) ÷ Design × 100.
5. **Under 20% wear:** the battery is healthy — your problem is calibration or parasitic drain. Continue with Fix 2.
6. **20-40% wear:** partially worn. Calibration may recover some usable runtime; also reduce load (Fix 4).
7. **Over 40% wear:** the battery is genuinely worn out. Skip to Fix 6 — calibration won't save it.

### Fix 2: Run a full calibration cycle

If wear is low but runtime is terrible, the gauge is lying. Recalibrate.

1. Charge to **100%** plus 2 hours plugged in (cell balancing).
2. **Settings > System > Power & battery**: set screen and sleep to **Never** on battery.
3. **Control Panel > Power Options > advanced settings > Battery**: set **Critical battery action** to **Shut down**, **Low battery level** to 5%.
4. Unplug and use lightly until the laptop shuts itself off.
5. Leave it **off and unplugged for 3+ hours** — the resting-voltage measurement is the whole point.
6. Charge **uninterrupted to 100%** with the laptop off or idle.
7. Test runtime. If the battery now declines smoothly and lasts proportionally to its wear level, the gauge was the problem. If it still dies suddenly, the cells can't deliver — Fix 6. Our detailed guide on [fixing calibration that won't work](/articles/how-to-fix-laptop-battery-calibration-not-working-reddit/) covers stubborn cases.

### Fix 3: Check for parasitic drain

Something might be drinking power that the battery report can't see.

1. Shut down the laptop fully (disable Fast Startup first: **Control Panel > Power Options > Choose what the power buttons do** → uncheck **Turn on fast startup**).
2. Note the exact battery percentage, unplug, and leave it off for **8 hours** (overnight).
3. Power on (still unplugged) and check the percentage. A healthy battery loses **0-3%** overnight while off. Losing 10%+ means parasitic drain or high self-discharge.
4. To distinguish: repeat the test with the battery **removed** (if removable) — if it still loses charge on the shelf, it's cell self-discharge (bad battery). If it only drains when installed and "off," something on the motherboard is drawing power.
5. Common parasitic sources: **USB charging-while-off** features (disable in BIOS), **Wake on LAN** (disable in BIOS and in the network adapter's Device Manager properties), and Thunderbolt docks backfeeding power.
6. If the laptop loses significant charge while fully off and the battery holds charge on the shelf, see our guide on [battery draining overnight while off](/articles/troubleshoot-battery-drains-overnight-when-laptop-is-off/).

### Fix 4: Reduce the load to match reality

A worn battery plus a heavy workload equals sudden death. Lighten the load.

1. **Settings > System > Power & battery > Power mode** → **Best power efficiency**.
2. Lower screen brightness to minimum comfortable; set screen-off after 2 minutes.
3. **Task Manager > Startup apps**: disable everything non-essential.
4. Close browser tab hoards; video playback and video calls are the heaviest common loads — a worn battery that idles for 2 hours may die in 25 minutes of video calls.
5. This doesn't fix wear, but it stretches remaining capacity and confirms the diagnosis: if light use gives reasonable runtime but heavy use kills it instantly, that's textbook voltage sag from worn cells.

### Fix 5: Reinstall drivers and update firmware

Rule out the software layer before buying hardware.

1. **Device Manager > Batteries**: uninstall **Microsoft ACPI-Compliant Control Method Battery**, shut down, unplug 30 seconds, reboot.
2. Update **BIOS** and **chipset drivers** from the manufacturer — EC firmware updates sometimes improve how the controller handles worn cells (better low-battery warnings instead of sudden death).
3. Check manufacturer tools for battery diagnostics: **Lenovo Vantage**, **Dell Power Manager**, **HP PC Hardware Diagnostics (F2)**, **MyASUS** — run their battery tests for a second opinion.
4. If the manufacturer's tool reports the battery as failed/poor while Windows seemed optimistic, trust the manufacturer's tool — it talks to the controller directly.

### Fix 6: Replace the battery

When wear is high or cells are damaged, replacement is the only fix.

1. Confirm the decision: wear over 40%, or sudden-death behavior persisting after calibration, or physical swelling.
2. **Safety check first:** if the bottom panel bulges or the trackpad lifts, stop using the laptop and get professional replacement — swollen batteries are fire hazards.
3. Find the exact battery part number (battery label, or manufacturer's support site via serial number).
4. Buy **genuine or manufacturer-certified**. This matters enormously: cheap batteries have worse cells, fake capacity labels, and controllers that misreport — you'll be back to "won't hold charge" within months.
5. Check warranty — many batteries are covered 12 months.
6. After installing, do one full calibration cycle (Fix 2) so the controller learns the new battery properly, then verify with `powercfg /batteryreport` that full charge capacity matches design.

### Fix 7: Break the habits that killed the last one

Make the replacement last.

1. Avoid sustained heat: don't game on soft surfaces, keep vents clear, clean dust annually.
2. If you mostly work plugged in, use the manufacturer's charge limit (Lenovo Conservation Mode 60%, ASUS 80%, Dell Adaptive) — holding at 100% constantly accelerates wear.
3. Don't leave the battery at 0% for days; don't store at 100% for months either — ~50% is ideal for storage.
4. Calibrate every 2-3 months so the gauge stays honest and you notice real degradation early.
5. Our guide on [checking design vs full charge capacity](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/) shows how to monitor wear over time — a 5-minute check every few months.

## Closing

"Won't hold a charge" is either a lying gauge or dying cells, and the battery report tells you which in two minutes. Calibrate when wear is low; replace when it's high; check for parasitic drain when the numbers don't add up. Don't buy a battery to fix a calibration problem, and don't calibrate hoping to fix worn-out chemistry.

*Related reading: [battery calibration not working](/articles/how-to-fix-laptop-battery-calibration-not-working-reddit/), [battery drains overnight while off](/articles/troubleshoot-battery-drains-overnight-when-laptop-is-off/)*
