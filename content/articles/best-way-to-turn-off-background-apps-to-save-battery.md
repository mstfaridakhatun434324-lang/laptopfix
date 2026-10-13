---
title: "How to Turn Off Background Apps to Save Battery on Your Laptop"
slug: best-way-to-turn-off-background-apps-to-save-battery
date: 2026-09-28
categories: ["battery"]
tags: ["background apps", "battery saver", "windows 11", "battery drain"]
description: "Stop hidden apps from eating your battery: the exact Windows settings to disable background activity, trim startup programs, and reclaim hours of runtime."
thumbnail: "/images/thumbs/best-way-to-turn-off-background-apps-to-save-battery.webp"
faqs:
  - q: "Do background apps really use much battery?"
    a: "Yes — on many laptops they are the single biggest avoidable drain. Chat clients, cloud sync tools, updaters, and launchers keep the CPU, network radio, and disk busy long after you close their windows. Disabling background permissions for apps you rarely use can add one to three hours of real runtime."
  - q: "Is it safe to turn off background permissions for every app?"
    a: "Mostly yes, but be selective. Mail, messaging, and alarm apps need background access to notify you. Games, launchers, printer utilities, and preinstalled bloatware generally do not. If an app misbehaves after you restrict it, reopen its Advanced options and set it back to Power optimized."
  - q: "What's the difference between background apps and startup apps?"
    a: "Startup apps launch when you sign in and sit in memory all session. Background apps may not be visibly running at all — Windows lets them wake periodically to sync, check for updates, or refresh content. Both drain power, and you should trim both lists."
  - q: "Will Battery Saver do this for me automatically?"
    a: "Energy saver (formerly Battery saver) throttles background activity, push notifications, and sync when it kicks in, but it doesn't permanently change per-app permissions. Use it as a safety net, and manually disable background access for the worst offenders for a lasting gain."
---

You close every program, put the laptop in your bag, and somehow the battery is still half gone a few hours later. The usual suspect is not the screen or the Wi-Fi — it is the army of apps Windows lets keep running behind your back. Chat clients syncing, cloud drives indexing, updaters phoning home, launchers sitting idle in the system tray. Each one sips a little power, and together they can drain more than an hour of video playback does.

The good news is that Windows gives you real control over this. You don't need a third-party "optimizer" — just the built-in permissions, startup manager, and a bit of discipline about what you install. This guide walks through the exact settings, in the order a technician would check them.

## Why this happens

- **Background permissions are on by default.** Most apps you install from the Microsoft Store get permission to run in the background the moment they're installed, so they keep syncing and refreshing even when never opened.
- **Startup programs pile up silently.** Every installer loves adding itself to startup: updaters, helpers, launchers, "quick start" utilities. After a year, twenty programs can be loading at every sign-in.
- **Closed doesn't mean stopped.** Desktop apps like Discord, Slack, Steam, and OneDrive minimize to the system tray instead of exiting. From Windows' perspective they're still running and still drawing power.
- **Notifications wake apps constantly.** Each notification can wake an app's background task, spin up the network radio, and light up the CPU — multiply that by dozens of apps and the drain adds up fast.
- **Cloud sync never sleeps.** OneDrive, Dropbox, and Google Drive index files, upload changes, and resolve conflicts in the background. On a big folder, that's sustained disk and CPU activity.
- **Some apps are just badly behaved.** Poorly coded background tasks can pin a CPU core at high usage indefinitely. [A fast-draining battery](/articles/laptop-battery-drains-fast-windows-11/) is often one rogue process, not a dying battery.

## How to fix it

Work through these in order. Each step builds on the last, and most people see a measurable improvement after the first three.

### Fix 1: Disable background permissions per app

Windows 11 lets you cut off background activity app by app. This is the highest-impact single change.

1. Open **Settings** and go to **Apps** > **Installed apps**.
2. Find an app you rarely need live updates from (a game launcher, a printer utility, a shopping app). Click the **three dots** next to it and choose **Advanced options**.
3. Under **Background apps permissions**, change the dropdown from **Power optimized** to **Never**.
4. Repeat for every app that doesn't need to notify or sync you. Be conservative with mail, messaging, calendar, and alarm apps.
5. Restart the laptop so the changes take full effect.

### Fix 2: Trim your startup list

Fewer programs at sign-in means less memory pressure, less CPU churn, and a faster boot.

1. Open **Settings** > **Apps** > **Startup**.
2. Sort by **Status** and look at everything marked **On**.
3. Toggle **Off** anything you don't need within seconds of signing in: updaters, game launchers, chat clients, "helper" utilities.
4. Alternatively, open **Task Manager** (Ctrl + Shift + Esc), go to the **Startup apps** tab, and check the **Startup impact** column — disable the **High** impact entries first.
5. Restart and time your boot. It should be noticeably quicker.

### Fix 3: Turn on Energy saver

Energy saver (the renamed Battery saver) is Windows' built-in throttle for background activity. Let it do its job automatically.

1. Go to **Settings** > **System** > **Power & battery**.
2. Expand **Energy saver** and set **Turn on energy saver automatically** to **Always** or **At 40% battery** depending on how aggressive you want to be.
3. Toggle **Lower screen brightness when using energy saver** on as well — the display is the other big drain.
4. Note that energy saver reduces background sync, mail fetch, and some visual effects. If you need full performance for a task, you can toggle it off temporarily from Quick Settings (Win + A).

### Fix 4: Hunt down tray squatters

Many desktop apps hide in the notification area instead of closing.

1. Click the **up arrow** in the taskbar's notification area to reveal hidden icons.
2. Right-click each one you don't actively use and choose **Quit** or **Exit**.
3. For the ones that keep coming back, open the app's own settings and look for **Run at startup**, **Start minimized**, or **Close to tray** — disable those.
4. In **Task Manager** > **Processes**, sort by **CPU** and watch for a few minutes. Any non-system process holding sustained CPU while idle is a prime candidate to restrict or uninstall.

### Fix 5: Pause or limit cloud sync

Sync clients are some of the heaviest background consumers, especially right after boot when they scan everything.

1. Click the **OneDrive** cloud icon in the taskbar, open **Settings**, and under **Sync and backup** consider pausing sync with **Pause syncing** when you're on battery and need maximum runtime.
2. Use **Choose folders** to sync only what you actually need on the laptop — fewer files means less indexing.
3. If you run Dropbox or Google Drive too, pick one primary client. Running two or three sync engines simultaneously is pure waste.
4. For our deeper walkthrough of Windows 11's specific toggles, see [how to turn off background apps in Windows 11](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/).

### Fix 6: Silence notification-hungry apps

Every buzz costs power. Cutting notification privileges reduces how often apps wake.

1. Go to **Settings** > **System** > **Notifications**.
2. Scroll to the per-app list and turn off notifications for apps whose alerts you ignore anyway.
3. Turn on **Do not disturb** automatically during your typical unplugged hours via **Set priority notifications** schedules.
4. This won't show up as one big number anywhere, but fewer wake-ups means the CPU spends more time in its deep low-power states.

### Fix 7: Uninstall what you never use

The bluntest tool is also the most effective. Preinstalled trials, expired antivirus, manufacturer "utilities" you opened once — they all ship with background services.

1. Open **Settings** > **Apps** > **Installed apps** and sort by **Size** or skim the full list honestly.
2. Uninstall anything you haven't opened in months. Use the app's own uninstaller via the three-dot menu.
3. After uninstalling, check **Task Manager** > **Services** for leftover services from removed software, and disable them via **services.msc** if you're confident they're orphans.
4. If [your battery still discharges quickly](/articles/how-to-fix-battery-discharges-quickly-on-laptop-in-windows-11-24h2/) after this cleanup, the drain is likely hardware-level (aging cells) rather than software.

Microsoft documents the background-app permission model in the official [Windows support pages](https://support.microsoft.com/en-us/windows) if you want the full reference for your Windows version.

## Closing

Background apps are death by a thousand cuts — no single one ruins your battery, but thirty of them together absolutely do. Work the list once: kill background permissions, trim startup, let Energy saver run, and evict the tray squatters. Check **Settings** > **System** > **Power & battery** > **Battery usage** afterward to confirm the worst offenders dropped off the chart. Do this cleanup twice a year and your battery will thank you with real, measurable extra hours.
