---
title: "Laptop Battery Won't Hold a Charge? How to Fix It"
slug: how-to-fix-laptop-battery-won-t-hold-charge
date: 2026-09-23
categories: ["battery"]
tags: ["battery drain", "battery wear", "troubleshooting"]
description: "Laptop battery won't hold a charge? Diagnose whether it's wear, calibration, or background drain, then apply the fixes that actually restore runtime."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-won-t-hold-charge.webp"
faqs:
  - q: "Why won't my laptop battery hold a charge anymore?"
    a: "The most common reason is chemical wear — after hundreds of cycles, the cells physically store less energy. Other causes include a miscalibrated gauge (it drops from 40% to 0% instantly), excessive background drain, or a battery at end of life that can no longer accept a full charge."
  - q: "Can a battery that won't hold charge be fixed?"
    a: "Sometimes. If the problem is calibration or software drain, yes — a calibration cycle or taming background apps can restore apparent runtime. If the cells are chemically worn, nothing restores lost capacity; only replacement helps."
  - q: "How do I test if my battery is worn out?"
    a: "Run powercfg /batteryreport in an administrator Terminal and compare Full Charge Capacity to Design Capacity. Below 70–80% of design means significant wear. Also check the cycle count — over 500 cycles on most consumer batteries means a tired pack."
  - q: "Does leaving my laptop plugged in ruin the battery's ability to hold charge?"
    a: "It accelerates wear because heat and constant 100% charge stress lithium cells. Using a manufacturer charge limit (typically 80%) dramatically slows this. But a battery that already won't hold charge is worn — unplugging it now won't reverse the damage."
---

"Won't hold a charge" covers a few different miseries: the laptop dies 45 minutes after unplugging, the percentage plunges from 50% to dead in minutes, or it charges to 100% but the runtime is a fraction of what it used to be. The fix depends entirely on which of these you have — and the first job is figuring that out.

This guide separates the three root causes — worn cells, lying gauge, and parasitic drain — and gives you the right fix for each. Start with diagnosis; the wrong fix wastes time. If your battery is losing capacity steadily over months, also read our guide on [what to do when full charge capacity keeps dropping](/articles/what-to-do-if-full-charge-capacity-dropping/).

## Why this happens

- **Chemical aging of the cells.** Lithium-ion cells lose capacity with every cycle and with calendar age. This is irreversible and is the cause in most "won't hold charge" cases on laptops over two years old.
- **Miscalibrated fuel gauge.** The percentage readout drifts, so the laptop reports 60% when the true charge is 20% — then "suddenly" dies. The cells are fine; the meter is lying.
- **Excessive background power drain.** Windows background activity — indexing, updates, poorly behaved apps, USB devices left plugged in — can drain a battery far faster than normal.
- **High-performance power plans.** A laptop set to Best Performance with maximum brightness and discrete GPU always-on can halve its runtime versus balanced settings.
- **Battery at end of life.** Below a certain capacity threshold, the battery's own controller may refuse to deliver stable power, causing abrupt shutdowns even at moderate percentages.
- **Heat damage.** Sustained high temperatures — gaming on a bed, blocked vents — permanently reduce cell capacity faster than normal cycling.

## How to fix it

Work through these in order, starting with measurement so you fix the real cause.

### Fix 1: Measure the actual wear with a battery report

Never guess about wear — measure it in two minutes.

1. Open **Terminal** as administrator (**Win + X**, then **Terminal (Admin)**) and run `powercfg /batteryreport`.
2. Open the HTML report from the path shown and find **Design Capacity** versus **Full Charge Capacity**.
3. If full charge is **80%+ of design**, the cells are reasonably healthy — your problem is likely calibration or drain, not wear. Continue with the fixes below.
4. If it is **below 60–70%**, the battery is significantly worn. Software fixes will help only marginally; start planning a replacement. Our [wear-level troubleshooting guide](/articles/battery-wear-level-too-high-troubleshooting/) goes deeper on interpreting these numbers.

### Fix 2: Calibrate the gauge

If the battery dies "suddenly" from a middling percentage, the gauge is lying, not the cells.

1. Charge to 100% and leave plugged in for 30 minutes.
2. Go to **Settings > System > Power & battery** and set the battery-saver and sleep timeouts so the laptop stays awake on battery.
3. Unplug and use the laptop normally until it reaches **5%**, then plug in and charge uninterrupted to 100%.
4. Repeat once more if the first cycle does not stabilize the readings.
5. After calibration, the percentage should decline smoothly. If it still cliff-dives, the cells themselves are weak.

### Fix 3: Find and kill the power hogs

A healthy battery can look broken if something is draining it abnormally fast.

1. Open **Settings > System > Power & battery** and click **Battery usage** to see per-app consumption over the last 24 hours.
2. Uninstall or restrict background activity for the worst offenders (**Settings > Apps > Installed apps**, then per-app **Background apps permissions**).
3. Open **Task Manager** (**Ctrl + Shift + Esc**), sort by CPU, and look for processes pinned at high usage while idle.
4. Unplug USB peripherals, external drives, and dongles when on battery — each draws power.
5. Retest runtime on battery after cleaning house. If runtime roughly doubles, drain was your problem.

### Fix 4: Switch to a battery-friendly power setup

Squeeze the most from whatever capacity remains.

1. In **Settings > System > Power & battery**, set **Power mode** to **Best power efficiency** when on battery.
2. Lower screen brightness to 50–60% — the display is typically the biggest single drain.
3. Turn on **Battery saver** and set it to kick in at 30–40% instead of the default 20%.
4. In **Settings > Bluetooth & devices**, turn off Bluetooth when not in use.
5. If your laptop has a discrete GPU, use the manufacturer's control panel to force integrated graphics for everyday apps.

### Fix 5: Check for firmware and driver issues

Outdated power management firmware can mismanage the battery.

1. Visit your manufacturer's support site and install the latest **BIOS** and **chipset** drivers for your exact model.
2. In **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, choose **Uninstall device**, then **Action > Scan for hardware changes** to get a fresh driver.
3. Run Windows Update (**Settings > Windows Update**) and install all pending updates — Microsoft periodically ships battery-management fixes.
4. Retest: charge fully, unplug, and time how long the laptop lasts doing light work. Microsoft's [Windows battery support pages](https://support.microsoft.com/en-us/windows) cover additional power-tuning options.

### Fix 6: Rule out a swelling or damaged battery

A battery that will not hold charge and shows physical symptoms needs immediate attention.

1. Power off and inspect the bottom panel — any bulging, unevenness, or gaps mean a swollen cell.
2. Check for a spongy keyboard, a trackpad that clicks differently, or a case that rocks on a flat table.
3. If you see swelling, stop using the battery: shut down, unplug, and do not puncture or press on the swollen area.
4. Take it to a professional for replacement and recycle the old battery properly. Swollen batteries are a fire risk — this is not a DIY-first situation.

### Fix 7: Replace the battery when wear is confirmed

When the report shows heavy wear, replacement is the honest fix.

1. Confirm the diagnosis: full charge capacity well below design, high cycle count, and poor runtime even after calibration and drain cleanup.
2. Buy a battery matching the exact part number on the old battery's label, from the manufacturer or a reputable seller.
3. After installing, run one full calibration cycle so Windows learns the new capacity.
4. To make the new battery last, enable the manufacturer's charge limit for desk use — see our guide on [limiting charge to 80%](/articles/how-to-limit-battery-charge-to-80/).

## Closing

A battery that will not hold a charge is telling you something specific — you just have to listen in the right order. Measure the wear first, because that determines whether you are fixing or replacing. Calibrate second, because a lying gauge mimics a dying battery perfectly. Tame the drain third, because software waste is free to fix. And when the report confirms the cells are simply worn out, replace the battery without guilt: you got every usable cycle out of it, and a fresh pack will make the laptop feel years younger.
