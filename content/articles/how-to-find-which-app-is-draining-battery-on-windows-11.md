---
title: "How to Find Which App Is Draining Your Battery on Windows 11"
slug: how-to-find-which-app-is-draining-battery-on-windows-11
date: 2026-09-16
categories: ["battery"]
tags: ["battery", "battery drain", "windows 11"]
description: "Find exactly which app is draining your Windows 11 laptop battery using per-app battery usage stats, Task Manager, and powercfg energy reports."
thumbnail: "/images/thumbs/how-to-find-which-app-is-draining-battery-on-windows-11.webp"
faqs:
  - q: "Where do I see per-app battery usage on Windows 11?"
    a: "Open Settings with Win + I, go to System, then Power and battery, and expand Battery usage. The list shows each app's share of battery consumption over the last 24 hours or 7 days. Click any app to split its usage into active screen-on time versus background activity, which tells you whether you were using it or it was draining power behind your back."
  - q: "Why does an app I never open show high battery usage?"
    a: "Many apps run background processes for syncing, notifications, and updates even when you never open their windows. Cloud storage tools, messaging apps, and launchers are classic examples. Windows counts that background energy against the app, so a high number for an app you rarely open means its background activity needs restricting."
  - q: "Is Task Manager or Settings better for finding battery drain?"
    a: "They answer different questions. Settings and Battery usage shows historical consumption per app over hours or days, which is best for identifying the overall culprit. Task Manager shows right-now power usage, which is best for catching a process misbehaving at this moment. Use Settings to find the suspect and Task Manager to catch it in the act."
  - q: "Can a Windows system process drain the battery?"
    a: "Yes. Windows Update, search indexing, antivirus scans, and the SysMain service can all consume significant power during their runs. These usually settle on their own, but if a system process shows constant high usage for days, check for stuck updates or run the power troubleshooter. Persistent system drain after that points to a driver or update issue."
---

Guessing which app is killing your battery is a losing game. Windows 11 already keeps score: it logs exactly how much energy every app consumed, split between the time you were using it and the time it ran in the background. Most people never open this screen, so they blame the battery while a chat app quietly burns through 30 percent in the background.

This guide shows you where to find that data, how to read it, and what to do about the offenders, using only built-in Windows 11 tools.

## Why this happens

- **Background sync and notifications.** Messaging, email, and cloud apps wake the CPU and radio regularly even when idle.
- **Browsers with many tabs.** Each tab is a live process, and video or animated ads in background tabs consume real power.
- **Startup apps that never quit.** Launchers, updaters, and helpers start at boot and stay resident all day.
- **Windows maintenance tasks.** Updates, indexing, and security scans are legitimate but power-hungry while they run.
- **A misbehaving app stuck in a loop.** A crashed sync or a runaway script can pin a CPU core indefinitely, which Task Manager reveals instantly.
- **Gaming and creative apps left open.** These hold the discrete GPU awake, which dwarfs every other power draw on the system.

## How to fix it

Work through these in order, from the historical overview down to catching live offenders.

### Fix 1: Read the Battery usage screen

This is the single most informative screen for battery drain, and it takes a minute.

1. Press **Win + I** to open **Settings**, then go to **System** and **Power & battery**.
2. Click **Battery usage** to expand it.
3. Change the dropdown from **Last 24 hours** to **Last 7 days** for a more reliable picture.
4. Scan the list sorted by percentage. Anything unexpected in the top five is a suspect.
5. Click a suspect app. Windows splits its usage into **In use** and **Background**. High background usage means the app is draining power without you.
6. Note the worst two or three offenders. You will act on them in the next fixes.
7. If the list is dominated by a browser, remember that the browser total includes every tab, so check which sites you leave open. For the broader fast-drain picture beyond individual apps, see our guide on [laptop battery draining fast on Windows 11](/articles/laptop-battery-drains-fast-windows-11/).

### Fix 2: Restrict background activity for the offenders

Background usage you did not ask for is the easiest drain to eliminate.

1. In **Settings**, go to **Apps**, then **Installed apps**.
2. Find the offending app, click the three dots, and choose **Advanced options**.
3. Under **Background apps permissions**, change it from **Power optimized** to **Never**.
4. For Microsoft Store apps this works directly. For traditional desktop apps, open the app's own settings and disable options like launch at startup, background sync, and notifications.
5. Cloud storage apps deserve special attention: pause syncing while on battery, or set them to sync on a schedule instead of continuously.
6. Recheck the Battery usage screen after a day. The offender's background slice should collapse.

### Fix 3: Catch live power hogs in Task Manager

The Battery usage screen shows history. Task Manager shows what is happening right now.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. On the **Processes** tab, right-click the column headers and enable **Power usage** and **Power usage trend** if they are not shown.
3. Sort by Power usage. Anything showing **Very high** while you are doing nothing deserves investigation.
4. Switch to the **Startup apps** tab and disable anything with high startup impact that you do not need immediately at boot.
5. If a single app is stuck at Very high, end the task, then reopen the app. A one-time glitch often clears with a restart.
6. If the same app misbehaves repeatedly, check for updates or reinstall it. Persistent runaway processes sometimes need the nuclear option.

### Fix 4: Tame the browser

Browsers are the number one battery consumer on most laptops, and a few tweaks help a lot.

1. Close tabs you are not using. Each one costs memory and CPU wake-ups.
2. In your browser settings, enable the efficiency or memory saver mode. In Edge this is **Settings**, **System and performance**, **Efficiency mode**. In Chrome, look for **Memory Saver** and **Energy Saver** under Performance.
3. Disable or remove extensions you do not use. Ad blockers paradoxically save battery by blocking heavy ads.
4. Avoid leaving video or animated content playing in background tabs.
5. Consider which browser you use on battery. Edge's efficiency mode is genuinely effective on Windows 11.

### Fix 5: Generate a powercfg energy report

For drain that the app list does not explain, this report finds system-level problems.

1. Open **Windows Terminal (Admin)**.
2. Run `powercfg /energy`. Windows observes the system for 60 seconds and writes `energy-report.html`.
3. Open the report and read the **Errors** and **Warnings** sections.
4. Common findings include devices preventing sleep, USB devices not suspending, and processes making excessive timer requests.
5. Act on the specific findings: update the named driver, change the named device's power management settings in Device Manager, or disable the offending timer source.
6. This report is the closest thing to a professional power audit you can run for free.

### Fix 6: Check for Windows maintenance drain

Sometimes the culprit is Windows itself doing legitimate work at the worst time.

1. Open **Settings**, **Windows Update**, and check whether updates are downloading or pending a restart. Finish them while plugged in.
2. In Task Manager, look for **Antimalware Service Executable**, **Windows Update**, or **Search Indexer** with high usage. These should finish and settle.
3. If a system process has shown high usage for days, run the power troubleshooter: **Settings**, **System**, **Troubleshoot**, **Other troubleshooters**, **Power**, **Run**.
4. For Intel systems, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can update chipset and graphics drivers that affect idle power.

### Fix 7: Reduce the offenders' opportunity

Even well-behaved apps drain less when the system gives them less to work with.

1. Lower screen brightness. The display amplifies every app's cost because the GPU works harder at high brightness.
2. Set the power mode slider to **Best power efficiency** when on battery.
3. Turn off Bluetooth and lower the keyboard backlight when you do not need them.
4. Our guide on [turning off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) collects these tweaks in one place for 24H2.
5. After a week of these changes, compare a fresh Battery usage screen against your original notes. The difference is usually dramatic.

## Closing

Battery drain stops being a mystery the moment you look at the per-app data. Find the offenders in Battery usage, restrict their background activity, catch live hogs in Task Manager, and let the energy report find what the app list misses. Most fast-drain complaints end with a settings change, not a repair bill. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document these battery tools if you want the official reference.
