---
title: "Design Capacity vs. Full Charge Capacity: What the Numbers Mean After a Windows 11 Update"
slug: how-to-fix-design-capacity-vs-full-charge-capacity-after-windows-11-update
date: 2026-09-11
categories: ["battery"]
tags: ["design capacity", "full charge capacity", "battery report"]
description: "Your battery report shows full charge capacity below design capacity after a Windows 11 update? Learn what the gap means, when it's normal, and how to fix a wrong reading."
thumbnail: "/images/thumbs/how-to-fix-design-capacity-vs-full-charge-capacity-after-windows-11-update.webp"
faqs:
  - q: "What is the difference between design capacity and full charge capacity?"
    a: "Design capacity is what the battery held when new (factory spec, in mWh). Full charge capacity is what it holds now. The gap between them is wear — a battery with 50,000 mWh full charge against 60,000 mWh design is at about 83% health."
  - q: "Why did full charge capacity drop after a Windows update?"
    a: "Updates can reset the battery gauge, making Windows report a lower full charge capacity until recalibrated. The battery didn't lose real capacity overnight — the estimate did. Calibrate and recheck before worrying."
  - q: "How much capacity loss is normal per year?"
    a: "Roughly 5-10% per year with normal use. Faster loss points to heat, constant 100% charging, or heavy cycling. A sudden 15%+ drop right after an update is almost always a gauge issue, not real wear."
  - q: "Can full charge capacity ever go back up?"
    a: "Yes, slightly — after calibration the reported number often rises because the previous reading was wrong. Real chemical capacity never increases, but the reported figure can recover to the true value."
---
You ran `powercfg /batteryreport` after the Windows 11 update and found two numbers that don't match: **design capacity** 62,000 mWh, **full charge capacity** 48,000 mWh. Last month the gap was much smaller. Did the update eat 20% of your battery overnight? Almost certainly not — but the numbers need interpreting before you decide anything.

Design vs. full charge capacity is the single most useful pair of numbers in battery diagnostics, and also the most misunderstood. Here's what they actually mean, why an update makes them jump, and how to get a trustworthy reading.

## Why the numbers shift after an update

- **The gauge was reset.** Windows updates can wipe the battery controller's learned capacity data. Until it relearns, full charge capacity is a rough guess — often a pessimistic one.
- **You're comparing against a stale design value.** Design capacity never changes (it's the factory spec), but if the battery was already worn, the update just made the existing gap visible in a fresh report.
- **The battery aged normally and you just noticed.** Many people only run a battery report when something feels wrong — the wear was gradual, the discovery was sudden.
- **Temperature skewed the reading.** Battery reports generated while the laptop is hot show slightly lower capacity. A report run during an update (heavy CPU, heat) reads worse than one run idle and cool.
- **A charge limit is active.** If the update enabled an 80% cap, full charge capacity reflects the capped value — the battery is fine, it's just not allowed to fill up.
- **Real accelerated wear.** Rare, but possible: an update that breaks sleep can leave the laptop hot and cycling all night for weeks, genuinely aging the battery faster.

## How to fix it

Work through these in order. The goal is a trustworthy number, then a decision.

### Fix 1: Generate a clean battery report

First, make sure you're reading good data.

1. Let the laptop cool to room temperature and unplug any heavy workloads.
2. Open **Terminal (Admin)** and run: `powercfg /batteryreport /output "C:\battery-report.html"`.
3. Find **Installed batteries** and write down both numbers. Calculate health: `(FULL CHARGE ÷ DESIGN) × 100`.
4. Don't act on a single report — you need the trend, which is Fix 2.

### Fix 2: Read the capacity history trend

One number is noise; the trend is the signal.

1. In the same report, open **Battery capacity history**.
2. Look at the weekly full-charge-capacity column going back months. A smooth downward slope is normal aging.
3. A vertical cliff exactly at the update date = gauge reset (fixable). A steady decline that you only just noticed = real wear that predates the update. If you want a guided read of every section, the [24H2 capacity-check walkthrough](/articles/how-to-check-battery-design-vs-full-charge-capacity-in-windows-11-24h2/) goes section by section.

### Fix 3: Rule out an active charge limit

1. Check your manufacturer's app for any limit: MyASUS Battery Health Charging, Lenovo Conservation Mode, Dell Power Manager custom thresholds, HP Battery Health Manager.
2. If a limit is on, the reported full charge capacity is capped by policy, not chemistry. Temporarily set full capacity and regenerate the report.
3. The general [charge limit guide](/articles/how-to-limit-battery-charge-to-80/) explains which setting does what on each brand.

### Fix 4: Calibrate to restore the true reading

If the history shows a cliff at the update date, recalibrate — this is the fix.

1. Charge to 100% and leave plugged in for 2 hours.
2. Unplug, use normally until auto-shutdown. Leave off and unplugged for 3-5 hours.
3. Recharge uninterrupted to 100%.
4. Regenerate the battery report. In most gauge-reset cases, full charge capacity jumps back up significantly — sometimes to nearly the pre-update value.

### Fix 5: Reinstall the battery driver

A corrupted driver can misreport capacity to Windows.

1. **Device Manager** > **Batteries** > right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
2. Restart. Windows reinstalls the driver.
3. Regenerate the report after 2-3 full charge cycles and compare — driver misreads usually correct themselves within a few cycles.

### Fix 6: Check whether the wear is real with a runtime test

Numbers are estimates; runtime is truth.

1. Charge to 100%, unplug, and use the laptop for a defined task (e.g., video playback at 50% brightness) until 20%.
2. Note the elapsed time. Compare with the **Battery life estimates** in the report.
3. If real runtime matches a healthy estimate but the capacity number looks bad, trust the runtime — the number is wrong. If runtime is genuinely short, the wear is real: [low full charge capacity fixes](/articles/how-to-fix-laptop-battery-full-charge-capacity-low-after-windows-11-update/) cover what to do next.

### Fix 7: Decide based on the real number

1. **85%+ of design:** healthy. The update just startled you — move on.
2. **70-85%:** normal wear. Enable a charge limit to slow further loss.
3. **Below 70% with a smooth history:** genuine wear. Start planning a replacement; check warranty coverage first.
4. Document the numbers with dated reports — useful evidence if you claim warranty.

### Fix 8: Archive dated reports as warranty evidence

If the numbers keep dropping, build a paper trail before you need it.

1. Every time you generate a battery report, save it with the date in the filename: `battery-report-2026-09.html`, and keep them in one folder.
2. If capacity falls off a cliff — especially right after an update — those dated files prove the timeline. "It was 92% in August and 71% in September" is a much stronger warranty conversation than "it feels worse."
3. Screenshot the **Battery capacity history** table too, since it visualizes the drop in one image.
4. Most manufacturers cover batteries for 12 months. A documented sudden drop inside the warranty window is often enough for a free replacement — without documentation, it's your word against theirs.

## Closing

Design capacity is the factory promise; full charge capacity is today's reality. After a Windows 11 update, that reality is often misreported — calibrate first, read the trend second, and only believe a low number after both. Most "my update killed my battery" stories end with the gauge, not the battery, being the culprit — and dated reports prove it either way.
