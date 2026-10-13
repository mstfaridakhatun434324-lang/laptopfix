---
title: "Best Way to Generate a Battery Report in Windows 11"
slug: best-way-to-generate-battery-report-in-windows-11
date: 2026-09-14
categories: ["battery"]
tags: ["battery report", "powercfg", "Windows 11"]
description: "The fastest way to generate a Windows 11 battery report is one powercfg command. Here's the exact command and how to read every section."
thumbnail: "/images/thumbs/best-way-to-generate-battery-report-in-windows-11.webp"
faqs:
  - q: "What is the command to generate a battery report in Windows 11?"
    a: "Open Terminal as administrator and run powercfg /batteryreport /output C:\\battery-report.html. Windows saves an HTML report to that location in seconds. Open it in Edge or any browser to see capacity history, recent usage, and estimated battery life."
  - q: "How often should I generate a battery report?"
    a: "Once a month is plenty for tracking gradual wear. Generate one immediately if you notice sudden changes — fast drain, the laptop dying at a high percentage, or charging stopping early. Comparing reports over time shows trends that a single snapshot cannot."
  - q: "What does full charge capacity mean in the report?"
    a: "It is how much energy your battery can currently store, in milliwatt-hours. Compare it with the design capacity, which is what the battery held when new. The gap between them is your wear: a battery at 70 percent of design capacity has lost 30 percent of its original runtime."
  - q: "Why is my battery report missing recent data?"
    a: "The report draws on Windows' power telemetry, which pauses when the battery driver is corrupted or when the laptop has been fully shut down for long stretches. Reinstall the battery driver in Device Manager, use the laptop on battery for a day, then regenerate the report."
---

Windows 11 has a built-in battery laboratory that almost nobody opens. The `powercfg /batteryreport` command produces a polished HTML document with your battery's design capacity, its current full charge capacity, months of capacity history, and a detailed log of recent drain. It is the single most useful diagnostic for any battery complaint, and generating it takes less time than reading this paragraph.

The best way to do it is from an elevated Terminal with an explicit output path, so you always know where the file landed. This guide gives you the exact command, teaches you to read each section, and shows what to do with what you find.

## Why this happens

- **Buried in the command line:** The richest battery data in Windows 11 lives in `powercfg`, not in Settings, so most users never find it.
- **Misread capacity figures:** Design capacity versus full charge capacity confuses people into thinking a healthy battery is dying, or vice versa.
- **History reveals patterns:** The capacity history table distinguishes slow chemical aging from sudden drops caused by updates or faults.
- **Usage log catches drain:** Recent usage data exposes overnight drain and idle waste that capacity numbers alone cannot show.
- **Reports go stale:** Without regular regeneration, you lose the trend lines that make the report truly valuable.

## How to fix it

Work through these in order — generate, read, interpret, and act.

### Fix 1: Generate the report with the best command

Use an explicit output path so the file is easy to find.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run `powercfg /batteryreport /output "C:\battery-report.html"`.
3. Wait for the success message confirming the file was written.
4. Open **File Explorer**, navigate to **C:\**, and double-click **battery-report.html**.
5. The report opens in your default browser — keep the tab open while you work through the sections below.

### Fix 2: Read the installed-battery summary

The top of the report gives you the headline numbers.

1. Locate the **Installed batteries** section and read the **Design Capacity** — the factory-fresh capacity in mWh.
2. Read the **Full Charge Capacity** right below it — what the battery holds today.
3. Calculate the health percentage: full charge divided by design capacity, times 100.
4. Above 80 percent is healthy, 60 to 80 percent is aging, and below 60 percent means start planning a replacement.
5. Note the **Cycle Count** and chemistry type for context — most packs are rated for a few hundred full cycles. Our deep dive on [design vs full charge capacity](/articles/best-way-to-fix-design-capacity-vs-full-charge-capacity/) explains these figures further.

### Fix 3: Interpret the capacity history table

Trends beat snapshots every time.

1. Scroll to **Battery capacity history** and scan the **Full Charge Capacity** column from oldest to newest entry.
2. A gentle downward slope over many months is normal lithium-ion aging.
3. A sudden step down between consecutive weeks usually follows a BIOS update, a Windows feature update, or a deep discharge — not sudden chemical failure.
4. If the drop lines up with an update, reinstall the battery driver and recalibrate before trusting the new number.
5. Save each month's report with the date in the filename so future comparisons are easy.

### Fix 4: Analyze battery usage and drain patterns

This section answers "where did my charge go?"

1. Find the **Battery usage** graph covering the last three days.
2. Look for steep drops during hours when the laptop should have been asleep — that is sleep drain, a settings problem rather than battery wear.
3. Check **Usage history** for per-hour drain rates and compare against your normal workload.
4. Match spikes to activities: video calls, gaming, and video rendering legitimately drain fast.
5. If usage looks normal but capacity is low, the battery is worn — the drain is honest, the tank is just smaller. Compare with the Windows 10 process in [checking a battery report via Command Prompt](/articles/how-to-check-battery-report-via-cmd-on-windows-10/).

### Fix 5: Estimate real-world battery life

The report includes Windows' own runtime estimates.

1. Scroll to **Battery life estimates**, which shows projected runtime at full charge based on actual recent drain.
2. Compare the estimate with what you experience — a big gap suggests background drain the averages have not caught up with.
3. Remember these are rolling averages: a week of heavy video editing lowers the estimate even if the battery is fine.
4. Use the estimate as a baseline, then re-check after fixing drain issues to measure improvement.
5. Do not panic at a low number alone — always cross-check with the capacity percentage from Fix 2.

### Fix 6: Generate the companion energy report

When the battery report raises questions, the energy report answers some of them.

1. In **Terminal (Admin)**, run `powercfg /energy /output "C:\energy-report.html"`.
2. Leave the laptop untouched for the 60-second observation window.
3. Open the report and review **Errors** and **Warnings** — these name devices and drivers that block sleep or waste power.
4. Fix flagged items one by one: update the named driver or disconnect the offending USB device.
5. Microsoft documents both tools on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Turn findings into action

A report only helps if you follow through.

1. Healthy capacity, fast drain → find the culprit in **Settings → System → Power & battery → Battery usage per app**.
2. Low capacity, normal drain → the pack is worn; replace it with a battery matched to your exact model.
3. Sudden cliff after an update → driver reinstall, then a full calibration cycle, then regenerate the report.
4. Set a monthly reminder to regenerate the report — catching wear early lets you plan a replacement instead of being surprised by it.

## Closing

Generating a Windows 11 battery report is a ten-second job that pays off every time a battery question comes up. Run the command, read design versus full charge capacity, scan the history for cliffs, and check the usage graph for mystery drain. Keep monthly copies, and you will always know whether your battery is aging gracefully or asking for help.
