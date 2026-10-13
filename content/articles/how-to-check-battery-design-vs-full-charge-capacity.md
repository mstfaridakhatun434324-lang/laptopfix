---
title: "How to Read Design vs Full Charge Capacity in a Battery Report"
slug: how-to-check-battery-design-vs-full-charge-capacity
date: 2026-09-11
categories: ["battery"]
tags: ["battery health", "design capacity", "powercfg", "battery report"]
description: "Design capacity vs full charge capacity tells you exactly how worn your battery is. Learn how to check both and read the numbers."
thumbnail: "/images/thumbs/how-to-check-battery-design-vs-full-charge-capacity.webp"
faqs:
  - q: "What is battery design capacity?"
    a: "Design capacity is the charge your battery was built to hold when new, measured in milliwatt-hours (mWh). It's the factory baseline printed in the battery's firmware. Windows compares everything against this number to judge wear."
  - q: "What is full charge capacity?"
    a: "Full charge capacity is what your battery can actually hold right now when charged to 100 percent. It declines with age and use. The gap between design capacity and full charge capacity is your battery's wear, expressed as a percentage."
  - q: "How do I check both numbers in Windows?"
    a: "Run powercfg /batteryreport in an admin terminal, open the generated HTML file, and look under Installed batteries. Both Design Capacity and Full Charge Capacity are listed there side by side, along with cycle count."
  - q: "What percentage difference is normal?"
    a: "Under 20 percent difference (over 80 percent health) is normal for a battery in regular use. Twenty to 40 percent means noticeable aging — shorter runtime but still usable. Over 40 percent difference means the battery is heavily worn and replacement is worth considering."
---

Every battery-health question comes down to two numbers: what the battery was designed to hold, and what it holds now. The gap between them is the single most honest measurement of battery wear in Windows — more honest than any third-party "health percentage," because it's straight from the battery's own firmware rather than someone's estimate. Repair shops use these exact numbers to decide whether your battery is a warranty case. Here's how to find both numbers and what they mean.

## Why this happens

- **Windows buries the numbers:** Settings shows percentage and estimated time, not capacities — you need the battery report.
- **Third-party apps disagree:** Different apps compute "health" differently, causing confusion; the raw capacities don't lie.
- **Design capacity varies by unit:** Manufacturing tolerance means your battery's design capacity may differ slightly from the spec sheet.
- **Full charge capacity fluctuates:** Temperature and recent usage make it wobble a few percent day to day — trends matter more than single readings.
- **Misreading the gap:** People panic at a 15 percent gap that's perfectly normal, or ignore a 45 percent gap that explains everything.
- **Single-reading obsession:** One report after a hot day can read several points worse than reality — always compare against your own history, not a stranger's forum post.
- **Counterfeit batteries fake the baseline:** Cheap replacement batteries sometimes report an inflated design capacity, so the "health percentage" looks fine while actual runtime is terrible — runtime is the final judge.

## How to fix it

You can't change the numbers directly — but you can read them correctly and act on them.

### Fix 1: Generate the battery report

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run `powercfg /batteryreport` and note the output path.
3. Open the HTML file in your browser.
4. Under **Installed batteries**, read **Design Capacity** and **Full Charge Capacity** — both in mWh.

### Fix 2: Compute your battery health

1. Divide Full Charge Capacity by Design Capacity and multiply by 100.
2. Example: 38,000 ÷ 50,000 = 76 percent health, or 24 percent wear.
3. Over 80 percent: healthy. 60-80 percent: aging but serviceable. Under 60 percent: replacement territory.
4. Write the numbers down with today's date — you'll compare against this baseline later.

### Fix 3: Check the capacity history trend

1. In the same report, scroll to **Battery capacity history**.
2. Look at the Full Charge Capacity column over recent weeks — a steady gentle decline is normal aging.
3. A sudden cliff (large drop in one week) suggests a failing cell, not normal wear.
4. A flat line at a low value after months of decline means the wear has stabilized.

### Fix 4: Cross-check with the manufacturer's tool

1. **Dell:** Dell Power Manager > Battery Information shows health status.
2. **HP:** HP Support Assistant > Battery > Battery Check, or F2 diagnostics.
3. **Lenovo:** Vantage > Device > Power shows battery health and cycle count.
4. If the manufacturer's verdict disagrees wildly with your computed number, trust the raw capacities — apps sometimes use different baselines. Our [Dell unknown-health guide](/articles/how-to-fix-dell-battery-health-unknown-step-by-step/) covers what to do when Dell can't read the battery at all.

### Fix 5: Recalibrate if the numbers look wrong

1. A full charge capacity that jumps up and down between reports suggests gauge drift, not real capacity changes.
2. Run a calibration cycle: full charge, discharge to auto-shutdown, 3+ hour rest, uninterrupted recharge.
3. Regenerate the report — the full charge capacity should now be stable across readings.
4. Recalibrate every 3-6 months to keep the numbers honest. See our [calibration guide](/articles/how-to-fix-laptop-battery-calibration-not-working/) for the full procedure.

### Fix 6: Slow future capacity loss

1. Enable a charge limit (80 percent) in the manufacturer's app if you're mostly docked — this is the highest-impact habit for preserving full charge capacity.
2. Keep the laptop cool — heat is the fastest ager of full charge capacity, worse than cycling in many cases.
3. Avoid deep discharges below 10 percent regularly; shallow cycles between 20 and 80 percent stress cells the least.
4. If you store the laptop for weeks, leave it at around 50 percent charge in a cool place.
5. These habits don't recover lost capacity, but they flatten the decline curve going forward.

### Fix 7: Decide on replacement with data

1. Under 60 percent of design capacity with runtime that doesn't cover your day: replace.
2. Find your exact battery part number from the manufacturer's support app or the battery label.
3. Buy genuine — counterfeit batteries lie about their own design capacity, making this whole measurement meaningless.
4. After replacing, generate a new report to confirm the new battery's design capacity matches expectations.

### Fix 8: Keep a simple capacity log

1. Once a month, regenerate the battery report and jot down the date, full charge capacity, and cycle count in a notes app.
2. After three or four entries you'll see your personal decline rate — most people lose 1-3 percent of capacity per month with normal use.
3. A month where the number drops 8-10 percent is your early warning of a failing cell, months before symptoms appear.
4. Bring the log when buying a replacement or claiming warranty — dated numbers beat vague complaints every time.

### Fix 9: Sanity-check the design capacity itself

1. Look up your laptop's spec sheet (manufacturer's product page or the battery label inside the compartment) for the rated capacity in Wh.
2. Compare it with the report's Design Capacity — they should agree within about 5 percent.
3. If the report shows a design capacity far above the spec (say, 80,000 mWh on a battery rated 56Wh), you're looking at a counterfeit or mislabeled battery whose firmware lies about its own baseline.
4. In that case, every health percentage computed from these numbers is fiction — judge the battery by actual runtime, and replace it with a genuine part from the manufacturer. Genuine batteries are the only ones whose self-reported numbers you can trust.

## Closing

Design vs full charge capacity is the closest thing to a battery truth serum in Windows: two numbers, one division, and you know exactly where you stand. Check it every few months, watch the trend rather than any single reading, and let the data — not anxiety — drive the replacement decision. A battery at 75 percent of design still has years of useful life for light use; a battery at 50 percent is telling you it's time. Either way, you'll know — and knowing beats wondering every time you unplug.

Microsoft documents the battery report at the [Windows support hub](https://support.microsoft.com/en-us/windows). To see how cycle count fits into the picture, read [how to check battery cycle count on Windows 11 24H2](/articles/how-to-check-battery-cycle-count-in-windows-11-24h2/).
