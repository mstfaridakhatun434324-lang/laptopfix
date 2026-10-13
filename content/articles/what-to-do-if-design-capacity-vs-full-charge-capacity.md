---
title: "What to Do If Full Charge Capacity Is Below Design Capacity"
slug: what-to-do-if-design-capacity-vs-full-charge-capacity
date: 2026-09-12
categories: ["battery"]
tags: ["design capacity", "full charge capacity", "battery report"]
description: "Confused by design capacity vs full charge capacity in your battery report? Learn what each number means and what to do about the gap."
thumbnail: "/images/thumbs/what-to-do-if-design-capacity-vs-full-charge-capacity.webp"
faqs:
  - q: "What is design capacity?"
    a: "Design capacity is the charge your battery was built to hold when new, measured in milliwatt-hours (mWh). It's a fixed factory specification printed in the battery report — it never changes."
  - q: "What is full charge capacity?"
    a: "Full charge capacity is what your battery can actually hold right now, also in mWh. It declines over time as the cells age, and Windows updates it as the battery controller re-estimates."
  - q: "How big a gap is normal?"
    a: "A gap under 20% (health above 80%) is normal for a battery with moderate use. Gaps of 20–40% mean noticeable wear; above 40% usually means short runtime and replacement is worth considering."
  - q: "Can the gap shrink again?"
    a: "Sometimes. If the gap is exaggerated by a miscalibrated gauge, a full calibration cycle can restore the reported full charge capacity. True chemical wear never reverses, though."
---

Open any Windows battery report and the two numbers jump out: DESIGN CAPACITY and FULL CHARGE CAPACITY. They're the single most useful pair of figures for understanding your battery — and the most misunderstood. People see a gap and panic, or see a small gap and assume everything's fine while the battery dies in two hours.

This guide explains what each number actually measures, how to compute your real battery health, and what to do at every level of the gap. Once you understand these two values, every other battery metric starts making sense too.

## Why this happens

- **Chemical aging:** lithium-ion cells lose capacity with every charge cycle — the gap is the physical record of that loss.
- **Heat damage:** high temperatures permanently reduce what the cells can hold.
- **Calendar aging:** time alone widens the gap, even on lightly used batteries.
- **Gauge miscalibration:** the controller's estimate of full charge capacity drifts, making the gap look bigger (or smaller) than reality.
- **Cell failure:** one dead cell in the pack creates a sudden, large gap.
- **Firmware misreporting:** buggy BIOS versions sometimes report wrong capacity values.
- **Third-party batteries:** replacement packs may report a design capacity that doesn't match the original spec.

## How to fix it

You can't close a genuine gap, but you can verify it's real and stop it widening.

### Fix 1: Generate the report and find the numbers

Get the authoritative figures first.

1. Right-click **Start**, open **Terminal (Admin)**, and run `powercfg /batteryreport /output "C:\battery-report.html"`.
2. Open the file in a browser and scroll to **Installed batteries**.
3. Write down **DESIGN CAPACITY** and **FULL CHARGE CAPACITY** (both in mWh).
4. Compute health: full charge ÷ design × 100. Compute the gap: 100 − health.
5. Note the **CYCLE COUNT** too — it tells you how hard the battery's life has been.

### Fix 2: Interpret the gap correctly

The number only matters with context.

1. **Gap under 20%:** healthy. Normal aging; no action needed beyond good habits.
2. **Gap 20–40%:** moderate wear. Runtime is noticeably shorter; enable charge limiters to slow further loss.
3. **Gap over 40%:** heavy wear. Replacement is usually the sensible move if runtime matters to you.
4. Cross-check with **Battery capacity history** in the same report: a smooth slope confirms gradual aging, while a sudden drop suggests cell failure or a reporting glitch.
5. Remember the gap is relative — a 30% gap on a huge 90Wh battery still leaves more runtime than a 10% gap on a tiny 35Wh one.

### Fix 3: Calibrate to verify the gap is real

Miscalibration exaggerates gaps all the time.

1. Charge to 100% and leave plugged in for two hours.
2. Drain the laptop until it shuts off by itself.
3. Leave it off for five hours, then charge uninterrupted to 100%.
4. Generate a fresh report and recompute. The full charge capacity often rises after calibration, shrinking the apparent gap.
5. If the gap barely moves, it's genuine wear — proceed to the protective steps below.
6. Detailed method: [how to calibrate your laptop battery on Windows 11](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 4: Slow further widening with a charge cap

You can't reverse wear, but 80% caps dramatically slow it.

1. Enable your manufacturer's limiter: **Lenovo Vantage** conservation mode, **MyASUS** Battery Health Charging, **Dell Power Manager**, **HP Battery Health Manager** (BIOS), or **Acer Care Center**.
2. Set the cap to 80% (or 60% for always-docked machines).
3. The general guide: [how to limit battery charge to 80 percent](/articles/how-to-limit-battery-charge-to-80/).
4. Re-measure monthly — the capacity history slope should flatten visibly.

### Fix 5: Reduce heat exposure

Heat widens the gap faster than anything except cycling.

1. Keep vents clear and use hard surfaces; clean dust with compressed air.
2. Avoid heavy workloads on battery — high discharge rates heat the cells from inside.
3. Don't store or use the laptop in hot environments.
4. In **Settings > System > Power & battery**, use **Best power efficiency** mode for routine work.
5. On gaming laptops, cap frame rates and use balanced performance profiles instead of max-turbo modes.

### Fix 6: Update the BIOS

Faulty firmware can misreport both numbers.

1. Check your manufacturer's support site for a BIOS update ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Install with the charger connected and don't interrupt it.
3. Generate a new report afterward — corrected firmware sometimes revises the full charge capacity upward.
4. If the numbers change dramatically after a BIOS update, the old gap was partly fiction.

### Fix 7: Decide about replacement

When the verified gap is large and runtime is poor, it's decision time.

1. Under 60% health with a genuine (calibrated) gap: replacement is the practical fix.
2. Check if the battery is user-replaceable or needs service.
3. Buy genuine or manufacturer-certified packs — accurate capacity reporting depends on a proper fuel-gauge chip.
4. After installing the new battery, generate a report: design capacity should match the spec sheet, and the gap should be near zero.
5. Enable the charge cap on day one to keep the new battery's gap small for years.
6. Keep the old report files — comparing the new battery's first report against the old one shows exactly what the replacement bought you.

### Fix 8: Watch the trend, not just the snapshot

A single report is a photograph; repeated reports are a film.

1. Save each battery report with the date in the filename, e.g. `battery-report-2026-09.html`.
2. Compare full charge capacity month to month. A loss of 1–2% per month under normal use is typical; faster loss deserves investigation.
3. If the gap jumps suddenly between two reports, think about what changed: a heat wave, a new game, a BIOS update, or a long period at 100%.
4. Trending data also helps warranty claims — "it dropped 25% in three months" is far more persuasive than a single number.

## Closing

Design capacity is what you bought; full charge capacity is what you have. Measure both with powercfg, calibrate before trusting the gap, and then either protect what's left or replace what's gone — the numbers will tell you which. Revisit the report every few months to watch the trend.
