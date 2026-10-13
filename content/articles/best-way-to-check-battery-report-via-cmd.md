---
title: "Battery Report via CMD: The powercfg Guide (Windows 10/11)"
slug: best-way-to-check-battery-report-via-cmd
date: 2026-10-03
categories: ["battery"]
tags: ["powercfg", "battery report", "command prompt"]
description: "Run powercfg /batteryreport from CMD to get a full battery health report on Windows 10/11. Learn to read design capacity, wear level, and usage history."
thumbnail: "/images/thumbs/best-way-to-check-battery-report-via-cmd.webp"
faqs:
  - q: "What is the command to check battery health in CMD?"
    a: "Open Command Prompt as administrator and type `powercfg /batteryreport`, then press Enter. Windows saves an HTML report (usually to your user folder) showing design capacity, full charge capacity, cycle count, recent usage, and battery drain history. Double-click the file to open it in your browser — no extra software needed."
  - q: "Do I need admin rights to run powercfg /batteryreport?"
    a: "Strictly speaking, no — the command runs in a normal Command Prompt too. But running as administrator avoids permission quirks when writing the file and is the reliable habit. Right-click the Start button, choose Terminal (Admin) or Command Prompt (Admin), then run the command."
  - q: "What does full charge capacity vs design capacity mean?"
    a: "Design capacity is what the battery held when new; full charge capacity is what it holds now. Divide full charge by design to get battery health as a percentage. For example, 45,000 mWh full charge against 60,000 mWh design equals 75% health, or 25% wear. Under 70-80% health, expect noticeably shorter runtime."
  - q: "Can the battery report tell me if I need a new battery?"
    a: "It gives you the strongest evidence short of a hardware test. Consistently low full-charge capacity, a steep drop in the capacity history graph, or usage history showing the battery dying in under an hour of light use all point to replacement. Combine the report with a physical check for swelling before deciding."
---

Windows has a built-in battery laboratory hiding behind one command. `powercfg /batteryreport` generates a detailed HTML report covering your battery's design specs, current health, cycle count, and weeks of usage history — no third-party tools, no guesswork. Every battery troubleshooting guide worth reading starts here, because it separates "the battery is dying" from "something else is wrong" in about thirty seconds.

This guide shows you how to generate the report on Windows 10 and 11 and, more importantly, how to read each section like a technician. Once you can read it, questions like [whether your wear level is too high](/articles/how-do-i-fix-battery-wear-level-too-high/) answer themselves.

## Why This Happens

- **People guess instead of measuring.** "Battery drains fast" has a dozen causes; the report narrows it to battery health versus software drain in one glance.
- **Windows hides battery health.** Unlike phones, Windows shows no health percentage in Settings — the report is the official way to see it.
- **Wear is invisible.** A battery can lose 40% of its capacity with no warning dialogs. The capacity history graph makes the decline visible.
- **Misleading symptoms.** Sudden shutdowns at 30% look like software bugs but are usually dying cells — the usage history proves it.
- **Warranty claims need evidence.** Manufacturers ask for battery report data before approving warranty battery replacements.
- **Calibration confusion.** A wrong fuel-gauge reading mimics a bad battery; the report's raw numbers tell them apart.

## How to Fix It

Work through these in order. By Fix 4 you will be reading the report like a pro.

### Fix 1: Generate the Battery Report

The command itself takes five seconds.

1. Press **Win + X** and select **Terminal (Admin)** or **Command Prompt (Admin)**.
2. Type `powercfg /batteryreport` and press **Enter**.
3. Note the file path it prints — usually `C:\Users\YourName\battery-report.html`.
4. To save it somewhere specific, use `powercfg /batteryreport /output "C:\battery-report.html"`.
5. Open the HTML file in your browser. It has several sections; the next fixes walk through each one.
6. On Windows 11, the same command works identically — Microsoft has not changed it in years.

### Fix 2: Read the Installed Batteries Section

This is the health verdict. Everything else is supporting detail.

1. At the top of the report, find **Installed batteries** with **DESIGN CAPACITY** and **FULL CHARGE CAPACITY**.
2. Divide full charge capacity by design capacity. Example: 38,210 / 52,000 = 73% health, meaning 27% wear.
3. Rough guide: above 85% is healthy, 70-85% is noticeably degraded, below 70% means short runtime is the battery's fault, and below 50% means start shopping for a replacement.
4. Check **CYCLE COUNT** if shown. Most laptop batteries are rated for 300-500 full cycles; well past that with low capacity confirms normal end-of-life.
5. If full charge capacity looks fine but runtime is still bad, your problem is power drain, not battery health — see [what to do when the battery drains fast](/articles/what-to-do-if-laptop-battery-drains-fast/).
6. Save or screenshot this section if you ever need warranty support; it is the number they ask for.

### Fix 3: Read Recent Usage and Battery Drains

These sections show what actually happened, hour by hour.

1. Scroll to **Recent usage**. Each row shows a time span, the power state (Active, Suspended, etc.), and the charge percentage at start and end.
2. Look for steep drops during **Suspended** or powered-off periods — a healthy laptop loses only a few percent overnight. Big overnight drops point to sleep-state drain, not battery wear.
3. Check the **Battery drains** section for the mW discharge rate during active use. Divide your full charge capacity (mWh) by the drain rate (mW) for a rough runtime estimate.
4. Compare drain rates across days: a sudden jump after a specific date often lines up with a Windows update or new software — a software problem, not a battery problem.
5. Look for the laptop waking from sleep repeatedly (many short Active periods overnight). That is usually a wake timer or device waking the machine.
6. If usage looks normal but capacity is low, the battery is simply worn — the two sections together make the diagnosis unambiguous.

### Fix 4: Read Battery Capacity History and Life Estimates

The long view: how your battery aged and what runtime to expect.

1. Find **Battery capacity history**. It lists full charge capacity by week going back months.
2. A gradual decline is normal aging. A sudden cliff — full capacity halving in one week — means cell failure, possibly accelerated by heat or a bad charger.
3. Scroll to **Battery life estimates**. Windows compares observed drain against capacity to estimate runtime at full charge.
4. Take these estimates as rough: they reflect your actual recent usage pattern, which is useful, but one heavy gaming session skews them.
5. If estimates say 2 hours at full charge while capacity health is 90%, something is draining power abnormally — background apps, high screen brightness, or a runaway process.
6. Re-run the report monthly (`powercfg /batteryreport` overwrites the old file) to track whether your battery is stable or still declining.

### Fix 5: Generate an Energy Report for Drain Diagnosis

When the battery report says the hardware is fine, the energy report finds the software culprit.

1. In the same elevated prompt, run `powercfg /energy`. Wait 60 seconds while it traces system activity.
2. Open the generated `energy-report.html`. Red errors and yellow warnings list specific power problems.
3. Common findings: USB devices not suspending, high CPU utilization by a named process, display brightness maxed, or sleep states blocked by a driver.
4. Each warning names the offender — a misbehaving app, a device, or a setting. Fix what it names.
5. For sleep-specific drain, also run `powercfg /sleepstudy` (Windows 10/11 on modern standby systems) to see exactly what woke the laptop and what consumed power overnight.
6. Microsoft documents these tools further on the [Windows support site](https://support.microsoft.com/en-us/windows) if you want the full reference.

### Fix 6: Act on What the Report Tells You

A report is only useful if it changes what you do next.

1. **Healthy battery + fast drain:** attack software — background apps, startup programs, screen brightness, and power mode. The drain fixes in [battery saver setup](/articles/how-can-i-enable-battery-saver-on-laptop/) help immediately.
2. **Worn battery (70-85% health):** set a charge limit at 80% to slow further wear, calibrate the gauge, and plan for replacement in 6-12 months.
3. **Badly worn battery (under 60%):** replacement is the fix. No setting recovers lost chemical capacity.
4. **Sudden cliff in capacity history:** check for heat exposure or charger issues first, then replace — and investigate the cause so the new battery does not suffer the same fate.
5. **Overnight drain with healthy capacity:** disable fast startup, check wake timers with `powercfg /waketimers`, and update drivers. This is the classic "drains while asleep" pattern.
6. Keep a copy of today's report. In three months, generate a new one and compare — that trend line is the most honest battery health monitor you will ever get, and it is free.

## Closing

`powercfg /batteryreport` turns battery anxiety into a number. Run it, read the capacity section first, then let the usage history tell you whether you have a hardware problem or a software problem. Most battery mysteries dissolve the moment you look at real data — and now you know exactly where to look.
