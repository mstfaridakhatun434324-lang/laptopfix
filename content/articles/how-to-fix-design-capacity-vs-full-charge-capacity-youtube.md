---
title: "Design Capacity vs Full Charge Capacity (Video Walkthrough)"
slug: how-to-fix-design-capacity-vs-full-charge-capacity-youtube
date: 2026-09-24
categories: ["battery"]
tags: ["battery health", "battery report", "capacity"]
description: "Confused by design capacity vs full charge capacity in your battery report? Learn what the gap means and when it signals a dying battery."
thumbnail: "/images/thumbs/how-to-fix-design-capacity-vs-full-charge-capacity-youtube.webp"
faqs:
  - q: "What is the difference between design capacity and full charge capacity?"
    a: "Design capacity is what the battery could hold when it left the factory. Full charge capacity is what it can actually hold right now. The gap between them is wear — every charge cycle and every hot summer shaves a little off, and the gap only grows over time."
  - q: "What is a good full charge capacity percentage?"
    a: "Above 80% of design capacity is healthy. Between 60-80% is aging but usable — expect noticeably shorter runtime. Below 60% the battery is worn out for practical purposes, and below 50% you should plan a replacement if you need portability."
  - q: "Can I increase my full charge capacity back up?"
    a: "No. Capacity loss is permanent chemical wear — calibration can fix inaccurate readings but cannot restore lost capacity. Anyone selling a 'battery restore' for lithium laptop batteries is selling wishful thinking. The only fix for lost capacity is a new battery."
  - q: "Why is my full charge capacity higher than design capacity?"
    a: "This happens on new batteries and is harmless — manufacturing variance means some batteries ship slightly above spec, and the controller's estimate can overshoot a little. It usually settles near or just below design capacity after a few cycles."
---

You ran `powercfg /batteryreport`, scrolled to the top, and found two numbers that do not match: Design Capacity and Full Charge Capacity. Maybe they are close. Maybe there is a Grand Canyon between them. Either way, you are wondering what the gap means, whether it is fixable, and when to worry.

These two numbers are the single most honest health readout your battery has. Everything else — the percentage in the taskbar, the "battery health" label in some app — is derived from them. Here is how to read them, what to do about the gap, and which "fixes" are myths.

## Why this happens

- **Normal chemical aging.** Every lithium battery loses capacity with each charge cycle — typically 15-25% over 300-500 cycles.
- **Heat exposure.** A laptop that runs hot ages its battery faster; heat is the biggest accelerator of capacity loss.
- **Being held at 100% constantly.** Batteries kept at full charge degrade faster than those kept at 40-80%.
- **Deep discharges.** Regularly running to 0% stresses cells more than shallow cycles.
- **Age alone.** Even an unused battery loses capacity sitting on a shelf — chemistry does not pause.
- **A miscalibrated gauge.** Sometimes the gap looks worse than it is because the controller's estimate drifted — this is the one cause you can actually fix.
- **Inconsistent measurement conditions.** The controller estimates capacity from voltage curves, and readings taken when the battery is hot or right after heavy use can skew the number temporarily. Always compare reports taken under similar conditions.

## How to fix it

Work through these in order — first get accurate numbers, then decide what the numbers mean.

### Fix 1: Generate a clean battery report

Get the numbers from the horse's mouth.

1. Open **Terminal (Admin)**.
2. Run `powercfg /batteryreport` and note the saved file path.
3. Open the HTML file in your browser.
4. At the top, find **Design Capacity** and **Full Charge Capacity** (both in mWh).
5. Divide full charge by design and multiply by 100 — that is your battery health percentage.
6. Scroll to **Battery capacity history** to see when the decline happened: gradual slope means normal aging, a sudden cliff means an event (overheating episode, bad update, long storage at 0%).
7. Also glance at the **Recent usage** section — it shows how fast the battery actually drained in recent sessions, which confirms whether the capacity number matches real-world runtime.

### Fix 2: Rule out gauge miscalibration

Before accepting the numbers, make sure they are real.

1. Charge to 100% and keep charging for 2 hours.
2. Unplug, set sleep timers to **Never** (**Settings** > **System** > **Power & battery**), and use the laptop until it shuts itself down.
3. Leave it off and unplugged for 3+ hours.
4. Charge uninterrupted back to 100%.
5. Generate a fresh battery report and compare. If full charge capacity jumped up significantly, the old reading was gauge drift, not real wear.
6. Our [calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/) covers the full procedure, and our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains every report section.

### Fix 3: Interpret your health percentage honestly

Now decide what the number means for you.

1. **90-100%:** Effectively new. Any battery complaints are software or calibration, not wear.
2. **80-90%:** Normal for a 1-2 year old laptop. Runtime is slightly shorter; no action needed.
3. **60-80%:** Noticeably aged. Consider a charge limiter (cap at 80%) to slow further loss.
4. **Below 60%:** Worn out for practical use. If you need real portability, price a replacement battery.
5. Write down today's percentage and recheck monthly — the trend matters more than any single reading.

### Fix 4: Slow down future capacity loss

You cannot recover lost capacity, but you can protect what is left.

1. Enable your manufacturer's charge limiter: Lenovo Vantage Conservation Mode, MyASUS Battery Health Charging, Dell Power Manager, or HP Battery Health Manager. Cap at 80% for desk use.
2. Keep the laptop cool — heat accelerates capacity loss more than anything else you control. See our [overheating guide](/articles/how-to-fix-laptop-overheating-while-charging-on-windows-10/).
3. Avoid deep discharges; plug in around 20% instead of running to empty.
4. If you store the laptop unused for weeks, leave it at 50-60% charge, not 100% and not empty.
5. Details per brand are in our [80% charge limit guide](/articles/how-to-limit-battery-charge-to-80/).

### Fix 5: Update the battery firmware

Occasionally the controller misjudges capacity due to old firmware.

1. Check your manufacturer's support site for BIOS or embedded controller updates: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Install with the charger connected.
3. Run one full calibration cycle afterward so the new firmware learns the battery from scratch.
4. Regenerate the battery report and compare — firmware updates sometimes correct pessimistic capacity estimates.

### Fix 6: Know when to replace

Honest math beats wishful thinking.

1. If full charge capacity is under 50% of design and you need portability, replacement is the answer — no software fix restores chemistry.
2. Get the exact battery model number from the old battery or the manufacturer's parts page. Match voltage, watt-hour rating, and connector.
3. Prefer genuine manufacturer batteries. Cheap third-party packs often lie about capacity and report garbage data to Windows.
4. For sealed laptops, watch a teardown for your exact model first, or have a shop do it — puncturing a lithium battery is dangerous.
5. Recycle the old battery properly — never throw lithium batteries in the trash. Most electronics stores take them.

## Closing

Design capacity is the factory promise; full charge capacity is today's reality. A small gap is just life, a big gap is a battery telling you it is tired, and no calibration trick or "battery restore" app changes the chemistry. Measure honestly, protect what remains with a charge cap and cool running, and replace when the runtime no longer covers your day. Check the numbers once a month — a sudden change between checks is always worth investigating, while a slow drift is simply the battery aging gracefully.
