---
title: "Design Capacity vs Full Charge Capacity: How to Check"
slug: how-can-i-check-battery-design-vs-full-charge-capacity
date: 2026-10-12
categories: ["battery"]
tags: ["design capacity", "battery health", "powercfg"]
description: "What do design capacity and full charge capacity actually mean? Learn to check both, compute your battery health, and read the numbers right."
thumbnail: "/images/thumbs/how-can-i-check-battery-design-vs-full-charge-capacity.webp"
faqs:
  - q: "What is the difference between design capacity and full charge capacity?"
    a: "Design capacity is the energy the battery was built to hold when new, set by the manufacturer. Full charge capacity is what it can actually hold now. The gap between them is wear. Divide full charge by design to get your battery health percentage."
  - q: "What is a good full charge capacity percentage?"
    a: "Above 80% of design capacity is healthy. Between 60 and 80% is normal aging on a laptop over two years old. Below 60%, you'll feel the runtime loss clearly, and below 50% a replacement is usually worth it if you use the laptop on battery often."
  - q: "Why is my full charge capacity higher than design capacity?"
    a: "This happens occasionally and is harmless — it means the battery shipped slightly above spec or the gauge is estimating generously. It's not an error to fix. Only worry when full charge capacity is significantly below design."
  - q: "Does full charge capacity change after calibration?"
    a: "It can shift by a few percent as the gauge re-learns the true endpoints. Calibration doesn't change the physical cells, but it corrects the controller's estimate. A small upward correction after calibration means the gauge was under-reporting, not that the battery healed."
---
Two numbers tell you everything about your battery's condition: what it was designed to hold, and what it holds now. Windows tracks both, but buries them in a report most people never open. Once you know where to look and how to read them, battery health stops being a mystery.

This guide shows you how to pull both numbers, compute your real battery health, and interpret what the result means for your laptop's future.

It takes about two minutes total, and the skill transfers everywhere: the same two numbers are what technicians, warranty desks, and repair shops ask for. Learn to read them once and you'll never be at anyone's mercy on battery questions again.

## Why this happens

- **No health dashboard in Windows:** Settings shows percentage and estimated time, but never the underlying capacity numbers. The data exists — it's just hidden.
- **Percentage lies by omission:** 100% charge means 100% of *current* capacity. On a worn battery, that's a fraction of the original energy.
- **Gradual wear is invisible:** Losing 2% a month doesn't register day to day, but the report's numbers make the trend undeniable.
- **Warranty claims need numbers:** "Battery dies fast" gets you nowhere with support. "Full charge capacity is 41% of design at 200 cycles" gets a replacement.
- **Misleading third-party apps:** Many "battery health" apps estimate crudely or show alarming numbers to sell premium features. The Windows report is the ground truth.

## How to fix it

Work through these in order — generate the numbers, compute health, then interpret and act.

### Fix 1: Generate the battery report

One command produces the whole picture.

1. Right-click **Start** and choose **Terminal (Admin)**.
2. Run `powercfg /batteryreport /output %USERPROFILE%\Desktop\battery.html`.
3. Open **battery.html** from your Desktop in any browser.
4. Scroll to the **Installed Batteries** section — both capacity numbers live there.

### Fix 2: Find the two capacity numbers

Know exactly what you're reading.

1. **DESIGN CAPACITY** is listed in milliwatt-hours (mWh) — e.g., 52,000 mWh. This never changes; it's the factory spec.
2. **FULL CHARGE CAPACITY** is right below it — e.g., 44,000 mWh. This is the controller's current estimate of what a full charge holds.
3. Note **CYCLE COUNT** too — it tells you how much use produced the wear you're seeing.
4. If the numbers look wildly wrong (like 0 mWh), the battery may not be detected properly — see our [battery detection fix](/articles/how-to-fix-battery-not-detected-on-laptop-step-by-step/).

### Fix 3: Compute your battery health percentage

Simple arithmetic, honest answer.

1. Divide full charge capacity by design capacity: 44,000 ÷ 52,000 = 0.846.
2. Multiply by 100: **84.6% health**.
3. 90–100%: excellent. 80–90%: good, normal for a year or two of use. 60–80%: aging, plan ahead. Below 60%: replacement territory.
4. Compare against cycle count: 85% health at 400 cycles is normal; 60% health at 100 cycles suggests a defective pack.

### Fix 4: Check the trend with an older report

One reading is a snapshot; two readings are a story.

1. If you have an older battery report, compare its full charge capacity to today's.
2. A drop of more than 10% in three months is faster than normal aging — look for heat or constant-100% charging as causes.
3. No old report? Generate one now and set a calendar reminder for three months out. Future you will be grateful.
4. Our [Windows 11 battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) shows how to archive reports for trend tracking.

### Fix 5: Recalibrate if the numbers look suspicious

A sudden capacity drop is often the gauge, not the cells.

1. If full charge capacity fell 15%+ in a single month with no change in habits, suspect gauge drift.
2. Run a full calibration: charge to 100% + 2-hour soak, discharge to hibernation, rest powered off for hours, recharge uninterrupted.
3. Regenerate the report. A partial recovery means the gauge was wrong.
4. No recovery after a clean calibration means the loss is real chemical wear.

### Fix 6: Slow further loss with a charge limit

You can't reverse wear, but you can brake hard.

1. Open your manufacturer's app (**Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **HP BIOS settings**).
2. Enable the charge limit / Conservation Mode at 60–80%.
3. This is the single most effective habit change for a desk-bound laptop.
4. Keep the battery cool during heavy work — heat accelerates the chemistry behind every lost milliwatt-hour.
5. For the full playbook on slowing decline, see our [capacity decline guide](/articles/how-to-fix-full-charge-capacity-dropping-in-windows-11-24h2/).

### Fix 7: Decide on replacement with real math

Let the numbers make the call.

1. Below 60% health: replacement makes sense if you regularly work unplugged.
2. Below 50%: even desk users benefit, since a weak battery can't handle power spikes and the laptop may throttle.
3. Check warranty first — many manufacturers cover batteries under 80% health within the first year.
4. The [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) has guidance on battery service options.

### Fix 8: Understand what the numbers can't tell you

Capacity numbers are honest, but they're not the whole battery story.

1. The report doesn't measure **internal resistance** — a battery can show decent capacity but still collapse under heavy load (gaming, compiling) because worn cells can't deliver current fast enough.
2. It also doesn't show **temperature history**. A battery baked at high temps for a year will keep degrading faster than its current numbers suggest.
3. If runtime is bad despite 80%+ health, the problem is drain, not capacity — check what's consuming power with `powercfg /energy` or the per-app usage in **Settings > System > Power & battery**.
4. Use capacity as the long-term health signal and real-world runtime as the day-to-day signal. When both agree the battery is done, believe them.

## Closing

Design capacity is the promise; full charge capacity is the reality. Check both with one command, do the division, and you know exactly where your battery stands — no apps, no guesswork, no surprises.
