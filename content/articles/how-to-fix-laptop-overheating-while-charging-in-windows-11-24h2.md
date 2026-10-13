---
title: "Laptop Overheating While Charging on Windows 11 (24H2)? How to Fix It"
slug: how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2
date: 2026-09-26
categories: ["battery"]
tags: ["overheating", "charging heat", "windows 11 24h2", "thermals", "battery health"]
description: "Laptop gets hot every time you plug in on Windows 11 24H2? Cool it down with these charging, power, and airflow fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2.webp"
faqs:
  - q: "Is it normal for a laptop to get warm while charging?"
    a: "Mild warmth is normal — charging is a chemical process that generates heat, and the charger brick gets warm too. What's not normal: the keyboard too hot to touch, fans screaming constantly, the underside burning your lap, or the machine throttling and slowing down while plugged in."
  - q: "Can charging overheat and damage my battery?"
    a: "Yes, sustained heat is the fastest way to kill a lithium battery. Every 10°C above room temperature roughly doubles the rate of capacity loss. A laptop that cooks its battery while charging will show degraded full charge capacity within months."
  - q: "Why does my laptop only overheat when plugged in, not on battery?"
    a: "On AC power, Windows switches to high-performance power plans, the CPU/GPU boost to higher clocks, background tasks run unrestricted, and the battery charges simultaneously — all generating heat at once. On battery, power limits keep everything cooler and slower."
  - q: "Should I remove the battery while using the laptop plugged in?"
    a: "On older laptops with removable batteries, yes — it keeps the battery cool. On modern sealed laptops you can't, so use the manufacturer's charge-limit feature (Lenovo Conservation Mode, HP Battery Health Manager) to reduce charging heat instead."
---

Plug in the charger and within twenty minutes the fans are roaring, the keyboard is uncomfortably warm, and the underside could double as a griddle. Unplug it and everything calms down. If your laptop only turns into a furnace on AC power, you're dealing with a specific, fixable interaction between charging heat, performance boosts, and airflow — not just "laptops run hot."

This matters beyond comfort. Heat while charging is the single fastest ager of laptop batteries. A machine that runs hot on the charger for months will show up later with a mysteriously degraded battery — and by then the damage is done. Fix the heat now, save the battery later.

## Why this happens

- **AC power unlocks full performance.** Plugged in, the CPU and GPU boost harder and longer, generating far more heat than on battery.
- **Charging itself generates heat.** Pushing current into lithium cells warms the battery, which sits right under the keyboard/palm rest on most laptops.
- **Background tasks go wild on AC.** Windows Update, indexing, OneDrive sync, and app updaters all run unrestricted when plugged in.
- **Blocked vents or dust-clogged fans.** A cooling system that copes on battery can't shed the extra AC heat load.
- **Dried-out thermal paste** on older machines — heat transfer from CPU to heatsink degrades over 3-5 years.
- **24H2 power plan behavior.** Feature updates can reset power plans to aggressive defaults or re-enable high-performance modes.
- **Charging a hot battery compounds the problem.** Using the laptop hard while charging means the battery absorbs ambient heat on top of its own charging heat.

## How to fix it

Work through these in order, from free and instant to deeper hardware fixes.

### Fix 1: Change what Windows does on AC power

The fastest win: stop the performance surge that comes with plugging in.

1. Go to **Settings → System → Power & battery** and set **Power mode** to **Balanced** or **Best power efficiency** — even on AC. You lose a little peak speed and gain a lot of cool.
2. Open **Control Panel → Hardware and Sound → Power Options → Change plan settings → Change advanced power settings**.
3. Expand **Processor power management → Maximum processor state**. Set **Plugged in** to **95%** instead of 100%. This tiny cut disables the hottest CPU turbo bins while costing almost no noticeable performance.
4. While you're there, check **System cooling policy → Plugged in** is set to **Active** (fans ramp before throttling).
5. If your workload allows, these settings alone can drop temperatures 10-15°C on AC.

### Fix 2: Stop the background stampede

Half the AC heat is Windows doing chores it postponed on battery.

1. Open **Task Manager → Processes**, click the **CPU** column, and watch for 5 minutes after plugging in. Common culprits: **Windows Update**, **Antimalware Service Executable** (Defender scan), **OneDrive**, **Search Indexer**.
2. Go to **Settings → Windows Update** and set **Active hours** to cover your work time, so updates install overnight instead of mid-afternoon.
3. Pause OneDrive sync while working: click the OneDrive cloud icon → **Pause syncing**.
4. In **Task Manager → Startup apps**, disable updaters and launchers you don't need (Adobe, game launchers, messaging apps).
5. Less background CPU = less heat = quieter fans. For battery-specific background hogs, see [how to find which app is draining battery](/articles/how-can-i-find-which-app-is-draining-battery/).

### Fix 3: Fix the physical airflow

No software setting overcomes a suffocated cooling system.

1. Always use the laptop on a **hard, flat surface**. Beds, couches, and laps block bottom intakes — this alone causes a shocking number of "overheating while charging" complaints.
2. Elevate the rear: a simple laptop stand or even two bottle caps under the back feet improves intake airflow measurably.
3. With the laptop off and cool, blow **short bursts of compressed air** through the exhaust vents to clear dust. Hold fans still with a toothpick if you can reach them — spinning them with air can damage bearings.
4. A **cooling pad** helps thin ultrabooks most, but even a passive aluminum stand drops temps a few degrees.
5. Keep the room reasonable — a laptop in a 35°C room starts 10°C hotter than in a 25°C room, and there's no setting for that.

### Fix 4: Separate heavy use from charging

Charging heat + workload heat stack. Don't make the battery absorb both.

1. If you're gaming or rendering, consider charging to 80-100% first, then unplugging for the heavy session (if battery allows), then plugging back in after.
2. Better: enable your maker's charge limit — **Lenovo Vantage → Conservation Mode**, **HP Battery Health Manager**, **MyASUS Battery Health Charging** — so the battery isn't cooking at 100% while you work. Our [overheating-while-charging companion guide](/articles/best-way-to-fix-laptop-overheating-while-charging/) covers charge-limit strategies in depth.
3. Avoid charging in hot cars, direct sunlight, or on top of blankets — obvious, but it happens constantly.

### Fix 5: Update BIOS, chipset, and fan control

Manufacturers tune fan curves and thermal behavior in firmware updates.

1. Install the latest **BIOS** from your maker's support site — changelogs mentioning "thermal," "fan curve," or "power" are directly relevant.
2. Update **chipset drivers** (Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) on Intel machines) — chipset drivers govern CPU power states.
3. Check for a maker utility with thermal profiles (**HP Command Center**, **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**) and try the **Quiet** or **Balanced** profile.
4. After updating, re-check Fix 1's power settings — BIOS updates love resetting them.

### Fix 6: Repaste or service aging thermals

For laptops 3+ years old, the thermal interface material is suspect.

1. Symptoms pointing here: sudden temperature rise over months, fans at max during light tasks, CPU hitting 95-100°C in Task Manager-adjacent monitoring tools.
2. **Repasting** (replacing thermal paste between CPU/GPU and heatsink) restores factory cooling — but it means full disassembly. If you've never opened a laptop, pay a shop; it's a 30-60 minute job for them.
3. While it's open, have them clean the fans and heatsink fins properly — compressed air from outside only does half the job.
4. Also ask them to check the battery's condition — months of heat may have degraded it. Run `powercfg /batteryreport` afterward to see the current full charge capacity.

### Fix 7: Rule out a failing battery

A damaged battery can generate abnormal heat while charging.

1. Run `powercfg /batteryreport` in admin Terminal and check **Full Charge Capacity** vs **Design Capacity**.
2. If the battery area (usually under the palm rest or keyboard) gets dramatically hotter than the CPU exhaust area, the battery itself may be the heat source.
3. Check for **swelling**: uneven keyboard, trackpad popping up, case not sitting flat. If you suspect swelling, stop charging immediately and see our [battery swelling guide](/articles/how-to-fix-laptop-battery-swelling-on-windows-10/).
4. A battery that heats abnormally during charging is a replacement candidate regardless of what the capacity numbers say.

## Closing

Overheating while charging is a stack of small heat sources — performance boost, background tasks, charging chemistry, and restricted airflow — adding up past what the cooling can handle. Peel them off one at a time: calm the power plan, quiet the background, fix the airflow. Your fans, your lap, and your battery's lifespan will all thank you.
