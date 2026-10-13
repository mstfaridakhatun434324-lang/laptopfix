---
title: "How to Check Your Battery Report Using CMD on Windows 11"
slug: how-to-check-battery-report-via-cmd-on-windows-11
date: 2026-09-01
categories: ["battery"]
tags: ["battery report", "powercfg", "cmd"]
description: "Windows 11 hides a detailed battery health report behind one command. Here's how to generate it with powercfg and read what it tells you."
thumbnail: "/images/thumbs/how-to-check-battery-report-via-cmd-on-windows-11.webp"
faqs:
  - q: "What command generates a battery report on Windows 11?"
    a: "Open Terminal or Command Prompt as administrator and run powercfg /batteryreport. Windows saves an HTML file (battery-report.html) in your user folder with capacity history, usage stats, and wear data. Double-click it to open in your browser."
  - q: "How do I know if my battery is healthy from the report?"
    a: "Compare Design Capacity to Full Charge Capacity under Installed batteries. Above 80% of design = healthy. 70–80% = noticeably worn. Below 70% = heavily worn and likely the cause of short runtime. Also check the capacity history graph for sudden drops."
  - q: "Where is the battery report file saved?"
    a: "By default in C:\\Users\\YourName\\battery-report.html. You can specify a path, e.g. powercfg /batteryreport /output C:\\battery.html, which is handy if you want to save reports over time and compare them."
  - q: "Does the battery report work on desktops?"
    a: "The command runs on any Windows 11 PC, but on a desktop without a battery it produces an empty report with no battery sections. It's only meaningful on laptops, tablets, and other battery-powered devices."
---

Windows 11 keeps a detailed dossier on your battery — its original capacity, its current capacity, how it's been used over the last three days, and how its capacity has changed over its lifetime. Most people never see it because it's hidden behind a single command. Generating a battery report takes ten seconds, and reading it properly answers the question behind half of all battery complaints: *is my battery actually worn out?*

Here's how to generate the report from CMD (or Terminal) and how to read the parts that matter.

## Why this matters (what the report tells you)

- **It settles the wear question definitively.** Design Capacity vs. Full Charge Capacity is the single most useful battery number on your laptop — no guessing, no apps required.
- **It shows usage patterns.** The recent-usage section reveals drain rates per session, which exposes whether the battery or your habits are the problem.
- **It tracks capacity history.** A gradual decline is normal aging; a sudden cliff means a failed cell group — very different situations with different fixes.
- **It's free and built in.** No third-party battery apps, no sketchy downloads, no background services. Just Windows telling you what it knows.
- **Support and shops respect it.** When you contact the manufacturer about a battery issue, having the report's numbers ready moves the conversation forward fast.

## How to do it

Work through these in order — generate, open, read, and act.

### Fix 1: Generate the report

The command itself couldn't be simpler.

1. Right-click **Start** and choose **Terminal (Admin)** — or search for **cmd**, right-click **Command Prompt**, and choose **Run as administrator**.
2. Type `powercfg /batteryreport` and press Enter.
3. Windows confirms where it saved the file — by default, `C:\Users\YourName\battery-report.html`.
4. Want it somewhere specific? Run `powercfg /batteryreport /output "C:\battery.html"` instead. Useful if you plan to generate reports monthly and compare them.

### Fix 2: Open and navigate the report

The report is an HTML file — double-click it to open in your browser.

1. Navigate to the saved `battery-report.html` and open it. You'll see several sections; the ones that matter most are **Installed batteries**, **Recent usage**, **Battery usage**, and **Battery capacity history**.
2. Start with **Installed batteries** at the top — this is where the headline numbers live.
3. Scroll through **Recent usage** to see your last 3 days of charge/discharge sessions with timestamps and energy figures.
4. The **Battery capacity history** table at the bottom shows full charge capacity over the battery's lifetime — the long-term trend line.

### Fix 3: Read the capacity numbers (the important part)

This is the section that answers "is my battery worn out?"

1. Under **Installed batteries**, find **DESIGN CAPACITY** and **FULL CHARGE CAPACITY** (both in mWh).
2. Divide full charge by design. Examples: 50,000 / 60,000 = 83% — healthy. 40,000 / 60,000 = 67% — heavily worn.
3. Rule of thumb: **above 80%** = fine, **70–80%** = aging but usable, **below 70%** = the battery is very likely why your runtime is short.
4. Check **CYCLE COUNT** if shown — most laptop batteries are rated for 300–500 full cycles before significant degradation. A high cycle count plus low capacity is normal end-of-life, not a defect.

### Fix 4: Read the usage and history sections

Capacity tells you the battery's condition; usage tells you whether behavior matches.

1. In **Recent usage**, look at the **Energy drained** per active session. Consistent heavy drain during light use points to software/settings issues rather than the battery.
2. In **Battery usage** (the graph), look for sessions where the battery dropped fast — then recall what you were doing. Gaming sessions draining 40% in an hour is normal; browsing doing the same is not.
3. In **Battery capacity history**, look at the trend: smooth gradual decline = normal aging. A sudden sharp drop in one period = likely cell failure — and that laptop needs a battery, not a settings tweak.
4. If the numbers show a healthy battery but fast drain, the [fast battery discharge troubleshooting guide](/articles/troubleshoot-battery-discharges-quickly-on-laptop/) picks up where this report leaves off.

### Fix 5: Compare reports over time

One report is a snapshot; several are a story.

1. Save each report with a dated filename: `powercfg /batteryreport /output "C:\battery-2026-10.html"`.
2. Generate a new one monthly (or when you notice runtime changes).
3. Compare **Full Charge Capacity** across reports. Losing 1–2% per month is normal; losing 10% in a month is not — that's a failing pack.
4. This history is also excellent evidence for warranty claims: "my battery lost 25% capacity in two months" with dated reports is hard to argue with.

### Fix 6: Act on what the report says

The report is only useful if it changes what you do next.

1. **Healthy battery (80%+) + short runtime:** it's software or settings — display brightness, background apps, power mode. Fix the consumption side.
2. **Worn battery (below 70%):** no setting restores capacity. Optimize what you can, but plan a replacement.
3. **Sudden capacity cliff:** failed cell group — replace sooner rather than later, and watch for swelling.
4. **Report won't generate or shows no battery:** run `powercfg /batteryreport` again from an elevated prompt, and if the battery sections are still empty, Windows isn't detecting the pack — see [laptop battery not detected](/articles/laptop-battery-not-detected-windows-11/).

### Fix 7: Try the other powercfg reports

The battery report has siblings worth knowing about.

1. `powercfg /energy` — runs a 60-second efficiency analysis and reports power-hungry culprits (great for idle drain mysteries).
2. `powercfg /sleepstudy` — detailed report of sleep sessions and what drained power during each one (the tool for overnight drain).
3. `powercfg /systempowerreport` — a broader power report covering the same ground as the battery report plus system power states.
4. Each generates an HTML file the same way. Together they give you a complete picture of your laptop's power behavior — all built into Windows, all free.

## Closing

The battery report is the closest thing Windows has to a battery truth serum: one command, ten seconds, and you know your battery's real condition instead of guessing from the percentage icon. Generate it with `powercfg /batteryreport`, compare design to full charge capacity, and let the numbers decide whether you're fixing software or replacing hardware. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents the full set of powercfg options if you want to go deeper. It's the first diagnostic step behind nearly every battery guide on this site — now you know how to run it yourself.
