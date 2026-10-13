---
title: "How to Find Which App Drains Battery on Your Laptop"
slug: how-to-find-which-app-is-draining-battery-on-laptop
date: 2026-10-06
categories: ["battery"]
tags: ["battery drain", "Task Manager", "power usage", "Windows 11"]
description: "Battery dying fast? Learn how to identify exactly which apps and background processes are eating your laptop's battery."
thumbnail: "/images/thumbs/how-to-find-which-app-is-draining-battery-on-laptop.webp"
faqs:
  - q: "How do I see which apps use the most battery in Windows 11?"
    a: "Open Settings > System > Power & battery, then expand Battery usage. Windows lists every app's battery consumption over the last 24 hours or 7 days, sorted from highest to lowest. Click any app to see whether it drained power in the background or while you were actively using it."
  - q: "Can Task Manager show power usage per app?"
    a: "Yes. Open Task Manager with Ctrl + Shift + Esc, go to the Processes tab, and look at the Power usage and Power usage trend columns. They show each running process's current and historical energy draw. Right-click the column headers and tick those boxes if they aren't visible."
  - q: "Why does an app drain battery when I'm not using it?"
    a: "Background activity is the usual culprit: syncing files, checking for updates, refreshing feeds, or keeping a live connection open. Windows 11 lets you restrict this per app under Settings > Apps > Installed apps > app > Advanced options, where you can set background activity to Never."
  - q: "Is there a command-line way to check battery drain?"
    a: "Yes. Run powercfg /batteryreport in an admin terminal to generate an HTML report of capacity and usage history, and powercfg /energy to produce a detailed energy-efficiency diagnostics report that flags processes and devices with abnormal power draw."
---

When your battery drops 30 percent in an hour and you barely did anything, something on your laptop is working harder than it should. The good news: Windows has built-in tools that name the culprit. You don't need third-party software — you just need to know where to look.

This guide shows you every reliable way to find the app or process draining your battery, and what to do once you've identified it.

## Why this happens

- **Background sync:** Cloud storage, email, and messaging apps constantly sync, upload, and check for changes even when idle.
- **Runaway processes:** A stuck updater, indexer, or crashed service can pin the CPU at high usage for hours.
- **Browser tabs:** Modern browsers with dozens of tabs — especially ones playing media or running ads — are among the top battery consumers.
- **Startup bloat:** Apps that launch at boot and sit in the system tray keep consuming power all session long.
- **Windows maintenance:** Search indexing, Windows Update, and Defender scans create temporary but heavy drain.
- **Misbehaving drivers:** A faulty driver can prevent the CPU from entering low-power states, draining the battery with no visible app to blame.

## How to fix it

Work through these in order to identify and then stop the drain.

### Fix 1: Check the Battery usage screen in Settings

1. Open **Settings > System > Power & battery**.
2. Expand the **Battery usage** section.
3. Change the dropdown to **Last 7 days** for a fuller picture.
4. Note the top three apps by percentage — these are your prime suspects.
5. Click any app to see the split between **In use** and **Background** drain. Heavy background drain means you can safely restrict it.

### Fix 2: Use Task Manager's power columns

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. Go to the **Processes** tab.
3. Right-click any column header and enable **Power usage** and **Power usage trend** if they're hidden.
4. Sort by **Power usage trend** — processes marked **Very high** over time are your drainers.
5. Right-click a suspicious non-system process and choose **End task** to test whether the drain stops. If you need to trim what's launching, see [how to turn off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/).

### Fix 3: Generate a battery report

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run `powercfg /batteryreport`.
3. Open the HTML report and scroll to **Battery usage** history — it shows drain per hour so you can match heavy-drain periods to what you were doing.
4. Check **Design Capacity** vs **Full Charge Capacity** to make sure the real problem isn't simply a worn battery. Our guide on [checking battery design vs full charge capacity](/articles/how-to-check-battery-design-vs-full-charge-capacity/) explains how to read these numbers.

### Fix 4: Run an energy efficiency diagnostic

1. In an admin terminal, run `powercfg /energy`.
2. Wait 60 seconds while Windows traces power behavior.
3. Open the generated `energy-report.html` — the **Errors** and **Warnings** sections name specific processes, devices, and settings causing abnormal drain.
4. Pay special attention to warnings about USB devices not suspending and processors not entering low-power states.

### Fix 5: Restrict background activity for the worst offenders

1. Open **Settings > Apps > Installed apps**.
2. Click the three dots next to a battery-hungry app and choose **Advanced options**.
3. Under **Background apps permissions**, set it to **Never**.
4. Repeat for other high-background-drain apps, but leave messaging and security apps you actually need notifications from.

### Fix 6: Tame your browser

1. In your browser's task manager (Shift + Esc in Chrome/Edge), sort by CPU and close heavy tabs.
2. Turn on the browser's **Memory Saver** / **Sleeping tabs** feature so idle tabs stop consuming resources.
3. Remove or disable extensions you don't use — ad-heavy and crypto-related extensions are notorious drainers.
4. If you stream video, use the installed app or Edge rather than Chrome where possible; hardware-accelerated playback uses less power.

### Fix 7: Clean up startup programs

1. Open **Task Manager > Startup apps**.
2. Disable everything you don't need immediately at boot — updaters, launchers, and chat apps are common offenders.
3. Restart and recheck battery behavior over a few hours.
4. For updaters you disabled, remember to open those apps manually once a week so they stay patched.

### Fix 8: Check the sleep study for hidden drain

Some drain happens when the lid is closed, with no app visibly running. Windows logs this too.

1. In an admin terminal, run `powercfg /sleepstudy`.
2. Open the generated HTML report and look for sessions with high **Drain Rate** while the screen was off.
3. The report names the specific processes and devices active during each sleep session — a common finding is a USB device or network adapter keeping the system in a light sleep state instead of deep sleep.
4. If a device is listed repeatedly, open **Device Manager**, find it, and on the **Power Management** tab uncheck **Allow this device to wake the computer**.

### Fix 9: Stop runaway Windows maintenance tasks

1. Open **Settings > Windows Update** and check whether an update is stuck downloading or installing — a stalled update can run the CPU for hours.
2. Open **Task Manager** and look for **Windows Modules Installer Worker**, **Search Indexer**, or **Antimalware Service Executable** using sustained high CPU.
3. Let a first-time search index finish overnight on AC power rather than fighting it on battery.
4. Run a full Microsoft Defender scan on charger power so scheduled scans don't ambush you on battery later.

## Closing

Finding a battery drainer is detective work, and Windows gives you all the tools: the Battery usage screen for the big picture, Task Manager for the live view, and the powercfg reports for hard evidence. Once you've named the culprit, restricting its background activity or removing it usually restores normal battery life the same day. If no app stands out and the drain persists, the issue may be hardware — a worn battery or a driver keeping the CPU awake — and that's the next thing to investigate.

Microsoft's official guidance on saving battery is at the [Windows battery support hub](https://support.microsoft.com/en-us/windows). If the drain happens specifically overnight, read [how to fix battery drains overnight when the laptop is off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/) next.
