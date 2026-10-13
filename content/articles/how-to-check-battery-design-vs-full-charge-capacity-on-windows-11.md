---
title: "How to Check Battery Design vs Full Charge Capacity on Windows 11"
slug: how-to-check-battery-design-vs-full-charge-capacity-on-windows-11
date: 2026-10-06
categories: ["battery"]
tags: ["battery", "battery report", "battery health", "windows 11"]
description: "Learn how to compare your laptop's battery design capacity with its full charge capacity on Windows 11 and what the numbers really mean."
thumbnail: "/images/thumbs/how-to-check-battery-design-vs-full-charge-capacity-on-windows-11.webp"
faqs:
  - q: "What is the difference between design capacity and full charge capacity?"
    a: "Design capacity is the energy your battery could hold when it left the factory, measured in milliwatt-hours. Full charge capacity is what it can actually hold now. The gap between the two shows how much the battery has worn down — a smaller gap means a healthier battery."
  - q: "What is a good full charge capacity percentage?"
    a: "A battery retaining 80 to 100 percent of its design capacity is in good shape. Between 60 and 80 percent means noticeable wear but it's still usable. Below 60 percent, the battery is worn out — expect short runtime and consider a replacement."
  - q: "Where do I find these numbers on Windows 11?"
    a: "Run powercfg /batteryreport in an administrator Command Prompt, then open battery-report.html. The Installed batteries section lists Design Capacity and Full Charge Capacity side by side, along with the full charge capacity history showing how the numbers changed over time."
  - q: "Why is my full charge capacity higher than the design capacity?"
    a: "It happens occasionally on a brand-new battery and isn't a problem — manufacturing tolerances mean some packs ship slightly above their rated design. The number settles toward the design value after a few charge cycles. Only worry if it swings wildly up and down, which suggests a calibration issue."
---

Every laptop battery ships with a rated energy storage — its design capacity — and then slowly loses the ability to reach that number. The difference between what your battery was designed to hold and what it can actually hold today is the single most honest measure of its health. Windows 11 hides this information in the battery report, but once you know where to look, it takes about a minute to find.

This guide walks you through generating the report, reading the two numbers correctly, and understanding what they mean for your laptop's remaining life. No third-party software needed — just a built-in Windows command and a web browser.

## Why this happens

- **Normal chemical aging.** Lithium-ion cells lose capacity with every charge cycle. A battery that started at 56,000 mWh might hold only 45,000 mWh after two years of daily use.
- **Heat accelerates wear.** Laptops that run hot — gaming, video rendering, blocked vents — degrade their cells faster, widening the gap between design and full charge capacity.
- **Deep discharges and full charges.** Regularly draining to 0% or sitting at 100% for long periods stresses cells more than partial cycles.
- **Calibration drift.** Sometimes the reported full charge capacity is wrong because Windows lost track of the true capacity. A calibration cycle can correct a misleading number.
- **Firmware reporting quirks.** After a BIOS or Windows update, the reported capacities can shift temporarily while the charge controller relearns the battery.
- **A defective cell pack.** A sudden, large drop — say from 90% to 55% in a week — can indicate a failing cell rather than normal wear.

## How to fix it

Work through these in order. "Fix" here means getting accurate numbers and knowing what to do about them.

### Fix 1: Generate the battery report

The report is the only built-in way to see both numbers side by side.

1. Right-click the **Start** button and open **Terminal (Admin)** or **Windows PowerShell (Admin)**.
2. Type `powercfg /batteryreport` and press **Enter**.
3. Note the file path in the output — usually `C:\Users\YourName\battery-report.html`.
4. Press **Win + R**, paste the path, and press **Enter** to open it in your browser.
5. Scroll to the **Installed batteries** section. You'll see **DESIGN CAPACITY** and **FULL CHARGE CAPACITY** listed in mWh. Divide full charge by design and multiply by 100 for your health percentage.

### Fix 2: Read the numbers correctly

A single snapshot can mislead, so interpret the figures in context.

1. In the same report, scroll down to **Battery capacity history** — this table shows how full charge capacity changed over weeks or months.
2. A slow, steady decline is normal aging. A sudden cliff suggests a problem worth investigating.
3. Check the **Battery life estimates** section too — it translates capacity into real-world runtime based on your actual usage.
4. If the capacity history is short or empty, Windows hasn't tracked enough cycles yet. Give it a week of normal use and regenerate the report. If your laptop also drops charge unexpectedly, read [how to fix sudden battery drops after a Windows 11 update](/articles/how-to-fix-laptop-battery-drops-suddenly-after-windows-11-update/).

### Fix 3: Rule out calibration drift

Before concluding the battery is worn, make sure Windows is measuring correctly.

1. Charge the laptop to 100% and leave it plugged in for 30 minutes.
2. Unplug and use it normally until it reaches about 10%. Avoid letting it die completely.
3. Plug back in and charge uninterrupted to 100% — don't use the laptop during this charge.
4. Run `powercfg /batteryreport` again the next day and compare. If the full charge capacity jumped back up, the old reading was drift, not wear. The full procedure is in [this calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 4: Reduce the wear rate going forward

You can't reverse wear, but you can slow it.

1. Open **Settings > System > Power & battery** and check whether your vendor offers a charge limit — Lenovo's Conservation Mode and Asus Battery Health Charging cap charging at 60–80%.
2. If your brand supports it, enable the cap. Staying below 100% noticeably slows capacity loss.
3. Improve cooling: elevate the laptop's rear, clean dust from vents with compressed air, and avoid heavy workloads on a soft bed or couch.
4. Avoid leaving the laptop plugged in at 100% for days on end in a hot room.

### Fix 5: Compare against the warranty threshold

Knowing when a replacement is justified matters.

1. Most manufacturers consider a battery defective — not just worn — if it falls below roughly 60–70% of design capacity within the warranty period.
2. Generate a fresh battery report and save it as evidence.
3. Check your warranty status on the manufacturer's site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. If the battery is out of warranty but below 60%, a third-party or manufacturer replacement is usually the cost-effective move rather than another year of 40-minute runtimes.

### Fix 6: Check for firmware-level misreporting

Sometimes the numbers lie because the firmware is confused.

1. Visit your manufacturer's support site and check for a **BIOS** update for your exact model. Install it with the charger connected.
2. Some brands ship battery firmware updates separately — look for anything labeled "battery" or "embedded controller" in the driver list.
3. After updating, run two full charge/discharge cycles, then regenerate the report.
4. If the numbers still look wrong after firmware updates and calibration, the battery's internal controller is the likely culprit, and the pack needs replacing.

## Closing

Design capacity versus full charge capacity is the closest thing to a battery report card that Windows offers. Generate the report, do the division, and you know exactly where you stand: above 80% means healthy, 60–80% means aging gracefully, and below 60% means it's time to plan a replacement. Recheck every few months and you'll never be surprised by a dying battery again.
