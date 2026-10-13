---
title: "Generate a Battery Report in Windows 11: Step-by-Step Guide"
slug: how-to-generate-battery-report-in-windows-11
date: 2026-09-01
categories: ["battery"]
tags: ["battery report", "powercfg", "windows 11"]
description: "Generate and read Windows 11's built-in battery report with powercfg — check wear, capacity history, and drain patterns."
thumbnail: "/images/thumbs/how-to-generate-battery-report-in-windows-11.webp"
faqs:
  - q: "What is the command to generate a battery report?"
    a: "Open Windows Terminal as administrator and run powercfg /batteryreport. Windows saves an HTML file (usually at C:\\Windows\\System32\\battery-report.html) that you open in any browser. No extra software needed — it's built into every copy of Windows 11."
  - q: "Where is the battery report saved?"
    a: "By default, in the current directory of the terminal you ran it from — typically C:\\Windows\\System32\\battery-report.html when run from an elevated prompt. You can specify a friendlier location with powercfg /batteryreport /output C:\\Users\\YourName\\Desktop\\battery-report.html."
  - q: "How do I check battery wear from the report?"
    a: "Find the 'Installed batteries' section and compare Design Capacity to Full Charge Capacity. The difference is your wear. For example, a design capacity of 50,000 mWh and a full charge capacity of 42,000 mWh means 16% wear — the battery holds 84% of what it did when new."
  - q: "How often should I generate a battery report?"
    a: "Generate one whenever battery behavior changes, and otherwise every few months to track the capacity history trend. Comparing reports over time is far more informative than any single snapshot — it shows whether wear is gradual (normal) or sudden (a failing cell or bad update)."
---

Windows 11 keeps a detailed diary of your battery's life — capacity, wear, charge cycles, drain patterns — and it will hand it to you as a neat HTML report any time you ask. Most people never know it exists, which is a shame, because the battery report answers the two questions that matter: is my battery actually worn out, and is something draining it abnormally? Everything else in battery troubleshooting builds on this document.

This guide covers generating the report two ways, reading each section properly, and using the numbers to make decisions. If you want the broader diagnostic process around the report, see [how to run battery diagnostics on Windows 11](/articles/how-to-run-battery-diagnostics-on-windows-11/).

## Why this happens

- **Hidden by design:** Microsoft buries powercfg in the terminal; there's no button in Settings that says "battery report," so most users never find it.
- **Admin requirement confusion:** The default save location (System32) needs elevation, which trips up people running a normal prompt.
- **Misreading capacity numbers:** The raw milliwatt-hour figures mean nothing until you compare design versus full charge capacity as a ratio.
- **Single-snapshot thinking:** One report shows current state; the real diagnostic power is in the history sections showing trends over weeks.
- **Ignoring the usage sections:** People check capacity but skip the recent-usage and drain-history sections that reveal abnormal background drain.
- **Not knowing the baseline:** Without an early report from when the machine was new-ish, you can't tell gradual wear from a sudden failure.

## How to fix it

Work through these in order — generate, locate, read, act.

### Fix 1: Generate the report with powercfg

The core command, two ways to run it.

1. Right-click **Start** and choose **Windows Terminal (Admin)**.
2. Type `powercfg /batteryreport` and press Enter — you'll see the path where the HTML file was saved.
3. Easier alternative: type `powercfg /batteryreport /output "%USERPROFILE%\Desktop\battery-report.html"` to drop the file right on your desktop.
4. Open the file in Edge, Chrome, or any browser — it's a self-contained local HTML page, nothing uploads anywhere.
5. If you get an "access denied" error, you forgot the Admin part — close and reopen the terminal as administrator.

### Fix 2: Read the Installed batteries section

Where wear lives.

1. At the top of the report, find **Installed batteries** — note the **Design Capacity** (factory-new capacity in mWh) and **Full Charge Capacity** (current maximum).
2. Compute the ratio: full charge ÷ design. Above 0.85 is healthy, 0.70-0.85 is aging, below 0.70 is significantly worn.
3. Check the **Cycle Count** if shown — consumer lithium packs are typically rated for 300-500 full cycles before notable degradation.
4. Note the battery's manufacture date and chemistry if listed; an old manufacture date on a "new" laptop explains premature wear.
5. Screenshot or save this section — it's your baseline for every future comparison.

### Fix 3: Study the capacity history and life estimates

Trends beat snapshots.

1. Scroll to **Battery capacity history** — this table shows full charge capacity over recent weeks.
2. A gentle downward slope is normal aging. A sudden vertical drop on a specific date points to a cell failure, a bad BIOS update, or a gauge recalibration event.
3. Check **Battery life estimates**: compare the "at full charge" estimate with your real-world experience — a big gap means drain (software) rather than capacity (hardware) is your problem.
4. Look at whether the estimates are based on actual observed drain or just design math; observed-data estimates are far more trustworthy.
5. If capacity fell off a cliff after a Windows or BIOS update, check for a newer firmware before assuming hardware failure.

### Fix 4: Analyze recent usage and battery usage history

Find abnormal drain patterns.

1. The **Recent usage** section logs power state changes (active, standby, hibernate) with timestamps over the last 3 days.
2. Look for long **Connected standby** periods with high drain — that's the Modern Standby problem; see [fixing HP sleep drain](/articles/how-to-fix-hp-laptop-battery-drains-in-sleep/) for the same mechanics on any brand.
3. The **Battery usage** graph shows drain rate over time — spikes during periods you weren't using the machine indicate background activity.
4. Correlate drain spikes with the **Usage history** app table if present, or cross-check with **Settings > System > Power & battery > Battery usage** per-app stats.
5. Normal idle drain on battery (screen off, truly idle) should be modest — if the report shows the pack draining fast while "idle," something is running.

### Fix 5: Generate the report on a schedule

Turn a one-off into a monitoring habit.

1. Create a simple scheduled task: open **Task Scheduler**, create a basic task running monthly that executes `powercfg /batteryreport /output "C:\BatteryReports\battery-%DATE%.html"` (adjust the command syntax for your needs).
2. Alternatively, just calendar a reminder every 3 months — manual is fine, the point is the trend data.
3. Keep old reports in one folder so you can open two side by side and compare capacity history tables directly.
4. After any major fix (new battery, calibration, driver updates), generate a fresh report immediately as the new baseline.
5. A sudden change between scheduled reports is your early warning system for cell failure — much better than discovering it via a dead laptop.

### Fix 6: Know what the report can't tell you

Understand its limits so you don't over-trust it.

1. The report shows what the fuel gauge *believes* — if the gauge is miscalibrated, the capacity numbers can be wrong; calibrate if percentages behave oddly (see [fixing a battery that dies at 30%](/articles/how-to-fix-laptop-battery-dies-at-30-percent/)).
2. It won't identify a specific bad app — pair it with the per-app battery usage screen in Settings for that.
3. It can't detect swelling or physical damage — that's a visual inspection.
4. Cycle count may be missing on some packs; its absence isn't a problem, just a firmware reporting gap.
5. For a second opinion at the hardware level, run your OEM's battery diagnostic (Lenovo Vantage, Dell SupportAssist, HP UEFI diagnostics).

### Fix 7: Act on what you find

Turn numbers into a decision.

1. **Wear under 20%, bad runtime:** It's drain, not the battery — hunt background apps and settings.
2. **Wear 20-40%:** Normal aging on a used machine — enable a charge limit (80% or Lenovo conservation mode) to slow further wear.
3. **Wear over 40% or sudden cliff:** Plan a replacement; check [how to replace a laptop battery](/articles/how-to-replace-laptop-battery-on-windows-10/) when ready.
4. **High standby drain:** Fix wake timers and Modern Standby activity per the sleep-drain guide.
5. Microsoft documents powercfg and power management officially at [Microsoft Support](https://support.microsoft.com/en-us/windows).

## Closing

The battery report takes thirty seconds to generate and answers questions that hours of guessing can't. Make it the first thing you do whenever battery behavior changes — and the periodic thing you do to catch wear early. It's the closest thing Windows offers to a battery health checkup, and it's been sitting in your terminal the whole time.
