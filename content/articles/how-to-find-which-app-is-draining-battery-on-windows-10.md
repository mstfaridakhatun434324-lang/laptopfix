---
title: "How to Find Which App Is Draining Your Battery on Windows 10"
slug: how-to-find-which-app-is-draining-battery-on-windows-10
date: 2026-09-17
categories: ["battery"]
tags: ["battery", "battery drain", "windows 10"]
description: "Find the app draining your Windows 10 laptop battery with per-app usage stats, Task Manager power columns, and background app controls."
thumbnail: "/images/thumbs/how-to-find-which-app-is-draining-battery-on-windows-10.webp"
faqs:
  - q: "Where is battery usage per app on Windows 10?"
    a: "Open Settings, go to System, then Battery, and click See which apps are affecting your battery life. The list shows each app's consumption over the last 6 hours, 24 hours, or week. It separates system, display, and app usage, so you can tell whether an app, the screen, or Windows itself is responsible for the drain."
  - q: "Why do apps use battery in the background on Windows 10?"
    a: "Windows 10 allows Store apps to run background tasks for notifications, syncing, and live tiles. Desktop programs can also keep helper processes alive after you close their windows. Both count toward battery consumption. The per-app screen shows background usage separately, which makes these silent consumers easy to spot."
  - q: "Does closing apps actually save battery on Windows 10?"
    a: "Closing the window often does not stop the app. Many programs minimize to the system tray and keep running. To actually stop the drain, quit the app from the tray icon, disable its background permission, or prevent it from starting with Windows. Task Manager confirms whether its processes are truly gone."
  - q: "Can I stop all background apps at once on Windows 10?"
    a: "Yes. In Settings, go to Privacy, then Background apps, and turn off Let apps run in the background. This is a blunt instrument that also silences notifications and live tiles, so most people prefer to leave the master switch on and disable individual apps instead. Either way, the battery savings are real."
---

Windows 10 tracks battery consumption per app just like Windows 11 does, but the screens live in different places and use slightly different names. If you are hunting a battery hog on Windows 10, this guide shows you exactly where to look: the per-app battery screen, Task Manager's power columns, background app permissions, and the classic powercfg tools that still work perfectly on Windows 10.

The approach is simple: measure first, then act. Never start disabling things at random when Windows will simply tell you the answer.

## Why this happens

- **Store apps running background tasks.** Windows 10 grants background execution to many Store apps for tiles, notifications, and syncing.
- **Desktop apps lingering in the tray.** Closing the window does not quit programs that minimize to the notification area.
- **Browsers with heavy tabs.** Video, ads, and web apps in open tabs keep the CPU and GPU busy.
- **Too many startup entries.** Every auto-starting program adds resident processes that consume power all day.
- **Windows Update and maintenance.** Update downloads, Defender scans, and indexing are periodic but power-hungry.
- **A stuck process in a loop.** One crashed helper can pin a CPU core at 100 percent indefinitely, which shows up instantly in Task Manager.

## How to fix it

Work through these in order, starting with the built-in per-app report.

### Fix 1: Open the per-app battery usage screen

Windows 10's version of this screen answers the whole question in one place.

1. Open **Settings** with **Win + I** and go to **System**, then **Battery**.
2. Click **See which apps are affecting your battery life**.
3. Set the time range dropdown to **24 hours** or **1 week** for a trustworthy picture.
4. The list shows each app's percentage of total drain. Note anything surprising near the top.
5. The screen also breaks total usage into **System**, **Display**, and **Apps**. If Display dominates, brightness is your problem, not an app.
6. Write down the top two or three unexpected apps. They are your targets for the next fixes.

### Fix 2: Disable background apps selectively

This is where Windows 10 gives you direct control over silent drain.

1. In **Settings**, go to **Privacy**, then scroll to **Background apps**.
2. Leave **Let apps run in the background** on, but toggle off individual apps you identified in Fix 1.
3. Prioritize messaging, cloud sync, news, and social apps you rarely open but which sync constantly.
4. Alternatively, return to the per-app battery screen, click an app, and uncheck **Let Windows decide** / **Allow app to run background tasks** for direct control.
5. Restart and use the laptop normally for a day, then recheck the battery screen to confirm the improvement.
6. If you prefer the nuclear option, the master toggle on the Privacy screen disables all background apps at once, at the cost of notifications and live tiles.

### Fix 3: Quit tray apps properly and trim startup

Many "closed" apps are still running, and Windows 10 makes this easy to verify.

1. Click the **Show hidden icons** arrow in the taskbar notification area. Every icon there is a running program.
2. Right-click icons for apps you do not need and choose **Quit** or **Exit**. Do not just close their windows.
3. Press **Ctrl + Shift + Esc** for **Task Manager**, then open the **Startup** tab.
4. Disable everything non-essential. Right-click an entry and choose **Disable**. When in doubt, disable it; you can still launch the app manually.
5. On the **Processes** tab, sort by CPU. A process pinned near the top while you do nothing is a live power hog worth ending and investigating.

### Fix 4: Use Task Manager's power columns

Windows 10's Task Manager can show per-process power usage, which catches what the battery screen misses.

1. In **Task Manager**, go to the **Processes** tab.
2. Right-click any column header and add **Power usage** and **Power usage trend**.
3. Sort by Power usage. Processes marked **Very high** are your live suspects.
4. Watch for a few minutes. A process that stays Very high while the system is idle is misbehaving.
5. End the task to confirm the drain stops, then decide whether to update, reconfigure, or remove the app.
6. Pay special attention after waking from sleep: a driver that fails to settle can hold power usage high until a restart.

### Fix 5: Rein in the browser

On most Windows 10 laptops the browser is the single biggest consumer, and it responds well to discipline.

1. Close tabs aggressively, especially ones playing video or running web apps.
2. Remove extensions you do not actively use. Each one is a persistent background process.
3. In Edge, enable efficiency features under **Settings**, **System**. In Chrome, check **Settings**, **Performance** for memory and energy saver options.
4. An ad blocker reduces the heavy advertising scripts that burn CPU on news and video sites.
5. If one browser consistently tops the battery list, try the other for a week on battery and compare.

### Fix 6: Run a powercfg energy report

When the app list looks innocent, this 60-second test finds system-level causes.

1. Open an elevated Command Prompt: right-click **Start**, choose **Command Prompt (Admin)** or **Windows PowerShell (Admin)**.
2. Run `powercfg /energy` and wait for the 60-second observation to finish.
3. Open the generated `energy-report.html` from the reported path.
4. Read the **Errors** section first, then **Warnings**. Typical findings: USB devices refusing to suspend, drivers blocking sleep, processes with excessive timer resolution requests.
5. Fix what it names: update the driver, adjust the device's power management in Device Manager, or uninstall the offending utility.
6. For overnight drain specifically, `powercfg /sleepstudy` reveals what kept the machine awake, a common companion problem covered in our guide on [battery draining overnight on Windows 10](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-10/). A general step-by-step drain checklist is at [fixing overnight battery drain step by step](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/).

### Fix 7: Reset expectations with a health check

If you have silenced every hog and runtime is still short, verify the battery itself.

1. In the admin terminal, run `powercfg /batteryreport` and open the HTML file.
2. Compare **FULL CHARGE CAPACITY** to **DESIGN CAPACITY**.
3. Above 80 percent with short runtime means a software hog is still hiding, so repeat Fix 1 with the 1-week view.
4. Below 60 to 70 percent means the battery is worn and no app-taming will restore the lost capacity.
5. Also confirm the power plan: **Control Panel**, **Power Options**, **Balanced**, and restore its defaults if third-party tools have mangled it.

## Closing

Windows 10 gives you every tool needed to name the app eating your battery; the per-app screen identifies it, background permissions silence it, and Task Manager catches it live. Work the list, verify with a fresh battery report, and the mystery drain usually turns out to be one chatty app you never suspected.
