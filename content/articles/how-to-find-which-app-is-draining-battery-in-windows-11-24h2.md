---
title: "How to Find Which App Is Draining Battery on Windows 11 24H2"
slug: how-to-find-which-app-is-draining-battery-in-windows-11-24h2
date: 2026-09-18
categories: ["battery"]
tags: ["battery drain", "battery usage", "background apps", "windows 11 24h2"]
description: "Battery dying too fast and you don't know why? Use Windows 11's built-in battery usage stats to catch the exact app eating your charge."
thumbnail: "/images/thumbs/how-to-find-which-app-is-draining-battery-in-windows-11-24h2.webp"
faqs:
  - q: "How do I see battery usage per app in Windows 11?"
    a: "Go to Settings > System > Power & battery and click Battery usage. The list shows each app's percentage of battery consumed over the last 24 hours or 7 days. Click any app to see whether it drained power in the foreground or in the background."
  - q: "Why does an app I never opened show high battery usage?"
    a: "It is running in the background — syncing, checking notifications, or updating. Expand the app in the battery usage list: if most of its drain is labeled background, restrict it via Settings > Apps > Installed apps > the app's Advanced options > Background apps permissions."
  - q: "Is Task Manager useful for finding battery drain?"
    a: "Somewhat. Task Manager shows current CPU, disk, and power usage trends per process, which catches apps draining power right now. But for drain over hours — especially overnight — the battery usage page and powercfg /batteryreport give the true picture."
  - q: "Can a browser really drain that much battery?"
    a: "Absolutely. Browsers with dozens of tabs, especially tabs playing video or running heavy web apps, are among the top battery consumers on most laptops. The battery usage page routinely shows browsers at the top of the list."
---
Your laptop used to last six hours. Now it barely manages three, and nothing obvious changed — no new software, no new habits. Somewhere in the background, something is eating your battery, and guessing is a waste of time. Windows 11 keeps score: every app's power consumption is logged, and the built-in tools will name the culprit in about two minutes.

This guide walks through the detective work in order — from the quick battery usage list to the deeper powercfg forensics — and then shows how to actually stop each type of offender once you've identified it.

## Why this happens

- **Background app activity:** messaging, mail, and cloud sync apps churn constantly even when you never open them.
- **Browser tab sprawl:** dozens of tabs with ads, auto-playing video, and web apps keep the CPU and network busy.
- **Windows processes:** search indexing, update downloads, and Defender scans cause temporary but heavy drain.
- **Misbehaving apps:** a stuck app can pin a CPU core at high usage indefinitely — the classic "yesterday it was fine" scenario.
- **High-performance power settings:** a laptop set to Best performance burns battery far faster than Balanced.
- **External displays and peripherals:** driving a 4K monitor or powering USB devices adds load the battery usage page doesn't attribute to any app.
- **Aging battery amplifying the effect:** as capacity shrinks, the same app drain translates into a bigger percentage drop per hour.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the battery usage list

The fastest answer Windows offers.

1. Go to **Settings > System > Power & battery** and click **Battery usage**.
2. Switch the dropdown between **Last 24 hours** and **Last 7 days** — the weekly view filters out one-off spikes.
3. Click the top few apps. The breakdown shows **In use** versus **Background** percentages, which tells you whether to close the app or restrict its background activity.
4. Write down the top three offenders before changing anything.

### Fix 2: Restrict background activity for the offenders

1. Go to **Settings > Apps > Installed apps**, click the three dots on the offending app, and open **Advanced options**.
2. Under **Background apps permissions**, change it from **Power optimized** to **Never** for apps you don't need running unseen.
3. For system apps without this option, use **Settings > System > Power & battery > Battery usage**, click the app, and adjust what controls exist there.
4. Recheck the battery usage list after a day to confirm the drain dropped.

### Fix 3: Catch live CPU hogs in Task Manager

For drain happening right now:

1. Press **Ctrl + Shift + Esc** to open **Task Manager** and go to the **Processes** tab.
2. Click the **CPU** column to sort. Anything sitting above 10–15 percent constantly while you're idle is suspicious.
3. Switch to the **Details** tab, right-click the columns, and add **Power usage** and **Power usage trend** for a direct per-process power ranking.
4. Right-click a stuck process and choose **End task** — if the same app keeps getting stuck, reinstall or replace it.

### Fix 4: Tame the browser

Browsers are the number-one surprise offender.

1. In your browser's task manager (Shift + Esc in Chrome/Edge), find which tabs or extensions use the most CPU and memory.
2. Close tabs you aren't using, or use a tab suspender extension for the tab-hoarders.
3. Turn off **Continue running background apps when the browser is closed** in the browser's system settings.
4. Disable or remove extensions you don't recognize — cryptominers and junk extensions hide here.

### Fix 5: Generate a battery report for the full picture

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`.
2. Open the HTML report and study the **Recent usage** section — it shows battery drain per hour with the system state, revealing drain during times you weren't even using the laptop.
3. The **Battery usage** graph correlates drain with activity. Steady drain while the machine should be asleep points to wake issues — see our [sleep drain guide](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-on-windows-11/).
4. Our [battery report walkthrough](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains every section.

### Fix 6: Check Windows' own background work

1. Open **Settings > Windows Update** — a stuck or repeatedly failing update can keep background services churning for days.
2. Go to **Settings > Privacy & security > Searching Windows** and check whether indexing is stuck on a large folder.
3. Open **Task Scheduler** and look for third-party tasks firing every few minutes — updaters for old software are notorious.
4. Let one-time tasks (indexing a new drive, first Defender scan) finish; only recurring mystery drain needs action.

### Fix 7: Switch to Balanced and lower the brightness

1. In **Settings > System > Power & battery**, set **Power mode** to **Balanced** or **Best power efficiency** instead of **Best performance**.
2. Drop screen brightness to 60–70 percent — the display is often the single biggest power draw, bigger than any app.
3. Turn on **Battery saver** to kick in automatically at 20 percent as a backstop.

### Fix 8: Rule out a worn battery exaggerating the drain

1. Run `powercfg /batteryreport` and compare **Full Charge Capacity** with **Design Capacity**.
2. If the battery holds half its original capacity, every app's drain looks twice as bad in percentage terms — the apps may be innocent and the battery guilty.
3. Confirm with our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) before blaming software.

## Closing

Battery drain mysteries almost always end the same way: one app, usually a browser or a background sync service, doing far more than it should. Windows 11's battery usage page names it, the per-app controls neuter it, and Task Manager catches it in the act. Two minutes of looking beats weeks of guessing — and once the offender is handled, that lost runtime comes right back.

For the overnight variant of this problem, see [disabling Fast Startup to cut idle drain](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/). Microsoft's power guidance is at [Microsoft support](https://support.microsoft.com/en-us/windows).
