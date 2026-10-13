---
title: "How to Fix a Laptop Overheating While Charging on Windows 10"
slug: how-to-fix-laptop-overheating-while-charging-on-windows-10
date: 2026-09-19
categories: ["battery"]
tags: ["overheating", "charging", "windows 10"]
description: "Laptop burning hot every time you plug in on Windows 10? Cool it down with these charging, airflow, and power plan fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-overheating-while-charging-on-windows-10.webp"
faqs:
  - q: "Is it normal for a laptop to get hot while charging?"
    a: "Warm is normal — charging generates heat, especially fast charging. Hot to the touch (uncomfortable to hold, fans screaming constantly) is not normal and shortens battery lifespan. If the bottom is too hot to rest on your lap, treat it as a problem worth fixing."
  - q: "Can charging overheat damage my battery?"
    a: "Yes. Sustained heat above 35-40°C accelerates chemical aging in lithium batteries, permanently reducing capacity. A laptop that always runs hot while charging will lose battery health noticeably faster than one that stays cool."
  - q: "Should I remove the battery while using the laptop plugged in?"
    a: "Only if the battery is removable — most modern laptops have sealed batteries. For removable batteries, running on AC without the battery reduces heat exposure, but you lose your backup power. For sealed batteries, use the manufacturer's charge limiter instead."
  - q: "What temperature is dangerous for a laptop while charging?"
    a: "CPU temperatures up to 85-90°C under load are typical and safe. The concern is sustained high battery temperature — keep it under 40°C. If the chassis is painfully hot or the laptop shuts down by itself, stop using it and get it serviced."
---

Some warmth while charging is physics — electricity moving into a battery makes heat. But there is a line between "warm" and "I could fry an egg on the keyboard," and if your Windows 10 laptop crosses it every time you plug in, something is amplifying the heat. Usually it is not the charging alone; it is charging plus a CPU working hard, blocked vents, or a power plan running everything at full tilt.

Heat is the number one enemy of battery lifespan, so this is worth fixing even if the laptop seems to "handle" it. These fixes attack the heat from every angle: airflow, workload, charging behavior, and power settings.

## Why this happens

- **Charging and heavy CPU load happen at once.** Gaming or video rendering while charging stacks CPU heat on top of charging heat.
- **Vents are blocked or clogged with dust.** The cooling system cannot shed heat if intake and exhaust vents are obstructed.
- **The power plan runs the CPU at maximum.** The High Performance plan keeps clock speeds pegged even for light tasks.
- **Background processes spike when plugged in.** Windows Update, indexing, and cloud syncs often wait for AC power to do heavy work.
- **The battery is aging.** Old batteries have higher internal resistance, which means more heat for the same charging current.
- **Thermal paste has dried out.** After 3-4 years, the paste between CPU and heatsink degrades and temperatures climb.
- **The charger is wrong.** An incorrect-voltage charger can cause excess heat in the charging circuit.

## How to fix it

Work through these in order — start with the free airflow fixes.

### Fix 1: Fix the airflow situation

This alone drops temperatures 5-15°C for most people.

1. Always use the laptop on a hard, flat surface. Beds, couches, and laps block the intake vents on the bottom.
2. Make sure no vent is pushed against a wall or monitor stand — exhaust needs a few inches of clearance.
3. Shut the laptop down and unplug it. Blow short bursts of compressed air into the intake and exhaust vents to clear dust. Hold fans still with a toothpick if you can see them, so they do not spin backwards.
4. Consider a simple cooling stand or even two bottle caps under the rear edge to lift the laptop — elevation alone improves airflow noticeably.
5. Feel the difference after 30 minutes of charging on the improved setup.

### Fix 2: Tame the power plan

Windows 10's High Performance plan is a space heater. Switch it.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options**.
2. Select the **Balanced** plan instead of **High performance**.
3. Click **Change plan settings** > **Change advanced power settings**.
4. Expand **Processor power management** > **Maximum processor state**.
5. Set **Plugged in** to **95%** instead of 100%. This tiny reduction disables turbo boost, which is responsible for a huge share of heat spikes, with barely noticeable performance loss.
6. Expand **System cooling policy** and set **Plugged in** to **Active** so fans ramp up before the CPU throttles.

### Fix 3: Find what is hammering the CPU while charging

Charging does not happen in a vacuum — something is usually generating heat alongside it.

1. Plug in the charger, wait 10 minutes, then open **Task Manager** (**Ctrl + Shift + Esc**).
2. Click the **CPU** column to sort by usage.
3. Look for anything consistently above 10-15%: Windows Update, antivirus scans, search indexing, or a runaway browser tab.
4. For Windows Update hogging the CPU, go to **Settings** > **Update & Security** > **Windows Update** > **Advanced options** and limit active hours or pause updates while you work.
5. Disable heavy startup apps: Task Manager > **Startup** tab > right-click and **Disable** anything you do not need at boot.
6. If a single app is always the culprit, check for an update to that app — runaway processes are often bugs.

### Fix 4: Change how the battery charges

Reducing charging stress directly reduces charging heat.

1. Open your manufacturer's battery app (Dell Power Manager, Lenovo Vantage, MyASUS, HP BIOS settings).
2. Enable a battery lifespan mode that caps charging at 80% or 60% — charging generates the most heat in the final 20%, so skipping it keeps things cooler. Our guide on [limiting battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) walks through every brand.
3. If your charger supports it, avoid "fast charge" modes in the BIOS — standard charging is gentler and cooler.
4. Charge the laptop while it is asleep or off when possible. A charging laptop that is also running is doing two heat-generating jobs at once.

### Fix 5: Verify the charger

The wrong charger makes the charging circuit work overtime.

1. Check the voltage and wattage printed on the charger and compare with the laptop's requirements on the bottom panel.
2. Never use a charger with the wrong voltage. Wattage should match or exceed the original — a 45W charger on a 90W laptop strains everything.
3. If the charger brick itself is burning hot (too hot to hold), replace it — that heat is wasted energy and a warning sign.
4. For USB-C laptops, use a quality PD charger rated for your laptop's wattage, not a phone charger.

### Fix 6: Update drivers and BIOS

Manufacturers regularly fix thermal and charging behavior in firmware updates.

1. Update the BIOS from the manufacturer's official support site: [Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en). Keep the charger plugged in during the flash.
2. Update chipset and thermal framework drivers from the same site.
3. Update the GPU driver — an old GPU driver can keep the discrete GPU awake and hot. Use [NVIDIA](https://www.nvidia.com/Download/index.aspx) directly for NVIDIA discrete GPUs.
4. After updating, monitor temperatures for a day. Free tools like HWMonitor can show you CPU and battery temps to confirm improvement.

### Fix 7: Service the cooling system

If the laptop is 3+ years old and still runs hot after all software fixes, the hardware needs attention.

1. Check fan behavior: if fans never spin up or make grinding noises, the fan may be dead — replacement is usually inexpensive.
2. Dried thermal paste is the classic cause of age-related overheating. Replacing it requires opening the laptop and removing the heatsink — doable with a guide for your model, or a repair shop can do it cheaply.
3. While inside, check the battery for swelling. A swollen battery presses against components, traps heat, and is a safety hazard — replace it immediately and do not charge the laptop until you do. See our [battery swelling safety guide](/articles/how-to-fix-battery-swelling-slightly-laptop-safe-in-windows-11-24h2/) for what to do next.
4. After servicing, run a stress test while charging and confirm temperatures stay in a sane range.

## Closing

Overheating while charging is rarely one thing — it is charging heat plus workload heat plus poor airflow, all stacking up. Fix the airflow, drop the maximum processor state to 95%, and cap charging at 80%, and most laptops go from alarming to merely warm. If it still burns after all that, the cooling hardware itself needs servicing.
