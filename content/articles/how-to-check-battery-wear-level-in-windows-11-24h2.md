---
title: "How to Check Your Laptop's Battery Wear Level in Windows 11"
slug: how-to-check-battery-wear-level-in-windows-11-24h2
date: 2026-09-03
categories: ["battery"]
tags: ["battery health", "battery wear", "windows 11"]
description: "Wondering how worn your laptop battery is? Here's how to check battery wear level in Windows 11 24H2 using the built-in battery report."
thumbnail: "/images/thumbs/how-to-check-battery-wear-level-in-windows-11-24h2.webp"
faqs:
  - q: "What is battery wear level?"
    a: "Battery wear is the percentage of original capacity your battery has lost. If your battery was designed for 60,000 mWh and now fully charges to 48,000 mWh, wear is 20%. Windows shows both numbers in the battery report — you just do the subtraction."
  - q: "What wear level means I need a new battery?"
    a: "Under 20% wear is normal for a battery 1–2 years old. At 30–40% wear you'll notice shorter runtime. Past 40–50% wear, most people find the battery impractical and replacement makes sense. Sudden jumps in wear can indicate a failing cell."
  - q: "Is the battery report accurate?"
    a: "It's accurate enough for wear assessment. The numbers come from the battery's own fuel-gauge chip. For the most reliable reading, calibrate first: charge to 100%, drain to shutdown, then recharge fully before generating the report."
  - q: "Does Windows 11 24H2 show battery health in Settings?"
    a: "Windows 11 shows battery level and estimated runtime in Settings → System → Power & battery, but not a wear percentage. The detailed wear data lives in the powercfg battery report, which works the same in 24H2 as in earlier builds."
---

Every lithium battery wears down a little with each charge cycle — that's just chemistry. But "my battery doesn't last like it used to" is vague, and vague doesn't help you decide whether to change your habits or buy a replacement. What you need is a number: your battery's wear level.

Windows 11 has a built-in tool that reports exactly this, no third-party software needed. The battery report it generates shows your design capacity, current full charge capacity, and a week-by-week history of how capacity has changed — everything you need to compute wear and judge whether the trend is normal aging or something wrong. Here's how to generate it, read it, and know what the numbers mean for your next decision.

## Why this happens

- **Charge cycles consume capacity** — Each full 0–100% cycle (or equivalent partial cycles) slightly degrades the battery's chemistry; 300–500 cycles typically cost 20% capacity.
- **Heat accelerates wear** — Batteries kept hot (gaming on a bed, charging in the sun) wear noticeably faster than cool ones.
- **Sitting at 100% stresses cells** — Lithium batteries age faster when stored at full charge for weeks; charge limits exist to fight this.
- **Deep discharges hurt** — Routinely draining to 0% wears cells faster than shallow 40–80% cycling.
- **Age alone causes wear** — Even an unused battery loses some capacity over 2–3 years through calendar aging.
- **A failing cell looks like sudden wear** — If wear jumps 15% in a month, one cell may be failing rather than normal gradual wear.

## How to fix it

You can't reverse wear, but you can measure it precisely and slow it down. Work through these in order.

### Fix 1: Generate the battery report

The report is the foundation — everything else builds on its numbers.

1. Right-click **Start** and open **Terminal (Admin)** or **Command Prompt (Admin)**.
2. Type `powercfg /batteryreport` and press Enter.
3. Note the file path it prints — usually `C:\Users\YourName\battery-report.html`.
4. Open that file in your browser.

The report opens as a clean HTML page with several sections. The one you want first is **Installed batteries**.

### Fix 2: Calculate your wear percentage

Two numbers tell the whole story.

1. In the report, find **DESIGN CAPACITY** and **FULL CHARGE CAPACITY** under Installed batteries.
2. Divide full charge by design: `Full Charge ÷ Design × 100` = remaining capacity %.
3. Subtract from 100 to get wear %. Example: 45,000 ÷ 60,000 = 75% remaining → 25% wear.
4. Write the number down with today's date — you'll compare against it in a few months.

For a fuller walkthrough of every section, see [how to generate a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 3: Read the capacity history for the trend

A single number is a snapshot; the history shows whether wear is normal or alarming.

1. Scroll to the **Battery capacity history** section.
2. Look at how full charge capacity changed over the recorded weeks.
3. A gentle downward slope over months = normal aging.
4. A sudden cliff — losing 15–20% in a few weeks — suggests a failing cell or a gauge error, not normal wear.

If you see a cliff, calibrate the gauge (Fix 5) before concluding the battery is dying.

### Fix 4: Check the usage history for context

Wear numbers mean more when you know how the battery has been used.

1. Scroll to **Battery usage** in the report.
2. Look for patterns: constant 100% plugged-in time accelerates wear; frequent deep discharges do too.
3. If the laptop lives on a desk plugged in, enable your manufacturer's charge limit (Lenovo Conservation Mode, ASUS Maximum Lifespan, HP Battery Health Manager) to hold the battery at 60–80%.
4. Related reading: [what to do when full charge capacity drops](/articles/how-to-fix-laptop-battery-full-charge-capacity-low/).

### Fix 5: Calibrate before trusting the numbers

A miscalibrated fuel gauge can report wear that isn't real.

1. Charge to 100% and leave plugged in for 2 hours.
2. Unplug and use the laptop until it shuts off by itself.
3. Leave it off and unplugged for 3–5 hours.
4. Charge back to 100% uninterrupted, then regenerate the report with `powercfg /batteryreport`.

If wear drops significantly after calibration, the "wear" was a gauge error. If it stays the same, the number is real.

### Fix 6: Slow future wear with better charging habits

You can't undo wear, but you can bend the curve.

1. Enable your manufacturer's charge limit to cap daily charging at 80% (or 60% for desk-bound laptops).
2. Avoid leaving the laptop baking in heat — don't charge on soft bedding that blocks vents.
3. Don't obsess over staying plugged in at 100% for weeks; the charge limit handles this automatically.
4. Check the official guidance on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for battery best practices on your Windows build.

### Fix 7: Decide when replacement makes sense

Wear is a number — here's how to turn it into a decision.

1. Under 20% wear: normal. Change nothing.
2. 20–35% wear: noticeable but livable. Apply Fix 6 and re-check in 3 months.
3. 35–50% wear: replacement worth considering if runtime frustrates you daily.
4. Over 50% wear, or sudden cliff in history: replace the battery. On sealed laptops use the manufacturer or a reputable shop.

If the report also shows the battery [draining abnormally fast](/articles/how-to-fix-laptop-battery-drains-fast-step-by-step/) despite modest wear, the issue is software — fix that first, since a new battery won't help.

## Closing

Battery wear isn't a mystery once you have the report — two numbers, one division, and you know exactly where your battery stands. Check it every few months, keep the history in mind, and you'll always know whether your battery is aging gracefully or asking for retirement.

One last habit worth building: screenshot or save the report's key numbers each time with the date. When you eventually contact support about a battery that died young, that dated history is the difference between "we'll look into it" and an approved warranty replacement. The `powercfg /batteryreport` command takes ten seconds; the clarity — and the paper trail — it gives you is worth far more.
