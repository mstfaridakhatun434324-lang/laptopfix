---
title: "How to Generate a Battery Report in Windows 11"
slug: how-can-i-generate-battery-report-in-windows-11
date: 2026-09-03
categories: ["battery"]
tags: ["battery report", "powercfg", "battery health"]
description: "Generate a detailed Windows 11 battery report with powercfg in under a minute, and learn how to read capacity, cycles, and usage history."
thumbnail: "/images/thumbs/how-can-i-generate-battery-report-in-windows-11.webp"
faqs:
  - q: "How do I generate a battery report in Windows 11?"
    a: "Open Terminal as administrator, type powercfg /batteryreport, and press Enter. Windows saves an HTML report to your user folder. Open it in a browser to see design capacity, full charge capacity, cycle count, and a full history of charge and drain sessions."
  - q: "Where is the battery report saved?"
    a: "By default it is saved as battery-report.html in your user profile folder, typically C:\\Users\\YourName. You can specify a custom path, for example powercfg /batteryreport /output C:\\reports\\battery.html, but the folder must exist first."
  - q: "What does full charge capacity vs design capacity mean?"
    a: "Design capacity is what the battery held when new. Full charge capacity is what it holds now. The gap between them is wear. A battery at 90 percent of design is healthy; at 50 percent it is heavily worn and likely causing short runtime and early shutdowns."
  - q: "Does the battery report show cycle count?"
    a: "Yes, near the top of the report under Installed batteries. Cycle count tells you how many full charge-discharge cycles the battery has endured. Most laptop batteries are rated for 300 to 500 cycles before significant degradation, though real-world life varies."
---

When something is wrong with your battery, guessing wastes time. Windows 11 can hand you the actual numbers: how much capacity the battery was designed with, how much it holds now, how many cycles it has survived, and exactly how it has been draining over the past days. All of it comes from one command.

The battery report is the first thing a technician generates, because it turns vague complaints like "it dies too fast" into facts. Here is how to create one and read what matters.

## Why this happens

People usually need a battery report because of one of these situations, and knowing which one you are in tells you what to look for:

- **Short runtime:** The laptop dies faster than it used to, and you want to know if the battery is worn or something is draining it.
- **Suspicious percentages:** The gauge jumps, freezes, or the laptop dies at a high percentage.
- **Buying used:** You want to verify the battery health of a secondhand laptop before paying.
- **Warranty claims:** Manufacturers often ask for capacity numbers before approving a battery replacement.
- **After an update:** Battery behavior changed following a Windows update and you want a baseline.
- **Planning a replacement:** You need the exact battery model and chemistry details, which the report lists.

## How to fix it

Work through these in order, from generating the report to acting on it.

### Fix 1: Generate the report with powercfg

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Type `powercfg /batteryreport` and press Enter.
3. Windows confirms where it saved the file, usually `C:\Users\YourName\battery-report.html`.
4. Double-click the file to open it in your browser. For a custom location, run `powercfg /batteryreport /output "C:\Temp\battery.html"` after creating the folder.

### Fix 2: Read the capacity numbers at the top

1. Find the **Installed batteries** section near the top of the report.
2. Compare **DESIGN CAPACITY** to **FULL CHARGE CAPACITY**. Divide full charge by design to get the health percentage.
3. Above 80 percent is good. Between 60 and 80 percent is aging but usable. Below 60 percent explains short runtime.
4. Note the **CYCLE COUNT** and the chemistry type (usually LION). For a primer on what these numbers mean, see [how to check battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/).

### Fix 3: Check the recent usage history

1. Scroll to **Recent usage**. This shows power state changes over the last three days with timestamps.
2. Look for the battery draining while the machine was supposedly asleep or off. That points to sleep-state drain rather than wear.
3. Note any sessions where a small percentage drop took a long time versus a large drop in minutes. Inconsistent drain suggests a calibration problem.
4. Cross-reference odd drain with our [powercfg report deep dive](/articles/how-to-generate-battery-report-windows-11-powercfg/) for advanced reading tips.

### Fix 4: Study the battery drains section

1. Find **Battery drains**, which lists individual drain sessions with start capacity, end capacity, and duration.
2. Calculate the rough drain rate. Losing 30 percent in 30 minutes of light browsing is abnormal; losing it in 2 hours of video calls may be normal.
3. Identify which sessions were heaviest and what you were doing. Patterns here beat guesswork.
4. If drain is heavy during active use only, the battery is likely just worn.

### Fix 5: Review usage history and capacity history

1. **Usage history** shows daily active and standby time over weeks. A shrinking active time trend confirms gradual degradation.
2. **Battery capacity history** tracks full charge capacity over time. A sudden cliff, rather than a slope, can follow a Windows or BIOS update.
3. **Battery life estimates** at the bottom show how Windows' runtime predictions have changed. Falling estimates confirm what you feel.
4. Save a copy of the report now so you have a baseline to compare against in six months.

### Fix 6: Act on what the report tells you

1. **Healthy capacity but fast drain:** Something is consuming power. Check background apps and power mode.
2. **Low capacity:** The battery is worn. Recalibrate once, and if runtime does not improve, plan a replacement.
3. **Drain while asleep:** Disable fast startup and check sleep settings rather than blaming the battery.
4. **Sudden capacity cliff after an update:** Update the BIOS and battery drivers; firmware sometimes misreports capacity after updates.

### Fix 7: Re-run the report after any fix

1. After calibration, driver updates, or settings changes, generate a fresh report with `powercfg /batteryreport`.
2. Compare the new full charge capacity and drain rates against your baseline.
3. Keep reports dated in a folder so you can track degradation over the laptop's life.
4. For official documentation on power features, see [Microsoft's Windows support](https://support.microsoft.com/en-us/windows).

### Fix 8: Build a battery health history with dated reports

One report is a snapshot. A series of reports is a health record that catches gradual decline early.

1. Create a folder like `C:\BatteryReports` to store your reports.
2. Generate a report with a dated filename: `powercfg /batteryreport /output "C:\BatteryReports\battery-2026-10.html"`.
3. Repeat monthly. Put a recurring reminder on your calendar for the first of each month.
4. Each time, record three numbers in a simple text file: date, full charge capacity, and cycle count.
5. After six months, plot the trend. A steady slope is normal aging. A sudden cliff points to an event like an update or overheating incident worth investigating.
6. This history is also powerful evidence for warranty claims. Manufacturers take "capacity dropped 30 percent in two months" far more seriously than "battery seems bad."
7. Automate it: create a Task Scheduler task that runs the powercfg command monthly so you never forget.

## Closing

The battery report turns battery anxiety into numbers you can act on. Generate it, read the capacity gap, study the drain patterns, and let the data decide whether you need new settings, a calibration, or a new battery. One command, one minute, no more guessing.
