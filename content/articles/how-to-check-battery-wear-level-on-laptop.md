---
title: "How to Check Your Laptop's Battery Wear Level"
slug: how-to-check-battery-wear-level-on-laptop
date: 2026-10-13
categories: ["battery"]
tags: ["battery wear", "battery health", "capacity", "powercfg"]
description: "Want to know how worn your laptop battery really is? Here are the reliable ways to check battery wear level on any Windows laptop."
thumbnail: "/images/thumbs/how-to-check-battery-wear-level-on-laptop.webp"
faqs:
  - q: "How do I check battery wear level on Windows 11?"
    a: "Open an admin Command Prompt and run powercfg /batteryreport. In the generated HTML report, divide Full Charge Capacity by Design Capacity and multiply by 100 — that's your battery health percentage. Wear level is 100 minus that number. For example, 45,000 mWh full charge against 60,000 mWh design = 75% health, 25% wear."
  - q: "What is a good battery wear level?"
    a: "Under 10% wear is excellent (typical for batteries under a year old), 10-20% is normal for 1-3 years of use, 20-40% means noticeable runtime loss, and over 40% wear means the battery is significantly degraded. Most people start considering replacement around 30-40% wear."
  - q: "Do I need third-party software to check battery wear?"
    a: "No — Windows' built-in battery report gives you everything you need. Third-party tools just repackage the same data Windows already exposes. Stick with powercfg /batteryreport for the most trustworthy numbers."
  - q: "Why does Windows show battery health but not wear level directly?"
    a: "Windows exposes the raw numbers (design capacity and full charge capacity) rather than a computed wear percentage, partly because wear is an interpretation. The math is simple division, and doing it yourself from the battery report keeps you in control of what the numbers mean."
---
"How worn is my battery, really?" It's the question behind half of all battery complaints — is the runtime loss in your head, is it software, or has the battery genuinely degraded? The answer is a number, and Windows will give it to you for free.

Battery wear level is simply the gap between what your battery could hold when new and what it can hold now, expressed as a percentage. Here's how to measure it accurately and what the number means.

## Why this happens

- **Windows doesn't show wear directly.** The raw capacity numbers exist, but Windows never computes the wear percentage for you — you have to do one division.
- **Third-party tools disagree.** Different apps use different formulas and polling methods, so two tools can report different wear levels for the same battery — confusing everyone.
- **The gauge needs calibration to be accurate.** If the fuel gauge is miscalibrated, the full charge capacity reading (and thus your wear calculation) can be off.
- **Wear isn't linear.** Batteries lose capacity faster in their first year, then settle into a slower decline — a single wear number doesn't tell you the rate of change.
- **Design capacity can be misreported.** Rarely, firmware reports the wrong design capacity, making wear math meaningless until the BIOS is updated.
- **People confuse wear with drain.** High wear means a smaller tank; fast drain means a leak. They feel similar but have completely different fixes.

## How to fix it

Work through these in order — measure properly first.

### Fix 1: Generate a battery report

The authoritative source for wear numbers.

1. Open **Command Prompt as administrator** and run: `powercfg /batteryreport /output "C:\battery-report.html"`
2. Open the report and find the **Installed batteries** section.
3. Note the two numbers: **Design Capacity** and **Full Charge Capacity** (in mWh).

### Fix 2: Do the wear math

One division gives you the answer.

1. Calculate: **(Full Charge Capacity ÷ Design Capacity) × 100** = health percentage.
2. **Wear level = 100 − health percentage.** Example: 48,000 ÷ 60,000 = 80% health → 20% wear.
3. Interpret: **0–10%** wear is excellent, **10–20%** normal for 1–3 years, **20–30%** noticeable, **30–40%** replacement territory, **40%+** badly degraded.
4. For a deeper read on what these numbers imply, see our guide on [full charge capacity dropping](/articles/troubleshoot-full-charge-capacity-dropping/).

### Fix 3: Verify with the capacity history

One snapshot can mislead — check the trend.

1. In the same battery report, scroll to the **Battery capacity history** table.
2. Look at how full charge capacity changed over weeks and months — a **steady gradual decline** is normal aging; a **sudden cliff** suggests a failed cell or a bad calibration.
3. If the latest reading looks suspiciously low compared to the trend, calibrate before trusting it (next step).

### Fix 4: Calibrate before trusting the number

A confused gauge produces a wrong wear reading.

1. Run a full **calibration cycle**: charge to 100% (+2 hours plugged in), discharge to automatic shutoff, rest 5 hours unplugged, recharge to 100%.
2. Generate a **fresh battery report** and redo the math.
3. If wear dropped significantly after calibration, the earlier number was gauge error, not real wear.

### Fix 5: Cross-check with manufacturer tools

A second opinion from the people who made the laptop.

1. Check your maker's utility — **Dell Power Manager**, **Lenovo Vantage**, **MyASUS**, **HP** app — for its own health assessment.
2. On Dell, you can also check health in **BIOS setup** (**F2** at boot) or via **ePSA diagnostics** (**F12** at boot).
3. If the manufacturer's reading roughly matches your computed wear, you can trust the number.

### Fix 6: Compare against design vs. full charge properly

Avoid the common misreading.

1. Make sure you're comparing **Full Charge Capacity** (current maximum) against **Design Capacity** (factory maximum) — not against some other number in the report.
2. Ignore momentary readings from third-party widgets; use the battery report's settled numbers.
3. Our [design vs. full charge capacity guide](/articles/how-to-fix-design-capacity-vs-full-charge-capacity-in-windows-11-24h2/) explains every nuance of this comparison.

### Fix 7: Act on the number

Measurement without action is just trivia.

1. **Under 20% wear:** healthy — if runtime feels short, the problem is software drain, not wear. See our [fast-drain guide](/articles/best-way-to-fix-laptop-battery-drains-fast/).
2. **20–35% wear:** aging — adopt battery-friendly habits (80% charge cap, avoid heat) to slow further decline.
3. **Over 35–40% wear:** plan a replacement — no setting recovers lost chemistry, and runtime will keep shrinking.

## Closing

Checking wear level takes five minutes and answers the most important battery question there is: is this a software problem or a hardware problem? The battery report plus one division gives you a number you can trust — and the capacity history tells you whether it's getting worse fast or slow. Check it every few months; catching accelerating wear early gives you time to change habits or budget for a replacement instead of being surprised.

A practical way to use the number: write down your current wear percentage and the date somewhere you'll find it — a note on your phone works. Next time battery life feels shorter, check again and compare. If wear barely moved, the problem is software and worth troubleshooting; if it jumped several points, the battery aged a step and no settings tweak will bring those hours back. That single comparison saves you from the most common battery mistake: endlessly tuning software for a hardware problem. For the official background on battery reporting, Microsoft's [power documentation](https://support.microsoft.com/en-us/windows) has the details.

One more nuance: wear percentage and runtime don't scale perfectly together. A battery at 20% wear doesn't necessarily deliver exactly 80% of its original runtime, because voltage sag under load and the system's power management both shift as the battery ages. Use wear as your health gauge and actual timed runtime — the one-hour test from our drain guides — as your practical gauge. When both agree the battery is fading, you have a complete picture; when they disagree, trust the timed test for daily planning and the wear number for the replacement decision.
