---
title: "How to Check Your Battery Report via CMD (powercfg Guide)"
slug: how-to-check-battery-report-via-cmd-on-laptop
date: 2026-10-13
categories: ["battery"]
tags: ["battery report", "powercfg", "cmd"]
description: "The powercfg battery report is Windows' built-in battery health check. Here's how to generate it via CMD and read every section."
thumbnail: "/images/thumbs/how-to-check-battery-report-via-cmd-on-laptop.webp"
faqs:
  - q: "What is the command to check battery health in CMD?"
    a: "Open Command Prompt as administrator and type powercfg /batteryreport then press Enter. Windows generates an HTML report (battery-report.html) in your user folder. Open it in any browser to see design capacity, full charge capacity, cycle count, usage history, and battery life estimates."
  - q: "Where is the battery report saved?"
    a: "By default in your user profile folder: C:\\Users\\YourName\\battery-report.html. The command output shows the exact path. You can specify a custom location with powercfg /batteryreport /output \"C:\\path\\report.html\" — useful for saving reports somewhere easy to find."
  - q: "How often should I generate a battery report?"
    a: "Every 2-3 months for routine monitoring, or immediately when you notice symptoms (fast drain, stuck percentage, not charging). Comparing reports over time is the real power of this tool — a single snapshot tells you the current state, but the trend tells you whether the battery is stable or declining."
  - q: "Does the battery report work on desktop PCs?"
    a: "The command runs on desktops too, but the report will show no battery data (or an error) since there's no battery. It's designed for laptops, tablets, and other battery-powered Windows devices. On a UPS-connected desktop, it still won't show the UPS — only internal batteries."
---
# How to Check Your Battery Report via CMD (powercfg Guide)

Every Windows laptop carries a built-in battery diagnostic that most owners never discover: the `powercfg /batteryreport` command. One line in Command Prompt generates a detailed HTML report with your battery's design capacity, current full-charge capacity, cycle count, recent usage, and life estimates. It's the same data technicians use — free, instant, no installs.

This guide shows you exactly how to generate the report, where to find it, and — most importantly — how to read each section so the numbers actually mean something.

## Why this happens

- **The tool is hidden in plain sight.** `powercfg` is a command-line utility with no Start menu entry — most users never encounter it.
- **People don't know what the numbers mean.** Design capacity vs. full charge capacity vs. cycle count — the report assumes you know the vocabulary.
- **Admin rights confusion.** The command needs an elevated Command Prompt, which trips up first-timers.
- **Finding the output file.** The report saves to the user folder with a generic name; people run the command and then can't find the result.
- **One snapshot vs. trend.** A single report is useful, but its real value is comparing reports over months — which nobody does until something breaks.
- **Third-party apps get the attention.** Battery monitoring apps market themselves hard while the superior built-in tool sits unused.

## How to fix it

Work through these in order, from quickest to deepest. Most people find the answer by Fix 3.

### Fix 1: Generate the Report (The Command)

Let's get the report created — it takes 30 seconds.

1. Press **Win + X** and choose **Terminal (Admin)**, **Command Prompt (Admin)**, or **Windows PowerShell (Admin)**.
2. Type exactly: `powercfg /batteryreport`
3. Press **Enter**. You'll see confirmation with the file path, typically `C:\Users\YourName\battery-report.html`.
4. To save it somewhere memorable, use: `powercfg /batteryreport /output "C:\Users\YourName\Desktop\battery-report.html"`
5. Navigate to the file and double-click to open it in your browser.

### Fix 2: Read the Header — Design vs. Full Charge Capacity

The top of the report has the two most important numbers.

1. Find **Design Capacity** — what the battery held when new (in mWh).
2. Find **Full Charge Capacity** — what it holds now.
3. Compute health: `Full Charge ÷ Design × 100` = remaining capacity percentage.
4. Compute wear: `100 − health` = wear percentage.
5. Rule of thumb: 85%+ remaining is healthy, 70–85% is aging, under 70% is degraded, under 50% is replacement territory.

Want the full interpretation framework? See [how to check battery wear level on Windows 10](/articles/how-to-check-battery-wear-level-on-windows-10/).

### Fix 3: Check Cycle Count and Battery Life Estimates

Deeper in the report are the numbers that predict the future.

1. Find **Cycle Count** (not all batteries report it) — under 300 is young, 300–500 middle-aged, 500+ elderly.
2. Scroll to **Battery life estimates** — Windows calculates these from your actual recent usage, not lab conditions.
3. Compare the "at full charge" estimate against your real-world experience — big gaps suggest background drain rather than battery problems.
4. Check **Recent usage** for the last 3 days: look for steep drops while the laptop was supposedly idle.
5. In **Usage history**, scan weeks of charge/discharge patterns for anomalies.

### Fix 4: Spot Problems in the Capacity History

The history table is where gradual decline vs. sudden failure becomes visible.

1. Open **Battery capacity history** — it lists full-charge capacity over time.
2. A gentle downward slope over months = normal aging. No action needed beyond good habits.
3. A sudden cliff (big drop between two entries) = cell failure or a damaged pack — investigate.
4. Erratic up-and-down readings = uncalibrated gauge or failing battery electronics.
5. If you see a cliff, run the diagnostics in Fix 6 before concluding anything.

### Fix 5: Compare Reports Over Time

One report is a snapshot; two reports are a diagnosis. Build the habit.

1. Save each report with a dated filename: `battery-report-2026-10.html`.
2. Every 2–3 months, generate a fresh one and compare full-charge capacity.
3. Calculate the decline rate: losing 2–3% per quarter is normal; 10%+ per quarter is not.
4. Note what changed between reports — new software, different usage, a hot summer — to correlate causes.
5. Bring two dated reports to a repair shop or warranty claim — it's compelling evidence.

### Fix 6: Run Manufacturer Diagnostics for Confirmation

The powercfg report is authoritative for capacity, but vendor diagnostics test the hardware independently.

1. **Dell:** **F12** at boot → **Diagnostics**.
2. **Lenovo:** **Lenovo Vantage > Device > Run diagnostics**, or **F10** at boot.
3. **HP:** **F2** at boot → **HP PC Hardware Diagnostics**.
4. Compare the vendor's health verdict with your report — they should agree.
5. If they disagree sharply, trust the powercfg capacity numbers but get a second opinion before replacing.

### Fix 7: Know the Related powercfg Commands

The battery report has siblings worth knowing.

1. `powercfg /energy` — generates an energy-efficiency report (60-second trace) flagging power-hungry settings and devices. Run in admin CMD.
2. `powercfg /sleepstudy` — shows what drained the battery during sleep/Modern Standby. Invaluable for overnight drain issues.
3. `powercfg /systempowerreport` — broader system power diagnostics.
4. Each generates an HTML file in the same way — same workflow, different insights.
5. For overnight drain specifically, the sleepstudy report is the tool most people need but never find.

If sleep drain is your actual problem, [fixing overnight battery drain](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-after-windows-11-update/) puts the sleepstudy data to work.

## Closing

`powercfg /batteryreport` is the closest thing Windows has to a battery truth serum — one command, and you get capacity, cycles, history, and estimates. Learn to read the design-vs-full-charge comparison and the capacity history, run it every few months, and you'll never again have to guess whether your battery is healthy, aging, or done. Every other battery fix on this site starts with this report for a reason: data first, decisions second.

## Verify your results

After generating the report, sanity-check it: does the full-charge capacity roughly match your real-world runtime? Does the recent-usage graph reflect how you actually used the laptop? If the numbers look alien, calibrate the battery and regenerate — the gauge needs good data to report good data. For official documentation, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) covers powercfg and power management in depth.
