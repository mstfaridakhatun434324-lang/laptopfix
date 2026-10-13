---
title: "How to Check a Battery Report via Command Prompt on Windows 10"
slug: how-to-check-battery-report-via-cmd-on-windows-10
date: 2026-09-10
categories: ["battery"]
tags: ["battery report", "powercfg", "command prompt"]
description: "Windows 10 can generate a detailed HTML battery report with one command. Here's how to run it and read the capacity and usage sections."
thumbnail: "/images/thumbs/how-to-check-battery-report-via-cmd-on-windows-10.webp"
faqs:
  - q: "What command generates a battery report on Windows 10?"
    a: "Open Command Prompt or PowerShell as administrator and run powercfg /batteryreport /output C:\\battery-report.html. Windows writes an HTML file to that path. Double-click it to open the report in your browser, where you will find capacity history, recent usage, and battery drain graphs."
  - q: "How do I know if my battery is healthy from the report?"
    a: "Compare the Design Capacity with the Full Charge Capacity at the top of the report. A healthy battery holds close to its design capacity. If the full charge capacity has fallen below about 60 percent of design capacity, the battery is significantly worn and will need replacing sooner rather than later."
  - q: "Why is there no battery report option on my laptop?"
    a: "The powercfg battery report only works on systems with a battery and a compatible battery driver. On desktops without a battery, the command produces an empty or missing report. If your laptop has a battery but the report is blank, reinstall the battery driver in Device Manager and try again."
  - q: "Does the battery report show which apps drain the battery?"
    a: "Not directly. The report shows system-level drain over time, not per-app consumption. For per-app battery usage, go to Settings, then System, then Battery, and check the per-app usage list. Combine both: the report tells you when drain happened, and Settings tells you which app was responsible."
---

Windows 10 keeps a detailed diary of your battery's life — its original capacity, its current capacity, every charge cycle trend, and hour-by-hour drain history. Most people never see it because it is hidden behind a command-line tool. Generating a battery report takes about ten seconds, and reading it takes five minutes, and together they answer the question every laptop owner eventually asks: is my battery actually dying, or is something else going on?

You do not need to install anything. The `powercfg` tool is built into Windows 10, and the report it produces opens in any web browser as a clean, readable page.

## Why this happens

- **Hidden by design:** Microsoft put the richest battery data in a command-line tool instead of the Settings app, so most users never discover it.
- **Confusing capacity numbers:** Design capacity, full charge capacity, and cycle count all sound similar but measure different things.
- **Report shows a cliff:** A sudden drop in the capacity history usually lines up with a Windows update, a BIOS change, or the battery crossing a wear threshold.
- **Usage history reveals drain:** The recent-usage section exposes overnight or idle drain that points at sleep problems rather than battery wear.
- **Stale data:** If the report has not been generated in months, its history only starts from the last time the data service ran cleanly.

## How to fix it

Work through these in order — generate the report, learn to read it, and act on what it shows.

### Fix 1: Generate the battery report

One command creates the full report.

1. Press **Win + X** and choose **Windows PowerShell (Admin)** or **Command Prompt (Admin)**.
2. Type `powercfg /batteryreport /output "C:\battery-report.html"` and press Enter.
3. Wait for the confirmation message that the report was saved.
4. Open **File Explorer**, go to **C:\**, and double-click **battery-report.html** to open it in your browser.
5. Bookmark the file location — you will regenerate it later to compare after making changes.

### Fix 2: Read the capacity summary

The top section tells you the battery's health at a glance.

1. Find **Installed batteries** and note the **Design Capacity** — what the battery held when new, in milliwatt-hours.
2. Compare it with **Full Charge Capacity** — what it holds now.
3. Divide full charge by design capacity. Above 80 percent is healthy, 60 to 80 percent is aging but usable, and below 60 percent means replacement time is near.
4. Check **Cycle Count** if listed. Most laptop batteries are rated for 300 to 500 full cycles before significant wear.
5. For a deeper explainer of these two numbers, see [design capacity vs full charge capacity](/articles/best-way-to-fix-design-capacity-vs-full-charge-capacity/).

### Fix 3: Study the capacity history

The history table shows whether wear is gradual or sudden.

1. Scroll to **Battery capacity history** and read the Full Charge Capacity column from oldest to newest.
2. A slow, steady decline over months is normal chemical aging — nothing is broken.
3. A sharp drop between two adjacent entries often follows a BIOS update, a Windows feature update, or a deep discharge event.
4. If the drop lines up with an update, reinstall the battery driver (Fix 5) and regenerate the report after a full charge cycle — the "lost" capacity is sometimes just a recalibrated estimate.
5. Generate a fresh report monthly and compare; trends matter more than any single reading.

### Fix 4: Analyze recent usage and drain

The usage section catches problems the capacity numbers miss.

1. Scroll to **Battery usage** and look at the graph of the last 72 hours.
2. Steep drops while the laptop was supposedly asleep point to sleep drain, not battery wear — see [fixing overnight battery drain](/articles/best-way-to-fix-battery-drains-overnight-when-laptop-is-off/).
3. Check **Usage history** for the average drain per hour; anything far above your normal pattern deserves investigation.
4. Match drain spikes to what you were doing — video calls and gaming legitimately drain fast, while idle drain does not.
5. If drain looks normal but capacity is low, the battery is simply worn and needs replacing.

### Fix 5: Reinstall the battery driver if the report looks wrong

A corrupted driver can feed the report bad data.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Shut down, unplug, wait 30 seconds, then power back on so Windows rebuilds the driver.
4. Charge to 100 percent, then regenerate the report with the command from Fix 1.
5. Compare the new capacity numbers with the old report — corrected readings usually appear after one full cycle.

### Fix 6: Run the energy report for deeper diagnostics

When the battery report is not enough, Windows can audit live power behavior.

1. In an admin Command Prompt, run `powercfg /energy /output "C:\energy-report.html"`.
2. Let it observe the system for 60 seconds without touching the laptop.
3. Open the report and read the **Errors** and **Warnings** sections — these flag misbehaving devices and drivers that prevent sleep or waste power.
4. Address any device flagged as preventing sleep; USB devices are frequent offenders.
5. Microsoft documents these tools further on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Act on what the report tells you

Data is only useful if you use it.

1. Healthy capacity but fast drain → hunt down the draining app or process in **Settings → System → Battery**.
2. Low capacity, normal drain → the battery is worn; start shopping for a replacement matched to your exact model.
3. Sudden capacity cliff after an update → driver reinstall and recalibration first, replacement last.
4. Regenerate the report after every fix to confirm the numbers actually improved. The Windows 11 version of this process is covered in [generating a battery report in Windows 11](/articles/best-way-to-generate-battery-report-in-windows-11/).

## Closing

The battery report turns battery anxiety into numbers you can act on. Run the command, compare design capacity against full charge capacity, scan the history for cliffs, and check the usage graph for mystery drain. Five minutes of reading replaces hours of guessing — and it tells you honestly whether you need a new battery or just a settings change.
