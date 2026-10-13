---
title: "What to Do When Your Laptop Battery Won’t Hold a Charge"
slug: what-to-do-if-laptop-battery-won-t-hold-charge
date: 2026-09-13
categories: ["battery"]
tags: ["battery won't hold charge", "laptop battery dies fast", "battery drains quickly"]
description: "Laptop battery dies minutes after unplugging? Diagnose whether it's wear, calibration, or a power hog — and fix it with these steps."
thumbnail: "/images/thumbs/what-to-do-if-laptop-battery-won-t-hold-charge.webp"
faqs:
  - q: "Why won't my laptop battery hold a charge anymore?"
    a: "Most commonly, the cells are worn out — lithium batteries lose capacity with every cycle, and after 2–4 years many hold far less than their rated capacity. Other causes include a miscalibrated gauge, a background app burning power, or a failing charging circuit."
  - q: "How do I know if the battery is worn out or just miscalibrated?"
    a: "Run powercfg /batteryreport and compare Full Charge Capacity to Design Capacity. If full charge is under 70% of design, it's wear — no calibration will restore lost chemistry. If capacity looks healthy but runtime is short, it's calibration or a power drain."
  - q: "Can a battery that won't hold charge be repaired?"
    a: "No — individual lithium cells can't be economically refurbished in a laptop pack, and opening packs is dangerous. Calibration can fix reporting errors that mimic a dead battery, but genuinely worn cells only get fixed by replacement."
  - q: "How long should a laptop battery last?"
    a: "Typically 2–4 years or 300–500 full cycles before capacity drops noticeably. Heavy heat, constant 100% charging, and deep discharges shorten that. With good habits — like an 80% charge cap — many packs stay useful for 4–5 years."
---
Unplug, and the battery plummets. Twenty minutes later you're hunting for an outlet like it's 2009. A battery that won't hold a charge is the most common laptop battery complaint there is — and the fix depends entirely on whether the problem is worn-out chemistry, a lying fuel gauge, or something secretly guzzling power in the background.

This guide helps you tell those three apart, because each has a completely different solution.

## Why this happens

- **Natural cell degradation:** Every charge cycle permanently reduces lithium capacity. After a few hundred cycles, "won't hold a charge" is just chemistry.
- **Miscalibrated fuel gauge:** The gauge thinks the battery is emptier than it is and shuts the laptop down early — the cells may be fine.
- **Background power hogs:** An app burning CPU or keeping the disk awake can drain a healthy battery in an hour.
- **Heat damage:** Sustained high temperatures (gaming on a bed, blocked vents) permanently reduce capacity faster than normal cycling.
- **Failing charging circuit:** Rare, but a bad charging IC can undercharge the pack, so it never actually fills up despite showing 100%.

## How to fix it

Work through these in order — diagnose before you spend money.

### Fix 1: Run a battery report and read the real capacity

This is the fork in the road: wear versus everything else.

1. Open an elevated **Command Prompt** and run `powercfg /batteryreport`.
2. Open the HTML report and compare **Design Capacity** to **Full Charge Capacity**.
3. Divide full charge by design: above 80% is healthy, 60–80% is worn but usable, below 60% is a replacement candidate.
4. Check **Cycle Count** too — several hundred cycles with low capacity is normal aging.

If capacity is healthy but runtime is terrible, skip to Fix 3 — your problem is consumption, not the battery. Our full [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains every section of this report.

### Fix 2: Calibrate the fuel gauge

If the report shows decent capacity but the laptop dies "early," the gauge is lying.

1. Charge to 100% and leave plugged in for 2 hours.
2. Unplug and use normally until it shuts itself off.
3. Leave it off and unplugged overnight.
4. Charge uninterrupted to full without using it.
5. Test runtime on battery again.

Calibration fixes the "dies at 30%" phenomenon where the gauge's empty point has drifted. It cannot restore worn chemistry — but it stops the laptop from shutting down with usable charge still in the pack. Details in our [calibration walkthrough](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 3: Find and kill the power hogs

A healthy battery drained by a rogue app looks exactly like a dead battery.

1. Go to **Settings** > **System** > **Power & battery** and expand **Battery usage**.
2. Sort by usage and look for anything unexpected burning double-digit percentages — browsers with dozens of tabs, updaters stuck in loops, and crypto miners (malware) are the usual suspects.
3. Open **Task Manager** (**Ctrl + Shift + Esc**), sort by **CPU**, and kill or uninstall the offenders.
4. In **Settings** > **Apps**, disable **Let this app run in background** for apps you don't need.

One stuck updater can halve your runtime. Our dedicated guide to [finding which app is draining your battery](/articles/best-way-to-find-which-app-is-draining-battery/) goes deeper into the detective work.

### Fix 4: Reduce the load the battery has to carry

Even without a single culprit, trimming consumption extends what the remaining capacity can do.

1. Lower screen brightness to 50–60% — the display is the biggest single drain.
2. Turn off keyboard backlighting when you don't need it.
3. Disable Bluetooth and Wi-Fi when working offline.
4. Set the power mode to **Best power efficiency** in **Settings** > **System** > **Power & battery**.
5. Close unused browser tabs and desktop apps — each one costs watts.

These tweaks can add 30–60 minutes to a worn battery's runtime. Not a fix for dead cells, but meaningful relief while you decide on replacement.

### Fix 5: Reset the ACPI battery driver

A corrupted driver can misreport both capacity and drain rate.

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
3. Shut down fully, unplug for 30 seconds, plug back in, and power on.
4. Re-run your battery report after a full charge cycle to confirm sane readings.

If the driver was feeding Windows bad data, capacity and runtime estimates should now make sense. Microsoft covers driver basics on their [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Check for heat damage and improve cooling

Heat-damaged batteries lose capacity permanently, but you can stop further damage.

1. Feel the laptop's underside during use — uncomfortably hot to the touch suggests cooling problems.
2. Clean the vents with compressed air; check that fans spin up under load.
3. Use the laptop on hard surfaces, not beds or couches that block intakes.
4. Consider a cooling pad if you regularly do heavy work.

You can't reverse heat damage, but stopping it now preserves whatever capacity remains. If the battery is swollen from heat, stop using it and replace it — swelling is a safety issue.

### Fix 7: Replace the battery

When the report shows severe wear, replacement is the honest fix.

1. Confirm wear with the report: full charge capacity below 60–70% of design, high cycle count.
2. Buy a genuine or high-quality replacement for your exact model — cheap packs often have inflated capacity claims and poor safety circuits.
3. For removable batteries, swap it yourself. For sealed laptops, use the manufacturer's service or a reputable shop.
4. After installing, run one full calibration cycle so the gauge learns the new pack.

A fresh battery in an otherwise healthy laptop feels like a new machine. And this time, set an [80% charge limit](/articles/best-way-to-limit-battery-charge-to-80-percent/) from day one to make it last longer.

## Closing

"Won't hold a charge" has three distinct causes — worn cells, a lying gauge, or a hidden power hog — and the battery report tells you which one you're dealing with in two minutes. Calibrate what can be calibrated, kill what's draining, and replace what's genuinely worn. Guessing without the report is how people buy new batteries for what was actually a stuck Windows updater.
