---
title: "How to Generate a Battery Report on Your Windows 11 Laptop"
slug: how-to-generate-battery-report-in-windows-11-on-laptop
date: 2026-10-03
categories: ["battery"]
tags: ["battery report", "powercfg", "windows 11"]
description: "Learn the one command that reveals your laptop battery's real health: design capacity, wear level, and usage history in under a minute."
thumbnail: "/images/thumbs/how-to-generate-battery-report-in-windows-11-on-laptop.webp"
faqs:
  - q: "Where is the battery report file saved?"
    a: "By default it saves to C:\\Windows\\System32\\battery-report.html, which is hard to open due to folder permissions. Run powercfg /batteryreport /output %USERPROFILE%\\battery-report.html instead to place it in your own user folder, then double-click it to open in your browser."
  - q: "How often should I generate a battery report?"
    a: "Once every three to six months is plenty for tracking wear. Generate a fresh one whenever runtime drops noticeably. Comparing design capacity against full charge capacity across reports shows the exact wear rate over time."
  - q: "What does cycle count mean in the battery report?"
    a: "Cycle count is the number of full discharge-charge cycles the battery has endured. One cycle equals a cumulative 100% discharge, not one unplug event. Most laptop batteries are rated for 300 to 500 cycles before capacity drops below 80% of design."
  - q: "Does the battery report work on all Windows 11 laptops?"
    a: "It works on any Windows 11 laptop with a built-in battery and ACPI battery drivers. Some 2-in-1 devices with dual batteries show combined data. If the report comes out empty, the battery drivers may be missing or the battery may not be detected."
---
Guessing about your battery's health is pointless when Windows keeps an exact ledger of it. The battery report is a built-in HTML document that records design capacity, current full-charge capacity, cycle count, and weeks of usage history — all from a single command, with no third-party software needed.

It takes about a minute to generate, and once you can read the numbers, you'll never wonder whether your battery is "going bad" again. Here's the complete walkthrough: generating it, finding the file, reading the sections that matter, and turning the numbers into a repair decision.

## Why this happens

- **Hidden battery wear:** Lithium batteries lose capacity silently with every cycle. Without a report, you only notice when runtime has already collapsed on a bad day.
- **Misleading taskbar percentage:** The percentage icon shows charge relative to the *current* capacity, not the original. A "100%" charge on a worn battery may hold half the energy it once did.
- **Disputes with support:** Repair shops and warranty desks ask for battery health numbers. The report gives you the exact figures they need, straight from the system.
- **No built-in dashboard:** Windows 11 doesn't show battery health anywhere in Settings. The command line is the only built-in path to the data.
- **Firmware quirks after updates:** Major updates sometimes change how the battery controller reports capacity. A fresh report shows you exactly what the system currently believes.
- **Calibration confusion:** After a Windows update or a deep discharge, the reported capacity can be wrong until the battery is recalibrated. The report shows you the raw numbers before you start guessing.

## How to fix it

Work through these in order — generating, finding, reading, tracking, and acting on the report.

### Fix 1: Open an admin Terminal and run the command

The report generator needs elevated privileges to read the battery telemetry.

1. Right-click the **Start** button and choose **Terminal (Admin)**.
2. Type `powercfg /batteryreport` and press **Enter**.
3. Wait for the confirmation line: `Battery life report saved to file path C:\Windows\System32\battery-report.html`.
4. Note the path — you'll move it somewhere readable in the next step.

### Fix 2: Save the report somewhere you can open

The default location is locked down by system permissions, so generate it into your own folder instead.

1. In the same admin Terminal, type `powercfg /batteryreport /output %USERPROFILE%\battery-report.html` and press **Enter**.
2. Open **File Explorer** and go to your user folder (`C:\Users\YourName`).
3. Double-click **battery-report.html**. It opens in your default browser with color-coded tables.
4. Keep this file — it becomes your baseline for comparing wear over time.

### Fix 3: Read the Installed Batteries section

This is where the truth lives. Everything else in the report is context for these two numbers.

1. Scroll to **Installed Batteries** near the top of the report.
2. Note **DESIGN CAPACITY** (what the battery held when new) and **FULL CHARGE CAPACITY** (what it holds now), both in milliwatt-hours.
3. Divide full charge capacity by design capacity. Above 0.8 (80%) is healthy; below 0.6 means replacement is worth considering.
4. Check **CYCLE COUNT**. Under 300 cycles with heavy wear suggests a defective battery rather than normal aging, and strengthens a warranty claim.

### Fix 4: Check the Battery Usage and History tables

Recent usage shows whether your real-world runtime matches the headline numbers.

1. Scroll to **Battery usage** for the last 3 days.
2. Compare the drain bars against what you were doing — steady drain with no apps running points to background processes or modern standby misbehaving.
3. Look at **Usage history**, which logs sessions back several weeks, to spot days where the battery fell far faster than usual.
4. If overnight sleep drain looks bad, our guide on [sleep-mode battery drain](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-step-by-step/) walks through the usual culprits.

### Fix 5: Archive reports to track wear over time

A single report is a snapshot; dated reports are a trend line.

1. Run `powercfg /batteryreport /output %USERPROFILE%\Documents\battery-report-Oct.html`, changing the name each time.
2. Save one report per quarter in a folder like `Documents\BatteryReports`.
3. Open any two in browser tabs to compare the capacity lines side by side.
4. A steady 2–3% loss per quarter is normal aging. A sudden 20% drop in one month points to a failing cell or firmware issue.

### Fix 6: Use the numbers to decide repair vs. replace

Numbers beat hunches when it's time to spend money.

1. If capacity is above 80% but runtime is bad, the problem is power-hungry software or settings — not the battery. Hunt down the drain first.
2. If capacity is 60–80% and the laptop is over 2 years old, that's normal wear. Try a full calibration cycle before deciding anything.
3. If capacity dropped suddenly between two reports, suspect a firmware regression or a dying cell — and check whether the battery is still under warranty.
4. For the capacity comparison explained in more detail, see [how to check design vs full charge capacity](/articles/how-to-check-battery-design-vs-full-charge-capacity-on-windows-11/).

### Fix 7: Pair it with an energy efficiency report

When runtime is bad despite a healthy capacity number, the drain is software-side.

1. In an admin Terminal, run `powercfg /energy`.
2. Wait 60 seconds while Windows observes power behavior, then open the generated `energy-report.html` from your user folder.
3. Look for red-marked errors — common ones are USB devices not suspending, misbehaving drivers, and CPU not entering low-power states.
4. For the full command reference, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents every `powercfg` switch.

## Closing

One command, one minute, and you know exactly where your battery stands. Save a report now as your baseline, check it again in three months, and you'll always be making battery decisions from facts instead of frustration, quarter after quarter.
