---
title: "How to Generate a Battery Report in Windows 11 With Powercfg"
slug: how-to-generate-battery-report-windows-11-powercfg
date: 2026-09-01
categories: ["battery"]
tags: ["battery report", "powercfg", "windows 11"]
description: "Learn how to generate a detailed battery report in Windows 11 using the powercfg command, and how to read the results to judge your battery's real health."
thumbnail: "/images/thumbs/how-to-generate-battery-report-windows-11-powercfg.webp"
faqs:
  - q: "Where does Windows save the battery report?"
    a: "By default, powercfg /batteryreport saves battery-report.html in your user profile folder (C:\\Users\\YourName). You can specify a custom path, such as powercfg /batteryreport /output \"C:\\battery-report.html\", which is easier to find later."
  - q: "Do I need administrator rights to run powercfg /batteryreport?"
    a: "Usually not for the basic report, but running Windows Terminal or Command Prompt as administrator avoids permission issues and also unlocks the /energy variant, which requires admin rights. When in doubt, elevate first."
  - q: "How far back does the battery report history go?"
    a: "The report keeps a usage history and battery capacity history covering roughly the last three days of usage plus weekly capacity snapshots going back several months, depending on how often the laptop is used."
  - q: "Can I generate a battery report on a desktop PC?"
    a: "The command runs but the report is mostly empty on a desktop because there is no battery. It is only meaningful on laptops, tablets, and 2-in-1 devices with a real battery attached."
---
You suspect your laptop battery is dying, but the little percentage in the taskbar tells you almost nothing. It doesn't say how much capacity the battery has lost, how fast it is degrading, or whether that one bad week was a fluke or a trend. Guessing is how people end up replacing a battery that was fine.

Windows 11 already keeps all of this data. The `powercfg /batteryreport` command turns it into a clean HTML report with your design capacity, current full charge capacity, cycle count, and a day-by-day usage history. It takes about ten seconds to generate, and it is the single most useful diagnostic before you buy a new battery or send a laptop in for repair.

## Why you'd want a battery report

- **You want a number, not a feeling.** "Battery feels worse" is vague. The report shows design capacity vs. full charge capacity in mWh, so you can calculate exact wear.
- **You're deciding whether to replace the battery.** If full charge capacity is still 85% of design, the battery is probably fine and something else is draining it. If it's 55%, replacement makes sense.
- **A recent update changed battery behavior.** Comparing capacity history before and after an update shows whether Windows 11 24H2 actually reduced capacity or just changed the estimate.
- **You're buying or selling a used laptop.** The report's cycle count and capacity history are the closest thing to a battery odometer.
- **Common generation failures:** the command fails when Terminal isn't elevated, the output path has a typo, or the HTML opens blank because the browser cached a stale copy.

## How to fix it

Work through these in order. The first two get you a report; the later ones solve the problems people hit when the report misbehaves.

### Fix 1: Open Terminal as administrator

The report command usually works without admin rights, but elevating first avoids most permission errors.

1. Press **Windows key + X** and select **Terminal (Admin)**.
2. Click **Yes** on the User Account Control prompt.
3. Confirm the tab says **Administrator** in the title bar before continuing.

### Fix 2: Generate the report to an easy location

By default the report lands in your user profile folder, which is annoying to find. Point it somewhere obvious.

1. In the admin Terminal, type: `powercfg /batteryreport /output "C:\battery-report.html"` and press Enter.
2. Wait for the message **Battery life report saved to file path C:\battery-report.html**.
3. Press **Windows key + E**, navigate to **C:\**, and double-click **battery-report.html** to open it in your browser.

### Fix 3: Read the three sections that matter

The report is long, but only three sections drive decisions.

1. Scroll to **Installed batteries** and note **DESIGN CAPACITY** and **FULL CHARGE CAPACITY** — the gap between them is your wear.
2. Open **Battery capacity history** and check the trend over weeks: steady decline is aging; a sudden cliff right after an update is suspicious. If that cliff bothers you, [compare the numbers properly](/articles/how-to-check-battery-design-vs-full-charge-capacity-in-windows-11-24h2/) before doing anything drastic.
3. Check **Battery life estimates** and **Usage history** for the last few days: high active drain with the screen on usually means workload or settings, not a dead battery. If the estimate keeps shrinking, [check the battery's overall health](/articles/how-to-check-battery-health-on-windows-11-laptop/) next.

### Fix 4: Generate the energy report for drain diagnosis

The battery report shows capacity; the energy report shows what is eating power right now.

1. In the same admin Terminal, run: `powercfg /energy` — this takes about 60 seconds and you should not touch the laptop while it runs.
2. Open the resulting **energy-report.html** (saved to the current directory, usually `C:\Windows\System32`).
3. Read the **Errors** and **Warnings** sections: look for USB devices not entering suspend, high CPU utilization, and platform power management issues.

### Fix 5: Resolve "Unable to perform operation" errors

This error usually means the battery driver stack isn't responding.

1. Open **Device Manager** (press **Windows key + X**, then **Device Manager**).
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Disable device**, then **Enable device**.
3. Run `powercfg /batteryreport` again.

### Fix 6: Fix a blank or stale HTML report

Sometimes the browser shows an old cached copy or a blank page.

1. Delete the old **battery-report.html** file first, then regenerate it.
2. Open the new file in a private/incognito browser window to bypass the cache.
3. If it is still blank, regenerate without a custom path — just `powercfg /batteryreport` — and open the file from your user folder.

### Fix 7: Run it monthly as a habit

One report is a snapshot; a series is a diagnosis.

1. Save the command in a text file or a scheduled task: `powercfg /batteryreport /output "C:\battery-report-%date%.html"`.
2. Compare **FULL CHARGE CAPACITY** month to month. A drop of 1-2% per month is normal aging; faster than that deserves attention.
3. Microsoft documents the powercfg switches on the [Windows support site](https://support.microsoft.com/en-us/windows) if you want the full syntax.

### Fix 8: Automate monthly reports with Task Scheduler

One report is a snapshot; a monthly series is a health record. Automate it so you never forget.

1. Open **Task Scheduler** (search for it in the Start menu) and click **Create Basic Task** in the right pane.
2. Name it **Monthly Battery Report**, set the trigger to **Monthly**, and pick the 1st of each month.
3. For the action, choose **Start a program**, set the program to `powercfg`, and add arguments: `/batteryreport /output "C:\battery-reports\battery-report.html"`.
4. Create the **C:\battery-reports** folder first, and in the task's properties check **Run with highest privileges** so it never fails on permissions.
5. Once a quarter, open two consecutive reports side by side and compare **FULL CHARGE CAPACITY**. A steady 1-2% monthly decline is normal aging; anything faster deserves a look at your charging habits — a [charge limit](/articles/how-to-limit-battery-charge-to-80/) is the easiest way to slow it down.

## Closing

A battery report turns "my battery feels bad" into actual numbers. Generate one, read the capacity history, and you'll know within minutes whether you're dealing with a worn battery, a hungry workload, or a software problem worth fixing — and with a monthly automated report, you'll spot the next problem months before it becomes a surprise.
