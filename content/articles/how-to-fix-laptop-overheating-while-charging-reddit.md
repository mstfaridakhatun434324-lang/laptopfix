---
title: "How to Fix a Laptop Overheating While Charging"
slug: how-to-fix-laptop-overheating-while-charging-reddit
date: 2026-09-19
categories: ["battery"]
tags: ["laptop overheating while charging", "laptop hot when plugged in", "charging heat fix"]
description: "Laptop gets scorching hot every time you plug in the charger? Separate normal charging warmth from real problems and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-overheating-while-charging-reddit.webp"
faqs:
  - q: "Is it normal for a laptop to get hot while charging?"
    a: "Some warmth is normal — charging is an exothermic chemical process, and the charger itself gets warm too. It becomes abnormal when the laptop is too hot to touch comfortably, the fans scream constantly at idle, or the heat is dramatically worse than it used to be. New, sudden heat deserves investigation."
  - q: "Why does my laptop only overheat when the charger is plugged in?"
    a: "Plugging in switches the laptop to its high-performance power plan, enables CPU turbo boost, and starts the chemically warm charging process all at once. If cooling is marginal — dust, blocked vents, dried thermal paste — the extra heat from charging pushes it over the edge."
  - q: "Should I use my laptop while it's charging?"
    a: "Yes, that's fine and normal — laptops are designed for it. Just avoid the maximum-heat combo: heavy gaming or video rendering while fast-charging on a soft surface in a warm room. For light work, using it while charging causes no harm."
  - q: "Can a faulty charger make my laptop overheat?"
    a: "Yes. A failing or incorrect charger can deliver unstable voltage, forcing the charging circuit to work harder and run hotter. If the charger brick itself is abnormally hot, or the heat started with a new third-party charger, test with the original adapter."
---

Plug in the charger and within twenty minutes the laptop is radiating heat like a space heater. Unplug it, and it cools right back down. That pattern — hot only while charging — narrows the suspects considerably, and most of them are fixable without opening the machine.

Charging adds heat from two directions: the battery chemistry itself warms up as it accepts current, and Windows switches to a more aggressive performance profile on AC power. When cooling can't keep up with both, you feel it. Here's how to bring temperatures back under control.

## Why this happens

- **AC power unlocks full performance.** On battery, Windows throttles the CPU; plugged in, turbo boost kicks in and heat output can double — right when charging adds its own warmth.
- **Charging is exothermic.** Pushing current into lithium cells generates heat, and fast charging generates proportionally more. A 0–100% fast charge is the hottest thing a battery normally does.
- **Vents are blocked or dusty.** Charging heat plus trapped heat is the classic combo — the cooling system was already marginal, and charging pushed it past the limit.
- **Heavy use while charging stacks the load.** Gaming or rendering while fast-charging means the CPU, GPU, and battery are all at maximum heat simultaneously.
- **The charger is wrong or failing.** An incorrect-wattage or dying adapter makes the power circuitry work overtime, generating excess heat in the charging path.
- **The battery is aging.** Worn cells have higher internal resistance, so more of the charging energy becomes waste heat instead of stored charge.

## How to fix it

Work through these in order — the first three handle the vast majority of cases.

### Fix 1: Break the heat-stacking habit

1. While charging, avoid maximum-load tasks (gaming, 4K export, compiling) — or at least pause them until the battery passes 80%, when charge current and heat taper off.
2. Always charge on a hard, flat surface with the vents clear — never on a bed or couch.
3. If the room is warm, charge near airflow: a fan pointed at the laptop's intake side makes a real difference.
4. Don't charge in direct sunlight or in a hot car — ambient heat leaves the cooling system no margin.
5. Consider charging to 80% for daily use (via your maker's battery utility) and only going to 100% when you need the runtime — the last 20% is the hottest part of the charge. Our [charge-limit guide](/articles/how-to-limit-battery-charge-to-80/) explains the setup.

### Fix 2: Clean the cooling system

1. Shut down and unplug, then blast the intake and exhaust vents with short bursts of compressed air (can upright, straw nozzle).
2. Check that all fans actually spin — put your hand near exhausts during a heavy task; no airflow from one side means a dead fan.
3. If the laptop is a few years old and the heat built up gradually, the internal heatsink fins are likely matted with dust — a shop cleaning is inexpensive and transformative.
4. For older machines, dried thermal paste is a prime suspect; repasting is a service-center job for most people but fixes chronic overheating properly.
5. After cleaning, verify improvement under the same charging conditions as before.

### Fix 3: Tame the plugged-in power plan

1. Open **Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **Processor power management > Maximum processor state** and set **Plugged in** to **95–99%** — this disables turbo boost's hottest edge while costing almost nothing in real tasks.
3. Expand **System cooling policy** and set **Plugged in** to **Active** so fans respond aggressively.
4. In **Settings > System > Power & battery**, try the **Balanced** power mode instead of **Best performance** for daily plugged-in use.
5. Restart and test: charge from ~30% while doing your normal work and note the temperature difference.

### Fix 4: Verify the charger

1. Check the wattage on the adapter label against your model's requirement — especially after any charger replacement.
2. Feel the charger brick itself: warm is normal, too-hot-to-hold is not, and suggests the adapter is failing or undersized.
3. Inspect the cable and connector for damage, and the laptop's port for looseness or debris.
4. If you're using a USB-C charger, confirm it's a proper PD charger at your laptop's rated wattage — phone chargers and weak hubs cause the charging circuit to struggle.
5. Test with the original manufacturer charger for a full cycle; if the heat disappears, the third-party adapter was the problem. Gaming-laptop owners should read our [charger wattage guide](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/).

### Fix 5: Check what's running while you charge

1. Open **Task Manager** (**Ctrl + Shift + Esc**) and sort by CPU — kill anything pegged that shouldn't be (stuck updaters, runaway browser tabs).
2. Check **Settings > Windows Update** — updates downloading in the background while you charge are a legitimate but temporary furnace.
3. Look at **Settings > System > Power & battery > Battery usage** for apps with heavy background drain.
4. Disable unnecessary startup items in **Task Manager > Startup apps**.
5. If a specific app always coincides with the heat, check for an update or an alternative — some apps are just thermally expensive.

### Fix 6: Update firmware and drivers

1. Install the latest **BIOS** from your maker's support page — thermal tables and charge-rate logic live in firmware, and makers revise them.
2. Update chipset drivers (or use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) on Intel machines).
3. Update the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — a GPU that won't sleep properly adds constant heat.
4. Run **Windows Update** fully; power-management regressions in specific builds are real and get fixed.
5. After updates, re-verify your Fix 3 power-plan tweaks — updates sometimes reset them.

### Fix 7: Evaluate the battery itself

1. Generate a battery report: `powercfg /batteryreport /output "C:\battery-report.html"` in an elevated terminal.
2. If **Full Charge Capacity** is far below **Design Capacity** and the battery area is the hottest part of the chassis, the cells' rising internal resistance is turning charge current into heat.
3. Check for swelling — a bulging bottom panel alongside heat means replace immediately, not eventually.
4. If the battery is worn, follow our [battery replacement guide](/articles/how-to-fix-laptop-battery-won-t-hold-charge-youtube/) — a fresh battery charges cooler.
5. Until replaced, limit charge to 80% and avoid heavy use while charging to keep temperatures in a safer range.

## Closing

Overheating while charging is heat stacking: charging warmth plus AC-performance heat plus whatever was already marginal about your cooling. Break the stack — charge on hard surfaces, cap the plugged-in processor state, clean the vents, verify the charger — and temperatures drop back to sane levels. If the battery itself has become the furnace, though, that's the cells telling you they're done; listen to them.
